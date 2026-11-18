#!/usr/bin/env python3
"""Deep probe for 2026-11-18.

Applies the 11-17 criterion ("tag -> commit -> code diff chain closure") plus
release-vs-tag asymmetry to the interesting trending repos, and reads the
real tree / workflows / skill manifests of the top candidates.

Output: /tmp/deep_1118.json
"""

import json
import os
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/deep_1118.json"

TARGETS = [
    "obra/superpowers",
    "affaan-m/ECC",
    "alibaba/open-code-review",
    "google-research/paper-orchestra",
    "Tencent/LoopForge",
    "backnotprop/plannotator",
    "GoogleChrome/modern-web-guidance-src",
    "elementalsouls/Claude-BugHunter",
    "anthropics/skills",
    "cursor/plugins",
    "addyosmani/agent-skills",
    "tradermonty/claude-trading-skills",
    "we-promise/sure",
    "getarcaneapp/arcane",
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


def repo_detail(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") for b in blobs]

    def pick(pred, cap=25):
        return [p for p in paths if p and pred(p)][:cap]

    workflows = pick(lambda p: p.startswith(".github/workflows/"))
    skills = pick(lambda p: os.path.basename(p) == "SKILL.md", 40)
    manifests = pick(lambda p: os.path.basename(p) in (
        "plugin.json", "marketplace.json", "server.json", "gemini-extension.json",
        "config.yaml", "package.json", "Cargo.toml", "go.mod", "pyproject.toml",
        "requirements.txt", "docker-compose.yml", "Dockerfile"), 20)
    harness = pick(lambda p: p.startswith((".claude-plugin/", ".codex-plugin/",
                                           ".cursor-plugin/", ".plugin/",
                                           ".grok-plugin/", ".gemini/",
                                           ".windsurf/")), 40)

    # release / tag chain closure
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    if not isinstance(rel, list):
        rel = []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    if not isinstance(tags, list):
        tags = []

    sample = []
    for t in tags[:12]:
        sha = t.get("commit", {}).get("sha")
        if not sha:
            continue
        c = api(f"repos/{full}/commits/{sha}") or {}
        files = [f.get("filename") for f in (c.get("files") or [])]
        parent = (c.get("parents") or [{}])[0].get("sha")
        pfiles, psrc = [], 0
        if parent:
            pc = api(f"repos/{full}/commits/{parent}") or {}
            pfiles = [f.get("filename") for f in (pc.get("parents") or [])] or []
            pfiles = [f.get("filename") for f in (pc.get("files") or [])]
            psrc = sum(1 for f in pfiles if os.path.splitext(f)[1].lower() in
                       (".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".sh",
                        ".java", ".c", ".cpp", ".rb", ".php", ".swift", ".kt"))
        src = sum(1 for f in files if os.path.splitext(f)[1].lower() in
                  (".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".sh",
                   ".java", ".c", ".cpp", ".rb", ".php", ".swift", ".kt"))
        sample.append({
            "tag": t.get("name"), "sha": sha[:8],
            "c_files": len(files), "c_src": src,
            "c_list": files[:12],
            "parent": (parent or "")[:8], "p_files": len(pfiles), "p_src": psrc,
            "p_list": pfiles[:12],
        })

    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    if not isinstance(commits, list):
        commits = []
    secs = []
    for c in commits:
        au = (c.get("commit", {}) or {}).get("author", {}) or {}
        if au.get("date"):
            secs.append(au["date"])
    msgs = [(c.get("commit", {}) or {}).get("message", "").split("\n")[0][:70]
            for c in commits[:25]]

    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "topics": m.get("topics", []),
        "n_blobs": len(blobs),
        "truncated_tree": tree.get("truncated"),
        "workflows": workflows,
        "n_workflows": len(workflows),
        "skill_files": skills,
        "n_skills": len([p for p in paths if p and os.path.basename(p) == "SKILL.md"]),
        "manifests": manifests,
        "harness_dirs": harness,
        "n_releases": len(rel),
        "n_tags": len(tags),
        "release_assets": sum(len(r.get("assets") or []) for r in rel),
        "release_list": [{"tag": r.get("tag_name"), "at": r.get("published_at"),
                          "assets": len(r.get("assets") or []),
                          "pre": r.get("prerelease")} for r in rel[:8]],
        "tag_sample": sample,
        "commit_dates": sorted(secs, reverse=True)[:12],
        "commit_msgs": msgs,
        "n_commits_sampled": len(commits),
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(repo_detail, TARGETS), 1):
            out.append(r)
            print(f"[{i}/{len(TARGETS)}] {r['full_name']:<40} ⭐{r['stars']:<7} "
                  f"blob={r['n_blobs']:<6} skill={r['n_skills']:<4} "
                  f"wf={r['n_workflows']:<3} rel={r['n_releases']:<4} "
                  f"tag={r['n_tags']:<4}", flush=True)
    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(out)} -> {OUT}")


if __name__ == "__main__":
    main()
