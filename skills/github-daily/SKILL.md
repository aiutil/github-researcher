---
name: github-daily
description: github-researcher 每日趋势研究流程。每次定时任务触发时使用。
---

# GitHub Researcher 每日研究流程

本 Skill 定义 github-researcher 子代理每次定时任务的**完整执行流程**。

## 核心原则

1. **不允许跳过任何 Phase**
2. **validate.py 是硬门槛** — 未通过不允许 push
3. **generate_pages.py 每次必跑** — 修改任何 MD 后必须重新生成 HTML
4. **项目档案不可遗漏** — key_projects 必须全部生成 profile
5. **禁止嵌套 `<a>` 标签** — 卡片外层必须用 `<div>` 而非 `<a>`，否则内部 GitHub 链接会变形（HTML 规范不允许 `<a>` 嵌套 `<a>`）

---

## Phase 1: 健康检查（每次必做）

运行验证脚本：

```bash
python3 skills/github-daily/scripts/validate.py
```

- `pass: true` → 进入 Phase 3
- `pass: false` → 记录 errors 和 gaps，进入 Phase 2

## Phase 2: 补齐缺口

根据 validate.py 的 `gaps` 列表逐项修复：

| 缺口类型 | 修复方式 |
|----------|----------|
| `missing_project_profile` | 按 references/project-profile.md 模板生成 |
| `missing_daily_html` | 运行 `python3 docs/generate_pages.py` |
| `missing_project_html` | 同上 |
| frontmatter 缺字段 | 补充必填字段（title, date, summary, trends, key_projects） |
| trend-index 过时 | 补充缺失日期的条目 |
| daily-report.md 过时 | 重新生成包含所有日期的核心主题索引 |

补齐后**重新运行 validate.py**，直到 `pass: true`。

## Phase 3: 今日研究

### 3.1 数据采集
使用 web_search 搜索以下来源：
- GitHub Trending（全球 + 各语言）
- 开源社区热门讨论
- 前一日趋势的延续性追踪

### 3.2 生成日报 MD

创建 `daily/YYYY-MM-DD.md`，必须包含合法 YAML frontmatter：

```yaml
---
title: "YYYY-MM-DD GitHub 趋势研究简报"
date: YYYY-MM-DD
version: "v1"
summary: "核心主题1 · 核心主题2 · 核心主题3"  # ← 这就是首页的核心主题
hero_badge: "YYYY-MM-DD"
stats:
  project_count: N          # 当天分析的项目数
  daily_updates: M          # 累计日报数
  core_directions: K        # 核心方向数
  weekly_stars: "XXk+"      # 本周Star增速
trends:
  - rank: 1
    name: "趋势名称"
    projects: ["项目1", "项目2"]
    score: 70
  # ... 至少 3 个趋势
key_projects:
  - name: "项目名"
    emoji: "🚀"
    stars: "N stars"
    desc: "一句话描述"
    category: "分类"
    tags: ["标签"]
    score: 85
    href: "projects/项目名.html"
---
```

**重要：`summary` 字段是首页和日报索引页的核心主题，必须精炼且有信息量。**

### 3.3 正文结构

按已有日报格式（参考 daily/2026-04-08.md 的正文风格）：
- 今日重点趋势（按排名展开）
- 最值得关注的方向
- 重点项目深度分析（top 3）
- 风险与机遇
- 重点项目档案

## Phase 4: 项目档案生成（不可跳过）

**当天 key_projects 中的每个项目**都必须有 `projects/{slug}.md`。

### 新项目

按 references/project-profile.md 模板生成完整档案，至少包含：
- frontmatter（title, slug, date_added, category, emoji, stars, score, tags, url）
- 一句话定位
- 解决的问题
- 为什么值得关注
- 热度来源判断
- 关键技术亮点
- 架构启发
- 定位判断
- 风险/局限/泡沫点
- 与同类项目的关系
- 是否值得持续跟踪
- 后续观察点

### 已有项目

更新档案中的：
- stars 数（如变化显著）
- 添加"最近动态"记录

## Phase 5: 级联同步（不可遗漏）

必须**逐一执行**以下步骤：

### 5.1 更新趋势指数
编辑 `indexes/trend-index.md`：
- 添加今日新增项目表格
- 更新持续跟踪项目状态
- 记录排名变化

### 5.2 更新 daily-report.md
编辑 `daily-report.md`：
- 在文件开头添加今日核心主题
- 保持按日期倒序排列

### 5.3 更新 README.zh-CN.md
```bash
python3 scripts/generate_readme.py
```
这会从 daily/ 和 projects/ 数据自动生成 README.zh-CN.md，确保中文入口与实际数据同步。英文 README.md 保持稳定的项目说明。

### 5.4 运行 HTML 生成器
```bash
python3 docs/generate_pages.py
```
这会重新生成所有 HTML（index.html、daily.html、trends.html、projects.html、各项目页）。

### 5.5 验证生成结果
检查生成的文件非空：
```bash
wc -c README.zh-CN.md docs/index.html docs/daily.html docs/trends.html docs/projects.html
```

## Phase 6: 最终验证

再次运行 validate.py：

```bash
python3 skills/github-daily/scripts/validate.py
```

- **通过** → git push
- **未通过** → 回到 Phase 2 修复，最多重试 2 次
- 仍不通过 → **不 push**，输出错误报告

## Git 操作

```bash
git add -A
git commit -m "daily: YYYY-MM-DD 趋势简报 + N个项目档案"
git push origin main
```

push 失败时重试 3 次。仍失败则保留本地变更，在报告中说明。

## 输出格式（每次任务结尾必须输出）

```
## 执行报告

### validate 结果
- Phase 1: [通过/失败 - 错误数]
- Phase 2: [无需修复/已修复N项]
- Phase 6: [通过/失败]

### 今日研究
- 日期: YYYY-MM-DD
- 分析项目数: N
- 新增项目档案: [列表]
- 更新项目档案: [列表]

### 关键发现
- [今日最重要的1-2个趋势判断]

### Git 状态
- commit: [hash]
- push: [成功/失败]
```
