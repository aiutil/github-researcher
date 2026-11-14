#!/usr/bin/env python3
"""2026-11-01: quantify farm delivery channels per day, reconstruction-aware.

Channels:
  CH-A  git-software.cc  (PowerShell WebClient DownloadString)
  CH-B  activation-gateway.cc (powershell -ExecutionPolicy Bypass + iex(irm ...))
  CH-C  telegra.ph mirror badge (non-PowerShell channel)
  EVAD  payload present but naive substring 'git-software.cc' absent (split vars)
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


NAIVE_A = re.compile(r"git-software\.cc", re.I)
SPLIT_A = re.compile(r"\$Node\s*=\s*'git-software\.'", re.I)
NAIVE_B = re.compile(r"activation-gateway\.cc", re.I)
DL = re.compile(r"DownloadString\s*\(|iex\s*\(\s*irm", re.I)
TELEG = re.compile(r"telegra\.ph", re.I)
RT = re.compile(r"real-time protection", re.I)
BY = re.compile(r"ExecutionPolicy\s+Bypass", re.I)


def classify(rd):
    if not rd:
        return "unreadable", []
    t = []
    a = bool(NAIVE_A.search(rd) or SPLIT_A.search(rd))
    b = bool(NAIVE_B.search(rd))
    dl = bool(DL.search(rd))
    if a: t.append("A")
    if b: t.append("B")
    if TELEG.search(rd): t.append("TELEG")
    if RT.search(rd): t.append("RT")
    if BY.search(rd): t.append("BYPASS")
    if not t:
        return "clean", []
    if (a or b) and dl:
        return "payload", t
    return "other", t


print(f"{'date':<12} {'total>=40':>9} {'size<=20':>8} {'checked':>7} {'payload':>7} "
      f"{'naiveA':>6} {'splitA':>6} {'B-gw':>5} {'evad':>5} {'TELEG':>5} {'clean':>5}")
print("-" * 100)
for date in sys.argv[1:]:
    res = japi(f"search/repositories?q=created:{date}+stars:>=40&per_page=100&sort=stars")
    if not res:
        print(f"{date}: search failed")
        continue
    tot = res["total_count"]
    small = japi(f"search/repositories?q=created:{date}+stars:>=40+size:<=20&per_page=1")
    nsmall = small["total_count"] if small else -1
    items = res["items"]
    c = collections.Counter()
    naiveA = splitA = B = evad = teleg = 0
    checked = 0
    for i in items[:100]:
        rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
        if not rd:
            continue
        checked += 1
        kind, tags = classify(rd)
        c[kind] += 1
        if "A" in tags:
            if SPLIT_A.search(rd) and not NAIVE_A.search(rd):
                splitA += 1
            else:
                naiveA += 1
        if "B" in tags: B += 1
        if "A" in tags and SPLIT_A.search(rd) and not NAIVE_A.search(rd): evad += 1
        if "TELEG" in tags: teleg += 1
    print(f"{date:<12} {tot:>9} {nsmall:>8} {checked:>7} {c['payload']:>7} "
          f"{naiveA:>6} {splitA:>6} {B:>5} {evad:>5} {teleg:>5} {c['clean']:>5}")
