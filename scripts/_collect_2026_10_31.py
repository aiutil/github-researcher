#!/usr/bin/env python3
"""Collect GitHub metadata for 2026-10-31 candidate projects (evidence gathering only)."""
import json, subprocess, sys, os

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


CANDS = [
    "heydamir/unslop",
    "BryceYuuu/RUN",
    "kevinraymond/florilegium",
    "soimy/c3rb3r-rescue",
    "Pika-Labs/Pika-H3-Flex",
    "0xCodez/cleanly",
    "VortexSo4/Weft",
    "tapoooooty/hypergrad",
    "jefferysha0627/agent-office-3d",
    "TomAnthony/YourOwnWeigh",
    "dbreunig/nesformer",
    "patch-gg/pixelfx",
    "wangzan101/Mika",
    "paipiange/nvzhuang",
    "Djihads80/Eglantine",
    "sleepy-zone/ai-ref-library-cn",
    "MarkBlah/smsofdeath",
    "wquguru/shisei",
    "0xCodez/cleanly",
    "NiazMorshed2007/reanimate",
]

seen = set()
for full in CANDS:
    if full in seen:
        continue
    seen.add(full)
    repo = api(f"repos/{full}")
    if not repo:
        print(f"{full}: FAILED")
        continue
    commits = api(f"repos/{full}/commits?per_page=1")
    ncommits = 0
    if commits:
        link = ""
        # count via link header is not available via gh api --jq; use contributors instead
        pass
    contrib = api(f"repos/{full}/contributors?per_page=100&anon=false")
    ncontrib = len(contrib) if isinstance(contrib, list) else None
    releases = api(f"repos/{full}/releases?per_page=100")
    nrel = len(releases) if isinstance(releases, list) else None
    assetcount = sum(len(r.get("assets", [])) for r in releases) if isinstance(releases, list) else 0
    lic = (repo.get("license") or {}).get("spdx_id")
    out = {
        "full_name": repo["full_name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "subs": repo["subscribers_count"],
        "oi": repo["open_issues_count"],
        "size_kb": repo["size"],
        "lang": repo["language"],
        "license": lic,
        "created": repo["created_at"],
        "pushed": repo["pushed_at"],
        "updated": repo["updated_at"],
        "topics": repo.get("topics", []),
        "contributors": ncontrib,
        "releases": nrel,
        "release_assets": assetcount,
        "archived": repo.get("archived"),
        "fork": repo.get("fork"),
        "desc": (repo.get("description") or "")[:200],
        "homepage": repo.get("homepage"),
    }
    print(json.dumps(out, ensure_ascii=False))
