---
title: "Contrastive-LM/CLM"
slug: clm
date_added: 2026-09-25
last_seen_date: 2026-09-26
category: "观察型"
emoji: "🧠"
stars: "892 stars"
stars_delta: "3 天 892⭐（粗略下限估计，created_at 2026-09-23 → 2026-09-26 总星数除以 3 天，09-25 769⭐ → 09-26 892⭐）"
language: "Python"
score: 90
tags: ["contrastive-lm", "clm", "python", "apache-2.0", "system-one", "contrastive-learning", "states-actions", "type-safe-compatible", "vllm", "qwen3-8b", "pip-install", "terminal-bench", "deep-swe", "sota-verifier", "decision-model", "jev-competitor", "fast-inference", "disaggregated-embeddings"]
url: "https://github.com/Contrastive-LM/CLM"
---

# Contrastive-LM/CLM

## 一句话定位
对比学习 System One 模型 CLM-8B（60M Nemotron Q&A + 30M synthetic hard negatives + 1M agentic trajectories 三段训练），TypeSafe 兼容 API，9× Jev 速度，Terminal-Bench 2.1 87.6% + DeepSWE 81.6% SOTA verifier，Apache-2.0 + pip install + vLLM serve 的开源挑战者。

## 它解决的问题
Jev / TypeSafe AI System One 决策模型虽有 2026 年最强的意图判断生态（jev-review / jeff / rizzo-flow / openJev-verdict / deepopen / unreal-agent / shapeshift / Astra-Ares / awesome-jev），但闭源 API + 应用层碎片化 + 开源挑战者稀少 + Apache-2.0 决策模型缺位 + System One verifier SOTA 缺位 + pip install 部署缺位 + 多 typed questions 接口统一。CLM 直击——用 **对比学习 objective（连接 states 和 actions）+ 三段训练 + states 和 actions 解耦（embeddings 独立缓存）+ TypeSafe 兼容 API + 9× Jev 速度 + Terminal-Bench / DeepSWE SOTA verifier + Apache-2.0 + pip install + vLLM serve**，让开发者用 `pip install contrastive-lm` 一行装，跑 `vllm serve` + `clm-serve` 即得 SOTA 决策模型后端，可无缝接入既有 Jev 应用层。解决的是 **「Jev 决策模型挑战者 + Apache-2.0 严肃工程化 + SOTA verifier + pip install 部署 + 多 typed questions 接口统一」** 的生态位缺位问题。

## 为什么值得关注
- **Stars:** 769（截至 2026-09-25），2 天突破 769，增速极快
- **Forks:** 61，社区贡献较活跃
- **License:** Apache-2.0（完全开源商用）
- **语言:** Python（含 vLLM serving + Hugging Face 模型发布生态）
- **活跃度:** created 2026-09-23，pushed_at 2026-09-24，持续高活跃
- **规模:** 892KB，训练 / 服务 / 评测 / fine-tuning 全套
- **Topics:** 未填写 GitHub topics（org: Contrastive-LM，Hugging Face: Contrastive-LM）
- **三段训练:** 60M Nemotron Q&A pairs + 30M synthetic hard negatives + 1M agentic trajectories
- **Apache-2.0 + pip install + vLLM serve + Discord + Hugging Face + blog** —— 完整开源生态

## 热度来源判断
Contrastive-LM/CLM 的热度是 **「Jev 决策模型挑战者 Apache-2.0 严肃工程化刚需 × 对比学习 states↔actions × 缓存独立 × 9× Jev 速度 × Terminal-Bench / DeepSWE SOTA verifier × TypeSafe 兼容 API × pip install × vLLM serve × Discord + Hugging Face + blog 完整生态」** 的强劲组合。Jev 已是 2026 年最热决策模型赛道（09-19 ~ 09-24 连续 12+ 项目构 Jev 后端 → 应用层 → 挑战者演化），但缺乏「Apache-2.0 + 9× Jev 速度 + SOTA verifier + pip install 部署」的严肃工程化挑战者。CLM 直击——它提供 **对比学习 objective** + **三段训练** + **states 和 actions 解耦 embeddings 独立缓存** + **CLMClient.system_one(state, questions={urgency:Noul, department:Choice, priority:Score})** + **computer-use / gaming / tool-calling 9× Jev 速度** + **Terminal-Bench 87.6% + DeepSWE 81.6% SOTA verifier** + **Apache-2.0 + pip install + vLLM serve**。热度**真实且具严肃挑战者潜力**——但需警惕：对比学习在多任务的稳定性；缓存独立在训练 / 服务的实际成本下降；9× Jev 速度在 production 部署的实用性；Terminal-Bench / DeepSWE SOTA verifier 在评测榜单的持续领先；TypeSafe 兼容 API 在既有 Jev 应用层（shapeshift / Astra-Ares / deepopen）的无缝切换；vLLM serve + Qwen3-8B 在多 GPU 部署的兼容性。

