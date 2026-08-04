---
title: "firecrawl/anydoc"
slug: "anydoc"
date_added: "2026-08-05"
last_seen_date: "2026-08-05"
category: "工具型"
emoji: "📑"
stars: "1,086 stars"
stars_delta: "8/03创建→8/05观测 1,086⭐ / 40 fork / 2 subscribers，v0.1.3，2 天"
language: "Rust"
license: "MIT"
score: 82
tags: ["document-parsing", "markdown", "rust", "agent-intake", "firecrawl", "llm-ready", "docx", "pptx", "xlsx", "pdf"]
url: "https://github.com/firecrawl/anydoc"
---

# firecrawl/anydoc — Office 文档转 LLM-ready Markdown

## 一句话定位
Firecrawl 官方的 Rust 库，把 Word/PowerPoint/Excel/OpenDocument/RTF/EPUB/CSV/PDF 转成干净的 GitHub-Flavored Markdown，单数毫秒级，提供 Node.js 和 Python 绑定，并作为 Agent Skill 分发。

## 它解决的问题
目标用户是构建 agent 应用的开发者。痛点：agent 要处理真实世界的 office 文档（合同、报告、表格、演示），但每种格式（docx/pptx/xlsx/pdf 等）各有二进制结构和解析复杂度。没有统一、快速、格式无关的解析层，agent 的文档摄入就需要为每种格式拼装不同的库。anydoc 提供单一 API 把这些格式统一转成 Markdown（LLM 友好的文本格式）。

## 为什么值得关注（2026-08-05）

这扩展了 agent 的**文档摄入基础设施**——从 web 抓取（Firecrawl 主线，149K⭐）扩展到 office 文档。2 天 1,086⭐ 说明需求真实。关键差异化是：(a) **Firecrawl 官方背书**（非个人项目，有 Firecrawl Parse 产品线支撑）；(b) **作为 Agent Skill 分发**（`npx skills add firecrawl/anydoc`，兼容 Claude Code/Codex/Cursor/OpenCode），直接嵌入 agent 工作流；(c) **Rust + 单数毫秒**的性能声明。

## 热度来源判断
- **真实需求信号**：1,086⭐ / 40 fork，2 天。Firecrawl 官方背书（主仓库 firecrawl 149K⭐，有现成用户基数导流）。Rust + Node/Python 绑定降低集成门槛。
- **品类时机信号**：agent 进入办公场景（genoffice 1.3K⭐、qm 11K⭐ 都在谈生产力），文档摄入是 agent 进入真实办公的前置基础设施。
- **话题性成分**：subscribers 仅 2（极低），说明目前是"收藏/试用"为主，深度使用尚少。2 天 1K⭐ 含 Firecrawl 品牌导流成分。

## 关键技术亮点

