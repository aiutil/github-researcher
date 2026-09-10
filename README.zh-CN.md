# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-11.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-11

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 8 | 569 | 7 | 12K+ |

**今日核心判断：** deepseek-ai/DeepSelect 1 天 232⭐ DeepSeek V3.2/V4/V4.1 TopK 内核（2-20× torch.topk 加速 · DSA · Lightning Indexer） · mizzlelover/gongwen-gbt9704-skill 2 天 301⭐ 中文公文 GB/T 9704-2012 排版 Skill（多 AI Harness · DOCX · fork/star 18.6%） · yudaprasetya007/routeVSCODE 1 天 326⭐ VSCode Copilot Chat Zero-Reload 模型切换本地代理（9Router · 40+ Provider） · kevinzakka/mjbatch 1 天 215⭐ MuJoCo CPU 并行仿真 Python 库（C++ thread pool · GIL 释放 · RL/MPC/SysID） · deepseek-ai/deepseek-recipe 1 天 209⭐ Rust 库把多种 API 格式统一转换到 DeepSeek V4.1 Conversation · Foadsf/vintage-latex 2 天 191⭐ 20 个复古科学论文 LuaLaTeX+MetaPost 示例 · viettranx/3dviz-pro-max 1 天 131⭐ Agent Skill Three.js/Blender 创意 3D 可视化（223 recipes · 440 knowledge · 37 runnable studies）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [deepseek-ai/DeepSelect](projects/deepselect.md) | 232 stars | 基础设施候选 |
| [mizzlelover/gongwen-gbt9704-skill](projects/gongwen-gbt9704-skill.md) | 301 stars | 工具型 |
| [yudaprasetya007/routeVSCODE](projects/routevscode.md) | 326 stars | 工具型 |
| [kevinzakka/mjbatch](projects/mjbatch.md) | 215 stars | 工具型 |
| [deepseek-ai/deepseek-recipe](projects/deepseek-recipe.md) | 209 stars | 基础设施候选 |
| [viettranx/3dviz-pro-max](projects/3dviz-pro-max.md) | 131 stars | 工具型 |
| [Foadsf/vintage-latex](projects/vintage-latex.md) | 191 stars | 工具型 |
| [Da7-Tech/SureForge](projects/sureforge.md) | 86 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **deepseek-official-kernel-release / DeepSeek 官方内核与 API 适配库同窗爆发——deepseek-ai/DeepSelect 1 天 232⭐（TopK kernel for DeepSeek Sparse Attention · V3.2/V4/V4.1 · bfloat16 / float32 · Lightning Indexer + Sampler · 2-20× torch.topk 加速 · benchmark 公开 · CUDA + MIT）+ deepseek-ai/deepseek-recipe 1 天 209⭐（Rust + Python bindings · 把 Messages / Chat Completions / Responses 多格式请求统一转换到 DeepSeek V4.1 Conversation · 推理后端无关）** · 相关项目：deepseek-ai/DeepSelect, deepseek-ai/deepseek-recipe · 强度：94
2. **chinese-formal-document-skill / 中文正式材料 Skill 首次标准化——mizzlelover/gongwen-gbt9704-skill 2 天 301⭐（GB/T 9704-2012 国标依据 · A4 + 版心 + 字体 + 标题层级 + 机构文号 + 页码 · 跨 Claude Code / Codex / OpenCode / Trae Code / Kimi / TraeWork / WorkBuddy / ZCode 8 Harness · fork 56 · fork/star 18.6% 高企服信号）** · 相关项目：mizzlelover/gongwen-gbt9704-skill · 强度：92
3. **zero-reload-copilot-model-router / VSCode Copilot Chat Zero-Reload 模型切换——yudaprasetya007/routeVSCODE 1 天 326⭐（9Router Gateway · Local Proxy Port 20129 · SSE 流式注入 · 40+ Provider · Live Model Comparison · Status Bar 切换 · Web Dashboard :5500 · MIT）** · 相关项目：yudaprasetya007/routeVSCODE · 强度：84
4. **robotics-mujoco-batch-cpu / MuJoCo CPU 并行仿真库——kevinzakka/mjbatch 1 天 215⭐（C++ thread pool + GIL 释放 · Batch(num_sims=4096) · set_const 重算 derived constants · 应用于 RL / MPC / SysID / hardware co-design · Go1 RL 在 5 年 M1 笔记本 < 1 min 学会行走 · Apache-2.0）** · 相关项目：kevinzakka/mjbatch · 强度：86

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-11](daily/2026-09-11.md) | 8 | 7 |
| [2026-09-09](daily/2026-09-09.md) | 10 | 7 |
| [2026-09-08](daily/2026-09-08.md) | 9 | 6 |
| [2026-09-07](daily/2026-09-07.md) | 10 | 6 |
| [2026-09-06](daily/2026-09-06.md) | 8 | 6 |
| [2026-09-05](daily/2026-09-05.md) | 10 | 7 |
| [2026-09-03](daily/2026-09-03.md) | 10 | 6 |

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
