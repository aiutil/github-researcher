#!/usr/bin/env python3
"""11-22 — SAME-17 install-command census, exactly the same repo set and
exactly the same caliber as /tmp/install_same17_1121.json (README-only).
This is the ONLY valid cross-day install-command comparison.
"""
import json
import os
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")

prev = json.load(open("/tmp/install_same17_1121.json"))
repos = [r["repo"] for r in prev]
print(f"same-17 set loaded from 11-21 snapshot: {len(repos)} repos\n")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
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


rows = []
for r in prev:
    full = r["repo"]
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    has_npx = "npx skills add" in rm
    has_mkt = "marketplace add" in rm
    m = api(f"repos/{full}") or {}
    rows.append({
        "repo": full,
        "npx_skills_add": has_npx,
        "marketplace_add": has_mkt,
        "both": has_npx and has_mkt,
        "stars": (m or {}).get("stargazers_count"),
    })
    print(f"  {full:44s} npx={str(has_npx):5s} mkt={str(has_mkt):5s} "
          f"both={str(has_npx and has_mkt):5s}  (11-21: npx={str(r.get('npx_skills_add')):5s} "
          f"mkt={str(r.get('marketplace_add')):5s} both={str(r.get('both')):5s})")

nb = sum(1 for r in rows if r["both"])
nn = sum(1 for r in rows if r["npx_skills_add"] and not r["marketplace_add"])
nm = sum(1 for r in rows if r["marketplace_add"] and not r["npx_skills_add"])
ne = sum(1 for r in rows if not r["npx_skills_add"] and not r["marketplace_add"])
print(f"\n  11-22: BOTH={nb}  npx-only={nn}  mkt-only={nm}  NEITHER={ne}  (of {len(rows)})")
pb = sum(1 for r in prev if r.get("both"))
pn = sum(1 for r in prev if r.get("npx_skills_add") and not r.get("marketplace_add"))
pm = sum(1 for r in prev if r.get("marketplace_add") and not r.get("npx_skills_add"))
pe = sum(1 for r in prev if not r.get("npx_skills_add") and not r.get("marketplace_add"))
print(f"  11-21: BOTH={pb}  npx-only={pn}  mkt-only={pm}  NEITHER={pe}  (of {len(prev)})")
print("\n  changed repos:")
for a, b in zip(prev, rows):
    if (a.get("npx_skills_add"), a.get("marketplace_add")) != (b["npx_skills_add"], b["marketplace_add"]):
        print(f"    {b['repo']:44s} "
              f"({a.get('npx_skills_add')},{a.get('marketplace_add')}) -> "
              f"({b['npx_skills_add']},{b['marketplace_add']})")

json.dump(rows, open("/tmp/install_same17_1122.json", "w"), ensure_ascii=False, indent=2)
