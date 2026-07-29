---
title: "Stash"
slug: "stash"
date_added: "2026-04-29"
last_seen_date: "2026-04-29"
category: "观察型"
emoji: "📦"
stars: "502 stars"
stars_delta: "5天500+，新项目"
language: "Go"
score: 67
tags: ["ai-memory", "postgres", "mcp", "self-hosted", "go"]
url: "https://github.com/alash3al/stash"
---

# Stash

## 一句话定位
面向 AI Agent 的持久化记忆层，Postgres 存储，MCP server 内置，Go 单二进制自部署。

## 它解决的问题
AI Agent 缺乏结构化的持久记忆能力。每次对话都是从零开始，无法记住之前的 episodes、facts 和 working context。Stash 提供了一个轻量级、自托管的解决方案。

## 为什么值得关注（2026-04-29）
在 MemPalace（50K stars）定义了 AI Memory 赛道后，Stash 代表了另一种技术路线：Go 单二进制 + Postgres，更轻量，更适合基础设施团队。MCP server 内置意味着可以直接接入 Claude Code 等 Agent。

## 热度来源判断
增长来自 AI Memory 赛道的整体热度溢出。502 stars 增长适中，不算泡沫。定位清晰（self-hosted, single binary），吸引不想依赖云服务的开发者。

## 关键技术亮点
1. **三层记忆模型**：Episodes（事件流）、Facts（事实知识）、Working Context（当前上下文），结构清晰
2. **MCP Server 内置**：直接暴露 MCP 接口，无需额外适配层
3. **Go 单二进制**：部署极简，无运行时依赖，Self-hosted 友好
4. **Postgres 后端**：成熟可靠，适合生产环境

## 架构启发
- Agent Memory 不一定需要向量数据库，结构化存储 + 语义索引可以是另一种路径
- MCP 作为 Memory 接口标准正在成为事实标准
- 单二进制 + Postgres 的组合在基础设施工具中越来越流行（参考 Ditto, Litestream）

## 定位判断
在 AI Memory 生态中处于「轻量级自托管方案」的位置。对标 mem0（云服务）、MemPalace（Python + ChromaDB）。适合已用 Postgres 的团队。

## 风险 / 局限 / 泡沫点
1. 502 stars 仍太小，社区验证不足
2. 只有两个 open issues，要么代码极简，要么用户群体太小
3. 与 MemPalace 的 50K stars 相比差距过大，可能被边缘化
4. 单人项目（alash3al），维护可持续性存疑

## 与同类项目的关系
- **MemPalace**（50K stars）：Python + ChromaDB，更重的方案，基准测试领先
- **mem0**（云服务）：托管方案，API-first
- **Zep**：另一个 Agent Memory 方案，更偏企业级

## 是否值得持续跟踪
是。作为 AI Memory 赛道的 Go 路线代表，如果 stars 突破 2K 则值得关注。

## 后续观察点
1. 是否吸引企业用户采用（Postgres 生态优势）
2. MCP 接口是否被主流 Agent 框架集成
3. 是否出现生产环境使用案例

---
*首次记录：2026-04-29*
