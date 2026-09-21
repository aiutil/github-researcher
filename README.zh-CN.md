# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-22.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-22

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 622 | 3 | 11k+ |

**今日核心判断：** Finderchangchang/jev-chat-JARVIS 1 天 833⭐ ⑂361 Android「聊天副驾」悬浮窗用 Jev 一次 7 道题判断对话（Kotlin · MIT · 微信 8.0.78 / QQ 9.3.50 / X 12.25 真机验证 · 无障碍读节点不 hook 不改包 · 发送永远由你点不碰转账红包 · 17103 KB · fork/star 43.3% 极高企业信号）· Rizzo-AI-Academy/rizzo-flow 1 天 221⭐ ⑂6 Jev 兼容 API 本地实现 0 generated tokens（Python · Apache-2.0 · Spark-X2.5-4B Apache-2.0 开源权重 · MLX Metal / CUDA / CPU 三路径 · 1M native context · ~250 ms / decision Q8 M4 Pro · ~5 GiB 内存 Q8 · POST /v1/decisions + POST /v1/systemone + GET /v1/models 三端点 · TYPESAFE_BASE_URL 指 localhost 即可替换官方 · 预填 KV cache 克隆给每道题 · 只算 answer letters logits 验证同语义 · 140 步 25.6 秒 ≈ 5.5/秒 Snake demo · 4770 KB · README 明示「Independent project, not affiliated with TypeSafe」+「Probabilities are uncalibrated unless you calibrate them」）· TianyuCodings/JevHarness 1 天 76⭐ ⑂4 LLM 写任务专属 Jev harness + GEPA 全轨迹反思演化（Python · 无 license · Claude Code / Codex 双接入 plugin marketplace add + plugin install jev-harness@jevharness · Pokémon 5 轮反思 Eval 胜率 25% → 75% · 选定 harness 完整决策 568 ms P95 657 ms · 单 Jev 请求 269 ms P95 348 ms · 226 Jev 请求 median · author LLM 不在 runtime · Frozen artifacts 绑定 spec + runtime + evaluator + 任务资源 · node.js website/build.mjs + preview.mjs 本地浏览器回放 · 43246 KB · honesty「improvement is on selection Eval set, not independent estimate of unseen games」）· fstandhartinger/chat-seek-vscode 1 天 54⭐ ⑂6 VS Code 跨 Claude Code / Codex / OpenCode 聊天本地检索 + Laya reranking（JavaScript · MIT · Ctrl+Shift+P → Chat Seek: Search past AI chats · 侧栏放大镜 Activity Bar · Laya 本地决策模型 1.7 GB 模型下载到 ~/.cache/receptron-laya · 可选 OpenAI / OpenRouter / TensorX / Custom OpenAI-compatible 摘要 默认 gpt-5.6-luna low reasoning · SecretStorage 存 API key · 摘要默认 off 默认完全本地 · Resume 跳到匹配 CLI 的 session id + cwd · 2753 KB · 与昨日 09-19 wuyoscar/jev-skill「Awesome Jev Skills 9 技能 + 90 场景」同构「Jev 周边工具 + 本地检索 + 双语 + 可执行化」但推到「跨 CLI 聊天记录本地搜索 + Laya reranking + VS Code 集成」领域）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [Finderchangchang/jev-chat-JARVIS](projects/jev-chat-jarvis.md) | 833 stars | 观察型 |
| [Rizzo-AI-Academy/rizzo-flow](projects/rizzo-flow.md) | 221 stars | 工具型 |
| [TianyuCodings/JevHarness](projects/jevharness.md) | 76 stars | 工具型 |
| [fstandhartinger/chat-seek-vscode](projects/chat-seek-vscode.md) | 54 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Android「聊天副驾」悬浮窗 Jev 一次 7 道题判断对话——Finderchangchang/jev-chat-JARVIS 1 天 833⭐ ⑂361（Kotlin · MIT · 微信 8.0.78 / QQ 9.3.50 / X 12.25 真机验证 · 飞书采集已接入 · 一套内核 + 一个 App 一个几十行的 ChatAppAdapter · 非侵入：无障碍读节点不 hook 不改包不走 App 接口不读数据库 · 看得懂：Jev 一次给意图 / 危险等级 1-9 / 对方要什么 / 该不该马上回 / 最佳动作 · 3 条候选 Jev 排序 · 发送永远由你点 · 隐私在本机：密钥只存 App 私有空间聊天内容只在分析那一刻发给模型 · 国产 ROM 后台冻结小米 / HyperOS 必做自启动 + 省电无限制 · 17103 KB · fork/star 43.3% 极高企业 / 个人开发者 fork 信号 · 与昨日 09-19 ~ 09-21 各 Jev / Laya 决策模型应用层同构但推到「Android 端无障碍采集 + Jev 实时判断 + 用户最终 gate」移动端具身智能领域 · README 明示「只读你自己设备上你自己有权查看的聊天」+「程序只把回复填进输入框从不自动发送不碰转账红包收款」）** · 相关项目：Finderchangchang/jev-chat-JARVIS · 强度：90
2. **Jev 兼容 API 本地实现 0 generated tokens——Rizzo-AI-Academy/rizzo-flow 1 天 221⭐ ⑂6（Python · Apache-2.0 · Spark-X2.5-4B / Spark-X2.5-1.7B Apache-2.0 开源权重 · MLX Metal / CUDA / CPU 三路径 · 1M tokens native context · ~250 ms / decision Q8 M4 Pro · ~5 GiB 内存 Q8 · POST /v1/decisions native API + POST /v1/systemone + GET /v1/models Jev 兼容三端点 · 4 类 typed decisions boolean / choice / score / numeric + 内置 __insufficient__ 弃权 · TYPESAFE_BASE_URL=http://127.0.0.1:8017 即可替换官方 · 预填 KV cache 克隆给每道题 · 只算 answer letters logits 验证 identical · Snake demo 140 步 25.6 秒 ≈ 5.5/秒 ≈ 150 ms / decision · uv sync --locked --extra mlx/cuda/cpu · 4770 KB · fork/star 2.7% · 与 09-19 NiazMorshed2007/jev-review「本地优先 MCP 质量评估」+ 09-20 logan-markewich/jeff「自托管 Jev drop-in GLiFormer 400M」同构「Jev 去 SaaS 化 + 自托管 drop-in」但推到「Spark-X2.5 4B Apache-2.0 开源权重 + Jev-compatible API + KV cache 克隆 + 0 generated tokens + 1M native context」具体实现 · README 明示「Independent project, not affiliated with TypeSafe」+「Probabilities are uncalibrated unless you calibrate them」+「The interface is compatible, the model is not Jev」）** · 相关项目：Rizzo-AI-Academy/rizzo-flow · 强度：88
3. **LLM 写任务专属 Jev harness + GEPA 全轨迹反思演化——TianyuCodings/JevHarness 1 天 76⭐ ⑂4（Python · 无 license · Claude Code plugin marketplace add + plugin install jev-harness@jevharness · Codex 接入 · Pokemon 例子里 5 轮反思 Eval 胜率 25% → 75% · 选定 harness 完整决策 568 ms median P95 657 ms · 单 Jev 请求 269 ms median P95 348 ms · 226 个 Jev 请求 median · Frozen artifacts 绑定 PipelineSpec + PipelineRuntime + evaluator + 任务资源 · task adapter 边界 owns observations + legal actions + side effects + scoring · harness owns feature construction + Jev judgments + decision logic · reflection 包含完整 decisions + observations + node inputs / outputs + Jev questions / answers + memory + failures · lossless dedup · 超出 byte cap 归档拒绝不截断 · node website/build.mjs + preview.mjs 本地浏览器回放 · 43246 KB · fork/star 5.3% · 与昨日 09-20 sutro-sh/jev-align「GEPA 对齐 Jev」同构「Jev + GEPA」但推到「LLM author harness once + GEPA full-trajectory reflection + freeze strategy + runtime Jev fast fuzzy」严肃工程化 · README 诚实「improvement is on selection Eval set, not independent estimate of performance on unseen games」）** · 相关项目：TianyuCodings/JevHarness · 强度：82
4. **VS Code 跨 Claude Code / Codex / OpenCode 聊天本地检索 + Laya reranking——fstandhartinger/chat-seek-vscode 1 天 54⭐ ⑂6（JavaScript · MIT · Ctrl+Shift+P → Chat Seek: Search past AI chats + 侧栏放大镜 Activity Bar + Pin search tab · Laya 本地决策模型 1.7 GB 模型下载到 ~/.cache/receptron-laya CPU inference · 可选摘要 OpenAI / OpenRouter / TensorX / Custom OpenAI-compatible 默认 gpt-5.6-luna low reasoning · SecretStorage 存 API key · 摘要默认 off 默认完全本地 · Resume 跳到匹配 CLI 的 session id + cwd · Read excerpt 打开索引上下文 · 一次 Laya 用法下载 1.7 GB 模型权重 · npm ci + npm test + npm run lint + npm run package + code --install-extension · 2753 KB · fork/star 11.1% · 与昨日 09-19 wuyoscar/jev-skill「Awesome Jev Skills 9 技能 + 90 场景」同构「Jev / Laya 周边工具 + 本地检索 + 双语 + 可执行化」但推到「跨 CLI 聊天记录本地搜索 + Laya reranking + VS Code 集成 + Resume」领域 · 与 09-18 wshobson/agents「多 Harness Skills 市场」同构「跨 Harness Agent 工具」但推到「跨 Harness 聊天记录检索」领域）** · 相关项目：fstandhartinger/chat-seek-vscode · 强度：78

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-22](daily/2026-09-22.md) | 4 | 3 |
| [2026-09-21](daily/2026-09-21.md) | 4 | 3 |
| [2026-09-20](daily/2026-09-20.md) | 4 | 3 |
| [2026-09-19](daily/2026-09-19.md) | 4 | 3 |
| [2026-09-18](daily/2026-09-18.md) | 5 | 3 |
| [2026-09-17](daily/2026-09-17.md) | 5 | 5 |
| [2026-09-16](daily/2026-09-16.md) | 5 | 4 |

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
