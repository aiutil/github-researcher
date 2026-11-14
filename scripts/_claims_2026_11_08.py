#!/usr/bin/env python3
'''Final claim verification for the 2026-11-08 report.'''

import json
import os
import subprocess
import urllib.parse
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
D = json.load(open("/tmp/cand_1107.json", encoding="utf-8"))


def api(path, params=None, timeout=90, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:
        return None, "parse"


print("=" * 72)
print("A. zero-breach: did the repo get reset? (11-06 snapshot said 4,475 stars, 55 commits)")
m, _ = api("repos/interplains/zero-breach")
print(f"  now: stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} "
      f"size={m.get('size')}KB created={m.get('created_at')} pushed={m.get('pushed_at')}")
c, _ = api("repos/interplains/zero-breach/commits", {"per_page": 100})
if isinstance(c, list):
    dates = [x["commit"]["author"]["date"] for x in c]
    print(f"  commits={len(c)} earliest={min(dates)} latest={max(dates)}")
    for x in c[:4]:
        print(f"    {x['commit']['author']['date']}  {x['commit']['message'][:70]!r}")
rels, _ = api("repos/interplains/zero-breach/releases")
print(f"  releases={len(rels) if isinstance(rels, list) else rels}")
owner, _ = api("users/interplains")
print(f"  owner: created={owner.get('created_at')} public_repos={owner.get('public_repos')} type={owner.get('type')}")
# older name
m2, e2 = api("repos/interplains/Zero-Breach-Toolkit")
print(f"  old path Zero-Breach-Toolkit -> {e2 or 'resolves'}")

print()
print("=" * 72)
print("B. sheeridVerify fork timing re-check (yesterday: median 73s = human)")
full = "JenkinWoo/sheeridVerify"
forks, _ = api(f"repos/{full}/forks", {"per_page": 100, "sort": "newest"})
if isinstance(forks, list):
    ts = sorted(datetime.strptime(f["created_at"], "%Y-%m-%dT%H:%M:%SZ") for f in forks)
    gaps = [(ts[i + 1] - ts[i]).total_seconds() for i in range(len(ts) - 1)]
    gaps_s = sorted(gaps)
    med = gaps_s[len(gaps_s) // 2]
    print(f"  forks={len(forks)} median_gap={med}s le10={sum(1 for g in gaps if g <= 10)}/{len(gaps)} "
          f"span={(ts[-1]-ts[0]).total_seconds()/60:.1f}min")

print()
print("=" * 72)
print("C. the 85-repo rpocket cluster creation window")
rp = [d for d in D if "rpocket" in d["full_name"].lower() or "respocket" in d["full_name"].lower()]
rp_all = [d for d in D if d["readme_len"] == 0]
print(f"  rpocket-named: {len(rp)}  all-empty-readme: {len(rp_all)}")
ts = sorted(d["created_at"] for d in rp_all)
print(f"  creation window (all 85): {ts[0]} .. {ts[-1]}")
span = (datetime.strptime(ts[-1], "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(ts[0], "%Y-%m-%dT%H:%M:%SZ")).total_seconds()
print(f"  span = {span:.0f}s ({span/60:.1f} min)")
per_sec = Counter(t[-2:] for t in ts)
print(f"  per-second buckets (top 8): {per_sec.most_common(8)}")

print()
print("=" * 72)
print("D. the 57-repo manus cluster creation window")
man = [d for d in D if "manus" in d["full_name"].lower()]
ts2 = sorted(d["created_at"] for d in man)
span2 = (datetime.strptime(ts2[-1], "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(ts2[0], "%Y-%m-%dT%H:%M:%SZ")).total_seconds()
print(f"  window {ts2[0]} .. {ts2[-1]}  span={span2/60:.1f} min")
print(f"  owner-name sample: {[d['full_name'].split('/')[0] for d in man[:10]]}")

print()
print("=" * 72)
print("E. ghostclick + solstice + satmux final metadata")
for full in ["MajestyPoemFold/ghostclick-mouse-double-click-fix", "SamG-Coder/solstice",
             "Th0rgal/satmux", "lxe/phoneuse", "dabingfy-dot/solo-to-team-skills"]:
    m, _ = api(f"repos/{full}")
    if not m:
        print(f"  {full}: not found")
        continue
    rels, _ = api(f"repos/{full}/releases")
    ct, _ = api(f"repos/{full}/contributors")
    own, _ = api(f"users/{m.get('owner',{}).get('login')}")
    tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    nfiles = len([t for t in (tree or {}).get("tree", []) if t["type"] == "blob"]) if tree else 0
    print(f"  {full}")
    print(f"    stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} "
          f"oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} "
          f"lic={(m.get('license') or {}).get('spdx_id')} files={nfiles}")
    print(f"    created={m.get('created_at')} pushed={m.get('pushed_at')} owner_created={own.get('created_at')} "
          f"owner_repos={own.get('public_repos')} releases={len(rels) if isinstance(rels, list) else 0} "
          f"contributors={len(ct) if isinstance(ct, list) else '?'} topics={len(m.get('topics') or [])}")
