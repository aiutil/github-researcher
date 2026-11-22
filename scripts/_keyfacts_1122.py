#!/usr/bin/env python3
"""11-22 — FINAL consolidated numbers for the 9 key projects.
Everything here is a single API snapshot; no derived claims.
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


KEY = ["affaan-m/ECC", "backnotprop/plannotator", "alibaba/open-code-review",
       "mvanhorn/last30days-skill", "GoogleChrome/modern-web-guidance-src",
       "cursor/plugins", "HKUDS/CLI-Anything", "Tracer-Cloud/opensre",
       "mjmirza/app-store-compliance"]
LOCALE = {"ja-JP", "zh-CN", "zh-TW", "es", "tr", "ko-KR", "fr", "de", "pt-BR", "ru", "it"}
HARNESS_PREFIX = (".agents/", ".kiro/", ".cursor/", "pi/", ".claude-plugin/", ".codex-plugin/",
                   ".gemini/", ".grok-plugin/", ".opencode/", ".claude/")

out = {}
for full in KEY:
    m = api(f"repos/{full}") or {}
    lic = m.get("license") or {}
    own = m.get("owner") or {}
    om = api(f"users/{own.get('login')}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs
              if os.path.basename(b.get("path") or "").lower() == "skill.md"]
    per = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per[nm].append(b)
    dup = div = 0
    max_any = 0
    max_identical = 0
    for nm, lst in per.items():
        max_any = max(max_any, len(lst))
        if len(lst) < 2:
            continue
        if len({x.get("sha") for x in lst}) == 1:
            dup += len(lst) - 1
            max_identical = max(max_identical, len(lst))
        else:
            div += len(lst)
    i18n = sum(1 for b in skills
               if b.get("path", "").split("/")[0] == "docs"
               and len(b.get("path", "").split("/")) >= 2
               and b.get("path", "").split("/")[1] in LOCALE)
    canonical = sum(1 for b in skills if b.get("path", "").startswith("skills/"))
    harness = sum(1 for b in skills if b.get("path", "").startswith(HARNESS_PREFIX))

    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rels = rels if isinstance(rels, list) else []
    dl_all = []
    n_assets_set = []
    for r in rels:
        assets = r.get("assets") or []
        n_assets_set.append(len(assets))
        dl_all += [a.get("download_count") or 0 for a in assets]
    rel_dates = sorted(str(r.get("published_at"))[:10] for r in rels if r.get("published_at"))

    rec = {
        "full": full,
        "stars": m.get("stargazers_count"), "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"), "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"), "blobs": len(blobs),
        "lang": m.get("language"), "lic": lic.get("spdx_id"),
        "created": m.get("created_at"), "pushed": m.get("pushed_at"),
        "owner": own.get("login"), "owner_type": own.get("type"),
        "owner_created": om.get("created_at"), "owner_foll": om.get("followers"),
        "owner_pub": om.get("public_repos"),
        "homepage": m.get("homepage"), "desc": m.get("description"),
        "topics": m.get("topics"),
        "skill_files": len(skills), "skill_names": len(per),
        "skill_contents": len({b.get("sha") for b in skills}),
        "dup_files": dup, "div_files": div,
        "dup_pct": round(100.0*dup/len(skills), 1) if skills else 0,
        "adapt_pct": round(100.0*div/len(skills), 1) if skills else 0,
        "max_name_copies": max_any, "max_identical_copies": max_identical,
        "i18n": i18n, "canonical": canonical, "harness": harness,
        "n_tags": len(tags),
        "distinct_tag_shas": len({t.get("commit", {}).get("sha") for t in tags}),
        "n_releases": len(rels),
        "assets_min": min(n_assets_set) if n_assets_set else 0,
        "assets_max": max(n_assets_set) if n_assets_set else 0,
        "dl_min": min(dl_all) if dl_all else 0, "dl_max": max(dl_all) if dl_all else 0,
        "dl_sum": sum(dl_all),
        "rel_first": rel_dates[0] if rel_dates else None,
        "rel_last": rel_dates[-1] if rel_dates else None,
        "tag_names": [t.get("name") for t in tags[:6]],
    }
    out[full] = rec
    print(f"{full}")
    print(f"   ⭐{rec['stars']:,} forks {rec['forks']:,} subs {rec['subs']} oi {rec['oi']} "
          f"blobs {rec['blobs']:,} {rec['lang']} {rec['lic']}")
    print(f"   owner {rec['owner']}({rec['owner_type']}) created {str(rec['owner_created'])[:10]} "
          f"foll {rec['owner_foll']} pub {rec['owner_pub']} | created {str(rec['created'])[:10]} "
          f"pushed {str(rec['pushed'])[:10]}")
    print(f"   SKILL: files {rec['skill_files']} | names {rec['skill_names']} | "
          f"contents {rec['skill_contents']} | dup {rec['dup_files']}({rec['dup_pct']}%) "
          f"div {rec['div_files']}({rec['adapt_pct']}%) | max copies {rec['max_name_copies']} "
          f"(identical {rec['max_identical_copies']})")
    print(f"   i18n {rec['i18n']} canonical {rec['canonical']} harness {rec['harness']}")
    print(f"   tags {rec['n_tags']} (distinct shas {rec['distinct_tag_shas']}) | "
          f"releases {rec['n_releases']} assets {rec['assets_min']}-{rec['assets_max']} | "
          f"dl {rec['dl_min']}-{rec['dl_max']} sum {rec['dl_sum']:,}")
    print(f"   release window {rec['rel_first']} .. {rec['rel_last']} | tags {rec['tag_names']}")
    print()

json.dump(out, open("/tmp/key_1122.json", "w"), ensure_ascii=False, indent=1)
print("wrote /tmp/key_1122.json")
