---
title: "cranebeaker/coop-anything"
slug: "coop-anything"
date_added: "2026-10-18"
last_seen_date: "2026-10-18"
category: "工具型"
emoji: "🎮"
stars: "147 stars"
stars_delta: "2 天 147⭐"
language: "Python"
score: 82
tags: ["coop-anything","cranebeaker","single-player-to-coop","ai-agent-playbook","agents-md","mcp-server","claude-code","codex","gemini-cli","cursor","opencode","coop-research","coop-revive","coop-qa","coop-reverse-engineer","coop-build-from-zero","coop-networking","rea-mcp","steam-relay","no-port-forwarding","one-click-install","deus-ex-coop","fnv-coop","ocarina-coop","dungeon-keeper-coop","stalker-soc","stalker-cs","megamanx","megamanx4","pilotwings-64","zelda-oracle-of-seasons","python","mit"]
url: "https://github.com/cranebeaker/coop-anything"
---

# cranebeaker/coop-anything

## 一句话定位
cranebeaker 个人发布的 **AI agent 把单人大作变 co-op 的严肃工程化 Playbook**——`AGENTS.md + .agents/skills + .claude/skills + Coop Anything MCP server + 6 skills (coop-research / coop-revive / coop-qa / coop-reverse-engineer / coop-build-from-zero / coop-networking) + 配 REA MCP (逆向) + 自动测试 bot + one-click install + Steam relay no-port-forwarding + 6 mod 仓排队 + 4 社区 crate 进行`，Python + MIT。

## 它解决的问题
单人大作变 co-op 的痛点：无数 mod 死在 abandoned 状态、缺自动测试、缺朋友 host 时端口转发、缺 reverse engineering 工具链。**Deus Ex coop** 是个完成品，但独立作者只想"玩 Ocarina of Time / STALKER / Mega Man X / Pilotwings 64 / Fallout New Vegas / Dungeon Keeper 多人"——cranebeaker/coop-anything 直击：**agent 读 AGENTS.md + 选路径 1（完成现 mod）+ 路径 2（从零 reverse engineer）+ 自动测试 bot + Steam relay no-port-forwarding + 配 REA MCP 做逆向 + PR 回主仓**。这是 2026-Q4 严肃工程化 "AI 把单人大作变多人共玩" 路线的代表样本。

## 为什么值得关注（2026-10-18）
今日观察窗为 GitHub Search API 抓取时刻起、且截至 2026-10-18 仍在快速增长的新发现项目 + 延续跟踪项目。`cranebeaker/coop-anything` 2 天 147⭐ ⑂13 fork/star 8.8%——147⭐ + 6 mod 仓排队（Deus Ex / FNV / OoT / Dungeon Keeper / STALKER SoC / CS）+ 4 社区 crate 进行（Mega Man X / X4 / Pilotwings 64 / OoS）意味着社群已现雏形。**AGENTS.md + 6 skills + Co-op MCP + REA MCP + Steam relay + 自动测试**六要素打包成单一 Playbook 是稀缺差异化。

## 热度来源判断
coop-anything 的热度是 **"AGENTS.md + skills + MCP server + REA 配对 + 自动化 bot + Steam relay no-port-forwarding + multi-game 仓排队 + 社区贡献友好" 七要素共振**。
- AGENTS.md：agent 唯一入口文档
- 6 skills：每个 skill 单一职责
- Co-op MCP server：client SDK + engine detect + playbook read
- REA MCP 配对：reverse engineering 工具链
- Steam relay no-port-forwarding：朋友无需 port-forward
- 6 mod 仓：Deus Ex 已 released / OoT fully synced / 其余 in-progress
- 4 社区 crate 进行（Mega Man X / X4 / Pilotwings 64 / OoS）

热度**真实且社区网络效应已现雏形**——multi-game modding community 是经典强信号。

