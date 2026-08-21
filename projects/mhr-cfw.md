---
title: "mhr-cfw"
slug: "mhr-cfw"
date_added: "2026-05-04"
category: "工具型"
emoji: "🌐"
stars: "1.9k stars"
stars_delta: "7天 1.9K，快速爆发"
language: "Python"
score: 76
tags: ["dpi-bypass", "domain-fronting", "gas", "cloudflare-workers", "censorship", "tls", "sni"]
url: "https://github.com/denuitt1/mhr-cfw"
last_seen_date: "2026-05-04"
---

# mhr-cfw

## 一句话定位
基于 Domain Fronting 的 DPI 绕过方案 — 通过 Google Apps Script 中继 + Cloudflare Workers 转发，利用 TLS SNI 隐藏实现网络审查绕过。

## 它解决的问题
在某些网络环境下，深度包检测（DPI）会阻止特定网站的访问。mhr-cfw 通过域前置技术，将流量伪装为对合法域名（Google Apps Script / Cloudflare）的访问来绕过检测。

面向的用户：在受限网络环境下需要自由访问互联网的用户。

## 为什么值得关注（2026-05-04）
- 7天 1.9K stars，反映了当前网络环境的现实需求
- 技术路线清晰：GAS 中继 → CF Workers 转发 → TLS SNI 隐藏
- MIT 开源，代码简洁
- 有 Rust 移植版（MasterHttpRelayVPN-RUST，1.6K stars），说明社区认可度高

## 热度来源判断
需求驱动 + 社会事件催化。不是技术突破驱动的 star，而是现实需求驱动的。热度与特定地区的网络政策变化高度相关。

## 关键技术亮点亮点

1. **GAS 中继层** — 利用 Google Apps Script 作为第一跳中继，流量表现为对 Google 服务的正常访问
2. **Cloudflare Workers 转发** — 第二跳利用 CF Workers 的边缘计算能力，进一步隐藏真实目标
3. **TLS SNI 隐藏** — 通过域前置使 TLS 握手中的 SNI 字段指向合法域名
4. **零基础设施** — 不需要自建服务器，完全利用免费平台

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 客户端 → GAS 中继 → Cloudflare Workers 转发 → 真实目标；依赖 Google 与 Cloudflare 两层受信任基础设施作为代理边界 | 档案明确 GAS、CF Workers、TLS SNI 域前置三层结构；无协议、部署形态、鉴权方式细节（待核验） |
| 主路径 | 客户端流量经 GAS 中继改写为对 Google 信任域的正常请求，再由 CF Workers 转发至真实目标，TLS 握手中 SNI 指向合法域名 | 主路径来自档案"关键技术亮点"；请求编码、中继 endpoint、Workers 路由规则均未给出（待核验） |
| 关键权衡 | 零基础设施成本与运维负担 vs 对 Google/Cloudflare 政策的高度依赖；个人场景可用 vs 不保证稳定性与合规风险 | 档案明示"零基础设施"与"平台依赖风险/不适合生产/合规风险"；性能、延迟、SLO 缺数据（待核验） |
| 最小 PoC | 单客户端 + GAS Web App 中继脚本 + 一个 CF Workers 转发路由 + 一个被测目标域名，验证 TLS SNI 是否成功伪装以及两端连通性 | 仅指出 PoC 应包含的组件类别；具体 GAS 代码、Workers 脚本、超时与重试策略档案未证（待核验） |

## 架构启发

从架构角度，这是一个典型的"利用合法基础设施作为代理"的设计模式：
- **第一层伪装**：GAS（Google 信任域）
- **第二层转发**：CF Workers（CDN 信任域）
- **核心机制**：TLS SNI 域前置

这种架构的巧妙之处在于每一层都是合法的、广泛使用的基础设施，单独看无法区分正常流量和代理流量。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    C[客户端] -->|HTTPS 请求| GAS[Google Apps Script 中继]
    GAS -->|伪造为 Google 信任域请求| CF[Cloudflare Workers 转发]
    CF -->|TLS SNI 指向合法域名| T[真实目标站点]
    GAS -.平台政策封堵.- R[(风险边界:Google 策略变化])
    CF -.平台政策封堵.- R
    GAS -.合规风险.- L[(法律/政策边界:各地法规待核验)]
    W[Workers 路由与脚本配置]:::待核验 --> CF
    S[GAS Web App endpoint]:::待核验 --> GAS
    classDef 待核验 stroke-dasharray: 5 5
```

## 定位判断
特定场景下的实用工具。不属于平台或基础设施，生命周期受制于 Google/Cloudflare 的政策。

## 风险 / 局限 / 泡沫点

1. **平台依赖风险** — GAS 和 CF Workers 随时可能封堵域前置行为
2. **不适合生产** — 仅适用于个人临时使用，不保证稳定性和性能
3. **合规风险** — 在某些环境下使用可能违反法律法规
4. **代码质量一般** — 49 个 open issues，MIT 许可但维护活跃度存疑

## 与同类项目的关系

| 项目 | 语言 | 定位 | 优势 | 劣势 |
|------|------|------|------|------|
| mhr-cfw | Python | GAS+CF 域前置 | 零基础设施、简单 | 平台依赖 |
| MasterHttpRelayVPN-RUST | Rust | Rust 移植版 | 性能好、桌面 UI | 同样的平台依赖 |
| Cloudflare WARP | — | 官方 VPN | 稳定、官方支持 | 不是开源方案 |

## 是否值得持续跟踪
**有限跟踪。** 技术方案本身不复杂，主要关注方向是：这类域前置方案的生命周期和平台对策。

## 后续观察点

1. Google/Cloudflare 是否会更新策略封堵域前置
2. Rust 移植版的发展 — 是否会发展出更完整的桌面应用
3. 同类方案的涌现速度 — 是否会出现更多变体

---
*首次记录：2026-05-04*
