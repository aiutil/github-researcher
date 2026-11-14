#!/usr/bin/env python3
"""2026-11-05: compare payload-indicator sets across the 11-02/11-03/11-04 cohorts."""
import json, subprocess, os, re, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}

URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
# Deliberately broad: any remote-script execution idiom, not just the one domain.
HINTS = ["irm ", "Invoke-Expression", "Invoke-RestMethod", "iwr ", "ExecutionPolicy Bypass",
         "Real-time protection", "Setup.ps1", "git-software.cc", "powershell", "curl ",
         "gcm i*x", "Security Settings", "antivirus"]
PASTED = re.compile(r"```(?:cmd|powershell|ps1|bash|sh)\n([^`]{0,400})```", re.S)


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
    blocks = PASTED.findall(rd)
    remote_exec = [b.strip()[:120] for b in blocks
                   if re.search(r"(irm|iwr|curl|wget)\b.*\|\s*(&|iex|Invoke|sh|bash)", b, re.I)]
    return {"full": full, "len": len(rd), "urls": urls, "hits": hits,
            "remote_exec": remote_exec}


def run(date, limit):
    items = json.load(open(f"/tmp/collect_1105/cohort_{date}.json"))
    small = [i for i in items if i["size"] <= 20]
    n = 0
    payload = 0
    remexec = 0
    doms = {}
    print(f"### {date}: fetched={len(items)} small(<=20KB)={len(small)} scanning {min(len(small), limit)}")
    for it in small[:limit]:
        n += 1
        s = scan(it["full_name"])
        if not s:
            print(f"  DEAD {it['full_name']}")
            continue
        isp = "git-software.cc" in s["urls"] or any("git-software.cc" in u for u in s["urls"])
        if isp:
            payload += 1
        if s["remote_exec"]:
            remexec += 1
            print(f"  REMOTE-EXEC {it['full_name']:<48} {s['remote_exec'][:1]}")
        for u in s["urls"]:
            if u not in ("https://img.shields.io/badge/Download%20Project-2ea44f?style=for-the-badge&logo=download&logoColor=white",):
                doms[u] = doms.get(u, 0) + 1
        print(f"  {'PAYLOAD' if isp else 'clean  '} {it['full_name']:<52} len={s['len']:<6} hits={s['hits']}")
    print(f"--> {date}: scanned={n} git-software.cc={payload} any-remote-exec-block={remexec}")
    print("--- top domains ---")
    for u, c in sorted(doms.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {c:>4}  {u}")
    print("=" * 100)
    return n, payload, remexec


if __name__ == "__main__":
    for date, limit in (("2026-11-02", 40), ("2026-11-03", 10)):
        run(date, limit)
