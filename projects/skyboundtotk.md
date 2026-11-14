---
title: "NotRexed/SkyboundTotk"
slug: skyboundtotk
date_added: "2026-10-30"
last_seen_date: "2026-11-03"
category: "生产可用"
emoji: "🌌"
stars: "485 stars"
stars_delta: "8 天 485⭐ ⑂44（fork/star 9.1%）· 快照 2026-11-03T06:00Z；10-30 首建档时记录 392⭐，本次为两次快照间的总量差，非当日新增；同期 commits 32→32（未变）、contributors 4→4（未变）、releases 0→0"
language: "C++"
score: 87
tags: ["skyboundtotk", "static-recompilation", "totk", "webgpu", "wgpu-native", "patched-wgpu", "linux-macos-windows", "build-id-gated-hooks", "45gb-build-footprint", "python-lz4", "emsdk-6.0.9", "rust-bindgen", "libclang", "pipeline-cache-rxcache", "astc-cpu-decode", "mit", "no-game-files", "mmap-4gb-window", "pr-19-keno80"]
url: "https://github.com/NotRexed/SkyboundTotk"
---

# NotRexed/SkyboundTotk

## 一句话定位

《塞尔达传说：王国之泪》base 1.0.0 的原生静态重编译移植（Windows x64 + Linux x86_64），**图形走 WebGPU 而非 Vulkan**——而它最值得记的不是移植本身，是它对「未验证的东西」的诚实分级：**「a successful build does not guarantee a complete playthrough」「The standalone startup test initialized the renderer and loaded the packaged RomFS, but did not verify full gameplay or graphics correctness.」**

## 它解决的问题

**把 Switch 上的 TotK base 1.0.0 变成可在 PC 上运行的原生程序。**

**⭐⭐ 核心的技术取舍写在 README 第一段**：游戏本体是 AArch64 代码，**被提前翻译成 C 并在本地编译为原生可执行文件**；一个 runtime 实现了游戏期望的主机服务；**渲染器把图形工作与着色器翻译给 WebGPU**。

**⭐⭐⭐ 但 README 立刻给这句技术路线加了一句限定，这一句是本档案最看重的地方**：

> **「This is a game-specific port, not a general-purpose Switch emulator. Some graphics translation still happens at runtime.」**

**即：它主动声明「我不是通用模拟器」——这把「静态重编译」这条路线的真实边界写在了最前面，而不是藏在 FAQ 里。**

**⭐⭐ 而它的第二个问题是「怎么让一个 5.6 GB 的项目在别人的机器上真的能被构建出来」——它给出的答案异常具体，具体到内存占用公式。**

## 为什么值得关注（2026-11-03）

- **⭐⭐⭐ 它的构建资源要求被写成了一个可计算的数字**：「Allow **at least 45 GB free in addition to the original game dump** for intermediate files and the separate packaged RomFS; the build is CPU- and memory-intensive. It runs **as many compiles at once as fit in 80% of your RAM at 3.5 GB each**（three on a 16 GB PC）；set `RX_JOBS=<n>` to choose.」
  **⭐⭐ 这三句话各自解决一个真实问题**：空间（45 GB）、并发策略（80% RAM）、以及**为什么默认是 3 个而不是更多**（3.5 GB × 3 = 10.5 GB ≈ 16 GB 的 66%，留出余量）。**「每个编译任务 3.5 GB」这种数字通常不会出现在文档里——它出现在真正跑通过的人手里。**
