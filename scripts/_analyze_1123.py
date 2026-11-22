#!/usr/bin/env python3
"""Analysis for the 2026-11-23 daily report.

Five strands:
  1. A REAL 5-day star time series (11-18 -> 11-23), one sample per day,
     closing the "star 增速未做统计" gap flagged in every recent report.
  2. SKILL.md replication factor vs the 11-18 baseline table.
  3. The version four-tuple (tag / release / diff closure / asset shape).
  4. Planted-repo discriminators (README md5 clustering, payload links,
     thin repos, owner account age).
  5. Distribution surface (harness dirs + install commands).
"""
import json
from collections import defaultdict
from datetime import date

DAYS = ["1118", "1119", "1120", "1121", "1122", "1123"]
DATES = ["2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21",
         "2026-11-22", "2026-11-23"]

SNAPS = {}
for d in DAYS:
    try:
        SNAPS[d] = {p["full_name"]: p for p in json.load(open(f"/tmp/probe_{d}.json"))}
    except FileNotFoundError:
        pass

P = json.load(open("/tmp/probe_1123.json"))
by = {p["full_name"]: p for p in P}

print("=" * 108)
print("1. STAR TIME SERIES — 6 daily snapshots, one per day (11-18 .. 11-23)")
print("=" * 108)
print(f"snapshot sizes: " + "  ".join(f"{DATES[DAYS.index(d)]}={len(SNAPS[d])}" for d in DAYS if d in SNAPS))

series = defaultdict(dict)
for d in DAYS:
    for fn, p in SNAPS.get(d, {}).items():
        if p.get("stars") is not None:
            series[fn][d] = p["stars"]

rows = []
for fn, s in series.items():
    pts = [(d, s[d]) for d in DAYS if d in s]
    if len(pts) < 2:
        continue
    first_d, first_v = pts[0]
    last_d, last_v = pts[-1]
    span_days = DAYS.index(last_d) - DAYS.index(first_d)
    delta = last_v - first_v
    rows.append((fn, first_d, first_v, last_d, last_v, delta, span_days,
                 delta / span_days if span_days else 0, len(pts), len(s)))
rows.sort(key=lambda r: -r[6 + 0] if False else -r[5])

print(f"{'repo':42s} {'from':>10s} {'start':>8s} {'to':>10s} {'end':>9s} {'delta':>8s} {'d/day':>8s} {'npts':>5s}")
for fn, fd, fv, ld, lv, delta, span, per, npts, nposs in rows:
    if abs(delta) < 50:
        continue
    print(f"{fn:42s} {fd:>10s} {fv:8,d} {ld:>10s} {lv:9,d} {delta:8,d} {per:8.1f} {npts:5d}")

print()
print("--- coverage: repos present in ALL 6 snapshots (clean 5-day series) ---")
full = [(fn, s) for fn, s in series.items()
        if all(d in s for d in DAYS) and s[DAYS[-1]] - s[DAYS[0]] > 100]
full.sort(key=lambda r: -(r[1][DAYS[-1]] - r[1][DAYS[0]]))
for fn, s in full:
    vals = [s[d] for d in DAYS]
    deltas = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    print(f"{fn:42s} " + " ".join(f"{v:>9,d}" for v in vals) +
          "  | daily deltas: " + " ".join(f"{x:>+7,d}" for x in deltas))

print()
print("--- daily-delta dispersion across the whole tracked set (is growth steady?) ---")
all_deltas = []
for fn, s in series.items():
    pts = [(d, s[d]) for d in DAYS if d in s]
    for i in range(len(pts) - 1):
        all_deltas.append(pts[i + 1][1] - pts[i][1])
if all_deltas:
    all_deltas.sort()
    n = len(all_deltas)
    print(f"n={n}  min={all_deltas[0]:+,d}  p25={all_deltas[n//4]:+,d}  "
          f"median={all_deltas[n//2]:+,d}  p75={all_deltas[3*n//4]:+,d}  max={all_deltas[-1]:+,d}")
    neg = sum(1 for x in all_deltas if x < 0)
    zero = sum(1 for x in all_deltas if x == 0)
    print(f"negative intervals: {neg} ({neg/n*100:.1f}%)   flat intervals: {zero} ({zero/n*100:.1f}%)")

print()
print("=" * 108)
print("2. SKILL.md REPLICATION FACTOR — 11-18 recorded baseline vs 11-23 live")
print("=" * 108)
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
print(f"{'repo':42s} {'11-18':>12s} {'11-23':>12s} {'repl18':>8s} {'repl23':>8s} {'delta':>8s}  harness")
for name, (f0, i0) in sorted(REC_1118.items(), key=lambda kv: -kv[1][0]):
    p = by.get(name)
    if not p:
        print(f"{name:42s} {'(off trending 11-23)':>12s}")
        continue
    f1, i1 = p["n_skill_files"], p["n_skill_identities"]
    r0 = f0 / i0 if i0 else 0
    r1 = p["skill_replication"]
    print(f"{name:42s} {f0:6d}/{i0:<5d} {f1:6d}/{i1:<5d} {r0:8.2f} {r1:8.2f} {r1-r0:+8.2f}  "
          f"{len(p['harness_dirs'])}")

