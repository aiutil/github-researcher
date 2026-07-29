---
title: "herdr"
slug: "herdr"
date_added: "2026-06-01"
category: "工具型"
emoji: "🦬"
stars: "15,766 stars"
stars_delta: "从 11.4K→15.8K（周增 4.3K），增速持续加速，Homebrew + mise 安装渠道开通"
last_seen_date: "2026-07-13"
language: "Rust"
score: 83
tags: ["Agent Multiplexer", "Terminal", "Rust", "DevEx", "多Agent管理"]
url: "https://github.com/ogulcancelik/herdr"
---

## 2026-07-13 更新

stars 达到 15,766（周增 4,349，+38%）。增速持续加速。Score 上调至 85（↑2），原因：
- Socket API 让 Agent 自身可以调用 herdr——创建 pane、读取输出、互相等待，这把 tmux 模型从人的工具变成 Agent 协作基础设施
- Homebrew + mise 双包管理器上架，分发渠道成熟
- 插件系统 + marketplace 上线，社区贡献开始
- 与 Orca（16.8K⭐ ADE）+ OfficeCLI（15.4K⭐ Office 操作）共同定义了'Agent 工作环境'三层架构
- 键盘 + 鼠标双 first-class 交互设计

---

## 2026-07-05 更新

stars 达到 11,372（日+706，周+3K）。增速从日 +513 加速到 +706，增长率 38%。Score 上调至 83（↑5），原因：
- 增速持续加速，不是短期脉冲
- Agent 终端多路复用赛道被验证为持续需求
- Socket API + 插件系统的可编程能力为平台化打开空间
- 与 Orca（12K⭐ ADE）、codex-plugin-cc（24.3K⭐ 跨 Agent 桥接）形成 Agent 管理三层生态
- tmux-for-agents 定位深入人心

---

## 2026-07-03 更新

stars 达到 10,108（周增 2,401）。持续上榜 Rust Trending。定位判断维持 "工具型"——在 Agent 多路复用赛道与 Orca（11K⭐ 多 Agent ADE）、gstack（119K⭐ 工具栈）形成三层竞争：终端层（herdr）→ IDE 层（Orca）→ 工作流层（gstack）。herdr 作为 "tmux for agents" 的定位清晰但天花板有限。Score 下调至 78（↓4），原因是 Agent IDE 层（Orca）的快速进化可能吸收终端多路复用的需求。

---

# herdr

## 一句话定位
终端里的 Agent 多路复用器——类似 tmux 但专为 AI Coding Agent 设计，支持 workspace/tab/pane 管理、Agent 状态感知、detach/reattach。

## 它解决的问题
当开发者同时使用 Claude Code + Codex + Cursor 等多个 Agent 时：
1. 终端窗口管理混乱
2. Agent 状态不可见（在忙？在等？完成了？）
3. 关闭终端 = 杀死 Agent
4. 不同 Agent 的工作空间隔离

herdr 解决的是多 Agent 并行开发的 DevEx 问题。

## 为什么值得关注（2026-06-01）
1. 多 Agent 并行开发正在成为主流工作模式
2. Rust 实现，轻量高效，无 Electron 依赖
3. Agent 状态感知是独特差异化——tmux 做不到
4. 支持鼠标操作，降低了终端工具的使用门槛

## 热度来源判断
3.4K star，+923/week。热度来自：
- 多 Agent 开发场景的真实需求
- Rust 社区的关注度
- "tmux for AI Agents"的定位容易理解

不是泡沫。工具型项目，切中真实痛点。

## 关键技术亮点
1. **Agent 状态感知**：通过进程名和终端输出检测 Agent 状态（blocked/working/done/idle）
2. **Server-Client 架构**：detach 关闭客户端，server 和 pane 进程继续运行
3. **Handoff 模式**：实验性支持将活跃 pane 从旧 server 迁移到新 server
4. **Agent 会话恢复**：配合官方集成，server 重启后 Agent 可从上次会话继续

## 架构启发
- tmux 的架构模式在 AI Agent 时代仍然有效
- Agent 状态检测是一个新的终端工具能力维度
- Server-Client 分离是长时运行 Agent 的必要架构

## 定位判断
工具型。解决特定 DevEx 痛点，不易平台化或基础设施化。但在多 Agent 工作流中是不可或缺的"螺丝刀"。

## 风险 / 屏限 / 泡沫点
1. **与 tmux 功能重叠**——大部分功能 tmux + 脚本也能实现
2. **Agent 集成深度有限**——状态检测依赖进程名和输出，不够精确
3. **Rust 生态**——相比 Electron 应用，终端工具的用户群体有限

## 与同类项目的关系
| 项目 | 定位 | 差异 |
|------|------|------|
| herdr | Agent 终端多路复用 | Agent 状态感知，Rust |
| cc-switch | Agent 桌面管理器 | GUI 桌面应用，跨平台切换 |
| tmux | 通用终端复用 | 无 Agent 感知 |
| AionUi | Agent Cowork UI | Web UI，24/7 运行 |

## 是否值得持续跟踪
🔍 观察。工具型，切中痛点但护城河不深。

## 后续观察点
1. Agent 状态检测的准确性是否会提升
2. 是否会支持更多 Agent 的官方集成
3. 与 cc-switch 等竞品的差异化是否可持续

---
*首次记录：2026-06-01*
