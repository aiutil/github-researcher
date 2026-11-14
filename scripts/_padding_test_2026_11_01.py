#!/usr/bin/env python3
"""DECISIVE TEST 2: was the 10-29 cohort's size<=20KB count dropped by in-place padding?

10-30 daily recorded: created:2026-10-29 + stars>=40 -> 206 repos, 180 with size<=20KB (87.4%).
Today the same query returns 268 total, 47 with size<=20KB.

Hypothesis P: the farm pushed a padding commit (.gitignore blob 6f596e17, 4664 bytes + extra
files) into those repos, growing `size` past the 20KB threshold.

Prediction: the repos that REMAIN size<=20 have pushed_at close to created_at (never padded),
while the ones that grew past 20KB have pushed_at after 2026-10-29T24:00Z.
"""
import json, subprocess, os, re

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def japi(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    try:
        return json.loads(r.stdout) if r.returncode == 0 else None
    except Exception:
        return None


def raw(path):
    r = subprocess.run(["gh", "api", path, "-H", "Accept:application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else ""


print("### A) the 47 still-small 10-29 repos: created_at vs pushed_at")
res = japi("search/repositories?q=created:2026-10-29+stars:>=40+size:<=20&per_page=100")
items = res["items"]
same_day = 0
later = 0
for i in items:
    r = japi(f"repos/{i['full_name']}")
    if not r:
        continue
    if r["pushed_at"][:10] <= "2026-10-29":
        same_day += 1
    else:
        later += 1
print(f"  n={len(items)}  pushed_on_or_before_10-29: {same_day}   pushed_later: {later}")
print("  (if padding is the cause, the survivors should be the never-pushed ones)")

print("\n### B) sample of repos that GREW past 20KB: do they carry the shared .gitignore blob?")
PAD_SHA = "6f596e17917419c463b0d15bf1f0bce19b8918eb"
res2 = japi("search/repositories?q=created:2026-10-29+stars:>=40+size:>20&per_page=40")
n = 0
pad = 0
for i in res2["items"][:40]:
    gi = japi(f"repos/{i['full_name']}/contents/.gitignore")
    if not gi:
        continue
    n += 1
    if gi.get("sha") == PAD_SHA:
        pad += 1
print(f"  checked={n}  with .gitignore sha==6f596e17...: {pad}")

print("\n### C) channel split across the whole 10-29 cohort (size:>20 bucket)")
NAIVE_A = re.compile(r"git-software\.cc", re.I)
NAIVE_B = re.compile(r"activation-gateway\.cc", re.I)
a = b = both = neither = 0
for i in res2["items"][:40]:
    rd = raw(f"repos/{i['full_name']}/readme")
    if not rd:
        continue
    ha, hb = bool(NAIVE_A.search(rd)), bool(NAIVE_B.search(rd))
    if ha and hb: both += 1
    elif ha: a += 1
    elif hb: b += 1
    else: neither += 1
print(f"  naiveA_only={a}  B_only={b}  both={both}  neither={neither}")

print("\n### D) QuantumBladesmith fork burst: count per minute")
r = japi("repos/QuantumBladesmith/FPS-Optimizer-Universal-Game-Performance-Booster-2026")
print(f"  stars={r['stargazers_count']} forks={r['forks_count']} subs={r['subscribers_count']} "
      f"created={r['created_at']} pushed={r['pushed_at']} size={r['size']}KB")
fk = japi("repos/QuantumBladesmith/FPS-Optimizer-Universal-Game-Performance-Booster-2026/forks?per_page=100") or []
ts = sorted(x["created_at"] for x in fk)
if ts:
    print(f"  first 100 forks span {ts[0]} .. {ts[-1]}  ({len(ts)} shown)")
    print(f"  fork names identical to parent repo name: "
          f"{sum(1 for x in fk if x['name'] == r['name'])}/{len(fk)}")
