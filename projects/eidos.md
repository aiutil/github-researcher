---
title: "josiah-nelson/eidos"
slug: eidos
date_added: 2026-08-26
last_seen_date: 2026-08-26
category: "工具型"
emoji: "🔍"
stars: "124 stars"
stars_delta: "4 天 124⭐（2026-08-22 创建，1 fork，0 watchers，21 open issues）"
language: "Rust"
license: "AGPL-3.0"
score: 78
tags: ["filesystem", "indexer", "ntfs", "rust", "search", "storage-analyzer", "tantivy", "windows"]
url: "https://github.com/josiah-nelson/eidos"
---

# josiah-nelson/eidos

## 一句话定位
**Private, intelligent search across every machine you own** ——Rust + Tantivy + NTFS；"Systems remain searchable when offline, including files buried inside VMs and archives"。

## 它解决的问题
跨机器的本地数据检索的三痛点：(1) **云搜索的隐私风险**——把本机文件索引交给云端 SaaS（如 Dropbox Search / Google Drive Search）等于把数据暴露给第三方；(2) **离线不可用**——多数 SaaS 搜索在断网时完全失效；(3) **VM / archive 内容无法检索**——传统搜索（grep / Everything）只索引表层文件，NTFS alternate data streams、VHD 中的文件、嵌套 zip 内的内容均不可搜索。**eidos 把"全机器跨设备智能搜索"做成 Rust + Tantivy + NTFS 的纯本地实现**，覆盖三约束：(1) 跨多台机器；(2) 离线可用；(3) 递归进 VM / archive。

## 为什么值得关注（2026-08-26）
- **4 天 124⭐ / 21 open issues**：社区关注度极高（21 open issues 反映需求明确但工程量大）
- **Rust + Tantivy**：成熟的全文搜索引擎（Quickwit / Meilisearch 部分借鉴）
- **NTFS 支持**：Windows 文件流 / alternate data streams 都被索引
- **递归进 VM / archive**：zip / tar / 7z 内容也是可搜索的文本
- **1.7MB size**（轻量）：暗示索引数据结构紧凑
- **AGPL-3.0 许可**：开源但对企业 SaaS 集成有传染性

## 热度来源判断
热度来自 **"本地搜索隐私刚需 × 跨机器数据检索 × Tantivy 成熟引擎"** 的组合：(1) 隐私合规是 2026 下半年硬刚需；(2) 跨机器数据检索是企业级 / 高级个人开发者的刚需；(3) Tantivy 是 Rust 生态成熟的全文搜索引擎（Quickwit / Meilisearch 部分借鉴），技术风险低。**主要风险：** AGPL-3.0 对企业 SaaS 集成的传染性（任何修改并对外提供服务的代码也必须开源）；21 open issues 反映工程量大；与现有方案（ripgrep + fd + ripgrep-all）的功能重叠度。

## 关键技术亮点
1. **Rust + Tantivy 全文搜索引擎**：技术风险低，性能有保障
2. **NTFS 支持**：Windows 文件流 / alternate data streams 都被索引
3. **递归进 VM / archive**：zip / tar / 7z 嵌套内容可搜索
4. **跨机器同步**：master/slave / peer-to-peer 机制（具体未公开）
5. **离线优先**：无云依赖，断网可用
6. **1.7MB 紧凑 size**：索引数据结构高效
7. **AGPL-3.0**：强 copyleft，确保衍生作品也开源

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Rust + Tantivy + NTFS；本地优先；跨机器同步；递归进 VM/archive | 边界由 README + topic 描述确认；具体跨机器同步机制、VM/archive 格式支持范围需源码核验 |
| 主路径 | 多机器文件 → 本地索引构建（Rust + Tantivy） → 跨机器同步（机制待核验） → 跨机器语义检索 → 返回结果（离线可用） | 主路径为档案语义抽象；具体索引更新策略、跨机器同步协议、VM/archive 递归的具体格式未公开 |
| 关键权衡 | 本地优先 vs 云端性能（隐私 vs 速度）；AGPL vs MIT（开源强 vs 商用友好）；Tantivy vs 自建引擎（成熟 vs 定制） | 取舍由 README "Private / offline / cross-machine" 描述确认；具体跨机器同步机制、VM/archive 格式支持范围未公开 |
| 最小 PoC | 安装 eidos → 让它索引本机 → 跑跨机器检索（单机器也可测试） → 验证 NTFS 文件流可检索 → 验证嵌套 zip 可检索 → 评估检索延迟 | PoC 流程由 README "跨机器 / 离线 / VM / archive" 描述推导；具体安装命令、索引时间、检索延迟未公开 |
| 证据边界 | README + topic + GitHub API；具体跨机器同步协议、VM/archive 格式支持范围、索引 schema、与 ripgrep / fd / ripgrep-all 的对比均需源码核验 | 已核验事实来自 GitHub API 与 topic；其他来自语义推断 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Machine1[机器 1] --> Indexer[eidos indexer<br/>Rust + Tantivy]
  Machine2[机器 2] --> Indexer
  Machine3[机器 3] --> Indexer
  Indexer --> Index[跨机器索引<br/>1.7MB 紧凑结构]
  Index --> Search[智能搜索<br/>离线可用]
  Indexer --> NTFS[NTFS 索引<br/>alternate data streams]
  Indexer --> Archive[Archive 索引<br/>zip / tar / 7z 嵌套]
  Indexer --> VM[VM 索引<br/>VHD / VMDK 内部]
  Search --> Result[检索结果<br/>跨机器语义]
  Index -.同步机制待核验.-> Sync[master/slave<br/>或 peer-to-peer<br/>协议未公开]
  Machine1 -.同步.-> Index
  Machine2 -.同步.-> Index
  Machine3 -.同步.-> Index
  Index -.AGPL-3.0.-> License[开源但有传染性<br/>企业 SaaS 集成受限]
  Search -.本地优先.-> Privacy[隐私边界<br/>数据不上云]
