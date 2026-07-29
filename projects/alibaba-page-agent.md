---
title: "alibaba/page-agent"
slug: "alibaba-page-agent"
date_added: "2026-06-24"
last_seen_date: "2026-06-26"
category: "平台候选"
emoji: "🎯"
stars: "19,760 stars"
stars_delta: "日增 196"
language: "TypeScript"
score: 86
tags: ["gui-agent", "dom-manipulation", "web-automation", "mcp", "browser-use", "in-page"]
url: "https://github.com/alibaba/page-agent"
---

# alibaba/page-agent

## 一句话定位
JavaScript in-page GUI agent——一段 JS 嵌入网页，即可用自然语言控制 DOM，不需要截图和多模态 LLM。

## 它解决的问题
传统 Web 自动化（browser-use、Playwright、Selenium）需要浏览器扩展、Python 环境、headless browser 或截图 + 多模态 LLM。成本高、延迟大、部署复杂。page-agent 把整个 GUI agent 压缩为一段 CDN 加载的 JS——零安装、零后端、零截图。

## 为什么值得关注（2026-06-24）
GitHub Trending 日榜连续出现，19.2K stars 且持续增长。代表了一种全新的 Web 交互范式——不是"自动化网页"，而是"赋予网页自然语言接口"。阿里巴巴背书，MIT 协议，生态可期。

## 热度来源判断
- **真实需求驱动**：SaaS 厂商需要 AI Copilot 嵌入产品，但不想重写后端
- **技术路线差异化**：不用多模态 LLM = 成本极低，用任何文本 LLM 即可
- **browser-use 生态延伸**：DOM 处理组件 derived from browser-use，有技术传承
- **阿里巴巴品牌**：大厂开源增加可信度

## 关键技术亮点
1. **纯文本 DOM 操作**：不截图、不多模态——基于 tree-sitter 式 DOM 解析，将页面结构化为文本传给 LLM，LLM 返回操作指令
2. **零依赖注入**：`<script src="cdn.../page-agent.js"></script>` 一行代码，无需浏览器扩展/Python/headless browser
3. **BYO LLM**：支持任何 OpenAI-compatible API（qwen3.5-plus、GPT 等），无供应商锁定
4. **MCP Server（Beta）**：外部 Agent 可通过 MCP 控制浏览器中的 page-agent
5. **Chrome 扩展（可选）**：支持跨页面多标签任务

## 架构启发
page-agent 的核心设计哲学是**"在页面内部解决，不绕道外部"**。传统 GUI agent 的链路是 `Agent → screenshot → multimodal LLM → coordinates → click`。page-agent 的链路是 `Page → DOM text → text LLM → DOM operation`。前者重、贵、慢；后者轻、快、便宜。trade-off 是复杂 Canvas/WebGL/视频内容无法通过 DOM 文本理解。

## 定位判断
**平台候选。** page-agent 定义了"In-page Agent"这一新品类。如果 SaaS 产品普遍嵌入 page-agent，它就成为了 Web 端 Agent 交互的标准层——类似 Stripe 之于支付、Auth0 之于认证。

## 风险 / 局限 / 泡沫点
1. **DOM 注入安全风险**：恶意页面可以构造陷阱 DOM 欺骗 Agent 执行危险操作
2. **复杂页面失效**：Canvas、WebGL、Video、复杂的 iframe 嵌套场景下 DOM 文本方案可能无效
3. **平台竞争**：browser-use 生态更大（截图方案），MCP 模式可能被浏览器原生 Agent 取代
4. **CDN 依赖**：demo CDN 使用阿里云测试 API，生产环境需要自行配置

## 与同类项目的关系
- **browser-use**：page-agent 的 DOM 处理组件 derived from browser-use，但路线不同（文本 vs 截图）
- **Playwright/Selenium**：传统 Web 自动化，需要编程，不是 Agent
- **Anthropic Computer Use**：全桌面截图方案，更通用但更重
- **firecrawl**：抓取层（Web → Data），page-agent 是操作层（Instruction → DOM Action）

## 是否值得持续跟踪
**是。** page-agent 代表了 GUI Agent 的"轻量级路线"，如果成功，将定义 Web 端 Agent 嵌入的标准模式。

## 后续观察点
1. SaaS 厂商是否开始在生产环境嵌入 page-agent
2. MCP Server 从 Beta 到稳定的时间线
3. 安全模型是否得到完善（目前 DOM 注入风险缺乏沙箱隔离）
4. 与 browser-use 是否会合并或分化为标准

---
*首次记录：2026-06-24*
