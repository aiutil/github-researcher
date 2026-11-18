#!/usr/bin/env python3
"""Decisive forensics for 2026-11-18.

Q1. SKILL.md FILE COUNT vs SKILL IDENTITY COUNT.
    A skill's identity is its parent directory name. If the same skill is
    replicated under .claude/ .codex/ .cursor/ .opencode/ with identical blob
    shas, then "N skills" is a multiplication artifact, not N skills.

Q2. paper-orchestra: 8 commits / 56 blobs / 0 releases / 0 tags, but 2,874
    stars with +1,175 today and 403 forks. Forks of a thin repo: organic or
    coordinated?

Q3. stargazer timeline (starred_at) if the endpoint permits it.
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

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
        return None, p.stderr.strip()[:300]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:300]}"


def skill_identity(full):
    m, _ = api(f"repos/{full}")
    m = m or {}
    branch = m.get("default_branch") or "main"
    tree, _ = api(f"repos/{full}/git/trees/{branch}?recursive=1")
    tree = tree or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    # identity = parent directory name
    ident = defaultdict(list)
    for b in skills:
        p = b.get("path")
        parent = os.path.basename(os.path.dirname(p)) if p else ""
        ident[parent].append((p, b.get("sha"), b.get("size")))
    sha_counter = Counter(b.get("sha") for b in skills)
    dup_sha = {s: c for s, c in sha_counter.items() if c > 1}
    # how many identities are pure harness replicas of one another
    replica_groups = 0
    replica_files = 0
    for name, lst in ident.items():
        if len(lst) > 1:
            replica_groups += 1
            replica_files += len(lst)
    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "n_blobs": len(blobs),
        "truncated_tree": tree.get("truncated"),
        "n_skill_files": len(skills),
        "n_identities": len(ident),
        "n_identities_replicated": replica_groups,
        "n_files_in_replicated": replica_files,
        "n_distinct_blob_shas": len(sha_counter),
        "n_dup_blobsha_groups": len(dup_sha),
        "top_dup_blobsha": sorted(dup_sha.values(), reverse=True)[:8],
        "identity_examples": {k: [x[0] for x in v][:4] for k, v in
                              list(ident.items())[:6]},
        "biggest_replicated": sorted(
            ((len(v), k) for k, v in ident.items()), reverse=True)[:6],
    }


def paper_orchestra():
    full = "google-research/paper-orchestra"
    out = {"repo": full}
    m, _ = api(f"repos/{full}")
    out["meta"] = {k: (m or {}).get(k) for k in
                   ("stargazers_count", "forks_count", "subscribers_count",
                    "open_issues_count", "size", "language", "created_at",
                    "pushed_at", "updated_at", "default_branch", "description",
                    "homepage", "topics", "archived", "fork",
                    "has_issues", "has_discussions")}
    out["meta"]["license"] = ((m or {}).get("license") or {}).get("spdx_id")
    tree, _ = api(f"repos/{full}/git/trees/{out['meta']['default_branch']}?recursive=1")
    blobs = [b for b in ((tree or {}).get("tree") or []) if b.get("type") == "blob"]
    out["n_blobs"] = len(blobs)
    out["blob_paths"] = sorted([b.get("path") for b in blobs if b.get("path")])[:80]
    commits, _ = api(f"repos/{full}/commits", {"per_page": 100})
    commits = commits if isinstance(commits, list) else []
    out["n_commits"] = len(commits)
    out["commits"] = [{
        "sha": c.get("sha", "")[:8],
        "date": ((c.get("commit") or {}).get("author") or {}).get("date"),
        "author": ((c.get("commit") or {}).get("author") or {}).get("name"),
        "msg": ((c.get("commit") or {}).get("message") or "").split("\n")[0][:90],
    } for c in commits]
    forks, _ = api(f"repos/{full}/forks", {"sort": "newest", "per_page": 100})
    forks = forks if isinstance(forks, list) else []
    out["n_forks_listed"] = len(forks)
    out["fork_sample"] = [{
        "full_name": f.get("full_name"),
        "created_at": f.get("created_at"),
        "owner_type": (f.get("owner") or {}).get("type"),
        "owner_created": (f.get("owner") or {}).get("created_at"),
    } for f in forks[:30]]
    out["fork_owner_types"] = dict(Counter(
        (f.get("owner") or {}).get("type") for f in forks))
    out["fork_created_dates"] = sorted({f.get("created_at") for f in forks})[:20]
    issues, _ = api(f"repos/{full}/issues", {"state": "all", "per_page": 50})
    issues = issues if isinstance(issues, list) else []
    out["n_issues"] = len(issues)
    out["issue_sample"] = [{
        "title": i.get("title"), "state": i.get("state"),
        "created_at": i.get("created_at"), "comments": i.get("comments"),
        "user": (i.get("user") or {}).get("login"),
    } for i in issues[:20]]
    # stargazer timeline
    stars, err = api(f"repos/{full}/stargazers",
                     {"per_page": 100},
                     headers=["Accept: application/vnd.github.star+json"])
    if stars:
        out["stargazer_page"] = [{
            "starred_at": s.get("starred_at"), "user": (s.get("user") or {}).get("login")
        } for s in stars[:20]]
        out["stargazer_error"] = None
    else:
        out["stargazer_error"] = err
    return out


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "identity"):
        print("========== Q1: SKILL.md files vs skill identities ==========")
        for t in ["affaan-m/ECC", "cursor/plugins", "tradermonty/claude-trading-skills",
                  "elementalsouls/Claude-BugHunter", "Tencent/LoopForge",
                  "backnotprop/plannotator", "obra/superpowers",
                  "anthropics/skills", "addyosmani/agent-skills",
                  "google-labs-code/stitch-skills"]:
            r = skill_identity(t)
            print(f"\n--- {r['repo']} --- ⭐{r['stars']} forks={r['forks']} "
                  f"subs={r['subs']} oi={r['oi']} blobs={r['n_blobs']} "
                  f"truncated={r['truncated_tree']} lang={r['language']}")
            print(f"    SKILL.md files = {r['n_skill_files']}   "
                  f"distinct identities = {r['n_identities']}   "
                  f"identities replicated across dirs = {r['n_identities_replicated']} "
                  f"(files involved {r['n_files_in_replicated']})")
            print(f"    distinct blob shas = {r['n_distinct_blob_shas']}   "
                  f"blob-sha groups with >1 copy = {r['n_dup_blobsha_groups']}   "
                  f"largest identical-sha multiplicities = {r['top_dup_blobsha']}")
            print(f"    biggest replicated identities = {r['biggest_replicated']}")

    if which in ("all", "po"):
        print("\n\n========== Q2: google-research/paper-orchestra ==========")
        po = paper_orchestra()
        print(json.dumps(po, ensure_ascii=False, indent=1)[:9000])
