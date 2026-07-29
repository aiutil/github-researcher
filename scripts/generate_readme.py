#!/usr/bin/env python3
"""
从 daily/ 和 projects/ 数据自动生成 README.zh-CN.md
确保中文 README 与实际数据始终一致。
"""

import os, glob, yaml
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY = os.path.join(BASE, 'daily')
PROJECTS = os.path.join(BASE, 'projects')

def parse_frontmatter(filepath):
    with open(filepath) as f:
        content = f.read()
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        fm = {}
    return fm, parts[2]

def load_daily_summaries():
    """加载所有日报的摘要信息"""
    dailies = []
    for fp in sorted(glob.glob(os.path.join(DAILY, '*.md')), reverse=True):
        fm, _ = parse_frontmatter(fp)
        if fm.get('date'):
            kp = fm.get('key_projects', [])
            dailies.append({
                'date': fm['date'],
                'summary': fm.get('summary', '无摘要'),
                'project_count': len(kp),
                'trends': fm.get('trends', []),
                'key_projects': kp,
            })
    return dailies

def load_projects():
    """加载所有项目档案"""
    projects = []
    for fp in sorted(glob.glob(os.path.join(PROJECTS, '*.md'))):
        fm, body = parse_frontmatter(fp)
        if fm:
            # Extract one-line description from body: "## 一句话定位" or first paragraph after title
            desc = ''
            import re
            m = re.search(r'## 一句话定位\s*\n(.+)', body)
            if m:
                desc = m.group(1).strip()[:80]
            if not desc:
                m = re.search(r'# .+\s*\n\s*(.+)', body)
                if m:
                    desc = m.group(1).strip()[:80]
            projects.append({
                'name': fm.get('title', os.path.basename(fp).replace('.md', '')),
                'file': os.path.basename(fp),
                'category': fm.get('category', '未分类'),
                'score': fm.get('score', 0),
                'desc': desc or fm.get('description', ''),
                'stars': fm.get('stars', ''),
                'status': fm.get('tracking_status', '持续跟踪'),
            })
    return projects

def generate_readme():
    dailies = load_daily_summaries()
    projects = load_projects()
    
    if not dailies:
        print("No daily data found")
        return

    latest = dailies[0]
    recent_7 = dailies[:7]

    # Latest summary section
    latest_kp = latest['key_projects'][:3]
    kp_bullets = '\n'.join(
        f"- **{p.get('name', '?')}**（{p.get('stars', '?')}）：{p.get('desc', '')}"
        for p in latest_kp
    )

    trends_text = latest.get('summary', '')

    daily_links = '\n'.join(
        f"**→ [查看 {d['date']} 完整简报](daily/{d['date']}.md)**"
        for d in recent_7[:4]
    )

    # 7-day table
    table_rows = '\n'.join(
        f"| [{d['date']}](daily/{d['date']}.md) | {d['summary'][:40]} | {d['project_count']} 个深度分析 |"
        for d in recent_7
    )

    # Trend directions (from latest)
    trend_items = latest.get('trends', [])[:5]
    trend_list = '\n'.join(
        f"{i+1}. **{t.get('name', '?')}**：相关项目 {', '.join(t.get('projects', [])[:3])}。"
        for i, t in enumerate(trend_items)
    )

    # Top projects table (top 10 by score)
    sorted_projects = sorted(projects, key=lambda p: p.get('score', 0), reverse=True)[:10]
    project_rows = '\n'.join(
        f"| [{p['name']}](projects/{p['file']}) | {p['category']} | {p.get('desc', '')[:40]} | {p.get('status', '持续跟踪')} |"
        for p in sorted_projects
    )

    readme = f"""# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（{latest['date']}）

**{trends_text}**

今日热榜新信号：
{kp_bullets}

{daily_links}

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
{table_rows}

---

## 当前最值得关注的趋势

{trend_list}

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
{project_rows}

---

## 数据统计

- 📊 项目档案：{len(projects)} 个
- 📅 日报总数：{len(dailies)} 期
- 🔄 最近更新：{latest['date']}

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
"""
    
    readme_path = os.path.join(BASE, 'README.zh-CN.md')
    with open(readme_path, 'w') as f:
        f.write(readme)
    print(f"README.zh-CN.md generated: {latest['date']}, {len(dailies)} dailies, {len(projects)} projects")

if __name__ == '__main__':
    generate_readme()
