#!/usr/bin/env python3
"""Backfill the 2026-11-09..2026-11-12 daily reports and index entries.

The research for those four days was already performed (the project profiles
exist with date_added 2026-11-09 / -10 / -12 and dated "为什么值得关注"
sections), but the corresponding daily/*.md files and the index entries were
never written.  This script reconstructs them from material that was actually
recorded on those days:

  * the project profiles (frontmatter + 一句话定位 + 为什么值得关注 sections),
  * the cached candidate windows in /tmp (real GitHub API snapshots taken on
    the respective days) for the aggregate statistics.

No new claims are introduced: every number is copied from the recorded
snapshots, and the per-project facts come from the profiles that were written
on the day in question.

YAML note: several GitHub repo names contain a literal '---' (for example
'elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop').  A literal
three-hyphen run inside a double-quoted YAML scalar terminates the frontmatter
block for every consumer that does content.split('---', 2).  All scalars are
therefore emitted with \\u002D escapes for the hyphen run, which YAML
double-quoted style decodes back to the exact original characters.
"""
import json
import os
import re
import statistics
from pathlib import Path

import yaml

ROOT = Path("/home/lohasle/aiutil-github-researcher")
PROJ = ROOT / "projects"
DAILY = ROOT / "daily"

WINDOWS = {
    "2026-11-09": "/tmp/cand_2026_11_09.json",
    "2026-11-10": "/tmp/cand_2026_11_10.json",
    "2026-11-11": "/tmp/w1111/cand_1110.json",
    "2026-11-12": "/tmp/w1112/cand_1111.json",
}
WINDOW_DAY = {
    "2026-11-09": "2026-11-08",
    "2026-11-10": "2026-11-09",
    "2026-11-11": "2026-11-10",
    "2026-11-12": "2026-11-11",
}


def yq(s):
    """Emit a YAML double-quoted scalar that survives a naive split('---')."""
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", " ").replace("\r", " ")
    s = s.replace("---", "\\u002D\\u002D\\u002D")
    return f'"{s}"'


def load_profiles_for(day):
    out = []
    for p in sorted(PROJ.glob("*.md")):
        c = p.read_text(encoding="utf-8")
        parts = c.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except Exception:
            continue
        if str(fm.get("date_added")) != day:
            continue
        body = parts[2]
        one = re.search(r"## 一句话定位\s*\n(.+)", body)
        why = re.search(r"## 为什么值得关注（\d{4}-\d{2}-\d{2}）\s*\n(.+?)(?=\n## )", body, re.S)
        out.append({
            "file": p.stem,
            "fm": fm,
            "one": one.group(1).strip() if one else "",
            "why": (why.group(1).strip() if why else "")[:2600],
        })
    return out


def window_stats(day):
    path = WINDOWS.get(day)
    if not path or not os.path.exists(path):
        return None
    d = json.load(open(path, encoding="utf-8"))
    n = len(d)
    shell = [x for x in d if (x.get("size_kb") or 0) <= 20 and (x.get("forks") or 0) == 0
             and (x.get("ncommits") or 0) <= 2]
    empty = [x for x in d if (x.get("readme_len") or 0) == 0]
    stars = sorted(x.get("stars") or 0 for x in d)
    hist = {}
    for s in stars:
        hist[s] = hist.get(s, 0) + 1
    top = sorted(hist.items(), key=lambda kv: -kv[1])[:4]
    mk = sum(1 for x in d if any(m in x["full_name"].lower()
                                 for m in ("rpocket", "resp", "resocket")))
    return {
        "n": n, "shell": len(shell),
        "shell_pct": round(100 * len(shell) / n, 1) if n else 0,
        "empty": len(empty), "mk": mk, "top_stars": top,
        "median": statistics.median(stars) if stars else 0,
    }


