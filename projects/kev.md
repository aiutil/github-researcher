---
title: "jaredpalmer/kev"
slug: kev
date_added: "2026-10-07"
category: "工具型"
emoji: "🧪"
stars: "8597 stars"
stars_delta: "20 天 8597⭐ ⑂563 fork/star 6.5%"
language: "Python"
license: "Apache-2.0"
score: 84
tags: ["kev", "jaredpalmer", "decision-model", "system-one", "jev-like", "qwen3-5", "qwen3-8", "kev-0-8b", "kev-4b", "kev-9b", "kev-27b", "noul", "choice", "score", "calibrated-probabilities", "fitted-temperature", "drop-in-jev", "typescript-system-one-api", "modal-deploy", "hugging-face", "hugging-face-spaces", "frozen-eval-suites", "breadth-v1", "14-datasets", "5-areas", "decision-index", "23-3-52-3", "brier-score", "0-851-vs-jev-0-857", "8k-context", "65k-context", "27b-65k", "8192", "mlx-apple-silicon", "cuda", "apache-2", "170467kb", "20-days"]
url: "https://github.com/jaredpalmer/kev"
---

# jaredpalmer/kev

## 一句话定位
自训 Jev-like System 1 决策模型族严肃工程化平台——把「Jev 闭源决策 API」推到「Kev 自训 Qwen3.5 / Qwen3.8 + Kev-0.8B/4B/9B/27B 4 size + noul/choice/score 单请求三类型共享 + Calibrated probabilities by default（fitted temperature）+ Drop-in for Jev: TypeSafe Python SDK 同样工作 + 65,536 tokens (Kev-27B) / 8,192 其他 + MLX Apple Silicon + CUDA + 任何 4GB GPU (Kev-0.8B) / L40S, H100 (4B/9B) / B200 H200 H100 80GB (27B) / 96-128 GB Mac (27B) + accuracy new sources 0.648-0.851 / trained sources 0.827-0.873 / Brier 0.481-0.225 + 0.851 vs Jev 0.857 within 1 point + frozen eval suites breadth-v1 14 数据集 5 区域 + Held-out datasets: index 23.3/38.0/41.0/52.3 + Validated context 8,192-65,536 + coding-agent skill Modal 一键部署 + scale to zero + v1.0 tag + kev-1.0 release SHA-256 + Hugging Face Spaces demo + Apache-2.0」（jaredpalmer 个人）。

## 它解决的问题
2026 年 Jev-like System 1 决策模型赛道的痛点是 **「Jev 闭源决策 API + 自训严肃工程化困难 + 多 size 覆盖不足 + 多硬件适配不足 + 多 benchmark 严谨度不足 + 上下文扩展不足 + 部署严肃工程化不足」**。Kev 直击这一痛点：把「Jev 闭源决策 API」推到「Kev 自训 Qwen3.5 / Qwen3.8 + Kev-0.8B/4B/9B/27B 4 size + noul/choice/score 单请求三类型共享 + Calibrated probabilities by default（fitted temperature）+ Drop-in for Jev TypeSafe Python SDK + 65,536 tokens (Kev-27B) / 8,192 其他 + MLX Apple Silicon + CUDA + accuracy new sources 0.648-0.851 / trained sources 0.827-0.873 / Brier 0.481-0.225 + 0.851 vs Jev 0.857 within 1 point + frozen eval suites breadth-v1 14 数据集 5 区域 + Held-out datasets: index 23.3/38.0/41.0/52.3 + Validated context 8,192-65,536 + coding-agent skill Modal 一键部署 + scale to zero + v1.0 tag + kev-1.0 release SHA-256 + Hugging Face Spaces demo + Apache-2.0」严肃工程化形态。解决的是 **「自训 Jev-like 决策模型族严肃工程化 + 多 size 覆盖 + 多硬件适配 + 多 benchmark 严谨度 + 上下文扩展 + 部署严肃工程化」** 的 Jev-like 决策模型严肃工程化问题。

## 为什么值得关注（2026-10-07）
- **Stars:** 8597（截至 2026-10-07），20 天 8597⭐，fork 563，fork/star 6.5%
- **Forks:** 563（典型高 fork 严肃工程化持续关注信号）
- **License:** Apache-2.0（明确许可，商用清晰）
- **语言:** Python
- **活跃度:** created 2026-09-17，pushed_at 2026-10-06，持续高活跃
- **规模:** 170467 KB
- **Topics:** 3 个覆盖（decision-model / jev / qwen3）

