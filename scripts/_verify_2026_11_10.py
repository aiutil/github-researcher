#!/usr/bin/env python3
"""Final verification for daily/2026-11-10.md claims."""
import json
import os
import re
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


def fork_timing(full, label=""):
    t = api(f"repos/{full}/forks")
    try:
        arr = json.loads(t)
    except Exception:
        return f"  {full[:44]:46s} fork fetch failed"
    ts = sorted(a.get("created_at") for a in arr if a.get("created_at"))
    if len(ts) < 2:
        return f"  {full[:44]:46s} sampled={len(ts)}"
    gaps = []
    for i in range(1, len(ts)):
        a = datetime.fromisoformat(ts[i - 1].replace("Z", "+00:00"))
        b = datetime.fromisoformat(ts[i].replace("Z", "+00:00"))
        gaps.append((b - a).total_seconds())
    gs = sorted(gaps)
    med = gs[len(gs) // 2]
    le10 = sum(1 for g in gaps if g <= 10)
    span = (datetime.fromisoformat(ts[-1].replace("Z", "+00:00"))
            - datetime.fromisoformat(ts[0].replace("Z", "+00:00"))).total_seconds() / 60
    return (f"  {full[:44]:46s} sampled={len(ts):>3} med_gap={med:>7.1f}s "
            f"le10={le10}/{len(gaps)} span={span:.1f}min  {label}")


print("=== 1. huamidev/GestaltX fork timing (is 1364* organic?) ===")
print(fork_timing("huamidev/GestaltX", "<-- 1364* 515 forks"))
time.sleep(0.2)
print(fork_timing("yetone/rewind-for-x", "<-- 221* 7 forks"))
time.sleep(0.2)
print(fork_timing("rippelz/rustudio", "<-- 72* 9 forks"))
time.sleep(0.2)
print(fork_timing("bookleme/bookleme", "<-- 37* 0 forks"))
time.sleep(0.2)
print(fork_timing("FJNB5/fujiang-pojia", "<-- 277* 168 forks"))

print("\n=== 2. roblox-studio-mcp README: tech-stack vs repo reality ===")
rm = raw("Nanoutrolley/roblox-studio-mcp", "README.md")
for ln in rm.splitlines():
    if any(k in ln for k in ["Tech Stack", "Core:", "Server:", "MCP", "Node", "Python", "TypeScript"]):
        print("   ", ln[:170])
print("   --- tree ---")
t = api("repos/Nanoutrolley/roblox-studio-mcp/git/trees/HEAD?recursive=1")
j = json.loads(t)
print("   files:", [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"])

print("\n=== 3. Roblox-FPS-Optimizer: self-contradiction lines ===")
rm2 = raw("TameCarpenterEstate/Roblox-FPS-Optimizer", "README.md")
for ln in rm2.splitlines():
    if any(k in ln for k in ["does not inject", "inject", "telegra.ph", "Core_Update_Pack",
                             "ProjectFiles.exe", "Core:", "UI:", "ban risk", "does not interact"]):
        print("   ", ln.strip()[:190])

print("\n=== 4. Roblox-FPS-Optimizer main.py / helpers.py full source ===")
print("   --- helpers.py ---")
print(raw("TameCarpenterEstate/Roblox-FPS-Optimizer", "helpers.py"))
print("   --- main.py ---")
print(raw("TameCarpenterEstate/Roblox-FPS-Optimizer", "main.py"))

print("\n=== 5. roblox-studio-mcp main.py (import check) ===")
print(raw("Nanoutrolley/roblox-studio-mcp", "main.py"))
print("   --- discord-auto-quest utils.py ---")
print(raw("Sectionsereclaim/discord-auto-quest", "utils.py"))

print("\n=== 6. GestaltX: README compatibility + backup claims (full) ===")
rm3 = raw("huamidev/GestaltX", "README.md")
i = rm3.find("## Compatibility")
print(rm3[i:i + 1700] if i >= 0 else rm3[-1700:])

print("\n=== 7. GestaltX: does it reference 'worse_query' (upstream dep)? ===")
for ln in rm3.splitlines():
    if "worse_query" in ln or "exploit" in ln.lower() or "NeoSpring" in ln:
        print("   ", ln.strip()[:190])
print("\n   --- AdvancedUnlockSequence.swift (274B) ---")
print(raw("huamidev/GestaltX", "GestaltX/AdvancedUnlockSequence.swift"))
print("\n   --- GestaltX.entitlements ---")
print(raw("huamidev/GestaltX", "GestaltX/GestaltX.entitlements"))

print("\n=== 8. bookleme: UNVERIFIED / fidelity claims ===")
rm4 = raw("bookleme/bookleme", "README.md")
for ln in rm4.splitlines():
    if any(k in ln for k in ["UNVERIFIED", "忠实", "measured", "heuristic", "版权", "零第三方"]):
        print("   ", ln.strip()[:190])

print("\n=== 9. rewind-for-x: privacy + on-device claims ===")
rm5 = raw("yetone/rewind-for-x", "README.md")
print("   readme len", len(rm5))
print("   --- privacy page (first 1800) ---")
print(raw("yetone/rewind-for-x", "site/privacy/index.html")[:1800])
