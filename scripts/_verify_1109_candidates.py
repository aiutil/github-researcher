#!/usr/bin/env python3
"""Verify 11-08-window counterexamples + LiveWall subs anomaly."""
import hashlib
import json
import os
import subprocess
import time
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
KNOWN = {"e18f025c87b71b9fe481f53ac6e8235d": "FARM .gitignore",
         "8470fd5b911eacd63327be59d2562f16": "FARM helpers.py",
         "258a0f5edf5d42288cfc1866497dc7dd": "FARM initial.html"}


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
    "ServantSieve/Roblox-Account-Manager-Multi-Account-Tool",
    "Manaclenodisconnect/Lichii-Enhanced",
    "finriderradial/Bunny-Hop-Script",
    "MuseumCassowaryCarve/twitch-drops-miner",
    "RapidSailorFreeze/studsmith",
]

print("=== 11-08-window candidate farm check (md5 fingerprints) ===")
for full in TARGETS:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        print(f"  {full}: tree failed")
        continue
    blobs = [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    print(f"\n  -- {full} ({len(blobs)} files)")
    for p, s in sorted(blobs):
        c = raw(full, p)
        h = hashlib.md5(c.encode("utf-8", "replace")).hexdigest() if c else "n/a"
        tag = KNOWN.get(h, "")
        print(f"       {s:>8} md5={h}  {p}   {tag}")
        time.sleep(0.08)
    rm = raw(full, "README.md")
    cta = [ln.strip()[:80] for ln in rm.splitlines() if "star the repo" in ln.lower()]
    tech = [ln.strip()[:100] for ln in rm.splitlines()
            if ln.strip().startswith(("**Core:**", "**Server:**", "**UI:", "- **Core:", "Core:"))]
    print(f"       CTA({len(cta)}): {cta[:1]}")
    print(f"       TECH: {tech[:3]}")
    time.sleep(0.15)

print("\n=== LiveWall: subs > stars anomaly ===")
lw = "elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop"
m = api(f"repos/{lw}")
j = json.loads(m)
for k in ["stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
          "size", "language", "created_at", "pushed_at", "watchers_count"]:
    print(f"  {k:22s} = {j.get(k)}")
t = api(f"repos/{lw}/git/trees/HEAD?recursive=1")
j2 = json.loads(t)
print("  files:", [(e["path"], e.get("size")) for e in j2.get("tree", []) if e.get("type") == "blob"])
print("  releases:", len(json.loads(api(f"repos/{lw}/releases") or "[]")))
print("  contributors:", len(json.loads(api(f"repos/{lw}/contributors") or "[]")))
print("\n  --- README ---")
print(raw(lw, "README.md")[:2600])

print("\n=== window-defender.cc farm: repo tree shape (11-09 window sample) ===")
for f in ["updatesealeradicate/start11", "OnyxAmbassador/actual-multiplie-monitors"]:
    t = api(f"repos/{f}/git/trees/HEAD?recursive=1")
    j3 = json.loads(t)
    print(f"  {f}: {[(e['path'], e.get('size')) for e in j3.get('tree', []) if e.get('type')=='blob']}")
    c = api(f"repos/{f}/commits")
    try:
        arr = json.loads(c)
        for cm in arr:
            au = (cm.get("commit") or {}).get("author") or {}
            print(f"      {au.get('date')}  {((cm.get('commit') or {}).get('message') or '').splitlines()[0][:70]}")
    except Exception:
        pass
