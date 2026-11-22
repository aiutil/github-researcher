#!/usr/bin/env python3
"""Deep forensics for the 2026-11-23 daily report.

Q1. subs/star ratio across the 6-day series (watchers vs starrers).
Q2. Asset download trajectories for the repos whose 11-18 report said
    "downloads too low to judge adoption".
Q3. Deep profile of the four new key projects (minimind / opensre /
    autoclip / Ghost-Downloader-3).
Q4. Are the "replicated" skill copies CI-generated, or hand-made?
Q5. Trending-list churn: what entered / left between 11-18 and 11-23.
"""
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
DAYS = ["1118", "1119", "1120", "1121", "1122", "1123"]
DATES = ["2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21",
         "2026-11-22", "2026-11-23"]


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


SNAPS = {}
for d in DAYS:
    try:
        SNAPS[d] = {p["full_name"]: p for p in json.load(open(f"/tmp/probe_{d}.json"))}
    except FileNotFoundError:
        SNAPS[d] = {}
P = json.load(open("/tmp/probe_1123.json"))
by = {p["full_name"]: p for p in P}

print("=" * 108)
print("Q1. SUBSCRIBERS vs STARS — who is 'watching' rather than 'starring'?")
print("=" * 108)
print(f"{'repo':42s} {'stars':>9s} {'subs':>6s} {'subs/star':>10s} {'forks':>6s} {'oi':>5s}")
for p in sorted(P, key=lambda x: -(x["subs"] / max(x["stars"], 1))):
    r = p["subs"] / max(p["stars"], 1) * 100
    print(f"{p['full_name']:42s} {p['stars']:9,d} {p['subs']:6d} {r:9.2f}% {p['forks']:6,d} {p['open_issues']:5d}")
print()
rates = [p["subs"] / max(p["stars"], 1) * 100 for p in P]
rates.sort()
print(f"cohort subs/star: min={rates[0]:.2f}%  median={rates[len(rates)//2]:.2f}%  max={rates[-1]:.2f}%")

print()
print("=" * 108)
print("Q2. ASSET DOWNLOAD TRAJECTORY (11-18 recorded vs 11-23 live)")
print("=" * 108)
for fn in ["backnotprop/plannotator", "alibaba/open-code-review", "zhouxiaoka/autoclip",
           "XiaoYouChR/Ghost-Downloader-3", "nginx/nginx", "pookjw/HermesEnabler",
           "we-promise/sure", "GoogleChrome/modern-web-guidance-src"]:
    p = by.get(fn)
    if not p:
        continue
    ra = p["rel_assets"]
    print(f"\n{fn}   tags={p['n_tags']} rel={p['n_releases']}")
    print(f"   {'tag':>16s} {'assets':>7s} {'total_dl':>10s} {'max_asset_dl':>13s}  prerel  asset sample")
    for r in ra:
        names = [str(x)[:34] for x in (r.get("asset_names") or [])[:3]]
        print(f"   {str(r['tag']):>16s} {r['n_assets']:7d} {r['total_downloads']:10,d} "
              f"{r['max_downloads']:13,d}  {str(r['prerelease']):>6s}  {names}")

print()
print("=" * 108)
print("Q3. DEEP PROFILE OF NEW KEY PROJECTS")
print("=" * 108)
NEW = ["jingyaogong/minimind", "Tracer-Cloud/opensre", "zhouxiaoka/autoclip",
       "XiaoYouChR/Ghost-Downloader-3"]
