#!/usr/bin/env python3
"""Decisive evidence: (a) farm 'aging' mass-push mechanism, (b) payload prevalence across cohorts."""
import json, subprocess, os, re, collections, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


print("### A) aging mechanism: pick a 10-29 shell now ~65KB, inspect files + commits")
for full in ["Yugiri-AO/battery-peek", "war4me12-star/dev-library-di-singleton", "dannairfawan/fast-activator"]:
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = sorted([(e["path"], e.get("size", 0)) for e in tree.get("tree", []) if e["type"] == "blob"],
                   key=lambda x: -x[1])
    cm = japi(f"repos/{full}/commits?per_page=10") or []
    print(f"\n  [{full}]")
    for p, s in blobs:
        print(f"     {s:>8}  {p}")
    print(f"     commits(first {len(cm)}):")
    for c in cm:
        print(f"       {c['commit']['author']['date']} | {c['commit']['message'].splitlines()[0][:70]}")

print("\n\n### B) payload prevalence: 10-29 cohort, sample 45 across size buckets")
c29 = japi("search/repositories?q=created:2026-10-29+stars:>=40&per_page=45")
hit = 0
tot = 0
small_hit = small_tot = 0
for i in c29["items"]:
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    if not rd:
        continue
    tot += 1
    p = ("git-software.cc" in rd) or ("Invoke-Expression" in rd)
    if p:
        hit += 1
    if i["size"] <= 20:
        small_tot += 1
        if p:
            small_hit += 1
print(f"  README readable={tot}; payload hits={hit} ({hit*100//max(tot,1)}%)")
print(f"  of size<=20 subset: {small_hit}/{small_tot}")

print("\n### C) payload prevalence: 10-30 cohort, sample 45")
c30 = japi("search/repositories?q=created:2026-10-30+stars:>=40&per_page=45")
hit30 = 0
tot30 = 0
for i in c30["items"]:
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    if not rd:
        continue
    tot30 += 1
    if ("git-software.cc" in rd) or ("Invoke-Expression" in rd):
        hit30 += 1
print(f"  README readable={tot30}; payload hits={hit30} ({hit30*100//max(tot30,1)}%)")

print("\n### D) 10-30 cohort: what do the 8-blob shells look like now?")
c30b = japi("search/repositories?q=created:2026-10-30+stars:>=40&per_page=100")
band = [i for i in c30b["items"] if 20 < i["size"] <= 100]
print(f"  21-100KB count in first 100: {len(band)}")
for i in band[:5]:
    tree = japi(f"repos/{i['full_name']}/git/trees/HEAD?recursive=1") or {}
    blobs = sorted([(e["path"], e.get("size", 0)) for e in tree.get("tree", []) if e["type"] == "blob"], key=lambda x: -x[1])
    print(f"   [{i['full_name']}] size={i['size']}KB blobs={len(blobs)} pushed={i['pushed_at']}")
    for p, s in blobs[:9]:
        print(f"       {s:>8}  {p}")
