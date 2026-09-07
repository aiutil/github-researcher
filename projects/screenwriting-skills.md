---
title: "jtydhr88/screenwriting-skills"
slug: screenwriting-skills
date_added: 2026-09-08
last_seen_date: 2026-09-08
category: "工具型"
emoji: "🎬"
stars: "301 stars"
stars_delta: "2 天 0→301⭐，单日均速 ~150⭐/day；12 项 Claude Code 编剧 Skill 蒸馏 19 本书 + 契诃夫 + 小津安二郎"
language: "Markdown"
score: 86
tags: ["agent-skill", "claude-code", "claude-skills", "creative-writing", "jtydhr88", "screenwriting", "storytelling"]
url: "https://github.com/jtydhr88/screenwriting-skills"
---

# jtydhr88/screenwriting-skills

## 一句话定位
12 项 Claude Code 编剧与剧作 Skill——蒸馏 19 本书（中美日）+ 契诃夫剧本全集 + 小津安二郎电影剧本全集；中英双语（Skill 主体中文 / frontmatter 英文 + 中文关键词），2 天 301⭐，fork 40（fork/star 13.3%），Markdown。

## 它解决的问题
2026 年 Coding Agent 在垂直领域（编剧 / 法律 / 设计 / 医生）的应用面临三大痛点：(a) **原始材料覆盖度**——LLM 通用知识无法替代专业领域专家的方法论蒸馏；(b) **Skill 碎片化**——每个编剧技巧需要单独 prompt，缺乏体系；(c) **多语言 Skill 的工程化**——双语 Skill 的内容一致性维护。`screenwriting-skills` 直击这三点：(a) 蒸馏 **19 本书**（Field / Snyder / McKee / Hoxter / Hicks / Lu Jun / Egri / Indick）+ **契诃夫剧本全集** + **小津安二郎电影剧本全集**；(b) 12 项 Skill 覆盖编剧全流程；(c) Skill 主体中文 + frontmatter 英文 + 中文关键词触发。

## 为什么值得关注
- **Stars:** 301（截至 2026-09-08），2 天净增，单日均速 ~150⭐/day
- **Forks:** 40（fork/star **13.3%**，显著高于 magnitude 7.2% / fastpotify 4.4%）
- **语言:** Markdown 主导（Skill 内容是结构化文档）
- **项目年龄:** 2 天（创建 2026-09-06）
- **核心差异:** 垂直领域 Skill 套装（12 项 vs 单 Skill）+ 19 本书 + 契诃夫 + 小津安二郎全集 + 中英双语

## 热度来源判断
`screenwriting-skills` 的热度来自三个趋势的交汇：(1) **垂直领域 Skill 套装化**——继 9-06 `mattpocock/skills`（252K⭐ 通用 Skills）之后，screenwriting-skills 把 Skill 模式推到"垂直领域深度蒸馏"；(2) **Claude Code 协议成熟**——`/plugin marketplace add` + `/plugin install` 标准化 Skill 分发；(3) **中英双语 Skill 工程化**——Skill 内容主体中文（来源与引文都是中译），frontmatter 英文 + 中文关键词触发——双语 Skill 是中国开发者的工程化路径。

2 天 301⭐ / fork 40（fork/star 13.3%）的组合反映 **"真实编剧采用 + 中英双语 + 原始材料覆盖度"** 三者叠加。

