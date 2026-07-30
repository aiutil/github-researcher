---
title: "vercel/eve"
slug: "eve"
date_added: "2026-06-19"
last_seen_date: "2026-07-31"
category: "平台候选"
emoji: "🌙"
stars: "4,198 stars"
stars_delta: "6/19 1.3K→7/31 4.2K；42天3.2倍增长，Vercel 官方持续投入"
language: "TypeScript"
score: 83
tags: ["agent-framework", "filesystem-first", "vercel", "typescript", "durable-agents", "workflows"]
url: "https://github.com/vercel/eve"
---

# vercel/eve

## 一句话定位
Vercel 出品的 filesystem-first durable agent 框架（TypeScript / Apache-2.0）——把 agent 的核心能力映射为约定的目录结构（instructions / tools / skills / channels / schedules 即文件），"filesystem is the authoring interface"。

## 它解决的问题
定义一个 production-grade agent 时，开发者通常要拼装 prompt、工具、技能、消息通道、定时任务等散落各处的配置。eve 把这些能力统一映射到一个 `agent/` 目录下的文件约定：`instructions.md`（常驻系统提示）、`tools/`（类型化函数）、`skills/`（按需加载的过程）、`channels/`（HTTP/Slack/Discord 消息通道）、`schedules/`（cron 定时任务）。目标用户是希望用可检视、可扩展的文件结构来构建与运维 durable agent 的开发者。

## 为什么值得关注（2026-07-31 更新）
- **官方背书 + 持续增长**：Vercel 出品，42 天从 1.3K 增至 4,198⭐（+3.2×），forks 407，仍在活跃 push（2026-07-30）。
- **filesystem-first 范式**：在今日 "coding agent harness 多极化" 趋势中代表**开发范式层**——与 grok-build（harness 本体）、omnigent（meta-harness 编排层）三线互补。
- **durable agent 定位**：强调持久化与可运维，区别于一次性脚本式 agent。
- **npm 即装即用**：`npx eve@latest init my-agent`，与 JS/TS 生态无缝。

## 热度来源判断
**官方品牌 + 范式红利双驱动。** Vercel 在前端与开发者工具领域的声誉贡献了首发流量；filesystem-first 的设计哲学迎合了"agent 应该可检视、可版本控制、可协作"的真实工程诉求。但 framework 类项目的高 star 不等于高生产采纳——需看真实部署案例。

## 关键技术亮点
1. **目录即能力**：agent 能力以约定文件结构存在（instructions.md / tools/ / skills/ / channels/ / schedules/），项目因此更易检视、扩展、运维。
2. **durable 定位**：面向持久化、可恢复的 agent，而非无状态的一次性调用。
3. **多通道**：channels 支持 HTTP / Slack / Discord，agent 可接入真实消息面。
4. **schedules 原生**：recurring cron jobs 作为一等公民，agent 可被定时驱动。

## 架构启发
eve 的核心 trade-off 是"约定优于配置"：用文件系统约定换取 agent 的可读性与可运维性。这与 omnigent 的"runtime-first 编排"、grok-build 的"harness 本体"形成层次划分——eve 回答"agent 怎么被定义"，omnigent 回答"多个 agent 怎么被编排"，grok-build 回答"一个 agent harness 长什么样"。

## 定位判断
在 Agent 生态中，eve 是 **filesystem-first 的 agent 开发范式**候选。它不试图编排多个外部 agent，而是提供一种用文件结构定义 durable agent 的方法论。若该范式被社区采纳，它将成为 agent 项目的脚手架标准之一。

## 风险 / 局限 / 泡沫点
1. **framework 竞争激烈**：agent 框架赛道拥挤（LangChain/LangGraph、Mastra、Inngest 等），filesystem-first 的差异化能否形成护城河待观察。
2. **生产成熟度待证**：高 star 不等于高采纳，需独立部署案例验证。
3. **TS 单语言**：与 Python 生态的 agent 工具链互操作需额外工程。

## 与同类项目的关系
- **vs omnigent**：eve 是"定义 agent 的开发范式"，omnigent 是"编排多个 agent 的运行时"——互补层次。
- **vs grok-build**：grok-build 是一个具体 harness 本体，eve 是定义 harness/agent 的方法论；eve 可作为定义范式作用于 grok-build 类本体。
- **vs LangChain/LangGraph**：同为 agent 框架，但 eve 强调 filesystem-first 与 durable，LangChain 强调链式组合。

## 是否值得持续跟踪
**是。** filesystem-first 是 agent 开发范式的一条独立路线，且 Vercel 持续投入。重点跟踪：社区采纳的 agent 模板数量、真实生产部署案例、是否被其他 harness 借鉴其目录约定。

## 后续观察点
1. 是否出现被广泛复用的 eve agent 模板与 skills 生态。
2. filesystem-first 约定是否被其他框架（或 grok-build 类 harness）借鉴。
3. 真实生产部署案例与 durability 在长任务中的表现。

---
*首次记录：2026-06-19 · 重大更新：2026-07-31 · 数据来源：GitHub API + 仓库 README*
