---
title: "deepopen-com/deepopen"
slug: deepopen
date_added: "2026-09-23"
last_seen_date: "2026-09-23"
category: "工具型"
emoji: "🐉"
stars: "206 stars"
stars_delta: "2 天 206⭐ ⑂1"
language: "Python"
score: 78
tags: ["deepopen", "system-1", "decision-engine", "non-autoregressive", "laya", "modernbert-large", "mmbert-base", "apache-2-0", "pypi", "router-preload", "clinc150", "banking77", "multilingual-1024", "eighths-jev-speed", "32ms-inference", "rlcd", "ece-0-081"]
url: "https://github.com/deepopen-com/deepopen"
---

# deepopen-com/deepopen

## 一句话定位
基于 laya 改进的完全开源非自回归 System 1 决策引擎，专为结构化类型决策场景设计——三检查点（ModernBERT-large 421M 英文 + mmBERT-base 322M 多语言 + ModernBERT-large 421M 类型决策）+ 纯 Python 语言检测路由 + RLCD 强化学习训练 + 严格校准 ECE 0.081；T4 显卡实测 32.8 ms 单请求 / 72.3 ms 10 题批量 / 103-332 问题/秒 / 7.8 倍 Jev 速度；2000 样本基准 0.766 准确率超 Jev 1.13.0 的 0.727 + Brier 0.062；Apache-2.0 完全开源权重 + pip install deepopen + Router preload；CLINC150 / Banking77 榜单第 2 / 第 5。

## 它解决的问题
当前决策模型在「非自回归 + 开源权重 + 多语言 + 严格校准 + 智能路由 + 高并发」赛道的痛点是「Jev 是 closed hosted service + Laya 已开源但部署复杂 + 用户希望完全开源权重 + 用户希望多语言（特别是非拉丁语种）+ 用户希望严格校准概率输出 + 用户希望智能路由避免高置信度错误 + 用户希望极致性能（毫秒级 + 高并发）+ 用户希望 Apache-2.0 商用可修改 + 用户希望 pip install 一键部署 + 用户希望对标 Jev / Laya 的基准成绩」——DeepOpen 用「Laya 改进 + 三检查点（英文 / 多语言 / 类型决策）+ 纯 Python 智能路由 + ModernBERT-large / mmBERT-base + 32.8 ms / 7.8× Jev 速度 + Apache-2.0 完全开源权重 + pip install deepopen + Router preload + ECE 0.081 + 2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062 + 100+ 语言 + 1024 上下文 + 高棉语 0 → 0.451」是「非自回归 System 1 决策引擎 + 三检查点 + Laya 改进 + 智能路由 + Apache-2.0」的具体路径。

## 为什么值得关注（2026-09-23）
- **Stars:** 206（截至 2026-09-23），2 天新增 206⭐，fork 1，fork/star 0.5% 极低反映观察收藏而非企业 fork
- **Forks:** 1（观察收藏）
- **Open Issues:** 6
- **Watchers/Subscribers:** 206
- **License:** Apache-2.0（明确许可可商用可修改）
- **语言:** Python
- **规模:** 2.65 MB（含三检查点 + Laya 改进 + Router preload + Apache-2.0 完全开源权重 + CLINC150 / Banking77 榜单）
- **活跃度:** created 2026-09-21，pushed 2026-09-22，2 天内快速迭代
- **Topics:** N/A（GitHub topics 未声明）
- **安装:** pip install deepopen
- **核心路由:** Router preload + device="cuda" + preload(["english", "multilingual"]) + max_loaded=2 + unload()
- **核心架构:** 三检查点 + 纯 Python 语言检测路由 + RLCD 强化学习 + Apache-2.0 完全开源权重

