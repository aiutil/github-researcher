#!/usr/bin/env python3
"""Same-caliber re-test of the 2026-11-18 / 2026-11-17 skill cohort.

Calibers are copied verbatim from the earlier scripts so the numbers are
directly comparable with the tables published on 11-17 and 11-18:

  * skill identity  -> parent-directory BASENAME (scripts/_identity_2026_11_18.py)
  * harness count   -> manifest-file patterns (scripts/_harness_2026_11_17.py)

Output: /tmp/caliber_1120.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/caliber_1120.json"

COHORT = [
    "anthropics/skills", "addyosmani/agent-skills", "mvanhorn/last30days-skill",
    "elementalsouls/Claude-BugHunter", "kajisho5/ffmpeg-skill",
    "google-labs-code/stitch-skills", "tradermonty/claude-trading-skills",
    "ag-ui-protocol/ag-ui", "affaan-m/ECC", "Tencent/LoopForge",
    "backnotprop/plannotator", "cursor/plugins", "alibaba/open-code-review",
    "obra/superpowers",
]


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


# --- harness detection, verbatim from scripts/_harness_2026_11_17.py ---
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
    if path.startswith(".codebuddy/"):
        return "codebuddy"
    if path.startswith(".kiro/"):
        return "kiro"
    if path.startswith(".agents/"):
        return "agents"
    if path.startswith(".agents/"):
        return "agents"
    if path.startswith(".antigravity/"):
        return "antigravity"
    return None


def probe(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") or "" for b in blobs]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    # identity = parent directory BASENAME
    ident = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        parent = os.path.basename(os.path.dirname(p)) if p else ""
        ident[parent].append((p, b.get("sha"), b.get("size")))
    n_ident = len(ident)
    replica_groups = sum(1 for v in ident.values() if len(v) > 1)
    replica_files = sum(len(v) for v in ident.values() if len(v) > 1)
    max_rep = max([len(v) for v in ident.values()] or [0])
    sha_c = Counter(b.get("sha") for b in skills)
    dup_sha = {s: c for s, c in sha_c.items() if c > 1}
    harn = sorted({h for h in (harness_of(p) for p in paths) if h})
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    cmds = sorted({c for c in re.findall(
        r"(npx\s+skills\s+add[^\n`\"]{0,80}|marketplace\s+add[^\n`\"]{0,80})", rm)})
    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "n_blobs": len(blobs),
        "n_skill_files": len(skills),
        "n_skill_identities": n_ident,
        "replication": round(len(skills) / n_ident, 2) if n_ident else 0,
        "replica_groups": replica_groups,
        "replica_files": replica_files,
        "max_replica": max_rep,
        "n_distinct_sha": len(sha_c),
        "n_dup_sha": len(dup_sha),
        "harness": harn,
        "n_harness": len(harn),
        "npx": any("skills add" in c for c in cmds),
        "mkt": any("marketplace" in c for c in cmds),
        "install_cmds": cmds,
        "top_identities": sorted(
            ((k, len(v)) for k, v in ident.items()), key=lambda kv: -kv[1])[:6],
        "skill_dirs": sorted(ident.keys())[:400],
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for r in ex.map(probe, COHORT):
            out.append(r)
            print(f"{r['repo']:42s} sk={r['n_skill_files']:>5} id={r['n_skill_identities']:>5} "
                  f"repl={r['replication']:>5} harn={r['n_harness']:>2} {r['harness']} "
                  f"npx={r['npx']} mkt={r['mkt']} blobs={r['n_blobs']}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
