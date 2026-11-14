#!/usr/bin/env python3
"""Owner-account creation-time clustering across the whole fingerprint set."""
import json
import sys
from collections import Counter, defaultdict

FP = sys.argv[1] if len(sys.argv) > 1 else "/tmp/fingerprint_1114.json"

data = json.load(open(FP, encoding="utf-8"))
rows = [r for r in data if r["day"] in ("2026-11-13", "2026-11-14")]
print(f"n={len(rows)} over 2026-11-13 + 2026-11-14\n")

# bucket owner_created by minute
buckets = defaultdict(list)
for r in rows:
    oc = r["owner_created"] or ""
    if oc:
        buckets[oc[:16]].append(r)

print("=== owner_created minute-buckets with >=4 accounts ===")
for k, g in sorted(buckets.items()):
    if len(g) < 4:
        continue
    subs = [r["subs"] for r in g]
    stars = [r["stars"] for r in g]
    print(f"\n  {k}Z  n={len(g)}")
    print(f"    subs: {sorted(Counter(subs).items())}")
    print(f"    stars: [{min(stars)}..{max(stars)}] distinct={len(set(stars))}")
    print(f"    repos: {sorted(set(r['full_name'].split('/')[1] for r in g))[:8]}")
    print(f"    owner_repos: {sorted(Counter(r['owner_repos'] for r in g).items())}")

print("\n=== the 7 high-subs repos ===")
hi = sorted([r for r in rows if r["subs"] >= 20], key=lambda r: -r["subs"])
for r in hi:
    print(f"  {r['subs']:>3}sub {r['stars']:>4}star {str(r['size_kb']):>6}KB oc={r['owner_created']} owner_repos={r['owner_repos']} followers={r['owner_followers']} {r['full_name']}")
    print(f"      topics={r['topics'][:4]} md5={r['readme_md5'][:12]} capsule={r['capsule']}")

print("\n=== 2026-10-14 creation window (dropbox farm owners) ===")
b2 = defaultdict(list)
for r in rows:
    oc = r["owner_created"] or ""
    if oc.startswith("2026-10-14"):
        b2[oc[:13]].append(r)
for k, g in sorted(b2.items()):
    print(f"  {k}Z n={len(g)} stars[{min(r['stars'] for r in g)}..{max(r['stars'] for r in g)}] md5s={len(set(r['readme_md5'] for r in g))}")
