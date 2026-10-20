---
title: "pengchujin/aerial-tv"
slug: "aerial-tv"
date_added: "2026-10-21"
category: "工具型"
emoji: "📺"
stars: "524 stars"
stars_delta: "创建 2 天（2026-10-20 起）"
language: "Kotlin"
score: 87
tags: ["aerial-tv", "pengchujin", "android-tv", "china-market-tv", "xiaomi", "tcl", "sony-bravia", "redmi", "hyperos-tv", "tvos-style", "no-ads", "launcher", "home-role", "accessibility-service", "notification-listener", "boot-autostart", "keep-adb", "screensaver", "wallpaper", "signal-source", "adb-install", "curl-one-liner", "agent-install-prompt", "device-notes", "kotlin", "mit", "offline-first"]
url: "https://github.com/pengchujin/aerial-tv"
---

# pengchujin/aerial-tv

## 一句话定位
给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告没有推荐流，开机自动接管；不 root、不卸载、不停用任何系统应用，一条 curl 命令即可还原。

## 它解决的问题
国产电视（小米、TCL、索尼国行等）的出厂桌面被推荐流、会员角标、限免标和屏保广告占满，用户想换掉它却要付出很大代价：root、卸载系统应用、失去保修、失去后续更新。**更麻烦的是这些电视"只认自家桌面"且"待机时还会强制停止第三方 App"**——就算装上了，也会被切回原桌面或被杀。

Aerial 的问题定义因此比同类更完整：不是"做一个好看的 launcher"，而是**"如何在敌意固件上活下来"**。README 用五层接管模型逐层回答了这个问题。

## 为什么值得关注（2026-10-21）
- **今日四个项目中唯一在真实异构硬件上被六款真机验证过的**：小米 MiTV-MFTR0 / MiTV-MFFU0 / Redmi X65 2026 · TCL MT5879 国行 · 索尼 XRJ-77A80J 国行 · 索尼 BRAVIA VH1 国行，每台挂一份 `docs/devices/*.md` 笔记
- **五层接管模型是可迁移的"敌意固件求生手册"**：HOME 角色 → 无障碍桌面守护 → 通知监听被杀复活 → 开机自启 → ADB 常开，可套用到机顶盒、车机、智能屏、定制 ROM 手机
- **权限明示表**：六类高危权限逐项说明用途，定位权限明确写"只用来读取 Wi-Fi 名称"，无障碍守护明确写"只看哪个窗口到了前台，不读屏幕内容"，通知监听明确写"不读取任何通知"
- **中文原创项目能拿全球 star**：2 天 524⭐ ⑂36（fork-star 6.9%），官网 aerial.qust.me，中英双 README
- **`open_issues_count = 39`（本批最高）**：说明有真实用户在提交问题，而不是只有 star

## 热度来源判断
**热度真实，但属赛道已验证后的跟随者。** 需要诚实指出：Android TV 桌面赛道在本周已出现至少 6 个项目（tv-vibehack、free-my-tv、tv-detox、tv-home、dumbtv、aerial-tv），其中 `simbasjungles/free-my-tv` 今日已达 1678⭐ ⑂172。**赛道需求是真的**（多团队独立推出即为证据），但也意味着**同质化严重**。

Aerial 的差异化不在 UI（同样是 tvOS 风格），而在**它把竞争维度从"能不能装"推到了"在什么机型上能活下来"**——六款真机矩阵、逐机型笔记、五层接管模型、五条已知限制，这三样在同赛道项目里是独一份。

