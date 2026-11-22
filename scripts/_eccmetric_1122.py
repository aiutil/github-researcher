#!/usr/bin/env python3
"""11-22 — three-axis skill metric for the 11-18 comparator repos that are NOT
on today's trending list (ECC, LoopForge) plus a control cohort of zero-
replication repos, so the corrected metric can be compared like-for-like.
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
    cmd = ["gh", "api"] + [url]
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


TARGETS = [
    "affaan-m/ECC", "Tencent/LoopForge", "addyosmani/agent-skills", "anthropics/skills",
    "obra/superpowers", "elementalsouls/Claude-BugHunter", "google-labs-code/stitch-skills",
    "mvanhorn/last30days-skill", "backnotprop/plannotator", "cursor/plugins",
    "tradermonty/claude-trading-skills", "alibaba/open-code-review", "HKUDS/CLI-Anything",
]

print(f"{'repo':42s} {'files':>6s} {'name':>6s} {'content':>7s} {'dupF':>6s} {'divF':>6s} "
      f"{'dup%':>6s} {'adapt%':>7s} {'F/content':>9s} {'nameRepl':>9s}")
rows = {}
for full in TARGETS:
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
    n = len(skills)
    n_name = len(per_name)
    n_content = len({b.get("sha") for b in skills})
    dup = div = 0
    for nm, lst in per_name.items():
        if len(lst) < 2:
            continue
        if len({x.get("sha") for x in lst}) == 1:
            dup += len(lst) - 1
        else:
            div += len(lst)
    rows[full] = dict(files=n, name=n_name, content=n_content, dup=dup, div=div,
                      dup_pct=round(100.0*dup/n, 1) if n else 0,
                      adapt_pct=round(100.0*div/n, 1) if n else 0,
                      f_per_c=round(n/n_content, 2) if n_content else 0,
                      name_repl=round(n/n_name, 2) if n_name else 0,
                      blobs=len(blobs), size_kb=m.get("size"), stars=m.get("stargazers_count"))
    r = rows[full]
    print(f"{full:42s} {n:6d} {n_name:6d} {n_content:7d} {dup:6d} {div:6d} "
          f"{r['dup_pct']:6.1f} {r['adapt_pct']:7.1f} {r['f_per_c']:9.2f} {r['name_repl']:9.2f}")

json.dump(rows, open("/tmp/skillmetric_full_1122.json", "w"), ensure_ascii=False, indent=1)
print("\nwrote /tmp/skillmetric_full_1122.json")

# ECC specifics: where are the byte-identical duplicates vs the divergent ones?
print("\n--- ECC duplicate structure (sample of groups) ---")
full = "affaan-m/ECC"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
skills = [b for b in blobs if os.path.basename(b.get("path") or "").lower() == "skill.md"]
per_name = defaultdict(list)
for b in skills:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
    per_name[nm].append(b)
ident = [n for n, l in per_name.items() if len({x.get("sha") for x in l}) == 1]
div = [n for n, l in per_name.items() if len(l) > 1 and len({x.get("sha") for x in l}) > 1]
print(f"   names appearing >1x: {len([n for n,l in per_name.items() if len(l)>1])}")
print(f"   of which BYTE-IDENTICAL: {len(ident)}   DIVERGENT: {len(div)}")
print(f"   max copies for an identical name: {max([len(per_name[n]) for n in ident] or [0])}")
print(f"   sample identical: {ident[:8]}")
print(f"   sample divergent: {div[:8]}")
# distinct root dirs holding skills
roots = defaultdict(int)
for b in skills:
    p = b.get("path") or ""
    roots["/".join(p.split("/")[:2])] += 1
print(f"   skill distribution by top-level dir: {dict(sorted(roots.items(), key=lambda x:-x[1])[:12])}")
