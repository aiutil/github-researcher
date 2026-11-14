#!/usr/bin/env python3
'''Verify the third-day farm template, the subscriber paradox, and read the
real projects' own evidence documents.'''

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
print("A. THE rpocket/respocket 85-REPO CLUSTER: what is actually inside?")
rp = [d for d in D if "rpocket" in d["full_name"].lower() or "respocket" in d["full_name"].lower()]
print(f"count={len(rp)}  all stars==42: {all(d['stars']==42 for d in rp)}  all forks==0: {all(d['forks']==0 for d in rp)}")
print(f"  all license None: {all(d['license'] is None for d in rp)}")
print(f"  all readme_len==0: {all(d['readme_len']==0 for d in rp)}")
print(f"  topics count distribution: {Counter(len(d['topics']) for d in rp)}")
print(f"  commit count distribution: {Counter(d['ncommits'] for d in rp)}")
print(f"  size distribution: {sorted(Counter(d['size_kb'] for d in rp).items())}")
print(f"  created_at spread: {sorted(set(d['created_at'] for d in rp))[:6]} ...")
print()
for full in ["QuantumQuietpulse/metatrader-5-respocket-bot", "ArmorBeforePrincess/rpocket-Exunys-ESP", "GoblinWildlord/5m-mods-rpocket-team-2026"]:
    tree, err = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    if not tree:
        print(f"  {full}: tree -> {err}")
        continue
    files = [(t["path"], t.get("size")) for t in tree.get("tree", []) if t["type"] == "blob"]
    print(f"  {full}: {len(files)} files -> {files[:10]}")
    for fpath, _ in files[:3]:
        r, _ = api(f"repos/{full}/contents/{urllib.parse.quote(fpath)}", raw=True,
                   headers=["Accept: application/vnd.github.raw"])
        if r:
            print(f"      [{fpath}] {r[:260]!r}")
    print()

print("=" * 72)
print("B. THE SUBSCRIBER PARADOX: subs for farms vs real projects")
allc = sorted(D, key=lambda d: -(d["subs"] or 0))
print("  top-12 by subscribers across the whole 162-repo candidate set:")
for d in allc[:12]:
    print(f"    {d['full_name']:50} stars={d['stars']:4} forks={d['forks']:4} subs={d['subs']:3} "
          f"size={d['size_kb']:6}KB comm={d['ncommits']:3} readme={d['readme_len']:5}")
print()
print("  ratio subs/forks for the top-6:")
for d in allc[:6]:
    print(f"    {d['full_name']:50} subs/forks={d['subs']/max(d['forks'],1):.3f}")

print()
print("=" * 72)
print("C. raygullcrease/axiom-launch-replay: fork owner ages + backfill check")
full = "raygullcrease/axiom-launch-replay"
forks, _ = api(f"repos/{full}/forks", {"per_page": 100, "sort": "newest"})
if isinstance(forks, list):
    print(f"  forks listed: {len(forks)}")
    years = Counter()
    for f in forks[:30]:
        u, _ = api(f"users/{f['owner']['login']}")
        if u:
            years[u.get("created_at", "")[:4]] += 1
    print(f"  fork-owner account creation years (n=30): {sorted(years.items())}")
cm, _ = api(f"repos/{full}/commits", {"per_page": 100})
if isinstance(cm, list):
    dates = [x["commit"]["author"]["date"] for x in cm]
    print(f"  commit dates: earliest={min(dates)} latest={max(dates)}")
    print(f"  repo created_at=2026-11-07T02:03:47Z -> commits predate repo creation by "
          f"{(datetime(2026,11,7,2,3,47)-datetime.strptime(min(dates),'%Y-%m-%dT%H:%M:%SZ')).days} days")

print()
print("=" * 72)
print("D. REAL PROJECTS: read their own evidence docs")
for full, path, lim in [
    ("lxe/phoneuse", "README.md", 3000),
    ("lxe/phoneuse", "ARCHITECTURE.md", 2000),
    ("Th0rgal/satmux", "README.md", 3000),
    ("dabingfy-dot/solo-to-team-skills", "README.md", 2000),
    ("MajestyPoemFold/ghostclick-mouse-double-click-fix", "README.md", 2500),
]:
    r, _ = api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
               headers=["Accept: application/vnd.github.raw"])
    print(f"\n--- {full} :: {path} ({len(r or '')} bytes) ---")
    print((r or "")[:lim])
