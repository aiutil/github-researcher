---
title: "Anything Analyzer"
slug: "anything-analyzer"
date_added: "2026-04-18"
category: "工具型/平台候选"
emoji: "🔍"
stars: "1,269 stars"
stars_delta: "5天1.3K星"
language: "TypeScript"
score: 77
tags: ["Protocol Analysis", "MITM", "AI Reverse Engineering", "MCP", "Electron"]
url: "https://github.com/Mouseww/anything-analyzer"
---

# Anything Analyzer

## 一句话定位
全场景协议分析工具：浏览器抓包 + MITM 代理 + AI 分析 + MCP Server，让 AI 自动逆向分析任何来源的流量。

## 它解决的问题
传统工具各管一摊：DevTools 只看浏览器、Fiddler/Charles 只做代理、Wireshark 看不了 HTTPS。抓完包还得手动翻几百条请求。Anything Analyzer 统一了所有流量来源，并让 AI 自动分析。

目标用户：安全研究员、API 逆向工程师、自动化测试工程师。

## 为什么值得关注（2026-04-18）
5天 1,269 星，293 forks。MCP Server 集成是亮点——协议分析结果可以直接被 Claude Code 等 Agent 消费，形成"抓包→分析→自动化"闭环。

## 热度来源判断
- 解决了真实痛点：多工具切换 + 手动分析
- AI 分析 + MCP 集成是差异化
- 中文开发者社区传播是主要驱动力
- 高 fork 数（293）表明有实际使用需求

## 关键技术亮点
1. **双通道抓包**：内嵌浏览器（CDP）+ MITM 代理（8888 端口），覆盖全场景
2. **统一 Session 模型**：网页、桌面应用、终端、脚本、手机流量汇入同一会话
3. **AI 智能分析**：一键生成协议逆向 / 安全审计 / 加密分析报告
4. **内置 MCP Server**：分析结果直接对接 AI Agent，形成自动化闭环

## 架构启发
"AI 原生工具链"的好案例——不是给传统工具加 AI，而是以 AI 为核心重新设计工具链。MCP Server 作为输出接口，使得工具从"人看结果"进化为"Agent 消费结果"。

## 定位判断
AI 驱动的协议分析平台。MCP 集成使其有可能成为自动化测试和安全审计的基础设施组件。

## 风险 / 局限 / 泡沫点
1. **MITM 合规风险**：中间人代理在企业环境使用可能违反安全策略
2. **Electron 体积**：桌面应用较重，不利于轻量化部署
3. **AI 分析准确性**：协议逆向的 AI 分析质量尚需验证

## 与同类项目的关系
- **Charles/Fiddler**：传统 MITM 代理，无 AI 分析
- **mitmproxy**：Python 命令行 MITM 工具，更偏开发者
- **Postman**：API 测试，不做协议逆向
- **ZAP (OWASP)**：安全测试，更偏企业级

## 是否值得持续跟踪
是。MCP + 协议分析是 Agent 工具链的重要方向。

## 后续观察点
1. MCP Server 的标准化程度和扩展性
2. AI 分析报告的准确性和实用性
3. 企业安全团队是否采用

---
*首次记录：2026-04-18*
