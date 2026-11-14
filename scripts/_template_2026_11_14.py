#!/usr/bin/env python3
"""Prove the -desktop family shares ONE README template with only the product name varied,
and print the structural fingerprint of the farm families' payloads."""
import hashlib
import json
import os
import re
import subprocess
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def raw(p):
    r = subprocess.run(["gh", "api", p, "-H", "Accept: application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV, timeout=120)
    return r.stdout if r.returncode == 0 else ""


def js(p):
    r = subprocess.run(["gh", "api", p], capture_output=True, text=True, env=ENV, timeout=120)
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


DESK = [
    "ariamitchell54/cubase-studio-desktop", "ben-miller-23/dxo-photolab-10-desktop",
    "amber-lance-72/xeno-roblox-desktop", "azure-teal-slope/windows-optimizer-desktop",
    "ben-cook-42/kontakt-8-desktop", "ben14-dunn/native-instruments-kontakt-desktop",
    "alex-wells-65/iobit-driver-booster-desktop", "ben-kennedy-81/xfer-serum-desktop",
    "azuresail195/wondershare-recoverit-desktop", "angela-cook-1988/vegas-pro-23-desktop",
    "azuremaple1997/coreldraw-desktop", "ava25-thompson/fishstrap-roblox-fps-booster-desktop",
    "brisk-thrush-husky/malware-defender-desktop", "bradburns2001/topaz-video-ai-desktop",
    "brave-shell-07/izotope-rx-11-desktop", "briskember13/adobe-acrobat-pdf-desktop",
    "brave-plum-co/leonardo-ai-desktop",
]

print(f"=== -desktop family: {len(DESK)} repos, template identity ===")
norm = Counter()
sizes = Counter()
for full in DESK:
    rm = raw(f"repos/{full}/readme")
    owner = full.split("/")[0]
    repo = full.split("/")[1]
    # parameterise: product name, owner slug, repo slug, dates, versions
    t = rm
    t = re.sub(r"https://[A-Za-z0-9_.-]+\.github\.io/[A-Za-z0-9_.-]+/", "https://OWNER.github.io/REPO/", t)
    t = re.sub(r"updated-\d{4}--\d{2}--\d{2}", "updated-DATE", t)
    t = re.sub(r"release-v[\d.]+", "release-vX", t)
    t = re.sub(r"#\s*[^\n]*?2026: Standalone Offline Build for Windows 11", "# PRODUCT 2026: Standalone Offline Build for Windows 11", t)
    t = re.sub(r"[A-Z][A-Za-z0-9]*(?:[ -][A-Za-z0-9]+)*? 2026", "PRODUCT 2026", t)
    t = re.sub(r"alt=\"[^\"]{0,80}?2026[^\"]{0,60}?\"", 'alt="PRODUCT 2026 alt"', t)
    h = hashlib.md5(t.encode()).hexdigest()
    norm[h] += 1
    sizes[(len(rm), h)] += 1
    print(f"  {full:<58} readme={len(rm):>6}B norm_md5={h[:12]}")

print(f"\n  distinct NORMALISED readme templates: {len(norm)}")
for k, v in norm.most_common():
    print(f"    {k[:14]} x{v}")

print("\n=== farm family payload trees (structure fingerprint) ===")
for full in ["armsworminterface/ai--manus", "WarriorRemember/IPTV_Player_2.0",
             "Topkiflare74/ai--manus2.0", "trackboatwrightplan/GitHub-Copilot-app"]:
    t = js(f"repos/{full}/git/trees/main?recursive=1")
    if not t:
        print(f"  {full}: tree unavailable")
        continue
    blobs = [e for e in t.get("tree", []) if e["type"] == "blob"]
    print(f"\n  {full}: {len(blobs)} blobs, total {sum(e.get('size',0) for e in blobs)}B")
    for e in sorted(blobs, key=lambda x: -x.get("size", 0))[:8]:
        print(f"     {e['path']:<38} {e.get('size'):>9}B")

print("\n=== -desktop shared file md5s (is it literally the same 3 cpp files?) ===")
for f in ["files/main.cpp", "files/util.cpp", "files/platform.cpp", "docs/index.html"]:
    hs = Counter()
    for full in DESK:
        c = raw(f"repos/{full}/contents/{f}")
        hs[hashlib.md5(c.encode()).hexdigest()] += 1
    print(f"  {f:<20} distinct md5 across {len(DESK)} repos: {len(hs)}  ->  {[(k[:10], v) for k, v in hs.most_common(4)]}")
