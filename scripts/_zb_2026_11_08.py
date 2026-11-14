#!/usr/bin/env python3
'''Which interplains repo does the archived zero-breach profile describe?'''

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


for full in ["interplains/zero-breach", "interplains/Zero-Breach-Toolkit"]:
    print("=" * 70)
    print(full)
    tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    files = [t["path"] for t in (tree or {}).get("tree", []) if t["type"] == "blob"]
    print(f"  files({len(files)}): {files[:30]}")
    c, _ = api(f"repos/{full}/commits", {"per_page": 100})
    print(f"  commits(first page)={len(c) if isinstance(c, list) else c}")
    for marker in ["PRIVACY.md", "docs/VERIFYING.md", "NOTICE", "SECURITY.md"]:
        r, _ = api(f"repos/{full}/contents/{urllib.parse.quote(marker)}", raw=True,
                   headers=["Accept: application/vnd.github.raw"])
        print(f"  {marker}: {'PRESENT (' + str(len(r)) + ' bytes)' if r else 'absent'}")
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    head = (rm or "")[:900]
    print(f"  README head:\n    " + head.replace("\n", "\n    "))
