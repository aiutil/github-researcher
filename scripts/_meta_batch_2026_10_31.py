#!/usr/bin/env python3
"""Fetch metadata for backlog + anomaly candidates."""
import json, subprocess, os, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def japi(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


TARGETS = sys.argv[1:]
for full in TARGETS:
    repo = japi(f"repos/{full}")
    if not repo:
        print(f"{full}: FAILED")
        continue
    contrib = japi(f"repos/{full}/contributors?per_page=100")
    rel = japi(f"repos/{full}/releases?per_page=30")
    cm = japi(f"repos/{full}/commits?per_page=6")
    iss = japi(f"repos/{full}/issues?state=all&per_page=10")
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1")
    owner = repo["owner"]["login"]
    org = japi(f"users/{owner}") or {}
    out = {
        "full_name": full,
        "stars": repo["stargazers_count"], "forks": repo["forks_count"],
        "subs": repo["subscribers_count"], "oi": repo["open_issues_count"],
        "size_kb": repo["size"], "lang": repo["language"],
        "lic": (repo.get("license") or {}).get("spdx_id"),
        "created": repo["created_at"], "pushed": repo["pushed_at"],
        "topics": repo.get("topics", []),
        "contributors": len(contrib) if isinstance(contrib, list) else None,
        "releases": len(rel) if isinstance(rel, list) else None,
        "release_assets": sum(len(r.get("assets", [])) for r in rel) if isinstance(rel, list) else 0,
        "owner_type": repo["owner"]["type"], "owner_created": org.get("created_at"),
        "owner_repos": org.get("public_repos"), "owner_followers": org.get("followers"),
        "desc": repo.get("description"),
        "fork": repo.get("fork"), "homepage": repo.get("homepage"),
        "tree_entries": len(tree.get("tree", [])) if tree and "tree" in tree else None,
        "recent_commits": [f"{c['commit']['author']['date']} {c['commit']['message'].splitlines()[0][:80]}" for c in (cm or [])[:6]],
        "issues": [f"#{i['number']} [{i['state']}] {i['title'][:75]}" for i in (iss or []) if "pull_request" not in i][:8],
    }
    print(json.dumps(out, ensure_ascii=False))
