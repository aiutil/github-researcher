---
title: "hermes-agent"
slug: "hermes-agent"
date_added: "2026-04-07"
last_seen_date: "2026-08-07"
category: "基础设施候选"
emoji: "🧙"
stars: "146,768"
language: "Python"
score: 62
tags: ["self-evolving-agent", "skill-system", "memory", "multi-platform", "mcp"]
url: "https://github.com/NousResearch/hermes-agent"
---

# hermes-agent

## 一句话定位
NousResearch 出品的自进化 AI Agent——"The agent that grows with you"，不是静态工具，而是会从经验中学习、生成新技能、在使用中自我改进的动态 Agent 系统。

## 它解决的问题
大多数 AI Agent 方案在记忆与学习上只做到两件事：把历史对话放进 Context（有限），或加个向量数据库做 RAG（只是检索，不是学习）。hermes-agent 走的是"从经验中生成技能并自动优化"这条路，更接近"真正学习"的方向。核心工程挑战是让 Agent 在跨会话使用中持续积累能力。

## 为什么值得关注
- **自进化 Skill 系统**：任务完成后自动提取可复用 Skill，Skill 在后续使用中自动优化
- **跨会话连续性**：FTS5 全文检索 + LLM Summarization，实现真正的长期记忆
- **Honcho 用户画像**：跨会话建立用户偏好模型，每次交互都在加深对用户的理解
- **多平台 Messaging Gateway**：Telegram、Discord、Slack、WhatsApp、Signal、Email
- **多终端部署**：$5 VPS / Docker / SSH / Daytona / Singularity / Modal
- **多 Provider 路由**：OpenRouter 200+ 模型、OpenAI、Kimi、GLM、MiniMax
- **Cron 调度 + 自然语言**：用自然语言描述定时任务，Agent 自动编排执行

## 热度来源判断
- 自进化 Agent 是 2026 年 Agent 领域的核心话题
- NousResearch 品牌效应（此前 Hermes 系列模型有影响力）
- 跨会话记忆 + Skill 自进化是开源中少见的能力
- 多平台 Gateway 降低了 adoption 门槛

## 关键技术亮点亮点
1. **自进化 Skill 系统**：不同于 RAG 的"检索已有知识"，这是"从经验中生成新能力"，Skill 在后续使用中自动优化
2. **FTS5 + LLM Summarization 长期记忆**：SQLite FTS5 全文检索保证召回速度，LLM 摘要压缩历史
3. **Honcho 用户画像建模**：跨会话建立用户偏好模型
4. **多平台 Messaging Gateway**：一个 Gateway 对接 Telegram/Discord/Slack/WhatsApp/Signal/Email
5. **OpenClaw 迁移路径**：明确提供从 OpenClaw 一键迁移，降低迁移门槛

## 架构启发
Skill 自进化机制是最值得深度研究的工程问题。如果能在企业内部落地，会是真正的差异化竞争力。核心思路：从"让 Agent 检索知识"升级到"让 Agent 从经验中创造知识"。Skill 系统、Memory 系统是多 Agent 平台必需的底层能力。

## 定位判断
**基础设施候选** — Skill 系统 + Memory 系统 + 多平台 Gateway 具备多 Agent 平台底层能力特征。

## 风险/局限/泡沫点
- **Skill 自进化的质量边界不明确**："自我优化"在实践中能走多远有待验证
- **OpenClaw 迁移功能**说明它正在蚕食 OpenClaw 生态，但迁移本身可能带来用户对供应商锁定风险的担忧
- **Stars 数据存在推算成分**（网络受限日的分析），需网络恢复后验证

## 与同类项目的关系
| 项目 | 定位 | 关系 |
|------|------|------|
| oh-my-claudecode | Claude Code 绑定的 Agent 编排 | 不同路径：独立部署 vs 平台绑定 |
| onyx | 开源 AI Chat 平台 | 不同定位：Chat 平台 vs 自进化 Agent |

## 是否值得持续跟踪
**是，深度跟踪 + 值得做 PoC** — 触及 Agent 核心问题（记忆+学习），对企业平台有直接参考价值。

## 后续观察点
- Skill 自进化质量的实际边界：复杂任务中自动生成的 Skill 是否可用
- 企业内部 PoC 的落地效果与反馈
- 多 Provider 路由的稳定性与成本控制
- 与 MCP 生态的集成深度
