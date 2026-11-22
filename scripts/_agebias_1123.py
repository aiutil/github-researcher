#!/usr/bin/env python3
"""RELEASE-AGE SELECTION BIAS TEST for the "asset download count" metric.

The 11-18 daily report concluded from `backnotprop/plannotator`:
    "asset 下载次数只有 1-12 次 ... 同样 100 个 release、同样闭合的 diff、
     同样认真的供应链纪律，「有多少人真的下载了」差了一到两个数量级"

But the probe only ever sampled the 6 MOST RECENT releases.  On 2026-11-23
the SAME tag (v0.28.67) reports max_asset_dl = 1354 and total = 7238.

Hypothesis H: download_count is monotone in release AGE, so sampling the
newest releases systematically reports the LOWEST download counts.

Test: for each repo, pull the full release list, and correlate
per-release total downloads with release age (days since published_at).
Also compare the newest-6 window against older releases for the same repo.
"""
import json
import os
import subprocess
import urllib.parse
from datetime import datetime, timezone

ENV = dict(os.environ, HOME="/home/lohasle")
NOW = datetime(2026, 11, 23, 6, 0, 0, tzinfo=timezone.utc)


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


REPOS = ["backnotprop/plannotator", "alibaba/open-code-review",
         "zhouxiaoka/autoclip", "XiaoYouChR/Ghost-Downloader-3",
         "nginx/nginx", "pookjw/HermesEnabler", "we-promise/sure"]

out = {}
for fn in REPOS:
    rels = api(f"repos/{fn}/releases", {"per_page": 100})
    if not isinstance(rels, list) or not rels:
        print(f"{fn}: no releases")
        continue
    rows = []
    for r in rels:
        pa = r.get("published_at")
        if not pa:
            continue
        dt = datetime.fromisoformat(pa.replace("Z", "+00:00"))
        age = (NOW - dt).total_seconds() / 86400.0
        assets = r.get("assets") or []
        rows.append({
            "tag": r.get("tag_name"),
            "published_at": pa,
            "age_days": round(age, 2),
            "n_assets": len(assets),
            "total_dl": sum(a.get("download_count") or 0 for a in assets),
            "max_dl": max([a.get("download_count") or 0 for a in assets] or [0]),
            "prerelease": r.get("prerelease"),
        })
    out[fn] = rows
    print(f"\n{fn}: {len(rows)} releases fetched", flush=True)

json.dump(out, open("/tmp/agebias_1123.json", "w"), ensure_ascii=False, indent=1)

print()
print("=" * 112)
print("A. NEWEST-6 WINDOW (what the probe actually samples) vs OLDER RELEASES")
print("=" * 112)
for fn, rows in out.items():
    rows_sorted = sorted(rows, key=lambda r: r["age_days"])
    newest6 = rows_sorted[:6]
    older = rows_sorted[6:]
    n_tot = sum(r["total_dl"] for r in newest6)
    n_max = max(r["max_dl"] for r in newest6)
    o_tot = sum(r["total_dl"] for r in older)
    o_max = max(r["max_dl"] for r in older)
    print(f"\n{fn}")
    print(f"   newest-6  : total_dl sum={n_tot:7,d}  max_asset={n_max:6,d}  "
          f"ages={[r['age_days'] for r in newest6]}")
    if older:
        print(f"   older({len(older):3d}) : total_dl sum={o_tot:7,d}  max_asset={o_max:6,d}  "
              f"age range {older[0]['age_days']:.1f}..{older[-1]['age_days']:.1f} d")
        ratio = (o_tot / n_tot) if n_tot else float("inf")
        print(f"   --> older/newest total_dl ratio = {ratio:.1f}x")

print()
print("=" * 112)
print("B. SAME TAG, DOWNLOAD COUNT OVER TIME (plannotator v0.28.67 & neighbours)")
print("=" * 112)
for fn in ["backnotprop/plannotator", "alibaba/open-code-review"]:
    rows = sorted(out.get(fn, []), key=lambda r: r["age_days"])
    print(f"\n{fn}  (11-18 published snapshot vs 11-23 live)")
    for r in rows[:8]:
        print(f"   {r['tag']:>18s}  age={r['age_days']:6.1f}d  assets={r['n_assets']:3d}  "
              f"total_dl={r['total_dl']:7,d}  max_dl={r['max_dl']:6,d}  pre={r['prerelease']}")

print()
print("=" * 112)
print("C. RANK CORRELATION: age vs total_dl (Spearman, per repo)")
print("=" * 112)


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                rk[order[k]] = avg
            i = j + 1
        return rk

    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    dy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


for fn, rows in out.items():
    rows = [r for r in rows if r["n_assets"] > 0]
    if len(rows) < 8:
        continue
    ages = [r["age_days"] for r in rows]
    dls = [r["total_dl"] for r in rows]
    rho = spearman(ages, dls)
    # bucket by age
    buckets = {}
    for r in rows:
        b = int(r["age_days"] // 7) * 7
        buckets.setdefault(b, []).append(r["total_dl"])
    bs = " | ".join(f"{b:3d}-{b+6}d n={len(v):3d} med={sorted(v)[len(v)//2]:6,d}"
                    for b, v in sorted(buckets.items()))
    print(f"\n{fn:42s} n={len(rows):3d}  spearman(age, total_dl) = {rho:+.3f}")
    print(f"   age buckets: {bs}")

print()
print("=" * 112)
print("D. ZERO-DOWNLOAD RELEASES — are they 'unpopular' or 'too new'?")
print("=" * 112)
for fn, rows in out.items():
    z = [r for r in rows if r["total_dl"] == 0]
    if not z:
        continue
    ages = [r["age_days"] for r in z]
    ages.sort()
    print(f"\n{fn}: {len(z)}/{len(rows)} releases with total_dl == 0")
    print(f"   their ages: min={ages[0]:.1f}d  median={ages[len(ages)//2]:.1f}d  max={ages[-1]:.1f}d")
    young = sum(1 for a in ages if a < 3)
    print(f"   of which age < 3 days: {young}  (age < 7d: {sum(1 for a in ages if a < 7)})")
