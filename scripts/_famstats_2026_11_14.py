#!/usr/bin/env python3
"""Family-level statistics for the 2026-11-14 window: owner creation windows, README md5 spread, forks distribution."""
import json
import re
import sys
from collections import Counter, defaultdict

CAND = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1114.json"
DAY = sys.argv[2] if len(sys.argv) > 2 else "2026-11-14"

data = json.load(open(CAND, encoding="utf-8"))
rows = [r for r in data if (r.get("created_at") or "")[:10] == DAY]

groups = defaultdict(list)
for r in rows:
    base = r["full_name"].split("/")[1].lower()
    key = re.sub(r"[^a-z0-9]", "", base)
    groups[key].append(r)

print(f"WINDOW {DAY}  n={len(rows)}")
print(f"star distribution: {sorted(Counter(r['stars'] for r in rows).items())[:12]} ... distinct values={len(set(r['stars'] for r in rows))}")
print(f"owner_created distinct: {len(set(r['owner_created'] for r in rows))}")
print(f"owner accounts with >1 repo in window: ", end="")
oc = Counter(r["owner_created"] for r in rows)
print(sum(1 for v in oc.values() if v > 1))
print(f"total unique owner accounts: {len(set(r['full_name'].split('/')[0] for r in rows))}")
print()

for key, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(g) < 3:
        continue
    md5s = Counter(r.get("readme_head", "")[:200] for r in g)
    forks = sorted(r["forks"] for r in g)
    stars = sorted(r["stars"] for r in g)
    subs = sorted(r["subs"] for r in g)
    ocreated = sorted((r["owner_created"] or "") for r in g)
    otypes = Counter(r["owner_type"] for r in g)
    print(f"### family '{key}'  n={len(g)}")
    print(f"    stars  min={stars[0]} max={stars[-1]} median={stars[len(stars)//2]} distinct={len(set(stars))}")
    print(f"    forks  min={forks[0]} max={forks[-1]} distinct={len(set(forks))}")
    print(f"    subs   min={subs[0]} max={subs[-1]} distinct={len(set(subs))}")
    print(f"    owner_created range {ocreated[0][:19]} .. {ocreated[-1][:19]}  distinct={len(set(ocreated))}")
    print(f"    owner types: {dict(otypes)}")
    print(f"    README first-200-char distinct: {len(md5s)}")
    print(f"    sizes: {sorted(set(r['size_kb'] for r in g))}  commits: {sorted(set(r['ncommits'] for r in g))}")
    print(f"    licenses: {dict(Counter(r['license'] for r in g))}")
    print(f"    examples: {[x['full_name'] for x in g[:3]]}")
    print()
