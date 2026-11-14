#!/usr/bin/env python3
"""First-pass triage of collected candidates: cluster by farm signals, rank real ones."""
import json
import re
import sys
from collections import Counter, defaultdict

CAND = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1114.json"
DAY = sys.argv[2] if len(sys.argv) > 2 else "2026-11-14"

data = json.load(open(CAND, encoding="utf-8"))
by_day = defaultdict(list)
for r in data:
    d = (r.get("created_at") or "")[:10]
    by_day[d].append(r)

print(f"total {len(data)}  days: { {k: len(v) for k, v in by_day.items()} }")
print()

for day in sorted(by_day):
    rows = by_day[day]
    print(f"===== {day}  n={len(rows)} =====")
    print("star histogram:", sorted(Counter(r["stars"] for r in rows).items())[:15])
    # payload hits
    hits = [r for r in rows if r["hit_invoke_expression"] or r["hit_irm"] or r["hit_iwr"] or r["hit_sal"]]
    print(f"payload-readme hits: {len(hits)}")
    for r in hits[:6]:
        print("   ", r["full_name"], r["stars"], r["owner_created"], r["readme_len"])
    print("--- top by stars ---")
    for r in rows[:18]:
        print(f"  {r['stars']:>6}⭐ ⑂{r['forks']:<5} sub{r['subs']:<4} {str(r['size_kb']):>7}KB {str(r['ncommits']):>4}c {str(r['owner_type'])[:6]:<6} created={str(r['owner_created'])[:10]} {r['full_name']}")
    print()
