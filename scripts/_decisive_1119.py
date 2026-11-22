#!/usr/bin/env python3
"""Three decisive checks for 2026-11-19.

Q1. NAME-REPLICATION vs CONTENT-REPLICATION.
    Yesterday's report said ECC has a skill "copied 10 times".  But blob-sha
    duplication maxes at 3.  Which is it?  If the 10 copies share a NAME but
    differ in content, then replication is per-harness *adaptation*, not
    blind copying -- a different phenomenon.

Q2. superpowers: 39 tags / 17 releases -> 22 tags with no release.
    Are those tags real version bumps (commits with diffs) or inert?

Q3. paper-orchestra: +45.8% stars in 24h on a 56-blob / 0-release repo.
    Re-run the 11-18 control-group methodology on the new star wave.
"""

import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


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


def q1_name_vs_content():
    print("=" * 100)
    print("Q1. NAME-REPLICATION vs CONTENT-REPLICATION")
    print("=" * 100)
    for full in ("affaan-m/ECC", "HKUDS/CLI-Anything", "cursor/plugins",
                 "tradermonty/claude-trading-skills"):
        m = api(f"repos/{full}") or {}
        branch = m.get("default_branch") or "main"
        tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
        blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
        skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
        by_name = defaultdict(list)
        for b in skills:
            p = b.get("path") or ""
            name = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
            by_name[name].append((p, b.get("sha"), b.get("size")))
        sha_ct = Counter(b.get("sha") for b in skills)
        dup_sha = {s: c for s, c in sha_ct.items() if c > 1}
        top_names = sorted(by_name.items(), key=lambda kv: -len(kv[1]))[:6]
        print(f"\n--- {full}  files={len(skills)} names={len(by_name)} "
              f"distinct_shas={len(sha_ct)} dup_sha_groups={len(dup_sha)} "
              f"max_dup_sha={max(dup_sha.values()) if dup_sha else 1} ---")
        print(f"    files_in_name-replicated={sum(len(v) for v in by_name.values() if len(v)>1)}")
        print(f"    files_in_sha-replicated={sum(c for c in dup_sha.values())}")
        for name, lst in top_names:
            shas = {s for _, s, _ in lst}
            sizes = {sz for _, _, sz in lst}
            paths = [p for p, _, _ in lst][:4]
            print(f"    name={name!r:32s} copies={len(lst):>2} distinct_shas={len(shas):>2} "
                  f"distinct_sizes={len(sizes):>2} e.g. {paths}")
        if dup_sha:
            big = sorted(dup_sha.items(), key=lambda kv: -kv[1])[:3]
            for sha, c in big:
                same = [b.get("path") for b in skills if b.get("sha") == sha]
                print(f"    identical-sha x{c}: {same[:4]}")


def q2_superpowers_tags():
    print()
    print("=" * 100)
    print("Q2. superpowers 39 tags / 17 releases -- do the unreleased tags carry real diffs?")
    print("=" * 100)
    for full in ("obra/superpowers", "GoogleChrome/modern-web-guidance-src"):
        rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
        tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
        rel_tags = {r.get("tag_name") for r in rel}
        orphan = [t for t in tags if t.get("name") not in rel_tags]
        print(f"\n--- {full}: {len(tags)} tags, {len(rel)} releases, "
              f"{len(orphan)} tags without release ---")
        print(f"    orphan tag names: {[t.get('name') for t in orphan][:25]}")
        # check each orphan tag's commit for a real diff
        checked = 0
        touched_src = 0
        for t in orphan[:8]:
            sha = t.get("commit", {}).get("sha")
            c = api(f"repos/{full}/commits/{sha}") or {}
            files = c.get("files") or []
            stats = c.get("stats") or {}
            paths = [f.get("filename") for f in files][:6]
            print(f"    tag={t.get('name'):24s} sha={str(sha)[:8]} "
                  f"files={len(files):>3} +{stats.get('additions')}/-{stats.get('deletions')} "
                  f"msg={(c.get('commit',{}).get('message','') or '').splitlines()[0][:60]!r}")
            print(f"        paths: {paths}")
            checked += 1
            if files:
                touched_src += 1
        print(f"    => {touched_src}/{checked} orphan tags carry a non-empty commit diff")


def q3_paper_orchestra():
    print()
    print("=" * 100)
    print("Q3. paper-orchestra: star surge +45.8% in 24h -- re-run the 11-18 control")
    print("=" * 100)
    full = "google-research/paper-orchestra"
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": 100}) or []
    print(f"    latest 100 forks listed: {len(forks)}")
    fresh = 0
    by_date = Counter()
    for f in forks:
        oc = (f.get("owner") or {}).get("created_at")
        cd = f.get("created_at")
        if oc and cd:
            # crude ISO compare
            if oc[:10] >= "2026-11-12":
                fresh += 1
        if cd:
            by_date[cd[:10]] += 1
    print(f"    owners created on/after 2026-11-12: {fresh}/100")
    print(f"    fork creation dates (top 8): {by_date.most_common(8)}")
    # stargazer timeline
    st = api(f"repos/{full}/stargazers", {"per_page": 100},
             headers=["Accept: application/vnd.github.star+json"])
    if st:
        days = Counter(s.get("starred_at", "")[:10] for s in st)
        print(f"    latest 100 stargazers by day: {days.most_common(8)}")
    else:
        print("    stargazer timeline endpoint unavailable")
    # control group: same measure on a repo that grew normally
    for ctrl in ("torvalds/linux", "sveltejs/svelte"):
        cf = api(f"repos/{ctrl}/forks", {"sort": "newest", "per_page": 100}) or []
        fresh_c = sum(1 for f in cf
                      if ((f.get("owner") or {}).get("created_at") or "")[:10] >= "2026-11-12")
        print(f"    CONTROL {ctrl}: {fresh_c}/100 owners created on/after 2026-11-12")


if __name__ == "__main__":
    q1_name_vs_content()
    q2_superpowers_tags()
    q3_paper_orchestra()
