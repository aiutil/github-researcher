---
title: "stablyai/orca"
slug: orca
date_added: 2026-06-22
last_seen_date: 2026-07-02
category: "平台候选"
emoji: "🐬"
stars: "39.3k stars"
score: 86
tags: ["agent-ide", "parallel-agents", "worktree", "multi-agent", "mobile", "yc-backed"]
url: "https://github.com/stablyai/orca"
---

# stablyai/orca

## 一句话定位
面向并行 Agent 队列的 ADE（Agent Development Environment）——用你自己的订阅运行任意编码 Agent，支持桌面、移动和 VPS 多端，YC 孵化。

## 它解决的问题
2026 年开发者同时使用多个 AI 编码 Agent（Claude Code、Codex、Cursor、OpenCode 等），但每个 Agent 独立运行在各自终端中，缺乏统一管理、并行协调和进度可视化。Orca 将这些 Agent 统一到一个开发环境中：支持 worktree 隔离（每个 Agent 在独立 Git 分支工作）、并行执行、移动端监控、SSH 远程控制。它让开发者像管理一个"AI 编码团队"一样管理多个 Agent。

## 为什么值得关注
- **39,320 stars:** 创建于 2026-03-17，4 个月内接近 4 万 stars
- **YC 孵化:** Y Combinator 支持，商业可行性有背书
- **30+ Agent 兼容:** Claude Code、Codex、Cursor Agent、OpenCode、GitHub Copilot 等
- **多端支持:** 桌面、移动端、VPS——随时随地管理 Agent 队列
- **Worktree 隔离:** 每个 Agent 在独立 Git worktree 工作，互不干扰
- **BYO 订阅:** 使用用户自己的 API 订阅，无额外 Agent 费用

## 热度来源判断
热度来自多 Agent 编程范式的兴起。2026 年开发者普遍认识到"一个 Agent 不够用"——需要多个 Agent 并行处理不同任务。Orca 作为"多 Agent 管理环境"的先行者获得了大量关注。YC 的品牌背书和"使用自己的订阅"（无中间商加价）的定位吸引了成本敏感的开发者。

## 关键技术亮点
- Git Worktree 原生集成：每个 Agent 绑定独立 worktree，代码变更天然隔离
- Agent 抽象层：统一接口适配 30+ 编码 Agent
- 并行调度：多个 Agent 同时工作，资源互不冲突
- 移动端控制：手机上查看 Agent 进度、审批 PR、回复 Agent 提问
- SSH 远程：从任何设备连接到 VPS 上的 Agent 运行环境
- Ghostty 终端：高性能终端渲染（tags 中提及 ghostty）

## 架构启发
Orca 的核心启发是"Git Worktree 是多 Agent 并行编程的天然隔离单元"。对架构师的启发是：**在代码协作场景中，Git 分支/worktree 比容器/沙箱更适合作为 Agent 的隔离边界**——它既是技术隔离（不同工作目录），又是流程隔离（不同 PR/分支），还天然支持代码审查和合并。

## 定位判断
**平台候选（强）。** 已具备 Agent IDE 的核心特征：多 Agent 管理、并行执行、多端支持。39k stars + YC 背景 + 快速增长使其成为 Agent IDE 赛道的领跑者之一。定位为"并行 Agent 的统一工作台"。

## 风险/局限/泡沫点
- **3,265 open issues:** 数量极高，可能反映快速增长中的质量挑战或复杂的兼容性维护
- **Agent 兼容性维护:** 30+ Agent 的 API 和行为差异是持续的工程负担
- **BYO 订阅模式:** 无中间收入，商业模式可能依赖增值功能
- **移动端体验:** 移动端编码管理体验的天花板受限于设备交互
- **与 Multica 的竞争:** 两者在多 Agent 管理维度高度重叠

## 与同类项目的关系
- 与 **Multica** 在多编码 Agent 管理维度是最直接的竞品——Orca 聚焦个人开发者，Multica 聚焦团队
- 与 **Claude Code**、**Cursor** 等单体 Agent 形成上下层——Orca 管理它们
- 与 **wshobson/agents**（Agent 技能市场）在 Agent 配置维度互补
- 与 **Codex Plugin CC**（跨 Agent 桥接）在 Agent 互通维度有交集
- YC 生态中与 Daytona（Agent 沙箱）可能形成投资组合互补

## 是否值得持续跟踪
**强烈推荐跟踪。** 作为并行 Agent ADE 的先行者，Orca 的架构设计（worktree 隔离、多端控制、BYO 订阅）代表了 AI 编程工作流的演进方向。建议持续关注其 Agent 兼容性和企业功能。

## 后续观察点
- 3,265 open issues 的处理速度（质量信号）
- 移动端使用场景的实际渗透率
- 是否推出团队协作功能（与 Multica 竞争）
- YC 后续融资和商业化路径
- 企业采用情况（开发者团队是否标准化使用 Orca）

---
> 数据来源: GitHub API (stablyai/orca) | 星标: 39,320 | 语言: TypeScript | 许可证: MIT
