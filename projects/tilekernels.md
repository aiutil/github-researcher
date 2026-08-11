---
title: "TileKernels"
slug: "tilekernels"
date_added: "2026-04-24"
last_seen_date: "2026-08-11"
category: "基础设施候选"
emoji: "⚡"
stars: "1,713 stars"
stars_delta: "4月1713，稳步增长"
language: "Python"
license: "MIT"
score: 80
tags: ["tilelang", "CUDA", "Inference", "DeepSeek", "GPU-Kernel", "MoE", "Quantization", "Engram"]
url: "https://github.com/deepseek-ai/TileKernels"
---

# deepseek-ai/TileKernels — 基于 tilelang 的高性能 GPU 推理内核库

## 一句话定位
DeepSeek-AI 出品的高性能 GPU 内核库，使用 tilelang DSL 编写，专为 LLM 训练和推理中的关键算子（MoE 路由、量化、注意力变体等）做接近硬件极限的优化，部分内核已在 DeepSeek 内部生产环境使用。

## 它解决的问题
大模型推理与训练的性能瓶颈正从模型架构层下沉到 GPU 内核层。FlashAttention 证明了专用内核的巨大价值，但针对 DeepSeek 新一代架构（MLA 注意力、MoE 专家路由、FP8/FP4 量化）仍缺乏高质量开源内核。传统 CUDA 手写门槛极高，可维护性差，迭代缓慢。TileKernels 用 tilelang DSL 重新定义内核开发范式：用更接近数学表达的 Python 级语法书写 GPU 计算模式，由编译器自动优化到接近手写 CUDA 的性能，同时保持敏捷开发能力。解决的核心问题是：**如何让前沿模型架构的专用算子以可维护、可迭代的方式达到硬件极限性能。**

## 为什么值得关注（2026-08-11）
- **Stars:** 1,713（从 4 月的 592 涨到 1,713，3 个月近 3 倍增长），质量型增长
- **Forks:** 155，内核工程师群体参与度较高
- **License:** MIT，商用友好
- **语言:** Python（tilelang DSL），非传统 C++/CUDA
- **活跃度:** created 2026-04-22，pushed 2026-04-23（初始发布密集，后续维护节奏较慢）
- **作者:** Xiangwen Wang、Chenhao Xu 等 DeepSeek 核心团队，与 tilelang 作者同属 tile-ai 组织
- **门槛:** 需 SM90（Hopper）或 SM100（Blackwell）GPU，CUDA 13.1+

## 热度来源判断
热度来自 **"DeepSeek 品牌效应 × tilelang 新范式 × 前沿算子稀缺性"** 三重叠加。DeepSeek 作为 2025-2026 年最受关注的中国开源 LLM 公司，其工程实践自带流量。tilelang 作为 GPU 编程的新抽象层（在 CUDA 之上、Triton 之侧），本身就有技术前瞻性。而 FP8/FP4 量化、MoE 路由等内核是当前推理优化的刚需且开源极少。关注者画像精准：GPU 内核工程师、推理框架开发者、AI Infra 团队——虽 star 数不高但质量极高，每一个 star 背后可能是能直接采用或贡献代码的专业用户。

## 关键技术亮点
1. **tilelang DSL 驱动:** 全部内核用 tilelang 编写，而非手写 CUDA/PTX。tilelang 提供 Python 级别的 tile 级编程抽象，编译器自动做调度优化、内存层级映射和向量化
2. **MoE 全套路由内核:** Top-k 专家选择与评分、Token-to-expert 映射、融合 expansion/reduction 与权重归一化——覆盖 MoE 模型推理最复杂的算子
3. **多精度量化:** 支持 per-token/per-block/per-channel 的 FP8/FP4/E5M6 转换，并融合 SwiGLU+量化操作减少访存
4. **Engram 门控内核:** 含融合 RMSNorm、前向/反向传播及权重梯度归约，对应 DeepSeek 的 Engram 机制
5. **Manifold HyperConnection:** 含 Sinkhorn 归一化和混合分裂/应用内核，面向 mHC 架构
6. **高层建模层:** 提供 `torch.autograd.Function` 封装，将底层内核组合成可训练的 PyTorch 层（engram gate、mHC pipeline）
7. **接近硬件极限:** README 明确指出"大部分内核接近计算强度和内存带宽的极限"

