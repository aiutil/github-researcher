---
title: "Graphify-Labs/graphify"
slug: "graphify"
date_added: "2026-04-26"
last_seen_date: "2026-08-11"
category: "平台候选"
emoji: "🧠"
stars: "105,100 stars"
stars_delta: "从84.5K到105K（3个月），日均~230 stars，持续攀升"
language: "Python"
license: "Apache-2.0"
score: 92
tags: ["graphrag", "knowledge-graph", "tree-sitter", "agent-skill", "claude-code", "codex", "cursor", "gemini-cli", "ast"]
url: "https://github.com/Graphify-Labs/graphify"
---

# Graphify-Labs/graphify — 把代码库变成可查询的知识图谱

## 一句话定位
Graphify 是一个跨 Agent 平台的代码知识图谱 Skill，用确定性 AST 解析（tree-sitter）将整个代码库（代码、文档、PDF、图片）转化为可查询的知识图谱——不是向量索引，而是真正的图遍历，支持 Claude Code、Cursor、Codex、Gemini CLI 等 20+ 平台。

## 它解决的问题
Coding Agent 在大型代码库中工作时，每次请求都需要重新理解代码结构，消耗大量 token 和工具调用（grep/read 循环）。Graphify 预先构建代码的知识图谱，让 Agent 直接查询结构化的代码关系（调用链、导入关系、继承层级），而非反复读取源文件。更重要的是，它不是向量检索——不依赖 embedding，而是确定性的 AST 解析 + 图遍历。

## 为什么值得关注（2026-08-11）
- **105,100 stars**（截至 2026-08-11），Apache-2.0 许可
- **10,225 forks**，社区贡献极其活跃（fork/star 比近 10%，典型网络效应）
- **356 subscribers**，开发者深度关注
- **YC S26 批次**（Y Combinator），已进入商业化阶段
- **官方网站 graphify.com** 已开放早期访问，平台化路径明确
- **LOCOMO Benchmark 领先**：recall@10 达到 0.497（mem0 仅 0.048，supermemory 0.149）
- **31 种语言 README 翻译**，全球化运营
- **PyPI 发布**：`pip install graphifyy`，安装门槛极低
- 代码解析完全本地（tree-sitter），零 LLM 消耗

## 热度来源判断
**真实需求 + 平台化预期 + YC 背书。** Agent 平台碎片化和大代码库 token 消耗是双重真实痛点。Graphify 的核心创新不是"又一个 RAG"，而是"不是向量索引"——用确定性 AST + 图遍历替代概率性 embedding 检索，这个技术判断击中了 GraphRAG 的核心争论。105K stars 中有趋势追逐成分（fork 比例异常高），但 YC S26 背书和实际 benchmark 数据支撑了核心价值。商业化平台 app.graphify.com 的开放说明团队在认真做产品。

## 关键技术亮点亮点
1. **确定性 AST 解析（tree-sitter）**：支持 ~40 种语言的 `calls`/`imports`/`inherits`/`mixes_in` 关系提取，无需 LLM，完全本地运行，代码不离开机器
2. **每条边都有解释**：每个连接标记为 `EXTRACTED`（源码中显式存在）或 `INFERRED`（由 graphify 推断），可追溯
3. **不是向量索引**：零 embedding，零向量存储——真正的图遍历，可查路径、解释概念、追溯关系
4. **Leiden 社区检测**：自动将图分割为子系统（社区），无需 LLM 即可生成标签
5. **三文件输出**：`graph.html`（浏览器可视化）+ `GRAPH_REPORT.md`（关键概念和连接摘要）+ `graph.json`（可查询的完整图）
6. **查询命令**：`graphify explain "APIRouter"`（解释节点）、`graphify path "FastAPI" "ModelField"`（追溯路径）、`graphify query "问题"`（自然语言子图）
7. **超越代码**：文档、PDF、图片、视频/音频都可映射到同一个图中（语义层使用 LLM，可选）

## 架构启发
- **确定性 > 概率性**：代码结构是确定的，不该用概率性 embedding 来表示——tree-sitter AST 是正确选择
- **图遍历 > 向量近邻**：查"A 调用了 B 吗"和"从 A 到 B 的路径"这类问题，图遍历比向量检索精准得多
- **Skill 即分发渠道**：Graphify 不卖工具，而是作为 Skill 分发到 20+ Agent 平台——这是 Agent 生态的新型分发模式
- **知识图谱作为 Agent 基础设施层**：Agent = Base Model + Skill Layer + Knowledge Graph + Memory Layer，Graphify 锁定 Knowledge Graph 层

## 定位判断
**平台候选**，且平台化路径已明确。Graphify 已从单一工具升级为知识图谱平台（graphify.com），目标是从 on-demand 查询升级为 always-on 的背景知识服务。在 Agent 生态五层架构中，锁定知识图谱/代码理解层。若成功，可能成为代码知识图谱的"npm"。

## 风险 / 局限 / 泡沫点
1. **增量更新效率**：代码频繁变化时，图谱的增量更新性能待验证（当前需重新运行 `/graphify`）
2. **882 个 Open Issues**：社区问题处理压力较大，可能影响质量口碑
3. **商业化与开源的平衡**：YC 背书意味着有融资压力，开源版可能功能受限
4. **与 IDE 内置索引竞争**：JetBrains/VS Code 都有内置代码索引，Graphify 的差异化在 Agent 集成
5. **graph.json 规模**：大型代码库（100K+ 文件）的图可能过大，影响查询效率
6. **105K stars 的增速异常**：fork 比近 10% 可能含营销驱动成分

## 与同类项目的关系
- **vs LlamaIndex**：LlamaIndex 更偏通用 RAG 框架，Graphify 专注代码知识图谱
- **vs codegraph (65.8K⭐)**：codegraph 也做代码图谱但偏 token 优化，Graphify 更偏知识图谱查询和可视化
- **vs Sourcegraph**：Sourcegraph 做代码搜索，Graphify 做知识图谱遍历，不同范式
- **vs mem0**：mem0 做 Memory 层，Graphify 做 Knowledge 层，互补
- **vs garden-skills**：garden-skills 是 Skill 合集，Graphify 是 Skill 编排框架

## 是否值得持续跟踪
**是。** 知识图谱作为 Agent 基础设施层是确定性趋势，Graphify 是该方向目前最成熟的开源实现，且已进入商业化（YC S26）。

## 后续观察点
1. graphify.com 平台的 always-on 功能发布和定价模式
2. 增量更新能力的实现（代码变更后自动同步图谱）
3. 大型代码库（100K+ 文件）的性能基准
4. 主流 Agent 平台是否官方集成
5. 企业级应用案例积累
6. 与 codegraph 的竞争/合作关系演变

---
> 数据来源: GitHub API (2026-08-11) | Stars: 105,100 | Forks: 10,225 | License: Apache-2.0 | 语言: Python | 创建: 2026-04-03