print()
print("--- skill-class repos on 11-23 trending NOT in the 11-18 table ---")
for p in P:
    if p["n_skill_files"] and p["full_name"] not in REC_1118:
        print(f"  {p['full_name']:42s} {p['n_skill_files']:5d} files / {p['n_skill_identities']:5d} ident "
              f"repl {p['skill_replication']:.2f}  harness={len(p['harness_dirs'])} {p['harness_dirs']}")

print()
print("=" * 108)
print("3. VERSION FOUR-TUPLE: tag / release / asset shape / sbom / downloads")
print("=" * 108)
print(f"{'repo':42s} {'tags':>5s} {'rel':>4s} {'rel/tag':>8s} {'assets':>10s} {'sbom':>5s} {'chk':>5s} "
      f"{'dl_max':>8s} {'dl_tot':>9s} {'prerel':>7s}")
for p in sorted(P, key=lambda x: -x["n_tags"]):
    ra = p["rel_assets"]
    na = [r["n_assets"] for r in ra]
    sbom = any(r["has_sbom"] for r in ra)
    chk = any(r["has_checksum"] for r in ra)
    dmax = max([r["max_downloads"] for r in ra] or [0])
    dtot = sum([r["total_downloads"] for r in ra] or [0])
    pre = sum(1 for r in ra if r["prerelease"])
    rt = f"{p['n_releases']/p['n_tags']:.2f}" if p["n_tags"] else "-"
    ar = f"{min(na)}-{max(na)}" if na else "-"
    print(f"{p['full_name']:42s} {p['n_tags']:5d} {p['n_releases']:4d} {rt:>8s} {ar:>10s} "
          f"{str(sbom):>5s} {str(chk):>5s} {dmax:8d} {dtot:9d} {pre:7d}")

print()
print("=" * 108)
print("4. PLANTED-REPO DISCRIMINATORS")
print("=" * 108)
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
print(f"{'repo':42s} {'blobs':>7s} {'commits':>7s} {'auth':>5s} {'stars':>8s} {'forks':>6s} "
      f"{'f/st':>6s} {'subs':>6s} {'oi':>5s} {'created':>12s} {'owner':>10s}")
for p in sorted(P, key=lambda x: x["n_blobs"]):
    fs = p["forks"] / p["stars"] * 100 if p["stars"] else 0
    print(f"{p['full_name']:42s} {p['n_blobs']:7d} {p['n_commits']:7d} {p['n_authors']:5d} "
          f"{p['stars']:8,d} {p['forks']:6,d} {fs:5.1f}% {p['subs']:6d} {p['open_issues']:5d} "
          f"{str(p['owner_created'])[:10]:>12s} {str(p['owner_login']):>10s}")

print()
print("--- THIN REPOS (low blob count) — star/fork density check ---")
for p in sorted(P, key=lambda x: x["n_blobs"])[:10]:
    dens = p["stars"] / max(p["n_blobs"], 1)
    exts = list(p["exts"].items())[:5]
    print(f"  {p['full_name']:42s} blobs={p['n_blobs']:5d} commits={p['n_commits']:4d} "
          f"stars={p['stars']:8,d} stars/blob={dens:8.0f} exts={exts}")

print()
print("=" * 108)
print("5. DISTRIBUTION SURFACE: harness dirs + install commands")
print("=" * 108)
for p in P:
    if p["n_skill_files"] or p["harness_dirs"] or p["install_cmds"]:
        print(f"{p['full_name']:42s} harness={len(p['harness_dirs'])} {p['harness_dirs']}")
        for c in p["install_cmds"]:
            print(f"      $ {c}")

print()
print("=" * 108)
print("6. SAME-17 INSTALL-COMMAND CONTINUITY (11-17 baseline cohort)")
print("=" * 108)
COHORT = [
    "anthropics/skills", "kajisho5/ffmpeg-skill", "mvanhorn/last30days-skill",
    "obra/superpowers", "addyosmani/agent-skills", "cursor/plugins",
    "backnotprop/plannotator", "affaan-m/ECC", "Tencent/LoopForge",
    "elementalsouls/Claude-BugHunter", "google/elephant-goldfish-model",
    "NVIDIA/SkillEvaluator", "ag-ui-protocol/ag-ui", "boringmarketer/boring-marketing-skills",
    "vercel-labs/agent-browser", "google-labs-code/stitch-skills",
    "tradermonty/claude-trading-skills",
]
for d in DAYS:
    snap = SNAPS.get(d, {})
    both = one = none = 0
    for fn in COHORT:
        p = snap.get(fn)
        if not p:
            continue
        cmds = " || ".join(p.get("install_cmds", []))
        has_npx = "npx skills add" in cmds or "npx skills" in cmds
        has_mkt = "marketplace add" in cmds
        if has_npx and has_mkt:
            both += 1
        elif has_npx or has_mkt:
            one += 1
        else:
            none += 1
    print(f"  {DATES[DAYS.index(d)]:>12s}  cohort_present={sum(1 for f in COHORT if f in snap):2d}/17  "
          f"both={both:2d}  one={one:2d}  none={none:2d}")

print()
print("--- today per-repo install command detail (cohort members on trending) ---")
for fn in COHORT:
    p = by.get(fn)
    if not p:
        continue
    print(f"  {fn:42s} {p['install_cmds']}")
