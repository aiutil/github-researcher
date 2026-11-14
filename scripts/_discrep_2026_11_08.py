#!/usr/bin/env python3
'''Resolve the zero-breach star/release discrepancy between the recorded
2026-11-06 snapshot and the live API, and sanity-check the trending page.'''

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
print("A. zero-breach: current vs old path -> same repo id?")
for path in ["repos/interplains/zero-breach", "repos/interplains/Zero-Breach-Toolkit"]:
    m, err = api(path)
    if m:
        print(f"  {path}")
        print(f"    id={m.get('id')} full_name={m.get('full_name')} stars={m.get('stargazers_count')} "
              f"forks={m.get('forks_count')} size={m.get('size')}KB created={m.get('created_at')}")
        print(f"    desc={str(m.get('description'))[:110]}")
    else:
        print(f"  {path} -> {err}")

print()
print("  release list (tags + published):")
rels, _ = api("repos/interplains/zero-breach/releases")
if isinstance(rels, list):
    for r in rels:
        print(f"    {r.get('tag_name'):10} published={r.get('published_at')} assets={len(r.get('assets') or [])}")

print()
print("  What did the repo frontmatter claim?")
fm = open("/home/lohasle/aiutil-github-researcher/projects/zero-breach.md", encoding="utf-8").read()
for line in fm.split("\n")[:16]:
    if "stars" in line or "date_added" in line or "last_seen" in line:
        print("   ", line[:400])

print()
print("=" * 72)
print("B. Same question for the 2026-11-07 archive entries (spot-check 4)")
for full, claimed in [
    ("voyager-so/vork", "197 stars / 1,502 blobs / 1 commit / forks 13 / subs 4"),
    ("JosssphZhou/poki", "406 stars / 23 commits / forks 83 / subs 1"),
    ("majorminorlabs/hermes-voice", "424 stars / 35 commits / forks 20 / subs 3"),
    ("devvmhq/devvm", "116 stars / 600 commits / forks 2 / subs 1"),
]:
    m, err = api(f"repos/{full}")
    if not m:
        print(f"  {full}: {err}")
        continue
    c, _ = api(f"repos/{full}/commits", {"per_page": 1})
    n = "? (need Link header)"
    p = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                       capture_output=True, text=True, env=ENV, timeout=60)
    mm = re.search(r'[?&]page=(\d+)>; rel="last"', p.stdout)
    if mm:
        n = mm.group(1)
    print(f"  {full}: live stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
          f"subs={m.get('subscribers_count')} commits~{n} | 11-06 record: {claimed}")

print()
print("=" * 72)
print("C. GitHub trending page - top repos today (sanity check on the window)")
import urllib.request

req = urllib.request.Request("https://github.com/trending?since=daily",
                             headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
    repos = re.findall(r'<h2 class="h3 lh-condensed">\s*<a href="/([^"]+)"', html)
    stars = re.findall(r'stargazers">\s*([\d,]+)\s*</a>', html)
    print(f"  trending entries: {len(repos)}")
    for i, r in enumerate(repos[:14]):
        s = stars[i] if i < len(stars) else "?"
        print(f"    {r:48} {s} stars")
except Exception as e:
    print("  trending fetch failed:", e)
