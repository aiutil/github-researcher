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

## 关键技术亮点
1. **Filesystem as API** — agent.ts（配置）、instructions.md（系统提示）、tools/（函数）、skills/（按需加载）、channels/（消息）、schedules/（定时）
2. **Skills 按需加载** — 不是一次性灌入所有 context，而是根据需要加载 skill
3. **Channels 抽象** — HTTP、Slack、Discord 消息通道统一管理
4. **内嵌文档** — npm 包包含完整文档，Coding Agent 无需联网查文档

## 架构启发
eve 的设计哲学是 **convention over configuration** 应用于 Agent 开发。这与 Next.js 的 app/ 目录约定一脉相承，Vercel 在把这个模式复制到 Agent 领域。

```mermaid
graph TD
    subgraph "eve Agent 目录结构"
        A["agent/"] --> AT["agent.ts<br/>模型 + 运行时配置"]
        A --> AI["instructions.md<br/>常驻系统提示"]
        A --> AT2["tools/<br/>typed 函数"]
        A --> AS["skills/<br/>按需加载程序"]
        A --> AC["channels/<br/>HTTP / Slack / Discord"]
        A --> AS2["schedules/<br/>cron 定时任务"]
    end
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
