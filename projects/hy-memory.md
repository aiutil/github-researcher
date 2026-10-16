---
title: "Tencent-Hunyuan/Hy-Memory"
slug: hy-memory
date_added: 2026-10-17
category: "生产可用"
emoji: "🧬"
stars: "314 stars"
stars_delta: "2 天 314⭐（粗略下限估计）"
language: "Python"
score: 87
tags: ["hy-memory","hunyuan","tencent","cognitive-memory","dual-system","self-evolving","llm-agents","chat-memory","working-memory","coding-memory","8-layer-hierarchy","conflict-reconciliation","schema-induction","diff-chain","memhub","claude-code","cursor","codex","opencode","qwen-code","hy-memory-30b-a3b","attributed-reinforcement-learning","cmb-benchmark","iclr-2027","emnlp-2026","chromadb","qdrant","faiss","neo4j","kuzu","python","apache-2"]
url: "https://github.com/Tencent-Hunyuan/Hy-Memory"
---

# Tencent-Hunyuan/Hy-Memory

## 一句话定位
腾讯混元开源的 production-grade dual-system cognitive memory for LLM agents——Python SDK (hy-memory==2.0.2) + MemHub 本地优先 desktop + CLI 统一 Claude Code / Cursor / Codex / OpenCode / Qwen Code + 自进化 LLM agents 的认知记忆引擎。

## 它解决的问题
2026 年 LLM agent 在多场景（Chat / Working / Coding）下需要 persistent memory，但市面方案有三个痛点：（1）stateless chat + ad-hoc memory tricks 让 agent 跨会话失忆；（2）多 agent 不共享 memory 导致重复劳动；（3）强 model 一把抓（强 sweep）成本高。Tencent-Hunyuan/Hy-Memory 用 dual-system 认知记忆 + 8-layer hierarchy + 30B-A3B MoE + attributed RL + 跨应用 MemHub 一站式解决。

## 为什么值得关注（2026-10-17）
- **Stars:** 314（截至 2026-10-17），2 天破 300
- **Forks:** 30，fork/star 9.6% 大量二次开发
- **Language:** Python
- **License:** Apache-2.0
- **Size:** 17763 KB
- **热度来源：** MemHub + Hy-Memory-30B-A3B + EMNLP 2026 + ICLR 2027 + Claude Code 等跨应用 unification
- **独特性：** 是「企业级 LLM agent 记忆库」+「跨应用统一」严肃工程化范本
- **架构独特性：** 三场景专门化（Chat / Working / Coding）+ 8-layer hierarchy + MemHub local-first + Hy-Memory-30B-A3B（30B MoE + attributed RL）

## 热度来源判断
**真实需求 + 大厂 + 开源 + 学术认证 + 跨应用统一** 五组合：
- **需求侧：** LLM agent 在多场景（Chat / Working / Coding）+ 多应用（Claude Code / Cursor / Codex / OpenCode / Qwen Code）+ 长生命周期（跨会话）+ 跨 agent 共享记忆 是真痛点
- **技术侧：** dual-system cognitive memory + 8-layer hierarchy + conflict reconciliation + cross-domain schema induction 是严肃的 cognitive engineering 尝试；EMNLP 2026 + ICLR 2027 + Hy-Memory-30B-A3B + attributed RL 是强学术背书
- **生态侧：** Tencent 集团 Hunyuan 团队 + Apache-2.0 + 多个 chat-history 来源（Claude Code / Cursor / Codex / OpenCode / Qwen Code）说明这是企业级 + 跨厂商 + 跨应用的解决方案
- **风险：** 「8-layer hierarchy + conflict reconciliation」在 production 不同 LLM（Claude / GPT / Qwen）上的实际 fidelity 未公开；Hy-Memory-30B-A3B 推理成本 vs general LLM 的性价比未公开；「self-evolving」在 RL 中是否 well-defined 未公开