## 热度来源判断
DeepOpen 的热度是「**Laya 改进 + 三检查点（ModernBERT-large 421M 英文 / mmBERT-base 322M 多语言 / ModernBERT-large 421M 类型决策）+ 纯 Python 语言检测路由 + RLCD 强化学习 + 严格校准 ECE 0.081 + T4 32.8 ms / 10 批 72.3 ms / 单卡 103-332 问题/秒 / 7.8× Jev 速度 + Apache-2.0 完全开源权重 + pip install deepopen + Router preload + 2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062 + 100+ 语言 + 1024 上下文 + 高棉语 0 → 0.451 + CLINC150 / Banking77 榜单第 2 / 第 5**」的强劲组合。Jev / Laya 决策模型从 09-15 的「API + SDK + 资源聚合」+ 09-22 的「Heman10x-NGU/openJev-verdict-2.0 Non-Autoregressive Decision Engine 击败 Jev & Laya」+「Rizzo-AI-Academy/rizzo-flow Spark-X2.5 4B Jev 兼容 0 generated tokens」+ 09-23 的「DeepOpen Laya 改进 + 三检查点 + 智能路由 + 32.8 ms + 7.8× Jev 速度 + Apache-2.0 + pip install」是「Jev / Laya 决策模型挑战者 + 开源权重 + 非自回归 + Apache-2.0」的具体路径。fork/star 0.5% 极低反映「Apache-2.0 + 三检查点 + Laya 改进 + 32.8 ms + 7.8× Jev」偏向观察收藏而非企业 fork（1 个 fork 几乎全部是「准备做决策模型本地化 / 多语言路由」研究者 fork）。热度**真实且具备 Apache-2.0 完全开源 + pip install + 多语言 + 严格校准的演化潜力**——但需警惕：三检查点在多任务的稳定性 + ModernBERT-large 在英文 / 类型决策的准确率 + mmBERT-base 在多语言的覆盖广度 + 智能路由在 <0.5 ms 识别脚本 / 语言的稳定性 + RLCD 强化学习在 hosted model 升级的兼容性 + 严格校准 ECE 0.081 在多任务的稳定性 + 32.8 ms / 10 批 72.3 ms 在多 GPU 的扩展。

