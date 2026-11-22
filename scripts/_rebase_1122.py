#!/usr/bin/env python3
"""DECISIVE TEST (11-22): is the skill-identity delta between 11-18 and 11-22
(a) a real repository restructuring, or (b) a caliber inconsistency in how the
11-18 report counted "independent skill identity"?

Method: for each repo, find the commit that was HEAD on 2026-11-18, fetch the
tree AT THAT COMMIT, and recompute all three calibers:
  calA = distinct parent-DIRECTORY-NAME   (what _identity_2026_11_18.py used)
  calB = distinct (parent path -> sha set)
  calC = distinct blob sha (pure content identity)

If calA@11-18 reproduces the number printed in the 11-18 daily report, then the
11-18 numbers are internally consistent and today's delta is a real repo change.
If it does NOT reproduce, the 11-18 table mixed calibers.
"""
import json
import os
import subprocess
import urllib.parse
from collections import defaultdict

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


REPOS = [
    "backnotprop/plannotator",
    "cursor/plugins",
    "tradermonty/claude-trading-skills",
    "alibaba/open-code-review",
    "affaan-m/ECC",
    "Tencent/LoopForge",
]
# numbers exactly as printed in the 2026-11-18 daily report table
REPORTED_1118 = {
    "backnotprop/plannotator": (23, 11),
    "cursor/plugins": (173, 113),
    "tradermonty/claude-trading-skills": (94, 74),
    "alibaba/open-code-review": (4, 4),
    "affaan-m/ECC": (1087, 330),
    "Tencent/LoopForge": (21, 9),
}
CUTOFF = "2026-11-18T23:00:00Z"


def calibers(tree_json):
    blobs = [b for b in (tree_json.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    if not skills:
        return 0, 0, 0, 0, []
    name_ident, shaset_ident = defaultdict(list), defaultdict(set)
    for b in skills:
        p = b.get("path") or ""
        parent_name = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        parent_path = p.rsplit("/", 1)[0] if "/" in p else "<root>"
        name_ident[parent_name].append(b.get("sha"))
        shaset_ident[parent_path].add(b.get("sha"))
    return (len(skills),
            len(name_ident),
            len({frozenset(v) for v in shaset_ident.values()}),
            len({b.get("sha") for b in skills}),
            sorted(name_ident.keys()))


for full in REPOS:
    print("=" * 100)
    print(full, " | 11-18 report said:", REPORTED_1118.get(full))
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    # find last commit at or before the 11-18 cutoff
    cs = api(f"repos/{full}/commits", {"until": CUTOFF, "per_page": 1}) or []
    if not isinstance(cs, list) or not cs:
        print("   no commit found before cutoff")
        continue
    old_sha = cs[0].get("sha")
    old_date = (cs[0].get("commit", {}).get("author", {}) or {}).get("date")
    old_msg = (cs[0].get("commit", {}).get("message") or "").split("\n")[0]
    print(f"   HEAD@11-18 = {old_sha[:10]}  {old_date}  {old_msg[:70]}")

    t_old = api(f"repos/{full}/git/trees/{old_sha}?recursive=1") or {}
    fo, calA_old, calB_old, calC_old, names_old = calibers(t_old)
    print(f"   AT 11-18 COMMIT: files={fo:5d}  calA(name)={calA_old:4d}  "
          f"calB(path)={calB_old:4d}  calC(sha)={calC_old:4d}   truncated={t_old.get('truncated')}")

    t_now = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    fn, calA_now, calB_now, calC_now, names_now = calibers(t_now)
    print(f"   AT 11-22 HEAD  : files={fn:5d}  calA(name)={calA_now:4d}  "
          f"calB(path)={calB_now:4d}  calC(sha)={calC_now:4d}")

    rf, ri = REPORTED_1118.get(full, (None, None))
    verdict = []
    if ri is not None:
        if ri == calA_old:
            verdict.append("11-18 report == calA@11-18 (NAME caliber) -> consistent")
        elif ri == calC_old:
            verdict.append("11-18 report == calC@11-18 (CONTENT caliber) -> MIXED caliber")
        elif ri == calB_old:
            verdict.append("11-18 report == calB@11-18 (PATH caliber) -> MIXED caliber")
        else:
            verdict.append(f"11-18 report ({ri}) matches NO caliber at 11-18 commit "
                           f"[calA={calA_old} calB={calB_old} calC={calC_old}]")
    print("   VERDICT: " + ("; ".join(verdict) if verdict else "n/a"))
    if calA_old != calA_now:
        print(f"   calA changed across 4 days: {calA_old} -> {calA_now}")
        added = [x for x in names_now if x not in names_old]
        removed = [x for x in names_old if x not in names_now]
        if added:
            print(f"      names added: {added[:15]}")
        if removed:
            print(f"      names removed: {removed[:15]}")
    print()