## 关键技术亮点
1. **AGENTS.md 主仓唯一入口**：与 Anthropic Skills 协议对齐，agent 读 AGENTS.md 知道该做什么
2. **.agents/skills + .claude/skills 双目录**：跨 harness 友好
3. **6 skills 一职一责**：coop-research / coop-revive / coop-qa / coop-reverse-engineer / coop-build-from-zero / coop-networking
4. **Co-op Anything MCP server**：检测 game engine + 读 playbook + 搜索 co-op directory + validate contributions
5. **REA MCP 配对**：npx rea-agents setup，逆向二进制
6. **路径 1（finish existing mod）**：coop-research（找最后一个 build + mine bug reports）+ coop-revive（audit code + fix）+ coop-qa（自动测试）
7. **路径 2（build from zero）**：coop-reverse-engineer（game + engine）+ coop-build-from-zero（hook + sync enemies/world/story/levels/saves）+ coop-qa
8. **路径 1 + 路径 2 收尾相同**：自动测试 bot in game + easy install + Steam relay + PR 回 coop-anything
9. **Steam relay no-port-forwarding**：朋友 Steam 客户端 → Coop relay → host machine
10. **One-click install**：朋友一键安装 + Steam join
11. **Deus Ex (released)**：完整完成 → cranebeaker/deus-ex-coop
12. **OoT (fully synced)**：Zelda Ocarina of Time mod，crane 同步 → cranebeaker/ocarina-coop
13. **FNV + Dungeon Keeper + STALKER SoC + STALKER CS**：in-progress
14. **Mega Man X + X4 (mstan/MegaManXSNESRecomp + MegaManX4Recomp)**：社区 crate，native PC with co-op netplay
15. **Pilotwings 64 (NoahVl/Birdman64)**：split-screen 社区 crate
16. **OoS (in progress)**：Zelda Oracle of Seasons 排队
17. **playbook/reviving-abandoned-mods.md + playbook/how-coop-mods-work.md + playbook/automated-qa.md + playbook/networking.md**：设计文档独立
18. **Claude Code + Codex + Gemini CLI + Cursor + OpenCode 通吃**：五家主流通用 coding agent

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 单仓 Playbook（AGENTS.md + 6 skills + Co-op Anything MCP server + README + playbook/*.md）+ 上游逆工程依赖 REA + 已有 6 个姊妹仓（Deus Ex / FNV / OoT / Dungeon Keeper / STALKER SoC / CS）+ 社区 crates（Mega Man X / X4 / Pilotwings 64）+ 进行中（OoS） | 基于 README「Quick start」+「Games being made co-op right now」+「from the community」 |
| 主路径 | user 说 "play X in co-op" → agent 读 AGENTS.md → Co-op MCP 搜目录与 engine → 选 path 1（coop-research + coop-revive + coop-qa）或 path 2（coop-reverse-engineer + coop-build-from-zero + coop-networking）→ 配 REA 做静态/动态分析 → 自动测试用 bot → Steam relay no-port-forwarding → one-click install → PR 回 coop-anything | 主路径由 README「How it works」表 +「Quick start」段推导；具体自动测试 bot 客户端怎么连与 Steam relay 拓扑（自建 / 用现成 relay）待核验 |
| 关键权衡 | Playbook 通用 vs 每个游戏得重写 engine adapter / REA 上游依赖 vs coop 主仓独立 / Steam relay 仅对好友 vs 公开互联网 / 已有 6 个 mod 上手速度 vs 路径 2 从零成本 / 1 day 攻击改游戏可行 vs 法律风险 | README 未列限制段；法律风险由 README 表述"point your AI agent at any single-player game" + Steam relay 段暗含 |
| 最小 PoC | 1. git clone + claude mcp add coop-anything -- python tools/mcp/coop_mcp.py → 2. 让 agent 选 path 2 处理 STALKER Clear Sky（README 在做）→ 看 AGENTS.md 是否按 README 流程推进 → 3. 引导 agent 调 REA 做 .pcap → 4. 对照 README「automated-qa」文档复现一次 PR | PoC 由 README Quick start +「Add the MCP server」段推导 |

## 架构启发
cranebeaker/coop-anything 的核心启发是 **"严肃工程化 AI 把单人大作变 co-op = AGENTS.md + 6 skills + Co-op MCP server + REA MCP 配对 + 自动化 bot + Steam relay no-port-forwarding + multi-game 排队"**。这是 2026-Q4 "AI agent 不只是 chat" 副线样本的稳定信号：Leonxlnx/earshot（earshot）+ mrsarac/ff-tracking（视频）+ LoreanXavier/pt-pc（P.T. 移植）+ LennyDuBois/leaderboard-auto-eval（评测）+ cranebeaker/coop-anything（co-op mod）。**AGENTS.md + SKILL.md 协议 + MCP server + 上游依赖 + 自动化测试 + 自动化分发**六位一体是稀缺差异化样本。

更深层的启发：**AI agent 把"死掉 mod"换成"由 agent 一遍流程重写到 PR"是 modding 社区的范式跃迁**——modding 作者不再是 hero，是 AGENTS.md 作者；agent 是工蜂，不是 mod 主。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[User: "I want to play X in co-op with my friends"]
  User --> Agent[Claude Code / Codex / Gemini CLI / Cursor / OpenCode agent]
  Agent --> AG[AGENTS.md 入口]
  AG --> CoopMCP[Co-op Anything MCP server<br/>claude mcp add coop-anything]
  CoopMCP --> Directory[搜 co-op directory<br/>检测 game engine<br/>读 playbook + skills]
  Directory --> Path1[Path 1: 完成现有 mod]
  Directory --> Path2[Path 2: 从零 reverse engineer]
  Path1 --> CoopRes[coop-research]
  Path1 --> CoopRev[coop-revive]
  Path1 --> CoopQA1[coop-qa]
  Path2 --> CoopRE[coop-reverse-engineer<br/>配 REA MCP npx rea-agents setup]
  Path2 --> CoopBuild[coop-build-from-zero]
  Path2 --> CoopNet[coop-networking]
  Path2 --> CoopQA2[coop-qa]
  CoopRev --> CodeEdit[Mod 仓库 audit + 修复代码]
  CoopRE --> .pcap[静态/动态分析 PCAP]
  CoopBuild --> Sync[同步 enemies/world/story/levels/saves]
  CoopNet --> SteamRelay[Steam relay no-port-forwarding<br/>自建 / 用现成 relay 待核验]
  CodeEdit --> AutoTest1[自动测试 bot in real game]
  Sync --> AutoTest2[自动测试 bot in real game]
  CoopQA1 --> AutoTest1
  CoopQA2 --> AutoTest2
  AutoTest1 --> OneClick1[One-click install + Steam join]
  AutoTest2 --> OneClick2[One-click install + Steam join]
  OneClick1 --> PR[PR 回 coop-anything 主仓]
  OneClick2 --> PR
  PR --> Released[Deus Ex released + OoT fully synced]
  PR -.in-progress.-> InProg[Deus Ex ✓ + FNV + OoT ✓ + Dungeon Keeper + STALKER SoC + CS]
  PR -.community.-> Comm[Mega Man X + X4<br/>Pilotwings 64<br/>OoS in progress]
```

## 定位判断
**工具型 / 平台候选型项目（AI-driven modding 平台）。** cranebeaker/coop-anything 是 2026-Q4 严肃工程化"AI 把单人大作变成多人共玩"路线的代表样本。**AGENTS.md + 6 skills + Co-op MCP server + REA MCP 配对 + 自动化 bot + Steam relay + multi-game 仓排队**七要素同时奉上是稀缺差异化。这与 Anthropic Skills 协议 + MCP 标准生态深耦合，是"AGENTS.md + skills 协议"的严肃工程化横向范例。

## 风险 / 局限 / 泡沫点
- **法律风险 / DRM / EULA / IP**："point your AI agent at any single-player game"+"Steam relay no-port-forwarding"在 anti-cheat 视角下是灰区；STALKER / Deus Ex / OoT / STALKER CS / Pilotwings 64 / Mega Man X4 / OoS 等 IP 法律位置含糊
- **路径 2 从零成本高**：从零 reverse engineer + hook in + sync enemies/world/story/levels/saves + handle saves 是数月工程，仅 Reddit/HackerNews"看到 PR 才上线"
- **REA MCP 上游依赖**：REA（Reverse Engineer Anything）的稳定性直接决定 coop-anything 路径 2 成功度
- **Steam relay 拓扑不明**：自建 / 用现成 relay / 第三方合作？README 未明示
- **Auto-test bot 客户端连接不明**：自动测试用"bot in real game"，bot 是否远程连真实游戏窗口？技术细节待核验
- **Multi-game engine 适配**：Unreal 1/2 / Source / id Tech / X-Ray / Mega Man / Birdman64 等不同引擎得重写 adapter
- **bus factor = cranebeaker 个人**：主仓 + 6 仓全部个人驱动
- **PR / merge 流程**：社区贡献友好，但 review 流程与 README + AGENTS.md 待核验

## 与同类项目的关系
- **vs Anthropic Skills + MCP 标准**：与 Anthropic Skills 协议深耦合，是该协议的严肃工程化横向范例
- **vs AkiKurisu/coop-mcp 上古 demo**：远不及 coop-anything 完整
- **vs Coop-mp / Co-op Commander**：独立作者项目，未到 coop-anything 规模
- **vs GooseMod / SKYNET 等 STALKER mod**：单一 mod，不通用
- **vs thommann/REStruct**：单一 RE tool，coop-anything 路径 2 配 REA MCP
- **vs Anthropic / OpenAI official AI-driven modding**：暂无竞品，coop-anything 抢先
- **vs LoreanXavier/pt-pc / mrsarac/ff-tracking (2026-10 同副线)**：同副线样本，但 coop-anything 是 Playbook 不是单一 mod

## 是否值得持续跟踪
**值得跟踪（AI-driven modding 平台候选）。** coop-anything 是 2026-Q4 严肃工程化 "AI 把单人大作变多人共玩" 路线的代表样本。建议关注：路径 2 完成度（STALKER CS 排队）、REA MCP 上游稳定性、Steam relay 拓扑 + anti-cheat 法律风险、Auto-test bot 真实连接、MCP + Skills 协议推进。

对 modder / 单人大作爱好者 / AGENTS.md 作者，这是值得仓库 review / fork 的项目；对 production 用户要谨慎法律风险。

## 后续观察点
- 6 仓（Deus Ex / FNV / OoT / Dungeon Keeper / STALKER SoC / CS）路径 2 完成度
- REA MCP 上游稳定性
- Steam relay 拓扑 + anti-cheat 法律风险
- Auto-test bot 真实连接机制
- Multi-game engine adapter 范式
- 与 Anthropic Skills + MCP 标准生态耦合深度
- 社区贡献 PR 流程
- 是否出现更多游戏 modding community 跟随（ex: Half-Life 2 / Quake / S.T.A.L.K.E.R. 2）

---
> 数据来源: GitHub API (2026-10-18) | Stars: 147 | Forks: 13 | License: MIT | 语言: Python | 创建: 2026-10-16 | Size: 237 KB | Topics: (README 未列 topics)
