---
title: "boykopovar/AnyPS5"
slug: "boykopovar-anyps5"
date_added: "2026-10-06"
category: "工具型"
emoji: "🎮"
stars: "4874 stars"
stars_delta: "2 个月 4874⭐，fork 364，fork/star 7.5%；持续 GitHub Trending daily 列表 994⭐ today"
language: "C++"
score: 90
tags: ["anyps5", "boykopovar", "ps5", "ps5-porting", "game-porting", "linux", "windows", "relinker", "dynamic-library", "spir-v", "shader-recompiler", "vulkan", "sdl", "input-mapping", "gpl-2", "6293kb", "2-months"]
url: "https://github.com/boykopovar/AnyPS5"
---

# boykopovar/AnyPS5

## 一句话定位
PS5 可执行文件到 Linux/Windows 的自动 porting 工具——relinker 把 PS5 可执行转目标系统原生格式 + 系统 prx 库实现 + SPIR-V shader 重编译 + SDL 输入映射。

## 它解决的问题
2026 年 PS5 平台独占了大量游戏，PC 玩家苦于无官方移植路径。Wine / Proton 在 PS5 二进制上无解，传统模拟器（PSP2XBOX / Vita3K / Xenia）只能跑早期游戏且性能差。开发者需要 PS5→PC 的严肃工程化工具：`AnyPS5` 提供 **relinker 自动格式转换 + 实现 PS5 系统 prx 库供动态链接 + SPIR-V shader 重编译 + SDL 输入映射 + 进度仪表盘** —— 解决 **「PS5→PC 移植缺 relinker + 缺 prx 库 + 缺 shader 重编译工具链」** 的工程链缺口。目标是成为 PS5→Linux/Windows 移植方向的严肃工程化平台候选。

## 为什么值得关注
- **Stars:** 4,874（截至 2026-10-06），2 个月突破 4.8K，增速极快
- **Forks:** 364，社区贡献活跃（relinker 移植方向天然适合贡献）
- **Watchers:** 未明示
- **Open Issues:** 未明示
- **License:** GPL-2.0 only（interoperability, research, preservation, compatibility 用途边界）
- **语言:** C++
- **活跃度:** created 2026-08-03，pushed_at 2026-10-05，持续高活跃
- **规模:** 6.3MB
- **Topics:** 7 个覆盖（anyps5 / dynamic-library / game-porting / ps5 / ps5-tools / spir-v / vulkan）
- **Trending:** GitHub Trending daily 列表 994⭐ today

## 热度来源判断
AnyPS5 的热度是 **「PS5→PC 移植刚需 × relinker 自动 porting × prx 库函数实现 × SPIR-V shader 重编译 × 进度仪表盘可视化」** 的强劲组合。PS5 是 2026 年游戏独占最多的平台之一，但 PC 玩家没有官方移植路径——这种供需缺口是真实刚需。`relinker` + `prx 库函数实现` 把 PS5→PC 移植从「模拟器层」推到「自动格式转换 + 系统 prx 库动态链接」的严肃工程化形态；`SPIR-V shader 重编译` + `Spirv-Tools 验证` 保证 shader 翻译的严谨度；`Dreaming Sarah 在 GTX 1050 Ti 60fps` 是真实跑通证据。`2 个月 4874⭐` + `994⭐ today` 反映社区对 PS5→PC 移植严肃工程化方向的强烈兴趣。热度**真实且具严肃工程化潜力**——但需警惕：GPL-2.0 与 PS5 SDK / 商业游戏的兼容性边界、relinker 在多 PS5 executable 类型的覆盖广度、prx 库函数覆盖率（声明 vs 实际可用）、shader 重编译在多 shader 类型的覆盖广度均未在档案中明示。

