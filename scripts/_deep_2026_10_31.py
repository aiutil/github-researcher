#!/usr/bin/env python3
"""Deep evidence collection for 2026-10-31 candidates."""
import json, subprocess, os, re, base64, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return None
    return r.stdout


def japi(path):
    r = api(path)
    if r is None:
        return None
    try:
        return json.loads(r)
    except Exception:
        return None


TARGETS = sys.argv[1:] or [
    "dbreunig/nesformer",
    "Djihads80/Eglantine",
    "soimy/c3rb3r-rescue",
    "MarkBlah/smsofdeath",
    "tapoooooty/hypergrad",
    "VortexSo4/Weft",
    "NiazMorshed2007/reanimate",
    "heydamir/unslop",
]

for full in TARGETS:
    print("=" * 100)
    print("REPO:", full)
    print("=" * 100)
    repo = japi(f"repos/{full}")
    if not repo:
        print("  FAILED")
        continue
    print(f"  stars={repo['stargazers_count']} forks={repo['forks_count']} subs={repo['subscribers_count']} "
          f"oi={repo['open_issues_count']} size={repo['size']}KB lang={repo['language']} "
          f"lic={(repo.get('license') or {}).get('spdx_id')} created={repo['created_at']} pushed={repo['pushed_at']}")
    print(f"  desc={repo.get('description')}")
    print(f"  homepage={repo.get('homepage')} topics={repo.get('topics')}")
    owner = repo["owner"]["login"]
    otype = repo["owner"]["type"]
    org = japi(f"users/{owner}")
    if org:
        print(f"  OWNER {owner} type={otype} created={org.get('created_at')} public_repos={org.get('public_repos')} "
              f"followers={org.get('followers')} repos_url={org.get('repos_url')}")
    # file tree
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1")
    if tree and "tree" in tree:
        entries = tree["tree"]
        blobs = [e for e in entries if e["type"] == "blob"]
        print(f"  TREE: {len(entries)} entries, {len(blobs)} blobs, truncated={tree.get('truncated')}")
        for e in sorted(blobs, key=lambda x: -x.get("size", 0))[:18]:
            print(f"    {e.get('size',0):>8} {e['path']}")
    # commits
    cm = japi(f"repos/{full}/commits?per_page=8")
    if cm:
        print(f"  COMMITS (latest {len(cm)} of first page):")
        for c in cm[:8]:
            print(f"    {c['commit']['author']['date']} | {c['commit']['message'].splitlines()[0][:95]}")
    # contributors
    ct = japi(f"repos/{full}/contributors?per_page=100")
    if isinstance(ct, list):
        print(f"  CONTRIBUTORS ({len(ct)}): " + ", ".join(f"{c['login']}({c['contributions']})" for c in ct[:12]))
    # releases
    rl = japi(f"repos/{full}/releases?per_page=20")
    if isinstance(rl, list):
        print(f"  RELEASES ({len(rl)}):")
        for r in rl[:10]:
            print(f"    {r['tag_name']} @ {r['published_at']} assets={len(r.get('assets',[]))} :: {(r.get('body') or '')[:110].replace(chr(10),' ')}")
    # issues
    iss = japi(f"repos/{full}/issues?state=all&per_page=15")
    if isinstance(iss, list):
        real = [i for i in iss if "pull_request" not in i]
        print(f"  ISSUES ({len(real)} non-PR):")
        for i in real[:10]:
            print(f"    #{i['number']} [{i['state']}] {i['title'][:88]} (comments={i['comments']})")
    # README
    rd = api(f"repos/{full}/readme", raw=True)
    if rd:
        print(f"  README ({len(rd)} bytes):")
        print("  " + "\n  ".join(rd[:7000].splitlines()[:170]))
    print()
