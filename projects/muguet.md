---
title: "c22dev/muguet"
slug: muguet
date_added: "2026-10-11"
last_seen_date: "2026-10-13"
category: "工具型"
emoji: "🎮"
stars: "532 stars"
score: 85
tags: ["muguet","c22dev","gta-v","mach-o","wasm","wasmtime","wgpu","metal","arm64-native","jit","ios-jit","udp-multiplayer","altstore","xcodegen","xcode-26","apple-silicon","macos-14","ios-15","gpl-3","2-days"]
url: "https://github.com/c22dev/muguet"
---

# c22dev/muguet

## 一句话定位
Muguet 是「GTA V 在 iOS / macOS 上的原生 Mach-O 移植」——通过 wasmtime 把游戏的 WebAssembly 版本当 native app 跑，wgpu on Metal 接管图形，并加了一层 UDP multiplayer。

## 它解决的问题
Rockstar 在 Apple 平台上从未正式发布过 GTA V（macOS 早在 2019 年起就不被官方支持；iOS 完全没有官方版）。同时，许多大型应用只有 WebAssembly 版本（如 Blender Web / Godot Web / Three.js 应用），无法在 iOS/macOS 上以 native 体验跑。Muguet 探索了「**WebAssembly + wasmtime + wgpu on Metal = native app 体验**」这一路径：
- **绕过 web engine / WebGPU / Web Audio overhead：** wasmtime 直接跑 wasm，wgpu on Metal 接管图形
- **绕过 iOS JIT 麻烦：** iOS 上 JIT 启用需企业证书或开发者账户；Muguet 在 iOS 上把 wasm 在编译时打包进 binary
- **保留原生性能：** macOS 上首次启动把 wasm 编译为 arm64 native 并缓存
- **小型多人：** UDP 端口 47520 的简单多人模式

## 为什么值得关注（2026-10-11）
- **Stars:** 269（截至 2026-10-11），2 天累计
- **Forks:** 60，fork/star 22.3%（社区高活跃度——很可能是游戏爱好者群体）
- **License:** GPL-3.0（开源但闭源不可二次分发）
- **Language:** Rust（wasmtime + wgpu 客户端 + 服务端）
- **Size:** 612 KB（仓库精简——游戏资源由玩家自备）
- **创新点:** 把 web 版本（GTA V 的 wasm 移植）通过 wasmtime 直接跑成 native app，避开 web engine / WebGPU / Web Audio overhead
- **定位：** wasm → native 路径的「游戏移植」代表 + Apple Silicon 上 wasm 应用的新工作流

## 热度来源判断
c22dev/muguet 的热度是「**GTA V 在 Apple 平台的强需求 + wasm → native 路径的工程启发 + Rockstar 不在 Apple 平台补缺的真空**」的组合。GTA V 本身是史上最畅销游戏之一，Apple 平台上无官方版 = 庞大未满足需求。60 个 fork 反映社区极高参与——但需警惕：fork/star 22.3% 的高比例可能反映「游戏爱好者 fork 一下看看」而非真正的代码贡献。热度**真实且具工程启发价值**——但需警惕：GPL-3.0（不能用于商业/闭源二次分发）+ 玩家需要自己的 .zip（GTA V 资源）+ Rockstar 法律风险（虽然是「native port」但用了 wasm 仍可能触发 DMCA）+ 性能未观察（wasmtime vs native C++）+ 多人仅本地 UDP（非互联网）。

