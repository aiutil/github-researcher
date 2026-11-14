#!/usr/bin/env python3
"""Fetch detailed evidence for specific repos: owner meta, tree, README, license, releases."""
import json
import os
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:300]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:300]}"


def one(full):
    owner = full.split("/")[0]
    m, _ = api(f"repos/{full}")
    m = m or {}
    u, _ = api(f"users/{owner}")
    u = u or {}
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    tree, _ = api(f"repos/{full}/git/trees/{m.get('default_branch')}?recursive=1")
    entries = (tree or {}).get("tree") or []
    files = [e["path"] for e in entries if e.get("type") == "blob"]
    rel, _ = api(f"repos/{full}/releases", {"per_page": 100})
    tags, _ = api(f"repos/{full}/tags", {"per_page": 20})
    lic_raw, _ = api(f"repos/{full}/license", raw=True, headers=["Accept: application/vnd.github.raw"])
    return {
        "full_name": full,
        "meta": {k: m.get(k) for k in ("stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
                                       "size", "language", "created_at", "pushed_at", "fork", "archived",
                                       "description", "homepage", "default_branch", "has_discussions", "is_template")},
        "parent": (m.get("parent") or {}).get("full_name"),
        "source": (m.get("source") or {}).get("full_name"),
        "topics": m.get("topics", []),
        "license": (m.get("license") or {}).get("spdx_id"),
        "owner": {"login": owner, "type": u.get("type"), "created_at": u.get("created_at"),
                  "public_repos": u.get("public_repos"), "followers": u.get("followers"),
                  "name": u.get("name"), "bio": u.get("bio")},
        "nfiles": len(files),
        "files": files[:80],
        "readme_len": len(rm or ""),
        "readme": (rm or "")[:4000],
        "readme_md5": __import__("hashlib").md5((rm or "").encode()).hexdigest(),
        "license_head": (lic_raw or "")[:300],
        "releases": [r.get("tag_name") for r in rel] if isinstance(rel, list) else [],
        "tags": [t.get("name") for t in tags] if isinstance(tags, list) else [],
    }


if __name__ == "__main__":
    repos = sys.argv[1:]
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(one, repos))
    json.dump(res, open("/tmp/evidence.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(res)} -> /tmp/evidence.json")
