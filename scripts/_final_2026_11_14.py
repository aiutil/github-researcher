#!/usr/bin/env python3
"""Final evidence: high-subs cluster release assets + cubase cpp identity."""
import hashlib
import json
import os
import subprocess

ENV = dict(os.environ, HOME="/home/lohasle")


def js(p):
    r = subprocess.run(["gh", "api", p], capture_output=True, text=True, env=ENV, timeout=120)
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


def raw(p):
    r = subprocess.run(["gh", "api", p, "-H", "Accept: application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV, timeout=120)
    return r.stdout if r.returncode == 0 else None


HIGH = [
    ("DimensionRobin/rob-run-private-cheat", 68, 202),
    ("prismarmorergirder/wallet-security-checker", 50, 115),
    ("summittypeplay/sims4-updater", 24, 226),
    ("Crateryeexpiate/TradePilot", 24, 184),
    ("Beachfromgate/Wallet-Hunter", 24, 179),
    ("Logosheshow47/crypto-panic", 24, 177),
    ("Hairzenexalt/Fragment-Sniper", 24, 170),
]

print("=== high-subs cluster: releases / downloads / blob count ===")
for full, subs, stars in HIGH:
    rels = js(f"repos/{full}/releases") or []
    dl = sum(a.get("download_count", 0) for r in rels for a in r.get("assets", []))
    assets = [(a["name"], a["size"], a.get("download_count")) for r in rels for a in r.get("assets", [])]
    t = js(f"repos/{full}/git/trees/main?recursive=1") or {}
    blobs = [e for e in t.get("tree", []) if e["type"] == "blob"]
    code = [e for e in blobs if e["path"].split(".")[-1].lower() in
            ("py", "js", "ts", "tsx", "go", "rs", "c", "cpp", "java", "kt", "sh", "rb", "php", "cs")]
    print(f"  {full}")
    print(f"      subs={subs} stars={stars} blobs={len(blobs)} code_files={len(code)} releases={len(rels)} total_downloads={dl}")
    if assets:
        print(f"      assets: {assets}")
    if code:
        print(f"      code files: {[(e['path'], e.get('size')) for e in code]}")

print("\n=== cubase-studio-desktop: cpp identity vs the other 16 ===")
for f in ["docs/files/main.cpp", "docs/files/util.cpp", "docs/files/platform.cpp"]:
    c = raw(f"repos/ariamitchell54/cubase-studio-desktop/contents/{f}")
    print(f"  {f}: md5={hashlib.md5((c or '').encode()).hexdigest() if c else None} len={len(c) if c else 0}")
print("  (compare: files/main.cpp md5=3e9f262e7f7646e89b4bdd87befb4ada across the other 16)")

print("\n=== owner placeholder repos (full listing) ===")
for o in ["DimensionRobin", "prismarmorergirder", "summittypeplay", "Crateryeexpiate",
          "Beachfromgate", "Logosheshow47", "Hairzenexalt"]:
    u = js(f"users/{o}")
    rs = js(f"users/{o}/repos?per_page=20") or []
    print(f"  {o}: created={u.get('created_at')} repos={u.get('public_repos')} followers={u.get('followers')}")
    for r in rs:
        print(f"      {r['name']:<26} {r['stargazers_count']:>4}⭐ created={r['created_at'][:19]} size={r['size']}KB lang={r.get('language')}")
