# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-07.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-07

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 671 | 5 | 850k+ |

**今日核心判断：** Niko1221/Strata 13 天 15616⭐ ⑂1331 fork/star 8.5% 消费级显卡跑 Qwen3.8-Flash-Next 125B 模型——把「本地 LLM 推理」从「24GB H100 / 双卡 A100」推到「RTX 5070 / RX 9070 XT 12GB + Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度 24576 experts + guess-and-check 1.6-1.8x 加速 + OpenAI/Anthropic 兼容 /v1 + Claude Code ANTHROPIC_BASE_URL 直连 + 严肃工程化 MIT 一键启动脚本 START-HERE.bat / setup.sh + docs/{INSTALL,MODELS,DETAILS,HOW_IT_WORKS,TROUBLESHOOTING}.md + 多 GPU + 多 README 语言」严肃工程化形态 · NandhaKishorM/laya 19 天 31195⭐ ⑂2755 fork/star 8.8% Non-autoregressive System 1 决策引擎——把「LLM 分类 / 评分 / 决策」从「自回归逐 token 200ms+ + 闭源」嵌入「Laya 33ms 单次前向 typed decision（choice/score/noul）+ 100+ 语言 + Router 自动路由到 english/multilingual checkpoint + Python 3.10+ pip install laya + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] extras + TypeScript laya-ts/ + 12 个 Apache-2.0 / 严肃工程化」严肃工程化形态 · jaredpalmer/kev 20 天 8597⭐ ⑂563 fork/star 6.5% 自训 Jev-like System 1 决策模型族（Kev-0.8B/4B/9B/27B 基于 Qwen3.5/Qwen3.8 + noul/choice/score 共享模型 + 8192-65536 token 上下文 + MLX/CUDA + TypeSafe System One API drop-in + Modal 一键部署 + Apache-2.0） · storytold/photocraft 7 天 5857⭐ ⑂742 fork/star 12.7% Adobe Photoshop clean-room 纯 Rust 重实现——把「Adobe Photoshop in Rust」从「单 alpha 半成品」嵌入「Photocraft 完整 layer / mask / adjustment / type / vectors / brushes / 真实 PSD（307/309 psd-tools 测试）+ wgpu GPU compositor Metal/Vulkan/DX12/WebGPU + agent-ready command/CLI/JSON/MCP + MIT OR Apache-2.0 + Discord 社区」严肃工程化形态 · 延续跟踪 KKKKhazix/AIHOT 4050→6176⭐ 自托管热点站框架（TypeScript · MIT · 12367 KB · Docker Compose · PostgreSQL 17 · Node 24 · MCP + RSS/JSON/X/微信公众号 6 信源 + SelectBench + 中文日报 08:00 · 周报周一/月报每月 1 日）持续增长——5 条主线严肃工程化跨领域：（A Strata 消费级硬件跑 125B 模型 + GPU/CPU/RAM/SSD 分层调度 24576 experts + guess-and-check + 双 API 兼容 + 一键启动 + 多 README 语言）+（B Laya 33ms 非自回归 typed decision + 100+ 语言 + Router + Python/TypeScript 双绑定 + 7 extras 集成 langchain/llamaindex/crewai/MCP/ONNX/fast）+（C Kev 自训 Qwen3.5/Qwen3.8 Jev-like 决策模型族 + 4 个 size + MLX/CUDA + drop-in API + Modal 部署）+（D Photocraft Photoshop 完整 layer/mask/type/PSD 重实现 + wgpu GPU compositor + agent-ready 多接口 + MIT OR Apache-2.0 + Discord）+（E AIHOT 自托管热点站 6176⭐ 持续 + AIHOT 鉴权 / 评分 / 聚簇 / 热度 严肃工程化 + MCP / RSS / API / llms.txt 接入 Agent）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [Niko1221/Strata](projects/strata.md) | 15616 stars | 基础设施候选 |
| [NandhaKishorM/laya](projects/laya.md) | 31195 stars | 平台候选 |
| [jaredpalmer/kev](projects/kev.md) | 8597 stars | 工具型 |
| [storytold/photocraft](projects/photocraft.md) | 5857 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Niko1221/Strata 13 天 15616⭐ ⑂1331 fork/star 8.5% 把「本地 LLM 推理」从「24GB H100 / 双卡 A100 集群」推到「Strata 消费级显卡跑 Qwen3.8-Flash-Next 125B 模型——RTX 5070 / RX 9070 XT 12GB+ 一键 + Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度 24576 experts（每 token 用 10 个）+ VGPU + VRAM + RAM 持 24-55GB + SSD lookup + guess-and-check 1.6-1.8x 加速 + 8192 token 块读 1000+ tokens/s + OpenAI / Anthropic /v1 兼容 + Claude Code ANTHROPIC_BASE_URL 直连 + 一键启动脚本 START-HERE.bat / setup.sh + docs/{INSTALL,MODELS,DETAILS,HOW_IT_WORKS,TROUBLESHOOTING,MCP_SERVER,AI_SETUP,BATCHING,COMMUNITY_BENCHMARKS,OLDER_GPUS,INTEL_ARC,STRIX_HALO,MULTI_GPU}.md + 7 语言 README + 多 GPU 协调 + Coder/Swift 1.5/Unsloth UD-IQ4_XS/UD-Q4_K_XL/OrcaRouter Uncensored IQ3_XXS 模型 + buymeacoffee + 13 days 15616⭐ ⑂1331 fork/star 8.5% + C++ · 19115 + topics 0 覆盖」严肃工程化形态（趋势分 92）** · 相关项目：Niko1221/Strata · 强度：92
2. **NandhaKishorM/laya 19 天 31195⭐ ⑂2755 fork/star 8.8% 把「LLM 分类 / 评分 / 决策」从「自回归逐 token 200ms+ + 闭源」嵌入「Laya 33ms 单次前向 typed decision（choice/score/noul 三类型）+ 100+ 语言 + Router 自动路由到 english/multilingual checkpoint + Python 3.10+ pip install laya + laya[serve/mcp/langchain/llamaindex/crewai/onnx/fast] 7 extras + TypeScript laya-ts/ + npm install laya-ts + MLX 7-14ms Apple Silicon + TileLang GPU fast path + RLCD reinforcement learning against strictly proper scoring rules + 8192 token 多语言长文档 + laya-train CLI 从 CSV fine-tune + 严肃工程化」形态（趋势分 90）** · 相关项目：NandhaKishorM/laya · 强度：90
3. **jaredpalmer/kev 20 天 8597⭐ ⑂563 fork/star 6.5% 把「Jev 闭源决策模型 API」推到「Kev 自训 Jev-like System 1 决策模型族——基于 Qwen3.5 / Qwen3.8 + Kev-0.8B/4B/9B/27B 4 size + noul/choice/score 共享模型 + 8192 token 上下文（Kev-27B 65536 token）+ MLX Apple Silicon + CUDA + TypeSafe System One API drop-in（同一 Python SDK）+ Modal 一键部署 + frozen eval suites breadth-v1 14 数据集 + held-out 23.3-52.3 + Brier 分数 + 0.851 vs Jev 0.857 + Apache-2.0 + jaredpalmer 个人 + HF Spaces demo」严肃工程化形态（趋势分 84）** · 相关项目：jaredpalmer/kev · 强度：84
4. **storytold/photocraft 7 天 5857⭐ ⑂742 fork/star 12.7% 把「Adobe Photoshop 在 Rust 重实现」从「单 alpha 半成品」嵌入「Photocraft 完整 layer / mask / adjustment layer / type / vectors / brushes / 真实 PSD 文件（307/309 psd-tools 测试保留）+ wgpu GPU compositor Metal/Vulkan/DX12/WebGPU + copy-on-write tiles + 多线程 filter + 无 Electron 无 web view 启动 + 100% Rust + macOS/Windows/Linux/FreeBSD/Web-native + agent-ready command / CLI / JSON / MCP + MIT OR Apache-2.0 + Discord + getartcraft.com + 7 days 5857⭐ ⑂742 fork/star 12.7%」严肃工程化形态（趋势分 80）** · 相关项目：storytold/photocraft · 强度：80

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-07](daily/2026-10-07.md) | 4 | 5 |
| [2026-10-06](daily/2026-10-06.md) | 4 | 7 |
| [2026-10-05](daily/2026-10-05.md) | 4 | 4 |
| [2026-10-03](daily/2026-10-03.md) | 5 | 4 |
| [2026-10-01](daily/2026-10-01.md) | 5 | 4 |
| [2026-09-30](daily/2026-09-30.md) | 5 | 3 |
| [2026-09-29](daily/2026-09-29.md) | 5 | 3 |

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
