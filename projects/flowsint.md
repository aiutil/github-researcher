---
title: "Flowsint"
slug: "flowsint"
date_added: "2026-06-03"
category: "工具型"
emoji: "🕸️"
stars: "4.5K stars"
stars_delta: "+190/day, +1.5K/week, TypeScript + Python"
language: "TypeScript"
score: 75
tags: ["osint", "graph", "cybersecurity", "investigation", "enricher"]
url: "https://github.com/reconurge/flowsint"
last_seen_date: "2026-06-03"
---

# Flowsint

## 一句话定位
开源 OSINT 图谱调查平台——可视化实体关系探索，支持域名/IP/社交/加密货币等多维度自动关联，Docker 一键部署。

## 它解决的问题
网络安全分析师和调查人员需要跨多个数据源（DNS/IP/WHOIS/社交/加密货币）进行关联分析。现有工具要么分散，要么昂贵。Flowsint 将所有数据源统一到可视化图谱中。

## 为什么值得关注（2026-06-03）
- **+190 stars/day**，GitHub Trending TypeScript 前列
- 图谱化 OSINT 调查是网络安全领域的刚需
- 模块化设计（Core/Types/Enrichers/API/App）架构清晰
- 完全本地部署，数据不出机器，隐私友好

## 热度来源判断
- 网络安全 + OSINT 垂直领域，用户群体明确
- Docker 一键部署降低使用门槛
- 4.5K stars 对安全工具来说已经很高

## 关键技术亮点
1. **丰富器（Enricher）架构**：每种数据源一个 Enricher，模块化可扩展
2. **图谱可视化**：千级节点无卡顿
3. **多维度关联**：域名→IP→ASN→CIDR→组织 的自动链条
4. **N8n 集成**：可接入自动化工作流

## 架构启发
- Enricher 模式可以推广到其他需要多源数据关联的场景（如供应链风险分析）
- 图谱 + 自动关联的交互模式比传统表格更适合探索性调查

## 定位判断
**工具型。** 面向安全分析师的专业工具，非通用基础设施。

## 风险/局限/泡沫点
1. 早期开发阶段，测试覆盖不完整
2. 社区贡献者较少，可持续性待验证
3. Enricher 质量参差不齐（部分依赖外部 API）
4. 非架构师日常关注范畴，偏安全专业领域

## 与同类项目的关系
- **Maltego**：商业 OSINT 平台，Flowsint 是开源替代
- **Shrek/Sherlock**：单项工具，Flowsint 做平台化整合

## 是否值得持续跟踪
**观察。** 安全垂直领域工具，非核心关注方向，但 Enricher 架构模式值得借鉴。

## 后续观察点
1. Enricher 生态的丰富度和质量
2. 社区活跃度和贡献者增长
3. 是否有企业级使用案例

---

*档案创建于 2026-06-03 · 数据截止 2026-06-03 06:00 CST*
