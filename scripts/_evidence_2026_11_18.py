#!/usr/bin/env python3
"""Final evidence gathering for 2026-11-18 profiles.

1. ECC: read README + release commit chain (its 19 releases vs 20 tags).
2. modern-web-guidance-src: README + the src/ layout + what the 100 tags
   actually are (auto-published guide/eval snapshots).
3. paper-orchestra: README + agent list.
4. arcane: README.
5. open-code-review: README + plugin contract workflow.
"""

import json
import os
import subprocess
import sys
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
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


def readme(full):
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"])
    return rm or ""


def tree_paths(full, branch="main", limit=400):
    t = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    return sorted(b.get("path") for b in (t.get("tree") or []) if b.get("path"))[:limit]


def rel_chain(full, n=8):
    rel = api(f"repos/{full}/releases", {"per_page": 20}) or []
    if not isinstance(rel, list):
        return []
    out = []
    for r in rel[:n]:
        sha = (r.get("target_commitish") or "")
        out.append({
            "tag": r.get("tag_name"), "at": r.get("published_at"),
            "assets": len(r.get("assets") or []), "target": sha,
            "body": (r.get("body") or "")[:300],
        })
    return out


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "ecc"):
        print("========== affaan-m/ECC README (first 5000 chars) ==========")
        print(readme("affaan-m/ECC")[:5000])
        print("\n========== ECC releases ==========")
        for r in rel_chain("affaan-m/ECC", 10):
            print(f"  {r['tag']:<12} {r['at'][:19]} assets={r['assets']} "
                  f"target={r['target'][:12]}")
            if r["body"]:
                print(f"     body: {r['body'][:150]!r}")

    if which in ("all", "mwg"):
        print("\n\n========== GoogleChrome/modern-web-guidance-src README ==========")
        print(readme("GoogleChrome/modern-web-guidance-src")[:4500])
        print("\n========== src/ layout ==========")
        for p in tree_paths("GoogleChrome/modern-web-guidance-src", limit=100000):
            if p.startswith(("src/", "guides/", ".agents/")) and p.count("/") <= 3:
                print("   ", p)

    if which in ("all", "po"):
        print("\n\n========== google-research/paper-orchestra README ==========")
        print(readme("google-research/paper-orchestra")[:4500])

    if which in ("all", "arcane"):
        print("\n\n========== getarcaneapp/arcane README ==========")
        print(readme("getarcaneapp/arcane")[:3500])

    if which in ("all", "ocr"):
        print("\n\n========== alibaba/open-code-review README ==========")
        print(readme("alibaba/open-code-review")[:3500])
