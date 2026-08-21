---
title: "vercel/eve"
slug: "vercel-eve"
date_added: "2026-06-19"
category: "平台候选"
emoji: "🌙"
stars: "3,360 stars"
stars_delta: "24天3.4K，日均140+（趋稳）"
language: "TypeScript"
score: 85
tags: ["agent-framework", "filesystem-first", "vercel", "typescript"]
url: "https://github.com/vercel/eve"
---

# Vercel Eve

## 一句话定位
Vercel 出品的 filesystem-first AI Agent 框架——agent 的能力（tools/skills/channels/schedules）映射到约定目录结构，文件系统就是 agent 的开发界面。

## 它解决的问题
构建 AI Agent 通常需要学习框架特定的 DSL 或配置格式。eve 的方案是：你不需要学框架，只需要按目录约定放文件——`tools/` 是工具，`skills/` 是技能，`channels/` 是消息通道，`schedules/` 是定时任务。

## 最近动态（2026-07-10）
- Star 数从 2,526（6-19）增长到 3,360（7-10），21 天增 834 Star
- 日均增速从初期 280+ 回落到 ~40/天——从爆发期进入稳步期
- Issues 增长到 223 个，社区活跃但可能暴露出早期质量问题
- 持续活跃推送（pushed_at: 2026-07-09），开发节奏健康
- 核心判断不变：filesystem-first 是 Agent 开发的优雅范式，但需要看生态是否跟进

## 为什么值得关注（2026-06-19）
- Vercel 出品，品牌信任 + npm 生态 + Vercel 部署链路
- 3 天 1,327 stars，开发者社区关注度高
- `npx eve@latest init` 一键创建 agent 项目，DX 极佳
- 文档内置在 npm 包中（`node_modules/eve/docs`），Coding Agent 可直接读取

## 热度来源判断
Vercel 品牌效应 + filesystem-first 理念优雅 + TypeScript 开发者基数大。热度有真实需求支撑，但也包含 Vercel 粉丝效应。

## 关键技术亮点亮点
1. **Filesystem as API** — agent.ts（配置）、instructions.md（系统提示）、tools/（函数）、skills/（按需加载）、channels/（消息）、schedules/（定时）
2. **Skills 按需加载** — 不是一次性灌入所有 context，而是根据需要加载 skill
3. **Channels 抽象** — HTTP、Slack、Discord 消息通道统一管理
4. **内嵌文档** — npm 包包含完整文档，Coding Agent 无需联网查文档

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | eve 是位于"入口渠道 / 模型供应商 / 工具与数据源"之间的 TypeScript Agent 编排框架，通过文件系统目录约定承载能力定义；上层边界含 HTTP、Slack、Discord，下层边界为模型与 typed 函数工具。 | 基于档案明示的 channels（HTTP/Slack/Discord）与 tools/（typed 函数）；未涉及具体鉴权、网络协议与传输细节。 |
| 主路径 | 请求经 channels 入口进入，由 agent.ts（模型与运行时配置）驱动编排，按需加载 skills/markdown 提示与 tools/，结果回写到会话或文件系统状态；schedules/ 提供 cron 驱动的旁路触发。 | 流程节点均来自档案目录约定与亮点描述；调度执行细节、模型协议与持久化介质未在档案中给出，需源码核验。 |
| 关键权衡 | "约定优于配置 + 内嵌文档"的 DX 收益，对照 Vercel 基础设施耦合与 TypeScript 单一语言锁定；扩展速度与权限边界、可观测性、供应商耦合尚未在档案中量化。 | 风险点仅以条目形式列出（TypeScript 限定、Vercel 锁定、78 forks/33 issues），无具体性能、可观测或成本数据。 |
| 最小 PoC | 用 `npx eve@latest init` 创建一个最小 agent，配置 agent.ts 指定单一模型、tools/ 暴露一个只读 typed 函数、channels/ 启用 HTTP 入口；先在最小权限与本地日志下跑通"HTTP 入站 → 工具调用 → 文本回写"，再评估扩展到 Slack/Discord 与 schedules/。 | init 命令、HTTP channel、typed tools、schedules/ 均来自档案明示；具体模型 SDK、日志格式、部署形态未在档案中确认，属"待核验"。 |

## 架构启发
eve 的设计哲学是 **convention over configuration** 应用于 Agent 开发。这与 Next.js 的 app/ 目录约定一脉相承，Vercel 在把这个模式复制到 Agent 领域。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    subgraph Entry["入口边界（外部）"]
        HTTP["HTTP"]
        Slack["Slack"]
        Discord["Discord"]
        Cron["schedules/（cron 触发）"]
    end
    subgraph Eve["eve Agent（filesystem-first）"]
        Agent["agent.ts<br/>模型 + 运行时配置"]
        Instr["instructions.md<br/>常驻系统提示"]
        Skills["skills/<br/>按需加载（待核验：加载协议）"]
        Tools["tools/<br/>typed 函数"]
        State["文件系统状态 / 会话回写（待核验：持久化介质）"]
    end
    subgraph Backend["下游边界（外部）"]
        Model["模型供应商（待核验：具体 SDK）"]
        Data["外部数据源（待核验：来源清单）"]
    end
    HTTP --> Agent
    Slack --> Agent
    Discord --> Agent
    Cron --> Agent
    Agent --> Instr
    Agent --> Skills
    Agent --> Tools
    Tools --> Data
    Agent --> Model
    Agent --> State
```

## 定位判断
eve 是 **Agent 开发框架层的 Next.js**——通过约定优于配置大幅降低 Agent 开发门槛。如果 Vercel 部署链路打通，它可能成为 TypeScript 开发者构建 Agent 的事实标准。

## 风险 / 局限 / 泡沫点
1. **TypeScript 限定** — Python/Go 开发者被排除在外
2. **Vercel 锁定风险** — channels/schedules 依赖 Vercel 基础设施才能发挥最大价值
3. **早期阶段** — 78 forks，33 issues，生态尚小
4. **与 LangChain/LangGraph 竞争** — 已有大型框架占据开发者心智

## 与同类项目的关系
- **vs LangChain/LangGraph** — LangChain 是 Python-first + 链式组合，eve 是 TypeScript-first + 目录约定
- **vs omnigent** — omnigent 编排已有 agent，eve 从零构建 agent
- **vs Claude Code skills** — Claude Code skills 是单个 Skill 文件，eve 是完整框架

## 是否值得持续跟踪
**是。** Vercel 的分发能力 + filesystem-first 的优雅设计 = TypeScript Agent 开发的重要变量。

## 后续观察点
1. npm 下载量趋势
2. 社区贡献的 tools/skills/channels 数量
3. 是否与 Vercel 部署链路深度集成
4. 是否出现基于 eve 构建的生产 Agent

---
*首次记录：2026-06-19 · 更新：2026-07-10*