## 热度来源判断
jaredpalmer/kev 的热度是 **「Jev-like 决策模型自训严肃工程化刚需 × Qwen3.5/Qwen3.8 base × 4 size 覆盖广度 × Calibrated probabilities × Drop-in for Jev TypeSafe Python SDK × frozen eval suites breadth-v1 × Modal 一键部署」** 的强劲组合。Jev-like 决策模型是 2026 年最热赛道（System 1 typed decision），但「Jev 闭源 + 自训严肃工程化困难」是真痛点——大多数用户的 Jev-like 决策模型需求需要自训（specific domain），但自训严肃工程化（multi-size + multi-hardware + multi-benchmark + multi-context + deploy）困难。一个把「Jev 闭源」推到「Kev 自训严肃工程化」的严肃工程化平台自然爆火。563 个 forks 反映社区高度参与。20 天 8597⭐ + fork/star 6.5% 说明这是真实严肃工程化信号（不是泡沫）。

## 关键技术亮点
1. **Qwen3.5/Qwen3.8 base + 4 size 覆盖广度**——Kev-0.8B/4B/9B/27B 基于 Qwen3.5-0.8B-Base / Qwen3.5-4B-Base / Qwen3.5-9B-Base / Qwen3.8-27B post-trained；任何 4GB GPU (Kev-0.8B) / L40S, H100 (4B/9B) / B200 H200 H100 80GB (27B) / 96-128 GB Mac (27B)
2. **小 adapter on frozen base 训练 recipe + Calibrated probabilities fitted temperature**——Kev-0.8B/4B/9B 训练 recipe：小 adapter on frozen base + Calibrated probabilities fitted temperature（每个 checkpoint 配 fitted temperature）
3. **noul/choice/score 单请求三类型共享 + Drop-in for Jev TypeSafe Python SDK**——单请求支持 noul / choice / score 三类型；TypeSafe Python SDK 直接对接 Kev server 不需要修改
4. **8,192 token 上下文 vs Kev-27B 65,536 token 上下文 + MLX/CUDA + 0.648-0.851 accuracy**——Kev-27B 65,536 token 上下文；MLX Apple Silicon + CUDA 多硬件；accuracy new sources 0.648-0.851 / trained 0.827-0.873 / Brier 0.481-0.225；Kev-27B 0.851 vs Jev 0.857 within 1 point
5. **frozen eval suites breadth-v1 14 数据集 5 区域 + Modal 一键部署 + scale to zero**——14 public datasets 5 areas 严格冻结；coding-agent skill Modal 一键部署 HTTPS endpoint + scale to zero when idle；v1.0 tag + kev-1.0 release SHA-256

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 自训 Jev-like System 1 决策模型族；Kev-0.8B/4B/9B/27B 基于 Qwen3.5/Qwen3.8 + noul/choice/score 单请求三类型共享 + Calibrated probabilities fitted temperature + Drop-in for Jev TypeSafe Python SDK + 8k-65k token + MLX/CUDA | 仅基于 README 描述的 Kev-0.8B/4B/9B/27B 4 size + Qwen3.5/Qwen3.8 base + 小 adapter on frozen base + Calibrated probabilities fitted temperature + Drop-in for Jev + 65,536 tokens (Kev-27B) / 8,192 其他 + MLX Apple Silicon + CUDA + accuracy new sources 0.648-0.851 / trained 0.827-0.873 / Brier 0.481-0.225 + 0.851 vs Jev 0.857 within 1 point + frozen eval suites breadth-v1 14 数据集 + decision-index 23.3-52.3 + Validated context 8,192-65,536 + coding-agent skill Modal 一键部署 + scale to zero + v1.0 tag + kev-1.0 release SHA-256 + Apache-2.0；具体 Kev 在多 GPU 调度的严谨度、Kev-27B 51 GB full weights 在 80GB H100 / 96-128 GB Mac 的严肃工程化承诺、accuracy 在多 benchmark 的严谨度、Drop-in for Jev 在多 Jev API 版本的兼容性未在档案中明示 |
| 主路径 | 开发者 → --run jaredpalmer/kev-4b@v1.0 → Kev-4B / Kev-9B / Kev-27B / Kev-0.8B → noul/choice/score 单请求三类型 → result[type] → Calibrated probabilities fitted temperature → Drop-in for Jev TypeSafe Python SDK → 8k-65k token 上下文 | 主路径为档案语义抽象；具体 Kev 在多 GPU 调度的严谨度、Drop-in for Jev 在多 Jev API 版本的兼容性、accuracy 在多 benchmark 的严谨度未在档案中讨论 |
| 关键权衡 | 4 size 覆盖广度 vs 单 size 决策模型 + Qwen3.5/Qwen3.8 base vs 自训 base + 小 adapter on frozen base vs full weights + noul/choice/score 单请求三类型共享 vs 单请求单类型 + Calibrated probabilities fitted temperature vs 默认概率 + Drop-in for Jev TypeSafe Python SDK vs 单接入 + 8,192 token vs 65,536 token (Kev-27B) + MLX Apple Silicon vs CUDA + 0.648-0.851 accuracy new sources vs Jev 0.857 + frozen eval suites breadth-v1 14 数据集 vs 单数据集 + Modal 一键部署 vs 单部署 + scale to zero vs 单实例 + Apache-2.0 商用清晰 | 档案明示 Kev-0.8B/4B/9B/27B 4 size + Qwen3.5/Qwen3.8 + 小 adapter on frozen base + Kev-27B 51 GB full weights + Calibrated probabilities fitted temperature + Drop-in for Jev + 8k-65k token + MLX/CUDA + 0.648-0.851 + Brier 0.481-0.225 + 0.851 vs Jev 0.857 within 1 point + frozen eval suites breadth-v1 14 数据集 + Modal + scale to zero + v1.0 tag + SHA-256 + Apache-2.0；具体 Kev 在多 GPU 调度的严谨度、Drop-in for Jev 在多 Jev API 版本的兼容性、Modal 一键部署在多 Claude Code / Codex / Cursor harness 的兼容性未在档案中讨论 |
| 最小 PoC | python -m pip install jaredpalmer-kev → --run jaredpalmer/kev-4b@v1.0 → 准备 state + questions{noul: 是否取消, choice: 哪个部门, score: 紧急程度} → 单次 predict → 验证 noul/choice/score 三类型输出 + 验证 Calibrated probabilities fitted temperature → 试 Apple Silicon MLX 验证 8,192-65k token → 试 TypeSafe Python SDK 验证 Drop-in for Jev → 试 Modal 一键部署在 Claude Code / Cursor harness → 验证 v1.0 tag SHA-256 | PoC 范围由档案「Kev-0.8B/4B/9B/27B 4 size + Qwen3.5/Qwen3.8 base + 小 adapter on frozen base + Calibrated probabilities fitted temperature + Drop-in for Jev + 8k-65k token + MLX/CUDA + 0.648-0.851 + frozen eval suites breadth-v1 + Modal 一键部署 + scale to zero + v1.0 tag SHA-256」建议推导；具体严谨度未在档案中讨论 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Dev[开发者] --> Install[kev install<br/>Python 3.10+]
  Install --> Run[--run jaredpalmer/kev-4b@v1.0]
  Run --> Model4B[Kev-4B<br/>Qwen3.5-4B-Base Apache-2.0<br/>小 adapter on frozen base]
  Run --> Model0B[Kev-0.8B<br/>Qwen3.5-0.8B-Base Apache-2.0<br/>任何 4GB GPU]
  Run --> Model9B[Kev-9B<br/>Qwen3.5-9B-Base Apache-2.0<br/>L40S, H100]
  Run --> Model27B[Kev-27B<br/>Qwen3.8-27B post-trained<br/>B200, H200, H100 80GB<br/>51 GB full weights]
  Model4B --> Question[state + questions<br/>noul + choice + score 三类型共享]
  Model0B --> Question
  Model9B --> Question
  Model27B --> Question
  Question --> Predict[predict]
  Predict --> Type1[noul: probability yes]
  Predict --> Type2[choice: 选 billing/technical/other]
  Predict --> Type3[score: not urgent/soon/blocking]
  Predict -.Calibrated.-> Temp[fitted temperature<br/>Calibrated probabilities by default]
  Predict -.Drop-in.-> Jev[Drop-in for Jev<br/>TypeSafe Python SDK 同样工作]
  Model4B -.Validated.-> V4B[Validated context 8,192<br/>Held-out datasets index 38.0]
  Model0B -.Validated.-> V0B[Validated context 8,192<br/>Held-out datasets index 23.3<br/>measured to 65k tokens]
  Model9B -.Validated.-> V9B[Validated context 8,192<br/>Held-out datasets index 41.0]
  Model27B -.Validated.-> V27B[Validated context 65,536<br/>Held-out datasets index 52.3]
  Model4B -.Backend.-> CUDA[CUDA]
  Model0B -.Backend.-> MLX[MLX Apple Silicon]
  Model9B -.Backend.-> CUDA
  Model27B -.Backend.-> CUDA
  Model0B -.Backend.-> MLX
  Predict -.accuracy.-> Acc[New sources 0.648-0.851<br/>Trained sources 0.827-0.873<br/>Brier 0.481-0.225]
  Acc -.0.851.-> JComp[Kev-27B 0.851 vs Jev 0.857<br/>within 1 point]
  Predict -.Eval.-> Eval[frozen eval suites breadth-v1<br/>14 public datasets 5 areas<br/>chance-corrected index]
  Predict -.Modal.-> Modal[Modal 一键部署<br/>HTTPS endpoint<br/>scale to zero when idle]
  Modal --> CC[Claude Code]
  Modal --> CX[Codex CLI]
  Modal --> CUR[Cursor]
  Modal --> OC[OpenCode]
  Model4B -.License.-> Ap[Apache-2.0 商用清晰<br/>jaredpalmer 个人]
  Model4B -.Weights.-> Hub[Hugging Face Collection<br/>+ Spaces demo<br/>+ v1.0 tag + kev-1.0 release SHA-256]
  Model4B -.Recipes.-> Recipes[小 adapter on frozen base<br/>Kev-27B full weights 51 GB<br/>每个 model card 全 recipe]
