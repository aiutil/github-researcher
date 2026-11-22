#!/usr/bin/env python3
"""Release-asset truth across ALL pages (not just page 1).

For each repo: total releases, releases carrying assets, asset-count
distribution, download-count distribution (min/median/max), whether any
asset is an SBOM or a checksum file, and total release payload size.

Output: /tmp/assets_1121.json
"""
import json
import os
import re
import statistics
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/assets_1121.json"

REPOS = [
    "kajisho5/ffmpeg-skill", "GoogleChrome/modern-web-guidance-src",
    "backnotprop/plannotator", "alibaba/open-code-review",
    "firecrawl/firecrawl", "nginx/nginx", "toeverything/AFFiNE",
    "ag-ui-protocol/ag-ui", "Tracer-Cloud/opensre", "dream-num/univer",
    "meta/astryx", "XiaoYouChR/Ghost-Downloader-3", "zhouxiaoka/autoclip",
    "we-promise/sure", "obenvinotoolkit/openvino",
]


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + "&".join(f"{k}={v}" for k, v in params.items())
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


def probe(full):
    rels = []
    page = 1
    while page <= 15:
        r = api(f"repos/{full}/releases", {"per_page": 100, "page": page})
        if not isinstance(r, list) or not r:
            break
        rels.extend(r)
        if len(r) < 100:
            break
        page += 1

    n_with = 0
    n_zero = 0
    asset_counts = []
    dls = []
    has_sbom = False
    has_chk = False
    sbom_names = set()
    chk_names = set()
    total_bytes = 0
    prerelease = 0
    earliest = latest = None
    for rel in rels:
        if rel.get("prerelease"):
            prerelease += 1
        ts = rel.get("published_at") or rel.get("created_at")
        if ts:
            earliest = ts if earliest is None or ts < earliest else earliest
            latest = ts if latest is None or ts > latest else latest
        assets = rel.get("assets") or []
        asset_counts.append(len(assets))
        if assets:
            n_with += 1
        else:
            n_zero += 1
        for a in assets:
            n = (a.get("name") or "")
            dls.append(a.get("download_count") or 0)
            total_bytes += a.get("size") or 0
            low = n.lower()
            if "sbom" in low or "cyclonedx" in low or "spdx" in low:
                has_sbom = True
                sbom_names.add(n)
            if re.search(r"sha256|checksum|\.sha$|\.sig$|\.asc$", low):
                has_chk = True
                chk_names.add(n)
    return {
        "repo": full,
        "n_releases_total": len(rels),
        "prerelease": prerelease,
        "rel_with_assets": n_with,
        "rel_zero_assets": n_zero,
        "asset_count_min": min(asset_counts) if asset_counts else 0,
        "asset_count_max": max(asset_counts) if asset_counts else 0,
        "asset_count_median": statistics.median(asset_counts) if asset_counts else 0,
        "dl_min": min(dls) if dls else 0,
        "dl_median": statistics.median(dls) if dls else 0,
        "dl_max": max(dls) if dls else 0,
        "n_assets_total": len(dls),
        "total_bytes": total_bytes,
        "has_sbom": has_sbom,
        "has_checksum": has_chk,
        "sbom_names": sorted(sbom_names)[:4],
        "chk_names": sorted(chk_names)[:5],
        "earliest": earliest,
        "latest": latest,
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(probe, REPOS):
            out.append(r)
            print(f"{r['repo']:42s} rel={r['n_releases_total']:>4} "
                  f"with_assets={r['rel_with_assets']:>4} zero={r['rel_zero_assets']:>4} "
                  f"assets[{r['asset_count_min']}-{r['asset_count_max']}] "
                  f"dl[{r['dl_min']}-{r['dl_max']}] sbom={r['has_sbom']} chk={r['has_checksum']}",
                  flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
