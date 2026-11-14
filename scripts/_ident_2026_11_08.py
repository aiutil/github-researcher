#!/usr/bin/env python3
'''Resolve zero-breach identity + gather remaining project evidence.'''

import json
import os
import re
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:
        return None, "parse"


print("=" * 72)
print("A. zero-breach vs Zero-Breach-Toolkit: fork? parent? releases?")
for full in ["interplains/zero-breach", "interplains/Zero-Breach-Toolkit"]:
    m, _ = api(f"repos/{full}")
    if not m:
        print(f"  {full}: not found")
        continue
    print(f"\n  {full}")
    print(f"    id={m.get('id')} fork={m.get('fork')} parent={(m.get('parent') or {}).get('full_name')} "
          f"source={(m.get('source') or {}).get('full_name')}")
    print(f"    stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} "
          f"oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} "
          f"lic={(m.get('license') or {}).get('spdx_id')} created={m.get('created_at')} pushed={m.get('pushed_at')}")
    rels, _ = api(f"repos/{full}/releases")
    if isinstance(rels, list):
        tags = [(r.get("tag_name"), r.get("published_at"), len(r.get("assets") or [])) for r in rels]
        print(f"    releases={len(tags)}: {tags[:6]}{' ...' if len(tags) > 6 else ''}")
    ct, _ = api(f"repos/{full}/contributors")
    print(f"    contributors={len(ct) if isinstance(ct, list) else ct}")

print()
print("=" * 72)
print("B. trending page (fixed regex)")
import urllib.request

req = urllib.request.Request("https://github.com/trending?since=daily",
                             headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
    repos = re.findall(r'href="/([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)"[^>]*>\s*<svg', html)
    stars = re.findall(r'aria-label="([\d,]+) users? starred', html)
    print(f"  entries={len(repos)}")
    for i, r in enumerate(repos[:16]):
        s = stars[i] if i < len(stars) else "?"
        print(f"    {r:50} {s}")
except Exception as e:
    print("  trending fetch failed:", e)

print()
print("=" * 72)
print("C. solstice README")
r, _ = api("repos/SamG-Coder/solstice/readme", raw=True,
           headers=["Accept: application/vnd.github.raw"])
print((r or "")[:2600])

print()
print("=" * 72)
print("D. ghostclick: 'how it works' + FAQ excerpt")
r, _ = api("repos/MajestyPoemFold/ghostclick-mouse-double-click-fix/readme", raw=True,
           headers=["Accept: application/vnd.github.raw"])
t = r or ""
i = t.find("## How it works")
if i < 0:
    i = t.find("how it works")
print(t[i:i + 2400])
