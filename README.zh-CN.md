# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-03.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-03

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 658 | 4 | 11k+ |

**今日核心判断：** Meta 官方 Muse Gadget SDK（ESP32+Linux 设备 SDK 开源）+ iPhone USB-C 加速 Mac 本地 27B LLM 推理 + Mac/iPhone 联合 196k-229k 上下文 + BootLoops 1.0 严肃工程化 LLM 物理计算引擎 + 反检测/网页/桌面 GUI 三向 Agent 副驾——今日 facebookincubator/muse-gadget-sdk 1 天 819⭐ ⑂127 fork/star 15.5% 把 Meta Muse AI 项目的「开源设备 SDK」推到「ESP32 设备 SDK + Linux/Raspberry Pi 设备 SDK + 屏幕 / 音频 / 传感器 / 舵机全配 + Apache-2.0 + gadgets.muse.ai」严肃工程化形态（C · Apache-2.0 · 2482 KB · ESP32 Device SDK + Linux Device SDK + Waveshare 圆 AMOLED + M5Stack StickS3 + Muse Home Link + Raspberry Pi + Seeed reTerminal e-ink + off-the-shelf boards + screens / buttons / sensors / actuators + 设备 SDK 公开 + 商用清晰 + Not affiliated with Meta in any way + 「Built by hackers, for hackers」）；StayLameBro/backburner 2 天 215⭐ ⑂21 fork/star 9.8% 把本地 27B 推理从「纯 Mac 24GB 64k 上下文」推到「iPhone USB-C 10 Gb/s + Mac layers 1-40 + iPhone GPU layers 41-64 split prefill + 29-44% prefill 加速 16k-48k + 196k-229k 8-bit 上下文 + iPhone attention over old keys past 64k + llama.cpp fork + SME2 + Metal fusions + DFlash2 speculative decoding + 0.3-5s SSD prompt cache + MacBook Pro M4 Pro 24GB + iPhone 17 Pro Max A19 Pro」严肃工程化形态（Python · license 未明示 · 800 KB · llama.cpp fork StayLameBro/backburner-llama.cpp + ios/Backburner + scripts/proxy.py SSD prompt cache + bench/{turn-bench.py,session-bench.py} + 256/256 tokens greedy token-identical 8k/32k + 32/32 at 140k + 67-73 tok/s 8-bit 64k-96k + 59-68 tok/s Mac alone 4-bit + 128k 3/3 planted facts recalled + 12 omp tools + 26,849 tokens prompt）；BootLoops-ai/bootloops 2 天 203⭐ ⑂42 fork/star 20.7% 把 LLM 驱动严肃科学计算从「前端集成 Python 包」推到「BootLoops 1.0 certified computational tools + house engines for exact and high-precision scientific computing + Feynman integrals polylogarithmic/elliptic/K3/Calabi–Yau closed form/hundreds of certified digits + recurrences with certificates + Bayesian evidence integrals closed form + ball arithmetic proven error radius + exhaustive enumeration completeness certificates + open implementations of standard statistical procedures + Comprehensive field-specific codebases JaCKandJill/Mixalot/Terrier/Popcorn + 49 packages under tools/ + `python3 run_selftests.py --par 8` 一次性自检 + `python3 tools/landau-alphabet/test_landau_alphabet.py` Landau Alphabet 引擎 reference results 一分半钟复现 + plain-markdown skills 协议 + bootloops.ai」严肃工程化形态（Python · MIT · 8104 KB · bootloops skills separate repo + 49 packages + per-package GUIDE.md + acceptance gates + verification class + Landau Alphabet engine + 12-step protocols including「no unsupported claims, no filler, every quoted number traceable」+ related repos skills/JaCKandJill/BootLoops-ai）；blendi-remade/agentcraft 0 天 184⭐ ⑂23 fork/star 12.5% 把多 Agent coding 协作从「wall of terminal text」推到「Minecraft 26.3 studio 走来走去 + 6 个手绘角色 Marlow/Juniper/Kit/Wren/Rowan/Tove + Marlow 拆任务 + workers 各坐各 desk + 各 git worktree + 各 live monitor + Task Wall kanban + Library shared memory + podium 决策 + real diff merge review screen + 482 tests passing + Foreman 离线重连继续 + 实测 6 个 feature landed with tests passing + 安全 worktrees 不动 checkout + 不推送」严肃工程化形态（Java · MIT · 28737 KB · Minecraft 26.3 + Fabric + Claude Agent SDK + foreman/test + AgentCraft HQ golden hour + agents/<agent>/<task> 命名 + `<kbd>!</kbd>` bell + `<kbd>J</kbd>` + clay figurines + particles + nameplates + speech bubbles + real pathfinding）；whirlchat/whirl 1 天 240⭐ ⑂15 fork/star 6.3% 把 AI chat app 从「单 SaaS 闭源」推到「whirl.chat full-stack open source + Next.js 16 + Convex 后端 + Clerk auth + OpenRouter models + 100% MIT + apps/{v2,console,mobile,waitlist,remotion,legacy} + packages/backend + docs/{self-hosting,configuration,architecture}.md + every top model + living artifacts + MCP OAuth + long-term memory + live web search + locked chats 客户端加密 + incognito mode + message queueing + voice input + image generation + file attachments + folders + sharing」严肃工程化形态（TypeScript · MIT · 4631 KB · Anterra © + Bun workspaces + apps/v2 + admin console Vite + native Expo + remotion promo video + Convex database/functions/streaming/crons + Clerk + OpenRouter AI SDK + postcss no Tailwind `unused-keep` + waiting chat 多 model + adjustable thinking levels）。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [facebookincubator/muse-gadget-sdk](projects/facebookincubator-muse-gadget-sdk.md) | 819 stars | 基础设施候选 |
| [StayLameBro/backburner](projects/staylamebro-backburner.md) | 215 stars | 基础设施候选 |
| [BootLoops-ai/bootloops](projects/bootloops-ai-bootloops.md) | 203 stars | 基础设施候选 |
| [blendi-remade/agentcraft](projects/blendi-remade-agentcraft.md) | 184 stars | 工具型 |
| [whirlchat/whirl](projects/whirlchat-whirl.md) | 240 stars | 生产可用 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Meta 官方 Muse Gadget SDK 开源——facebookincubator/muse-gadget-sdk 1 天 819⭐ ⑂127 fork/star 15.5% 把 AI 项目的「开源设备 SDK」推到「ESP32 设备 SDK + Linux/Raspberry Pi 设备 SDK + 屏幕/音频/传感器/舵机全配 + Apache-2.0 + gadgets.muse.ai」严肃工程化形态（趋势分 92）** · 相关项目：facebookincubator/muse-gadget-sdk · 强度：92
2. **iPhone USB-C 加速 Mac 本地 27B LLM 推理 + 196k-229k 上下文——StayLameBro/backburner 2 天 215⭐ ⑂21 fork/star 9.8% split prefill layers 1-40 Mac + 41-64 iPhone GPU + 29-44% prefill 加速 + llama.cpp fork + SME2 + Metal fusions + DFlash2 speculative decoding + SSD prompt cache 0.3-5s（趋势分 88）** · 相关项目：StayLameBro/backburner · 强度：88
3. **BootLoops 1.0 严肃工程化 LLM 物理计算引擎——BootLoops-ai/bootloops 2 天 203⭐ ⑂42 fork/star 20.7% Feynman integrals polylogarithmic/elliptic/K3/Calabi-Yau + recurrences with certificates + Bayesian evidence closed form + ball arithmetic + 49 packages + plain-markdown skills 协议 + Landau Alphabet engine reference results（趋势分 85）** · 相关项目：BootLoops-ai/bootloops · 强度：85
4. **Minecraft 26.3 + 6 个手绘角色 + Marlow 拆任务 + workers 各 git worktree + 各 live monitor + podium 决策 + real diff merge review + Foreman 重连继续——blendi-remade/agentcraft 0 天 184⭐ ⑂23 fork/star 12.5% 严肃工程化多 Agent coding 协作跨工作流（趋势分 82）** · 相关项目：blendi-remade/agentcraft · 强度：82

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-03](daily/2026-10-03.md) | 5 | 4 |
| [2026-10-01](daily/2026-10-01.md) | 5 | 4 |
| [2026-09-30](daily/2026-09-30.md) | 5 | 3 |
| [2026-09-29](daily/2026-09-29.md) | 5 | 3 |
| [2026-09-28](daily/2026-09-28.md) | 5 | 3 |
| [2026-09-26](daily/2026-09-26.md) | 5 | 3 |
| [2026-09-25](daily/2026-09-25.md) | 5 | 3 |

