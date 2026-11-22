#!/usr/bin/env python3
"""Deep-dive on the 11-22 caliber finding: 'replication' actually mixes
byte-identical CI-generated copies with per-harness DIVERGENT adaptations.

For each skill repo, classify every skill NAME that appears in >1 directory:
  * identical  -> all copies share one blob sha  (true duplication / CI mirror)
  * divergent  -> copies have different blob shas (per-harness adaptation)

Then measure, per repo:
  - how many files are in identical groups vs divergent groups
  - the size delta between divergent copies (how much was adapted)
  - whether a CI workflow/script plausibly generates the identical set

Output: /tmp/deep_1122.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/deep_1122.json"


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


TARGETS = [
    "backnotprop/plannotator",
    "cursor/plugins",
    "tradermonty/claude-trading-skills",
    "alibaba/open-code-review",
    "HKUDS/CLI-Anything",
]


def deep(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per_name = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        parent = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per_name[parent].append(b)

    groups = []
    for name, lst in per_name.items():
        if len(lst) < 2:
            continue
        shas = {x.get("sha") for x in lst}
        sizes = [x.get("size") or 0 for x in lst]
        groups.append({
            "name": name,
            "copies": len(lst),
            "distinct_sha": len(shas),
            "kind": "identical" if len(shas) == 1 else "divergent",
            "paths": sorted(x.get("path") for x in lst),
            "sizes": sizes,
            "size_delta": max(sizes) - min(sizes),
        })

    ident = [g for g in groups if g["kind"] == "identical"]
    div = [g for g in groups if g["kind"] == "divergent"]
    ident_files = sum(g["copies"] for g in ident)
    div_files = sum(g["copies"] for g in div)

    # total distinct content = identical groups contribute 1 blob each,
    # divergent groups contribute distinct_sha blobs
    distinct_content = (len(ident) + sum(g["distinct_sha"] for g in div)
                         + len([n for n, l in per_name.items() if len(l) == 1]))

    # search tree for generator scripts that mention the skill dirs
    gen_hits = []
    for b in blobs:
        p = b.get("path") or ""
        if re.search(r"(sync|generate|gen|mirror|propagat|distribut|copy)"
                     r"[-_]?(skill|plugin|harness|marketplace)", p, re.I):
            gen_hits.append(p)
    # also look for common generator filenames
    gen_hits += [b.get("path") for b in blobs
                 if re.search(r"(^|/)(sync|generate|copy|mirror)[^/]*\.(py|ts|js|sh|yml|yaml)$",
                              b.get("path") or "", re.I)]

    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "open_issues": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "n_blobs": len(blobs),
        "n_skill_files": len(skills),
        "n_name_ident": len(per_name),
        "n_distinct_content": distinct_content,
        "repl_by_content": round(len(skills) / distinct_content, 2) if distinct_content else 0,
        "n_identical_groups": len(ident),
        "n_divergent_groups": len(div),
        "identical_files": ident_files,
        "divergent_files": div_files,
        "identical_pct": round(100.0 * ident_files / len(skills), 1) if skills else 0,
        "divergent_pct": round(100.0 * div_files / len(skills), 1) if skills else 0,
        "groups": sorted(groups, key=lambda g: (g["kind"], -g["copies"])),
        "generator_candidates": sorted(set(gen_hits))[:25],
    }


def main():
    out = []
    for t in TARGETS:
        r = deep(t)
        out.append(r)
        print(f"== {t}: files={r['n_skill_files']} name_ident={r['n_name_ident']} "
              f"distinct_content={r['n_distinct_content']} repl_content={r['repl_by_content']}")
        print(f"   identical groups={r['n_identical_groups']} ({r['identical_files']} files, "
              f"{r['identical_pct']}%) | divergent groups={r['n_divergent_groups']} "
              f"({r['divergent_files']} files, {r['divergent_pct']}%)")
        print(f"   generator candidates: {r['generator_candidates']}")
        for g in r["groups"][:8]:
            print(f"     [{g['kind']:9s}] {g['name']:32s} x{g['copies']} "
                  f"sha_variants={g['distinct_sha']} size_delta={g['size_delta']}")
            if g["kind"] == "divergent":
                for pp in g["paths"][:6]:
                    print(f"          {pp}")
        print(flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {len(out)} -> {OUT}")


if __name__ == "__main__":
    main()
