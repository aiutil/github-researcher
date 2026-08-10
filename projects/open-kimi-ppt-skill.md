---
title: "Binaryify/open-kimi-ppt-skill"
slug: "open-kimi-ppt-skill"
date_added: "2026-08-06"
last_seen_date: "2026-08-09"
category: "工具型"
emoji: "🎞️"
stars: "1,607 stars (archived)"
stars_delta: "⚠️ 已归档（archived=true）。8/05创建→8/09观测 1,588⭐ / 1,113 fork，fork/star=0.70 极端异常，昨日判断被验证，降级案例库"
language: "Python"
license: "MIT"
score: 70
tags: ["ppt-generation", "kimi-slides", "reverse-engineering", "agent-skill", "pptx", "python"]
url: "https://github.com/Binaryify/open-kimi-ppt-skill"
---

# Binaryify/open-kimi-ppt-skill — 逆向 Kimi Slides 的 PPT 生成 Skill

## 一句话定位
通过逆向分析 Kimi Slides 的 Skill、PPTD 格式和公开网页编辑器前端行为/通信协议，让 AI agent 生成可编辑 PPTD+PPTX（自动嵌入字体+动画）的非官方 Skill，含本地浏览器编辑器。

## 它解决的问题
目标用户是需要在 agent 工作流中生成演示文稿的用户。痛点：AI 生成 PPT 通常输出静态图片或不可编辑的成品，无法后续调整。open-kimi-ppt-skill 通过逆向 Kimi Slides 的 PPTD 格式，每次生成**两份成果**——可继续编辑的 PPTD 项目 + 开箱即用的 PPTX 成品（自动嵌入字体、写入淡入淡出切换动画），并提供本地浏览器 PPTD 编辑器支持随时手动导出。

## 为什么值得关注（2026-08-06）

这标志着**中文 agent skill 品类向办公场景扩展**——与 human-writing（写作）同日爆发，但面向演示场景。530⭐ / 149 fork（fork/star 比例高）说明有用户在尝试部署/定制。关键差异化：(a) **逆向工程路径**（非官方，逆向 Kimi Slides 的格式和协议）；(b) **双产物交付**（PPTD 可编辑 + PPTX 可用）；(c) **Skill 分发模式**（兼容 Codex/Claude Code/Cursor/WorkBuddy 等 SKILL.md 规范 agent）。149 fork（高于 human-writing 的 98 fork，虽然 star 更低）说明部署意愿强。

## 热度来源判断
- **真实需求信号**：149 fork（fork/star 28%，异常高）说明大量用户在尝试部署/定制。AI 生成可编辑 PPT 是办公场景高频需求。
- **话题性成分**：逆向 Kimi Slides 有话题性（"破解官方能力"），首日数据可能含话题爆发成分。
- **风险成分**：逆向工程项目依赖公开前端资源，**README 明确声明非官方项目，可能随 Kimi 更新失效**。

## 关键技术亮点

1. **逆向 PPTD 格式**：通过逆向分析 Kimi Slides Skill、PPTD 格式和公开网页编辑器的前端行为与通信协议实现。PPTD 是可编辑的项目格式（非最终成品）。
2. **双产物交付**：每次生成默认同时交付 PPTD（可继续编辑）和 PPTX（开箱即用，自动嵌入字体+淡入淡出动画）。
3. **本地浏览器编辑器**：提供本地在线 PPTD 编辑器，支持随时手动导出。不依赖云服务编辑。
4. **多 Agent 兼容**：兼容 Codex、Claude Code、Cursor、WorkBuddy 等任何兼容 SKILL.md 规范的 agent。
5. **npm 分发**：`open-kimi-ppt-skills` npm 包，`npx open-kimi-ppt-skills` 或 Agent 安装命令。

## 架构启发
open-kimi-ppt-skill 的设计哲学是 **"逆向官方格式以获得可编辑性"**——与其从零构建 PPT 生成（复杂、质量不稳定），不如逆向已有成熟产品（Kimi Slides）的格式，复用其排版/动画能力。对架构师的启发：**逆向成熟产品的格式/协议可以快速获得可用性**，但代价是依赖上游稳定性（官方更新可能 break）。双产物交付（可编辑 + 可用）是降低用户迁移成本的设计。

