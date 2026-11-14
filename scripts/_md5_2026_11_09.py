#!/usr/bin/env python3
"""md5-fingerprint the candidate file set to detect shared templates."""

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
TARGETS = sys.argv[1].split(",")
PATHS = sys.argv[2].split(",") if len(sys.argv) > 2 else [
    "Cargo.lock", "src/theme.rs", "src/widgets.rs", "docs/design/mockup.html",
    "src/app.rs", "README.md", "LICENSE", "src/stats.rs",
]


def api(path, raw=True):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github.raw", path]
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=90)
    if p.returncode != 0:
        return None
    return p.stdout


def main():
    by_hash = defaultdict(list)
    for full in TARGETS:
        print(f"\n### {full}", file=sys.stderr)
        for path in PATHS:
            body = api(f"repos/{full}/contents/{path}")
            if body is None:
                continue
            h = hashlib.md5(body.encode("utf-8", "replace")).hexdigest()
            by_hash[(path, h)].append(full)
            print(f"  {h}  {len(body):>8}B  {path}", file=sys.stderr)
            time.sleep(0.25)
    print("\n\n=== SHARED HASHES (same path + same md5 across repos) ===")
    for (path, h), repos in sorted(by_hash.items(), key=lambda x: -len(x[1])):
        if len(repos) > 1:
            print(f"  {h}  {path}  ->  {repos}")


if __name__ == "__main__":
    main()
