#!/usr/bin/env python3
"""11-22 — final verification batch before writing.

F1. ECC: are the docs/<locale>/ SKILL.md files installable skills, or only
    documentation-site material?  Check the skills manifest / packaging config.
F2. ECC: exact split of the 1,089 SKILL.md into canonical / harness / i18n.
F3. opensre: dual version scheme (calendar + semver) + duplicate tag->commit.
F4. CLI-Anything: what does the "82 names / 131 contents" divergence look like?
F5. open-code-review: full download distribution for ALL its 100 releases, to
    test whether the 11-18 published range "57-951" was a truncated sample.
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


print("=" * 100)
print("F1/F2. ECC — i18n vs canonical vs harness, and are docs/<locale> installable?")
print("=" * 100)
full = "affaan-m/ECC"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
skills = [b for b in blobs if os.path.basename(b.get("path") or "").lower() == "skill.md"]
LOCALE = {"ja-JP", "zh-CN", "zh-TW", "es", "tr", "ko-KR", "fr", "de", "pt-BR", "ru", "it"}
HARNESS_PREFIX = (".agents/", ".kiro/", ".cursor/", "pi/", ".claude-plugin/", ".codex-plugin/",
                   ".gemini/", ".grok-plugin/", ".opencode/", ".claude/")
cat = Counter()
for b in skills:
    p = b.get("path") or ""
    parts = p.split("/")
    if parts[0] == "docs" and len(parts) >= 2 and parts[1] in LOCALE:
        cat["i18n(docs/<locale>)"] += 1
    elif p.startswith(HARNESS_PREFIX):
        cat["harness(<harness dir>)"] += 1
    elif p.startswith("skills/"):
        cat["canonical(skills/)"] += 1
    else:
        cat["other"] += 1
print("   category split of the 1,089 SKILL.md:")
for k, v in cat.most_common():
    print(f"      {k:28s} {v:5d}  ({100.0*v/len(skills):5.1f}%)")

# is there a skills manifest that enumerates installable skills?
for cand in ["skills.json", "skills/index.json", "package.json", "README.md",
             ".agents/skills", "skills"]:
    r = api(f"repos/{full}/contents/{urllib.parse.quote(cand)}")
    if isinstance(r, list):
        print(f"   contents/{cand}: {len(r)} entries "
              f"sample={[x.get('name') for x in r[:6]]}")
    elif isinstance(r, dict) and r.get("name"):
        print(f"   contents/{cand}: file {r.get('size')} B")
    else:
        print(f"   contents/{cand}: NOT FOUND")

# README statement about locale docs
rm = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"]) or ""
for ln in rm.splitlines():
    if re.search(r"(locale|i18n|translat|docs/|18 |language)", ln, re.I) if (re := __import__("re")) else False:
        print("   README>", ln[:170])

print()
print("=" * 100)
print("F3. opensre — dual version scheme + duplicate tag->commit")
print("=" * 100)
full = "Tracer-Cloud/opensre"
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
tags = tags if isinstance(tags, list) else []
cal, sem = [], []
for t in tags:
    n = t.get("name") or ""
    (cal if n.startswith("v2026.") else sem).append(n)
print(f"   tags={len(tags)}  calendar-style(v2026.M.D)={len(cal)}  semver-style={len(sem)}")
print(f"   calendar sample: {cal[:6]} ... {cal[-3:] if cal else ''}")
print(f"   semver sample  : {sem[:8]} ... {sem[-3:] if sem else ''}")
sha2 = defaultdict(list)
for t in tags:
    sha2[t.get("commit", {}).get("sha")].append(t.get("name"))
dups = {k: v for k, v in sha2.items() if len(v) > 1}
print(f"   distinct commit shas={len(sha2)} / {len(tags)} tags; dup groups={len(dups)}")
shown = 0
for k, v in dups.items():
    if shown < 8:
        print(f"     sha {k[:10]} -> {v}")
    shown += 1
print(f"   (total {shown} duplicate-sha groups)")
# release/tag correspondence
rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
rels = rels if isinstance(rels, list) else []
rel_tags = [r.get("tag_name") for r in rels]
print(f"   releases={len(rels)}; release tags not in tag list: "
      f"{[t for t in rel_tags if t not in {x.get('name') for x in tags}][:6]}")
# skills-sync workflow
wf = api(f"repos/{full}/contents/.github/workflows/skills-sync.yml", raw=True,
         headers=["Accept: application/vnd.github.raw"])
print("   skills-sync.yml present:", bool(wf))
if wf:
    for ln in wf.splitlines()[:40]:
        print("     |", ln[:150])

print()
print("=" * 100)
print("F4. CLI-Anything — the 82-name / 131-content divergence")
print("=" * 100)
full = "HKUDS/CLI-Anything"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
skills = [b for b in blobs if os.path.basename(b.get("path") or "").lower() == "skill.md"]
per = defaultdict(list)
for b in skills:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
    per[nm].append(b)
multi = {n: v for n, v in per.items() if len(v) > 1}
print(f"   files={len(skills)} names={len(per)} names_with_multi={len(multi)}")
tot_multi = sum(len(v) for v in multi.values())
print(f"   files in multi-copy names={tot_multi}")
div = {n: v for n, v in multi.items() if len({x.get('sha') for x in v}) > 1}
print(f"   of those, divergent names={len(div)}")
for n, v in list(div.items())[:6]:
    print(f"     {n}: {len(v)} copies, sizes={[x.get('size') for x in v]}, "
          f"distinct_sha={len({x.get('sha') for x in v})}")
    for x in v[:4]:
        print(f"        {x.get('path')}")
tops = Counter("/".join(b.get("path", "").split("/")[:2]) for b in skills)
print(f"   top dirs: {dict(tops.most_common(10))}")

print()
print("=" * 100)
print("F5. alibaba/open-code-review — FULL download distribution across 100 releases")
print("=" * 100)
full = "alibaba/open-code-review"
rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
rels = rels if isinstance(rels, list) else []
allmin, allmax = [], []
per_rel = []
for r in rels:
    dl = [a.get("download_count") or 0 for a in (r.get("assets") or [])]
    if dl:
        allmin.append(min(dl)); allmax.append(max(dl))
        per_rel.append((r.get("tag_name"), min(dl), max(dl), len(dl)))
if per_rel:
    gmin = min(x[1] for x in per_rel); gmax = max(x[2] for x in per_rel)
    print(f"   releases with assets: {len(per_rel)} / {len(rels)}")
    print(f"   GLOBAL min={gmin}  GLOBAL max={gmax}")
    print(f"   11-18 published range was '57-951'")
    print(f"   per-release (newest 12):")
    for t, mn, mx, n in per_rel[:12]:
        print(f"     {str(t):12s} n={n} min={mn:6d} max={mx:7d}")
    # how many releases have min < 57 (i.e. below the published floor)
    below = [x for x in per_rel if x[1] < 57]
    above = [x for x in per_rel if x[2] > 951]
    print(f"   releases whose min < 57 (below published floor): {len(below)}")
    print(f"   releases whose max > 951 (above published ceiling): {len(above)}")
    for t, mn, mx, n in above[:6]:
        print(f"     {t}: max={mx}")
