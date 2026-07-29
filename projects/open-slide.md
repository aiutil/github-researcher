---
title: "Open Slide"
slug: "open-slide"
date_added: "2026-05-05"
category: "工具型"
emoji: "📽️"
stars: "2,624 stars（实测）"
stars_delta: "10 天 2.6K，稳步增长"
language: "TypeScript"
score: 74
tags: ["slides", "agent", "presentation", "react", "agent-native"]
url: "https://github.com/1weiho/open-slide"
---

# Open Slide

## 一句话定位
为 AI Agent 构建的幻灯片生成框架，Agent 原生的 PPT 生成方案。

## 它解决的问题
**目标用户：** 需要自动化生成演示文稿的开发者和知识工作者。

**痛点：**
- 传统 PPT 生成工具（python-pptx、Slidev 等）不是为 Agent 设计的
- Agent 生成 PPT 需要专门的框架：结构化输入、模板系统、输出格式
- 现有 Skill（如 PPT Skill for Claude Code）分散且不统一

## 为什么值得关注（2026-05-05）
"Agent 生成 PPT" 是当前 Agent Skill 生态中的高频需求（多个 PPT Skill 同时上 Trending）。Open Slide 试图做一个通用的 Agent Slide 框架，而非单次 Skill。方向正确但验证不足。

## 热度来源判断
- **Skill 生态带动** — PPT 生成是 Agent Skill 的高频场景
- **真实需求** — 自动化 PPT 生成在企业场景有应用
- **竞争激烈** — 同时存在多个 PPT Skill 项目，赛道拥挤

## 关键技术亮点
1. **Agent-First 设计** — API 专为 Agent 调用优化，结构化输入输出
2. **React 组件系统** — 基于 React 的幻灯片渲染，可定制性强
3. **多格式输出** — 支持网页、PDF 等多格式导出

## 架构启发
- Agent 生成内容的标准化：如果 Agent 要生成 PPT/文档/报告，需要标准化的中间格式
- "Agent-Native" 框架设计：API 设计从 Agent 调用场景出发，而非人类操作场景

## 定位判断
**工具型。** 在 Agent Skill 生态中是一个垂直工具。需要与大量同类 PPT Skill 竞争。

## 风险 / 局限 / 泡沫点
1. **赛道拥挤** — PPT Skill 项目泛滥，差异化困难
2. **需求验证不足** — Agent 生成 PPT 是否真的是高频刚需？
3. **质量天花板** — 自动生成的 PPT 质量是否能满足商业场景？

## 与同类项目的关系
- **guizang-ppt-skill（4.9K stars）** — 杂志风格 HTML PPT Skill，单 Skill 路线
- **ppt-image-first** — 以图片为主的 PPT Skill
- **Open Slide** — 试图做通用框架路线

## 是否值得持续跟踪
**有限跟踪。** 需要观察是否能在 PPT Skill 红海中脱颖而出。

## 后续观察点
1. 是否获得 Agent 框架（Claude Code、Codex）的官方集成
2. 与同类 PPT Skill 的差异化是否足够清晰

---
*首次记录：2026-05-05*
