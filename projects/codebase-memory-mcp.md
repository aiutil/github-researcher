---
title: "codebase-memory-mcp"
slug: "codebase-memory-mcp"
date_added: "2026-06-20"
last_seen_date: "2026-07-12"
category: "基础设施候选"
emoji: "🧠"
stars: "30,110 stars"
stars_delta: "从 26.1K→30.1K（周增约 4K），总计从 8K→30.1K。增速趋稳但持续走高，进入基础设施级稳定增长期"
language: "C"
score: 92
tags: ["code-intelligence", "knowledge-graph", "mcp", "tree-sitter", "agent-infrastructure", "hybrid-lsp"]
url: "https://github.com/DeusData/codebase-memory-mcp"
---

## 2026-07-12 更新

stars 达到 30,110（从 7/5 的 26,117 增至 30,110，周增约 4K）。v0.9.0 发布（2026-07-08），30 名贡献者，220 open issues，5604 测试通过。SLSA 3 安全等级。arXiv 论文（2603.27277）发表。关键判断维持：Score 92（不变），基础设施候选定位进一步确认。

重要变化：
- 增速从爆发期进入稳定增长期，但周增 4K 仍是 MCP 生态顶级水平
- v0.9.0 功能趋于稳定，工程成熟度评分提升
- Hybrid LSP 已覆盖 10 语言（Python/TS/JS/JSX/TSX/PHP/C#/Go/C/C++/Java/Kotlin/Rust/Perl）
- Infrastructure-as-code indexing：Dockerfile/K8s manifests/Kustomize overlays 被索引为图节点
- 已成为 MCP 生态 Code Intelligence 赛道的事实标准

---

## 2026-07-05 更新

stars 达到 26,117（周增 10,186）。GitHub Trending 全球 #6。本周增速创历史新高。关键判断维持：Score 92（不变），基础设施候选定位进一步确认。重要信号：
- codebase-memory-mcp 已成为 MCP 生态中 code intelligence 赛道的标杆项目
- 与 cognee（27K⭐）形成 "代码记忆 + 通用记忆" 双子星格局，两者均在持续高速增长
- Agent 记忆层从创新变为标配，行业标准正在形成
- 企业 PoC 信号持续积极

---

## 2026-07-03 更新

stars 达到 24,603（周增 9,697，近乎翻倍）。GitHub Trending 全球 Top 4。增长继续加速，"基础设施候选" 定位进一步确认。关键变化：
- 与 cognee（26.6K⭐ 周+5.2K）形成 "代码记忆 + 通用记忆" 双子星格局
- "Agent 记忆层从可选变必选" 已成为行业共识
- Score 提升至 92（↑3），原因：增速翻倍 + Trending 榜首级别曝光 + 在 Agent 技术栈中的基础设施地位被广泛认可

---

## 2026-06-28 更新

stars 从 14.7K→17.5K（周增 2.8K）。与 cognee 并列为本周 "Agent 大脑层" 双子星。趋势确认：代码智能 MCP 正在从创新变为标配。新增观察：
- 与 cognee 的互补关系明确（代码理解 vs 通用记忆）
- 企业 PoC 信号积极
- 建议 codebase-memory-mcp + cognee 组合使用作为 Agent 知识层

---

## 2026-06-22 更新

stars 从 8K 增长到 10K（日增 1,029）。持续稳定增长表明这不是短期热度。新增观察：
- 基础设施即代码索引：Dockerfile/K8s manifests/Kustomize overlays 作为图节点
- 3D 交互式图谱可视化 UI（localhost:9749）
- .codebase-memory/graph.db.zst 可提交到仓库让队友跳过 reindex
- 11 agent 自动检测配置
- Hybrid LSP 语义类型解析扩展到 11 语言
- arXiv 预印本背书（2603.27277）
# codebase-memory-mcp

## 一句话定位

高性能代码智能 MCP Server——用 tree-sitter 将代码库索引为持久化知识图谱，158 语言、sub-ms 查询、120x token 削减，单个静态二进制零依赖。

## 解决的问题

Coding Agent（Claude Code、Codex 等）在理解大型代码库时依赖 `grep` + `read` 暴力搜索。这种方式 token 消耗巨大（Linux 内核级代码库需要 ~412K tokens），速度慢，且无法理解代码结构（调用链、类型关系、路由定义）。codebase-memory-mcp 用知识图谱将这个成本降低 120 倍。

## 为什么值得关注（2026-06-20）

