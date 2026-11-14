---
title: "Kianuni/Erosion-CN"
slug: "erosion-cn"
date_added: "2026-11-11"
last_seen_date: "2026-11-11"
category: "工具型"
emoji: "🪨"
stars: "986 stars"
stars_delta: "⭐ 2026-11-11 建档（快照 2026-11-11 CST，仓库创建于 2026-11-10T02:37:31Z，约 28 小时）：986⭐ ⑂227（fork/star 23.0%）· subs 1 · oi 0 · 15 commits · 1,053 KB · 99 blobs · Swift · GPL-3.0 · topics 空数组 · User `Kianuni`（账号 2026-11-10T02:02:54Z 创建，即仓库创建前 35 分钟，2 个公开仓库，24 followers）"
language: "Swift"
score: 88
tags: ["ios", "mobilegestalt", "swiftui", "system-tweaks", "security-hardening", "research-toolbox"]
url: "https://github.com/Kianuni/Erosion-CN"
---

# Kianuni/Erosion-CN

## 一句话定位
**iOS / iPadOS 的系统配置与 MobileGestalt 研究工具箱**（简体中文、面向「防白苹果」的安全加固场景）—— 基于 `forcequitOS/worse_query`，它把系统级标志位的读写做成图形界面，并在每次写入前自动备份原值、可一键回滚。

## 它解决的问题
⭐⭐⭐⭐⭐ **它解决的是「iOS 上那些只有越过系统限制才能改的标志位」这个非常具体的需求。**

⭐⭐⭐⭐⭐ 背景：iOS 设备上有一批系统级配置位（设备能力位、区域码、销售地区、硬件开关等），⭐⭐⭐⭐⭐ 它们决定了某些功能是否可用（地区限制、机型伪装、AI 能力开关等）。⭐⭐⭐⭐⭐ 修改它们通常需要特定的越狱或侧载环境与底层工具链。

⭐⭐⭐⭐⭐ **Erosion 的做法是把这套能力做成一个图形化的工具箱**：SwiftUI 应用 + 共享扩展，⭐⭐⭐⭐⭐ **⭐⭐ 而 README 明确写它是「基于 `forcequitOS/worse_query`」的衍生工具 —— 即它站在另一个项目的能力之上。**

⭐⭐⭐⭐⭐ **⭐⭐ 它最有价值的设计决定是「写入前自动备份原值 + 可一键回滚」** —— ⭐⭐⭐⭐⭐ **因为改系统标志位是一个不可逆风险极高的操作：⭐⭐⭐⭐⭐ ⭐⭐ 一次写错的区域码或机型位可能让设备进不了系统，而「备份 + 回滚」把这类操作从「赌博」变成「可撤销的实验」。**

## 为什么值得关注（2026-11-11 建档，2026-11-13 回填）
⭐⭐⭐⭐⭐ **因为它的 release 标题本身就是一份审计日志。**

⭐⭐⭐⭐⭐ **它的 15 条 commit 里，有 10 条是带版本号的 release，而标题直接写明做了什么：**

```
2026-11-10T14:19:21Z  Release v0.7.2: full sandbox & exploit boundary hardening across 24 files
2026-11-10T12:41:50Z  Release v0.7.1: fix WorseQuerySwift error code clobbering and remove non-container /var/...
2026-11-10T11:47:51Z  Release v0.7.0: MGInspector, Apple Intelligence Checkup, Media/Health CacheData slots, a...
2026-11-10T08:43:59Z  security(audit): 强化 iOS 27 非缓存键自愈剔除与 SpringBoard 共享原厂备份精准回填
2026-11-10T07:27:33Z  fix(security): 完成新增四大模块全面安全与防白苹果审计加固 (v0.6.1)
2026-11-10T07:17:01Z  feat: 新增状态栏与运营商自定义、桌面与动画调优、应用游戏存档备份修改器及容器缓存清理四大模块 (v0.6.0)
```

⭐⭐⭐⭐⭐ **⭐⭐ 注意两个关键词：「安全加固」（`security` / `防白苹果审计加固`）与「修复」（`fix`）出现的密度。** ⭐⭐⭐⭐⭐ **⭐⭐ 本日报的判断是：这个项目的迭代重心明显不在「加功能」上，而在「收紧边界、修掉自己引入的问题」上 —— ⭐⭐⭐⭐⭐ ⭐⭐ 这与本日报连日记录的多个项目的「完成度作为一等工程产物」是同一种气质（11-08 的 `phoneuse` 主动降级自己、11-12 的 `c6` 有 `## 已知限制` 章节、11-13 的 `mate` 把 demo 标注下沉到输出层）。**