## 定位判断
属于 **L5 应用层/skill 层**，是中文 agent skill 生态中的**办公演示 skill**。与 human-writing（写作）共同构成中文垂直 skill 首批代表。

## 风险 / 局限 / 泡沫点

1. **逆向工程的法律/稳定性风险**：README 明确声明"通过逆向分析实现，并非 Kimi 或 Moonshot AI 的官方项目，也未获得其认可或支持。项目依赖的公开前端资源和兼容协议可能随 Kimi 更新而失效，仅供学习与研究使用。"这意味着**任何 Kimi 更新都可能 break 这个 skill**。
2. **首日数据，持续性未验**：530⭐ 是首日数据，需观察 08-07 是否回落。149 fork 的高比例可能是"试用/好奇"而非"生产部署"。
3. **生成质量需独立验证**：逆向 Kimi Slides 的排版/动画质量取决于对官方格式的逆向完整度，复杂版式（图表、嵌入视频、母版）的还原度未独立验证。
4. **强绑定 Kimi 生态**：PPTD 格式是 Kimi 的私有格式，skill 的可维护性完全取决于 Kimi 是否持续维护该格式。

## 与同类项目的关系
- **vs human-writing（1,006⭐）**：同日爆发的中文 agent skill，human-writing 面向写作（文本），open-kimi-ppt-skill 面向演示（PPT）。两者共同构成中文 skill 品类。
- **vs genoffice（1,755⭐）**：genoffice 是完整 AI-native 办公套件（含演示），open-kimi-ppt-skill 是专门的 PPT 生成 skill。genoffice 是平台，open-kimi-ppt-skill 是 skill。
- **vs Marp/reveal.js**：Marp/reveal.js 是 Markdown→slides 工具，open-kimi-ppt-skill 是 AI→PPTD/PPTX。前者是格式转换，后者是 AI 生成。

## 是否值得持续跟踪
**是，作为"中文 agent skill + 逆向工程路径"的代表项目跟踪，但标注高风险。** 逆向工程路径有法律/稳定性风险，需持续观察 Kimi 更新是否 break 以及是否有官方替代。

## 后续观察点
1. **Kimi 更新影响**：Kimi Slides 下一次更新是否 break 这个 skill，以及作者的修复速度。
2. **生成质量**：复杂版式（图表、嵌入视频、母版、动画）的还原度。
3. **官方反应**：Kimi/Moonshot AI 是否会对逆向项目采取法律行动或发布官方 skill。

---
*首次记录：2026-08-06* · *数据来源: GitHub API + 仓库 README*

## 最近动态（2026-08-07）

- **第三日爆发 +756（+142%），fork 149→343（+194）**：530 → 1,286，fork 增量 +194 是强部署意愿信号（fork/star 比 26.7%，极高）。增速从首日爆发后不降反升（+142%），说明话题性爆发有持续放大。
- **判断修正**：score 82 → 83。爆发持续 + fork 高增长。但 +142% 增速不可持续，关键看 08-08 回落斜率。
- **风险（不变）**：逆向工程路径有法律/稳定性风险（README 自述非官方，可能随 Kimi 更新失效）。pushed_at 08-06（活跃维护）。

## 最近动态（2026-08-08）

- **第四日 +301（+23%），但 fork 异常暴增 343→914（+571）**：1,286 → 1,587，fork/star=0.58 异常（正常项目 <0.3）。单日 fork +571 远超 star +301，疑似刷量或批量部署。降级观察。
- **判断修正**：score 83 → 82。fork 异常比值是可疑信号。

## 最近动态（2026-08-09）

- **⚠️ 仓库已被作者归档（archived=true，GitHub API 可核验）**：1,588⭐ / 1,113 fork。昨日报告的"fork 异常暴增 343→914（单日+571），fork/star=0.58 异常，疑似刷量或批量部署"判断今天落地为归档。
- **fork 异常持续但 star 几乎不动**：fork 914→1,113（+199，异常持续），star 1,587→1,588（+1，几乎无增长）。fork/star=0.70 极端异常。
- **方法论验证案例**：这是一个"异常 fork 增速 → 提前标记 → 落地归档"的完整案例。fork 增速远超 star 增速（fork/star 比从 0.27→0.58→0.70 持续恶化）是"刷量/批量部署/弃坑前兆"的可靠信号。
- **判断修正**：score 82 → 70。降级为案例库，不再跟踪。归档后 star/fork 基本冻结。
