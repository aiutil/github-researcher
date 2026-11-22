#!/usr/bin/env python3
"""11-22 — precise decomposition of the 'replication factor', so the daily can
state exactly WHICH replication is being measured.

For each repo:
  files            = SKILL.md count
  names            = distinct parent-directory names
  contents         = distinct blob SHAs
  byteIdentExtra   = files - contents          (files that are byte-copies)
  inMultiName      = files whose name has >1 copy
  allIdentical     = files whose name-group is entirely byte-identical
  inDivergentName  = files whose name-group has >1 distinct content
"""
import json
import os
import subprocess
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")

SAME12 = [
    "affaan-m/ECC", "Tencent/LoopForge", "backnotprop/plannotator", "cursor/plugins",
    "tradermonty/claude-trading-skills", "alibaba/open-code-review",
    "elementalsouls/Claude-BugHunter", "obra/superpowers", "addyosmani/agent-skills",
    "anthropics/skills", "mvanhorn/last30days-skill", "google-labs-code/stitch-skills",
]


def api(path, params=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    try:
        p = subprocess.run(["gh", "api", url], capture_output=True, text=True,
                           env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


out = {}
print(f"{'repo':34s} {'files':>6s} {'names':>6s} {'cont':>6s} {'byteExtra':>10s} "
      f"{'byte%':>7s} {'inMultiName':>13s} {'multiName%':>11s} {'allIdent':>9s} {'diverge':>8s}")
for full in SAME12:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per[nm].append(b)
    n = len(skills)
    names = len(per)
    cont = len({b.get("sha") for b in skills})
    byte_extra = n - cont
    multi = {nm: v for nm, v in per.items() if len(v) > 1}
    in_multi = sum(len(v) for v in multi.values())
    all_ident = sum(len(v) for v in multi.values()
                    if len({x.get("sha") for x in v}) == 1)
    diverge = sum(len(v) for v in multi.values()
                  if len({x.get("sha") for x in v}) > 1)
    rec = {"files": n, "names": names, "contents": cont, "byteExtra": byte_extra,
           "bytePct": round(100.0 * byte_extra / n, 1) if n else 0,
           "inMultiName": in_multi,
           "multiNamePct": round(100.0 * in_multi / n, 1) if n else 0,
           "allIdentical": all_ident, "divergent": diverge,
           "nameRep": round(n / names, 2) if names else 0,
           "contentRep": round(n / cont, 2) if cont else 0}
    out[full] = rec
    print(f"{full:34s} {n:6d} {names:6d} {cont:6d} {byte_extra:10d} "
          f"{rec['bytePct']:6.1f}% {in_multi:13d} {rec['multiNamePct']:10.1f}% "
          f"{all_ident:9d} {diverge:8d}")

json.dump(out, open("/tmp/decomp_table_1122.json", "w"), ensure_ascii=False, indent=2)
print("\nwrote /tmp/decomp_table_1122.json")
