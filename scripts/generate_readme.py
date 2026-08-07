#!/usr/bin/env python3
"""Generate bilingual daily READMEs and a GitHub-renderable activity chart."""

from __future__ import annotations

import glob
import html
import os
import re
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily"
PROJECTS = ROOT / "projects"
CHART = ROOT / "docs" / "images" / "research-activity.svg"


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        metadata = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        metadata = {}
    return metadata, parts[2]


def normalize_date(value) -> str:
    if isinstance(value, date):
        return value.isoformat()
    return str(value or "")


def load_dailies() -> list[dict]:
    dailies = []
    for path in sorted(DAILY.glob("*.md")):
        metadata, _ = parse_frontmatter(path)
        if not metadata.get("date"):
            continue
        key_projects = metadata.get("key_projects") or []
        stats = metadata.get("stats") or {}
        dailies.append(
            {
                "date": normalize_date(metadata["date"]),
                "summary": str(metadata.get("summary") or ""),
                "project_count": int(stats.get("project_count") or len(key_projects)),
                "weekly_stars": str(stats.get("weekly_stars") or "-"),
                "core_directions": int(stats.get("core_directions") or len(metadata.get("trends") or [])),
                "trends": metadata.get("trends") or [],
                "key_projects": key_projects,
            }
        )
    return dailies


def load_projects() -> list[dict]:
    projects = []
    for path in sorted(PROJECTS.glob("*.md")):
        metadata, body = parse_frontmatter(path)
        if not metadata:
            continue
        match = re.search(r"## 一句话定位\s*\n(.+)", body)
        description = match.group(1).strip() if match else str(metadata.get("description") or "")
        projects.append(
            {
                "name": str(metadata.get("title") or path.stem),
                "file": path.name,
                "category": str(metadata.get("category") or "Unclassified"),
                "score": int(metadata.get("score") or 0),
                "stars": str(metadata.get("stars") or "-"),
                "status": str(metadata.get("tracking_status") or "持续跟踪"),
                "description": description,
                "date_added": normalize_date(metadata.get("date_added")),
            }
        )
    return projects


def archive_count(projects: list[dict], day: str) -> int:
    return sum(1 for project in projects if project["date_added"] and project["date_added"] <= day)


def activity_rows(dailies: list[dict], projects: list[dict], limit: int = 30) -> list[dict]:
    return [
        {**daily, "archive_count": archive_count(projects, daily["date"])}
        for daily in dailies[-limit:]
    ]


def build_svg(rows: list[dict]) -> str:
    width, height = 1200, 420
    left, top, chart_width, chart_height = 76, 78, 1048, 238
    max_daily = max((row["project_count"] for row in rows), default=1)
    max_archive = max((row["archive_count"] for row in rows), default=1)
    step = chart_width / max(len(rows), 1)
    bar_width = max(8, min(25, step * 0.6))
    points = []
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">GitHub Researcher daily activity</title>',
        '<desc id="desc">Repositories analyzed per day and cumulative research archive over the latest thirty reports.</desc>',
        '<rect width="1200" height="420" rx="20" fill="#f8fafc"/>',
        '<text x="56" y="42" font-family="Inter,system-ui,sans-serif" font-size="22" font-weight="700" fill="#111827">30-day research activity</text>',
        '<text x="1144" y="42" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="14" fill="#64748b">daily analysis + cumulative archive</text>',
    ]
    for tick in range(5):
        daily_value = round(max_daily * tick / 4)
        archive_value = round(max_archive * tick / 4)
        y = top + chart_height - chart_height * tick / 4
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_width}" y2="{y:.1f}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{left - 12}" y="{y + 5:.1f}" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="12" fill="#64748b">{daily_value}</text>')
        parts.append(f'<text x="{left + chart_width + 12}" y="{y + 5:.1f}" font-family="Inter,system-ui,sans-serif" font-size="12" fill="#64748b">{archive_value}</text>')
    for index, row in enumerate(rows):
        x = left + step * index + (step - bar_width) / 2
        bar_height = chart_height * row["project_count"] / max_daily
        y = top + chart_height - bar_height
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{bar_height:.1f}" rx="4" fill="#2563eb"><title>{html.escape(row["date"])} · {row["project_count"]} repositories analyzed</title></rect>')
        line_x = x + bar_width / 2
        line_y = top + chart_height - chart_height * row["archive_count"] / max_archive
        points.append(f"{line_x:.1f},{line_y:.1f}")
        if index in {0, len(rows) - 1} or index % 5 == 0:
            parts.append(f'<text x="{line_x:.1f}" y="{top + chart_height + 24}" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="11" fill="#64748b">{html.escape(row["date"][5:])}</text>')
    if points:
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="#d97706" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        for point in points[-1:]:
            x, y = point.split(",")
            parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#d97706" stroke="#fff" stroke-width="2"/>')
    latest = rows[-1] if rows else {"date": "n/a", "project_count": 0, "archive_count": 0}
    parts.extend(
        [
            '<rect x="76" y="365" width="12" height="12" rx="3" fill="#2563eb"/>',
            '<text x="96" y="376" font-family="Inter,system-ui,sans-serif" font-size="13" fill="#334155">Repositories analyzed / day</text>',
            '<line x1="300" y1="371" x2="328" y2="371" stroke="#d97706" stroke-width="3"/>',
            '<text x="338" y="376" font-family="Inter,system-ui,sans-serif" font-size="13" fill="#334155">Cumulative research archive</text>',
            f'<text x="1144" y="376" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="13" font-weight="600" fill="#111827">Latest: {html.escape(latest["date"])} · {latest["project_count"]} analyzed · {latest["archive_count"]} archived</text>',
            "</svg>",
        ]
    )
    return "\n".join(parts) + "\n"


