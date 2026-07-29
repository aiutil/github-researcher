---
title: "Google Workspace CLI"
slug: "google-workspace-cli"
date_added: "2026-04-26"
category: "生产可用"
emoji: "📁"
stars: "25.4k stars"
stars_delta: "稳步增长"
language: "Rust"
score: 74
tags: ["google", "cli", "productivity", "agent-tool"]
url: "https://github.com/googleworkspace/cli"
---

# Google Workspace CLI

## 一句话定位
Google 官方统一 CLI 工具，一个命令行工具覆盖 Drive、Gmail、Calendar、Sheets、Docs、Chat、Admin。

## 它解决的问题
Google Workspace API 分散、认证复杂、每个服务有独立的 SDK。官方 CLI 统一了这些接口，降低自动化门槛。

## 为什么值得关注（2026-04-26）
Google 自己下场做统一 CLI，这是平台厂商拥抱 Agent-Native 的强烈信号。Rust 编写，性能和可靠性有保障。

## 热度来源判断
真实需求驱动。企业大量使用 Google Workspace，统一 CLI 是刚需。

## 关键技术亮点
1. Rust 编写，性能优秀、资源占用低
2. 动态发现 API，自动适配新 Workspace 服务
3. OAuth2 内置，认证流程简化

## 架构启发
当平台厂商开始提供 CLI 优先接口时，说明 Agent-Native 基础设施正在成熟。企业内部也应考虑：所有对内服务都提供 CLI 接口。

## 定位判断
生产可用。Google 官方出品，可直接用于自动化场景。

## 风险 / 局限 / 泡沫点
1. 依赖 Google API，国内使用受限
2. 功能覆盖仍在迭代，部分 API 可能不完整
3. 企业级权限管理需要额外配置

## 与同类项目的关系
- vs **CLI-Anything**：CLI-Anything 做通用，Google CLI 做自家生态
- vs **n8n Google 节点**：n8n 通过 GUI 操作 Google API，CLI 更适合 Agent 调用

## 是否值得持续跟踪
是。作为 Agent 调用 SaaS 的标杆案例。

## 后续观察点
- 是否成为 Agent 平台的标准 Google 集成方式
- API 覆盖完整度
- 企业采纳情况
