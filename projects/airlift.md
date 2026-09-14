---
title: "0xjohnnydev/airlift"
slug: airlift
date_added: "2026-09-15"
last_seen_date: "2026-09-15"
category: "工具型"
emoji: "🪂"
stars: "33 stars"
stars_delta: "1 天 33⭐ / fork 2 / fork/star 6.1%"
language: "Objective-C"
score: 84
tags: ["ios", "ios27", "sandbox-escape", "airtraffic", "atairlock", "books-sync", "symlink-follow", "security-research", "poc", "objective-c", "noassertion"]
url: "https://github.com/0xjohnnydev/airlift"
---

# 0xjohnnydev/airlift

## 一句话定位
iOS 27.0 RC AirTraffic 沙箱逃逸 PoC；漏洞根因清晰到 `-[ATAirlock processCompletedAsset:]` 字符串前缀校验 + ancestor symlink 跟随；12 个目录 fresh-file 写权限已验证；Objective-C 极简 PoC。

## 它解决的问题
iOS 沙箱逃逸类研究在 iOS 17 之后公开化程度持续降低（Apple Security Bounty 转向私下披露），但学术研究 + Apple Security 报告仍需要可复现 PoC。airlift 是 **「iOS 27.0 公开可复现 AirTraffic 沙箱逃逸」** 的 PoC——它不声称 0-day 武器化，而是 **「给开发者与安全研究者了解 AirTraffic / ATAirlock / Books 同步链路的边界设计缺陷」**。漏洞根因清晰：`-[ATAirlock processCompletedAsset:]` 仅校验 `destination` 字符串前缀（`[destination hasPrefix:@"/var/mobile/Media/"]`）未校验 `source`，destination 跟随 ancestor symlink；Books 「Persistent ID」作为 `asset.identifier` 直接拼接路径无校验。这是 path traversal 类的标准反模式（应使用 `realpath` 或 sandbox token 而非字符串前缀 + symlink 跟随）。

## 为什么值得关注（2026-09-15）
- **Stars:** 33（截至 2026-09-15），1 天 33⭐，安全研究 PoC 早期信号
- **Forks:** 2
- **Watchers/Subscribers:** 2
- **Open Issues:** 1
- **License:** NOASSERTION（合规风险；安全研究 PoC 典型）
- **语言:** Objective-C
- **活跃度:** created 2026-09-14，pushed_at 2026-09-14
- **规模:** 123 KB，极简 PoC
- **Topics:** （GitHub API 未列出 topics）
- **测试环境:** iOS 27.0 RC (24A435) + iOS 27.0 final (24A437)
- **触发条件:** 「paired Mac over Wi-Fi or USB, no iOS app required」

## 热度来源判断
airlift 的热度是 **「iOS 27.0 公开沙箱逃逸稀缺性 × 漏洞根因清晰度 × PoC 极简可复现 × 不 burn for clout 立场」** 的组合。iOS 27 公开沙箱逃逸 PoC 在 2026 Q3 是稀缺品（多数研究转向私下披露）；**漏洞根因清晰到 `[destination hasPrefix:@"/var/mobile/Media/"]`** 是 Apple Security 团队可直接对照修复的程度；**123 KB repo + Objective-C 极简实现**便于研究者快速验证；**「there are always more bugs 🔥🪲4⃣☃️」的反 burn-for-clout 立场**是 PoC 公开的关键伦理声明。33⭐ / fork 2 / 1 天是「学术 + 安全研究」圈层典型扩散速度。热度 **真实且具安全研究价值**——但需关注 Apple Security 是否已收到报告及补丁窗口期。

