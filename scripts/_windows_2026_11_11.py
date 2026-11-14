#!/usr/bin/env python3
"""Collect the remaining figures needed for the 2026-11-09 / 2026-11-10 / 2026-11-11 dailies.

Windows (repo convention: the daily dated D covers repos created on D-1 UTC):
  daily 2026-11-09 -> created 2026-11-08  (/tmp/cand_2026_11_09.json, n=171)
  daily 2026-11-10 -> created 2026-11-09  (/tmp/cand_2026_11_10.json, n=97)
  daily 2026-11-11 -> created 2026-11-10  (/tmp/w1111/cand_1110.json, n=77)
"""
import json
import os
import subprocess
import time
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def raw(full, path_):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github.raw", f"repos/{full}/contents/{path_}"]
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    return p.stdout if p.returncode == 0 else ""


def repo(full):
    return api(f"repos/{full}") or {}


def owner_info(login):
    u = api(f"users/{login}") or {}
    return (u.get("created_at"), u.get("public_repos"), u.get("followers"))


# ---------- 1. per-window distribution ----------
WINDOWS = [
    ("2026-11-08", "/tmp/cand_2026_11_09.json", "daily 2026-11-09"),
    ("2026-11-09", "/tmp/cand_2026_11_10.json", "daily 2026-11-10"),
    ("2026-11-10", "/tmp/w1111/cand_1110.json", "daily 2026-11-11"),
]

print("=" * 100)
print("=== 1. WINDOW DISTRIBUTIONS ===")
for day, path, label in WINDOWS:
    rows = json.load(open(path))
    empty = sum(1 for r in rows if r["readme_len"] == 0)
    tiny = sum(1 for r in rows if (r["size_kb"] or 0) <= 20)
    zerof = sum(1 for r in rows if (r["forks"] or 0) == 0)
    oneblob = None
    payload = sum(1 for r in rows if r.get("hit_irm") or r.get("hit_invoke_expression"))
    stars = Counter(r["stars"] for r in rows)
    dup = [(v, c) for v, c in sorted(stars.items(), key=lambda x: (-x[1], -x[0])) if c >= 2][:8]
    print(f"\n  {label}  (created {day})  n={len(rows)}")
    print(f"    readme_len==0        : {empty} ({empty/len(rows)*100:.1f}%)")
    print(f"    size<=20KB           : {tiny} ({tiny/len(rows)*100:.1f}%)")
    print(f"    forks==0             : {zerof} ({zerof/len(rows)*100:.1f}%)")
    print(f"    payload hit (irm/Invoke): {payload} ({payload/len(rows)*100:.1f}%)")
    print(f"    top duplicate star values: {dup}")
    nolic = sum(1 for r in rows if not r["license"])
    print(f"    no license           : {nolic} ({nolic/len(rows)*100:.1f}%)")
    c1 = sum(1 for r in rows if r["ncommits"] == 1)
    print(f"    exactly 1 commit     : {c1} ({c1/len(rows)*100:.1f}%)")

# ---------- 2. key project metadata for the three dailies ----------
KEY = {
    "daily 2026-11-09": [
        "elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop",
        "PlateParrotTerminal/lag-doctor",
        "ToneProtectorSolve48/drift-doctor",
        "wrencanfly/research-loop-skills",
        "jhaizhou-ops/S2Arm",
        "danyuchn/claude-work-mode",
    ],
    "daily 2026-11-10": [
        "huamidev/GestaltX",
        "rippelz/rustudio",
        "yetone/rewind-for-x",
        "bookleme/bookleme",
        "TameCarpenterEstate/Roblox-FPS-Optimizer",
        "Nanoutrolley/roblox-studio-mcp",
    ],
    "daily 2026-11-11": [
        "Kianuni/Erosion-CN",
        "ValidatorStack/solana-vigil",
        "2SinceJuly/SkyDot",
        "bea4dev/shoji-bar-4",
        "egoist/tinytraffic",
        "SwitchRECOMP-Dev/Switch2RECOMP",
        "AngleCentipede/ifunbox",
        "crewbookkeepercastle/trx-drainer-bot",
    ],
}

print("\n" + "=" * 100)
print("=== 2. KEY PROJECT METADATA ===")
for label, targets in KEY.items():
    print(f"\n--- {label} ---")
    for full in targets:
        m = repo(full)
        if not m:
            print(f"  {full}: FETCH FAILED")
            continue
        lic = m.get("license") or {}
        ow = m.get("owner") or {}
        oc, orp, ofl = owner_info(ow.get("login"))
        t = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
        blobs = [e for e in t.get("tree", []) if e.get("type") == "blob"]
        c = api(f"repos/{full}/commits?per_page=100") or []
        contrib = api(f"repos/{full}/contributors") or []
        rel = api(f"repos/{full}/releases") or []
        secs = set()
        for cm in (c if isinstance(c, list) else []):
            au = (cm.get("commit") or {}).get("author") or {}
            if au.get("date"):
                secs.add(au["date"][-2:])
        print(f"  {full}")
        print(f"    stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} "
              f"oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} "
              f"lic={lic.get('spdx_id')} blobs={len(blobs)} commits={len(c) if isinstance(c,list) else '?'} "
              f"sec_entropy={len(secs)} contrib={len(contrib) if isinstance(contrib,list) else '?'} "
              f"releases={len(rel) if isinstance(rel,list) else '?'}")
        print(f"    created={m.get('created_at')} pushed={m.get('pushed_at')} owner={ow.get('login')}"
              f"({ow.get('type')}) owner_created={oc} owner_repos={orp} owner_followers={ofl}")
        print(f"    topics={m.get('topics')}")
        print(f"    desc={m.get('description')}")
        time.sleep(0.25)
