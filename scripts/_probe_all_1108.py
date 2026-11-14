#!/usr/bin/env python3
"""Quantify the FULL farm cluster in the 2026-11-08 window (all 171 candidates).

For each candidate: fetch root tree, md5 every blob, check against known farm
fingerprints, check for 'Star the repo' CTA, compute fork-arrival timing.
Output a machine-readable summary.
"""
import hashlib
import json
import os
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
KNOWN = {
    "e18f025c87b71b9fe481f53ac6e8235d": "FARM_gitignore",
    "8470fd5b911eacd63327be59d2562f16": "FARM_helpers_py",
    "258a0f5edf5d42288cfc1866497dc7dd": "FARM_initial_html",
}


def api(path_, headers=None, binary=False):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    if binary:
        return p.stdout
    return p.stdout.decode("utf-8", "replace")


def raw_bytes(full, path_):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github.raw",
           f"repos/{full}/contents/{path_}"]
    p = subprocess.run(cmd, capture_output=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return b""
    return p.stdout


data = json.load(open("/tmp/cand_2026_11_09.json", encoding="utf-8"))


def probe(x):
    full = x["full_name"]
    out = {"full_name": full, "stars": x["stars"], "forks": x["forks"],
           "subs": x["subs"], "size_kb": x["size_kb"], "language": x["language"],
           "license": x["license"], "ncommits": x["ncommits"],
           "created_at": x["created_at"], "readme_len": x["readme_len"],
           "desc": x["desc"], "farm_hits": [], "nfiles": 0, "cta": 0}
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    try:
        j = json.loads(t)
    except Exception:
        return out
    blobs = [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    out["nfiles"] = len(blobs)
    for p, s in blobs:
        b = raw_bytes(full, p)
        h = hashlib.md5(b).hexdigest()
        if h in KNOWN:
            out["farm_hits"].append((p, KNOWN[h]))
    rm = raw_bytes(full, "README.md").decode("utf-8", "replace")
    out["cta"] = rm.lower().count("star the repo")
    out["readme_bytes"] = len(rm)
    # fork timing
    ft = api(f"repos/{full}/forks")
    try:
        arr = json.loads(ft)
        ts = sorted(a.get("created_at") for a in arr if a.get("created_at"))
        if len(ts) >= 2:
            gaps = []
            for i in range(1, len(ts)):
                a = datetime.fromisoformat(ts[i - 1].replace("Z", "+00:00"))
                b = datetime.fromisoformat(ts[i].replace("Z", "+00:00"))
                gaps.append((b - a).total_seconds())
            gs = sorted(gaps)
            out["fork_med"] = gs[len(gs) // 2]
            out["fork_le10"] = sum(1 for g in gaps if g <= 10)
            out["fork_n"] = len(gaps)
            out["fork_span_min"] = (datetime.fromisoformat(ts[-1].replace("Z", "+00:00"))
                                     - datetime.fromisoformat(ts[0].replace("Z", "+00:00"))).total_seconds() / 60
        else:
            out["fork_med"] = None
            out["fork_n"] = len(ts)
    except Exception:
        out["fork_med"] = None
    return out


results = []
with ThreadPoolExecutor(max_workers=6) as ex:
    for i, r in enumerate(ex.map(probe, data)):
        results.append(r)
        if (i + 1) % 20 == 0:
            print(f"  ... {i+1}/{len(data)}", flush=True)

json.dump(results, open("/tmp/probe_1108.json", "w"), ensure_ascii=False, indent=1)

farm = [r for r in results if r["farm_hits"]]
print(f"\n=== SUMMARY 2026-11-08 window: {len(results)} candidates ===")
print(f"FARM (known md5 hit): {len(farm)}")
print(f"CTA 'star the repo' present: {sum(1 for r in results if r['cta'])}")
print(f"fork_med <= 10s: {sum(1 for r in results if r.get('fork_med') is not None and r['fork_med'] <= 10)}")
print(f"\n=== FARM MEMBERS ===")
for r in sorted(farm, key=lambda z: -(z["stars"] or 0)):
    print(f"  {r['full_name'][:46]:48s} {r['stars']:>4}* {r['forks']:>4}f sub{r['subs']:>4} "
          f"files={r['nfiles']:>3} c{r['ncommits']:>3} cta={r['cta']} "
          f"fmed={r.get('fork_med')} le10={r.get('fork_le10')}/{r.get('fork_n')} "
          f"hits={[h[0] for h in r['farm_hits']]}")
print(f"\n=== NON-FARM (sorted by stars) ===")
for r in sorted([x for x in results if not x["farm_hits"]], key=lambda z: -(z["stars"] or 0)):
    print(f"  {r['full_name'][:46]:48s} {r['stars']:>4}* {r['forks']:>4}f sub{r['subs']:>4} "
          f"files={r['nfiles']:>3} c{r['ncommits']:>3} cta={r['cta']} "
          f"fmed={r.get('fork_med')} le10={r.get('fork_le10')}/{r.get('fork_n')} "
          f"span={r.get('fork_span_min')}")
