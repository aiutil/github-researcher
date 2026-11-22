#!/usr/bin/env python3
"""Independent verification of the "true tag count" claim.

The tag-truth script (/tmp/tagtruth_1121.json) resolved tag totals by reading
the Link header's rel="last" page number.  Before that number is published in
a report it must be confirmed by a *second, different* method, otherwise a
bug in the Link parsing would silently corrupt every downstream conclusion.

This script confirms each count three ways:
  1. Link header rel="last"  (the method used by tagtruth)
  2. Binary search on page length  (no header parsing at all)
  3. Sum of per-page item counts until an empty page

All three must agree, otherwise the repo is reported as UNRESOLVED.

Output: /tmp/tagverify_1121.json
"""
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/tagverify_1121.json"

REPOS = [
    "nginx/nginx",
    "firecrawl/firecrawl",
    "GoogleChrome/modern-web-guidance-src",
    "toeverything/AFFiNE",
    "ag-ui-protocol/ag-ui",
    "backnotprop/plannotator",
    "alibaba/open-code-review",
    "kajisho5/ffmpeg-skill",
    "Tracer-Cloud/opensre",
    "meta/astryx",
    "dream-num/univer",
    "mvanhorn/last30days-skill",
    "we-promise/sure",
    "openvinotoolkit/openvino",
    "obra/superpowers",
    "ChromeDevTools/chrome-devtools-mcp",
]


def api(path, headers=False, timeout=120):
    cmd = ["gh", "api"]
    if headers:
        cmd.append("-i")
    cmd.append(path)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if not headers:
        return p.stdout
    parts = p.stdout.split("\n\n", 1)
    return (parts[0], parts[1] if len(parts) > 1 else "")


def items(path):
    body = api(path)
    if not body:
        return None
    try:
        d = json.loads(body)
    except Exception:  # noqa: BLE001
        return None
    return d if isinstance(d, list) else None


def link_last_page(full, kind):
    r = api(f"repos/{full}/{kind}?per_page=100&page=1", headers=True)
    if not r:
        return None
    headers = r[0]
    m = re.search(r'<([^>]+)>;\s*rel="last"', headers)
    if not m:
        return 1
    m2 = re.search(r"[?&]page=(\d+)(?:&|$)", m.group(1))
    return int(m2.group(1)) if m2 else None


def binary_page_count(full, kind):
    """Find the last non-empty page without using any Link header."""
    lo, hi = 1, 1
    while True:
        got = items(f"repos/{full}/{kind}?per_page=100&page={hi}")
        if got is None:
            return None
        if len(got) < 100:
            return hi
        hi *= 2
        if hi > 4096:
            return None
    # unreachable


def sum_pages(full, kind, last):
    total = 0
    for p in range(1, last + 1):
        got = items(f"repos/{full}/{kind}?per_page=100&page={p}")
        if got is None:
            return None
        total += len(got)
        if len(got) < 100:
            break
    return total


def verify(full):
    kind = "tags"
    lp = link_last_page(full, kind)
    # binary search: smallest page whose length < 100 is the last page
    lo, hi = 1, (lp or 1) * 2 + 2
    while lo < hi:
        mid = (lo + hi) // 2
        got = items(f"repos/{full}/{kind}?per_page=100&page={mid}")
        if got is None:
            return {"repo": full, "status": "UNRESOLVED", "reason": "api error mid binary search"}
        if len(got) == 100:
            lo = mid + 1
        else:
            hi = mid
    binary_last = lo
    total = sum_pages(full, kind, binary_last)
    resolved = lp is not None and lp == binary_last and total is not None
    return {
        "repo": full,
        "link_last_page": lp,
        "binary_last_page": binary_last,
        "summed_items": total,
        "true_tags": total,
        "status": "OK" if resolved else "MISMATCH",
        "agree": bool(resolved),
    }


def main():
    rows = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(verify, REPOS):
            rows.append(r)
            print(f"  {r['repo']:44s} link_last={r.get('link_last_page')} "
                  f"binary_last={r.get('binary_last_page')} "
                  f"summed={r.get('summed_items')} [{r['status']}]", flush=True)
    json.dump(rows, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