def recent_table(dailies: list[dict], language: str) -> str:
    if language == "en":
        lines = ["| Date | Repositories analyzed | Core directions |", "| --- | ---: | ---: |"]
    else:
        lines = ["| 日期 | 深度分析项目 | 核心趋势方向 |", "| --- | ---: | ---: |"]
    for daily in reversed(dailies[-7:]):
        lines.append(f'| [{daily["date"]}](daily/{daily["date"]}.md) | {daily["project_count"]} | {daily["core_directions"]} |')
    return "\n".join(lines)


def project_link(project: dict, index: dict[str, dict]) -> str:
    name = str(project.get("name") or "Unknown")
    matched = index.get(name.lower()) or index.get(name.split("/")[-1].lower())
    return f'[{name}](projects/{matched["file"]})' if matched else name


def latest_projects(latest: dict, projects: list[dict], language: str) -> str:
    index = {}
    for project in projects:
        index[project["name"].lower()] = project
        index[project["name"].split("/")[-1].lower()] = project
    if language == "en":
        lines = ["| Repository | Snapshot | Category |", "| --- | --- | --- |"]
    else:
        lines = ["| 项目 | 当日快照 | 分类 |", "| --- | --- | --- |"]
    for project in latest.get("key_projects", [])[:8]:
        lines.append(f'| {project_link(project, index)} | {project.get("stars", "-")} | {project.get("category", "-")} |')
    return "\n".join(lines)


def trend_list(latest: dict, language: str) -> str:
    rows = []
    for position, trend in enumerate((latest.get("trends") or [])[:4], 1):
        projects = ", ".join(trend.get("projects") or []) or "-"
        if language == "en":
            rows.append(f'{position}. **Signal {position}** · score {trend.get("score", "-")} · repositories: {projects}')
        else:
            rows.append(f'{position}. **{trend.get("name", "待补充")}** · 相关项目：{projects} · 强度：{trend.get("score", "-")}')
    return "\n".join(rows) or ("No trend data yet." if language == "en" else "暂无趋势数据。")


