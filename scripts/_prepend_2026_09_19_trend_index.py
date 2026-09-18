#!/usr/bin/env python3
"""Prepend 2026-09-19 section to indexes/trend-index.md (newest first, after frontmatter)."""
from pathlib import Path
import re

p = Path("indexes/trend-index.md")
text = p.read_text(encoding="utf-8")

# Update last_updated in frontmatter
text = re.sub(
    r"(last_updated: ')\d{4}-\d{2}-\d{2}(')",
    r"\g<1>2026-09-19\g<2>",
    text,
    count=1,
)

# Idempotency
if "## 2026-09-19" in text:
    print("OK (idempotent: today's section already present, skipping)")
    raise SystemExit(0)

# Find end of frontmatter
lines = text.split("\n")
fm_end = 0
for i, l in enumerate(lines):
    if i > 0 and l.strip() == "---":
        fm_end = i + 1
        break

new_section = """

## 2026-09-19

### eliasstravik/herdr-projects（140 stars · fork 4）· indada/repopilot（95 stars · fork 6）· LingxiangXu/traceclause（58 stars · fork 4）· CYBERVERSE-Research/skyline-speeder（33 stars · fork 4）

> 证据边界：项目名称、星标、tags、description、license、size、forks 来自 2026-09-19 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license / size）+ 各项目 README 公开摘录（API readme 字段 base64 解码）。"X 天 Y⭐"基于 created_at→2026-09-19 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**今日观察窗为 2026-09-18 创建且截至 2026-09-19 仍在快速增长的 4 个非游戏类高质量工程型项目**；09-19 当日新创仓库在 GitHub API 暴露窗口 < 12 小时，本批重点放在 09-18 创建且仍持续增长的项目。**今日最大事件是 `eliasstravik/herdr-projects` 1 天 140⭐ / fork 4 / fork/star 2.9% — Herdr 协调器对话 + 并行 worker 线程 Coding Agent 项目编排**——把「一个协调器对话 + 多个 worker 线程各跑各的 git worktree + 分支 + 共享指令与项目级 memory」做成 Herdr 0.9.1+ 的 Rust 插件；协调器永不亲自干活永远可对话，5 组 sidebar（ready-for-review / waiting-on-you / working / landing / idle）聚合线程状态；lessons under `## Remember` 流回 memory 给下一个 thread；自托管 macOS / Linux 无 hosted service；不需预装 Node.js；MIT + Rust + 151 KB 是「可独立部署的最小多 agent 项目编排内核」形态。**今日 4 个项目分两条主线**：**A. 多 agent 协作 + 验证治理**（herdr-projects 协调器线程 + repopilot 验证驱动迭代）——把昨日 thruwire/foreman「Jev supervisor 双 loop」的「监管不打断生成」思路推到「用户决策不打断 worker」+「独立 Docker verifier 守最后一道门」；**B. 本地优先 + 证据可核验**（traceclause 文档证据审查 + skyline-speeder 网络栈可复现加速）——把昨日 NiazMorshed2007/jev-review「本地优先 + 无 backend / database / telemetry / proxy」推到「文档内容不外发 AI + SHA-256 指纹 + SQLite 持久化」+「eBPF kernel-level 加速 + 可复现基准 + GPL-2.0 严肃许可」；**与昨日「TypeSafe Jev 决策模型生态爆发」不同**，今日没有 Jev 标签强信号（cobanov/awesome-jev / fatwang2/awesome-jev / kyotofin/tax-doc-classifier / wy-coliney/jev-browser-use / mrnugget/jev-shell-history / featherless-ai/simple-jev / razorback16/openjev / obie/ruby_decision_model / yusukebe/hono-jev-router / RafalWilinski/vibecheck / zeredy879/minojev 仍在长但单点星数已不及 100⭐）——意味着 Jev 生态从 09-18 的「单日爆发」回到「持续填充 + 横向应用」正常节奏，**真正的今日主线是「多 agent 编排 + 验证治理」+「本地优先证据可核验」两条非 Jev 主线**。

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|---:|---|---|---:|
| 1 | herdr-coordinator-threads / Herdr 协调器对话 + 并行 worker 线程 Coding Agent 项目编排——eliasstravik/herdr-projects 1 天 140⭐ ⑂4 fork/star 2.9%（Rust · MIT · Herdr 0.9.1+ 插件 · 协调器永不亲自干活永远可对话 · 每个任务一个独立 agent 跑在自己 git worktree + 分支 · 所有线程共享同一份指令 + 项目级 memory · 侧栏按 ready-for-review / waiting-on-you / working / landing / idle 五组聚合 · 卡权限 > 30 秒自动 waiting-on-you · lessons under `## Remember` 流回 memory 给下一个 thread · threads 状态 ticker 跟 PR + 例行 routine · 自托管 macOS / Linux · 无 hosted service · 不需预装 Node.js · 151 KB repo · 与昨日 thruwire/foreman「Jev supervisor」同构 AI Coding Agent 多 loop 工程化但推到「多 worker 线程并行 + 协调器只做路由 + 项目级 memory 共享」用户决策侧最高抽象 · 同一指令同一 memory 跨线程是「agent 上下文复用」的工程化形式 · 9 项对比表 8 项 ✅ 仅「Runs with no machine of yours switched on」❌ vs cloud projects products） | eliasstravik/herdr-projects | 88 |
| 2 | verification-driven-iteration / 验证驱动 AI 软件迭代引擎——indada/repopilot 1 天 95⭐ ⑂6 fork/star 6.3%（TypeScript · MIT · OpenAI Codex SDK + 自托管 worker · GitHub Issue / PR → 需求驱动测试生成 → 失败复现 → 代码修复 → 独立 Docker runner 验证 → 维护者保留 merge 决策 · 修复前冻结测试 · 候选必须保留测试身份 + 通过独立执行 + 通过 policy 重检 · 环境失败有界重试 · 不稳定证据阻断自动修复 · JSON / Markdown 报告本地保留 findings + test outcomes + repair attempts + publication state · AGENTS.md 项目规约静态规则 + Codex 语义审查 + 引用规则 + 代码证据 · 双语 README 英文 + 中文 · 378 KB repo · 与昨日 thruwire/foreman「Jev supervisor」同构多 loop 工程化但推到「Codex SDK 直接做工程迭代 + 独立 Docker verifier」领域 · 与前日 clawback/claude-code-cost-ledger「session 层成本治理」同构但推到「仓库级 Issue / PR 验证迭代闭环」领域） | indada/repopilot | 86 |
| 3 | local-first-doc-evidence-workbench / 本地优先需求文档证据审查工作台——LingxiangXu/traceclause 1 天 58⭐ ⑂4 fork/star 6.9%（Python · MIT · 3.11+ · FastAPI · SQLite · 文本 PDF / DOCX / UTF-8 TXT / Markdown 导入 · PDF 页引用 + DOCX 段落 / 表行引用 + 文本行引用 · 原文件字节 SHA-256 指纹 + 精确需求引用偏移 · 中文 bigram + 英文 word BM25 检索至多 3 候选 + 共享术语 + 词覆盖 · 候选 / 可能冲突 / 缺失证据三类提示 · 数字差异触发复核提醒 · 人类审查选定源段 + 书面理由 + 变更历史 · Markdown / CSV / JSON 三格式导出 · 不需 model API key · 文档内容不外发 AI · 大小上限 10 MB / 文件 + 200 PDF 页 + 5000 抽取块 + 50 万字符 + 500 需求 / 任务 · 98 KB repo · 与前日 skill-lab/feishu-chat-archive「中国云办公 API 反 SaaS 编排」同构但推到「本地需求文档 + 反 SaaS 证据审查」领域 · 与昨日 NiazMorshed2007/jev-review「本地优先 MCP 软件质量评估」同构但推到「本地优先文档证据审查」合规证据链领域） | LingxiangXu/traceclause | 82 |
| 4 | sender-side-ebpf-tcp-congestion-control / 发送端 eBPF struct_ops TCP 拥塞控制——CYBERVERSE-Research/skyline-speeder 1 天 33⭐ ⑂4 fork/star 12.1%（Python + Rust · GPL-2.0 · kernel 6.12 LTS+ · Debian / Ubuntu · eBPF CO-RE struct_ops · 4 件套 skyline_cc eBPF struct_ops 拥塞控制 + skyline_policy cgroup sockops 早期丢包观察 + skyline_tc TC egress DSCP 标记 + skyline-speederd / ssctl Rust userspace 驻留控制面 · 仅部署发送端客户端零改造 · 目标 10-20% 丢包 + 100-300 ms RTT 长单向流 · 假设丢包不带拥塞信息 · 仅识别两个真拥塞信号 队列延迟 + ECN marks · CUBIC 0.05-0.31 vs BBR 3-84 vs Skyline 79-95 Mbit/s 九宫格 +13% ~ +26.8x · 守卫项失活场景 < 0.01% 偏差 · RTO ceiling 防 101s 退避 · 双语 README 英文 + 简体中文 · 297 KB repo · 与昨日 arvindear/wp2shell-PoC「RCE 链 PoC」同构基础设施领域但推到「网络栈层 eBPF 加速」领域） | CYBERVERSE-Research/skyline-speeder | 78 |

#### 当日重点项目

- 🐑 eliasstravik/herdr-projects (1 天 140⭐ ⑂4) — Herdr 协调器对话 + 并行 worker 线程 Coding Agent 项目编排；Rust · MIT · Herdr 0.9.1+ 插件；协调器永不亲自干活永远可对话；每个任务一个独立 agent 跑在自己 git worktree + 分支；所有线程共享同一份指令 + 项目级 memory；侧栏按 ready-for-review / waiting-on-you / working / landing / idle 五组聚合；卡权限 > 30 秒自动 waiting-on-you；lessons under `## Remember` 流回 memory 给下一个 thread；threads 状态 ticker 跟 PR + 例行 routine；自托管 macOS / Linux；无 hosted service；不需预装 Node.js；151 KB，fork/star 2.9%，Score 88
- 🛩️ indada/repopilot (1 天 95⭐ ⑂6) — 验证驱动 AI 软件迭代引擎；TypeScript · MIT · OpenAI Codex SDK + 自托管 worker；GitHub Issue / PR → 需求驱动测试生成 → 失败复现 → 代码修复 → 独立 Docker runner 验证 → 维护者保留 merge 决策；修复前冻结测试；候选必须保留测试身份 + 通过独立执行 + 通过 policy 重检；环境失败有界重试；不稳定证据阻断自动修复；JSON / Markdown 报告本地保留；AGENTS.md 项目规约静态规则 + Codex 语义审查；双语 README；378 KB，fork/star 6.3%，Score 86
- 📜 LingxiangXu/traceclause (1 天 58⭐ ⑂4) — 本地优先需求文档证据审查工作台；Python 3.11+ · MIT · FastAPI · SQLite；文本 PDF / DOCX / UTF-8 TXT / Markdown 导入；PDF 页引用 + DOCX 段落 / 表行引用 + 文本行引用；原文件字节 SHA-256 指纹 + 精确需求引用偏移；中文 bigram + 英文 word BM25 检索至多 3 候选；候选 / 可能冲突 / 缺失证据三类提示；数字差异触发复核提醒；人类审查选定源段 + 书面理由 + 变更历史；Markdown / CSV / JSON 三格式导出；不需 model API key；文档内容不外发 AI；98 KB，fork/star 6.9%，Score 82
- 🛰️ CYBERVERSE-Research/skyline-speeder (1 天 33⭐ ⑂4) — 发送端 eBPF struct_ops TCP 拥塞控制；Python + Rust · GPL-2.0 · kernel 6.12 LTS+ · Debian / Ubuntu；4 件套 skyline_cc + skyline_policy + skyline_tc + skyline-speederd；仅部署发送端客户端零改造；目标 10-20% 丢包 + 100-300 ms RTT；CUBIC 0.05-0.31 vs BBR 3-84 vs Skyline 79-95 Mbit/s 九宫格 +13% ~ +26.8x；守卫项失活场景 < 0.01% 偏差；RTO ceiling 防 101s 退避；双语 README；297 KB，fork/star 12.1%，Score 78


"""

out = "\n".join(lines[:fm_end]) + "\n" + new_section + "\n".join(lines[fm_end:])
p.write_text(out, encoding="utf-8")
print("Updated trend-index.md with 2026-09-19 section")
