---
title: "CLI-Anything"
slug: "cli-anything"
date_added: "2026-04-26"
last_seen_date: "2026-08-11"
category: "基础设施候选"
emoji: "🔌"
stars: "46,882 stars"
stars_delta: "+14K (4个月)"
language: "Python"
score: 83
tags: ["cli", "agent-native", "integration", "universal-adapter", "CLI-Hub", "HKUDS"]
url: "https://github.com/HKUDS/CLI-Anything"
---

# CLI-Anything — 让所有软件变为 Agent 可调用的 CLI

## 一句话定位
港大 HKUDS 团队出品的 Agent-Native CLI 生成框架，自动将 GUI 软件转换为标准 CLI 接口，让 AI Agent（Claude Code / Codex / Cursor / OpenClaw）直接调用任何软件——配套 CLI-Hub 包管理器和 18+ 已适配应用。

## 它解决的问题
AI Agent 要操控 GUI 软件极其困难——需要浏览器自动化、OCR、坐标点击、屏幕截图分析，且极其脆弱。CLI-Anything 的核心思路是**"与其让 Agent 学会操作所有 GUI，不如先把 GUI → CLI 标准化"**。它自动发现 GUI 软件的可操作入口并生成 CLI 包装，让 Agent 通过标准命令行协议调用。目前已覆盖 Blender、FreeCAD、Godot、Inkscape、Kdenlive、Zotero、Obsidian、n8n、QGIS 等 18+ 应用，配套 CLI-Hub 包管理器（`pip install cli-anything-hub`）可一行安装社区贡献的 CLI。

## 为什么值得关注（2026-08-11）
- **Stars:** 46,882（截至 2026-08-11），4 个月内从 32.6K 增至 46.9K
- **Forks:** 4,360，社区贡献极其活跃（平均每周新增 CLI 适配）
- **Watchers:** 178
- **License:** Apache-2.0
- **语言:** Python（Click CLI 框架）
- **Open Issues:** 80
- **测试覆盖:** 2,461 个测试通过，单元 + E2E 覆盖
- **学术背书:** 港大数据科学实验室 (HKUDS) 出品，有 arXiv 技术报告
- **CLI-Hub:** 类似 npm 的 CLI 包管理器，社区可贡献新 CLI
- **多语言文档:** 中文、日文、德文 README

## 热度来源判断
CLI-Anything 的热度是**"Agent-Native 接口标准化的确定性趋势 × 港大学术背书 × CLI-Hub 社区贡献飞轮 × 18+ 真实应用覆盖"**的组合。"万物 Agent-Native"的愿景极具吸引力，但关键是它**不只是概念**——已有 18+ 真实应用适配（Blender、Godot、FreeCAD 等都是主流工具），2461 个测试通过说明工程质量扎实。4,360 个 forks 反映社区高度参与——这正是"包管理器"类项目的网络效应：贡献的 CLI 越多，价值越大，吸引更多用户和贡献者。热度**真实且具有飞轮潜力**。178 个 subscribers 说明核心开发者群体深度关注。

## 关键技术亮点
1. **HARNESS.md 渐进式披露设计:** 每个 CLI 适配包含一个 SKILL.md（AI 可发现的技能定义）+ HARNESS.md（渐进式操作指南），Agent 按需加载详细文档，而非一次性灌入全部上下文
2. **CLI-Hub 包管理器:** `pip install cli-anything-hub` + `cli-hub install <name>`——类似 npm 的社区 CLI 分发机制，支持 pip/npm/brew 多源安装
3. **SKILL.md 自动生成 (Phase 6.5):** 每个生成的 CLI 自动附带 AI 可发现的技能定义，Agent 可以自主发现和安装 CLI
4. **CLI-Hub Meta-Skill:** Agent 可以自主发现、安装、管理 CLI——真正的"Agent 自主扩展能力"
5. **标准输出格式:** JSON + Human-readable 双模式输出，既适合 Agent 解析也适合人类阅读
6. **Click 框架 + Python ≥3.10:** 基于成熟的 Click CLI 框架，代码质量和可维护性有保障
7. **多工具兼容:** 生成的 CLI 可被 Pi、OpenClaw、nanobot、Cursor、Claude Code 等 Agent 直接使用

