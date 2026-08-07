---
title: "diffusionstudio/lottie"
slug: "diffusionstudio-lottie"
date_added: "2026-06-11"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "🎬"
stars: "5,075 stars"
stars_delta: "forks 275，从 2K 增至 5K+"
language: "TypeScript"
license: "MIT"
score: 78
tags: ["lottie", "animation", "claude-code", "ai-design", "codex", "text-to-lottie"]
url: "https://github.com/diffusionstudio/lottie"
homepage: "https://diffusion.studio"
---

# diffusionstudio/lottie (Text-to-Lottie)

## 一句话定位

开源框架，通过 Claude Code、Codex 或任何支持 Skills 的 Coding Agent 生成生产级 Lottie 动画（Text-to-Lottie），安装方式：`npx skills add diffusionstudio/lottie`。

## 它解决的问题

Lottie 动画是移动端和 Web 的工业标准格式，但制作 Lottie 需要专业设计工具和技能。该项目让 AI Agent 直接生成可用的 Lottie JSON 文件，包含内置播放器和实时编辑预览。Y Combinator F24 批次公司出品。

## 为什么值得关注

1. **5,075 stars / 275 forks**，MIT 许可证，从 2K 快速增长到 5K+
2. **AI → 生产资产**：不是概念验证，直接生成标准 Lottie JSON，兼容所有 Lottie 播放器
3. **Agent 原生集成**：作为 Skill 安装，Claude Code / Codex 直接调用
4. **实时预览**：Agent 编辑 Lottie 时播放器实时更新，可检查、拖拽、精修
5. **Y Combinator F24**：有商业 backing
6. 提供详细的 prompt guide（grounding、motion design 术语、camera 操作、FPS/duration 控制）

## 热度来源判断

- **Lottie 刚需格式 + AI 生成设计资产爆发 + Agent 工具链集成**
- 设计工具链 AI 化的代表项目
- 从 2K 增至 5K+，增速持续
- 有实际 demo GIF 展示生成效果

## 关键技术亮点

1. **Skill 化分发**：`npx skills add diffusionstudio/lottie`，符合 agentskills.io 标准
2. **Scene + Project 架构**：每个动画是 project 下的 scene，从 `public/projects/<project>/<scene>/lottie.json` 自动加载
3. **实时编辑预览**：Agent 编辑时播放器实时更新
4. **生成标准 Lottie JSON**：兼容 lottie-web、React Native Skia（Skottie）、After Effects
5. **Prompt guide 工程化**：5 条原则（grounding、motion 术语、camera 思维、controls 请求、FPS/duration）

## 架构启发

**AI 生成设计资产的关键不是「能生成」，而是「生成的东西能直接进产品」。** Lottie 格式的标准化使得 AI 输出可以直接进入产品流程。Scene + Project 的文件组织模式让 Agent 可以增量编辑而非每次全量重生成。

## 定位判断

**工具型。** 有明确的单一用途（生成 Lottie），不会演化为平台。但代表了设计工具链 AI 化的趋势。

## 风险 / 局限 / 泡沫点

1. **动画质量上限待验证** — AI 生成的动画创意和复杂度可能受限
2. **单一用途** — 只做 Lottie，扩展性有限
3. **依赖模型能力** — 动画生成质量高度依赖 LLM 理解设计意图和 SVG 路径的能力
4. **需要 grounding 素材** — prompt guide 明确建议提供 SVG/截图，纯文本生成效果较差

## 与同类项目的关系

- **LottieFiles / lottie-web**：播放器生态，Text-to-Lottie 生成兼容这些播放器的文件
- **After Effects**：传统 Lottie 制作工具，Text-to-Lottie 可导入 AE 进一步精修
- **其他 AI 设计工具（Galileo AI 等）**：AI 生成 UI/设计资产，Text-to-Lottie 聚焦动画格式
- **diffusion.studio**：出品公司的商业产品

## 是否值得持续跟踪

**观察。** 工具型但增速快，代表设计资产 AI 化趋势。关注其是否能扩展到更多设计资产格式。

## 后续观察点

1. 生成动画的复杂度和质量提升（从简单图标动画到复杂场景）
2. 在实际产品中的使用情况
3. 是否扩展到其他设计资产格式（GIF、WebM、3D 动画）
4. Y Combinator 背景下的商业化路径
5. prompt guide 的演进和生成质量的关系
