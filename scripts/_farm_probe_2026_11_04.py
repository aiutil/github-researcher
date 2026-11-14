#!/usr/bin/env python3
"""2026-11-04: probe farm-cluster READMEs for payload URLs. Read-only GitHub API."""
import json, subprocess, os, re, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


PATTERNS = [
    r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+",
]
PAYLOAD_HINTS = [
    "Invoke-Expression", "irm ", "Invoke-RestMethod", "ExecutionPolicy Bypass",
    "pause", "Real-time protection", "Setup.ps1", "git-software.cc",
]


def scan(full):
    rd = api(f"repos/{full}/readme", raw=True)
    if not rd:
        return None
    urls = sorted(set(re.findall(PATTERNS[0], rd)))
    hits = [h for h in PAYLOAD_HINTS if h.lower() in rd.lower()]
    return {"full": full, "len": len(rd), "urls": urls[:40], "hits": hits}


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "cohort_scan":
        date = sys.argv[2]
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        res = japi(f"search/repositories?q=created:{date}+stars:>=40&per_page=100&sort=stars")
        items = res["items"]
        print(f"### created:{date} stars>=40 total={res['total_count']} fetched={len(items)}")
        small = [i for i in items if i["size"] <= 20]
        print(f"### size<=20KB: {len(small)}/{len(items)} = {len(small)/max(len(items),1)*100:.1f}%")
        # sample of the small ones
        n_hit = 0
        doms = {}
        for i in small[:limit]:
            s = scan(i["full_name"])
            if not s:
                print(f"  DEAD  {i['full_name']}")
                continue
            n_hit += 1 if s["hits"] else 0
            for u in s["urls"]:
                m = re.match(r"https?://([^/]+)", u)
                if m:
                    doms[m.group(1)] = doms.get(m.group(1), 0) + 1
            if s["hits"]:
                print(f"  HIT  {i['full_name']:<45} hits={s['hits']}")
            else:
                print(f"  ---  {i['full_name']:<45} len={s['len']} urls={s['urls'][:3]}")
        print(f"### scanned={n_hit} with_payload_hint={sum(1 for _ in [])}")
        print("### domains:", json.dumps(doms, indent=2, ensure_ascii=False))
    elif mode == "readme_urls":
        for full in sys.argv[2:]:
            s = scan(full)
            print("=" * 90)
            print(full, "len=", s["len"] if s else "FAIL")
            if s:
                print("  hits:", s["hits"])
                for u in s["urls"]:
                    print("   ", u)
    elif mode == "readme":
        for full in sys.argv[2:]:
            rd = api(f"repos/{full}/readme", raw=True)
            print("=" * 100)
            print("README:", full, "len=", len(rd) if rd else 0)
            print("=" * 100)
            print((rd or "FAILED")[:12000])
    elif mode == "meta":
        for full in sys.argv[2:]:
            r = japi(f"repos/{full}")
            if not r:
                print(f"  FAILED {full}")
                continue
            print(f"{full}")
            print(f"  stars={r['stargazers_count']} forks={r['forks_count']} subs={r['subscribers_count']} "
                  f"oi={r['open_issues_count']} size={r['size']}KB lang={r['language']} "
                  f"lic={(r.get('license') or {}).get('spdx_id')}")
            print(f"  created={r['created_at']} pushed={r['pushed_at']} owner={r['owner']['login']}({r['owner']['type']}) "
                  f"archived={r['archived']} topics={r.get('topics')}")
            print(f"  desc={r.get('description')}")
            print(f"  homepage={r.get('homepage')}")
