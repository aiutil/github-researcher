---
title: "furkan-bayrak/lg-tv-blocklist"
slug: lg-tv-blocklist
date_added: "2026-09-12"
category: "工具型"
emoji: "📺"
stars: "125 stars"
stars_delta: "3 天 125⭐ / fork 2"
language: "Python"
score: 76
tags: ["dns", "blocklist", "adguard-home", "pi-hole", "lg-tv", "webos", "privacy", "telemetry", "ad-blocking", "cc-by-4.0"]
url: "https://github.com/furkan-bayrak/lg-tv-blocklist"
---

# furkan-bayrak/lg-tv-blocklist

## 一句话定位
LG webOS TV 遥测 / 广告 / phone-home DNS 拦截列表——safe + strict 双层；AdGuard Home / Pi-hole 直接接入；CC-BY-4.0（署名即可商用）。

## 它解决的问题
LG webOS TV（LG 智能电视操作系统）在客厅场景出货量大，但默认开启大量遥测、广告追踪、phone-home 数据外发——用户的观看行为、广告 ID、设备指纹持续发往 LG 服务器。**lg-tv-blocklist 提供 curated DNS blocklist，按 safe（保守，仅阻止明确遥测 / 广告）+ strict（激进，阻止所有可疑 LG 子域）双层分级**。家庭网络只需把列表喂给 AdGuard Home 或 Pi-hole，所有 LG TV 设备自动获益。

## 为什么值得关注（2026-09-12）
- 3 天 125⭐ / fork 2
- Python（用于列表生成 / 校验工具）
- 120 KB 仓库体积（紧凑）
- CC-BY-4.0 license——**鼓励衍生与商业化（署名即可）**
- safe + strict 双层分级（用户可按风险偏好选择）
- AdGuard Home + Pi-hole 双兼容（主流家庭网络 ad-block 平台）
- 精确定位 LG webOS TV 单一品牌（垂直细分）

## 热度来源判断
家庭网络 ad-block（AdGuard Home / Pi-hole）在 2026 年持续渗透，DNS 拦截列表是刚需——但主流列表（StevenBlack / OISD / Hagezi）覆盖范围太广，新手难以判断哪些条目会影响正常功能。**lg-tv-blocklist 切入「单品牌垂直化」**——精准只针对 LG webOS TV，提供 curated 与分级。**热度来源是「LG TV 客厅场景基数 × DNS 拦截刚需 × 家庭隐私意识上升 × 双层分级降低使用门槛」四因素叠加**。CC-BY-4.0 鼓励衍生与商业化。**热度真实且垂直**，未来可能出现同类"三星 Tizen TV blocklist"、"Sony Bravia blocklist"等。

## 关键技术亮点
1. **safe + strict 双层分级**：safe 保守（仅阻止明确遥测 / 广告）/ strict 激进（阻止所有可疑 LG 子域）——用户按风险偏好选择
2. **AdGuard Home + Pi-hole 双兼容**：直接接入主流家庭网络 ad-block 平台，无需自定义
3. **Python 列表生成 / 校验工具**：列表质量可审计、可追溯
4. **LG webOS TV 垂直细分**：精确定位 LG 单一品牌，避免主流列表的"过度拦截"
5. **CC-BY-4.0 license**：鼓励衍生与商业化（署名即可）
6. **120 KB 紧凑体积**：便于镜像分发与版本控制

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | DNS 拦截列表 + Python 列表生成 / 校验工具；用户部署到 AdGuard Home 或 Pi-hole | 仅基于 README 与 GitHub 元数据；具体拦截域名数量、更新频率、误杀测试覆盖矩阵均待核验 |
| 主路径 | LG TV 发起网络请求（DNS 查询）→ AdGuard Home / Pi-hole DNS 拦截 → 命中 blocklist 域名 → 返回 0.0.0.0 / NXDOMAIN → 阻断遥测 / 广告 / phone-home | 主路径为 README 语义抽象；DNS 拦截响应延迟、子域递归覆盖、DNS-over-HTTPS 兼容均待核验 |
| 关键权衡 | 拦截完整度 vs 误杀风险（影响 LG TV 正常功能） vs 列表更新频率 vs 单品牌垂直 vs CC-BY-4.0 衍生 vs 早期阶段社区 | 档案明示「safe + strict 双层」与「单品牌垂直」两点；具体误杀测试覆盖、列表自动化更新机制、LG 新版 webOS 子域跟进均待核验 |
| 最小 PoC | 在家庭网络部署 AdGuard Home（已有或新装）；添加 lg-tv-blocklist safe 层；让 LG webOS TV 联网一天；检查 (a) 广告是否消失 (b) TV 正常功能（应用商店 / Netflix / YouTube）是否受影响 (c) AdGuard Home 日志拦截量 | PoC 范围与退出路径由档案"先 safe 层、最小化误杀、可回滚"原则推导；具体 LG TV 型号兼容矩阵、列表更新频率、strict 层启用建议均待核验 |
| 依赖与红线 | 依赖 AdGuard Home / Pi-hole；CC-BY-4.0 允许商业衍生（需署名）；LG TV 升级 webOS 后新增子域需要列表跟进 | 依赖与红线均来自 README + GitHub 元数据；具体列表自动更新机制、LG 新 webOS 子域跟进节奏、DNS-over-HTTPS 兼容均待核验 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
  LGTV[LG webOS TV] -->|DNS 查询| Router[家庭路由器 DNS]
  Router -->|转发| AdGuard[AdGuard Home / Pi-hole]
  AdGuard -->|查询 blocklist| BlockList[lg-tv-blocklist<br/>safe / strict 双层]
  BlockList -->|命中域名| Blocked[返回 0.0.0.0 / NXDOMAIN]
  BlockList -->|未命中域名| Allow[放行到上游 DNS]
  Blocked -->|阻断遥测 / 广告 / phone-home| LGServer[LG 服务器]
  Allow -->|正常访问| Internet[互联网]
  BlockList -.Python 校验工具.-> Tool[列表质量可审计]
  BlockList -.CC-BY-4.0.-> License[鼓励衍生与商业化]
  LGTV -.升级 webOS 后子域变化.-> Compat[列表跟进节奏 待核验]
