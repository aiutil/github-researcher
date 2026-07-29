---
title: "9arm-skills"
slug: "9arm-skills"
date_added: "2026-05-23"
category: "工具型"
emoji: "🦑"
stars: "1,487 stars"
stars_delta: "1.5K/3天（创建于 2026-05-20）"
language: "Shell"
score: 72
tags: ["Claude Code", "Skills", "Agent技能", "SKILL.md"]
url: "https://github.com/thananon/9arm-skills"
last_seen_date: "2026-05-23"
---

# 9arm-skills

## 一句话定位
Claude Code 技能集合，包含工程/生产力/调试/审查等分类技能，标准 SKILL.md 结构。

## 它解决的问题
目标用户：使用 Claude Code 的开发者。

痛点：
- Claude Code 的技能系统需要手动编写 SKILL.md
- 缺少经过实践验证的技能模板

## 为什么值得关注（2026-05-23）
代表 Claude Skills 生态的持续细分。虽然项目本身是个人技能集合，但其结构和分类方式为社区提供了参考。

## 热度来源判断
1.5K stars / 3 天。热度来自 Claude Skills 生态的整体热度。属于「蹭生态热度」型项目，但内容有一定价值。

## 关键技术亮点

### 1. 标准化技能结构
每个技能有独立的 SKILL.md（含 YAML frontmatter：name、description）和配套脚本。

### 2. 分类体系
工程（debug-mantra、post-mortem、scrutinize）/ 生产力（management-talk）/ 个人 / 进行中 / 废弃 — 清晰的分类管理。

### 3. 自动化链接脚本
link-skills.sh 将所有可发布的技能自动链接到 ~/.claude/skills/。

## 架构启发
展示了 Claude Code Skills 的标准组织方式，可以作为企业内部技能管理的参考。

## 定位判断
**学习型 / 工具型。** 个人技能集合，质量参差不齐。主要价值是提供技能组织结构的参考。

## 风险 / 局限 / 泡沫点

1. **个人项目**：技能内容与作者个人工作流强绑定
2. **技能数量有限**：目前只有少量技能
3. **热度主要来自 Claude 生态蹭流量**

## 与同类项目的关系
| 项目 | 定位 | 规模 |
|------|------|------|
| Superpowers | 技能框架 + 方法论 | 201K⭐ |
| ECC | Agent Harness + 技能 | 188K⭐ |
| 9arm-skills | 个人技能集合 | 1.5K⭐ |

## 是否值得持续跟踪
**否。** 项目规模小，内容有限。除非作者持续产出高质量技能。

## 后续观察点
1. 技能数量和质量的增长
2. 是否被 Claude Plugins Official 等标准化入口收录

---
*首次记录：2026-05-23*
