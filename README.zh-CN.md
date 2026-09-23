# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-24.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-24

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 631 | 3 | 12k+ |

**今日核心判断：** anishfn/shapeshift 2 天 387⭐ ⑂43 「一个文本框变出对应卡片」的 Jev 决策 UI（TypeScript · MIT · 12.1 MB · 一句话判断 14 个 typed 问题决定走哪张卡片 · 日期 / 金额 / 单位 / 算式全用确定性代码 · 内置离线关键词分类器兜底 · 18 类卡片 · 滞回状态机 challenger 赢两次才换 · URL 参数 ?debug=1 ?demo=1&loop=1 可视化 · fork/star 11.1% Jev 应用层强信号 · 与昨日 09-22 Rizzo-AI-Academy/rizzo-flow「Spark-X2.5 4B Jev 兼容 API 0 generated tokens」+ 09-22 TianyuCodings/JevHarness「LLM 写 harness + GEPA 全轨迹反思」同构「Jev 应用层 + 内核分层」但推到「UI 端 typed questions + 决定走哪张卡片 + 确定性代码计算 + 内置离线兜底」具身交互形态）· SewCabinSpout/cleanupper 1 天 723⭐ ⑂0 macOS 终端清理 CLI 替代 CleanMyMac（JavaScript · MIT · 253 KB · macOS 11+ · Node.js 18+ · 一行 `xcode-select --install && mkdir diskclean && cd diskclean && npm install github:SewCabinSpout/cleanupper` 即装 · cleanupper scan 列出 user-caches / xcode-deriveddata / npm-cache / homebrew / browser-cache 五类回收空间 · Trash-first 删除可还原 · 保护路径黑名单让灾难性删除结构性不可能 · --json --yes 让 CI / cron 可脚本化 · Zero telemetry 全程不联网 · fork/star 0% 极干净个人开发者信号 · 与昨日 unreallabsai/unreal-agent「async-first harness 八组件」同构「严肃工程化个人开发者作品」但推到「macOS CLI + Trash-first 安全模型 + 保护路径黑名单 + Zero telemetry」安全工程化形态）· miuuyy/Astra-Ares 2 天 234⭐ ⑂15 GPT-6 Codex 任务自适应推理 effort（Jev 选 effort）（JavaScript · MIT · 716 KB · 单独安装打过补丁的 Codex CLI · OpenRouter 默认 · `ares configure` 配 key · `/model` 选 Astra / Sol / Luna Ares · Jev 在 GPT-6 调 reasoning effort 不破坏前缀缓存 · 显示 Jev LOW → HIGH ✓ APPLIED · macOS Apple Silicon 已本地构建测试 · macOS Intel / Linux 路径提供 · Windows 不支持 Unix-socket 集成 · 与昨日 09-22 Rizzo-AI-Academy/rizzo-flow + anishfn/shapeshift 同构「Jev + Codex / 严肃应用层」但推到「Codex 任务动态推理 effort + 不破坏前缀缓存 + 显示应用状态」严肃工程化形态）· edison-land/paragravity 2 天 186⭐ ⑂16 Google Antigravity 多账号并行沙箱管理器（Python · MIT · 136 KB · 一行 macOS `curl install.sh | bash` · Windows PowerShell clone · pgrav create work · 100% 非侵入基于 Chromium/Electron `--user-data-dir` · 零二进制补丁 · 0 MB idle overhead · 纯 Python 3 零外部依赖 · Native Google OAuth 完整登录流 · 自动生成 macOS .app 包 Spotlight 索引 · Windows .lnk 快捷方式 · SSH / config 三档 --links full / minimal / none · --inherit-config -i 继承宿主配置 · --no-mcp 排除 MCP · 与昨日 09-22 jev-chat 系列 + 09-23 unreallabsai/unreal-agent 同构「严肃工程化个人开发者工具 + 隐私 / 安全边界」但推到「Chromium / Electron user-data-dir 多账号并行 + 完整 OAuth 流 + 自动 .app / .lnk 集成 + Python 3 零依赖」跨平台形态）· lhlGitHub/threejs-architecture-effects 2 天 172⭐ ⑂35 Agent Skill 用 Three.js 动态组装古建（TypeScript · MIT · 66.3 MB · Codex / Claude Code / Cursor 三平台安装到 ~/.codex/skills / ~/.claude/skills / ~/.cursor/skills · Node.js 22.13+ WebGL2 浏览器 · `npm ci && npm run dev` · 一个 0-1 时间轴 play / pause / scrub backward · 程序化砖 / 木 / 抹灰 / 瓦 / 石 / 青铜 PBR · 飞檐细赏 + 石狮近观 镜头 · Vite + React + Three.js starter · 完全程序化几何无付费模型 · scaffold.mjs 拷 starter 不覆盖 · 与 09-19 ~ 09-22 各 agent skill / harness 同构「Agent Skill 严肃工程化」但推到「Three.js 古建程序化动态组装 + 0-1 时间轴 + 三平台 skills 安装 + 程序化材质 + Vite + React starter」3D 严肃工程化形态）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [anishfn/shapeshift](projects/shapeshift.md) | 387 stars | 观察型 |
| [miuuyy/Astra-Ares](projects/astra-ares.md) | 234 stars | 工具型 |
| [SewCabinSpout/cleanupper](projects/cleanupper.md) | 723 stars | 工具型 |
| [edison-land/paragravity](projects/paragravity.md) | 186 stars | 工具型 |
| [lhlGitHub/threejs-architecture-effects](projects/threejs-architecture-effects.md) | 172 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Jev 应用层 UI 端具身形态——anishfn/shapeshift 2 天 387⭐ ⑂43 fork/star 11.1%（TypeScript · MIT · 12.1 MB · 一个文本框根据输入自动变出对应卡片 · 一句话判断 14 个 typed questions（哪类卡片 + 该不该高亮警示）并行回答 · 日期 / 金额 / 单位 / 数学计算全用确定性代码 · 内置离线关键词分类器兜底不联网 · 18 类卡片 Event / Reminder / Checklist / Timer / Habit / Color / Split / Expense / Convert / Calculate / Trip / Poll / Contact / Bookmark / Countdown / Time zone / Random / Goal / Note · 滞回状态机 challenger 赢两次才换卡片防抖 · 信号徽章开 / 关用滞回带宽 · URL 参数 ?debug=1 显示每个概率 ?demo=1&loop=1 播放脚本演示 · ?shape=event etc 强制卡片类型 · Bun 1.2+ + Three.js + Next.js · 与昨日 09-22 Rizzo-AI-Academy/rizzo-flow「Spark-X2.5 4B Jev 兼容 0 generated tokens」+ 09-22 TianyuCodings/JevHarness「LLM 写 harness + GEPA 全轨迹反思」同构「Jev 应用层 + 内核分层」但推到「UI 端 typed questions + 决定走哪张卡片 + 确定性代码计算 + 内置离线兜底 + 滞回状态机 + URL 参数可视化 + Next.js」具身交互形态 · fork/star 11.1% Jev 应用层强信号）** · 相关项目：anishfn/shapeshift · 强度：88
2. **Jev 在 Codex 任务里动态选 reasoning effort——miuuyy/Astra-Ares 2 天 234⭐ ⑂15（JavaScript · MIT · 716 KB · 单独安装打过补丁的 Codex CLI 不动原有 codex 与 Codex desktop · OpenRouter 默认 Jev key · `ares configure` 配 OpenRouter 配 OpenRouter credits · `astra-ares` 启动 Codex 在 /model 选 Astra / Sol / Luna Ares · 每条选 underlying 模型固定 Jev 选 reasoning effort · 调 effort 用 GPT-6 原生机制不破坏前缀缓存 · 显示 Jev LOW → HIGH ✓ APPLIED · Step N · 321 ms · macOS Apple Silicon 已本地构建测试 · macOS Intel / Linux 路径提供 · Windows 不支持 Unix-socket 集成 · 与昨日 09-22 Rizzo-AI-Academy/rizzo-flow + anishfn/shapeshift 同构「Jev + Codex / 严肃应用层」但推到「Codex 任务动态推理 effort + 不破坏前缀缓存 + 显示应用状态 + OpenRouter 默认 + ares configure 配置 + 仅 macOS Apple Silicon 已 acceptance-test」严肃工程化形态）** · 相关项目：miuuyy/Astra-Ares · 强度：85
3. **macOS 终端清理 CLI 替代 CleanMyMac——SewCabinSpout/cleanupper 1 天 723⭐ ⑂0（JavaScript · MIT · 253 KB · macOS 11+ · Node.js 18+ · 一行 `xcode-select --install && mkdir diskclean && cd diskclean && npm install github:SewCabinSpout/cleanupper` 即装 · cleanupper scan 列出 user-caches / xcode-deriveddata / npm-cache / homebrew / browser-cache 五类回收空间 · Trash-first 删除可还原 · 保护路径黑名单让灾难性删除结构性不可能 · Xcode DerivedData & DeviceSupport / npm / Yarn / pnpm / pip / uv / CocoaPods / Gradle / Cargo / Go caches 全部覆盖 · purge 命令扫项目里 stale node_modules / target / .venv · --json --yes 让 CI / cron 可脚本化 · Zero telemetry 全程不联网 · 与昨日 unreallabsai/unreal-agent「async-first harness 八组件」同构「严肃工程化个人开发者作品」但推到「macOS CLI + Trash-first 安全模型 + 保护路径黑名单 + Zero telemetry + JSON 输出 + CI 脚本化 + 多语言依赖清理」安全工程化形态 · fork/star 0% 极干净个人开发者信号 · 723⭐ / fork 0 高质量粉丝结构）** · 相关项目：SewCabinSpout/cleanupper · 强度：82
4. **Google Antigravity 多账号并行沙箱管理器——edison-land/paragravity 2 天 186⭐ ⑂16（Python · MIT · 136 KB · 一行 macOS `curl install.sh | bash` · Windows PowerShell clone · pgrav create work · 100% 非侵入基于 Chromium/Electron `--user-data-dir` · 零二进制补丁 · 0 MB idle overhead · 纯 Python 3 零外部依赖 · Native Google OAuth 完整登录流 · 自动生成 macOS .app 包 Spotlight 索引 · Windows .lnk 快捷方式 · SSH / config 三档 --links full / minimal / none · --inherit-config -i 继承宿主配置 · --no-mcp 排除 MCP · 多账号 side-by-side 独立窗口 · 每实例 extensions / local storage / indexedDB / 聊天历史 完全隔离 · 流程可启动时不重启 · 与昨日 09-22 jev-chat 系列 + 09-23 unreallabsai/unreal-agent 同构「严肃工程化个人开发者工具 + 隐私 / 安全边界」但推到「Chromium / Electron user-data-dir 多账号并行 + 完整 OAuth 流 + 自动 .app / .lnk 集成 + Python 3 零依赖 + 三档链接策略 + 继承 / 排除 MCP」跨平台形态）** · 相关项目：edison-land/paragravity · 强度：78

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-24](daily/2026-09-24.md) | 5 | 3 |
| [2026-09-23](daily/2026-09-23.md) | 5 | 3 |
| [2026-09-22](daily/2026-09-22.md) | 4 | 3 |
| [2026-09-21](daily/2026-09-21.md) | 4 | 3 |
| [2026-09-20](daily/2026-09-20.md) | 4 | 3 |
| [2026-09-19](daily/2026-09-19.md) | 4 | 3 |
| [2026-09-18](daily/2026-09-18.md) | 5 | 3 |

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
