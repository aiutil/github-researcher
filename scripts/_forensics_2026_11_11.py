#!/usr/bin/env python3
"""Forensics for the 2026-11-10 window (data window of daily/2026-11-11.md).

Covers:
  A. tree + README md5 + payload line for the 1 KB shell cluster
  B. fork-arrival timing for substantive projects
  C. deep dive (meta/tree/commits/contributors/releases/README) for chosen targets
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_, headers=None, raw=False):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def raw_file(full, path_):
    return api(f"repos/{full}/contents/{path_}", headers=["Accept: application/vnd.github.raw"], raw=True) or ""


def md5(s):
    return hashlib.md5(s.encode("utf-8", "replace")).hexdigest()


def fork_timing(full, sample=30):
    """Sample fork creation timestamps; report median gap + <=10s share."""
    forks = api(f"repos/{full}/forks?per_page=100&sort=newest")
    if not forks or not isinstance(forks, list):
        return None
    ts = []
    for f in forks[:sample]:
        c = f.get("created_at")
        if c:
            ts.append(datetime.fromisoformat(c.replace("Z", "+00:00")))
    ts.sort()
    if len(ts) < 2:
        return {"n": len(ts), "med": None, "le10": None, "span_min": None}
    gaps = sorted((ts[i + 1] - ts[i]).total_seconds() for i in range(len(ts) - 1))
    med = gaps[len(gaps) // 2]
    le10 = sum(1 for g in gaps if g <= 10)
    span = (ts[-1] - ts[0]).total_seconds() / 60
    return {"n": len(ts), "med": med, "le10": le10, "ngaps": len(gaps), "span_min": round(span, 1)}


MODE = sys.argv[1] if len(sys.argv) > 1 else "all"

SHELL_SAMPLES = [
    "AngleCentipede/ifunbox",
    "crewbookkeepercastle/trx-drainer-bot",
    "Cordkushelter78/tenorshare-4ukey",
    "Tremorfualembic30/whale-tracker",
    "ChainDistributor/photo-commander",
    "VarnishBakerTrek/claude-jailbreak-prompt",
    "UpgradeHorse/canva-pro",
    "RobustAI24/Autocad-For-Windows",
]

REAL_TARGETS = [
    "Kianuni/Erosion-CN",
    "ValidatorStack/solana-vigil",
    "2SinceJuly/SkyDot",
    "bea4dev/shoji-bar-4",
    "egoist/tinytraffic",
    "SwitchRECOMP-Dev/Switch2RECOMP",
    "JDhruv14/line-art-animation",
    "simplexai-labs/linger",
]

if MODE in ("all", "shells"):
    print("#" * 100)
    print("=== A. 1KB SHELL CLUSTER: tree / README fingerprint / payload line ===")
    readme_md5s = Counter()
    payload_hits = Counter()
    for full in SHELL_SAMPLES:
        print("=" * 90)
        print(f"### {full}")
        t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
        if isinstance(t, dict):
            blobs = [(e["path"], e.get("size")) for e in t.get("tree", []) if e.get("type") == "blob"]
            print(f"  blobs={len(blobs)}  {blobs}")
        c = api(f"repos/{full}/commits?per_page=100")
        if isinstance(c, list):
            for cm in c[:4]:
                au = (cm.get("commit") or {}).get("author") or {}
                print(f"  commit {au.get('date')}  {((cm.get('commit') or {}).get('message') or '').splitlines()[0][:80]}")
        rm = raw_file(full, "README.md")
        print(f"  README len={len(rm)} md5={md5(rm)}")
        readme_md5s[md5(rm)] += 1
        for line in rm.splitlines():
            ls = line.strip()
            if ls.startswith("irm ") or "Invoke-Expression" in ls or "gcm i*x" in ls or "windows-defender.cc" in ls or "git-software.cc" in ls:
                payload_hits[ls[:120]] += 1
        print("  --- README full ---")
        print(rm)
    print("\n=== A2. distinct README md5 ===")
    for m, cnt in readme_md5s.most_common():
        print(f"  md5={m}  count={cnt}")
    print("=== A3. payload lines ===")
    for p, cnt in payload_hits.most_common():
        print(f"  {cnt}x  {p}")

if MODE in ("all", "forks"):
    print("\n" + "#" * 100)
    print("=== B. FORK ARRIVAL TIMING (substantive candidates) ===")
    for full in REAL_TARGETS:
        ft = fork_timing(full)
        m = api(f"repos/{full}") or {}
        if ft:
            print(f"  {full:44s} stars={m.get('stargazers_count'):>5} forks={m.get('forks_count'):>4} "
                  f"sampled={ft['n']:>3} med_gap={ft['med']} le10={ft['le10']}/{ft.get('ngaps')} span={ft['span_min']}min")
        else:
            print(f"  {full:44s} fork fetch failed (forks={m.get('forks_count')})")
        time.sleep(0.2)

if MODE in ("all", "deep"):
    print("\n" + "#" * 100)
    print("=== C. DEEP DIVE ===")
    for full in REAL_TARGETS:
        print("=" * 90)
        print(f"### {full}")
        m = api(f"repos/{full}")
        if not m:
            print("  fetch failed")
            continue
        for k in ["stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
                  "size", "language", "created_at", "pushed_at", "default_branch", "archived", "homepage"]:
            print(f"  {k:22s} = {m.get(k)}")
        lic = m.get("license") or {}
        print(f"  {'license.spdx':22s} = {lic.get('spdx_id')} / {lic.get('name')}")
        print(f"  {'topics':22s} = {m.get('topics')}")
        print(f"  {'description':22s} = {m.get('description')}")
        ow = m.get("owner") or {}
        print(f"  {'owner.type':22s} = {ow.get('type')}")
        u = api(f"users/{ow.get('login')}") or {}
        print(f"  {'owner.created':22s} = {u.get('created_at')} public_repos={u.get('public_repos')} followers={u.get('followers')}")
        t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
        if isinstance(t, dict):
            blobs = sorted([(e.get("size") or 0, e["path"]) for e in t.get("tree", []) if e.get("type") == "blob"])
            print(f"  -- TREE ({len(blobs)} blobs) --")
            for s, p in blobs[:30]:
                print(f"      {s:>9}  {p}")
            if len(blobs) > 30:
                print(f"      ... +{len(blobs)-30} more")
        c = api(f"repos/{full}/commits?per_page=100")
        if isinstance(c, list):
            print(f"  -- COMMITS (page1={len(c)}) --")
            for cm in c[:10]:
                au = (cm.get("commit") or {}).get("author") or {}
                print(f"      {au.get('date')}  {((cm.get('commit') or {}).get('message') or '').splitlines()[0][:88]}")
        for ep in ["contributors", "releases"]:
            arr = api(f"repos/{full}/{ep}")
            if isinstance(arr, list):
                if ep == "contributors":
                    print(f"  contributors={len(arr)} :: " + ", ".join(f"{a.get('login')}({a.get('contributions')})" for a in arr[:8]))
                else:
                    print(f"  releases={len(arr)} :: " + ", ".join(a.get("tag_name", "?") for a in arr[:10]))
        rm = raw_file(full, "README.md")
        print(f"  -- README (len={len(rm)}) --")
        print(rm[:2600])
        time.sleep(0.3)