## 关键技术亮点
1. **三检查点架构：** 英文检查点（ModernBERT-large 421M 参数训练，支持 512 上下文窗口，在英文单语种任务中实现 39.5 ms 单请求延迟，在英文意图分类 / XNLI 等基准测试中准确率达到 0.783-0.860）+ 多语言检查点（mmBERT-base 322M 参数训练，支持 1024 上下文窗口，推理速度比英文模型快 2 倍，覆盖 100+ 种语言，其中 45 种语言的准确率超过 3 倍随机基线，在非拉丁语种下性能远超纯英文模型，13 种非英文语言的意图分类准确率达到 0.451，是英文检查点的 1.47 倍）+ 类型决策检查点（ModernBERT-large 421M 参数训练，支持 1024 上下文窗口，专门针对结构化类型决策场景微调，在 2000 个决策样本的基准测试中，准确率达到 0.766，超过 TypeSafe Jev 1.13.0 的 0.727，同时 Brier 分数低至 0.062）
2. **核心技术特性：** 零幻觉非自回归设计（全程不生成任何文本内容，所有输出均为开发者预先定义的结构化类型结果，无需后续解析处理，从根源上杜绝了传统大模型的幻觉问题，输出结果 100% 符合预设的类型边界）+ 全链路智能路由机制（在模型前向推理前，通过纯 Python 实现的语言检测模块，在 <0.5 ms 内识别输入内容的脚本类型和所属语言，自动匹配最优检查点，彻底避免了英文模型在非拉丁语种下「高置信度错误」的致命问题——此前纯英文检查点在高棉语任务中准确率为 0，却给出 95.2% 的错误置信度，仅靠置信度阈值完全无法规避风险）+ 严格校准的概率输出（依托 RLCD 强化学习框架训练，所有输出的置信度分数具备严格的统计意义，经过域温度校准后，ECE（预期校准误差）低至 0.081，远优于同类方案，可直接用于生产环境的自动置信门控流程，高置信度请求直接自动处理，低置信度请求自动流转人工审核）+ 极致的性能表现（在特斯拉 T4 显卡上实测，单请求推理仅需 32.8 ms，10 题批量处理仅 72.3 ms，单 T4 显卡最高支持每秒 103-332 个问题的吞吐量，实测速度是 TypeSafe Jev 的 7.8 倍）+ 完全开源零成本部署（采用 Apache 2.0 开源许可，所有权重完全开放，支持本地自托管，无需调用任何付费 API，不存在按 Token 计费的额外成本，对比 TypeSafe Jev 每百万 Token 0.042 美元的定价，长期大规模部署可节省近 100% 的推理成本）
3. **快速上手部署：** pip install deepopen → Router(preload=True, device="cuda") → 定义自定义类型决策规则 → router.predict(state, questions) → 自动路由到最优模型完成推理 → res_en["answers"]["department"]["choice"] + res_en["routing"]["model"]
4. **生产环境部署优化：** router.preload(["english", "multilingual"]) 节省显存 + max_loaded=2 LRU 缓存 + router.unload() 手动卸载
5. **内置生产级工作流程预设：** 智能模型路由（自动判断用户请求的复杂度，将简单任务路由到小模型、复杂任务路由到大模型）+ 意图分类 + 风险识别 + 多语言路由
6. **关键差异（多语言路由的硬动机）：** 纯英文检查点在高棉语任务中准确率为 0，却给出 95.2% 的错误置信度，仅靠置信度阈值完全无法规避风险
7. **榜单成绩：** CLINC150 第 2 位 / Banking77 第 5 位（对照参考成绩）
8. **Apache-2.0 完全开源权重：** 长期大规模部署可节省近 100% 推理成本

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 非自回归 System 1 决策引擎（PyPI 包），边界为三检查点 + 纯 Python 智能路由 + RLCD 强化学习 + 严格校准 ECE 0.081 + Apache-2.0 完全开源权重 | 仅基于档案描述的三检查点 + 智能路由 + RLCD + ECE 0.081 + Apache-2.0；具体三检查点在多任务的稳定性、ModernBERT-large 在英文 / 类型决策的准确率、mmBERT-base 在多语言的覆盖广度均为档案描述 |
| 主路径 | Router(preload=True) → 纯 Python 语言检测（<0.5 ms）→ 自动匹配最优检查点（英文 / 多语言 / 类型决策）→ 推理（单请求 32.8 ms / 10 批 72.3 ms）→ 严格校准 ECE 0.081 输出 → 类型决策结果（boolean / choice / score / noul 等） | 主路径为档案语义抽象；三检查点在多任务的稳定性、ModernBERT-large 在英文 / 类型决策的准确率、mmBERT-base 在多语言的覆盖广度、智能路由在 <0.5 ms 识别脚本 / 语言的稳定性、RLCD 强化学习在 hosted model 升级的兼容性、严格校准 ECE 0.081 在多任务的稳定性、32.8 ms / 10 批 72.3 ms 在多 GPU 的扩展均待核验 |
| 关键权衡 | 非自回归价值 vs 三检查点稳定性 vs ModernBERT-large 准确率 vs mmBERT-base 多语言覆盖 vs 智能路由稳定性 vs RLCD 强化学习兼容性 vs 严格校准 ECE 0.081 稳定性 vs 32.8 ms 性能 vs Apache-2.0 商用兼容性 vs CLINC150 / Banking77 榜单成绩 vs 高棉语 0 → 0.451 多语言路由验证 vs pip install deepopen 一键部署可用度 | 档案明示三检查点 + 智能路由 + RLCD + ECE 0.081 + Apache-2.0 + CLINC150 / Banking77 榜单第 2 / 第 5 + 高棉语 0 → 0.451；具体稳定性、准确率、多语言覆盖、兼容性、严肃 benchmark 验证、多 GPU 扩展均为档案描述 |
| 最小 PoC | Python 3.10+ + CUDA → pip install deepopen → Router(preload=True, device="cuda") → 测试英文检查点（39.5 ms + 0.783-0.860 准确率）→ 测试多语言检查点（mmBERT-base + 100+ 语言 + 45 种 > 3× 随机基线 + 13 种非英文 0.451 准确率 + 高棉语 0 → 0.451）→ 测试类型决策检查点（1024 ctx + 2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062）→ 测试智能路由（<0.5 ms 识别脚本 / 语言 + 自动匹配最优检查点）→ 测试严格校准（ECE 0.081）→ 测试 Apache-2.0 商用兼容性 + 修改权重 + 自托管部署 → 跑 CLINC150 / Banking77 榜单验证 | PoC 范围、退出路径由档案「pip install + Router preload + 三检查点 + 智能路由 + RLCD + ECE 0.081 + Apache-2.0 + CLINC150 / Banking77」建议推导；具体稳定性、准确率、多语言覆盖、兼容性、严肃 benchmark 验证、多 GPU 扩展、付费与商业条款均待核验 |

