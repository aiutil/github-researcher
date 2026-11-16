#!/usr/bin/env python3
"""Final evidence dump for the 2026-11-17 report.

1. The placeholder-repo signature: content of the 10-byte README.md files.
2. Subscriber lists for the high-subs cheat repos (are the watchers real?).
3. Per-project detail dump for the nine key projects.
"""
import json
import os
import re
import subprocess
import urllib.parse
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


def part1_placeholders():
    print("=" * 92)
    print("1. PLACEHOLDER REPO SIGNATURE")
    print("=" * 92)
    ph = ["SandstoneShoutMoon/szoyxrqs", "VergeEnvoyAdze/fzohpjud",
          "ashtherapistpillar/cwjhmbpo", "OceanChandlerSewer/trckulpa",
          "DestroyerStrait/rqpylldg", "delugesovereignphase/khcmkgzv"]
    for full in ph:
        rm = api(f"repos/{full}/readme", raw=True,
                 headers=["Accept: application/vnd.github.raw"])
        m = api(f"repos/{full}") or {}
        tree = api(f"repos/{full}/git/trees/{m.get('default_branch') or 'main'}?recursive=1") or {}
        blobs = [(b.get("path"), b.get("size"), b.get("sha")) for b in (tree.get("tree") or [])
                 if b.get("type") == "blob"]
        print(f"\n  {full}")
        print(f"    created={m.get('created_at')} pushed={m.get('pushed_at')} "
              f"stars={m.get('stargazers_count')} size={m.get('size')}KB "
              f"license={(m.get('license') or {}).get('spdx_id')}")
        print(f"    blobs={blobs}")
        print(f"    README bytes={rm!r}")


def part2_subscribers():
    print("\n" + "=" * 92)
    print("2. SUBSCRIBER LISTS (are the high subs/star watchers real accounts?)")
    print("=" * 92)
    for full in ["OceanChandlerSewer/rob-run-cheat-private",
                 "SandstoneShoutMoon/ROB-RUN-cheat-client",
                 "ashtherapistpillar/PUBG-private-cheat-midnight",
                 "VergeEnvoyAdze/GTA5-cheat-client"]:
        subs = api(f"repos/{full}/subscribers") or []
        m = api(f"repos/{full}") or {}
        logins = [s.get("login") for s in subs] if isinstance(subs, list) else []
        # account creation dates of a sample of subscribers
        sample = logins[:8]
        rows = []
        for lg in sample:
            u = api(f"users/{lg}") or {}
            rows.append((lg, (u.get("created_at") or "")[:10],
                         u.get("followers"), u.get("public_repos")))
        print(f"\n  {full}: stars={m.get('stargazers_count')} "
              f"subs={m.get('subscribers_count')} watchers={m.get('watchers_count')} "
              f"forks={m.get('forks_count')} oi={m.get('open_issues_count')}")
        print(f"    subscribers ({len(logins)}): {logins[:20]}")
        for r in rows:
            print(f"      {r[0]:<26} created={r[1]} foll={r[2]} repos={r[3]}")


KEY = [
    "kajisho5/ffmpeg-skill",
    "NVIDIA/SkillEvaluator",
    "google/elephant-goldfish-model",
    "vercel-labs/agent-browser",
    "ag-ui-protocol/ag-ui",
    "elementalsouls/Claude-BugHunter",
    "mvanhorn/last30days-skill",
    "OceanChandlerSewer/rob-run-cheat-private",
    "boringmarketer/boring-marketing-skills",
]


def part3_detail():
    print("\n" + "=" * 92)
    print("3. KEY PROJECT DETAIL")
    print("=" * 92)
    for full in KEY:
        m = api(f"repos/{full}") or {}
        branch = m.get("default_branch") or "main"
        tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
        paths = [b.get("path") for b in (tree.get("tree") or []) if b.get("type") == "blob"]
        top = [p for p in paths if p.count("/") <= 1][:26]
        rm = api(f"repos/{full}/readme", raw=True,
                 headers=["Accept: application/vnd.github.raw"]) or ""
        commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
        if not isinstance(commits, list):
            commits = []
        contribs = api(f"repos/{full}/contributors", {"per_page": 100}) or []
        owner = m.get("owner") or {}
        u = api(f"users/{owner.get('login')}") or {}
        print(f"\n" + "-" * 92)
        print(f"{full}")
        print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
              f"subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} "
              f"size={m.get('size')}KB lang={m.get('language')} "
              f"lic={(m.get('license') or {}).get('spdx_id')}")
        print(f"  created={m.get('created_at')} pushed={m.get('pushed_at')} "
              f"homepage={m.get('homepage')} topics={m.get('topics')}")
        print(f"  owner={owner.get('login')} owner_created={u.get('created_at')} "
              f"owner_foll={u.get('followers')} owner_repos={u.get('public_repos')}")
        print(f"  blobs={len(paths)} commits(<=100)={len(commits)} "
              f"contributors={[(c.get('login'), c.get('contributions')) for c in (contribs or [])][:6]}")
        print(f"  top-level paths: {top}")
        n_skill = sum(1 for p in paths if p.endswith("SKILL.md"))
        print(f"  SKILL.md count = {n_skill}")
        # CI
        print(f"  workflows: {[p for p in paths if p.startswith('.github/workflows')][:8]}")
        print(f"  manifests: {[p for p in paths if p.endswith('plugin.json') or p.endswith('extension.json') or p.endswith('server.json')][:8]}")
        print("  commit msgs:")
        for c in commits[:8]:
            print("    -", ((c.get("commit") or {}).get("message") or "").split("\n")[0][:84])


if __name__ == "__main__":
    part1_placeholders()
    part2_subscribers()
    part3_detail()
