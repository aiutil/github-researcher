---
title: "HRM-Text"
slug: "hrm-text"
date_added: "2026-05-23"
category: "学习型"
emoji: "🧪"
stars: "650 stars"
stars_delta: "650/5天（创建于 2026-05-18）"
language: "Python"
score: 80
tags: ["HRM", "预训练", "小模型", "PyTorch", "FSDP2", "FlashAttention"]
url: "https://github.com/sapientinc/HRM-Text"
last_seen_date: "2026-05-28"
---

# HRM-Text

## 一句话定位
基于 HRM（层级循环模型）架构的 1B 文本生成模型，展示如何用 $1000 从头预训练基础模型。

## 它解决的问题
目标用户：AI 研究者、想要预训练自有模型的团队。

痛点：
- 传统预训练需要数千张 GPU，成本数百万美元
- 中小团队无法承担基础模型预训练的成本
- 现有开源模型的架构创新主要来自大厂

## 为什么值得关注（2026-05-23）
HRM-Text 用层级循环架构（非 Transformer）展示了 130-600x 更少算力、150-900x 更少数据即可预训练基础模型。1B 模型在 GSM8k 上达到 84.7%，这挑战了「只有 Transformer + 大规模数据才能训练好模型」的假设。

## 热度来源判断
650 stars / 5 天。热度来自：
- **$1000 预训练**的惊人声称
- HRM（Hierarchical Recurrent Model）是非常规架构，引发讨论
- 有完整的预训练框架和复现指南

热度合理 — 这是一个学术性项目，受众是研究者和深度技术用户。

## 关键技术亮点

### 1. 层级循环架构（HRM）
非 Transformer 架构，用层级循环替代 self-attention。理论上更高效，因为循环计算的复杂度是 O(n) 而非 O(n²)。

### 2. PrefixLM sequence packing
高效序列打包策略，提升训练利用率。

### 3. FlashAttention 3 + PyTorch FSDP2
使用最新的 FlashAttention 3 内核和 FSDP2 分布式训练框架。

### 4. 完整预训练框架
不只是模型权重，而是完整的预训练工具链：数据准备（data_io）→ tokenization → stratified sampling → 预训练 → 评估 → checkpoint 转换。

## 架构启发
HRM 架构挑战了 Transformer 在语言模型中的统治地位。如果层级循环架构被证明在小规模上优于 Transformer，可能催生新的模型设计方向。

关键问题：这种优势是否能在更大规模（10B+）上保持？

## 定位判断
**学习型。** 主要是学术研究和技术演示。短期内不会成为生产可用模型，但其架构思路值得关注。

## 风险 / 局限 / 泡沫点

1. **$1000 预训练的前提是 8-16 张 H100**：对大多数组织仍不现实
2. **1B 规模的参考价值有限**：从 1B 到 10B+ 的扩展性未验证
3. **HRM 架构未经大规模验证**：可能在更大规模时遇到 Transformer 没有的问题
4. **与 Transformer 生态不兼容**：现有工具链（vLLM、TensorRT-LLM 等）不支持 HRM

## 与同类项目的关系
| 项目 | 架构 | 规模 | 预训练成本 |
|------|------|------|-----------|
| Llama 4 | Transformer | 8B-405B | 数千万美元 |
| RWKV | 线性 RNN | 1.5B-14B | 低 |
| HRM-Text | 层级循环 | 0.6B-1B | ~$1000 |

## 是否值得持续跟踪
**中性。** 作为学术项目值得关注其后续发展，但短期内不会影响企业技术决策。如果 HRM 架构在更大规模上验证成功，则需要重新评估。

## 后续观察点
1. HRM 架构在更大规模（10B+）上的表现
2. 学术社区对 HRM 架构的反馈和复现结果
3. 是否有团队基于 HRM 训练生产级模型

---
*首次记录：2026-05-23*
