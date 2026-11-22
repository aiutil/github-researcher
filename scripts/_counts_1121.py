#!/usr/bin/env python3
"""Ground-truth tag / release counts by brute-force page walk.

Why this script exists
-----------------------
Earlier reports in this archive repeatedly printed "100 tag / 100 release"
for several repositories.  That number was produced by a single
`per_page=100` request: **a page-1 length of exactly 100 means ">= 100",
not "== 100"**.  Worse, the page walker used earlier stops as soon as a
page returns fewer than 100 items -- which is wrong, because GitHub's
`releases` endpoint returned 99 items on page 1 for `toeverything/AFFiNE`
while pages 2..7 were full.

This script therefore walks pages until it observes an **empty** page, and
records the per-page shape so the pagination is auditable.  Nothing is
inferred from header parsing.

Output: /tmp/counts_1121.json
"""
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/counts_1121.json"

REPOS = [
    "obra/superpowers", "firecrawl/firecrawl", "toeverything/AFFiNE",
    "mvanhorn/last30days-skill", "cathrynlavery/diagram-design",
    "jingyaogong/minimind", "HKUDS/CLI-Anything",
    "ChromeDevTools/chrome-devtools-mcp", "alibaba/open-code-review",
    "nginx/nginx", "meta/astryx", "dream-num/univer", "ag-ui-protocol/ag-ui",
    "cursor/plugins", "we-promise/sure", "elementalsouls/Claude-BugHunter",
    "backnotprop/plannotator", "XiaoYouChR/Ghost-Downloader-3",
    "Tracer-Cloud/opensre", "zhouxiaoka/autoclip",
    "openvinotoolkit/openvino", "google-labs-code/stitch-skills",
    "GoogleChrome/modern-web-guidance-src", "kajisho5/ffmpeg-skill",
    "tradermonty/claude-trading-skills", "mjmirza/app-store-compliance",
    "pookjw/HermesEnabler",
]


def page(full, kind, p):
    cmd = ["gh", "api", f"repos/{full}/{kind}?per_page=100&page={p}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=150)
    except subprocess.TimeoutExpired:
        return None
    if r.returncode != 0:
        return None
    try:
        d = json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        return None
    return d if isinstance(d, list) else None


def walk(full, kind, max_pages=60):
    counts = []
    for p in range(1, max_pages + 1):
        got = page(full, kind, p)
        if got is None:
            counts.append(None)
            break
        counts.append(len(got))
        if len(got) == 0:
            break
    nonempty = [c for c in counts if c]
    return {
        "per_page_counts": counts,
        "total": sum(nonempty),
        "last_nonempty_page": (len(nonempty) if nonempty else None),
        "pages_full": sum(1 for c in nonempty if c == 100),
        "first_page_short": bool(nonempty and nonempty[0] < 100),
    }


def probe(full):
    t = walk(full, "tags")
    r = walk(full, "releases")
    return {
        "repo": full,
        "tags": t,
        "releases": r,
        "tags_minus_releases": t["total"] - r["total"],
        "page1_cap_illusion": (t["total"] > 100 or r["total"] > 100),
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for row in ex.map(probe, REPOS):
            out.append(row)
            print(f"  {row['repo']:44s} tags={row['tags']['total']:>5} "
                  f"rel={row['releases']['total']:>5} "
                  f"gap={row['tags_minus_releases']:>+6} "
                  f"tagpages={row['tags']['per_page_counts']} "
                  f"relpages={row['releases']['per_page_counts']}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    illus = [r["repo"] for r in out if r["page1_cap_illusion"]]
    print(f"\nrepos where a single per_page=100 request would have undercounted: "
          f"{len(illus)}/{len(out)}")
    for x in illus:
        print("   ", x)


if __name__ == "__main__":
    main()