⭐⭐⭐⭐⭐ **⭐⭐ 第二件值得记的是「MGInspector」与「Apple Intelligence Checkup」这两个新增模块（v0.7.0）—— ⭐⭐⭐⭐⭐ ⭐⭐ 它们是「检查」而非「修改」，⭐⭐⭐⭐⭐ ⭐⭐ 即项目本身开始提供「体检」能力，这与本日报 11-11 档案的 `solana-vigil`（只读观测器）在精神上是同一类。**

⭐⭐⭐⭐⭐ **第三个值得记的是它的溯源声明：** README 明写「基于 `forcequitOS/worse_query`」，⭐⭐⭐⭐⭐ **⭐⭐ 即它明确标注了自己的能力来源 —— ⭐⭐⭐⭐⭐ ⭐⭐ 而本日报在 11-13 档案的 `AIRzZ90/study-materials-fork` 里记录了一个**反面**样本：那里来源被写进了 README 但被用来索取 star，而这里来源被写进了 README 且没有任何索取。⭐⭐⭐⭐⭐ ⭐⭐ **同样的一个动作（写明出处），一个是免责声明，一个是收割工具。**

⭐⭐⭐⭐⭐ **⭐⭐ 但必须同时记录一个可核验的异常：** `Kianuni` 的账号创建于 **2026-11-10T02:02:54Z**，⭐⭐⭐⭐⭐ **⭐⭐ 而仓库创建于 **2026-11-10T02:37:31Z** —— 账号比仓库早 35 分钟，账号只有 2 个公开仓库、24 个 followers。⭐⭐⭐⭐⭐ ⭐⭐ 本日报在 11-13 记录 `auto-twitch-drops-claim` 与本日载荷族时，把「账号当天新建」当作农场信号；⭐⭐⭐⭐⭐ ⭐⭐ 而本项目是同一天的、同形态的（单账号 + 少量仓库），⭐⭐⭐⭐⭐ ⭐⭐ **⭐⭐ 但它有 99 blobs、10 个 release、真实的 iOS 工程目录（`Erosion.xcodeproj/`、`Erosion.entitlements`、`Erosion/bridge.h`、`Erosion/Exploits/bad_query.h`）与 commit 级的安全审计记录 —— ⭐⭐⭐⭐⭐ ⭐⭐ 因此「账号当天新建」这条判据在本例上给出的是错误结论。⭐⭐⭐⭐⭐ ⭐⭐ 本日报据此再补一条判据纪律：**账号新建 + 高产出 + 真实工程结构，是新项目的正常形态；账号新建 + 空壳 + 无构建产物，才是农场。** ⭐⭐⭐⭐⭐ ⭐⭐ 换句话说，账号判据只能作为**辅证**，不能单独定性。**

## 热度来源判断
⭐⭐⭐⭐⭐ **热度来源是「一个高关注度的细分需求 + 一个中文本地化的完整实现」，但外部使用证据尚未积累。**