## 架构启发
TileKernels 代表了 GPU 内核开发的**DSL 化趋势**：从手写 CUDA → Triton → tilelang，抽象层逐步提升，让开发者聚焦算法定义而非微架构细节。更深层的是，它揭示了一个产业现实：**顶级 AI 公司的竞争力已不仅在于模型架构，更在于为自有架构定制的内核生态**。DeepSeek 开源这些内核，既是技术分享，也是在定义其架构的"事实标准"——当 MLA、MoE 的优化内核以 DeepSeek 的实现为参照系时，整个推理生态都会向其靠拢。tilelang 作为承载这些内核的 DSL，也在借势扩大自己的影响力，形成"模型架构→专用内核→编程 DSL"的闭环飞轮。

## 定位判断
**基础设施候选。** 推理内核是 LLM 推理栈最底层的基础设施。TileKernels 目前专注于 DeepSeek 系列架构的算子优化，若 tilelang 生态成熟，它有望从"DeepSeek 专用内核库"演化为"通用 GPU 内核开发平台"——类似 cuDNN 之于 NVIDIA 的定位，但以开源、DSL 驱动的方式。平台化潜力取决于 tilelang 能否吸引更多模型架构的贡献。

## 风险 / 局限 / 泡沫点
- **硬件门槛极高:** 仅支持 SM90/SM100（Hopper/Blackwell），大量 A100/4090 用户无法直接使用
- **维护节奏偏慢:** 初始发布后 push 活跃度下降，内核更新频率不确定
- **tilelang 依赖:** 与 tilelang 深度绑定，若 tilelang 生态未成气候，项目价值受限
- **文档与测试待完善:** README 自述"不代表最佳实践，正积极改进代码质量和文档"
- **受众极窄:** 受益者限于具备高端 GPU + 内核工程能力的团队
- **竞争激烈:** Triton（OpenAI）生态成熟，FlashAttention 3 已覆盖主流注意力，tilelang 需证明差异化优势

## 与同类项目的关系
- **vs FlashAttention 2/3:** FA 聚焦注意力；TileKernels 覆盖 MoE/量化/Engram/mHC 等更广算子，且用 DSL 而非 C++/CUDA
- **vs Triton (OpenAI):** 都是 GPU 编程抽象，Triton 更成熟（被 vLLM 等广泛采用），tilelang 更新但专注于 tile 级表达力
- **vs FlashKDA (Moonshot):** 同为国产 AI 公司的推理内核，FlashKDA 聚焦 Delta Attention
- **vs cuDNN/cuBLAS:** NVIDIA 官方闭源库覆盖通用算子，TileKernels 补充前沿架构专用算子
- **vs DeepGEMM:** 同为 DeepSeek 开源的高性能库，GEMM 聚焦矩阵乘法，TileKernels 聚焦更广算子

## 是否值得持续跟踪
**是，高优先级。** DeepSeek 的内核工程能力是其核心壁垒，TileKernels 直接展示了其最前沿的算子优化实践。对 AI Infra 团队，这是研究 FP8/FP4 量化内核、MoE 路由优化的稀有开源参考。对推理框架开发者，关注哪些算子被纳入、性能数据如何，有助于提前布局适配。对 GPU 编程语言研究者，tilelang 的 DSL 设计理念值得学习。

## 后续观察点
1. tilelang 社区是否独立发展壮大，吸引非 DeepSeek 架构的贡献
2. 是否发布与 Triton/FlashAttention 的性能基准对比数据
3. 是否被 vLLM、SGLang 等主流推理框架集成
4. 硬件支持是否扩展到 SM89/SM80（Ada/Ampere）以降低采用门槛
5. DeepSeek 下一代模型架构（如传闻中的 V4）是否会同步更新内核

---
> 数据来源: GitHub API (2026-08-11) | Stars: 1,713 | Forks: 155 | License: MIT | 语言: Python | 创建: 2026-04-22
