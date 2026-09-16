# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-17.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-17

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 601 | 5 | 9k+ |

**今日核心判断：** dsh-lab/cordis-bundle-publisher 1 天 14⭐ ⑂3 DSH cordis bundle 打包发布 CLI（Python · MIT · bundle.manifest.yml schema 校验 + cordis-1.x 兼容矩阵 + SHA-256 bundle 元数据 + minisign 离线签名 + PyPI + OCI 双注册源 + GH Actions / GitLab CI / 本地三套分发通道 + bundle 一行 install + 自动 prerelease 标签 · 与昨日 dsh-computer-use_codex-style cordis.patch.yml 安装机制同构 DSH bundle 工具链补齐「打包签名发布」侧）· Neuroscale/cortical-stack 1 天 56⭐ ⑂9 Frozen LM × 皮层微电路栈（Python · Apache-2.0 · 7 层皮层微电路属性 + 31,200 保留节点 + 4,485,600 directed connections · 412,000 参数 adapter · Liquid AI LFM2-1.2B 冻结 · token embeddings + 微电路位置编码双驱动固定 graph · adapter 双流 readout · Apple Silicon MPS + NVIDIA CUDA + CPU 三路径 · upstream SHA-256 + 可选 Triton kernel 加速 SciPy 同语义 · 48 corpus + 24 synthetic style 训练 + 32 separate test 评估 · parameter-matched 直接输入 adapter 控制组 · runs/conversation-v3/ 写一次不被覆盖 · /reset 清空 /quit 退出 · 与昨日 FLModel/flm 同构「frozen LM + trainable adapter + fixed graph readout」但推到「哺乳动物皮层 7 层微电路」研究领域）· skill-lab/feishu-chat-archive 1 天 11⭐ 飞书群聊归档 Codex Skill（Python · MIT · 按群名精确匹配 + 默认 24h 可指定时长/历史截止时间/已确认群 ID · tenant_access_token + im/v1/messages 全量分页 + 增量游标 + WAL 增量 · 文本/富文本/可解析卡片/消息引用 · 每个报告条目引用本次真实 message_id · 已确认/已接收/待完成/个人观点/报告建议五分类 · PNG 长图 + HTML 网页 + Markdown 摘要三格式同一正文 · requests + cryptography + zstandard + Pillow + Python 3.12 · 中文字体微软雅黑可指定其他字体 · tenant_access_token 默认仅存内存退出清理 · 默认不上传原始记录/数据库/个人配置 · 飞书开放平台 API v1 实际验证 · MIT 许可 + 1.1 MB repo · 与昨日 Tina2088/wechat-group-report「本地数据库 + Codex Skill」同构但推到「云 API + Codex Skill 编排」飞书场景）· agent-sec/mod-provenance-graph 1 天 9⭐ ⑂4 Claude Code Mod 依赖图 + provenance SBOM 工具（JavaScript · Apache-2.0 · Anthropic 2026-09-09 function hooks 发版后 + claude plugin validate 静态扫描产物 · `mod-graph build` 解析每个 Mod package.json + $.hooks + plugin.json + references · 生成 mod-graph.json 有向图节点为 mod 边为依赖/钩子事件/$ 调用 · `mod-graph provenance` 输出 CycloneDX 1.5 SBOM 含每个 mod 维护者/许可/钩子事件/L0-L3 reach · `mod-graph diff` 对比昨日 mod-graph.json 与今日生成版本仅差异输出（与昨日 karanb192/awesome-claude-code-mods L0/L1/L2/L3 reach 同构但推到「Mod 依赖图 + SBOM 标准化」领域）· clawback/claude-code-cost-ledger 1 天 17⭐ ⑂2 Claude Code token 成本分账账本（Python · MIT · ~/.claude/projects/**/*.jsonl 读取 · canonical JSON 编码 + content_hash 去重 · message_id / parent_uuid 链 + cache_read_input_tokens / cache_creation_input_tokens / input / output 四类 token · per-session / per-day / per-bucket 聚合 · cost.csv / cost.json / cost.md 三格式输出 · 当前价格快照可被本地覆盖 · buckets.yaml 分账维度 + slack 通知（可选）· pre-commit hook 校验单日成本超阈值 · 188 KB repo · 与昨日 ToolMonsters/claude-code-routing「cheap model 当 worker + Claude 当 orchestrator」成本优化同构但推到「成本可见 + 分账账本」治理层 · 与昨日 ToolReplay「session 层审计」同构但推到「session 层成本治理」领域）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [dsh-lab/cordis-bundle-publisher](projects/cordis-bundle-publisher.md) | 14 stars | 工具型 |
| [Neuroscale/cortical-stack](projects/cortical-stack.md) | 56 stars | 观察型 |
| [skill-lab/feishu-chat-archive](projects/feishu-chat-archive.md) | 11 stars | 工具型 |
| [agent-sec/mod-provenance-graph](projects/mod-provenance-graph.md) | 9 stars | 工具型 |
| [clawback/claude-code-cost-ledger](projects/claude-code-cost-ledger.md) | 17 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **dsh-bundle-publisher / DSH cordis bundle 打包签名发布 CLI——dsh-lab/cordis-bundle-publisher 1 天 14⭐ ⑂3（Python · MIT · bundle.manifest.yml schema 校验 + cordis-1.x 兼容矩阵声明 + SHA-256 bundle 元数据 + minisign 离线签名 + PyPI + OCI 双注册源 + GitHub Actions / GitLab CI / 本地三套分发通道 · bundle 一行 install · 自动 prerelease 标签 · 与昨日 dsh-computer-use_codex-style cordis.patch.yml 安装机制同构 DSH bundle 工具链补齐「打包签名发布」侧）** · 相关项目：dsh-lab/cordis-bundle-publisher · 强度：86
2. **cortical-microcircuit-stack / Frozen LM × 哺乳动物皮层 7 层微电路栈——Neuroscale/cortical-stack 1 天 56⭐ ⑂9（Python · Apache-2.0 · 7 层皮层微电路属性 + 31,200 保留节点 + 4,485,600 directed connections · 412,000 参数 adapter · Liquid AI LFM2-1.2B 冻结 · token embeddings + 微电路位置编码双驱动固定 graph · adapter 双流 readout · Apple Silicon MPS + NVIDIA CUDA + CPU 三路径 · upstream SHA-256 · 可选 Triton kernel 加速 SciPy 同语义 · 48 corpus + 24 synthetic style 训练 + 32 separate test 评估 · parameter-matched 直接输入 adapter 控制组 · runs/conversation-v3/ 写一次不被覆盖 · /reset 清空 /quit 退出 · fork/star 16.1% 学术信号 · 与昨日 FLModel/flm「Frozen LM × 苍蝇脑连接组」同构但推到「哺乳动物皮层 7 层微电路」研究领域）** · 相关项目：Neuroscale/cortical-stack · 强度：82
3. **feishu-chat-archive-skill / 飞书群聊归档 Codex Skill——skill-lab/feishu-chat-archive 1 天 11⭐（Python · MIT · 按群名精确匹配 + 默认 24h 可指定时长/历史截止时间/已确认群 ID · tenant_access_token + im/v1/messages 全量分页 + 增量游标 + WAL 增量 · 文本/富文本/可解析卡片/消息引用 · 每个报告条目引用本次真实 message_id · 已确认/已接收/待完成/个人观点/报告建议五分类 · PNG 长图 + HTML 网页 + Markdown 摘要三格式同一正文 · requests + cryptography + zstandard + Pillow + Python 3.12 · 中文字体微软雅黑 · tenant_access_token 默认仅存内存退出清理 · 默认不上传原始记录 · 飞书开放平台 API v1 实际验证 · 1.1 MB repo · 与昨日 Tina2088/wechat-group-report「本地数据库 + Codex Skill 编排」同构但推到「云 API + Codex Skill 编排」飞书场景 · 反 SaaS 范式扩展到「中国云办公 API」）** · 相关项目：skill-lab/feishu-chat-archive · 强度：80
4. **claude-mod-provenance-graph / Claude Code Mod 依赖图 + provenance SBOM 工具——agent-sec/mod-provenance-graph 1 天 9⭐ ⑂4（JavaScript · Apache-2.0 · Anthropic 2026-09-09 function hooks 发版后 + claude plugin validate 静态扫描产物 · `mod-graph build` 解析每个 Mod package.json + $.hooks + plugin.json + references · 生成 mod-graph.json 有向图节点为 mod 边为依赖/钩子事件/$ 调用 · `mod-graph provenance` 输出 CycloneDX 1.5 SBOM 含每个 mod 维护者/许可/钩子事件/L0-L3 reach · `mod-graph diff` 对比昨日 mod-graph.json 与今日生成版本仅差异输出 · 145 KB repo · fork/star 44.4% 极高早期信号 · 与昨日 karanb192/awesome-claude-code-mods L0/L1/L2/L3 reach 同构但推到「Mod 依赖图 + SBOM 标准化」治理层 · 与昨日 ToolReplay「session 层审计」同构但推到「plugin/mod 供应链可见性」领域）** · 相关项目：agent-sec/mod-provenance-graph · 强度：81

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-17](daily/2026-09-17.md) | 5 | 5 |
| [2026-09-16](daily/2026-09-16.md) | 5 | 4 |
| [2026-09-15](daily/2026-09-15.md) | 5 | 4 |
| [2026-09-14](daily/2026-09-14.md) | 4 | 4 |
| [2026-09-13](daily/2026-09-13.md) | 6 | 4 |
| [2026-09-12](daily/2026-09-12.md) | 8 | 6 |
| [2026-09-11](daily/2026-09-11.md) | 8 | 7 |

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
