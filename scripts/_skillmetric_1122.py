#!/usr/bin/env python3
"""11-22 — the three-axis skill metric (final form) + download-range correction.

Axis 1 (name)  : distinct parent-DIRECTORY-NAME   -> how many skill NAMES
Axis 2 (sha)   : distinct blob sha                  -> how many distinct CONTENTS
Axis 3 (split) : of the name-collisions, how many are BYTE-IDENTICAL copies
                  vs genuinely DIVERGENT per-harness variants

derived:
  duplication   = byte-identical extra copies / files        (waste)
  adaptation    = divergent-copy files / files                (real per-harness work)
  true_repl     = files / distinct_content                   (files per unique content)

Also: full asset-download distribution for the repos whose 11-18 entry quoted a
truncated sample ("1-12 downloads"), to correct the published range.
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


probe = {p["full_name"]: p for p in json.load(open("/tmp/probe_1122.json"))}
skill_repos = [n for n, p in probe.items() if p["n_skill_files"] > 0]

print("=" * 118)
print("THREE-AXIS SKILL METRIC — 11-22 (files | name-ident | content-ident | "
      "byte-identical dup files | divergent files | dup% | adapt% | files/content)")
print("=" * 118)
results = {}
for full in sorted(skill_repos, key=lambda n: -probe[n]["n_skill_files"]):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per_name = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per_name[nm].append(b)
    n_name = len(per_name)
    n_content = len({b.get("sha") for b in skills})
    dup_files = 0
    div_files = 0
    for nm, lst in per_name.items():
        if len(lst) < 2:
            continue
        if len({x.get("sha") for x in lst}) == 1:
            dup_files += len(lst) - 1        # copies beyond the first
        else:
            div_files += len(lst)
    n = len(skills)
    results[full] = {
        "files": n, "name_ident": n_name, "content_ident": n_content,
        "dup_files": dup_files, "div_files": div_files,
        "dup_pct": round(100.0 * dup_files / n, 1) if n else 0,
        "adapt_pct": round(100.0 * div_files / n, 1) if n else 0,
        "files_per_content": round(n / n_content, 2) if n_content else 0,
        "name_repl": round(n / n_name, 2) if n_name else 0,
    }
    r = results[full]
    print(f"{full:42s} {n:5d} | {n_name:5d} | {n_content:5d} | {dup_files:5d} | {div_files:5d} | "
          f"{r['dup_pct']:5.1f} | {r['adapt_pct']:5.1f} | {r['files_per_content']:.2f}")

json.dump(results, open("/tmp/skillmetric_1122.json", "w"), ensure_ascii=False, indent=1)

print()
print("=" * 118)
print("DOWNLOAD-RANGE CORRECTION — repos whose 11-18 entry quoted a truncated sample")
print("=" * 118)
for full in ["backnotprop/plannotator", "alibaba/open-code-review", "getarcaneapp/arcane"]:
    rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rels = rels if isinstance(rels, list) else []
    if not rels:
        print(f"{full}: no releases")
        continue
    print(f"\n{full}: {len(rels)} releases")
    for r in rels[:3]:
        dl = sorted(a.get("download_count") or 0 for a in (r.get("assets") or []))
        if not dl:
            print(f"   {r.get('tag_name')}: 0 assets")
            continue
        print(f"   {str(r.get('tag_name')):12s} n={len(dl):3d} min={dl[0]:6d} "
              f"median={dl[len(dl)//2]:7d} max={dl[-1]:7d} sum={sum(dl):8d}")
        print(f"      full sorted: {dl}")