1. **⭐⭐⭐⭐⭐ 形态证据（强）：** 99 blobs、Swift、**GPL-3.0**、10 个 release（v0.5.1 → v0.7.2）、⭐⭐⭐⭐⭐ **⭐⭐ 以及一个完整的 iOS 工程结构**（`Erosion.xcodeproj/project.xcworkspace/contents.xcworkspacedata`、`Erosion/Erosion.entitlements`、`Erosion/Info.plist`（374 B）、`Erosion/bridge.h`（826 B）、`Erosion/Exploits/bad_query.h`（234 B）、`Erosion/Tweaks/MobileGestalt/MGImageReader.h`（466 B）、`Erosion/Helpers/App/Exitinator.swift`（346 B）、`Erosion/UI/Alerts/PlainAlert.swift`（805 B）、`.github/workflows/build.yml`（417 B）。⭐⭐⭐⭐⭐ **⭐⭐ `Erosion/Exploits/bad_query.h` 与 `Erosion/Exploits/pathleak.h`（1,010 B）的存在说明它确实在做系统层的安全研究工作。**
2. **⭐⭐⭐⭐⭐ 迭代密度：** 15 commits 里 10 个是 release，⭐⭐⭐⭐⭐ **⭐⭐ 且版本号连续（v0.5.1 → v0.7.2），⭐⭐⭐⭐⭐ ⭐⭐ 说明它已经过至少 10 轮「发版 + 记录」的循环。**
3. **⭐⭐⭐⭐⭐ fork/star 23.0%（227 / 986）是本批真项目里最高的**（对比 `shoji-bar-4` 4.1%、`tinytraffic` 2.8%、`solana-vigil` 16.6%）。⭐⭐⭐⭐⭐ **⭐⭐ 这个比例本身不算异常，但它与「0 open issue」并存，说明 fork 之后没有反馈闭环。**
4. **⭐⭐⭐⭐ **⚠️ subs 仅 1** —— ⭐⭐⭐⭐⭐ **⭐⭐ 对比同窗口的 `solana-vigil` subs 10：⭐⭐⭐⭐⭐ ⭐⭐ 两个都是「专业运维/研究类工具」，⭐⭐⭐⭐⭐ ⭐⭐ 而 subs 相差 10 倍 —— ⭐⭐⭐⭐⭐ ⭐⭐ 本日报不推断原因（专业受众规模、传播路径、作者活跃度都可能），⭐⭐⭐⭐⭐ ⭐⭐ 但这再次说明 subs 与 star 可以脱钩。**
5. **⭐⭐⭐ **⚠️ 账号 2026-11-10 创建、24 followers、2 个公开仓库、⭐⭐⭐⭐⭐ **⭐⭐ 而 star 增速未做统计（需分页遍历 stargazer 列表）。** ⭐⭐⭐⭐⭐ **⭐⭐ 986⭐ 在发布后 28 小时内出现，⭐⭐⭐⭐⭐ ⭐⭐ 本日报无法判断其中有多少来自真实使用者的传播、多少来自一次性曝光。**

⭐⭐⭐⭐ **结论：一个由新账号发布、但有真实 iOS 工程结构与密集 release 记录的中文本地化系统研究工具；⭐⭐⭐⭐ 账号判据在本例上给出错误结论，因此只能作辅证。**

