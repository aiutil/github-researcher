#!/usr/bin/env python3
"""Size the 'cheat client' deployment across a 3-day window.

Signature = README contains the capsule-render.vercel.app banner generator OR
points at modbay.live.  This searches created:2026-11-14..2026-11-16 and
reports every hit, so the daily report can state an exact count rather than
"several".
"""
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


QUERIES = [
    'created:2026-11-14..2026-11-16 cheat in:name stars:>=1',
    'created:2026-11-14..2026-11-16 crack in:name stars:>=1',
    'created:2026-11-14..2026-11-16 trainer in:name stars:>=1',
    'created:2026-11-14..2026-11-16 "cheat client" in:description stars:>=1',
]
SIGS = ["capsule-render.vercel.app", "modbay.live", "readme-typing-svg.demolab.com"]


def probe(it):
    full = it["full_name"]
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    owner = m.get("owner") or {}
    u = api(f"users/{owner.get('login')}") or {}
    o_repos = api(f"users/{owner.get('login')}/repos", {"per_page": 100,
                                                       "sort": "created"}) or []
    if not isinstance(o_repos, list):
        o_repos = []
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "created_at": m.get("created_at"),
        "desc": m.get("description"),
        "n_blobs": len(blobs),
        "readme_len": len(rm),
        "readme_head": rm[:1500],
        "sig_hits": [s for s in SIGS if s in rm],
        "owner_login": owner.get("login"),
        "owner_created": u.get("created_at"),
        "owner_followers": u.get("followers"),
        "owner_public_repos": u.get("public_repos"),
        "owner_repo_names": [r.get("name") for r in o_repos],
        "owner_repo_stars": [(r.get("full_name"), r.get("stargazers_count"),
                              r.get("created_at")) for r in o_repos],
    }


if __name__ == "__main__":
    items = []
    seen = set()
    for Q in QUERIES:
        print(f"query: {Q}")
        for page in (1, 2):
            d = api("search/repositories", {"q": Q, "sort": "stars", "order": "desc",
                                           "per_page": 100, "page": page})
            if not d:
                break
            got = d.get("items", [])
            for g in got:
                if g["full_name"] not in seen:
                    seen.add(g["full_name"])
                    items.append(g)
            if len(got) < 100:
                break
    print(f"unique candidates: {len(items)}")

    out = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(probe, items):
            out.append(r)
    sig = [r for r in out if r["sig_hits"]]
    print(f"\nrepos matching the deployment signature: {len(sig)}/{len(out)}")
    for r in sorted(sig, key=lambda r: -(r["stars"] or 0)):
        print(f"  {r['full_name']:<52} ⭐{r['stars']:<5} f={r['forks']:<4} "
              f"s={r['subs']:<4} oi={r['oi']:<3} blobs={r['n_blobs']:<3} "
              f"created={r['created_at']} owner={r['owner_login']} "
              f"owner_created={r['owner_created']} "
              f"owner_repos={r['owner_public_repos']} sig={r['sig_hits']}")
    print("\n=== owner account registry (signature repos only) ===")
    owners = {}
    for r in sig:
        owners.setdefault(r["owner_login"], []).append(r)
    for lg in sorted(owners, key=lambda l: owners[l][0]["owner_created"] or ""):
        rs = owners[lg]
        u0 = rs[0]
        print(f"  {lg:<28} created={u0['owner_created']} foll={u0['owner_followers']} "
              f"repos={u0['owner_public_repos']}")
        for x in u0["owner_repo_stars"]:
            print(f"      - {x[0]:<52} ⭐{x[1]:<5} {x[2]}")
    print("\n=== owner creation-time spread ===")
    ts = sorted(r["owner_created"] for r in sig if r["owner_created"])
    print(f"  n={len(ts)} earliest={ts[0]} latest={ts[-1]}")
    print("\n=== payload hosts across signature repos ===")
    URL = re.compile(r"https?://[^\s)\"'<>\]`]+")
    hosts = Counter()
    for r in sig:
        for u in URL.findall(r["readme_head"]):
            hosts[u.split("/")[2] if "//" in u else u] += 1
    for h, c in hosts.most_common(10):
        print(f"  {h:<42} x{c}")
    print("\n=== stars vs subs vs open issues (signature repos) ===")
    for r in sorted(sig, key=lambda r: -(r["stars"] or 0)):
        print(f"  {r['full_name']:<52} ⭐{r['stars']:<5} subs{str(r['subs']):<4} "
              f"oi{str(r['oi']):<4} n_blobs={r['n_blobs']}")
    json.dump(out, open("/tmp/cheat_scan_1117.json", "w"), ensure_ascii=False, indent=1)
    print(f"\nwrote /tmp/cheat_scan_1117.json ({len(out)} rows)")
