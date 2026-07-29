---
title: "oh-my-codex"
slug: "oh-my-codex"
date_added: "2026-04-08"
category: "工具层"
emoji: "🔮"
stars: "18k"
stars_delta: "+14k/week"
language: "TypeScript"
score: 60
tags: ["AI Coding Agent", "TypeScript", "Codex CLI", "多Agent编排", "MCP"]
url: "https://github.com/Yeachan-Heo/oh-my-codex"
---

# oh-my-codex

## 一句话定位

OpenAI Codex CLI 的多 Agent 编排层——让 Codex 不再"独自工作"，而是组队协作。

## 它解决的问题

OpenAI 的 Codex CLI 提供了强大的单 Agent 编码能力，但缺乏：

1. **任务编排**：无法将复杂任务分解为多个角色协作完成
2. **持久化状态**：会话结束后上下文丢失
3. **可复用工作流**：常见开发模式（如"写测试→实现→审查"）无法模板化
4. **MCP 扩展**：无法接入外部工具和数据源

oh-my-codex（OMX）在 Codex CLI 之上构建了一层编排能力，解决了这些问题。

## 为什么值得关注（2026-04-08）

本周增长 **14K stars**，是 Claude Code 生态中增长最快的组件之一。与 oh-my-claudecode 形成双平台覆盖（Codex + Claude Code），说明开发者社区对"AI Agent 编排层"的需求是跨 LLM 供应商的。

## 热度来源判断

- **Codex CLI 缺陷**：OpenAI 的 Codex CLI 功能强大但"裸奔"，缺少工程化所需的编排能力
- **与 oh-my-claudecode 的协同**：同一作者/团队的双平台策略，降低了用户的学习成本
- **TypeScript 生态**：Web/JS 开发者群体庞大，TypeScript 工具更容易被采纳

## 关键技术亮点

1. **Staged Team Pipeline**：将任务分解为多个 Agent 角色（如 Planner、Coder、Reviewer），按阶段执行
2. **Role Keywords**：用 `@role` 语法快速激活特定 Agent 角色，使角色切换成为工作流的一部分
3. **OMX Skills**：可复用的工作流模板，常见开发模式一次定义、到处使用
4. **`.omx/` 目录**：存储计划、日志、记忆和运行时状态，实现跨会话持久化
5. **MCP Server 集成**：通过 MCP 协议接入外部工具和数据源

## 架构启发

oh-my-codex 的核心架构是 **薄编排层**——不替代 Codex，而是在其之上添加编排能力。这是一个明智的架构选择：

- **低耦合**：不依赖 Codex 内部实现，只通过 CLI 接口交互
- **高复用**：编排逻辑与底层 Agent 解耦，理论上可以适配任何 CLI Agent
- **Trade-off**：薄层意味着无法深度优化底层行为，但换来了灵活性和可维护性

## 定位判断

**工具层**。oh-my-codex 是 Codex CLI 的增强工具，不是独立框架。它的价值依赖于 Codex CLI 的存在。

## 风险 / 局限 / 泡沫点

- **Codex CLI 依赖**：如果 OpenAI 改变 Codex CLI 的接口或方向，oh-my-codex 可能一夜失效
- **与 Claude Code 生态的竞争**：oh-my-claudecode 和 oh-my-codex 的双平台策略分散了精力
- **增长泡沫**：14K/week 的增速部分来自 oh-my-claudecode 的引流，自然增长可能没那么快

## 与同类项目的关系

- **Claude Code**：oh-my-claudecode 覆盖 Claude Code 生态，oh-my-codex 覆盖 Codex 生态
- **claw-code**：claw-code 是全栈 Rust 实现，oh-my-codex 是 TypeScript 编排层，定位不同
- **Aider**：Aider 是独立的 AI 编码工具，不依赖 Codex CLI

## 是否值得持续跟踪

**持续跟踪。** 作为 AI Coding Agent 编排层的代表，oh-my-codex 的演进方向值得关注，尤其是其跨 LLM 平台的编排抽象。

## 后续观察点

1. **Codex CLI 兼容性**：OpenAI 更新 Codex CLI 后 oh-my-codex 的适配速度
2. **Skill 生态**：社区贡献的 OMX Skills 数量和质量
3. **双平台策略**：oh-my-claudecode 和 oh-my-codex 是否会合并为统一编排层

---

*首次记录：2026-04-08*
