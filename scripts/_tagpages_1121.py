#!/usr/bin/env python3
"""Brute-force enumeration of the tags endpoint for one repository.

Used to settle the single remaining disagreement (firecrawl/firecrawl: Link
header said last page 9, binary search said 10).  This method makes no
assumption about page numbering: it walks pages 1..N until it sees a page
that is empty, and reports the per-page item counts so the shape of the
pagination is visible.

Output: /tmp/tagpages_1121.json
"""
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/tagpages_1121.json"

TARGETS = ["firecrawl/firecrawl", "nginx/nginx", "toeverything/AFFiNE", "ag-ui-protocol/ag-ui"]


def page(full, kind, p):
    cmd = ["gh", "api", f"repos/{full}/{kind}?per_page=100&page={p}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
    except subprocess.TimeoutExpired:
        return None
    if r.returncode != 0:
        return None
    try:
        d = json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        return None
    return d if isinstance(d, list) else None


def walk(full, kind):
    rows = []
    p = 1
    while p <= 40:
        got = page(full, kind, p)
        if got is None:
            rows.append({"page": p, "n": None, "error": True})
            break
        rows.append({"page": p, "n": len(got)})
        if len(got) == 0:
            break
        p += 1
    return rows


def main():
    out = {}
    for full in TARGETS:
        for kind in ("tags", "releases"):
            rows = walk(full, kind)
            total = sum(r["n"] for r in rows if r["n"])
            nonempty = [r for r in rows if r["n"]]
            out.setdefault(full, {})[kind] = {
                "per_page_counts": rows,
                "total": total,
                "last_nonempty_page": nonempty[-1]["page"] if nonempty else None,
                "pages_with_full_100": sum(1 for r in rows if r["n"] == 100),
            }
            print(f"  {full:34s} {kind:9s} total={total:>5} "
                  f"last_nonempty_page={out[full][kind]['last_nonempty_page']} "
                  f"pages={[r['n'] for r in rows]}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