## 为什么做这个项目

GitHub Trending 展示注意力，不等于长期价值。本项目记录带日期的仓库事实，阅读代码、文档和 Release，对比跨日变化，区分事实与推断，并保留 Benchmark 未复现、许可证变化或异常 Star 等风险。

## 研究工作流

```mermaid
flowchart LR
  A["采集公开仓库信号"] --> B["阅读代码、文档、Release 与元数据"]
  B --> C["对比跨日变化"]
  C --> D["判断价值与风险"]
  D --> E["发布日报"]
  E --> F["更新项目档案与趋势账本"]
```

- `daily/`：带来源快照的每日研究报告。
- `projects/`：可持续修订的项目档案。
- `indexes/`：跨项目、跨日期的趋势记录。
- `docs/`：生成后的公开站点。
- `scripts/generate_readme.py`：从已提交数据生成双语 README 和活动图表。

## 证据边界

Star、Fork、Release、许可证、语言与时间戳属于采集时可观察的 GitHub 事实；产品质量、架构意义、市场方向和疑似刷星属于研究判断。作者自述在独立复现前会明确标注，后续修正保留在带日期的记录里。

## 生成与验证

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

定时研究任务运行在 AIUtil 私有自动化环境中，Token、私有运行记忆和运营状态不进入仓库。

## 安全

请勿提交访问令牌、私有仓库内容、用户级活动数据或未经脱敏的运营记忆。安全问题请通过 [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new) 私下报告。

## 开源协议

Apache License 2.0，详见 [NOTICE](NOTICE)。
