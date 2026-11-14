#!/usr/bin/env python3
'''Gather interplains/Zero-Breach-Toolkit evidence for a new archive profile, and
verify the upstream interplains/zero-breach release count.'''

import json
import os
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


UP = "interplains/zero-breach"
TK = "interplains/Zero-Breach-Toolkit"

print("=" * 70)
print("UPSTREAM release count (the 10-30 daily claimed 0):")
rels, _ = api(f"repos/{UP}/releases")
print(f"  releases={len(rels) if isinstance(rels, list) else rels}")
if isinstance(rels, list):
    for r in rels[:4]:
        print(f"    {r.get('tag_name')} published={r.get('published_at')} assets={len(r.get('assets') or [])}")
print("  NOTE: pushed_at is 2026-10-20T14:26:41Z and has not moved, so releases existed on 2026-10-30.")

print()
print("=" * 70)
print("TOOLKIT metadata:")
m, _ = api(f"repos/{TK}")
print(f"  id={m.get('id')} stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
      f"subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} size={m.get('size')}KB "
      f"lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')}")
print(f"  created={m.get('created_at')} pushed={m.get('pushed_at')} owner={m.get('owner',{}).get('login')}"
      f"({m.get('owner',{}).get('type')}) topics={m.get('topics')}")
print(f"  desc={m.get('description')}")
ct, _ = api(f"repos/{TK}/contributors")
print(f"  contributors={len(ct) if isinstance(ct, list) else ct}")
rels, _ = api(f"repos/{TK}/releases")
if isinstance(rels, list):
    print(f"  releases={len(rels)}")
    for r in rels[:6]:
        print(f"    {r.get('tag_name')} published={r.get('published_at')} assets={len(r.get('assets') or [])}")
    print(f"    ... oldest: {rels[-1].get('tag_name')} {rels[-1].get('published_at')}")

print()
print("=" * 70)
print("TOOLKIT key files:")
tree, _ = api(f"repos/{TK}/git/trees/HEAD?recursive=1")
files = [t["path"] for t in (tree or {}).get("tree", []) if t["type"] == "blob"]
print(f"  total files={len(files)}")
interesting = [f for f in files if any(k in f.upper() for k in ["PRIVACY", "VERIFY", "SECURITY", "NOTICE", "SIGN", "LOCALE", "ANDROID", "IOS", "IPHONE", "BACKUP"])]
print(f"  interesting ({len(interesting)}): {interesting[:40]}")
print(f"  top-level: {[f for f in files if '/' not in f][:30]}")

for path in ["PRIVACY.md", "docs/VERIFYING.md", "SECURITY.md"]:
    r, _ = api(f"repos/{TK}/contents/{urllib.parse.quote(path)}", raw=True,
               headers=["Accept: application/vnd.github.raw"])
    if r:
        print(f"\n--- {path} ({len(r)} bytes) ---")
        print(r[:2600])
