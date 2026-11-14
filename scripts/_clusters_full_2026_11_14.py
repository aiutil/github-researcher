#!/usr/bin/env python3
"""Full-window cluster analysis on all candidates (not just top 60)."""
import json
import re
import sys
from collections import Counter, defaultdict

CAND = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1114.json"
DAY = sys.argv[2] if len(sys.argv) > 2 else "2026-11-14"

data = json.load(open(CAND, encoding="utf-8"))
rows = [r for r in data if (r.get("created_at") or "")[:10] == DAY]
print(f"n={len(rows)}")

groups = defaultdict(list)
for r in rows:
    base = r["full_name"].split("/")[1].lower()
    key = re.sub(r"[^a-z0-9]", "", base)
    groups[key].append(r)

print(f"\n=== name-families with >=3 members ({sum(1 for g in groups.values() if len(g)>=3)} families) ===")
for key, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(g) < 3:
        continue
    stars = sorted(r["stars"] for r in g)
    forks = sorted(r["forks"] for r in g)
    subs = sorted(r["subs"] for r in g)
    sizes = sorted({r["size_kb"] for r in g})
    commits = sorted({r["ncommits"] for r in g})
    oc = sorted({(r["owner_created"] or "") for r in g})
    print(f"  n={len(g):<4} {key[:34]:<34} sizes={sizes} commits={commits}")
    print(f"         stars[{stars[0]}..{stars[-1]}] forks[{forks[0]}..{forks[-1]}] subs[{subs[0]}..{subs[-1]}] oc[{oc[0][:19]}..{oc[-1][:19]}]")
    print(f"         ex: {[x['full_name'] for x in g[:2]]}")

print(f"\n=== singletons ({sum(1 for g in groups.values() if len(g)==1)}) ===")
for key, g in groups.items():
    if len(g) != 1:
        continue
    r = g[0]
    print(f"  {r['stars']:>5}⭐ ⑂{r['forks']:<4} sub{r['subs']:<3} {str(r['size_kb']):>6}KB {r['ncommits']:>3}c {str(r['owner_type'])[:6]:<6} {r['full_name']}")
    print(f"        desc={str(r['desc'])[:110]}")
    print(f"        lic={r['license']} lang={r['language']} topics={r['topics'][:5]} fork={r['fork']} parent={r['parent']}")
    print(f"        readme_len={r['readme_len']} :: {r['readme_head'][:180]!r}")
