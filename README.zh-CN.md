# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-06.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-06

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 8 | 539 | 6 | 11K+ |

**今日核心判断：** mattpocock/skills 2666⭐/day · DietrichGebert/ponytail 2813⭐/day · affaan-m/ECC 1325⭐/day · blader/humanizer 988⭐/day · cathrynlavery/diagram-design 852⭐/day · sgl-project/sglang 862⭐/day · magnitudedev/magnitude 686⭐/day · NousResearch/hermes-agent 573⭐/day · anthropics/skills 472⭐/day · humanlayer/skills 408⭐/day

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [mattpocock/skills](projects/skills.md) | 252,441 stars (+2,666/day) | 平台候选 |
| [DietrichGebert/ponytail](projects/ponytail.md) | 127,831 stars (+2,813/day) | 工具型 |
| [affaan-m/ECC](projects/ecc.md) | 249,777 stars (+1,325/day) | 平台候选 |
| [blader/humanizer](projects/humanizer.md) | 43,416 stars (+988/day) | 工具型 |
| [cathrynlavery/diagram-design](projects/diagram-design.md) | 31,639 stars (+852/day) | 工具型 |
| [magnitudedev/magnitude](projects/magnitude.md) | 3,159 stars (+686/day) | 工具型 |
| [NousResearch/hermes-agent](projects/hermes-agent.md) | 241,962 stars (+573/day) | 平台候选 |
| [anthropics/skills](projects/skills.md) | 174,531 stars (+472/day) | 平台候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **agent-skills-content-explosion / Agent Skills 内容生态全面爆发——9 个 Skill 类项目同时进入 daily trending 总榜，mattpocock 2666⭐/day 与 ponytail 2813⭐/day 双破 2500+ 单日** · 相关项目：mattpocock/skills, DietrichGebert/ponytail, affaan-m/ECC, blader/humanizer, cathrynlavery/diagram-design, anthropics/skills, humanlayer/skills, WorldFlowAI/everything-claude-code · 强度：96
2. **agent-harness-perf-optimization / Agent Harness 性能优化作为独立赛道成型——affaan-m/ECC 自定位"agent harness operating system"1325⭐/day 是赛道头部** · 相关项目：affaan-m/ECC, NousResearch/hermes-agent · 强度：88
3. **ai-writing-deai-skill / "去 AI 化"成为 Agent Skill 的高频用例——blader/humanizer 988⭐/day 验证 Skill 分发模式** · 相关项目：blader/humanizer · 强度：84
4. **design-system-skills / 视觉设计 / 图表设计 Agent Skill 化——cathrynlavery/diagram-design 852⭐/day（38 种编辑级图表模板）** · 相关项目：cathrynlavery/diagram-design · 强度：80

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-06](daily/2026-09-06.md) | 8 | 6 |
| [2026-09-05](daily/2026-09-05.md) | 10 | 7 |
| [2026-09-03](daily/2026-09-03.md) | 10 | 6 |
| [2026-09-02](daily/2026-09-02.md) | 8 | 5 |
| [2026-09-01](daily/2026-09-01.md) | 6 | 5 |
| [2026-08-31](daily/2026-08-31.md) | 6 | 5 |
| [2026-08-30](daily/2026-08-30.md) | 6 | 5 |

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
