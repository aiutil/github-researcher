#!/usr/bin/env python3
"""Dump READMEs + metadata for projects needing profiles. Saves to /tmp/rd_<slug>.md"""
import json, subprocess, os, sys, re

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def raw(path):
    r = subprocess.run(["gh", "api", path, "-H", "Accept:application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


def slugify(full):
    return re.sub(r"[^a-z0-9]+", "-", full.lower()).strip("-")


os.makedirs("/tmp/rd", exist_ok=True)
for full in sys.argv[1:]:
    slug = slugify(full)
    rd = raw(f"repos/{full}/readme") or ""
    with open(f"/tmp/rd/{slug}.md", "w") as f:
        f.write(rd)
    repo = japi(f"repos/{full}") or {}
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    paths = [e["path"] for e in tree.get("tree", []) if e["type"] == "blob"]
    meta = {
        "full": full, "stars": repo.get("stargazers_count"), "forks": repo.get("forks_count"),
        "subs": repo.get("subscribers_count"), "oi": repo.get("open_issues_count"),
        "size": repo.get("size"), "lang": repo.get("language"),
        "lic": (repo.get("license") or {}).get("spdx_id"),
        "created": repo.get("created_at"), "pushed": repo.get("pushed_at"),
        "topics": repo.get("topics"), "readme_bytes": len(rd), "tree_blobs": len(paths),
        "doc_paths": [p for p in paths if re.search(r"(?i)(docs/|/doc/|\.md$|LICENSE|NOTICE|SECURITY|CONTRIBUT|AGENTS)", p)][:60],
    }
    with open(f"/tmp/rd/{slug}.json", "w") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print(f"{full}: readme={len(rd)}B blobs={len(paths)} -> /tmp/rd/{slug}.md")
