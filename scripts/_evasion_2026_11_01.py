#!/usr/bin/env python3
"""2026-11-01: verify the farm's detection-evasion upgrade.

Hypotheses:
 H1: payload URL is now string-split so naive substring matching fails.
 H2: repos are padded (large .gitignore) to escape the size<=20KB filter.
 H3: subscriber counts are inflated / anomalous.
"""
import json, subprocess, os, re, collections, sys

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


# --- payload detection: naive vs reconstruction-aware ---
NAIVE = re.compile(r"git-software\.cc", re.I)
RECON = re.compile(r"git-software\W{0,4}'\s*;\s*\$Zone='cc'", re.I)
SPLITV = re.compile(r"\$Node\s*=\s*'git-software\.'", re.I)
DLSTR = re.compile(r"DownloadString\s*\(", re.I)
PSBLOCK = re.compile(r"scriptblock\]\s*:\s*:\s*Create", re.I)
TELEG = re.compile(r"telegra\.ph", re.I)
BYPASS = re.compile(r"ExecutionPolicy\s+Bypass", re.I)
REALTIME = re.compile(r"real-time protection", re.I)


def classify(rd):
    if not rd:
        return None
    tags = []
    if NAIVE.search(rd): tags.append("naive_domain")
    if SPLITV.search(rd): tags.append("split_var")
    if DLSTR.search(rd): tags.append("downloadstring")
    if PSBLOCK.search(rd): tags.append("scriptblock_create")
    if BYPASS.search(rd): tags.append("exec_bypass")
    if REALTIME.search(rd): tags.append("realtime_pause")
    if TELEG.search(rd): tags.append("telegra")
    if not tags:
        return ("clean", [])
    payload = ("split_var" in tags) or ("naive_domain" in tags and ("downloadstring" in tags or "scriptblock_create" in tags))
    return ("payload" if payload else "other", tags)


for date in sys.argv[1:]:
    res = japi(f"search/repositories?q=created:{date}+stars:>=40&per_page=100&sort=stars")
    items = res["items"]
    print(f"\n{'='*100}\n### created:{date}  total_count={res['total_count']}\n{'='*100}")
    buckets = collections.Counter()
    tagcount = collections.Counter()
    sizes = []
    gi = []
    checked = 0
    for i in items[:100]:
        rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
        if not rd:
            continue
        checked += 1
        kind, tags = classify(rd)
        buckets[kind] += 1
        for t in tags:
            tagcount[t] += 1
        sizes.append(i["size"])
        if i["size"] <= 30:
            gi.append(i["full_name"])
    print(f"  checked={checked}  buckets={dict(buckets)}")
    print(f"  tag counts: {dict(tagcount)}")
    print(f"  size<=30KB count in sample: {len(gi)}  (the 10-29 filter was size<=20KB)")
    if sizes:
        print(f"  size min={min(sizes)} med={sorted(sizes)[len(sizes)//2]} max={max(sizes)}")
    # .gitignore padding check on a handful
    print("  --- .gitignore / file-size anatomy for first 8 payload hits ---")
    shown = 0
    for i in items[:100]:
        if shown >= 8:
            break
        rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
        kind, tags = classify(rd)
        if kind != "payload":
            continue
        tree = japi(f"repos/{i['full_name']}/git/trees/HEAD?recursive=1") or {}
        blobs = sorted([(e.get("size", 0), e["path"]) for e in tree.get("tree", []) if e["type"] == "blob"],
                       key=lambda x: -x[0])
        shown += 1
        print(f"   [{i['full_name']}] stars={i['stargazers_count']} size={i['size']}KB tags={tags}")
        for s, p in blobs[:5]:
            print(f"        {s:>7}  {p}")