## 关键技术亮点
1. **完整系统栈明示**——macOS 侧 `MobileDevice.framework → AirTrafficHost.framework`；iOS 侧 `com.apple.streaming_zip_conduit → com.apple.afc → com.apple.atc / AirTrafficDevice → Books sync client → ATLegacyAssetLink → ATAirlock → NSFileManager`
2. **触发条件简洁**——「paired Mac over Wi-Fi or USB, no iOS app required」；普通用户的默认 Books 同步场景
3. **漏洞根因清晰**——`-[ATAirlock processCompletedAsset:]` 仅校验 `destination` 字符串前缀（`[destination hasPrefix:@"/var/mobile/Media/"]`）未校验 `source`；destination 跟随 ancestor symlink；Books 「Persistent ID」作为 `asset.identifier` 直接拼接路径无校验
4. **12 个目录 fresh-file 写权限已验证**——`/var/mobile`, `/var/mobile/Documents`, `/var/mobile/Library`, `/var/mobile/Library/Preferences`, `/var/mobile/Library/Caches`, `/var/mobile/Library/SpringBoard`, `/var/mobile/Library/SMS`, `/var/mobile/Library/Safari`, `/var/mobile/Containers`, `/var/mobile/Containers/Data/Application`, `/var/mobile/Containers/Shared/AppGroup`, `/var/tmp`
5. **reads 是 indirect**——先移动已知文件到 Media → 通过 AFC 读 → 移回；这种「不直接 read」的设计是为了规避直接 read 路径上的额外校验
6. **MobileGestalt plist 当前不工作**——明确标注局限（无法直接绕过 Activation Lock 或篡改设备激活状态）
7. **测试环境明示**——iOS 27.0 RC (24A435) + iOS 27.0 final (24A437)
8. **PoC 意图明示**——「there are always more bugs 🔥🪲4⃣☃️」的反 burn-for-clout 立场；明确「simple proof-of-concept for developers and security researchers」
9. **Objective-C + NOASSERTION + 33⭐ / fork 2 / 123 KB**——「安全研究 PoC」典型形态（小、专、目标明确）

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | iOS 27.0 RC + paired Mac + Books sync 启用场景；macOS 侧 MobileDevice.framework + AirTrafficHost.framework；iOS 侧 streaming_zip_conduit → afc → atc → AirTrafficDevice → Books sync client → ATLegacyAssetLink → ATAirlock → NSFileManager；沙箱逃逸 12 个目录写权限已验证；reads indirect（移动已知文件到 Media → AFC 读 → 移回） | 来自 README 关于「12 个目录」「- [ATAirlock processCompletedAsset:] 字符串前缀校验」「ancestor symlink 跟随」「iOS 27.0 RC 24A435 + final 24A437」「no iOS app required」的明示；具体漏洞利用代码（移动 symlink + 触发 Books sync 的 Objective-C 源码）、NSFileManager 默认行为细节、MobileDevice.framework 在 paired Mac 侧的具体调用在 README 中未完整给出 |
| 主路径 | paired Mac + Books sync enabled → 构造 symlink + Books 「Persistent ID」→ 触发 AirTraffic sync → ATAirlock `-[processCompletedAsset:]` 取 asset.identifier 无校验直接拼接到 source 路径 → 取 asset.path（FileComplete.AssetPath 控制）拼接到 destination 路径 → 仅校验 destination 字符串前缀未校验 source → `[NSFileManager moveItemAtPath:source toPath:destination]` 跟随 ancestor symlink → 写入 12 个目录之一 | 主路径来自 README 关于漏洞利用流程的明示；具体 Objective-C PoC 代码（移动 symlink + 触发 Books sync 的实现细节）在本档案未读取；每个步骤的具体函数调用待核验 |
| 关键权衡 | 公开 PoC（教育 + 推动修复 vs 给攻击者武器化）/ 仅 Books 同步场景（聚焦 vs 攻击面窄）/ 不工作于 MobileGestalt plist（数据读写可 vs 设备控制不可）/ iOS 27.0 RC + final（早期补丁窗口 vs 已公开补丁窗口）/ Objective-C 实现（Apple 栈原生 vs 复杂 PoC 工程） | 权衡五因素均从 README 推导；具体 Apple Security 是否已收到报告、ETA 修复时间、patched iOS 版本号、其他 Books 同步路径变种待核验 |
| 最小 PoC | macOS + Xcode + paired iPhone（iOS 27.0 RC 24A435 或 final 24A437）+ 启用 Books sync + Objective-C 编译 PoC；触发条件：构造 symlink + 触发 AirTraffic sync；验证：写入 `/var/mobile/Library/Preferences`（最敏感目录之一）+ 读取 indirect（移动已知文件到 Media → AFC 读 → 移回）；不应尝试 MobileGestalt plist（README 明示当前不工作） | PoC 由「12 个目录验证 + paired Mac + Books sync + Objective-C 漏洞利用代码」路径推导；具体 PoC 编译步骤、symlink 构造细节、AFC 命令行调用待核验 |

