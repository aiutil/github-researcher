#!/usr/bin/env python3
"""Decisive cross-repo forensics for 2026-11-18.

Q1. COORDINATED FORK NETWORK: do the same accounts fork multiple trending
    repos on the same day?  If a set of accounts appears across many repos'
    fork lists, "trending" is being self-fed.

Q2. Fork owner ACCOUNT AGE for paper-orchestra's 100-fork wave.

Q3. TAG WITHOUT RELEASE: GoogleChrome/modern-web-guidance-src has 100 tags
    and 1 release (tag 'audit-data', prerelease).  Are the 100 tags real
    version bumps with code diffs (i.e. a third category distinct from
    ffmpeg-skill's 100 releases and steam-library-bridge's 4 fake releases)?

Q4. affaan-m/ECC: what are the 330 distinct skill identities actually?
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:300]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:300]}"


TRENDING = [
    "google-research/paper-orchestra", "Tencent/LoopForge",
    "backnotprop/plannotator", "getarcaneapp/arcane",
    "google-labs-code/stitch-skills", "elementalsouls/Claude-BugHunter",
    "obra/superpowers", "affaan-m/ECC", "cursor/plugins",
    "tradermonty/claude-trading-skills", "alibaba/open-code-review",
    "we-promise/sure", "anthropics/skills", "addyosmani/agent-skills",
    "GoogleChrome/modern-web-guidance-src",
]

_USER_CACHE = {}


def user_meta(login):
    if login not in _USER_CACHE:
        u, _ = api(f"users/{login}")
        _USER_CACHE[login] = u or {}
    return _USER_CACHE[login]


def fork_owners(full, n=100):
    forks, _ = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n})
    forks = forks if isinstance(forks, list) else []
    rows = []
    for f in forks:
        o = f.get("owner") or {}
        rows.append({
            "login": o.get("login"),
            "type": o.get("type"),
            "created_at": f.get("created_at"),
            "updated_at": f.get("updated_at"),
            "pushed_at": f.get("pushed_at"),
        })
    return full, rows


def tag_chain(full, n=14):
    """For each tag: does the tagged commit touch source? does the parent?"""
    tags, _ = api(f"repos/{full}/tags", {"per_page": 100})
    tags = tags if isinstance(tags, list) else []
    SRC = (".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".sh", ".java",
           ".c", ".cpp", ".rb", ".php", ".swift", ".kt", ".md", ".json", ".yaml")
    out = []
    for t in tags[:n]:
        sha = (t.get("commit") or {}).get("sha")
        c, _ = api(f"repos/{full}/commits/{sha}")
        c = c or {}
        files = [f.get("filename") for f in (c.get("files") or [])]
        parent = ((c.get("parents") or [{}])[0] or {}).get("sha")
        pf = []
        if parent:
            pc, _ = api(f"repos/{full}/commits/{parent}")
            pf = [f.get("filename") for f in ((pc or {}).get("files") or [])]
        out.append({
            "tag": t.get("name"),
            "sha": (sha or "")[:8],
            "date": (((c.get("commit") or {}).get("author") or {}).get("date")),
            "msg": (((c.get("commit") or {}).get("message") or "").split("\n")[0])[:70],
            "c_files": len(files), "c_list": files[:8],
            "p_files": len(pf), "p_list": pf[:8],
            "c_has_src": any(os.path.splitext(f)[1].lower() in SRC for f in files),
            "p_has_src": any(os.path.splitext(f)[1].lower() in SRC for f in pf),
        })
    return {"repo": full, "n_tags": len(tags), "chain": out}


def ecc_identities():
    full = "affaan-m/ECC"
    tree, _ = api(f"repos/{full}/git/trees/main?recursive=1")
    blobs = [b for b in ((tree or {}).get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    ident = defaultdict(list)
    for b in skills:
        p = b.get("path")
        parent = os.path.basename(os.path.dirname(p)) if p else ""
        ident[parent].append(p)
    roots = Counter()
    for b in skills:
        p = b.get("path") or ""
        parts = p.split("/")
        # which harness dir
        for h in (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".plugin",
                  ".grok-plugin", ".gemini", ".windsurf", ".opencode", ".agents",
                  ".kiro", ".cursor", ".claude", ".codebuddy"):
            if p.startswith(h + "/"):
                roots[h] += 1
                break
        else:
            roots["<" + (parts[0] if len(parts) > 1 else "root") + ">"] += 1
    return {
        "n_skill_files": len(skills),
        "n_identities": len(ident),
        "roots": dict(roots.most_common()),
        "sample_identities": sorted(ident)[:40],
    }


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "network"):
        print("========== Q1: COORDINATED FORK NETWORK ==========")
        fork_map = {}
        with ThreadPoolExecutor(max_workers=5) as ex:
            for full, rows in ex.map(lambda t: fork_owners(t), TRENDING):
                fork_map[full] = rows
                print(f"  fetched {full}: {len(rows)} forks")

        # who forked >1 repo?
        who = defaultdict(list)
        for full, rows in fork_map.items():
            for r in rows:
                if r["login"]:
                    who[r["login"]].append((full, r["created_at"], r["type"]))
        multi = {k: v for k, v in who.items() if len({f for f, _, _ in v}) >= 2}
        print(f"\n  distinct fork accounts observed: {len(who)}")
        print(f"  accounts that forked >=2 of the {len(TRENDING)} repos: {len(multi)}")
        for k, v in sorted(multi.items(), key=lambda kv: -len(kv[1]))[:30]:
            repos = sorted({f for f, _, _ in v})
            days = Counter((c or '')[:10] for _, c, _ in v)
            print(f"    {k:<26} repos={len(repos)} forks={len(v)} "
                  f"days={dict(days)} -> {repos[:6]}")

        print("\n  === per-repo: distinct fork accounts & repeat rate ===")
        for full, rows in fork_map.items():
            logins = [r["login"] for r in rows if r["login"]]
            c = Counter(logins)
            rep = sum(1 for v in c.values() if v > 1)
            print(f"    {full:<44} forks={len(rows):<4} distinct={len(c):<4} "
                  f"repeat_forkers={rep}")

        print("\n  === Q2: fork owner account age (paper-orchestra wave) ===")
        po = fork_map.get("google-research/paper-orchestra", [])
        metas = []
        for r in po[:40]:
            u = user_meta(r["login"]) if r["login"] else {}
            metas.append((r["login"], (u.get("created_at") or "")[:10],
                          u.get("public_repos"), u.get("followers"),
                          u.get("type"), r["created_at"]))
        ages = Counter(m[1] for m in metas)
        print(f"    sampled {len(metas)} fork owners; account-created dates:")
        for d, n in sorted(ages.items(), reverse=True)[:25]:
            print(f"      {d}: {n}")
        newish = sum(1 for m in metas if m[1] and m[1] >= "2026-11-01")
        print(f"    accounts created on/after 2026-11-01: {newish}/{len(metas)}")
        print(f"    sample rows (login, created, repos, followers, type, forked_at):")
        for m in metas[:15]:
            print(f"      {m}")

    if which in ("all", "tagchain"):
        print("\n\n========== Q3: tag chain for repos with tag/release asymmetry ==========")
        for t in ["GoogleChrome/modern-web-guidance-src", "obra/superpowers",
                  "we-promise/sure", "Tencent/LoopForge"]:
            r = tag_chain(t)
            print(f"\n--- {r['repo']} --- n_tags={r['n_tags']}")
            for x in r["chain"][:10]:
                print(f"    {x['tag']:<16} {x['date'][:10]} c={x['c_files']:<3}"
                      f"src={int(x['c_has_src'])} p={x['p_files']:<3}"
                      f"psrc={int(x['p_has_src'])}  {x['msg'][:50]}")
                print(f"        c_list={x['c_list']}")
                print(f"        p_list={x['p_list']}")

    if which in ("all", "ecc"):
        print("\n\n========== Q4: affaan-m/ECC skill identity anatomy ==========")
        r = ecc_identities()
        print(json.dumps(r, ensure_ascii=False, indent=1))
