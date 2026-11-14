#!/usr/bin/env python3
"""Evidence collection for 2026-11-06 daily. Read-only GitHub API."""
import json, subprocess, os, re, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}
OUT = "/tmp/collect_1106"
os.makedirs(OUT, exist_ok=True)


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


def ncommits(full):
    h = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                       capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    return int(m.group(1)) if m else 1


def meta(full):
    r = japi(f"repos/{full}")
    if not r:
        return None
    contrib = japi(f"repos/{full}/contributors?per_page=100&anon=false")
    rel = japi(f"repos/{full}/releases?per_page=100")
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    root = japi(f"repos/{full}/git/trees/HEAD") or {}
    blobs = [e for e in tree.get("tree", []) if e["type"] == "blob"]
    out = {
        "full": full,
        "stars": r["stargazers_count"], "forks": r["forks_count"],
        "subs": r["subscribers_count"], "oi": r["open_issues_count"],
        "size": r["size"], "lang": r["language"],
        "lic": (r.get("license") or {}).get("spdx_id"),
        "created": r["created_at"], "pushed": r["pushed_at"],
        "desc": r.get("description"), "homepage": r.get("homepage"),
        "topics": r.get("topics"), "archived": r["archived"],
        "owner_type": r["owner"]["type"], "owner_login": r["owner"]["login"],
        "ncontrib": len(contrib) if isinstance(contrib, list) else None,
        "nrel": len(rel) if isinstance(rel, list) else None,
        "rel_assets": sum(len(x.get("assets", [])) for x in rel) if isinstance(rel, list) else None,
        "ncommits": ncommits(full),
        "tree_truncated": tree.get("truncated"),
        "nblobs": len(blobs),
        "root": [e["path"] for e in root.get("tree", [])],
        "topics_count": len(r.get("topics") or []),
    }
    rd = api(f"repos/{full}/readme", raw=True)
    out["readme_len"] = len(rd) if rd else 0
    if rd:
        with open(f"{OUT}/{full.replace('/', '__')}.README.md", "w") as f:
            f.write(rd)
    with open(f"{OUT}/{full.replace('/', '__')}.meta.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


def show(d):
    if not d:
        print("  FAILED")
        return
    print(f"  {d['full']}")
    print(f"    stars={d['stars']} forks={d['forks']} subs={d['subs']} oi={d['oi']} size={d['size']}KB "
          f"lang={d['lang']} lic={d['lic']} readme_len={d['readme_len']}")
    print(f"    created={d['created']} pushed={d['pushed']} owner={d['owner_login']}({d['owner_type']}) "
          f"archived={d['archived']}")
    print(f"    commits={d['ncommits']} contributors={d['ncontrib']} releases={d['nrel']} "
          f"rel_assets={d['rel_assets']} blobs={d['nblobs']} truncated={d['tree_truncated']}")
    print(f"    desc={d['desc']}")
    print(f"    homepage={d['homepage']} topics={d['topics']}")
    print(f"    root({len(d['root'])}): {d['root'][:40]}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "meta"

    if mode == "meta":
        for t in sys.argv[2:]:
            show(meta(t))
            print("-" * 90)

    elif mode == "readme":
        for full in sys.argv[2:]:
            rd = api(f"repos/{full}/readme", raw=True)
            print("=" * 100)
            print("README:", full, "len=", len(rd) if rd else 0)
            print("=" * 100)
            print((rd or "")[:18000])

    elif mode == "contents":
        full, path = sys.argv[2], sys.argv[3]
        raw = api(f"repos/{full}/contents/{path}", raw=True)
        print((raw or "FAILED")[:14000])

    elif mode == "releases":
        for full in sys.argv[2:]:
            rel = japi(f"repos/{full}/releases?per_page=20") or []
            print("=" * 90)
            print(f"RELEASES {full} count={len(rel)}")
            for r in rel[:14]:
                body = (r.get("body") or "")[:500].replace("\r", "")
                print(f"  {r['tag_name']:<16} {r['published_at'][:19]} assets={len(r.get('assets', []))} "
                      f"dl={sum(a['download_count'] for a in r.get('assets', []))}")
                if body.strip():
                    print(f"      {body}")

    elif mode == "issues":
        for full in sys.argv[2:]:
            iss = japi(f"repos/{full}/issues?state=all&per_page=40")
            print("=" * 90)
            print(f"ISSUES {full} count={len(iss) if isinstance(iss, list) else 'FAIL'}")
            for i in (iss or [])[:40]:
                tag = "PR " if "pull_request" in i else "ISS "
                print(f"  {tag}#{i['number']:<4} {i['state']:<6} {i['title'][:85]} "
                      f"[{i['user']['login']}] {i['created_at'][:10]}")

    elif mode == "commits":
        for full in sys.argv[2:]:
            cs = japi(f"repos/{full}/commits?per_page=25") or []
            print("=" * 90)
            print(f"COMMITS {full} page1={len(cs)}")
            for c in cs[:25]:
                print(f"  {c['commit']['author']['date'][:19]}  {c['commit']['message'].splitlines()[0][:90]}")

    elif mode == "tree":
        for full in sys.argv[2:]:
            t = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
            paths = [e["path"] for e in t.get("tree", [])]
            print("=" * 90)
            print(f"TREE {full} entries={len(paths)} truncated={t.get('truncated')}")
            for p in paths[:200]:
                print("   ", p)

    elif mode == "rate":
        print(api("rate_limit"))