1. **多格式统一输出**：Word（.docx）、PowerPoint（.pptx）、Excel（.xlsx）、OpenDocument（.odt/.odp/.ods）、RTF、EPUB、CSV、PDF——八种格式转成统一的 GitHub-Flavored Markdown。README 声称"one consistent output no matter which format goes in"。
2. **Rust 单数毫秒**：用 Rust 实现，README 声称"single-digit milliseconds"。提供 Node.js（`@firecrawl/anydoc`）和 Python（`firecrawl-anydoc`）绑定，以及 `npx` CLI。
3. **Agent Skill 分发**：作为 [Agent Skill](https://agentskills.io) 发布，`npx skills add firecrawl/anydoc` 后 agent 可直接读文档。skill 定义在 `skills/convert-documents-to-markdown/SKILL.md`，兼容 Claude Code/Codex/Cursor/OpenCode 及任何兼容 agent。
4. **三种 API 入口**：`toMarkdown(path)`（从文件路径）、`toMarkdownBytes(bytes, format?)`（从字节，格式检测或显式命名）、`toDocument(bytes)`（停在文档模型，携带嵌入资产）。
5. **Firecrawl Parse 产品线支撑**：anydoc 是 Firecrawl Parse（hosted API）的开源底层，"如果不想自跑，hosted API 给同样的转换 + OCR 模型（处理 anydoc 无法读取的扫描页）"。

## 架构启发
anydoc 的设计哲学是 **"格式无关的输出统一"**——无论输入是 docx 还是 pdf，输出都是结构一致的 Markdown。这与 Firecrawl 主线（web→Markdown）形成自然延伸：web 和 office 文档都流向同一 LLM-ready 文本格式。对架构师的启发：**agent 的摄入层应该向调用者隐藏格式差异**——agent 不应关心"这是 docx 还是 pdf"，只应看到统一的结构化文本。这也是 Graphify（代码 AST→图谱）的同类思路在不同领域（文档→Markdown）的体现。

## 定位判断
属于 **L1 基础设施/工具层**，是 agent 文档摄入基础设施。与 Firecrawl 主线（web 抓取）互补，共同覆盖 agent 的"读外部世界"能力。不直接与应用层竞争，而是为应用层（如 genoffice、qm）提供摄入底座。

## 风险 / 局限 / 泡沫点

1. **"单数毫秒"为设计声明**：README 声称 single-digit milliseconds，但未提供独立基准测试（不同文档大小/复杂度/格式的实测数据）。复杂文档（大表格、嵌入图片、宏）的实际耗时未披露。
2. **"格式无关一致性"未在复杂场景验证**：README 声称"one consistent output no matter which format goes in"，但复杂 docx（宏、嵌入对象、修订追踪）、扫描 PDF（需 OCR，anydoc 明确表示自己不读扫描页，需 Firecrawl Parse 的 OCR 模型）的实际表现未独立验证。
3. **极早期**：v0.1.3，2 天，subscribers 仅 2。Firecrawl 品牌导流成分不可忽视——1K⭐ 含 Firecrawl 主仓库（149K⭐）用户的注意力转移。
4. **扫描 PDF 依赖 Firecrawl 付费服务**：anydoc 本身不读扫描页，需 Firecrawl Parse hosted API 的 OCR——这把"完整文档处理"绑定到 Firecrawl 商业服务。

## 与同类项目的关系
- **vs Firecrawl 主仓库（149K⭐）**：主线是 web→Markdown，anydoc 是 office 文档→Markdown。同公司、同"→Markdown"理念，互补覆盖 agent 的两类主要摄入源（web + 文档）。
- **vs Graphify（94.8K⭐）**：都解决"agent 如何摄入结构化信息"，但 Graphify 面向代码库（AST→图谱，非向量检索），anydoc 面向 office 文档（二进制→Markdown）。领域不同，但都是"把非文本结构转成 agent 可消化形式"。
- **vs Unstructured/LlamaParse 等**：同为文档解析，anydoc 的差异化是 Rust 性能 + Firecrawl 生态 + Agent Skill 分发模式。未做直接 benchmark 对比。

## 是否值得持续跟踪
**是，作为"agent 文档摄入层"的代表项目跟踪。** Firecrawl 官方背书 + 2 天 1K⭐ 说明需求真实。重点验证复杂文档（宏/嵌入对象/扫描页）的实际解析质量，以及 Agent Skill 分发模式的采用度。

## 后续观察点
1. **复杂文档的解析质量**：宏、嵌入对象、修订追踪、复杂表格在 anydoc 下的实际输出质量（vs 设计声明）。
2. **Agent Skill 分发采用度**：`npx skills add firecrawl/anydoc` 是否被 Claude Code/Codex/Cursor 社区实际采用，还是仅作为库被直接集成。
3. **与 Firecrawl Parse 的边界**：开源 anydoc 与付费 Firecrawl Parse（OCR/扫描页）的功能边界是否会推动用户走向付费，还是 anydoc 独立足够。

---
*首次记录：2026-08-05* · *数据来源: GitHub API + 仓库 README*
