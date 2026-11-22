#!/usr/bin/env python3
"""11-22 — reconcile the 11-18 "harness 清单数 / harness 目录" caliber.
The 11-18 report used a DIRECTORY-NAME list; my census used MANIFEST FILES.
Measure all three axes on the same tree so the daily report can state which is which.
"""
import json
import os
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")

# EXACT list from the 11-18 report (projects/ecc.md 架构师速览 table)
HARNESS_11_18 = (".agents", ".claude-plugin", ".codebuddy", ".codex-plugin", ".cursor",
                 ".gemini", ".grok-plugin", ".kiro", ".opencode")

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


print(f"{'repo':34s} {'dirs(11-18 list)':>18s} {'dirs w/ SKILL.md':>17s} {'manifest files':>16s}")
for full in SAME12:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") or "" for b in blobs]
    skill_paths = [p for p in paths
                   if os.path.basename(p).lower() == "skill.md"]
    dirs = sorted({p.split("/")[0] for p in paths if "/" in p and p.split("/")[0] in HARNESS_11_18})
    dirs_skill = sorted({p.split("/")[0] for p in skill_paths
                         if "/" in p and p.split("/")[0] in HARNESS_11_18})
    man = sorted({p for p in paths if os.path.basename(os.path.dirname(p)) in
                  (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".grok-plugin",
                   ".kiro-plugin", ".opencode-plugin", ".devin-plugin", ".kimi-plugin",
                   ".muse-plugin", ".antigravity-plugin", ".agents")
                  and os.path.basename(p) in ("plugin.json", "marketplace.json", "plugin.yaml")
                  or p == "gemini-extension.json"})
    print(f"{full:34s} {len(dirs):18d} {len(dirs_skill):17d} {len(man):16d}")
    print(f"{'':34s} dirs={dirs}")
    print(f"{'':34s} skill_dirs={dirs_skill}")
    print(f"{'':34s} manifests={man}")

# weekly star totals
t = json.load(open("/tmp/trend_1122.json"))
dw = [x for x in t if x["period"] == "daily"]
wk = [x for x in t if x["period"] == "weekly"]
print(f"\ndaily rows={len(dw)} sum_period_stars={sum(x['period_stars'] for x in dw):,}")
print(f"weekly rows={len(wk)} sum_period_stars={sum(x['period_stars'] for x in wk):,}")
print(f"total sum_period_stars={sum(x['period_stars'] for x in t):,}")
print("\ndaily ranking by period stars:")
for x in sorted(dw, key=lambda y: -y["period_stars"]):
    print(f"   {x['full_name']:42s} *{x['stars']:>8,} +{x['period_stars']:>6}")
