---
title: "quer3q/kraken-mount"
slug: "kraken-mount"
date_added: "2026-11-15"
last_seen_date: "2026-11-15"
category: "工具型"
emoji: "🗄️"
stars: "321 stars"
stars_delta: "⭐ 2026-11-15 建档（快照 2026-11-15 CST，仓库创建于 2026-11-13T07:25:37Z，约 39 小时）：321⭐ ⑂27 · **subs 8** · **oi 19** · **5 commits** · 1,602 KB · **57 个文件**（21 `.rs` + 10 `.c` + 3 `.toml` + 3 `.md` + 2 `.sh` + 2 `.png`）· Rust + C · **GPL-3.0** · **v0.0.1-beta** · 2 topics · User `quer3q`（账号 **2020-04-15** 创建，8 个公开仓库，0 followers，bio「Backend Engineer」）"
language: "Rust"
score: 89
tags: ["ps5", "rust", "elf-payload", "homebrew", "explicit-non-goals", "gpl-3.0", "supply-chain-hash"]
url: "https://github.com/quer3q/kraken-mount"
---

# quer3q/kraken-mount

## 一句话定位
**一个 PS5 上的 ELF payload：在主机与 USB/扩展硬盘上查找游戏，挂载调试 FPKG 与游戏目录** —— ⭐⭐⭐⭐⭐ 它的独特之处是**用 `DESIGN.md` 把「支持的来源只有三种」写成了一节标题，并在同一节里逐条说明「不支持什么」**，同时**把一个不自己构建的外部二进制（`ampr-emu-ng`）的 SHA256 校验写进了构建脚本**。

## 它解决的问题
**PS5 上没有官方的第三方游戏挂载机制。** ⭐⭐⭐⭐⭐ 使用者手上有的是三种形态的资产：dump-forge 出来的调试 FPKG `.pkg`、普通游戏目录（或被 zstd / LZ4 打包的目录）、以及分布在多个盘上的集合。⭐⭐⭐⭐⭐ kraken-mount 负责扫描这些位置、注册到主屏幕 tile、在启动时覆盖 fakelib 与共享的 `ampr-emu-ng` 目录。

## 为什么值得关注（2026-11-15）
⭐⭐⭐⭐⭐ **因为它是本数据集里把「非目标」写得最清楚的项目之一**，⭐⭐⭐⭐⭐ 并且**19 个 open issue 是本日四个真项目里最多的**。

⭐⭐⭐⭐⭐ **可核验事实一：`DESIGN.md` 用一节标题声明边界。**

原文（节标题与条目）：

> ## Supported sources (nothing else)
> - **FPKG**: a dump-forge debug `.pkg` file directly in a scan root. Sparse layout extents (holes: a kind-0x40 boundary up to the next boundary) are read as zeros.
> - **Folder**: a directory directly in a scan root with `eboot.bin` and `sce_sys/param.json`. Packing: `ampr_zstd.index` present = zstd, else `ampr_assets.index` = lz4, else plain.
> - Any drive. The cache is always on the internal SSD.

⭐⭐⭐⭐⭐ **「(nothing else)」这四个字在括号里** —— ⭐⭐⭐⭐⭐ 即「只支持这三种，没有第四种」被写成了标题的一部分。⭐⭐⭐⭐⭐ 并且「Sparse layout extents (holes …) are read as zeros」连稀疏布局的边界行为都写明了。

⭐⭐⭐⭐⭐ **可核验事实二：供应链边界被写进构建脚本。**

原文：

> The ampr-emu-ng runtime is **NOT built here**: its released `libSceAmpr.sprx` is bundled from `vendor/ampr-emu-ng/` (`VERSION`, `SHA256SUMS` from the GitHub release, **checked by `ps5/build.sh`**) and installed into `/data/krakenmount/ampr/` at start.

⭐⭐⭐⭐⭐ **即「我不构建这个二进制，我拉它的官方 release 并校验 SHA256」是一条被显式记录的供应链边界** —— ⭐⭐⭐⭐⭐ 按 11-13 记录的 `hikaku-extension` 判据（把上游 commit hash 写进文档），⭐⭐⭐⭐⭐ **这是同一条实践在二进制分发场景下的版本。** ⭐⭐⭐ ⚠️ **但 `vendor/ampr-emu-ng/` 目录未出现在 `git/trees` 输出中，因此「该目录确实含 `VERSION` 与 `SHA256SUMS`」本日报未能核验。**