## 关键技术亮点
1. **Production-grade dual-system cognitive memory engine + Python SDK (hy-memory):** System 1 + System 2 认知架构；hy-memory==2.0.2 在 PyPI 上
2. **Three task scenes 专门化管道：** (a) hierarchical long-term cognitive memory for Chat (8-layer hierarchy: raw dialogues / atomic facts / summaries / schemas / prospective intentions + conflict reconciliation + cross-domain schema induction) + (b) two-layer fact and reusable-experience memory for Working + (c) version-evolution diff-chain tracking for Coding
3. **MemHub: local-first desktop + CLI product 跨应用统一：** unified conversation history and coding traces from Claude Code / Cursor / Codex / OpenCode / Qwen Code 一个 managed runtime + 本地数据目录 → governed cross-application memory recall
4. **Hy-Memory-30B-A3B MoE model:** 30B MoE（待激活 A3B）专门用于 high-precision long-term memory extraction + conflict reconciliation，在 Hugging Face Open-Sourced
5. **Attributed reinforcement learning for long-term memory writing:** arXiv 2610.22196
6. **CMB: A Coding Memory Benchmark for Long-Horizon and Interleaved Coding Agents:** 提交给 ICLR 2027；为 Coding Memory 提供 benchmark
7. **Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents:** EMNLP 2026 accepted
8. **多层后端可选：** ChromaDB + Kuzu（core, 默认）+ Qdrant + FAISS + Neo4j (graph) + MySQL + cross-encoder rerank + 7 个 extra 安装选项
9. **OpenAI-compatible：** 任何 OpenAI-compatible LLM service 都能接入（Claude / GPT / Gemini / Qwen / Ollama 等）
10. **Self-evolving：** LLM agents 通过使用 memory 自动演化（attributed RL 把 memory 写入训练成专门化模型）

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 一个 Python SDK (hy-memory==2.0.2) `pip install hy-memory[core/qdrant/faiss/graph/mysql/rerank/all]==2.0.2`（core includes ChromaDB and Kuzu） + 一个 MemHub 本地优先的 desktop 和 CLI product（统一对话历史与编码轨迹 从 Claude Code / Cursor / Codex / OpenCode / Qwen Code 一个 managed runtime + 本地数据目录） + 一个 Chat scene 管道（hierarchical long-term cognitive memory：8-layer hierarchy raw dialogues / atomic facts / summaries / schemas / prospective intentions + conflict reconciliation + cross-domain schema induction） + 一个 Working scene 管道（two-layer：fact memory + reusable-experience memory） + 一个 Coding scene 管道（version-evolution diff-chain tracking 保留 reusable engineering experiences + exact code revision trajectories across interleaved tasks） + 一个 Hy-Memory-30B-A3B 模型（在 Hugging Face Open-Sourced） + 一个 attributed RL 训练系统（专门用于 high-precision long-term memory extraction + conflict reconciliation） + 一个 CMB 基准（ICLR 2027 submitted） + 一个 EMNLP 2026 paper（Memory Beyond Recall Dual-Process Cognitive Memory System for Self-Evolving LLM Agents） + 一个 ICLR 2027 paper（CMB） + 一个 technical report（arXiv 2610.22196） + 一个 Official Website（https://memory.hunyuan.tencent.com/）+ Discord community（memory channel）+ Apache-2.0 + Python + Tencent 集团 Hunyuan 团队 | 仅基于 README「Hy Memory (https://memory.hunyuan.tencent.com/) is a production-grade dual-system cognitive memory engine and Python SDK (hy-memory) for self-evolving LLM agents, providing specialized memory pipelines across three task scenes: hierarchical long-term cognitive memory for Chat, two-layer fact and reusable-experience memory for Working, and version-evolution diff-chain tracking for Coding. Built on top of Hy Memory, MemHub is a local-first desktop and CLI product that unifies conversation history and coding traces from user-authorized AI applications (such as Claude Code, Cursor, Codex, OpenCode, and Qwen Code) into a single managed runtime and local data directory, enabling governed cross-application memory recall. + Latest News 4 条 + Papers 3 篇（EMNLP 2026 + ICLR 2027 + technical report） + Quick Start pip install 7 个 extra」+ license badge + size 推断；具体 8-layer hierarchy 在不同 LLM 上的实际 fidelity、conflict reconciliation 的冲突检测粒度、cross-domain schema induction 的跨域边界、MemHub desktop 产品是否是 Electron/Tauri/Qt、Hy-Memory-30B-A3B 模型的具体架构 vs Qwen3-30B-A3B 的关系未在档案明示 |
| 主路径 | 用户 `pip install hy-memory==2.0.2`（core + ChromaDB + Kuzu）或 `hy-memory[all]==2.0.2`（Qdrant/FAISS/Neo4j/MySQL/rerank） → `export MEMORY_LLM_API_KEY=sk-your-key` → 启动 MemHub desktop 或 CLI → 授权 Claude Code / Cursor / Codex / OpenCode / Qwen Code（user-authorized AI applications）→ MemHub 捕获对话历史 + 编码轨迹（统一 managed runtime）→ 8-layer hierarchy 写入 Chat memory → two-layer 写入 Working memory → diff-chain tracking 写入 Coding memory → Hy-Memory-30B-A3B 专门提取 long-term memory + reconciliation → 跨应用 governed recall → 跨任务 continuous improvement | 主路径为 README「Hy Memory + MemHub + Quick Start」段落整理；具体 8-layer hierarchy 在大型 conversation 上的 token 级 granularity、conflict reconciliation 是 user-triggered 还是 automatic、MemHub 是否仅 macOS/Windows 或也 Linux、MemHub 的 govern policy 机制、与 Zep / mem0 / Letta 等同样 LLM memory 项目的实测对比未在档案明示 |
| 关键权衡 | dual-system (System 1+System 2) cognitive architecture vs single-tier flat memory vs vector-only (ChromaDB/Qdrant) vs graph-only (Neo4j/Kuzu) vs 单一 model 一把抓（强 model + long context）vs specialized model (Hy-Memory-30B-A3B) vs 8-layer hierarchy (raw/atomic/summary/schema/prospective) vs flat + system prompt + RAG vs conflict reconciliation vs cross-domain schema induction vs 30B-A3B MoE + attributed RL training vs general LLM (e.g. GPT-4/Claude) vs closed-loop self-evolving memory vs Chat/Working/Coding 三场景专门化 vs MemHub 本地优先跨应用 unification vs Zep / mem0 / Letta / LangGraph memory vs EMNLP 2026 paper 与 ICLR 2027 paper | 权衡来自 README「production-grade dual-system cognitive memory + Python SDK (hy-memory) + self-evolving LLM agents + three task scenes (hierarchical long-term Chat + two-layer fact and reusable-experience Working + version-evolution diff-chain Coding) + MemHub local-first desktop + CLI + Claude Code + Cursor + Codex + OpenCode + Qwen Code + managed runtime + local data directory + governed cross-application memory recall + Released Hy Memory 2.0 + Open-sourced Hy-Memory-30B-A3B + CMB ICLR 2027 + Memory Beyond Recall EMNLP 2026 + attributed RL + ChromaDB + Kuzu + Qdrant + FAISS + Neo4j + MySQL + rerank + Apache-2.0」 |
| 最小 PoC | a) `pip install hy-memory==2.0.2` + `export MEMORY_LLM_API_KEY=...` → 起 in-memory demo → 跑 Chat scene 8-layer hierarchy → 跑 Working scene two-layer → 跑 Coding scene diff-chain；b) 装 MemHub desktop + 授权 Claude Code / Cursor / Codex / OpenCode / Qwen Code → 跨应用 recall 一段过往对话；c) 装 Hy-Memory-30B-A3B 模型 → 跑 high-precision long-term memory extraction on a long conversation → 看 conflict reconciliation；d) 跑 CMB benchmark baseline | PoC 由 README「Quick Start + Latest News + MemHub」段落整理；具体 8-layer hierarchy 在长对话（100+ turns）上的实际 recall 准确率、MemHub 的授权机制（OAuth / API key）、Hy-Memory-30B-A3B 在不同 LLM（Claude/GPT/Qwen）上的 extraction 准确率、与 Zep / mem0 / Letta 的实测 benchmark 对比未在档案明示 |
| 证据边界 | 仅核验：仓库存在、stars/forks/description/license/size/language 来自 GitHub API；README 节录自 raw 接口；production-grade dual-system cognitive memory + Python SDK (hy-memory==2.0.2) + self-evolving + three task scenes + MemHub local-first desktop + CLI + Claude Code + Cursor + Codex + OpenCode + Qwen Code + managed runtime + governed cross-application memory recall + Released Hy Memory 2.0 + Open-sourced Hy-Memory-30B-A3B + CMB ICLR 2027 + Memory Beyond Recall EMNLP 2026 + attributed RL for long-term memory writing (arXiv 2610.22196) + ChromaDB + Kuzu + Qdrant + FAISS + Neo4j + MySQL + cross-encoder rerank + Apache-2.0 + Python + Tencent Hunyuan 由 README 直接叙述 | 待核验：8-layer hierarchy 在不同 LLM 上的 fidelity、conflict reconciliation 粒度、cross-domain schema induction 边界、MemHub desktop 平台与授权、Hy-Memory-30B-A3B 架构与基础 model 关系、closed-loop self-evolving 的具体 RL 算法 (DPO/PPO/GRPO)、MemHub 的 govern policy 与隐私边界、与 Zep / mem0 / Letta / LangGraph memory 的实测对比、在企业 (Tencent 内部) 的采用规模 |

