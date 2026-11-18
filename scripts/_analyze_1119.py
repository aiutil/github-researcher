#!/usr/bin/env python3
"""Analyse today's probe: shape discriminators, release discipline, skill
replication, and continuity vs the 11-18 snapshot where available."""
import json
from collections import Counter

P = json.load(open("/tmp/probe_1119.json"))
TR = {t["full_name"]: t for t in json.load(open("/tmp/trend_1119.json"))}

# 11-18 archive values for continuity (from projects/*.md stars_delta of that day)
PREV = {
    "GoogleChrome/modern-web-guidance-src": 8414,
    "affaan-m/ECC": 305425,
    "backnotprop/plannotator": 13035,
    "alibaba/open-code-review": 53682,
    "google-research/paper-orchestra": 2884,
    "getarcaneapp/arcane": 9275,
    "Tencent/LoopForge": 3071,
    "elementalsouls/Claude-BugHunter": 9120,
    "mvanhorn/last30days-skill": 68964,
}

print("=" * 110)
print(f"{'repo':44s} {'stars':>9s} {'d11-18':>9s} {'d%':>7s} {'forks':>7s} {'f/s%':>6s} "
      f"{'subs':>5s} {'oi':>5s} {'blobs':>6s} {'tag':>4s} {'rel':>4s} {'skill':>10s} {'repl':>5s}")
print("=" * 110)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    fn = r["full_name"]
    prev = PREV.get(fn)
    d = (r["stars"] - prev) if prev else None
    dp = f"{(d/prev*100):+.1f}" if prev else "  new"
    fs = (r["forks"] / r["stars"] * 100) if r["stars"] else 0
    sk = f'{r["n_skill_files"]}/{r["n_skill_identities"]}'
    print(f"{fn:44s} {r['stars']:>9,} {str(prev or '-'):>9s} {dp:>7s} {r['forks']:>7,} "
          f"{fs:>5.1f}% {r['subs']:>5} {r['open_issues']:>5} {r['n_blobs']:>6,} "
          f"{r['n_tags']:>4} {r['n_releases']:>4} {sk:>10s} {r['skill_replication']:>5}")

print()
print("### RELEASE DISCIPLINE (tag/release/assets)")
print("=" * 110)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    if r["n_releases"] == 0 and r["n_tags"] == 0:
        continue
    ra = r["rel_assets"]
    tot_a = sum(a["n_assets"] for a in ra)
    tot_dl = sum(a["total_downloads"] for a in ra)
    sbom = any(a["has_sbom"] for a in ra)
    chk = any(a["has_checksum"] for a in ra)
    print(f"{r['full_name']:44s} tag={r['n_tags']:>4} rel={r['n_releases']:>4} "
          f"sampled_assets={tot_a:>4} dl={tot_dl:>8,} sbom={'Y' if sbom else 'n':1s} "
          f"chk={'Y' if chk else 'n':1s}")
    for a in ra[:2]:
        print(f"    - {a['tag']} prerelease={a['prerelease']} n_assets={a['n_assets']} "
              f"max_dl={a['max_downloads']} sbom={a['has_sbom']} names={a['asset_names'][:5]}")

print()
print("### SKILL REPLICATION (replication > 1.0 means duplicated SKILL.md)")
print("=" * 110)
for r in sorted(P, key=lambda x: -(x["skill_replication"] or 0)):
    if r["n_skill_files"] == 0:
        continue
    print(f"{r['full_name']:44s} files={r['n_skill_files']:>5} ident={r['n_skill_identities']:>5} "
          f"repl={r['skill_replication']:>6} harness={len(r['harness_dirs']):>2} "
          f"{r['harness_dirs'][:8]}")

print()
print("### HARNESS / INSTALL SURFACE")
print("=" * 110)
for r in sorted(P, key=lambda x: -(len(x["harness_dirs"]) or 0)):
    if not r["harness_dirs"] and not r["install_cmds"]:
        continue
    print(f"{r['full_name']:44s} harness={len(r['harness_dirs']):>2} {r['harness_dirs']}")
    print(f"    installs: {r['install_cmds']}")

print()
print("### ZERO-SHAPE / ANOMALY WATCH")
print("=" * 110)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    flags = []
    if r["n_blobs"] <= 5 and r["stars"] and r["stars"] > 1000:
        flags.append(f'BLOB_FARM({r["n_blobs"]})')
    if r["open_issues"] == 0 and r["stars"] and r["stars"] > 1000:
        flags.append("ZERO_ISSUES")
    if r["subs"] == 0 and r["stars"] and r["stars"] > 1000:
        flags.append("ZERO_SUBS")
    if r["forks"] == 0 and r["stars"] and r["stars"] > 1000:
        flags.append("ZERO_FORKS")
    if r["n_commits"] <= 3 and r["stars"] and r["stars"] > 1000:
        flags.append(f'LOW_COMMITS({r["n_commits"]})')
    if r["license"] in (None, "NOASSERTION"):
        flags.append(f'LICENSE={r["license"]}')
    if r["payload_urls"]:
        flags.append(f'PAYLOAD={r["payload_urls"]}')
    if r["owner_created"] and r["owner_created"] >= "2026-10-01":
        flags.append(f'NEW_OWNER({r["owner_created"]})')
    if flags:
        print(f"{r['full_name']:44s} {' | '.join(flags)}")

print()
print("### README MD5 CLUSTERS (templated deployment fingerprint)")
print("=" * 110)
c = Counter(r["readme_md5"] for r in P)
for h, n in c.most_common():
    if n > 1:
        same = [r["full_name"] for r in P if r["readme_md5"] == h]
        print(f"  md5={h} x{n}: {same}")

print()
print("### TRENDING PAGE vs API STARS")
print("=" * 110)
for r in P:
    t = TR.get(r["full_name"])
    if t:
        print(f"{r['full_name']:44s} api={r['stars']:>8,} page_stars={t['stars']:>7} "
              f"period_delta={t['period_stars']} {t['period']}")
