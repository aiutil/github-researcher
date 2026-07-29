---
title: "claw-code"
slug: "claw-code"
date_added: "2026-04-08"
category: "基础设施候选"
emoji: "🦀"
stars: "188.8k stars"
stars_delta: "+10k/week"
language: "Rust"
score: 75
tags: ["AI Coding Agent", "Rust", "多Agent编排", "开源"]
url: "https://github.com/ultraworkers/claw-code"
---

# claw-code

## 一句话定位

史上最快突破 100K stars 的开源项目——基于 Rust 的 AI Coding Agent 框架，Claude Code 架构的 Clean-room 重实现。

## 它解决的问题

AI Coding Agent 是 2025-2026 年最热的赛道之一，但大多数方案要么绑定特定 LLM（如 Claude Code 绑 Anthropic），要么性能不足以处理大型代码库。claw-code 试图解决三个核心问题：

1. **性能**：Rust 实现带来极致的启动速度和内存效率，适合处理大型 monorepo
2. **供应商中立**：Clean-room 重实现意味着不绑定任何 LLM 供应商
3. **多 Agent 编排**：支持 sub-agent 并行执行复杂任务，而非单线程调用

面向的用户是需要在本地或私有环境中高效运行 AI Coding Agent 的开发者，尤其是处理大型 Rust/C++/Go 项目的团队。

## 为什么值得关注（2026-04-08）

claw-code 的增长速度创造了 GitHub 历史：**发布 2 小时即破 50K stars**，一周内飙升至 168.7K，全球排名 #34。这种增长速度远超之前的任何开源项目（包括 Linux、React、TensorFlow）。

2026-04-08 当天，claw-code 仍保持 +10K/week 的增速，且两个并行仓库（ultraworkers 和 instructkr）同时爆发，说明社区需求远未被满足。

## 热度来源判断

- **技术稀缺性**：Rust 实现的 AI Agent 框架极其罕见，性能优势明显
- **Claude Code 替代**：大量开发者想要 Claude Code 的能力但不想被 Anthropic 锁定
- **自主维护叙事**：项目声称由 AI（lobsters/claws）而非人类维护，引发巨大好奇
- **Clean-room 法律叙事**：作为 Claude Code 的"重写"而非"fork"，避免法律争议的同时提供功能替代

## 关键技术亮点

1. **Rust 原生实现**：所有核心组件（Tool calling、Context 管理、Sub-agent 编排）均为 Rust 实现，启动速度和内存占用远优于 Node.js/Python 方案
2. **Claude Code 架构复刻**：保持了 Claude Code 的核心设计——Tool protocol、Permission system、Session management——但完全重写，不依赖任何 Anthropic 代码
3. **Sub-agent 编排**：支持将复杂任务分解为多个 sub-agent 并行执行，每个 sub-agent 有独立的 context 和 tool set
4. **Terminal-native**：深度集成终端操作，不是 Web IDE 插件，而是直接在终端中运行的 Agent
5. **多 LLM Provider 支持**：通过 Provider 抽象层支持 OpenAI、Anthropic、Google 等多种 LLM

## 架构启发

claw-code 的核心架构决策是 **Rust + Clean-room**。这个组合的含义是：

- **Rust 选择**：AI Agent 是一个 I/O 密集 + 内存密集的场景。Rust 的零成本抽象和所有权模型使其在处理大型代码库时具备天然优势
- **Clean-room 重写**：避免了 fork 带来的法律风险和代码债，但也意味着需要大量工程投入来复现已有功能
- **Trade-off**：Rust 的开发效率低于 TypeScript/Python，但运行效率显著更高。对于 Agent 框架这种"写一次、运行百万次"的基础设施，这个 trade-off 是合理的

## 定位判断

**基础设施层**。claw-code 不是应用，不是平台，而是 AI Coding Agent 的运行时框架。它的价值在于提供高性能的 Agent 执行环境，上层可以构建各种 AI 辅助开发工具。

## 风险 / 局限 / 泡沫点

- **"自主维护"叙事存疑**：虽然声称由 AI 维护，但实际上需要人类设定目标和审核，纯粹的"AI 自主维护"仍是不现实的
- **功能追赶**：作为 Claude Code 的重写，永远在追赶原版的功能更新
- **168K stars 的泡沫成分**：大量 star 来自好奇心而非实际使用，真正的活跃用户数可能远低于 star 数
- **Rust 生态人才稀缺**：贡献者需要同时懂 Rust 和 AI Agent，这个交集很小

## 与同类项目的关系

- **Claude Code（Anthropic）**：claw-code 是其 Clean-room 重实现，功能对标但供应商中立
- **oh-my-codex**：TypeScript 生态的 Codex 编排层，定位类似但技术栈不同
- **Aider / Continue.dev**：更轻量的 AI 编码辅助工具，claw-code 更偏"全功能 Agent"
- **claw-code-parity**：claw-code 生态内部的 Rust 重写版本，专注于架构改进

## 是否值得持续跟踪

**⭐ 必须跟踪。** 无论最终产品形态如何，claw-code 已经定义了 AI Coding Agent 赛道的性能天花板和社区规模。它的 Rust 架构选择和多 Agent 编排能力值得深入研究。

## 后续观察点

1. **claw-code-parity 的架构差异**：两个版本的演进方向是否一致
2. **实际用户留存率**：GitHub 上的活跃 PR/Issue 数量 vs star 数量
3. **LLM Provider 生态**：哪些 LLM 在 claw-code 上运行效果最好
4. **企业采用情况**：是否有大公司在生产环境使用

---

*首次记录：2026-04-08*

*最近更新：2026-04-23 — stars 增至 187.5k，持续领跑 Coding Agent 赛道*