## 架构启发
DeepOpen 的核心启发是「**非自回归 System 1 决策引擎 + Laya 改进 + 三检查点（ModernBERT-large 421M × 2 + mmBERT-base 322M）+ 纯 Python 语言检测路由 + RLCD 强化学习训练 + 严格校准 ECE 0.081 + T4 32.8 ms / 10 批 72.3 ms / 单卡 103-332 问题/秒 / 7.8× Jev 速度 + Apache-2.0 完全开源权重 + pip install deepopen + Router preload + 2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062 + 100+ 语言 + 1024 上下文 + 高棉语 0 → 0.451 + CLINC150 / Banking77 榜单第 2 / 第 5**」。当前大部分决策模型走「closed hosted service + 单语言 + 无严格校准 + 无智能路由 + 无 Apache-2.0 + 无 pip install + 无 Laya 改进」路线，但 DeepOpen 反向走「**非自回归 + Laya 改进 + 三检查点 + 纯 Python 智能路由 + RLCD 强化学习 + 严格校准 ECE 0.081 + 极致性能 + Apache-2.0 完全开源 + pip install 一键部署 + 严肃 benchmark 验证**」路线——是「**非自回归 vs 自回归 + Laya 改进 vs 单模型 + 三检查点 vs 单模型 + 智能路由 vs 单语言 + 严格校准 vs 无校准 + Apache-2.0 vs closed + pip install vs 复杂部署 + 严肃 benchmark vs 无 benchmark**」的工程化对比。**更深层的启发是：三检查点架构 + 纯 Python 智能路由是「非自回归 System 1 决策引擎」的具体路径——把英文 / 多语言 / 类型决策三个任务分离成三个独立优化的检查点，通过纯 Python 语言检测路由在 <0.5 ms 内自动匹配，避免了「单一模型在多语言上高置信度错误」的致命问题**——这是「**任务分离 + 智能路由 + 严格校准**」的工程化形式。**RLCD 强化学习训练 + 严格校准 ECE 0.081 + 32.8 ms + 7.8× Jev 速度**——是把「严格统计意义的置信度 + 极致性能 + 高并发」三个具体工程问题严肃化的具体路径。**Apache-2.0 完全开源权重 + pip install deepopen + Router preload**——是「**完全开源 + 一键部署 + 显存优化**」的具体路径。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Input[用户输入<br/>state + questions] --> LangDetect[纯 Python 语言检测<br/><0.5 ms 识别脚本 / 语言]
  LangDetect --> Router[Router 智能路由<br/>preload + max_loaded=2 + unload]
  Router --> Checkpoint1[英文检查点<br/>ModernBERT-large 421M<br/>512 ctx + 39.5 ms<br/>0.783-0.860 准确率]
  Router --> Checkpoint2[多语言检查点<br/>mmBERT-base 322M<br/>1024 ctx + 英文 2 倍速度<br/>100+ 语言 + 45 种 > 3× 随机基线<br/>13 种非英文 0.451 准确率<br/>高棉语 0 → 0.451]
  Router --> Checkpoint3[类型决策检查点<br/>ModernBERT-large 421M<br/>1024 ctx + 2000 样本<br/>0.766 准确率超 Jev 0.727<br/>Brier 0.062]
  Checkpoint1 --> RLCD[RLCD 强化学习训练]
  Checkpoint2 --> RLCD
  Checkpoint3 --> RLCD
  RLCD --> Calibrate[严格校准 ECE 0.081<br/>域温度校准]
  Calibrate --> Output[类型决策结果<br/>boolean / choice / score / noul]
  Output --> Production[生产环境<br/>高置信度直接处理<br/>低置信度人工审核]
  Router -.设备.-> CUDA[NVIDIA CUDA / Apple MPS / CPU]
  Router -.显存优化.-> Mem[preload + max_loaded=2 + unload]
  Calibrate -.Apache-2.0.-> OpenSource[完全开源权重<br/>本地自托管<br/>pip install deepopen<br/>零成本部署]
  LangDetect -.待核验.-> Risk[三检查点稳定性<br/>ModernBERT-large 准确率<br/>mmBERT-base 多语言覆盖<br/>智能路由 <0.5 ms 稳定性<br/>RLCD hosted model 兼容性<br/>ECE 0.081 严格校准稳定性<br/>32.8 ms 多 GPU 扩展]