## 架构启发
Tencent-Hunyuan/Hy-Memory 的核心启发是 **「LLM agent 的记忆不应该 stateless chat + ad-hoc memory tricks；应该 production-grade dual-system cognitive memory + three task scenes 专门化 + MemHub 本地优先跨应用统一」**。四层意义：
1. **Dual-system cognitive architecture 是严肃的 cognitive engineering 路径：** System 1 (fast, intuitive) + System 2 (slow, analytical) 让 memory 表达既高效又可推理，这是 cognitive science 经典理论在 LLM memory 上的工程化
2. **Three task scenes 专门化 vs one-size-fits-all：** Chat（8-layer hierarchy）/ Working（two-layer fact + experience）/ Coding（diff-chain tracking）针对每个场景设计专门 pipeline，比 universal memory 更高效
3. **MemHub local-first 跨应用统一：** 5 个 coding agent（Claude Code / Cursor / Codex / OpenCode / Qwen Code）的对话历史统一进一个 managed runtime + local data directory → governed cross-application recall，是「memory 可携带」的产品化
4. **30B-A3B MoE + attributed RL 专门化模型：** 与 LLM 通用模型（GPT-4/Claude/Qwen）不同，专门训练 small-medium model 做 long-term memory extraction，比走 LLM 强 sweep 更低成本

