---
title: "MoonshotAI/Kimi-K3"
slug: kimi-k3
date_added: "2026-07-30"
last_seen_date: "2026-07-30"
category: "基础设施候选"
emoji: "🧠"
stars: "5,511 stars"
stars_delta: "3 天 5.5K⭐（2026-07-27 创建）"
language: "N/A（模型权重仓库）"
score: 93
tags: ["llm", "moe", "agentic", "multimodal", "moonshot", "long-context"]
url: "https://github.com/MoonshotAI/Kimi-K3"
---

# MoonshotAI/Kimi-K3

## 一句话定位
首个开源 3T 级模型——2.8T 参数 MoE / 104B 激活，KDA + Attention Residuals 新架构，原生多模态 + 1M 上下文，面向 long-horizon coding 与 agentic knowledge work。

## 它解决的问题
前沿大模型能力此前主要由闭源 API（Claude/GPT 系列）提供，开源社区能拿到的最大公开权重长期停留在更低量级。Kimi K3 把 3T 级模型的完整权重开源，目标用户是需要前沿能力且要求权重可控的研究者与企业——可做评测复现、本地/私有部署、二次训练。

## 为什么值得关注（2026-07-30）
- **规模里程碑**：首个公开权重的 3T 级模型（2.8T 总参数）。
- **新架构**：Kimi Delta Attention (KDA) + Attention Residuals (AttnRes)，不同于标准 MLA/MHA。
- **生态动员**：发布同日带动 MoonEP（训练通信）、deltafin（本地推理）、axrl（Agent RL）涌入 trending。
- **热度真实**：3 天 5.5K⭐、397 fork、11 open issues，有权重可下载。

## 热度来源判断
**真实需求主导，但叠加品牌效应。** Moonshot AI（月之暗面）是国内头部模型团队，Kimi 系列已有用户基础；"首个开源 3T"的话题性放大了传播。但 397 fork + 有可下载权重说明不只是围观。风险在于：跑分对标为厂商自报，需独立复现才能区分"前沿能力"与"营销叙事"。

## 关键技术亮点
1. **KDA + Attention Residuals（AttnRes）新注意力架构**：93 层中 69 层用 KDA、24 层用 Gated MLA，官方称这是 scaling 效率提升的关键（2.5× over K2，待验证）。
2. **Stable LatentMoE**：896 专家选 16 + 2 共享专家，SiTU-GLU 激活，3584 Latent MoE 维度。稀疏度设计旨在稳定大规模 MoE 训练。
3. **1M token 上下文 + 原生多模态**：同一模型理解文本与图像（MoonViT-V2，401M 参数视觉编码器），上下文窗口 1,048,576。
4. **量化感知训练**：MXFP4 权重 / MXFP8 激活，训练阶段即引入量化，非训后量化。

## 架构启发
K3 的设计哲学是"用架构创新换 scaling 效率"而非单纯堆参数：KDA/AttnRes 重新设计注意力，Stable LatentMoE 重新设计 MoE 稀疏度与稳定性。896 选 16 的稀疏比（~1.8%）配合 104B 激活，说明团队在"总容量"与"单 token 成本"间做了明确权衡。Trade-off：2.8T 权重的存储/带宽成本极高，推理侧工程挑战大（deltafin 的 14.6s/token 是反面证明）。

## 定位判断
在开源模型生态中，K3 是**新的规模上限标杆**。它不是轻量推理模型，而是"前沿能力开源化"的载体——价值在于权重可复现、可二次训练、可私有部署。企业若要用，需配套量化/蒸馏工程或云端推理服务。

## 风险 / 局限 / 泡沫点
1. **评测为厂商自报**：GPQA 93.5、Terminal-Bench 88.3 等对标 Claude Fable 5/GPT-5.6 的分数存在选择性披露风险，部分项（FrontierSWE、Kimi Code Bench）落后于对标模型，需独立复现。
2. **"2.5× scaling 效率"为官方声称**：基于自比 K2，缺乏第三方对照，待验证。
3. **推理成本高**：2.8T 权重的存储与带宽需求使本地推理不实用（deltafin 14.6s/token），企业落地依赖云端服务或激进度量化。
4. **License 限制**：Kimi K3 License（非标准开源协议），商用条款需确认。

## 与同类项目的关系
- **vs DeepSeek-V3/R1**：同为开源大 MoE，K3 在总参数量上更高（2.8T），但 DeepSeek 系列有更长的独立复现与生态成熟度。
- **vs Llama 系列**：Meta 主导的开放权重模型，规模与 K3 不同量级，但许可证与生态更成熟。
- **vs Kimi K2**：同系列前作，K3 官方称有 2.5× scaling 效率提升（待验证）。

## 是否值得持续跟踪
**是，深度跟踪。** 首个开源 3T 级模型是结构性事件，但其真实能力需独立评测复现来确认。重点跟踪：独立 benchmark、实际推理成本、长上下文稳定性、社区基于权重的衍生工作（量化版/蒸馏版）。

## 后续观察点
1. 独立第三方评测（非 Moonshot 自报）结果，尤其 SWE/Coding/Agentic 基准。
2. 社区产出的量化/蒸馏版本能否把推理成本降到可用区间。
3. 1M 上下文在真实长文档任务中的稳定性与召回表现。

---
*首次记录：2026-07-30 · 数据来源：GitHub API + 仓库官方 README/技术报告*