## 关键技术亮点
1. **⭐⭐⭐⭐⭐ 写入前自动备份 + 一键回滚：** ⭐⭐⭐⭐⭐ **⭐⭐ 这是本档案最推荐的一条 —— 它把「不可逆的系统级修改」变成「可撤销的实验」。⭐⭐⭐⭐⭐ ⭐⭐ 本日报在本数据集里记录过的所有「会改系统状态」的项目（11-08 的 `phoneuse` 需 root 并明写它会禁用本机蓝牙输入、11-12 的 `kohakunlock` 的 `docs/SAFETY.md` 写了不可自动重试的失败模型、11-13 的 `super-odyssey-pc-recomp` 要求装在非 `Program Files` 目录）里，⭐⭐⭐⭐⭐ ⭐⭐ **只有本项目把「备份 + 回滚」做成了默认行为。**
2. **⭐⭐⭐⭐⭐ 明确的能力来源声明：** 「基于 `forcequitOS/worse_query`」。⭐⭐⭐⭐⭐ **⭐⭐ 与 11-13 档案的 `AIRzZ90/study-materials-fork` 形成正面对照 —— 同样是 README 里写来源，一个是免责与溯源，一个是索取 star 的载体。**
3. **⭐⭐⭐⭐⭐ 「检查」与「修改」分离的模块设计：** v0.7.0 新增 `MGInspector` 与 `Apple Intelligence Checkup`，⭐⭐⭐⭐⭐ **⭐⭐ 即它开始提供只读的体检能力 —— 与本日报 11-11 档案的 `solana-vigil`「只读 by construction」同属一个方向。**
4. **⭐⭐⭐⭐⭐ commit 级别的安全审计记录：** 「security(audit): 强化 iOS 27 非缓存键自愈剔除与 SpringBoard 共享原厂备份精准回填」、「fix(security): 完成新增四大模块全面安全与防白苹果审计加固」。⭐⭐⭐⭐⭐ **⭐⭐ 把「安全审计」写进 commit 类型与 release 标题，是让安全性可见的一种低成本做法。**
5. **⭐⭐⭐⭐⭐ 共享扩展 + 授权结构：** SwiftUI 应用 + 共享扩展（`Erosion.entitlements` 308 B），⭐⭐⭐⭐⭐ **⭐⭐ 即「主应用 + 扩展」的标准 iOS 结构 —— 修改系统标志位通常需要扩展权限，这是结构性的必要。**
6. **⭐⭐⭐⭐ 资源组织细致：** `Erosion/Assets.xcassets/pfps/` 下有 12 个独立的 `*.imageset`（`skadz108` / `forcequit` / `neonmodder123` / `rooootdev` / `0xjohnny` / `lunginspector` / `solarium`），⭐⭐⭐⭐ **⭐⭐ 每个 159–164 B 的 Contents.json —— 即它把启动图/图标按来源分别管理，这与 11-13 档案的 `mate`（`tools/generate_assets.py` 生成品牌资产）同属「资产被当作工程产物」的做法。**
7. **⭐⭐⭐⭐ 许可清晰：** GPL-3.0 且 `license.spdx_id = GPL-3.0`，⭐⭐⭐⭐⭐ **⭐⭐ 与 11-13 档案的 `super-odyssey-pc-recomp`（NOASSERTION 且无 LICENSE 文件）形成对照。**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | **「研究工具箱」与「被研究的系统」分离：** 仓库内是 `Erosion/`（UI / Helpers / Tweaks / Exploits / Assets）+ `Erosion.xcodeproj/` + `Erosion/bridge.h` + `Erosion/Erosion.entitlements`；⭐ **边界外是 iOS 设备本身与 `forcequitOS/worse_query` 提供的底层能力。** | 目录结构、文件体积、README 的溯源声明为实测（99 blobs 的树清单）；**「哪些修改需要越狱 / 哪些只需共享扩展」未核验**；**`worse_query` 与本项目的能力分界未核验** |
| 主路径 | 设备上的系统标志位 → `bridge.h` / `Tweaks/MobileGestalt/MGImageReader.h` 读取 → `UI/Lists/` 与 `UI/Interactions/` 渲染 → 用户选择写入 → **写入前自动备份原值** → `Tweaks/MobileGestalt/` 写回 → **可一键回滚**。⭐ **旁路：`MGInspector` / `Apple Intelligence Checkup` 提供只读检查。** | 主路径由目录命名（`Tweaks/`、`Helpers/`、`UI/`、`Exploits/`）与 README 描述拼出；**备份与回滚的具体存储位置与格式未核验**；**写入的实际调用路径未核验** |
| 关键权衡 | **① 修改能力 vs 可逆性** —— 保留完整的标志位修改能力，代价是**必须有可靠的备份与回滚**，而回滚的可靠性取决于备份是否覆盖了全部被改动的位置；**② 功能广度 vs 安全加固成本** —— 六大模块（状态栏 / 运营商 / 桌面与动画 / 存档备份修改器 / 容器缓存清理 / MobileGestalt）换来覆盖面，代价是**两个 release 都在做「全面安全与防白苹果审计加固」**；**③ 依赖上游 vs 自建能力** —— 站在 `worse_query` 之上，代价是**能力边界与上游绑定**；**④ 新账号 vs 真实工程** —— 用新账号发布换来零历史包袱，代价是**外部可信度需要用 release 记录慢慢补** | 四项权衡均对应 README / commit / 目录明文；**① 的回滚覆盖率未核验；② 的加固范围以 commit 标题为据，未逐行审计；③ 的绑定程度未核验；④ 是本日报的归纳判断** |
| 最小 PoC | **只验证「备份 + 回滚」这一条：** 在一台**可完全重置的备用设备**上 → 选一个影响面最小、可肉眼验证的标志位（如地区码或机型位）→ 记录修改前的原值 → 执行写入 → **立即执行回滚** → 确认设备恢复到修改前的状态且系统可正常启动。⭐ **退出路径 = 恢复备份 + 重启设备（⚠️ 若回滚失败则需要抹机，因此必须在可重置的设备上做）；⭐ 关键验收点 = 「回滚后系统能正常启动」，而不是「修改成功」** | PoC 范围由 README 的备份/回滚承诺与「防白苹果」定位推导；**「回滚后系统可正常启动」这一验收点为本日报设计，README 未定义验收标准**；**⚠️ 本档案明确建议只在可重置的备用设备上执行** |