```

## 架构启发
lg-tv-blocklist 的核心启发是 **「DNS 拦截列表垂直化」**——主流列表（StevenBlack / OISD / Hagezi）覆盖范围太广，新手难以判断哪些条目会影响正常功能；垂直化列表（按品牌 / 场景）降低使用门槛、提高拦截精确度。**更深层的启发是「safe + strict 双层分级」**——给用户按风险偏好选择的余地，避免"过度拦截"和"拦截不足"两个极端。**最值得借鉴的是「CC-BY-4.0 license」**——鼓励衍生与商业化（署名即可），适合"基础设施型列表"。

## 定位判断
**工具型项目（家庭网络 DNS 拦截垂直化）。** lg-tv-blocklist 与 StevenBlack / OISD / Hagezi 等主流 DNS blocklist 处于同一赛道，但走"单品牌垂直化"差异化路线。**真正的差异化是「单品牌垂直 + safe/strict 双层分级」**——精准只针对 LG webOS TV，避免主流列表的"过度拦截"。能否扩展取决于：(a) 是否出现同类"三星 Tizen TV blocklist"、"Sony Bravia blocklist"、"Roku blocklist"等；(b) 列表自动化更新机制（决定长期可持续性）；(c) 误杀测试覆盖（决定实际可用性）。当前定位是"LG webOS TV 垂直 DNS 拦截列表首批标杆"，向更多品牌垂直化演进是合理路径。

## 风险 / 局限 / 泡沫点
- **早期阶段**：125⭐ / fork 2 反映用户基础小，列表自动化更新机制尚未成熟
- **LG webOS 版本跟进**：LG 升级 webOS 后新增子域需要列表同步跟进，否则部分遥测会漏网
- **误杀风险**：strict 层可能误杀 LG TV 正常功能（应用商店 / 系统更新 / Netflix 授权服务器等）
- **DNS-over-HTTPS 兼容**：部分 LG TV 启用 DoH 会绕过 AdGuard Home 拦截
- **CC-BY-4.0 衍生分散**：商业衍生版本可能分流用户
- **个人项目属性**：furkan-bayrak 个人维护，长期维护依赖作者持续投入

## 与同类项目的关系
- **vs StevenBlack / OISD / Hagezi 等主流 blocklist**：这些是综合性 blocklist；lg-tv-blocklist 是单品牌垂直 blocklist
- **vs AdGuard Home / Pi-hole**：这些是 DNS 拦截平台；lg-tv-blocklist 是 blocklist 数据源
- **vs NextDNS / ControlD**：这些是 SaaS DNS 服务（含 blocklist 订阅）；lg-tv-blocklist 是自托管数据源
- **vs 单品牌隐私项目（如 smart-tv-block）**：smart-tv-block 等也是单品牌垂直项目，定位类似
- **vs Brave / Firefox 内置隐私保护**：那些是浏览器侧；lg-tv-blocklist 是网络侧

## 是否值得持续跟踪
**值得短期观察（单品牌垂直 DNS blocklist 首批标杆）。** lg-tv-blocklist 代表了"主流 blocklist 过度拦截 + 垂直化降低门槛"的细分需求，无论其本身成败，这一方向会持续影响家庭网络隐私赛道。建议关注：(a) 是否出现同类垂直 blocklist（三星 / Sony / Roku 等）；(b) 列表自动化更新机制（决定长期可持续性）；(c) 误杀测试覆盖（决定实际可用性）。**对家庭网络隐私用户，这是 AdGuard Home / Pi-hole 用户的优秀数据源补充**。对家庭网络隐私观察者，它是"单品牌垂直化"的代表样本。

## 后续观察点
- 是否出现同类垂直 blocklist（三星 Tizen / Sony Bravia / Roku 等）
- 列表自动化更新机制（webOS 版本跟进）
- 误杀测试覆盖（TV 正常功能兼容矩阵）
- DNS-over-HTTPS 兼容（部分 LG TV 已支持 DoH）
- 是否提供 strict 层的"启用建议"文档
- 社区贡献机制（接受用户反馈新增 / 删除域名）

---

*首次记录：2026-09-12*
