# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-19.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-19

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 610 | 3 | 10k+ |

**今日核心判断：** eliasstravik/herdr-projects 1 天 140⭐ ⑂4 协调器对话 + 并行 worker 线程 Coding Agent 项目编排（Rust · MIT · Herdr 0.9.1+ 插件 · 协调器永不亲自干活始终保持可对话 · 每个任务一个独立 agent 跑在自己 git worktree + 分支 · 所有线程共享同一份指令 + 项目级 memory · 侧栏按 ready-for-review / waiting-on-you / working / landing / idle 五组聚合 · threads 状态 ticker 跟 PR + 例行 routine · 自托管 macOS / Linux · 无 hosted service · 与昨日 thruwire/foreman「Jev 软件工厂监管层」同构 AI Coding Agent 多 loop 工程化但推到「多 worker 线程并行 + 协调器只做路由 + 项目级 memory 共享」用户决策侧最高抽象）· indada/repopilot 1 天 95⭐ ⑂6 验证驱动 AI 软件迭代引擎（TypeScript · MIT · OpenAI Codex SDK + 自托管 worker · GitHub Issue / PR → 需求驱动测试生成 → 失败复现 → 代码修复 → 独立 Docker runner 验证 → 维护者保留 merge 决策 · 修复前冻结测试 · 候选必须保留测试身份 + 通过独立执行 + 通过 policy 重检 · 环境失败有界重试 · 不稳定证据阻断自动修复 · JSON / Markdown 报告本地保留 findings + test outcomes + repair attempts + publication state · AGENTS.md 项目规约静态规则 + Codex 语义审查 + 引用规则 + 代码证据 · 378 KB · 与昨日 thruwire/foreman「Jev supervisor」同构但推到「Codex SDK 直接做工程迭代 + 独立验证器」领域 · 与昨日 clawback/claude-code-cost-ledger「session 层成本治理」同构但推到「仓库级 Issue / PR 验证迭代闭环」领域）· LingxiangXu/traceclause 1 天 58⭐ ⑂4 本地优先需求文档证据审查工作台（Python · MIT · 3.11+ · FastAPI · SQLite · 文本 PDF/DOCX/UTF-8 TXT/Markdown 导入 · PDF 页引用 + DOCX 段落/表行引用 + 文本行引用 · 原文件字节 SHA-256 指纹 + 精确需求引用偏移 · 中文 bigram + 英文 word BM25 检索至多 3 候选 + 共享术语 + 词覆盖 · 候选 / 可能冲突 / 缺失证据三类提示 · 数字差异触发复核提醒 · 人类审查选定源段 + 书面理由 + 变更历史 · Markdown / CSV / JSON 三格式导出 · 不需 model API key · 文档内容不外发 AI · 与昨日 skill-lab/feishu-chat-archive「中国云办公 API 反 SaaS 编排」同构但推到「本地需求文档 + 反 SaaS 证据审查」领域 · 与昨日 NiazMorshed2007/jev-review「本地优先 MCP 软件质量评估」同构但推到「本地优先文档证据审查」合规证据链领域）· CYBERVERSE-Research/skyline-speeder 1 天 33⭐ ⑂4 发送端 eBPF struct_ops TCP 拥塞控制（Python + Rust · GPL-2.0 · kernel 6.12 LTS+ · Debian / Ubuntu · 4 件套 skyline_cc eBPF struct_ops + skyline_policy cgroup sockops + skyline_tc TC egress + skyline-speederd / ssctl Rust userspace · 仅部署发送端客户端零改造 · 目标 10-20% 丢包 + 100-300 ms RTT 长单向流 · 假设丢包不带拥塞信息 · CUBIC 0.05-0.31 vs BBR 3-84 vs Skyline 79-95 Mbit/s 九宫格 +13% ~ +26.8x · 守卫项失活场景 < 0.01% 偏差 · RTO ceiling 防 101s 退避 · 297 KB · 与昨日 arvindear/wp2shell-PoC「RCE 链 PoC」同构但推到「网络栈层 eBPF 加速」基础设施领域 · 与昨日 thruwire/foreman「快决策 / 慢生成分层」同构但推到「网络栈层快路径 / 慢回退分层」基础设施领域）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [eliasstravik/herdr-projects](projects/herdr-projects.md) | 140 stars | 基础设施候选 |
| [indada/repopilot](projects/repopilot.md) | 95 stars | 工具型 |
| [LingxiangXu/traceclause](projects/traceclause.md) | 58 stars | 工具型 |
| [CYBERVERSE-Research/skyline-speeder](projects/skyline-speeder.md) | 33 stars | 基础设施候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **协调器对话 + 并行 worker 线程 Coding Agent 项目编排——eliasstravik/herdr-projects 1 天 140⭐ ⑂4（Rust · MIT · Herdr 0.9.1+ 插件 · 协调器永不亲自干活始终保持可对话 · 每个任务一个独立 agent 跑在自己 git worktree + 分支 · 所有线程共享同一份指令 + 项目级 memory · 侧栏按 ready-for-review / waiting-on-you / working / landing / idle 五组聚合 · threads 状态 ticker 跟 PR + 例行 routine · lessons under `## Remember` 流回 memory 给下一个 thread · 自托管 macOS / Linux · 无 hosted service · 不需要预装 Node.js · 与昨日 thruwire/foreman「Jev supervisor 双 loop 并行」同构但推到「多 worker 线程并行 + 协调器只做路由 + 项目级 memory 共享」用户决策侧最高抽象 · 同一指令同一 memory 跨线程是「agent 上下文复用」的工程化形式 · 对比 cloud projects 产品保持自托管 + 免费 + 适配现有 agent CLI）** · 相关项目：eliasstravik/herdr-projects · 强度：88
2. **验证驱动 AI 软件迭代引擎——indada/repopilot 1 天 95⭐ ⑂6（TypeScript · MIT · OpenAI Codex SDK + 自托管 worker · GitHub Issue / PR → 需求驱动测试生成 → 失败复现 → 代码修复 → 独立 Docker runner 验证 → 维护者保留 merge 决策 · 修复前冻结测试 · 候选必须保留测试身份 + 通过独立执行 + 通过 policy 重检 · 环境失败有界重试 · 不稳定证据阻断自动修复 · JSON / Markdown 报告本地保留 findings + test outcomes + repair attempts + publication state · AGENTS.md 项目规约静态规则 + Codex 语义审查 + 引用规则 + 代码证据 · 与昨日 thruwire/foreman「Jev supervisor」同构 AI Coding Agent 多 loop 工程化但推到「Codex SDK 直接做工程迭代 + 独立验证器」领域 · 与昨日 clawback/claude-code-cost-ledger「session 层成本治理」同构但推到「仓库级 Issue / PR 验证迭代闭环」领域 · 与昨日 thruwire/foreman「verifier 是另一个 Codex worker」同构但推到「verifier 是独立 Docker runner + 维护者最终 merge gate」多 harness 治理）** · 相关项目：indada/repopilot · 强度：86
3. **本地优先需求文档证据审查工作台——LingxiangXu/traceclause 1 天 58⭐ ⑂4（Python · MIT · 3.11+ · FastAPI · SQLite · 文本 PDF / DOCX / UTF-8 TXT / Markdown 导入 · PDF 页引用 + DOCX 段落 / 表行引用 + 文本行引用 · 原文件字节 SHA-256 指纹 + 精确需求引用偏移 · 中文 bigram + 英文 word BM25 检索至多 3 候选 + 共享术语 + 词覆盖 · 候选 / 可能冲突 / 缺失证据三类提示 · 数字差异触发复核提醒 · 人类审查选定源段 + 书面理由 + 变更历史 · Markdown / CSV / JSON 三格式导出 · 不需 model API key · 文档内容不外发 AI · 与昨日 skill-lab/feishu-chat-archive「中国云办公 API 反 SaaS 编排」同构但推到「本地需求文档 + 反 SaaS 证据审查」领域 · 与昨日 NiazMorshed2007/jev-review「本地优先 MCP 软件质量评估」同构但推到「本地优先文档证据审查」合规证据链领域 · 10 MB 单文件 + 200 PDF 页 + 5000 抽取块 + 50 万字符 + 500 需求上限）** · 相关项目：LingxiangXu/traceclause · 强度：82
4. **发送端 eBPF struct_ops TCP 拥塞控制——CYBERVERSE-Research/skyline-speeder 1 天 33⭐ ⑂4（Python + Rust · GPL-2.0 · kernel 6.12 LTS+ · Debian / Ubuntu · 4 件套 skyline_cc eBPF struct_ops 拥塞控制 + skyline_policy cgroup sockops 早期丢包观察 + skyline_tc TC egress DSCP 标记 + skyline-speederd / ssctl Rust userspace 驻留控制面 · 仅部署发送端客户端零改造 · 目标 10-20% 丢包 + 100-300 ms RTT 长单向流 · 假设丢包不带拥塞信息 · CUBIC 0.05-0.31 vs BBR 3-84 vs Skyline 79-95 Mbit/s 九宫格 +13% ~ +26.8x · 守卫项失活场景 < 0.01% 偏差 · RTO ceiling 防 101s 退避 · 与昨日 arvindear/wp2shell-PoC「RCE 链 PoC」同构基础设施领域但推到「网络栈层 eBPF 加速」领域 · 与昨日 thruwire/foreman「快决策 / 慢生成分层」同构分层思想但推到「网络栈层快路径 / 慢回退分层」基础设施领域 · 与昨日 chaseleantj/desktop-habitats「macOS 菜单栏 + Three.js 桌面生态」同构 macOS 桌面应用层但推到「Linux 服务器网络栈层」）** · 相关项目：CYBERVERSE-Research/skyline-speeder · 强度：78

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-19](daily/2026-09-19.md) | 4 | 3 |
| [2026-09-18](daily/2026-09-18.md) | 5 | 3 |
| [2026-09-17](daily/2026-09-17.md) | 5 | 5 |
| [2026-09-16](daily/2026-09-16.md) | 5 | 4 |
| [2026-09-15](daily/2026-09-15.md) | 5 | 4 |
| [2026-09-14](daily/2026-09-14.md) | 4 | 4 |
| [2026-09-13](daily/2026-09-13.md) | 6 | 4 |

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
