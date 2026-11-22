#!/usr/bin/env python3
"""11-22 — SAME 12 SKILL REPOS AS THE 11-18 REPORT, ONE CALIBER, FAST.
Tree-based identity metrics + README-only install-command census.
README-only is the exact caliber used by the 11-18 report ("安装命令" column).
"""
import json
import os
import re
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")

SAME12 = [
    "affaan-m/ECC", "Tencent/LoopForge", "backnotprop/plannotator", "cursor/plugins",
    "tradermonty/claude-trading-skills", "alibaba/open-code-review",
    "elementalsouls/Claude-BugHunter", "obra/superpowers", "addyosmani/agent-skills",
    "anthropics/skills", "mvanhorn/last30days-skill", "google-labs-code/stitch-skills",
]
HARNESS_DIRS = ("claude", "codex", "cursor", "gemini", "copilot", "windsurf", "amp",
                "zed", "opencode", "aider", "droid", "qwen", "claude-code",
                "antigravity", "kiro", "trae", "augment", "devin", "kimi", "muse",
                "hermes", "pi")


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


out = {}
print(f"{'repo':34s} {'files':>6s} {'nameId':>7s} {'pathId':>7s} {'contId':>7s} "
      f"{'nameRep':>8s} {'pathRep':>8s} {'contRep':>8s} {'i18n':>5s} {'canon':>6s} {'harn':>5s}")
for full in SAME12:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    paths = [b.get("path") or "" for b in skills]
    names = {os.path.basename(os.path.dirname(p)) if "/" in p else "<root>" for p in paths}
    pids = set(paths)
    cids = {b.get("sha") for b in skills}
    i18n = sum(1 for p in paths if p.startswith("docs/"))
    canon = sum(1 for p in paths if p.startswith("skills/"))
    harn = sum(1 for p in paths
               if any(s in HARNESS_DIRS for s in p.split("/")[:-1]))
    n = len(skills)
    rec = {"files": n, "nameId": len(names), "pathId": len(pids), "contentId": len(cids),
           "i18n": i18n, "canon": canon, "harness": harn,
           "nameRep": round(n / len(names), 2) if names else 0,
           "pathRep": round(n / len(pids), 2) if pids else 0,
           "contRep": round(n / len(cids), 2) if cids else 0,
           "stars": (m or {}).get("stargazers_count")}
    out[full] = rec
    print(f"{full:34s} {n:6d} {rec['nameId']:7d} {rec['pathId']:7d} {rec['contentId']:7d} "
          f"{rec['nameRep']:8.2f} {rec['pathRep']:8.2f} {rec['contRep']:8.2f} "
          f"{i18n:5d} {canon:6d} {harn:5d}")

json.dump(out, open("/tmp/same12_1122.json", "w"), ensure_ascii=False, indent=2)

print("\n--- install command census (README only, same caliber as 11-18) ---")
tally = {"BOTH": 0, "npx-only": 0, "mkt-only": 0, "NEITHER": 0}
for full in SAME12:
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    has_npx = "npx skills add" in rm
    has_mkt = "marketplace add" in rm
    tag = ("BOTH" if (has_npx and has_mkt) else "npx-only" if has_npx
           else "mkt-only" if has_mkt else "NEITHER")
    tally[tag] += 1
    print(f"   {full:34s} {tag}")
print(f"\n   {tally}  (of {len(SAME12)})")
