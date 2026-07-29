---
title: "WhichLLM"
slug: "whichllm"
date_added: "2026-06-10"
category: "工具型"
emoji: "🎯"
stars: "4,747 stars"
stars_delta: "周增 1,794"
language: "Python"
score: 80
tags: ["local-llm", "benchmark", "hardware", "model-selection", "gguf"]
url: "https://github.com/Andyyyy64/whichllm"
last_seen_date: "2026-06-15"
---

# WhichLLM

## 一句话定位
证据驱动的本地 LLM 硬件匹配工具 — 一条命令找到最适合你硬件的模型，基于真实基准测试而非参数量。

## 它解决的问题
本地 LLM 数量爆发后，用户面临"哪个模型能在我的硬件上跑且效果最好"的选择困难。现有工具（如 ollama list）只告诉你哪些模型能装下，不告诉你哪个效果最好。whichllm 解决的是"硬件适配 + 质量排名"的交叉问题。

目标用户：想跑本地 LLM 但不确定选哪个模型的开发者、考虑买 GPU 跑模型的用户。

## 为什么值得关注（2026-06-10）
今日日增 631 stars。本地 LLM 生态正在从"能跑就行"进入"选最好的跑"阶段。whichllm 的证据驱动 + 时效性感知方法代表了模型选型工具的进化方向。

## 热度来源判断
真实需求驱动。本地 LLM 用户快速增长，但模型选型信息严重不对称。whichllm 的 `--gpu` 模拟功能对买卡决策有直接价值。

## 关键技术亮点
1. **多源基准融合**：LiveBench + Artificial Analysis + Aider + Chatbot Arena ELO + Open LLM Leaderboard
2. **时效性感知**：过时基准分数自动降权，按模型 lineage 跟踪
3. **证据分级**：每个分数标记 direct / variant / base / interpolated / self-reported，伪造分数被主动拒绝
4. **架构感知 VRAM 估算**：权重 + GQA KV Cache + 激活 + 开销，MoE 模型区分 active/total 参数
5. **GPU 模拟**：`whichllm --gpu "RTX 4090"` 买卡前先测试
6. **一条命令**：`uvx whichllm@latest` 无需安装

## 架构启发
whichllm 的"证据分级"机制值得借鉴 — 在 AI 工具生态中，很多数据来源不可靠，需要一套置信度评估体系。这种"不信任数据，但利用数据"的工程哲学适用于更广泛的场景。

## 定位判断
本地 LLM 工具链的"入口级"工具 — 用户决策链的起点。与 ollama（运行时）、llama.cpp（推理引擎）互补而非竞争。

## 风险 / 局限 / 泡沫点
1. **基准测试偏差**：所有基准都有偏差，多源融合不能完全消除
2. **HuggingFace API 依赖**：实时数据依赖 HF API，离线模式使用缓存的冻结数据
3. **功能边界有限**：不做推理、不做服务，只是选型工具
4. **竞争壁垒低**：核心逻辑可被 ollama / lm-studio 等平台内建替代

## 与同类项目的关系
- **ollama**：模型运行时，有 list/show 但无智能排名
- **lm-studio**：GUI 工具，有硬件检测但无基准排名
- **Artificial Analysis**：在线排行榜，无硬件匹配能力

## 是否值得持续跟踪
中等优先级。工具本身实用但壁垒不高，关键是观察它是否被更大平台内建或收购。

## 后续观察点
1. 是否被 ollama / llama.cpp 等平台内建为推荐引擎
2. 基准测试数据源的扩展和更新频率
3. 多模态模型（视觉、音频）的支持进度

---
*首次记录：2026-06-10*
