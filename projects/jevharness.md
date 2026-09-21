---
title: "TianyuCodings/JevHarness"
slug: jevharness
date_added: "2026-09-22"
last_seen_date: "2026-09-22"
category: "工具型"
emoji: "🧬"
stars: "76 stars"
stars_delta: "1 天 76⭐ ⑂4"
language: "Python"
score: 82
tags: ["jevharness", "jev", "typesafe", "gepa", "harness", "reflection", "frozen-strategy", "pokemon", "claude-code-plugin", "codex", "lossless-dedup", "python"]
url: "https://github.com/TianyuCodings/JevHarness"
---

# TianyuCodings/JevHarness

## 一句话定位
让一个 LLM 写一个任务专属的 Jev harness——freeze 该 harness 后，由 Jev 在 runtime 做 fast fuzzy decisions；可选 GEPA 从完整执行 traces + rewards 改进 harness；Pokemon 例子 5 轮反思 Eval 胜率 25% (3/12) → 75% (9/12) 严肃工程化。

## 它解决的问题
当前 Jev 决策模型在「**任务专属 harness + 演化 + 严肃工程化**」赛道的痛点是「**Jev 只回答 narrow decisions（choice / score / noul）+ 任务需要 feature construction + 任务需要 observations → features → actions 整条链 + 任务需要 runtime 不依赖 LLM per decision + 任务需要 reflection 从 rewards 改进 harness + 任务需要 frozen artifacts 可重现**」——JevHarness 把「**Authoring LLM → Harness（Python + expression code + Jev questions）→ Task action → Environment → Reward → Complete traces → 可选 GEPA reflection 改进 Harness**」做成完整工程化模板 + Pokemon 严肃 example + Claude Code plugin marketplace 一键接入。

## 为什么值得关注（2026-09-22）
- **Stars:** 76（截至 2026-09-22），1 天新增 76⭐，fork 4
- **Forks:** 4（fork/star 5.3%，偏向观察收藏）
- **Open Issues:** N/A（详情未抓取）
- **License:** 无（⚠ 企业 / 商业复用风险点）
- **语言:** Python
- **规模:** 43246 KB（含 Pokemon 资源 + GEPA + Jev harness + 浏览器回放系统代码）
- **活跃度:** created 2026-09-21，pushed 2026-09-21，1 天内快速迭代
- **Topics:** N/A（GitHub topics 未声明）
- **接入:** Claude Code plugin marketplace add + plugin install jev-harness@jevharness + reload-plugins；Codex 接入
- **Pokemon Eval:** 5 轮反思 25% (3/12) → 75% (9/12)

## 热度来源判断
JevHarness 的热度是「**LLM author harness once + GEPA full-trajectory reflection + freeze strategy + runtime Jev fast fuzzy + Pokemon 严肃 example + Claude Code plugin 接入 + 完整 Frozen artifacts + lossless dedup**」的强劲组合。Jev 决策模型从 09-15 ~ 09-21 的「**单点 API + SDK + 资源聚合 + 具身智能 + 可执行技能**」推到 09-22 的「**LLM author task-specific harness + GEPA reflection + Frozen artifacts + 任务适配器 / harness 边界划分**」严肃工程化，是「**Jev + GEPA 从对齐 Jev 到全轨迹反思演化**」的具体兑现。4 个 fork 反映社区观察（fork/star 5.3%）。76⭐ / 1 天是 09-22 当日 GitHub Search created 2026-09-21..2026-09-22 stars>30 全站 trending 第十位左右。热度**真实且具备 Jev + GEPA 严肃演化潜力**——但需警惕：Pokemon 5 轮反思胜率 25% → 75% 的泛化到其他任务的可复现性 + Frozen artifacts 在 hosted model 升级的兼容性 + README 诚实表态边界。

