#!/usr/bin/env python3
"""DECISIVE TEST: did the 10-29 farm mutate its existing repos in place after 10-30?

The 10-30 daily reported: created:2026-10-29 + stars>=40 -> 206 repos, 180 with size<=20KB (87.4%),
and 88/100 of the top-by-stars sample carried `git-software.cc`.

Today the same queries return: 268 total, 47 size<=20KB, and only 1/100 naive git-software.cc
but 46/100 activation-gateway.cc.

Two hypotheses:
  M1  The farm padded repo size AND swapped the payload channel in place (pushed_at > 10-29).
  M2  The 10-30 measurement was simply wrong.

M1 predicts: repos with pushed_at after 2026-10-29T24:00Z correlate with channel B and larger size.
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
TELEG = re.compile(r"telegra\.ph", re.I)

res = japi("search/repositories?q=created:2026-10-29+stars:>=40&per_page=100&sort=stars")
items = res["items"]
print(f"total_count={res['total_count']} fetched={len(items)}\n")

table = []
for i in items:
    r = japi(f"repos/{i['full_name']}")
    if not r:
        continue
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    chan = []
    if NAIVE_A.search(rd) or SPLIT_A.search(rd): chan.append("A")
    if NAIVE_B.search(rd): chan.append("B")
    if TELEG.search(rd): chan.append("TELEG")
    table.append({
        "full": i["full_name"], "size": r["size"], "stars": r["stargazers_count"],
        "created": r["created_at"], "pushed": r["pushed_at"], "chan": ",".join(chan) or "-",
        "readme_len": len(rd), "ncommits": None,
    })

# group by whether pushed_at is after the 10-30 report snapshot
CUT = "2026-10-30T00:00:00Z"
mutated = [t for t in table if t["pushed"] > CUT]
static = [t for t in table if t["pushed"] <= CUT]
print(f"{'group':<10} {'n':>4} {'chA':>5} {'chB':>5} {'TELEG':>6} {'no-chan':>8} "
      f"{'size<=20':>8} {'size>20':>8} {'medsize':>8}")
for name, g in (("MUTATED", mutated), ("STATIC", static)):
    if not g:
        continue
    ca = sum(1 for t in g if "A" in t["chan"])
    cb = sum(1 for t in g if "B" in t["chan"])
    ct = sum(1 for t in g if "TELEG" in t["chan"])
    nc = sum(1 for t in g if t["chan"] == "-")
    small = sum(1 for t in g if t["size"] <= 20)
    big = sum(1 for t in g if t["size"] > 20)
    med = sorted(t["size"] for t in g)[len(g) // 2]
    print(f"{name:<10} {len(g):>4} {ca:>5} {cb:>5} {ct:>6} {nc:>8} {small:>8} {big:>8} {med:>8}")

print("\n--- MUTATED repos: size + pushed_at + channel (up to 30) ---")
for t in sorted(mutated, key=lambda x: x["pushed"])[:30]:
    print(f"  {t['full']:<52} size={t['size']:>7}KB stars={t['stars']:>5} "
          f"created={t['created'][:19]} pushed={t['pushed'][:19]} chan={t['chan']} rd={t['readme_len']}")

print("\n--- STATIC repos: size + channel (up to 25) ---")
for t in static[:25]:
    print(f"  {t['full']:<52} size={t['size']:>7}KB stars={t['stars']:>5} "
          f"pushed={t['pushed'][:19]} chan={t['chan']} rd={t['readme_len']}")