## 架构启发
airlift 的核心启发是 **「iOS 沙箱路径校验的反模式」**——path traversal 类的经典漏洞。`-[ATAirlock processCompletedAsset:]` 的 `destination` 校验是 **「字符串前缀 + 未验证 source + 跟随 ancestor symlink」** 的组合——这是教科书级的反模式。Apple 框架层正确做法应是 **「realpath 解析 + sandbox token 校验 + source 独立验证」** 三件套，而非简单的字符串前缀。更深层的启发是 **「paired Mac + 默认服务（Books sync）是 iOS 沙箱逃逸的高暴露面」**——任何开启 Mac-iPhone Books 同步的用户都暴露于本 PoC 的攻击面；这意味着 iOS 沙箱逃逸不必依赖物理接触或 0-day 漏洞链，仅「默认服务启用」即可触发。**MobileGestalt plist 当前不工作**限制了设备配置修改能力（无法直接绕过 Activation Lock），但 **12 个目录的写权限已足以造成数据泄露 / 篡改 / 持久化**。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Mac[paired Mac<br/>Wi-Fi or USB] --> MobileDev[MobileDevice.framework<br/>macOS 侧]
  MobileDev --> AirTrafficHost[AirTrafficHost.framework<br/>macOS 侧]
  AirTrafficHost --> Conduit[com.apple.streaming_zip_conduit<br/>iOS 侧]
  Conduit --> Afc[com.apple.afc<br/>Apple File Connection]
  Afc --> Atc[com.apple.atc<br/>AirTrafficDevice]
  Atc --> Books[Books sync client]
  Books --> AssetLink[ATLegacyAssetLink]
  AssetLink --> Airlock[ATAirlock<br/>- processCompletedAsset]
  Airlock --> Fm[NSFileManager<br/>moveItemAtPath:toPath:]
  Fm --> Varify{destination<br/>hasPrefix /var/mobile/Media?}
  Varify -->|是| SymlinkCheck{ancestor symlink<br/>跟随?}
  SymlinkCheck -->|是| Escape[沙箱逃逸<br/>12 个目录写权限]
  SymlinkCheck -->|否| Block[阻断]
  Varify -->|否| Block
  Escape --> Dir1[/var/mobile]
  Escape --> Dir2[/var/mobile/Documents]
  Escape --> Dir3[/var/mobile/Library]
  Escape --> Dir4[/var/mobile/Library/Preferences]
  Escape --> Dir5[/var/mobile/Library/Caches]
  Escape --> Dir6[/var/mobile/Library/SpringBoard]
  Escape --> Dir7[/var/mobile/Library/SMS]
  Escape --> Dir8[/var/mobile/Library/Safari]
  Escape --> Dir9[/var/mobile/Containers]
  Escape --> Dir10[/var/mobile/Containers/Data/Application]
  Escape --> Dir11[/var/mobile/Containers/Shared/AppGroup]
  Escape --> Dir12[/var/tmp]
  Books -. Persistent ID 无路径校验 .-> Airlock
  Fm -.间接 read .-> Afc
