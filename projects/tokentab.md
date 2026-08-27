---
title: "damejan80/tokentab"
slug: tokentab
date_added: 2026-08-28
last_seen_date: 2026-08-28
category: "工具型"
emoji: "📊"
stars: "211 stars"
stars_delta: "1 天 211⭐（2026-08-27 创建，created 14:16:09Z，pushed 2026-08-27 14:20:23Z，forks 12，size 317 KB）"
language: "Python"
license: "MIT"
score: 82
tags: ["claude-code", "codex", "gemini-cli", "cursor", "token-usage", "cost-tracking", "observability", "ai-coding"]
url: "https://github.com/damejan80/tokentab"
---

# damejan80/tokentab

## 一句话定位
**本地 CLI 读取 Claude Code / Codex / Cursor / Gemini CLI session 日志**——按模型 / 项目 / 日 / 任务类型聚合 token 与成本，**纯本地运行**，不传数据；支持 JSON 输出供 jq 管道处理。

## 它解决的问题
2026 年下半年 AI Coding 团队 / 个人开发者面临"成本不可观测"痛点：**(1) 多 harness 碎片化**——Claude Code / Codex / Cursor / Gemini CLI 各自的 session 日志路径不同，难以统一聚合；**(2) 隐私顾虑**——直接上传 session 日志到第三方服务可能泄漏业务数据；**(3) 成本归因难**——无法按"哪个项目 / 哪种任务 / 哪一天 / 哪个模型"精准归因成本。tokentab 直击这三点：**多 harness 日志读取 + 纯本地运行 + 按多维度聚合**。

## 为什么值得关注（2026-08-28）
- **1 天 211⭐ + 12 forks**：AI Coding 成本可观测赛道的早期代表样本
- **多 harness 完整支持**：Claude Code（`~/.claude/projects/**/*.jsonl`）+ Codex（`~/.codex/sessions/**/rollout-*.jsonl`）+ Gemini CLI（`~/.gemini/tmp/**/session-*.json`）+ Cursor（stub wired but not finished）
- **纯本地运行**：README 自述 "It runs entirely locally: no account, no API key, nothing leaves your machine"
- **多维度聚合**：按 model / project / day / 任务类型聚合 token + cost
- **JSON 输出**：支持 `python cli.py --json | jq .` 脚本管道处理
- **Web dashboard**：README 自述 "python cli.py -web" 启动 Web dashboard
- **MIT 许可**：商用友好

## 热度来源判断
热度来自 **"AI Coding 成本不可观测 × 多 harness 碎片化 × 隐私顾虑"** 的组合：(1) AI Coding 用户对 token / cost 可观测的强需求；(2) Claude Code / Codex / Cursor / Gemini CLI 各自日志路径不同，统一聚合有真实价值；(3) "纯本地运行"满足企业 IT 的合规需求。**主要风险：** Cursor stub 状态影响"四工具齐全"的产品承诺；token 计价精度（是否含上下文缓存折扣 / batch API 折扣）需独立核验；定价表同步机制可靠性待观察；与 Anthropic / OpenAI 官方 dashboard 的竞合关系。

## 关键技术亮点
1. **多 harness 日志读取**：自动扫描 Claude Code / Codex / Gemini CLI session 日志路径（Cursor stub）
2. **纯本地运行**：no account / no API key / nothing leaves your machine
3. **多维度聚合**：按 model / project / day / 任务类型聚合 token + cost
4. **CLI + Web dashboard 双形态**：`python cli.py`（CLI）+ `python cli.py -web`（Web）
5. **JSON 输出**：`--json | jq .` 脚本管道处理
6. **时间窗口查询**：`--from 2026-06-01 --to 2026-06-15` 特定窗口
7. **MIT 许可**：商用友好

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Python CLI + Web dashboard，本地读取 session 日志（jsonl / json）并聚合，不传任何数据 | 仅基于 README 的"reads the session logs ... adds up token usage and cost"；具体日志解析逻辑、token 计价表、Cursor stub 完成时间表、JSON schema 稳定性均未在档案中量化 |
| 主路径 | 扫描 Claude Code/Codex/Gemini CLI session 日志 → 解析每条会话的 token / cost → 按 model/project/day/任务类型聚合 → CLI 输出或 Web dashboard 显示 | 主路径来自 README 的"broken down by model, by project, by day, and by the kind of work"；具体"任务类型"的分类逻辑（read code / write code / run command / other）、token 计价表更新机制、上下文缓存折扣处理均待核验 |
| 关键权衡 | 多 harness 覆盖 vs 单 harness 深度 vs 纯本地 vs 计价精度 vs 官方 dashboard 竞合 vs Cursor stub 状态 | 档案明示多 harness + 本地 + JSON 输出；具体 Cursor stub 完成时间、token 计价表同步机制、官方 dashboard 兼容路径均待核验 |
| 最小 PoC | 用真实一周 Claude Code session → 跑 tokentab 验证 token 聚合准确性 → 对比 Anthropic 官方 dashboard 的 token 数 → 验证 `--json | jq .` 管道处理 | PoC 范围由"先单 harness、可对照、可管道"原则推导；具体聚合准确度、与官方 dashboard 差异、JSON schema 稳定性待核验 |

