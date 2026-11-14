#!/usr/bin/env python3
"""Check whether LiveWall's 30 forks come from accounts created in a burst."""

import json
import os
import subprocess
import time

ENV = dict(os.environ, HOME="/home/lohasle")
FULL = "elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop"


def api(path):
    p = subprocess.run(["gh", "api", path], capture_output=True, text=True,
                       env=ENV, timeout=90)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


forks = api(f"repos/{FULL}/forks?per_page=100&sort=newest") or []
print(f"forks: {len(forks)}\n")
rows = []
for f in forks:
    o = f["owner"]["login"]
    u = api(f"users/{o}") or {}
    rows.append((f["created_at"], o, u.get("created_at"), u.get("public_repos"),
                 u.get("followers"), u.get("type")))
    time.sleep(0.25)

rows.sort()
print(f"{'fork_at':22s} {'owner':34s} {'acct_created':21s} repos foll type")
for r in rows:
    print(f"{r[0]:22s} {r[1]:34s} {str(r[2]):21s} {str(r[3]):>5} {str(r[4]):>4} {r[5]}")

print("\n=== account creation date distribution ===")
from collections import Counter
print(Counter(str(r[2])[:10] for r in rows).most_common())
print("\n=== account creation within 60 min of each other ===")
ts = sorted(str(r[2]) for r in rows if r[2])
print("min:", ts[0] if ts else None, " max:", ts[-1] if ts else None)
if ts:
    import datetime as dt
    p = dt.datetime.strptime(ts[0], "%Y-%m-%dT%H:%M:%SZ")
    q = dt.datetime.strptime(ts[-1], "%Y-%m-%dT%H:%M:%SZ")
    print(f"span of account creation: {(q-p).total_seconds()/60:.1f} minutes")