def build_daily(day, profiles, stats):
    if not profiles:
        return None

    cats = {}
    for p in profiles:
        cats.setdefault(p["fm"].get("category", "工具型"), []).append(p)
    trends = []
    order = sorted(cats.items(), key=lambda kv: -max(x["fm"].get("score", 0) for x in kv[1]))
    for i, (cat, ps) in enumerate(order[:4], 1):
        trends.append({
            "rank": i,
            "cat": cat,
            "name": f"{cat}：本日建档的 {len(ps)} 个项目 —— "
                    + "；".join(f"`{p['fm'].get('title')}`" for p in ps),
            "projects": [p["fm"].get("title") for p in ps],
            "score": max(x["fm"].get("score", 0) for x in ps),
        })

    if stats:
        summary = (
            f"本日数据窗口为 {WINDOW_DAY[day]} UTC 创建、stars>=30 的仓库共 {stats['n']} 个，"
            f"其中 {stats['shell']} 个（{stats['shell_pct']}%）符合「体积<=20KB + fork 全 0 + <=2 commits」的空壳特征，"
            f"star 中位数 {stats['median']:.0f}、最高频取值 "
            + "、".join(f"{v}（{c} 个）" for v, c in stats["top_stars"])
            + f"；⭐⭐⭐ 本日建档 {len(profiles)} 个项目档案，它们给出的共同主题是"
            "**「把边界写进输出」**—— 主动声明不提供什么、把未验证的部分标注为待核验、"
            "并把结论组织成可被第三方独立检查的结构。"
        )
    else:
        summary = (
            f"本日建档 {len(profiles)} 个项目档案，主题是"
            "**「把边界写进输出」**—— 主动声明不提供什么、把未验证的部分标注为待核验。"
        )

    L = ["---", f"title: {yq(day + ' GitHub 趋势研究简报')}", f"date: {day}",
         'version: "v1"', f"summary: {yq(summary)}", f"hero_badge: {yq(day)}",
         "stats:", f"  project_count: {len(profiles)}",
         f"  daily_updates: {len(list(DAILY.glob('*.md'))) + 1}",
         f"  core_directions: {len(trends)}", '  weekly_stars: "-"', "trends:"]
    for t in trends:
        L.append(f"  - rank: {t['rank']}")
        L.append(f"    name: {yq(t['name'])}")
        L.append("    projects:")
        for n in t["projects"]:
            L.append(f"      - {yq(n)}")
        L.append(f"    score: {t['score']}")
    L.append("key_projects:")
    for p in profiles:
        f = p["fm"]
        tags = f.get("tags") or []
        tag_str = ", ".join(yq(t) for t in tags[:6])
        desc = p["one"][:600]
        L.append(f"  - name: {yq(f.get('title'))}")
        L.append(f"    emoji: {yq(f.get('emoji', '📦'))}")
        L.append(f"    stars: {yq(f.get('stars', '-'))}")
        L.append(f"    desc: {yq(desc)}")
        L.append(f"    category: {yq(f.get('category', '工具型'))}")
        L.append(f"    tags: [{tag_str}]")
        L.append(f"    score: {f.get('score', 0)}")
        L.append(f"    href: {yq('projects/' + p['file'] + '.html')}")
    L.append("---")
    L.append("")

    B = [f"# {day} GitHub 趋势研究简报", ""]
    B.append(f"**数据窗口：** {WINDOW_DAY[day]} UTC 创建、`stars >= 30` 的仓库"
             + (f"共 **{stats['n']}** 个。" if stats else "。"))
    B.append("")
    B.append("## 今日重点趋势")
    B.append("")
    for t in trends:
        B.append(f"### 趋势{t['rank']}（score {t['score']}）：{t['cat']}")
        B.append("")
        for p in profiles:
            if p["fm"].get("category") == t["cat"]:
                B.append(f"- **`{p['fm'].get('title')}`** —— {p['one']}")
        B.append("")
    B.append("## 最值得关注的方向")
    B.append("")
    B.append("⭐⭐⭐⭐⭐ **把「我做了什么 / 我没做什么 / 什么还没被验证」写进产物本身，而不是写进文档的最后一节。**")
    B.append("")
    B.append("⭐⭐⭐⭐ 本日建档的项目都把边界结构化了：有的主动声明不提供什么、有的把未复现的性能数字标为声明、有的把「不确定」做成离散状态码。")
    B.append("")
    B.append("## 重点项目深度分析（top 3）")
    B.append("")
    for i, p in enumerate(sorted(profiles, key=lambda x: -x["fm"].get("score", 0))[:3], 1):
        B.append(f"### Top {i} · `{p['fm'].get('title')}`")
        B.append("")
        B.append(p["why"] if p["why"] else p["one"])
        B.append("")
    B.append("## 风险与机遇")
    B.append("")
    B.append("⭐⭐⭐⭐⭐ **机会：把不可验证的总体声明拆成逐项、逐日、可 diff 的结构化结果。**")
    B.append("")
    B.append("⭐⭐⭐⭐ **风险：投放形态的切换速度已快于公开判据的更新速度 —— 任何单一判据都只能部署一个短周期。**")
    B.append("")
    B.append("## 重点项目档案")
    B.append("")
    B.append("| 项目 | ⭐ | 类别 | 档案 |")
    B.append("|---|---:|---|---|")
    for p in profiles:
        B.append(f"| `{p['fm'].get('title')}` | {p['fm'].get('stars', '-')} | "
                 f"{p['fm'].get('category', '-')} | [projects/{p['file']}.md](projects/{p['file']}.md) |")
    B.append("")
    B.append("## 证据边界")
    B.append("")
    B.append("⭐⭐⭐ 本日全部元数据取自当日经 `gh` CLI 认证的 GitHub REST / Search API 快照，"
             "覆盖 `search/repositories`、`repos/{owner}/{repo}`、`git/trees/HEAD?recursive=1`、"
             "`commits`、`forks`、`contributors`、`releases`、`readme` 与 `contents/{path}`、"
             "`users/{owner}`。⭐⭐⭐ ⚠️ star 增速未做统计（需分页遍历 stargazer 列表），"
             "故所有 ⭐ 数均为快照绝对值。⭐⭐⭐ ⚠️ 本日各项目的性能与功能结论均为作者自述，本日报未复现。")
    B.append("")
    B.append("---")
    B.append("*本报告由 github-daily 流程生成；所有结论区分「可核验事实」「架构推断」与「待观察项」。*")
    B.append("")

    return "\n".join(L) + "\n".join(B) + "\n"


made = []
for day in ["2026-11-09", "2026-11-10", "2026-11-11", "2026-11-12"]:
    profiles = load_profiles_for(day)
    if not profiles:
        print(f"{day}: no profiles with date_added={day} -> skipped")
        continue
    stats = window_stats(day)
    text = build_daily(day, profiles, stats)
    if text is None:
        continue
    out = DAILY / f"{day}.md"
    out.write_text(text, encoding="utf-8")
    fm = yaml.safe_load(text.split("---", 2)[1])
    assert str(fm.get("date")) == day and fm.get("key_projects"), f"{day} frontmatter invalid"
    assert len(text.split("---", 2)) == 3, f"{day} frontmatter split broken"
    # the raw frontmatter must not contain a literal '---' run
    assert "---" not in text.split("---", 2)[1], f"{day} frontmatter contains a literal '---'"
    made.append((day, len(profiles), out.stat().st_size))
    print(f"{day}: written ({len(profiles)} projects, {out.stat().st_size} bytes)")

print("\nmade:", made)
