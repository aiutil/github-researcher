---
title: "LoreanXavier/pt-pc"
slug: pt-pc
date_added: "2026-10-09"
category: "工具型"
emoji: "👻"
stars: "949 stars"
stars_delta: "2 天 949⭐ ⑂57 fork/star 6.0%"
language: "C++"
license: "NOASSERTION"
score: 85
tags: ["pt-pc", "loreanxavier", "p-t", "ps4-teaser", "kojima", "native-pc-port", "vulkan", "vulkan-1-3", "cusa01127", "ps4-dump", "dlss", "fsr", "xess", "rtx-ray-traces", "steam-deck", "steamos", "linux-glibc-2-38", "windows-10-11", "patreon", "cplusplus", "noassertion", "2-days"]
url: "https://github.com/LoreanXavier/pt-pc"
---

# LoreanXavier/pt-pc

## 一句话定位
P.T. 2014 PS4 试玩 demo 的 C++ 原生 PC 移植严肃工程化实现——把「P.T. 复刻」从「模拟器 / 闭源移植」推到「C++ 原生 PC 移植 + Vulkan 渲染器 + 读玩家自己的 PS4 dump + 完整关卡/模型/纹理/音效/脚本/过场 + Windows 10/11 + Linux glibc 2.38+ + SteamOS + Vulkan 1.3 + 可选 DLSS/FSR/XeSS + 麦克风收音 + patreon + NOASSERTION」严肃工程化形态。

## 它解决的问题
2026 年「P.T. 复刻」的痛点是 **「P.T. 是 2014 年小岛秀夫的 PS4 试玩 demo，被 Sony 在 2014 年从 PSN 下架后已成绝响 + 模拟器层性能受限 + 闭源移植法律风险 + 缺乏严肃工程化替代」**。LoreanXavier/pt-pc 直击这一痛点：把「P.T. 复刻」从「模拟器 / 闭源移植」推到「C++ 原生 PC 移植 + Vulkan 渲染器 + 读玩家自己的 PS4 dump + 完整关卡/模型/纹理/音效/脚本/过场 + voice part 完整 + Windows 10/11 + Linux glibc 2.38+ + SteamOS + Vulkan 1.3 + 可选 DLSS/FSR/XeSS + 麦克风收音（key=J 替代）」严肃工程化形态。解决的是 **「P.T. 严肃工程化 PC 移植 + 玩家自备 dump 版权干净路径 + Vulkan 渲染器 + 完整关卡/模型/纹理/音效/脚本/过场 + voice part 完整 + Steam Deck desktop 模式 + patreon 支持」** 的 P.T. 严肃工程化 PC 移植问题。

## 为什么值得关注（2026-10-09）
- **Stars:** 949（截至 2026-10-09），2 天 949⭐，fork 57，fork/star 6.0%（fork/star 中等，反映严肃工程化关注）
- **Forks:** 57（典型 fork 严肃工程化持续关注信号）
- **License:** NOASSERTION（第三方组件许可不明，需观察）
- **语言:** C++（原生 C++ + Vulkan 渲染器）
- **活跃度:** created 2026-10-07，2 天内冲到 949 推严肃工程化承诺
- **规模:** 24556 KB（严肃工程化典型规模）
- **Topics:** pt-pc / loreanxavier / p-t / ps4-teaser / kojima / native-pc-port / vulkan / vulkan-1-3 / cusa01127 / ps4-dump / dlss / fsr / xess / rtx-ray-traces / steam-deck / steamos / linux-glibc-2-38 / windows-10-11 / patreon / cplusplus / noassertion / 2-days（覆盖广）

