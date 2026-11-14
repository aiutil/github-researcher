#!/usr/bin/env python3
"""Cluster the deep-dive records by farm signature; print candidate clusters + standalone repos."""
import json
import re
import sys
from collections import Counter, defaultdict

DEEP = sys.argv[1] if len(sys.argv) > 1 else "/tmp/deep_1114.json"

data = json.load(open(DEEP, encoding="utf-8"))
by_day = defaultdict(list)
for r in data:
    by_day[(r.get("created_at") or "")[:10]].append(r)

for day in sorted(by_day):
    rows = by_day[day]
    print(f"\n########## {day}  n={len(rows)} ##########")
    # group by (normalized basename, size, commits)
    groups = defaultdict(list)
    for r in rows:
        base = r["full_name"].split("/")[1].lower()
        key = (re.sub(r"[^a-z0-9]", "", base), r["size_kb"], r["ncommits"])
        groups[key].append(r)
    print("--- size/name clusters (>=2 members) ---")
    for key, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        if len(g) < 2:
            continue
        stars = sorted({x["stars"] for x in g})
        forks = sorted({x["forks"] for x in g})
        subs = sorted({x["subs"] for x in g})
        oc = sorted({x["owner_created"] for x in g})
        print(f"  n={len(g):<3} name={key[0][:30]:<30} size={key[1]} commits={key[2]} stars={stars} forks={forks} subs={subs}")
        print(f"        owner_created: {oc[:3]}{'...' if len(oc)>3 else ''}  examples: {[x['full_name'] for x in g[:3]]}")
    print("--- singletons (possible real projects) ---")
    for key, g in groups.items():
        if len(g) > 1:
            continue
        r = g[0]
        print(f"  {r['stars']:>5}⭐ ⑂{r['forks']:<5} sub{r['subs']:<4} oi{r['oi']:<4} {str(r['size_kb']):>6}KB {r['nblobs']:>4}blobs {r['ncommits']:>3}c {str(r['owner_type'])[:6]:<6} oc={str(r['owner_created'])[:10]} rel={r['release_count']:<3} {r['full_name']}")
        print(f"        exts={r['top_exts'][:6]} lic={r['license']} lang={r['language']} desc={str(r['desc'])[:90]}")
        print(f"        files={r['top_files'][:12]}")
