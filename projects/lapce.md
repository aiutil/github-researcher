---
title: "lapce/lapce"
slug: lapce
date_added: 2026-07-25
last_seen_date: 2026-08-07
category: "工具型"
emoji: "⚡"
stars: "38,728 stars"
score: 80
tags: ["code-editor", "developer-tools", "rust", "text-editor", "vim"]
url: "https://github.com/lapce/lapce"
---

# lapce/lapce

## 一句话定位
用纯 Rust 编写的极速代码编辑器，从底层（Floem UI 框架、Druid GPUI）到上层层层优化性能，目标是成为 VS Code 的轻量高性能替代。

## 它解决的问题
VS Code 虽功能丰富但基于 Electron，内存占用大、启动慢、大型项目卡顿。Vim/Emacs 虽快但配置门槛高、生态小众。Lapce 试图占据"性能 + 现代体验"的中间地带：用 Rust 原生编译，启动毫秒级，操作丝滑流畅，同时提供现代编辑器期待的语法高亮、LSP 支持、插件系统、Vim 模式等能力。

## 为什么值得关注
- **Stars:** 38,728（截至 2026-08-07），代码编辑器领域新星
- **Forks:** 1,313，社区贡献活跃
- **License:** Apache-2.0
- **活跃度:** pushed_at 2026-07-15，持续开发中
- **Watchers:** 195
- **语言:** Rust（内存安全 + 零开销抽象）
- **内置 Vim 模式:** 原生支持 Vim 键位，无需插件

## 热度来源判断
Lapce 的热度是**"反 Electron"情绪 + Rust 生态崛起**双重驱动。开发者对 Electron 应用（VS Code、Slack、Discord）的内存占用长期不满，而 Rust 在系统编程领域的信誉持续提升。Lapce 作为"Rust 写的编辑器"自带话题性。但需注意：当前热度部分来自"概念期待"——它仍在积极开发中，功能成熟度尚未达到 VS Code 级别。

## 关键技术亮点亮点
1. **纯 Rust 实现:** 从 UI 框架（Floem）到核心逻辑全部 Rust，无 GC 停顿
2. **WASI 插件系统:** 插件用 WASM 运行，安全沙箱 + 跨语言支持（可用任何能编译 WASM 的语言写插件）
3. **内置 Vim 模式:** 原生 modal editing，无需安装插件
4. **LSP 支持:** 完整 Language Server Protocol 支持，复用 VS Code 生态的语言服务器
5. **Floem UI:** 自研的 Rust UI 框架，专为编辑器响应式场景优化
6. **远程开发:** 内置 SSH 远程编辑能力

## 架构启发
Lapce 的核心架构启发是 **"编辑器 = UI 框架 + 文本数据结构 + 插件运行时"** 三层解耦。自研 Floem（而非用 egui/iced）反映了一个判断：通用 UI 框架难以满足编辑器场景的极致性能需求。WASI 插件系统则是对"安全扩展"的回答——比 VS Code 的 Node 插件更安全（沙箱），比 Vim 的 VimScript 更现代（任意语言）。

## 定位判断
**潜力型工具项目。** Lapce 尚未成熟到挑战 VS Code，但它的技术路线（Rust + WASI + 原生性能）代表了代码编辑器的未来方向之一。适合两类人：(1) Vim 用户想要更现代体验；(2) 性能敏感的开发者。当前更适合"尝鲜 + 关注"，不建议作为主力编辑器。

## 风险/局限/泡沫点
- **功能成熟度:** 生态、插件、调试器等远不及 VS Code
- **开发者资源:** 核心团队较小，迭代速度受限于人力
- **竞争残酷:** 对手是 VS Code（巨无霸）、Zed（另一 Rust 编辑器，有商业支持）、Helix（终端编辑器）
- **UI 框架负担:** 自研 Floem 既是优势也是负担（需持续投入）
- **插件生态冷启动:** WASI 插件虽好，但生态建设需要时间

## 与同类项目的关系
- **vs VS Code:** VS Code 生态碾压（插件、调试、远程）；Lapce 性能和轻量碾压
- **vs Zed:** Zed 是另一个 Rust 编辑器（Atom 团队），有商业支持，GPU 加速渲染；Lapce 是纯社区
- **vs Helix:** Helix 是终端编辑器（Kakoune 范式），Lapce 是 GUI 编辑器
- **vs Neovim:** Neovim 是终端 + Lua 扩展；Lapce 是 GUI，对 Vim 用户更友好
- **vs Emacs:** Emacs 极致可定制但学习曲线陡峭；Lapce 开箱即用

## 是否值得持续跟踪
**值得跟踪。** Lapce 代表了"后 VS Code 时代"编辑器的一种可能方向（Rust + WASI + 原生性能）。即使最终未能取代 VS Code，它的技术选择（Floem UI、WASI 插件）会持续影响整个生态。

## 后续观察点
- 插件生态是否能突破冷启动（是否有重量级插件出现）
- 是否获得商业投资或基金会支持（决定可持续性）
- 与 Zed 的竞争格局分化
- 远程开发、调试器等"生产级功能"的成熟度
- 是否被大厂（如 JetBrains）关注或收购

---
> 数据来源: GitHub API (2026-08-07) | Stars: 38,728 | Forks: 1,313 | License: Apache-2.0