## 关键技术亮点
1. **wasmtime + wgpu on Metal 栈：** 绕过 JS engine / WebGPU / Web Audio overhead，让 wasm 版 GTA V 以 native 体验跑
2. **macOS 首次启动 arm64 native 编译并缓存：** 利用 Apple Silicon 性能，避免每次启动重编译
3. **iOS 编译时打包 binary（绕过 JIT 麻烦）：** 把 wasm 在编译时嵌入 binary，避免 iOS JIT 启用需企业证书的麻烦
4. **UDP 47520 multiplayer：** 简单但够用的小型多人模式（muguet-server 可在任意机器跑）
5. **玩家自己 .zip：** data/ + b/<build>/（含 game.wasm 和 shaders/）——避免 Rockstar 资源版权
6. **make-app.sh / make-ios.sh + xcodegen：** 完整构建脚本链
7. **AltStore 分发：** 避开 App Store 审核（SideStore 已知有问题）
8. **Apple Silicon + macOS 14+ + iOS 15+ 8GB+：** 现代 Apple 平台覆盖

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 把 WebAssembly 编译的 GTA V 游戏通过 wasmtime 跑成 native app，wgpu on Metal 接管图形，UDP 提供 multiplayer | 仅基于 README 列出的 wasmtime / wgpu / Metal / UDP 47520；具体 frame scheduler、input handling、网络协议、anti-cheat 未在档案中给出 |
| 主路径 | 用户跑 make-app.sh/make-ios.sh → 启动 Muguet.app → wasmtime 跑 game.wasm → wgpu on Metal 渲染 → muguet-server 提供 UDP multiplayer | 主路径来自 README 描述；具体 first-launch arm64 缓存位置、Metal shader 缓存、内存压力处理均待核验 |
| 关键权衡 | web → native（wasmtime/wgpu）vs native C++ 直接移植 vs 静态重编译路径 vs 第三方 native port（如 M-series Rosetta）+ GPL-3.0（开源但闭源不可）+ Rockstar 法律灰区 | 档案明示 wasm → native 路径；Rosetta 2 兼容性、Steam Deck / Linux 版本、iPad 分辨率适配未证实 |
| 最小 PoC | Apple Silicon Mac + macOS 14+ → brew install xcodegen + rustup 1.98.1 → ./make-app.sh → 启动 Muguet.app → 加载玩家自己的 .zip → 跑一段游戏 + 启动 muguet-server → 第二个玩家加入 | PoC 范围由 README「How does this work」反推；具体 macOS 14/15 兼容、性能基准 vs 原生 GTA V 路径待核验 |

## 架构启发
c22dev/muguet 的核心启发是 **「WebAssembly + native runtime（如 wasmtime/wgpu）可绕过 Apple App Store / 系统限制，让大型应用以 native 体验跑在 iOS/macOS 上」**。把 GTA V 的 web 版本（GTA V 的 wasm 移植）通过 wasmtime 直接跑成 native app，避免 web engine / WebGPU / Web Audio 这一层 overhead。这与「静态重编译 PSP / PS3 / PS4 / PS5 / Wii U / Xbox 360 / GameCube」社区的「native port」思路互补：**wasm native 是另一条把 web 应用跑成 native 的路径**。更深层的启发是：**wasmtime 已足够成熟，可在消费级游戏上提供可接受的 native 体验**——这为更多 wasm-only 应用（Blender Web / Godot Web / Three.js 应用 / 自研 wasm 应用）打开 native port 思路。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Player[玩家] --> Zip[玩家自己的 .zip<br/>data/ + b/<build>/<br/>game.wasm + shaders/]
  Zip --> Muguet[Muguet.app<br/>Rust + wasmtime + wgpu on Metal]
  Player --> AltStore[AltStore 分发<br/>绕开 App Store]
  AltStore --> Muguet
  Muguet --> wasmtime[wasmtime 跑 game.wasm<br/>不需 JS engine]
  Muguet --> wgpu[wgpu on Metal<br/>原生 Metal 图形]
  Muguet -.macOS 首次启动.-> Cache[arm64 native 编译并缓存]
  Muguet -.iOS.-> Bake[编译时打包 wasm 进 binary<br/>绕过 JIT 麻烦]
  Player2[第二个玩家<br/>同 port 玩家] --> UDP[UDP 端口 47520<br/>muguet-server]
  UDP --> Muguet
  Muguet -.GPL-3.0.-> Limit[闭源不可二次分发<br/>Rockstar 法律灰区]
  Muguet -.苹果平台.-> HW[Apple Silicon<br/>macOS 14+ / iOS 15+ 8GB+<br/>Xcode 26]
