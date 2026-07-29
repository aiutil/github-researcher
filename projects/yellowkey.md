---
title: "YellowKey"
slug: "yellowkey"
date_added: "2026-05-14"
category: "安全研究"
emoji: "🔑"
stars: "927 stars"
stars_delta: "2 天 927 stars，安全社区高关注度"
language: "N/A"
score: 90
tags: ["bitlocker", "windows", "vulnerability", "bypass", "security", "winre"]
url: "https://github.com/Nightmare-Eclipse/YellowKey"
last_seen_date: "2026-05-15"
---

# YellowKey

## 一句话定位
Windows BitLocker 绕过漏洞 PoC，声称在 WinRE 中发现疑似后门组件，仅影响 Windows 11/Server 2022/2025。

## 它解决的问题
这不是解决用户问题的项目，而是暴露了一个严重的安全问题：攻击者可以通过特制的 USB 存储设备绕过 BitLocker 全盘加密，获得对加密卷的无限制 shell 访问。

**利用方式**：
1. 将 FsTx 文件夹复制到 USB 存储设备的 `System Volume Information` 路径
2. 插入目标 Windows 11 电脑
3. 进入 WinRE（Shift+重启，然后按住 Ctrl）
4. 获得无限制 shell 访问加密卷

**核心指控**：触发漏洞的组件仅存在于 WinRE 镜像中，正常 Windows 安装中有同名组件但无此功能 — 暗示可能是故意放置的后门。

## 为什么值得关注（2026-05-14）
- 安全漏洞类项目极少在 2 天内获得近千 star
- 涉及 Windows 安全架构的核心信任链
- 已与 Microsoft 安全团队（MORSE、MSTIC、GHOST）协调披露
- 仅影响 Windows 11+，Windows 10 不受影响

## 热度来源判断
热度真实。BitLocker 是企业级全盘加密的标准方案，绕过漏洞直接威胁所有依赖 BitLocker 的企业。作者提供了完整复现步骤，且已与微软安全团队协调。

## 关键技术亮点
1. **WinRE 攻击面**：Windows Recovery Environment 中的组件具有比正常系统更高的权限，这是安全审计的盲区
2. **FsTx 组件异常**：同名组件在正常系统和 WinRE 中功能不同，这是"疑似后门"指控的技术依据
3. **物理攻击向量**：需要物理访问或 EFI 分区写入权限，但攻击门槛极低（一个 USB 设备即可）

## 架构启发
- 操作系统的恢复环境是安全审计的薄弱环节
- 全盘加密的安全依赖于加密外的组件（引导、恢复环境）的完整性
- 供应链安全不只是软件包，还涉及操作系统内置组件的可审计性

## 定位判断
安全研究 / 漏洞披露。不是可部署的工具，而是安全团队必须评估的威胁情报。

## 风险 / 屧限 / 泡沫点
1. **"后门"指控尚未独立验证**：作者声称是后门，但可能只是设计缺陷，需要安全社区独立确认
2. **攻击需要物理访问**：远程攻击场景有限
3. **PoC 级别**：没有提供修复方案或检测工具

## 与同类项目的关系
- CVE-2026-31431（前一日热门）：同属 Windows 安全漏洞赛道
- BitLocker 相关安全研究一直是企业安全的高优先级领域

## 是否值得持续跟踪
**是**。等待 Microsoft 官方回应和独立安全团队的验证结果。

## 后续观察点
1. Microsoft 是否发布安全公告和补丁
2. 独立安全研究团队是否验证"后门"指控
3. 是否催生 WinRE 审计工具生态

---
*首次记录：2026-05-14*

## 最近动态 (2026-05-15)

- **2026-05-15:** 网络受限日，趋势延续分析。基于 05-14 实测数据推算，持续跟踪中。
- Stars 数据为推算值，网络恢复后验证。

---
