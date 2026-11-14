#!/usr/bin/env python3
"""Deep evidence for the 2026-11-12 window (targets daily/2026-11-13.md)."""
import json, os, subprocess, time, hashlib
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")


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


def md5(s):
    return hashlib.md5(s.encode("utf-8", "replace")).hexdigest()


def fork_timing(full, sample=60):
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
    return {"n": len(ts), "med": gaps[len(gaps) // 2],
            "le10": sum(1 for g in gaps if g <= 10),
            "span_min": round((ts[-1] - ts[0]).total_seconds() / 60, 1)}


TARGETS = [
    "AIRzZ90/study-materials-fork",
    "rivet-dev/open-orange",
    "Simon3Sarkis/super-odyssey-pc-recomp",
    "DevedevT/FFmpeg-GUI-Editor-Windows",
    "lawandrorder/mate",
    "routerhubSI/kimi-uncensored",
    "simonklee/opencode-native-preview",
    "siwen-121/agent-shared-facts",
    "jackson-cmd/risk-aware-trading-agents",
    "2697106714/cpa-bps",
    "StitchSerfJump/Microsoft-Visio-For-Windows",
    "BottingRocks/Shape",
    "alinuo666/ComfyUI-Banzhang-All",
]

for full in TARGETS:
    print("=" * 100)
    print(f"### {full}")
    m = api(f"repos/{full}") or {}
    for k in ("stargazers_count", "forks_count", "subscribers_count", "open_issues_count",
              "size", "language", "created_at", "pushed_at", "archived", "description", "homepage"):
        print(f"  {k:20s} = {m.get(k)}")
    lic = m.get("license") or {}
    print(f"  license.spdx         = {lic.get('spdx_id')}")
    print(f"  topics                = {m.get('topics')}")
    ow = m.get("owner") or {}
    print(f"  owner.type            = {ow.get('type')}  owner.created={ow.get('created_at')}")
    ua = api(f"users/{ow.get('login')}") or {}
    print(f"  owner.public_repos    = {ua.get('public_repos')}  followers={ua.get('followers')}  created={ua.get('created_at')}")

    tree = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    print(f"  -- TREE ({len(blobs)} blobs) --")
    for b in sorted(blobs, key=lambda x: -(x.get("size") or 0))[:22]:
        print(f"      {b.get('size'):>8}  {b.get('path')}")
    if len(blobs) > 22:
        print(f"      ... +{len(blobs)-22} more")

    commits = api(f"repos/{full}/commits?per_page=100") or []
    if isinstance(commits, list):
        secs = set()
        for c in commits:
            au = (c.get("commit", {}) or {}).get("author", {}) or {}
            if au.get("date"):
                secs.add(au["date"][-2:])
        print(f"  -- COMMITS (page1={len(commits)}, distinct_secs={len(secs)}) --")
        for c in commits[:12]:
            au = (c.get("commit", {}) or {}).get("author", {}) or {}
            print(f"      {au.get('date')}  {(c.get('commit',{}) or {}).get('message','').splitlines()[0][:110]}")
        bots = 0
        for c in commits:
            if c.get("author", {}) and (c["author"].get("login") or "").endswith("[bot]"):
                bots += 1
        print(f"  bot_commits={bots}/{len(commits)}")

    contrib = api(f"repos/{full}/contributors") or []
    if isinstance(contrib, list):
        print("  contributors=%d :: " % len(contrib) + ", ".join(f"{c.get('login')}({c.get('contributions')})" for c in contrib[:8]))
    rel = api(f"repos/{full}/releases") or []
    if isinstance(rel, list):
        print(f"  releases={len(rel)} :: " + ", ".join(str(r.get("tag_name")) for r in rel[:8]))

    ft = fork_timing(full)
    if ft:
        print(f"  FORKS: sampled={ft['n']} med_gap={ft['med']}s le10={ft['le10']} span={ft['span_min']}min")

    rm = api(f"repos/{full}/readme", headers=["Accept: application/vnd.github.raw"], raw=True) or ""
    print(f"  -- README (len={len(rm)}, md5={md5(rm)}) --")
    print(rm[:3000])
    time.sleep(0.3)
