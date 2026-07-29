---
title: "agent-governance-toolkit"
slug: "agent-governance-toolkit"
date_added: "2026-05-29"
category: "基础设施候选"
emoji: "🛡️"
stars: "3.6K stars"
stars_delta: "+1.5K/week，覆盖 OWASP Agentic Top 10，Public Preview"
language: "Python"
score: 86
tags: ["Agent治理", "安全", "OWASP", "Microsoft", "合规"]
url: "https://github.com/microsoft/agent-governance-toolkit"
last_seen_date: "2026-06-02"
---

# Microsoft Agent Governance Toolkit

## 一句话定位
Microsoft 出品的 AI Agent 安全治理工具包，提供策略执行、零信任身份、执行沙箱和可靠性工程，覆盖 OWASP Agentic Top 10 全部 10 项。

## 它解决的问题
Agent 部署到生产环境后，面临三个核心安全问题：
1. **动作授权**：Agent 有 send_email 和 query_database 权限，不应该能 drop_table
2. **身份追溯**：5 个 Agent 共享一个 API key 时，出问题无法定位
3. **审计追踪**：审计需要防篡改的决策记录

Prompt 级安全无法解决这些问题（OWASP LLM01:2025 明确指出），需要确定性的代码拦截。

## 为什么值得关注（2026-05-29）
1. Microsoft 出品，工程质量和长期维护有保障
2. 覆盖 OWASP Agentic Top 10 全部 10 项，是业界最全面的安全覆盖
3. 确定性拦截（非 prompt 级），被拒绝的操作「结构上不可能执行」
4. 三平台 SDK（Python / npm / NuGet）

## 热度来源判断
- **真实需求。** 企业 Agent 部署的安全合规是刚性需求
- Microsoft 背书，OpenSSF Scorecard + OpenSSF Best Practices 认证
- 3.2K 但周增速 1.3K，成长性高

## 关键技术亮点
1. **确定性拦截**：在工具调用前用代码拦截，不依赖 prompt 安全
2. **OWASP Agentic Top 10 全覆盖**：业界唯一声称覆盖 10/10 的工具包
3. **多框架兼容**：Claude Code Plugin + 通用 Python SDK
4. **审计日志**：防篡改的决策记录，满足合规要求

## 架构启发
- **安全不是功能，是架构**：Agent 安全需要在架构层面设计，而不是事后加 prompt 规则
- **确定性 > 概率性**：对于安全场景，确定性拦截远优于概率性 prompt 防御
- **治理即基础设施**：Agent 治理应该像 IAM 一样成为基础设施层

## 定位判断
- **基础设施候选**
- 企业 Agent 落地的必经之路
- 可能成为 Agent 安全的行业标准

## 风险/局限/泡沫点
1. Public Preview 阶段，可能有 breaking changes
2. 目前主要是 Python，其他语言支持待完善
3. 3.2K 规模较小，社区生态尚未建立
4. 依赖 Microsoft 的长期投入

## 与同类项目的关系
- **vs prompt 级安全（Claude Guardrails）**：AGT 是确定性拦截，不是 prompt 规则
- **vs Agent 沙箱（E2B）**：E2B 是运行时隔离，AGT 是策略治理
- **vs OWASP LLM Top 10 指南**：AGT 是实现，不是指南

## 是否值得持续跟踪
**强烈建议。** 企业 Agent 安全是刚需，Microsoft 出品增加了标准化的可能性。

## 后续观察点
1. GA 时间线和稳定性
2. 是否被 Claude Code / Codex 等主流 Agent 官方集成
3. 企业实际部署案例
4. 与其他安全工具（如 OPA、SPIFFE）的集成