## 关键技术亮点
1. **relinker 自动格式转换:** core/relinker 把 PS5 可执行转目标系统（Linux / Windows）原生格式（ELF / PE + DLL），无需 emulation
2. **系统 prx 库动态链接:** core/libs/prx 实现 PS5 系统 prx 库供动态链接，覆盖率由进度仪表盘 libraries 跟踪
3. **SPIR-V shader 重编译:** core/shader/recompiler/Recompiler.cpp 编译 SPIR-V，通过 Spirv-Tools 验证（`ANYPS5_ENABLE_SPIRV_TOOLS`）
4. **SDL 输入映射:** SDL-mapped game controllers + analog sticks + triggers + 键盘 / 鼠标 + anyps5-input.ini 配置
5. **verified games 验证:** Dreaming Sarah 2D platformer 在 GTX 1050 Ti / i5-7500 3.4GHz 稳定 60fps
6. **进度仪表盘:** 三个 SVG（libraries 函数覆盖率 + shaders 重编译覆盖率 + progress map），可视化严肃工程化进度
7. **严格 runtime_error:** Unsupported or unexpected states 严格抛 `std::runtime_error`，what() stderr + 进程终止（避免静默错误）
8. **完整文档:** docs/{user/USAGE, dev/BUILD, dev/TechnicalDebt, dev/CONVENTIONS}.md + COMPatibility list

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | PS5 可执行文件到 Linux/Windows 的自动 porting 工具；relinker 自动格式转换 + 系统 prx 库函数实现 + SPIR-V shader 重编译 + SDL 输入映射 + 进度仪表盘 | 仅基于 README 描述的 relinker + core/libs/prx + SPIR-V shader 重编译通过 Spirv-Tools 验证 + SDL 输入映射 + anyps5-input.ini + Dreaming Sarah 2D platformer GTX 1050 Ti 60fps + 进度仪表盘 libraries / shaders / progress map + GPL-2.0；具体 relinker 在多 PS5 executable 类型的覆盖广度、prx 库函数覆盖率（声明 vs 实际可用）、shader 重编译在多 shader 类型的覆盖广度未在档案中明示 |
| 主路径 | PS5 executable → relinker 转换 → 目标系统原生格式 + core/libs/prx 动态链接 + 加载 SPIR-V 重编译 shader + SDL 输入映射 + 进度仪表盘 → verified games 60fps | 主路径为档案语义抽象；具体 relinker 转换算法、prx 库函数实现深度、SPIR-V shader 重编译管线、SDL ↔ 手柄 / 键鼠 输入集成代码未在档案中讨论 |
| 关键权衡 | relinker 自动 porting 覆盖广度 vs 单 game 移植深度 + 系统 prx 库函数覆盖率 vs 单 SDK 优化 + SPIR-V shader 重编译覆盖广度 vs 单 shader 优化 + SDL 输入映射 vs 严格实现 + verified games 稳定性 vs 新 game 兼容性 + GPL-2.0 商用边界 vs 闭源 PS5 SDK 兼容性 | 档案明示 GPL-2.0 + This project is intended for interoperability, research, preservation, and compatibility purposes + It does not include, distribute, or require copyrighted software, firmware, cryptographic keys, or proprietary game data + Unsupported or unexpected states strictly throw std::runtime_error + Dreaming Sarah GTX 1050 Ti 60fps；具体 GPL-2.0 与 PS5 SDK / 商业游戏的边界、新 game 兼容性边界未在档案中讨论 |
| 最小 PoC | 在 Linux (Ubuntu 24.04) 或 Windows 11 上 git clone boykopovar/AnyPS5 + 按 docs/dev/BUILD.md 构建 + 跑 Dreaming Sarah 验证 SDL 输入映射 + 60fps；再尝试 verified games 列表中另一个游戏验证 prx 库函数覆盖广度；最后查进度仪表盘（libraries / shaders / progress map）看覆盖率 | PoC 范围由档案「relinker + 系统 prx 库 + SPIR-V shader 重编译 + SDL 输入映射 + 进度仪表盘」建议推导；具体 verified games 在多硬件的覆盖广度、shader 重编译在多 shader 类型的可用性未在档案中讨论 |

## 架构启发
AnyPS5 的核心启发是 **「跨平台 porting 应该用 relinker 而不是 emulator」**。传统 PS5→PC 移植方向走模拟器层（PSP2XBOX / Vita3K / Xenia），性能差且难以支持新硬件；新机制要求 **自动 relinker 把可执行转目标系统原生格式 + 实现 PS5 系统 prx 库供动态链接 + SPIR-V shader 重编译** —— 这是严肃工程化平台的方向，类比 Wine / Proton 在 Windows 二进制上的「翻译层 + thunk 库」范式。更深层的启发是：**游戏移植方向的关键不是模拟器，而是 prx 库函数覆盖率 + shader 重编译工具链**。2 个月 4874⭐ + 994⭐ today 显示这是真实严肃工程化信号——但能否持续，取决于 GPL-2.0 与 PS5 SDK / 商业游戏的兼容性边界、relinker 在多 PS5 executable 类型的覆盖广度、shader 重编译在多 shader 类型的可用性。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  PS5Exe[PS5 可执行文件] --> Relinker[relinker core/relinker<br/>自动转换目标系统原生格式]
  Relinker --> Linux[Linux Native ELF]
  Relinker --> Win[Windows Native PE + DLL]
  Linux --> Prx[core/libs/prx 系统 prx 库<br/>动态链接]
  Win --> Prx
  Prx --> Shader[SPIR-V shader 重编译<br/>Recompiler.cpp]
  Shader -.Spirv-Tools.-> Validate[ANYPS5_ENABLE_SPIRV_TOOLS<br/>通过 Spirv-Tools 验证]
  Linux --> SDL[SDL 输入映射<br/>手柄 / 键鼠 / anyps5-input.ini]
  Win --> SDL
  SDL --> Verified[Dreaming Sarah 2D platformer<br/>GTX 1050 Ti 60fps]
  Verified --> Compat[COMPatibility list<br/>verified games]
  Prx -.覆盖率.-> Lib[进度仪表盘<br/>libraries 函数覆盖率]
  Shader -.覆盖率.-> ShaderProg[进度仪表盘<br/>shaders 重编译覆盖率]
  Lib --> Map[progress map<br/>github.io 仪表盘]
  ShaderProg --> Map
  PS5Exe -.不支持.-> Error[Unsupported 抛 std::runtime_error<br/>what() stderr + 进程终止]
  Linux -.许可证.-> GPL[GPL-2.0 only<br/>interoperability research preservation]
  Win -.许可证.-> GPL
