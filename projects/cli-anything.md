---
title: "CLI-Anything"
slug: "cli-anything"
date_added: "2026-04-26"
category: "基础设施候选"
emoji: "🔌"
stars: "32.6k stars"
stars_delta: "稳步增长"
language: "Python"
score: 76
tags: ["cli", "agent-native", "integration", "universal-adapter"]
url: "https://github.com/HKUDS/CLI-Anything"
last_seen_date: "2026-05-19"
---

# CLI-Anything

## 一句话定位
将所有软件变为 Agent 可调用的 CLI 接口——Making ALL Software Agent-Native。

## 它解决的问题
Agent 要操控 GUI 软件非常困难（需要浏览器自动化、OCR、坐标点击）。CLI-Anything 的思路是先把 GUI 软件变成 CLI，再让 Agent 通过标准 CLI 协议调用。

## 为什么值得关注（2026-04-26）
32.6K Stars，来自港大团队，定位极具野心。Agent-Native 接口标准化是当前最热门的架构话题之一。

## 热度来源判断
概念驱动为主。"万物 Agent-Native"的愿景吸引眼球，但实际覆盖率需要验证。

## 关键技术亮点
1. 自动发现 GUI 软件的可操作入口并生成 CLI 包装
2. 标准 CLI 协议让任何 Agent 都能调用
3. 接口适配器模式在 Agent 时代的新应用

## 架构启发
与其让 Agent 学会操作所有 GUI，不如先把 GUI → CLI 标准化。这是经典的适配器模式在 AI 时代的应用。企业架构师应考虑：所有内部工具都应暴露 CLI 接口。

## 定位判断
基础设施候选。如果 CLI 成为 Agent 调用标准接口，CLI-Anything 就是转换层。

## 风险 / 局限 / 泡沫点
1. GUI 软件变化频繁，CLI 包装层维护成本极高
2. 很多 GUI 操作有复杂状态依赖，CLI 化不完整
3. "ALL Software"的定位过于宏大，实际覆盖率存疑

## 与同类项目的关系
- vs **Google Workspace CLI**：Google 自家产品 CLI 化，CLI-Anything 做通用化
- vs **OpenCLI**：OpenCLI 偏 Web → CLI，CLI-Anything 偏 Desktop Software → CLI

## 是否值得持续跟踪
是。Agent-Native 接口标准是确定趋势。

## 后续观察点
- 实际支持的软件覆盖范围
- 是否有 Agent 平台官方集成
- 是否形成 CLI-for-Agent 标准规范
