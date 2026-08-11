---
title: "microsoft/skill-recorder"
slug: skill-recorder
date_added: "2026-08-03"
last_seen_date: "2026-08-09"
category: "工具型"
emoji: "🎥"
stars: "2,805 stars"
stars_delta: "7/29创建→8/09 2,509⭐（第八日 +197/+9%，增速稳定），fork 245→266"
language: "TypeScript"
license: "MIT"
score: 84
tags: ["skill-authoring", "copilot", "screen-recording", "automation", "microsoft", "electron", "typescript"]
url: "https://github.com/microsoft/skill-recorder"
---

# microsoft/skill-recorder — 录屏→Copilot 重建意图+步骤→生成可复用 Skill

## 一句话定位
Microsoft 官方桌面应用：录屏捕获一次真实工作会话（点击、应用切换、页面、可选语音叙述），用 GitHub Copilot CLI 重建为"意图 + 有序步骤"，再一键生成可复用 Skill（`SKILL.md`）或定时 Automation，面向 Microsoft Scout / Copilot Cowork / Copilot Studio。

## 它解决的问题
目标用户是希望把"自己会做的重复任务"变成 agent 可复用技能的人。痛点：手动写 agent skill/automation 需要把隐性操作知识显式化成步骤文档，门槛高且易遗漏。skill-recorder 的路径是**从人类真实执行反推 skill**——录一次屏，让 Copilot 重建意图与步骤，再生成可复用产物。

## 为什么值得关注（2026-08-03）

这是 Microsoft 官方在 agent skill 生态的入场。它的独特之处是**"从观察到技能"的反向路径**——多数 agent 工具是从 skill 到执行（写好 SKILL.md 让 agent 跑），skill-recorder 是从人类执行到 skill 提取（录屏→重建→生成）。这填补了 skill 生态里"如何低成本把人类隐性知识变成 agent 可用技能"的入口缺口。5 天 726⭐ + 75 fork，MIT 开源。

## 热度来源判断
- **真实需求信号**：Microsoft 官方仓库（`microsoft/` org），fork 75 说明有人在实际尝试；README 详尽（含安装、使用、平台支持），是认真发布的产品。
- **品类热度成分**：受益于本周 agent skill 生态整体热度（Superpowers/ECC/mattpocock skills 等）；但"录屏→重建→生成"是独立差异化路径。
- **官方背书权重**：`microsoft/` org 的项目天然有更高关注度，726⭐ 含品牌溢价成分。

## 关键技术亮点亮点

1. **录屏 → Copilot CLI 重建意图+步骤**：捕获屏幕活动（点击、应用/窗口切换、页面、可选语音），用 GitHub Copilot CLI 重建为"一个整体意图 + 有序列表"。强调优先用 agent 的**原生工具**（如 `gh` CLI、`web_fetch`）而非重放 UI 点击，并从单次示例泛化（录一次提交表单 → 教 agent 提交所有同类表单）。
2. **两种输出产物**：(a) **Skill**——`SKILL.md` 过程文档，agent 按需运行；(b) **Automation**——同样过程但按计划/触发器运行。
3. **源码发布模式**：不提供预编译二进制，而是 pin 一个 release commit + 本地构建（`curl install.sh | bash`，下载 pinned Node.js runtime + 构建精确 commit），添加"Skill Recorder (Source)"应用。不全局安装。这是可审计的发布方式，但对非技术用户有门槛。
4. **跨平台**：macOS 为主目标，Windows 11（x64 + ARM64）支持，Ubuntu 也有应用条目。

## 架构启发
核心启发是 **"观察→重建→泛化"的 skill 提取范式**。传统 skill 创作是"人写步骤文档"，skill-recorder 是"人做一次，模型重建步骤"。这与 Ponytail（约束输出）、loop-engineering（设计循环）从不同角度共同指向：**agent 的能力获取正在从"手写 prompt/skill"走向"从人类行为提取/约束生成"**。trade-off 是：重建质量依赖 Copilot CLI 的理解能力，复杂任务的意图重建可能不准确，需人工审阅编辑（README 也强调"Review and edit until it reads right"）。

## 定位判断
在 agent skill 生态中占据**"skill 创作入口工具"**位置——在 Superpowers/ECC/mattpocock skills（成品 skill 库）与 Ponytail/loop-engineering（skill 设计方法论）之间，提供"从人类执行到 skill"的低门槛入口。强绑定 Microsoft Copilot 生态（Scout/Copilot Cowork/Copilot Studio），跨生态适用性有限。

## 风险 / 局限 / 泡沫点

1. **强绑定 Microsoft 生态**：需 GitHub Copilot 访问权限，面向 Scout/Copilot Cowork/Copilot Studio。对 Claude Code/Codex/OpenCode 等其他 harness 的 skill 格式不直接适用。生态封闭性限制其作为通用工具的价值。
2. **重建质量依赖 Copilot CLI**：复杂任务的意图重建可能不准确（漏步骤、误判意图），需人工审阅。README 虽强调"review and edit"，但审阅成本可能在高复杂度任务上抵消"录屏比手写快"的优势。
3. **源码发布对非技术用户有门槛**：pin commit + 本地构建模式对开发者友好，但对业务用户（CRM/销售场景）门槛高。
4. **29 open issues**：5 天 29 个 open issue 说明早期质量问题。

