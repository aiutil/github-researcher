#!/usr/bin/env python3
"""Structural comparison of the Rust Windows-utility cluster + fork timing."""

import difflib
import json
import os
import subprocess
import sys
import time
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
RUST = [
    "PlateParrotTerminal/lag-doctor",
    "AmbassadorTassel/omnigear-peripheral-manager",
    "ToneProtectorSolve48/drift-doctor",
    "majestydamseldecoder/truestretch-stretched-resolution",
    "Avalanchevonproxy69/fanatic-laptop-control",
    "basinshinobiend/wow-undercut-sniper",
    "AutocratMinaret/valorant-ai-clip-editor",
]
OTHER = ["elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop"]


def api(path, raw=True, params=None):
    url = path
    if params:
        url = path + "?" + params
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github.raw", url]
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=90)
    if p.returncode != 0:
        return None
    return p.stdout


print("=== RUST CLUSTER: identical file PATHS across repos ===")
trees = {}
for full in RUST:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        print(f"  {full}: tree fetch failed")
        continue
    trees[full] = {x["path"]: x.get("size") for x in j.get("tree", []) if x.get("type") == "blob"}
    time.sleep(0.3)

paths = defaultdict(list)
for full, t in trees.items():
    for p in t:
        paths[p].append(full)
print(f"  distinct file paths across {len(RUST)} repos: {len(paths)}")
print("  paths present in ALL repos:")
for p, rs in sorted(paths.items()):
    if len(rs) == len(RUST):
        print(f"    {p}")

print("\n=== RUST CLUSTER: similarity ratio of same-path files (lag-doctor as base) ===")
base = RUST[0]
for other in RUST[1:]:
    common = [p for p in paths if len(paths[p]) == len(RUST)]
    ratios = []
    for p in common:
        if not p.endswith(".rs") and not p.endswith(".html"):
            continue
        a = api(f"repos/{base}/contents/{p}")
        b = api(f"repos/{other}/contents/{p}")
        if a is None or b is None:
            continue
        r = difflib.SequenceMatcher(None, a, b).quick_ratio()
        ratios.append((p, r))
        time.sleep(0.2)
    if ratios:
        avg = sum(r for _, r in ratios) / len(ratios)
        print(f"  {other:50s} avg_quick_ratio={avg:.3f}  files={len(ratios)}")
        for p, r in sorted(ratios, key=lambda x: -x[1])[:4]:
            print(f"      {r:.3f}  {p}")

print("\n=== FORK TIMING (all pages) ===")
for full in RUST + OTHER:
    ts = []
    for page in range(1, 6):
        r = api(f"repos/{full}/forks", params=f"per_page=100&sort=newest&page={page}")
        try:
            j = json.loads(r)
        except Exception:
            break
        if not isinstance(j, list) or not j:
            break
        ts.extend(f["created_at"] for f in j)
        if len(j) < 100:
            break
        time.sleep(0.3)
    if not ts:
        print(f"  {full}: no forks")
        continue
    ts.sort()
    gaps = []
    for i in range(1, len(ts)):
        a = time.mktime(time.strptime(ts[i - 1][:19], "%Y-%m-%dT%H:%M:%S"))
        b = time.mktime(time.strptime(ts[i][:19], "%Y-%m-%dT%H:%M:%S"))
        gaps.append(b - a)
    gaps.sort()
    med = gaps[len(gaps) // 2] if gaps else -1
    le10 = sum(1 for g in gaps if g <= 10) / len(gaps) * 100 if gaps else 0
    print(f"  {full}")
    print(f"      n_forks={len(ts)} first={ts[0]} last={ts[-1]} span={(ts[-1][:19])}")
    print(f"      median_gap={med:.0f}s  pct_gaps<=10s={le10:.1f}%")
    if len(ts) <= 40:
        print(f"      all forks: {[t[11:19] for t in ts]}")
    time.sleep(0.3)
