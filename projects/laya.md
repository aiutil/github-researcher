---
title: "NandhaKishorM/laya"
slug: laya
date_added: "2026-10-07"
category: "平台候选"
emoji: "🧠"
stars: "31195 stars"
stars_delta: "19 天 31195⭐ ⑂2755 fork/star 8.8%"
language: "Python"
license: "Apache-2.0"
score: 90
tags: ["laya", "nandhakishorm", "decision-engine", "system-1", "non-autoregressive", "typed-decisions", "choice", "score", "noul", "rlcd", "reinforcement-learning", "strictly-proper-scoring-rules", "router", "multilingual", "100-languages", "modernbert", "pytorch", "mlx", "apple-silicon", "laya-mlx", "7-14ms-m3-max", "tile-gpu-fast-path", "pip-install", "typescript", "laya-ts", "npm", "extras-serve-mcp-langchain-llamaindex-crewai-onnx-fast", "kaggle-2xt4", "laya-train-csv", "laya-evals", "8192-token", "4000-token", "apache-2", "10068kb", "19-days", "huggingface"]
url: "https://github.com/NandhaKishorM/laya"
---

# NandhaKishorM/laya

## 一句话定位
33ms 非自回归 System 1 typed decision 引擎严肃工程化平台——把「LLM 分类 / 评分 / 决策」从「自回归逐 token 200ms+ 闭源」嵌入「Laya 33ms 单次前向 typed decision（choice/score/noul 三类型）+ 100+ 语言 + Router 自动路由到 english/multilingual checkpoint + Python 3.10+ pip install laya + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] 7 extras + TypeScript laya-ts/ + npm install laya-ts + MLX Apple Silicon 7-14ms + TileLang GPU fast path + RLCD reinforcement learning against strictly proper scoring rules + laya-multilingual 8192 token 多语言长文档 + 16-18/20 requests correct with up to ~4,000 tokens of text before them + laya-train --data tickets.csv --out ./ft CSV fine-tune + laya-evals + 0.766 fine-tuned accuracy on typed-decisions benchmark vs 0.362 base + Hugging Face Spaces demo + Open In Colab + dev.to article + docs/{hooks,structured,docker,langchain}.md + 12 topics + Apache-2.0 + Python 10068 KB」（NandhaKishorM 个人）。

## 它解决的问题
2026 年 LLM 分类 / 评分 / 决策赛道的痛点是 **「绝大多数 LLM 决策都是自回归逐 token 200ms+ 闭源 + 单分类 + 单语言 + 单 Python + 商用边界不清 + 速度承诺含糊」**。Laya 直击这一痛点：把「LLM 分类 / 评分 / 决策」从「自回归逐 token 200ms+ 闭源」嵌入「Laya 33ms 单次前向 typed decision（choice/score/noul 三类型）+ 100+ 语言 + Router 自动路由 + Python 3.10+ pip install laya + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] 7 extras + TypeScript laya-ts/ + npm install laya-ts + MLX Apple Silicon 7-14ms + TileLang GPU fast path + RLCD reinforcement learning against strictly proper scoring rules + laya-multilingual 8192 token 多语言长文档 + 16-18/20 requests correct with up to ~4,000 tokens + laya-train --data tickets.csv --out ./ft CSV fine-tune + laya-evals + 0.766 fine-tuned accuracy on typed-decisions benchmark vs 0.362 base + Hugging Face Spaces demo + Open In Colab + dev.to article + docs 全 + Apache-2.0」严肃工程化形态。解决的是 **「LLM 决策非自回归 33ms + 100+ 语言自动路由 + 严肃工程化 + 多框架覆盖 + 多语言绑定 + 学术严谨度（RLCD against strictly proper scoring rules）+ 商用清晰」** 的 LLM 决策严肃工程化问题。

## 为什么值得关注（2026-10-07）
- **Stars:** 31195（截至 2026-10-07），19 天 31195⭐，fork 2755，fork/star 8.8%
- **Forks:** 2755（典型高 fork 严肃工程化持续关注信号）
- **License:** Apache-2.0（明确许可，商用清晰）
- **语言:** Python
- **活跃度:** created 2026-09-18，pushed_at 2026-10-05，持续高活跃
- **规模:** 10068 KB
- **Topics:** 12 个覆盖（calibration / classification / decision-model / huggingface / jev / modernbert / multilingual / nlp / python / pytorch / routing / typed-decisions / zero-shot）

