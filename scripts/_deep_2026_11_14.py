#!/usr/bin/env python3
"""Deep-dive: owner account metadata + repo trees for the top candidates."""
import json
import os
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

CAND = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1114.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/deep_1114.json"
TOP_N = int(sys.argv[3]) if len(sys.argv) > 3 else 60

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
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:200]}"


def main():
    data = json.load(open(CAND, encoding="utf-8"))
    data.sort(key=lambda r: -r["stars"])
    top = data[:TOP_N]

    def work(r):
        full = r["full_name"]
        owner_login = r["full_name"].split("/")[0]
        u, _ = api(f"users/{owner_login}")
        u = u or {}
        tree, _ = api(f"repos/{full}/git/trees/{r['default_branch']}?recursive=1")
        entries = (tree or {}).get("tree") or []
        blobs = [e for e in entries if e.get("type") == "blob"]
        exts = {}
        for e in blobs:
            p = e.get("path", "")
            if "." in p.rsplit("/", 1)[-1]:
                ext = p.rsplit(".", 1)[-1].lower()
                exts[ext] = exts.get(ext, 0) + 1
        top_exts = sorted(exts.items(), key=lambda kv: -kv[1])[:8]
        files = [e["path"] for e in blobs]
        dirs = sorted({os.path.dirname(f) for f in files if "/" in f})
        rel, _ = api(f"repos/{full}/releases/latest")
        return {
            "full_name": full,
            "stars": r["stars"],
            "owner_login": owner_login,
            "owner_type": u.get("type"),
            "owner_created": u.get("created_at"),
            "owner_repos": u.get("public_repos"),
            "owner_followers": u.get("followers"),
            "owner_bio": u.get("bio"),
            "owner_name": u.get("name"),
            "nblobs": len(blobs),
            "tree_truncated": (tree or {}).get("truncated"),
            "top_exts": top_exts,
            "top_files": files[:60],
            "dirs": dirs[:40],
            "release": (rel or {}).get("tag_name") if isinstance(rel, dict) else None,
            "release_count": 0,
            "size_kb": r["size_kb"],
            "ncommits": r["ncommits"],
            "forks": r["forks"],
            "subs": r["subs"],
            "oi": r["oi"],
            "license": r["license"],
            "language": r["language"],
            "topics": r["topics"],
            "desc": r["desc"],
            "homepage": r["homepage"],
            "created_at": r["created_at"],
            "pushed_at": r["pushed_at"],
            "fork": r["fork"],
            "parent": r["parent"],
            "readme_len": r["readme_len"],
            "readme_head": r["readme_head"],
        }

    with ThreadPoolExecutor(max_workers=5) as ex:
        res = list(ex.map(work, top))

    # release counts
    def rc(r):
        rel, _ = api(f"repos/{r['full_name']}/releases", {"per_page": 100})
        r["release_count"] = len(rel) if isinstance(rel, list) else 0
        return r

    with ThreadPoolExecutor(max_workers=5) as ex:
        res = list(ex.map(rc, res))

    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(res)} -> {OUT}")


if __name__ == "__main__":
    main()
