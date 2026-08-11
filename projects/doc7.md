---
title: "magicrew/doc7"
slug: "doc7"
date_added: "2026-08-06"
last_seen_date: "2026-08-08"
category: "观察型"
emoji: "🗂️"
stars: "608 stars"
stars_delta: "8/02创建→8/08观测 608⭐ / 16 fork，第七日 +143（+31%），增速回升（昨日 +2%→今日 +31%），本地路线获补涨"
language: "Go"
license: "MIT"
score: 81
tags: ["document-ai", "pdf-to-markdown", "docx-to-markdown", "local-ai", "multimodal", "vision-language-model", "go"]
url: "https://github.com/magicrew/doc7"
---

# magicrew/doc7 — 本地 VLM 文档解析

## 一句话定位
通过本地 OpenAI 兼容多模态模型（LM Studio/Ollama），把 PDF/Office/扫描/截图/图表/公式/图表转成 AI-ready Markdown 的 Go 工具，不依赖云服务或 OCR 栈。

## 它解决的问题
目标用户是需要私有化/离线文档解析的开发者和企业。痛点：云文档解析服务（如 Firecrawl Parse）要求数据上传，不适合敏感文档；传统 OCR 栈（Tesseract + 格式解析）复杂且对扫描页/图表/公式效果差。doc7 用**本地多模态 VLM**（视觉语言模型）直接"看"文档并转 Markdown，无需云服务、无需独立 OCR 栈。

## 为什么值得关注（2026-08-06）

这代表 agent 文档摄入层的**本地私有化路线**，与 anydoc（4,688⭐，云/Rust/单数毫秒）构成"云 vs 本地"路线分化。关键差异化：(a) **本地 VLM**（用 LM Studio/Ollama 跑本地多模态模型，数据不离机）；(b) **覆盖扫描页/截图**（anydoc 明确表示不读扫描页，需 Firecrawl Parse OCR；doc7 用 VLM 直接处理）；(c) **无 OCR 栈依赖**（"No required OCR stack. No document-processing service lock-in"）。454⭐ / 9 fork 说明本地化路线有需求但关注度远低于 anydoc 的云路线。

## 热度来源判断
- **真实需求信号**：私有化/离线文档解析是企业刚需（合规/隐私）。"no cloud, no OCR stack"的定位明确切中这个痛点。fork 仅 9（vs anydoc 205）说明目前关注度低，可能因为本地 VLM 门槛（需 GPU/本地模型）高于 anydoc 的 npm install。
- **话题性成分**：doc7 热度（454⭐）远低于 anydoc（4,688⭐），没有爆发性话题成分。更像"稳定但小众"的项目。

## 关键技术亮点亮点

1. **本地 OpenAI 兼容多模态模型**：通过 OpenAI 兼容 API 调用本地 VLM（LM Studio/Ollama 部署），数据完全本地。"No required OCR stack"——VLM 直接理解文档视觉内容。
2. **覆盖扫描页/截图/图表/公式/图表**：PDF/Office/扫描/截图/图表/公式/diagrams 都能处理——VLM 的视觉理解能力覆盖传统 OCR 难处理的复杂视觉元素。
3. **Go 实现**：单二进制部署，install 脚本（curl | bash）。与 anydoc 的 Rust 不同，doc7 用 Go。
4. **Benchmark 示例**：README 含 benchmarks/attention-is-all-you-need 示例，展示对学术论文（含公式/图表）的解析效果。

## 架构启发
doc7 的设计哲学是 **"用 VLM 替代专用 OCR + 格式解析"**——不针对每种格式（docx/pdf/扫描）写专用解析器，而是用通用 VLM"看"文档统一输出。这与 anydoc 的"专用 Rust 解析器 + 格式无关输出"是两种范式：anydoc 追求**速度和确定性**（专用解析器，单数毫秒，格式无关），doc7 追求**通用性和私有化**（VLM 看一切，本地运行）。对架构师的启发：文档解析的"速度/确定性 vs 通用性/隐私"是核心 trade-off。

## 定位判断
属于 **L1 基础设施/工具层**，是 agent 文档摄入层的**本地私有化路线代表**。与 anydoc（云路线）互补，覆盖不同场景（敏感文档/离线 vs 快速/集成友好）。

## 风险 / 局限 / 泡沫点

1. **本地 VLM 门槛高**：需 GPU + 本地多模态模型（LM Studio/Ollama），部署门槛远高于 anydoc 的 `npm install`。这可能解释 fork 仅 9。
2. **VLM 解析质量依赖模型**：输出质量完全取决于本地 VLM 的能力，弱模型会导致 Markdown 质量差。不同模型（Qwen-VL/Llama-Vision 等）的效果差异未披露。
3. **速度劣势**：VLM 推理（秒级）远慢于 anydoc 的专用解析器（单数毫秒），不适合大批量处理。
4. **关注度低**：454⭐ / 9 fork 远低于 anydoc，本地化路线可能是边缘场景而非主流需求。需观察是否放量。

## 与同类项目的关系
- **vs anydoc（4,688⭐）**：核心路线分化——anydoc 云/Rust/专用解析器/单数毫秒 vs doc7 本地/Go/VLM/秒级。anydoc 不读扫描页（需 Firecrawl Parse OCR），doc7 用 VLM 覆盖扫描页。两者是"云 vs 本地"的路线分化。
- **vs Unstructured/LlamaParse**：同为文档解析，doc7 的差异化是纯本地 VLM（无云依赖）。Unstructured 也有本地模式但架构不同。
- **vs Marker（PDF→Markdown）**：Marker 专注 PDF，doc7 覆盖更多格式 + 用 VLM 处理复杂视觉。

## 是否值得持续跟踪
**是，作为"agent 文档摄入层本地化路线"的代表项目跟踪。** 与 anydoc（云路线）互补，观察本地化路线是否从边缘场景变为主流需求。重点验证 VLM 解析质量和部署门槛的影响。

## 后续观察点
1. **放量情况**：fork 是否从 9 增长——如果持续低，说明本地化是边缘场景；如果放量，说明私有化需求真实。
2. **VLM 模型兼容性**：不同本地 VLM（Qwen-VL/Llama-Vision 等）的解析质量差异。
3. **与 anydoc 的路线竞争**：云路线（anydoc 爆发）是否会挤压本地路线（doc7）的生存空间，还是两者各占细分市场。

---
*首次记录：2026-08-06* · *数据来源: GitHub API + 仓库 README*

## 最近动态（2026-08-07）

- **第六日 +11（+2%），关注度低**：454 → 465，fork 9 → 10（+1）。增量极低，说明本地化路线（本地 VLM 文档解析）当前是边缘场景而非主流需求。
- **与 anydoc 的路线竞争——云路线碾压本地路线**：anydoc 同期从 4,688 → 8,069（+3,381），doc7 仅 +11。云路线（anydoc，Firecrawl Parse hosted API）以 300 倍的增量优势碾压本地路线（doc7）。
- **判断修正**：score 81 → 80。关注度低 + 增量极低。本地化路线可能需要等待私有化需求成熟（如企业数据合规场景），当前非主流。pushed_at 仍停在 08-04（无新代码）。
