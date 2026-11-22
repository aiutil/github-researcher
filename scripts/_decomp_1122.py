#!/usr/bin/env python3
"""11-22 — FINAL decomposition measurement:
 (a) ECC: for each 10-copy skill name, classify every copy as
     i18n / harness / canonical / other, and detect byte-identical groups.
 (b) same-12 harness-DIRECTORY count using the EXACT 11-18 directory list.
 (c) same-12 "installable caliber": drop docs/<locale>/ and recompute
     files / nameId / contentId, to expose how much of the name-caliber
     replication factor is really just documentation translations.
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
# EXACT list used by the 11-18 report for "harness 目录"
HARNESS_11_18 = (".agents", ".claude-plugin", ".codebuddy", ".codex-plugin", ".cursor",
                 ".gemini", ".grok-plugin", ".kiro", ".opencode")


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


def tree_of(full):
    m = api(f"repos/{full}") or {}
    t = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    return [b for b in (t.get("tree") or []) if b.get("type") == "blob"]


def klass(p):
    seg = p.split("/")
    if len(seg) > 1 and seg[0] == "docs":
        return "i18n"
    if len(seg) > 1 and seg[0] in HARNESS_11_18:
        return "harness"
    if len(seg) > 1 and seg[0] == "skills":
        return "canonical"
    return "other"


# ---------- (a) ECC 10-copy decomposition ----------
print("=" * 92)
print("(a) ECC — the six 10-copy skill names, decomposed by copy provenance")
print("=" * 92)
full = "affaan-m/ECC"
blobs = tree_of(full)
skills = [b for b in blobs
          if os.path.basename(b.get("path") or "").lower() == "skill.md"]
per = defaultdict(list)
for b in skills:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
    per[nm].append(b)
for nm in ["backend-patterns", "coding-standards", "frontend-patterns",
           "security-review", "tdd-workflow", "verification-loop"]:
    lst = per[nm]
    k = defaultdict(list)
    for x in lst:
        k[klass(x.get("path"))].append(x)
    shas = defaultdict(int)
    for x in lst:
        shas[x.get("sha")] += 1
    ident = sum(v - 1 for v in shas.values() if v > 1)
    print(f"\n  {nm}: {len(lst)} copies | "
          f"i18n={len(k['i18n'])} harness={len(k['harness'])} "
          f"canonical={len(k['canonical'])} other={len(k['other'])} | "
          f"byte-identical extra copies={ident} | distinct_sha={len(shas)}")
    for x in sorted(lst, key=lambda y: y.get("path")):
        tag = "IDENTICAL-TO-SIBLING" if shas[x.get("sha")] > 1 else "unique-content"
        print(f"      [{klass(x.get('path')):9s}] {x.get('size'):7d}B "
              f"{x.get('sha')[:8]} {x.get('path')}   <{tag}>")

# ---------- (b)+(c) same-12, two calibers ----------
print()
print("=" * 92)
print("(b)(c) same-12 — 11-18 caliber (all files, name identity) vs installable")
print("     caliber (docs/<locale> removed)")
print("=" * 92)
hdr = (f"{'repo':34s} | {'ALL FILES':^28s} | {'INSTALLABLE (no docs/<locale>)':^34s}")
print(hdr)
print(f"{'':34s} | {'files nameId contId nRep':^28s} | "
      f"{'files nameId contId nRep  i18n':^34s}")
print("-" * len(hdr))
agg = {}
for full in SAME12:
    blobs = tree_of(full)
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    allp = [(b.get("path") or "", b.get("sha")) for b in skills]
    inst = [(p, s) for p, s in allp if not p.startswith("docs/")]

    def stats(items):
        ps = [p for p, _ in items]
        nm = {os.path.basename(os.path.dirname(p)) if "/" in p else "<root>" for p in ps}
        sh = {s for _, s in items}
        return len(ps), len(nm), len(sh), (round(len(ps) / len(nm), 2) if nm else 0)

    a = stats(allp)
    i = stats(inst)
    hdirs = sorted({p.split("/")[0] for p, _ in allp
                    if "/" in p and p.split("/")[0] in HARNESS_11_18})
    agg[full] = {"all": a, "inst": i, "harnessDirs": hdirs}
    print(f"{full:34s} | {a[0]:5d} {a[1]:5d} {a[2]:6d} {a[3]:5.2f} | "
          f"{i[0]:5d} {i[1]:5d} {i[2]:6d} {i[3]:5.2f} {len(allp)-i[0]:5d}"
          f"   harnessDirs={hdirs}")

json.dump(agg, open("/tmp/final_decomp_1122.json", "w"), ensure_ascii=False, indent=2)
print("\nwrote /tmp/final_decomp_1122.json")
