---
title: "mubix/cyber-resume-reviewer-skill"
slug: cyber-resume-reviewer-skill
date_added: 2026-09-09
last_seen_date: 2026-09-09
category: "工具型"
emoji: "📄"
stars: "112 stars"
stars_delta: "2 天 0→112⭐，单日均速 ~56⭐/day；网络安全简历证据化审查 Agent Skill"
language: "Python"
score: 72
tags: ["mubix", "agent-skill", "cybersecurity", "resume", "pdf", "markdown", "evidence-based"]
url: "https://github.com/mubix/cyber-resume-reviewer-skill"
---

# mubix/cyber-resume-reviewer-skill

## 一句话定位
网络安全简历 Agent Skill——证据化审查 + JD 适配 + 精确编辑 + 诊断打分 + Markdown 报告 + 样式 PDF；不排名 / 不预测 / 不编造；2 天 112⭐，是 2026-09-09 "反 AI 化 / 反 Claude 风格化 Skill" 趋势的代表样本之一。

## 它解决的问题
网络安全 / IT 行业的简历审查存在三个痛点：(1) **AI 简历幻觉**——通用 LLM 经常编造不存在的经验或夸大能力；(2) **JD 适配繁琐**——每份 JD 需要重新调整简历重点；(3) **审查报告格式混乱**——人工 review 输出格式不统一，难以复用。`mubix/cyber-resume-reviewer-skill` 直击这三点：

1. **证据化审查**——只审查简历中已有的证据，不引入外部假设
2. **JD 适配**——给定的 JD 自动调整简历重点
3. **诊断打分**——客观评分 + 优先级 findings + 精确编辑建议
4. **Markdown 报告 + 样式 PDF**——可编辑 Markdown + 样式 PDF 双输出

**明确边界**："The skill does not rank candidates, predict interviews, or invent missing achievements."——明确不排名 / 不预测 / 不编造——这是 Skill 模式**反 AI 幻觉**的关键设计。

## 为什么值得关注（2026-09-09）
- **Stars:** 112（截至 2026-09-09），2 天净增，单日均速 ~56⭐/day
- **Forks:** 10（fork/star 8.9%，中等区间）
- **Watchers/Subscribers:** 待观察
- **Open Issues:** 待观察
- **License:** None（仓库无 license 文件）
- **语言:** Python 主导
- **项目年龄:** 2 天（创建 2026-09-07），是 2026-09-09 trending 新项目
- **核心差异:** 证据化审查 + 反 AI 幻觉 + Markdown + 样式 PDF + 网络安全垂直

## 热度来源判断
热度来自 **三个层面的叠加**：(1) **网络安全 / IT 行业简历刚需**——mubix 是网络安全社区知名作者，简历审查是高频需求；(2) **反 AI 幻觉的 Skill 设计**——"不编造"明确边界，对比通用 LLM 简历审查有差异化；(3) **垂直领域 Skill**——网络安全 vs 通用，覆盖深度差异化。

2 天 112⭐ / 10 fork 反映 **"网络安全垂直 + 反 AI 幻觉 + 证据化审查"** 三者叠加——是真实垂直需求场景。

## 关键技术亮点
1. **证据化审查：** 只审查简历中已有的证据，不引入外部假设——反 AI 幻觉
2. **JD 适配：** 给定 JD 后自动调整简历重点——目标导向审查
3. **精确编辑：** 提供具体的编辑建议（不是泛泛而谈）——可执行改进
4. **诊断打分：** 客观评分 + 优先级 findings——可对比改进
5. **Markdown + 样式 PDF：** Markdown 报告可编辑 + 样式 PDF 可分享——双输出
6. **明确边界：** 不排名 / 不预测 / 不编造——这是 Skill 模式**反 AI 幻觉**的关键设计

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Agent Skill 层 + 简历 / JD 解析 + 证据化审查 + Markdown / PDF 报告生成；输入是简历 + JD，输出是诊断报告 | 边界由 README 明示；具体 LLM 调用方式、Markdown / PDF 报告生成方式需代码审阅 |
| 主路径 | 用户提供简历 + JD → Skill 触发 → 简历 / JD 解析 → 证据化审查 → 精确编辑 + 诊断打分 → Markdown 报告 + 样式 PDF | 主路径为 README 语义抽象；具体审查规则、编辑建议生成、打分逻辑需代码审阅 |
| 关键权衡 | 证据化（反幻觉）vs 通用 LLM 自由发挥；垂直网络安全（深度）vs 通用简历（广度）；Markdown + PDF（双输出）vs 单 Markdown（简单） | README 明示证据化 + 网络安全垂直 + 双输出；具体审查规则深度未在 README 可见 |
| 最小 PoC | 安装 Skill → 提供简历（PDF / DOCX / 文本）+ JD → 触发 Skill → 检查 Markdown 报告 + 样式 PDF → 验证审查只引用简历证据，不引入外部假设 | PoC 范围由 README 明示；具体审查准确性、打分合理性需 benchmark |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[求职者] --> Resume[简历<br/>PDF / DOCX / 文本]
  User --> JD[目标 JD<br/>职位描述]
  Resume --> Skill[Agent Skill 触发]
  JD --> Skill
  Skill --> Parse[简历 / JD 解析]
  Parse --> Review[证据化审查<br/>只引用简历证据]
  Review --> Edit[精确编辑建议]
  Review --> Score[诊断打分<br/>优先级 findings]
  Edit --> MD[Markdown 报告]
  Score --> MD
  Edit --> PDF[样式 PDF]
  Score --> PDF
  MD --> User
  PDF --> User
  Review -.反 AI 幻觉.-> Boundary["不排名 / 不预测 / 不编造"]
  Skill -.agentskills.io.-> Runtime["Claude Code / Codex / Cursor"]
