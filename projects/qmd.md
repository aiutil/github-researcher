---
title: "qmd"
slug: "qmd"
date_added: "2026-04-07"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "📄"
stars: "18,843"
language: "TypeScript"
score: 51
tags: ["local-search", "cli", "mcp", "bm25", "vector-search", "reranking"]
url: "https://github.com/qmd-project/qmd"
---

# qmd

## 一句话定位
本地 CLI 文档搜索引擎，结合 BM25 全文检索 + 向量语义搜索 + LLM 重排，全本地跑 GGUF 模型，支持 MCP Server 暴露工具给 AI Agent。

## 它解决的问题
开发者有大量本地文档（Notes、Meeting transcripts、Work docs、Knowledge bases），AI Agent 时代如何让 Agent 精准检索这些本地文档是个真实问题。qmd 用纯本地方案解决了隐私 + 离线 + AI Agent 集成三个需求。现有的本地搜索要么只做关键词匹配（ripgrep），要么依赖云端 API（隐私风险），qmd 提供了全本地的混合检索方案。

## 为什么值得关注
- **隐私优先 + 全本地运行**：通过 node-llama-cpp + GGUF 模型，不需要 GPU 和云端 API
- **MCP 协议集成**：暴露 query/get/multi_get/status 工具给 Claude Desktop、Claude Code 等
- **context 树机制**：返回带层级上下文的树状结构，不是简单的文档片段
- **混合检索 + LLM 重排**：BM25（精确）+ 向量（语义）+ LLM reranking（质量最优）三层级联
- **纯 npm 安装**：`npm install -g @tobilu/qmd`，零门槛
- **agentic 格式输出**：`--json`、`--all --files --min-score 0.3` 等专为 Agent 设计

## 热度来源判断
- AI Agent 越来越热，本地文档隐私成为强需求
- MCP 协议成为标准让 MCP-native 工具获得增长红利
- 394/day 增速稳健，总量 18.8k
- 隐私优先 + 全本地是差异化的市场定位

## 关键技术亮点
1. **混合检索 + LLM 重排**：BM25（精确）+ 向量（语义）+ LLM reranking（质量最优），三层级联
2. **context 树机制**：文档的层级关系被编码为 context 树，返回结果时带着父级上下文。让 Agent 能理解"这份文档在哪里、它和什么相关"
3. **全本地 LLM**：通过 node-llama-cpp 跑 GGUF 模型，不需要云端 API，纯本地推理
4. **MCP Server 原生集成**：query、get、multi_get、status 四个工具直接暴露为 MCP 工具

## 架构启发
1. **context 树设计**：检索结果不只是"相关文档列表"，而是带着层级上下文的树状结构
2. **Agent 记忆系统的本地化路径**：qmd 是"个人知识库 + AI Agent"的轻量级解法
3. **MCP 工具暴露**：把搜索能力通过 MCP 暴露给 AI Agent，比 API 更规范，比插件更通用

## 定位判断
**工具型** — 目前是 CLI 工具，但定位是"Agent 的本地记忆系统"。如果 AI Agent 的本地上下文管理成为标配，有从工具演化为基础设施组件的潜力。

## 风险/局限/泡沫点
1. **竞品压力**：pagefind（静态站点搜索）、ripgrep + LLM 等方案成熟后，差异化会缩小
2. **模型质量依赖**：全本地 GGUF 模型的质量直接影响搜索效果，不同模型差异大
3. **不支持多用户协作**：纯本地设计，不适合团队共享知识库场景
4. **index 更新成本**：每次文档变化需要重新 embed，大文档库索引成本不可忽视

## 与同类项目的关系
| 项目 | 定位 | 关系 |
|------|------|------|
| ripgrep | CLI 文本搜索 | 竞品：ripgrep 做精确匹配，qmd 做语义搜索 |
| pagefind | 静态站点搜索 | 竞品：不同场景的本地搜索 |
| Elasticsearch 本地版 | 全文搜索引擎 | 竞品：更重但功能更全 |

## 是否值得持续跟踪
**是，持续跟踪** — 如果 MCP 协议成为标准，类似 qmd 的 MCP-native 工具会越来越多。context 树机制是差异化亮点。

## 后续观察点
- context 树机制在竞品压力下能否保持差异化优势
- MCP 生态发展对 qmd adoption 的推动
- 是否演进支持多用户/团队共享知识库场景
- GGUF 模型质量提升对搜索效果的影响
