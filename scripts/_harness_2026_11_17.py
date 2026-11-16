#!/usr/bin/env python3
"""Quantify the multi-harness plugin-manifest spread — the core evidence for
the 'Agent Skills has become a portability package format' claim."""
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")


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


REPOS = [
    "anthropics/skills", "addyosmani/agent-skills", "mvanhorn/last30days-skill",
    "boringmarketer/boring-marketing-skills", "elementalsouls/Claude-BugHunter",
    "kajisho5/ffmpeg-skill", "google-labs-code/stitch-skills",
    "tradermonty/claude-trading-skills", "asimawdah/material-expressive-skill",
    "NVIDIA/SkillEvaluator", "google/elephant-goldfish-model",
    "ag-ui-protocol/ag-ui", "vercel-labs/agent-browser",
    "google-research/paper-orchestra", "openai/codex-security",
    "sherlock-project/sherlock", "QwenLM/qwen-code",
]

HARNESS_DIR = re.compile(
    r"^\.([a-z0-9\-\.]+)-plugin/(marketplace\.)?plugin\.json$|"
    r"^(gemini-extension|server|plugin)\.json$|"
    r"^\.gemini/(config\.yaml|styleguide\.md)$")


def harness_of(path):
    if path.startswith(".claude-plugin/") or path == ".claude/settings.json":
        return "claude-code"
    if path.startswith(".cursor-plugin/"):
        return "cursor"
    if path.startswith(".codex-plugin/"):
        return "codex"
    if path.startswith(".grok-plugin/"):
        return "grok"
    if path.startswith(".plugin/"):
        return "opencode/omp"
    if path == ".gemini/config.yaml":
        return "gemini-cli"
    if path == "gemini-extension.json":
        return "gemini-ext"
    if path == "server.json":
        return "mcp-server"
    if path == ".mcp.json":
        return "mcp"
    if path.startswith(".opencode/"):
        return "opencode"
    if path.startswith(".windsurf/"):
        return "windsurf"
    if path.startswith(".antigravity/"):
        return "antigravity"
    return None


if __name__ == "__main__":
    rows = []
    for full in REPOS:
        m = api(f"repos/{full}") or {}
        tree = api(f"repos/{full}/git/trees/{m.get('default_branch') or 'main'}?recursive=1") or {}
        paths = [b.get("path") for b in (tree.get("tree") or []) if b.get("type") == "blob"]
        harnesses = sorted({harness_of(p) for p in paths if harness_of(p)})
        n_skill = sum(1 for p in paths if p.endswith("SKILL.md"))
        rows.append({"repo": full, "stars": m.get("stargazers_count"),
                     "n_skill": n_skill, "harnesses": harnesses,
                     "n_harnesses": len(harnesses),
                     "plugin_manifests": [p for p in paths
                                         if p.endswith("plugin.json")
                                         or p.endswith("marketplace.json")
                                         or p in ("gemini-extension.json", "server.json")][:12]})
        print(f"{full:<44} ⭐{m.get('stargazers_count'):<7} SKILL.md={n_skill:<4} "
              f"harnesses({len(harnesses)})={','.join(h for h in harnesses if h)}")
        print(f"      manifests: {rows[-1]['plugin_manifests']}")
    print("\n=== harness coverage distribution ===")
    c = Counter(r["n_harnesses"] for r in rows)
    for k in sorted(c):
        print(f"  {k} harness manifests: {c[k]} repos")
    print("\n=== repos with >=3 distinct harness manifests ===")
    for r in sorted(rows, key=lambda r: -r["n_harnesses"]):
        if r["n_harnesses"] >= 3:
            print(f"  {r['repo']:<44} {r['n_harnesses']}  {','.join(h for h in r['harnesses'] if h)}")
    multi = sum(1 for r in rows if r["n_harnesses"] >= 3)
    print(f"\n  {multi}/{len(rows)} repos ship >=3 harness-specific manifests")
    print(f"  repos shipping a SKILL.md: {sum(1 for r in rows if r['n_skill']>0)}/{len(rows)}")
    json.dump(rows, open("/tmp/harness_1117.json", "w"), ensure_ascii=False, indent=1)