⭐⭐⭐⭐⭐ **可核验事实三：授权来源的合法性边界写在 README 靠前位置。**

原文：「A `.pkg` must be a **plaintext debug FPKG from `dump-forge`**. A folder needs `eboot.bin` and `sce_sys/param.json`.」

⭐⭐⭐⭐⭐ **即它要求使用者自己提供合法转储的调试包，不提供任何获取途径。** ⭐⭐⭐⭐⭐ 这与 11-13 记录的 `super-odyssey-pc-recomp`（「**You must bring your own game**… requests for game files or keys will be closed」）⭐⭐⭐⭐⭐ 是同一种责任姿态。

⭐⭐⭐⭐⭐ **可核验事实四：19 个 open issue。**
⭐⭐⭐⭐⭐ 按 11-12 记录 `solo-to-team-skills`（9 个 issue）时确立的判据：**issue 的存在说明项目正在被真实使用与质疑，这是正信号。** ⭐⭐⭐⭐⭐ 本日四个真项目的 issue 数为 0 / 0 / 0 / **19**，⭐⭐⭐⭐⭐ kraken-mount 是唯一一个「有人真的在用它、并且在跟作者争论」的项目。⭐⭐⭐ ⚠️ **本日报未逐条打开这 19 个 issue 内容**，因此「issue 是真实使用信号」是推断而非实测。

⭐⭐⭐⭐⭐ **可核验事实五：运行期行为也被设计过。**
缓存路径 `/data/krakenmount/caches/<TITLE_ID>`、配置 `/data/krakenmount/config.toml`、日志 `/data/krakenmount/kraken.log`；⭐⭐⭐⭐⭐ 每个游戏会得到一个「<name> registered」通知与独立的主屏幕 tile；⭐⭐⭐⭐⭐ 且支持通过 `http://<ps5-ip>:8097/` 从电脑侧管理游戏、重建/删除、改设置、读日志。⭐⭐⭐⭐⭐ **最后这条尤其值得记 —— 它把「一个跑在游戏机上的 payload」做成了可从外部运维的服务。**

⭐⭐⭐⭐⭐ **可核验事实六：许可清晰，且有第三方声明。**
`license.spdx_id = GPL-3.0`，根目录有完整 `LICENSE`（GNU GPL v3 原文），⭐⭐⭐⭐⭐ 且额外有 `THIRD_PARTY_NOTICES` 文件与 README 里的致谢段（「`drakmor/ShadowMountPlus`: home-screen registration, the fakelib sandbox overlay and backports are ported from it」）。⭐⭐⭐⭐⭐ **这与本日 `super-odyssey-pc-recomp`（NOASSERTION 且根目录无 LICENSE 文件）形成整整一个档次的差距。**

## 热度来源判断
⭐⭐⭐⭐⭐ **真实需求 + 真实使用，且「低 fork/star + 高 subs + 高 issue」的组合在本日样本里是独特的。**

⭐⭐⭐⭐⭐ ⑂27 / 321⭐ = **fork/star 8.4%**；⭐⭐⭐⭐⭐ **subs 8** 相对 321⭐ = 2.5%（本日投放体的 subs 是 0–3，而本项目的订阅数在真实关注一侧）；⭐⭐⭐⭐⭐ **oi 19** 在 star 321 的规模下是极高的参与度。

⭐⭐⭐⭐⭐ owner `quer3q` 账号 **2020-04-15** 创建（6 年）、8 个公开仓库、bio「Backend Engineer」⭐⭐⭐⭐⭐ —— ⭐⭐⭐⭐⭐ **既不新、也非组织、也无账号聚集特征**，按 11-13 建立的判据完全不符合投放体特征。⭐⭐⭐⭐⭐ 且它自带一个独立工具链仓库 `quer3q/ampr-emu-ng`（README 提到「comes bundled」并指向 `github.com/quer3q/ampr-emu-ng`），⭐⭐⭐⭐⭐ **即作者是长期做 PS5 homebrew 的持续产出者，不是「投放当天现造的账号」。**

⭐⭐⭐⭐⭐ ⚠️ **未核验**：`ampr-emu-ng` 仓库本日报**未打开**（仅从 README 的引用确认其存在与作者归属一致）；⭐⭐⭐⭐⭐ **本项目涉及绕过 PS5 官方软件授权机制，本档案只记录其工程结构与文档做法，不评价其合法性，不提供使用指引。**

