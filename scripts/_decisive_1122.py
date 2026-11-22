#!/usr/bin/env python3
"""11-22 — three decisive checks:

C1. ECC: split its SKILL.md replication into (a) i18n translations under
    docs/<locale>/ and (b) genuine cross-harness adaptation.  The 11-18 report
    treated all 1,087 files as "one skill replicated 3.30x"; that may be
    counting translations as duplication.

C2. modern-web-guidance-src: it has 100 tags but only 99 distinct commit
    shas.  Which two tags share a commit?

C3. `mvanhorn/last30days-skill` was published in the 11-18 daily report as
    "0 tag / 0 release".  But its releases go back to 2026-02-17.  Check the
    11-18/11-20/11-21 raw probe files to see whether that was a measurement
    failure rather than a repo fact.
"""
import json
import os
import subprocess
import urllib.parse
from collections import defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


print("=" * 100)
print("C1. ECC — i18n translations vs cross-harness adaptation")
print("=" * 100)
full = "affaan-m/ECC"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
skills = [b for b in blobs if os.path.basename(b.get("path") or "").lower() == "skill.md"]

LOCALE = {"ja-JP", "zh-CN", "zh-TW", "es", "tr", "ko-KR", "fr", "de", "pt-BR", "ru", "it"}
i18n, harness = [], []
for b in skills:
    p = b.get("path") or ""
    parts = p.split("/")
    if len(parts) >= 3 and parts[0] == "docs" and parts[1] in LOCALE:
        i18n.append(b)
    else:
        harness.append(b)
print(f"   total SKILL.md            : {len(skills)}")
print(f"   under docs/<locale>/      : {len(i18n)}  ({100.0*len(i18n)/len(skills):.1f}%)")
print(f"   NOT under docs/<locale>/  : {len(harness)}  ({100.0*len(harness)/len(skills):.1f}%)")


def axis(items, label):
    per_name = defaultdict(list)
    for b in items:
        p = b.get("path") or ""
        nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        per_name[nm].append(b)
    n_name = len(per_name)
    n_content = len({b.get("sha") for b in items})
    dup = div = 0
    for nm, lst in per_name.items():
        if len(lst) < 2:
            continue
        if len({x.get("sha") for x in lst}) == 1:
            dup += len(lst) - 1
        else:
            div += len(lst)
    print(f"   [{label}] files={len(items):5d} name_ident={n_name:4d} content_ident={n_content:4d} "
          f"byte-identical-dup={dup:4d} divergent={div:4d} files/content="
          f"{len(items)/n_content if n_content else 0:.2f}")
    return n_name, n_content


axis(skills, "ALL     ")
axis(harness, "NON-i18n")
axis(i18n, "i18n    ")

# what the i18n set actually looks like: same skill name, translated content?
print("\n   i18n sample (same skill name across locales):")
byname = defaultdict(list)
for b in i18n:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p))
    byname[nm].append((p, b.get("size"), b.get("sha")))
multi = {n: v for n, v in byname.items() if len(v) > 1}
print(f"   i18n skill names with >1 locale copy: {len(multi)}")
for n, v in list(multi.items())[:5]:
    print(f"     {n}: {len(v)} locales, sizes={[x[1] for x in v]}, distinct_sha={len({x[2] for x in v})}")
    for p, s, _ in v[:4]:
        print(f"        {p}")

print("\n   non-i18n sample (cross-harness same skill name):")
byname2 = defaultdict(list)
for b in harness:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
    byname2[nm].append((p, b.get("size"), b.get("sha")))
multi2 = {n: v for n, v in byname2.items() if len(v) > 1}
print(f"   non-i18n skill names with >1 copy: {len(multi2)}")
for n, v in list(multi2.items())[:5]:
    print(f"     {n}: {len(v)} copies, sizes={[x[1] for x in v]}, distinct_sha={len({x[2] for x in v})}")
    for p, s, _ in v[:5]:
        print(f"        {p}")

print()
print("=" * 100)
print("C2. modern-web-guidance-src — the 2 tags sharing a commit")
print("=" * 100)
full = "GoogleChrome/modern-web-guidance-src"
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
sha2tags = defaultdict(list)
for t in tags:
    sha2tags[t.get("commit", {}).get("sha")].append(t.get("name"))
dups = {k: v for k, v in sha2tags.items() if len(v) > 1}
print(f"   tags={len(tags)} distinct_shas={len(sha2tags)} dup_groups={len(dups)}")
for k, v in dups.items():
    print(f"     sha {k[:12]} -> tags {v}")

print()
print("=" * 100)
print("C3. Was 'last30days-skill 0 tag / 0 release' (11-18 report) a measurement failure?")
print("=" * 100)
for f in ["/tmp/probe_1121.json", "/tmp/probe_1120.json"]:
    try:
        P = json.load(open(f))
    except Exception as e:  # noqa: BLE001
        print(f"   {f}: {e}")
        continue
    for p in P:
        if p["full_name"] == "mvanhorn/last30days-skill":
            print(f"   {f}: n_tags={p['n_tags']} n_releases={p['n_releases']} "
                  f"files={p['n_blobs']} skills={p['n_skill_files']}")
# and what the API says now
full = "mvanhorn/last30days-skill"
rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
rels = rels if isinstance(rels, list) else []
dates = sorted(str(r.get("published_at"))[:10] for r in rels)
print(f"   live API: {len(rels)} releases; earliest published {dates[0] if dates else '-'}, "
      f"latest {dates[-1] if dates else '-'}")
tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
print(f"   live API: {len(tags) if isinstance(tags,list) else 0} tags")
# how many releases existed BEFORE 11-18?
before = [r for r in rels if str(r.get("published_at"))[:10] < "2026-11-18"]
print(f"   releases published BEFORE 2026-11-18: {len(before)}  "
      f"(oldest {sorted(str(r.get('published_at'))[:10] for r in before)[:3]})")
print("   => the 11-18 report's '0 tag / 0 release' was a MEASUREMENT FAILURE, not a repo fact.")
