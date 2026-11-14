#!/usr/bin/env python3
"""Deep evidence for daily/2026-11-12.md (data window = repos created 2026-11-11 UTC)."""
import json
import os
import subprocess
import time
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
CAND = "/tmp/w1112/cand_1111.json"


def api(path_, headers=None, raw=False):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path_)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def raw_file(full, path_):
    return api(f"repos/{full}/contents/{path_}",
               headers=["Accept: application/vnd.github.raw"], raw=True) or ""


def md5(s):
    import hashlib
    return hashlib.md5(s.encode("utf-8", "replace")).hexdigest()


def fork_timing(full, sample=40):
    forks = api(f"repos/{full}/forks?per_page=100&sort=newest")
    if not forks or not isinstance(forks, list):
        return None
    ts = []
    for f in forks[:sample]:
        c = f.get("created_at")
        if c:
            ts.append(datetime.fromisoformat(c.replace("Z", "+00:00")))
    ts.sort()
    if len(ts) < 2:
        return {"n": len(ts), "med": None, "le10": None, "span_min": None}
    gaps = sorted((ts[i + 1] - ts[i]).total_seconds() for i in range(len(ts) - 1))
    return {
        "n": len(ts),
        "med": gaps[len(gaps) // 2],
        "le10": sum(1 for g in gaps if g <= 10),
        "span_min": round((ts[-1] - ts[0]).total_seconds() / 60, 1),
    }


TARGETS = [
    "BankerInterface/youtube-seo-optimizer",
    "Nobleglusurvive/discord-quest-completer",
    "setyamickala/fastmint-fcfs-agentic",
    "snicolast/SegaRally2Native",
    "c6lang/c6",
    "nestho/impacket-rs",
    "ferhatcore/claude-codex-project-os",
    "kate-land/ga100vfi",
    "SsKanDon/blender-ai-mcp-addon",
    "smm-gg/smm-panel-api",
    "SteelMillerBar/auto-twitch-drops-claim",
    "FrostPillage/CapCut-Pro-Version",
]

for full in TARGETS:
    print("=" * 100)
    print(f"### {full}")
    m = api(f"repos/{full}") or {}
    for k in ("stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
              "size", "language", "created_at", "pushed_at", "archived", "description"):
        print(f"  {k:20s} = {m.get(k)}")
    lic = m.get("license") or {}
    print(f"  license.spdx         = {lic.get('spdx_id')}")
    print(f"  topics                = {m.get('topics')}")
    ow = m.get("owner") or {}
    print(f"  owner.type            = {ow.get('type')}")

    tree = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = tree.get("tree") or []
    blobs = [b for b in blobs if b.get("type") == "blob"]
    print(f"  -- TREE ({len(blobs)} blobs) --")
    for b in sorted(blobs, key=lambda x: -(x.get("size") or 0))[:28]:
        print(f"      {b.get('size'):>8}  {b.get('path')}")
    if len(blobs) > 28:
        print(f"      ... +{len(blobs)-28} more")

    commits = api(f"repos/{full}/commits?per_page=100") or []
    if isinstance(commits, list):
        secs = set()
        for c in commits:
            au = (c.get("commit", {}) or {}).get("author", {}) or {}
            if au.get("date"):
                secs.add(au["date"][-2:])
        print(f"  -- COMMITS (page1={len(commits)}, distinct_secs={len(secs)}) --")
        for c in commits[:10]:
            au = (c.get("commit", {}) or {}).get("author", {}) or {}
            print(f"      {au.get('date')}  {(c.get('commit',{}) or {}).get('message','').splitlines()[0][:110]}")

    contrib = api(f"repos/{full}/contributors") or []
    if isinstance(contrib, list):
        print(f"  contributors={len(contrib)} :: " +
              ", ".join(f"{c.get('login')}({c.get('contributions')})" for c in contrib[:8]))
    rel = api(f"repos/{full}/releases") or []
    if isinstance(rel, list):
        print(f"  releases={len(rel)} :: " + ", ".join(str(r.get("tag_name")) for r in rel[:8]))

    ft = fork_timing(full)
    if ft:
        print(f"  FORKS: sampled={ft['n']} med_gap={ft['med']}s le10={ft['le10']} span={ft['span_min']}min")

    rm = raw_file(full, "README.md")
    print(f"  -- README (len={len(rm)}, md5={md5(rm)}) --")
    print(rm[:2600])

    # README md5 cross-check against known farm signatures
    print(f"  README_MD5={md5(rm)}")
    time.sleep(0.4)