```

## 架构启发
jaredpalmer/kev 的核心启发是 **「Jev-like 决策模型自训严肃工程化必须四件事：多 size 覆盖 + 多硬件适配 + frozen eval suites + 一键部署」**。当前大多数 Jev-like 决策模型自训都是「单 size + 单硬件 + 单 benchmark + 手动部署」——严肃工程化友好度不足。Kev 尝试做「Jev-like 决策模型自训的严肃工程化栈」——类似：
  - Ollama / LM Studio 之于本地 LLM（多 size + 多硬件 + 一键启动）
  - Hugging Face Transformers 之于 LLM（多 model + 多 training recipe）

更深层的启发是：**「Kev-0.8B/4B/9B 小 adapter on frozen base vs Kev-27B full weights 51 GB」的设计哲学是「严肃工程化优先（adapter） vs 严肃工程化承诺（full weights）」**。Kev-0.8B/4B/9B 是「严肃工程化优先」（小 adapter 可以快速部署到任何硬件），Kev-27B 是「严肃工程化承诺」（full weights 保证最佳 accuracy）。这种「分级严肃工程化」是 2026 年自训 LLM 严肃工程化方向的范式。20 天 8597⭐ + 563 forks 已显示其严肃工程化影响力。

## 定位判断
**工具型项目（自训 Jev-like 决策模型族严肃工程化）。** jaredpalmer/kev 不仅是 Jev-like 决策模型自训工具，更试图成为「Jev-like 决策模型自训严肃工程化」的范式——类似 TypeSafe Jev 的开源 Apache-2.0 版本。20 天 8597⭐ + 563 forks 已显示其严肃工程化影响力。但「Jev-like 决策模型自训严肃工程化」取决于一个关键问题：Kev-0.8B/4B/9B/27B 4 size 在多用户 specific domain 自训的严肃工程化承诺（adapter 可行性）——若 adapter 在多 specific domain 的准确性下降（catastrophic forgetting），Kev 自训严肃工程化承诺会受影响。目前定位是「最有影响力的 Jev-like 决策模型自训严肃工程化平台」，向更通用决策模型自训平台演进是合理路径。

## 风险/局限/泡沫点
- **Kev-27B 51 GB full weights 严肃工程化承诺:** README 明示 Kev-27B starts from Qwen's post-trained release, and we don't know what that was trained on——Kev-27B 严肃工程化承诺基于「我们不知道的 Qwen post-trained release」，存在版本不一致风险
- **accuracy new sources 0.648-0.851 严肃工程化承诺:** README 明示「We don't know what Jev was trained on, so this isn't a controlled comparison of the two architectures」——0.851 vs Jev 0.857 within 1 point 是非受控对比，严肃工程化承诺边界
- **frozen eval suites breadth-v1 14 数据集 严谨度:** README 明示「We pick checkpoints using the development sets and read each test set only once per released model」——frozen eval 是为了避免数据泄露，但仍存在 benchmark gaming 风险
- **MLX Apple Silicon 严肃工程化承诺:** README 明示 Kev-27B 在 96-128 GB Mac 上「expected, not measured」——部分严肃工程化承诺基于期望而非实测
- **Drop-in for Jev TypeSafe Python SDK 兼容性:** README 明示「the TypeSafe Python SDK works against a Kev server unchanged」——但具体 Jev API 版本变化时的兼容性未明示
- **Modal 一键部署严肃工程化承诺:** Modal 是较新的 serverless GPU 平台，社区成熟度与多 vendor 兼容性未明示
- **个人项目属性:** jaredpalmer 个人维护，563 forks 但核心治理仍集中，长期可持续性需要观察

## 与同类项目的关系
- **vs TypeSafe's Jev:** TypeSafe 的 Jev 是闭源商业决策模型 API；Kev 是 Apache-2.0 自训 Jev-like 决策模型族（Drop-in for Jev TypeSafe Python SDK）
- **vs Laya:** Laya 是非自回归 + 33ms + typed decision + 100+ 语言 + Apache-2.0 严肃工程化平台；Kev 是自训 Jev-like 决策模型族 + 4 size + frozen eval suites + Modal 部署
- **vs Qwen3.5/Qwen3.8:** Qwen3.5/Qwen3.8 是通用 LLM；Kev 在 Qwen3.5/Qwen3.8 之上做 Jev-like 决策模型自训严肃工程化
- **vs Hugging Face Transformers:** Transformers 是通用 transformer 库；Kev 在 Transformers 之上做 Jev-like 决策模型自训严肃工程化
- **vs Modal / Replicate:** Modal / Replicate 是 serverless ML 部署平台；Kev 通过 Modal 一键部署严肃工程化
- **vs vLLM / TGI:** vLLM / TGI 是 LLM 服务化推理框架；Kev 是决策模型自训严肃工程化（不是推理框架）

## 是否值得持续跟踪
**值得跟踪（Jev-like 决策模型自训严肃工程化平台）。** jaredpalmer/kev 代表了「Jev-like 决策模型自训严肃工程化」诉求，无论其本身成败，这一方向是行业趋势。建议关注：Kev-27B 51 GB full weights 在多硬件的严肃工程化承诺（决定 Kev-27B 严肃工程化可行性）、accuracy new sources 0.648-0.851 在多 specific domain 的严谨度（决定 Kev 自训严肃工程化承诺）、frozen eval suites breadth-v1 14 数据集 在多 benchmark 的严谨度（决定 Kev 严肃工程化严谨度）、MLX Apple Silicon 96-128 GB Mac「expected, not measured」的严肃工程化承诺兑现度。对 Jev-like 决策模型自训严肃工程化用户，Kev 是「Apache-2.0 + 多 size + frozen eval + Modal 部署」的实用严肃工程化方案，值得直接采用。

## 后续观察点
- Kev-27B 51 GB full weights 在多硬件（80GB H100 / 96-128 GB Mac）的严肃工程化承诺
- accuracy new sources 0.648-0.851 在多 specific domain 自训的严谨度
- frozen eval suites breadth-v1 14 数据集 在多 benchmark 的严谨度
- MLX Apple Silicon 96-128 GB Mac「expected, not measured」的严肃工程化承诺兑现度
- Drop-in for Jev TypeSafe Python SDK 在多 Jev API 版本的兼容性
- Modal 一键部署在多 Claude Code / Codex / Cursor harness 的兼容性
- 个人项目治理结构（563 forks 但核心治理仍集中于 jaredpalmer 个人）

---
> 数据来源: GitHub API (2026-10-07) | Stars: 8597 | Forks: 563 | License: Apache-2.0 | 语言: Python | 创建: 2026-09-17 | 大小: 170467 KB