#!/usr/bin/env python3
"""Is the 5-repo Rust utility cluster one codebase cloned N times?

Probes the shared paths and reports md5 + the first divergent line.
Also checks the 11-06 farm fingerprints (e18f025c... / 8470fd5b...) against
today's 279-281* cluster.
"""
import hashlib
import json
import os
import subprocess
import time
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    return p.stdout if p.returncode == 0 else None


def raw_file(full, path_):
    t = api(f"repos/{full}/contents/{path_}", headers=["Accept: application/vnd.github.raw"])
    return t or ""


RUST = ["PlateParrotTerminal/lag-doctor", "ToneProtectorSolve48/drift-doctor",
        "AmbassadorTassel/omnigear-peripheral-manager",
        "majestydamseldecoder/truestretch-stretched-resolution",
        "Avalanchevonproxy69/fanatic-laptop-control"]

SHARED = ["src/app.rs", "src/theme.rs", "src/widgets.rs", "src/main.rs",
          "import.json", "docs/design/banner.html", "docs/design/mockup.html",
          ".gitignore", ".gitattributes", "LICENSE", "Cargo.toml"]

print("=== SHARED-PATH md5 ACROSS THE 5 RUST UTILITIES ===")
per_path = defaultdict(dict)
for full in RUST:
    for p in SHARED:
        c = raw_file(full, p)
        per_path[p][full] = hashlib.md5(c.encode("utf-8", "replace")).hexdigest() if c else "MISSING"
        time.sleep(0.08)
for p in SHARED:
    hs = per_path[p]
    c = Counter(hs.values())
    print(f"\n  {p}   distinct={len(c)}")
    for h, n in c.most_common():
        who = [f.split('/')[0] for f, hh in hs.items() if hh == h]
        print(f"     {h}  x{n}  {who}")

# show the divergent part of src/app.rs if it differs
print("\n=== src/app.rs : first differing line between two repos ===")
a = raw_file(RUST[0], "src/app.rs").splitlines()
b = raw_file(RUST[1], "src/app.rs").splitlines()
print(f"  {RUST[0]} lines={len(a)}   {RUST[1]} lines={len(b)}")
shown = 0
for i in range(min(len(a), len(b))):
    if a[i] != b[i]:
        print(f"   L{i+1}:")
        print(f"     A: {a[i][:150]}")
        print(f"     B: {b[i][:150]}")
        shown += 1
        if shown >= 6:
            break
if shown == 0:
    print("   (identical over common prefix)")

print("\n=== import.json (full) from lag-doctor ===")
print(raw_file(RUST[0], "import.json")[:900])

print("\n=== .gitignore (full) from lag-doctor ===")
print(raw_file(RUST[0], ".gitignore"))

print("\n=== TODAY: 279-281* cluster vs KNOWN 11-06 farm fingerprints ===")
KNOWN = {"e18f025c87b71b9fe481f53ac6e8235d": "11-06/11-07 FARM .gitignore",
         "8470fd5b911eacd63327be59d2562f16": "11-06/11-07 FARM helpers.py",
         "258a0f5edf5d42288cfc1866497dc7dd": "11-08 FARM initial.html"}
CLUSTER = ["Nanoutrolley/roblox-studio-mcp", "Sectionsereclaim/discord-auto-quest",
           "ridgecobblerslide/windows-animated-wallpapers",
           "TameCarpenterEstate/Roblox-FPS-Optimizer",
           "Platoonritomb/Fortnite-FPS-Booster-Performance-Optimizer"]
for full in CLUSTER:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        print(f"  {full}: tree failed")
        continue
    blobs = [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    print(f"\n  -- {full} ({len(blobs)} files)")
    hits = []
    for p, s in sorted(blobs):
        c = raw_file(full, p)
        h = hashlib.md5(c.encode("utf-8", "replace")).hexdigest() if c else "n/a"
        tag = KNOWN.get(h, "")
        if tag:
            hits.append((p, h, tag))
        print(f"       {s:>8}  md5={h}  {p}   {tag}")
        time.sleep(0.08)
    print(f"     >>> KNOWN-FARM FINGERPRINT MATCHES: {hits}")
    time.sleep(0.15)
