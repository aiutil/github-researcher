---
title: "0xwilliamortiz/humanizer-cli"
slug: "humanizer-cli"
date_added: "2026-08-07"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "🔎"
stars: "581 stars"
stars_delta: "8/01创建→8/07观测 581⭐ / 72 fork / 208 watchers（高关注度），pushed 08-04"
language: "JavaScript"
license: "MIT"
score: 83
tags: ["ai-writing-detection", "humanizer", "terminal", "cli", "skill-derived", "zero-dependencies", "wikipedia-signs-of-ai-writing"]
url: "https://github.com/0xwilliamortiz/humanizer-cli"
---

# 0xwilliamortiz/humanizer-cli — 终端去 AI 腔检测 CLI

## 一句话定位
一个终端参考工具，把 [humanizer](https://github.com/blader/humanizer) skill 收集的 33 种 AI 写作模式（来自 Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing)）做成可交互查询和草稿检查的 CLI——零网络、零 API key、零运行时依赖，核心是 87KB 的 C 二进制，Node 仅作启动器。

## 它解决的问题
目标用户是写作者、编辑、需要产出"不像 AI 写的"文本的人。痛点：AI 生成的文本有可识别的模式（dash 滥用、"not just X, it's Y"、填充措辞、标题里的 emoji、制造热情），但人类很难在写作时同时记住所有模式并自检。humanizer-cli 把 Wikipedia 目录化的 33 种模式变成终端里可查询、可检查草稿的参考工具，且数据不离开本机。

## 为什么值得关注（2026-08-07）

它是今日发现的"去 AI 腔"写作治理品类的一个关键节点——**终端化、事后检测**的封装。关键信号是 **208 watchers**（远高于其 581⭐ 和 72 fork 的比例，通常 watchers < stars 的 5%），说明这是一个被密切关注的工具型项目（人们 star 不一定用，但 watch 说明"我在等它成熟"）。它与 human-writing（中文，事中改写）、ratchet（事前约束）构成完整的"写作治理三层谱系"。

## 热度来源判断
- **真实需求信号**：208 watchers 是强关注信号——watchers 代表"我想持续关注这个项目的发展"，比 star 更深度。72 fork 说明有人愿意部署/修改。
- **品类热度成分**：它踩中"AI 写作检测/治理"热点，且明确溯源 blader/humanizer（34K⭐）——这不是孤立项目，而是一个已验证品类（humanizer 34K⭐）的接口扩展。
- **Wikipedia 权威性**：33 种模式来自 Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing)，有社区共识的目录化基础，非个人主观清单。

## 关键技术亮点

1. **零依赖 C 二进制 + Node 启动器**：核心是 87KB 的 C 二进制（`sources/humanizer.zip`，Windows x64），Node 仅作启动器。`npm install` 不下载除包以外的任何东西，无运行时依赖。设计哲学：把检测逻辑放在最小、最快的可执行单元。
2. **33 种 AI 写作模式目录**：来自 Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing)，每个模式带 before/after 示例。覆盖 dash 滥用、"not just X, it's Y"、填充措辞、标题里的 emoji、制造热情等。
3. **交互式终端查询**：`humanizer show 14`（看第 14 号模式）、`humanizer check draft.md`（检查草稿）、`humanizer search hedging`（搜索相关模式）、`humanizer patterns`（分组列出所有模式）。
4. **离线优先**：程序读取旁边的 `SKILL.md` 并打印，数据不离开本机。无网络、无 API key。

## 架构启发
humanizer-cli 的设计是 **"skill → CLI"的封装模式**——把一个 Agent skill（blader/humanizer 的 SKILL.md）转成一个独立的终端工具，脱离 agent 运行时。这代表了 skill 生态的一种演进：skill 不一定只能在 agent 内用，也可以被"提取"成独立工具。对架构师的启发：**skill 是可移植的知识载体**，同一份模式库可以同时服务于 agent（skill 内）和人类（CLI 内）。

## 定位判断
在"去 AI 腔"写作治理品类中占据 **"事后检测 + 终端接口"** 位置。与 human-writing（事中改写，中文）、ratchet（事前约束，agent 规则）互补。它是 blader/humanizer（34K⭐，通用 skill）的终端化分支——把 skill 从 agent 上下文里拿出来，变成写作者可在任何终端随时调用的参考工具。

## 风险 / 局限 / 泡沫点

1. **208 watchers vs 72 fork——关注度 > 部署意愿**：watchers 高说明被关注，但 fork 低说明实际部署/修改的人少。可能是"收藏了但还没用"的状态，实际使用率需观察。
2. **Windows x64 限制**：C 二进制仅提供 Windows x64 版本（`sources/humanizer.zip`），跨平台支持有限。macOS/Linux 用户依赖 Node 启动器但核心检测可能受限（README 标注 Windows x64）。
3. **33 种模式为 Wikipedia 目录，非完整检测方案**：这些模式是"AI 写作的常见迹象"，但不是穷尽的检测算法。复杂/微妙的 AI 写作痕迹可能不被这 33 种模式覆盖。
4. **检查模式（check）的效果未独立验证**：`humanizer check draft.md` 的检测准确率、误报率未独立基准测试。

## 与同类项目的关系
- **vs blader/humanizer（34,004⭐）**：humanizer 是源头 skill（通用，agent 内用），humanizer-cli 是其终端化封装（脱离 agent，人类直接用）。README 明确声明"the humanizer skill 的终端参考"。
- **vs KKKKhazix/human-writing（1,552⭐）**：human-writing 是事中改写（让 AI 写的中文有活人感，中文），humanizer-cli 是事后检测（检查已有文本的 AI 痕迹，英文）。阶段和语言不同，互补。
- **vs 0xwilliamortiz/ratchet（435⭐，同一作者）**：ratchet 是事前约束（agent 写作前的规则检查），humanizer-cli 是事后检测。同一作者的"写作治理"产品线，覆盖事前→事后。

## 是否值得持续跟踪
**是，作为"去 AI 腔"写作治理品类的"终端检测"节点跟踪。** 208 watchers 是强关注信号，且它明确溯源 blader/humanizer（34K⭐ 已验证品类）。重点验证 check 模式的实际检测效果，以及跨平台支持是否扩展。

## 后续观察点
1. **watchers 持续性**：208 watchers 是否增长，还是停滞——增长说明品类有持续吸引力。
2. **跨平台扩展**：是否增加 macOS/Linux 的原生二进制支持，扩大用户群。
3. **与 humanizer 上游的同步**：blader/humanizer skill 更新时，humanizer-cli 是否同步新的模式。

---
*首次记录：2026-08-07* · *数据来源: GitHub API + 仓库 README*
