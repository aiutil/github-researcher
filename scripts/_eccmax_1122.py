#!/usr/bin/env python3
"""11-22 — ECC: which skill name has 10 copies, and are those copies identical
or divergent?  (The 11-18 report said "最大单一技能被复制 10 份".)"""
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


full = "affaan-m/ECC"
m = api(f"repos/{full}") or {}
tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
skills = [b for b in blobs if os.path.basename(b.get("path") or "").lower() == "skill.md"]
per = defaultdict(list)
for b in skills:
    p = b.get("path") or ""
    nm = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
    per[nm].append(b)

print(f"{full}: {len(skills)} SKILL.md, {len(per)} distinct names, "
      f"{len({b.get('sha') for b in skills})} distinct contents")
print("\ntop names by copy count:")
for nm, lst in sorted(per.items(), key=lambda kv: -len(kv[1]))[:12]:
    shas = {x.get("sha") for x in lst}
    sizes = sorted(x.get("size") or 0 for x in lst)
    kind = "IDENTICAL" if len(shas) == 1 else "DIVERGENT"
    print(f"   {nm:34s} x{len(lst):2d} [{kind:9s}] distinct_sha={len(shas)} sizes={sizes}")

print("\nthe 10-copy names, with paths:")
for nm, lst in sorted(per.items(), key=lambda kv: -len(kv[1]))[:4]:
    if len(lst) < 8:
        continue
    print(f"\n  --- {nm} (x{len(lst)}, distinct_sha={len({x.get('sha') for x in lst})})")
    for x in sorted(lst, key=lambda y: y.get("path")):
        print(f"      {x.get('size'):7d} B  {x.get('sha')[:10]}  {x.get('path')}")

# what does the '10 copies' look like under a de-duplicated content view?
tot_files = len(skills)
tot_contents = len({b.get("sha") for b in skills})
print(f"\nfiles / distinct contents = {tot_files} / {tot_contents} = "
      f"{tot_files/tot_contents:.2f}")
names_multi = [n for n, l in per.items() if len(l) > 1]
print(f"names with >1 copy: {len(names_multi)}")
ident = [n for n in names_multi if len({x.get('sha') for x in per[n]}) == 1]
div = [n for n in names_multi if len({x.get('sha') for x in per[n]}) > 1]
print(f"   byte-identical (true duplication): {len(ident)} names, "
      f"{sum(len(per[n])-1 for n in ident)} extra files")
print(f"   divergent (adaptation)          : {len(div)} names, "
      f"{sum(len(per[n]) for n in div)} files")