```

## 定位判断
**工具型项目（Apple 平台上的 wasm → native 游戏移植实验 + Apple Silicon 工程展示）。** c22dev/muguet 不仅是「让 GTA V 在 macOS 上跑起来」的 hack，更是「**wasm → native 路径在大型游戏上可不可行**」的工程展示。它把 wasmtime + wgpu on Metal 这条非主流路径在消费级游戏上跑了一遍，验证了可行性。其潜在演进路径：(1) 成为「wasm 应用 native port」的参考实现（类似 React Native 之于 mobile）；(2) 被用于其他 wasm-only 应用（Blender Web / Godot Web）；(3) c22dev 个人继续添加更多平台（iPad / Apple TV / Linux）。当前定位：「**wasm → native 在游戏上的严肃工程化验证**」。

## 风险 / 局限 / 泡沫点
- **GPL-3.0：** 不能用于商业/闭源二次分发——商业 Mac App Store 上架受限
- **Rockstar 法律灰区：** 虽是「native port」但用了 wasm 仍可能触发 DMCA（特别是分发版本）
- **玩家需要自己的 .zip：** 需找到 GTA V 资源（GTA V 资源分发本身涉及版权）
- **性能未观察：** wasmtime vs native C++（特别是 GPU 调用开销）
- **多人仅本地 UDP：** 非互联网 multiplayer（除非玩家自己跑 muguet-server + 公网 IP）
- **c22dev 个人项目：** 治理可持续性、安全更新、未观察
- **SideStore 已知有问题：** AltStore 是首选，但分发门槛仍较高
- **Limitations（GTA V 解锁任务绕过有问题 / 字体 / 文本缺失）：** README 自述的 limitations

## 与同类项目的关系
- **vs LoreanXavier/pt-pc：** pt-pc 是 P.T. 的 native PC 移植（静态重编译路径）；Muguet 是 GTA V 的 native Apple port（wasm → native 路径）
- **vs nullmoth/nvidia-macos-driver：** nvidia-macos-driver 是 NVIDIA Metal 驱动；Muguet 是 GTA V 的 Apple 平台移植（都涉及 Apple 平台的「不被官方支持」空间）
- **vs Rosetta 2：** Rosetta 2 跑 x86_64 macOS 应用；Muguet 跑 wasm（不同的桥接技术）
- **vs Static Recompilation（PS3/PS4/PS5/Xbox 360/GameCube）：** 静态重编译是 native → native；Muguet 是 wasm → native
- **vs Steam / Apple Arcade：** Steam/Apple Arcade 是官方游戏分发；Muguet 是非官方 native port（法律灰区）

## 是否值得持续跟踪
**值得跟踪（wasm → native 路径在游戏上的严肃工程化验证）。** c22dev/muguet 代表了「**wasm → native 路径**」在消费级游戏上的可行性验证——无论其本身成败，这一技术路径对 Apple 平台游戏移植、对 wasm 应用 native 化都有启发。建议关注：性能基准（wasmtime vs native C++）、是否被 DMCA、是否衍生出其他 wasm → native 应用、对 Godot Web / Blender Web 的启发。对 Apple Silicon Mac 用户，这是「在 macOS 上跑 GTA V」的开源路径；对 wasm 生态观察者，这是 wasmtime 成熟度的标杆。

## 后续观察点
- 性能基准（wasmtime vs native C++，特别是 GPU 调用开销）
- Rockstar 法律行动（DMCA、takedown）
- 是否被 GameCube / PS3 静态重编译社区借鉴
- wasm → native 路径在 Blender Web / Godot Web / Three.js 应用的复用
- c22dev 是否衍生出更通用的「wasm → Apple native port」工具
- iPad / Apple TV / Linux 版本扩展

---
> 数据来源: GitHub Search API + Repository API (2026-10-11) + README 公开摘录 | Stars: 269 | Forks: 60 | License: GPL-3.0 | 语言: Rust | 创建: 2026-10-09
