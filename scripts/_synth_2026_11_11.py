#!/usr/bin/env python3
"""Synthesize the 2026-11-10 candidate set (data window for the 2026-11-11 daily).

Reads /tmp/w1111/cand_1110.json and prints a compact distribution report:
star bands, forks, subs, size, license, language, README emptiness, commit entropy,
and the farm/farm-cluster heuristics used on previous days.
"""
import json
import sys
from collections import Counter

CAND = sys.argv[1] if len(sys.argv) > 1 else "/tmp/w1111/cand_1110.json"

with open(CAND, encoding="utf-8") as f:
    rows = json.load(f)

print(f"### candidates = {len(rows)}\n")

# --- star bands ---
bands = Counter()
for r in rows:
    s = r["stars"] or 0
    if s >= 400:
        bands["400+"] += 1
    elif s >= 300:
        bands["300-399"] += 1
    elif s >= 200:
        bands["200-299"] += 1
    elif s >= 100:
        bands["100-199"] += 1
    elif s >= 60:
        bands["60-99"] += 1
    else:
        bands["30-59"] += 1
print("=== A. star bands ===")
for k, v in sorted(bands.items()):
    print(f"  {k:10s} {v:4d}  ({v/len(rows)*100:.1f}%)")

# --- exact repeated star values (farm signature) ---
starvals = Counter(r["stars"] for r in rows)
print("\n=== B. repeated exact star values (>=2) ===")
for v, c in sorted(starvals.items(), key=lambda x: (-x[1], -x[0])):
    if c >= 2:
        print(f"  stars={v:5d}  count={c}")

# --- subs ---
print("\n=== C. subs ranking (all) ===")
for r in sorted(rows, key=lambda x: -(x["subs"] or 0))[:14]:
    print(f"  {r['full_name']:58s} subs={r['subs']:>4} stars={r['stars']:>5} forks={r['forks']:>4} "
          f"size={r['size_kb']:>6}KB c={r['ncommits']:>3} {r['language']}")

# --- empty README + tiny size + zero forks ---
print("\n=== D. shell-like repos (size<=20KB, forks==0, commits<=2) ===")
shells = [r for r in rows if (r["size_kb"] or 0) <= 20 and (r["forks"] or 0) == 0 and (r["ncommits"] or 0) <= 2]
print(f"  count = {len(shells)} / {len(rows)} = {len(shells)/len(rows)*100:.1f}%")
if shells:
    lic = Counter((r["license"] or "None") for r in shells)
    print(f"  licenses = {dict(lic)}")
    lang = Counter((r["language"] or "None") for r in shells)
    print(f"  languages = {dict(lang)}")
    print(f"  star values = {dict(sorted(Counter(r['stars'] for r in shells).items(), key=lambda x: -x[0]))}")
    print(f"  size values = {dict(sorted(Counter(r['size_kb'] for r in shells).items(), key=lambda x: -x[1]))}")
    print(f"  readme_len values = {dict(sorted(Counter(r['readme_len'] for r in shells).items(), key=lambda x: -x[1])[:6])}")
    print(f"  ncommits = {dict(Counter(r['ncommits'] for r in shells))}")
    print("  ALL samples:")
    for r in sorted(shells, key=lambda x: -(x["stars"] or 0)):
        print(f"    {r['full_name']:58s} size={r['size_kb']}KB stars={r['stars']} forks={r['forks']} "
              f"c={r['ncommits']} rl={r['readme_len']} lang={r['language']} lic={r['license']}")
        print(f"        desc: {(r['desc'] or '')[:100]}")

print("\n=== D2. size <= 5KB regardless of forks ===")
tiny = [r for r in rows if (r["size_kb"] or 0) <= 5]
print(f"  count = {len(tiny)}")
for r in sorted(tiny, key=lambda x: -(x["stars"] or 0)):
    print(f"    {r['full_name']:58s} size={r['size_kb']}KB stars={r['stars']} forks={r['forks']} c={r['ncommits']} rl={r['readme_len']} lang={r['language']}")

# --- high fork/star ratio ---
print("\n=== E. fork/star >= 50% (farm signature) ===")
fs = [r for r in rows if r["stars"] and (r["forks"] or 0) / r["stars"] >= 0.5]
print(f"  count = {len(fs)}")
for r in sorted(fs, key=lambda x: -(x["forks"] or 0)):
    print(f"    {r['full_name']:58s} stars={r['stars']:>5} forks={r['forks']:>4} "
          f"({(r['forks'] or 0)/r['stars']*100:.1f}%) subs={r['subs']} size={r['size_kb']}KB c={r['ncommits']}")

# --- commit second-field entropy ---
print("\n=== F. commit second-entropy (low => scripted) ===")
for r in sorted(rows, key=lambda x: (x["commit_secs"] if x["commit_secs"] is not None else 999)):
    if r["ncommits"] and r["ncommits"] <= 8:
        print(f"    {r['full_name']:58s} commits={r['ncommits']:>3} distinct_secs={r['commit_secs']:>3} stars={r['stars']:>5}")

# --- real-project candidates (readme non-empty, size > 20KB or commits > 8) ---
print("\n=== G. substantive candidates (readme>500 AND (size>20KB OR commits>8)) ===")
real = [r for r in rows if r["readme_len"] > 500 and ((r["size_kb"] or 0) > 20 or r["ncommits"] > 8)]
for r in sorted(real, key=lambda x: -(x["stars"] or 0)):
    print(f"    {r['full_name']:58s} stars={r['stars']:>5} forks={r['forks']:>4} subs={r['subs']:>3} oi={r['oi']:>3} "
          f"size={r['size_kb']:>6}KB c={r['ncommits']:>3} {r['language']} {r['license']}")
    print(f"        desc: {(r['desc'] or '')[:110]}")
    print(f"        created={r['created_at']} owner_created={r['owner_created']}")
