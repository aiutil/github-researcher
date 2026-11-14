#!/usr/bin/env python3
"""Forensics for the 2026-11-09 UTC candidate window (daily report 2026-11-10).

Focus:
  A. The 279-281* / high-fork cluster: is it the 11-06 template (md5 e18f025c... / 8470fd5b...)?
  B. subs inflation: Roblox-FPS-Optimizer has subs 77 -- above the 25/35 that the
     2026-11-08 report identified as an attacked criterion.
  C. windows-defender.cc payload: same domain, lower star band (280-290 vs 400).
  D. The 40* rpocket/respocket empty-README cluster.
  E. huamidev/GestaltX (1362*) deep look.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_2026_11_10.json"
data = json.load(open(PATH, encoding="utf-8"))


def api(path_, raw=True, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    return p.stdout


def raw_file(full, path_):
    t = api(f"repos/{full}/contents/{path_}", headers=["Accept: application/vnd.github.raw"])
    return t or ""


print(f"### candidates={len(data)}\n")

# ---------------- A. the 279-281 template cluster ------------------------
CLUSTER = [
    "Nanoutrolley/roblox-studio-mcp",
    "Sectionsereclaim/discord-auto-quest",
    "ridgecobblerslide/windows-animated-wallpapers",
    "TameCarpenterEstate/Roblox-FPS-Optimizer",
    "Platoonritomb/Fortnite-FPS-Booster-Performance-Optimizer",
]
KNOWN = {
    "e18f025c87b71b9fe481f53ac6e8235d": "11-06/11-07 farm .gitignore",
    "8470fd5b911eacd63327be59d2562f16": "11-06/11-07 farm helpers.py",
}
print("=== A. TEMPLATE CLUSTER: file inventory + md5 fingerprints ===")
for full in CLUSTER:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        print(f"  {full}: tree failed")
        continue
    files = [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    print(f"\n  -- {full}  ({len(files)} files)")
    for p, s in sorted(files):
        content = raw_file(full, p)
        h = hashlib.md5(content.encode("utf-8", "replace")).hexdigest()
        tag = KNOWN.get(h, "")
        print(f"       {s:>8}  md5={h}  {p}   {tag}")
        time.sleep(0.1)
    time.sleep(0.2)

print("\n=== A2. cluster README: 'Star the repo' CTA check ===")
for full in CLUSTER:
    rm = raw_file(full, "README.md")
    cta = [ln.strip() for ln in rm.splitlines() if "star the repo" in ln.lower()]
    print(f"  {full[:46]:48s} readme_len={len(rm):>6} CTA={len(cta)} {cta[:1]}")
    time.sleep(0.15)

print("\n=== A3. cluster fork-arrival timing ===")
for full in CLUSTER:
    t = api(f"repos/{full}/forks")
    try:
        arr = json.loads(t)
    except Exception:
        print(f"  {full}: fork fetch failed")
        continue
    ts = sorted(a.get("created_at") for a in arr if a.get("created_at"))
    if len(ts) < 2:
        print(f"  {full[:46]:48s} forks sampled={len(ts)}")
        continue
    gaps = []
    for i in range(1, len(ts)):
        a = datetime.fromisoformat(ts[i - 1].replace("Z", "+00:00"))
        b = datetime.fromisoformat(ts[i].replace("Z", "+00:00"))
        gaps.append((b - a).total_seconds())
    gs = sorted(gaps)
    med = gs[len(gs) // 2]
    le10 = sum(1 for g in gaps if g <= 10)
    span = (datetime.fromisoformat(ts[-1].replace("Z", "+00:00"))
            - datetime.fromisoformat(ts[0].replace("Z", "+00:00"))).total_seconds() / 60
    print(f"  {full[:46]:48s} sampled={len(ts):>3} med_gap={med:>7.1f}s le10={le10}/{len(gaps)} span={span:.1f}min")
    time.sleep(0.2)

# ---------------- B. subs inflation ranking ------------------------------
print("\n=== B. SUBS RANKING (all candidates) ===")
for x in sorted(data, key=lambda y: -(y["subs"] or 0))[:12]:
    print(f"  {x['full_name'][:46]:48s} subs={x['subs']:>4} stars={x['stars']:>4} forks={x['forks']:>4} {x['size_kb']:>7}KB c{x['ncommits']:>3}")

# ---------------- C. windows-defender.cc payload today --------------------
print("\n=== C. windows-defender.cc TODAY ===")
wd = [x for x in data if "windows-defender.cc" in x["readme_head"]]
print(f"  count={len(wd)}  stars={sorted(Counter(x['stars'] for x in wd).items())}")
print(f"  created range: {min(x['created_at'] for x in wd)} .. {max(x['created_at'] for x in wd)}")
print(f"  forks={Counter(x['forks'] for x in wd).most_common(4)} size={Counter(x['size_kb'] for x in wd).most_common(4)}")
rm = raw_file(wd[0]["full_name"], "README.md")
for m in re.findall(r"irm\s+https?://[^\s|]+[^\n]*", rm):
    print(f"  payload line: {m.strip()}")
print(f"  md5 of one README: {hashlib.md5(rm.encode()).hexdigest()} len={len(rm)}")

# ---------------- D. the 40* respocket empty-README cluster -------------
print("\n=== D. 40* respocket cluster ===")
rp = [x for x in data if x["stars"] == 40]
print(f"  count={len(rp)}  readme_len set={sorted(set(x['readme_len'] for x in rp))[:8]}")
print(f"  forks={Counter(x['forks'] for x in rp).most_common(3)}  ncommits={Counter(x['ncommits'] for x in rp).most_common(3)}")
print(f"  size_kb={Counter(x['size_kb'] for x in rp).most_common(5)}  license={Counter(str(x['license']) for x in rp).most_common(3)}")
print(f"  language={Counter(str(x['language']) for x in rp).most_common(5)}")
print(f"  name markers resp/rpocket/resocket: {sum(1 for x in rp if re.search('resp|rpocket|resocket', x['full_name'], re.I))}/{len(rp)}")
print("  sample descs:")
for x in rp[:8]:
    print(f"    {x['full_name'][:46]:48s} :: {str(x['desc'])[:70]}")

# ---------------- E. huamidev/GestaltX -----------------------------------
print("\n=== E. huamidev/GestaltX (1362*) ===")
g = "huamidev/GestaltX"
m = api(f"repos/{g}")
try:
    j = json.loads(m)
    for k in ["stargazers_count", "forks_count", "subscribers_count", "open_issues_count", "size",
              "language", "created_at", "pushed_at", "default_branch"]:
        print(f"  {k} = {j.get(k)}")
    print(f"  license = {(j.get('license') or {}).get('spdx_id')}")
    print(f"  topics = {j.get('topics')}")
    print(f"  desc = {j.get('description')}")
except Exception as e:
    print("  repo fetch failed", e)
t = api(f"repos/{g}/git/trees/HEAD?recursive=1")
try:
    j = json.loads(t)
    blobs = [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    print(f"  files={len(blobs)}")
    for p, s in sorted(blobs)[:28]:
        print(f"    {s:>9}  {p}")
except Exception:
    print("  tree failed")
