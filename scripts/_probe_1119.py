#!/usr/bin/env python3
"""Full forensic probe of today's Trending repos using GitHub REST API
(via `gh` CLI, authenticated).  Collects the discriminators this project has
established over 11-12 .. 11-18:

  * stars / forks / subscribers / open issues / watchers  (star-farm shape)
  * tree blob count + extension mix                       (payload farms)
  * README md5 (identical READMEs across repos = templated deployment)
  * commit author-date seconds distribution                (burst commits)
  * owner account age / followers / public repos          (fresh-account farms)
  * license, topics, created_at, pushed_at
  * tag / release counts + release asset inventory
  * SKILL.md inventory (files, distinct identities, replication factor)
  * harness directories + install commands

Output: /tmp/probe_1119.json
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/probe_1119.json"

PAY = ("dropbox", "mediafire", "mega.nz", "drive.google", "wetransfer",
       "pixeldrain", "linkbox", "discord.gg", "quark", "pan.baidu", "bit.ly",
       "modbay.live", "capsule-render", "readme-typing-svg")


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


_OWNER = {}


def owner_meta(login):
    if login not in _OWNER:
        u = api(f"users/{login}") or {}
        _OWNER[login] = {
            "owner_created": u.get("created_at"),
            "owner_followers": u.get("followers"),
            "owner_public_repos": u.get("public_repos"),
            "owner_type": u.get("type"),
            "owner_bio": (u.get("bio") or "")[:200],
        }
    return _OWNER[login]


SKILL_RE = re.compile(r"(^|/)SKILL\.md$", re.I)
HARNESS_DIRS = ("claude", "codex", "cursor", "gemini", "copilot", "windsurf",
                "amp", "zed", "opencode", "aider", "droid", "qwen", "codex-cli",
                "claude-code", "antigravity", "kiro", "trae", "augment")


def probe(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"

    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    commits = commits if isinstance(commits, list) else []
    secs, authors = set(), set()
    for c in commits:
        au = (c.get("commit") or {}).get("author") or {}
        if au.get("date"):
            secs.add(au["date"][-2:])
        if au.get("name"):
            authors.add(au["name"])

    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path", "") for b in blobs]
    exts = Counter()
    for p in paths:
        e = os.path.splitext(p)[1].lower() or "<none>"
        exts[e] += 1

    # SKILL.md inventory
    skill_blobs = [b for b in blobs if SKILL_RE.search(b.get("path", ""))]
    skill_by_dir = {}
    for b in skill_blobs:
        p = b.get("path", "")
        parent = p.rsplit("/", 1)[0] if "/" in p else "<root>"
        skill_by_dir.setdefault(parent, set()).add(b.get("sha"))
    n_ident = len({frozenset(v) for v in skill_by_dir.values()})
    skill_shas = [b.get("sha") for b in skill_blobs]

    # harness directories present in tree
    harness_hits = set()
    for p in paths:
        parts = p.split("/")
        for hp in HARNESS_DIRS:
            if hp in parts:
                harness_hits.add(hp)

    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    lic = m.get("license") or {}
    owner = m.get("owner") or {}
    ometa = owner_meta(owner.get("login")) if owner.get("login") else {}

    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    releases = api(f"repos/{full}/releases", {"per_page": 100}) or []
    releases = releases if isinstance(releases, list) else []

    rel_assets = []
    for r in releases[:6]:
        assets = r.get("assets") or []
        rel_assets.append({
            "tag": r.get("tag_name"),
            "prerelease": r.get("prerelease"),
            "n_assets": len(assets),
            "asset_names": [a.get("name") for a in assets][:12],
            "total_downloads": sum(a.get("download_count") or 0 for a in assets),
            "max_downloads": max([a.get("download_count") or 0 for a in assets] or [0]),
            "has_sbom": any("sbom" in (a.get("name") or "").lower()
                            or "cyclonedx" in (a.get("name") or "").lower()
                            or "spdx" in (a.get("name") or "").lower()
                            for a in assets),
            "has_checksum": any(re.search(r"sha256|checksum|\.sha", a.get("name") or "", re.I)
                                 for a in assets),
        })

    wf = api(f"repos/{full}/contents/.github/workflows") or []
    wf_names = [w.get("name") for w in wf] if isinstance(wf, list) else []

    issues = api(f"repos/{full}/issues", {"state": "open", "per_page": 30}) or []
    issues = issues if isinstance(issues, list) else []

    install_cmds = sorted({c for c in re.findall(
        r"(npx\s+skills\s+add[^\n`\"]{0,60}|marketplace\s+add[^\n`\"]{0,60}|"
        r"pip\s+install\s+[a-zA-Z0-9_.\-]+|npm\s+i(?:nstall)?\s+-g\s+[a-zA-Z0-9_.\-@]+|"
        r"cargo\s+install\s+[a-zA-Z0-9_.\-]+|brew\s+install\s+[a-zA-Z0-9_.\-]+)", rm)})

    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "watchers": m.get("watchers_count"),
        "subs": m.get("subscribers_count"),
        "open_issues": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": lic.get("spdx_id"),
        "license_name": lic.get("name"),
        "topics": m.get("topics", []),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "updated_at": m.get("updated_at"),
        "default_branch": branch,
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "archived": m.get("archived"),
        "is_fork": m.get("fork"),
        "has_issues": m.get("has_issues"),
        "has_discussions": m.get("has_discussions"),
        "owner_login": owner.get("login"),
        "owner_type": owner.get("type"),
        "owner_created": ometa.get("owner_created"),
        "owner_followers": ometa.get("owner_followers"),
        "owner_public_repos": ometa.get("owner_public_repos"),
        "owner_bio": ometa.get("owner_bio"),
        "n_commits": len(commits),
        "n_authors": len(authors),
        "commit_secs": sorted(secs),
        "n_blobs": len(blobs),
        "exts": dict(exts.most_common(12)),
        "truncated_tree": tree.get("truncated"),
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:2500],
        "n_tags": len(tags),
        "tag_names": [t.get("name") for t in tags][:20],
        "n_releases": len(releases),
        "rel_assets": rel_assets,
        "n_skill_files": len(skill_blobs),
        "n_skill_identities": n_ident,
        "skill_replication": round(len(skill_blobs) / n_ident, 2) if n_ident else 0,
        "skill_dirs": sorted(skill_by_dir.keys())[:40],
        "harness_dirs": sorted(harness_hits),
        "install_cmds": install_cmds,
        "workflows": wf_names,
        "n_open_issues_listed": len(issues),
        "issue_titles": [i.get("title") for i in issues][:30],
        "payload_urls": sorted({u for u in re.findall(r"https?://[^\s)\"'<>`]+", rm)
                               if any(p in u.lower() for p in PAY)}),
    }


def main():
    trend = json.load(open("/tmp/trend_1119.json"))
    items = [t["full_name"] for t in trend]
    print(f"probing {len(items)} repos", flush=True)
    out = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(probe, items), 1):
            if r is None:
                continue
            out.append(r)
            print(f"  [{i}/{len(items)}] {r['full_name']:42s} *{r['stars']} "
                  f"blob={r['n_blobs']} tags={r['n_tags']} rel={r['n_releases']} "
                  f"skills={r['n_skill_files']}/{r['n_skill_identities']}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {len(out)} -> {OUT}", flush=True)


if __name__ == "__main__":
    main()