## 关键技术亮点
1. **Authoring LLM 写 Harness:** 可改 code + questions + graph + memory
2. **Freeze selected harness:** 选定 harness 不需 Authoring LLM 在 runtime——reason deeply during development, freeze the strategy, let Jev make fast, fuzzy decisions
3. **Frozen artifacts:** 绑定 PipelineSpec + PipelineRuntime + evaluator + 任务资源
4. **task adapter 边界:** owns observations + legal actions + side effects + scoring
5. **harness 边界:** owns feature construction + Jev judgments + decision logic
6. **composing judgments:** Jev 支持 choice / score / noul + 多问题可一次发 + 独立 graph nodes 可并发
7. **reflection from evidence:** GEPA 从 instance frontier 选 parent + 同一训练 batch 比较 parent 和 proposal + 接受 proposal 完整 Eval + 记录 actual ancestry 含 rejected proposals
8. **keep whole trace:** 每集完整 decisions + observations + node inputs / outputs + Jev questions / answers + memory + failures
9. **lossless deduplication:** 减少 trace 重复
10. **超出 byte cap 归档拒绝不截断:** 严格边界
11. **hosted model alias 不 pinned future provider behavior:** stored responses 和 fresh calls 有不同 reproducibility guarantees
12. **Pokemon 5 轮反思 Eval 胜率 25% (3/12) → 75% (9/12):** 搜索保留 round-3 candidate 作为最佳 harness；Eval 用于选择
13. **性能基线:** 选定 harness 完整决策 568 ms median / P95 657 ms / 113 decisions；初始 harness 完整决策 678 ms median / P95 1495 ms / 238 decisions；选定 harness 单 Jev 请求 269 ms median / P95 348 ms / 226 requests
14. **12 Eval games per harness:** 每个 included Jev call explicitly marked as missing the local response cache
15. **Claude Code plugin marketplace 一键接入:** `/plugin marketplace add https://github.com/TianyuCodings/JevHarness.git` + `/plugin install jev-harness@jevharness` + `/reload-plugins`
16. **Codex 接入:** skill 形态
17. **本地浏览器回放:** node website/build.mjs + preview.mjs --port 8768；battle animations 下载 Pokemon Showdown renderer assets；archived battle log 留在浏览器不上传 replay server

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Claude Code / Codex plugin + Authoring LLM + Harness（Python + Jev questions） + Task adapter + Environment + Frozen artifacts；边界为 task adapter / harness 划分 + Frozen artifacts 绑定 | 仅基于档案描述的 task adapter / harness 边界 + Frozen artifacts + Claude Code plugin 接入；具体 plugin 权限范围、Codex 接入细节、跨平台兼容性未在档案中给出 |
| 主路径 | Task contract + examples → Authoring LLM 写 Harness → Harness（Python + expression code + Jev questions） → Observation → Task action → Environment → Reward → Complete traces → 可选 GEPA reflection 改进 Harness | 主路径为档案语义抽象；具体 Authoring LLM 调用方式（哪个 LLM）、Jev endpoint 选型、GEPA instance frontier 实现细节未在档案中给出 |
| 关键权衡 | LLM author harness 一次性投资 vs 长期 Jev fast fuzzy decisions vs GEPA full-trajectory reflection 改进 vs Frozen artifacts 可重现 vs task adapter / harness 边界清晰度 vs README 诚实表态边界 vs ⚠ 无 license | 档案明示 8 项限制（Frozen artifacts 仍需 Jev / hosted model alias 不 pinned / stored responses 和 fresh calls 不同 guarantees / 等等）；具体企业部署态度、付费策略未证实 |
| 最小 PoC | 单 Claude Code 安装 plugin marketplace → `/jev-harness:jev-harness Build a harness that routes support tickets to the right team` → 跑 Pokemon example → 验证 568 ms median 完整决策 → 5 轮 GEPA reflection → 验证 Frozen artifacts | PoC 范围、退出路径由档案「Claude Code plugin + Pokemon example + 5 轮反思」建议推导；具体 Authoring LLM 选型、Jev endpoint 配置、Plugin marketplace 维护策略待核验 |

