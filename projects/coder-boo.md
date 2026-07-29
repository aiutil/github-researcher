---
title: "coder/boo"
slug: "coder-boo"
date_added: "2026-06-19"
category: "工具型"
emoji: "👻"
stars: "661 stars"
stars_delta: "9天+661"
language: "Zig"
score: 79
tags: ["terminal", "multiplexer", "libghostty", "ai-agent", "zig"]
url: "https://github.com/coder/boo"
---

# Coder Boo

## 一句话定位
基于 libghostty 的终端多路复用器（GNU screen 替代品），用 Zig 实现——每个 session 的完整屏幕状态可被 AI agent 精确读取。

## 它解决的问题
tmux/screen 的 detach/reattach 只恢复终端的"显示"内容，不保留完整终端状态（styles、cursor position、scrolling regions、terminal modes）。对于 AI agent 来说，无法准确读取另一个 session 的屏幕状态。

## 为什么值得关注（2026-06-19）
- Coder 公司出品（知名开发者工具公司）
- Zig + libghostty，技术栈前沿
- `boo peek` / `boo wait` / `--json` 输出，专为 AI agent 自动化设计
- libghostty 的终端模拟核心保证屏幕状态精确

## 热度来源判断
Coder 品牌效应 + AI agent 自动化场景热度。661 stars 对于终端工具体量已属不错。

## 关键技术亮点
1. **libghostty 终端模拟** — 不是截屏，而是解析所有终端序列，维护精确状态
2. **Agent-friendly API** — send/peek/wait + JSON 输出，无需 TTY
3. **Faithful redraw** — SGR styles、cursor、scrollback 完整恢复
4. **Zig 实现** — 低内存占用、高性能

## 架构启发
boo 代表了 **Terminal as Agent Interface** 趋势——终端不再只是人的工具，也是 AI agent 的工具。如果 AI agent 能可靠地读取和操作终端，就拥有了一个通用的系统交互接口。

## 定位判断
工具型项目，但可能成为 AI agent 工具链的重要组件。如果 Coder 将其与 remote development 产品线整合，价值更大。

## 风险 / 局限 / 泡沫点
1. **Zig 小众** — 贡献者门槛高于 Go/Rust
2. **libghostty 依赖** — 绑定 Ghostty 生态
3. **tmux 已有统治地位** — 切换成本高
4. **AI agent 场景尚未验证** — 哪些 agent 真的需要读终端屏幕？

## 与同类项目的关系
- **vs tmux** — tmux 更成熟，boo 更 AI-friendly
- **vs screen** — screen 已过时，boo 是精神继任者
- **vs Claude Code terminal** — Claude Code 内置终端是内嵌的，boo 是外部多路复用器

## 是否值得持续跟踪
**是。** Terminal-as-Agent-Interface 是值得关注的新范式。

## 后续观察点
1. 是否被主流 Coding Agent 集成
2. Coder 是否推出基于 boo 的商业产品
3. 社区贡献活跃度

---
*首次记录：2026-06-19*