## 关键技术亮点
1. **12 项 Skill 覆盖编剧全流程:** `sw-story-structure` / `sw-premise-theme` / `sw-character-conflict` / `sw-dialogue` / `sw-scene-craft` / `sw-pacing` 等；每项 Skill 是蒸馏后的方法论
2. **19 本书 + 契诃夫 + 小津安二郎全集:** 原始材料覆盖度极高——Field (Screenplay) / Snyder (Save the Cat) / McKee (Story) / Hoxter / Hicks / Lu Jun (起承转合) / Egri (The Art of Dramatic Writing) / Indick 等
3. **中英双语 Skill 工程化:** Skill 内容主体中文（来源与引文都是中译），frontmatter 英文 + 中文关键词——双语 Skill 的可工程化路径
4. **Claude Code 协议适配:** `/plugin marketplace add jtydhr88/screenwriting-skills` + `/plugin install screenwriting@screenwriting-skills` 标准化安装
5. **方法论蒸馏而非简单摘要:** 蒸馏深度（如"八种开头 / 八种结尾 / 五种前提 / 三种冲突上升模式"等具体框架）vs LLM 简单摘要

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 垂直领域 Skill 套装层——12 项 Skill 覆盖编剧全流程；Skill 内容是蒸馏后的方法论，不是原始材料 | 边界由 README 明示 12 项 Skill；具体蒸馏深度（是否完整保留原文）需 README 核验 |
| 主路径 | 用户创作问题 → 触发对应 Skill（如 `sw-character-conflict`）→ Skill 加载蒸馏方法论 → LLM 应用方法论 → 输出创作建议 | 主路径为 README 语义抽象；Skill 触发机制（frontmatter keywords vs SKILL.md 描述）需 README 核验 |
| 关键权衡 | 蒸馏深度（vs 简单摘要）vs Skill 文件大小；19 本书的版权边界（vs 合理使用）；中英双语 Skill 的内容一致维护（vs 仅英文） | README 列出来源书目；版权 / 翻译授权细节未在 README 中可见 |
| 最小 PoC | Claude Code 安装 Skill → 在 `/plugin` 触发 `sw-story-structure` → 给定一个故事大纲 → 检查输出是否引用 Save the Cat beats + McKee event/scene + Lu Jun 起承转合 | PoC 范围由 README "Install" 推导；Skill 输出质量需 benchmark |

## 架构启发
`screenwriting-skills` 的核心启发是 **"Skill 不只是单点技巧，而是专业方法论的蒸馏套装"**。传统 Skill 模式（humanizer / sepia）输出"指令转换"或"去 AI 化"；screenwriting-skills 输出"编剧方法论"。更深层的启发是 **"垂直领域专家的认知蒸馏"**——19 本书 + 契诃夫 + 小津安二郎的覆盖率反映作者对编剧领域的深度投入，这是通用 LLM 难以替代的。

风险提示：**"蒸馏 19 本书" 的版权边界需要核验**——是否取得原作者 / 版权方授权 / 是否引用超出合理使用范围；与 anthropics/skills（蒸馏 Claude 使用经验）的法律边界类似。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户/编剧] --> Q[创作问题<br/>如角色冲突/故事结构]
  Q --> Trigger[Claude Code Plugin 触发<br/>frontmatter keywords 中英]
  Trigger --> Match{匹配 Skill}
  Match -->|sw-story-structure| S1[结构方法论<br/>Save the Cat + McKee + Lu Jun]
  Match -->|sw-premise-theme| S2[前提主题<br/>Egri + McKee + Cron]
  Match -->|sw-character-conflict| S3[角色冲突<br/>Egri + Indick + Freud/Jung/Campbell]
  Match -->|sw-dialogue| S4[对白方法论<br/>待核验]
  Match -->|其他 8 项| S5[其他 8 项方法论<br/>待核验]
  S1 --> Corpus[蒸馏来源<br/>19 本书 + 契诃夫 + 小津安二郎]
  S2 --> Corpus
  S3 --> Corpus
  S4 --> Corpus
  S5 --> Corpus
  S1 --> Out[创作建议<br/>中英输出]
  S2 --> Out
  S3 --> Out
  S4 --> Out
  S5 --> Out
  Corpus -.版权边界 待核验.-> Legal[合理使用 / 翻译授权]
  Trigger -.agentskills.io.-> Runtime[Claude Code Runtime]
