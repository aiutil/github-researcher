# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-01）

**Coding agent 应用层从 harness 扩散为完整产品形态——qm 多人协作 agent harness（1.4K⭐/Slack+Web/每人独立沙箱）、cindy 开箱即用多 harness agent 客户端（1.3K⭐/Claude Code+Codex 混合驱动）、better-harness harness 工程化（1.3K⭐/loop engineering），harness 层从工具进化为多人协同平台 · 边缘推理边界推到极致——esp32-ai 在 8 美元 ESP32-S3 上跑 28.9M 参数 LLM（9.5 tok/s/Per-Layer Embeddings/flash 存储 25M 参数表），quill 全本地 macOS 会议录音转录（Parakeet TDT/系统音频+麦克风双轨），"把模型塞进最小内存"从 MoE 下沉到微控制器 · Kimi K3 生态延续增长（K3 7.5K→7.7K/AgentENV 2.6K→2.7K）**

今日热榜新信号：
- **yc-software/qm**（1,367 stars）：多人协作 agent harness for work，Slack + Web 双入口，每人独立沙箱/记忆/权限/技能，统一编排 Pi/OpenCode/Claude Code/Codex，面向初创团队的共享 agent 平台
- **slvDev/esp32-ai**（2,627 stars）：在 8 美元 ESP32-S3 微控制器上运行 28.9M 参数 LLM，用 Google Per-Layer Embeddings 把 25M 参数表存入 flash，每 token 仅读取 ~450B，实测 9.5 tok/s，完全离线
- **makecindy/cindy**（1,260 stars）：开箱即用的开源 AI agent 客户端（Electron+React Native），混合驱动 Claude Code/Codex，可在任务中途切换 harness×model 组合，本地运行用真实文件和已登录应用

**→ [查看 2026-08-01 完整简报](daily/2026-08-01.md)**
**→ [查看 2026-07-31 完整简报](daily/2026-07-31.md)**
**→ [查看 2026-07-30 完整简报](daily/2026-07-30.md)**
**→ [查看 2026-07-29 完整简报](daily/2026-07-29.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |
| [2026-07-28](daily/2026-07-28.md) | openclaw（384,378 stars） · hermes-agent（2 | 8 个深度分析 |
| [2026-07-27](daily/2026-07-27.md) | freeCodeCamp（453,008 stars） · openclaw（3 | 8 个深度分析 |
| [2026-07-26](daily/2026-07-26.md) | freeCodeCamp（453,008 stars） · react（246, | 8 个深度分析 |

---

## 当前最值得关注的趋势

1. **Coding agent 应用层产品化：从 harness 工具扩散为多人协作平台（qm）/开箱即用客户端（cindy）/harness 工程化（better-harness）**：相关项目 qm, cindy, better-harness。
2. **边缘推理边界推到极致：esp32-ai 在 8 美元 ESP32-S3 上跑 28.9M LLM（Per-Layer Embeddings/flash 存参数表/9.5 tok/s），quill 全本地 macOS 会议转录**：相关项目 esp32-ai, quill。
3. **Kimi K3 全栈生态延续增长：K3 7.5K→7.7K、AgentENV 2.6K→2.7K，注意力持续但增长斜率趋平**：相关项目 kimi-k3, agentenv, moonep。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [MoonshotAI/Kimi-K3](projects/kimi-k3.md) | 基础设施候选 | 首个开源 3T 级模型——2.8T 参数 MoE / 104B 激活，KDA + | 持续跟踪 |
| [DietrichGebert/ponytail](projects/ponytail.md) | 工具型 | 让 AI Agent 像最懒的资深工程师一样思考——YAGNI 极简主义 Ski | 持续跟踪 |
| [12-Factor Agents](projects/12-factor-agents.md) | 基础设施候选 | 构建足够好到可以交给专业用户使用的 LLM 驱动软件的 12 条工程原则，Age | 持续跟踪 |
| [codebase-memory-mcp](projects/codebase-memory-mcp.md) | 基础设施候选 | 高性能代码智能 MCP Server——用 tree-sitter 将代码库索引 | 持续跟踪 |
| [gstack](projects/garrytan-gstack.md) | 平台候选 | YC CEO Garry Tan 的 Claude Code 工具栈——23 个 | 持续跟踪 |
| [Graphify](projects/graphify.md) | 平台候选 | 跨 Agent 平台的 GraphRAG 编排 Skill，一次编写，7+ Ag | 持续跟踪 |
| [andrewyng/openworker](projects/openworker.md) | 平台候选 | Andrew Ng 出品的开源本地 AI Coworker——运行在你的桌面上， | 持续跟踪 |
| [Understand-Anything](projects/understand-anything.md) | 平台候选 | 将任意代码转换为交互式知识图谱，支持探索、搜索和问答，兼容 Claude Cod | 持续跟踪 |
| [NVIDIA OpenShell](projects/openshell.md) | 基础设施候选 | NVIDIA 出品的 Agent 安全运行时沙箱——Rust 实现，四层策略防御 | 持续跟踪 |
| [Agent-Reach](projects/agent-reach.md) | 基础设施候选 | AI Agent 的互联网感知层——一个 CLI 聚合 Twitter/Redd | 持续跟踪 |

---

## 数据统计

- 📊 项目档案：291 个
- 📅 日报总数：117 期
- 🔄 最近更新：2026-08-01

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