日增 1,055 stars 达到 8,119，且有 arXiv 预印本（2603.27277）背书。在 31 个真实仓库上的评测结果：83% 答案质量、10x token 削减、2.1x 更少工具调用。这不是概念验证——是已验证的工程方案。C 语言编写的单静态二进制 + 零运行时依赖 + 自动检测 11 种 Coding Agent 并配置，工程完成度极高。

## 热度来源判断

**真实需求 + 极致工程。** Coding Agent 的代码理解效率是行业核心痛点。codebase-memory-mcp 不只是做了（tree-sitter 索引），还做到了极致（158 语言、Hybrid LSP 类型推断、Cypher 查询、3D 可视化）。arXiv 论文提供了学术可信度。日增 1,055 不是泡沫——是真实需求的映射。

## 关键技术亮点

1. **tree-sitter 知识图谱：** 158 种语言的 vendored grammar 编译进二进制，索引 Linux 内核（28M LOC, 75K 文件）仅需 3 分钟。产出包含 CALLS / IMPORTS / DEFINES / IMPLEMENTS / INHERITS / HTTP_CALLS / DATA_FLOWS / EMITS 等边的持久化图。

2. **Hybrid LSP 语义类型解析：** 用轻量 C 实现模拟 tsserver / pyright / gopls / rust-analyzer 的类型推断（参数绑定、返回类型推断、泛型替换），覆盖 11 种主流语言。

3. **多维度查询：** 14 个 MCP 工具——架构概览、调用图、死代码检测、Cypher 查询、语义搜索（bundled Nomic embeddings）、BM25 全文搜索、HTTP 路由匹配、基础设施即代码索引。

4. **团队协作：** 提交 `.codebase-memory/graph.db.zstd`（8-13:1 压缩），队友 clone 后增量索引，跳过全量重建。

5. **单静态二进制：** macOS / Linux / Windows 三平台，无 Docker / 无运行时 / 无 API key。`curl install | bash` 即用。

## 架构启发

codebase-memory-mcp 的核心设计哲学是"结构化索引替代暴力搜索"。这不仅是性能优化，而是范式转变：
- 传统方式：Agent → grep → read file → LLM 分析 → 重复（大量 token）
- 知识图谱方式：Agent → 一次图查询 → 精确结果（极少量 token）

CacheAligner-like 的思路：稳定 prefix 让 provider KV cache 命中率最大化。这种"为下游系统优化"的设计意识是基础设施级思维。

## 定位判断

**Coding Agent 的知识层。** 如果 headroom 是 LLM 的"压缩层"，codebase-memory-mcp 就是 LLM 的"索引层"。两者互补——headroom 压缩内容，codebase-memory-mcp 减少需要压缩的内容量。

在 MCP 生态中，这是"code intelligence"赛道的标杆项目。

## 风险 / 局限 / 泡沫点

1. **单一维护者风险：** DeusData 是个人/小团队。企业依赖需评估可持续性。
2. **索引时效性：** 文件变更后的增量索引质量取决于 watcher 的可靠性。大型 monorepo 的增量更新可能滞后。
3. **Hybrid LSP ≠ 真正 LSP：** C 实现的类型推断是近似方案，复杂场景（如 Python 动态类型、Ruby monkey patching）可能不准。
4. **MCP 生态早期：** 如果 MCP 标准变化，14 个工具接口可能需要重写。

## 与同类项目的关系

| 项目 | 方案 | Token 削减 | 语言覆盖 |
|------|------|-----------|----------|
| codebase-memory-mcp | tree-sitter 知识图谱 | 120x | 158 |
| headroom | 内容感知压缩 | 5-20x | N/A |
| FastContext | 专用小模型做仓库探索 | 10x | N/A |
| Sourcegraph Cody | 商业代码智能 | N/A | N/A |

codebase-memory-mcp 与 headroom 是互补关系——前者减少查询次数，后者压缩每次查询的内容。与 FastContext 是竞争关系——一个用规则和 AST，一个用 ML 模型。

## 是否值得持续跟踪

**是，重点跟踪。** codebase-memory-mcp 代表了 Coding Agent 基础设施的另一个关键层。如果它持续发展，可能成为 MCP 生态中 code intelligence 的标准组件。

## 后续观察点

1. 企业采用情况：是否有大公司在内部部署 codebase-memory-mcp
2. MCP 工具接口稳定性：14 个工具是否在真实使用中演化
3. arXiv 论文引用情况：学术影响力
4. 索引增量更新性能：在超大 monorepo（如 Google/Meta 内部规模）的表现
5. 是否有 IDE 集成计划（VS Code 扩展等）

---
*首次记录：2026-06-20*