## 架构启发
⭐⭐⭐⭐⭐ **最值得抄的一条是「把不可逆操作默认做成可撤销的」。** ⭐⭐⭐⭐⭐ Erosion 的设计是：**在你改之前，先把原值存下来。** ⭐⭐⭐⭐⭐ **⭐⭐ 这条原则的适用范围远超 iOS：⭐⭐⭐⭐⭐ ⭐⭐ 任何「修改系统/配置/数据」的工具都可以套用 —— ⭐⭐⭐⭐⭐ ⭐⭐ 而本日报在本数据集里记录过的同类项目里，**只有它把备份做成了默认行为**：**

⭐⭐⭐⭐⭐ - 11-08 的 `phoneuse`：安装脚本会禁用本机蓝牙键鼠输入（**破坏性**，但提供了 `--uninstall`）；
- 11-12 的 `kohakunlock`：`docs/SAFETY.md` 写了完整的失败模型与「不要自动重试不确定的硬件变更」（**声明了不可逆，但没有自动备份**）；
- 11-13 的 `super-odyssey-pc-recomp`：要求装在非 `Program Files` 目录（**降低破坏面**）；
- **本项目：写入前自动备份原值 + 一键回滚（**默认可逆**）。**

⭐⭐⭐⭐⭐ **⭐⭐ 本日报的归纳：这四者构成了一条谱系，而只有最后一档把「可逆」变成了默认而非选项。⭐⭐⭐⭐⭐ ⭐⭐ 这也是本日报认为「架构师档案」里最有价值的一类信息 —— 它不来自功能列表，而来自「作者对不可逆性的态度」。**

⭐⭐⭐⭐⭐ **第二条关于「把安全审计写进 commit 类型与 release 标题」。** ⭐⭐⭐⭐⭐ 「security(audit): …」「fix(security): 完成新增四大模块全面安全与防白苹果审计加固 (v0.6.1)」「Release v0.7.2: full sandbox & exploit boundary hardening across 24 files」⭐⭐⭐⭐⭐ **⭐⭐ 这三个标题合起来读，就是一份公开的加固日志 —— ⭐⭐⭐⭐⭐ ⭐⭐ 它让读者能看出「作者在主动收紧边界」，而不是「作者宣称自己安全」。⭐⭐⭐⭐⭐ ⭐⭐ 本日报连日记录的 `raven` 用 `LICENSES.json`（结构化许可边界）、`ex-ussr-kinship-research` 用 `independence_group`（代码层禁止凭空声明）、`c6` 用 `## 已知限制`（显式列出未完成）⭐⭐⭐⭐⭐ ⭐⭐ 属于同一族思路的不同形态 —— **让边界可被第三方读到，而不必信任作者的声明。**

⭐⭐⭐⭐⭐ **第三条关于「账号判据只能作辅证」。** ⭐⭐⭐⭐⭐ 本日报在 11-12 记录 `auto-twitch-drops-claim`（账号当天新建 → 判为农场）、在 11-13 记录 8 个载荷族账号（3 分 28 秒窗口内批量注册 → 判为农场）时，都把账号信号当作强判据。⭐⭐⭐⭐⭐ **⭐⭐ 而本项目是同一天的、单账号、986⭐、99 blobs、10 个 release 的真实工程。⭐⭐⭐⭐⭐ ⭐⭐ 因此本日报的修正是：**账号年龄/聚集度只能用于「排除」，不能用于「定性」** —— ⭐⭐⭐⭐⭐ ⭐⭐ 一个新账号发布的真实项目，与一个新账号发布的空壳，在账号信号上完全一样。⭐⭐⭐⭐⭐ ⭐⭐ 真正的分界在内容侧：有没有构建产物、有没有 release、有没有工程结构、有没有可核验的迭代记录。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；标注「待核验」的节点不应视为项目实现事实。