## 热度来源判断
LoreanXavier/pt-pc 的热度是 **「P.T. 复刻真实需求 × 模拟器层性能受限 + 闭源移植法律风险 + 缺乏严肃工程化替代 × C++ 原生 PC 移植 + Vulkan 渲染器 + 玩家自备 dump 版权干净路径严肃工程化承诺 × Steam Deck desktop 模式 × patreon 支持严肃工程化承诺」** 的强劲组合。P.T. 是 2014 年小岛秀夫的 PS4 试玩 demo，被 Sony 在 2014 年从 PSN 下架后已成绝响，但 P.T. 在游戏史上地位重要（小岛秀夫的「寂静岭」后续线索）+ 玩家强烈需求 + 模拟器层性能受限 + 闭源移植法律风险 + 缺乏严肃工程化替代。LoreanXavier/pt-pc 直击这一真实需求，把「P.T. 复刻」从「模拟器 / 闭源移植」推到「C++ 原生 PC 移植 + Vulkan 渲染器 + 玩家自备 dump 版权干净路径 + Steam Deck desktop 模式 + patreon 支持」严肃工程化形态。热度**真实且具网络效应潜力**——但需警惕：NOASSERTION 许可边界需关注；Sony 法务反应是潜在风险；「Not an emulator」+ 「from the original's behaviour」描述需观察 Sony 是否认可为「clean-room」还是「derivative work」；patreon 经济模型依赖玩家持续付费；玩家自备 dump（CUSA01127）路径的版权清晰度依赖 Sony 是否采取行动。

## 关键技术亮点
1. **Native PC port of P.T., the 2014 PS4 teaser by Kojima Productions:** Not an emulator；game logic was rebuilt in C++ from the original's behaviour + The renderer is written on Vulkan
2. **读玩家自己的 PS4 dump:** every level, model, texture, sound, script and cutscene is read at run time from your own copy of the PS4 game + There is no game data in this repository and none in the installer
3. **完整游戏体验:** It plays the whole teaser from the first wake-up to the street, with the voice part included
4. **多平台支持:** Windows 10 or 11 (x64), or Linux x86-64 with glibc 2.38 or newer (Ubuntu 24.04, Debian 13, Fedora 39, current Arch and SteamOS)
5. **Vulkan 1.3 + 可选 DLSS/FSR/XeSS:** A GPU and driver with Vulkan 1.3 + DLSS needs a GeForce RTX card; FSR and XeSS run on any recent GPU + The settings page greys out what your machine cannot run and says why
6. **麦克风收音严肃工程化承诺:** A microphone for one part of the game, as on the PS4 + key=J 替代
7. **玩家自备 dump 路径:** Your own copy of P.T. The port is built and tested with the US release, CUSA01127, as a dump folder from your console or a fake PKG made from that dump + European and Japanese releases install too, with a note, but I have not seen their data myself + A store PKG cannot be used: it is encrypted for the console that owns it, and nothing here decrypts it
8. **完整安装路径:** Download the installer from the Releases page: P.T.PC.Port.Setup.exe on Windows, the Linux setup binary on Linux + Point it at your dump folder or fake PKG and at a destination folder + It copies the three game archives it needs (chunk1.psarc, texture.qar, pathid_list_ps4.bin) next to the port + Default Windows install path %LocalAppData%\Programs\P.T. PC Port + Linux chmod +x + setup binary
9. **完整配置路径:** Settings go to %APPDATA%\pt-port\pt\pt.ini on Windows and ~/.local/share/pt-port/pt/ on Linux, together with the save, the log (pt.log) and crash dumps + The game checks the Releases page for a newer version once at start; [network] check_updates = 0 turns that off
10. **完整控制路径:** Mouse and WASD, right mouse button to zoom, left button, Enter or E to interact, Esc for the pause menu, Alt+Enter for fullscreen, F10 for the PC settings + Any gamepad works as the PS4 pad
11. **Steam Deck desktop 模式支持:** On a Steam Deck install from desktop mode and add pt as a non-Steam game; it runs on SteamOS as it is
12. **patreon 经济模型:** If the port is worth something to you, you can support me on Patreon: patreon.com/loreanxavier. It keeps the testing hardware and the releases coming

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | P.T. 在 PC 上的严肃工程化原生移植，仓库是 C++ 原生代码 + Vulkan 渲染器 + 多平台安装路径 + Steam Deck desktop 模式支持 | 基于档案描述的完整组件栈；具体游戏逻辑重建方法、关卡/模型/纹理/音效/脚本/过场的源码获取方式、Vulkan 渲染器对 PS4 着色器的重实现路径未在档案中详细给出 |
| 主路径 | 玩家自备 CUSA01127 PS4 dump → installer (P.T.PC.Port.Setup.exe 或 Linux setup binary) → 拷贝 chunk1.psarc/texture.qar/pathid_list_ps4.bin → C++ 原生 PC 移植 + Vulkan 渲染器 → Windows 10/11 + Linux glibc 2.38+ (Ubuntu 24.04/Debian 13/Fedora 39/current Arch/SteamOS) | 主路径为档案语义抽象；具体 installer 实现、dump 路径的合规边界、Sony 法务态度、Steam Deck desktop 模式集成细节均待核验 |
| 关键权衡 | C++ 原生 PC 移植严肃工程化承诺 + 玩家自备 dump 版权干净路径 vs NOASSERTION 许可边界 vs Sony 法务风险 vs 「from the original's behaviour」+「Not an emulator」描述的合法性 vs patreon 经济模型可持续性 vs 「玩家需自备 PS4 dump」门槛 vs 麦克风收音严肃工程化承诺 | 档案明示 C++ 原生 + Vulkan + 玩家自备 dump + voice part 完整 + Steam Deck desktop 模式 + patreon；NOASSERTION 许可合规、Sony 法务风险、patreon 模式可持续性、麦克风收音实现未给出 |
| 最小 PoC | 安装 P.T.PC.Port.Setup.exe，指向 CUSA01127 dump，运行验证「first wake-up to the street」完整流程 + voice part 完整 + DLSS RTX/FSR/XeSS 设置 | PoC 范围、退出路径由档案「单渠道、最小风险、可审计」建议推导；具体测试场景、性能基准、SLO 指标待核验 |

