#!/usr/bin/env python3
'''Summarise the candidate set and flag farm-like clusters.'''

import json
import re
from collections import Counter, defaultdict

D = json.load(open("/tmp/cand_1107.json", encoding="utf-8"))
print(f"total candidates: {len(D)}")

sizes = [d["size_kb"] for d in D if d.get("size_kb") is not None]
print(f"size<=20KB: {sum(1 for s in sizes if s <= 20)}  ({sum(1 for s in sizes if s<=20)/len(sizes)*100:.1f}%)")
print(f"forks==0: {sum(1 for d in D if d.get('forks') == 0)}  ({sum(1 for d in D if d.get('forks')==0)/len(D)*100:.1f}%)")

stars = sorted(d["stars"] for d in D)
print(f"star min={stars[0]} max={stars[-1]} median={stars[len(stars)//2]}")
band = Counter()
for s in stars:
    band[s // 25 * 25] += 1
print("star bands (25-wide, top 12):", band.most_common(12))

print()
print("=== payload hits ===")
for k in ["hit_git_software", "hit_invoke_expression", "hit_irm", "hit_iwr", "hit_defender", "hit_discord_webhook"]:
    hits = [d for d in D if d.get(k)]
    print(f"{k:26} {len(hits):4}  e.g. {[h['full_name'] for h in hits[:4]]}")

print()
print("=== fork/star ratio high (>=30%) ===")
hi = [d for d in D if d.get("stars") and d.get("forks", 0) / d["stars"] >= 0.30]
hi.sort(key=lambda d: -(d["forks"] / d["stars"]))
for d in hi[:25]:
    print(f"  {d['full_name']:52} stars={d['stars']:5} forks={d['forks']:5} fs={d['forks']/d['stars']*100:5.1f}% size={d['size_kb']:6}KB comm={d['ncommits']:4} subs={d['subs']} lang={d['language']}")

print()
print("=== subs >= 2 (depth signal) ===")
sd = [d for d in D if (d.get("subs") or 0) >= 2]
sd.sort(key=lambda d: -(d.get("subs") or 0))
for d in sd:
    print(f"  {d['full_name']:52} stars={d['stars']:5} forks={d['forks']:4} subs={d['subs']:3} oi={d['oi']:4} size={d['size_kb']:7}KB comm={d['ncommits']:4} lang={str(d['language'])[:12]:12} lic={d['license']}")

print()
print("=== commits >= 10 and size >= 100KB (real engineering candidates) ===")
real = [d for d in D if (d.get("ncommits") or 0) >= 10 and (d.get("size_kb") or 0) >= 100]
real.sort(key=lambda d: -d["stars"])
for d in real:
    print(f"  {d['full_name']:52} stars={d['stars']:5} forks={d['forks']:4} subs={d['subs']:3} comm={d['ncommits']:4} size={d['size_kb']:8}KB lang={str(d['language'])[:14]:14} lic={d['license']} secs={d['commit_secs']}")
    print(f"       desc: {str(d['desc'])[:150]}")