```mermaid
flowchart TB
  subgraph Device[iOS / iPadOS 设备 · 边界外]
    Sys[系统标志位<br/>设备能力位 · 区域码 · 销售地区 · 硬件开关]
    Key[受保护数据<br/>缓存 / 存档 / 容器状态]
    OS[iOS 27.x 内核与系统服务]
  end
  subgraph Upstream[能力来源]
    Worse[forcequitOS/worse_query<br/>底层能力<br/>README 明写「基于」]
  end
  subgraph App[Erosion · SwiftUI 应用 + 共享扩展]
    Bridge[Erosion/bridge.h 826 B]
    Mg[Tweaks/MobileGestalt/<br/>MGImageReader.h 466 B]
    Exploits[Exploits/<br/>bad_query.h 234 B<br/>pathleak.h 1,010 B]
    Helpers[Helpers/App/<br/>Exitinator.swift · Hapticinator.swift]
    UI[UI/Lists/ · UI/Interactions/ · UI/Alerts/]
    Inspect[MGInspector · Apple Intelligence Checkup<br/>只读检查模块 v0.7.0]
    Backup[(写入前自动备份原值<br/>可一键回滚)]
    Assets[Assets.xcassets/pfps/<br/>12 个独立 imageset]
    Entitle[Erosion.entitlements 308 B<br/>共享扩展授权]
  end
  subgraph Release[发布与加固记录]
    Rel[10 个 release<br/>v0.5.1 → v0.7.2]
    Sec[commit 中的安全审计条目<br/>security(audit) · fix(security)<br/>Release v0.7.2 sandbox & exploit boundary hardening]
    Build[.github/workflows/build.yml 417 B]
  end
  Sys --> Bridge
  Key --> Bridge
  OS --> Bridge
  Worse -.提供底层能力.-> Bridge
  Bridge --> Mg
  Bridge --> Exploits
  Mg --> UI
  Exploits --> UI
  Helpers --> UI
  UI --> Backup
  Backup -.先存后改.-> Sys
  Backup -.回滚路径.-> Sys
  Inspect -.只读 不写入.-> Sys
  Assets --> UI
  Entitle --> Bridge
  Sec --> Rel
  Build --> Rel
  Lim[证据边界与未核验项<br/>未在设备上运行 · 未执行任何写入<br/>备份与回滚的存储位置与覆盖范围未核验<br/>哪些修改需越狱 未核验<br/>与 worse_query 的能力分界未核验<br/>986⭐ 为发布后 28 小时快照值 增速未统计<br/>subs 1 · fork/star 23.0% · 0 issue · 账号 2026-11-10 新建]
  App -.受其约束.-> Lim
```

## 定位判断
**工具型（tool），且是「iOS 系统级研究工具」这一小众品类里发布节奏与安全记录最规范的一个。** ⭐⭐⭐⭐⭐

⭐⭐⭐⭐⭐ **它在生态里的位置是「中文本地化的 MobileGestalt / 系统标志位工作台」** —— 它不与 `worse_query` 竞争（明确标注基于它），⭐⭐⭐⭐⭐ **而是提供图形界面、备份回滚与安全加固后的实现。** ⭐⭐⭐⭐⭐ **⭐⭐ 本日报给它的定级是「工具型」而非「生产可用」，依据与本日报其余档案一致的三项尺子：⭐⭐⭐⭐⭐ ⭐⭐ 发布历史（10 个 release，✅）、外部使用证据（0 issue、subs 1，❌）、缺陷响应能力（release 标题显示有，⚠️ 但样本仅 28 小时）。⭐⭐⭐⭐⭐ ⭐⭐ 而它与同日窗口的 `solana-vigil`（1 commit / 59 blobs / 0 issue）相比，⭐⭐⭐⭐⭐ ⭐⭐ **在「工程完整度」这一项上明显更强 —— 这是本窗口内两个真项目之间最清晰的对比。**