for fn in NEW:
    m, _ = api(f"repos/{fn}")
    m = m or {}
    print(f"\n----- {fn} -----")
    print(f"  desc      : {m.get('description')}")
    print(f"  homepage  : {m.get('homepage')}")
    print(f"  topics    : {m.get('topics')}")
    print(f"  created   : {m.get('created_at')}   pushed: {m.get('pushed_at')}")
    print(f"  license   : {(m.get('license') or {}).get('spdx_id')}")
    print(f"  size_kb   : {m.get('size')}   default_branch: {m.get('default_branch')}")
    print(f"  archived={m.get('archived')} fork={m.get('fork')} "
          f"issues={m.get('has_issues')} discussions={m.get('has_discussions')}")
    wf, _ = api(f"repos/{fn}/contents/.github/workflows")
    print(f"  workflows : {[w.get('name') for w in wf] if isinstance(wf, list) else wf}")
    contrib, _ = api(f"repos/{fn}/contributors", {"per_page": 12})
    if isinstance(contrib, list) and contrib:
        print(f"  contributors: " + " · ".join(
            f"{c.get('login')}({c.get('contributions')})" for c in contrib))
    tree, _ = api(f"repos/{fn}/git/trees/{m.get('default_branch') or 'main'}?recursive=1")
    blobs = [b for b in ((tree or {}).get("tree") or []) if b.get("type") == "blob"]
    print(f"  blobs={len(blobs)} truncated={((tree or {}).get('truncated'))}")
    topdirs = Counter()
    for b in blobs:
        pp = (b.get("path") or "").split("/")[0]
        topdirs[pp] += 1
    print(f"  top-level dirs: {dict(topdirs.most_common(12))}")
    issues, _ = api(f"repos/{fn}/issues", {"state": "open", "per_page": 12})
    if isinstance(issues, list) and issues:
        print("  open issue titles:")
        for i in issues[:8]:
            print(f"     - #{i.get('number')} [{i.get('user',{}).get('login')}] "
                  f"c={i.get('comments')} {str(i.get('title'))[:88]}")
    rels, _ = api(f"repos/{fn}/releases", {"per_page": 3})
    if isinstance(rels, list) and rels:
        print("  latest releases:")
        for r in rels:
            body = (r.get("body") or "")[:260].replace("\n", " / ")
            print(f"     {r.get('tag_name')}  {r.get('published_at')}  assets="
                  f"{len(r.get('assets') or [])}  {body}")
    tags, _ = api(f"repos/{fn}/tags", {"per_page": 12})
    if isinstance(tags, list) and tags:
        print(f"  tags(sample): {[t.get('name') for t in tags]}")

print()
print("=" * 108)
print("Q4. ARE THE 'REPLICATED' SKILL COPIES CI-GENERATED OR HAND-MADE?")
print("=" * 108)
for fn in ["affaan-m/ECC", "backnotprop/plannotator", "cursor/plugins",
           "tradermonty/claude-trading-skills", "HKUDS/CLI-Anything"]:
    m, _ = api(f"repos/{fn}")
    m = m or {}
    tree, _ = api(f"repos/{fn}/git/trees/{m.get('default_branch') or 'main'}?recursive=1")
    blobs = [b for b in ((tree or {}).get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") or "" for b in blobs]
    gen = [p for p in paths if re.search(
        r"(generat|sync|mirror|copy|propagat|replicat|bundle|publish).*\.(py|js|ts|mjs|sh|yml|yaml)$",
        p, re.I)]
    print(f"\n{fn}: {len(paths)} blobs; {len(gen)} generator/sync-looking paths")
    for g in gen[:14]:
        print(f"    {g}")

print()
print("=" * 108)
print("Q5. TRENDING CHURN 11-18 -> 11-23")
print("=" * 108)
a = set(SNAPS["1118"])
b = set(SNAPS["1123"])
print(f"11-18 count={len(a)}  11-23 count={len(b)}  kept={len(a & b)}")
print("LEFT the list:")
for fn in sorted(a - b):
    print(f"   - {fn:44s} stars={SNAPS['1118'][fn].get('stars')}")
print("ENTERED the list:")
for fn in sorted(b - a):
    print(f"   + {fn:44s} stars={SNAPS['1123'][fn].get('stars')} "
          f"created={str(SNAPS['1123'][fn].get('created_at'))[:10]}")

print()
print("=" * 108)
print("Q6. NEW REPOS CREATED IN THE LAST 5 DAYS THAT REACHED THE LIST")
print("=" * 108)
for fn in sorted(b):
    p = SNAPS["1123"][fn]
    created = str(p.get("created_at") or "")[:10]
    if created >= "2026-11-18":
        age = None
        print(f"   {fn:44s} created={created} stars={p.get('stars'):,} "
              f"blobs={p.get('n_blobs')} commits={p.get('n_commits')} "
              f"owner_created={str(p.get('owner_created'))[:10]} "
              f"owner_followers={p.get('owner_followers')} "
              f"owner_repos={p.get('owner_public_repos')}")
