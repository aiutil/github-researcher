---
title: "code-review-graph"
slug: "code-review-graph"
date_added: "2026-07-24"
category: "平台候选"
emoji: "🔍"
stars: "26,051 stars"
stars_delta: "周增 6,257"
language: "Python"
score: 89
tags: ["code-intelligence", "tree-sitter", "mcp", "knowledge-graph", "code-analysis", "agent-context"]
url: "https://github.com/tirth8205/code-review-graph"
---

# code-review-graph

## 一句话定位
通过 tree-sitter AST 构建代码知识图谱的 MCP 工具，让 AI 编程助手精确获取上下文——只读真正需要读的文件。

## 它解决的问题
AI 编程助手（Claude Code / Cursor / Codex 等）在 code review 时反复扫描大量代码，Token 浪费严重且上下文不精确。传统 RAG 方案用向量相似度搜索代码，语义近似但结构关系丢失——不知道哪个函数调用了哪个，哪些测试覆盖了变更。

## 为什么值得关注（2026-07-24）
26K⭐ + 周增 6.3K，从上周 Graphify 的范式验证到本周 code-review-graph 的工程化落地，速度极快。CRG 不是概念验证——它可以直接 `pip install` 并通过 MCP 集成主流 AI 编程工具。支持 40+ 语言，2900 文件项目增量索引 < 2 秒。

## 热度来源判断
- **工程成熟度**：一行命令安装（`code-review-graph install` 自动检测平台写 MCP 配置）
- **真实痛点**：Agent 上下文管理是 2026 年 AI 编程的核心瓶颈
- **数据说话**：monorepo 27,700+ 文件排除，实际只读 ~15 文件
- **生态集成**：Claude Code / Cursor / Codex / Gemini CLI / Copilot / Kiro 全覆盖

## 关键技术亮点亮点
1. **Tree-sitter AST 解析**：40+ 语言的函数/类/导入/调用/继承/测试覆盖的结构化图谱，不依赖向量
2. **Blast Radius 分析**：文件变更时自动追踪所有调用方、依赖方、测试——"爆炸半径"精确定义上下文边界
3. **增量索引**：SHA-256 hash diff 只重解析变更文件，2900 文件项目 < 2 秒
4. **MCP 原生集成**：一行 `code-review-graph install` 自动写入所有支持平台的 MCP 配置
5. **对称卸载**：`code-review-graph uninstall` 原子化清理，不残留

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | CRG 是一个本地 Python CLI，通过 `code-review-graph install` 写入 Claude Code / Cursor / Codex / Gemini CLI / Copilot / Kiro 的 MCP 配置，作为这些 AI 编程工具的上下文供给侧。它只触达被分析代码库与受支持 IDE/CLI 端点，不替代 LLM 与代码仓库本身。 | 边界来自 README「生态集成」「一行 install」描述；未公开具体 MCP server 进程模型与通信协议。 |
| 主路径 | 源码 → Tree-sitter AST(40+ 语言) → 知识图谱(函数/类/导入/调用/继承/测试覆盖) → Blast Radius 图遍历 → 经 MCP 暴露给 AI 客户端 → LLM 仅消费精确上下文。 | 路径见档案「技术亮点」与「架构启发」图；增量索引 < 2s 仅在 2900 文件项目上证实，10K+ 文件属待核验。 |
| 关键权衡 | 用 AST 精确结构关系换取对动态语言隐式依赖（反射、monkey patch）的覆盖盲区；用 `pip install` + 自动改写 MCP 配置换取采用速度，代价是配置写入对宿主环境的隐式副作用。 | 风险点由档案「风险/局限」直接列出；tree-sitter 各语种 grammar 质量在 40+ 语言完整列表上未核验。 |
| 最小 PoC | 在受限目录跑 `code-review-graph install` 接入单一 CLI（如 Gemini CLI），以一个 2900 文件级项目对比传统 RAG 读取文件数与 token 消耗；同时用 `uninstall` 验证配置可逆性。 | 基准数字仅在 README 描述的 27,700→15 文件场景得到；其它规模、其它 LLM 成本/SLO 属待核验。 |

## 架构启发
## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    User["👤 开发者"] --> IDE["🖥️ AI 编程客户端<br/>Claude Code / Cursor / Codex<br/>Gemini CLI / Copilot / Kiro"]
    IDE -- "MCP 请求" --> CRG["🐍 code-review-graph<br/>Python CLI · MCP server"]
    CRG -- "Tree-sitter AST 解析" --> TS["🌳 Tree-sitter<br/>40+ 语言 grammar"]
    TS --> Graph["📊 知识图谱<br/>节点: 函数/类/导入<br/>边: 调用/继承/测试覆盖"]
    Graph --> Blast["🔎 Blast Radius 遍历<br/>SHA-256 增量索引"]
    Blast -- "精确上下文" --> IDE
    CRG -. "install / uninstall<br/>自动改写 MCP 配置" .-> IDE
    IDE -- "上下文 + 代码" --> LLM["🤖 LLM<br/>供应商待核验"]
    CRG -. "动态依赖盲区<br/>反射 / monkey patch" .-> Risk["⚠️ 风险边界<br/>覆盖率待核验"]
```

**核心差异：** RAG 回答"哪些代码语义相似"，CRG 回答"哪些代码有真实依赖关系"。前者是近似，后者是精确。

## 定位判断
处于 **AI 编程工具上下文管理层**，正在从"新兴方案"向"事实标准"过渡。与 Graphify 属于同一范式但定位不同——Graphify 更偏平台化/通用知识图谱，CRG 更聚焦 code review 工程场景。

## 风险 / 局限 / 泡沫点
1. **Tree-sitter 依赖**：语言覆盖取决于 tree-sitter grammar 质量，非主流语言支持可能不完整
2. **动态类型语言**：Python/JS 的隐式依赖可能遗漏（如反射、猴子补丁）
3. **与 Graphify 竞争**：两个项目在同一赛道，可能分散社区精力
4. **单语言（Python）实现**：对非 Python 项目的集成可能增加摩擦

## 与同类项目的关系
| 维度 | code-review-graph | Graphify | Augment Code |
|------|------------------|----------|--------------|
| 实现方式 | Tree-sitter AST | Tree-sitter AST | 闭源 |
| 集成方式 | MCP（开源） | MCP（开源） | IDE 插件（闭源） |
| 安装 | pip install | pip install | 付费订阅 |
| 语言覆盖 | 40+ | 40+ | 未公开 |
| 定位 | Code Review 场景 | 通用代码知识图谱 | 商业产品 |

## 是否值得持续跟踪
**强烈建议。** 代码知识图谱正在从"创新概念"变为"工程标配"。CRG 和 Graphify 谁先达到生产级稳定性，谁就可能成为 Agent 上下文管理的事实标准。

## 后续观察点
1. 与 Graphify 是否会合并或互操作
2. 企业级 monorepo（10K+ 文件）的性能表现
3. IDE 原生 hook 集成的深度（目前依赖外部触发）
4. 社区贡献的语言 parser 数量增长
5. 是否被 Cursor / Replit 等商业产品集成

---
*首次记录：2026-07-24*
