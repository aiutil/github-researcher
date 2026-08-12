---
title: "sohaibdevv/youtube-music"
slug: "youtube-music"
date_added: "2026-08-13"
last_seen_date: "2026-08-13"
category: "观察型"
emoji: "⚠️"
stars: "848 stars"
stars_delta: "+848 (0→848，两日；fork 0，open issues 0)"
language: "TypeScript"
license: "MIT"
score: 65
tags: ["case-study", "suspected-malware", "password-zip", "zero-fork-anomaly", "evidence-ledger", "typescript"]
url: "https://github.com/sohaibdevv/youtube-music"
---

# sohaibdevv/youtube-music

## 一句话定位
疑似恶意软件投递伪装样本——README 声称"YouTube Music 免费客户端"，但以密码保护 ZIP（Password: ytm4all）分发可执行文件，848 stars / 0 forks 的极端背离 + 密码 ZIP 分发模式是经典恶意软件投递特征，作为"开源平台信任滥用"的新型风险对照案例入库（推断，ZIP 载荷未下载验证）。

## 它解决的问题（声称 vs 实际）
**README 声称：** 轻量级、无广告 YouTube Music 流媒体客户端，支持后台播放、搜索、本地播放列表、媒体键控制、暗色主题、单文件 EXE 免安装。
**实际判断（推断）：** 分发模式（密码保护 ZIP + 可执行文件）与"开源项目"定位矛盾。合法开源项目以源码仓库 + CI/CD 构建分发，而非密码保护的二进制压缩包。848 stars / 0 forks 的极端背离进一步支持"非自然热度"判断。

## 为什么值得关注（2026-08-13）
- **新型风险样本：** 与 WeChat-AI（fork≈star 刷量模式）不同，youtube-music 呈现 **0 fork + 密码 ZIP 分发**——这是经典恶意软件投递向量，代表"开源平台信任滥用"的新模式。
- **方法论对照价值：** 与 WeChat-AI（热度数据异常）+ open-kimi-ppt-skill（归档后 fork 异常增长）构成三类不同的"热度≠价值"风险样本。
- **平台安全信号：** GitHub 作为开源分发平台的信任正在被利用——密码 ZIP + 高 star 低参与度是新的风险信号模式，值得研究者建立检测规则。

## 热度来源判断
**判断：疑似恶意软件投递驱动的非自然热度（推断，未验证载荷）。**
- **848 stars / 0 forks = 极端背离：** 一个有 848 人 star 的项目不可能 0 fork。fork 是开源项目参与的最低门槛，0 fork 意味着"848 人看了 README 想 star，但没人想看代码/fork/改进"——这与正常开源项目行为模式严重矛盾。
- **密码保护 ZIP：** README 明确 `Password: ytm4all`，下载 `youtube-music-free.zip` 解压运行 `youtube-music-free.exe`。合法开源项目不使用密码 ZIP 分发——密码 ZIP 是规避自动扫描的经典手法。
- **作者画像：** sohaibdevv（2024-10 注册，95 公开仓库，9 followers）。95 个公开仓库但仅 9 followers，账号活跃度与影响力不匹配。
- **0 open issues：** 848 stars / 0 issues 意味着无用户反馈——对一个"音乐客户端"来说不正常（通常会有 bug 报告、功能请求）。

**⚠️ 关键证据边界：以上为基于 API 字段和 README 分发模式的推断。未下载 ZIP、未分析实际载荷——标记为待观察。**

## 关键技术亮点
**不适用。** 本档案的价值在于风险分析而非技术评估。README 描述的"功能"（无广告、后台播放等）为声称内容，未验证。

## 架构启发
（不适用——风险样本，非技术参考项目）

## 定位判断
**观察型（疑似恶意软件投递样本，证据账本对照案例）。** youtube-music 的核心价值是作为"开源平台信任滥用"的证据样本。它与 WeChat-AI（刷量型）、open-kimi-ppt-skill（归档后异常增长型）构成三类不同的"热度≠价值"风险模式。研究者可基于此建立检测规则：**密码 ZIP + 高 star 低参与度（0 fork/0 issue）= 投递型风险信号。**

## 风险 / 局限 / 泡沫点
- **疑似恶意软件投递（核心风险，推断未验证）：** 密码保护 ZIP + 可执行文件分发是经典恶意软件投递向量。未下载验证实际载荷。
- **版权侵权风险：** 即使功能如 README 所述（无广告 YouTube Music 流媒体），也涉及 YouTube 服务条款违规和潜在版权问题。
- **平台信任侵蚀：** 此类项目利用 GitHub 的开源信誉作为分发渠道，侵蚀平台信任。
- **热度真实性存疑：** 848 stars / 0 forks 的极端背离可能是刷量/购买 star，也可能是恶意软件投递 campaign 的一部分。

## 与同类项目的关系
- **vs SMNETSTUDIO/WeChat-AI（刷量型）：** WeChat-AI 是 fork≈star 的刷量模式（热度数据异常）；youtube-music 是 0 fork + 密码 ZIP 的投递模式（分发模式异常）。两者风险本质不同。
- **vs Binaryify/open-kimi-ppt-skill（归档后异常增长型）：** open-kimi-ppt-skill 归档后 fork 仍异常增长，是"僵尸热度"信号；youtube-music 是"活跃投递"信号。

## 是否值得持续跟踪
**作为证据账本对照案例入库（非技术跟踪）。** youtube-music 的价值在于方法论——为"开源平台信任滥用"提供新的检测信号模式（密码 ZIP + 0 fork + 0 issue）。建议关注：项目是否被 GitHub 下架、star 数后续变化（是否持续增长说明投递 campaign 活跃）、是否出现更多同模式项目。

## 后续观察点
- 项目是否被 GitHub 安全团队下架/标记
- star 数后续变化（若持续快速增长，说明投递 campaign 仍在活跃）
- 是否出现更多"密码 ZIP + 高 star 低 fork"同模式项目
- 作者 sohaibdevv 其他 95 个仓库是否有类似模式

---
> 数据来源: GitHub API (2026-08-13) | Stars: 848 | Forks: 0 | Open Issues: 0 | License: MIT (声称) | 语言: TypeScript | 创建: 2026-08-11 | 作者: sohaibdevv (GitHub since 2024-10, 95 repos, 9 followers) | ⚠️ 疑似恶意软件投递样本——ZIP 载荷未下载验证，"恶意软件"判断为推断
