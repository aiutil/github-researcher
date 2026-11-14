#!/usr/bin/env python3
"""Evidence collection for the 2026-11-07 daily (data window 2026-11-05/06 UTC).

Read-only against the GitHub REST/Search API via the authenticated `gh` CLI.
Every number printed here is a direct API field value; nothing is estimated.
"""
import json, subprocess, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}
OUT = "/tmp/collect_1107"
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
        "owner_created": r["owner"].get("created_at"),
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
    print(f"    topics={d['topics']}")
    print(f"    root({len(d['root'])}): {d['root'][:40]}")


def search(q, per_page=100):
    res = japi(f"search/repositories?q={q}&per_page={per_page}&sort=stars")
    return res or {"total_count": 0, "items": []}


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "meta"

    if mode == "meta":
        for t in sys.argv[2:]:
            show(meta(t))
            print("-" * 90)

    elif mode == "cohort":
        # Dump every repo created on a given day with a star floor, with the
        # search-level fields only (cheap, one API call per page).
        day = sys.argv[2]
        floor = sys.argv[3] if len(sys.argv) > 3 else "30"
        res = search(f"created:{day} stars:>={floor}", per_page=100)
        items = res["items"]
        print(f"total_count={res['total_count']} fetched={len(items)}")
        with open(f"{OUT}/cohort_{day}.json", "w") as f:
            json.dump([{
                "full_name": i["full_name"], "stars": i["stargazers_count"],
                "forks": i["forks_count"], "size": i["size"],
                "created_at": i["created_at"], "pushed_at": i["pushed_at"],
                "desc": i.get("description"), "lang": i.get("language"),
                "topics": i.get("topics"), "owner_type": i["owner"]["type"],
            } for i in items], f, indent=2)
        small = [i for i in items if i["size"] <= 20]
        print(f"size<=20KB: {len(small)}/{len(items)} = {100*len(small)/max(1,len(items)):.1f}%")
        # star value distribution
        from collections import Counter
        c = Counter(i["stargazers_count"] for i in items)
        print("star value histogram (top 15):", c.most_common(15))
        # creation-minute clustering
        mins = Counter(i["created_at"][:16] for i in items)
        print("top creation minutes:", mins.most_common(10))
        zero_fork = [i for i in items if i["forks_count"] == 0]
        print(f"zero-fork repos: {len(zero_fork)}/{len(items)}")
        print("-" * 90)
        for i in items:
            print(f"  {i['stargazers_count']:>7}\t{i['forks_count']:>5}f\t{i['size']:>7}KB\t"
                  f"{i['created_at'][:16]}\t{i['full_name']}\t{(i.get('description') or '')[:80]}")

    elif mode == "readme":
        for full in sys.argv[2:]:
            rd = api(f"repos/{full}/readme", raw=True)
            print("=" * 100)
            print("README:", full, "len=", len(rd) if rd else 0)
            print("=" * 100)
            print((rd or "")[:16000])

    elif mode == "contents":
        full, path = sys.argv[2], sys.argv[3]
        raw = api(f"repos/{full}/contents/{path}", raw=True)
        print((raw or "FAILED")[:16000])

    elif mode == "tree":
        for full in sys.argv[2:]:
            t = japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
            paths = [e["path"] for e in t.get("tree", [])]
            print("=" * 90)
            print(f"TREE {full} entries={len(paths)} truncated={t.get('truncated')}")
            for p in paths[:250]:
                print("   ", p)

    elif mode == "releases":
        for full in sys.argv[2:]:
            rel = japi(f"repos/{full}/releases?per_page=30")
            print("=" * 90)
            print(f"RELEASES {full} count={len(rel) if isinstance(rel,list) else 'FAIL'}")
            for r in (rel or [])[:20]:
                body = (r.get("body") or "")[:700].replace("\r", "")
                print(f"  {r['tag_name']:<16} {r['published_at'][:19]} assets={len(r.get('assets',[]))} "
                      f"dl={sum(a['download_count'] for a in r.get('assets',[]))}")
                if body.strip():
                    print(f"      {body}")

    elif mode == "issues":
        for full in sys.argv[2:]:
            iss = japi(f"repos/{full}/issues?state=all&per_page=40")
            print("=" * 90)
            print(f"ISSUES {full} count={len(iss) if isinstance(iss,list) else 'FAIL'}")
            for i in (iss or [])[:40]:
                tag = "PR " if "pull_request" in i else "ISS "
                print(f"  {tag}#{i['number']:<4} {i['state']:<7} {i['title'][:88]} "
                      f"[{i['user']['login']}] {i['created_at'][:10]}")

    elif mode == "commits":
        for full in sys.argv[2:]:
            cs = japi(f"repos/{full}/commits?per_page=30")
            print("=" * 90)
            print(f"COMMITS {full} page1={len(cs) if isinstance(cs,list) else 'FAIL'}")
            for c in (cs or [])[:30]:
                print(f"  {c['commit']['author']['date'][:19]}  {c['commit']['message'].splitlines()[0][:95]}")

    elif mode == "owner":
        for owner in sys.argv[2:]:
            u = japi(f"users/{owner}")
            print("=" * 90)
            print(f"OWNER {owner}: {json.dumps(u, ensure_ascii=False)[:600] if u else 'FAIL'}")
            o = japi(f"orgs/{owner}")
            if o:
                print(f"  ORG: {o.get('login')} created={o.get('created_at')} "
                      f"repos={o.get('public_repos')} followers={o.get('followers')}")

    elif mode == "probe":
        # Read the READMEs of a sample of small repos from a cohort file and
        # look for payload markers / template placeholders.
        cohort = f"{OUT}/cohort_{sys.argv[2]}.json"
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        items = json.load(open(cohort))
        URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
        HINTS = ["Invoke-Expression", "irm ", "Invoke-RestMethod", "ExecutionPolicy Bypass",
                 "Real-time protection", "Setup.ps1", "git-software.cc", "iwr ",
                 "powershell", "cmd /c", "{{", "}}"]
        pool = [i for i in items if i["size"] <= 20][:limit]
        print(f"probing {len(pool)} small repos")
        doms, flagged = {}, []
        def one(it):
            rd = api(f"repos/{it['full_name']}/readme", raw=True)
            if rd is None:
                return it["full_name"], None
            hits = [h for h in HINTS if h.lower() in rd.lower()]
            urls = sorted(set(URL_RE.findall(rd)))
            return it["full_name"], {"len": len(rd), "hits": hits, "urls": urls[:20]}
        with ThreadPoolExecutor(max_workers=6) as ex:
            for name, s in ex.map(one, pool):
                if s is None:
                    print(f"  DEAD  {name}")
                    continue
                tag = "PAYLOAD" if s["hits"] else "clean  "
                if s["hits"]:
                    flagged.append((name, s["hits"], s["urls"]))
                for u in s["urls"]:
                    doms[u] = doms.get(u, 0) + 1
                print(f"  {tag} {name:<52} len={s['len']:<6} hits={s['hits']}")
        print("=" * 90)
        print(f"scanned {len(pool)}; flagged={len(flagged)}")
        print("--- top urls ---")
        for u, c in sorted(doms.items(), key=lambda kv: -kv[1])[:20]:
            print(f"  {c:>4}  {u}")
        print("--- flagged detail ---")
        for n, h, u in flagged[:12]:
            print(f"  {n}\n     hits={h}\n     urls={u}")

    elif mode == "rate":
        print(api("rate_limit"))