## 架构启发
JevHarness 的核心启发是「**Reason deeply during development. Freeze the strategy. Let Jev make fast, fuzzy decisions.**」——这是「**开发期深度推理 + runtime 快速决策**」分层的工程化形式。传统做法是 LLM per decision 既要快又要准，但 JevHarness 反向走「**Authoring LLM 一次性写 harness + freeze 后 runtime 只跑 harness + Jev 做 narrow decisions**」路线——是「**慢开发 vs 快 runtime**」的工程化对比。**更深层的启发是：task adapter 边界 owns observations + legal actions + side effects + scoring，harness 边界 owns feature construction + Jev judgments + decision logic**——这种「**边界划分**」让 harness 可独立修改而不让它重写自己的 reward 或读隐藏任务状态，是「**安全 + 可审计**」的工程化形式。**GEPA from instance frontier + 同一训练 batch 比较 parent / proposal + 接受 proposal 完整 Eval + 记录 actual ancestry 含 rejected proposals**——是「**严肃演化算法**」的工程化形式。**lossless dedup + 超出 byte cap 归档拒绝不截断**——是「**严格边界**」的工程化形式。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  Task[Task contract + examples] --> Author[Authoring LLM<br/>reason deeply during development]
  Author --> Harness[Harness<br/>Python + expression code<br/>+ Jev questions]
  Harness --> Adapter[task adapter<br/>observations + legal actions<br/>+ side effects + scoring]
  Adapter --> Obs[Allowed task observation]
  Obs --> Harness
  Harness --> Jev[Jev<br/>choice / score / noul<br/>~269 ms median]
  Harness --> Action[Task action]
  Action --> Env[Trusted environment + reward]
  Env --> Traces[Complete execution traces<br/>decisions + observations<br/>+ node inputs / outputs<br/>+ Jev Q/A + memory + failures]
  Traces -.可选 reflection.-> Author
  Traces --> GEPA[GEPA reflection<br/>instance frontier 选 parent<br/>同训练 batch 比较<br/>接受 proposal 完整 Eval]
  GEPA --> Author
  Harness --> Freeze[Frozen artifacts<br/>PipelineSpec + PipelineRuntime<br/>+ evaluator + 任务资源]
  Freeze -.仍需 Jev if Jev nodes.-> Jev
  Harness -.hosted model alias 不 pinned future provider.-> Note1[stored responses vs fresh calls<br/>不同 reproducibility guarantees]
  Traces --> Dedup[Lossless deduplication<br/>超出 byte cap 归档拒绝不截断]
  Harness -.Claude Code plugin marketplace 一键接入.-> Plugin[/plugin marketplace add<br/>/plugin install jev-harness@jevharness<br/>/reload-plugins]
