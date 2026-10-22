# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-23.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-23

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 743 | 4 | 112k+ |

**今日核心判断：** 本日最值得记的不是四个项目各自的领域，而是三条各自独立却在同一天浮现出的同构信号：**第一，Apple 内核移植的两条互不相识路径（UniXNU 走 UEFI 伪平台契约 + 35 款设备文档，Snapintosh 走 EL2 hypervisor + 单机型 + 依赖一台 Mac 主机）撞上了同一组核心技术难点——16 KiB→4 KiB 页表翻译与 Apple 私有输入的合规处理，且各自独立地把「Apple kernelcache 不得入库」写成了仓库级制度**（UniXNU 的 README Private blobs 段、Macintosh 的 AGENTS.md 第 1 条与 THIRD_PARTY_NOTICES 的「contains no Apple binaries」声明）；**第二，DeepSeek 官方开源 DeepInfer（7 天 19,806⭐ ⑂2,106 Apache-2.0，subs 43 为本批最高）时在 README 里用整段明列「本次发布不含什么」——KV cache 系统、PD 分离、跨副本负载均衡——而这恰恰是本日报采信的全部材料里唯一一处「大厂把生产系统的缺口写在 README 而不是写在私有 wiki 里」的样本**；**第三，colinhacks/reylo（1.9 天 616⭐ ⑂3 fork/star 0.5%，subs 0）把 codegen 这个事实彻底从派生物里删掉——TypeScript 7.1 beta 的 content mappers 让 type checker 直接向引擎查询 SQL 类型，「派生物不存在于磁盘上，因此不可能过期」**。而热度判读必须与前日保持一致的限制：本日四个项目 fork-star 分化极端（0.5% / 5.5% / 10.6% / 15.7%），**fork-star 高的是「fork 去移植自己的机型」（UniXNU），低的是「不需要 fork，只需等待上游 beta 特性」（reylo）**——fork 比例在不同类型项目之间不可直接比较，这是连续第三天观察到的同一条分界线。今天没有 CVE 驱动的注意力洪峰，这是自 php2shell 事件以来第一次：**热度排序对技术选型的干扰比昨天小，但这四个项目没有一个是可以直接采用的**——UniXNU 与 Macintosh 是研究快照，DeepInfer 缺三成系统，reylo 依赖 beta 语言特性。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [UniXNU/UniXNU](projects/unixnu.md) | 750 stars | 观察型 |
| [deepseek-ai/DeepInfer](projects/deepinfer.md) | 19,806 stars | 基础设施候选 |
| [Acelogic/Snapintosh](projects/snapintosh.md) | 530 stars | 观察型 |
| [colinhacks/reylo](projects/reylo.md) | 616 stars | 观察型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Apple 内核移植的两条独立路径撞上同一组难点：UniXNU/UniXNU（3.5 天 750⭐ ⑂118 fork/star 15.7% 本批最高）走 UEFI + 伪平台契约 + 16 个驱动独立 submodule + 35 份设备文档（docs/devices/amethyst / sheng / fajita / nuwa / pipa / piano / q2q / tb128fu / gta4l …），并在 10-22 宣布原生 Adreno 740 Metal 驱动在小米平板 6S Pro 上完全可用；Acelogic/Snapintosh（20 小时 530⭐ ⑂29）走 EL2 hypervisor 跑官方 macOS 27 kernelcache（J700/T8140，默认未修改）于 ASUS Zenbook A16，自写 AdrenoMetal.bundle + AdrenoX2 IOGPU kext + air2ir3（AIR→Mesa ir3 shader 编译器）并明文「无软件/CPU/半虚拟渲染路径」，用 Status 表逐项写明流畅度 in progress（目标 60 Hz，120 Hz 排后）、Wi-Fi 仅 host-proxy 可用、音频摄像头蓝牙休眠外接显示器全不支持，且必须配一台 macOS 27 Mac 主机经 USB-C NCM 驱动。两者都把 16 KiB→4 KiB 页表翻译单列为核心章节，都把「Apple 私有输入不得入库」写成仓库级制度** · 相关项目：UniXNU/UniXNU, Acelogic/Snapintosh · 强度：90
2. **deepseek-ai/DeepInfer（7 天 19,806⭐ ⑂2,106 fork/star 10.6%，subs 43 本批最高）用整段 README 明列本次发布不含什么：KV cache 系统、VE/Prefill/Decode 分离（引擎大部分必需功能已实现）、prefill 与 decode 两侧的跨 DP 副本负载均衡（doc/inference_deployment_qa.md 补充称前两者与内部基础设施耦合紧密尚未完全开源）；同时用 QA 文档给出三条可核验的生产目标（支持多厂商加速器 / prefill 用普通 8 卡机而 decode 用 64–128 卡超节点 / KV cache 保留 >72h 换上下文复用）与一条作者声明（单集群 155T tokens/日、38 USD per GPU-hour 谷值定价），开源部分为 FlashMLA + DeepGEMM + DeepEP + TileKernels + DeepSelect + TileLang kernel 之上，加 DSpark 置信度调度验证、SWA bounded replay（compact 模式 + KEEP_TOKENS=140，保留后缀须覆盖 SWA 窗口 + 最大回退长度）、默认开启的异步调度、batch-invariant 与确定性采样（均标注 NVIDIA only）** · 相关项目：deepseek-ai/DeepInfer · 强度：89
3. **colinhacks/reylo（1.9 天 616⭐ ⑂3 fork/star 0.5% 本批最低，subs 0）把 codegen 从派生物里彻底删除：TypeScript 7.1 beta 的 content mappers 让 type checker 直接向 Rust 引擎查询 SQL 类型，六卖点明写「No codegen — the type checker asks Reylo directly: no generated files, no watcher」「Checked against your database — 拼错的列名、错误参数、已删除的表都是类型错误，且在 tsc 与编辑器里成立」「类型来自 SQL 本身（::int → number），无手写行类型、无 schema 文件需同步」，并首次把 DRY 论证改写为 agent 论证（each fact lives in one place, so an agent cannot leave a stale type behind）** · 相关项目：colinhacks/reylo · 强度：87

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-23](daily/2026-10-23.md) | 4 | 4 |
| [2026-10-22](daily/2026-10-22.md) | 4 | 4 |
| [2026-10-21](daily/2026-10-21.md) | 4 | 4 |
| [2026-10-20](daily/2026-10-20.md) | 4 | 4 |
| [2026-10-19](daily/2026-10-19.md) | 4 | 4 |
| [2026-10-18](daily/2026-10-18.md) | 4 | 4 |
| [2026-10-17](daily/2026-10-17.md) | 4 | 4 |

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