## 关键技术亮点
1. **对比学习 objective** —— 连接 states 和 actions 的对比学习目标；CLM-8B 预训练 + mid-train + post-train 三段
2. **States 和 actions 解耦** —— embeddings 独立缓存重用，训练和服务都又快又便宜
3. **TypeSafe 兼容 API** —— `CLMClient.system_one(state, questions={...})` 一次判断多 typed questions（Noul / Choice / Score），client 用 `CLM_BASE_URL` + `CLM_API_KEY` 接入既有 Jev 应用层（shapeshift / Astra-Ares / deepopen 即可无缝切换 CLM 后端）
4. **9× Jev 速度** —— computer-use / gaming / tool-calling 三类任务与 Jev 同水平但低 9× 延迟
5. **Terminal-Bench 87.6% + DeepSWE 81.6%** —— SOTA verifier（agentic coding benchmarks 微调后 verifier SOTA）
6. **三段训练** —— 60M Nemotron Q&A pairs + 30M synthetic hard negatives + 1M agentic trajectories
7. **`pip install contrastive-lm`** —— pip install 部署
8. **`vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --port 8090`** —— encoder serving
9. **`clm-serve` 8700** —— API serving（首次运行下载 75 MB reference head）
10. **Noul / Choice / Score** —— typed questions 类型（urgent?/department?/priority?）
11. **Apache-2.0 + Discord + Hugging Face + blog Contrastive-LM org** —— 完整开源 + 社区 + 模型发布生态
12. **fine-tuning tutorial** —— 文档 `/docs/fine-tuning-clm-on-your-own-data`

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 对比学习 System One 模型库 + CLM-8B 模型权重（Hugging Face 发布）+ TypeSafe 兼容 API 后端（CLMClient + clm-serve）+ encoder serving（vLLM Qwen3-8B pooling）；用户用 pip install contrastive-lm 拉库，启 vLLM encoder + clm-serve API，对外讲 TypeSafe 兼容 Noul/Choice/Score typed questions | 仅基于 README 公开摘录 + GitHub Search API 元数据；具体 60M/30M/1M 数据集细节、vLLM Qwen3-8B pooling 参数、CLM-8B 8B 模型架构（Qwen3 基底？自研？）未在档案中给出 |
| 主路径 | CLMClient.system_one(state, questions={...}) → vLLM Qwen3-8B encoder pooling 抽 state embedding + action embedding → 75 MB reference head 计算 typed questions 答案（Noul/Choice/Score）→ 返回 typed answers → 应用层（shapeshift/Astra-Ares/deepopen）渲染对应卡片 | 主路径为 README 语义抽象；reference head 架构、typed questions 推理延迟、CLM-8B 与 Qwen3-8B 的权重关系（联合训练 / LoRA / 全量微调）均待核验 |
| 关键权衡 | 对比学习 states↔actions vs 对比学习训练稳定性 vs 缓存独立 vs 训练 / 服务成本下降 vs 9× Jev 速度 vs production 部署实用性 vs Terminal-Bench/DeepSWE SOTA verifier vs 评测榜单持续领先 vs Apache-2.0 vs 商业使用的可用度 vs vLLM serve + Qwen3-8B vs 多 GPU 部署的兼容性 | 档案明示「对比学习 + 缓存独立 + 9× 速度 + SOTA verifier + Apache-2.0 + pip install」六点权衡；具体 CLM-8B 模型架构、reference head 推理细节、对比学习训练稳定性边界、vLLM 多 GPU 兼容性均待核验 |
| 最小 PoC | `pip install contrastive-lm` → `vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --port 8090 &` → `clm-serve` → `CLMClient().system_one(state="Customer: my invoice was charged twice!", questions={"urgency": Noul(...), "department": Choice(...)})` 验证 typed questions 一次判断多问 → 接入 shapeshift 替换 TYPESAFE_API_KEY 为 CLM_BASE_URL + CLM_API_KEY 验证 Jev 应用层无缝切换 | PoC 范围、退出路径由档案「pip install + vLLM serve + clm-serve + shapeshift 切换」建议推导；具体 vLLM 多 GPU 部署、Hugging Face 模型下载、CLM-8B vs Qwen3-8B 关系均待核验 |

