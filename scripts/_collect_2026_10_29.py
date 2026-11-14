#!/usr/bin/env python3
"""2026-10-29 数据采集辅助脚本（一次性）。"""
import json, subprocess, sys, os

def gh(args):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True)
    if r.returncode != 0:
        return {"__error__": r.stderr.strip()[:300]}
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"__raw__": r.stdout[:2000]}

def repo(full):
    return gh([f"repos/{full}"])

def tree(full, recursive=False):
    p = f"repos/{full}/git/trees/HEAD" + ("?recursive=1" if recursive else "")
    return gh([p])

def commits(full, n=100):
    return gh([f"repos/{full}/commits?per_page={n}"])

def contributors(full):
    return gh([f"repos/{full}/contributors?per_page=100"])

def releases(full):
    return gh([f"repos/{full}/releases?per_page=30"])

def issues(full, state="all", n=30):
    return gh([f"repos/{full}/issues?state={state}&per_page={n}"])

def raw(full, path):
    return gh([f"repos/{full}/contents/{path}", "-H", "Accept: application/vnd.github.raw"])

def summary(full):
    r = repo(full)
    if "__error__" in r:
        return {"full_name": full, "error": r["__error__"]}
    t = tree(full)
    tree_items = t.get("tree", []) if isinstance(t, dict) else []
    cm = commits(full)
    ct = contributors(full)
    rl = releases(full)
    return {
        "full_name": full,
        "stars": r.get("stargazers_count"),
        "forks": r.get("forks_count"),
        "subs": r.get("subscribers_count"),
        "oi": r.get("open_issues_count"),
        "size": r.get("size"),
        "lang": r.get("language"),
        "lic": (r.get("license") or {}).get("spdx_id"),
        "created": r.get("created_at"),
        "pushed": r.get("pushed_at"),
        "topics": len(r.get("topics") or []),
        "owner_type": r.get("owner", {}).get("type"),
        "desc": (r.get("description") or "")[:200],
        "homepage": r.get("homepage"),
        "archived": r.get("archived"),
        "default_branch": r.get("default_branch"),
        "tree_truncated": t.get("truncated") if isinstance(t, dict) else None,
        "tree_n": len(tree_items),
        "tree_top": [x["path"] for x in tree_items][:60],
        "commits_len": len(cm) if isinstance(cm, list) else cm,
        "contrib_n": len(ct) if isinstance(ct, list) else ct,
        "contrib_logins": [c.get("login") for c in ct] if isinstance(ct, list) else [],
        "releases_n": len(rl) if isinstance(rl, list) else rl,
        "releases_list": [{"tag": x.get("tag_name"), "pub": x.get("published_at"),
                           "assets": len(x.get("assets") or [])} for x in rl] if isinstance(rl, list) else [],
    }

if __name__ == "__main__":
    out = {}
    for full in sys.argv[1:]:
        out[full] = summary(full)
    print(json.dumps(out, ensure_ascii=False, indent=1))
