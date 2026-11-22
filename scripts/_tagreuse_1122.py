#!/usr/bin/env python3
"""11-22 — final: how many tags point at commits that are NOT the expected
'content refresh' commit?  This tests the 11-18 claim that "10/10 sampled tags
changed the RAG index artefacts and their parents touched source".
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


full = "GoogleChrome/modern-web-guidance-src"
m = api(f"repos/{full}") or {}
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
tags = tags if isinstance(tags, list) else []
print(f"{full}: {len(tags)} tags")

shas = [t.get("commit", {}).get("sha") for t in tags]
cnt = Counter(shas)
print(f"distinct commit shas: {len(cnt)}")
print("duplicate-sha groups:")
for sha, c in cnt.most_common():
    if c > 1:
        names = [t.get("name") for t in tags if t.get("commit", {}).get("sha") == sha]
        print(f"   {sha[:12]} x{c} -> {names}")

# For a SAMPLE of tags, what does the commit actually change?
print("\nsampled tag commits (12 spread across the list):")
idxs = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 84, 96]
rag_paths = ("guide-chunk-cache.i8", "guide-chunk-cache.json", "guide-chunk-cache.scale.f32")
n_rag = n_src = n_other = 0
for i in idxs:
    if i >= len(tags):
        continue
    t = tags[i]
    sha = t.get("commit", {}).get("sha")
    cm = api(f"repos/{full}/commits/{sha}") or {}
    files = cm.get("files") or []
    names = [f.get("filename") for f in files]
    is_rag = any(any(rp in (n or "") for rp in rag_paths) for n in names)
    is_src = any((n or "").startswith(("src/", "guides/")) for n in names)
    date = (cm.get("commit", {}).get("author", {}) or {}).get("date")
    msg = (cm.get("commit", {}).get("message") or "").split("\n")[0][:70]
    kind = "RAG" if is_rag else ("SRC" if is_src else "OTHER")
    if is_rag:
        n_rag += 1
    elif is_src:
        n_src += 1
    else:
        n_other += 1
    print(f"   {t.get('name'):11s} {str(date)[:10]} files={len(files):3d} [{kind:5s}] {msg}")
    if not is_rag:
        print(f"        paths: {names[:5]}")

print(f"\nsample breakdown: RAG={n_rag} SRC-only={n_src} OTHER={n_other} (of {len(idxs)} sampled)")

# commit date distribution across ALL 100 tags (cheap: /commits?sha=)
print("\nall-100 tag commit dates (via commits endpoint per tag sha):")
dates = []
for t in tags:
    sha = t.get("commit", {}).get("sha")
    cm = api(f"repos/{full}/commits/{sha}") or {}
    d = (cm.get("commit", {}).get("author", {}) or {}).get("date")
    dates.append((t.get("name"), str(d)[:10], (cm.get("commit", {}).get("message") or "").split("\n")[0][:60]))
ym = Counter(d[:7] for _, d, _ in dates if d)
print("   commit month distribution:", dict(sorted(ym.items())))
oldest = sorted(dates, key=lambda x: x[1])[:5]
print("   5 oldest tag commits:")
for n, d, msg in oldest:
    print(f"      {n:11s} {d}  {msg}")

print()
print("=" * 100)
print("opensre — same check across its 100 tags")
print("=" * 100)
full = "Tracer-Cloud/opensre"
m = api(f"repos/{full}") or {}
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
tags = tags if isinstance(tags, list) else []
cnt = Counter(t.get("commit", {}).get("sha") for t in tags)
print(f"   {len(tags)} tags, {len(cnt)} distinct shas")
for sha, c in cnt.most_common():
    if c > 1:
        names = [t.get("name") for t in tags if t.get("commit", {}).get("sha") == sha]
        print(f"   {sha[:12]} x{c} -> {names}")