```

## 定位判断
**工具型项目（垂直领域 Skill 套装——编剧），向"专业方法论蒸馏市场"演进。** `screenwriting-skills` 不仅是一个 Skill 仓库，更是 Skill 模式从"通用单 Skill"升级到"垂直领域深度蒸馏"的样本。2 天 301⭐ / fork/star 13.3% 已显示初步采用。但套装化的成功取决于：(a) 19 本书的版权边界；(b) 中英双语 Skill 的内容一致维护；(c) 蒸馏深度 vs 简单摘要的差异化。当前定位是"中文社区最深的编剧 Skill 套装"，向"专业方法论 Skill 商店"演进是合理路径。

## 风险/局限/泡沫点
- **19 本书的版权边界:** 是否取得原作者 / 版权方授权 / 是否引用超出合理使用范围需要核验；与 anthropics/skills 的法律边界类似
- **中英双语 Skill 的内容一致性维护:** Skill 主体中文 + frontmatter 英文——双语维护成本高；中英 Skill 触发机制是否真的双语触发需要测试
- **垂直领域专家级 Skill 的冷启动门槛:** 需要作者本人是真实编剧领域专家（jtydhr88 是中文社区编剧 / 剧作爱好者，19 本书蒸馏反映深度投入）；复制难度高
- **Skill 输出的质量稳定性:** 蒸馏方法论 vs LLM 简单摘要——Skill 触发的输出是否真的比 LLM 默认输出更优需要 benchmark
- **2 天新项目风险:** jtydhr88 是新 GitHub 账号（screenwriting-skills 是其首个 300+⭐ 项目），项目可持续性 / 治理结构未验证
- **Skill 触发机制的歧义:** 12 项 Skill 的 frontmatter 关键词是否有重叠（如 "character" 同时匹配 `sw-character-conflict` 和 `sw-story-structure`）需要测试

## 与同类项目的关系
- **vs mattpocock/skills (9-06, 252K⭐):** mattpocock 是通用 Skills 集合（252K⭐，多领域）；screenwriting-skills 是垂直领域深度蒸馏——通用 vs 垂直
- **vs DietrichGebert/ponytail (9-06, 2813⭐/day):** ponytail 是 "Laziest senior dev" 单 Skill；screenwriting-skills 是 12 项 Skill 套装——单 Skill vs 套装
- **vs anthropics/skills (9-06, 472⭐/day):** anthropics 是 Claude 官方 Skills；screenwriting-skills 是社区垂直领域——官方 vs 社区
- **vs humanlayer/skills (9-06, 408⭐/day):** humanlayer 是 multi-agent Skills；screenwriting-skills 是单 Agent 垂直领域
- **vs Nanako0129/sepia (9-07, 2324⭐):** sepia 是 77+ Agent 兼容的去 AI 化 Skill；screenwriting-skills 是单 Agent 垂直领域——通用 vs 垂直

## 是否值得持续跟踪
**值得跟踪（垂直领域 Skill 套装头部样本——编剧）。** `screenwriting-skills` 代表了 Skill 模式从"通用单 Skill"升级到"专业方法论蒸馏套装"的方向，与 Claude Code Plugin 协议 + 19 本书 + 中英双语 + 2 天 301⭐ 共同构成新方向。建议关注：(a) 19 本书的版权治理；(b) 中英双语 Skill 的内容一致维护；(c) 蒸馏深度 vs 简单摘要的 benchmark；(d) 下一波垂直领域（律师 / 医生 / 设计师）Skill 套装是否跟进。对编剧 / 剧作 / 创意写作从业者，这是中文社区首个深度蒸馏 Skill 套装。

## 后续观察点
- 19 本书的版权 / 翻译授权细节
- 蒸馏深度的工程实现（vs LLM 简单摘要的差异）
- 中英双语 Skill 触发机制的歧义处理
- 下一波垂直领域 Skill 套装（律师 / 医生 / 设计师）
- Claude Code Plugin Marketplace 的演进
- Skill 输出质量的 benchmark（vs LLM 默认输出）

---
> 数据来源: GitHub API (2026-09-08) | Stars: 301 | Forks: 40 | License: 待核验 | 语言: Markdown | 创建: 2026-09-06
