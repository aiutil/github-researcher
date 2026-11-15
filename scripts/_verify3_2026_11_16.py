#!/usr/bin/env python3
"""Final evidence pass for the 2026-11-16 daily: remaining key projects."""
import hashlib
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
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


def blob(full, path):
    return api(f"repos/{full}/contents/{path}", raw=True,
               headers=["Accept: application/vnd.github.raw"])


print("=== upstream Gemini vs mirror: license & payload divergence ===")
up = "MatinSenPai/Gemini-Config-Checker"
mi = "WindGatorRise37/Gemini-Config-Checker-"
for full in (up, mi):
    m = api(f"repos/{full}") or {}
    print(f"  {full}")
    print(f"    lic={(m.get('license') or {}).get('spdx_id')} stars={m.get('stargazers_count')} "
          f"forks={m.get('forks_count')} subs={m.get('subscribers_count')} size={m.get('size')}KB "
          f"created={m.get('created_at')} pushed={m.get('pushed_at')}")
    print(f"    fork={m.get('fork')} parent={(m.get('parent') or {}).get('full_name')}")
    rm = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"]) or ""
    print(f"    readme_len={len(rm)} md5={hashlib.md5(rm.encode()).hexdigest()[:12]}")
    for u in set(re.findall(r"https?://[^\s)\"'<>]+", rm)):
        if "dropbox" in u or "releases/download" in u:
            print(f"    payload: {u}")
    lic = blob(full, "LICENSE") or ""
    print(f"    LICENSE head: {lic.splitlines()[0][:90] if lic else '(none)'}")
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    blobs = [b for b in (t.get("tree") or []) if b.get("type") == "blob"]
    print(f"    blobs={len(blobs)}")

print("\n=== upstream repo tree (to compare with mirror layout) ===")
t = api(f"repos/{up}/git/trees/HEAD?recursive=1") or {}
print("  " + ", ".join(sorted(b.get("path", "") for b in (t.get("tree") or []))[:40]))

print("\n=== pydtcpip: CI + release + PyPI + issue sample ===")
p = "tsukumijima/pydtcpip"
for f in (".github/workflows/ci.yml", ".github/workflows/deploy.yml"):
    d = blob(p, f) or ""
    print(f"  --- {f} ({len(d)} B) ---")
    for line in d.splitlines()[:28]:
        print(f"    {line}")
iss = api(f"repos/{p}/issues", {"state": "open", "per_page": 12}) or []
print(f"  open issues ({len(iss)}):")
for i in iss:
    print(f"    #{i.get('number')} [{i.get('user',{}).get('login')}] {i.get('title')[:80]}")

print("\n=== coordinator: skills + token ceilings ===")
c = "petekp/coordinator"
for f in (".token-ceilings", "skills/coordinator/SKILL.md"):
    d = blob(c, f) or ""
    print(f"  --- {f} ({len(d)} B) ---")
    for line in d.splitlines()[:18]:
        print(f"    {line[:120]}")

print("\n=== interspace: LICENSE presence ===")
m = api(f"repos/cnrad/interspace") or {}
print(f"  license={(m.get('license') or {}).get('spdx_id')} key={(m.get('license') or {}).get('key')}")
lic = blob("cnrad/interspace", "LICENSE") or ""
print(f"  LICENSE first 3 lines: {lic.splitlines()[:3]}")

print("\n=== mixbar: THIRD_PARTY_NOTICES + docs ===")
for f in ("THIRD_PARTY_NOTICES.md", "docs"):
    d = blob("lishuangqiang/mixbar", f) or ""
    print(f"  --- {f} ({len(d)} B) ---")
    for line in d.splitlines()[:10]:
        print(f"    {line[:120]}")

print("\n=== rauchg/winamp-ui-sdk: source layout ===")
t = api("repos/rauchg/winamp-ui-sdk/git/trees/HEAD?recursive=1") or {}
for b in (t.get("tree") or []):
    if b.get("type") == "blob":
        print(f"    {b.get('size'):>9} B  {b.get('path')}")

print("\n=== h3-fight: library content ===")
t = api("repos/huangserva/h3-fight/git/trees/HEAD?recursive=1") or {}
for b in (t.get("tree") or []):
    if b.get("type") == "blob" and b.get("path", "").startswith(("工具/", "库/")):
        print(f"    {b.get('size'):>8} B  {b.get('path')}")

print("\n=== TradingAgents-crypto: bytx layer + .env.enterprise ===")
for f in (".env.enterprise.example", "cli"):
    d = blob("Dart-veider01/TradingAgents-crypto", f) or ""
    print(f"  --- {f} ({len(d)} B) ---")
    for line in d.splitlines()[:14]:
        print(f"    {line[:120]}")
cm = api("repos/Dart-veider01/TradingAgents-crypto/commits", {"per_page": 10}) or []
print("  commits:")
for x in cm:
    cc = x.get("commit") or {}
    au = cc.get("author") or {}
    print(f"    {au.get('date')} {(cc.get('message') or '').splitlines()[0][:70]}")

print("\n=== WZM offline: MANIFEST ===")
d = blob("Pixelgamer4k/WZM-4.5.2-offline-source", "MANIFEST.txt") or ""
for line in d.splitlines()[:22]:
    print(f"    {line[:120]}")
