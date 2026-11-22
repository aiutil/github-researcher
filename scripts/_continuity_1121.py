#!/usr/bin/env python3
"""Continuity measurement for 2026-11-18.

Re-measure the EXACT repo set used on 2026-11-17 for the install-protocol
convergence metric, so the two days are directly comparable:

  11-17 reported "3 of 17 repos publish both `npx skills add` and
  `/plugin marketplace add`".  We re-run the same measurement today on the
  same 17 repos and report the delta.

Also: contributors, workflow lists and harness manifest counts for today's
key projects.
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")

SAME_17 = [
    "google/elephant-goldfish-model", "mvanhorn/last30days-skill",
    "kajisho5/ffmpeg-skill", "addyosmani/agent-skills",
    "ag-ui-protocol/ag-ui", "boringmarketer/boring-marketing-skills",
    "elementalsouls/Claude-BugHunter", "NVIDIA/SkillEvaluator",
    "anthropics/skills", "obra/superpowers", "cursor/plugins",
    "affaan-m/ECC", "alibaba/open-code-review", "Tencent/LoopForge",
    "backnotprop/plannotator", "tradermonty/claude-trading-skills",
    "google-labs-code/stitch-skills",
]

KEY = [
    "affaan-m/ECC", "GoogleChrome/modern-web-guidance-src",
    "google-research/paper-orchestra", "backnotprop/plannotator",
    "alibaba/open-code-review", "Tencent/LoopForge",
    "elementalsouls/Claude-BugHunter", "mvanhorn/last30days-skill",
    "vercel-labs/agent-browser",
]


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def harness_of(tree):
    """Which harness-specific manifests does the tree contain?"""
    dirs = Counter()
    files = Counter()
    for b in (tree.get("tree") or []):
        p = b.get("path") or ""
        if b.get("type") != "blob":
            continue
        for h in (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".plugin",
                  ".grok-plugin", ".gemini", ".windsurf", ".opencode", ".codebuddy",
                  ".kiro", ".agents", ".cursor"):
            if p.startswith(h + "/"):
                dirs[h] += 1
                if "/" not in p[len(h) + 1:]:
                    files[h] += 1
                break
    return dirs, files


def measure(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") or "" for b in blobs]
    dirs, files = harness_of(tree)
    npx = "npx skills add" in rm
    mkt = "marketplace add" in rm
    return {
        "repo": full,
        "npx_skills_add": npx,
        "marketplace_add": mkt,
        "both": npx and mkt,
        "harness_dirs": sorted(dirs),
        "n_harness_dirs": len(dirs),
        "n_harness_root_manifests": sum(files.values()),
        "n_skills": sum(1 for p in paths if os.path.basename(p) == "SKILL.md"),
        "n_blobs": len(blobs),
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "topics": m.get("topics", []),
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "archived": m.get("archived"),
        "has_discussions": m.get("has_discussions"),
        "has_wiki": m.get("has_wiki"),
        "workflows": sorted(p for p in paths if p.startswith(".github/workflows/")),
        "n_workflows": sum(1 for p in paths if p.startswith(".github/workflows/")),
    }


def contributors(full, n=15):
    c = api(f"repos/{full}/contributors", {"per_page": n}) or []
    if not isinstance(c, list):
        return []
    return [{"login": x.get("login"), "contributions": x.get("contributions"),
             "type": x.get("type")} for x in c]


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "same17"

    if which in ("same17", "all"):
        print("========== install-protocol continuity (same 17 repos as 11-17) ==========")
        rows = []
        with ThreadPoolExecutor(max_workers=5) as ex:
            for r in ex.map(measure, SAME_17):
                rows.append(r)
                print(f"  {r['repo']:<44} npx={int(r['npx_skills_add'])} "
                      f"mkt={int(r['marketplace_add'])} both={int(r['both'])} "
                      f"harness_dirs={r['n_harness_dirs']:<2} "
                      f"manifests={r['n_harness_root_manifests']:<2} "
                      f"skills={r['n_skills']:<5} ⭐{r['stars']}", flush=True)
        b = sum(1 for r in rows if r["both"])
        n = len(rows)
        print(f"\n  BOTH install commands: {b}/{n}")
        print(f"  npx only: {sum(1 for r in rows if r['npx_skills_add'] and not r['marketplace_add'])}")
        print(f"  marketplace only: {sum(1 for r in rows if r['marketplace_add'] and not r['npx_skills_add'])}")
        print(f"  neither: {sum(1 for r in rows if not r['both'] and not r['npx_skills_add'] and not r['marketplace_add'])}")
        print(f"  >=3 harness dirs: {sum(1 for r in rows if r['n_harness_dirs'] >= 3)}/{n}")
        print(f"  >=2 harness dirs: {sum(1 for r in rows if r['n_harness_dirs'] >= 2)}/{n}")
        json.dump(rows, open("/tmp/install_same17_1121.json", "w"),
                  ensure_ascii=False, indent=1)

    if which in ("key", "all"):
        print("\n\n========== KEY project metadata ==========")
        with ThreadPoolExecutor(max_workers=5) as ex:
            for r in ex.map(measure, KEY):
                print(f"\n--- {r['repo']} ---")
                for k in ("stars", "forks", "subs", "oi", "size_kb", "language",
                          "license", "created_at", "pushed_at", "n_blobs",
                          "n_skills", "n_workflows", "n_harness_dirs",
                          "harness_dirs", "archived", "has_discussions",
                          "homepage"):
                    print(f"    {k} = {r[k]}")
                print(f"    description = {r['description']}")
                print(f"    topics = {r['topics'][:12]}")
                print(f"    workflows = {r['workflows'][:12]}")
                cs = contributors(r["repo"])
                print(f"    contributors = {cs[:8]}")
                r["contributors"] = cs
            json.dump(rows if False else [], open("/tmp/x.json", "w"))
