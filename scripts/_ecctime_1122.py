#!/usr/bin/env python3
"""11-22 — pin down the ECC number discrepancy (published 330 vs calA@11-18 = 317).

The 11-18 daily report was generated on 2026-11-19 CST, so its tree snapshot may
be later than the 2026-11-18T23:00Z commit.  Sample the tree at several
timestamps and report calA / calC at each, to state the ECC finding precisely
rather than implying the repo changed.
"""
import json
import os
import subprocess
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def calibers(full, sha):
    tree = api(f"repos/{full}/git/trees/{sha}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per[nm].append(b)
    dup = div = 0
    for nm, lst in per.items():
        if len(lst) < 2:
            continue
        if len({x.get("sha") for x in lst}) == 1:
            dup += len(lst) - 1
        else:
            div += len(lst)
    return {"files": len(skills), "calA": len(per),
            "calC": len({b.get("sha") for b in skills}),
            "dup": dup, "div": div}


full = "affaan-m/ECC"
print(f"{'timestamp (until)':26s} {'sha':10s} {'files':>6s} {'calA':>6s} {'calC':>6s} "
      f"{'dup':>5s} {'div':>5s} {'calA repl':>10s}")
for until in ["2026-11-18T20:00:00Z", "2026-11-18T23:00:00Z", "2026-11-19T02:00:00Z",
              "2026-11-19T06:00:00Z", "2026-11-20T06:00:00Z", "2026-11-22T06:00:00Z"]:
    cs = api(f"repos/{full}/commits", {"until": until, "per_page": 1}) or []
    if not isinstance(cs, list) or not cs:
        print(f"{until:26s}  (no commit)")
        continue
    sha = cs[0].get("sha")
    c = calibers(full, sha)
    repl = c["files"] / c["calA"] if c["calA"] else 0
    print(f"{until:26s} {sha[:10]} {c['files']:6d} {c['calA']:6d} {c['calC']:6d} "
          f"{c['dup']:5d} {c['div']:5d} {repl:10.2f}")

print()
print("--- Same for cursor/plugins (published 173/113 = 1.53) ---")
for until in ["2026-11-18T12:00:00Z", "2026-11-19T06:00:00Z", "2026-11-22T06:00:00Z"]:
    cs = api("repos/cursor/plugins/commits", {"until": until, "per_page": 1}) or []
    if not isinstance(cs, list) or not cs:
        continue
    sha = cs[0].get("sha")
    c = calibers("cursor/plugins", sha)
    print(f"{until:26s} {sha[:10]} files={c['files']:4d} calA={c['calA']:4d} calC={c['calC']:4d} "
          f"dup={c['dup']:3d} div={c['div']:3d}")

print()
print("--- Same for backnotprop/plannotator (published 23/11 = 2.09) ---")
for until in ["2026-11-18T12:00:00Z", "2026-11-22T06:00:00Z"]:
    cs = api("repos/backnotprop/plannotator/commits", {"until": until, "per_page": 1}) or []
    if not isinstance(cs, list) or not cs:
        continue
    sha = cs[0].get("sha")
    c = calibers("backnotprop/plannotator", sha)
    print(f"{until:26s} {sha[:10]} files={c['files']:4d} calA={c['calA']:4d} calC={c['calC']:4d} "
          f"dup={c['dup']:3d} div={c['div']:3d}")
