#!/usr/bin/env python3
"""Find which search window reproduces yesterday's reported (206, 180) farm numbers."""
import json, subprocess, os, itertools

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def total(q):
    r = subprocess.run(["gh", "api", f"search/repositories?q={q}&per_page=1"],
                       capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)["total_count"]
    except Exception:
        return None


windows = [
    "created:2026-10-29", "created:2026-10-30", "created:>2026-10-28",
    "created:>2026-10-29", "created:2026-10-29..2026-10-30",
    "created:2026-10-28..2026-10-30", "created:>2026-10-27",
    "created:>2026-10-20",
]
sizes = ["size:<=20", "size:<=20480", "size:<=100", "size:<=200", "size:<=1024"]

print(f"{'window':<30} {'stars>=40':>11} " + " ".join(f"{s:>14}" for s in sizes))
for w in windows:
    base = total(f"{w}+stars:>=40")
    row = []
    for s in sizes:
        row.append(str(total(f"{w}+stars:>=40+{s}")))
    print(f"{w:<30} {str(base):>11} " + " ".join(f"{v:>14}" for v in row))
