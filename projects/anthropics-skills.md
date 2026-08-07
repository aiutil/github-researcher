---
title: "anthropics/skills"
slug: "anthropics-skills"
date_added: "2026-05-29"
last_seen_date: "2026-08-07"
category: "平台候选"
emoji: "📚"
stars: "166,829 stars"
stars_delta: "forks 19,873，GitHub Star Top 10"
language: "Python"
license: "待核验（部分 Apache-2.0，文档技能 source-available）"
score: 85
tags: ["Claude", "Skills", "Anthropic", "标准化", "Agent", "agentskills.io"]
url: "https://github.com/anthropics/skills"
---

# anthropics/skills

## 一句话定位

Anthropic 官方 Agent Skills 公共仓库，包含 Skills 规范（spec）、技能模板（template）和示例技能集（创意设计、开发技术、企业通讯、文档技能），是 Claude/Claude Code/Claude.ai/API 的 Skills 标准来源。

## 它解决的问题

Agent Skills 生态碎片化：每个社区项目有自己的 Skills 格式和安装方式，缺少官方标准。anthropics/skills 提供了 Anthropic 官方的 Skills 规范（agentskills.io）、模板和示例，同时包含驱动 Claude 文档能力的 docx/pdf/pptx/xlsx 技能（source-available）。

## 为什么值得关注

1. **166,829 stars / 19,873 forks**，GitHub Star Top 10 级别
2. **Anthropic 官方出品**，定义了 Agent Skills 标准（agentskills.io spec）
3. 包含 4 大技能集：Creative & Design、Development & Technical、Enterprise & Communication、Document Skills
4. **文档技能（docx/pdf/pptx/xlsx）source-available**：这些技能驱动 Claude 的文档创建功能，展示了生产级 Skill 的复杂度
5. 可作为 Claude Code Plugin marketplace 安装：`/plugin marketplace add anthropics/skills`
6. 在 Claude.ai（付费版）、Claude API 中原生可用

## 热度来源判断

- **官方背书驱动。** Anthropic 官方仓库自带信任度，166K stars 是 Claude 生态规模的直接体现
- Agent Skills 标准化是确定性趋势 — Skills 成为 Agent 生态一等公民
- 与 anthropics/knowledge-work-plugins（23K）、anthropics/claude-plugins-official 形成完整生态

## 关键技术亮点

1. **Skills 规范（agentskills.io）**：定义 Skills 的标准格式（`SKILL.md` + YAML frontmatter）
2. **Claude Code Plugin marketplace 集成**：`/plugin marketplace add` + `/plugin install`
3. **Skills = 文件夹 + SKILL.md**：纯文件架构，无代码，Claude 动态加载
4. **文档技能 source-available**：docx/pdf/pptx/xlsx 技能展示生产级 Skill 设计模式
5. **Skills API**：通过 Claude API 上传和使用自定义 Skills

## 架构启发

**Skills 作为 Agent 生态的一等公民**：从附属功能到独立生态组件。Skills 的设计模式（文件夹 + SKILL.md + YAML frontmatter）简洁而强大 — 用文件系统组织 Agent 能力，类似 Unix 的"一切皆文件"哲学。标准化胜于碎片化：官方目录的价值在于统一入口和规范。

## 定位判断

**平台候选。** Skills 目录是 Agent 平台的核心组件。166K stars 说明生态规模巨大。

## 风险 / 局限 / 泡沫点

1. **文档技能是 source-available 非开源** — 商业限制
2. **仅服务于 Anthropic/Claude 生态**，通用性有限
3. **与 openai/skills、cursor/plugins 的标准竞争** — Skills 标准尚未统一
4. 示例 Skills 是"演示和教育用途"，实际效果可能与 Claude 中有所不同
5. 166K stars 中有 Anthropic 品牌效应的放大

## 与同类项目的关系

- **anthropics/knowledge-work-plugins**（23K stars）：面向知识工作者的官方插件
- **ECC**（238K stars）：第三方 Harness，使用 anthropics/skills 标准
- **wshobson/agents**（38K stars）：社区多 Harness 插件市场
- **mukul975/Anthropic-Cybersecurity-Skills**（27K stars）：安全领域社区 Skills
- **openai/skills / cursor/plugins**：竞争标准

## 是否值得持续跟踪

**是。** 官方 Skills 仓库的方向性意义大于内容本身 — 它定义了 Agent Skills 的标准。

## 后续观察点

1. Skills 数量和质量增长（特别是企业级技能）
2. agentskills.io 标准是否会成为跨平台 Skills 标准
3. 文档技能（docx/pdf/pptx/xlsx）的演进和开放程度
4. 与 Claude Code / Claude Cowork / Claude API 的集成深度
5. 社区贡献的 Skills 增长趋势