```

## 定位判断
**工具型项目（Jev + LLM author harness + GEPA reflection + Frozen artifacts）。** JevHarness 不仅是 Pokemon 模板，更试图成为「**Jev 决策模型 + 任务专属 harness + 严肃演化 + 可重现**」的工程化框架——通过 Authoring LLM 写 Harness + Freeze selected harness + task adapter / harness 边界划分 + GEPA from evidence + keep whole trace + lossless dedup + 拒绝截断 + Pokemon 严肃 example + Claude Code plugin marketplace 一键接入，把「**Jev + 任务专属 harness + 严肃工程化**」做到极致。76⭐ + 4 fork 已显示社区初步关注。但「**框架化**」取决于一个关键问题：Pokemon 5 轮反思胜率 25% → 75% 的泛化到其他任务的可复现性 + GEPA 在 instance frontier + parent / proposal 完整 Eval 的稳定性 + task adapter / harness 边界划分的清晰度。目前定位是「**最有影响力的 Jev + LLM author harness + GEPA 严肃工程化**」，向多任务 + 多 LLM + 企业部署是合理路径。

## 风险 / 局限 / 泡沫点
- **Pokemon 5 轮反思胜率 25% → 75% 的泛化性:** README 明示「The reported improvement is an example result on the selection Eval set, not an independent estimate of performance on unseen games」，未给其他任务泛化数据
- **GEPA 在 instance frontier + parent / proposal 完整 Eval 的稳定性:** 评估成本高，复杂度随 instance frontier 指数增长
- **task adapter / harness 边界划分的清晰度:** 实际项目中边界可能模糊，需要开发者自律
- **lossless dedup 在长 trace 的稳定性:** 长 trace 的 dedup 性能未给具体数据
- **Frozen artifacts 在 hosted model 升级的兼容性:** README 明示「hosted model alias does not pin future provider behavior」，stored responses 和 fresh calls 有不同 reproducibility guarantees
- **⚠ 无 license:** 企业 / 商业复用风险点
- **Authoring LLM 依赖:** 需要一个能写 harness 的 LLM，可能成本较高
- **Jev API 依赖:** 需要 Jev API key，模型不可用或额度耗尽会直接断链
- **Pokemon 资源依赖:** 浏览器回放需要下载 Pokemon Showdown renderer assets
- **个人项目属性:** TianyuCodings 个人维护，4 forks 但核心治理仍集中

## 与同类项目的关系
- **vs 官方 TypeSafe Jev endpoint:** 官方 Jev 是 closed hosted service + 通用 decision API；JevHarness 是 LLM author harness + GEPA reflection + Frozen artifacts + Pokemon 严肃 example
- **vs thruwire/foreman:** thruwire/foreman 是「**Jev supervisor 双 loop + Python policy 5 类动作 + FactoryConfig**」；JevHarness 是「**LLM author harness + GEPA reflection + Frozen artifacts + task adapter / harness 边界**」——两者都用 Jev 但走不同工程化路径：foreman 是 runtime supervisor，JevHarness 是 task-specific harness
- **vs sutro-sh/jev-align:** sutro-sh/jev-align 是「**GEPA 对齐 Jev**」；JevHarness 是「**LLM author harness + GEPA from instance frontier + 完整 Eval + Pokemon 5 轮反思胜率 25% → 75%**」——jev-align 是对齐 Jev 模型本身，JevHarness 是对齐 harness（而非 Jev）
- **vs ekzhang/openjev-sglang:** openjev-sglang 是「**Jev-compatible API endpoint 基于开源模型 prefill-only**」；JevHarness 是「**Jev + LLM author harness + GEPA reflection + Frozen artifacts**」——openjev-sglang 是基础设施，JevHarness 是应用工程化
- **vs Pokemon Showdown / Pokemon battle simulators:** Pokemon Showdown 是 battle simulator；JevHarness 是 harness + reflection + browser replay 系统

## 是否值得持续跟踪
**值得跟踪（Jev + LLM author harness + GEPA reflection + Frozen artifacts 候选）。** JevHarness 代表了「**Jev 决策模型 + 任务专属 harness + 严肃演化 + 可重现**」的演化方向，无论其本身成败，这一方向是行业趋势。建议关注：Pokemon 5 轮反思胜率泛化性、GEPA 在多任务的稳定性、task adapter / harness 边界在多任务的清晰度、Authoring LLM 选型、Frozen artifacts 在 hosted model 升级的兼容性。对 Jev 决策模型应用开发者，这是「**Jev + 任务专属 harness + GEPA 严肃工程化**」的具体样本，值得直接采用。对 AI 决策模型生态观察者，它是「**慢开发 + 快 runtime + 严肃演化**」的头部样本。

## 后续观察点
- Pokemon 5 轮反思胜率 25% → 75% 在其他任务（route support tickets / 决策博弈 / 自动交易）的泛化（决定框架可用性）
- GEPA 在 instance frontier + parent / proposal 完整 Eval 的稳定性（决定 GEPA 严肃性）
- task adapter / harness 边界在多任务项目的清晰度（决定可维护性）
- Authoring LLM 选型（决定开发成本）
- Frozen artifacts 在 hosted model 升级的兼容性（决定可重现性）
- ⚠ 许可决策（无 license 是企业 / 商业复用风险点）
- 多 LLM 接入（除 OpenAI / Anthropic / Codex 外是否支持其他 LLM）
- 是否演化为独立平台 / 商店（从 GitHub 仓库升级为 harness marketplace）

---
> 数据来源: GitHub API (2026-09-22) | Stars: 76 | Forks: 4 | License: 无 (⚠ 风险点) | 语言: Python | 创建: 2026-09-21 | Pokemon Eval: 25% → 75% (5 轮反思)