## 架构启发
CLI-Anything 的核心启发是**"适配器模式在 AI 时代的重大应用"**。经典软件工程中，适配器模式用于让不兼容的接口协同工作。CLI-Anything 将其提升到生态级别——**为所有 GUI 软件生成统一的 CLI 适配层**，让 Agent 获得一个标准化的"操作系统级 API"。

更深层的启发是**CLI 作为 Agent 与软件交互的标准协议**。当前 Agent 与软件交互的方式极其碎片化（浏览器自动化、API 调用、MCP 工具、屏幕操作），而 CLI-Anything 提出了一种统一范式：**所有软件都应暴露 CLI 接口**。这与 Google Workspace CLI 的思路一致——平台厂商和学术界都在向 CLI 优先靠拢。

企业架构师应认真考虑：**所有内部工具都应提供 CLI 接口**，这是 Agent-Native 基础设施的基本要求。

## 定位判断
**基础设施候选（强）。** CLI-Anything 试图成为 **Agent 与软件之间的标准适配层**——类似 MCP（工具协议）但面向完整应用而非单个工具。如果 CLI 成为 Agent 调用软件的标准接口（这是确定性趋势），CLI-Anything 就是这个转换层的头部实现。CLI-Hub 包管理器赋予了它平台化潜力——社区贡献的 CLI 越多，它就越接近"Agent 的应用商店"。46K stars + 4.3K forks + 18+ 真实应用已显示飞轮雏形。

## 风险 / 局限 / 泡沫点
- **GUI 软件变化频繁:** CLI 包装层需要持续跟进底层软件的 UI/API 变化，维护成本极高
- **状态依赖操作:** 很多 GUI 操作有复杂状态依赖（如 Blender 的编辑模式、Godot 的场景树），CLI 化可能不完整
- **"ALL Software"的宏大定位:** 实际覆盖率需要持续验证——18+ 应用虽不少，但相比"所有软件"仍是极小比例
- **与 MCP 的潜在竞争:** MCP (Model Context Protocol) 是 Anthropic 推动的工具协议标准，如果 MCP 扩展到覆盖完整应用，CLI-Anything 的"适配层"价值可能被吸收
- **学术项目可持续性:** HKUDS 是大学实验室，核心维护者可能随学生毕业而变动

## 与同类项目的关系
- **vs Google Workspace CLI:** Google 自家产品 CLI 化（官方、专一）；CLI-Anything 做通用化（社区、广泛）
- **vs MCP (Anthropic):** MCP 是工具调用协议标准（细粒度）；CLI-Anything 是应用级 CLI 适配（粗粒度）——不同层级，可能互补
- **vs OpenCLI:** OpenCLI 偏 Web → CLI；CLI-Anything 偏 Desktop Software → CLI
- **vs npm / PyPI:** CLI-Hub 是专门面向 Agent 的 CLI 分发渠道，类似"Agent 的包管理器"
- **vs wshobson/agents:** agents 提供 Agent 技能/规则；CLI-Anything 提供软件操作能力——不同层面的 Agent 赋能

## 是否值得持续跟踪
**是（高优先级）。** Agent-Native 接口标准化是确定性趋势，CLI-Anything 是这一方向的头部项目。建议：对 Agent 系统构建者，直接评估采用 CLI-Hub 安装已有适配（Blender/Godot/FreeCAD 等）。对架构师，将其"CLI 优先"理念纳入内部工具设计规范。对生态观察者，关注它是否成为 Agent 调用软件的事实标准。

## 后续观察点
1. **CLI 覆盖范围增长:** CLI-Hub 中社区贡献的 CLI 数量增速（目前 18+，是否突破 100+）
2. **Agent 平台原生集成:** Claude Code / Codex / OpenClaw 是否原生支持 CLI-Hub 安装
3. **与 MCP 的关系:** 是被吸收、互补，还是竞争
4. **企业采纳:** 是否有企业将 CLI-Anything 作为内部工具 Agent 化的标准方案
5. **标准化努力:** 是否形成"CLI-for-Agent"规范草案
6. **社区贡献质量:** 社区贡献的 CLI 是否经过充分测试和安全审查

---
> 数据来源: GitHub API (2026-08-11) | Stars: 46,882 | Forks: 4,360 | License: Apache-2.0 | 语言: Python | 创建: 2026-03-08 | arXiv: 2606.03854
