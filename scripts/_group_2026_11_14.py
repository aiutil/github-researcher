#!/usr/bin/env python3
"""Group the fingerprint set by full-README md5 and summarise each group."""
import json
import sys
from collections import Counter, defaultdict

FP = sys.argv[1] if len(sys.argv) > 1 else "/tmp/fingerprint_1114.json"
DAY = sys.argv[2] if len(sys.argv) > 2 else "2026-11-14"

data = json.load(open(FP, encoding="utf-8"))
rows = [r for r in data if r["day"] == DAY]
print(f"WINDOW {DAY}  n={len(rows)}")

groups = defaultdict(list)
for r in rows:
    groups[r["readme_md5"]].append(r)

print(f"\n=== README-md5 groups with >=3 members: {sum(1 for g in groups.values() if len(g)>=3)} ===")
for md5, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(g) < 3:
        continue
    stars = sorted(r["stars"] for r in g)
    forks = sorted(r["forks"] for r in g)
    subs = sorted(r["subs"] for r in g)
    oc = sorted((r["owner_created"] or "") for r in g)
    hosts = Counter()
    for r in g:
        for h, c in r["hosts"].items():
            hosts[h] += c
    print(f"\n  md5={md5[:16]}  n={len(g)}  readme_len={g[0]['readme_len']}B")
    print(f"    stars[{stars[0]}..{stars[-1]}] distinct={len(set(stars))} | forks[{forks[0]}..{forks[-1]}] | subs[{subs[0]}..{subs[-1]}]")
    print(f"    owner_created [{oc[0][:19]} .. {oc[-1][:19]}] distinct={len(set(oc))}")
    print(f"    owners: {len(set(r['full_name'].split('/')[0] for r in g))} accounts, each with {sorted(set(r['owner_repos'] for r in g))} public repos")
    print(f"    offline_build={sum(r['offline_build'] for r in g)}  download_link={sum(r['has_download_link'] for r in g)}  capsule={sum(r['capsule'] for r in g)}")
    print(f"    hosts: {dict(hosts.most_common(5))}")
    print(f"    licenses: {dict(Counter(r['license'] for r in g))}")
    print(f"    ex: {[x['full_name'] for x in g[:4]]}")

print(f"\n=== groups with 1-2 members ({sum(1 for g in groups.values() if len(g)<3)}) ===")
for md5, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(g) >= 3:
        continue
    r = g[0]
    print(f"  n={len(g)} md5={md5[:12]} {r['stars']:>4}⭐ {r['subs']:>3}sub {str(r['size_kb']):>6}KB {r['full_name']}")
    print(f"      hosts={r['hosts']} offline={r['offline_build']} dl={r['has_download_link']} capsule={r['capsule']} oc={str(r['owner_created'])[:19]} owner_repos={r['owner_repos']} lic={r['license']}")

# aggregate coverage
farm = sum(len(g) for g in groups.values() if len(g) >= 3)
print(f"\n=== coverage ===\n  in md5-groups of size>=3: {farm}/{len(rows)} = {farm/len(rows)*100:.1f}%")
ob = sum(1 for r in rows if r["offline_build"])
dl = sum(1 for r in rows if r["has_download_link"])
print(f"  'Standalone Offline Build' in README: {ob}  ({ob/len(rows)*100:.1f}%)")
print(f"  external download link in README:  {dl}  ({dl/len(rows)*100:.1f}%)")
