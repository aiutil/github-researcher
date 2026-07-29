---
title: "TileKernels"
slug: "tilekernels"
date_added: "2026-04-24"
last_seen_date: "2026-05-01"
category: "基础设施候选"
emoji: "⚡"
stars: "1.4k stars"
score: 80
tags: ["tilelang", "CUDA", "Inference", "DeepSeek", "GPU-Kernel", "MoE", "Quantization", "Engram"]
url: "https://github.com/deepseek-ai/TileKernels"
---

# TileKernels

## 一句话定位
DeepSeek 出品的基于 tilelang 的高性能 GPU 推理内核库。

## 解决的问题
大模型推理性能瓶颈越来越依赖底层 GPU 内核优化，而非仅靠模型架构改进。FlashAttention 证明了专用内核的价值，但针对新兴模型架构（如 DeepSeek 的 MLA、MoE）仍缺乏高质量开源内核。

## 为什么值得关注
1. DeepSeek 是当前最活跃的开源 LLM 公司之一，其内核工程能力直接决定推理成本
2. tilelang 作为 GPU 编程 DSL，可能是 CUDA 之上的下一代抽象
3. 开源内核库有助于降低社区复现和优化门槛

## 热度来源判断
- DeepSeek 品牌效应：deepseek-ai 组织的直接背书
- 技术前沿性：tilelang 是较新的 GPU 编程抽象
- Star 数偏低但增长质量高，关注者是内核/系统工程师

## 关键技术亮点
- 基于 tilelang DSL 编写，比直接写 CUDA 更高层的抽象
- 专注于推理阶段的算子优化
- DeepSeek 模型推理的核心工程组件

## 架构启发
模型推理优化的主战场正在从模型架构下沉到 GPU 内核级别。tilelang 代表了一种趋势：用 DSL 而非手写 CUDA 来表达 GPU 计算模式。

## 定位判断
**基础设施候选。** 推理内核是 LLM 推理栈的最底层，具有平台化潜力。

## 风险/局限/泡沫点
- tilelang 生态尚小，社区采用率不确定
- 目前 star 数不高（592），仍处于早期
- 与 FlashAttention / Triton 等成熟方案的竞争关系不明

## 与同类项目的关系
- FlashKDA (Moonshot)：同为国产 AI 公司的推理内核，但 FlashKDA 聚焦 Delta Attention
- FlashAttention：注意力优化的先驱，TileKernels 可视为其在更广算子范围的延续
- Triton (OpenAI)：另一 GPU 编程抽象，tilelang 的直接竞争者

## 是否值得持续跟踪
**是。** DeepSeek 的内核工程能力是其核心壁垒之一，TileKernels 的演进值得关注。

## 后续观察点
1. tilelang 社区是否独立发展
2. 是否支持更多模型架构（不仅是 DeepSeek 系列）
3. 与 Triton 的性能对比数据
4. 是否被其他推理框架集成

## 评分

| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 5 | Star 数不高但来源质量高 |
| 技术创新度 | 8 | tilelang 是较新的 GPU 编程范式 |
| 工程成熟度 | 6 | 早期阶段，文档和测试待完善 |
| 架构启发价值 | 8 | GPU 内核 DSL 化趋势明确 |
| 企业落地潜力 | 6 | 需要深度 GPU 工程能力才能使用 |
| 中期趋势概率 | 7 | 推理优化是确定性趋势 |
| 平台化潜力 | 7 | tilelang 可发展为通用 GPU 编程框架 |
| 基础设施潜力 | 8 | 推理内核是 LLM 栈最底层 |

**总分：55/80**
**归类：基础设施候选**
**建议持续跟踪：是**
