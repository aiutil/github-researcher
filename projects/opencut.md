---
title: "OpenCut"
slug: "opencut"
date_added: "2026-07-14"
category: "平台候选"
emoji: "🎬"
stars: "66,019 stars"
stars_delta: "日增 1,077"
language: "TypeScript / Rust"
score: 85
tags: ["video-editor", "rust", "mcp-server", "agent-native", "creator-tools", "open-source"]
url: "https://github.com/OpenCut-app/OpenCut"
---

# OpenCut

## 一句话定位
开源的 CapCut 替代品，正在用 Rust 从头重写，内建 MCP Server、Headless 批渲染和插件系统，定位为 Agent 原生的视频创作基础设施。

## 它解决的问题
短视频创作者依赖 CapCut 等闭源工具，面临水印、订阅费、数据上传隐私风险、无法批量自动化等问题。OpenCut 提供完全开源、本地运行、可脚本化、可被 Agent 驱动的替代方案。

## 为什么值得关注（2026-07-14）
66K⭐ 日增 1K+，在 GitHub Trending 日榜排名第一。关键不只是"开源 CapCut 替代"——而是它在重写中明确加入了 MCP Server（让 AI Agent 直接调用视频编辑能力）和 Headless 模式（批量渲染/自动化），这意味着 OpenCut 正在从"人用手操作的工具"进化为"Agent 用 API 驱动的创作平台"。

## 热度来源判断
- CapCut 在美国多州被封禁，用户急需替代品——真实需求驱动
- 66K 星中相当一部分来自"开源替代"社区效应
- Rust 重写 + MCP Server 的技术路线吸引开发者关注
- fal.ai 等生成式 AI 公司赞助，暗示与 AI 内容生成的深度整合

## 关键技术亮点
1. **Rust 核心重写**：桌面、移动、浏览器共享同一代码库，性能与可维护性大幅提升
2. **MCP Server 内建**：Agent 可通过 MCP 协议直接操作视频编辑流程（剪辑/转场/字幕/导出）
3. **Headless 批渲染模式**：无需 GUI，支持自动化批量视频生产
4. **插件优先架构**：第三方插件作为一等公民，支持扩展功能生态
5. **编辑器内建脚本面板**：直接在编辑器中写脚本控制视频生产

## 架构启发
OpenCut 的重写路线图揭示了一个重要趋势：**创作工具正在从 GUI-first 转为 API-first + GUI-optional**。当工具内建 MCP Server，它就从"人用的工具"变成了"Agent 用的平台"。这种架构模式可推广到所有创作工具领域（图片/音频/3D/文档）。

## 定位判断
在 Agent 创作工具生态中，OpenCut 占据"视频编辑基础设施"的位置。如果 MCP Server 落地，它将成为 Agent 视频生产流水线的标准后端。

## 风险 / 局限 / 泡沫点
1. **重写尚未完成**：当前 opencut.app 仍运行旧版，新版在 new.opencut.app 开发中，不接受外部贡献——架构未稳定
2. **社区热度可能流失**：重写期间无法让社区参与开发，星标增长≠实际使用
3. **MCP Server 是路线图而非现实**：目前仅在 README 中提及，尚无实现
4. **与专业工具差距大**：DaVinci Resolve、Final Cut Pro 的专业能力远超 OpenCut

## 与同类项目的关系
- **CapCut（闭源）**：OpenCut 直接对标，但 CapCut 有字节跳动的资源投入
- **Augani/openreel-video（4.2K⭐）**：另一个开源视频编辑器，纯浏览器端，无 MCP/Agent 定位
- **heygen-com/hyperframes（34.8K⭐）**：写 HTML 渲染视频，面向 Agent，但路线完全不同

## 是否值得持续跟踪
**是。** MCP Server + Headless 渲染的组合如果落地，将开创 Agent 驱动视频生产的范式。

## 后续观察点
1. MCP Server 的具体实现——什么时候可用、API 设计如何
2. Rust 重写完成度——new.opencut.app 何时取代旧版
3. 插件生态是否有真实第三方参与
4. Headless 批渲染的实际应用场景（批量广告/个性化视频/模板化生产）

---
*首次记录：2026-07-14*