更深层的启发：**LLM agent memory 是 2026 年 AI infrastructure 的核心底层**——从 vendor-locked solutions（OpenAI Assistants / Anthropic Memory）到 open-source production-grade（Hy Memory + Zep + mem0 + Letta）的演化，标志着「agent memory」开始进入产品化阶段。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户 / LLM agent / 跨应用场景] --> MemHub[MemHub<br/>local-first desktop + CLI<br/>unified managed runtime + local data directory]
  MemHub --> ClaudeCode[Claude Code<br/>chat history + code traces]
  MemHub --> Cursor[Cursor<br/>chat history + code traces]
  MemHub --> Codex[Codex<br/>chat history + code traces]
  MemHub --> OpenCode[OpenCode<br/>chat history + code traces]
  MemHub --> QwenCode[Qwen Code<br/>chat history + code traces]
  MemHub --> HYMemory[hy-memory Python SDK<br/>pip install hy-memory core all == 2.0.2]
  HYMemory --> Chat[Chat Scene<br/>8-layer hierarchy<br/>raw dialogues / atomic facts / summaries / schemas / prospective intentions<br/>+ conflict reconciliation + cross-domain schema induction]
  HYMemory --> Working[Working Scene<br/>two-layer<br/>fact memory + reusable-experience memory]
  HYMemory --> Coding[Coding Scene<br/>version-evolution diff-chain tracking<br/>reusable engineering experiences + exact code revision trajectories]
  Coding --> CMB[CMB Benchmark<br/>Long-Horizon Interleaved Coding Agents<br/>ICLR 2027 submitted]
  HYMemory --> Backend[后端多选<br/>ChromaDB + Kuzu core<br/>Qdrant / FAISS / Neo4j / MySQL / cross-encoder rerank]
  Chat --> Model[Hy-Memory-30B-A3B MoE<br/>Hugging Face Open-Sourced]
  Chat --> RL[attributed reinforcement learning<br/>high-precision long-term memory extraction + conflict reconciliation]
  RL -.arXiv 2610.22196.-> Paper1[technical report]
  Chat -.EMNLP 2026.-> Paper2[Memory Beyond Recall<br/>Dual-Process Cognitive Memory System<br/>for Self-Evolving LLM Agents]
  Backend -.ICLR 2027.-> Paper3[CMB Coding Memory Benchmark]
  Model --> Output[governed cross-application memory recall<br/>+ 跨任务 continuous improvement]
