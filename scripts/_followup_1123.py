#!/usr/bin/env python3
"""Follow-up forensics for 2026-11-23.

A. The download-count correction, applied consistently: compare every repo
   under (a) the 11-18 truncated view  sorted(dl)[:12]  and (b) the full
   view  min(dl)..max(dl).  This quantifies how much of yesterday's
   "adoption differs by 1-2 orders of magnitude" claim was a measurement
   artifact.

B. Remaining facts for the projects to be profiled today.
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter
from datetime import datetime, timezone

ENV = dict(os.environ, HOME="/home/lohasle")


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
        return None, None
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:  # noqa: BLE001
        return None, None


REPOS = ["backnotprop/plannotator", "alibaba/open-code-review",
         "zhouxiaoka/autoclip", "XiaoYouChR/Ghost-Downloader-3",
         "nginx/nginx", "pookjw/HermesEnabler", "we-promise/sure",
         "getarcaneapp/arcane", "GoogleChrome/modern-web-guidance-src"]

print("=" * 112)
print("A. DOWNLOAD COUNT — 11-18 truncated view vs full view, same moment, same releases")
print("=" * 112)
print(f"{'repo':42s} {'tag':>18s} {'n_assets':>8s} {'11-18 view[:12]':>20s} "
      f"{'TRUE min':>9s} {'TRUE max':>9s} {'understated?':>12s}")
for fn in REPOS:
    rels = api(f"repos/{fn}/releases", {"per_page": 5})
    if not isinstance(rels, list):
        continue
    for rel in rels[:3]:
        assets = rel.get("assets") or []
        if not assets:
            continue
        dl = sorted((a.get("download_count") or 0) for a in assets)
        head12 = dl[:12]
        ratio = (dl[-1] / head12[-1]) if head12[-1] else float("inf")
        print(f"{fn:42s} {str(rel.get('tag_name')):>18s} {len(dl):8d} "
              f"{str(head12[0]) + '-' + str(head12[-1]):>20s} {dl[0]:9d} {dl[-1]:9d} "
              f"{ratio:11.1f}x")

print()
print("=" * 112)
print("B. FACT COLLECTION FOR TODAY'S PROFILES")
print("=" * 112)
TARGETS = ["nginx/nginx", "pookjw/HermesEnabler", "HKUDS/CLI-Anything",
           "jingyaogong/minimind", "Tracer-Cloud/opensre",
           "zhouxiaoka/autoclip", "XiaoYouChR/Ghost-Downloader-3"]
for fn in TARGETS:
    m, _ = api(f"repos/{fn}")
    m = m or {}
    print(f"\n================ {fn} ================")
    print(f"  desc     : {m.get('description')}")
    print(f"  homepage : {m.get('homepage')}")
    print(f"  topics   : {m.get('topics')}")
    print(f"  created  : {m.get('created_at')}  pushed: {m.get('pushed_at')}")
    print(f"  license  : {(m.get('license') or {}).get('spdx_id')}  "
          f"lang: {m.get('language')}  size_kb: {m.get('size')}")
    print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
          f"subs={m.get('subscribers_count')} watchers={m.get('watchers_count')} "
          f"oi={m.get('open_issues_count')} branch={m.get('default_branch')}")
    print(f"  archived={m.get('archived')} fork={m.get('fork')} "
          f"issues={m.get('has_issues')} disc={m.get('has_discussions')} "
          f"is_template={m.get('is_template')}")
    wf, _ = api(f"repos/{fn}/contents/.github/workflows")
    wfn = [w.get("name") for w in wf] if isinstance(wf, list) else []
    print(f"  workflows ({len(wfn)}): {wfn}")
    contrib, _ = api(f"repos/{fn}/contributors", {"per_page": 8})
    if isinstance(contrib, list) and contrib:
        print("  contributors: " + " · ".join(
            f"{c.get('login')}({c.get('contributions')})" for c in contrib))
    tree, _ = api(f"repos/{fn}/git/trees/{m.get('default_branch') or 'main'}?recursive=1")
    blobs = [b for b in ((tree or {}).get("tree") or []) if b.get("type") == "blob"]
    top = Counter()
    for b in blobs:
        top[(b.get("path") or "").split("/")[0]] += 1
    print(f"  blobs={len(blobs)} truncated={((tree or {}).get('truncated'))} "
          f"topdirs={dict(top.most_common(14))}")
    ext = Counter(os.path.splitext(b.get("path") or "")[1].lower() or "<none>" for b in blobs)
    print(f"  exts={dict(ext.most_common(10))}")
    rm, _ = api(f"repos/{fn}/readme", raw=True,
                headers=["Accept: application/vnd.github.raw"])
    rm = rm or ""
    print(f"  readme_len={len(rm)}")
    print("  README head:\n" + "\n".join("      " + l for l in rm.split("\n")[:38]))
    issues, _ = api(f"repos/{fn}/issues", {"state": "open", "per_page": 8})
    if isinstance(issues, list) and issues:
        print("  open issues:")
        for i in issues[:6]:
            print(f"     #{i.get('number')} [{i.get('user',{}).get('login')}] "
                  f"c={i.get('comments')} {str(i.get('title'))[:82]}")
