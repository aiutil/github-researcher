#!/usr/bin/env python3
'''Deep-dive the 2026-11-07 candidate set: clone-family detection, fork timing
distribution, commit-timestamp entropy, and README payload checks.'''

import json
import os
import re
import subprocess
import time
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
D = json.load(open("/tmp/cand_1107.json", encoding="utf-8"))


def api(path, params=None, timeout=90, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:
        return None, "parse"


# ---------- 1. clone family detection ----------
print("=" * 70)
print("1. CLONE FAMILY: repos whose name contains manus")
fam = [d for d in D if "manus" in d["full_name"].lower()]
print(f"count: {len(fam)}")
by_suffix = Counter()
for d in fam:
    base = d["full_name"].split("/")[1]
    norm = re.sub(r"[^a-z0-9]+", "", base.lower())
    by_suffix[norm] += 1
for k, v in by_suffix.most_common():
    print(f"  normalized name {k:26} x{v}")
print(f"  distinct stars among them: {sorted(set(d['stars'] for d in fam))}")
print(f"  distinct forks among them: {sorted(set(d['forks'] for d in fam))}")
print(f"  distinct sizes: {sorted(set(d['size_kb'] for d in fam))}")
print(f"  distinct commits: {sorted(set(d['ncommits'] for d in fam))}")
print(f"  licenses: {Counter(d['license'] for d in fam)}")

print()
print("  sample READMEs (manus family):")
for d in fam[:3]:
    print(f"  --- {d['full_name']} (stars={d['stars']} forks={d['forks']} subs={d['subs']} size={d['size_kb']}KB comm={d['ncommits']}) ---")
    print("   ", d["readme_head"][:900].replace("\n", "\n    "))
    print()

# ---------- 2. README template similarity across the whole set ----------
print("=" * 70)
print("2. README SIMILARITY (first 400 chars normalized) - groups with >=3 members")
sig = defaultdict(list)
for d in D:
    body = re.sub(r"\s+", " ", d.get("readme_head") or "").strip().lower()
    if len(body) < 60:
        body = f"<empty-or-tiny:{len(body)}>"
    sig[body[:300]].append(d["full_name"])
for k, v in sorted(sig.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= 3:
        print(f"  group of {len(v)}: {v[:8]}")
        print(f"     sig: {k[:200]}")

# ---------- 3. fork timing for top candidates ----------
print()
print("=" * 70)
print("3. FORK TIMING DISTRIBUTION (top 12 by stars)")


def fork_times(full):
    arr, _ = api(f"repos/{full}/forks", {"per_page": 100, "sort": "newest"})
    if not isinstance(arr, list):
        return []
    return [f["created_at"] for f in arr]


def median(xs):
    xs = sorted(xs)
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


from datetime import datetime


def parse(t):
    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")


targets = sorted(D, key=lambda d: -d["stars"])[:12]
for d in targets:
    ft = fork_times(d["full_name"])
    if not ft:
        print(f"  {d['full_name']:50} stars={d['stars']:4} forks={d['forks']:4} -> no fork timestamps")
        continue
    ts = sorted(parse(t) for t in ft)
    gaps = [(ts[i + 1] - ts[i]).total_seconds() for i in range(len(ts) - 1)]
    med = median(gaps)
    le10 = sum(1 for g in gaps if g <= 10)
    span = (ts[-1] - ts[0]).total_seconds()
    print(
        f"  {d['full_name']:50} stars={d['stars']:4} forks={d['forks']:4} sampled={len(ft):3} "
        f"med_gap={med}s le10={le10}/{len(gaps)} span={span/60:.1f}min"
    )
    time.sleep(0.5)