```

## 定位判断
**生产可用 / 平台候选（LLM agent 时代 cognitive memory）。** Tencent-Hunyuan/Hy-Memory 试图成为「LLM agent 时代 cognitive memory」的事实标准——dual-system + three task scenes 专门化 + 8-layer hierarchy + MemHub 本地优先跨应用统一 + Hy-Memory-30B-A3B 专门化模型 + EMNLP/ICLR 学术背书。**定位判断：**
- **现在：** Hy Memory 2.0（hy-memory==2.0.2）+ MemHub desktop + Hy-Memory-30B-A3B + EMNLP 2026 + ICLR 2027 在 2026-10 完整发布
- **如果 MemHub 在 5 个 coding agent（Claude Code / Cursor / Codex / OpenCode / Qwen Code）上稳定 recall 跨会话：** 它会变成「coding agent 用户」+「SaaS」+「企业」的认知记忆首选
- **如果 Hy-Memory-30B-A3B 在 long-term extraction 上比 LLM sweep 更省 cost：** 它会变成「长对话 + Coding + Chat」场景的 "dedicated memory model"
- **如果 8-layer hierarchy 在不同 LLM 上 fidelity 高：** 它会变成 vendor-neutral memory 标准，比 vendor-locked solutions（OpenAI Assistants / Anthropic Memory）开放
- **风险：** 「8-layer hierarchy + conflict reconciliation」数学严格性 + Hy-Memory-30B-A3B 推理成本 + MemHub 跨应用授权机制 + closed-loop self-evolving RL 算法稳定性都未公开 benchmark
- **潜力：** Apache-2.0 + Tencent 集团 Hunyuan 团队 + 双 EMNLP/ICLR 论文 + 5 个 coding agent 整合 + MemHub 本地优先 + 30B-A3B MoE 专门化模型，构成了完整的"生产可用 + 平台候选 + 学术认证 + 工程化"矩阵

## 风险 / 局限 / 泡沫点
- **8-layer hierarchy 在不同 LLM 上的 fidelity 未公开：** Claude / GPT / Gemini / Qwen 在 8-layer 提取上 fidelity 差距多大未公开 benchmark
- **Conflict reconciliation 粒度与触发机制未明：** 是 user-triggered 还是 automatic；粒度到 token / sentence / section
- **Cross-domain schema induction 边界：** 跨域 schema 抽象的 fidelity 未公开
- **Hy-Memory-30B-A3B 推理成本 vs general LLM sweep：** 30B MoE 比强 sweep 更省吗？没有 benchmark
- **MemHub desktop 平台与授权机制：** Electron / Tauri / Qt？OAuth / API key / 本地 token？多平台？
- **Governed cross-application memory recall 隐私边界：** MemHub 捕获 5 个 coding agent 的对话历史与编码轨迹，跨应用的隐私 boundary 未公开
- **Closed-loop self-evolving RL 算法稳定性：** DPO / PPO / GRPO / RLHF / SFT 选择；closed-loop 是真 self-evolution 还是 manual re-train 未公开
- **MemHub 用户授权机制：** 与 Claude Code / Cursor / Codex / OpenCode / Qwen Code 的具体授权方式（OAuth / 单独 token / 共享 token）未公开
- **企业 (Tencent 内部) 的采用规模：** 是否 Tencent 集团自家产品大规模使用
- **与 Zep / mem0 / Letta / LangGraph memory 的实测对比：** 4 个同样定位的开源项目，hy-memory 的差异化与优劣未公开 benchmark
- **CMB benchmark 提交 ICLR 2027 尚未正式发表：** 提交 + 接受是不同状态
- **依赖 specific embedding model：** 系统默认 ChromaDB / Kuzu，但 cross-encoder rerank 需要额外 model
- **个人项目可能性：** Hunyuan 团队是 Tencent 集团内部团队，但仓库以个人 Org "Tencent-Hunyuan" 形式公开，长期 governance 待观察

## 与同类项目的关系
- **vs Zep：** Zep 也是 LLM agent memory 开源项目，位置相近；具体差异（architecture + benchmark）待比较
- **vs mem0：** mem0 是 scalable memory layer for AI apps，vendor-neutral；hy-memory 是 Tencent Hunyuan 出品，三场景专门化；差异化在中文化 + 跨 5 个 coding agent
- **vs Letta（前 memGPT）：** Letta 偏 persistent AI agents + long-term memory + stateful agents；hy-memory 偏 production-grade 三场景专门化；两者可配合
- **vs LangGraph memory：** LangGraph 是 agent orchestration framework，自带 memory；hy-memory 是 standalone memory library；可集成
- **vs vendor-locked solutions（OpenAI Assistants / Anthropic Memory）：** vendor 锁定 vs vendor-neutral open-source；hy-memory 可跨 LLM 用
- **vs Long context（Claude 1M token / Gemini 1M token）：** long context 是 stateless sweep，hy-memory 是 persistent memory；两者可配合
- **vs Haystack / LlamaIndex：** 偏 RAG framework，自带 memory layer；hy-memory 是 production-grade dedicated memory library

## 是否值得持续跟踪
**值得跟踪（LLM agent 时代 cognitive memory 生产可用）。** Tencent-Hunyuan/Hy-Memory 是「LLM agent 时代 cognitive memory」+「跨应用统一」+「学术认证」+「生产可用」严肃工程化范本，比 vendor-locked solutions 开放、比单一 memory layer 更专门化。对 LLM agent 团队 / AI engineering 团队 / 企业 AI 部门 / 个人 hard-core AI coder，建议：
1. 直接 `pip install hy-memory[all]==2.0.2`，启 in-memory demo，跑 Chat + Working + Coding 三场景
2. 装 MemHub desktop + 授权 Claude Code / Cursor / Codex / OpenCode / Qwen Code 中至少 2 个，跨应用 recall 一段过往对话
3. 装 Hy-Memory-30B-A3B，跑 high-precision long-term memory extraction on a long conversation，看 conflict reconciliation
4. 跑 CMB benchmark baseline（PyPI 安装 + script）

对 AI 生态观察者，它是「LLM agent 时代 cognitive memory」+「跨应用统一」+「学术认证」+「生产可用」严肃工程化样本，与 Zep / mem0 / Letta 形成对比，值得持续关注：
- 8-layer hierarchy 在大型 conversation 上的实际 fidelity
- Hy-Memory-30B-A3B 在不同 LLM 上的 extraction 准确性
- MemHub 在 5 个 coding agent 上的授权机制
- 与 Zep / mem0 / Letta 的实测 benchmark
- closed-loop self-evolving 的 RL 算法稳定性
- EMNLP 2026 + ICLR 2027 论文的实际引用数
- Tencent 集团内部产品采用

## 后续观察点
- **8-layer hierarchy 实测 fidelity：** 在 Claude / GPT / Gemini / Qwen 不同 LLM 上的 benchmark
- **Hy-Memory-30B-A3B 推理成本：** 30B MoE vs general LLM sweep 在 conversation 上的 cost / latency
- **MemHub 跨应用授权机制：** OAuth / API key / 本地 token
- **MemHub 平台支持：** macOS / Windows / Linux 是否都支持
- **CMB benchmark 接受 / rejection：** ICLR 2027 论文审稿结果
- **CMB benchmark 社区使用：** 是否被其他 LLM agent 项目采用
- **与其他 LLM agent memory 项目对比：** Zep / mem0 / Letta / LangGraph memory 的实测差异
- **Tencent 集团内部采用：** Hunyuan 团队自家产品 + Tencent Cloud LLM 服务是否使用
- **Closed-loop self-evolving 公开：** RL 算法 + 训练数据
- **跨语言 / 跨文化：** 英文为主 + 简中 README + Discord memory channel；西方开发者接受度
- **Conflict reconciliation 触发机制：** user-triggered 还是 automatic
- **Cross-domain schema induction 实测：** 跨域 schema 的 quality

---
> 数据来源: GitHub API (2026-10-17) | Stars: 314 | Forks: 30 | License: Apache-2.0 (LICENSE file) — 注意 GitHub API 显示 NOASSERTION，但 README badges + LICENSE 标识为 Apache-2.0 | 语言: Python | 创建: 2026-10-15 | Size: 17763 KB
