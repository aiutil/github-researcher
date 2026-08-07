---
title: "MasterHttpRelayVPN"
slug: "master-http-relay-vpn"
date_added: "2026-04-26"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "🔒"
stars: "3,941 stars"
stars_delta: "forks 460，活跃增长中"
language: "Python"
license: "MIT"
score: 60
tags: ["proxy", "domain-fronting", "vpn", "censorship-circumvention", "google-apps-script"]
url: "https://github.com/masterking32/MasterHttpRelayVPN"
homepage: "https://t.me/masterdnsvpn"
---

# MasterHttpRelayVPN

## 一句话定位

利用 Google Apps Script 域前置（domain fronting）的 HTTP/SOCKS5 代理隧道，流量经 Google 网络中继到目标站点，支持 MITM TLS 拦截、HTTP/1-2 多路复用和 DPI 规避。

## 它解决的问题

在受限网络环境中建立代理隧道，利用 Google Apps Script 作为中继实现域前置。流量路径：`Browser → Local proxy → Google front → Apps Script relay → Target site`，使网络过滤器看到的只是连接到 Google 的流量。只需一个免费 Google 账户即可部署。

## 为什么值得关注

1. **技术思路巧妙** — 利用 Google Apps Script（免费、可信域名）作为代理中继
2. 3,941 stars / 460 forks，在隐私/翻墙社区有实际用户群
3. 支持可选 exit node（Cloudflare Workers / VPS），解决部分站点封锁 Google IP 的问题
4. 已内置绕过 YouTube safe search 和直播限制

## 热度来源判断

- **隐私/翻墙社区驱动。** 技术上有创新但受众有限
- 主要在受限网络地区（如伊朗 — 有波斯语 README）传播
- Telegram 频道（@MasterDnsVPN）运营活跃

## 关键技术亮点

1. **Google Apps Script 域前置**：利用 Google 可信域名做流量伪装
2. **MITM + Domain Fronting 双技术**：中间人拦截 + 域前置组合
3. **HTTP/1-2 多路复用**：提升代理吞吐
4. **可选 exit node 架构**：Cloudflare Workers / VPS 作为出口节点，解决目标站点封锁 Google IP 的问题
5. 支持 LAN 共享、Docker 部署，一键启动器（Windows/Linux/macOS）

## 架构启发

**利用可信云服务的免费层作为代理基础设施**是一个可复用的模式。Google Apps Script 的 Web App 部署 + 域前置，本质上是用 Google 的 CDN 网络做免费代理。这种"借力大平台基础设施"的思路在其他场景也有参考价值。

## 定位判断

**工具型。** 短期热点。与 AI/开发趋势无关，但作为隐私工具在特定地区有持续需求。

## 风险 / 局限 / 泡沫点

1. **域前置技术随时可能被 Google 封堵** — Google Apps Script 政策变化是最大风险
2. **MITM TLS 有安全和法律风险** — 需要在本地安装 CA 证书
3. **与 AI/开发趋势无关**，不在本仓库核心关注范围
4. 目标站点可能封锁 Google 出口 IP（需 exit node 解决）

## 与同类项目的关系

- **Shadowsocks / V2Ray / Xray**：主流翻墙工具，MasterHttpRelayVPN 以 Google Apps Script 为差异化
- **已有 Rust 移植版** MasterHttpRelayVPN-RUST（社区贡献）
- **Cloudflare Workers 代理方案**：同为"利用大平台免费层做代理"的思路

## 是否值得持续跟踪

**否。** 与 AI 趋势无关，技术思路已记录，后续无需深度跟踪。

## 后续观察点

- Google 是否会封堵 Apps Script 域前置
- 项目活跃度（最后 push 2026-06-09，需关注是否持续维护）