## 架构启发
Contrastive-LM/CLM 的核心启发是 **「对比学习 objective（连接 states 和 actions）+ States 和 actions 解耦（embeddings 独立缓存）」是 System One 决策模型的严肃工程化路径**。当前所有 LLM 决策模型都把 state 和 action 耦合编码（让模型生成完整结构），违背 state action 各自的缓存重用边界，引入冗余计算。CLM 尝试做 **「state embedding + action embedding 独立缓存」** 的解耦架构，让 state 查询和 action 推理可以独立扩展。更深层的启发是：**「TypeSafe 兼容 API」是 Jev 应用层生态的可扩展性关键**——CLM 提供 `CLMClient.system_one(state, questions={...})` 与 Jev 同构（shapeshift / Astra-Ares / deepopen 用 TYPESAFE_API_KEY，CLM 用 CLM_BASE_URL + CLM_API_KEY），应用层只需切换 base URL 和 key，无需改代码，是「单一 API 协议 + 多后端实现」的严肃工程化设计。再深一层：**「Apache-2.0 + pip install + vLLM serve + Hugging Face 模型发布」是开源 ML 项目的严肃工程化标配**——vs 闭源 SaaS API，Apache-2.0 让商用无门槛，pip install 让安装一行，vLLM serve 让 GPU serving 开箱即用，Hugging Face 让模型权重可下载可微调。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[应用层<br/>shapeshift / Astra-Ares / deepopen] --> CLMClient["CLMClient.system_one<br/>state, questions={...}<br/>CLM_BASE_URL + CLM_API_KEY"]
  CLMClient --> CLMServe["clm-serve :8700<br/>TypeSafe 兼容 API"]
  CLMServe --> RefHead["75 MB reference head<br/>首次运行下载"]
  RefHead --> VLLM["vLLM Qwen3-8B<br/>encoder pooling :8090"]
  VLLM --> StateEmb["state embedding<br/>独立缓存"]
  VLLM --> ActionEmb["action embedding<br/>独立缓存"]
  StateEmb --> RefHead
  ActionEmb --> RefHead
  RefHead --> Noul[Noul / Is it urgent?]
  RefHead --> Choice[Choice / Which team?]
  RefHead --> Score[Score / 0-10 priority?]
  Noul --> Answer[typed answers 返回]
  Choice --> Answer
  Score --> Answer
  Answer --> User
  CLMServe -. Apache-2.0 开源商用无门槛 .-> Pip["pip install contrastive-lm"]
  VLLM -. Hugging Face 发布 .-> Weights["CLM-8B 模型权重<br/>60M+30M+1M 三段训练"]
  User -. 切换后端 .-> JevAPI["Jev API<br/>TYPESAFE_API_KEY"]
  User -. 无缝切换 .-> CLMServe
