#!/usr/bin/env python3
"""Extract today's GitHub Trending (daily + weekly) repo list + star deltas
from the raw HTML snapshots fetched via curl.

Output: /tmp/trend_1119.json
"""
import json
import re

OUT = "/tmp/trend_1119.json"

SNAP = {
    "daily": "/tmp/trending_daily_1119.html",
    "weekly": "/tmp/trending_weekly_1119.html",
}


def parse(path, period):
    src = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for blk in re.findall(r'<article class="Box-row">.*?</article>', src, re.S):
        m = re.search(r'<h2 class="h3 lh-condensed">.*?href="/([^"?]+)"', blk, re.S)
        if not m:
            continue
        full = m.group(1).strip()
        # star count: the anchor ending in /stargazers
        stars = None
        sm = re.search(r'href="/[^"]+/stargazers"[^>]*>\s*(?:<svg.*?</svg>\s*)?([\d,]+)\s*stars?', blk, re.S)
        if sm:
            stars = int(sm.group(1).replace(",", ""))
        else:
            sm2 = re.search(r'stargazers"[^>]*>.*?([\d,]+)\s*</', blk, re.S)
            if sm2:
                stars = int(sm2.group(1).replace(",", ""))
        # period delta: "N stars today" / "N stars this week"
        delta = None
        dm = re.search(r'([\d,]+)\s*stars?\s*(today|this week|this month)', blk, re.I)
        if dm:
            delta = int(dm.group(1).replace(",", ""))
        lang = None
        lm = re.search(r'<span itemprop="programmingLanguage">([^<]+)</span>', blk)
        if lm:
            lang = lm.group(1).strip()
        forks = None
        fm = re.search(r'href="/[^"]+/forks"[^>]*>.*?([\d,]+)\s*</', blk, re.S)
        if fm:
            forks = int(fm.group(1).replace(",", ""))
        out.append({
            "full_name": full,
            "period": period,
            "stars": stars,
            "period_stars": delta,
            "language": lang,
            "forks": forks,
        })
    return out


rows = []
for period, path in SNAP.items():
    try:
        rows.extend(parse(path, period))
    except FileNotFoundError:
        print(f"missing snapshot {path}")

seen = {}
order = []
for r in rows:
    fn = r["full_name"]
    if fn not in seen:
        seen[fn] = dict(r)
        seen[fn]["periods"] = [r["period"]]
        order.append(fn)
    else:
        if r["period"] not in seen[fn]["periods"]:
            seen[fn]["periods"].append(r["period"])
        if r["stars"]:
            seen[fn]["stars"] = max(seen[fn]["stars"] or 0, r["stars"])

data = [seen[fn] for fn in order]
json.dump(data, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"wrote {len(data)} repos -> {OUT}")
for d in data:
    print(f"  {d['full_name']:45s} *{d['stars']} ({d['period_stars']} {d['period']}) "
          f"{d['language']} periods={d['periods']}")