## 与同类项目的关系
- **vs Ponytail（80K⭐）/ loop-engineering（6.9K⭐）**：后两者是 skill/agent 行为的**设计方法论**（约束输出/设计循环），skill-recorder 是 skill 的**创作入口工具**（从执行提取）。互补而非竞争。
- **vs Superpowers（252K⭐）/ ECC（228K⭐）**：后两者是成品 skill 市场/库，skill-recorder 是 skill 的**生产工具**——让人不依赖现成 skill 库就能造自己的 skill。
- **vs OpenCut/video-use（agent 创作视频）**：方向不同——后者是 agent 创作内容，skill-recorder 是人创造 skill 给 agent 用。

## 是否值得持续跟踪
**是，作为"agent skill 创作入口"的官方代表跟踪。** 关注其是否扩展到非 Microsoft 生态（如支持 Claude Code/Codex 的 SKILL.md 格式）、重建质量在复杂任务上的表现。

## 后续观察点
1. **跨生态扩展**：是否会支持非 Copilot 的 skill 格式（如通用 AGENTS.md/CLAUDE.md），还是保持 Microsoft 封闭生态。
2. **重建质量基准**：复杂任务（多步骤、跨应用）的意图重建准确率，是否有公开评测。
3. **29 open issues 的收敛**：早期质量问题是否随版本迭代收敛。

## 最近动态（2026-08-04）

- **续涨 +640（726→1,366），fork 75→141**：连续增长，"从观察到技能提取"的官方入场持续获关注。fork 141 说明有人在真实尝试构建 Skill。
- **品类定位**：与今日新增的 ratchet（agent 代码质量约束）形成正交互补——skill-recorder 解决"技能从哪来"，ratchet 解决"执行后是否守住底线"。两者共同构成 agent 工作流的质量基础设施。

## 最近动态（2026-08-05）

- **续涨 +385（1,366→1,751），fork 141→177**：增速从 +640 衰减到 +385，但仍维持正增长。作为 agent 三层质量栈的"技能提取层"，随 numbat（可观测性层）今日加入，skill-recorder 的品类定位进一步巩固。
- **三层栈成型**：skill-recorder（技能提取，事前）→ ratchet（执行约束，事中）→ numbat（可观测/取证/阻断，事中+事后）。skill-recorder 是这个栈的入口。
- **待观察（不变）**：强绑 Microsoft 生态（需 Copilot 访问权限），29 open issues 早期质量问题待收敛。

---
*首次记录：2026-08-03* · *最近更新：2026-08-06（1,751→1,944，+193/+11%，稳定增长）*

## 最近动态（2026-08-06）

- **第五日 +193（1,751→1,944，+11%），fork 177→193**：增速从 +385 衰减到 +193，但仍维持正增长。作为 agent 三层质量栈的"技能提取层"稳定增长，未出现爆发或骤降。
- **三层栈稳定**：skill-recorder（技能提取，事前）→ ratchet（执行约束，事中）→ numbat（可观测/取证/阻断，事中+事后）。今日 human-writing/open-kimi-ppt-skill 等中文 skill 出现，说明 skill 生态在横向扩张——skill-recorder 作为"制造 skill 的工具"定位进一步巩固。
- **待观察（不变）**：强绑 Microsoft 生态（需 Copilot 访问权限），33 open issues（较昨日 29 上升，早期质量问题待收敛）。

## 最近动态（2026-08-07）

- **第六日 +183（+9%），跨入 2K 关口**：1,944 → 2,127，fork 193 → 220（+27）。增速稳定衰减（+11%→+9%），但仍维持正增长。
- **三层栈稳定**：skill-recorder（技能提取，事前）+ 今日发现的"去 AI 腔"写作治理三层谱系（ratchet 事前约束 / human-writing 事中改写 / humanizer-cli 事后检测）共同构成 agent 写作/技能质量基础设施。skill-recorder 是"制造 skill 的工具"，与 humanizer 谱系是"改善 skill 输出质量的工具"互补。
- **判断**：score 维持 84。稳定增长 + 品类定位巩固。pushed_at 08-06（活跃开发）。open_issues 30（略降，健康的 issue 处理）。

## 最近动态（2026-08-08）

- **第七日 +185（+9%），增速稳定**：2,127 → 2,312，fork 220 → 245（+25）。增速维持 +9%，是应用层中最稳定的项目。

## 最近动态（2026-08-09）

- **第八日 +197（+9%），增速稳定，fork 245→266（+21）**：2,312 → 2,509，连续两日 +9%，是应用层中唯一增速稳定（非衰减）的项目。今日有新提交（pushed_at 08-07）。open_issues 32（略升）。
- **判断（维持 score 84）**：连续两日 +9% 稳定增长，三层栈"技能提取层"定位巩固。对比 qm（+2%）、crm（+4%）、genoffice（+4%）的衰减，skill-recorder 的稳定性说明"录屏→Skill 生成"有持续需求。
