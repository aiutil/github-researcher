#!/usr/bin/env python3
"""Sweep the 2026-11-11 candidate set for the 'activity-pulse' CI pattern.

Signature found on SteelMillerBar/auto-twitch-drops-claim:
  - a .github/workflows/*.yml that only appends a timestamp stamp file
  - a stamp file with random-named path (uppercase+digits)
  - github-actions[bot] as a top contributor with N commits
  - commit messages that are two random words from a fixed prefix list
    ("import analyze", "merge encrypt", "docs encrypt", ...)
"""
import json
import os
import re
import subprocess
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")
CAND = "/tmp/w1112/cand_1111.json"


def api(path_, headers=None, raw=False):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


rows = json.load(open(CAND, encoding="utf-8"))
print(f"scanning {len(rows)} candidates\n")

hits = []
for r in rows:
    full = r["full_name"]
    tree = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = [b.get("path") for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    wf = [p for p in blobs if p.startswith(".github/workflows/") and p.endswith((".yml", ".yaml"))]
    stamp = [p for p in blobs if p.startswith(".github/") and not p.startswith(".github/workflows/")
             and not p.startswith(".github/ISSUE_TEMPLATE")]
    contrib = api(f"repos/{full}/contributors") or []
    bot = 0
    if isinstance(contrib, list):
        bot = sum(c.get("contributions", 0) for c in contrib
                  if str(c.get("login", "")).endswith("[bot]"))
    total = sum(c.get("contributions", 0) for c in contrib) if isinstance(contrib, list) else 0
    commits = api(f"repos/{full}/commits?per_page=100") or []
    msgs = []
    if isinstance(commits, list):
        for c in commits:
            msgs.append(((c.get("commit", {}) or {}).get("message", "") or "").splitlines()[0])
    # two-word random commit messages
    twoword = sum(1 for m in msgs if len(m.split()) == 2 and not m.startswith(("Add", "Update", "Fix", "Merge")))
    pulse = bool(wf) and bool(stamp) and bot > 0
    if pulse or bot > 0 or twoword >= 3:
        hits.append((full, r["stars"], r["forks"], r["subs"], r["size_kb"], r["ncommits"],
                     len(blobs), wf, stamp, bot, total, twoword, len(msgs)))
        print(f"### {full}")
        print(f"    stars={r['stars']} forks={r['forks']} subs={r['subs']} size={r['size_kb']}KB "
              f"commits={r['ncommits']} blobs={len(blobs)}")
        print(f"    workflows={wf}  stamp_files={stamp}")
        print(f"    bot_commits={bot}/{total}  two_word_msgs={twoword}/{len(msgs)}")
        print(f"    sample_msgs={msgs[:8]}")
        print()

print(f"\n=== {len(hits)} candidates show a bot/pulse/two-word-message signal ===")