```

## 架构启发
`mubix/cyber-resume-reviewer-skill` 的核心启发是 **"反 AI 幻觉的 Skill 设计模式"**——"The skill does not rank candidates, predict interviews, or invent missing achievements." 是 Skill 模式**反 AI 幻觉**的关键设计。这与 9-06 `blader/humanizer`（去 AI 化 Agent Skill）+ 9-07 `Nanako0129/sepia`（去 AI 化）+ 9-09 `andrewroxby/claude-style-patch`（反 Claude 风格化补丁）共同构成"反 AI 化 Skill" 趋势。

更深层的启发是 **"Skill 不只是'加能力'，也可以是'改行为'"**——传统 Skill 模式（humanizer / sepia / screenwriting-skills）是"加新能力"；`claude-style-patch` 是"改风格"；`cyber-resume-reviewer-skill` 是"加约束（不编造）"。**Skill 模式的内涵正在扩展**。

风险提示：**License 缺失**——仓库无 license 文件，使用 / 二次开发 / 商用的法律边界不清晰；**审查准确性的 benchmark 缺失**——README 没有给出审查准确性的实测数据。

## 定位判断
**工具型项目（网络安全简历证据化审查 Agent Skill）。** `mubix/cyber-resume-reviewer-skill` 在 2026-09-09 "反 AI 化 / 反 Claude 风格化 Skill" 趋势中切入，作为网络安全垂直的简历审查工具。差异化定位是 **"网络安全垂直 + 反 AI 幻觉 + 证据化审查 + Markdown + PDF"**——比通用 LLM 简历审查更严谨，比商业简历审查工具更垂直。当前定位是 **"网络安全简历审查 Skill 样板"**，向"垂直领域证据化审查 Skill"扩展是合理路径。

## 风险/局限/泡沫点
- **License 缺失：** 仓库无 license 文件，使用 / 二次开发 / 商用的法律边界不清晰
- **审查准确性的 benchmark 缺失：** README 没有给出审查准确性的实测数据——需要独立测试
- **网络安全垂直的局限：** 覆盖范围限于网络安全 / IT 行业，跨领域泛化能力需要观察
- **mubix 个人品牌依赖：** mubix 是网络安全社区知名作者，Skill 的可信度依赖作者个人品牌
- **PDF 提取准确性：** README 明示"A PDF or DOCX lets the agent check extraction and visible layout; pasted text supports content review only."——PDF 提取错误可能影响审查准确性
- **反 AI 幻觉的局限：** 证据化审查只能约束"不引入外部假设"，但 LLM 仍可能在审查过程中误解简历内容
- **2 天新项目风险：** mubix 是网络安全知名作者，但项目本身年龄 2 天——Skill 成熟度需要观察

## 与同类项目的关系
- **vs 通用 LLM 简历审查（ChatGPT / Claude 直接用）:** 通用 LLM 自由发挥但容易编造；mubix 证据化 + 反 AI 幻觉——**严谨 vs 灵活**
- **vs 商业简历审查工具（Resume Worded / Jobscan 等）:** 商业工具付费 + 通用；mubix 开源 + 网络安全垂直——**开源 vs 闭源**
- **vs 9-06 blader/humanizer (9-06, 988⭐/day):** humanizer 是去 AI 化 Agent Skill；mubix 是证据化审查——**反 AI 化 vs 证据化**
- **vs 9-07 Nanako0129/sepia (10 天 2,324⭐):** sepia 是 77+ Agent 兼容 deAI Skill；mubix 是网络安全垂直证据化审查——**广度 vs 深度**
- **vs 9-09 andrewroxby/claude-style-patch (1 天 91⭐):** claude-style-patch 是反 Claude 风格化；mubix 是反 AI 幻觉——**改风格 vs 加约束** 两条路线
- **vs Codex Skill 生态（holo-card-studio / RuiC-card-skill）:** Codex Skill 主要是"加能力"；mubix 是"加约束"——**加能力 vs 加约束**

## 是否值得持续跟踪
**值得跟踪（反 AI 幻觉 Skill 模式 + 网络安全垂直证据化审查）。** `mubix/cyber-resume-reviewer-skill` 代表 "Skill 不只是'加能力'，也可以是'改行为'" 的新方向——反 AI 幻觉是关键设计。建议关注：(a) 反 AI 幻觉 Skill 模式是否扩展到其他领域（医疗 / 法律 / 教育）；(b) 证据化审查的准确性 benchmark；(c) Skill 引用链 / 版本管理机制。对网络安全求职者，是免费的反 AI 幻觉简历审查工具；对 Skill 模式观察者，是"加约束"Skill 的早期样本。

## 后续观察点
- 反 AI 幻觉 Skill 模式是否扩展到其他领域（医疗 / 法律 / 教育）
- 证据化审查的准确性 benchmark——决定工具价值
- Skill 引用链 / 版本管理机制
- mubix 是否持续维护 / 治理结构演化
- License 是否补全——影响二次开发 / 商用

---
> 数据来源: GitHub API (2026-09-09) | Stars: 112 | Forks: 10 | License: None | 语言: Python | 创建: 2026-09-07
