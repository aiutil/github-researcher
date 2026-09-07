---
title: "alchaincyf/huashu-mac-use"
slug: huashu-mac-use
date_added: 2026-09-08
last_seen_date: 2026-09-08
category: "工具型"
emoji: "🍎"
stars: "181 stars"
stars_delta: "2 天 0→181⭐，单日均速 ~91⭐/day；macOS computer use + 每步取证"
language: "Swift"
score: 84
tags: ["agent-skill", "alchaincyf", "claude-code", "codex", "computer-use", "forensics", "macos", "openclaw", "swift"]
url: "https://github.com/alchaincyf/huashu-mac-use"
---

# alchaincyf/huashu-mac-use

## 一句话定位
让任何 agent 操控 Mac 上没有 API 的原生 app——"读后台、写不打扰、每步留取证" Agent Skill for macOS computer use；自研 L0 通道（bpy / CDP / 内嵌 Chromium）不调用云端 computer use API，2 天 181⭐，fork 25（fork/star 13.8%），Swift。

## 它解决的问题
2026 年 Computer Use Agent（OpenAI Operator / Anthropic Computer Use）已经能做 GUI 自动化，但绝大多数是：(a) **云端调用**——数据上传到云端模型；(b) **抢焦点**——操作时屏幕被 agent 占据；(c) **不可复现**——失败时无证据。`huashu-mac-use` 直击这三点：(a) **自研 L0 通道**（`bpy` 命令行 / `CDP` 调试协议 / macOS Accessibility API）**不调用云端 computer use API**——数据本地化；(b) **`mac shot` 后台截图**——**不抢用户焦点**（"读后台、写不打扰"）；(c) **每步取证**——`mac shot` 后台截图 + 状态日志，可复现。

## 为什么值得关注
- **Stars:** 181（截至 2026-09-08），2 天净增，单日均速 ~91⭐/day
- **Forks:** 25（fork/star **13.8%**，显著高于 magnitude 7.2% / fastpotify 4.4%）
- **语言:** Swift 主导
- **项目年龄:** 2 天（创建 2026-09-06）
- **核心差异:** 自研 L0 通道（不调用云端 API）+ 后台取证（不抢焦点）+ 多 Runtime 兼容

## 热度来源判断
`huashu-mac-use` 的热度来自三个因素：(1) **Computer Use 真实需求**——GUI 自动化是 2026 年 Agent 应用最热赛道之一；(2) **云端 API 的数据隐私担忧**——自研 L0 通道（不调用云端）是真实差异化；(3) **多 Runtime 兼容**——Claude Code / Codex / Kimi Code / Cursor / OpenClaw / WorkBuddy / 豆包工作 / 千问办公 / ZCode——Skill 模式的"广度分发"路线。

2 天 181⭐ / fork 25（fork/star 13.8%）的组合反映 **"Computer Use 真实需求 + 数据本地化差异化"**。

## 关键技术亮点
1. **自研 L0 通道:** `bpy` 命令行（Blender 自动化）/ `CDP`（豆包工作内嵌 Chromium）/ macOS Accessibility API（系统设置 / WPS 等）——不调用云端 computer use API
2. **`mac shot` 后台截图:** 实时后台取证，**不抢用户焦点**（"读后台、写不打扰"）
3. **每步取证:** 截图 + 状态日志——可复现 / 可调试 / 可回放
4. **多 Runtime 兼容:** 任何能读 SKILL.md 的 Runtime（Claude Code / Codex / Kimi Code / Cursor / OpenClaw / WorkBuddy / 豆包工作 / 千问办公 / ZCode）
5. **三个真实案例:** (a) Blender 巧克力甜甜圈（Metal GPU 2 分钟出 1920×1440）；(b) 4 张 AI 生成照片 → Blender 建模 → 同机位渲染邮轮（33 分钟 / 8 轮迭代）；(c) 豆包工作 8 张过程截图**一次焦点都没借**
6. **agentskills.io 协议:** README 注明 "Agent Skills Protocol"——标准化 Skill 分发

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | macOS Computer Use Skill 层 + L0 自研通道 + 取证子系统；关键差异是"自研通道"（不调用云端 API）vs "云端 computer use" | 边界由 README 明示；具体 L0 通道的实现（bpy / CDP / Accessibility 封装）需代码审阅 |
| 主路径 | agent 触发 Skill → 选择 L0 通道（bpy / CDP / Accessibility）→ 模拟键盘鼠标输入 → `mac shot` 后台取证 → 每步对比目标 → 继续或回退 | 主路径为 README 语义抽象；具体每步对比的实现（视觉对比 / 状态对比）需 README 核验 |
| 关键权衡 | 自研通道的工程复杂度（vs 通用性）vs 数据本地化；后台取证的实时性（vs 抢焦点）；多 Runtime 兼容广度（vs 每个 Runtime 的适配深度） | README 列出三个真实案例；多 Runtime 适配深度的差异需 benchmark |
| 最小 PoC | macOS 安装 Skill → 在 Claude Code 触发 huashu-mac-use → "在 Blender 做一个巧克力甜甜圈" → 观察 bpy 通道执行 + 每步截图 → 检查"读后台"（不抢用户焦点） | PoC 范围由 README 案例推导；具体资源消耗（macOS Accessibility / Screen Recording 权限）需 benchmark |

