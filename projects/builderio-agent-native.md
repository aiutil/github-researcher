---
title: "BuilderIO agent-native"
slug: "builderio-agent-native"
date_added: "2026-06-20"
last_seen_date: "2026-06-20"
category: "平台候选"
emoji: "🏗️"
stars: "1,002 stars"
stars_delta: "日增 210"
language: "TypeScript"
score: 82
tags: ["agent-native", "framework", "builderio", "multiplayer", "agentic-applications", "mcp", "a2a"]
url: "https://github.com/BuilderIO/agent-native"
---

# BuilderIO agent-native

## 一句话定位

Agent 原生应用框架——UI 和 Agent 是同一系统的平等公民，每个 action 既能点击也能对话，支持 CRDT 实时多人协作。

## 解决的问题

当前 Agent 应用和 UI 是割裂的：Agent 在聊天窗口里，UI 在另一边。开发者需要分别维护 Agent 的 action 和 UI 的 handler。agent-native 把它们统一——`defineAction` 定义一次，从 UI 按钮、Agent 对话、HTTP API、MCP、A2A 到 CLI 全部复用。

## 为什么值得关注（2026-06-20）

BuilderIO 出品（Steve Sewell 团队），1,002 stars 日增 210。核心理念"不要在富 UI 和自主 Agent 之间二选一"直击 SaaS 产品开发痛点。已有 6 个完整 SaaS 模板（Calendar / Content / Plans / Slides / Analytics / Clips），每个都是 100% 开源可 clone 的完整应用。

## 热度来源判断

**BuilderIO 品牌 + 范式创新。** "Agent 和 UI 共享 action"是一个真正的架构创新。日增 210 虽然不高，但 BuilderIO 在前端开发者社区的影响力意味着一旦开发者理解这个概念，增长会加速。

## 关键技术亮点

1. **defineAction 统一接口：** 一次定义，UI / Agent / HTTP / MCP / A2A / CLI 全部复用。这是"action 即 API 即 Agent 能力"的范式创新。

2. **CRDT 实时多人协作：** 人类和 Agent 在同一 document 上同时工作。live presence（cursor、selection ring）让 Agent 成为 first-class peer editor。

3. **三种应用形态：** Headless API / Rich chat / 完整 SaaS 应用——同一套 primitives，不同 surface。

4. **全协议集成：** A2A + MCP + MCP Apps + AG-UI + Claude Agent SDK + Vercel AI SDK——所有主流 Agent 协议开箱即用。

5. **Backend agnostic：** 任何 Drizzle 支持的 SQL + 任何 Nitro 兼容的 host。无锁定。

## 架构启发

agent-native 的核心洞察是"action 是 agent-native 应用的原子单位"：
```
defineAction → UI button + Agent tool + HTTP endpoint + MCP method + A2A call + CLI command
```

这类似于 12-Factor App 把 config 和 code 分离——agent-native 把"做什么"和"谁来做（人/Agent/API）"分离。这在架构上意味着：
- 新增 Agent 能力不需要写新代码
- UI 和 Agent 天然保持同步
- 产品可以"自进化"（Agent 修改自己的 UI）

## 定位判断

**Agent 原生 SaaS 的框架层。** 在应用框架光谱中：
- Next.js = Web 应用框架（无 Agent）
- Astro flue = 通用 Agent 应用框架
- BuilderIO agent-native = Agent 原生 SaaS 框架（含 UI + Agent + 多人协作）

agent-native 比 flue 更偏应用层，比传统 SaaS 框架更偏 Agent。

## 风险 / 局限 / 泡沫点

1. **概念教育成本高：** "Agent 原生"是新概念，开发者需要理解 action/UI/Agent 统一的范式。
2. **TypeScript 限定：** 不支持 Python。
3. **BuilderIO 商业策略：** 可能从开源走向商业 hosted（类似 BuilderIO Qwik 的商业化路径）。
4. **早期阶段：** 6 个模板虽然好，但核心框架的稳定性需验证。

## 与同类项目的关系

| 项目 | 核心差异化 | 目标场景 |
|------|-----------|----------|
| agent-native | UI = Agent，action 统一 | Agent 原生 SaaS |
| Astro flue | 沙箱 + 持久执行 | 通用 Agent 应用 |
| Vercel eve | filesystem-first | Agent 定义和组织 |
| Convex + AI | Realtime DB + AI | Agent 后端 |

agent-native 和 flue 是互补的——agent-native 做应用层，flue 做运行时层。但两者也有重叠（都做 Agent 应用框架）。

## 是否值得持续跟踪

**是。** "UI 和 Agent 是同一系统的平等公民"这个理念值得长期跟踪。如果 BuilderIO 全力推动，agent-native 有潜力定义"Agent 原生应用"这个新品类。

## 后续观察点

1. 6 个 SaaS 模板的 fork 和使用数据
2. defineAction 在真实项目中的开发体验
3. CRDT 多人协作在 Agent 场景的稳定性
4. BuilderIO 的商业化路径（是否推出 hosted 版本）
5. 是否有企业采用案例

---
*首次记录：2026-06-20*
