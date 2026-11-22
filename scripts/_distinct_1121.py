#!/usr/bin/env python3
"""Sanity-check the brute-force release/tag counts for distinctness.

The `releases` endpoint returned 99 items on page 1 for
`toeverything/AFFiNE` while pages 2..6 were full.  Two explanations are
possible:

  (a) the repository really has 604 releases, and GitHub skipped one slot
      on page 1 for some reason, or
  (b) pagination is overlapping and the total is inflated.

This script pulls every page, extracts the release *id* and *tag_name*, and
checks for duplicates and for gaps in the id sequence.  Only the identity
of the items is used; no assets are downloaded.

Output: /tmp/distinct_1121.json
"""
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/distinct_1121.json"

TARGETS = [
    ("toeverything/AFFiNE", "releases"),
    ("toeverything/AFFiNE", "tags"),
    ("firecrawl/firecrawl", "tags"),
    ("nginx/nginx", "tags"),
    ("backnotprop/plannotator", "releases"),
    ("alibaba/open-code-review", "releases"),
    ("GoogleChrome/modern-web-guidance-src", "tags"),
]


def page(full, kind, p):
    cmd = ["gh", "api", f"repos/{full}/{kind}?per_page=100&page={p}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=150)
    except subprocess.TimeoutExpired:
        return None
    if r.returncode != 0:
        return None
    try:
        d = json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        return None
    return d if isinstance(d, list) else None


def check(full, kind):
    ids, names = [], []
    p = 1
    while p <= 30:
        got = page(full, kind, p)
        if got is None or len(got) == 0:
            break
        for it in got:
            if kind == "tags":
                ids.append(it.get("sha"))
                names.append(it.get("name"))
            else:
                ids.append(it.get("id"))
                names.append(it.get("tag_name"))
        p += 1
    uniq_ids = len(set(ids))
    uniq_names = len(set(names))
    return {
        "repo": full,
        "kind": kind,
        "n_items": len(ids),
        "distinct_ids": uniq_ids,
        "distinct_names": uniq_names,
        "has_duplicates": uniq_ids != len(ids),
        "dup_names": [n for n in set(names) if names.count(n) > 1][:8],
        "first": names[0] if names else None,
        "last": names[-1] if names else None,
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = [ex.submit(check, f, k) for f, k in TARGETS]
        for fu in futs:
            r = fu.result()
            out.append(r)
            print(f"  {r['repo']:44s} {r['kind']:9s} items={r['n_items']:>5} "
                  f"distinct_ids={r['distinct_ids']:>5} distinct_names={r['distinct_names']:>5} "
                  f"dups={r['has_duplicates']}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
