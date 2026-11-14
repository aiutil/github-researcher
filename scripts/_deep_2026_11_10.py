#!/usr/bin/env python3
"""Deep evidence for the projects that will be profiled in daily/2026-11-10.md."""
import json
import os
import subprocess
import time
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    return p.stdout if p.returncode == 0 else None


def raw(full, path_):
    return api(f"repos/{full}/contents/{path_}", headers=["Accept: application/vnd.github.raw"]) or ""


TARGETS = [
    "huamidev/GestaltX",
    "yetone/rewind-for-x",
    "TameCarpenterEstate/Roblox-FPS-Optimizer",
    "rippelz/rustudio",
    "FJNB5/fujiang-pojia",
    "bookleme/bookleme",
]

for full in TARGETS:
    print("=" * 100)
    print(f"### {full}")
    m = api(f"repos/{full}")
    try:
        j = json.loads(m)
    except Exception:
        print("  repo fetch failed")
        continue
    for k in ["stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
              "size", "language", "created_at", "pushed_at", "default_branch", "archived"]:
        print(f"  {k:22s} = {j.get(k)}")
    lic = j.get("license") or {}
    print(f"  {'license.spdx':22s} = {lic.get('spdx_id')} / {lic.get('name')}")
    print(f"  {'topics':22s} = {j.get('topics')}")
    print(f"  {'description':22s} = {j.get('description')}")
    print(f"  {'homepage':22s} = {j.get('homepage')}")
    ow = j.get("owner") or {}
    print(f"  {'owner.type':22s} = {ow.get('type')}")
    u = api(f"users/{ow.get('login')}")
    try:
        uj = json.loads(u)
        print(f"  {'owner.created':22s} = {uj.get('created_at')}  public_repos={uj.get('public_repos')}  followers={uj.get('followers')}")
    except Exception:
        print("  owner fetch failed")

    print("  -- TREE --")
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        tj = json.loads(t)
        blobs = [(e["path"], e.get("size")) for e in tj.get("tree", []) if e.get("type") == "blob"]
        print(f"     {len(blobs)} blobs")
        for p, s in sorted(blobs)[:40]:
            print(f"       {s:>9}  {p}")
        if len(blobs) > 40:
            print(f"       ... +{len(blobs)-40} more")
    except Exception:
        print("     tree failed")

    print("  -- COMMITS --")
    c = api(f"repos/{full}/commits?per_page=100")
    try:
        arr = json.loads(c)
        for cm in arr[:12]:
            au = (cm.get("commit") or {}).get("author") or {}
            print(f"       {au.get('date')}  {((cm.get('commit') or {}).get('message') or '').splitlines()[0][:90]}")
        print(f"       (page1={len(arr)})")
    except Exception:
        print("     commits failed")

    print("  -- CONTRIBUTORS / RELEASES --")
    for ep in ["contributors", "releases"]:
        r = api(f"repos/{full}/{ep}")
        try:
            arr = json.loads(r)
            if ep == "contributors":
                print(f"     contributors={len(arr)} :: " + ", ".join(
                    f"{a.get('login')}({a.get('contributions')})" for a in arr[:8]))
            else:
                print(f"     releases={len(arr)} :: " + ", ".join(a.get("tag_name", "?") for a in arr[:10]))
        except Exception:
            print(f"     {ep} failed")

    print("  -- README (first 3200 chars) --")
    rm = raw(full, "README.md")
    print(rm[:3200])
    print(f"  [README len={len(rm)}]")
    time.sleep(0.3)