```

## 定位判断
**工具型项目（PS5→PC porting 严肃工程化平台候选）。** AnyPS5 不仅是一个 porting 工具，更试图成为 PS5→Linux/Windows 移植方向的 relinker 工具链平台——类似 Wine / Proton 在 Windows 二进制上的「翻译层 + thunk 库」范式。若成功，它会成为 PS5 移植方向的默认入口，具有工具级价值。2 个月 4874⭐ + 994⭐ today 已显示社区对 PS5→PC 移植严肃工程化方向的强烈兴趣。但"平台化"取决于关键问题：relinker 在多 PS5 executable 类型的覆盖广度、prx 库函数覆盖率、shader 重编译在多 shader 类型的可用性、GPL-2.0 与 PS5 SDK / 商业游戏的兼容性边界均未在档案中明示。目前定位是"PS5→PC porting relinker 严肃工程化先驱"，向平台演进是合理路径。

## 风险/局限/泡沫点
- **relinker 覆盖广度:** PS5 executable 类型多样（system app / game / utility），relinker 自动转换在多类型的覆盖广度未在档案中明示
- **prx 库函数覆盖率:** 进度仪表盘 libraries 显示「percentage of the functions known to the project so far (declared in core/libs/prx), not of every PS5 system function」，覆盖率（声明 vs 实际可用）未在档案中明示
- **shader 重编译覆盖广度:** SPIR-V 重编译在多 PS5 shader 类型的覆盖广度未在档案中明示
- **GPL-2.0 与 PS5 SDK / 商业游戏兼容性边界:** GPL-2.0 only + This project is intended for interoperability, research, preservation, and compatibility purposes + It does not include, distribute, or require copyrighted software, firmware, cryptographic keys, or proprietary game data —— 与 PS5 SDK / 商业游戏的兼容性边界未在档案中讨论
- **verified games 数量未明示:** graph 数据「Dreaming Sarah 2D platformer 在 GTX 1050 Ti 60fps」是唯一明确验证，其他游戏的稳定性未在档案中讨论
- **Windows 平台稳定性:** relinker 在 Windows 上的稳定性未在档案中明示（仅提及 Windows packages）
- **Discord 社区规模:** Discord BHFztBPUe 链接存在，但社区活跃度未在档案中明示

## 与同类项目的关系
- **vs PSP2XBOX / Vita3K / Xenia:** 那些是模拟器层；AnyPS5 是 relinker 自动 porting + prx 库函数实现，性能更好
- **vs Wine / Proton:** Wine / Proton 翻译 Windows 二进制；AnyPS5 翻译 PS5 二进制，思路相似
- **vs ShadPS4:** ShadPS4 是 PS4 模拟器；AnyPS5 走 PS5 relinker 路线
- **vs PCSX2 / RPCS3:** PCSX2 / RPCS3 是 PS2 / PS3 模拟器；AnyPS5 是 PS5 relinker
- **vs RPCSX:** RPCSX 也是 PS5 模拟器；AnyPS5 走 relinker 自动 porting 路线

## 是否值得持续跟踪
**值得跟踪（PS5→PC porting 严肃工程化方向）。** AnyPS5 代表了 PS5→Linux/Windows 移植方向的 relinker 自动 porting 严肃工程化诉求，无论其本身成败，这一方向是行业趋势。建议关注：relinker 在多 PS5 executable 类型的覆盖广度、prx 库函数覆盖率、GPL-2.0 与 PS5 SDK / 商业游戏的兼容性边界、shader 重编译在多 shader 类型的可用性、verified games 列表扩展。对 PC 玩家 / PS5→PC 移植开发者，这是 PS5 严肃工程化 porting 工具链的实用来源，值得直接采用。对游戏移植生态观察者，它是"relinker 自动 porting"赛道的头部样本。

## 后续观察点
- relinker 在多 PS5 executable 类型的覆盖广度（系统 app / game / utility）
- 系统 prx 库函数覆盖率（声明 vs 实际可用）
- SPIR-V shader 重编译在多 PS5 shader 类型的覆盖广度
- verified games 列表扩展（Dreaming Sarah 之外的兼容性验证）
- GPL-2.0 与 PS5 SDK / 商业游戏的兼容性边界（法律风险）
- Discord 社区活跃度（BHFztBPUe）
- 进度仪表盘（libraries / shaders / progress map）的更新频率
- 与 ShadPS4 / RPCSX 等 PS5 模拟器的对比（relinker vs emulator 性能差距）

---
> 数据来源: GitHub API (2026-10-06) | Stars: 4,874 | Forks: 364 | License: GPL-2.0 | 语言: C++ | 创建: 2026-08-03