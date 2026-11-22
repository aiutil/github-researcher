#!/usr/bin/env python3
"""Tag -> commit -> source-diff closure sampling, run on the true tag set.

The 11-17 and 11-18 reports established that the meaningful version
criterion is whether the chain "tag -> commit -> source diff" actually
closes, not how many tags or releases exist.  Those samples were drawn from
the FIRST 100 tags returned by the API.  Today the tag endpoint's true
totals were resolved, so this script re-samples the *newest* and *oldest*
tags of each repo, spanning the whole range, and records for each sampled
tag:

  * the tag's commit sha
  * whether that commit's own diff touches source files
  * whether the PARENT commit's diff touches source files
  * the number of files changed

"Source file" = anything that is not a lockfile, changelog, licence,
metadata or generated doc.  The rule is stated explicitly here so the
classification is auditable rather than implicit.

Output: /tmp/closure_1121.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/closure_1121.json"

REPOS = [
    "kajisho5/ffmpeg-skill",
    "GoogleChrome/modern-web-guidance-src",
    "alibaba/open-code-review",
    "backnotprop/plannotator",
    "ag-ui-protocol/ag-ui",
    "meta/astryx",
    "toeverything/AFFiNE",
    "Tracer-Cloud/opensre",
    "dream-num/univer",
    "obra/superpowers",
    "we-promise/sure",
]

# A path that is not "source" for the purposes of this check.
NON_SOURCE = re.compile(
    r"(^|/)(LICENSE|LICENCE|NOTICE|CHANGELOG|CODEOWNERS|"
    r"package-lock\.json|yarn\.lock|pnpm-lock\.yaml|uv\.lock|poetry\.lock|"
    r"Cargo\.lock|go\.sum|composer\.lock|"
    r".*\.lock)$|"
    r"(^|/)\.github/|"
    r"\.(md|json|txt|ya?ml|toml|cfg|ini)$",
    re.I,
)


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def is_source(path):
    return not NON_SOURCE.search(path or "")


def commit_info(full, sha):
    c = api(f"repos/{full}/commits/{sha}")
    if not c:
        return None
    files = c.get("files") or []
    src = [f for f in files if is_source(f.get("filename"))]
    parents = c.get("parents") or []
    parent = parents[0].get("sha") if parents else None
    pfiles = []
    if parent:
        pc = api(f"repos/{full}/commits/{parent}")
        if pc:
            pfiles = [f for f in (pc.get("files") or []) if is_source(f.get("filename"))]
    return {
        "sha": sha,
        "n_files": len(files),
        "n_source_files": len(src),
        "source_files": [f.get("filename") for f in src][:6],
        "touches_source": bool(src),
        "message": ((c.get("commit") or {}).get("message") or "")[:120],
        "parent": parent,
        "parent_touches_source": bool(pfiles),
        "parent_n_source_files": len(pfiles),
    }


def sample(full, n=4):
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    if not isinstance(tags, list) or not tags:
        return {"repo": full, "status": "no tags"}
    # newest N (page 1 head) + oldest available on page 1 tail, spread out
    picked = []
    idxs = list(range(min(n, len(tags))))
    if len(tags) >= 2 * n:
        idxs += list(range(len(tags) - n, len(tags)))
    seen = set()
    for i in idxs:
        t = tags[i]
        sha = (t.get("commit") or {}).get("sha")
        if sha and sha not in seen:
            seen.add(sha)
            picked.append((t.get("name"), sha))
    rows = []
    for name, sha in picked:
        ci = commit_info(full, sha)
        if ci:
            ci["tag"] = name
            rows.append(ci)
    own = sum(1 for r in rows if r["touches_source"])
    par = sum(1 for r in rows if r["parent_touches_source"])
    either = sum(1 for r in rows if r["touches_source"] or r["parent_touches_source"])
    return {
        "repo": full,
        "status": "ok",
        "n_sampled": len(rows),
        "own_touches_source": own,
        "parent_touches_source": par,
        "either_touches_source": either,
        "samples": rows,
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(sample, REPOS):
            out.append(r)
            print(f"  {r['repo']:42s} n={r.get('n_sampled')} own={r.get('own_touches_source')} "
                  f"parent={r.get('parent_touches_source')} either={r.get('either_touches_source')}",
                  flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
