# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-01.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-01

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 653 | 4 | 16k+ |

**今日核心判断：** 反检测 AI 浏览器底层 + 跨 NPU 高性能通信库 + 严肃工程化 PC 游戏 modding + 自托管 AI 热点网站持续扩张——今日 feder-cr/dots 2 天 1931⭐ ⑂320 fork/star 16.6% 推开「AI agent 自己带 Firefox 内核反检测浏览器」（patched Firefox C++ 内核 + One identity per seed + 屏幕 / 字体 / GPU / 时区语言同意 + No WebDriver 标志 / DevTools 协议 / automation globals + The pointer travels to what it clicks + 一只手一行键盘事件 + `--profile-dir` 持久登录 + `--proxy` 时区跟随出口 + OpenRouter `--model` 一键换模型 + uvx 一行启动 + 127.0.0.1:8765 左对话右浏览器 + `invisible_playwright_mcp` 给 Claude Code / Codex / Gemini CLI / 任何 MCP 客户端 + 全部 patches 在 C++ 内核 + MIT）严肃工程化形态；deepseek-ai/DeepEP-Ascend + DeepGEMM-Ascend 同日推到「Ascend NPU 高性能通信库 + Ascend GEMM kernel 公开」严肃工程化（DeepEP-Ascend：MoE dispatch/combine + FP8 dispatch + deferred epilogue + Pipeline / Context / Data Parallel Bucket collectives + Engram 远端内存 + HCCL/HCOMM/UBMEM/URMA + DeepJIT 运行时编译 + Ascend 950DT EP8 dispatch 373-375 GB/s + EP128 dispatch 313-320 GB/s 90-95% 物理带宽 + API 与 NVIDIA 版 DeepEP 对齐 + DeepGEMM-Ascend：完全 API 兼容 DeepGEMM + BF16/FP8/FP4 GEMM + MQA logits + MegaMoE + 稀疏数据加载 + 协程流水线 + 2026.09.30 Initial release for Ascend 950 + MIT）；rehan-remade/universal-modder 1 天 739⭐ ⑂48 fork/star 6.5% Claude Code plugin 把 PC 游戏 modding 推到「严肃工程化跨工作流」（`/plugin marketplace add rehan-remade/universal-modder` + Claude Code plugin + `mod-any-game` skill 包含 12 个 engine playbooks Unity/Unreal/.NET XNA (Terraria/Stardew/Celeste)/Godot/Source 1-2/Bethesda/Minecraft/AoE2/RE Engine/native C++/indie engines + `game-recon` 找引擎 + `reverse-engineering` ILSpy/Cpp2IL/Vineflower/Ghidra/IDA MCP/Cheat Engine/Frida/RenderDoc + `fal-assets` sprites/pixel art/seamless textures/PBR/image-to-3D/auto-rigging/SFX/music/voice/cutscene + `asset-pipeline` art→engine-exact frames + `game-automation` GPU-safe screenshot/windowed/crash-reporter cleanup + `showcase-video` GPU 录制 + 音频 process-loopback + `um scan/fal/sprite/render3d/win/video/backup/publish` Python CLI + 年龄卡 + 战术核弹 + 真实 Terra/AoE2 测试 + 25 MB 模型压缩 3-8 MB + MIT）；KKKKhazix/AIHOT 持续 3 日 4050⭐ ⑂1158 fork/star 28.6% 持续头部 + 同期 feder-cr/dots 共同把「反检测 / 自托管 / 严肃工程化 / MIT / 跨工作流」推到新高度。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [feder-cr/dots](projects/feder-cr-dots.md) | 1931 stars | 基础设施候选 |
| [deepseek-ai/DeepEP-Ascend](projects/deepseek-ai-deepep-ascend.md) | 180 stars | 基础设施候选 |
| [deepseek-ai/DeepGEMM-Ascend](projects/deepseek-ai-deepgemm-ascend.md) | 377 stars | 基础设施候选 |
| [rehan-remade/universal-modder](projects/rehan-remade-universal-modder.md) | 739 stars | 工具型 |
| [OpSafari/hypoarena](projects/op-safari-hypoarena.md) | 545 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **反检测 AI 浏览器底层 + stealth browser + One identity per seed——feder-cr/dots 2 天 1931⭐ ⑂320 fork/star 16.6% patched Firefox C++ 内核 + No WebDriver/DevTools/automation globals + `--proxy` 时区跟随出口 + `--model` 一键换模型 + uvx 一行启动 + 127.0.0.1:8765 左对话右浏览器 + `invisible_playwright_mcp` 给 Claude Code / Codex / Gemini CLI / 任何 MCP 客户端 + MIT（趋势分 90）** · 相关项目：feder-cr/dots · 强度：90
2. **Ascend NPU 高性能通信库 + DeepGEMM kernel 公开——deepseek-ai/DeepEP-Ascend 1 天 180⭐ ⑂15 + DeepGEMM-Ascend 2 天 377⭐ ⑂20 同日推到「Huawei Ascend 950 上 EP8 dispatch 373-375 GB/s + 90-95% 物理带宽 + API 与 NVIDIA 版 DeepEP 对齐 + 完全 API 兼容 DeepGEMM + BF16/FP8/FP4/MQA logits/MegaMoE + DeepJIT 运行时编译 + Ascend C kernels」严肃工程化形态（趋势分 84）** · 相关项目：deepseek-ai/DeepEP-Ascend, deepseek-ai/DeepGEMM-Ascend · 强度：84
3. **严肃工程化 PC 游戏 modding 跨工作流——rehan-remade/universal-modder 1 天 739⭐ ⑂48 fork/star 6.5% Claude Code plugin + 12 个 engine playbooks + ILSpy/Cpp2IL/Ghidra/IDA/Cheat Engine/Frida/RenderDoc + fal assets MCP + sprite/render3d/win/video Python CLI + `mod-any-game` skill + 真实 Terra/AoE2 测试（趋势分 82）** · 相关项目：rehan-remade/universal-modder · 强度：82
4. **科学假设发现工作台 + AI co-scientist 推到「全离线」严肃工程化——OpSafari/hypoarena 1 天 545⭐ ⑂28 fork/star 5.1% generate–debate–evolve loop + 引用支承的假设 / 证据图 + 合成文献工厂 + span-level grounding verification + pluggable agent adapters + Bradley-Terry / Elo tournaments + MinHash LSH paraphrase dedup + Bayesian evidence accumulation + NumPy core + CPU-only torch extra + `hypoarena demo` 端到端离线跑（趋势分 80）** · 相关项目：OpSafari/hypoarena · 强度：80

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-01](daily/2026-10-01.md) | 5 | 4 |
| [2026-09-30](daily/2026-09-30.md) | 5 | 3 |
| [2026-09-29](daily/2026-09-29.md) | 5 | 3 |
| [2026-09-28](daily/2026-09-28.md) | 5 | 3 |
| [2026-09-26](daily/2026-09-26.md) | 5 | 3 |
| [2026-09-25](daily/2026-09-25.md) | 5 | 3 |
| [2026-09-24](daily/2026-09-24.md) | 5 | 3 |

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
