#!/usr/bin/env python3
"""Analyse today's (2026-11-20) probe: shape discriminators, release
discipline, skill replication, and continuity vs the 11-18 / 11-17 archives.

Output is a compact text report to /tmp/analyze_1120.txt
"""
import json
from collections import Counter

P = json.load(open("/tmp/probe_1120.json"))
TR = {t["full_name"]: t for t in json.load(open("/tmp/trend_1120.json"))}

# Prior-day archive values (stars) for continuity, from projects/*.md snapshots
PREV = {
    "elementalsouls/Claude-BugHunter": 9120,     # 11-18
    "backnotprop/plannotator": 13035,            # 11-18
    "GoogleChrome/modern-web-guidance-src": 8414, # 11-18
    "alibaba/open-code-review": 53682,           # 11-18
    "mvanhorn/last30days-skill": 68964,          # 11-18
    "kajisho5/ffmpeg-skill": 6630,               # 11-17
    "obra/superpowers": None,
    "cursor/plugins": None,
    "HKUDS/CLI-Anything": None,
    "jingyaogong/minimind": None,
    "firecrawl/firecrawl": None,
    "nginx/nginx": None,
    "openvinotoolkit/openvino": None,
    "cathrynlavery/diagram-design": None,
    "google-labs-code/stitch-skills": 10069,     # 11-18
    "mjmirza/app-store-compliance": None,
    "Tracer-Cloud/opensre": None,
    "toeverything/AFFiNE": None,
    "XiaoYouChR/Ghost-Downloader-3": None,
    "zhouxiaoka/autoclip": None,
    "ChromeDevTools/chrome-devtools-mcp": None,
    "tradermonty/claude-trading-skills": None,
    "ag-ui-protocol/ag-ui": None,
    "meta/astryx": None,
    "pookjw/HermesEnabler": None,
    "we-promise/sure": None,
    "dream-num/univer": None,
}

out = []
def pr(s=""):
    out.append(s)
    print(s)


pr("=" * 116)
pr(f"{'repo':44s} {'stars':>9s} {'prev':>9s} {'d%':>7s} {'forks':>8s} {'f/s%':>6s} "
   f"{'subs':>5s} {'oi':>5s} {'blobs':>7s} {'tag':>4s} {'rel':>4s} {'sk':>9s} {'repl':>5s} {'harn':>4s}")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    fn = r["full_name"]
    prev = PREV.get(fn)
    d = (r["stars"] - prev) if prev else None
    dp = f"{(d/prev*100):+.1f}%" if prev else "   new"
    fs = (r["forks"] / r["stars"] * 100) if r["stars"] else 0
    sk = f'{r["n_skill_files"]}/{r["n_skill_identities"]}'
    pr(f"{fn:44s} {r['stars']:>9,} {str(prev or '-'):>9s} {dp:>7s} {r['forks']:>8,} "
       f"{fs:>5.1f}% {r['subs']:>5} {r['open_issues']:>5} {r['n_blobs']:>7,} "
       f"{r['n_tags']:>4} {r['n_releases']:>4} {sk:>9s} {r['skill_replication']:>5} "
       f"{len(r['harness_dirs']):>4}")

pr()
pr("### RELEASE DISCIPLINE (tag/release/asset)")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    if r["n_releases"] == 0 and r["n_tags"] == 0:
        continue
    ra = r["rel_assets"]
    tot_a = sum(a["n_assets"] for a in ra)
    tot_dl = sum(a["total_downloads"] for a in ra)
    sbom = any(a["has_sbom"] for a in ra)
    chk = any(a["has_checksum"] for a in ra)
    pr(f"{r['full_name']:44s} tag={r['n_tags']:>4} rel={r['n_releases']:>4} "
       f"sampled_assets={tot_a:>4} dl={tot_dl:>9,} sbom={'Y' if sbom else 'n':1s} "
       f"chk={'Y' if chk else 'n':1s}")
    for a in ra[:2]:
        pr(f"    - {a['tag']} pre={a['prerelease']} n_assets={a['n_assets']} "
           f"max_dl={a['max_downloads']} sbom={a['has_sbom']} names={a['asset_names'][:6]}")

pr()
pr("### TAG WITHOUT RELEASE / RELEASE WITHOUT TAG")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    if r["n_tags"] == r["n_releases"] == 0:
        continue
    if r["n_tags"] != r["n_releases"]:
        pr(f"{r['full_name']:44s} tag={r['n_tags']:>4} rel={r['n_releases']:>4} "
           f"gap={r['n_tags']-r['n_releases']:+}")

pr()
pr("### SKILL REPLICATION")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(x["skill_replication"] or 0)):
    if r["n_skill_files"] == 0:
        continue
    pr(f"{r['full_name']:44s} files={r['n_skill_files']:>5} ident={r['n_skill_identities']:>5} "
       f"repl={r['skill_replication']:>6} harness={len(r['harness_dirs']):>2} "
       f"{r['harness_dirs'][:9]}")

pr()
pr("### HARNESS / INSTALL SURFACE")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(len(x["harness_dirs"]) or 0)):
    if not r["harness_dirs"] and not r["install_cmds"]:
        continue
    pr(f"{r['full_name']:44s} harness={len(r['harness_dirs']):>2} {r['harness_dirs']}")
    pr(f"    installs: {r['install_cmds']}")

pr()
pr("### ZERO-SHAPE / ANOMALY WATCH")
pr("=" * 116)
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
    if r["is_fork"]:
        flags.append("IS_FORK")
    if flags:
        pr(f"{r['full_name']:44s} {' | '.join(flags)}")

pr()
pr("### README MD5 CLUSTERS")
pr("=" * 116)
c = Counter(r["readme_md5"] for r in P)
for h, n in c.most_common():
    if n > 1:
        same = [r["full_name"] for r in P if r["readme_md5"] == h]
        pr(f"  md5={h} x{n}: {same}")

pr()
pr("### TRENDING PAGE vs API STARS")
pr("=" * 116)
for r in P:
    t = TR.get(r["full_name"])
    if t:
        pr(f"{r['full_name']:44s} api={r['stars']:>8,} page_stars={t['stars']:>7} "
           f"period_delta={t['period_stars']} {t['period']}")

pr()
pr("### TOPIC / LICENSE / CREATION SUMMARY")
pr("=" * 116)
for r in sorted(P, key=lambda x: -(x["stars"] or 0)):
    pr(f"{r['full_name']:44s} lic={str(r['license']):>12s} created={r['created_at']} "
       f"pushed={r['pushed_at']} lang={r['language']} owner={r['owner_login']}"
       f"(born {r['owner_created']}, {r['owner_public_repos']} repos, {r['owner_followers']} fol)")

pr()
pr("### COMBO INSTALL COUNT (npx skills add + marketplace add)")
pr("=" * 116)
both = one = none = 0
for r in P:
    cmds = " ".join(r["install_cmds"])
    a = "skills add" in cmds
    b = "marketplace" in cmds
    if a and b:
        both += 1
        pr(f"  BOTH  {r['full_name']}")
    elif a or b:
        one += 1
        pr(f"  ONE   {r['full_name']}  {r['install_cmds']}")
    else:
        none += 1
pr(f"  both={both} one={one} none={none} total={len(P)}")

open("/tmp/analyze_1120.txt", "w").write("\n".join(out))