def generate_readmes() -> None:
    dailies = load_dailies()
    projects = load_projects()
    if not dailies:
        raise RuntimeError("No dated daily reports found")
    latest = dailies[-1]
    rows = activity_rows(dailies, projects)
    CHART.parent.mkdir(parents=True, exist_ok=True)
    CHART.write_text(build_svg(rows), encoding="utf-8")

    en = f'''# GitHub Researcher

<h3 align="center">Daily, evidence-linked research on fast-moving open-source projects and developer trends.</h3>

<p align="center">
  More than a ranking table: what changed, why it may matter, how strong the signal is, and what remains unverified.
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="https://github-research.aiutil.com">Live research site</a> ·
  <a href="daily/{latest['date']}.md">Latest report</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="README data checks" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="Daily research" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub Researcher live site](docs/images/readme-overview.png)

## Latest report · {latest['date']}

| Repositories analyzed today | Research archive | Core directions | Weekly star movement |
| ---: | ---: | ---: | ---: |
| {latest['project_count']} | {len(projects)} | {latest['core_directions']} | {latest['weekly_stars']} |

{latest_projects(latest, projects, 'en')}

![Thirty-day GitHub research activity](docs/images/research-activity.svg)

## Current trend signals

{trend_list(latest, 'en')}

The structured source reports are written in Chinese today; the charts, repository snapshots, methodology, and evidence boundaries are bilingual. Follow the [latest report](daily/{latest['date']}.md) for the complete source-linked reasoning record.

## Recent research cadence

{recent_table(dailies, 'en')}

## Why this repository exists

GitHub Trending reveals attention, not durable value. This project records dated repository facts, reads the underlying code and documentation, compares multi-day movement, separates observations from inference, and keeps explicit risks such as unverifiable benchmarks or suspicious star patterns.

## Research workflow

```mermaid
flowchart LR
  A["Collect public repository signals"] --> B["Read code, docs, releases and metadata"]
  B --> C["Compare multi-day movement"]
  C --> D["Classify value and risk"]
  D --> E["Publish daily report"]
  E --> F["Update project archive and trend ledger"]
```

- `daily/` contains dated research reports with source snapshots.
- `projects/` contains durable project records and later corrections.
- `indexes/` tracks cross-project trends over time.
- `docs/` is the generated public site.
- `scripts/generate_readme.py` regenerates both READMEs and the activity chart from committed data.

## Evidence boundaries

Stars, forks, releases, licenses, languages, and timestamps are treated as observable GitHub facts at collection time. Product quality, architectural significance, market direction, and suspected manipulation are research judgments. Author claims are labeled until independently reproduced; corrections stay in the dated record.

## Generate and verify

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

The scheduled research worker runs in AIUtil's private automation environment. Tokens, private runtime memory, and operator state are not committed.

## Security

Do not add access tokens, private repository content, user-level activity, or unredacted operator memory. Report vulnerabilities privately through [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new).

## License

Apache License 2.0. See [NOTICE](NOTICE).
'''

    zh = f'''# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/{latest['date']}.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · {latest['date']}

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| {latest['project_count']} | {len(projects)} | {latest['core_directions']} | {latest['weekly_stars']} |

**今日核心判断：** {latest['summary']}

{latest_projects(latest, projects, 'zh')}

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

{trend_list(latest, 'zh')}

## 最近 7 期更新量

{recent_table(dailies, 'zh')}

## 为什么做这个项目

GitHub Trending 展示注意力，不等于长期价值。本项目记录带日期的仓库事实，阅读代码、文档和 Release，对比跨日变化，区分事实与推断，并保留 Benchmark 未复现、许可证变化或异常 Star 等风险。

## 研究工作流

```mermaid
flowchart LR
  A["采集公开仓库信号"] --> B["阅读代码、文档、Release 与元数据"]
  B --> C["对比跨日变化"]
  C --> D["判断价值与风险"]
  D --> E["发布日报"]
  E --> F["更新项目档案与趋势账本"]
```

- `daily/`：带来源快照的每日研究报告。
- `projects/`：可持续修订的项目档案。
- `indexes/`：跨项目、跨日期的趋势记录。
- `docs/`：生成后的公开站点。
- `scripts/generate_readme.py`：从已提交数据生成双语 README 和活动图表。

## 证据边界

Star、Fork、Release、许可证、语言与时间戳属于采集时可观察的 GitHub 事实；产品质量、架构意义、市场方向和疑似刷星属于研究判断。作者自述在独立复现前会明确标注，后续修正保留在带日期的记录里。

## 生成与验证

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

定时研究任务运行在 AIUtil 私有自动化环境中，Token、私有运行记忆和运营状态不进入仓库。

## 安全

请勿提交访问令牌、私有仓库内容、用户级活动数据或未经脱敏的运营记忆。安全问题请通过 [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new) 私下报告。

## 开源协议

Apache License 2.0，详见 [NOTICE](NOTICE)。
'''

    (ROOT / "README.md").write_text(en, encoding="utf-8")
    (ROOT / "README.zh-CN.md").write_text(zh, encoding="utf-8")
    print(f"Generated bilingual READMEs for {latest['date']}: {len(dailies)} reports, {len(projects)} project records")


if __name__ == "__main__":
    generate_readmes()
