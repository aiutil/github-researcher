# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-03.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-03

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 10 | 528 | 6 | 5.8K+ |

**今日核心判断：** sapientinc/PRAXIST 连续 6 日 6675⭐ · CopilotKit/OpenBot 跨 7 日 3891⭐ · duty1g/x64dbg-mcp-server 12 天 1846⭐ · crmne/fastpotify 7 天 +626⭐ 至 2133 · cbrock84/headcount 1105⭐ · Tencent/WeMM-Embedding 1085⭐ · ApodexAI/FrontierAgent 12 天 1389⭐ · N4darae/anti-mage 12 天 1419⭐

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [sapientinc/PRAXIST](projects/praxist.md) | 6675 stars | 基础设施候选 |
| [CopilotKit/OpenBot](projects/openbot.md) | 3891 stars | 平台候选 |
| [duty1g/x64dbg-mcp-server](projects/x64dbg-mcp-server.md) | 1846 stars | 工具型 |
| [crmne/fastpotify](projects/fastpotify.md) | 2133 stars | 生产可用 |
| [cbrock84/headcount](projects/headcount.md) | 1105 stars | 平台候选 |
| [N4darae/anti-mage](projects/anti-mage.md) | 1419 stars | 工具型 |
| [Tencent/WeMM-Embedding](projects/tencent-wemm-embedding.md) | 1085 stars | 基础设施候选 |
| [ApodexAI/FrontierAgent](projects/frontieragent.md) | 1389 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **autonomous-research-system / PRAXIST 稳态第三日（6 天 1451→6675 stars，4.6 倍），增速回升 +555⭐/日，仍是 scientific agent 唯一头部样本** · 相关项目：sapientinc/PRAXIST · 强度：93
2. **mcp-debugging-verticalization / MCP 协议在调试 / 逆向 / 二进制分析方向的纵深（x64dbg-mcp-server 1846⭐；reverify 579⭐；duty1g 同期 246 forks）** · 相关项目：duty1g/x64dbg-mcp-server, 2akouwu/reverify · 强度：86
3. **agent-org-as-product / 「公司化 agent 组织」成为 agent harness 下一形态（cbrock84/headcount 1105⭐，15 部门 / 125 技能，可独立安装）** · 相关项目：cbrock84/headcount, ApodexAI/FrontierAgent · 强度：85
4. **antidetect-detection-security / 反「反检测浏览器」进入 OSS 工具化阶段（N4darae/anti-mage 12 天 1419⭐ / 54 forks，runtime coherence analysis）** · 相关项目：N4darae/anti-mage · 强度：82

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-03](daily/2026-09-03.md) | 10 | 6 |
| [2026-09-02](daily/2026-09-02.md) | 8 | 5 |
| [2026-09-01](daily/2026-09-01.md) | 6 | 5 |
| [2026-08-31](daily/2026-08-31.md) | 6 | 5 |
| [2026-08-30](daily/2026-08-30.md) | 6 | 5 |
| [2026-08-29](daily/2026-08-29.md) | 6 | 5 |
| [2026-08-28](daily/2026-08-28.md) | 6 | 5 |

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