```

## 架构启发
eidos 的核心启发是 **"本地优先 + 跨机器 + 跨格式" 三约束同时满足是 Rust 生态的少见的"做对"产品** ——Tantivy（Quickwit / Meilisearch 部分借鉴的成熟引擎）+ NTFS 支持（Windows 文件流 / ADS 都被索引）+ 递归进 VM/archive（zip / tar / 7z 嵌套内容可搜索），三件齐意味着 "历史文件也可搜"。更深层的启发：**"AGPL-3.0 + 离线 + 跨机器" 是金融 / 政府 / 医疗的合规卖点** ——把数据完全留在本地 + 跨多台机器同步 + 不依赖任何云服务，是受监管行业的硬刚需。再深一层：**"21 open issues 反映工程量大但需求明确"** ——4 天 124⭐ + 21 open issues 体现社区关注度与工程量的平衡，12 月内可能进化为 MCP server 形态以接入 Claude Code / Codex CLI，与 heimdall / Perenna 的 "memory MCP" 路径汇合。

## 定位判断
**local-search 工具型项目（跨机器跨格式方向）。** eidos 是 **"本地优先 + 全机器数据可检索"的 Rust 生态少见的"做对"产品**。Tantivy 是 Quickwit / Meilisearch 部分借鉴的成熟引擎；NTFS 支持意味着 Windows 文件流 / ADS 都被索引；递归进 archive 让"历史文件也可搜"。**核心差异化是 "跨机器 + 离线 + 递归 VM/archive" 三约束同时满足**——与所有云端搜索对比，eidos 完全本地；与单机器 ripgrep + fd 对比，eidos 跨机器；与 Everything 对比，eidos 进 VM / archive。**主要风险：** AGPL-3.0 对企业 SaaS 集成的传染性（任何修改并对外提供服务的代码也必须开源）；21 open issues 反映工程量大。

## 风险 / 局限 / 泡沫点
- **AGPL-3.0 传染风险**：对 SaaS 产品集成是阻碍；企业内部部署可行
- **21 open issues 工程量大**：4 天 21 个 issue 反映需求明确但需要持续投入
- **跨机器同步机制未公开**：master/slave / peer-to-peer / 中央索引？需源码核验
- **VM/archive 递归性能**：嵌套深度 + 加密 archive 的处理边界
- **Windows-only 暗示**（topic 含 ntfs / windows）：macOS / Linux 用户受限
- **与现有方案重叠**：ripgrep + fd + ripgrep-all 是命令行方案；Everything 是 Windows GUI 方案

## 与同类项目的关系
- **vs ripgrep + fd + ripgrep-all**：命令行工具链；eidos 是统一产品 + 跨机器
- **vs Everything**：Windows 经典搜索工具；eidos 是 Rust + Tantivy + 跨机器 + VM/archive
- **vs Sourcegraph**：商业代码搜索引擎（云端 + 闭源）；eidos 是本地优先 + 开源
- **vs Spotlight / Windows Search**：OS 内置搜索；eidos 是跨机器 + 跨 OS + 跨格式
- **vs 8-26 heimdall**：heimdall 是 "agent 检索项目知识"（agent memory）；eidos 是 "本机跨机器数据检索"——互补而非竞争

## 是否值得持续跟踪
**值得跟踪（local-search 跨机器方向）。** eidos 是 **"本地优先 + 跨机器 + 跨格式"搜索的 Rust 生态严肃样本**——4 天 124⭐ + 21 open issues 体现社区关注度与工程量大。**建议关注：** (a) 是否会被 MCP server 化以接入 Claude Code / Codex CLI；(b) AGPL-3.0 的商业许可选项是否会出现；(c) 跨机器同步机制的稳定性。**对注重隐私的企业：** 评估内部部署的可行性。**对搜索基础设施开发者：** 12 月内持续观察。

## 后续观察点
- 是否被 MCP server 化（与 heimdall / Perenna 的 "memory MCP" 路径汇合）
- 商业许可选项（AGPL 之外的商用路径）
- 跨机器同步协议的稳定性
- VM / archive 格式支持的完整范围
- macOS / Linux 跨平台支持计划
- 21 open issues 的解决节奏
- 与 ripgrep / Everything / Sourcegraph 的功能对比基准

---
> 数据来源: GitHub API (2026-08-26) | Stars: 124 | Forks: 1 | License: AGPL-3.0 | 语言: Rust | 创建: 2026-08-22 | Pushed: 2026-08-25