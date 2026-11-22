#!/usr/bin/env python3
"""Split GitHub's `open_issues_count` into real issues and pull requests.

Rationale
---------
The REST field `open_issues_count` on a repository counts **issues + pull
requests** together.  Every prior report in this archive used that raw
number as a "is it really being used" signal (e.g. 11-18: "modern-web-
guidance-src 404 open issues" vs "arcane 9 open issues").  If a repository
is a monorepo with heavy bot-driven PR traffic, the raw number measures
*merge queue depth*, not *user friction*.

This script measures, for every repo in today's cohort:
  * open_issues_count            (raw REST field)
  * n_issues                     (items WITHOUT a `pull_request` key)
  * n_prs                        (items WITH a `pull_request` key)
  * issue_sample_titles          (a few real issue titles, for texture)

It also runs the same split for a small control set of well-known
repositories so the ratio can be read against a baseline rather than in
isolation.

Output: /tmp/issuepr_1121.json
"""
import json
import os
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/issuepr_1121.json"

# Today's cohort (from /tmp/trend_1121.json) plus a control set.
CONTROL = [
    "torvalds/linux",
    "rust-lang/rust",
    "golang/go",
    "sveltejs/svelte",
]


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def split(full):
    m = api(f"repos/{full}") or {}
    raw = m.get("open_issues_count")
    # The issues endpoint returns pull requests as well; they carry a
    # `pull_request` key.  Read enough pages to characterise the mix.
    items = api(f"repos/{full}/issues", {"state": "open", "per_page": 100}) or []
    if not isinstance(items, list):
        items = []
    issues = [i for i in items if not i.get("pull_request")]
    prs = [i for i in items if i.get("pull_request")]
    return {
        "repo": full,
        "raw_open_issues_count": raw,
        "n_listed": len(items),
        "n_issues": len(issues),
        "n_prs": len(prs),
        "issue_share": round(len(issues) / len(items), 4) if items else None,
        "issue_titles": [i.get("title") for i in issues][:12],
        "pr_titles": [i.get("title") for i in prs][:6],
        "oldest_listed_at": min([i.get("created_at") for i in items if i.get("created_at")], default=None),
        "newest_listed_at": max([i.get("created_at") for i in items if i.get("created_at")], default=None),
        "labels_on_issues": sorted({l.get("name") for i in issues for l in (i.get("labels") or [])})[:15],
    }


def main():
    trend = json.load(open("/tmp/trend_1121.json"))
    cohort = [t["full_name"] for t in trend] + CONTROL
    rows = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for r in ex.map(split, cohort):
            if r:
                rows.append(r)
                print(f"  {r['repo']:44s} raw={r['raw_open_issues_count']:>6} "
                      f"issues={r['n_issues']:>4} prs={r['n_prs']:>4} "
                      f"issue_share={r['issue_share']}", flush=True)
    json.dump(rows, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {len(rows)} -> {OUT}")


if __name__ == "__main__":
    main()
