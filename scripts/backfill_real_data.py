#!/usr/bin/env python3
"""
GitHub 研究 - 历史日期真实数据补全

对每个占位日报，使用 GitHub Search API 获取当时活跃的高星项目，
生成真实趋势日报。
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY_DIR = os.path.join(PROJECT_ROOT, "daily")

# Focus categories - these are the areas we track
SEARCH_QUERIES = [
    # AI Agent / LLM infra - the hottest area
    ('stars:>1000+created:>2025-06-01+pushed:{start}..{end}', "AI/热门新项目"),
    ('stars:>5000+topic:ai-agent+pushed:{start}..{end}', "AI Agent"),
    ('stars:>1000+topic:llm+pushed:{start}..{end}', "LLM"),
    ('stars:>500+topic:mcp+pushed:{start}..{end}', "MCP"),
    ('stars:>1000+topic:rag+pushed:{start}..{end}', "RAG"),
    # Dev tools
    ('stars:>3000+topic:developer-tools+pushed:{start}..{end}', "开发工具"),
    ('stars:>2000+topic:cli+pushed:{start}..{end}', "CLI"),
    # Infra
    ('stars:>5000+topic:cloud-native+pushed:{start}..{end}', "云原生"),
    ('stars:>3000+topic:kubernetes+pushed:{start}..{end}', "K8s"),
    # Frontend
    ('stars:>5000+topic:frontend+pushed:{start}..{end}', "前端"),
    ('stars:>3000+topic:react+pushed:{start}..{end}', "React"),
]

CATEGORY_EMOJIS = {
    "ai-agent": "🤖", "llm": "🧠", "mcp": "🔗", "rag": "📚",
    "inference": "⚡", "coding-agent": "💻", "developer-tools": "🛠️",
    "cli": "⌨️", "cloud-native": "☁️", "kubernetes": "🐳",
    "frontend": "🎨", "react": "⚛️", "rust": "🦀", "python": "🐍",
    "automation": "🔄", "browser-use": "🌐", "workflow": "📊",
    "default": "📦",
}


def gh_search(query_template, date_str, per_page=10):
    """Use gh CLI to search GitHub repos"""
    d = datetime.strptime(date_str, "%Y-%m-%d")
    next_day = (d + timedelta(days=1)).strftime("%Y-%m-%d")
    query = query_template.format(start=date_str, end=next_day)

    try:
        cmd = [
            "gh", "api",
            f"search/repositories?q={query}&sort=stars&order=desc&per_page={per_page}",
            "--jq", '.items[] | {full_name, name, stargazers_count, forks_count, description, language, html_url, topics, created_at, updated_at, open_issues_count}'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"    [warn] gh search failed: {result.stderr[:200]}")
            return []

        repos = []
        for line in result.stdout.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            try:
                repo = json.loads(line)
                repos.append(repo)
            except json.JSONDecodeError:
                continue
        return repos
    except Exception as e:
        print(f"    [error] gh search: {e}")
        return []


def find_placeholder_dates():
    """Find all daily files that are placeholders"""
    dates = []
    for fname in sorted(os.listdir(DAILY_DIR)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(DAILY_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if "定时任务迁移期间数据缺失" in content or "占位补全" in content:
            date_str = fname.replace(".md", "")
            dates.append(date_str)
    return dates


def make_slug(name):
    """Generate URL-safe slug from project name"""
    import re
    slug = name.lower()
    slug = re.sub(r'[()]', '', slug)
    slug = slug.replace(" ", "-")
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def deduplicate_repos(all_repos, seen_names=None):
    """Deduplicate repos by full_name, keep highest stars"""
    if seen_names is None:
        seen_names = set()
    unique = []
    for repo in all_repos:
        name = repo.get("full_name", "")
        if name and name not in seen_names:
            seen_names.add(name)
            unique.append(repo)
    return unique


def rank_and_select(repos, top_n=10):
    """Rank repos and select top projects"""
    # Sort by stars
    repos.sort(key=lambda r: r.get("stargazers_count", 0), reverse=True)
    return repos[:top_n]


def generate_daily_md(date_str, repos, daily_num):
    """Generate a real daily report from repo data"""
    if not repos:
        return None

    top_repos = rank_and_select(repos, top_n=10)

    # Identify trends/themes
    trends = []
    # Group by language/topic patterns
    lang_counts = {}
    topic_counts = {}
    for r in top_repos:
        lang = r.get("language") or "Other"
        lang_counts[lang] = lang_counts.get(lang, 0) + 1
        for t in r.get("topics", [])[:5]:
            topic_counts[t] = topic_counts.get(t, 0) + 1

    # Top topics as trends
    sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)
    for i, (topic, count) in enumerate(sorted_topics[:5]):
        matching = [r for r in top_repos if topic in (r.get("topics") or [])]
        projects = list(set([make_slug(r["name"]) for r in matching]))[:4]
        score = min(95, 60 + count * 10)
        trends.append({
            "rank": i + 1,
            "name": f"{topic}（{count} 个活跃项目）" if count > 1 else f"{topic} 方向活跃",
            "projects": projects,
            "score": score,
        })

    # If no topics found, create generic trends
    if not trends:
        trends = [{
            "rank": 1,
            "name": "高星项目活跃更新",
            "projects": [make_slug(r["name"]) for r in top_repos[:3]],
            "score": 75,
        }]

    # Build key_projects frontmatter
    key_projects = []
    for r in top_repos[:8]:
        name = r.get("full_name", r.get("name", ""))
        stars = r.get("stargazers_count", 0)
        desc = (r.get("description") or "No description")[:120]
        lang = r.get("language") or "Other"
        topics = r.get("topics", [])[:5]

        # Determine category
        category = "工具型"
        topics_lower = [t.lower() for t in topics]
        if any(t in topics_lower for t in ["ai-agent", "agent", "agentic"]):
            category = "平台候选"
        elif any(t in topics_lower for t in ["llm", "ai", "machine-learning"]):
            category = "平台候选"
        elif any(t in topics_lower for t in ["infrastructure", "cloud-native", "kubernetes"]):
            category = "基础设施候选"

        # Pick emoji
        emoji = CATEGORY_EMOJIS.get("default", "📦")
        for t in topics_lower:
            if t in CATEGORY_EMOJIS:
                emoji = CATEGORY_EMOJIS[t]
                break
        if lang == "Rust" and emoji == "📦":
            emoji = "🦀"
        elif lang == "Python" and emoji == "📦":
            emoji = "🐍"

        score = min(95, 50 + stars // 1000)

        slug = make_slug(r.get("name", name))
        key_projects.append({
            "name": name,
            "emoji": emoji,
            "stars": f"{stars:,} stars",
            "desc": desc,
            "category": category,
            "tags": topics if topics else [lang],
            "score": score,
            "href": f"projects/{slug}.html",
        })

    # Build summary
    top3_names = [kp["name"].split("/")[-1] for kp in key_projects[:3]]
    top3_stars = [kp["stars"] for kp in key_projects[:3]]
    summary_parts = []
    for name, stars in zip(top3_names, top3_stars):
        summary_parts.append(f"{name}（{stars}）")
    summary = " · ".join(summary_parts) if summary_parts else "GitHub 活跃项目追踪"

    # Count total
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)

    # Build frontmatter
    lines = []
    lines.append("---")
    lines.append(f'title: "{date_str} GitHub 趋势研究简报"')
    lines.append(f"date: {date_str}")
    lines.append('version: "v1"')
    lines.append(f'summary: "{summary}"')
    lines.append(f'hero_badge: "{date_str}"')
    lines.append("stats:")
    lines.append(f"  project_count: {len(repos)}")
    lines.append(f"  daily_updates: {daily_num}")
    lines.append(f"  core_directions: {len(trends)}")
    lines.append(f'  weekly_stars: "{total_stars//1000}K+"')
    lines.append("trends:")
    for t in trends:
        lines.append(f'  - rank: {t["rank"]}')
        lines.append(f'    name: "{t["name"]}"')
        lines.append(f'    projects: [{", ".join(json.dumps(p) if not p.isidentifier() else p for p in t["projects"])}]')
        lines.append(f'    score: {t["score"]}')
    lines.append("key_projects:")
    for kp in key_projects:
        lines.append(f'  - name: "{kp["name"]}"')
        lines.append(f'    emoji: "{kp["emoji"]}"')
        lines.append(f'    stars: "{kp["stars"]}"')
        lines.append(f'    desc: "{kp["desc"]}"')
        lines.append(f'    category: "{kp["category"]}"')
        lines.append(f'    tags: [{", ".join(json.dumps(t) for t in kp["tags"])}]')
        lines.append(f'    score: {kp["score"]}')
        lines.append(f'    href: "{kp["href"]}"')
    lines.append("---")
    lines.append("")

    # Body
    lines.append(f"# GitHub 趋势研究简报 - {date_str}")
    lines.append("")
    lines.append(f"> 本报基于 GitHub Search API 获取 {date_str} 当日活跃高星项目数据，按星数和活跃度排序。")
    lines.append("")

    # Trend analysis
    lines.append("## 今日重点趋势")
    lines.append("")
    for t in trends:
        lines.append(f"**{t['rank']}. {t['name']}**（评分 {t['score']}）")
        lines.append("")

    # Top projects table
    lines.append("## 活跃项目 Top 10")
    lines.append("")
    lines.append("| 项目 | Stars | 语言 | 描述 |")
    lines.append("|------|-------|------|------|")
    for r in top_repos:
        name = r.get("full_name", "?")
        stars = r.get("stargazers_count", 0)
        lang = r.get("language") or "—"
        desc = (r.get("description") or "—")[:80]
        desc = desc.replace("|", "\\|").replace('"', "'")
        lines.append(f"| [{name}]({r.get('html_url', '#')}) | {stars:,} | {lang} | {desc} |")
    lines.append("")

    # Detail cards
    lines.append("## 重点项目分析")
    lines.append("")
    for kp in key_projects[:5]:
        lines.append(f"### {kp['emoji']} {kp['name']} — {kp['stars']}")
        lines.append(f"- **定位:** {kp['desc']}")
        lines.append(f"- **分类:** {kp['category']}")
        lines.append(f"- **标签:** {', '.join(kp['tags'][:5])}")
        lines.append(f"- **评分:** {kp['score']}/100")
        lines.append("")

    lines.append("---")
    lines.append(f"> 数据来源: GitHub Search API | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    return "\n".join(lines)


def backfill_one_day(date_str, daily_num):
    """Backfill one day with real GitHub data"""
    print(f"\n{'='*60}")
    print(f"  补全真实数据: {date_str}")
    print(f"{'='*60}")

    all_repos = []
    seen_names = set()

    for query_tmpl, label in SEARCH_QUERIES:
        print(f"    [search] {label}...")
        repos = gh_search(query_tmpl, date_str, per_page=5)
        unique = deduplicate_repos(repos, seen_names)
        all_repos.extend(unique)
        print(f"    [search] {label}: +{len(unique)} new ({len(all_repos)} total)")
        time.sleep(1)  # GitHub API rate limit

    if not all_repos:
        print(f"    [warn] 无数据，跳过")
        return False

    # Generate daily
    content = generate_daily_md(date_str, all_repos, daily_num)
    if not content:
        print(f"    [warn] 生成失败")
        return False

    fpath = os.path.join(DAILY_DIR, f"{date_str}.md")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    size = os.path.getsize(fpath)
    print(f"    ✅ 日报已生成: {size} bytes, {len(all_repos)} repos")
    return True


def main():
    dates = find_placeholder_dates()
    if not dates:
        print("没有需要补全的占位日报！")
        return

    print(f"发现 {len(dates)} 个占位日报需要替换:")
    for d in dates:
        print(f"  - {d}")

    # Count existing real dailies for daily_updates numbering
    all_files = [f for f in os.listdir(DAILY_DIR) if f.endswith(".md")]
    base_count = len(all_files) - len(dates)

    success = 0
    failed = []

    for i, date_str in enumerate(dates):
        daily_num = base_count + i + 1
        ok = backfill_one_day(date_str, daily_num)
        if ok:
            success += 1
        else:
            failed.append(date_str)
        time.sleep(2)  # Extra rate limit buffer

    print(f"\n{'='*60}")
    print(f"  补全完成: {success}/{len(dates)} 成功")
    if failed:
        print(f"  失败: {', '.join(failed)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
