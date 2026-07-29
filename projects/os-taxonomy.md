---
title: "Marble Skill Taxonomy"
slug: "os-taxonomy"
date_added: "2026-07-11"
category: "观察型"
emoji: "📚"
stars: "2,071 stars"
stars_delta: "3天2.1K，日均~690"
language: "JavaScript"
score: 78
tags: ["education", "knowledge-graph", "curriculum", "open-data", "dag"]
url: "https://github.com/withmarbleapp/os-taxonomy"
---

# Marble Skill Taxonomy (os-taxonomy)

## 一句话定位
开源结构化课程知识图谱——1590 个微主题、3221 条前置依赖边、8 个学科，对齐 NGSS / Common Core / UK National Curriculum 等国家标准。

## 它解决的问题
教育科技领域最缺的基础设施：结构化的、有前置依赖关系的课程数据。现有课程标准要么是扁平的条目列表（Common Core），要么锁在商业产品内部。教育 AI 应用（个性化学习、自适应课程、AI 辅导）没有可编程的知识地图就无法精准推荐。

## 为什么值得关注（2026-07-11
3 天 2K+ star，不是 AI 项目，但为 AI 教育提供了结构化数据基座。每个微主题有：
- 描述（plain-language）
- 掌握证据标准（mastery evidence）
- 评估提示（assessment prompt，带 `{{name}}` 占位符）
- 类型分类（概念/程序/表征/语言/元认知）
- 学科+领域+年龄范围
- 中心性分数（centrality，图论指标）
- 对齐的课程标准引用

这是教育领域的"知识图谱即基础设施"。

## 热度来源判断
- **README 3D 可视化动图**——旋转的知识图谱极其直观，传播力强
- **数据质量极高**——不是粗糙爬虫数据，是精心设计的结构化数据
- **教育社区真实需求**——Homeschooling、个性化学习、AI tutoring 都是增长场景
- **Marble 商业背景**——教育科技公司开放核心数据，表明其壁垒在产品体验而非数据锁
- 真实需求，非 AI 炒作泡沫

## 关键技术亮点
1. **DAG 前置依赖图**：3221 条有向边，区分 hard/soft 依赖，每条边有一行理由
2. **多标准对齐**：NGSS（美国科学）、Common Core（美国数学+英语）、UK NC（英国国家课程），用 `curriculum-slug:code` 格式交叉引用
3. **微主题粒度**：1590 个节点不是"章节"级别，而是"一个可教学概念"级别
4. **JSON Schema 约束**：有正式的 schema/ 目录和 manifest.json（含 SHA-256 校验）
5. **Domain Clusters**：183 个按（学科、领域、年龄段）聚合的家长友好摘要

## 架构启发
- **知识图谱+前置依赖 DAG 是跨领域的基础设施模式**——课程、技能树、依赖管理、合规检查、DevOps 流水线
- **开放核心数据+增值服务的商业模式**——Marble 开放了数据，商业价值在交互体验和个性化推荐引擎
- **微主题粒度在大语言模型时代有了新消费场景**——AI 辅导可以精确诊断"学生卡在哪个前置概念"

## 定位判断
**观察型。** 数据质量极高，但由单一公司维护，版本治理和社区参与模式不明。如果 Marble 能够建立类似 OpenAPI Specification 的社区治理模式，有潜力成为教育领域的知识图谱标准。

## 风险 / 局限 / 泡沫点
1. **单一公司维护**——Marble 停止维护则数据过时
2. **版本治理不明**——v1 后如何迭代、如何接受社区贡献不清晰
3. **教育市场变现路径不确定**——免费数据如何支撑公司运营
4. **覆盖范围有限**——目前仅覆盖小学/初级教育，高中+大学空白
5. **文化适配**——以英语国家课程标准为主，其他地区适配成本高

## 与同类项目的关系
| 项目 | 数据结构 | 开放程度 | 维护状态 |
|------|---------|---------|---------|
| **os-taxonomy** | DAG 前置依赖图 | 完全开放 JSON | 活跃（v1） |
| Common Core Standards | 扁平条目列表 | 公共领域 | 静态 |
| Khan Academy Knowledge Map | 依赖图（内部） | 封闭 | 活跃 |
| OpenStax | 教材级内容 | CC BY | 活跃 |

os-taxonomy 是唯一开放的、有前置依赖 DAG 的、多标准对齐的课程知识图谱。

## 是否值得持续跟踪
**是。** 如果 AI 教育起飞，这类结构化数据是刚需。关键观察点：是否有 AI 教育产品基于此数据构建、是否有社区贡献扩展到更多地区和学段。

## 后续观察点
- 是否有 AI tutoring 产品基于 os-taxonomy 数据构建
- 社区是否贡献更多地区课程标准对齐
- Marble 公司是否建立数据治理社区
- 是否出现高等教育版或职业教育的同类项目
