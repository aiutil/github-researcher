#!/usr/bin/env python3
"""Deep analysis of the 2026-11-08 candidate set."""

import json
import re
import sys
from collections import Counter, defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_2026_11_09.json"
data = json.load(open(path, encoding="utf-8"))

# --- Cluster A: the "pre-configured environment" farm --------------------
farmA = [d for d in data if "pre-configured environment" in (d["desc"] or "").lower()
         or "automated deployment pipeline" in (d["desc"] or "").lower()]
print(f"=== Cluster A (pre-configured / deployment pipeline) : {len(farmA)} ===")
print("stars:", Counter(d["stars"] for d in farmA).most_common())
print("forks:", Counter(d["forks"] for d in farmA).most_common())
print("size_kb:", Counter(d["size_kb"] for d in farmA).most_common())
print("ncommits:", Counter(d["ncommits"] for d in farmA).most_common())
print("language:", Counter(str(d["language"]) for d in farmA).most_common())
print("license:", Counter(str(d["license"]) for d in farmA).most_common())
print("subs:", Counter(d["subs"] for d in farmA).most_common())
print("commit_secs:", Counter(d["commit_secs"] for d in farmA).most_common())
print("readme_len distinct:", len(set(d["readme_len"] for d in farmA)))
print("sample descs:")
for d in farmA[:6]:
    print("   ", d["full_name"], "|", d["desc"])

rest = [d for d in data if d not in farmA]
print(f"\n=== REST: {len(rest)} ===")

# --- Cluster B: forks > 0 (real-ish) ------------------------------------
real = [d for d in rest if (d["forks"] or 0) > 0]
print(f"\n--- REST with forks>0: {len(real)}, sorted by stars ---")
for d in sorted(real, key=lambda x: -(x["stars"] or 0)):
    print(f"  {d['full_name']:48s} ⭐{d['stars']:>5} ⑂{d['forks']:>4} subs{d['subs']:>3} "
          f"oi{d['oi']:>3} {d['size_kb']:>6}KB c{d['ncommits']:>3} sec{d['commit_secs']:>3} "
          f"{str(d['language']):11s} {str(d['license']):12s} rm{d['readme_len']:>6} :: {str(d['desc'])[:60]}")

# --- Cluster C: REST with 0 forks ---------------------------------------
nofork = [d for d in rest if (d["forks"] or 0) == 0]
print(f"\n--- REST with forks==0: {len(nofork)}, sorted by stars ---")
for d in sorted(nofork, key=lambda x: -(x["stars"] or 0))[:40]:
    print(f"  {d['full_name']:48s} ⭐{d['stars']:>5} ⑂{d['forks']:>4} subs{d['subs']:>3} "
          f"oi{d['oi']:>3} {d['size_kb']:>6}KB c{d['ncommits']:>3} sec{d['commit_secs']:>3} "
          f"{str(d['language']):11s} {str(d['license']):12s} rm{d['readme_len']:>6} :: {str(d['desc'])[:60]}")

# --- owner analysis -----------------------------------------------------
owners = defaultdict(list)
for d in data:
    owners[d["full_name"].split("/")[0]].append(d)
newish = [(o, v) for o, v in owners.items() if len(v) >= 2]
print(f"\n=== owners with >=2 repos: {len(newish)} ===")
for o, v in sorted(newish, key=lambda x: -len(x[1]))[:25]:
    print(f"  {o:38s} n={len(v):>3} stars={sorted(set(x['stars'] for x in v))[:6]} "
          f"forks={sorted(set(x['forks'] for x in v))[:6]}")

# --- created_at spread --------------------------------------------------
times = sorted(d["created_at"] for d in data if d["created_at"])
print(f"\ncreated_at window: {times[0]} .. {times[-1]}")
buckets = Counter(t[:13] for t in times)
print("per-hour buckets:", sorted(buckets.items())[:24])

# --- owner account age --------------------------------------------------
print("\nowner account ages (distinct owner_created):")
oc = Counter(d["owner_created"][:10] if d["owner_created"] else None for d in data)
print(" ", oc.most_common(10))
print("owner_type:", Counter(d["owner_type"] for d in data).most_common())

# --- readme head of one farm A repo -------------------------------------
print("\n=== sample README head (Cluster A) ===")
print(repr(farmA[0]["readme_head"][:1400]) if farmA else "none")
