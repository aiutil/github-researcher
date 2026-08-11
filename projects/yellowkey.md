---
title: "Nightmare-Eclipse/YellowKey"
slug: "yellowkey"
date_added: "2026-05-14"
last_seen_date: "2026-08-11"
category: "安全研究"
emoji: "🔑"
stars: "927 stars"
stars_delta: "2天927 stars，安全社区高关注度；仓库后续不可访问"
language: "N/A"
license: "N/A"
score: 90
tags: ["bitlocker", "windows", "vulnerability", "bypass", "security", "winre"]
url: "https://github.com/Nightmare-Eclipse/YellowKey"
---

# Nightmare-Eclipse/YellowKey — Windows BitLocker 绕过漏洞 PoC

## 一句话定位
YellowKey 是一个 Windows BitLocker 绕过漏洞的概念验证（PoC），声称在 WinRE（Windows Recovery Environment）中发现疑似后门组件，攻击者可通过特制 USB 存储设备获得对加密卷的无限制 shell 访问——仅影响 Windows 11/Server 2022/2025。

## 它解决的问题
这不是解决用户问题的项目，而是暴露了一个严重的安全问题。攻击链如下：
1. 将 FsTx 文件夹复制到 USB 存储设备的 `System Volume Information` 路径
2. 插入目标 Windows 11 电脑
3. 进入 WinRE（Shift+重启，然后按住 Ctrl）
4. 获得无限制 shell 访问加密卷

**核心指控**：触发漏洞的组件仅存在于 WinRE 镜像中，正常 Windows 安装中有同名组件但无此功能——暗示可能是故意放置的后门。

## 为什么值得关注（2026-08-11）
- **仓库状态**：截至 2026-08-11，GitHub API 返回 404——原仓库 `Nightmare-Eclipse/YellowKey` 已不可访问（可能被删除或转为私有）
- 安全漏洞类项目极少在 2 天内获得近千 star
- 涉及 Windows 安全架构的核心信任链
- 已与 Microsoft 安全团队（MORSE、MSTIC、GHOST）协调披露
- 仅影响 Windows 11+，Windows 10 不受影响
- 相关 CVE：搜索发现 `YellowKey-Bitlocker-CVE-2026-45585` 的衍生仓库存在

## 热度来源判断
热度真实。BitLocker 是企业级全盘加密的标准方案，绕过漏洞直接威胁所有依赖 BitLocker 的企业。作者提供了完整复现步骤，且已与微软安全团队协调。仓库后续不可访问（404）可能是 Microsoft 协调披露后的下架，或作者自行删除——无论哪种，都增加了安全社区的关注度。

## 关键技术亮点
1. **WinRE 攻击面**：Windows Recovery Environment 中的组件具有比正常系统更高的权限，这是安全审计的盲区
2. **FsTx 组件异常**：同名组件在正常系统和 WinRE 中功能不同，这是"疑似后门"指控的技术依据
3. **物理攻击向量**：需要物理访问或 EFI 分区写入权限，但攻击门槛极低（一个 USB 设备即可）
4. **绕过全盘加密**：BitLocker 本身没有被破解，而是绕过了它依赖的引导环境信任链

## 架构启发
- **操作系统的恢复环境是安全审计的薄弱环节**：WinRE 被设计用于系统修复，但其高权限组件缺少同等安全审查
- **全盘加密的安全性依赖加密外的组件**：引导环境、恢复环境的完整性是 BitLocker 安全的基础
- **供应链安全不只是软件包**：还涉及操作系统内置组件的可审计性——"同名不同功能"的组件是审计噩梦
- **信任链的断裂点**：安全链条的强度取决于最弱环节，BitLocker 加密再强，WinRE 组件可被滥用就等于前门上锁后门敞开

## 定位判断
安全研究 / 漏洞披露。不是可部署的工具，而是安全团队必须评估的威胁情报。仓库已不可访问，处于协调披露后的静默期。

## 风险 / 局限 / 泡沫点
1. **"后门"指控尚未独立验证**：作者声称是后门，但可能只是设计缺陷——需要安全社区独立确认
2. **仓库已下架（404）**：原 PoC 代码不可获取，后续验证困难
3. **攻击需要物理访问**：远程攻击场景有限
4. **PoC 级别**：没有提供修复方案或检测工具
5. **CVE 编号不确定**：衍生仓库提及 CVE-2026-45585，但官方 CVE 记录需确认
6. **信息可信度**：原仓库消失后，网络上流传的衍生仓库（如 `YellowKey-Bitlocker-CVE-2026-45585`）可信度参差不齐

## 与同类项目的关系
- **CVE-2026-31431（Copy Fail）**：前一日热门，同属 Windows 安全漏洞赛道
- **Dirty Pipe (CVE-2022-0847)**：Linux 内核的 Page-Cache Write 漏洞，不同平台但同类型
- **BitLocker 相关安全研究**：一直是企业安全的高优先级领域
- **衍生仓库**：多个 `YellowKey-Bitlocker-CVE-2026-45585` 命名的仓库出现在搜索结果中，但来源和可信度各异

## 是否值得持续跟踪
**是。** 等待 Microsoft 官方回应和独立安全团队的验证结果。仓库下架不代表问题消失——可能正处于补丁开发期。

## 后续观察点
1. Microsoft 是否发布安全公告和补丁（KB 文章）
2. 独立安全研究团队是否验证"后门"指控
3. CVE 编号的正式分配和描述
4. 是否催生 WinRE 审计工具生态
5. 企业级 BitLocker 部署指南是否因此更新
6. 原作者 Nightmare-Eclipse 是否在其他渠道发布更新

---
> 数据来源: GitHub API (2026-08-11) | 仓库状态: 404 Not Found（已下架或转为私有） | 历史 Stars: ~927（2026-05-14）
