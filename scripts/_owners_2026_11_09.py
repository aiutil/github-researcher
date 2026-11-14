#!/usr/bin/env python3
"""Fetch owner account creation dates for all candidates + md5 of key files.

The `repos` API's owner object does not carry created_at, so we need one
`users/{owner}` call per distinct owner.
"""

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_2026_11_09.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/owners_2026_11_09.json"


def api(path, raw=False, headers=None):
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(path)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=90)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    owners = sorted({d["full_name"].split("/")[0] for d in data})
    print(f"distinct owners: {len(owners)}", file=sys.stderr)

    def work(o):
        u = api(f"users/{o}") or {}
        return o, {
            "created_at": u.get("created_at"),
            "public_repos": u.get("public_repos"),
            "followers": u.get("followers"),
            "type": u.get("type"),
            "name": u.get("name"),
            "blog": u.get("blog"),
        }

    with ThreadPoolExecutor(max_workers=6) as ex:
        res = dict(ex.map(work, owners))

    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(res)} owners -> {OUT}", file=sys.stderr)

    # --- cluster owners by creation minute ---
    by_min = defaultdict(list)
    for o, v in res.items():
        c = v.get("created_at")
        if c:
            by_min[c[:16]].append(o)
    print("\n=== owners grouped by creation MINUTE (>=2 owners) ===")
    for minute, olist in sorted(by_min.items()):
        if len(olist) >= 2:
            print(f"  {minute}  n={len(olist)}  {olist[:8]}")

    print("\n=== owner creation DATE distribution ===")
    print(Counter(v["created_at"][:10] for v in res.values() if v.get("created_at")).most_common(20))

    print("\n=== owners created 2026-08-15 (the suspicious cluster) ===")
    c15 = [o for o, v in res.items() if (v.get("created_at") or "").startswith("2026-08-15")]
    print(f"  count={len(c15)}")
    for o in sorted(c15, key=lambda x: res[x]["created_at"]):
        d = next((x for x in data if x["full_name"].split("/")[0] == o), None)
        st = f"⭐{d['stars']} ⑂{d['forks']} subs{d['subs']} {d['size_kb']}KB c{d['ncommits']} {d['language']}" if d else ""
        print(f"    {res[o]['created_at']}  {o:40s} repos={res[o]['public_repos']:>3} {st}")

    print("\n=== owner public_repos distribution ===")
    print(Counter(v.get("public_repos") for v in res.values()).most_common(12))


if __name__ == "__main__":
    main()
