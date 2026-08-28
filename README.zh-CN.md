# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-08-29.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-08-29

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 6 | 509 | 5 | 2.7K+ |

**今日核心判断：** sapientinc/PRAXIST（1451 stars）· crmne/fastpotify（388 stars）· Nanako0129/sepia（245 stars）· XiaoDuoYa/codex-with-chatgpt（239 stars）· acryldev/acryl（219 stars）· buaacyw/code-world-model（205 stars）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [sapientinc/PRAXIST](projects/praxist.md) | 1451 stars | 基础设施候选 |
| [crmne/fastpotify](projects/fastpotify.md) | 388 stars | 生产可用 |
| [Nanako0129/sepia](projects/sepia.md) | 245 stars | 工具型 |
| [XiaoDuoYa/codex-with-chatgpt](projects/codex-with-chatgpt.md) | 239 stars | 工具型 |
| [acryldev/acryl](projects/acryl.md) | 219 stars | 平台候选 |
| [buaacyw/code-world-model](projects/code-world-model.md) | 205 stars | 基础设施候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **autonomous-research / 可测量的计算机可执行研究系统正式开源（arXiv + PyPI 双发）** · 相关项目：sapientinc/PRAXIST · 强度：94
2. **native-spotify-client / Rust + egui + librespot 跨平台原生 Spotify 客户端替代** · 相关项目：crmne/fastpotify · 强度：86
3. **humanizer-skill / 从表面润色升级到叙事架构层的去 AI 化写作 skill** · 相关项目：Nanako0129/sepia · 强度：86
4. **harness-economy / ChatGPT 订阅 + Codex Harness 的 MCP 只读桥接** · 相关项目：XiaoDuoYa/codex-with-chatgpt · 强度：84

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-08-29](daily/2026-08-29.md) | 6 | 5 |
| [2026-08-28](daily/2026-08-28.md) | 6 | 5 |
| [2026-08-27](daily/2026-08-27.md) | 6 | 5 |
| [2026-08-26](daily/2026-08-26.md) | 6 | 5 |
| [2026-08-25](daily/2026-08-25.md) | 6 | 5 |
| [2026-08-24](daily/2026-08-24.md) | 6 | 5 |
| [2026-08-23](daily/2026-08-23.md) | 6 | 5 |

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
