# 日报 Frontmatter 规范

每个 daily MD 必须包含合法的 YAML frontmatter。

## 必填字段

```yaml
---
title: "YYYY-MM-DD GitHub 趋势研究简报"
date: YYYY-MM-DD
version: "v1"
summary: "核心主题1 · 核心主题2 · 核心主题3"
hero_badge: "YYYY-MM-DD"
stats:
  project_count: N
  daily_updates: M
  core_directions: K
  weekly_stars: "XXk+"
trends:
  - rank: 1
    name: "趋势名称"
    projects: ["项目1", "项目2"]
    score: 70
key_projects:
  - name: "项目slug名"
    emoji: "🚀"
    stars: "N stars"
    desc: "一句话描述"
    category: "分类"
    tags: ["标签"]
    score: 85
    href: "projects/项目名.html"
---
```

## 字段说明

| 字段 | 用途 | 要求 |
|------|------|------|
| `summary` | 首页核心主题、日报索引、趋势页摘要 | 精炼，3个主题用 · 分隔 |
| `trends` | 趋势页数据源 | ≥ 3 个趋势条目 |
| `key_projects` | 项目卡片、趋势页项目区 | ≥ 2 个项目，name 必须与 projects/ 文件名对应 |
| `stats.project_count` | 当天分析项目数 | 不要写死为总数 |
| `stats.weekly_stars` | 首页展示 | 估算值即可 |

## 质量底线

- summary 长度 > 10 字符
- trends ≥ 3 条
- key_projects ≥ 2 个
- 每个 key_project 的 name 必须有对应的 projects/*.md
