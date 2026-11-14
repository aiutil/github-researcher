#!/usr/bin/env python3
"""Forensics for the 2026-11-08 UTC candidate window (daily report 2026-11-09).

Goals:
 1. Prove the farm cluster shares ONE README template (md5 of full body, not head).
 2. Prove the payload instruction is byte-identical across the cluster.
 3. Detect the SEO keyword block ("Organic Discovery & Identification").
 4. Fork-arrival timing for the non-farm candidates.
 5. Structural comparison of the Rust Windows-utility cluster.
"""
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_2026_11_09.json"
data = json.load(open(PATH, encoding="utf-8"))


def api(path_, raw=True, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    return p.stdout


def raw_readme(full):
    t = api(f"repos/{full}/readme", headers=["Accept: application/vnd.github.raw"])
    return t or ""


farm = [x for x in data if "windows-defender.cc" in x["readme_head"]]
rest = [x for x in data if "windows-defender.cc" not in x["readme_head"]]

print(f"### window candidates={len(data)} farm(windows-defender.cc)={len(farm)} rest={len(rest)}\n")

# ---------- 1. README template md5 over FULL body (sample) --------------
print("=== 1. FULL README md5 over 24 farm repos (sorted by stars) ===")
sample = sorted(farm, key=lambda y: -(y["stars"] or 0))[:24]
md5s = Counter()
per = []
for x in sample:
    rm = raw_readme(x["full_name"])
    h = hashlib.md5(rm.encode("utf-8", "replace")).hexdigest()
    md5s[h] += 1
    per.append((x["full_name"], len(rm), h))
    time.sleep(0.15)
for full, ln, h in per:
    print(f"  {full[:48]:50s} len={ln:>6} md5={h}")
print("  distinct md5:", len(md5s), md5s.most_common(5))

# ---------- 2. payload instruction identity ----------------------------
print("\n=== 2. PAYLOAD INSTRUCTION (exact line) across 20 farm repos ===")
pat = re.compile(r"irm\s+https?://[^\s|]+[^\n]*")
seen = Counter()
for x in sample[:20]:
    rm = raw_readme(x["full_name"])
    for m in pat.findall(rm):
        seen[m.strip()] += 1
    time.sleep(0.15)
for line, n in seen.most_common(8):
    print(f"  [{n:>3}x] {line}")

# ---------- 3. SEO keyword block ---------------------------------------
print("\n=== 3. 'Organic Discovery & Identification' block ===")
seo = 0
kw_samples = []
for x in sample[:12]:
    rm = raw_readme(x["full_name"])
    if "Organic Discovery" in rm:
        seo += 1
        m = re.search(r"## \U0001F50D Organic Discovery.*?\n\n(.*?)\n\n", rm, re.S)
        if m and len(kw_samples) < 3:
            kw_samples.append((x["full_name"], m.group(1).strip()))
    time.sleep(0.15)
print(f"  present in {seo}/12 sampled farm READMEs")
for full, kw in kw_samples:
    print(f"  -- {full}")
    print(f"     {kw[:300]}")

# ---------- 4. fork timing for non-farm --------------------------------
print("\n=== 4. FORK ARRIVAL TIMING (non-farm, top 14 by stars) ===")
for x in sorted(rest, key=lambda y: -(y["stars"] or 0))[:14]:
    if not x["forks"]:
        print(f"  {x['full_name'][:46]:48s} forks=0")
        continue
    t = api(f"repos/{x['full_name']}/forks", raw=False)
    try:
        arr = json.loads(t)
    except Exception:
        print(f"  {x['full_name'][:46]:48s} fork fetch failed")
        continue
    ts = sorted(a.get("created_at") for a in arr if a.get("created_at"))
    if len(ts) < 2:
        print(f"  {x['full_name'][:46]:48s} forks={x['forks']:>4} sampled={len(ts)} (too few)")
        continue
    from datetime import datetime
    gaps = []
    for i in range(1, len(ts)):
        a = datetime.fromisoformat(ts[i - 1].replace("Z", "+00:00"))
        b = datetime.fromisoformat(ts[i].replace("Z", "+00:00"))
        gaps.append((b - a).total_seconds())
    gaps_sorted = sorted(gaps)
    med = gaps_sorted[len(gaps_sorted) // 2]
    le10 = sum(1 for g in gaps if g <= 10)
    span = (datetime.fromisoformat(ts[-1].replace("Z", "+00:00"))
            - datetime.fromisoformat(ts[0].replace("Z", "+00:00"))).total_seconds() / 60
    print(f"  {x['full_name'][:46]:48s} forks={x['forks']:>4} sampled={len(ts):>3} "
          f"med_gap={med:>7.1f}s le10={le10}/{len(gaps)} span={span:.1f}min")
    time.sleep(0.2)

# ---------- 5. Rust Windows-utility cluster: file paths ----------------
print("\n=== 5. RUST UTILITY CLUSTER: file paths + sizes ===")
RUST = ["PlateParrotTerminal/lag-doctor", "ToneProtectorSolve48/drift-doctor",
        "AmbassadorTassel/omnigear-peripheral-manager",
        "majestydamseldecoder/truestretch-stretched-resolution",
        "Avalanchevonproxy69/fanatic-laptop-control"]
trees = {}
for full in RUST:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        print(f"  {full}: tree fetch failed")
        continue
    trees[full] = {e["path"]: e.get("size") for e in j.get("tree", []) if e.get("type") == "blob"}
    time.sleep(0.2)
paths = defaultdict(list)
for full, tr in trees.items():
    for p in tr:
        paths[p].append(full)
print(f"  repos probed: {len(trees)}  distinct paths: {len(paths)}")
common = [p for p, rs in paths.items() if len(rs) == len(trees)]
print(f"  paths present in ALL {len(trees)} repos ({len(common)}):")
for p in sorted(common):
    print(f"    {p}")
for full, tr in trees.items():
    print(f"  -- {full}: {len(tr)} files")
    for p in sorted(tr)[:14]:
        print(f"       {tr[p]:>8}  {p}")
    if len(tr) > 14:
        print(f"       ... +{len(tr)-14} more")

# ---------- 6. Cargo.toml / Cargo.lock identity ------------------------
print("\n=== 6. Cargo.toml md5 (is it one crate cloned N times?) ===")
cm = Counter()
for full in RUST:
    t = api(f"repos/{full}/contents/Cargo.toml")
    txt = ""
    if t:
        try:
            if t.startswith("{"):
                txt = base64.b64decode(json.loads(t).get("content", "")).decode("utf-8", "replace")
            else:
                txt = t
        except Exception:
            txt = ""
    h = hashlib.md5(txt.encode()).hexdigest() if txt else "n/a"
    cm[h] += 1
    print(f"  {full[:46]:48s} md5={h} len={len(txt)}")
    time.sleep(0.15)
print("  distinct Cargo.toml md5:", cm.most_common())
