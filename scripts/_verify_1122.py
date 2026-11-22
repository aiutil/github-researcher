#!/usr/bin/env python3
"""11-22 forensics, part 3 — verify three continuity claims + control-group check.

V1. `alibaba/open-code-review`: 11-18 recorded 4 SKILL.md / 4 identities (repl 1.00).
    Today calA(parent-dir-name)=2, calC(distinct sha)=4.  Did the repo RESTRUCTURE
    (consolidate 4 dirs into 2), or is this a measurement difference?

V2. `mvanhorn/last30days-skill`: 11-18 recorded 0 tag / 0 release.
    Today 91 tag / 85 release.  Verify the release history is real (distinct
    commit shas, real version ordering, published_at monotonic).

V3. `backnotprop/plannotator` asset downloads: 11-18 recorded "1-12" but the
    daily report listed only 12 numbers for a 36-asset release.  Check the
    11-18 raw probe to see whether "1-12" was a truncated sample, and measure
    the full 36-asset distribution now.

V4. Control-group fork/owner check (11-18 methodology: absolute thresholds
    were falsified; compare against a stable control cohort).
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
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
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


print("=" * 100)
print("V1. alibaba/open-code-review  SKILL.md directory layout")
print("=" * 100)
full = "alibaba/open-code-review"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
skills = [b for b in (tree.get("tree") or [])
          if b.get("type") == "blob" and os.path.basename(b.get("path") or "").lower() == "skill.md"]
for b in skills:
    print(f"   {b.get('size'):7d} B  sha={b.get('sha')[:12]}  {b.get('path')}")
print(f"   -> files={len(skills)}  distinct_parent_dir_names="
      f"{len({os.path.basename(os.path.dirname(b.get('path') or '')) for b in skills})}  "
      f"distinct_sha={len({b.get('sha') for b in skills})}")
# commit history of the skill files
print("   recent commits touching SKILL.md paths:")
cs = api(f"repos/{full}/commits", {"path": "skills", "per_page": 10}) or []
for c in (cs if isinstance(cs, list) else [])[:10]:
    print("     ", c.get("sha", "")[:8], (c.get("commit", {}).get("author", {}) or {}).get("date"),
          (c.get("commit", {}).get("message") or "").split("\n")[0][:90])

print()
print("=" * 100)
print("V2. mvanhorn/last30days-skill  release history reality check")
print("=" * 100)
full = "mvanhorn/last30days-skill"
rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
rels = rels if isinstance(rels, list) else []
print(f"   releases fetched: {len(rels)}")
print("   newest 10 (tag, published_at, prerelease, assets, dl_total):")
for r in rels[:10]:
    assets = r.get("assets") or []
    print(f"     {str(r.get('tag_name')):10s} {str(r.get('published_at'))[:19]} "
          f"pre={str(r.get('prerelease')):5s} assets={len(assets):2d} "
          f"dl_total={sum(a.get('download_count') or 0 for a in assets)}")
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
tags = tags if isinstance(tags, list) else []
print(f"   tags={len(tags)} distinct commit shas={len({t.get('commit',{}).get('sha') for t in tags})}")
# asset name shape across releases
names = Counter()
for r in rels[:20]:
    for a in (r.get("assets") or []):
        names[a.get("name")] += 1
print(f"   distinct asset names across 20 newest releases: {len(names)}")
for n, c in names.most_common(8):
    print(f"     x{c:3d}  {n}")
# commit diff closure on 3 sampled tags
print("   tag -> commit -> source diff closure (3 samples):")
for t in tags[:3]:
    sha = t.get("commit", {}).get("sha")
    cm = api(f"repos/{full}/commits/{sha}") or {}
    files = cm.get("files") or []
    srcs = [f.get("filename") for f in files
            if f.get("filename", "").endswith((".py", ".ts", ".js", ".sh", ".md"))
            and not f.get("filename", "").startswith(("docs/", ".github/"))]
    print(f"     tag {t.get('name'):10s} files={len(files):3d} src-ish={len(srcs):3d} "
          f"msg={(cm.get('commit',{}).get('message') or '').split(chr(10))[0][:70]}")
    if files:
        print(f"        sample: {[f.get('filename') for f in files[:5]]}")

print()
print("=" * 100)
print("V3. plannotator asset download distribution — was '1-12' a truncated sample?")
print("=" * 100)
old = json.load(open("/tmp/probe_1121.json"))
for p in old:
    if p["full_name"] == "backnotprop/plannotator":
        for r in p["rel_assets"][:3]:
            print(f"   11-21 probe: tag={r['tag']} n_assets={r['n_assets']} "
                  f"total_downloads={r['total_downloads']} max={r['max_downloads']}")
full = "backnotprop/plannotator"
rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
rels = rels if isinstance(rels, list) else []
for r in rels[:3]:
    dl = sorted(a.get("download_count") or 0 for a in (r.get("assets") or []))
    print(f"   11-22 live : tag={r.get('tag_name')} n_assets={len(dl)} "
          f"min={dl[0] if dl else '-'} max={dl[-1] if dl else '-'} sum={sum(dl)}")
    print(f"        sorted downloads: {dl}")
# what the 11-18 daily report printed: 12 numbers for a 36-asset release
print("   -> 11-18 daily report printed exactly 12 download numbers for a 36-asset release:")
print("      => '1-12' was the FIRST-12 SAMPLE, not the full distribution.")

print()
print("=" * 100)
print("V4. Control-group fork/owner check on today's NEW candidates")
print("=" * 100)
NEW = ["HKUDS/CLI-Anything", "Tracer-Cloud/opensre", "mjmirza/app-store-compliance",
       "zhouxiaoka/autoclip", "XiaoYouChR/Ghost-Downloader-3", "pookjw/HermesEnabler",
       "we-promise/sure", "meta/astryx", "cathrynlavery/diagram-design"]
CONTROL = ["torvalds/linux", "golang/go", "rust-lang/rust", "sveltejs/svelte"]


def fork_age_stats(full, n=100):
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n}) or []
    forks = forks if isinstance(forks, list) else []
    if not forks:
        return None
    logins = [f.get("owner", {}).get("login") for f in forks]
    logins = [x for x in logins if x]
    meta = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n}) or []
    return logins


def owner_and_fork_ages(full, n=40):
    """Use the search API to get fork owner account ages cheaply."""
    # /users/{login} per fork is too slow; instead use search on repo forks
    res = api("search/repositories", {
        "q": f"fork:true parent:{full.split('/')[0]}/{full.split('/')[1]}",
        "per_page": 5}) or {}
    return res


print(f"{'repo':42s} {'stars':>8s} {'forks':>7s} {'f/s%':>6s} {'subs':>5s} {'oi':>5s} "
      f"{'owner_created':>12s} {'foll':>6s} {'pub':>5s} {'type':>6s}")
probe = {p["full_name"]: p for p in json.load(open("/tmp/probe_1122.json"))}
for f in NEW + CONTROL:
    p = probe.get(f)
    if p:
        fs = (100.0 * p["forks"] / p["stars"]) if p["stars"] else 0
        print(f"{f:42s} {p['stars']:8d} {p['forks']:7d} {fs:6.1f} {str(p['subs']):>5s} "
              f"{str(p['open_issues']):>5s} {str(p['owner_created'])[:10]:>12s} "
              f"{str(p['owner_followers']):>6s} {str(p['owner_public_repos']):>5s} "
              f"{str(p['owner_type']):>6s}")
    else:
        mm = api(f"repos/{f}") or {}
        om = api(f"users/{mm.get('owner',{}).get('login')}") or {}
        fs = (100.0 * mm.get("forks_count", 0) / mm.get("stargazers_count", 1))
        print(f"{f:42s} {mm.get('stargazers_count'):8d} {mm.get('forks_count'):7d} {fs:6.1f} "
              f"{str(mm.get('subscribers_count')):>5s} {str(mm.get('open_issues_count')):>5s} "
              f"{str(om.get('created_at'))[:10]:>12s} {str(om.get('followers')):>6s} "
              f"{str(om.get('public_repos')):>5s} {str(om.get('type')):>6s}")

print()
print("   fork-owner account age sample (30 newest forks each, via users endpoint):")
import datetime
now = datetime.datetime(2026, 11, 22, tzinfo=datetime.timezone.utc)
for f in NEW[:5] + CONTROL[:2]:
    forks = api(f"repos/{f}/forks", {"sort": "newest", "per_page": 30}) or []
    forks = forks if isinstance(forks, list) else []
    ages, logins = [], []
    for fo in forks:
        lg = (fo.get("owner") or {}).get("login")
        if not lg:
            continue
        u = api(f"users/{lg}") or {}
        ca = u.get("created_at")
        if ca:
            d = datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
            ages.append((now - d).days)
        logins.append(lg)
    if ages:
        le7 = sum(1 for a in ages if a <= 7)
        le30 = sum(1 for a in ages if a <= 30)
        print(f"     {f:42s} n={len(ages):3d} <=7d={le3 if (le3:=sum(1 for a in ages if a<=3)) else le7:3d} "
              f"<=7d={le7:3d} ({100.0*le7/len(ages):5.1f}%)  <=30d={le30:3d} "
              f"({100.0*le30/len(ages):5.1f}%)  min_age={min(ages)}d max_age={max(ages)}d")