## 关键技术亮点
1. **Rust 编写的主 payload + C 的 PS5 兼容层**：21 个 `.rs` + 10 个 `.c`；`ps5/` 目录下有 `Dockerfile`、`build.sh`、`compat.c`、`entry.c` —— ⭐⭐⭐⭐⭐ **用 Docker 固定构建环境**，对交叉编译目标机代码是标准做法。
2. **workspace 化的 crate 拆分**：`crates/kraken-mount-pkg` 独立成 crate（含 `Cargo.lock`、`examples/ls.rs`），⭐⭐⭐⭐⭐ 其 `src/decoder/` 下有 `huff.rs` / `lz.rs` / `timing.rs` / `mod.rs` —— ⭐⭐⭐⭐⭐ **即 FPKG 的块解码被拆成独立模块并单独成 crate**。
3. **稀疏布局处理**：`DESIGN.md` 明写 sparse extents（holes）按零读取 ⭐⭐⭐⭐⭐ —— ⭐⭐⭐⭐⭐ 这是 FPKG 格式的一个具体边界，多数同类项目会跳过不提。
4. **多存储位置扫描**：`/data/homebrew`、`/data/etaHEN/games`、USB 根目录下的 `homebrew` / `etaHEN/games`；backports 放 `<scan root>/backports/<TITLE_ID>*`。
5. **配置与日志分离**：`config.toml` + `kraken.log` 分开，日志路径固定。
6. **外部 HTTP 管理面**（8097 端口）⭐⭐⭐⭐⭐ —— 对一个跑在游戏机上的 payload 来说，这是少见但极实用的设计。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 「PS5 侧的游戏挂载运行时」；边界 = 扫描根目录内的三种资产 + 一个外部 ampr-emu-ng 运行时 + 一个 8097 管理面；**主机内部 SSD 是缓存的唯一落点** | `DESIGN.md` 的「Supported sources (nothing else)」+ README 路径表；⚠️ **未在 PS5 上运行、未编译、未构建 Docker 镜像** |
| 主路径 | 启动 → 扫描各扫描根 → 按 `ampr_zstd.index` / `ampr_assets.index` 判定打包方式 → 解码 FPKG 或直接挂目录 → 写内部 SSD 缓存 → 注册主屏幕 tile → 启动时 overlay fakelib 与 ampr 目录 → 8097 提供管理界面 | 主路径由 `DESIGN.md` 与 README 的 1–5 步推导；⚠️ **未逐文件审阅 Rust/C 实现** |
| 关键权衡 | ①**自建 vs 借用运行时**：不构建 ampr-emu-ng，改为拉官方 release + SHA256 校验 —— 换供应链可信度，牺牲自举能力；②**缓存位置**：永远在内部 SSD —— 换可靠性，牺牲 USB 性能；③**支持面**：三种来源写死 —— 换明确性，牺牲通用性；④**许可**：GPL-3.0 + THIRD_PARTY_NOTICES —— 换可审计性，牺牲闭源嵌入 | 四个权衡的**存在**均由 DESIGN.md/README/许可证文件证实；**每项的实际代价本日报未评估**（未测性能、未核验校验是否真在构建时执行） |
| 最小 PoC | 在有 homebrew 环境的 PS5 上：放一个 dump-forge 调试 FPKG 到扫描根 → 用 elfldr（9021）发送 `kraken-mount.elf` → 观察主屏幕 tile → 开 8097 管理面 → 读日志 → 用 `ps5/build.sh`（需 Docker）本地复现构建并核对 SHA256 校验步骤 | PoC 范围由 README 的「How to」推导；**本日报未执行**（需 PS5 + homebrew 环境 + Docker） |

## 架构启发
⭐⭐⭐⭐⭐ **第一条：把「不支持什么」写成节标题的一部分。** ⭐⭐⭐⭐⭐ 「Supported sources (nothing else)」比任何一段免责文字都更有效 —— ⭐⭐⭐⭐⭐ **它在读者做错误预期之前就完成了筛选。**

⭐⭐⭐⭐⭐ **第二条：不为一个外部依赖重建供应链，而是绑定它的发布物并校验哈希。** ⭐⭐⭐⭐⭐ `VERSION` + `SHA256SUMS` + `checked by ps5/build.sh` 是一个可以照抄的三件套。

