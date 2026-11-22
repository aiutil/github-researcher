#!/usr/bin/env python3
"""Analysis over /tmp/probe_1122.json (+ 1121/1120 for same-caliber continuity).

Covers:
  1. SKILL.md replication factor (identity = parent-dir name + blob-sha set)
     compared 11-18 snapshot (embedded constants from the 11-18 daily report)
     against today's live measurement.
  2. The four-tuple version criteria: tag / release / diff-closure / asset shape.
  3. Planted-repo discriminators: README md5 clustering, payload URLs, blob counts.
  4. Harness / install-command surface.
"""
import json
from collections import defaultdict

P = json.load(open("/tmp/probe_1122.json"))
by = {p["full_name"]: p for p in P}

print("=" * 100)
print("1. SKILL.md IDENTITY / REPLICATION — 11-18 recorded vs 11-22 live re-measure")
print("=" * 100)
# 11-18 daily report table (SKILL.md files / distinct identities / replication)
REC_1118 = {
    "affaan-m/ECC": (1087, 330),
    "Tencent/LoopForge": (21, 9),
    "backnotprop/plannotator": (23, 11),
    "cursor/plugins": (173, 113),
    "tradermonty/claude-trading-skills": (94, 74),
    "alibaba/open-code-review": (4, 4),
    "elementalsouls/Claude-BugHunter": (83, 83),
    "obra/superpowers": (15, 15),
    "addyosmani/agent-skills": (25, 25),
    "anthropics/skills": (20, 20),
    "google-labs-code/stitch-skills": (16, 16),
    "mvanhorn/last30days-skill": (1, 1),
}
print(f"{'repo':42s} {'11-18 files/ident':>20s} {'11-22 files/ident':>20s} {'repl 11-18':>11s} {'repl 11-22':>11s}  delta")
rows = []
for name, (f0, i0) in REC_1118.items():
    p = by.get(name)
    if not p:
        print(f"{name:42s} {'(not on 11-22 trending)':>20s}")
        continue
    f1, i1 = p["n_skill_files"], p["n_skill_identities"]
    r0 = f0 / i0 if i0 else 0
    r1 = f1 / i1 if i1 else 0
    rows.append((name, f0, i0, r0, f1, i1, r1))
for name, f0, i0, r0, f1, i1, r1 in sorted(rows, key=lambda r: r[3] - r[6], reverse=True):
    print(f"{name:42s} {f0:10d}/{i0:<9d} {f1:10d}/{i1:<9d} {r0:11.2f} {r1:11.2f}  {r1 - r0:+.2f}")

print()
print("skill-class repos on 11-22 trending NOT in the 11-18 table:")
for p in P:
    if p["n_skill_files"] and p["full_name"] not in REC_1118:
        print(f"  {p['full_name']:42s} {p['n_skill_files']:5d} files / {p['n_skill_identities']:5d} ident "
              f"repl {p['skill_replication']:.2f}  harness={p['harness_dirs']}")

print()
print("=" * 100)
print("2. VERSION FOUR-TUPLE: tag / release / asset shape")
print("=" * 100)
print(f"{'repo':42s} {'tags':>5s} {'rel':>4s} {'rel/tag':>8s} {'assets(last6)':>14s} {'sbom':>5s} {'chk':>4s} {'dl_max':>8s} {'dl_tot':>8s}")
for p in sorted(P, key=lambda x: -x["n_tags"]):
    ra = p["rel_assets"]
    n_assets = [r["n_assets"] for r in ra]
    sbom = any(r["has_sbom"] for r in ra)
    chk = any(r["has_checksum"] for r in ra)
    dmax = max([r["max_downloads"] for r in ra] or [0])
    dtot = sum([r["total_downloads"] for r in ra] or [0])
    rt = f"{p['n_releases']/p['n_tags']:.2f}" if p["n_tags"] else "-"
    print(f"{p['full_name']:42s} {p['n_tags']:5d} {p['n_releases']:4d} {rt:>8s} "
          f"{(str(min(n_assets)) + '-' + str(max(n_assets))) if n_assets else '-':>14s} "
          f"{str(sbom):>5s} {str(chk):>4s} {dmax:8d} {dtot:8d}")

print()
print("=" * 100)
print("3. PLANTED-REPO DISCRIMINATORS")
print("=" * 100)
md5s = defaultdict(list)
for p in P:
    md5s[p["readme_md5"]].append(p["full_name"])
dupes = {k: v for k, v in md5s.items() if len(v) > 1}
print(f"README md5 clusters with >1 repo: {len(dupes)}")
for k, v in dupes.items():
    print("   ", k[:12], v)
pay = [(p["full_name"], p["payload_urls"]) for p in P if p["payload_urls"]]
print(f"payload-link repos: {len(pay)}")
for n, u in pay:
    print(f"    {n}: {u}")
print()
print(f"{'repo':42s} {'blobs':>7s} {'exts':>4s} {'commits':>7s} {'auth':>4s} {'owner_created':>12s} {'foll':>5s} {'pub':>4s} {'subs':>5s} {'oi':>5s}")
for p in sorted(P, key=lambda x: x["n_blobs"]):
    print(f"{p['full_name']:42s} {p['n_blobs']:7d} {len(p['exts']):4d} {p['n_commits']:7d} {p['n_authors']:4d} "
          f"{str(p['owner_created'])[:10]:>12s} {str(p['owner_followers']):>5s} {str(p['owner_public_repos']):>4s} "
          f"{str(p['subs']):>5s} {str(p['open_issues']):>5s}")

print()
print("=" * 100)
print("4. DISTRIBUTION SURFACE: harness dirs + install commands")
print("=" * 100)
for p in P:
    if p["n_skill_files"] or p["harness_dirs"]:
        print(f"{p['full_name']:42s} harness={p['harness_dirs']}")
        for c in p["install_cmds"]:
            print(f"      $ {c}")

print()
print("=" * 100)
print("5. TOP-LEVEL EXTENSION MIX (payload farm check)")
print("=" * 100)
for p in sorted(P, key=lambda x: x["n_blobs"]):
    print(f"{p['full_name']:42s} {p['exts']}")
