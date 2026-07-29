---
title: "Agentic Stack"
slug: "agentic-stack"
date_added: "2026-04-30"
category: "基础设施候选"
emoji: "🧳"
stars: "1.8k stars"
stars_delta: "15天1.8K，稳步增长"
language: "Python"
score: 79
tags: ["agent-portability", "memory", "skills", "interoperability", "coding-agent"]
url: "https://github.com/codejunkie99/agentic-stack"
---

# Agentic Stack

## 一句话定位
可移植的 `.agent/` 文件夹 — 一个 Agent 的人格、记忆、技能跨工具不丢失。

## 它解决的问题
Coding Agent 生态碎片化：Claude Code、Cursor、Windsurf、OpenCode 等各有优势，但切换工具意味着丢失 Agent 积累的经验和技能配置。

目标用户：使用多种 Coding Agent 的开发者。

## 为什么值得关注（2026-04-30）
- 提出了 `.agent/` 标准目录概念，类似 `.env`、`.github/` 的定位
- 跨 6+ 种主流 Coding Agent 兼容
- 解决的是真实的迁移痛点

## 热度来源判断
**真实痛点驱动**。多 Agent 工具并存的开发者确实面临"切换成本高"的问题。

## 关键技术亮点

1. **`.agent/` 目录结构**：memory/（记忆）+ skills/（技能）+ protocols/（协议），标准化 Agent 的"家目录"。
2. **多 Agent 兼容**：Claude Code、Cursor、Windsurf、OpenCode、OpenClaw、Hermes、DIY Python。
3. **保留知识不重置**：切换工具时 Agent 的学习成果不丢失。

## 架构启发

**设计哲学**：Agent 的核心价值不在工具，在积累的经验。标准化这个"经验载体"是让 Agent 生态走向成熟的关键一步。

**类比**：`.env` 标准化了环境变量 → 所有框架支持。`.agent/` 标准化了 Agent 配置 → 所有 Agent 工具支持。如果成功，价值巨大。

## 定位判断
**基础设施候选**。如果被主流 Agent 工具采纳，将成为生态标准。

## 风险 / 局限 / 泡沫点

1. **需要 Agent 工具主动支持**：如果主流工具不采纳 `.agent/` 标准，这个项目将停留在理念层面。
2. **记忆格式标准化难度大**：不同 Agent 的记忆结构差异巨大，统一接口是硬问题。
3. **安全问题**：`.agent/` 包含所有技能和记忆，如果误提交到 Git 会泄露敏感信息。

## 与同类项目的关系

| 项目 | 定位 | 差异 |
|------|------|------|
| OpenChronicle | Agent 记忆 | 聚焦记忆捕获，不涉及技能/协议 |
| Mercury Agent | 完整 Agent | 内置记忆但非标准化格式 |
| Agent Skills Spec | 技能标准 | 只管技能不管记忆 |

## 是否值得持续跟踪
**是，中优先级**。标准化方向的尝试值得观察，关键看主流工具是否采纳。

## 后续观察点

1. 是否有主流 Agent 工具宣布支持 `.agent/` 格式
2. 记忆格式的跨 Agent 实际迁移测试结果
3. 是否被 OpenClaw 或 Cursor 等项目参考

---
*首次记录：2026-04-30*