## 热度来源判断
NandhaKishorM/laya 的热度是 **「LLM 决策非自回归 33ms 刚需 × typed decision（choice/score/noul）覆盖 × 100+ 语言 × Router × 7 extras 严肃工程化 × 学术严谨度（RLCD against strictly proper scoring rules）」** 的强劲组合。LLM 决策是 2026 年最热赛道，但「自回归 + 200ms+」是真痛点——大多数用户的分类 / 评分 / 决策需求不需要自回归文本生成，只需要结构化决策输出（typed decision）。一个把「自回归 + 200ms+」嵌入「非自回归 + 33ms + typed decision + 100+ 语言 + Router + 7 extras + 学术严谨度」的严肃工程化平台自然爆火。2755 个 forks 反映社区高度参与——这正是「LLM 决策严肃工程化」类项目的网络效应。19 天 31195⭐ + fork/star 8.8% 说明这是真实严肃工程化信号（不是泡沫）。

## 关键技术亮点
1. **33ms 非自回归单次前向 typed decision（choice/score/noul 三类型）**——区别于自回归逐 token 200ms+ LLM，Laya 是非自回归 System 1 决策引擎，33ms 单次前向即可输出 typed decision（choice/score/noul 三类型）
2. **100+ 语言 + Router 自动路由**——Router 检测脚本和语言，自动路由到 english / multilingual checkpoint；同一调用在 100+ 语言下工作
3. **Python + TypeScript 双绑定 + 7 extras 严肃工程化**——Python 3.10+ pip install laya + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] 7 extras；TypeScript laya-ts/ + npm install laya-ts
4. **MLX Apple Silicon 7-14ms + TileLang GPU fast path**——MLX 在 M3 Max 上 7-14ms 决策；TileLang GPU fast path 多硬件严肃工程化承诺
5. **学术严谨度（RLCD against strictly proper scoring rules）**——训练用 RLCD（reinforcement learning against strictly proper scoring rules），区别于标准 cross-entropy，决策分数更严谨

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | LLM 分类 / 评分 / 决策的 33ms 非自回归 System 1 typed decision 引擎；choice / score / noul 三类型 + 100+ 语言 + Router 自动路由 + Python/TypeScript 双绑定 + 7 extras + MLX Apple Silicon 7-14ms + TileLang GPU fast path + RLCD + laya-multilingual 8192 token | 仅基于 README 描述的 33ms 单次前向 typed decision + choice/score/noul 三类型 + 100+ 语言 + Router 三 checkpoint + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] 7 extras + TypeScript laya-ts/ + MLX Apple Silicon 7-14ms + TileLang GPU fast path + RLCD against strictly proper scoring rules + laya-multilingual 8192 token + 16-18/20 requests correct with up to ~4,000 tokens + laya-train --data tickets.csv --out ./ft + laya-evals + 0.766 fine-tuned accuracy vs 0.362 base + 12 topics 覆盖 + 19 days 31195⭐ ⑂2755 fork/star 8.8% / Python Apache-2.0 10068 KB；具体 33ms 单次前向在多 typed decision 类型的准确性、100+ 语言自动路由严谨度、laya-multilingual 8192 token 长文档准确率、MLX Apple Silicon 7-14ms 多设备严谨度、TileLang GPU fast path 严谨度未在档案中明示 |
| 主路径 | 用户 → pip install laya → router = Router() → router.predict(state, questions) → choice/score/noul typed decision → result["answers"][key][type] → 33ms 训练在 RLCD strictly proper scoring rules + 100+ 语言自动路由 multilingual | 主路径为档案语义抽象；具体 33ms 单次前向在多 typed decision 类型的准确性、Router 三 checkpoint 调度准确性、choice/score/noul 训练目标严谨度未在档案中讨论 |
| 关键权衡 | 33ms 单次前向 vs 自回归逐 token 200ms+ + choice/score/noul 三类型 vs 单分类 + 100+ 语言自动路由 vs 单语言 + laya[7 extras] 多框架覆盖 vs 单 Python + TypeScript laya-ts 多语言绑定 vs 单 Python + MLX Apple Silicon 7-14ms vs 单 PyTorch + RLCD strictly proper scoring rules vs 标准 cross-entropy + laya-multilingual 8192 token vs laya 评估 + laya-train CSV fine-tune vs 默认 base + 0.766 vs 0.362 fine-tuned accuracy 严肃工程化承诺 + Apache-2.0 商用清晰 | 档案明示 33ms 单次前向 + choice/score/noul 三类型 + 100+ 语言 + Router + 7 extras + TypeScript laya-ts + MLX Apple Silicon 7-14ms + TileLang GPU fast path + RLCD + laya-multilingual 8192 token + 16-18/20 vs 8-17/20 + laya-train --data tickets.csv + laya-evals + 0.766 vs 0.362 + Apache-2.0；具体 33ms 单次前向在多 typed decision 类型的严谨度、100+ 语言自动路由严谨度、MLX Apple Silicon 7-14ms 多设备严谨度未在档案中讨论 |
| 最小 PoC | pip install laya（Python 3.10+） → 准备 example state + questions{department: choice, urgency: score, churn_risk: noul} → router = Router() → router.predict(state, questions) → 验证 choice/score/noul 三类型输出 + 验证 33ms 决策时间 → 试 100+ 语言（印地语 / 西班牙语）验证 Router 自动路由 multilingual → 试 laya-train --data tickets.csv --out ./ft 验证 CSV fine-tune → 试 Apple Silicon MLX 验证 7-14ms | PoC 范围由档案「33ms 单次前向 + choice/score/noul 三类型 + 100+ 语言 + Router + 7 extras + TypeScript + MLX 7-14ms + TileLang + RLCD + 0.766 vs 0.362」建议推导；具体严谨度未在档案中讨论 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Dev[开发者] --> Install[pip install laya<br/>Python 3.10+]
  Install --> Router[Router<br/>downloads checkpoint first use<br/>Router(preload=True) loads all three up front]
  Router -.detect script+lang.-> Decide[Router 选 english / multilingual]
  Decide --> English[laya-english checkpoint]
  Decide --> Multi[laya-multilingual checkpoint<br/>100+ languages]
  Dev --> State[state: Hi, we were billed twice...]
  Dev --> Questions[questions:<br/>department: choice<br/>urgency: score<br/>churn_risk: noul]
  State --> Predict[router.predict]
  Questions --> Predict
  English --> Predict
  Multi --> Predict
  Predict --> Out[result answers key type<br/>choice / score / noul]
  Predict --> Meta[result routing model<br/>english / multilingual]
  Predict -.33ms.-> Fast[单次前向 33ms]
  Multi -.100+ lang.-> ML[100+ languages<br/>Hindi/Spanish/...]
  Multi -.8192 tokens.-> Long[laya-multilingual max_len=8192<br/>16-18/20 ~4k tokens]
  Predict -.extras.-> Extras[laya serve<br/>laya mcp<br/>laya langchain / llamaindex / crewai<br/>laya onnx<br/>laya fast TileLang GPU]
  Predict -.TS.-> TS[TypeScript laya-ts/<br/>npm install laya-ts]
  English -.Apple.-> MLX[laya-mlx 7-14ms<br/>Apple Silicon M3 Max]
  Fast -.RLCD.-> RL[RLCD reinforcement learning<br/>against strictly proper scoring rules]
  Predict -.train.-> Train[laya-train --data tickets.csv --out ./ft<br/>+ laya-evals]
  Train --> FT[0.766 fine-tuned accuracy<br/>vs 0.362 base on typed-decisions]
  Train -.Kaggle.-> K2T4[Kaggle 2xT4 notebook]
  Train -.Apple.-> APS[Apple Silicon MPS / CPU script]
  FT --> Saved[laya-typed-decisions checkpoint<br/>saved question schema]
  Fast -.Demo.-> Demo[Hugging Face Spaces demo<br/>laya-demo]
  Fast -.Colab.-> Colab[Open In Colab]
  Fast -.Article.-> Article[dev.to article<br/>I built non-autoregressive decision models a year ago]
  Fast -.Backend.-> Back[laya.backends<br/>Agent backend eager / set_backend<br/>0.3.28 packaging fix]
  Fast -.License.-> Ap[Apache-2.0<br/>NandhaKishorM 个人<br/>+ Buy Me a Coffee]
  Fast -.Docs.-> Docs[docs/{hooks,structured,docker,langchain}.md<br/>+ API reference + Colab]
  Fast -.HF.-> HF[convaiinnovations/laya + laya-multilingual]
