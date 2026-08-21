---
title: "anthropics/claude-plugins-official"
slug: "claude-plugins-official"
date_added: "2026-05-22"
last_seen_date: "2026-08-11"
category: "平台候选"
emoji: "🔌"
stars: "33,389 stars"
stars_delta: "从22.2K到33.4K（3个月），日均~125 stars"
language: "Python"
license: "Apache-2.0"
score: 90
tags: ["Claude", "插件", "Anthropic", "Agent生态", "MCP", "Skills", "插件市场"]
url: "https://github.com/anthropics/claude-plugins-official"
---

# anthropics/claude-plugins-official — Anthropic 官方 Claude Code 插件目录

## 一句话定位
Anthropic 官方管理的高质量 Claude Code 插件目录（marketplace）——Agent 插件的标准化注册入口，类似 npm registry 之于 Node.js 生态，是 Claude 生态的官方"应用商店"。

## 它解决的问题
Claude Code Skills/Plugins 生态正在碎片化爆发，大量社区和个人 Skills 仓库涌现，但没有统一的质量标准和发现机制。开发者不知道该用哪个 Skill，Skill 作者缺乏分发渠道。anthropics/claude-plugins-official 提供官方管理的插件市场，通过 `/plugin install {name}@claude-plugins-official` 一键安装，解决发现-信任-安装三段式问题。

## 为什么值得关注（2026-08-11）
- **33,389 stars**（截至 2026-08-11），Apache-2.0 许可
- **3,766 forks**，大量开发者基于此分发自己的插件
- **204 subscribers**，深度关注
- **Anthropic 官方管理**：这是 Anthropic 直接维护的官方仓库（非社区项目）
- **当天推送**（pushed_at 2026-08-11），持续高活跃
- **标准化插件结构**：`.claude-plugin/plugin.json`（元数据）+ `.mcp.json`（MCP 配置）+ `commands/` + `agents/` + `skills/`
- **支持 Skill-bundle 插件**：可以打包第三方仓库的 Skills 而无需 manifest
- **不可变插件名 + 重命名映射**：`renames` map 确保用户安装的插件名变更后自动迁移
- 官方文档 code.claude.com/docs/en/plugins

## 热度来源判断
**Anthropic 官方品牌 + 生态刚需。** Claude Code 用户量爆发式增长，官方插件目录是发现插件的默认入口。日增 125 stars 来自 Claude Code 用户的实际需求——不是围观，而是"我要找插件来用"。3,766 forks 说明大量开发者在提交自己的插件到市场。这是典型的平台网络效应：用户越多 → 插件越多 → 价值越大 → 吸引更多用户。

## 关键技术亮点
1. **标准插件结构**：每个插件包含 `.claude-plugin/plugin.json`（必需元数据）+ 可选的 MCP 配置/命令/Agent 定义/Skills
2. **内部插件 vs 外部插件**：`/plugins`（Anthropic 内部开发）和 `/external_plugins`（第三方提交），双层质量管控
3. **Marketplace 模式**：通过 `/plugin marketplace add` 添加市场源，`/plugin install` 安装——类似 npm 的 registry 模式
4. **Skill-bundle 插件**：`strict: false` + `skills` 数组，可以打包没有 manifest 的 SKILL.md 文件集合
5. **不可变 slug + 自动迁移**：插件名一旦发布不可更改，通过 `renames` map 自动迁移旧名到新名
6. **外部插件提交流程**：通过 plugin-directory-submission 表单提交，需通过质量和安全审核

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 官方插件目录定位为 Claude Code Agent 插件的"注册-发现-安装"分发层与质量管控入口，自身不直接托管模型与工具，仅编排 marketplace.json 与插件源仓库 | 档案仅描述结构（plugin.json / .mcp.json / commands / agents / skills）与安装命令；运行时协议、服务器实现未在档案中证实 |
| 主路径 | 用户 `plugin install {name}@claude-plugins-official` → marketplace 拉取插件源 → Claude Code 加载 plugin.json 与 .mcp.json → 调用 MCP 工具 / Skills / Agents → 结果回写会话 | `install` 与 MCP 配置来自档案；具体解析顺序、版本协商、状态持久化方式待源码核验 |
| 关键权衡 | 官方双层（/plugins 内部 vs /external_plugins 第三方）+ `strict:false` Skill-bundle 与 `renames` 不可变 slug 机制，体现"生态扩张速度 vs 命名/质量稳定性"的取舍；安全审计靠 plugin-directory-submission 表单，覆盖度有限 | 双层目录与重命名映射来自档案；审核 SLA、签名机制、沙箱策略档案未给出 |
| 最小 PoC | 以单一 Skill-bundle 插件（无 manifest 的 SKILL.md 集合）接入 `claude-plugins-official`，最小工具权限下验证 `/plugin install`、MCP 加载与会话回写，再扩展到带 plugin.json 的标准插件 | 提交流程与命令来自档案；执行环境、权限模型、退出路径需结合 code.claude.com 文档与源码核验 |