```

## 定位判断
**挑战者 + 平台候选型项目（System One 决策模型 Apache-2.0 后端）。** Contrastive-LM/CLM 不仅是模型权重，更是「Jev 决策模型生态多后端」的标志——它提供 TypeSafe 兼容 API 让既有 Jev 应用层（shapeshift / Astra-Ares / deepopen）可无缝切换 CLM 后端，9× Jev 速度 + Terminal-Bench / DeepSWE SOTA verifier + Apache-2.0 + pip install 部署是「严肃挑战者」的标志。Apache-2.0 + Discord + Hugging Face + blog + Contrastive-LM org 显示网络效应雏形。但「挑战者 Jev」取决于一个关键问题：CLM-8B 在多任务 / 多语言的泛化稳定性 vs Jev 已积累的 12+ 项目生态。目前定位是「Apache-2.0 + SOTA verifier + pip install 部署」的最强严肃挑战者，向平台演进是合理路径。

## 风险/局限/泡沫点
- **对比学习训练稳定性:** 对比学习在多任务（computer-use / gaming / tool-calling）的训练稳定性需要长期验证
- **缓存独立实际收益:** states 和 actions 解耦 embeddings 独立缓存的实际成本下降需要实测
- **9× 速度边界:** 9× Jev 速度在 production 部署（多并发 / 长 context）的实用性需要验证
- **SOTA verifier 持续性:** Terminal-Bench / DeepSWE SOTA verifier 在新版本评测榜单的持续领先需要验证
- **TypeSafe 兼容性深度:** `CLMClient.system_one` 与 `JevClient.system_one` 在 Noul / Choice / Score 接口的语义兼容性需要验证
- **CLM-8B 模型架构未知:** 是 Qwen3-8B 基底微调 / 自研 8B / LoRA？档案未给出
- **Apache-2.0 商业威胁:** Apache-2.0 完全开源商用，TypeSafe AI 可能推出竞争性 Apache-2.0 模型
- **vLLM 多 GPU 兼容性:** vLLM serve + Qwen3-8B 在多 GPU 部署的兼容性需要长期验证
- **个人项目属性:** Contrastive-LM org 新创，社区治理 / 长期维护可持续性存疑

## 与同类项目的关系
- **vs TypeSafe AI Jev:** Jev 闭源 SaaS API；CLM Apache-2.0 开源 + TypeSafe 兼容 + 9× 速度 + SOTA verifier
- **vs deepopen-com/deepopen:** deepopen 是非自回归 System 1 决策引擎 Laya 改进 + 三检查点 + Apache-2.0；CLM 是对比学习 + 缓存独立 + TypeSafe 兼容 + 9× 速度
- **vs anishfn/shapeshift / miuuyy/Astra-Ares:** 那些是 Jev 应用层（UI 端 / Codex effort）；CLM 是 Jev 后端的 Apache-2.0 开源挑战者
- **vs Heman10x-NGU/openJev-verdict-2.0:** openJev-verdict 是 Non-Autoregressive Decision Engine；CLM 是对比学习 Decision Engine
- **vs wshobson/agents:** wshobson 是 Agent Skills 跨平台；CLM 是 System One 决策模型后端，互补
- **vs Hugging Face Transformers + 各类 BERT / ModernBERT:** 那些是通用 NLP 编码器；CLM 是 System One 决策专用对比学习模型

## 是否值得持续跟踪
**值得跟踪（Jev 决策模型 Apache-2.0 严肃挑战者）。** Contrastive-LM/CLM 代表了 System One 决策模型「Apache-2.0 + SOTA verifier + pip install 部署 + TypeSafe 兼容 API」的方向，无论其本身成败，这一方向是行业趋势。建议关注：CLM-8B 在多任务 / 多语言的泛化稳定性；Terminal-Bench / DeepSWE SOTA verifier 的持续领先；TypeSafe 兼容 API 在既有 Jev 应用层的无缝切换采用率；Apache-2.0 + pip install + vLLM serve + Hugging Face 的生态扩散。对 System One 决策模型研究者，这个项目是对比学习 states↔actions + 缓存独立 + 三段训练的具体实现；对 Jev 应用层开发者，可作为可无缝切换的 Apache-2.0 后端；对 ML 系统工程师，是「TypeSafe 兼容 API + vLLM serve + SOTA verifier + Hugging Face 模型发布」的具体路径。

## 后续观察点
- CLM-8B 是否扩展到 70B / 更大规模（vs Qwen3-8B 基底 8B 边界）
- Terminal-Bench / DeepSWE 持续保持 SOTA verifier 的稳定性
- TypeSafe 兼容 API 在既有 Jev 应用层（shapeshift / Astra-Ares / deepopen / kydlikebtc/awesome-jev）的无缝切换采用率
- Apache-2.0 + pip install + vLLM serve 的 PyPI / Hugging Face 下载量与活跃度
- Discord + Hugging Face + blog 在社区的活跃度与贡献者增长
- Contrastive-LM org 是否推出更多模型规模（如 CLM-1B / CLM-70B）
- 是否演化为独立平台（从 GitHub 仓库升级为对比学习 System One 模型门户）
- TypeSafe AI 是否推出竞争性 Apache-2.0 模型应对
- vLLM serve + Qwen3-8B 在多 GPU 部署（NVIDIA / AMD / Apple Silicon）的兼容性

---
> 数据来源: GitHub API (2026-09-25) | Stars: 769 | Forks: 61 | License: Apache-2.0 | 语言: Python | 创建: 2026-09-23 | pushed_at: 2026-09-24 | Topics: 无（org: Contrastive-LM）