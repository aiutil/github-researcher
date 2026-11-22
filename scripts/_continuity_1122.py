#!/usr/bin/env python3
"""11-22 — continuity measurement using the EXACT calibers of the 11-18 report,
so that cross-day comparisons are valid:

  * harness 清单数  : count of harness-like DIRECTORY names in the tree
                      (same HARNESS_DIRS list as scripts/_probe_1121.py)
  * SKILL.md 三指标 : files / name-identities / content-identities
  * tag/release/asset four-tuple

Also checks autoclip's pushed_at vs default-branch head (an unexplained gap).
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
HARNESS_DIRS = ("claude", "codex", "cursor", "gemini", "copilot", "windsurf",
                "amp", "zed", "opencode", "aider", "droid", "qwen", "codex-cli",
                "claude-code", "antigravity", "kiro", "trae", "augment")

REPOS = ["affaan-m/ECC", "obra/superpowers", "cursor/plugins", "backnotprop/plannotator",
         "mvanhorn/last30days-skill", "google-labs-code/stitch-skills",
         "alibaba/open-code-review", "tradermonty/claude-trading-skills",
         "Tencent/LoopForge", "addyosmani/agent-skills", "anthropics/skills",
         "elementalsouls/Claude-BugHunter", "HKUDS/CLI-Anything",
         "GoogleChrome/modern-web-guidance-src", "kajisho5/ffmpeg-skill"]


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


print(f"{'repo':40s} {'SKILL files':>11s} {'nameIdent':>10s} {'contentId':>10s} "
      f"{'nameRepl':>9s} {'contentRepl':>11s} {'harnessDirs':>12s} {'maxNameCopy':>12s}")
for full in REPOS:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path", "") for b in blobs]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per[nm].append(b)
    n_name = len(per)
    n_content = len({b.get("sha") for b in skills})
    maxcopy = max([len(v) for v in per.values()] or [0])
    harness = set()
    for p in paths:
        for hp in HARNESS_DIRS:
            if hp in p.split("/"):
                harness.add(hp)
    nr = len(skills) / n_name if n_name else 0
    cr = len(skills) / n_content if n_content else 0
    print(f"{full:40s} {len(skills):11d} {n_name:10d} {n_content:10d} "
          f"{nr:9.2f} {cr:11.2f} {len(harness):12d} {maxcopy:12d}   {sorted(harness)}")

print()
print("--- autoclip: pushed_at vs default-branch HEAD ---")
m = api("repos/zhouxiaoka/autoclip") or {}
cs = api("repos/zhouxiaoka/autoclip/commits", {"per_page": 3}) or []
print(f"   pushed_at={m.get('pushed_at')} updated_at={m.get('updated_at')} "
      f"default_branch={m.get('default_branch')}")
for c in (cs if isinstance(cs, list) else [])[:3]:
    print(f"   HEAD {c.get('sha','')[:8]} "
          f"author={(c.get('commit',{}).get('author',{}) or {}).get('date')} "
          f"committer={(c.get('commit',{}).get('committer',{}) or {}).get('date')}")
br = api("repos/zhouxiaoka/autoclip/branches/main") or {}
print(f"   branch main head={br.get('commit',{}).get('sha','')[:8]} "
      f"(commit date via commits endpoint above)")
