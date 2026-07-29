---
category: 工具型
date_added: '2026-04-07'
emoji: 📄
github_url: https://github.com/qmd-project/qmd
mcp: true
poc_recommend: false
score: 51
stars_per_day: 394
summary: 本地 CLI 文档搜索引擎，BM25 + 向量 + LLM 重排，全本地跑 GGUF 模型。
tech_stack: TypeScript
title: qmd
total_stars: 18.8k
---

# qmd — 本地 CLI 搜索引擎

> 2026-04-07 新增跟踪

---

## 基本信息

| 字段 | 值 |
|------|------|
| GitHub | https://github.com/tobi/qmd |
| Stars | 18,843（总） / 394（今日） |
| 语言 | TypeScript |
| 作者 | @tobi |

---

## 它是做什么的

**mini cli search engine for your docs, knowledge bases, meeting notes**

一个本地运行的文档搜索引擎，结合 BM25 全文检索 + 向量语义搜索 + LLM 重排，全部跑在本地（通过 node-llama-cpp + GGUF 模型）。支持 MCP Server 暴露工具给 AI Agent。

核心功能：
- **keyword search**：`qmd search "project timeline"` — 快速关键词搜索
- **semantic search**：`qmd vsearch "how to deploy"` — 向量语义搜索
- **hybrid reranking**：`qmd query "quarterly planning process"` — BM25 + 向量 + LLM 重排，质量最高
- **context 树**：`qmd context add qmd://notes "Personal notes and ideas"` — 为检索结果提供上下文，帮助 LLM 做更好选择
- **MCP Server**：`qmd mcp` — 暴露 query/get/multi_get/status 工具给 Claude Desktop、Claude Code 等
- **agentic 格式输出**：`--json`、`--all --files --min-score 0.3` 等专为 Agent 设计的输出格式

安装：
```bash
npm install -g @tobilu/qmd
# 或
bun install -g @tobilu/qmd
```

---

## 它为什么火

1. **隐私优先 + 全本地运行**：在 AI Agent 越来越热的时候，本地文档隐私成为强需求。
2. **MCP 协议集成**：MCP Server 暴露让 qmd 可以无缝接入 Claude Desktop、Claude Code、Windsurf 等 AI 工具。
3. **context 树机制**：这是 qmd 最有特色的设计——不是返回文档片段，而是返回"上下文树"，让 LLM 更好地理解文档层级关系。
4. **纯 npm 安装**：零门槛，本地跑 LLM 模型（GGUF），不需要 GPU。

---

## 真正的技术亮点

1. **混合检索 + LLM 重排**：BM25（精确）+ 向量（语义）+ LLM reranking（质量最优），三层级联。
2. **context 树机制**：文档的层级关系被编码为 context 树，返回结果时带着父级上下文。这个设计让 Agent 能理解"这份文档在哪里、它和什么相关"，而不只是匹配关键词。
3. **全本地 LLM**：通过 node-llama-cpp 跑 GGUF 模型，不需要云端 API，纯本地推理。
4. **MCP Server 原生集成**：query、get、multi_get、status 四个工具直接暴露为 MCP 工具，Claude Code 一行配置即可使用。

---

## 解决的问题是否真实存在

**真实，是强需求。**

开发者有大量本地文档：Notes、Meeting transcripts、Work docs、Knowledge bases。AI Agent 时代，如何让 Agent 精准检索这些本地文档是个真实问题。qmd 用纯本地方案解决了隐私 + 离线 + AI Agent 集成三个需求。

---

## 它更偏玩具、工具、平台还是基础设施

**工具型，但有基础设施潜力。**

qmd 目前是一个 CLI 工具，但它的定位是"Agent 的本地记忆系统"。如果 AI Agent 的本地上下文管理成为标配（这很可能是趋势），qmd 这类工具会从工具演化为基础设施组件。

---

## 它属于短期热点还是中期趋势

**中期趋势。**

隐私优先的本地文档检索 + AI Agent 集成是持续需求，不会在短期内消失。但竞品（ripgrep + LLM、pagefind、Elasticsearch 本地版）也在发展，qmd 需要在 context 树等差异化能力上持续强化。

---

## 对架构师最有价值的启发

1. **context 树设计**：检索结果不只是"相关文档列表"，而是带着层级上下文的树状结构。这个设计让 Agent 能做更智能的上下文选择，而不只是关键词匹配。
2. **Agent 记忆系统的本地化路径**：qmd 是"个人知识库 + AI Agent"的一个轻量级解法。如果企业内部需要类似能力，qmd 的架构值得参考。
3. **MCP 工具暴露**：把搜索能力通过 MCP 暴露给 AI Agent，比 API 更规范，比插件更通用。

---

## 是否值得持续跟踪

**是，持续跟踪。**

如果 MCP 协议成为标准，类似 qmd 的 MCP-native 工具会越来越多。qmd 的 context 树机制是差异化亮点，值得观察它是否能在竞争中保持优势。

---

## 是否值得企业内部做 PoC

**可以小范围尝试。**

适合场景：团队成员有大量本地文档（会议记录、技术文档、个人笔记），且对数据隐私有要求。使用 qmd + Claude Code 可以快速构建本地知识检索能力。

---

## 风险、局限、泡沫点

1. **竞品压力**：pagefind（静态站点搜索）、ripgrep + LLM 等方案成熟后，qmd 的差异化会缩小。
2. **模型质量依赖**：全本地 GGUF 模型的质量直接影响搜索效果，不同模型差异大。
3. **不支持多用户协作**：纯本地设计，不适合团队共享知识库场景。
4. **index 更新成本**：每次文档变化需要重新 embed，大文档库索引成本不可忽视。

---

## 是否值得沉淀进长期研究仓库

**值得持续跟踪。**

标签：**值得跟踪 | Agent 记忆基础设施 | MCP 生态**

---

## 评分

| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 7 | 394/day，稳健增长，但总量 18.8k 与增长速率有一定背离 |
| 技术创新度 | 7 | context 树 + 混合检索 + 全本地 LLM，工程实现扎实 |
| 工程成熟度 | 7 | npm 发布，MCP 集成完整，文档清晰 |
| 架构启发价值 | 8 | Agent 本地记忆系统的轻量级参考实现 |
| 企业落地潜力 | 5 | 单用户本地工具，多用户协作场景需定制 |
| 中期趋势概率 | 7 | 本地隐私 + AI Agent 需求是持续趋势 |
| 平台化潜力 | 4 | 工具定位明确，平台化路径不清晰 |
| 基础设施潜力 | 6 | Agent 本地记忆层有基础设施潜力，但依赖 MCP 生态 |
| **总分** | **51/80** | |

**归类：工具型 | 建议持续跟踪**