## 风险 / 局限 / 泡沫点
- **⭐⭐⭐⭐⭐ 设备级不可逆风险：** ⭐⭐⭐⭐⭐ **⭐⭐ 修改系统标志位若出错可能导致设备无法正常启动。⭐⭐⭐⭐⭐ ⭐⭐ 本项目提供了备份与回滚，这是本档案最看重的优点 —— 但**回滚是否覆盖全部被改动的位置，本日报无法核验**，⭐⭐⭐⭐⭐ ⭐⭐ 因此本档案在 PoC 中明确要求只在**可完全重置的备用设备**上验证。**
- **⭐⭐⭐⭐⭐⭐ 账号与发布的时间关系异常：** 账号创建于 2026-11-10T02:02:54Z，仓库创建于 02:37:31Z（相差 35 分钟）。⭐⭐⭐⭐⭐⭐ **⭐⭐ 这本身不是问题（本日报在本数据集里见过「新号发布真实项目」的正常案例，如 11-12 的 `c6lang/c6` 组织账号创建于仓库创建前 7 分钟），⭐⭐⭐⭐⭐⭐ 但它再次证明账号信号不能单独定性。**
- **⭐⭐⭐⭐ 依赖上游能力：** README 明写「基于 `forcequitOS/worse_query`」。⭐⭐⭐⭐⭐ **⭐⭐ 本日报未核验上游的可用性、许可与维护状态；⭐⭐⭐⭐⭐ ⭐⭐ 若上游停止维护或改变接口，本项目的适配成本未知。**
- **⭐⭐⭐⭐ fork/star 23.0% 而 0 open issue：** ⭐⭐⭐⭐⭐ **⭐⭐ 227 个 fork 却没有任何公开反馈，⭐⭐⭐⭐⭐ ⭐⭐ 这个组合要么意味着 fork 者不反馈，要么意味着反馈发生在别处（issue 被关闭 / 讨论在外部群组）—— 本日报未核验。**
- **⭐⭐⭐⭐ 「防白苹果」是目标而非状态：** ⭐⭐⭐⭐⭐ **⭐⭐ README 描述的是「简体中文防白苹果安全加固版」，⭐⭐⭐⭐⭐ ⭐⭐ 但本日报未核验加固的具体清单与效果；⭐⭐⭐⭐⭐ ⭐⭐ 「加固」这一措辞也暗示它承认基线版本存在风险。**
- **⭐⭐⭐⭐ subs 1 而 star 986：** ⭐⭐⭐⭐⭐ **⭐⭐ 本批次中 `solana-vigil` subs 10 / `Erosion-CN` subs 1，⭐⭐⭐⭐⭐ ⭐⭐ 两个都是专业工具而关注度差 10 倍，⭐⭐⭐⭐⭐ ⭐⭐ 说明传播路径比 star 数更能解释 subs。**
- **⚠️ 证据边界：** 未在任何设备上运行、未执行任何写入或回滚；备份与回滚的存储位置、格式与覆盖率未核验；哪些修改需要越狱、哪些只需共享扩展未核验；与 `worse_query` 的能力分界未核验；`Erosion/Exploits/` 下两个头文件的具体作用未核验；**star 增速未做统计**（需分页遍历 stargazer 列表），986⭐ 为发布后约 28 小时的快照绝对值；topics 为空数组。

## 与同类项目的关系
- **vs `forcequitOS/worse_query`：** ⭐⭐⭐⭐⭐ **不是竞品，是上游。** ⭐⭐⭐⭐⭐ README 明写「基于」，⭐⭐⭐⭐⭐ **⭐⭐ 而本日报在本数据集里记录过「搬运上游」的反面样本（11-13 的 `AIRzZ90/study-materials-fork`，把上游代码整个镜像并索取 star）—— ⭐⭐⭐⭐⭐ ⭐⭐ **⭐⭐ 同一个动作（使用上游能力），一次是「基于它构建并公开溯源」，一次是「把它整个复制并收割 star」。⭐⭐⭐⭐⭐ ⭐⭐ 本日报认为这正是「内容层证据」优于「元数据层证据」的最好例证。**
- **vs `huamidev/GestaltX`（11-10 档案）：** ⭐⭐⭐⭐⭐ **⭐⭐ 同一天（11-09 窗口）出现的同类项目 —— GestaltX 是 iOS 27.x 的 MobileGestalt 编辑器（SwiftUI + 共享扩展），⭐⭐⭐⭐⭐ ⭐⭐ 而 Erosion-CN 是「系统配置与 MobileGestalt 研究工具箱」。⭐⭐⭐⭐⭐ ⭐⭐ **⭐⭐ 本日报在本数据集里第一次看到同一细分品类在 24 小时内出现两个独立实现（GestaltX 1,364⭐ / Erosion-CN 986⭐），⭐⭐⭐⭐⭐ ⭐⭐ 这说明该品类在本季度已进入「多人独立实现」的阶段。⭐⭐⭐⭐⭐ ⭐⭐ 而两者的差别很值得记：GestaltX 的档案强调「把『导入的文件是不是这台设备自己的』也做成了可验证的条件」，⭐⭐⭐⭐⭐ ⭐⭐ Erosion-CN 的强调是「写入前自动备份 + 一键回滚」—— **两者都在回答同一个问题：如何让不可逆的系统级操作变得可控。** ⭐⭐⭐⭐⭐**
- **vs `kolbicz/WQFiles`（11-10 窗口，同为 iOS 27 无越狱工具）：** ⭐⭐⭐⭐⭐ **⭐⭐ 同窗口的第三个 iOS 27 工具（153⭐，Objective-C，GPL-3.0）。⭐⭐⭐⭐⭐ ⭐⭐ 三个项目同框说明「iOS 27 的系统级折腾工具」在本季度已成一个小赛道。**
- **vs `solana-vigil`（11-11 档案，同窗口）：** ⭐⭐⭐⭐⭐ **⭐⭐ 本窗口内两个真项目的清晰对照 —— Vigil 是「1 commit / 59 blobs / 只读 / 0 issue」，⭐⭐⭐⭐⭐ ⭐⭐ 而 Erosion-CN 是「15 commits / 99 blobs / 10 个 release / 可写但有备份回滚 / 0 issue」。⭐⭐⭐⭐⭐ ⭐⭐ **⭐⭐ 一个用「读」定义安全，一个用「可撤销的写」定义安全 —— 两者是同一个问题的两种答案。**
- **vs 各类越狱 tweak 商店：** ⭐⭐⭐⭐ **⭐⭐ 本项目是研究工具箱而非分发渠道；⭐⭐⭐⭐ ⭐⭐ 本日报未核验它是否提供 tweak 分发。**

