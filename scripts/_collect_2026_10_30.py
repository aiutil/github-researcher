#!/usr/bin/env python3
"""2026-10-30 数据采集（一次性）。候选发现 + 元数据核验。"""
import json, subprocess, re, sys, os

def gh(args):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True)
    if r.returncode != 0:
        return {"__error__": r.stderr.strip()[:300]}
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"__raw__": r.stdout[:2000]}

def gh_raw(args):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""

def exact_commits(full):
    out = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                         capture_output=True, text=True).stdout
    m = re.search(r'<https://api\.github\.com/[^>]*[?&]page=(\d+)>;\s*rel="last"', out)
    if m:
        return int(m.group(1))
    body = out.split("\r\n\r\n", 1)[-1]
    try:
        return len(json.loads(body))
    except Exception:
        return None

def repo(full):
    return gh([f"repos/{full}"])

def tree(full, recursive=False):
    p = f"repos/{full}/git/trees/HEAD" + ("?recursive=1" if recursive else "")
    return gh([p])

def contributors(full):
    r = gh([f"repos/{full}/contributors?per_page=100"])
    return len(r) if isinstance(r, list) else None

def releases(full):
    r = gh([f"repos/{full}/releases?per_page=30"])
    return r if isinstance(r, list) else []

def issues(full, n=30):
    r = gh([f"repos/{full}/issues?state=all&per_page={n}"])
    return r if isinstance(r, list) else []

def blob_sha(full, path):
    r = gh([f"repos/{full}/contents/{path}"])
    return r.get("sha") if isinstance(r, dict) else None

def summarize(full):
    r = repo(full)
    if "__error__" in r:
        return {"full_name": full, "error": r["__error__"]}
    t = tree(full)
    tr = tree(full, recursive=True)
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
        "topics": r.get("topics") or [],
        "owner_type": (r.get("owner") or {}).get("type"),
        "desc": (r.get("description") or "")[:250],
        "homepage": r.get("homepage"),
        "archived": r.get("archived"),
        "commits": exact_commits(full),
        "contributors": contributors(full),
        "releases_n": len(releases(full)),
        "root_files": [x["path"] for x in (t.get("tree") or []) if x.get("type") == "blob"][:40] if isinstance(t, dict) else [],
        "tree_n": len(tr.get("tree") or []) if isinstance(tr, dict) else None,
        "truncated": (tr.get("truncated") if isinstance(tr, dict) else None),
        "file_count": sum(1 for x in (tr.get("tree") or []) if x.get("type") == "blob") if isinstance(tr, dict) else None,
    }

def search(q, n=100):
    from urllib.parse import quote
    r = gh([f"search/repositories?q={quote(q, safe=':>=<,')}&sort=stars&order=desc&per_page={n}"])
    if not isinstance(r, dict):
        return []
    return [i["full_name"] for i in r.get("items", [])]

def owner_info(owner):
    r = gh([f"users/{owner}"])
    if "__error__" in r:
        return {"login": owner, "error": r["__error__"]}
    return {"login": r.get("login"), "type": r.get("type"), "created": r.get("created_at"),
            "repos": r.get("public_repos"), "followers": r.get("followers"),
            "name": r.get("name")}

def out_path(default):
    import sys as _s
    for i, a in enumerate(_s.argv):
        if a == "--out" and i + 1 < len(_s.argv):
            return _s.argv[i + 1]
    return default

if __name__ == "__main__":
    mode = sys.argv[1]
    argv = [a for i, a in enumerate(sys.argv) if not (a == "--out" or (i > 0 and sys.argv[i - 1] == "--out"))]
    out = {}
    if mode == "discover":
        queries = {
            "new3d": "created:2026-10-27..2026-10-29 stars:>=40",
            "new5d": "created:2026-10-25..2026-10-29 stars:>=150",
            "recent_push": "pushed:>2026-10-28 stars:>=300",
        }
        for k, q in queries.items():
            out[k] = search(q)
            print(f"# {k}: {len(out[k])}", file=sys.stderr)
        json.dump(out, open("/tmp/discover_1030.json", "w"), ensure_ascii=False, indent=1)
    elif mode == "repos":
        fulls = argv[2:]
        out = {}
        for f in fulls:
            out[f] = summarize(f)
            print(f"done {f}", file=sys.stderr)
        json.dump(out, open(out_path("/tmp/repos_1030.json"), "w"), ensure_ascii=False, indent=1)
    elif mode == "owners":
        for o in argv[2:]:
            out[o] = owner_info(o)
        json.dump(out, open("/tmp/owners_1030.json", "w"), ensure_ascii=False, indent=1)
    elif mode == "issues":
        for f in argv[2:]:
            out[f] = [{"number": i.get("number"), "title": i.get("title"),
                       "state": i.get("state"), "created": i.get("created_at"),
                       "user": (i.get("user") or {}).get("login"),
                       "body": (i.get("body") or "")[:900],
                       "is_pr": "pull_request" in i} for i in issues(f)]
            print(f"issues {f}", file=sys.stderr)
        json.dump(out, open(out_path("/tmp/issues_1030.json"), "w"), ensure_ascii=False, indent=1)
    elif mode == "commits":
        for f in argv[2:]:
            r = gh([f"repos/{f}/commits?per_page=30"])
            out[f] = [{"sha": c["sha"][:8], "date": c["commit"]["committer"]["date"],
                        "msg": c["commit"]["message"].split("\n")[0][:220],
                        "author": (c.get("author") or {}).get("login")} for c in r] if isinstance(r, list) else []
            print(f"commits {f}", file=sys.stderr)
        json.dump(out, open(out_path("/tmp/commits_1030.json"), "w"), ensure_ascii=False, indent=1)
    elif mode == "blob":
        for pair in argv[2:]:
            full, path = pair.split("::")
            out[pair] = blob_sha(full, path)
        json.dump(out, open(out_path("/tmp/blob_1030.json"), "w"), ensure_ascii=False, indent=1)
    elif mode == "raw":
        for pair in argv[2:]:
            full, path = pair.split("::")
            out[pair] = gh_raw([f"repos/{full}/contents/{path}", "-H", "Accept: application/vnd.github.raw"])[:12000]
        json.dump(out, open(out_path("/tmp/raw_1030.json"), "w"), ensure_ascii=False, indent=1)