## 关键技术亮点
1. **五层接管模型**（README 逐层解释）：① 正常申请 HOME 角色设为默认桌面（原生 Android TV / Google TV 到这步就够）② **无障碍服务桌面守护**——官方桌面一到前台就把 Aerial 拉回来 ③ **通知监听被杀复活**——小米待机会强停所有第三方 App，系统约 0.5 秒内重新绑定通知监听，Aerial 借此复活并用 `WRITE_SECURE_SETTINGS` 重开守护 ④ **开机自启**——开机时系统绑定通知监听，Aerial 随之启动；TCL 的"自启动管理"用 `appops` 放行 ⑤ **ADB 常开（可选）**——`KEEP_ADB=1` 应对小米待机唤醒后自动关闭 ADB
2. **权限明示表**：`WRITE_SECURE_SETTINGS`（重开守护 / 保持为系统屏保 / KEEP_ADB / 写入小米背光值）· 通知监听（被强停或开机后被系统拉起，**不读取任何通知**）· 悬浮窗（开机后从后台打开）· 修改系统设置（标准接口调亮度）· 定位（**只用来读取 Wi-Fi 名称**）· TCL `APP_AUTO_START` / `APP_ASSOC_START`
3. **逐机型安装步骤表**：小米/Redmi（连按"产品型号"确认键进开发者模式 → 设置→账号与安全开 ADB）· TCL/雷鸟（按遥控器 上→下→左→右，底部出现"更多"）· 原生 Android TV / Google TV / 海信（连按版本号 7 次）
4. **三条安装路径**：一行 curl（`curl -fsSL …/tools/get.sh | KEEP_ADB=1 TV=<IP> bash`）+ 手动 5 条 adb 命令 + **一段给 Claude Code/Codex/Cursor 的 Agent 安装 prompt**（该 prompt 明确要求"不要卸载或停用任何系统应用，不要删除电视上不是这次安装创建的文件，失败时把命令输出原样给我看"）
5. **固件对抗分支**：`aerial-guard.apk`（不声明 HOME）应对固件拒绝安装桌面类 App；**TCL 拒绝一切 ADB 安装时改走电视自带"多屏互动"推送**，无此功能时退回当贝市场
6. **屏保三形态**：114 段 Apple TV 航拍影片实时播放（1080p H.264 约 15–20 Mbps，镜头移动时显示地名）+ 每日精选与用户照片缓慢推移 + 每分钟换位的时钟屏保（防烧屏）。在标准 Android 屏保机型（如 TCL）上 Aerial 就是系统屏保；在小米上会在桌面空闲时抢先启动，挡在小米广告屏保前面
7. **UI 细节**：大号细体时钟压在壁纸上、壁纸底部与左侧自动压暗、滚动时时钟收进状态栏；每行 5 个应用网格聚焦浮起（有电视横幅用横幅 / 方形图标底色铺满磁贴 / 自适应图标拆两层做视差）；**显示无标准入口的国产系统 App**（小米应用中心、高清播放器、米家）；信号源磁贴把 HDMI/AV/天线固定到首页；返回键语义与 tvOS 一致（网格内返回第一行，第一行返回触发屏保）
8. **手机壁纸面板**：扫描二维码在手机上传照片、选壁纸、换屏保；页面只在面板打开时开放，地址带随机令牌
9. **不 root、不卸载、不停用任何系统应用**，且 `bash -s restore` 一条命令还原

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 单个 Android TV launcher APK（`app.orchard.tv`）+ `aerial-guard.apk` 变体 + 控制中心 + 屏保 + 手机壁纸面板（QR + 随机令牌）+ `tools/get.sh` / `tools/install.sh` + `docs/devices/` 机型笔记；数据面依赖 Apple 航拍服务器与必应每日精选 | 由 README 安装段 + 权限表 + 已验证矩阵推得；app 包名 `app.orchard.tv` 来自 README 手动安装段；**航拍与每日精选的实际数据通路（直连 Apple / 有无 CDN）未明示** |
| 主路径 | 电视开 ADB（逐机型步骤表）→ `curl … get.sh \| KEEP_ADB=1 TV=<IP> bash` → 装 APK + 授予权限 + `appops` 放行 + 接管桌面与屏保 → 开机自启 → 桌面守护对抗官方桌面 | 全路径由 README 三段（安装 / 一行命令 / 手动安装 5 条 adb）+ 五层接管模型直读；**TCL 分支改走"多屏互动"推送、无此功能时退回当贝市场**——该 fallback 可靠性待核验 |
| 关键权衡 | 无障碍服务守护（换来桌面不被抢，代价是长期持有高敏感权限）vs 放弃守护（小米/TCL 会被切回）· 通知监听复活（借系统 0.5 秒重绑）vs 自启动白名单（品牌差异大）· 拿 `WRITE_SECURE_SETTINGS`（能重开守护）vs 拒绝（被强停后回不来）· 航拍直连 Apple 15–20 Mbps（画质好、不占本地存储）vs 本地预置素材（不依赖外网）· `guard` 变体（过固件检查）vs 标准变体（功能全）· 手机壁纸面板（随机令牌 + 仅打开时开放）vs 全开放面板 | README 明示各层与理由；**无障碍 + 通知监听 + `WRITE_SECURE_SETTINGS` 三项叠加的隐私暴露面，README 只做了"不读屏幕/不读通知"的自我声明，未提第三方审计**——这是最该被外部验证的一点 |
| 最小 PoC | 1. 手上有任意 Android TV 5.0+ 电视 → 2. 按机型表开 ADB → 3. 跑一行 curl 安装 → 4. `adb shell dumpsys window \| grep mCurrentFocus` 确认前台是 `app.orchard.tv`（README 在 Agent prompt 里也如此建议）→ 5. `adb reboot` 验证开机直达 → 6. 停在别的 App 空闲 10 分钟，验证小米屏保是否被抢先 → 7. 跑还原命令确认能恢复原桌面 | 第 3–7 步逐条来自 README；**若没有对应品牌真机，只能用原生 Android TV / Google TV 走第 1 层，2–5 层无法验证**——这直接决定可信度能被检验到什么程度 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart TB
  subgraph 设备与系统敌意边界
    OEM[国产电视固件<br/>小米 HyperOS TV · TCL · 索尼国行]
    KILL[待机强制停止第三方 App]
    SELFSTART[自启动管理默认拦截<br/>TCL 需 appops 放行]
    OFFADB[待机唤醒后自动关闭 ADB]
    GUARDUP[固件坚持自家桌面<br/>拒绝桌面类 App 安装]
  end

  subgraph Aerial 职责面
    HOME[第1层 正常申请<br/>HOME 角色 默认桌面]
    ACC[第2层 无障碍桌面守护<br/>官方桌面一到前台即拉回<br/>只看前台窗口 不读屏幕]
    NLS[第3层 通知监听复活<br/>系统约 0.5 秒重绑<br/>不读取任何通知]
    BOOT[第4层 开机自启<br/>随通知监听绑定而启动]
    KEEP[第5层 ADB 常开 可选<br/>KEEP_ADB=1]
    UI[桌面 UI<br/>时钟 · 5 列应用网格 · 信号源磁贴<br/>控制中心 · 长按菜单]
    SS[屏保<br/>114 段 Apple 航拍 1080p H.264 约 15-20Mbps<br/>每日精选照片 · 每分钟换位时钟防烧屏]
    PHONE[手机壁纸面板<br/>二维码 + 随机令牌<br/>仅面板打开时开放]
  end

  subgraph 安装与控制面
    ADB[电脑 adb over Wi-Fi<br/>逐机型开 ADB 步骤表]
    CURL[一行 curl<br/>get.sh KEEP_ADB=1 TV=IP bash]
    PROMPT[Agent 安装 prompt<br/>Claude Code / Codex / Cursor<br/>明令不卸载不停用系统应用]
    MANUAL[手动 5 条 adb 命令<br/>install -r + pm grant + allow_listener<br/>appops + am start]
    RESTORE[还原 bash -s restore<br/>一条 curl 恢复原桌面]
  end

  subgraph 高危权限 权限明示表
    P1[WRITE_SECURE_SETTINGS<br/>重开守护 · 保持系统屏保<br/>KEEP_ADB · 写入小米背光]
    P2[通知监听 不读取通知]
    P3[悬浮窗 SYSTEM_ALERT_WINDOW<br/>开机后从后台打开]
    P4[修改系统设置 调亮度]
    P5[定位 只读 Wi-Fi 名称]
    P6[TCL APP_AUTO_START / APP_ASSOC_START]
  end

  ADB --> CURL
  ADB --> MANUAL
  PROMPT -.指导.-> CURL
  CURL --> P1 & P2 & P3 & P4 & P5 & P6
  MANUAL --> P1 & P2 & P3
  CURL --> HOME
  HOME --> UI
  GUARDUP -.拒绝桌面类 App.-> MANUAL
  MANUAL -.改用不声明 HOME 的变体<br/>aerial-guard.apk.-> GUARDUP
  OEM --> KILL
  KILL -.强停.-> NLS
  NLS -->|系统重绑| ACC
  ACC -->|拉回前台| OEM
  P1 -->|重开守护| ACC
  SELFSTART -.拦截.-> BOOT
  P6 -.appops 放行.-> BOOT
  NLS -->|开机时绑定| BOOT
  OFFADB -.关闭.-> ADB
  KEEP -->|重开| OFFADB
  KEEP --> P1
  UI --> SS
  PHONE --> UI
  PHONE --> SS
  SS -->|待机空闲抢先启动| OEM
  RESTORE -.反向恢复.-> OEM

  UNV[待核验 无障碍 + 通知监听 + WRITE_SECURE_SETTINGS<br/>三项叠加的隐私暴露面<br/>README 仅自声明 未见第三方审计]
  UNV -.-> ACC
  UNV -.-> NLS
  UNV -.-> P1
  FALLBACK[待核验 TCL 走多屏互动<br/>无此功能时退回当贝市场<br/>可靠性未知] -.-> ADB
