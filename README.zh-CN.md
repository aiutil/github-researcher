# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-15.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-15

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 592 | 4 | 9k+ |

**今日核心判断：** Matthew0822/ToolReplay 1 天 171⭐ ⑂18 fork/star 10.5% Agent 工具调用会话审计 CLI（Python · MIT · hash-chain 封存 + 确定性 replay + 权限越权 scope 检查 + 无三方依赖 + seal/replay/verify/scope/version 五命令 · 单一六行样本跑通 non-determinism + redundant-call + permission-overreach 三类 finding）· yifanzhang-pro/FlashREINFORCE 1 天 39⭐ ⑂3 NVIDIA 2026-09 论文 Asynchronous RL 框架（Python · Apache-2.0 · Critic-Free 单 rollout + token importance sampling + Sequence Trust Region + Sample-Mean Optimization + 整合 Molt 异步训练 + R1 / Qwen2.5-Math pinned launcher + ALFWorld 设置）· 0xjohnnydev/airlift 1 天 33⭐ ⑂2 iOS 27.0 RC AirTraffic 沙箱逃逸 PoC（Objective-C · NOASSERTION · /var/mobile/Media/Airlock/Book ATAirlock 路径校验漏洞 + MobileDevice.framework + AirTrafficHost + paired-Mac Wi-Fi/USB 触发 + 已验证 12 个目录写权限 + Books 同步链 NSFileManager follow symlink）· FelixQiu1/XiaoAi-LLM-Router 1 天 20⭐ MIT 老旧小米小爱同学升级 DeepSeek/Ollama 本地智能管家网关（Python · LiteLLM 100+ 供应商统一接口 + MiService 拦截 + MiTTS 切句播放 + 唤醒词路由 + 多轮对话记忆 session + Docker Compose 一键部署 + Ollama 模式链路不出局域网）· ToolMonsters/claude-code-routing 1 天 19⭐ ⑂3 Spotify Portal 90% Claude Code token 削减开源复现（HTML · MIT · code-write Haiku 直写盘 + bulk-read 整文件读 Haiku + PreToolUse 350 行阻断 hook + 4 个 psf/requests 复现基准 + Opus 5 实际成本对比）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [Matthew0822/ToolReplay](projects/toolreplay.md) | 171 stars | 工具型 |
| [yifanzhang-pro/FlashREINFORCE](projects/flashreinforce.md) | 39 stars | 生产可用 |
| [0xjohnnydev/airlift](projects/airlift.md) | 33 stars | 工具型 |
| [FelixQiu1/XiaoAi-LLM-Router](projects/xiaoai-llm-router.md) | 20 stars | 工具型 |
| [ToolMonsters/claude-code-routing](projects/claude-code-routing.md) | 19 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **agent-transcript-audit / Coding Agent 工具调用会话审计 CLI——Matthew0822/ToolReplay 1 天 171⭐ ⑂18 fork/star 10.5%（Python · MIT · seal/replay/verify/scope/version 五命令 · hash-chain 封存 + canonical JSON 编码比较 deterministic + state-change mutator 识别 redundant + 外部声明权限 scope 文件比对 overreach · Python 3.11+ 零三方依赖 · samples/session-dirty.jsonl 单一六行样本覆盖三类 finding · exit code 1 标记有 finding · 报告顺序稳定到 byte-identical · 464KB repo · 与昨日 tracecrate/birdview/ccompactor 同构 AI Coding 可观测栈第七件套「session 层审计」）** · 相关项目：Matthew0822/ToolReplay · 强度：92
2. **async-agentic-rl-framework / NVIDIA FlashREINFORCE Asynchronous Agent RL 框架——yifanzhang-pro/FlashREINFORCE 1 天 39⭐ ⑂3（Python · Apache-2.0 · flashreinforce/loss.py 参考实现含 batch centering + token IS + sequence trust + sample mean + entropy-based failure-token filter · scripts/train_molt.py Molt 异步训练 launcher · R1 / Qwen2.5-Math reasoning + Python tools + MoE + ALFWorld 实验设置 · docs/training.md GPU/data/命令/paper-to-code 映射 · pip install -e '.[test]' + pytest · 701KB repo · 官方代码仓 NVIDIA-NeMo/labs-molt）** · 相关项目：yifanzhang-pro/FlashREINFORCE · 强度：86
3. **ios27-airtraffic-sandbox-escape / iOS 27.0 RC AirTraffic 沙箱逃逸 PoC——0xjohnnydev/airlift 1 天 33⭐ ⑂2（Objective-C · NOASSERTION · MobileDevice.framework + AirTrafficHost.framework 链路 · com.apple.streaming_zip_conduit → afc → atc → AirTrafficDevice → Books sync client → ATLegacyAssetLink → ATAirlock → NSFileManager 12 个目录写权限已验证 · -[ATAirlock processCompletedAsset:] 仅校验 destination 字符串前缀未验证 source · ancestor symlink 跟随 · Books "Persistent ID" 无路径校验 · 仅声明 PoC 给开发者与安全研究者 · iOS 27.0 RC 24A435 + final 24A437 验证）** · 相关项目：0xjohnnydev/airlift · 强度：84
4. **xiaoai-local-llm-gateway / 老旧小米小爱同学升级 DeepSeek/Ollama 本地智能管家网关——FelixQiu1/XiaoAi-LLM-Router 1 天 20⭐（Python · NOASSERTION · MiService 拦截小爱收音 + LiteLLM 100+ 供应商统一接口 + MiTTS 切句播放回小爱 · 多轮对话记忆按 device + 时间窗 TTL 默认 10 分钟 max_turns 10 · 唤醒词路由「请问 / 深思」命中才走 LLM · Ollama 模式链路不出局域网 · docker compose up -d 一键部署 · config.yaml 切换 deepseek/ollama/openai/claude 同套唤醒词记忆 · 20KB repo · 与昨日 tracecrate/maskit 本地 AI Coding 工具链三件套同构「本地 + 自带 key」反 SaaS 范式推到智能音箱领域）** · 相关项目：FelixQiu1/XiaoAi-LLM-Router · 强度：78

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-15](daily/2026-09-15.md) | 5 | 4 |
| [2026-09-14](daily/2026-09-14.md) | 4 | 4 |
| [2026-09-13](daily/2026-09-13.md) | 6 | 4 |
| [2026-09-12](daily/2026-09-12.md) | 8 | 6 |
| [2026-09-11](daily/2026-09-11.md) | 8 | 7 |
| [2026-09-09](daily/2026-09-09.md) | 10 | 7 |
| [2026-09-08](daily/2026-09-08.md) | 9 | 6 |

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