## 架构启发
LoreanXavier/pt-pc 的核心启发是 **「P.T. 复刻应该从「模拟器 / 闭源移植」推到「C++ 原生 PC 移植 + Vulkan 渲染器 + 玩家自备 dump 版权干净路径 + 完整关卡/模型/纹理/音效/脚本/过场 + Windows 10/11 + Linux glibc 2.38+ + SteamOS + Vulkan 1.3 + 可选 DLSS/FSR/XeSS + 麦克风收音（key=J 替代）」严肃工程化形态，正如 Patreon 严肃工程化经济模型支持的独立开发者严肃工程化完整移植」**。P.T. 是 2014 年小岛秀夫的 PS4 试玩 demo，被 Sony 在 2014 年从 PSN 下架后已成绝响，但 P.T. 在游戏史上地位重要（小岛秀夫的「寂静岭」后续线索）+ 玩家强烈需求 + 模拟器层性能受限 + 闭源移植法律风险 + 缺乏严肃工程化替代。LoreanXavier/pt-pc + C++ 原生 PC 移植 + Vulkan 渲染器 + 玩家自备 dump 版权干净路径 + 完整关卡/模型/纹理/音效/脚本/过场 + voice part 完整 + Steam Deck desktop 模式 + patreon 支持严肃工程化承诺，反映「独立开发者 + 严肃工程化 + 玩家付费 patreon」严肃工程化经济模型支持的独立开发者严肃工程化完整移植方向。能否持续，取决于 Sony 法务反应 + NOASSERTION 许可合规边界 + patreon 经济模型可持续性 + 玩家自备 dump（CUSA01127）路径的版权清晰度。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Player[玩家自备 P.T. CUSA01127 US dump] --> Installer[P.T.PC.Port.Setup.exe Windows<br/>Linux setup binary]
  Installer --> Files[拷贝 chunk1.psarc + texture.qar + pathid_list_ps4.bin<br/>next to the port]
  Files --> Game[C++ 原生 PC 移植<br/>rebuilt in C++ from the original's behaviour]
  Game --> Render[Vulkan 渲染器<br/>Vulkan 1.3]
  Game --> Audio[音效 + voice part 完整]
  Render --> Upscale[可选 DLSS RTX/FSR/XeSS]
  Render --> OS[Windows 10/11 x64<br/>Linux glibc 2.38+<br/>Ubuntu 24.04/Debian 13/Fedora 39<br/>current Arch/SteamOS]
  Audio --> Mic[麦克风收音<br/>key=J 替代]
  Game --> Pad[游戏手柄 = PS4 pad<br/>button prompts follow whatever you used]
  Game --> Steam[Deck desktop 模式<br/>添加为 non-Steam game]
  Game -.配套.-> Settings[pt.ini %APPDATA%\pt-port\pt\<br/>~/.local/share/pt-port/pt/<br/>save + log pt.log + crash dumps<br/>[network] check_updates = 0 关闭自动更新]
  Game -.边界.-> Risk[Sony 法务风险<br/>NOASSERTION 许可合规边界<br/>patreon 经济模型可持续性<br/>玩家自备 dump 门槛]
```

## 定位判断
**工具型项目（P.T. 严肃工程化 PC 移植）。** LoreanXavier/pt-pc 不仅是 P.T. 移植，更试图成为「P.T. 严肃工程化 PC 移植 + 玩家自备 dump 版权干净路径 + 完整游戏体验 + Steam Deck desktop 模式 + patreon 经济模型支持」的完整严肃工程化形态。2 天 949⭐ + fork/star 6.0% 已显示市场强烈关注。但「Sony 法务反应 + NOASSERTION 许可合规边界 + patreon 经济模型可持续性 + 玩家自备 dump（CUSA01127）路径的版权清晰度」是长期可持续性的关键。目前定位是「最有影响力的 P.T. 严肃工程化 PC 移植 + patreon 经济模型支持」，向「P.T. 严肃工程化 PC 移植 + patreon 严肃工程化经济模型 + Sony 法务应对」演进是合理路径。

## 风险 / 局限 / 泡沫点
- **Sony 法务风险：** P.T. 是 Sony IP，LoreanXavier 「from the original's behaviour」+「Not an emulator」描述需观察 Sony 是否认可为「clean-room」还是「derivative work」；Sony 在 2014 年从 PSN 下架 P.T.，未来 Sony 是否采取行动不确定
- **NOASSERTION 许可边界：** 第三方组件许可不明，合规风险需关注
- **patreon 经济模型依赖玩家持续付费：** If the port is worth something to you, you can support me on Patreon: patreon.com/loreanxavier. It keeps the testing hardware and the releases coming + 独立开发者模式
- **玩家自备 dump（CUSA01127）门槛：** 玩家需自备 PS4 dump（CUSA01127 US release），欧洲和日本版本「install too, with a note, but I have not seen their data myself」实测覆盖有限
- **European/Japanese 版本未独立验证：** European and Japanese releases install too, with a note, but I have not seen their data myself
- **「Not an emulator」vs「from the original's behaviour」描述的法律含义需观察**
- **LoreanXavier 个人项目属性：** 个人维护 + patreon 资金模式，可持续性需观察

## 与同类项目的关系
- **vs 模拟器层 P.T. 移植：** 模拟器层性能受限；LoreanXavier/pt-pc 是 C++ 原生 PC 移植 + Vulkan 渲染器严肃工程化承诺
- **vs 闭源 P.T. 移植：** 闭源移植法律风险；LoreanXavier/pt-pc 是「Not an emulator」+「from the original's behaviour」+「player 需自备 dump」版权干净路径
- **vs 其他 patreon 经济模型支持的独立开发者严肃工程化移植：** 反映「独立开发者 + 严肃工程化 + 玩家付费 patreon」严肃工程化经济模型支持方向
- **vs 其他绝响游戏复活项目：** 类似 Bloodborne PC（droogie/bbhost）+ P.T. PC（droogie/bbhost 268⭐ 16 fork）+ PSP Web recomp（snuri00/psp-web-recomp 182⭐ 4 fork）+ GTA5 PC（shadany7824/playgta5 650⭐ 370 fork）等独立开发者严肃工程化移植方向

## 是否值得持续跟踪
**值得跟踪（P.T. 严肃工程化 PC 移植）。** LoreanXavier/pt-pc 代表了「绝响游戏严肃工程化 PC 移植 + patreon 经济模型 + 玩家自备 dump 版权干净路径」的诉求。建议关注：Sony 法务反应 + NOASSERTION 许可合规边界 + patreon 经济模型可持续性 + 玩家自备 dump（CUSA01127）路径的版权清晰度 + Steam Deck desktop 模式集成细节。对 P.T. 玩家，这个仓库是「P.T. 严肃工程化 PC 移植」的实用来源，值得直接采用。对游戏移植生态观察者，它是「P.T. 严肃工程化 PC 移植 + patreon 经济模型」赛道的头部样本。

## 后续观察点
- Sony 法务反应（2014 年下架后是否采取行动）
- NOASSERTION 许可合规边界
- patreon 经济模型可持续性
- 玩家自备 dump（CUSA01127）路径的版权清晰度
- European/Japanese 版本独立验证
- Steam Deck desktop 模式集成细节
- LoreanXavier 个人项目治理可持续性

---
*首次记录：2026-10-09*