#!/usr/bin/env python3
'''Detail pass on the three clusters found in the 2026-11-07 candidate set.'''

import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter, defaultdict
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
print("A. EMPTY-README CLUSTER (readme_len == 0)")
empty = [d for d in D if (d.get("readme_len") or 0) == 0]
print(f"count: {len(empty)} / {len(D)}")
print(f"size distribution: {Counter(d['size_kb'] for d in empty).most_common(8)}")
print(f"star distribution: {sorted(Counter(d['stars'] for d in empty).items())[:12]}")
print(f"forks==0: {sum(1 for d in empty if d['forks']==0)}")
print(f"licenses: {Counter(d['license'] for d in empty)}")
print(f"topics empty: {sum(1 for d in empty if not d['topics'])}/{len(empty)}")
print("names (first 20):")
for d in empty[:20]:
    print(f"   {d['full_name']:52} stars={d['stars']:4} forks={d['forks']:3} size={d['size_kb']:5}KB comm={d['ncommits']:3} lang={str(d['language'])[:10]:10} desc={str(d['desc'])[:70]}")
print()
print("  name keyword counts:")
kw = Counter()
for d in empty:
    n = d["full_name"].lower()
    for k in ["respocket", "rpocket", "resp-", "cheat", "spoofer", "aimbot", "wallhack", "esp", "bot", "tool", "edition", "2026"]:
        if k in n:
            kw[k] += 1
print("   ", kw.most_common())
print()
print("  full descriptions (first 15):")
for d in empty[:15]:
    print(f"   {d['full_name']:50} -> {d['desc']}")

print()
print("=" * 72)
print("B. THE TWO MACHINE-FORK REPOS (Steam-Idler / Minecraft-AFK-Bot)")
for full in ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot"]:
    m, _ = api(f"repos/{full}")
    tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    files = [(t["path"], t.get("size")) for t in (tree or {}).get("tree", []) if t["type"] == "blob"] if tree else []
    print(f"\n--- {full} ---")
    print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')}")
    print(f"  created={m.get('created_at')} pushed={m.get('pushed_at')} owner_type={(m.get('owner') or {}).get('type')}")
    print(f"  desc={m.get('description')}")
    print(f"  files({len(files)}): {files[:20]}")
    c, _ = api(f"repos/{full}/commits", {"per_page": 100})
    if isinstance(c, list):
        print(f"  commits({len(c)}):")
        for x in c[:8]:
            au = x["commit"]["author"]
            print(f"     {au['date']}  {x['commit']['message'][:80]!r}  author={au['name']!r}")
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    print(f"  README ({len(rm or '')} bytes):")
    print("   ", (rm or "")[:700].replace("\n", "\n    "))

print()
print("=" * 72)
print("C. RAYGULL / AXIOM-LAUNCH-REPLAY — commit entropy check")
full = "raygullcrease/axiom-launch-replay"
m, _ = api(f"repos/{full}")
tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
files = [(t["path"], t.get("size")) for t in (tree or {}).get("tree", []) if t["type"] == "blob"] if tree else []
print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} size={m.get('size')}KB lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')}")
print(f"  created={m.get('created_at')} pushed={m.get('pushed_at')} owner={m.get('owner',{}).get('created_at')} type={m.get('owner',{}).get('type')}")
print(f"  desc={m.get('description')}")
print(f"  top-level tree: {[f for f in files if '/' not in f[0]][:25]}")
print(f"  file count={len(files)}")
c, _ = api(f"repos/{full}/commits", {"per_page": 100})
if isinstance(c, list):
    secs = Counter()
    for x in c:
        secs[x["commit"]["author"]["date"][-2:]] += 1
    print(f"  commits={len(c)} second-field entropy: {len(secs)} distinct -> {secs.most_common(8)}")
    for x in c[:6]:
        print(f"     {x['commit']['author']['date']}  {x['commit']['message'][:70]!r}")
