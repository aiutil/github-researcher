#!/usr/bin/env python3
"""Decisive test: did the 10-29 cohort once carry the payload (README history)? And what does it carry now?"""
import json, subprocess, os, re

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


SAMPLES = [
    "Yugiri-AO/battery-peek",
    "war4me12-star/dev-library-di-singleton",
    "dannairfawan/fast-activator",
    "mhilali260-glitch/responsive-web-hub",
    "valeriofix15-arch/kms-activation-tool",
]
for full in SAMPLES:
    print("=" * 90)
    print(full)
    print("=" * 90)
    hist = japi(f"repos/{full}/commits?path=README.md&per_page=100") or []
    print(f"  README.md history: {len(hist)} commits")
    for c in hist[:12]:
        date = c["commit"]["author"]["date"]
        sha = c["sha"][:8]
        raw = api(f"repos/{full}/contents/README.md?ref={sha}", raw=True) or ""
        flags = []
        if "git-software.cc" in raw:
            flags.append("PAYLOAD")
        if "Invoke-Expression" in raw:
            flags.append("PS")
        if "telegra" in raw.lower():
            flags.append("TELEGRAPH")
        if "real-time protection" in raw or "实时保护" in raw:
            flags.append("AV-BYPASS")
        print(f"    {date} {sha} len={len(raw):>6} {' '.join(flags) or '-'}")
    print()
