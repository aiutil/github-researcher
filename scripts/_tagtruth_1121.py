#!/usr/bin/env python3
"""Measure the TRUE tag count for every repo whose first API page returned
exactly 100 tags.

The `tags` endpoint caps at per_page=100, so a page-1 length of exactly 100
means ">= 100", not "== 100". The Link header's rel="last" gives the real
page count. This script resolves the real totals and also counts releases
across all pages.

Output: /tmp/tagtruth_1121.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/tagtruth_1121.json"

REPOS = [
    "nginx/nginx", "firecrawl/firecrawl", "meta/astryx",
    "GoogleChrome/modern-web-guidance-src", "alibaba/open-code-review",
    "backnotprop/plannotator", "ag-ui-protocol/ag-ui", "dream-num/univer",
    "toeverything/AFFiNE", "kajisho5/ffmpeg-skill", "Tracer-Cloud/opensre",
    "XiaoYouChR/Ghost-Downloader-3", "openvinotoolkit/openvino",
    "obra/superpowers", "mvanhorn/last30days-skill", "we-promise/sure",
    "zhouxiaoka/autoclip", "ChromeDevTools/chrome-devtools-mcp",
]


def raw_api(path, timeout=120):
    cmd = ["gh", "api", "-i", path]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, None
    if p.returncode != 0:
        return None, None
    out = p.stdout
    # split headers from body: gh api -i prints headers then a blank line
    parts = out.split("\n\n", 1)
    headers = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    m = re.search(r'<([^>]+)>;\s*rel="last"', headers)
    last_url = m.group(1) if m else None
    return body, last_url


def count_paged(path, key):
    """Page through until no rel=next; return (total, last_page)."""
    total = 0
    page = 1
    last_page = 1
    while page <= 30:
        body, last_url = raw_api(f"{path}?per_page=100&page={page}")
        if not body:
            break
        try:
            items = json.loads(body)
        except Exception:  # noqa: BLE001
            break
        if not isinstance(items, list):
            break
        total += len(items)
        if last_url:
            m = re.search(r"page=(\d+)", last_url)
            if m:
                last_page = int(m.group(1))
        if len(items) < 100:
            break
        page += 1
    return total, last_page


def probe(full):
    tags, tpages = count_paged(f"repos/{full}/tags", "tags")
    rels, rpages = count_paged(f"repos/{full}/releases", "releases")
    return {
        "repo": full,
        "true_tags": tags,
        "tag_pages": tpages,
        "true_releases": rels,
        "release_pages": rpages,
        "tags_minus_releases": tags - rels,
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(probe, REPOS):
            out.append(r)
            print(f"{r['repo']:42s} tags={r['true_tags']:>5} (pages={r['tag_pages']:>2}) "
                  f"releases={r['true_releases']:>4} (pages={r['release_pages']:>2}) "
                  f"gap={r['tags_minus_releases']:+}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
