#!/usr/bin/env python3
"""Why do yesterday's farm numbers (206/180) not reproduce today? Measure size shift + payload migration."""
import json, subprocess, os, re, collections

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


cohort = japi("search/repositories?q=created:2026-10-29+stars:>=40&per_page=100")
items = cohort["items"]
print(f"10-29 cohort total_count={cohort['total_count']} fetched={len(items)}")
buckets = collections.Counter()
for i in items:
    s = i["size"]
    if s <= 20:
        buckets["<=20KB"] += 1
    elif s <= 100:
        buckets["21-100KB"] += 1
    elif s <= 20480:
        buckets["101KB-20MB"] += 1
    else:
        buckets[">20MB"] += 1
print("  size buckets:", dict(buckets))

# Which repos are now 21-100KB but still farm-shaped (1-2 files)?
print("\n### repos now 21..100KB — check file count + payload (are they former 1-2KB shells that grew?)")
cands = [i for i in items if 20 < i["size"] <= 100]
print(f"  candidates: {len(cands)}")
for i in cands[:14]:
    full = i["full_name"]
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = [e for e in tree.get("tree", []) if e["type"] == "blob"]
    rd = api(f"repos/{full}/readme", raw=True) or ""
    pay = "git-software.cc" in rd or "Invoke-Expression" in rd
    tel = "telegra" in rd.lower()
    print(f"  {full:<48} size={i['size']:>5}KB blobs={len(blobs):>3} payload={pay} telegraph={tel} pushed={i['pushed_at']}")

print("\n### how many of the 46 size<=20 on 10-29 carry payload?")
small = [i for i in items if i["size"] <= 20]
hits = 0
for i in small[:20]:
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    if "git-software.cc" in rd or "Invoke-Expression" in rd:
        hits += 1
print(f"  {hits}/{min(20,len(small))} sampled size<=20 carry the payload")

print("\n### 10-30 cohort: same buckets")
c30 = japi("search/repositories?q=created:2026-10-30+stars:>=40&per_page=100")
b30 = collections.Counter()
for i in c30["items"]:
    s = i["size"]
    if s <= 20:
        b30["<=20KB"] += 1
    elif s <= 100:
        b30["21-100KB"] += 1
    elif s <= 20480:
        b30["101KB-20MB"] += 1
    else:
        b30[">20MB"] += 1
print(f"  total={c30['total_count']} buckets={dict(b30)}")