⭐⭐⭐⭐⭐ **第三条：把「不支持」的粒度写到格式级别。** ⭐⭐⭐⭐⭐ 「Sparse layout extents (holes: a kind-0x40 boundary up to the next boundary) are read as zeros」⭐⭐⭐⭐⭐ —— **大多数项目只写「支持 FPKG」，而这会让使用者误以为所有 FPKG 布局都正确。**

⭐⭐⭐⭐⭐ 第四条：**给一个跑在专用设备上的程序配一个外部管理面**（8097 + 日志 + TOML 配置），是本数据集里少见的成熟度信号。

## 架构图（MMD）

> 证据边界：结构取自 `DESIGN.md`、`README.md` 与 `git/trees` 文件清单；标注「实测」的为本日报直接读取到的内容，标注「待核验」的为推断。

```mermaid
flowchart LR
  subgraph Assets["扫描根 资产 三种 仅此三种"]
    FPKG["调试 FPKG .pkg<br/>必须来自 dump-forge<br/>稀疏 extents 按零读取"]
    Folder["游戏目录<br/>需 eboot.bin + sce_sys/param.json"]
    Packed["打包目录<br/>ampr_zstd.index → zstd<br/>ampr_assets.index → lz4<br/>否则普通目录"]
    Roots["扫描根位置<br/>/data/homebrew · /data/etaHEN/games<br/>homebrew · etaHEN/games · USB 根"]
    Backports["backports/<TITLE_ID>*"]
  end
  subgraph Payload["kraken-mount payload · Rust + C"]
    Scan["扫描器"]
    Dec["crates/kraken-mount-pkg<br/>FPKG reader + Kraken block decoder<br/>decoder/huff.rs · lz.rs · timing.rs"]
    Cache["内部 SSD 缓存<br/>/data/krakenmount/caches/<TITLE_ID><br/>DESIGN: cache is always on the internal SSD"]
    Reg["主屏幕 tile 注册<br/>每游戏一个 tile + registered 通知"]
    Overlay["启动时 overlay<br/>fakelib + 共享 ampr 目录<br/>ported from ShadowMountPlus"]
    Mgmt["管理面 http://<ps5-ip>:8097/<br/>重建 删除 改设置 读日志"]
    Cfg["config.toml + kraken.log"]
  end
  subgraph Supply["供应链"]
    Ampr["ampr-emu-ng<br/>不自行构建<br/>拉官方 release 的 libSceAmpr.sprx<br/>VERSION + SHA256SUMS<br/>checked by ps5/build.sh 待核验"]
    Vendor["vendor/ampr-emu-ng/<br/>未出现在 git/trees 待核验"]
    Docker["ps5/Dockerfile + build.sh<br/>可复现构建 需 Docker"]
  end
  Roots --> Scan
  FPKG --> Dec
  Folder --> Scan
  Packed --> Dec
  Backports --> Scan
  Scan --> Cache --> Reg
  Ampr -.安装到 /data/krakenmount/ampr/.-> Overlay
  Vendor --> Ampr
  Reg --> Overlay
  Payload -.启动.-> Overlay
  Overlay --> Mgmt
  Cfg -.配置与日志.-> Mgmt
  Ampr -.SHA256 校验.-> Docker
  Docker -.构建 kraken-mount.elf.-> Payload
```

## 定位判断
**工具型项目（主机侧 homebrew 运行时）。** ⭐⭐⭐⭐⭐ 在 PS5 侧「游戏挂载」这个细分位置上，它是本数据集里文档质量最高的样本 —— ⭐⭐⭐⭐⭐ **不是因为功能更强（它的功能范围被自己写死了），而是因为它的文档把「边界」「供应链」「许可」三件事都交代清楚了。** ⭐⭐⭐⭐⭐ 对照 11-13 记录的 `super-odyssey-pc-recomp`（同样的「静态重编译 / 需自备素材」定位，但 NOASSERTION 且无 LICENSE 文件），⭐⭐⭐⭐⭐ **两者之间的差距不在技术，在工程规范。**