## 架构启发
`huashu-mac-use` 的核心启发是 **"Computer Use 不一定要调用云端 API，可以走原生 SDK / 调试协议"**。传统 Computer Use（OpenAI Operator / Anthropic Computer Use）依赖云端截图 + 云端决策 + 云端输入模拟——数据上云、依赖网络、模型昂贵；`huashu-mac-use` 走 **"L0 通道 + 本地决策 + 原生输入"**——数据本地、离线可用、低成本。

更深层的启发是 **"Computer Use 的取证层"**——`mac shot` 后台截图 + 状态日志把 Computer Use 从"黑盒"升级到"白盒"——失败时能看到哪一步出错，每步可回放。

风险提示：**macOS 权限滥用是攻击面**——Accessibility / Screen Recording 权限一旦获取，理论上可监控用户所有操作；**computer use 的法律边界**——huashu-mac-use 操作原生 App 是否违反某些 App 的 EULA 需要逐个核验。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户] --> Agent[Agent<br/>Claude Code / Codex / Cursor / OpenClaw ...]
  Agent --> Skill[huashu-mac-use<br/>SKILL.md 触发]
  Skill --> Channel{选择 L0 通道}
  Channel -->|Blender| BPY[bpy 命令行<br/>3D 自动化]
  Channel -->|豆包工作| CDP[CDP<br/>内嵌 Chromium]
  Channel -->|系统/WPS| AX[macOS Accessibility API]
  BPY --> Input[模拟键盘鼠标<br/>原生输入]
  CDP --> Input
  AX --> Input
  Input --> App[原生 App<br/>Blender / 豆包 / 系统]
  App --> State[App 状态变化]
  State --> Shot[mac shot<br/>后台截图]
  Shot --> Compare[每步对比目标]
  Compare -->|通过| Continue[继续]
  Compare -->|失败| Retry[回退重试]
  Continue --> Shot
  Shot -.取证.-> Log[取证日志<br/>可复现]
  Skill -.agentskills.io.-> Standard[Agent Skills 协议]
  AX -.权限.-> Perm[Accessibility<br/>Screen Recording<br/>攻击面]
```

## 定位判断
**工具型项目（macOS Computer Use Skill + 每步取证），向"Computer Use Observability"演进。** `huashu-mac-use` 不仅是一个 Computer Use Skill，更是 Computer Use 从"云端闭源"到"本地开源 + 取证"模式的样本。2 天 181⭐ / fork/star 13.8% 已显示初步采用。当前定位是"macOS Computer Use Skill 头部样本"，向"Computer Use Observability Platform"演进是合理路径。

## 风险/局限/泡沫点
- **macOS 权限滥用:** Accessibility / Screen Recording 权限一旦获取，理论上可监控用户所有操作；权限滥用是攻击面
- **Computer use 的法律边界:** 操作原生 App 是否违反某些 App 的 EULA 需要逐个核验（如剪映 / WPS 等）
- **多 Runtime 适配深度:** 9 个 Runtime（Claude Code / Codex / Kimi Code / Cursor / OpenClaw / WorkBuddy / 豆包工作 / 千问办公 / ZCode）的兼容广度 vs 每个 Runtime 的适配深度需要测试
- **L0 通道的工程复杂度:** 自研 bpy / CDP / Accessibility 封装的维护成本高；macOS 版本升级可能 break
- **2 天新项目风险:** alchaincyf 是新 GitHub 账号，项目可持续性 / 治理结构未验证
- **取证日志的安全:** 截图 + 状态日志可能包含敏感数据（日志泄露是攻击面）

## 与同类项目的关系
- **vs OpenAI Operator:** Operator 是云端闭源 Computer Use；huashu-mac-use 是本地开源 + 取证
- **vs Anthropic Computer Use:** Computer Use 是 Claude API 能力；huashu-mac-use 是独立 Skill（多 Runtime）
- **vs wz1119/Codex-Minecraft-Gameplay (9-08, 126⭐):** Codex-Minecraft 是 Windows Computer Use；huashu-mac-use 是 macOS Computer Use——平台不同
- **vs OpenClaw:** OpenClaw 是 Agent Runtime；huashu-mac-use 是 Skill（可被 OpenClaw 加载）
- **vs vinzdg/codenotch (9-07, 667⭐):** codenotch 是 Coding Agent 用量 Monitor；huashu-mac-use 是 Computer Use Skill——监控 vs 执行

## 是否值得持续跟踪
**值得跟踪（macOS Computer Use Skill + 每步取证头部样本）。** `huashu-mac-use` 代表了 Computer Use 从"云端闭源"到"本地开源 + 取证"模式的方向，与 L0 自研通道 + 多 Runtime 兼容 + 2 天 181⭐ 共同构成新方向。建议关注：(a) macOS 权限滥用的治理；(b) Computer use 法律边界的演化；(c) 多 Runtime 适配深度的差异；(d) "Computer Use Observability Platform"是否成型。对 macOS 高级用户 / 创意工作者，huashu-mac-use 是数据本地化的 Computer Use 方案。

## 后续观察点
- macOS 权限滥用的治理（Accessibility / Screen Recording）
- Computer use 法律边界的演化（App EULA）
- 多 Runtime 适配深度的差异（9 个 Runtime 的实际表现）
- L0 通道的工程复杂度（macOS 版本升级兼容性）
- 取证日志的安全治理（日志泄露风险）
- "Computer Use Observability Platform"是否成型

---
> 数据来源: GitHub API (2026-09-08) | Stars: 181 | Forks: 25 | License: MIT | 语言: Swift | 创建: 2026-09-06
