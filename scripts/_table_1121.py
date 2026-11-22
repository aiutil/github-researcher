#!/usr/bin/env python3
"""Emit the consolidated 2026-11-21 table used by the daily report.

One place that joins every measurement taken today, so the numbers in the
report can be regenerated rather than transcribed by hand.

Output: /tmp/table_1121.md  (markdown tables) + /tmp/table_1121.json
"""
import json

probe = {r["full_name"]: r for r in json.load(open("/tmp/probe_1121.json"))}
trend = {t["full_name"]: t for t in json.load(open("/tmp/trend_1121.json"))}
counts = {r["repo"]: r for r in json.load(open("/tmp/counts_1121.json"))}
ip = {r["repo"]: r for r in json.load(open("/tmp/issuepr_1121.json"))}
gates = {r["repo"]: r for r in json.load(open("/tmp/gatetax_1121.json"))}
assets = {r["repo"]: r for r in json.load(open("/tmp/assets_1121.json"))}
closure = {r["repo"]: r for r in json.load(open("/tmp/closure_1121.json"))}

ORDER = [
    "obra/superpowers", "firecrawl/firecrawl", "toeverything/AFFiNE",
    "mvanhorn/last30days-skill", "cathrynlavery/diagram-design",
    "jingyaogong/minimind", "HKUDS/CLI-Anything",
    "ChromeDevTools/chrome-devtools-mcp", "alibaba/open-code-review",
    "nginx/nginx", "meta/astryx", "dream-num/univer", "ag-ui-protocol/ag-ui",
    "cursor/plugins", "we-promise/sure", "elementalsouls/Claude-BugHunter",
    "backnotprop/plannotator", "XiaoYouChR/Ghost-Downloader-3",
    "Tracer-Cloud/opensre", "zhouxiaoka/autoclip",
    "openvinotoolkit/openvino", "google-labs-code/stitch-skills",
    "GoogleChrome/modern-web-guidance-src", "kajisho5/ffmpeg-skill",
    "tradermonty/claude-trading-skills", "mjmirza/app-store-compliance",
    "pookjw/HermesEnabler",
]

rows = []
for name in ORDER:
    p = probe[name]
    t = trend[name]
    c = counts.get(name, {})
    i = ip.get(name, {})
    a = assets.get(name, {})
    cl = closure.get(name, {})
    g = gates.get(name, {})
    cg = g.get("gates", [])
    rows.append({
        "repo": name,
        "stars": p["stars"],
        "forks": p["forks"],
        "fork_star_pct": round(100.0 * (p["forks"] or 0) / max(p["stars"] or 1, 1), 1),
        "subs": p["subs"],
        "raw_oi": p["open_issues"],
        "issues": i.get("n_issues"),
        "prs": i.get("n_prs"),
        "issue_share": i.get("issue_share"),
        "blobs": p["n_blobs"],
        "tags": c.get("tags", {}).get("total"),
        "releases": c.get("releases", {}).get("total"),
        "tags_minus_releases": c.get("tags_minus_releases"),
        "tag_pages": c.get("tags", {}).get("per_page_counts"),
        "rel_pages": c.get("releases", {}).get("per_page_counts"),
        "skill_files": p["n_skill_files"],
        "skill_identities": p["n_skill_identities"],
        "skill_replication": p["skill_replication"],
        "harness_dirs": len(p["harness_dirs"]),
        "n_workflows": len(p["workflows"]),
        "install_cmds": p["install_cmds"],
        "both_install": bool(
            any("npx skills add" in x for x in p["install_cmds"])
            and any("marketplace add" in x for x in p["install_cmds"])
        ),
        "language": p["language"],
        "license": p["license"],
        "created_at": p["created_at"],
        "pushed_at": p["pushed_at"],
        "owner": p["owner_login"],
        "owner_created": p["owner_created"],
        "owner_followers": p["owner_followers"],
        "owner_public_repos": p["owner_public_repos"],
        "topics": p["topics"],
        "description": p["description"],
        "period": t["period"],
        "period_stars": t["period_stars"],
        "assets_total": a.get("n_assets_total"),
        "assets_dl_median": a.get("dl_median"),
        "assets_dl_max": a.get("dl_max"),
        "assets_bytes": a.get("total_bytes"),
        "has_sbom": a.get("has_sbom"),
        "has_checksum": a.get("has_checksum"),
        "closure_own": cl.get("own_touches_source"),
        "closure_parent": cl.get("parent_touches_source"),
        "closure_either": cl.get("either_touches_source"),
        "closure_n": cl.get("n_sampled"),
        "gates": [{"workflow": x["workflow"], "kind": x["kind"],
                   "adv": x["declared_advisory"], "blk": x["declared_blocking"],
                   "can": x["declared_canary"]} for x in cg],
        "n_gates": len(cg),
    })

json.dump(rows, open("/tmp/table_1121.json", "w"), ensure_ascii=False, indent=1)

out = []
out.append("| 项目 | ⭐ | forks | f/s% | subs | oi(raw) | issues | PRs | blobs | tag | rel | skill f/i | wf | 语言 |")
out.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
for r in rows:
    out.append(
        f"| `{r['repo']}` | {r['stars']:,} | {r['forks']:,} | {r['fork_star_pct']}% | "
        f"{r['subs']} | {r['raw_oi']} | {r['issues']} | {r['prs']} | {r['blobs']:,} | "
        f"{r['tags']} | {r['releases']} | {r['skill_files']}/{r['skill_identities']} | "
        f"{r['n_workflows']} | {r['language']} |"
    )
open("/tmp/table_1121.md", "w").write("\n".join(out) + "\n")
print("\n".join(out))
