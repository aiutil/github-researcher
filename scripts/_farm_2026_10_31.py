#!/usr/bin/env python3
"""Farm-campaign continuity check for 2026-10-31 + hypergrad anomaly."""
import json, subprocess, os, re, sys

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
    if r is None:
        return None
    try:
        return json.loads(r)
    except Exception:
        return None


DAY = sys.argv[1] if len(sys.argv) > 1 else "2026-10-30"
res = japi(f"search/repositories?q=created:{DAY}+stars:>=40+size:<=20&per_page=100")
print(f"=== FARM CANDIDATES created {DAY}: total_count={res['total_count']} (fetched {len(res['items'])}) ===")
hits = {}
filesizes = {}
readmes = {}
for it in res["items"]:
    full = it["full_name"]
    rd = api(f"repos/{full}/readme", raw=True) or ""
    readmes[full] = rd
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1")
    files = []
    if tree and "tree" in tree:
        files = [(e["path"], e.get("size", 0)) for e in tree["tree"] if e["type"] == "blob"]
    filesizes[full] = files
    for pat in ["git-software.cc", "Invoke-Expression", "irm ", "Setup.ps1", "Windows Security Center",
                "实时保护", "实时保護", "security center"]:
        if pat.lower() in rd.lower():
            hits.setdefault(pat, []).append(full)

print("\n--- payload pattern hits in README ---")
for pat, lst in hits.items():
    print(f"  {pat!r}: {len(lst)} repos  e.g. {lst[:4]}")

print("\n--- file-structure fingerprints (top 8 by structure) ---")
struct_count = {}
for full, files in filesizes.items():
    key = tuple(sorted((p, s) for p, s in files))
    struct_count.setdefault(key, []).append(full)
for key, lst in sorted(struct_count.items(), key=lambda kv: -len(kv[1]))[:8]:
    print(f"  {len(lst)} repos share structure: {[(p, s) for p, s in key]}")
    print(f"      e.g. {lst[:3]}")

print("\n--- sample README of a farm repo ---")
for full, rd in list(readmes.items())[:1]:
    print(f"[{full}] {len(rd)} bytes")
    print(rd[:2500])

print("\n--- owner-name patterns ---")
owners = sorted({f.split('/')[0] for f in readmes})
print(f"  {len(owners)} distinct owners; sample: {owners[:12]}")
print(f"  owner name lengths: {sorted({len(o) for o in owners})}")
