---
title: "qmd"
slug: "qmd"
date_added: "2026-04-07"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "📄"
stars: "deleted (404) — 原 18,843 stars"
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

## 关键技术亮点亮点
1. **混合检索 + LLM 重排**：BM25（精确）+ 向量（语义）+ LLM reranking（质量最优），三层级联
2. **context 树机制**：文档的层级关系被编码为 context 树，返回结果时带着父级上下文。让 Agent 能理解"这份文档在哪里、它和什么相关"
3. **全本地 LLM**：通过 node-llama-cpp 跑 GGUF 模型，不需要云端 API，纯本地推理
4. **MCP Server 原生集成**：query、get、multi_get、status 四个工具直接暴露为 MCP 工具

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | qmd 是 TypeScript CLI + MCP Server，节点为 CLI 用户与 MCP 客户端（如 Claude Desktop、Claude Code），运行依赖本地文档集合与 GGUF 模型（node-llama-cpp），离线无云端 API。 | 边界仅依据档案"一句话定位""MCP 协议集成""全本地 LLM"；未列具体文档格式、模型族、文件监听机制。 |
| 主路径 | 主路径为：本地文档 → BM25 全文检索 + 向量语义搜索 → LLM reranking（三层级联）→ context 树（含父级层级）→ MCP 工具（query / get / multi_get / status）或 CLI 输出（`--json`、`--all --files --min-score 0.3`）。 | 组件顺序与工具集合为档案明文；context 树内部编码方式、reranker 与向量索引的耦合细节档案未给。 |
| 关键权衡 | 隐私/离线（全本地 GGUF）↔ 模型质量与索引成本（每次文档变化需重新 embed，大库成本高）；单用户简洁 ↔ 不支持多用户协作。 | 权衡点均来自档案"风险/局限"与"为什么值得关注"；未给出量化性能、索引时延、模型基准。 |
| 最小 PoC | 在单机 Node 环境 `npm install -g @tobilu/qmd`，接入一份本地文档集合与一个 GGUF 模型，对 Claude Desktop 或 Claude Code 暴露 MCP 四个工具，以小语料验证 BM25+向量+rerank 端到端返回与 context 树形态。 | 安装命令、MCP 工具名、CLI flag 取自档案；未列模型下载来源、具体配置项与最低硬件门槛，待核验。 |

## 架构启发
1. **context 树设计**：检索结果不只是"相关文档列表"，而是带着层级上下文的树状结构
2. **Agent 记忆系统的本地化路径**：qmd 是"个人知识库 + AI Agent"的轻量级解法
3. **MCP 工具暴露**：把搜索能力通过 MCP 暴露给 AI Agent，比 API 更规范，比插件更通用

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    A[本地文档集合<br/>Notes/Meeting/Work docs/KB] --> D[索引与检索层<br/>BM25 + 向量语义]
    D --> E[LLM Reranking<br/>node-llama-cpp / GGUF<br/>模型细节待核验]
    E --> F[Context 树构建<br/>层级上下文编码方式待核验]
    F --> G[MCP Server<br/>query / get / multi_get / status]
    F --> H[CLI 输出<br/>--json / --all --files --min-score 0.3]
    G --> I[MCP 客户端<br/>Claude Desktop / Claude Code 等<br/>具体清单待核验]
    H --> J[CLI 用户]
    K[文档变更触发重 embed<br/>触发机制与成本待核验] --> D
</brief>
```

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
