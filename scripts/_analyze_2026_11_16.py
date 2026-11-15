#!/usr/bin/env python3
"""Analyse the 2026-11-15 candidate set: cluster by README md5, extract
payload links, rank by engineering-effort proxies."""
import json
import re
import sys
from collections import Counter, defaultdict

SRC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cand_1115.json"
C = json.load(open(SRC))
print(f"candidates: {len(C)}")

# ---- cluster by README md5 ----
by_md5 = defaultdict(list)
for r in C:
    by_md5[r["readme_md5"]].append(r)

print("\n=== README md5 clusters (>=2) ===")
clusters = [(k, v) for k, v in by_md5.items() if len(v) >= 2]
clusters.sort(key=lambda kv: -len(kv[1]))
for md5, group in clusters:
    stars = sorted(g["stars"] for g in group)
    owners = sorted({g["owner_login"] for g in group})
    roots = Counter()
    for g in group:
        n = g["full_name"].split("/")[1].lower()
        for tok in ("ai--manus", "iptv", "github-copilot", "desktop", "player", "pro"):
            if tok in n:
                roots[tok] += 1
                break
        else:
            roots["<other>:" + n[:24]] += 1
    print(f"\nmd5={md5[:16]}… n={len(group)} readme_len={group[0]['readme_len']} "
          f"stars={stars[0]}–{stars[-1]} distinct_stars={len(set(stars))}")
    print(f"  owners: {len(owners)} distinct; roots: {dict(roots.most_common(6))}")
    print(f"  created range: {min(g['created_at'] for g in group)} .. {max(g['created_at'] for g in group)}")
    print(f"  example: {group[0]['full_name']}")

print("\n=== singletons ===")
sing = [v[0] for k, v in by_md5.items() if len(v) == 1]
print(f"count: {len(sing)}")

# ---- payload links ----
URL = re.compile(r"https?://[^\s)\"'<>\]`]+")
print("\n=== payload-ish external links (dropbox / mediafire / drive / release) ===")
for r in C:
    m = URL.findall(r.get("readme_head", ""))
    sus = [u for u in m if any(k in u.lower() for k in
           ("dropbox", "mediafire", "mega.nz", "drive.google", "wetransfer",
            "pixeldrain", "linkbox", "discord.gg", "quark", "pan.baidu"))]
    if sus:
        print(f"  {r['full_name']} *{r['stars']} -> {sus[:2]}")

# ---- engineering effort ranking ----
print("\n=== effort ranking (blobs, ext mix, commits, subs, oi) ===")
CODE = {".py", ".ts", ".tsx", ".js", ".jsx", ".rs", ".go", ".c", ".cpp", ".h",
        ".hpp", ".java", ".kt", ".kts", ".swift", ".rb", ".php", ".cs", ".m",
        ".mm", ".sh", ".bash", ".sql", ".scala", ".ex", ".exs", ".lua", ".vue",
        ".svelte", ".zig", ".dart", ".clj", ".hs", ".ml", ".ipynb"}
for r in sorted(C, key=lambda x: (-x["n_blobs"], -x["n_commits"])):
    code_n = sum(v for k, v in r["exts"].items() if k in CODE)
    r["code_n"] = code_n
for r in sorted(C, key=lambda x: (-x["code_n"], -x["n_commits"]))[:28]:
    print(f"  {r['full_name']:52s} *{r['stars']:5d} ⑂{r['forks']:4d} subs{r['subs']:3d} "
          f"oi{r['oi']:3d} blobs={r['n_blobs']:5d} code={r['code_n']:5d} "
          f"cmt={r['n_commits']:4d} {r['size_kb']:7d}KB {r['language']} {r['license']}")

# ---- subscriber outliers ----
print("\n=== subscriber outliers (subs high) ===")
for r in sorted(C, key=lambda x: -x["subs"])[:12]:
    print(f"  {r['full_name']:52s} subs={r['subs']:4d} *{r['stars']:5d} "
          f"blobs={r['n_blobs']:4d} code={r['code_n']:4d} oi={r['oi']:3d} {r['language']}")

# ---- fork/star outliers ----
print("\n=== fork/star outliers ===")
for r in sorted(C, key=lambda x: -(x["forks"] / max(x["stars"], 1)))[:12]:
    print(f"  {r['full_name']:52s} ⑂{r['forks']:4d}/{r['stars']:5d} = "
          f"{r['forks']/max(r['stars'],1)*100:6.1f}% blobs={r['n_blobs']:4d} "
          f"code={r['code_n']:4d} subs={r['subs']:3d}")

# ---- open issues (real usage signal) ----
print("\n=== open issues >= 3 ===")
for r in sorted(C, key=lambda x: -x["oi"]):
    if r["oi"] >= 3:
        print(f"  {r['full_name']:52s} oi={r['oi']:3d} *{r['stars']:5d} "
              f"blobs={r['n_blobs']:4d} code={r['code_n']:4d} subs={r['subs']:3d} "
              f"cmt={r['n_commits']:4d} {r['language']}")

# ---- owner account clustering ----
print("\n=== owner account creation times (farm signal) ===")
own = defaultdict(list)
for r in C:
    own[r["owner_login"]].append(r)
rows = []
for o, g in sorted(own.items()):
    # owner_created is absent from older collector snapshots; group by it
    # only when present so a missing field cannot abort the whole report.
    created = next((x.get("owner_created") for x in g if x.get("owner_created")), None)
    rows.append((created or "", o, len(g), sum(x["stars"] for x in g)))
rows.sort()
for t, o, n, s in rows[:40]:
    print(f"  {t or '(unknown)':22s}  {o:40s} repos={n:2d} stars={s}")
print(f"  ... total distinct owners: {len(own)}")
print(f"  ... owners with known creation time: "
      f"{sum(1 for r in rows if r[0])}/{len(rows)}")
