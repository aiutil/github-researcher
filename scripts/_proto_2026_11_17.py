#!/usr/bin/env python3
"""Quantify the 'Agent Skills install protocol' trend across the tracked
set, and finish the ffmpeg-skill release-vs-code-change verification.

Q1  How many of the agent-skill repos publish the SAME two install commands
    (`npx skills add <owner>/<repo>` and `/plugin marketplace add <owner>/<repo>`)?
    If the format has converged, both should appear verbatim.

Q2  For kajisho5/ffmpeg-skill, list ALL files touched by each sampled tagged
    commit (the earlier run only printed the first 5) so we can tell whether
    the tagged commit is metadata-only or carries code.
"""
import json
import os
import re
import subprocess
import urllib.parse

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


SKILL_REPOS = [
    "anthropics/skills",
    "addyosmani/agent-skills",
    "mvanhorn/last30days-skill",
    "boringmarketer/boring-marketing-skills",
    "elementalsouls/Claude-BugHunter",
    "kajisho5/ffmpeg-skill",
    "google-labs-code/stitch-skills",
    "tradermonty/claude-trading-skills",
    "asimawdah/material-expressive-skill",
    "NVIDIA/SkillEvaluator",
    "google/elephant-goldfish-model",
    "ag-ui-protocol/ag-ui",
    "vercel-labs/agent-browser",
    "google-research/paper-orchestra",
    "CoderL98/hghub-plugins",
]

MARKERS = {
    "npx skills add": r"npx\s+skills\s+add",
    "plugin marketplace add": r"/plugin\s+marketplace\s+add",
    "plugin install": r"/plugin\s+install",
    "SKILL.md mention": r"SKILL\.md",
    "claude-plugin manifest": r"\.claude-plugin/",
    "cursor-plugin manifest": r"\.cursor-plugin/",
    "MCP tools/list": r"tools/list",
    "frontmatter yaml": r"^---\s*$",
}


def q1():
    print("=" * 100)
    print("Q1  install-protocol convergence across agent-skill repos")
    print("=" * 100)
    rows = []
    for full in SKILL_REPOS:
        rm = api(f"repos/{full}/readme", raw=True,
                 headers=["Accept: application/vnd.github.raw"]) or ""
        m = api(f"repos/{full}") or {}
        tree = api(f"repos/{full}/git/trees/{m.get('default_branch') or 'main'}?recursive=1") or {}
        paths = [b.get("path") for b in (tree.get("tree") or []) if b.get("type") == "blob"]
        n_skill_md = sum(1 for p in paths if p.endswith("SKILL.md"))
        hit = {k: bool(re.search(v, rm, re.M)) for k, v in MARKERS.items()}
        rows.append({"repo": full, "readme_len": len(rm), "n_skill_md": n_skill_md,
                     "n_blobs": len(paths), "markers": hit,
                     "stars": m.get("stargazers_count"),
                     "created": m.get("created_at")})
        print(f"{full:<44} ⭐{m.get('stargazers_count'):<7} SKILL.md={n_skill_md:<4} "
              f"blobs={len(paths):<5} readme={len(rm)}")
        print("      " + "  ".join(f"{k}={'Y' if v else '.'}" for k, v in hit.items()))
    both = [r for r in rows if r["markers"]["npx skills add"]
            and r["markers"]["plugin marketplace add"]]
    print(f"\n  repos publishing BOTH `npx skills add` AND `/plugin marketplace add`: "
          f"{len(both)}/{len(rows)}")
    for r in both:
        print(f"    - {r['repo']}")
    json.dump(rows, open("/tmp/install_proto_1117.json", "w"),
              ensure_ascii=False, indent=1)


def q2():
    print("\n" + "=" * 100)
    print("Q2  kajisho5/ffmpeg-skill: full file list per tagged commit")
    print("=" * 100)
    full = "kajisho5/ffmpeg-skill"
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    sample = [tags[i] for i in (0, 1, 2, 25, 50, 75, 98, 99)]
    code_hits = 0
    for t in sample:
        sha = t["commit"]["sha"]
        c = api(f"repos/{full}/commits/{sha}") or {}
        files = [(f["filename"], f.get("status"), f.get("additions"), f.get("deletions"))
                 for f in (c.get("files") or [])]
        codeish = [f for f in files
                   if re.search(r"\.(py|js|mjs|ts|sh)$", f[0])
                   or f[0].startswith("tools/") or f[0].startswith("scripts/")]
        if codeish:
            code_hits += 1
        msg = ((c.get("commit") or {}).get("message") or "").split("\n")[0]
        print(f"\n  {t['name']:<10} {sha[:8]}  {msg[:70]}")
        print(f"    total files={len(files)}  code-ish={len(codeish)}")
        for f in files:
            mark = "CODE" if f in codeish else "meta"
            print(f"      [{mark}] {f[0]:<52} {f[1]} +{f[2]}/-{f[3]}")
    print(f"\n  sampled tags whose tagged commit touches source files: "
          f"{code_hits}/{len(sample)}")

    # Are the real fix/feat commits always immediately BEFORE the release commit?
    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    seq = []
    for c in commits:
        cm = c.get("commit") or {}
        au = cm.get("author") or {}
        msg = (cm.get("message") or "").split("\n")[0]
        seq.append((au.get("date"), msg, (c.get("sha") or "")[:8]))
    pairs = 0
    for i in range(len(seq) - 1):
        if seq[i][1].startswith("chore(release)") and seq[i + 1][1].startswith(("fix:", "feat:")):
            pairs += 1
    print(f"  release-commit immediately preceded by a fix:/feat: commit: "
          f"{pairs} of the {sum(1 for s in seq if s[1].startswith('chore(release)'))} "
          f"release commits in the last 100")


if __name__ == "__main__":
    q1()
    q2()
