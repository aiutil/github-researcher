#!/usr/bin/env python3
"""CALIBER AUDIT for the SKILL.md "replication factor" metric.

The 11-18 daily report's headline claim was:
    "SKILL.md 数量是复制放大的计数" with ECC = 1087 files / 330 identities
    (3.30x), plannotator = 23/11 (2.09x), cursor/plugins = 173/113 (1.53x).

Those numbers came from scripts/_identity_2026_11_18.py, where an "identity"
is the PARENT-DIRECTORY NAME of a SKILL.md.

The daily probe (scripts/_probe_1119.py .. _probe_1123.py) instead counts
an identity as a distinct (parent-dir -> blob-sha-set) mapping, i.e. two
directories count as ONE identity only if their file CONTENT is byte-identical.

So the two calibers can disagree, and the direction of disagreement is
informative: if content-caliber yields MORE identities than name-caliber,
then same-named skills in different directories are NOT byte-identical copies.

This script measures BOTH calibers on the same tree, same moment, so the
comparison is apples-to-apples.
"""
import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
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
        return None, None
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:  # noqa: BLE001
        return None, None


REPOS = [
    "affaan-m/ECC",
    "backnotprop/plannotator",
    "cursor/plugins",
    "tradermonty/claude-trading-skills",
    "elementalsouls/Claude-BugHunter",
    "obra/superpowers",
    "google-labs-code/stitch-skills",
    "alibaba/open-code-review",
    "mvanhorn/last30days-skill",
    "HKUDS/CLI-Anything",
    "GoogleChrome/modern-web-guidance-src",
    "kajisho5/ffmpeg-skill",
    "ag-ui-protocol/ag-ui",
    "ChromeDevTools/chrome-devtools-mcp",
]


def measure(full):
    m, _ = api(f"repos/{full}")
    m = m or {}
    branch = m.get("default_branch") or "main"
    tree, _ = api(f"repos/{full}/git/trees/{branch}?recursive=1")
    tree = tree or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]

    # CALIBER A (11-18): identity = parent directory NAME
    by_name = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        parent = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        by_name[parent].append((p, b.get("sha"), b.get("size")))

    # CALIBER B (11-19..11-23): identity = distinct (parent-dir -> sha-set)
    by_dir_shas = defaultdict(set)
    for b in skills:
        p = b.get("path") or ""
        parent = p.rsplit("/", 1)[0] if "/" in p else "<root>"
        by_dir_shas[parent].add(b.get("sha"))
    content_idents = {frozenset(v) for v in by_dir_shas.values()}

    # CALIBER C: content identity by blob sha (dedupe identical files globally)
    sha_counter = Counter(b.get("sha") for b in skills)
    n_distinct_shas = len(sha_counter)

    # Which same-NAMED skills differ in content across their directories?
    named_divergent = {}
    for name, lst in by_name.items():
        if len(lst) > 1:
            shas = {x[1] for x in lst}
            if len(shas) > 1:
                named_divergent[name] = {
                    "copies": len(lst),
                    "distinct_shas": len(shas),
                    "paths": [x[0] for x in lst][:6],
                }

    # how many copies of the largest replicated names share byte-identical content
    identical_named = sum(1 for name, lst in by_name.items()
                           if len(lst) > 1 and len({x[1] for x in lst}) == 1)

    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "n_blobs": len(blobs),
        "n_skill_files": len(skills),
        "name_idents": len(by_name),
        "content_idents": len(content_idents),
        "distinct_shas": n_distinct_shas,
        "named_replicated": sum(1 for lst in by_name.values() if len(lst) > 1),
        "named_identical": identical_named,
        "named_divergent": named_divergent,
        "repl_name": round(len(skills) / len(by_name), 2) if by_name else 0,
        "repl_content": round(len(skills) / len(content_idents), 2) if content_idents else 0,
        "repl_sha": round(len(skills) / n_distinct_shas, 2) if n_distinct_shas else 0,
    }


out = []
for i, r in enumerate(REPOS, 1):
    res = measure(r)
    out.append(res)
    print(f"[{i}/{len(REPOS)}] {res['repo']:40s} files={res['n_skill_files']:5d} "
          f"name={res['name_idents']:5d}({res['repl_name']:5.2f}x) "
          f"content={res['content_idents']:5d}({res['repl_content']:5.2f}x) "
          f"sha={res['distinct_shas']:5d}({res['repl_sha']:5.2f}x) "
          f"repNamed={res['named_replicated']:4d} "
          f"identical={res['named_identical']:4d} "
          f"divergent={len(res['named_divergent']):4d}", flush=True)

json.dump(out, open("/tmp/caliber_1123.json", "w"), ensure_ascii=False, indent=1)

print()
print("=" * 110)
print("CALIBER COMPARISON — 11-18 published numbers vs 11-23 dual-caliber measurement")
print("=" * 110)
PUB_1118 = {
    "affaan-m/ECC": (1087, 330),
    "backnotprop/plannotator": (23, 11),
    "cursor/plugins": (173, 113),
    "tradermonty/claude-trading-skills": (94, 74),
    "elementalsouls/Claude-BugHunter": (83, 83),
    "obra/superpowers": (15, 15),
    "google-labs-code/stitch-skills": (16, 16),
    "alibaba/open-code-review": (4, 4),
    "mvanhorn/last30days-skill": (1, 1),
}
print(f"{'repo':38s} {'11-18 pub':>11s} {'name-caliber':>13s} {'content-caliber':>15s} {'agree?':>8s}")
for res in out:
    fn = res["repo"]
    pub = PUB_1118.get(fn)
    pubstr = f"{pub[0]}/{pub[1]}" if pub else "-"
    agree = ""
    if pub:
        agree = "same" if pub[1] == res["name_idents"] else "DIFF"
        if pub[1] == res["content_idents"]:
            agree = "same(content)"
    print(f"{fn:38s} {pubstr:>11s} {res['name_idents']:6d} ({res['repl_name']:4.2f}x) "
          f"{res['content_idents']:8d} ({res['repl_content']:4.2f}x) {agree:>8s}")

print()
print("=" * 110)
print("SAME-NAMED SKILLS WHOSE COPIES DIFFER IN CONTENT (name-caliber says 'replica', content says 'not a replica')")
print("=" * 110)
for res in out:
    if not res["named_divergent"]:
        continue
    print(f"\n{res['repo']}  ({res['named_replicated']} replicated names, "
          f"{res['named_identical']} byte-identical, {len(res['named_divergent'])} divergent)")
    for name, d in sorted(res["named_divergent"].items(),
                          key=lambda kv: -kv[1]["copies"])[:6]:
        print(f"   {name:36s} {d['copies']:3d} copies / {d['distinct_shas']:3d} distinct shas")
        for pth in d["paths"][:3]:
            print(f"        {pth}")