## 架构启发
- **注册-发现-安装三段式架构**：这是所有插件市场的标准模式（npm/PyPI/VS Code Marketplace），Anthropic 在 Claude 生态中复现了它
- **官方目录 vs 社区市场的双轨模式**：官方保证质量底线，社区保证创新自由度——类似 Apple App Store vs TestFlight
- **Marketplace 作为分发协议**：插件不存储在 Anthropic 服务器，而是通过 marketplace.json 描述源仓库地址，运行时拉取——去中心化分发
- **MCP 作为工具协议**：插件通过 `.mcp.json` 接入 MCP Server，实现工具调用标准化

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    U[开发者或 Claude Code 用户] -->|/plugin install 或 marketplace add| MP[claude-plugins-official marketplace.json]
    MP --> PR[external_plugins 第三方插件源仓库 去中心化分发]
    MP --> PO[/plugins 内部插件 Anthropic 官方维护]
    PR --> P[plugin.json 元数据 不可变 slug renames 映射 待核验]
    PO --> P
    P --> M[.mcp.json MCP Server 配置]
    P --> SK[skills/ SKILL.md 集合 strict false 可打包]
    P --> AG[agents/ 与 commands/ 定义]
    M --> RT[Claude Code 运行时 编排层]
    SK --> RT
    AG --> RT
    RT --> ST[会话 状态 审计 待核验]
    RT --> RS[插件安全审核 plugin-directory-submission 表单 916 Open Issues 风险边界]
```

## 定位判断
**平台候选**——如果 Anthropic 持续投入，它将成为 Claude 生态的「npm registry」。控制了插件目录就控制了生态入口。目前已具备平台的所有要素：标准结构、提交流程、发现机制、安装命令。商业化潜力在于付费插件、企业私有市场、插件认证。

## 风险 / 局限 / 泡沫点
1. **916 Open Issues**：大量未解决问题，说明审核和响应速度跟不上增长
2. **过度依赖 Anthropic 单一厂商**：Anthropic 政策变化直接影响整个插件生态
3. **与社区仓库的边界不清晰**：superpowers（201K⭐）、wshobson/agents（38.6K⭐）等社区仓库是竞争还是补充？
4. **插件质量参差**：虽然有审核机制，但 external_plugins 的质量难以完全保证
5. **安全风险**：插件可能包含恶意 MCP Server 或 Prompt Injection，官方审核无法完全覆盖
6. **可能限制社区创新**：官方目录的存在可能让用户不去探索社区仓库

## 与同类项目的关系
- **vs superpowers (201K⭐)**：社区最大技能框架，互补但竞争——官方 vs 社区
- **vs wshobson/agents (38.6K⭐)**：跨平台 Agent 插件市场，官方仅服务 Claude
- **vs alirezarezvani/claude-skills (24.3K⭐)**：个人精选技能库，官方有审核机制
- **vs codegraph / ponytail 等**：这些是具体的插件/技能，可作为此目录的子集
- **vs npm / PyPI / VS Code Marketplace**：概念类比，但 Claude 插件生态远小于这些

## 是否值得持续跟踪
**是。** Anthropic 官方动作是生态风向标。插件目录的演进直接反映 Claude Code 的平台化进程。

## 后续观察点
1. 插件数量增长曲线（目前规模 vs npm/VS Code 等成熟市场）
2. 是否出现杀手级插件（定义一个品类的插件）
3. 是否引入付费机制或插件商店
4. 与社区仓库（superpowers、wshobson/agents）的整合方式
5. 企业级私有市场的推出
6. 插件安全审计机制的成熟度

---
> 数据来源: GitHub API (2026-08-11) | Stars: 33,389 | Forks: 3,766 | License: Apache-2.0 | 语言: Python | 创建: 2025-11-20
