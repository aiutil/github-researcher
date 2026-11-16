#!/usr/bin/env python3
"""Analyse the 2026-11-16 candidate set: cluster by README md5, extract
payload links, rank by engineering-effort proxies, flag anomalies."""
import json
import re
import sys
from collections import Counter, defaultdict

SRC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1116.json"
C = json.load(open(SRC))
print(f"candidates: {len(C)}\n")

by_md5 = defaultdict(list)
for r in C:
    by_md5[r["readme_md5"]].append(r)

print("=== README md5 clusters (>=2) ===")
clusters = [(k, v) for k, v in by_md5.items() if len(v) >= 2]
clusters.sort(key=lambda kv: -len(kv[1]))
for md5, group in clusters:
    stars = sorted(g["stars"] for g in group)
    owners = sorted({g["owner_login"] for g in group})
    roots = Counter(g["full_name"].split("/")[1].lower() for g in group)
    print(f"\nmd5={md5[:16]}… n={len(group)} readme_len={group[0]['readme_len']} "
          f"stars={stars[0]}–{stars[-1]} distinct_stars={len(set(stars))}")
    print(f"  owners={len(owners)} created={min(g['created_at'] for g in group)} .. "
          f"{max(g['created_at'] for g in group)}")
    print(f"  roots: {dict(roots.most_common(8))}")
    for g in group[:4]:
        print(f"    - {g['full_name']} ⭐{g['stars']} commits={g['n_commits']} "
              f"blobs={g['n_blobs']} oi={g['oi']} subs={g['subs']} "
              f"owner={g['owner_login']} ocreated={g['owner_created']}")

sing = [v[0] for k, v in by_md5.items() if len(v) == 1]
print(f"\n=== singletons: {len(sing)} ===")

URL = re.compile(r"https?://[^\s)\"'<>\]`]+")
PAY = ("dropbox", "mediafire", "mega.nz", "drive.google", "wetransfer",
       "pixeldrain", "linkbox", "discord.gg", "quark", "pan.baidu", "bit.ly")
print("\n=== payload-ish external links in README head ===")
for r in C:
    m = URL.findall(r.get("readme_head", ""))
    sus = [u for u in m if any(k in u.lower() for k in PAY)]
    if sus:
        print(f"  {r['full_name']} ⭐{r['stars']} -> {sus[:3]}")

print("\n=== ranked by engineering-effort proxy ===")
print(f"{'repo':<50} {'⭐':>6} {'forks':>5} {'subs':>5} {'oi':>4} "
      f"{'cmt':>4} {'blob':>5} {'sec':>4} {'lic':<14} owner/age")


def eff(r):
    return (r["n_blobs"] * 2 + r["n_commits"] * 3 + (r["forks"] or 0) * 5
            + (r["oi"] or 0) * 3 + (r["subs"] or 0) * 2 + len(r["exts"]) * 2)


for r in sorted(C, key=eff, reverse=True):
    print(f"{r['full_name']:<50} {r['stars']:>6} {r['forks'] or 0:>5} "
          f"{r['subs'] or 0:>5} {r['oi'] or 0:>4} {r['n_commits']:>4} "
          f"{r['n_blobs']:>5} {len(r['commit_secs']):>4} "
          f"{(r['license'] or '-'):<14} {r['owner_login']}/"
          f"{(r['owner_created'] or '-')[:10]} foll={r['owner_followers']} "
          f"repos={r['owner_public_repos']}")
    print(f"    exts={r['exts']} lang={r['language']} size={r['size_kb']}KB "
          f"desc={(r['description'] or '')[:100]}")