## 风险/局限/泡沫点
- ⭐⭐⭐⭐⭐ **用途本身涉及绕过主机平台的官方软件授权机制** —— ⭐⭐⭐⭐⭐ 本档案只记录工程结构与文档做法，**不评价其合法性，也不提供任何使用指引**。
- ⭐⭐⭐⭐⭐ **强依赖外部生态**：`elfldr`（9021）、`ampr-emu-ng` 的 `.sprx`、`dump-forge` 产出的 FPKG —— ⭐⭐⭐⭐⭐ 任何一环变动都会让项目失效。
- ⭐⭐⭐⭐⭐ **功能面被自己写死**：只支持三种来源，⭐⭐⭐⭐⭐ 因此遇到新格式只能等待上游更新。
- ⭐⭐⭐⭐⭐ **「fakelib sandbox overlay」是移植来的**（源自 `drakmor/ShadowMountPlus`）⭐⭐⭐⭐⭐ —— **上游若变更该机制，此处需要跟进**；⭐⭐⭐ ⚠️ **归属关系本日报未独立核验**（仅读到 README 致谢段）。
- ⭐⭐⭐ ⚠️ **未核验项**：未编译、未在 PS5 上运行、未构建 Docker 镜像、未核验 `vendor/ampr-emu-ng/` 是否存在、未运行 `crates/kraken-mount-pkg` 的解码器、未逐条打开 19 个 issue。

## 与同类项目的关系
- **vs `drakmor/ShadowMountPlus`**：⭐⭐⭐⭐⭐ **本项目明确声明移植了它的 home-screen registration、fakelib sandbox overlay 与 backports** —— ⭐⭐⭐⭐⭐ 即两者是**继承关系而非竞争关系**。
- **vs `quer3q/ampr-emu-ng`**：同一作者的配套运行时项目，本项目**消费**它并校验其哈希。
- **vs 其他 PS5 payload 工具**：⭐⭐⭐⭐⭐ 多数同类项目是单文件 payload + 简短 README；⭐⭐⭐⭐⭐ kraken-mount 的差异在于**有 crate 拆分、有 DESIGN.md、有 Docker 构建、有外部管理面、有 SHA256 校验**。
- **vs 11-13 的 `super-odyssey-pc-recomp`** ⭐⭐⭐⭐⭐ 同为「需自备素材」的边界清晰型项目，⭐⭐⭐⭐⭐ **但本项目有 GPL-3.0 与 `THIRD_PARTY_NOTICES`，那个项目根目录没有 LICENSE 文件** —— ⭐⭐⭐⭐⭐ 差距在许可与第三方声明，不在功能。

## 是否值得持续跟踪
**值得跟踪（作为 PS5 homebrew 生态的活跃样本与文档规范样本）。** ⭐⭐⭐⭐⭐ 具体建议：
1. **做同类主机侧工具的人应抄它的 `DESIGN.md` 结构**：一节「Supported sources (nothing else)」+ 逐条边界 + 供应链声明 + 缓存位置；
2. **抄它的供应链三件套**：拉官方 release + 记 `VERSION` + 记 `SHA256SUMS` + 在构建脚本里校验；
3. 观察 19 个 issue 里的高频问题 —— 那会直接告诉你下一个版本该修什么；
4. 观察 `ampr-emu-ng` 的版本节奏（0.4.0 已在 2026-11-13 被 bundle），⭐⭐⭐⭐⭐ 它是判断本项目活跃度的最佳代理指标。

## 后续观察点
- 19 个 issue 的分布与关闭率（判断是「被真实使用」还是「只有人在提 issue」）
- `vendor/ampr-emu-ng/` 是否实际入库且 `ps5/build.sh` 的 SHA256 校验是否真的生效（⭐⭐⭐⭐⭐ 本档案最想确认但未能确认的一点）
- 是否发布 `v0.0.1-beta` 之后的版本，以及是否补上 i18n（提交标题提到「11 languages」）
- 稀疏 FPKG / 打包目录的支持是否扩展（`DESIGN.md` 的「nothing else」是否松动）
- 是否有其他工具开始采用同样的「拉 release + 校验哈希」依赖方式（若成为惯例，本档案的三件套建议价值上升）

---
> 数据来源: GitHub API (2026-11-15) | Stars: 321 | Forks: 27 | Subscribers: 8 | Open Issues: 19 | License: GPL-3.0 | 语言: Rust | 创建: 2026-11-13T07:25:37Z | release v0.0.1-beta | owner 创建: 2020-04-15T13:54:41Z