## 架构启发
tokentab 的核心启发是 **"AI Coding 成本可观测产品化"的早期代表样本**——延续 8-25..8-27 的"AI Coding 项目复盘"判断，但今日具体到"成本 dashboard"。**这意味着 AI Coding 已从"开发尝鲜"进入"团队成本管理"阶段**——个人开发者关心"花了多少钱"，团队负责人关心"哪个项目花得最多"。**更深层的启发是：** "纯本地运行 + 多 harness 支持 + JSON 输出" 三个特性的组合让 tokentab 既可个人用（隐私优先），也可团队用（脚本管道）。**对 AI Coding 工具厂商：** Claude Code / Codex / Gemini CLI 是否会官方化"成本 dashboard"是观察点。**对团队负责人：** 12 月内应评估部署 tokentab 等成本可观测工具控制 AI Coding 预算。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Logs[本地 session 日志]
  Logs --> CC[Claude Code<br/>~/.claude/projects/**/*.jsonl]
  Logs --> CX[Codex<br/>~/.codex/sessions/**/rollout-*.jsonl]
  Logs --> GC[Gemini CLI<br/>~/.gemini/tmp/**/session-*.json]
  Logs -.stub.-> CUR[Cursor<br/>wired but not finished]
  CC --> Parser[日志解析<br/>token + cost]
  CX --> Parser
  GC --> Parser
  Parser --> Agg[按多维度聚合<br/>model / project / day / 任务类型]
  Agg --> CLI[CLI 输出<br/>默认 + --json | jq .]
  Agg --> Web[Web dashboard<br/>python cli.py -web]
  Agg -.风险.-> Pricing[token 计价表<br/>同步机制待核验]
  Agg -.风险.-> Cache[上下文缓存折扣<br/>是否计入待核验]
  Web -.风险.-> Official[与 Anthropic/OpenAI 官方<br/>dashboard 兼容性]
  CLI -.纯本地.-> Privacy[数据不出本地<br/>no account / no API key]
```

## 定位判断
**工具型项目（AI Coding cost observability CLI）。** tokentab 不做云服务，不做商业 SaaS，只做"本地多 harness token-cost CLI + Web dashboard"——这是工具型定位。**核心竞争壁垒：** 多 harness 完整支持 + 纯本地运行 + 多维度聚合 + JSON 输出 + MIT 许可。**主要风险：** Cursor stub 状态影响"四工具齐全"承诺；token 计价精度（上下文缓存折扣 / batch API 折扣）；定价表同步机制可靠性；与 Anthropic / OpenAI 官方 dashboard 竞合关系。

## 风险 / 局限 / 泡沫点
- **Cursor stub 状态**：README 明示 "Cursor (stub - see below)"——四工具齐全的产品承诺待兑现
- **token 计价精度**：是否含上下文缓存折扣 / batch API 折扣 / 阶梯定价，未在 README 中明示
- **定价表同步机制**：Anthropic / OpenAI / Google 定价更新后的同步延迟
- **1 天新项目**：维护持续性待观察
- **任务类型分类逻辑**："the kind of work each session was doing" 的具体分类方法（read code / write code / run command / other）未明示
- **JSON schema 稳定性**：未来版本兼容性问题

## 与同类项目的关系
- **vs Anthropic Usage Dashboard / OpenAI Usage**：官方 dashboard，tokentab 是多 harness + 本地 + 开源
- **vs LangSmith / Langfuse**：商业 LLM observability 平台，tokentab 是 CLI 形态 + 本地 + 开源
- **vs Helicone / Portkey**：商业 LLM observability，tokentab 是本地 + 开源
- **vs CCUsage / ccusage（其他 token 跟踪 CLI）**：同类项目，tokentab 覆盖更多 harness（Claude Code / Codex / Cursor / Gemini CLI）
- **vs 8-25 itshen/source-reading-methodology**：同样是 AI Coding 工具，itshen 侧重方法论，tokentab 侧重成本

## 是否值得持续跟踪
**值得跟踪（AI Coding 成本可观测的早期代表样本）。** tokentab 1 天 211⭐ 体现"多 harness + 本地 + 开源"AI Coding 成本可观测的市场需求，**多 harness 完整支持 + 纯本地 + JSON 输出三特性组合是显著加分项**。**对 AI Coding 个人用户：** 12 月内可安装 tokentab 监控自己的 token / cost。**对 AI Coding 团队负责人：** 12 月内应评估部署 tokentab 等成本可观测工具控制 AI Coding 预算。建议关注：(1) Cursor stub 是否补齐；(2) token 计价表同步机制；(3) 任务类型分类逻辑；(4) 与 Anthropic / OpenAI 官方 dashboard 兼容性。

## 后续观察点
- Cursor stub 是否补齐（决定四工具齐全承诺）
- token 计价表同步机制（上下文缓存折扣 / batch API 折扣）
- 任务类型分类逻辑（如何定义"the kind of work each session was doing"）
- 与 Anthropic / OpenAI 官方 dashboard 兼容性
- 团队部署可行性（多用户 / 集中 dashboard）
- 1 天新项目维护持续性

---
> 数据来源: GitHub API (2026-08-28) | Stars: 211 | Forks: 12 | License: MIT | 语言: Python | 创建: 2026-08-27 | 数据截至 2026-08-28 06:00 UTC