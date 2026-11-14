#!/usr/bin/env python3
"""Fast md5-only farm census for the 2026-11-08 window (no fork calls)."""
import hashlib
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
KNOWN = {
    "e18f025c87b71b9fe481f53ac6e8235d": "FARM_gitignore",
    "8470fd5b911eacd63327be59d2562f16": "FARM_helpers_py",
    "258a0f5edf5d42288cfc1866497dc7dd": "FARM_initial_html",
}


def raw_bytes(full, path_):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github.raw",
           f"repos/{full}/contents/{path_}"]
    try:
        p = subprocess.run(cmd, capture_output=True, env=ENV, timeout=45)
    except Exception:
        return b""
    return p.stdout if p.returncode == 0 else b""


def tree(full):
    try:
        p = subprocess.run(["gh", "api", f"repos/{full}/git/trees/HEAD?recursive=1"],
                           capture_output=True, text=True, env=ENV, timeout=45)
        if p.returncode != 0:
            return []
        j = json.loads(p.stdout)
        return [(e["path"], e.get("size")) for e in j.get("tree", []) if e.get("type") == "blob"]
    except Exception:
        return []


data = json.load(open("/tmp/cand_2026_11_09.json", encoding="utf-8"))


def probe(x):
    full = x["full_name"]
    blobs = tree(full)
    hits = []
    for p, s in blobs:
        if s is not None and s > 200000:
            continue  # skip big binaries
        b = raw_bytes(full, p)
        if b:
            h = hashlib.md5(b).hexdigest()
            if h in KNOWN:
                hits.append((p, KNOWN[h]))
    rm = raw_bytes(full, "README.md").decode("utf-8", "replace")
    return {"full_name": full, "stars": x["stars"], "forks": x["forks"],
            "subs": x["subs"], "size_kb": x["size_kb"], "ncommits": x["ncommits"],
            "language": x["language"], "license": x["license"],
            "created_at": x["created_at"], "nfiles": len(blobs),
            "farm_hits": hits, "cta": rm.lower().count("star the repo"),
            "has_wdcc": "windows-defender.cc" in rm}


results = []
with ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(probe, data):
        results.append(r)

json.dump(results, open("/tmp/census_1108.json", "w"), ensure_ascii=False, indent=1)
farm = [r for r in results if r["farm_hits"]]
print(f"=== 2026-11-08 window census: {len(results)} candidates ===")
print(f"md5-FARM (known template): {len(farm)}")
print(f"windows-defender.cc payload: {sum(1 for r in results if r['has_wdcc'])}")
print(f"CTA 'star the repo': {sum(1 for r in results if r['cta'])}")
print(f"\n=== md5-FARM members ===")
for r in sorted(farm, key=lambda z: -(z["stars"] or 0)):
    print(f"  {r['full_name'][:46]:48s} {r['stars']:>4}* {r['forks']:>4}f sub{r['subs']:>4} "
          f"files={r['nfiles']:>3} c{r['ncommits']:>3} cta={r['cta']} wdcc={r['has_wdcc']} "
          f"hits={[h[0] for h in r['farm_hits']]}")
print(f"\n=== NON-farm, NON-wdcc (real candidates) ===")
for r in sorted([x for x in results if not x["farm_hits"] and not x["has_wdcc"]],
                key=lambda z: -(z["stars"] or 0)):
    print(f"  {r['full_name'][:46]:48s} {r['stars']:>4}* {r['forks']:>4}f sub{r['subs']:>4} "
          f"files={r['nfiles']:>3} c{r['ncommits']:>3} cta={r['cta']} {r['size_kb']:>7}KB "
          f"{str(r['language'])[:10]:11s} {str(r['license'])[:11]}")
