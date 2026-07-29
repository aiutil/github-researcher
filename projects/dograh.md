---
title: "Dograh"
slug: "dograh"
date_added: "2026-06-02"
last_seen_date: "2026-06-02"
category: "Voice AI"
emoji: "🎙️"
stars: "4.1K"
score: 80
tags: ["voice-ai", "self-hosted", "speech-to-speech", "telephony", "mcp"]
url: "https://github.com/dograh-hq/dograh"
---

# Dograh — 开源语音 AI 平台

## 一句话定位

开源语音 AI 平台，Vapi/Retell 的自托管替代，支持 STT/TTS/LLM 工作流可视化构建器，MCP 原生，电话集成。

## 解决的问题

语音 AI 部署目前依赖 Vapi/Retell 等闭源 SaaS，数据隐私、成本、定制能力都受限。企业需要自托管方案。

## 为什么值得关注

1. 定位精准：Vapi/Retell 的直接开源替代
2. 可视化工作流构建器降低使用门槛
3. MCP 原生 — 与 Agent 生态集成
4. 支持电话集成，企业场景刚需

## 热度来源判断

- 4.1K stars，周增量 +1.3K，增长健康
- 语音 AI 赛道热度 + 自托管需求
- BYOK（Bring Your Own Key）模式吸引企业用户

## 关键技术亮点

1. **可视化工作流构建器**：拖拽式构建语音 AI 流程
2. **MCP 原生**：与 AI Agent 生态无缝集成
3. **多协议支持**：Speech-to-Speech 或 LLM/STT/TTS 组合
4. **电话集成**：真实业务场景（客服、外呼）
5. **BYOK**：自带模型 API Key，成本可控

## 架构启发

语音 AI 平台的典型架构：
```
用户语音 → STT → LLM → TTS → 语音输出
              ↓
          工作流引擎
              ↓
          MCP Tools
```

Dograh 把这条链路产品化了，加上可视化编辑和电话集成。

## 定位判断

**工具型 → 平台候选。** 如果能建立语音 AI 开源生态，有平台化潜力。

## 风险/局限/泡沫点

- Vapi/Retell 功能更成熟，Dograh 需要快速追赶
- 语音质量依赖底层 STT/TTS 模型
- 电话集成需要运营商合作，门槛不低
- 4K stars 规模还小，需要验证可持续性

## 与同类项目的关系

- 直接对标 Vapi/Retell（闭源 SaaS）
- 与 VoxCPM 互补：VoxCPM 提供模型，Dograh 提供平台
- 与 FunASR 不同层：FunASR 是 ASR 引擎，Dograh 是完整平台

## 是否值得持续跟踪

**是。** 企业语音 AI 部署的刚需，自托管趋势明确。

## 后续观察点

1. 工作流构建器的易用性和灵活性
2. 电话集成的稳定性和覆盖范围
3. 社区和企业用户增长
4. 与其他语音模型（VoxCPM、MOSS-TTS）的集成深度
