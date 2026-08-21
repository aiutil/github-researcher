---
title: "HTML PPT Skill"
slug: "html-ppt-skill"
date_added: "2026-04-20"
category: "工具型"
emoji: "📊"
stars: "1396 stars"
stars_delta: "5天 1396⭐，增速 ~279⭐/天"
language: "HTML"
score: 65
tags: ["ppt", "html", "skill", "presentation", "agent"]
url: "https://github.com/lewislulu/html-ppt-skill"
---

# HTML PPT Skill

## 一句话定位
AgentSkill 实现，提供 24 主题、31 布局、20+ 动画的 HTML 演示文稿生成能力。

## 它解决的问题
用 AI agent 生成演示文稿是高频需求，但现有方案（PPT、Google Slides API）要么格式受限，要么需要复杂依赖。HTML PPT Skill 提供纯 HTML/CSS/JS 方案，agent 一键生成可播放的演示文稿。

目标用户：需要快速生成演示文稿的开发者和 AI agent 用户。

## 为什么值得关注（2026-04-20）
- Agent Skill 生态中"生产力工具"品类的代表
- 1396 star 增速不错，说明社区对 agent 生成 PPT 有真实需求
- 纯 HTML 实现，零依赖

## 热度来源判断
40% 真实需求 + 40% Agent Skill 热潮推动 + 20% star 刷量可能。PPT 生成是刚需，但技术门槛不高。

## 关键技术亮点亮点
1. 24 主题 31 布局的模板系统
2. 20+ CSS 动画效果
3. 纯 HTML/CSS/JS 实现，无外部依赖
4. 作为 AgentSkill 可被 Claude Code 等直接调用

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 本项目即一整套 Agent Skill 资产，由 SKILL.md + 模板目录组成，被 Claude Code 等 agent 调用，外部仅依赖运行环境与用户 | 仅基于档案"AgentSkill 实现 / SKILL.md + 模板目录 / 可被 Claude Code 等直接调用"得出，未核验 SKILL.md 实际内容、模板目录结构、Claude Code 协议细节 |
| 主路径 | agent 接收生成请求 → 加载 Skill 的 SKILL.md 与模板 → 选择主题/布局/动画 → 产出单文件 HTML → 用户在浏览器播放 | 档案明确给出"24 主题、31 布局、20+ 动画、纯 HTML/CSS/JS、零依赖、agent 一键生成可播放的演示文稿"；未给出生成时序、模板选择算法、是否支持增量编辑 |
| 关键权衡 | 零依赖/单文件可分发 ↔ 演示表现力与排版精度低于 Keynote/PPT；社区热度增长 ↔ 同质化与 star 泡沫风险 | 档案明确"零依赖""演示效果难以匹敌专业工具""star 刷量可能""同质化风险"；未量化演示质量差距、未给出 star 真实度判定依据 |
| 最小 PoC | 选用一个 agent（Claude Code）调用该 Skill，输入固定主题生成 5 页 PPT，验证输出 HTML 在浏览器可播放、主题/布局/动画生效、无外部网络请求 | 档案给出"HTML/CSS/JS 零依赖"可推断无网络请求，但具体主题清单、动画名册、浏览器兼容范围未在档案中列出，需源码核验 |

## 架构启发
- **Skill 作为轻量能力扩展**：不需要复杂框架，一个 SKILL.md + 模板目录就是完整的 agent 能力包
- 技术门槛不高但实用性强的 Skill 更容易获得关注

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    A[Agent 调用方 e.g. Claude Code] --> B[Skill 入口: SKILL.md]
    B --> C[模板与资源目录 24主题 31布局 20+动画]
    C --> D[生成的 单文件 HTML 演示文稿]
    D --> E[浏览器 播放]
    A --> F[用户输入 主题与内容]
    F --> D
    D --> G[待核验 增量编辑/二次生成流程]
    B --> H[外部边界 零运行时依赖 仅依赖 agent 宿主]
</mermaid>
```

## 定位判断
典型的**工具型 Agent Skill**，解决具体问题但不构成平台或基础设施。

## 风险 / 局限 / 泡沫点
1. **同质化风险**：HTML 演示方案技术门槛低，竞品容易涌现
2. **演示质量**：HTML 方案的演示效果难以匹敌专业工具（Keynote、PPT）
3. **泡沫点**：star 数可能含 Agent Skill 热潮的泡沫成分

## 与同类项目的关系
- **Marp**：Markdown → PPT，更成熟但不是 Agent Skill
- **Slidev**（Anthony Fu）：开发者演示工具，更偏手动编写
- **Reveal.js**：HTML 演示框架，更底层

## 是否值得持续跟踪
**短期关注即可**。技术门槛不高，重点看是否有持续迭代和差异化。

## 后续观察点
1. 是否出现商业化的 HTML 演示 agent 服务
2. 模板和动画是否有社区贡献增长

---
*首次记录：2026-04-20*
