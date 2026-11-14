#!/usr/bin/env python3
"""Evidence collection for 2026-11-01 daily. Read-only GitHub API."""
import json, subprocess, os, re, sys, collections

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


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


def ncommits(full, sha=None):
    p = f"repos/{full}/commits?per_page=1" + (f"&sha={sha}" if sha else "")
    h = subprocess.run(["gh", "api", "-i", p], capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    if m:
        return int(m.group(1))
    m2 = re.search(r'page=(\d+)>; rel="next"', h)
    return 1


def meta(full):
    r = japi(f"repos/{full}")
    if not r:
        return None
    br = japi(f"repos/{full}/branches") or []
    contrib = japi(f"repos/{full}/contributors?per_page=100&anon=false")
    rel = japi(f"repos/{full}/releases?per_page=100")
    tree = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = [e for e in tree.get("tree", []) if e["type"] == "blob"]
    root = japi(f"repos/{full}/git/trees/HEAD") or {}
    rootnames = [e["path"] for e in root.get("tree", [])]
    out = {
        "full": full,
        "stars": r["stargazers_count"], "forks": r["forks_count"],
        "subs": r["subscribers_count"], "oi": r["open_issues_count"],
        "size": r["size"], "lang": r["language"],
        "lic": (r.get("license") or {}).get("spdx_id"),
        "created": r["created_at"], "pushed": r["pushed_at"],
        "default_branch": r["default_branch"],
        "desc": r.get("description"), "homepage": r.get("homepage"),
        "topics": r.get("topics"), "archived": r.get("archived"),
        "owner_type": r["owner"]["type"],
        "ncontrib": len(contrib) if isinstance(contrib, list) else None,
        "nrel": len(rel) if isinstance(rel, list) else None,
        "rel_assets": sum(len(x.get("assets", [])) for x in rel) if isinstance(rel, list) else None,
        "ncommits": ncommits(full),
        "tree_truncated": tree.get("truncated"),
        "nblobs": len(blobs),
        "root": rootnames,
        "readme_len": None,
    }
    rd = api(f"repos/{full}/readme", raw=True)
    if rd:
        out["readme_len"] = len(rd)
    return out


def show(d):
    if not d:
        print("  FAILED")
        return
    print(f"  {d['full']}")
    print(f"    stars={d['stars']} forks={d['forks']} subs={d['subs']} oi={d['oi']} size={d['size']}KB "
          f"lang={d['lang']} lic={d['lic']}")
    print(f"    created={d['created']} pushed={d['pushed']} default={d['default_branch']} "
          f"archived={d['archived']} owner_type={d['owner_type']}")
    print(f"    commits={d['ncommits']} contributors={d['ncontrib']} releases={d['nrel']} "
          f"rel_assets={d['rel_assets']} blobs={d['nblobs']} truncated={d['tree_truncated']} "
          f"readme_len={d['readme_len']}")
    print(f"    desc={d['desc']}")
    print(f"    homepage={d['homepage']} topics={d['topics']}")
    print(f"    root({len(d['root'])}): {d['root'][:40]}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "meta"

    if mode == "meta":
        targets = sys.argv[2:]
        for t in targets:
            show(meta(t))
            print("-" * 90)

    elif mode == "cohort":
        # New repos created on given date with stars>=40
        for date in sys.argv[2:]:
            res = japi(f"search/repositories?q=created:{date}+stars:>=40&per_page=100&sort=stars")
            if not res:
                print(f"{date}: search failed")
                continue
            items = res["items"]
            small = sum(1 for i in items if i["size"] <= 20)
            print(f"### created:{date} stars>=40 -> total_count={res['total_count']} fetched={len(items)} "
                  f"size<=20KB={small}")
            # payload scan on top 60 by stars
            hit = 0; tel = 0; both = 0; neither = 0; checked = 0
            for i in items[:60]:
                rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
                if not rd:
                    continue
                checked += 1
                p = ("git-software.cc" in rd) or ("Invoke-Expression" in rd)
                t = "telegra" in rd.lower()
                if p and t: both += 1
                elif p: hit += 1
                elif t: tel += 1
                else: neither += 1
            print(f"  README checked={checked} ps_payload={hit} telegraph_only={tel} both={both} neither={neither}")
            owners = [i["owner"]["login"] for i in items]
            print(f"  distinct owners={len(set(owners))}/{len(owners)} otypes={ {i['owner']['type'] for i in items} }")
            print("  top by stars:")
            for i in items[:25]:
                print(f"    {i['stargazers_count']:>6} {i['size']:>6}KB {i['full_name']}")
            print("-" * 90)

    elif mode == "trending":
        # GitHub trending page scrape
        r = subprocess.run(["curl", "-sL", "https://github.com/trending?since=daily"],
                           capture_output=True, text=True)
        arts = re.findall(r'<h2 class="h3 lh-condensed">\s*<a href="/([^"]+)"', r.stdout)
        print("trending daily:", arts[:30])
        r2 = subprocess.run(["curl", "-sL", "https://github.com/trending?since=weekly"],
                            capture_output=True, text=True)
        arts2 = re.findall(r'<h2 class="h3 lh-condensed">\s*<a href="/([^"]+)"', r2.stdout)
        print("trending weekly:", arts2[:30])

    elif mode == "readme":
        for full in sys.argv[2:]:
            rd = api(f"repos/{full}/readme", raw=True)
            print("=" * 100)
            print("README:", full, "len=", len(rd) if rd else 0)
            print("=" * 100)
            print((rd or "")[:9000])