```

## 定位判断
**工具型（iOS 安全研究 PoC）。** airlift 不是武器化工具，而是 **「开发者与安全研究者了解 AirTraffic / ATAirlock / Books 同步链路边界设计缺陷」的最小可复现 PoC**。它的价值不在于「利用价值」，而在于 **「漏洞模式公开化 + 推动 Apple Security 修复」**。对 Apple Security 团队：这是应该直接对应修复的清晰漏洞模式；对 iOS 安全研究者：这是 2026 Q3 公开的最具体 iOS 27 沙箱绕过案例；对企业 iOS 管理员：这是「应暂时关闭 Books 同步直到补丁」的明确信号。**NOASSERTION 许可 + 反 burn-for-clout 立场**是 PoC 公开的负责任态度。

## 风险/局限/泡沫点
- **NOASSERTION 许可**——合规扫描拒绝；安全研究 PoC 典型但企业直接采用有风险
- **漏洞利用窗口期**——若 Apple Security 未收到报告则漏洞持续暴露；若已收到则补丁窗口期内是攻击高发期
- **MobileGestalt plist 当前不工作**——无法直接绕过 Activation Lock 或篡改设备激活状态，限制了设备控制能力
- **仅 Books 同步场景**——攻击面聚焦；其他 AirTraffic 同步路径（Music / Photos / etc.）需独立研究
- **paired Mac 触发条件**——需要 Mac 与 iPhone 物理或近场接触 + Books 同步启用；远程攻击可能性低
- **公开 PoC 风险**——任何 paired Mac + Books sync 启用用户在补丁发布前暴露
- **fork 2 / 1 天 / 123 KB**——「学术 + 安全研究」圈层典型扩散速度，非大规模漏洞利用

## 与同类项目的关系
- **vs 其他 iOS 沙箱逃逸 PoC**：多数 iOS 沙箱逃逸研究在 iOS 17 后转向私下披露；airlift 是 2026 Q3 公开的最具体 iOS 27 沙箱绕过案例
- **vs Ian Beer / Google Project Zero iOS 研究**：Google Project Zero 是 iOS 公开研究的标杆；airlift 是 iOS 27.0 RC 阶段的极简 PoC
- **vs Apple Security Bounty 报告**：Apple Security 报告多私下披露 + 90 天补丁窗口；airlift 是「公开 PoC + 反 burn-for-clout 立场」的清晰样本
- **vs KernelSU / unc0ver / checkra1n 等越狱工具**：airlift 是数据读写 PoC 而非设备越狱；不涉及 Activation Lock 绕过或内核代码执行
- **vs Dr-TSNG/altdb（昨日 1 天 53⭐）**：altdb 是 KernelSU 模块（无线 ADB 替代）；airlift 是 iOS 沙箱逃逸 PoC（系统服务漏洞）——**不同安全研究类别**

## 是否值得持续跟踪
**值得跟踪（iOS 27.0 公开沙箱逃逸 PoC）。** airlift 代表了 iOS 27.0 公开沙箱逃逸的清晰样本，无论其本身被利用程度，这一方向是 Apple Security 工作的关键输入。建议关注：**(a) Apple Security 是否已收到报告 + 补丁窗口期**（决定实际攻击窗口）、**(b) PoC 是否被扩展到 MobileGestalt plist 或其他 AirTraffic 同步路径**（决定威胁面扩展）、**(c) iOS 27.0.x 后续补丁是否修复此漏洞模式**（决定 Apple Security 响应速度）。对企业 iOS 管理员：在补丁发布前应暂时关闭 Books 同步。

## 后续观察点
- Apple Security 补丁版本号与发布时间
- PoC 是否被扩展到其他 AirTraffic 同步路径（Music / Photos / etc.）
- 其他 iOS 27.0 公开沙箱逃逸 PoC 出现（airlift 是否是第一个）
- paired Mac 触发条件是否可远程化
- MobileGestalt plist 攻击路径是否被独立研究员补齐
- iOS 27.0.x 后续版本对 ATAirlock 路径校验的修复细节
- Apple Security Bounty 是否为此 PoC 设置类别

---
> 数据来源: GitHub API (2026-09-15) + README API readme 字段 base64 解码 | Stars: 33 | Forks: 2 | License: NOASSERTION | 语言: Objective-C | 创建: 2026-09-14