```

## 架构启发
NandhaKishorM/laya 的核心启发是 **「LLM 决策应该非自回归 + 33ms + typed decision + 100+ 语言——System 1 决策引擎是 LLM 应用的杀手架构」**。当前 LLM 决策普遍基于自回归逐 token（200ms+），但绝大多数分类 / 评分 / 决策需求不需要生成文本——只需要结构化决策输出（typed decision）。Laya 尝试做「LLM 决策的非自回归革命」，类似：
  - llama.cpp 之于移动端 LLM（Ollama / LM Studio 之于桌面）
  - vLLM 之于 LLM 服务化推理
  - Speculative decoding 之于自回归 LLM 加速

更深层的启发是：**MoE 模型的稀疏激活 + RLCD 强化学习 + 100+ 语言 + Router 自动路由 + 7 extras 严肃工程化（serve/mcp/langchain/llamaindex/crewai/onnx/fast） = LLM 决策的完整严肃工程化栈**。这种「System 1 决策引擎 + 严肃工程化栈」组合，是 2026 年 LLM 决策严肃工程化方向的范式。19 天 31195⭐ + 2755 forks 已显示其严肃工程化影响力。

## 定位判断
**平台候选型项目（LLM 决策严肃工程化平台）。** NandhaKishorM/laya 不仅是 LLM 决策工具，更试图成为「LLM 决策的非自回归革命」的严肃工程化平台——类似 TypeSafe's Jev 但 Apache-2.0 + Python/TypeScript 双绑定 + 100+ 语言 + 7 extras 严肃工程化。19 天 31195⭐ + 2755 forks 已显示其严肃工程化影响力。但「LLM 决策的非自回归革命」取决于一个关键问题：33ms 单次前向在多 typed decision 类型的准确性是否能持续保持 0.766 fine-tuned accuracy——若 typed decision 类型变化或 prompt 分布变化导致准确率下降，typed decision 的严肃工程化承诺会受影响。目前定位是「最有影响力的 LLM 决策严肃工程化平台」，向更通用 LLM 决策平台演进是合理路径。

## 风险/局限/泡沫点
- **33ms 单次前向准确性边界:** typed decision 在多类型（choice/score/noul）的准确性是否能持续保持 0.766 fine-tuned accuracy；README 明示 0.766 vs 0.362 base，但具体多 prompt 类型是否同样 0.766 未明示
- **100+ 语言自动路由边界:** Router 在多语言的自动路由准确性；README 明示 Router 检测脚本和语言自动路由，但具体多语言边界未明示
- **laya-multilingual 8192 token 长文档准确率:** README 明示 16-18/20 ~4k tokens，8-17/20 超出（4K token），具体 4000+ token 准确率下降
- **MLX Apple Silicon 7-14ms 严肃工程化承诺:** README 明示 M3 Max 7-14ms，但具体多 Apple Silicon 设备（Macbook Air / Macbook Pro / Mac Pro / iPad / iPhone）边界未明示
- **laya[fast] TileLang GPU fast path:** TileLang GPU fast path 是较新的库，社区成熟度与多硬件兼容性未明示
- **laya.backends 0.3.28 packaging 修复:** README 明示 0.3.25 / 0.3.26 / 0.3.27 缺失 laya.backends，0.3.28 才修复——之前版本用户可能受影响
- **个人项目属性:** NandhaKishorM 个人维护，2755 forks 但核心治理仍集中，长期可持续性需要观察

## 与同类项目的关系
- **vs TypeSafe's Jev:** TypeSafe 的 Jev 是闭源商业决策模型 API；Laya 是 Apache-2.0 + Python/TypeScript 双绑定 + 100+ 语言 + 7 extras 严肃工程化
- **vs Transformers pipeline:** Transformers pipeline 是通用 NLP 库（自回归逐 token 200ms+）；Laya 是非自回归 + 33ms + typed decision + 100+ 语言严肃工程化
- **vs LangChain / LlamaIndex:** LangChain / LlamaIndex 是 LLM 编排框架；Laya 通过 laya[langchain] / laya[llamaindex] extras 与之集成
- **vs CrewAI / AutoGen:** CrewAI / AutoGen 是多 Agent 编排框架；Laya 通过 laya[crewai] extras 与之集成
- **vs ModernBERT / BERT:** ModernBERT 是通用 transformer 编码器；Laya 在 ModernBERT 之上做 typed decision 严肃工程化
- **vs scikit-learn classifiers:** scikit-learn classifiers 是传统机器学习分类器；Laya 是基于深度学习的非自回归 + 100+ 语言严肃工程化

## 是否值得持续跟踪
**值得跟踪（LLM 决策严肃工程化平台）。** NandhaKishorM/laya 代表了「LLM 决策非自回归 33ms 严肃工程化」诉求，无论其本身成败，这一方向是行业趋势。建议关注：33ms 单次前向在多 typed decision 类型的准确性持续性（决定 typed decision 严肃工程化承诺）、100+ 语言自动路由在多语言的严谨度、laya-multilingual 8192 token 长文档准确率在 4000+ token 的下降度、MLX Apple Silicon 7-14ms 在多设备的严肃工程化承诺、laya[fast] TileLang GPU fast path 的多硬件严肃工程化承诺。对 LLM 决策应用开发者，Laya 是「非自回归 + 33ms + typed decision + 100+ 语言 + Apache-2.0」的实用严肃工程化方案，值得直接采用。

## 后续观察点
- 33ms 单次前向在多 typed decision 类型的准确性持续性
- 100+ 语言自动路由在多语言的严谨度
- laya-multilingual 8192 token 长文档准确率在 4000+ token 的下降度
- MLX Apple Silicon 7-14ms 在多 Apple Silicon 设备的严谨度
- laya[fast] TileLang GPU fast path 的多硬件严谨度
- laya.backends 0.3.28 packaging 修复对之前版本用户的回溯
- 个人项目治理结构（2755 forks 但核心治理仍集中于 NandhaKishorM 个人）

---
> 数据来源: GitHub API (2026-10-07) | Stars: 31195 | Forks: 2755 | License: Apache-2.0 | 语言: Python | 创建: 2026-09-18 | 大小: 10068 KB