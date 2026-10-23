# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-24.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-24

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 747 | 4 | 95k+ |

**今日核心判断：** 本日最值得记的不是四个项目各自的领域，而是**同一件事在三种完全不同的技术层里被同时做出来：把'我不做的事'写进可核验的位置，并且用机器检查而不是用承诺来兜底**。**第一，Apple 内核移植在 48 小时内长出第三条互不相识的路径**——oosexgang/hackios-xnu-kernel（1.7 天 1,064⭐ ⑂183 fork/star 17.2%，subs 4，oi 7）走的是**第四条路线：不改内核、不伪造平台契约，而是直接编译 Apple 开源的 XNU 源码并打补丁**（xnu-8796.121.2 = iOS 16.5 的内核），用自写 EFI loader + Mu-Silicium UEFI 移植 + 替代闭源驱动 + Linux Wi-Fi 驱动兼容层跑**未修改的 iOS 16.5 用户态**（launchd → backboardd → SpringBoard → apps），且**它把'我们自己的检查会骗我们'写成了整整一篇 docs/checks.md**——十一让检查说谎的方式，每一条都附了真实代价（'被跳过的检查没有计数'让 68+3+7=78 这个和式把 78 项里的未检查项也算成了匹配）；**第二，theorem-labs/oss-verify-proofs（92⭐ ⑂6，subs 0，Rocq Prover）把'我证明了什么'与'我没证明什么'做成了可执行的形式**——20,164 条 statement 里 138 条已证、19,797 条仍 open，README 用一整节 'What a proof does not say' 逐条列出边界（不证明库正确、不覆盖整个库、只针对 riscv64 静态二进制而非源码、**没有一条 proof 证明 halts 所以不能排除永不终止的运行**），且把信任边界写成了一张清单（Rocq 内核与 vm_compute、LPS 语义模型、elf-snapshot 工具、oft check 对 Print Assumptions 的读取）；**第三，xevrion/hatchzip（2.5 天 888⭐ ⑂17，fork/star 1.9%，Rust + Apache-2.0）把'破坏性操作'变成了一个带不变量的工程**——它从归档尾部反向解压并边解压边截断归档文件（因为只有截尾在各文件系统上都可用，打洞不支持 FAT32/exFAT），AGENTS.md 第一条原则即'The tool destroys its input. The invariant is absolute'，并且**它拒绝在改动任何东西之前先算一遍'能不能装下'——7-Zip 默认把整个归档压成一个 solid block 时它直接拒绝执行，因为那块在解压完成前一点空间都释放不了**；**第四，haplollc/Vesalius（1.7 天 61⭐ ⑂1，Swift）用一个诚实的 benchmark 回答了'agent 到底会不会用我的 MCP'**——第一轮 24 次运行里 agent 只调用了 2 次，所以那一轮的 token 差距**主要是噪声**，作者把这个失败写进 README 而不是藏起来，重做后 20/20 次都调用，token 减 51%、质量 −0.5 分、且**它逐类列出'我没有赢的地方'（哪里功能在哪 −2.1 分、符号在哪 −1.7 分）**。**必须同时说清的热度限定**：本日四个项目 fork-star 为 17.2% / 1.9% / 6.5% / 1.6%，**依然不可横向比较**——HackiOS 的高比例对应'fork 去移植自己的机型'（仓库明写 common/new-device.sh + docs/PORTING.md + 设备 profile 模板），oss-verify 的 6.5% 对应'fork 去读证明语句'，hatchzip 的 1.9% 与 Vesalius 的 1.6% 对应'**不需要 fork，只需等待上游或直接下载安装包**'；**连续第四天观察到同一条分界线**。**而本日最刺眼的一条是生态层面的**：2026-10-22 12:24–12:28 之间，**至少 11 个互不相关的仓库在 8 分钟内集中发布**，全部使用 12 位随机字符的 owner 名（cs2-external-esp / pubg-external-esp / ff-external-esp / dbd-external-esp / deadlock-external / yt-view-bot / roblox-account-switcher / tiktok-dm-blaster / tiktok-view-bot / twitch-viewer-bot-ai / warzone-dlc-unlocker / pdf-annotate），**其中 9 个是 ESP 外挂、刷量机器人或账号切换器**——这是**可核验的批量账号行为**，不是有机增长。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [oosexgang/hackios-xnu-kernel](projects/hackios-xnu-kernel.md) | 1,064 stars | 观察型 |
| [theorem-labs/oss-verify-proofs](projects/oss-verify-proofs.md) | 92 stars | 观察型 |
| [xevrion/hatchzip](projects/hatchzip.md) | 888 stars | 工具型 |
| [haplollc/Vesalius](projects/vesalius.md) | 61 stars | 观察型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Apple 内核移植的第三条路径：不改内核、不伪造平台契约，而是直接编译 Apple 开源的 XNU 源码并打补丁。oosexgang/hackios-xnu-kernel（1.7 天 1,064⭐ ⑂183 fork/star 17.2%，subs 4 oi 7，NOASSERTION，20677 KB）以 xnu-8796.121.2（iOS 16.5 内核）为基线，配自写 EFI loader（xnuloader/loader.c，clang+lld-link，无 EDK2）、Mu-Silicium UEFI 移植（uefi/ + mkxnuimg.py，打包出 hackios-redwood-boot.img 供 fastboot boot）、Apple 闭源驱动的替代实现（IOSurface / IOMobileFramebuffer / AppleKeyStore / 网络栈）、Linux Wi-Fi 驱动（WCN6750 via ath11k + LinuxKPI 层）与 Metal 驱动工作（Mesa 25.0.7 + AIR 前端，docs/air.md 记录 456 个系统 shader 中 293 个已在 Adreno 642L 上运行），**跑未修改的 iOS 16.5 用户态**（'The iOS programs, frameworks and dyld shared cache are not changed by a single byte'，缺失部分由内核替代驱动或 DYLD_INSERT_LIBRARIES 注入库补齐）。它跑在两处：POCO X5 Pro 5G（redwood / Snapdragon 778G，fastboot boot 不写闪存，重启即回 Android）与 QEMU aarch64（无需真机）。**README 用两列表格逐项写明 What works / Does not work (yet)**（蜂窝、蓝牙、本内核下充电、App Store 与 Apple ID 登录因无 Secure Enclave 而不可用、视频与实况照片不可用）。**最值得记的是 docs/checks.md——'How our own checks lie'：十一让检查说谎的方式 + 一条对策，每条都附真实代价**（被跳过的检查没有计数 → 68+3+7=78 的和式把未检查项算成匹配；被静默的命令（patch -s --dry-run 返回 0 却不说话）被读成'恰好适用'；从缺席推断（'日志里没有' ≠ '没发生'，日志中间段被丢弃；grep 的视野问题导致漏掉二十行之上的守卫；一个从不触发的看门狗只有在同时给出运行次数（26/26 零漂移）时才证明任何事）**且它明写 'missing information reads as a missing problem'**。⚠️ 许可为 NOASSERTION 而 LICENSE 首行是 'APPLE PUBLIC SOURCE LICENSE Version 2.0 - August 6, 2003'（APSL 2.0，与 GPL 不同的 copyleft，含专利报复条款）——**这是本批第四处可核验的元数据不一致** · 相关项目：oosexgang/hackios-xnu-kernel, oosexgang/hackios-xnu-userland · 强度：91
2. **把'我证明了什么'与'我没证明什么'做成可执行的形式。theorem-labs/oss-verify-proofs（92⭐ ⑂6，fork/star 6.5%，subs 0 oi 1，Rocq Prover，MIT，2142968 KB ≈ 2.1 GB）针对 OSS-Fuzz 的 fuzz target 给出机器检验的 Rocq 证明：'There are 60 entry points in 25 libraries with proofs. The proofs are checked with Rocq 9.2.0. They are stated in LPS, a formal model of a Linux process that runs a RISC-V binary.' **证明的对象是编译后的二进制而非源码**——每条 agreement statement 主张'在 plain build 未超内存预算的每个输入上，sanitizer build 不触发任何错误，且两者的可观测行为集合相同'。**README 有独立一节 'What a proof does not say' 逐条列边界**：不证明库正确（sanitizer 检测不到的错误如错误结果或内存泄漏不在排除范围内）、只覆盖一个入口点可达的代码而非整个库、只针对 clang 20.1.8 + musl 构建的静态 riscv64 程序而非源码也非 x86-64 构建、**在 LPS 中为真而 LPS 与 Linux 不同处可能不适用**、**且本次发布没有任何一条 proof 证明 halts，因此都不能排除'永不终止的运行'**。**规模被诚实地摊开**：1,381 个 OSS-Fuzz 项目中 427 个可构建，2,148 个 harness、20,164 条 statement——138 条已证、0 条已知为假、229 条被模型阻塞、19,797 条仍 open。**信任边界写成清单**：Rocq 内核与其 vm_compute、toolchain/allowed-axioms.txt 里的公理（LPS 之外的只有 Rocq 原生整数/数组/字符串类型规范与 6 条标准库公理）、LPS 语义模型（commit f1006fe81783）、把 ELF 变成 LPS 内存映像的 elf-snapshot 与 rocq-read-file 0.0.2、oft check 对 Print Assumptions 的读取。**许可处理值得单列**：NOTICE 明确'我们自己写的 statements/tools/docs/proofs 用 MIT'，而'由 Anthropic 以 Apache-2.0 或 MIT 授权的证明派生而来的证明，保留那些许可与其文件头'，LICENSES/ 下同时存放 anthropic-proofs-LICENSE（Apache-2.0）、anthropic-proofs-LICENSE-MIT 与 anthropic-proofs-NOTICE，且每个此类证明的 build record 指名这三个文件。⚠️ subs 0、contributors API 返回空数组、**仅 2 个 commit**（'OSS Verify proofs 2026.10.0' 与一条 CI 改动），**这是机构发布而非社区共建** · 相关项目：theorem-labs/oss-verify-proofs · 强度：90
3. **把'破坏性操作'变成带不变量的工程，并且用'提前拒绝'代替'事后补救'。xevrion/hatchzip（2.5 天 888⭐ ⑂17，fork/star 1.9%，subs 1 oi 8，Rust，Apache-2.0，1990 KB）解决一个具体到能算的空间问题：180 GB 的归档解出 200 GB，用 WinRAR/7-Zip/unzip 需要 380 GB 磁盘，因为归档与产物必须同时存在；**HatchZip 从归档尾部反向解压，边解边把已完成的单元从归档文件尾部截断，于是归档让出的空间被下一个文件复用，只需略多于 200 GB**。它支持 ZIP / 7z / tar / .tar.gz / 分卷。**技术选择被写成理由链**：只能从尾部截断，因为从前或从中删除需要打洞（Linux fallocate / Windows FSCTL_SET_ZERO_DATA / macOS F_PUNCHHOLE），**而 FAT32 与 exFAT 不支持打洞，且各系统行为不同**；7z 的 solid block 只能从头解码，所以'最大单元'就是就地解压的主要成本。**它给出的唯一硬拒绝场景是一个可复算的判断**：7-Zip 默认设置会把整个归档放进一个 solid block，此时'一块在被完全解出前一点空间都释放不了'，**HatchZip 在碰任何东西之前就拒绝并说明原因**。**README 的对比表给了具体数值**：220 MiB tmpfs 上约 50 MB 空闲，200 MB 数据（21 文件）——ZIP 180 MB 时 unzip 在第 6/21 个文件耗尽空间而 HatchZip 全部完成且逐字节一致、7z -ms=20m（10 个 solid block）需 380 MB 而 HatchZip 0.64 s 完成、分成 5 卷的 7z 峰值占用 210 MB、tar 需 400 MB 而 HatchZip 0.12 s 完成、**7z 默认设置被拒绝**；速度上 ZIP 解压 0.25–0.35 s 对比 unzip 6.00 的 1.48–1.50 s（含一次 unzip 跳过的 fsync）。**AGENTS.md 把不变式写成绝对句**：'The tool destroys its input. The invariant is absolute: the journal never claims a file before it is durable, and the archive is never truncated past an entry the journal doesn't claim.'，并写明 'Anything that can be refused is refused before the archive is touched' 与 'Never run extract on an archive you can't recreate. It deletes it.'。**它还把踩过的坑写成具体条目**：zip crate 反向扫描整个归档找 end record，storage::Reader 必须对已截断区域返回零而不是报错，否则每次恢复都失败；Windows 上必须用字节区间锁因为锁归档会阻塞自己的读取线程；Linux 用一次 syncfs 刷新一批所以每目录的 bug 只在 macOS 与 Windows 上暴露；恢复时崩溃批次写过但未提交的文件仍占空间，必须先删除再做空间检查。**3 个 release（v0.1.0/v0.1.1/v0.1.2），每个 22 个 asset，含 Linux tar.gz 与 .deb/.rpm/AppImage 与 macOS dmg 与 Windows 安装器** · 相关项目：xevrion/hatchzip · 强度：89
4. **用一次诚实的失败轮次回答'agent 到底会不会用我的 MCP'。haplollc/Vesalius（1.7 天 61⭐ ⑂1，fork/star 1.6%，subs 1 oi 1，Swift，lic=null 无根级 LICENSE 文件，7870 KB）为 Claude Code 提供一个本地代码图（SwiftSyntax 解析的调用图 + MCP server + CLI + Mac app + VS Code 扩展），五个只读工具（usages / feature_map / outline / architecture / dependency_cycles）。**它最有价值的部分不是功能而是 benchmark 的诚实**：作者做了两轮——第一轮 24 次运行中 Claude 只在 2 次里调用了 Vesalius，**于是作者判定那一轮 13% 的 token 差距'主要是 run-to-run 噪声'并把失败原因写进 README**（根因是 Claude Code 把 MCP 工具藏在 tool search 后面而几乎从不搜索）；重做后按问题类型各配一个更锋利的工具、并把最常被问的两个预加载，**20/20 次全部调用，token 中位数减 51%（95% CI 36%–62%，几何均值；204k → 113k），轮数减 43%，耗时减 41%，质量 −0.5 分（95% CI −1.6 到 +0.8）**。**它诚实标注了没赢的地方**：按问题类型列出 token 与质量差——哪里功能在哪 −38% token 但 **−2.1 分**、符号在哪只 −8% token 且 **−1.7 分**、架构 −33% 且 −1.2 分、变更影响 −42% 且 −1.0 分；**20 题中有 4 题 token 反而更多（+2% 到 +19%），11 题质量移动超过 1 分（3 题更好、8 题更差）**，并说明'每题只有一次运行和一次评审，单题噪声很大'。**它还划出方法论边界**：8 题是留出集（在 Vesalius 2 设计之后写的、来自两个从未用于构建它的代码库），留出集上减 44%（95% CI 12%–65%），另 12 题是它对着建的。**三个代码库是私有应用且答案 key 与 transcript 不公开**（'so they cannot leak into future tool designs or training data'）。**对比表写明它不是所有人的正确工具**：调用图只覆盖 Swift（经类型解析）、TypeScript、JavaScript、Python，其余 13 种语言只有词法；只在 macOS 15+ Apple silicon 上运行；**在仓库里不留任何东西**（对比 CodeGraph 留 .codegraph/、graphify 留 graphify-out/）；无网络（对比 CodeGraph 默认开匿名遥测）。⚠️ **无根级 LICENSE 文件**（tree 递归查询确认仅有 CTreeSitter 与 tree-sitter 语法与 vscode-extension 的第三方许可），GitHub license 字段为 null，**这意味着默认版权保留** · 相关项目：haplollc/Vesalius · 强度：88

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-24](daily/2026-10-24.md) | 4 | 4 |
| [2026-10-23](daily/2026-10-23.md) | 4 | 4 |
| [2026-10-22](daily/2026-10-22.md) | 4 | 4 |
| [2026-10-21](daily/2026-10-21.md) | 4 | 4 |
| [2026-10-20](daily/2026-10-20.md) | 4 | 4 |
| [2026-10-19](daily/2026-10-19.md) | 4 | 4 |
| [2026-10-18](daily/2026-10-18.md) | 4 | 4 |

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