```

## 定位判断
**平台候选型项目（非自回归 System 1 决策引擎 + Apache-2.0 完全开源）。** DeepOpen 不只是 Laya 的简单升级版，而是「Laya 改进 + 三检查点（ModernBERT-large 421M × 2 + mmBERT-base 322M）+ 纯 Python 智能路由 + RLCD 强化学习 + 严格校准 ECE 0.081 + T4 32.8 ms / 10 批 72.3 ms / 单卡 103-332 问题/秒 / 7.8× Jev 速度 + Apache-2.0 完全开源权重 + pip install deepopen + Router preload + 2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062 + 100+ 语言 + 1024 上下文 + 高棉语 0 → 0.451 + CLINC150 / Banking77 榜单第 2 / 第 5」的具体工程化形态——类似 Hugging Face Transformers 之于预训练模型 / spaCy 之于 NLP 任务。206⭐ / 2 天 / fork 1 / fork/star 0.5% 反映观察收藏而非企业 fork。但「**平台化**」取决于一个关键问题：三检查点在多任务的稳定性 + ModernBERT-large 在英文 / 类型决策的准确率 + mmBERT-base 在多语言的覆盖广度 + 智能路由在 <0.5 ms 识别脚本 / 语言的稳定性 + RLCD 强化学习在 hosted model 升级的兼容性 + 严格校准 ECE 0.081 在多任务的稳定性 + 32.8 ms / 10 批 72.3 ms 在多 GPU 的扩展 + Apache-2.0 在企业的商用兼容性 + CLINC150 / Banking77 榜单成绩的严肃 benchmark 验证 + 高棉语 0 → 0.451 多语言路由的硬动机验证 + pip install deepopen 一键部署的实际可用度。目前定位是「**最有影响力的 Apache-2.0 非自回归 System 1 决策引擎**」，向平台演进是合理路径。

## 风险 / 局限 / 泡沫点
- **三检查点多任务稳定性：** 英文 / 多语言 / 类型决策三个独立优化的检查点同时加载时的稳定性
- **ModernBERT-large 英文 / 类型决策准确率：** 0.783-0.860 在 XNLI / 0.766 在 2000 样本 vs Jev 0.727
- **mmBERT-base 多语言覆盖广度：** 100+ 语言 + 45 种 > 3× 随机基线 + 13 种非英文 0.451 准确率
- **智能路由 <0.5 ms 识别脚本 / 语言稳定性：** 纯 Python 实现 vs C++ 实现
- **RLCD 强化学习 hosted model 升级兼容性：** 版本化 + 兼容性 + 迁移
- **严格校准 ECE 0.081 多任务稳定性：** 域温度校准在不同任务上的迁移
- **32.8 ms / 10 批 72.3 ms 多 GPU 扩展：** 单 T4 显卡 103-332 问题/秒 vs 多卡 / Apple Silicon / CPU 扩展
- **Apache-2.0 企业商用兼容性：** 权重可商用可修改 + 本地自托管 + 零成本 vs Jev 每百万 Token 0.042 美元节省近 100%
- **CLINC150 / Banking77 榜单成绩严肃 benchmark 验证：** 第 2 / 第 5 位的可复现性
- **高棉语 0 → 0.451 多语言路由硬动机验证：** 纯英文检查点在高棉语 0 准确率 + 95.2% 错误置信度的修复
- **pip install deepopen 一键部署实际可用度：** 模型下载 + 预加载 + 多设备
- **企业部署态度：** 严肃企业是否允许 Apache-2.0 + 自托管
- **付费策略：** Apache-2.0 但商业支持 / SLA 未明
- **个人项目属性：** deepopen-com 单一组织维护，可持续性存疑

## 与同类项目的关系
- **vs TypeSafe AI Jev（closed hosted service）：** 同构「System 1 决策模型」但 DeepOpen 是「Apache-2.0 完全开源权重 + pip install + 本地自托管 + 零成本」+ Jev 是「closed hosted service + 每百万 Token 0.042 美元」
- **vs Laya（开源 encoder）：** DeepOpen 是「Laya 改进 + 三检查点 + 智能路由 + RLCD + ECE 0.081 + 32.8 ms + Apache-2.0 + pip install」+ Laya 是「开源 encoder + 单模型」
- **vs Heman10x-NGU/openJev-verdict-2.0（昨日）：** 同构「Non-Autoregressive Decision Engine 击败 Jev & Laya」但 DeepOpen 是「三检查点 + Laya 改进 + 智能路由 + 32.8 ms + Apache-2.0 + pip install + ECE 0.081 + CLINC150 / Banking77」+ openJev-verdict-2.0 是「Non-Autoregressive Decision Engine 击败 Jev & Laya」
- **vs Rizzo-AI-Academy/rizzo-flow（昨日）：** 同构「Jev 兼容 API 本地实现」但 DeepOpen 是「Apache-2.0 + Laya 改进 + 三检查点 + 智能路由 + 32.8 ms + pip install + ECE 0.081 + 100+ 语言」+ rizzo-flow 是「Spark-X2.5 4B Apache-2.0 + Jev 兼容 API + KV cache 克隆 + 0 generated tokens + 1M native context」
- **vs ModernBERT / mmBERT（基础模型）：** DeepOpen 是「在 ModernBERT-large / mmBERT-base 上 RLCD 微调 + 三检查点 + 智能路由 + 严格校准 + Apache-2.0 + pip install」+ ModernBERT / mmBERT 是「基础预训练模型」
- **vs Hugging Face Transformers：** DeepOpen 是「非自回归 System 1 决策引擎 + 三检查点 + 智能路由 + Apache-2.0 + pip install」+ Transformers 是「通用预训练模型库」

## 是否值得持续跟踪
**值得跟踪（Apache-2.0 非自回归 System 1 决策引擎 + pip install + 三检查点 + 智能路由）。** DeepOpen 代表了「Apache-2.0 完全开源 + pip install 一键部署 + Laya 改进 + 三检查点 + 智能路由 + 严格校准 ECE 0.081 + 极致性能 + 多语言 + 严肃 benchmark 验证」的方向，无论其本身成败，这一方向是行业趋势。建议关注：三检查点在多任务的稳定性 + ModernBERT-large 在英文 / 类型决策的准确率 + mmBERT-base 在多语言的覆盖广度 + 智能路由在 <0.5 ms 识别脚本 / 语言的稳定性 + RLCD 强化学习在 hosted model 升级的兼容性 + 严格校准 ECE 0.081 在多任务的稳定性 + 32.8 ms / 10 批 72.3 ms 在多 GPU 的扩展 + Apache-2.0 在企业的商用兼容性 + CLINC150 / Banking77 榜单成绩的严肃 benchmark 验证 + 高棉语 0 → 0.451 多语言路由的硬动机验证 + pip install deepopen 一键部署的实际可用度。对决策模型研究者，这个仓库是「Apache-2.0 + Laya 改进 + 三检查点 + 智能路由 + RLCD + ECE 0.081 + 32.8 ms + 7.8× Jev」的严肃工程化来源，值得直接采用。对 Jev / Laya 决策模型生态观察者，它是「Apache-2.0 完全开源 + pip install + pip install + 三检查点 + 多语言 + 严肃 benchmark」的头部样本。

## 后续观察点
- 三检查点（英文 / 多语言 / 类型决策）在多任务的稳定性
- ModernBERT-large 421M 在英文（0.783-0.860 准确率）+ 类型决策（2000 样本 0.766 准确率超 Jev 0.727 + Brier 0.062）的准确率
- mmBERT-base 322M 在多语言（100+ 语言 + 45 种 > 3× 随机基线 + 13 种非英文 0.451 准确率 + 高棉语 0 → 0.451）的覆盖广度
- 智能路由在 <0.5 ms 识别脚本 / 语言的稳定性 + 纯 Python 实现 vs C++ 实现
- RLCD 强化学习在 hosted model 升级的兼容性 + 版本化 + 迁移
- 严格校准 ECE 0.081 在多任务的稳定性 + 域温度校准在不同任务上的迁移
- 32.8 ms / 10 批 72.3 ms 在多 GPU / Apple Silicon / CPU 的扩展
- Apache-2.0 在企业的商用兼容性 + 权重可商用可修改 + 本地自托管 + 零成本 vs Jev 每百万 Token 0.042 美元节省近 100%
- CLINC150 / Banking77 榜单第 2 / 第 5 位的可复现性 + 严肃 benchmark 验证
- 高棉语 0 → 0.451 多语言路由的硬动机验证
- pip install deepopen 一键部署的实际可用度 + 模型下载 + 预加载 + 多设备
- router.preload(["english", "multilingual"]) + max_loaded=2 + router.unload() 在生产环境的实际效果
- 内置生产级工作流程预设（智能模型路由 + 意图分类 + 风险识别 + 多语言路由）的实际可用度
- 企业部署态度 + 合规边界 + 付费策略 + 商业支持 / SLA
- 单一组织（deepopen-com）维护的可持续性

---
> 数据来源: GitHub API (2026-09-23) | Stars: 206 | Forks: 1 | License: Apache-2.0 | 语言: Python | 创建: 2026-09-21 | 安装: pip install deepopen | 核心: 三检查点 + 纯 Python 智能路由 + RLCD + ECE 0.081 + 32.8 ms / 7.8× Jev