```

## 架构启发
Aerial 最值得抄的不是 UI，而是**它把"敌意环境"当成一等设计约束来逐层应对**。多数系统集成文档假设宿主环境是可配合的；Aerial 假设宿主会拒绝你、会在待机时杀你、会在你装好之后切回原桌面，然后给出五层递进：正常申请 → 无障碍守护 → 借系统重绑复活 → 借系统绑定实现自启 → 保持控制通道。每层都在上一层失效时接管。

这套递进的核心洞察是：**不与固件对抗，而是借用固件自身的行为**。第 3 层没有去申请开机自启白名单（各品牌差异极大），而是注册通知监听——因为系统保证在进程被杀后约 0.5 秒内重绑它，于是"被杀"反而成了复活机会。这个思路可以迁移到任何"应用必须长期驻留但系统不配合"的场景。

第二个启发关于**权限的自我陈述**：README 用一张表把六类高危权限逐项摊开，并对最敏感的两项给出可验证的否定式承诺——无障碍服务"不读屏幕内容"、通知监听"不读取任何通知"。**当一个项目必须申请危险权限时，主动写出"它不做什么"比解释"它要做什么"更能建立信任**，因为用户担心的正是"它会看到什么"。这个表达方式值得抄——但也必须指出：**自我声明不等于保证，未经审计的承诺仍然只是承诺**。

第三个启发是一个容易被误读的点：**open issues 39 是这个项目最健康的质量信号之一**。一个刚发布 2 天就收到 39 个 issue 的项目，说明有真实用户在真机上反复尝试，而不是围观点星。相形之下，"0 issue"往往说明的是没人用。

反面是这套模型的结构性脆弱：它建立在 OEM 行为之上——系统会重绑通知监听、系统开机时绑定通知监听、TCL 用 appops 可放行。**一次固件更新就可能推翻某一层，而这不是代码能防御的。** 这是所有"与宿主系统博弈"方案的共同天花板。

## 定位判断
**工具型（但可作为方法论样本）。** 在生态里它与 free-my-tv、tv-vibehack、tv-detox、tv-home、dumbtv 同属 Android TV 去广告赛道，但**它是第一个把竞争维度从"UI 好不好看"移到"在什么机型上能活下来"的项目**——六款真机矩阵、逐机型笔记、五层接管模型、权限明示表、五条已知限制这套组合，在同赛道里是独一份。

它的真正价值可能溢出电视领域：**"敌意固件求生"的五层递进模型（正常申请 → 无障碍守护 → 借系统重绑复活 → 借系统绑定实现自启 → 保持控制通道）是一份可迁移的操作手册**，适用于机顶盒、车机、智能屏、定制 ROM 手机上任何试图替换系统桌面或常驻后台的开发者。

## 风险 / 局限 / 泡沫点
- **权限组合敏感**：无障碍服务 + 通知监听 + `WRITE_SECURE_SETTINGS` + 悬浮窗四项叠加。README 做了"不读屏幕/不读通知"的自我声明，但**未见第三方审计**——用户无法独立验证承诺是否被遵守。这是最该被外部验证的一点
- **航拍依赖 Apple 服务器**：1080p H.264 约 15–20 Mbps 实时播放。Apple 若变更策略、地区封锁或流量限制则功能失效；README 已把它列为已知限制
- **接管并非 100%**：README 自列的两条即证据——TCL 调音量会双弹自家音量条；停在别的 App 空闲时小米自己的屏保仍会出现
- **TCL 的 fallback 链路脆弱**：多屏互动推送 → 无此功能时退回当贝市场，后者可靠性完全未知
- **39 open issues + 0 subscribers**：典型的"项目有用、社区未形成"——有人在用，但没人长期跟踪
- **整套模型建立在 OEM 行为之上**：系统会重绑通知监听、系统开机时绑定通知监听实现自启、TCL 用 appops 可放行——**一次固件更新就可能推翻某一层**，且这不是代码能防御的
- **赛道同质化**：本周至少 6 个同类项目；`free-my-tv` 已 1678⭐ ⑂172，资源与注意力会向头部集中

## 与同类项目的关系
- **vs simbasjungles/free-my-tv**（1678⭐ ⑂172，Java，MIT）：最直接的对位。free-my-tv 主打"不 root 不卸载 + 60fps/16.6ms 帧时间 + 96MB vs 242MB 内存在 TV 自身芯片跑 + 跟随真实日落切换主题 + freemytv.io 官网"，走**产品形态与性能数据**路线；Aerial 主打**国产机型适配与敌意固件存活率**，走**工程验证密度**路线。两者方向互补而非替代
- **vs Gathin23/tv-vibehack**（10-19 跟踪，1739⭐）：走"逆向 + 通用方案"路线，强调 direct boot launcher 与遥控器热键重映射；Aerial 不逆向，走公开 API + 无障碍服务路线，兼容性更窄但更安全
- **vs Ansub/tv-detox / mihirgupta0900/tv-home / humblemuzzu/dumbtv**（同周同期）：Aerial 的差异化是**中文 + 国产机型 + 真机验证矩阵**
- **vs 电视厂商官方桌面**：Aerial 的存在前提是厂商桌面的商业化推荐流不可接受；一旦厂商把桌面做得足够安静，动机就消失

## 是否值得持续跟踪
**值得，且它是今日四个项目中最可验证的一个。** 理由不是它 star 多，而是**它把验证矩阵、权限用途、已知限制三者都公开写了出来，别人可以逐条复核**——这是研究报告最需要的性质。

**但要注意它的高权限属性**：在第三方审计出现之前，不建议在没有备份的电视上直接部署。**观察重点：`docs/devices/` 机型笔记是否持续增加（说明社区在补验证）、用户验证类 issue 是否继续出现、国产固件大版本更新后五层模型是否需要改。**

## 后续观察点
- `docs/devices/` 机型笔记增长速度——社区是否在主动补验证矩阵（最能说明项目健康度的指标）
- 是否引入第三方无障碍权限审计，或提供权限最小化模式（关掉不需要的层）
- 小米 / TCL / 索尼 的固件大版本更新后，五层接管模型是否需要改
- 航拍直连 Apple 的地区可用性（国内网络环境下的实测）
- `open_issues_count = 39` 中的高频问题是什么（哪一层最容易失效）
- 与 free-my-tv 是否出现互指或功能合并（同赛道头尾效应）
- 是否补齐 `open_issues_count` 所暴露的安装失败机型

---
*首次记录：2026-10-21*

> 数据来源: GitHub REST API + README 原文（2026-10-21 CST 06:00） | Stars: 524 | Forks: 36 | License: MIT | 语言: Kotlin | 创建: 2026-10-20 | 推送: 2026-10-20 | Subscribers: 0 | Open Issues: 39 | Android TV 5.0+