---
title: "agents-md"
slug: "agents-md"
date_added: "2026-04-24"
last_seen_date: "2026-04-24"
category: "DevEx"
emoji: "📋"
stars: "489"
score: 73
tags: ["AGENTS.md", "Agent-Behavior", "Coding-Agent", "Karpathy", "Prompt-Engineering"]
url: "https://github.com/TheRealSeanDonahoe/agents-md"
---

# agents-md

## 一句话定位
即插即用的 AGENTS.md 文件，让任何 Coding Agent 表现如资深工程师——反谄媚、反无脑重构、强制验证循环。

## 解决的问题
当前 Coding Agent 普遍存在"谄媚"（过度迎合用户）、"无脑重构"（不必要的代码改动）和"缺乏验证"（不测就提交）三大行为问题。agents-md 通过精心设计的指令注入来解决这些问题。

## 为什么值得关注
1. 将 Karpathy 四原则和 Boris Cherny 工作流凝练为单一配置文件
2. 跨 Agent 兼容（Claude Code / Codex / Gemini CLI / Cursor）
3. 代表了"Agent 行为配置即代码"的新范式

## 热度来源判断
- 解决了所有 Coding Agent 用户的共同痛点
- "让 Agent 表现如资深工程师"的定位精准击中需求
- 轻量级（单文件），低门槛试用

## 关键技术亮点
- Kills sycophancy：反谄媚机制
- Stops drive-by refactors：约束不必要的重构
- Forces verification loops：强制验证循环
- 综合 Karpathy 四原则和 Boris Cherny 工作流
- 零依赖，纯 markdown 配置

## 架构启发
"配置即行为约束"范式。用 markdown 文件定义 Agent 行为，轻量、可版本控制、可组合。这是 AgentOps 工具链中的"约束层"。

## 定位判断
**学习型 + 工具型。** 理念先进但高度依赖 LLM 的指令遵循能力。

## 风险/局限/泡沫点
- 效果高度依赖底层模型的指令遵循能力
- 不同模型对同一 AGENTS.md 的遵从度差异大
- 缺乏量化评估：难以衡量"资深程度"提升
- 本质是高级 prompt engineering，技术壁垒不高

## 与同类项目的关系
- agentic-stack：解决 Agent 的可移植性（跨平台配置）
- skills-manage：解决 Skill 的管理问题
- claude-doctor：解决 Agent 会话诊断问题
- agents-md：解决 Agent 行为约束问题

三者构成 AgentOps 的完整工具链。

## 是否值得持续跟踪
**是。** Agent 行为治理是独立且重要的方向。

## 后续观察点
1. 是否产生量化效果对比数据
2. 社区是否贡献针对不同模型的变体
3. 是否被 Agent 平台原生集成

## 评分

| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 6 | 解决普遍痛点 |
| 技术创新度 | 5 | 高级 prompt engineering |
| 工程成熟度 | 6 | 单文件，简单可靠 |
| 架构启发价值 | 7 | 配置即行为约束范式 |
| 企业落地潜力 | 7 | 企业级 Agent 采纳需要行为治理 |
| 中期趋势概率 | 7 | Agent 行为治理是确定性需求 |
| 平台化潜力 | 5 | 可能被平台原生能力吸收 |
| 基础设施潜力 | 4 | 不太可能成为基础设施 |

**总分：47/80**
**归类：工具型 + 学习型**
**建议持续跟踪：是**
