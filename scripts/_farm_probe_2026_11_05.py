#!/usr/bin/env python3
"""2026-11-05: probe the 11-04 farm batch READMEs for payload URLs. Read-only."""
import json, subprocess, os, re, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}
COHORT = "/tmp/collect_1105/cohort_2026-11-04.json"

URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
HINTS = ["Invoke-Expression", "irm ", "Invoke-RestMethod", "ExecutionPolicy Bypass",
         "Real-time protection", "Setup.ps1", "git-software.cc", "iwr ",
         "powershell", "cmd /c", "chmod", "curl "]


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def scan(full):
    rd = api(f"repos/{full}/readme", raw=True)
    if rd is None:
        return None
    urls = sorted(set(URL_RE.findall(rd)))
    hits = [h for h in HINTS if h.lower() in rd.lower()]
    return {"full": full, "len": len(rd), "urls": urls[:40], "hits": hits}


if __name__ == "__main__":
    items = json.load(open(COHORT))
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    n = 0
    payload_repos = []
    doms = {}
    for it in items:
        if it["size"] > 20:
            continue
        n += 1
        if n > limit:
            break
        s = scan(it["full_name"])
        if not s:
            print(f"  DEAD  {it['full_name']}")
            continue
        flag = "PAYLOAD" if s["hits"] else "clean  "
        if s["hits"]:
            payload_repos.append((it["full_name"], s["hits"], s["urls"]))
        for u in s["urls"]:
            doms[u] = doms.get(u, 0) + 1
        print(f"  {flag} {it['full_name']:<52} len={s['len']:<6} hits={s['hits']}")
    print("=" * 90)
    print(f"scanned {min(n, limit)} small repos; payload-bearing = {len(payload_repos)}")
    print("--- url domain counts ---")
    for u, c in sorted(doms.items(), key=lambda kv: -kv[1])[:25]:
        print(f"  {c:>4}  {u}")
    if payload_repos:
        print("--- payload repos ---")
        for f, h, u in payload_repos[:10]:
            print(f"  {f}\n     hits={h}\n     urls={u[:12]}")
