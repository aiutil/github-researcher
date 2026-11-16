#!/usr/bin/env python3
"""Two verifications for the 2026-11-17 report.

H-A  The 'cheat client' family is one deployment: shared README template
     (capsule-render banner), shared payload host (modbay.live), near-empty
     trees, and owners drawn from a tight registration cohort.

H-B  For kajisho5/ffmpeg-skill, every one of its 100 releases corresponds to
     a DISTINCT commit that actually changed code (the counter-example to
     the 11-16 'release stuffing' finding).
"""
import hashlib
import json
import os
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


def blob_sha(full, path, branch="main"):
    t = api(f"repos/{full}/contents/{urllib.parse.quote(path)}",
            headers=["Accept: application/vnd.github.raw"]) if False else None
    # use git/trees sha instead (no content download)
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    for b in tree.get("tree") or []:
        if b.get("path") == path:
            return b.get("sha"), b.get("size")
    return None, None


def owner_repos(login):
    out = []
    for page in (1, 2):
        rs = api(f"users/{login}/repos", {"per_page": 100, "page": page,
                                          "sort": "created"})
        if not rs:
            break
        out.extend(rs)
        if len(rs) < 100:
            break
    return out


def owner_row(login):
    u = api(f"users/{login}") or {}
    rs = owner_repos(login)
    return {
        "login": login,
        "created_at": u.get("created_at"),
        "followers": u.get("followers"),
        "public_repos": u.get("public_repos"),
        "repos": [{"full_name": r.get("full_name"),
                   "stars": r.get("stargazers_count"),
                   "created_at": r.get("created_at"),
                   "desc": r.get("description")} for r in rs],
    }


def h_a():
    print("=" * 78)
    print("H-A  cheat-client family: template + payload + owner cohort")
    print("=" * 78)
    src = json.load(open("/tmp/cheat_family_1117.json"))
    # 1. shared payload host / template markers across READMEs
    markers = ["capsule-render.vercel.app", "modbay.live", "img.shields.io/badge",
               "for-the-badge"]
    for m in markers:
        hits = [r["full_name"] for r in src if m in r["readme_head"]]
        print(f"  marker {m:<32} present in {len(hits)}/{len(src)}: "
              f"{[h.split('/')[0] for h in hits]}")

    # 2. LICENSE blob identity (MIT text) across the family
    print("\n  LICENSE blob sha (identical MIT text => same template):")
    for r in src:
        sha, size = blob_sha(r["full_name"], "LICENSE")
        rsha, rsize = blob_sha(r["full_name"], "README.md")
        print(f"    {r['full_name']:<52} LICENSE sha={str(sha)[:10]} size={size} "
              f"| README sha={str(rsha)[:10]} size={rsize}")

    # 3. owner cohort
    print("\n  owner accounts:")
    logins = [r["owner_login"] for r in src]
    with ThreadPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(owner_row, logins))
    for r in sorted(rows, key=lambda x: x["created_at"] or ""):
        print(f"    {r['login']:<30} created={r['created_at']} foll={r['followers']} "
              f"repos={r['public_repos']}")
        for rr in r["repos"]:
            print(f"        - {rr['full_name']:<52} ⭐{rr['stars']:<6} "
                  f"{rr['created_at']}  {(rr['desc'] or '')[:52]}")
    json.dump(rows, open("/tmp/cheat_owners_1117.json", "w"),
              ensure_ascii=False, indent=1)

    # 4. payload hosts actually used
    print("\n  payload hosts found in README (first 1400 chars):")
    import re
    URL = re.compile(r"https?://[^\s)\"'<>\]`]+")
    hosts = Counter()
    for r in src:
        for u in URL.findall(r["readme_head"]):
            h = u.split("/")[2] if "//" in u else ""
            hosts[h] += 1
    for h, c in hosts.most_common(12):
        print(f"    {h:<40} x{c}")


def h_b():
    print("\n" + "=" * 78)
    print("H-B  kajisho5/ffmpeg-skill: do 100 releases map to 100 distinct code commits?")
    print("=" * 78)
    full = "kajisho5/ffmpeg-skill"
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    print(f"  tags: {len(tags)}")
    tag_shas = []
    for t in tags:
        tag_shas.append((t["name"], t["commit"]["sha"]))
    distinct = len({s for _, s in tag_shas})
    print(f"  distinct target commit shas: {distinct} / {len(tag_shas)}")
    dup = [n for n, c in Counter(s for _, s in tag_shas).items() if c > 1]
    print(f"  tags sharing a commit: {dup}")

    # for a sample of tags, diff the tagged commit against its parent
    sample = tag_shas[:14] + tag_shas[-6:]
    print(f"\n  per-tag code-change check ({len(sample)} sampled tags):")
    real = 0
    for name, sha in sample:
        c = api(f"repos/{full}/commits/{sha}") or {}
        files = c.get("files") or []
        st = c.get("stats") or {}
        msg = ((c.get("commit") or {}).get("message") or "").split("\n")[0]
        changed = [f["filename"] for f in files]
        kind = "real-code-change" if changed else "no-file-change"
        if changed:
            real += 1
        print(f"    {name:<10} {sha[:8]} files={len(files):<3} +{st.get('additions')}/-"
              f"{st.get('deletions')}  {kind:<18} {msg[:56]}")
        print(f"        changed: {changed[:5]}")
    print(f"\n  tags whose commit touched files: {real}/{len(sample)}")

    # release assets
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    with_assets = sum(1 for r in rel if r.get("assets"))
    print(f"  releases: {len(rel)}, with assets: {with_assets}")

    # release -> tag sha correspondence
    rel_tags = [r["tag_name"] for r in rel]
    print(f"  release tag_names == git tags (first 100)? "
          f"{set(rel_tags) == {n for n, _ in tag_shas}}")
    out = {"tag_shas": tag_shas, "distinct": distinct,
           "releases": len(rel), "with_assets": with_assets,
           "sample_checked": len(sample), "sample_with_changes": real}
    json.dump(out, open("/tmp/ffmpeg_releases_1117.json", "w"), indent=1)


if __name__ == "__main__":
    h_a()
    h_b()
