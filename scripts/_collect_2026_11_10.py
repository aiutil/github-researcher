#!/usr/bin/env python3
'''Collect today's GitHub candidate set via the GitHub REST/Search API.

Window: repos created on the target UTC day with stars >= 30 (the same floor
used on 2026-11-06/07).  Metadata is chosen to discriminate real projects from
star farms: size, forks, subscribers, open issues, commit timestamps, license,
topics, and the README text itself (payload / templating checks).
'''

import json
import os
import subprocess
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

DAY = sys.argv[1] if len(sys.argv) > 1 else "2026-11-09"
MIN_STARS = int(sys.argv[2]) if len(sys.argv) > 2 else 30
OUT = sys.argv[3] if len(sys.argv) > 3 else "/tmp/cand.json"

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


def search(q, page=1, per_page=100):
    d, _ = api("search/repositories", {"q": q, "sort": "stars", "order": "desc", "per_page": per_page, "page": page})
    return d.get("items", []) if d else []


def main():
    q = f"created:{DAY} stars:>={MIN_STARS}"
    items = []
    for page in (1, 2):
        batch = search(q, page=page)
        if not batch:
            break
        items.extend(batch)
        time.sleep(3.0)  # search rate limit: 30 req/min unauth, 30/min auth
    print(f"search '{q}' -> {len(items)} repos", file=sys.stderr)

    seen = {}
    for it in items:
        seen[it["full_name"]] = it
    items = list(seen.values())
    items.sort(key=lambda r: -r["stargazers_count"])
    print(f"unique: {len(items)}", file=sys.stderr)

    def work(it):
        full = it["full_name"]
        m, _ = api(f"repos/{full}")
        m = m or {}
        commits, _ = api(f"repos/{full}/commits", {"per_page": 100})
        commits = commits if isinstance(commits, list) else []
        secs = set()
        for c in commits:
            au = (c.get("commit", {}) or {}).get("author", {}) or {}
            if au.get("date"):
                secs.add(au["date"][-2:])
        rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
        rm = rm or ""
        lic = m.get("license") or {}
        return {
            "full_name": full,
            "stars": m.get("stargazers_count"),
            "forks": m.get("forks_count"),
            "subs": m.get("subscribers_count"),
            "oi": m.get("open_issues_count"),
            "size_kb": m.get("size"),
            "language": m.get("language"),
            "license": lic.get("spdx_id"),
            "license_name": lic.get("name"),
            "topics": m.get("topics", []),
            "created_at": m.get("created_at"),
            "pushed_at": m.get("pushed_at"),
            "default_branch": m.get("default_branch"),
            "owner_type": (m.get("owner") or {}).get("type"),
            "owner_created": (m.get("owner") or {}).get("created_at"),
            "owner_repos": None,
            "ncommits": len(commits),
            "commit_secs": len(secs),
            "desc": m.get("description"),
            "homepage": m.get("homepage"),
            "archived": m.get("archived"),
            "readme_len": len(rm),
            "readme_head": rm[:1500],
            "hit_git_software": "git-software.cc" in rm,
            "hit_invoke_expression": "Invoke-Expression" in rm,
            "hit_irm": "irm https" in rm.lower(),
            "hit_iwr": "iwr https" in rm.lower(),
            "hit_defender": "Windows Security" in rm or "antivirus" in rm.lower() or "disable your antivirus" in rm.lower(),
            "hit_discord_webhook": "discord.com/api/webhooks" in rm,
            "hit_config_py": "config.py" in rm,
        }

    with ThreadPoolExecutor(max_workers=5) as ex:
        results = list(ex.map(work, items))

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(results)} -> {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
