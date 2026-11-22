#!/usr/bin/env python3
"""11-22 — deep probe of the NEW candidates that will get fresh profiles.
For each: repo metadata, tree composition, README head, tag/release four-tuple,
asset inventory + download distribution, workflows, issues, contributors, and
tag->commit diff closure sample.
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

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
    "Tracer-Cloud/opensre",
    "mjmirza/app-store-compliance",
    "pookjw/HermesEnabler",
    "we-promise/sure",
    "zhouxiaoka/autoclip",
    "XiaoYouChR/Ghost-Downloader-3",
]

for full in TARGETS:
    print("=" * 110)
    print(full)
    print("=" * 110)
    m = api(f"repos/{full}") or {}
    lic = m.get("license") or {}
    own = m.get("owner") or {}
    om = api(f"users/{own.get('login')}") or {}
    print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
          f"subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} "
          f"watchers={m.get('watchers_count')} size_kb={m.get('size')}")
    print(f"  lang={m.get('language')} license={lic.get('spdx_id')} created={m.get('created_at')} "
          f"pushed={m.get('pushed_at')} default_branch={m.get('default_branch')}")
    print(f"  homepage={m.get('homepage')} topics={m.get('topics')} fork={m.get('fork')} "
          f"archived={m.get('archived')}")
    print(f"  owner: {own.get('login')} type={own.get('type')} created={om.get('created_at')} "
          f"followers={om.get('followers')} public_repos={om.get('public_repos')}")
    print(f"  desc: {m.get('description')}")

    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    exts = Counter(os.path.splitext(b.get("path", ""))[1].lower() or "<none>" for b in blobs)
    print(f"  blobs={len(blobs)} truncated={tree.get('truncated')} exts={dict(exts.most_common(10))}")
    tops = Counter(b.get("path", "").split("/")[0] for b in blobs)
    print(f"  top dirs: {dict(tops.most_common(12))}")

    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    print(f"  README len={len(rm)}")
    print("  README head:")
    for ln in rm.splitlines()[:34]:
        print("    | " + ln[:140])

    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rels = rels if isinstance(rels, list) else []
    print(f"  tags={len(tags)} names={[t.get('name') for t in tags[:8]]} "
          f"distinct_shas={len({t.get('commit',{}).get('sha') for t in tags})}")
    print(f"  releases={len(rels)}")
    for r in rels[:4]:
        assets = r.get("assets") or []
        dl = sorted(a.get("download_count") or 0 for a in assets)
        print(f"    {str(r.get('tag_name')):14s} pub={str(r.get('published_at'))[:19]} "
              f"pre={r.get('prerelease')} assets={len(assets):3d} "
              f"dl_min={dl[0] if dl else '-'} dl_max={dl[-1] if dl else '-'} "
              f"dl_sum={sum(dl)} body_len={len(r.get('body') or '')}")
        if assets:
            names = [a.get("name") for a in assets]
            ext = Counter(os.path.splitext(n or "")[1].lower() or "<none>" for n in names)
            print(f"        asset ext mix: {dict(ext.most_common(8))}")
            print(f"        sample names: {names[:6]}")
            print(f"        full dl sorted: {dl}")

    wf = api(f"repos/{full}/contents/.github/workflows") or []
    print(f"  workflows: {[w.get('name') for w in wf] if isinstance(wf, list) else wf}")

    cs = api(f"repos/{full}/commits", {"per_page": 100}) or []
    cs = cs if isinstance(cs, list) else []
    print(f"  commits_fetched={len(cs)}")
    for c in cs[:8]:
        print(f"    {c.get('sha','')[:8]} {(c.get('commit',{}).get('author',{}) or {}).get('date')} "
              f"{(c.get('commit',{}).get('message') or '').split(chr(10))[0][:88]}")

    ct = api(f"repos/{full}/contributors", {"per_page": 12}) or []
    if isinstance(ct, list) and ct:
        print(f"  contributors: {[(c.get('login'), c.get('contributions')) for c in ct[:10]]}")

    iss = api(f"repos/{full}/issues", {"state": "open", "per_page": 20}) or []
    iss = iss if isinstance(iss, list) else []
    print(f"  open issues (first 20) total_shown={len(iss)}")
    for i in iss[:10]:
        print(f"    #{i.get('number')} [{i.get('user',{}).get('login')}] "
              f"{str(i.get('title'))[:88]} (comments={i.get('comments')})")
    print()
