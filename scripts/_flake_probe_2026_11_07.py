#!/usr/bin/env python3
import json, subprocess, os, statistics, datetime

ENV = {**os.environ, "HOME": "/home/lohasle", "GH_PAGER": "cat"}
def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, env=ENV, timeout=90)
    if r.returncode != 0:
        return None, r.stderr[:200]
    return r.stdout, None

REPO = "Tropicaldrescoop/discord-id-osint-checker"

# 1) commit timestamps
out, err = gh("api", f"repos/{REPO}/commits?per_page=100")
print("=== COMMITS ===")
if out:
    commits = json.loads(out)
    ts = []
    for c in commits:
        t = c["commit"]["author"]["date"]
        msg = c["commit"]["message"].split("\n")[0][:80]
        ts.append(t)
        print(f"  {t}  {msg}")
    if ts:
        ts_sorted = sorted(ts)
        print(f"  count={len(ts)} earliest={ts_sorted[0]} latest={ts_sorted[-1]}")
        # span in seconds
        def parse(x): return datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ")
        span = (parse(ts_sorted[-1]) - parse(ts_sorted[0])).total_seconds()
        print(f"  span_seconds={span:.0f} ({span/60:.1f} min)")
else:
    print("  ERR", err)

# 2) fork cadence
print("\n=== FORKS ===")
allforks = []
page = 1
while page <= 5:
    out, err = gh("api", f"repos/{REPO}/forks?per_page=100&page={page}")
    if not out:
        print("  ERR", err); break
    arr = json.loads(out)
    if not arr:
        break
    allforks.extend(arr)
    if len(arr) < 100:
        break
    page += 1

if allforks:
    times = sorted([f["created_at"] for f in allforks])
    print(f"  total_forks_fetched={len(allforks)}")
    print(f"  earliest={times[0]} latest={times[-1]}")
    dt = [parse(t) for t in times]
    gaps = [(dt[i+1]-dt[i]).total_seconds() for i in range(len(dt)-1)]
    if gaps:
        gs = sorted(gaps)
        print(f"  gap_median={statistics.median(gaps):.1f}s  min={min(gaps):.0f}s max={max(gaps):.0f}s")
        print(f"  p10={gs[len(gs)//10]:.0f}s p90={gs[int(len(gs)*0.9)]:.0f}s")
        under10 = sum(1 for g in gaps if g <= 10)
        print(f"  gaps<=10s: {under10}/{len(gaps)} = {100*under10/len(gaps):.1f}%")
    # fork owner ages
    owners = [f["owner"]["login"] for f in allforks[:12]]
    print("  --- fork owner profiles (sample 12) ---")
    for o in owners:
        out2, _ = gh("api", f"users/{o}")
        if out2:
            u = json.loads(out2)
            print(f"    {o:22s} created={u.get('created_at')} public_repos={u.get('public_repos')} followers={u.get('followers')}")
else:
    print("  no forks fetched")

# 3) is it in the farm cohort json?
print("\n=== COHORT CHECK ===")
cp = "/tmp/collect_1107/cohort_2026-11-06.json"
if os.path.exists(cp):
    d = json.load(open(cp))
    items = d if isinstance(d, list) else d.get("items", d.get("repos", []))
    hit = [x for x in items if "discord-id-osint" in json.dumps(x)]
    print(f"  cohort size={len(items)} hits={len(hit)}")
    for h in hit[:2]:
        print("  ", json.dumps(h)[:400])
