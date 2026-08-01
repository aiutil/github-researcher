---
title: "VictorTaelin/OptMem"
slug: optmem
date_added: "2026-08-02"
last_seen_date: "2026-08-02"
category: "工具型"
emoji: "🧠"
stars: "1,058 stars"
stars_delta: "7/25创建→8/02 1,058⭐，8天破千"
language: "Python"
license: "未声明"
score: 85
tags: ["agent-memory", "persistent-memory", "append-only", "minimal", "single-file", "python", "position-is-identity"]
url: "https://github.com/VictorTaelin/OptMem"
---

# OptMem — Agent 永久记忆（426-token prompt + 单 Python 脚本）

## 一句话定位
用 426-token 的 prompt + 单个无依赖 Python 脚本，给 AI agent 一个永久的、可重建的记忆系统——没有数据库、没有后台进程、没有依赖。

## 它解决的问题
目标用户是自建 agent（用 Claude Code/Codex/任意 agent）的开发者。痛点：agent 每次会话从零开始，没有跨会话记忆；现有记忆方案（向量库 + 数据库 + 后台服务）重、有依赖、与具体平台绑定。OptMem 要解决的是"让 agent 在任何会话/模型/厂商切换后仍记得自己是谁、做过什么"，且**集成成本极低**（贴一段 prompt 即完成）。

## 为什么值得关注（2026-08-02）
在应用层（qm/qwen-audio-agent）把 agent 做成完整产品的同时，记忆作为**可独立交付的最小单元**开始成型。OptMem 是这条路线里最极简的一个——1,058⭐/61 fork，作者 VictorTaelin（HVM/Formality 的作者，交互式定理证明器与函数式语言背景，有技术公信力）。它的设计哲学（数据格式即索引、缓存可重建、无后台进程）对任何做 agent 基础设施的人都有启发。

## 热度来源判断
- **真实需求信号**：fork 61（高于同期 star 量级项目）说明有人在尝试集成；agent 记忆是 coding agent 生态的普遍痛点。
- **话题性成分**：作者声誉（HVM 作者）带来初始关注度；"426-token + 单脚本"的极简叙事有传播性。
- **不推荐点**：license 未声明（README 无 LICENSE 文件提及），采用上有法律不确定性。

## 关键技术亮点

1. **Position-is-identity**：记忆记录定长（≤280B/条），位置即身份，每次 lookup 是一次磁盘 seek。1M 记忆（608MB）时 `wake` 仅 0.03s。这是把"数据格式即索引"做到极致——无需 B-tree、无需哈希索引。
2. **Append-only log + 重建式树摘要**：`LOG.txt` 是所有记忆的 append-only 单行记录（永不编辑），`TREE/` 是从 log 派生的摘要缓存——**可随时删除重建**。这是"事实源（log）与派生物（缓存）分离"的经典工程思想。
3. **Merges 一次一个、无后台进程**：摘要合并在 `note` 的输出里逐个到来，由 agent 在正常输出里处理。没有后台 daemon、没有定时任务——降低运维复杂度。
4. **426-token prompt 即全部集成**：installer 打印一段 markdown，贴到 agent 的 `AGENTS.md`/`CLAUDE.md` 顶部即完成。工具 `~/.optmem/memo` 是单个无依赖 Python 3 文件。

## 架构启发
核心启发是**"把记忆从基础设施降维到数据格式"**。传统记忆方案假设"需要数据库/向量库/索引服务"，OptMem 通过定长记录 + append-only log + 可重建缓存，把记忆变成"一个文件 + 一个 prompt"。这种**"可观测的最小化"**（`memo zoom` 把树节点展开成两半、`memo forget` 删坏摘要让下次 nap 重建）让 agent 的记忆行为可审计。对 agent 生成代码的部署（结合 scriptc 的"显式静态度"）也有呼应——都是"让系统的边界可观测、可降级"。

```
~/.optmem/
  memo          单个 Python 3 文件，无依赖
  memory/
    LOG.txt     所有记忆，append-only，永不编辑
    TREE/       摘要缓存，可从 LOG 重建
    config      尺寸配置
```

## 定位判断
在 agent 生态中占据**横向工具层**——不绑定具体 harness/平台，可接入任意 agent（只要有 AGENTS.md/CLAUDE.md）。与 qm（记忆内嵌在平台 per-scope）、cindy（跨会话记忆内嵌）形成对比：OptMem 把记忆**拆出来做独立可插拔单元**。定位为工具型，但若集成模式被验证，有成为 agent 记忆层事实标准的潜力。

## 风险 / 局限 / 泡沫点

1. **并发写边界未验**：append-only log 的单进程设计在多 agent 并发写场景下的一致性未说明；多人/多 agent 场景需额外协调。
2. **长上下文压缩效率待验**：树摘要在极长记忆历史下的压缩质量、召回精度未经规模评测；`recall <regex>` 是精确匹配而非语义检索，对模糊记忆需求支持有限。
3. **单人项目 + license 未声明**：作者虽有声望，但 OptMem 是单人极简实现，license 未声明带来采用不确定性。
4. **无语义检索**：position-is-identity 的代价是查询只能是 regex 精确匹配，不能"语义相近"——这是刻意的 trade-off，但对需要模糊回忆的 agent 场景是局限。

## 与同类项目的关系
- **vs mem0（若存在同类）**：传统记忆框架多用向量库 + 语义检索，OptMem 用 append-only log + regex，定位为"无依赖最小单元"，不追求语义检索能力。
- **vs qm 的 per-scope memory**：qm 把记忆绑定在团队平台里（与 scope/sandbox 绑定），OptMem 做成独立工具——集成度 vs 独立性的取舍。
- **vs Claude Code/Codex 内建记忆**：内建记忆是 harness 私有的，OptMem 跨 harness/跨厂商——模型/厂商切换后仍可用。

## 是否值得持续跟踪
**是，作为"agent 记忆独立成品类"的代表跟踪。** 关注其集成模式（426-token prompt）是否被其他 agent 项目采用、并发写与长上下文压缩的实际边界。

## 后续观察点
1. **license 声明**：若作者补充 LICENSE，采用障碍消除；若长期未声明，可能限制企业采用。
2. **语义检索扩展**：是否在 position-is-identity 基础上补充可选语义层，或坚持纯精确匹配。
3. **多 agent 并发**：是否出现多人团队使用的反馈，append-only log 在并发写下的表现。

---
*首次记录：2026-08-02* · *数据来源: GitHub API (gh CLI) + README 深度阅读*
