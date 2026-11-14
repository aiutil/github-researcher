#!/usr/bin/env python3
"""Full-cohort payload prevalence for the 10-30 farm (all 168), with owner/name fingerprints."""
import json, subprocess, os, collections

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def j(p):
    r = subprocess.run(["gh", "api", p], capture_output=True, text=True, env=ENV)
    try:
        return json.loads(r.stdout) if r.returncode == 0 else None
    except Exception:
        return None


def raw(p):
    r = subprocess.run(["gh", "api", p, "-H", "Accept:application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else ""


c = j("search/repositories?q=created:2026-10-30+stars:>=40+size:<=20&per_page=100")
items = c["items"]
print(f"total_count={c['total_count']} fetched={len(items)}")
hit = tel = both = 0
readable = 0
lens = collections.Counter()
for i in items:
    rd = raw(f"repos/{i['full_name']}/readme")
    if not rd:
        continue
    readable += 1
    lens[len(rd) // 100 * 100] += 1
    p = ("git-software.cc" in rd) or ("Invoke-Expression" in rd)
    t = "telegra" in rd.lower()
    if p and t:
        both += 1
    elif p:
        hit += 1
    elif t:
        tel += 1
print(f"readable={readable} payload_only={hit} telegraph_only={tel} both={both}")
print("README size buckets (100B):", dict(sorted(lens.items())))
owners = [i["owner"]["login"] for i in items]
print(f"distinct owners={len(set(owners))} of {len(owners)}")
print("owner name length set:", sorted({len(o) for o in owners}))
print("owner type set:", {i["owner"]["type"] for i in items})
names = [i["name"] for i in items]
print("repo name length set:", sorted({len(n) for n in names}))
