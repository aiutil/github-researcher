#!/usr/bin/env python3
"""Summarise the collected candidate set: cluster by signature, then rank."""

import json
import re
import sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_2026_11_09.json"
data = json.load(open(path, encoding="utf-8"))
print(f"total candidates: {len(data)}\n")

# --- cluster by README length + size + forks signature -----------------
clusters = Counter()
for d in data:
    if d["readme_len"] == 0:
        clusters["empty_readme"] += 1
    elif d["readme_len"] < 500:
        clusters["tiny_readme"] += 1
    else:
        clusters["real_readme"] += 1
print("readme size classes:", dict(clusters))

empty = [d for d in data if d["readme_len"] == 0]
tiny = [d for d in data if 0 < d["readme_len"] < 500]
real = [d for d in data if d["readme_len"] >= 500]
print(f"\nempty={len(empty)} tiny={len(tiny)} real={len(real)}")

print("\n--- EMPTY README repos (top 25 by stars) ---")
for d in sorted(empty, key=lambda x: -(x["stars"] or 0))[:25]:
    print(f"  {d['full_name']:52s} ⭐{d['stars']:>5} ⑂{d['forks']:>4} subs{d['subs']:>3} "
          f"{d['size_kb']:>7}KB commits{d['ncommits']:>3} {str(d['language']):12s} "
          f"{str(d['license']):12s} topics{len(d['topics']):>2} :: {str(d['desc'])[:60]}")

print("\n--- star value distribution (empty cluster) ---")
print(Counter(d["stars"] for d in empty).most_common(12))
print("\n--- size distribution (empty cluster) ---")
print(Counter(d["size_kb"] for d in empty).most_common(12))

print("\n--- keyword markers across ALL candidates ---")
for marker in ["git-software.cc", "Invoke-Expression", "Star the repo", "star the repo",
               "discord.com/api/webhooks", "Downloads-40K", "Related Search Terms",
               "PROMO2026", "hack", "cheat", "esp", "spoofer", "miner"]:
    hits = [d["full_name"] for d in data if marker.lower() in d["readme_head"].lower()]
    if hits:
        print(f"  {marker:28s} {len(hits):>4}  e.g. {hits[:3]}")

print("\n--- REAL README candidates (>=500B), sorted by stars ---")
for d in sorted(real, key=lambda x: -(x["stars"] or 0))[:45]:
    print(f"  {d['full_name']:50s} ⭐{d['stars']:>5} ⑂{d['forks']:>4} subs{d['subs']:>3} "
          f"oi{d['oi']:>3} {d['size_kb']:>7}KB c{d['ncommits']:>3} {str(d['language']):12s} "
          f"{str(d['license']):12s} rm{d['readme_len']:>6} :: {str(d['desc'])[:55]}")
