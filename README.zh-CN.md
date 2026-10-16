# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-17.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-17

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 719 | 4 | 1860k+ |

**今日核心判断：** chenglou/handwired 2 天 1523⭐ ⑂117 fork/star 7.7% 把「JavaScript → neural net」从「PyTorch/TF 重训 + 训练数据 + 不可微分支」推到「Turn your regular JavaScript code into a neural net; no training, exact, yet also fully differentiable + A program's made of if-else, loops, and state. Handwired transforms them into matrix multiplication + reglu over floats + Math.max(0, x) is ReLU + collect all + and * and relu into a giant matmul + either run it on JS or WebGPU + weights don't need training since they're written manually + existing GPU techniques (fusion, sparsity, reordering) optimize such minimal primitives + unfreezing the weights and train them + attaching a specific frozen program to a generic neural net and train end-to-end (nanoGPT + Shakespeare + your UI) + GPU-level parallelism in single-threaded JS (JSON search demo over 100k docs in milliseconds) + Bun + source starter + docs + lab + MIT」严肃工程化形态 · feder-cr/git-ai 2 天 1053⭐ ⑂110 fork/star 10.4% 把「AI agent 的 VCS」从「git clone + merge queue + client-side history walk + slow + single human」推到「Anthropic built Scion, a faster version control system for coding agents + I built gitai, an open-source version of that design + always-online clients fetch exactly what they need (ObjectService + graft clone + graft sparse) + source control as an API (history runs server-side + memoized as derived data) + landing without a merge queue (UserLand rebases a change onto current tip and lands with compare-and-swap; concurrent lands batched) + automatic conflict resolution (resolvers via versioned, vendor-neutral protocol; any LLM provider or deterministic tool or none) + changeset log + write-ahead log in SQLite or PostgreSQL + compare-and-swap per reference + packs in object storage (file, S3, GCS, Azure) + stateless servers any node can rebuild + graft-verify tests the tip, bisects and reverts the culprit + monitoring agents (superfans) + agent-friendly review (semantic approval rules) + agents as first-class users (per-agent tokens + RPC allowlist + branch policies) + started as fork of Gitaly (the GitLab Git RPC server) + Go + Linux + macOS + Go 1.26 + C + Meson + Ninja + MIT + vendor-neutral (server never calls a language model) + independent implementation」严肃工程化形态 · Tencent-Hunyuan/Hy-Memory 2 天 314⭐ ⑂30 fork/star 9.6% 把「LLM agent 的记忆」从「stateless chat + ad-hoc memory tricks + 多 agent 不共享 + 强 model 强 sweep」推到「Production-grade dual-system cognitive memory for LLM agents + hy-memory Python SDK (pip install hy-memory==2.0.2 includes ChromaDB and Kuzu + qdrant + faiss + graph + mysql + rerank + all extras) + three task scenes: hierarchical long-term cognitive memory for Chat (8-layer hierarchy: raw dialogues / atomic facts / summaries / schemas / prospective intentions + conflict reconciliation + cross-domain schema induction) + two-layer fact and reusable-experience memory for Working + version-evolution diff-chain tracking for Coding + MemHub: local-first desktop and CLI product that unifies conversation history and coding traces from user-authorized AI applications (Claude Code / Cursor / Codex / OpenCode / Qwen Code) into a single managed runtime and local data directory, enabling governed cross-application memory recall + open-sourced Hy-Memory-30B-A3B (Hugging Face) + technical report on attributed reinforcement learning for long-term memory writing (arXiv 2610.22196) + CMB: A Coding Memory Benchmark for Long-Horizon and Interleaved Coding Agents (ICLR 2027) + Memory Beyond Recall Dual-Process Cognitive Memory System for Self-Evolving LLM Agents accepted at EMNLP 2026 + Python + Apache-2.0」严肃工程化形态 · Leonxlnx/earshot 2 天 302⭐ ⑂19 fork/star 6.3% 把「coding agent 的听觉」从「Agent 看不到声音 + 录音依赖 + 无 quantitative critique + 无 self-iteration」推到「Ears for coding agents: let AI hear, review and make sound + CPU-only + open source + earshot turns sound into evidence an agent can reason about: what a file sounds like in words + how well it fits a description + the best moment inside a long recording + real recording or code-synthesized + second-by-second listening transcript of a whole film + annotated picture of it + scorecard against professional launch films + describe / match / rank / find / compare / ab / realness / timeline / sheet / critique / profile / measure / forge / llm / mcp / doctor 16 commands + earshot forge: make sounds in code (recipe of physical synthesis: modal resonators + contact excitations + filtered noise + computed room + microphone, no recorded audio) and improve them by listening (evolutionary search + critic scoring) + MCP server for Claude Code and other agents + Python + CLI + Python API + MIT」严肃工程化形态——四条主线同时推到 AI agent 感官/工作流的严肃工程化：(A chenglou/handwired JS 程序可微化 + WebGPU / Bun / single-thread JS → GPU-parallel + MIT + TypeScript)；(B feder-cr/git-ai Anthropic Scion 严肃工程化开源复刻 + server-centric VCS + merge queue 拆除 + changeset WAL + SQLite/PostgreSQL + compare-and-swap + object storage (file/S3/GCS/Azure) + stateless server + Gitaly fork + Go + vendor-neutral + MIT)；(C Tencent-Hunyuan/Hy-Memory LLM agent 双系统认知记忆 + 三场景 (Chat / Working / Coding) + 8 层 hierarchy + MemHub (local-first desktop + CLI across Claude Code / Cursor / Codex / OpenCode / Qwen Code) + Hy-Memory-30B-A3B + RL 记忆写入 + CMB benchmark + EMNLP 2026 + Apache-2.0)；(D Leonxlnx/earshot coding agent 听见 / 评 / 做声音 + CPU-only 16 commands + earshot forge 物理合成 + 进化搜索 + MCP + MIT)。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [chenglou/handwired](projects/handwired.md) | 1523 stars | 工具型 |
| [feder-cr/git-ai](projects/git-ai.md) | 1053 stars | 基础设施候选 |
| [Tencent-Hunyuan/Hy-Memory](projects/hy-memory.md) | 314 stars | 生产可用 |
| [Leonxlnx/earshot](projects/earshot.md) | 302 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **chenglou/handwired 2 天 1523⭐ ⑂117 fork/star 7.7% 把「JavaScript → neural net」从「PyTorch/TF 重训 + 训练数据 + 不可微分支」推到「Turn your regular JavaScript code into a neural net; no training, exact, yet also fully differentiable + program made of if-else + loops + state → matrix multiplication + relu over floats + collect +, *, relu into a giant matmul + either run on JS or WebGPU + weights don't need training since written manually + existing GPU techniques (fusion, sparsity, reordering) optimize such minimal primitives + unfreezing weights and train them + attaching a specific frozen program to a generic neural net and train end-to-end (nanoGPT + Shakespeare + your UI) + GPU-level parallelism in single-threaded JS (JSON search demo over 100k docs in milliseconds) + Bun + source starter + docs/ + lab/ + MIT」严肃工程化形态** · 相关项目：chenglou/handwired · 强度：92
2. **feder-cr/git-ai 2 天 1053⭐ ⑂110 fork/star 10.4% 把「AI agent 的 VCS」从「git clone + merge queue + client-side history walk + slow + single human」推到「Anthropic built Scion, a faster version control system for coding agents + I built gitai, an open-source version of that design + always-online clients fetch exactly what they need + source control as an API (server-side history + memoized as derived data) + landing without a merge queue (UserLand rebases onto current tip + compare-and-swap; concurrent lands batched) + automatic conflict resolution (resolvers via versioned, vendor-neutral protocol; any LLM provider or deterministic tool or none) + changeset log + write-ahead log in SQLite or PostgreSQL + compare-and-swap per reference + packs in object storage (file, S3, GCS, Azure) + stateless servers any node can rebuild + graft-verify tests the tip, bisects and reverts the culprit + monitoring agents (superfans) + agent-friendly review (semantic approval rules) + agents as first-class users (per-agent tokens + RPC allowlist + branch policies) + fork of Gitaly (GitLab Git RPC) + Go + Linux + macOS + Go 1.26 + C + Meson + Ninja + MIT + vendor-neutral (server never calls a language model) + independent implementation」严肃工程化形态** · 相关项目：feder-cr/git-ai · 强度：90
3. **Tencent-Hunyuan/Hy-Memory 2 天 314⭐ ⑂30 fork/star 9.6% 把「LLM agent 的记忆」从「stateless chat + ad-hoc memory tricks + 多 agent 不共享 + 强 model 强 sweep」推到「Production-grade dual-system cognitive memory for LLM agents + hy-memory Python SDK (pip install hy-memory==2.0.2 includes ChromaDB and Kuzu + qdrant + faiss + graph + mysql + rerank + all extras) + three task scenes: hierarchical long-term cognitive memory for Chat (8-layer hierarchy: raw dialogues / atomic facts / summaries / schemas / prospective intentions + conflict reconciliation + cross-domain schema induction) + two-layer fact and reusable-experience memory for Working + version-evolution diff-chain tracking for Coding + MemHub: local-first desktop and CLI product that unifies conversation history and coding traces from user-authorized AI applications (Claude Code / Cursor / Codex / OpenCode / Qwen Code) into a single managed runtime and local data directory, enabling governed cross-application memory recall + open-sourced Hy-Memory-30B-A3B (Hugging Face) + technical report on attributed reinforcement learning for long-term memory writing (arXiv 2610.22196) + CMB: A Coding Memory Benchmark for Long-Horizon and Interleaved Coding Agents (ICLR 2027) + Memory Beyond Recall Dual-Process Cognitive Memory System for Self-Evolving LLM Agents accepted at EMNLP 2026 + Python + Apache-2.0」严肃工程化形态** · 相关项目：Tencent-Hunyuan/Hy-Memory · 强度：87
4. **Leonxlnx/earshot 2 天 302⭐ ⑂19 fork/star 6.3% 把「coding agent 的听觉」从「Agent 看不到声音 + 录音依赖 + 无 quantitative critique + 无 self-iteration」推到「Ears for coding agents: let AI hear, review and make sound + CPU-only + open source + earshot turns sound into evidence an agent can reason about: what a file sounds like in words + how well it fits a description + the best moment inside a long recording + real recording or code-synthesized + second-by-second listening transcript of a whole film + annotated picture of it + scorecard against professional launch films + describe / match / rank / find / compare / ab / realness / timeline / sheet / critique / profile / measure / forge / llm / mcp / doctor 16 commands + earshot forge: make sounds in code (recipe of physical synthesis: modal resonators + contact excitations + filtered noise + computed room + microphone, no recorded audio) and improve them by listening (evolutionary search + critic scoring) + MCP server for Claude Code and other agents + Python + CLI + Python API + MIT」严肃工程化形态** · 相关项目：Leonxlnx/earshot · 强度：84

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-17](daily/2026-10-17.md) | 4 | 4 |
| [2026-10-16](daily/2026-10-16.md) | 4 | 4 |
| [2026-10-15](daily/2026-10-15.md) | 4 | 4 |
| [2026-10-14](daily/2026-10-14.md) | 4 | 4 |
| [2026-10-13](daily/2026-10-13.md) | 4 | 4 |
| [2026-10-12](daily/2026-10-12.md) | 5 | 5 |
| [2026-10-11](daily/2026-10-11.md) | 5 | 5 |

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
