#!/usr/bin/env python3
"""Compact endpoint + payload verification for 2026-11-01 report."""
import json, os, re, subprocess, urllib.request, urllib.error

ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}
def api(p, raw=False):
    a = ["gh","api",p] + (["-H","Accept:application/vnd.github.raw"] if raw else [])
    r = subprocess.run(a, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None
def j(p):
    try: return json.loads(api(p) or "null")
    except Exception: return None

def head(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 research"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            b = r.read(400000)
            return r.status, len(b), b
    except urllib.error.HTTPError as e:
        try: b = e.read(400000)
        except Exception: b = b""
        return e.code, len(b), b
    except Exception as e:
        return "ERR", str(e)[:60], b""

print("== ENDPOINTS (host, path, status, bytes) ==")
EPS = [
 ("battery-peek","https://activation-gateway.cc/activation.ps1"),
 ("battery-peek","https://activation-gateway.cc/"),
 ("battery-peek","https://shell-activation.top/"),
 ("battery-peek","https://shell-activation.top/activation.ps1"),
 ("battery-peek","https://shell-activation.top/install.ps1"),
 ("farm2026","https://git-software.cc/ps/Setup.ps1"),
 ("farm2026","https://git-software.cc/"),
 ("farm2026","https://telegra.ph/TRANSITION-06-17-3"),
]
for tag,u in EPS:
    s,n,b = head(u)
    hosts = sorted(set(x.split("/")[2] for x in re.findall(rb"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+", b)))[:6]
    print(f"  {tag:10s} {u:52s} status={s} bytes={n} hosts={hosts}")

print("\n== battery-peek README irm lines ==")
rd = api("repos/Yugiri-AO/battery-peek/readme", raw=True) or ""
for ln in rd.splitlines():
    if "irm" in ln.lower() or "activation" in ln.lower() or "http" in ln.lower():
        print("   |", ln.strip()[:160])
print("\n== battery-peek file tree ==")
t = j("repos/Yugiri-AO/battery-peek/git/trees/HEAD?recursive=1") or {}
for e in t.get("tree",[]):
    print(f"   {e.get('type'):5s} {e.get('size')} {e.get('path')}")
print("\n== battery-peek commits ==")
for c in (j("repos/Yugiri-AO/battery-peek/commits?per_page=30") or []):
    print("   ", c["commit"]["author"]["date"], c["commit"]["message"].splitlines()[0][:90])