- **⭐⭐⭐ 它的失败模式分级非常清楚，且**每一条都写明了「会不会自己动」**：
  - 「**Python or `lz4` missing:** install them for the Python on PATH, then reopen the tools prompt」→ **需要你动手**；
  - 「**Compiler, headers or libraries missing:** open the x64 Native Tools prompt and check that…」→ **需要你动手**；
  - 「**Wrong module or missing RomFS:** check the extracted folder layout and version. **A base-game ID match is not a complete integrity check.**」→ **需要你动手**；
  - 「**Existing output or stale/incomplete lift:** move the indicated package or build directory aside, **preserving `user/` first**, then retry.」→ **需要你动手，而且顺序错了会丢存档**；
  - 「**"Not enough memory left" after long play:** older builds kept every render pipeline used in the last 10 minutes, which reached **about 14,000 pipelines and 17 GB of memory in one report (issue #10)**」→ **⭐⭐ 这是唯一一个已经被修掉的历史 bug，且它同时给出了修复后的机制**：「Past 9000 pipelines, the ones unused for a minute are now released（`RX_PIPELINE_HARD_CAP=<n>` 和 `RX_PIPELINE_HARD_TTL=<s>` 可改）」；
  - 「**GPU device lost or wrong GPU:** AMD cards lost the WebGPU device at startup while the GPU ASTC decoder was created（**issue #1; fixed**）」→ **已修，且给了环境变量**（`RX_WGPU_LOG=info|debug|trace`、`RX_ADAPTER=Radeon` 选 GPU、`RX_ASTC_CPU=1` 用 CPU 解 ASTC）；
  - 「**Crash or graphics issue:** note the game version, hardware, driver, location and settings.」→ **需要你动手**。
  **⭐⭐⭐ 关键在于：这七条的分类不是「按症状」而是「按责任」——六条要用户动手，一条已修。这个分法让读者一眼知道「哪里还没好」。**
- **⭐⭐⭐ 它的流水线缓存机制被写成了「能做什么/不能做什么」**：「**The native pipeline cache helps prepare previously encountered pipelines on later launches; it cannot guarantee stutter-free play.**」——**⭐⭐ 同时在故障排查里再次重复这句边界**。**同一句限制在两处出现，且都不弱化，这是本日最好的文档纪律之一。**
- **⭐⭐⭐ 它的可移植性策略是本批唯一做了「跨平台 × 跨图形栈」的**：Linux 上**不打 `build.bat`，而是 `python build_game.py`**，产物是 ELF；**Windows 用打包的 `wgpu_native.dll` + `SDL2.dll`，Linux 用系统 SDL3 + FFmpeg + 一个自己编译的打过补丁的 `libwgpu_native.so`**。**⭐ 这是一个有意思的分层：图形栈（wgpu）是自己编的，而窗口与媒体层（SDL/FFmpeg）在 Linux 上是系统的。**
- **⭐⭐⭐ 它的 wgpu 补丁流程被写成了完整可复现的 5 步命令序列**，且**版本被钉死**：
  ```
  git clone --recurse-submodules --branch v29.0.1.1 https://github.com/gfx-rs/wgpu-native.git
  git clone --branch v29.0.3 https://github.com/gfx-rs/wgpu.git wgpu-patched
  git -C wgpu-native apply "$SKYBOUND/third_party/wgpu-native/totk-patches/wgpu-native-29.0.1.1.patch"
  patch -d wgpu-patched -p1 < "$SKYBOUND/third_party/wgpu-native/totk-patches/wgpu-29.0.3.patch"
  cargo build --release --manifest-path wgpu-native/Cargo.toml
  ```
  **⭐⭐ 值得单独指出的是：它同时维护了 wgpu-native v29.0.1.1 与 wgpu v29.0.3 两个不同版本号，并分别提供对应补丁——这说明补丁是针对具体版本写的，跨版本直接用会失败。README 还明写「The Windows DLL in that folder is the unmodified v29.0.1.1 release.」**
- **⭐⭐ 它把「绑定哪个游戏版本」的机制写成了可检查的规则**：构建脚本「**checks the `main` and `sdk` module build IDs** and a few RomFS directories」；**1.2.1 的适配方式被精确描述**：「Version 1.2.1 also builds from its own ExeFS and the RomFS with the update applied（**PR #19, contributed and tested by keno80: the build picks the hooks by the main module's build id**）；everything else in this README was tested on 1.0.0, and **other updates are not supported by the game-specific hooks**.」
  **⭐⭐⭐ 这是本日最值得抄的一条工程描述**：它同时说明了 (a) 适配范围、(b) **适配是怎么做的（按主模块 build id 选钩子）**、(c) 谁贡献并测试了它、(d) 什么不支持。**「other updates are not supported by the game-specific hooks」是一句把未来限制提前讲清的实话。**
- **⭐⭐ 它对「完整性检查」的边界非常明确**：「The checks do **not** verify the entire RomFS or guarantee that a dump is complete.」以及「**A base-game ID match is not a complete integrity check.**」——**⭐⭐⭐ 与很多项目把 build ID 匹配说成「完整性验证」不同，它两次主动降级自己的检查强度。**
- **⭐⭐⭐ 它的版权边界写得非常完整，且**给出了机制而不只是声明**：「No game files, generated game code, keys, firmware or saves are included in this source project. The build does not extract NSP or XCI files.」+「Keep your game files, generated code, executable package and saves private. **The `game/`, `build/` and `dist/` directories are Git-ignored, but check what you are publishing rather than relying on ignore rules alone.**」+「The generated standalone package contains copyrighted game-derived data and **must not be shared or committed**.」
  **⭐⭐ 「不要只依赖 .gitignore，自己检查你要发布的东西」——这句话是本档案在本日报见到的最实用的一条仓库安全建议。**
- **⭐⭐ 它对「构建产物被复用」的处理有明确的失效规则**：「The builder **reuses a completed lift only when its recorded game and lifter inputs match**. If the lift was interrupted or those inputs change, move the existing `build/` directory aside before retrying.」——**⭐⭐ 即缓存有正确的失效条件，而不是无条件复用。**
- **⭐⭐ 它拒绝覆盖已有产物的理由写得很实在**：「The script **refuses to overwrite a nonempty `dist/SkyboundTOTK/`**: move the existing package aside before a new build. **Copy its `user/` folder into the new package if you want to retain its saves and settings. Do not delete your only save backup.**」
  **⭐⭐⭐ 注意最后一句：**「Do not delete your only save backup.」**——**这不是技术文档的必然内容，这是一个见过存档丢失的人写下的警告。**
- **⭐⭐ 它的 Linux 故障排查里有一个非常具体的失败**：「**`mmap guest window` failed:** the log includes `errno`. **The runtime reserves a 4 GB window at a fixed address.** A restrictive `vm.overcommit_memory` setting can reject that reservation.」——**⭐⭐ 一个 Linux 特有的、只有真正跑过的人才会遇到的坑，且给出了内核参数这一层的原因。**
- **⭐⭐ 它对像素格式的失败做了兜底**：「**RX_ASTC_CPU=1** decodes ASTC textures on the CPU instead of the GPU」——**给 GPU 解码失败一条 CPU 退路。**
- **⭐⭐ 它明写自己不是通用模拟器、也不是完整移植**：README 第一段同时给出两句自我限制——「**Expect graphical problems and incomplete compatibility; a successful build does not guarantee a complete playthrough.**」+「This is a game-specific port, not a general-purpose Switch emulator.」**⭐⭐ 「构建成功 ≠ 能通关」这句话，很多项目只在 issue 里隐含表达。**
- **⭐⭐⭐ 它有一个真实的外部贡献且被点名**：`releases` API 返回 0 个（**没有发行版**），但 README 明确署名「**PR #19, contributed and tested by keno80**」——**⭐⭐⭐ 本批新项目里唯一一个在文档正文里给外部贡献者署名的项目**，而且不是泛泛的「thanks to contributors」，是**指名的、带测试责任的**（「contributed and tested by」）。

## 热度来源判断

**⭐ 热度是真实的，但本日几乎没有变化——这本身就是本批最有价值的一个对照样本。**

**⭐⭐⭐ 本日报同日抓到的两个数字必须并列看**：
- **485⭐（8 天前 392⭐）→ +93⭐（+23.7%）**——**温和**；
- **commits 32 → 32（未变）**、**contributors 4 → 4（未变）**、**releases 0 → 0（未变）**、**pushed_at 仍停在 2026-10-31T13:37:44Z（距快照 3 天）**。

**⭐⭐⭐ 这组数字的含义非常清楚：这是一个「star 还在缓慢涨、但代码已经三天没动」的项目。** 它与本批的农场形成**完美的对照组**——农场是「star 暴涨 + 代码不动」，SkyboundTotk 是「star 温和涨 + 代码不动」。**⭐ 关键区别在于：SkyboundTotk 的代码不动是因为它本来就做完了（一个能跑的移植 + 完整文档），而农场的代码不动是因为根本没有代码。**

**⭐⭐ 它的 fork/star 9.1%**（44 forks / 485⭐）——**在本批四个新项目里居中**（CivSwitch 21.0% > SkyboundTotk 9.1% > dsh-see-now 5.0% > stack-diagram 4.5%）。**⭐ 它的 9.1% 有明确用途**：**fork 出去改补丁、改构建脚本、改 runtime**——而它恰好把补丁放在了 `third_party/wgpu-native/totk-patches/` 这个可被直接 patch 的位置，**所以 fork 有具体的着力点**。
- **subs 17** 是本批新项目中**最高的**（CivSwitch 13、stack-diagram 2、dsh-see-now 0）。**⭐⭐ 17 个深度关注者 vs 485 星 = 3.5% 的关注/点赞比，偏高**——**对一个「已经做完、不再天天更新」的项目，这个比例反而是合理的**（关注它的人是会回来查文档的人）。
- **⭐⭐ 它有 12 个 open issue**（`open_issues_count`）——**这个数字本身就是「有人在用它并遇到问题」的最强信号之一**，且比 star 更能说明它是活的软件。

**⭐ 结论：热度真实、采用信号真实、但增长已经放缓。** 它已经从「star 驱动」进入了「issue 驱动」阶段——**这恰恰是研究快照类项目的正常形态。**

## 关键技术亮点

1. **⭐⭐⭐ 静态重编译 + 运行时服务模拟的两层结构**：AArch64 游戏代码**提前**翻成 C 并编译为本地原生可执行文件；runtime 提供游戏期望的主机服务。**⭐ README 明写「Some graphics translation still happens at runtime」——即不是纯 AOT，边界被如实标注。**
2. **⭐⭐⭐ WebGPU 而非 Vulkan 的图形路线**（本批四个 TotK 移植项目中唯一的一个）：渲染器把图形工作与着色器翻译给 WebGPU，底层是 **wgpu-native v29.0.1.1**（Windows 打包未修改的 DLL，Linux 用自己编译的补丁版 `.so`）。
3. **⭐⭐⭐ 两份针对特定版本的 wgpu 补丁**：`wgpu-native-29.0.1.1.patch` 与 `wgpu-29.0.3.patch`，分别对应 wgpu-native v29.0.1.1 与 wgpu v29.0.3。**⭐⭐ 这是「上游版本漂移成本」的显式承担方式——不追上游，而是钉住版本并自带补丁。**
4. **⭐⭐ Linux 上把 wgpu 与宿主库分层**：wgpu 自己用 Rust + libclang（bindgen）编译；SDL3 与 FFmpeg 走系统库（pkg-config 检查 `sdl3` / `libavformat` / `libavcodec` / `libavutil` / `libswscale`）；`libwgpu_native.so` 通过 `$ORIGIN` rpath 定位；`totk-mimalloc` 为可选 cargo feature。
5. **⭐⭐ 管线缓存与硬上限**：`rxcache/pipelines.bin` 存在可执行文件旁；旧版有「10 分钟内用过的管线全部保留」的泄漏（一次报告 14,000 条管线 / 17 GB 内存，issue #10），**新版在 9000 条之上开始释放 1 分钟未用的管线**，并提供 `RX_PIPELINE_HARD_CAP` 与 `RX_PIPELINE_HARD_TTL` 两个可调参数。
6. **⭐⭐ build ID 门控的游戏钩子**：构建脚本校验 `main` 与 `sdk` 模块的 build ID 与若干 RomFS 目录；**钩子按主模块 build id 选择**（1.2.1 的适配即由此而来，PR #19）。
7. **⭐⭐ 字节码级缓存失效规则**：lift 结果只在「记录的游戏输入与 lifter 输入都匹配」时才复用。
8. **⭐⭐ 显存窗口的固定地址预留**：runtime 在固定地址预留 **4 GB 窗口**，`mmap guest window failed` 的错误里带 `errno`；Linux 上 `vm.overcommit_memory` 过严会导致预留失败。
9. **⭐⭐ 像素格式与 ASTC 解码的探针化处理**：ASTC 可强制走 CPU（`RX_ASTC_CPU=1`）；多 GPU 机器可用 `RX_ADAPTER` 指定；wgpu 自身日志由 `RX_WGPU_LOG` 控制。
10. **⭐⭐ 两平台统一的构建入口**：Windows `build.bat`（需 x64 Native Tools 命令提示符）；Linux `python build_game.py`（同一游戏文件、同一逻辑）。**⭐⭐⭐ 两个平台的 README 都重复了同一组 lift 复用 / 非空 `dist/` 拒绝 / `user/` 存档规则——即跨平台行为被刻意保持一致。**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 四层：① **游戏代码层**（AArch64 → C → 本地原生可执行，编译期完成）· ② **主机服务 runtime 层**（实现游戏期望的主机职责，含 4 GB 固定地址窗口与内存映射）· ③ **图形层**（渲染器 + 着色器翻译 → WebGPU，底层 wgpu-native，**部分图形翻译仍在运行时发生**）· ④ **构建与分发层**（`build.bat` / `build_game.py` → lift → 编译 → 打包 `dist/`，含管线缓存 `rxcache/`）。**法律边界是第五层且是硬边界**：仓库不含任何游戏文件/生成代码/密钥/固盘/存档，构建不解包 NSP 或 XCI，生成包含版权派生数据不得分享或提交 | 四层划分由 README 的分节（Game files and distribution / Build on Windows / Build on Linux / Patched wgpu-native）直接支持；**未核验** runtime 内部模块划分；**未核验**「部分图形翻译仍在运行时」具体指哪一部分；**⭐ 未核验** `a64-kit/` 与 `ports/` 的职责边界；**未核验** `third_party/` 除 wgpu 之外的内容 |
| 主路径 | ① 用户自备已提取且**未修改**的 1.0.0 ExeFS + RomFS（**必须是已提取的目录，构建不解包 NSP/XCI**）→ ② 布局必须严格是 `game/exefs/{main,main.npdm,rtld,sdk,...}` 与 `game/romfs/{ActorSystem,Event,...}`（README 明写「**must look like this, not `game/exefs/exefs/main`**」）→ ③ 准备工具链（Win：VS2022 Build Tools + Windows SDK + Clang/clang++/lld + emsdk 6.0.9 或 PATH 上的 LLVM + Python 3.10+ 与 lz4；Linux：clang/lld/pkg-config/python3/lz4 + SDL3 + FFmpeg dev + Rust 1.93+ 与 libclang）→ ④ Linux 额外一步：按 5 步命令编译补丁版 `libwgpu_native.so` 并拷入 `third_party/wgpu-native/lib/` → ⑤ 运行 `build.bat` / `python build_game.py` → ⑥ 脚本校验 build ID 与 RomFS 目录 → ⑦ lift（耗时很长）→ ⑧ 并发编译（3.5 GB/任务，80% RAM 预算）→ ⑨ 打包 `dist/SkyboundTOTK/`（含 `image.bin`、`image.json`、`romfs/`、图形库、SDL、FFmpeg）→ ⑩ 启动（目录可整体搬移，不需原 `game/` 目录，Linux 也不需 Wine）→ ⑪ 存档在 `user/`，渲染器设置在 `user/present.txt` | ①–⑪ 由 README 明文支持；**⭐ 未核验** 「45 GB」与「3.5 GB/任务」的测量环境；**未核验** lift 的实际耗时；**未核验**「build id 与若干 RomFS 目录」的具体校验项清单；**⭐ ① 的「已提取且未修改」是用户侧最重的前置**；**⭐⭐ 「README 目录结构必须精确匹配」是本档案见到的最易踩的构建失败点**（README 明写反例） |
| 关键权衡 | **① 静态重编译而非模拟器**——换来无解释器开销，代价是**绑定特定游戏版本**（本作绑 base 1.0.0，1.2.1 靠 build-id 门控钩子，「other updates are not supported」）；**② WebGPU 而非 Vulkan**——换来一套跨平台的现代图形抽象与**可编译的补丁路径**（wgpu 是 Rust，补丁是 diff），代价是**必须自己维护 wgpu 补丁并钉死版本**，且 **ASTC 等纹理解码路径与 GPU 设备行为成为新的故障面**（issue #1）；**③ Linux 上系统 SDL3/FFmpeg + 自编 wgpu**——换来更小的分发体与更少的平台代码，代价是**Linux 侧多出一次手工编 Rust 库的步骤**；**④ 构建期 AOT + 运行时部分图形翻译**——两边成本都付，README 明写；**⑤ 拒绝覆盖非空 `dist/`**——换来存档安全，代价是用户必须手动搬移目录 | ①–⑤ 的取舍方向由 README 明文支持；**⭐⭐ ① 与 COGBox 的「强制 TU6」构成一对可直接对照的版本策略**（见架构启发）；**② 的长期维护成本是本项目最实在的风险**——它被绑定在上游 wgpu 的版本节奏上；**⭐ ② 的代价有实测支撑**：AMD 显卡在 GPU ASTC 解码器创建时丢失 WebGPU 设备（issue #1，已修）——**这是「选了 WebGPU 就要处理的新故障面」的实例**；**④ 的边界未量化**（哪部分图形翻译在运行时，未核验） |
| 最小 PoC | ① **只做 Windows 路径**，跳过 Linux（省掉编 Rust 库的一整套步骤）→ ② 用 `game/` 布局严格对齐 README 的示例（**先确认 `exefs/main` 与 `sdk` 都在**）→ ③ 显式设 `RX_JOBS=2`（**不要用默认的「80% RAM ÷ 3.5 GB」**，16 GB 机器上默认是 3 个，留余量）→ ④ 构建完成后**先只启动一次**，确认渲染器初始化与 RomFS 加载成功（README 明说这一步**不验证完整游戏性或图形正确性**）→ ⑤ 确认 `user/` 目录已生成 → ⑥ 之后才进游戏 → ⑦ 出现 stutter 先归因到管线编译（README 明说首遇场景会 stutter，缓存只能缓解不能保证无卡顿） | PoC 的**顺序由 README 的分节顺序与三处「已修/需你动手」的分类反推**；**⭐ ③ 的 `RX_JOBS=2` 是本档案的建议而非 README 建议**（README 给的是自动策略 + 可覆盖的环境变量）；**⭐⭐ ④ 的期望结果被严格限定为「渲染器初始化 + RomFS 加载成功」，不是「游戏能玩」**——这是 README 自己划的线；**退出路径**：删除 `dist/SkyboundTOTK/` 即可，**但必须先复制 `user/`**（README 明写「Do not delete your only save backup」） |
| 证据边界 | 见下方专节 | 见档案末尾「证据边界」行 |

## 架构启发

**⭐⭐⭐ SkyboundTotk 的启发集中在「把不确定的东西分成三类并给每类不同的处理」——这是本日最值得学的一条文档方法。**

它的 README 里有三个可辨识的分类轴：

**① 责任轴（构建故障排查的七条）**——六条要用户动手（缺 Python/lz4、缺编译器、目录或版本不对、产物残留、崩溃要记信息），一条已修（管线泄漏、AMD 设备丢失）。**⭐ 这条轴直接回答了读者的第一个问题：「这活儿现在能不能干？」**

**② 强度轴（自陈的可靠性）**——从最强到最弱依次是：
- **已验证**：渲染器初始化 + RomFS 加载（README 明说这一点**没有**验证完整游戏性）；
- **已验证但有条件**：1.0.0 全部功能（README 的其余部分都基于 1.0.0 测试）；1.2.1 可构建（PR #19 贡献并测试）；
- **部分成立**：Linux 路径（README 明写 playtest 用的是默认 `--release` 构建，且需要自编 wgpu）；
- **不保证**：无卡顿（管线缓存「cannot guarantee stutter-free play」）、完整通关（「a successful build does not guarantee a complete playthrough」）、dump 完整性（「A base-game ID match is not a complete integrity check」）。

**⭐⭐⭐ 「已验证但有条件」这一档是大多数项目完全没有的**——它们要么说「支持」，要么说「实验性」，中间没有「在 1.0.0 上测过，但换版本就不行」这种精确表述。**

**③ 作用域轴（法律边界）**——仓库里有什么、没有什么、生成的东西能不能分享、`.gitignore` 靠不靠得住。**⭐⭐⭐ 「check what you are publishing rather than relying on ignore rules alone」这一句把「工具提供的保证」与「你仍然要承担的检查」明确分开——这是本日报所有项目里最清晰的一次责任划分。**

**⭐⭐⭐ 第二个启发：把「上游版本漂移」显式承担而不是隐式承受。**

SkyboundTotk 没有追 wgpu 的最新版本，而是**钉住 v29.0.1.1 / v29.0.3，并自带两份 diff 补丁**，且把「Windows 用未修改的官方 DLL、Linux 用补丁版」这件事写明。**这是一种很值得学的处理：当你的项目必须改上游时，把「改了哪一版、diff 在哪」变成仓库的一部分，而不是每次重新摸索。**

**⭐⭐ 但这个选择也有明确的代价，必须一并记住**：它把项目的生命周期**绑定到了 wgpu 的版本节奏上**。上游若继续演进、补丁若不再适用，SkyboundTotk 需要持续跟进——**而它的 commits 三天没动了。**（这是推断，不是事实：停滞的原因可能是工作完成、也可能是精力转移，README 与 commit 记录不足以区分。）

**⭐⭐ 第三个启发：跨平台的一致性比跨平台的支持更值钱。** README 的 Linux 一节明写「**Same game files and same `build_game.py` launcher as Windows**」，并把「lift 复用 / 非空 `dist/` 拒绝 / `user/` 存档」三条规则重复一遍。**⭐ 即：Linux 用户面对的不是「另一种玩法」，而是「同一套规则，命令不同」。**

**⭐⭐ 第四个启发（与 COGBox 对照）：版本绑定策略是架构选择，不是技术副产物。** 同一批里：
- **SkyboundTotk**：绑定 base 1.0.0，**允许** 1.2.1 但靠 build-id 门控钩子，且明说「other updates are not supported」；
- **COGBox**：**强制** TU6/TU4，**纯光盘版不再支持**，且 TU 出现在游戏安装目录的固定路径。

**两者的差别不是质量，是「用户要多做一步，还是作者要多做一步」。** 两个项目都用 README 把这个选择及其后果写清楚了——**这才是可比较的维度。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  subgraph INPUT[用户自备输入]
    EXE[已提取且未修改的<br/>1.0.0 ExeFS main/main.npdm/rtld/sdk]
    ROM[已提取且未修改的 RomFS<br/>ActorSystem / Event / ...]
    TUP[可选 1.2.1<br/>自己的 ExeFS + 打了更新的 RomFS]
    LAYOUT[目录必须严格匹配<br/>game/exefs/main 而非 game/exefs/exefs/main]
  end

  subgraph TOOLCHAIN[工具链准备]
    WIN_T[Windows: VS2022 Build Tools<br/>+ Windows SDK + Clang/clang++/lld<br/>+ emsdk 6.0.9 或 PATH LLVM<br/>+ Python 3.10+ 与 lz4]
    LIN_T[Linux: clang/lld/pkg-config/python3/lz4<br/>+ SDL3 dev + FFmpeg dev<br/>+ Rust 1.93+ 与 libclang]
    WGPU_BUILD[Linux 额外一步 5 步命令<br/>clone wgpu-native v29.0.1.1<br/>clone wgpu v29.0.3<br/>apply 两份版本对应补丁<br/>cargo build --release]
  end

  subgraph BUILD[构建层]
    ENTRY[build.bat (Win x64 Native Tools)<br/>build_game.py (Linux 同一逻辑)]
    CHECK[校验 main 与 sdk 的 build ID<br/>+ 若干 RomFS 目录<br/>不等于完整性验证]
    LIFT[Lift AArch64 → C<br/>耗时很长<br/>只在输入匹配时复用]
    COMPILE[并发编译<br/>3.5 GB 每任务<br/>80% RAM 预算 → 16GB 机器 3 个<br/>RX_JOBS 可覆盖]
    PACK[打包 dist/SkyboundTOTK/<br/>image.bin image.json romfs/<br/>+ 图形库 + SDL<br/>拒绝覆盖非空目录]
  end

  subgraph RUNTIME[运行层]
    EXE2[原生可执行文件<br/>Windows x64 或 ELF]
    SVC[主机服务 runtime<br/>含 4 GB 固定地址窗口 mmap<br/>部分图形翻译仍在运行时]
    REND[渲染器 → WebGPU<br/>经 wgpu-native<br/>ASTC 可强制 CPU 解码<br/>RX_ADAPTER 指定 GPU]
    PIPE[管线缓存 rxcache/pipelines.bin<br/>9000 之上释放 1 分钟未用<br/>RX_PIPELINE_HARD_CAP / _TTL]
    PRES[user/present.txt 渲染设置<br/>user/ 存档]
  end

  subgraph GRAPHICS[图形栈分层]
    DLL_WIN[Windows: 未修改的<br/>wgpu_native.dll v29.0.1.1<br/>+ SDL2.dll]
    SO_LIN[Linux: 自编补丁版 libwgpu_native.so<br/>SDL3 与 FFmpeg 走系统库<br/>$ORIGIN rpath 定位]
    PATCH1[wgpu-native-29.0.1.1.patch]
    PATCH2[wgpu-29.0.3.patch]
  end

  LEGAL[版权边界<br/>仓库不含游戏文件/生成代码/密钥/固盘/存档<br/>不解包 NSP 或 XCI<br/>生成包含版权派生数据 不得分享或提交<br/>不要只依赖 .gitignore 自己检查要发布的东西]

  EXE --> LAYOUT --> CHECK
  ROM --> LAYOUT
  TUP -.build-id 门控钩子.-> CHECK
  WIN_T --> ENTRY
  LIN_T --> ENTRY
  WGPU_BUILD --> SO_LIN
  PATCH1 --> WGPU_BUILD
  PATCH2 --> WGPU_BUILD
  CHECK --> LIFT --> COMPILE --> PACK
  PACK --> EXE2
  EXE2 --> SVC --> REND
  REND --> PIPE
  SVC --> PRES
  REND --> DLL_WIN
  REND --> SO_LIN
  DLL_WIN -.Win 路径.-> REND
  SO_LIN -.Linux 路径.-> REND
  LEGAL -.约束.-> BUILD
  LEGAL -.约束.-> RUNTIME
```

## 定位判断

**「一个把移植做完了、把文档写成了工程手册、但已经停止演进的成熟快照。」**

**⭐ 它在同题材 TotK 移植群里的位置（本日第四次记录该赛道）**：

| | SkyboundTotk | totk-pc-recomp | ultratears | COGBox |
|---|---|---|---|---|
| 图形栈 | **WebGPU（wgpu-native + 自带补丁）** | Vulkan | Vulkan | D3D12 |
| 目标版本 | base 1.0.0（+1.2.1 via build-id 钩子） | 1.4.3 | 1.4.3 | Gears TU6/TU4 |
| 分发 | **源码构建 → dist/（无发行版）** | 安装器 + 发行版 | AppImage | 启动器 + zip |
| 外部贡献 | **PR #19（贡献并测试，README 点名）** | PR 多条（oi 207） | PR 4 条（单作者） | 5 contributors |
| 成熟度信号 | **文档最完整** | 采用信号最强 | 承诺表最诚实 | 产品化最好 |

**⭐⭐⭐ 它的独特贡献是「它是这一批里唯一一个把「我做了什么、没做什么、什么条件下成立」写成三分级清单的」**——而这个清单（责任轴 / 强度轴 / 作用域轴）在其它三个项目里都只能部分找到。

**⭐⭐ 但它的位置有一个硬伤：它已经没有发行版（`releases` API 返回 0），因此它不是一个「装上就能用」的东西，而是一个「愿意自己搭工具链的人可以用」的东西。** 45 GB 磁盘、80% RAM 的并发预算、Rust + libclang 编 wgpu 的额外步骤——**⭐ 这些门槛把它的用户群压缩到了「想读源码并且有一台闲机器」的人。**

**⭐⭐⭐ 因此本档案的判断是：SkyboundTotk 的读者价值远大于用户价值。** 它是一份**关于「怎么把一个大规模移植项目写成别人能复现的文档」的样本**，而不是一个推荐使用的软件。

## 风险 / 局限 / 泡沫点

- **⭐⭐⭐ 上游 wgpu 绑定是最大的长期风险**：项目自带两份针对 v29.0.1.1 / v29.0.3 的补丁。**⭐ 补丁一旦与上游演进脱节，需要重做；且 Linux 用户必须自己完成这一步。**（这是基于其版本钉死策略的结构性推断，不是已发生的事实。）
- **⭐⭐⭐ 构建门槛极高**：45 GB 额外磁盘、3.5 GB/编译任务、80% RAM 预算、VS2022 + emsdk 6.0.9 + Python/lz4（Win）或 Rust 1.93 + libclang + SDL3/FFmpeg dev（Linux）、Linux 还要手工编 Rust 库。**⭐ 这些门槛对「想试试」的人是实质性的劝退。**
- **⭐⭐⭐ 目录结构必须精确匹配**：README 明写反例「must look like this, **not** `game/exefs/exefs/main` 或 `game/romfs/romfs/Event`」——**解压层级差一层就会失败，且报错信息未必直指这一点。**
- **⭐⭐⭐ 完整性检查是弱的**：只校验 build ID 与若干 RomFS 目录；README 两次明说「不验证整个 RomFS」「base-game ID match is not a complete integrity check」。**⭐ 即「构建通过」不等于「你的 dump 是完整的」。**
- **⭐⭐⭐ 无发行版**：用户必须自己从源码构建。**⭐ 这既是「源码可得」的纯粹性，也是可用性的硬门槛。**
- **⭐⭐ 明确的能力缺口**：README 明写「**Expect graphical problems and incomplete compatibility**」+「a successful build does not guarantee a complete playthrough」+「Some graphics translation still happens at runtime」+「It is not affiliated with Nintendo」。
- **⭐⭐ Linux 路径未在真机验证的迹象**：README 写「The playtest below used a default `--release` build」，且 `libwgpu_native.so`「is not in the repository」——**Linux 用户必须自建**。
- **⭐⭐ 版本白名单**：1.2.1 依赖 build-id 门控的钩子（PR #19），「other updates are not supported by the game-specific hooks」。**⭐ 这意味着游戏每次更新，这个项目都可能需要重做适配。**
- **⭐⭐⭐ 开发已停滞**：commits 32 → 32（未变）、pushed_at 停在 2026-10-31T13:37:44Z（快照前 3 天）、releases 0、contributors 4（未变）。**⭐ 这与 12 个 open issue 并存——有人在用，但没有人改。**（停滞原因不可核验。）
- **⭐ 12 个 open issue 未核验**：**本日报未逐条读取 issue 内容**，因此不能判断这些问题的严重程度。
- **⭐ 许可信息简化风险**：GitHub `license.spdx_id` 为 MIT，但 README 明写生成包「contains copyrighted game-derived data and must not be shared or committed」——**⭐ 仓库许可与产物许可不是一回事，后者受著作权约束。**
- **⭐ 热度判断**：485⭐ / +93⭐ in 8 days / subs 17 / fork-star 9.1%——**热度温和且有真实使用信号（12 open issues），但 8 天 +23.7% 说明它已不是上升期。**

## 与同类项目的关系

- **vs 本日同题材的 TotK 移植群**：见定位判断的对比表。**⭐ 最关键的差异是图形栈——它是四个里唯一走 WebGPU 的**，这带来「可编译的补丁路径」（Rust + diff）但也带来「ASTC 解码与 GPU 设备行为」这类新故障面。
- **vs gfx-rs/wgpu 与 wgpu-native（上游）**：**它不是从零实现图形栈，而是维护两个版本的上游补丁。** **⭐ 这是「下游项目如何与上游共存」的一个具体样本**：钉版本 + 自带 diff，而不是追最新版或 fork 整个上游。
- **vs COGBox（同为静态重编译，跨游戏）**：见架构启发的版本策略对照。**⭐⭐ COGBox 有发行版与启动器，SkyboundTotk 有源码与构建脚本——两者恰好是「产品化」与「可复现性」的两端。**
- **vs Ryujinx / RPCS3（模拟器）**：模拟器持续跟进主机固件与游戏版本；静态重编译把成本前置到编译期。**⭐ SkyboundTotk 的 build-id 门控钩子，正是静态重编译路线「必须跟版本」这一代价的具象化。**
- **vs Zero-Breach-Toolkit（本日同批）**：**同为安全取向的开源项目，但方向正交**——一个做「判断」（间谍软件痕迹），一个做「移植」（游戏）。**⭐ 值得并置的原因是它们对「不可核验性」的处理方式相反**：Zero-Breach 把「干净 ≠ 安全」写进产品输出；SkyboundTotk 把「构建成功 ≠ 通关」写进文档。**都是把不确定性外显。**
- **vs 本批农场仓库**：SkyboundTotk 8 天 +93⭐ 而 commits 不变，**与农场「star 暴涨 + 代码不动」的形态表面相似**——**⭐ 但两者的判别依据不同且都可核验**：农场是**当天新建、体积 ≤20KB、blob 数个位数**；SkyboundTotk 是 **8 天前已存在、586 个 blob、32 commits、17 subs、12 open issues**。**⭐⭐ 这组对比说明「star 涨而代码不动」本身不是判据，「代码不动」必须结合仓库年龄与结构来看。**

## 是否值得持续跟踪

**值得跟踪（作为「大型移植项目的文档工程样本」），但不建议作为软件采用。**

**⭐ 对本日报的研究目的**：**它提供了本日最完整的一份「分级诚实」样本**——把不确定的东西分成「要你动手 / 已修 / 不保证 / 有条件」四类并逐条给出。这与本日报已连续记录多日的「把边界写进可核验位置」主题完全同源（10-24 `docs/checks.md`、10-30 Zero-Breach `docs/VERIFYING.md`、本日 stack-diagram 的 agent 自查、dsh-see-now 的实测刻度表）。**⭐ SkyboundTotk 在这条线上的独特之处是：它把边界写成了可执行的构建指令，而不只是一份声明。**

**⭐⭐ 对想实际玩 TotK PC 移植的人**：**优先看 `totk-pc-recomp`（有发行版、25,735 次下载、207 个 open issue、多人参与）而不是 SkyboundTotk。** 本档案不推荐任何人尝试 SkyboundTotk 的完整构建路径，除非他就是想读一份大型移植的工程文档。

**⭐⭐ 对做图形栈下游的人**：**值得读它的 wgpu 补丁流程**（两份版本对应 diff + 5 步 cargo 构建）——这是「如何在上游不接受你的修改时继续维护」的可行模板。

**⭐ 观察优先级**：**① 12 个 open issue 是否有人回应**（这决定它是「停更但有生命」还是「停更且无人管」）；**② commits 是否重新动起来**（若 7 天后仍为 32，则可判定为实质归档）；**③ wgpu 上游是否继续演进到补丁不再适用**。

## 后续观察点

1. **⭐⭐⭐ 12 个 open issue 的内容与作者是否得到回应** —— **本日报未逐条读取**；这是判断「停更是否等于弃坑」的关键。**⭐ 注意 `open_issues_count` 12 与 `contributors` 4 之间的差：有人在用，但没有人改。**
2. **⭐⭐⭐ commits 是否重新增长** —— 当前 32 且三天未动。**⭐ 这是本档案最想观察的一项**，因为它决定这个项目是「已完成」还是「被放弃」。
3. **⭐⭐ wgpu 上游版本漂移** —— 补丁针对 v29.0.1.1 / v29.0.3；**上游若继续演进，需要重做补丁**。**这是它最实在的长期风险。**
4. **⭐⭐ Linux 路径是否被更多验证** —— `libwgpu_native.so` 不在仓库里，必须自编；**若社区开始分发预编译库，说明这条路径真的在被使用**。
5. **⭐ 1.2.1 之外的游戏更新是否被支持** —— README 明说「other updates are not supported by the game-specific hooks」；**观察是否出现按 build id 选钩子的通用化**。
6. **⭐ 是否出现发行版** —— `releases` API 返回 0。**一旦出现带预编译产物的发行版，它会从「读者价值」变成「用户价值」。**
7. **⭐ `a64-kit/` 与 `ports/` 的职责边界** —— **本档案未核验**；若它们是公开的移植工具链，则项目的复用价值会显著上升。

---
> 数据来源: GitHub REST/Search API（gh CLI 认证），UTC **2026-11-03T06:00Z** 单一快照 | Stars: 485 | Forks: 44 | Subscribers: 17 | Open Issues: 12 | License: MIT | 语言: C++ | 创建: 2026-10-27T23:23:07Z | pushed: 2026-10-31T13:37:44Z | 32 commits | contributors 4 人 | releases 0 个 | topics 0 | 5,633 KB
> 结构证据: 全树 586 blob（`truncated: false`）；根目录 `a64-kit/` / `build.bat` / `build_game.py` / `ports/` / `third_party/` / `NOTICE.md` / `LICENSE` / `README.md`；`third_party/wgpu-native/totk-patches/` 含 wgpu-native-29.0.1.1.patch 与 wgpu-29.0.3.patch；Windows 用未修改的 wgpu_native.dll v29.0.1.1 + SDL2.dll，Linux 需自编 libwgpu_native.so（Rust 1.93 + libclang bindgen）
> 证据边界: **未构建、未运行、未编译任何补丁**；`a64-kit/` 与 `ports/` 职责未核验；runtime 内部模块划分未核验；「部分图形翻译仍在运行时」具体所指未核验；lift 实际耗时与 45 GB / 3.5 GB 每任务的测量环境未核验；12 个 open issue 内容未逐条读取；Linux 路径未实测；485⭐ 的来源无法核验（`stargazers` 端点对本 token 返回 404），故只作总量记录；**⭐ 10-30 → 11-03 的 +93⭐ 是两次快照间的总量差，不是当日新增；同期 commits / contributors / releases 均未变**
