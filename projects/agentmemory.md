---
title: "rohitg00/agentmemory"
slug: "agentmemory"
date_added: "2026-05-29"
last_seen_date: "2026-08-11"
category: "基础设施候选"
emoji: "🧠"
stars: "26,858 stars"
stars_delta: "从19.3K到26.9K（3个月），持续增长"
language: "TypeScript"
license: "Apache-2.0"
score: 90
tags: ["Agent记忆", "MCP", "持久化", "iii引擎", "记忆服务", "knowledge-graph"]
url: "https://github.com/rohitg00/agentmemory"
---

# rohitg00/agentmemory — AI Coding Agent 的统一持久记忆服务

## 一句话定位
agentmemory 是基于 iii 引擎构建的 AI 编程 Agent 统一持久记忆服务——支持 Claude Code、Codex、Cursor、Gemini CLI、Hermes、OpenClaw 等 10+ Agent 平台，通过 MCP Server / Hooks / Native Plugin 三种方式接入，实现跨会话、跨 Agent 的共享记忆。

## 它解决的问题
Agent 最大的工程缺陷是**无状态**：每次对话从零开始，不记得上次做过什么、用户偏好、项目上下文。agentmemory 提供统一的记忆服务层（`agentmemory` 运行在 :3111 端口），让所有 Agent 共享同一个记忆服务器，具备置信度评分、生命周期管理、知识图谱和混合搜索能力。

## 为什么值得关注（2026-08-11）
- **26,858 stars**（截至 2026-08-11），Apache-2.0 许可
- **2,282 forks**，社区贡献活跃
- **75 subscribers**，核心开发者关注
- **95.2% 检索 R@5**（Recall@5），**92% 更少 token**
- **54 个 MCP 工具**，**12 个自动 Hooks**
- **1,596+ 测试通过**，工程质量扎实
- **零外部数据库依赖**（0 external DBs）
- **官方网站 agent-memory.dev**，npm 包 `@agentmemory/agentmemory`
- 支持 10+ Agent：Claude Code（native plugin + 12 hooks + MCP）、Codex CLI、Copilot CLI、Cursor、Gemini CLI、Hermes、OpenClaw、pi、OpenCode、Cline、Goose
- **15 个原生 Skills**（8 个可调用 + 7 个参考），Agent 自动知道何时使用记忆工具
- 扩展了 Karpathy 的 LLM Wiki 模式（GitHub Gist 1.3K stars / 182 forks）

## 热度来源判断
**真实需求驱动。** 记忆是 Agent 从「玩具」到「工具」的关键能力。来自 rohitg00（ai-engineering-from-scratch 作者），有社区信任基础。iii 引擎提供了强有力的底层支持。Stars 从 19.3K 到 26.9K 的稳定增长说明持续采纳而非一时热度。11 种语言 README 说明全球化运营。95.2% recall@5 的 benchmark 数据是技术实力的证明。

## 关键技术亮点
1. **统一记忆服务**：所有 Agent 共享同一个记忆服务器（:3111），跨 Agent 记忆可互通——你在 Claude Code 里做的事，Codex 也能记住
2. **置信度评分 + 生命周期管理**：不是简单存储，而是有质量评估的智能记忆——低置信度记忆会衰减
3. **知识图谱 + 混合搜索**：支持结构化（图谱遍历）和语义（向量）检索
4. **实时 Viewer（iii Console）**：可视化记忆内容、使用情况和置信度变化
5. **三种接入方式**：MCP Server（标准协议）、Hooks（事件驱动）、Native Plugin（深度集成）
6. **零外部数据库依赖**：内置存储，部署门槛极低（`npm install -g @agentmemory/agentmemory`）
7. **Karpathy LLM Wiki 扩展**：在原模式上增加置信度评分、生命周期、知识图谱、混合搜索

## 架构启发
- **记忆即服务（Memory as a Service）**：Agent 记忆应该是独立服务，而非嵌入在 Agent 内部——与微服务架构理念一致
- **MCP 作为统一接入协议**：通过 MCP 实现跨平台兼容，是 Agent 基础设施设计的正确方向
- **置信度评分的必要性**：不是所有记忆都等价，需要质量评估机制——这解决了 Agent 记忆"越用越糊"的问题
- **Agent = Base Model + Skill Layer + Knowledge Layer + Memory Layer**：agentmemory 锁定 Memory Layer

## 定位判断
**基础设施候选**。记忆层是 Agent 的"水电煤"——所有 Agent 都需要，但目前缺失。如果记忆服务标准化，agentmemory 可能成为 Agent 生态的基础组件。已有官方网站和 npm 包，具备从开源工具向 SaaS 演进的条件。

## 风险 / 局限 / 泡沫点
1. **与 iii 引擎的强绑定**：agentmemory 锁定 iii-engine v0.11.2，如果 iii 出问题或方向变化，agentmemory 受影响
2. **记忆准确性衰减**：长期记忆在多次更新后可能产生矛盾，置信度评分能否完全解决待验证
3. **隐私风险**：集中式记忆服务存储所有 Agent 交互历史，企业级部署需要数据隔离方案
4. **432 Open Issues**：问题处理压力较大
5. **75 subscribers 相对较低**：相比 27K stars，深度关注者比例偏低，说明大量用户是"先 star 后用"
6. **单人主导项目**：rohitg00 个人主导，bus factor 风险

## 与同类项目的关系
- **vs mem0**：mem0 是独立记忆产品，agentmemory 更像 Agent 生态组件（更通用，支持所有 Agent）
- **vs Claude Mem**：Claude Mem 仅服务 Claude，agentmemory 跨平台
- **vs honcho**：honcho 更偏学术研究，agentmemory 更实用工程化
- **vs Graphify**：Graphify 做 Knowledge 层（代码图谱），agentmemory 做 Memory 层（交互记忆），互补
- **vs iii engine**：agentmemory 基于 iii 构建，是 iii 的上层应用

## 是否值得持续跟踪
**强烈建议。** Agent 记忆是确定性需求，agentmemory 在标准化方向上走得最远——跨 Agent 共享记忆 + 置信度评分 + MCP 接入是正确架构。

## 后续观察点
1. iii 引擎的独立健康度和社区活跃度
2. 是否被主流 Agent 平台（Claude Code / Codex）官方集成
3. 企业级隐私和安全方案（数据隔离、加密、审计）
4. 记忆准确性在长期使用（6 个月+）中的表现
5. SaaS 化路径（agent-memory.dev 的商业化）

---
> 数据来源: GitHub API (2026-08-11) | Stars: 26,858 | Forks: 2,282 | License: Apache-2.0 | 语言: TypeScript | 创建: 2026-02-25