## 是否值得持续跟踪
**值得跟踪（工具型 / 早期）。** ⭐⭐⭐⭐⭐

⭐⭐⭐⭐⭐ 对做 iOS 系统研究的开发者，**它是一个中文本地化、能力来源明确、且把「备份 + 回滚」作为默认行为的工具箱**；⭐⭐⭐⭐⭐ **⭐⭐ 对架构师，它的价值主要在两条做法：** ① 不可逆操作的默认可撤销化；② 把安全审计写进 commit 类型与 release 标题，让边界可被第三方读到。

⭐⭐⭐⭐⭐ **⭐⭐ 而它对本日报方法论的最大贡献是那个负面教训：一个「当天新建的单账号仓库」既可能是 986⭐ 的真实工程，也可能是 76⭐ 的投递壳 —— ⭐⭐⭐⭐⭐ ⭐⭐ 账号信号只能排除，不能定性。**

## 后续观察点
- ⭐⭐⭐⭐⭐ **备份与回滚的实际覆盖率** —— ⭐⭐⭐⭐⭐ **⭐⭐ 这是本档案最想验证的一条：回滚是否覆盖了全部被改动的系统位置。⭐⭐⭐⭐⭐ ⭐⭐ 若出现「回滚后仍无法启动」的 issue，本档案对它的正面评价需要修正。**
- ⭐⭐⭐⭐⭐ **issue 与外部反馈是否出现** —— ⭐⭐⭐⭐⭐ **⭐⭐ 当前 0 issue 且 fork/star 23.0%；⭐⭐⭐⭐⭐ ⭐⭐ 按本日报的判据，issue 的出现说明项目在被真实使用与质疑，因此这里要跟踪的是「它是否开始有 issue」。**
- ⭐⭐⭐⭐⭐ **与 `huamidev/GestaltX` 的关系** —— ⭐⭐⭐⭐⭐ **⭐⭐ 两者都是 iOS 27.x 的 MobileGestalt 工具，⭐⭐⭐⭐⭐ ⭐⭐ 本日报要跟踪它们是各自独立实现、还是存在代码/文档上的相互引用 —— ⭐⭐⭐⭐⭐ ⭐⭐ 这直接关系到「该品类是两人独立探索还是一次协同」这一判断。**
- ⭐⭐⭐⭐ **与 `forcequitOS/worse_query` 上游的适配跟进** —— ⭐⭐⭐⭐⭐ **⭐⭐ 若 iOS 27.x 后续小版本改变接口，本项目是否及时跟进，是一个可观测的维护指标。**
- ⭐⭐⭐⭐⭐ **账号与社区的建立** —— ⭐⭐⭐⭐⭐ **⭐⭐ 当前 24 followers、2 个公开仓库；⭐⭐⭐⭐⭐ ⭐⭐ 本日报会跟踪它是否开始有第二个项目与持续 issue 讨论 —— ⭐⭐⭐⭐⭐ ⭐⭐ 那将是「真实项目」这一判断的进一步确认。**
- ⭐⭐⭐⭐⭐ **「防白苹果加固」的清单是否被结构化** —— ⭐⭐⭐⭐⭐ **⭐⭐ 若能像 10-26 的 `raven` 用 `LICENSES.json` 那样，把加固项做成可机读的清单，本档案关于「让边界可被第三方读到」的评价会进一步加强。**

---
*首次记录：2026-11-11（依据 2026-11-11 当日的 GitHub API 快照；2026-11-13 回填建档）*
