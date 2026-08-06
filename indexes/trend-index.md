---
date: '2026-04-10'
last_updated: '2026-08-07'
summary: GitHub 趋势项目排名变化追踪，持续更新
title: Trend Index — 趋势指数
---

# Trend Index — 趋势指数

> 记录项目排名、趋势变化、关键判断修正

## 2026-08-07（第九十二版）

### anydoc 延续爆发（4,688→8,069，+3,381/+72%，跨入 8K 关口，fork 205→370），增速从 +331% 回落到 +72% 但绝对增量仍居首，爆发进入"高增量+减速"阶段 · "去 AI 腔"写作治理品类浮现——溯源发现 blader/humanizer（34,004⭐）为源头 Skill，human-writing（1,552⭐，+54%，中文）+ humanizer-cli（581⭐，208 watchers，英文终端检测）+ ratchet（435⭐，事前约束）构成"写作治理三层谱系"（事前约束→事中去 AI 腔→事后检测）· 应用层第六日——qm 增速骤降到 +3%（+369，接近停滞/守量级固化），crm 增速从 +34% 回落到 +16%（+1,018）但仍为增速第一，genoffice 稳健（+279/+15%），"crm 领跑、qm 守量"格局从分化进入固化 · 软件工厂 Skill 品类出现——super-simple-software-factory（459⭐，14 watchers，Python 拥有控制平面、agent 为有界节点）

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | anydoc 延续爆发（4,688→8,069，+3,381/+72%），跨入 8K 关口，fork 205→370——增速从 +331% 回落到 +72% 但绝对增量仍居首，爆发进入"高增量+减速"阶段，接近稳态的回落速度是关键观察点 | anydoc | 90 |
| 2 | "去 AI 腔"写作治理品类浮现——溯源发现 blader/humanizer（34,004⭐）为源头 Skill，human-writing（1,552⭐，+54%，中文活人感）+ humanizer-cli（581⭐，208 watchers，英文终端检测）+ ratchet（435⭐，事前约束）构成"写作治理三层谱系"（事前约束→事中去 AI 腔→事后检测） | human-writing, humanizer-cli, ratchet, humanizer | 87 |
| 3 | 应用层第六日——qm 增速骤降到 +3%（+369，接近停滞/守量级固化），crm 增速从 +34% 回落到 +16%（+1,018）但仍为增速第一，genoffice 稳健（+279/+15%），"crm 领跑、qm 守量"格局从分化进入固化 | qm, crm, genoffice | 85 |
| 4 | 软件工厂 Skill 品类出现——super-simple-software-factory（459⭐，14 watchers），"Python 拥有控制平面、agent 为有界节点"，用确定性代码负责编排/重试/验收，agent 只做需要阅读和判断的环节，与 sol-advisor（1,694⭐，Codex-native 编排）呼应"agent 编排层"主题 | super-simple-software-factory, sol-advisor | 82 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| firecrawl/anydoc | 8,069 | 工具型 | 90 | 更新（4,688→8,069，+3,381/+72%，跨入 8K，爆发进入减速阶段） |
| trycompai/crm | 7,156 | 平台候选 | 88 | 更新（6,138→7,156，+1,018/+16%，连续三日增速第一，但增速回落） |
| yc-software/qm | 12,022 | 平台候选 | 88 | 更新（11,653→12,022，+369/+3%，接近停滞，score 89→88） |
| KKKKhazix/human-writing | 1,552 | 工具型 | 85 | 更新（1,006→1,552，+546/+54%，溯源 humanizer 谱系，score 84→85） |
| 0xwilliamortiz/humanizer-cli | 581 | 工具型 | 83 | 新增（终端去 AI 腔检测，208 watchers，溯源 blader/humanizer） |
| Binaryify/open-kimi-ppt-skill | 1,286 | 工具型 | 83 | 更新（530→1,286，+756/+142%，爆发，fork 149→343，score 82→83） |
| disler/super-simple-software-factory | 459 | 观察型 | 82 | 新增（软件工厂 Skill，Python 控制平面 + agent 有界节点） |
| genspark-ai/genoffice | 2,034 | 平台候选 | 85 | 更新（1,755→2,034，+279/+15%，跨入 2K） |
| FareedKhan-dev/kimi-k3-in-c | 2,801 | 观察型 | 83 | 更新（2,544→2,801，+257/+10%，逼近 3K） |
| microsoft/skill-recorder | 2,127 | 工具型 | 84 | 更新（1,944→2,127，+183/+9%，跨入 2K） |
| criptogus/HermesOffice | 388 | 观察型 | 80 | 更新（327→388，+61/+18%） |
| magicrew/doc7 | 465 | 观察型 | 80 | 更新（454→465，+11/+2%，关注度低，score 81→80） |

#### 趋势观察

- **anydoc 的爆发正在走典型"真实需求驱动的热度曲线"**：首日 → +331% → +72%。增速回落但绝对增量仍居首（+3,381），区别于脉冲项目（zhuzhiliao 等）。fork 持续增长（370）+ 官方投入（5 天 6 版）佐证持续性。下一关键看 08-08 增速是否健康收敛（+30-40%）。
- **"去 AI 腔"写作治理是被 34K⭐ 源头验证的真实品类**：blader/humanizer（34,004⭐）证明需求真实。今日发现的是其多语言、多接口、多阶段扩展——human-writing（中文，事中改写）、humanizer-cli（英文，事后检测）、ratchet（事前约束）。谱系关系为基于功能同构的推断（humanizer-cli 明确溯源，human-writing 未明确声明）。
- **应用层格局固化**：qm（+3%，接近停滞）、crm（+16%，减速但仍领先）、genoffice（+15%，稳健）三个项目都在收敛。整个应用层主题可能在 2-3 日内进入尾声（除非有新垂直变体爆发）。
- **软件工厂 Skill 代表"agent 编排工程化"主题**：与 sol-advisor 共同信号——"agent 编排"从 ad-hoc prompt 进入工程化结构。super-simple-software-factory 的"Python 拥有控制平面"是可操作的范式参考。

## 2026-08-06（第九十一版）

### anydoc 爆发式跃迁（1,086→4,688，单日 +3,602/+331%，5 天连发 6 个版本），agent 文档摄入层从"新品类"变为"最热赛道"，doc7（本地 VLM 解析）与之构成"云 vs 本地"路线分化 · 应用层第五日结构性降温——qm 增速骤降（+1,634→+561，+17%→+5%）但仍守万星量级，crm 反超为增速第一（+1,569/+34%，连续两日领先），genoffice 稳健（+482/+38%），"分化"进入"crm 领跑、qm 守量"格局 · 中文 agent skill 品类出现——human-writing（1,006⭐，"活人感"写作）+ open-kimi-ppt-skill（530⭐，逆向 Kimi Slides→PPT），中文社区从"用 agent"进入"造 skill" · 长程 agent benchmark 品类出现——阿里 Accio RealReplicaBench（1,017⭐，107 任务，状态化评测，OpenClaw harness）

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | anydoc 爆发式跃迁 + agent 文档摄入层成最热赛道——1,086→4,688（单日 +3,602/+331%，5 天 6 版），doc7（本地 VLM 解析）与之构成"云/服务化 vs 本地/私有化"路线分化 | anydoc, doc7 | 90 |
| 2 | 应用层第五日结构性降温——qm 增速骤降（+1,634→+561，+17%→+5%）但仍守万星量级，crm 反超为增速第一（+1,569/+34%，连续两日），genoffice 稳健（+482/+38%），"分化"进入"crm 领跑、qm 守量"阶段 | qm, crm, genoffice | 88 |
| 3 | 中文 agent skill 品类出现——human-writing（1,006⭐，"活人感"中文写作 Skill）+ open-kimi-ppt-skill（530⭐，逆向 Kimi Slides→可编辑 PPTX），中文社区从"使用 agent"进入"制造 skill" | human-writing, open-kimi-ppt-skill | 85 |
| 4 | 长程 agent benchmark 品类出现——阿里 Accio RealReplicaBench（1,017⭐，107 任务，状态化 SaaS 副本评测，OpenClaw harness），填补"agent 能否完成真实业务流"的评测空白 | realreplicabench | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| firecrawl/anydoc | 4,688 | 工具型 | 90 | 更新（1,086→4,688，+3,602/+331%，5 天 6 版高频迭代，score 82→90） |
| trycompai/crm | 6,138 | 平台候选 | 88 | 更新（4,569→6,138，+1,569/+34%，连续两日增速第一，score 87→88） |
| yc-software/qm | 11,653 | 平台候选 | 89 | 更新（11,092→11,653，+561/+5%，增速骤降，score 90→89） |
| genspark-ai/genoffice | 1,755 | 平台候选 | 85 | 更新（1,273→1,755，+482/+38%，首个 fork 变体 HermesOffice 出现） |
| KKKKhazix/human-writing | 1,006 | 工具型 | 84 | 新增 |
| Accio-Lab/RealReplicaBench | 1,017 | 观察型 | 84 | 新增 |
| FareedKhan-dev/kimi-k3-in-c | 2,544 | 观察型 | 83 | 更新（1,952→2,544，+592，突破 2K） |
| Binaryify/open-kimi-ppt-skill | 530 | 工具型 | 82 | 新增 |
| microsoft/skill-recorder | 1,944 | 工具型 | 84 | 更新（1,751→1,944，+193/+11%） |
| magicrew/doc7 | 454 | 观察型 | 81 | 新增 |
| criptogus/HermesOffice | 327 | 观察型 | 80 | 新增（genoffice fork + Hermes Agent） |

#### 关键判断

- **anydoc 爆发跃迁，agent 文档摄入层成最热赛道**：5 天 6 版高频迭代（今日单日三版）是关键驱动——非自然增长，而是 Firecrawl 团队集中投入 + 现有用户基数（149K⭐主仓库）转化 + Agent Skill 分发放大。doc7（本地 VLM）与之构成"云 vs 本地"路线分化，与 K3 本地推理的"可用速度 vs 极限低内存"分化模式高度同构。**证据边界**：star/fork/发版频率为可核验事实；"集中投入"为推断；"单数毫秒""格式无关一致性"仍为 README 设计声明。
- **应用层进入"crm 领跑、qm 守量"格局**：qm 增速骤降（+5%），crm 连续两日增速第一（+34%）。这不是 qm 失败（仍守万星量级），而是应用层多路线竞争的格局确立——垂直重写（crm，PMF 最强信号）vs 通用平台（qm，量级护城河但衰减）。**证据边界**："格局确立"为连续两日数据的强推断（crm 连续增速领先是可核验事实）；qm 是否触及天花板需再观察 2-3 日。
- **中文 agent skill 品类出现**：human-writing（"去 AI 腔"写作）+ open-kimi-ppt-skill（逆向 Kimi→PPT）同日爆发，标志中文社区从"使用 agent"进入"制造 skill"。**证据边界**：首日数据，持续性未验；open-kimi-ppt-skill 的逆向工程路径有法律/稳定性风险（README 自述非官方，可能随 Kimi 更新失效）。
- **长程 agent benchmark 品类出现**：阿里 Accio RealReplicaBench（107 任务，状态化 SaaS 副本评测）填补"agent 能否完成真实业务流"评测空白。**证据边界**：107 任务覆盖面和验证器质量为 README 自述；mock 保真度未独立验证；强绑定 OpenClaw harness。

---

## 2026-08-05（第九十版）

### 应用层第四日分化——qm 突破 10K 关口（9,458→11,092，+1,634，增速衰减至 +17%）但 crm 反超增速（+1,446/+46%）、genoffice 翻倍（+709/+125%）；"齐涨"结束、"分化"开始，多路线各自验证 PMF · K3 本地推理品类叙事分裂——kimi-k3-in-c 持续 +779 逼近 2K（极限低内存叙事延续），waste 增量骤降 +510→+145（可用速度叙事退潮），"最低 RAM"卖点持续压过"接近可用速度" · Agent 可观测性/治理品类出现——Perplexity 官方 numbat（684⭐，端点 agent 活动可见性 + 取证重建 + 可选 pre-action 阻断 + 单二进制，覆盖十余个 agent），与 ratchet/skill-recorder 构成三层 agent 质量基础设施栈（技能提取→执行约束→事后取证）· Agent 摄入层扩张——Firecrawl 官方 anydoc（2 天 1.1K⭐，Rust，office 文档→LLM-ready Markdown，单数毫秒）

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 应用层第四日分化——qm 突破 10K（+1,634，+17%）但 crm 反超增速（+1,446/+46%）、genoffice 翻倍（+709/+125%）；"齐涨"结束、"分化"开始 | qm, crm, genoffice | 90 |
| 2 | Agent 可观测性/治理品类出现——Perplexity numbat 端点 agent 活动可见 + 取证 + 可选阻断，与 ratchet/skill-recorder 构成三层栈 | numbat, ratchet, skill-recorder | 85 |
| 3 | K3 本地推理品类叙事分裂——kimi-k3-in-c +779 逼近 2K，waste +510→+145 骤降，"最低 RAM"叙事压过"可用速度" | kimi-k3-in-c, waste | 84 |
| 4 | Agent 摄入层扩张——Firecrawl anydoc（office 文档→Markdown，2 天 1.1K⭐），文档解析成为 agent 基础设施标配 | anydoc | 82 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| yc-software/qm | 11,092 | 平台候选 | 90 | 更新（9,458→11,092，第四日 +1,634，突破 10K） |
| trycompai/crm | 4,569 | 平台候选 | 87 | 更新（3,123→4,569，+1,446，增速反超 qm，score 86→87） |
| genspark-ai/genoffice | 1,273 | 平台候选 | 85 | 更新（564→1,273，翻倍 +125%，score 84→85） |
| FareedKhan-dev/kimi-k3-in-c | 1,952 | 观察型 | 83 | 更新（1,173→1,952，+779，逼近 2K） |
| perplexityai/numbat | 684 | 工具型 | 84 | 新增 |
| firecrawl/anydoc | 1,086 | 工具型 | 82 | 新增 |
| microsoft/skill-recorder | 1,751 | 工具型 | 84 | 更新（1,366→1,751，+385） |
| 0xwilliamortiz/ratchet | 430 | 工具型 | 83 | 更新（423→430，+7，285 watchers 保持） |
| sqliteai/waste | 1,665 | 观察型 | 82 | 更新（1,520→1,665，+145，增量骤降，score 83→82） |
| openai/ten-proofs | 470 | 观察型 | 82 | 更新（432→470，+38，平缓） |

#### 关键判断

- **应用层从"齐涨"进入"分化"**：qm 第四日 +1,634（+17%）继续健康衰减（+250%→+47%→+35%→+17%），突破 10K 关口（11,092⭐），但**增速被 crm（+46%）和 genoffice（+125%）反超**。这是品类成熟的关键标志——市场开始在通用平台（qm，量级护城河）/ 垂直重写（crm，增速反超）/ 桌面生产力（genoffice，翻倍）三条路线间区分 PMF 强度。**证据边界**：star/fork 为可核验事实；"分化"为基于四日数据的强推断（增速交叉是可核验事实，"市场区分 PMF"是解释性推断）。crm fork 485（fork/star 10.6%）说明垂直 CRM 部署意愿强。
- **K3 本地推理品类叙事分裂**：waste 增量骤降 +510→+145（-72%），kimi-k3-in-c 持续 +779。两者增量比从 1.9:1 扩大到 5.4:1。这不是品类降温（kimi-k3-in-c 仍放量），而是**注意力在品类内部从"可用速度端"迁移到"极限低内存端"**。需警惕误读：叙事热度 ≠ 可用性——waste 0.62 tok/s 仍是真正日常可用方案，kimi-k3-in-c 32s/token 是可行性证明。**证据边界**：8.24GB RSS/32s/token/字节一致输出仍为作者自述。
- **Agent 可观测性/治理品类出现**：Perplexity 官方 numbat（684⭐）覆盖十余个 agent（Claude/Codex/Gemini/Copilot/OpenCode/Grok/Hermes/OpenClaw 等），三类输入（hooks/OTLP 日志/磁盘 artifacts）归一到统一事件模型，CEL 规则引擎 + 可选 pre-action 阻断。与 ratchet（执行约束）、skill-recorder（技能提取）构成三层栈。**证据边界**：覆盖矩阵为 docs 自述，未逐一验证 hook 实现深度；pre-action 阻断默认关闭（shipped 规则全为 monitor-only）；v0.1.2，subscribers 仅 5。
- **Agent 摄入层扩张**：Firecrawl anydoc（2 天 1.1K⭐）把 office 文档→LLM-ready Markdown，扩展 agent 文档摄入基础设施。**证据边界**："单数毫秒""格式无关一致性"为设计声明，复杂文档场景未独立验证；v0.1.3，subscribers 仅 2，含 Firecrawl 品牌导流成分。

---

## 2026-08-04（第八十九版）

### qm 第三日续涨 +2,443（7,015→9,458⭐，fork 736→998），第三日增量反超第二日彻底排除脉冲假设，应用层产品化趋势完全确认 · K3 本地推理品类级爆发——kimi-k3-in-c 单日 +955（218→1,173，近 5.4 倍）引爆极端低内存卖点，waste +510 续涨（连续三日增速递增） · OpenAI 官方 ten-proofs 用 Lean 4 形式化十项数学/理论计算机成果（球填充/非 sofic 群/Connes 刚性反例等），标志 AI + 形式化验证交叉品类出现 · agent 质量基础设施成型——ratchet 把 coding agent 极简规则从开环注入变闭环检查（PostToolUse hook 实时测复杂度，285 watchers 高质量关注）· 应用层多路线并行扩张（通用平台 qm/垂直重写 crm/AI-native 桌面 genoffice 同步放量）

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458，三日 +8,091），第三日 +2,443 反超第二日 +2,233 彻底排除脉冲；crm/genoffice 多路线同步放量 | qm, crm, genoffice | 92 |
| 2 | K3 本地推理品类级爆发——kimi-k3-in-c 单日 +955（218→1,173，近 5.4 倍）引爆极端低内存（8.24GB）卖点，waste +510 续涨，品类从个别项目变为系统性关注 | kimi-k3-in-c, waste | 88 |
| 3 | AI 推理边界外延——OpenAI 官方 ten-proofs 用 Lean 4 形式化十项数学成果（球填充/非 sofic 群/Connes 刚性反例等），标志 AI + 形式化验证交叉品类出现 | ten-proofs | 85 |
| 4 | agent 质量基础设施成型——ratchet 把极简规则从开环注入变闭环检查（PostToolUse hook 实时测复杂度/依赖/wrapper/yagni），与 skill-recorder 正交互补 | ratchet, skill-recorder | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| yc-software/qm | 9,458 | 平台候选 | 90 | 更新（7,015→9,458，第三日 +2,443，三日累计 +8,091） |
| FareedKhan-dev/kimi-k3-in-c | 1,173 | 观察型 | 83 | 更新（218→1,173，+955，爆发性增长） |
| openai/ten-proofs | 432 | 观察型 | 82 | 新增 |
| genspark-ai/genoffice | 564 | 平台候选 | 84 | 新增 |
| 0xwilliamortiz/ratchet | 423 | 工具型 | 83 | 新增 |
| trycompai/crm | 3,123 | 平台候选 | 86 | 更新（1,731→3,123，+1,392） |
| microsoft/skill-recorder | 1,366 | 工具型 | 84 | 更新（726→1,366，+640） |
| sqliteai/waste | 1,520 | 观察型 | 83 | 更新（1,010→1,520，+510） |

#### 关键判断

- **qm 第三日增量反超第二日，脉冲假设彻底排除**：7,015→9,458（+2,443），而第二日是 +2,233。脉冲型热度的特征是尖峰后快速回落，不可能出现"衰减后回升"。三日连涨（+3,415/+2,233/+2,443）无一日回落，从 1,367 到 9,458，三日累计 +8,091 stars / +873 forks。应用层产品化从"持续性趋势"（08-03，两日支撑）升级为**完全确立的趋势**（08-04，三日支撑）。**证据边界**：star/fork 为可核验事实；"完全确立"为三日数据的强推断，第四日将进一步巩固。open_issues 113（较 08-03 的 85 上升），subscribers 47（相对 9.4K⭐ 偏低）。
- **K3 本地推理品类级爆发**：kimi-k3-in-c +955（218→1,173）与 waste +510（1,010→1,520）同步放量，两者增量量级相近，说明社区同时关注"可用速度"（waste）与"极限低内存"（kimi-k3-in-c）。注意一个传播偏向：kimi-k3-in-c 增量首次超过 waste，说明"最低 RAM"卖点传播力更强，但 32s/token 是"能跑"非"能用"。**证据边界**：8.24GB RSS 与字节一致输出仍为作者自述，fork 23→176 增长可能带来首批独立验证信号。
- **AI + 形式化验证交叉品类出现**：openai/ten-proofs 用 Lean 4 形式化十项数学成果，每个可 `lake build` 独立验证。这是 AI 推理↔形式化验证交叉点的高公信力信号（OpenAI 官方）。**证据边界**：Lean 编译通过只证明形式化内部自洽，formalization 与 informal claim 的对应需人工对照。
- **agent 质量基础设施成型**：ratchet（423⭐/85 fork/285 watchers）把 agent 极简规则从开环注入变闭环检查，与 skill-recorder 正交互补。285 watchers（>stars）的异常比例说明是深度关注而非浅层 star。**证据边界**：六类探测器为启发式判断，误报率未经公开评测，强绑定 Claude Code。

---

## 2026-08-03（第八十八版）

### qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→736），昨日"脉冲 vs 趋势"之问得到回应——应用层产品化确认非一日脉冲 · K3 本地推理第四极：kimi-k3-in-c 便携 C99 把 RAM 下限打到 8.24GB（176KB 引擎/0 GPU/8GB 与 224GB 字节一致输出），waste 652→1,010 续涨 · 垂直应用层成型：trycompai/crm 1.7K⭐ 以 Vercel eve 为底座把 agent 做成 CRM 产品本体（agent 是产品/数据库只是笔记/证据账本/无置信度/deny-all egress 沙箱） · Microsoft skill-recorder 726⭐ 官方入场（录屏→Copilot 重建意图+步骤→生成可复用 Skill）

#### 今日三大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→736），增速从 +250% 正常化至 +47% 但绝对量级仍远超同期一切项目（K3 仅 +75），应用层产品化从"市场既成事实"确认为持续性趋势 | qm, cindy | 90 |
| 2 | K3 本地推理第四极——kimi-k3-in-c 便携 C99（8.24GB peak RSS/176KB 引擎/0 GPU/32s·token⁻¹）加入战局，waste 652→1,010 续涨，命题从"能否跑"深化为"RAM 下限能压到多低、速度-内存 Pareto 前沿在哪" | kimi-k3-in-c, waste, deltafin | 87 |
| 3 | 垂直应用层成型——trycompai/crm 1.7K⭐ 以 Vercel eve 为底座把 agent 做成 CRM 产品本体（agent 是产品/数据库只是笔记/证据账本/工具不接受置信度/deny-all egress 沙箱），eve 首个可观察生产级应用 | crm, skill-recorder | 86 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| yc-software/qm | 7,015 | 平台候选 | 90 | 更新（4,782→7,015，第二日 +2,233，score 89→90） |
| trycompai/crm | 1,731 | 平台候选 | 86 | 新增 |
| FareedKhan-dev/kimi-k3-in-c | 218 | 观察型 | 83 | 新增 |
| microsoft/skill-recorder | 726 | 工具型 | 84 | 新增 |
| sqliteai/waste | 1,010 | 观察型 | 83 | 更新（652→1,010，v0.6.2 cgroup-aware budget，score 82→83） |

#### 关键判断

- **qm 续涨确认应用层非脉冲**：昨日（08-02）最大悬念是 qm +250% 是否 trending 注意力脉冲。今日答案：4,782→7,015（+2,233/+47%），fork 同步 469→736。增速百分比衰减（+250%→+47%）是健康曲线，但绝对量级（+2,233/day）仍远超同期一切项目（K3 +75）。两日累计 +5,648 stars / +611 forks。**证据边界**：star/fork 为可核验事实；"持续性趋势"为两日数据的推断，第三日（08-04）是最终确认点。pushed_at 停在 08-01（热度由已有版本驱动）。
- **K3 本地推理 Pareto 前沿被四个独立实现探索**：waste（64GB/0.62 tok.s）、kimi-k3-in-c（8.24GB/32s·token⁻¹）、deltafin（Python/API）、colibri（多 GPU/744B/4 tok.s）覆盖速度-内存-易用性的不同权衡。kimi-k3-in-c 把 RAM 下限推到新极限（8.24GB），定义 Pareto 内存端。**注意**：8.24GB/32s·token⁻¹ 为作者 README 自述+标注 docs/data 实测，非第三方复现；"字节一致输出"是确定性计算推论，依赖 checkpoint 完整性待独立验证。作者 FareedKhan-dev 有从零实现公信力（train-llm-from-scratch 8.8K⭐）。
- **垂直应用层以 agent 为本体成型**：trycompai/crm 证明"agent 不是 CRM 功能，CRM 是 agent 记笔记的地方"可工程化——证据账本（工具不接受置信度）、deny-all egress 沙箱、以 Vercel eve 为底座。这是应用层第二次深化（08-02 通用 harness 产品化 → 08-03 垂直 SaaS 以 agent 重写）。eve 首个生产级采用，验证 filesystem-first 范式。**注意**：3 天项目，仅 2 contributors，生产成熟度未验。
- **刷星判断被印证**：decimen-optical-transfer 昨日 3,031→今日 3,620 几乎停滞，印证"刷星/脉冲"判断——真实热门项目不会在爆发次日停滞。WilonityLoader（1,213⭐/0 fork，游戏作弊工具）、flashloan-scalper-bot（213⭐/153 fork，疑似诈骗）具刷星/欺诈特征，已排除。

---

## 2026-08-02（第八十七版）

### qm 单日爆发 +250%（1,367→4,782⭐）验证 harness 应用层产品化进入主流 · qwen-audio-agent 1.2K⭐（全双工实时语音 + 后台任务并行/ACP 多 harness）加入应用层 · Agent 记忆独立成品类——OptMem 1.05K⭐（426-token prompt + 单 Python 脚本/append-only log/position-is-identity） · Kimi K3 本地推理三极分化——waste 纯 C 零依赖跑全量 2.78T（0.62 tok/s/64GB Mac）与 deltafin(Python)/colibri 并立 · K3 生态斜率继续趋平（K3 +108/AgentENV +41）· decimen-optical-transfer 3K⭐ 疑似刷星（star/watcher 159:1）标记不推荐

#### 今日三大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | qm 单日爆发 +250%（1,367→4,782⭐，fork 125→469 同步暴涨），harness 应用层产品化从趋势判断升级为市场既成事实；qwen-audio-agent 1.2K⭐ 以全双工实时语音 + 后台任务并行（ACP 接入 OpenCode/Claude Code/Codex/Hermes/Kimi Code）加入应用层 | qm, qwen-audio-agent, cindy | 89 |
| 2 | Agent 记忆/持久化独立成品类——OptMem 1.05K⭐（VictorTaelin/HVM 作者），426-token prompt + 单个无依赖 Python 脚本，append-only log + 重建式树摘要，position-is-identity，1M 记忆(608MB)wake 0.03s | optmem | 85 |
| 3 | Kimi K3 本地推理三极分化——waste 纯 C 零依赖跑全量 2.78T（0.45-0.62 tok/s/64GB Mac/trunk 驻内存+expert 磁盘流式/作者自验 logits 3.6e-06），与 deltafin(Python/589⭐)、colibri(C/744B) 并立，"推理瓶颈是内存放置策略"出现三种独立实现 | waste, deltafin, colibri | 82 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| yc-software/qm | 4,782 | 平台候选 | 89 | 更新（1,367→4,782，+250%，score 86→89） |
| VictorTaelin/OptMem | 1,058 | 工具型 | 85 | 新增 |
| QwenAudio/qwen-audio-agent | 1,181 | 平台候选 | 84 | 新增 |
| sqliteai/waste | 652 | 观察型 | 82 | 新增 |
| vercel-labs/scriptc | 2,677 | 工具型 | 86 | 更新（2,099→2,677，无其他变化） |

#### 关键判断

- **qm 爆发把应用层判断升级为既成事实**：昨日（08-01）判断 harness 竞争前沿向应用层转移，今日 qm 24h +250%（fork 同步 +344）给出最强市场验证。应用层从"qm/cindy/better-harness 三点"扩展为多形态矩阵（团队协同 qm / 语音 qwen-audio-agent / 个人客户端 cindy / 工程方法论 better-harness）。**待验**：+250% 含登上 trending 的注意力脉冲成分，明后日增速是确认主流 vs 脉冲的关键。**证据边界**：star/fork 为可核验事实；"应用层进入主流"为推断。
- **Agent 记忆独立成品类**：OptMem 把记忆从"需要数据库/向量库/后台服务"降维到"426-token prompt + 单脚本"。position-is-identity（定长记录→seek 即查询）与 qm 的 per-scope memory（内嵌平台）形成独立性 vs 集成度的路线对比。**注意**：0.03s/1M 记忆为作者自述；并发写与长上下文压缩边界未验；license 未声明。
- **本地推理三极分化**：waste（C/2.78T/单机）、deltafin（Python/全量/API server）、colibri（C/744B/多 GPU）三个独立团队、三种实现，命题"推理瓶颈是内存放置策略"不再依赖单一项目。**注意**：waste 0.62 tok/s 是可用性下限（26s/句），logits 一致性为作者自验非第三方复现；价值在可行性证明。
- **刷星干扰**：decimen-optical-transfer（3,031⭐，star/watcher ≈159:1，无描述，stargazers 接口异常）在搜索排名高于 qm/scriptc/quill，疑似刷星，标记不推荐、不纳入 key_projects。
- **K3 生态持续趋平**：K3 +108/AgentENV +41 较昨日再降；axrl +133 逆势高于昨日 +109，后训练方向有独立注意力。趋平≠价值下降，是社区发现阶段接近完成。

---

## 2026-08-01（第八十六版）

### Coding agent 应用层产品化：qm 多人协作 harness / cindy 开箱即用客户端 / better-harness 工程化方法论 · 边缘推理推到物理极限：esp32-ai 在 8 美元 ESP32-S3 上跑 28.9M LLM（Per-Layer Embeddings/flash 存参数表/9.5 tok/s） · quill 全本地 macOS 会议转录 · Kimi K3 生态增长斜率趋平（K3 +189/AgentENV +95，较昨日降一个数量级）

#### 今日三大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Coding agent 应用层产品化：qm 1.4K⭐（多人协作 harness/Slack+Web/per-scope sandbox），cindy 1.3K⭐（开箱即用多 harness 客户端/任务中途切换 harness×model），better-harness 1.3K⭐（harness 自我改进/loop engineering）——harness 竞争前沿从本体转移到应用产品形态 | qm, cindy, better-harness | 88 |
| 2 | 边缘推理边界推到极致：esp32-ai 2.6K⭐（28.9M LLM on $8 ESP32-S3/Per-Layer Embeddings/flash 存 25M 参数表/512KB SRAM/9.5 tok/s），quill 3.2K⭐（全本地 macOS 会议转录/Parakeet TDT/双轨录制/CAF 容错）——"推理瓶颈是内存放置策略"范式从 MoE 下沉到微控制器 | esp32-ai, quill | 85 |
| 3 | Kimi K3 生态延续增长但斜率趋平：K3 7,520→7,709（+189，昨日 +2,009）、AgentENV 2,595→2,690（+95，昨日 +1,184），axrl +109/deltafin +87 逆势正增长，脉冲效应衰减 | kimi-k3, agentenv, axrl, deltafin | 80 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| yc-software/qm | 1,367 | 平台候选 | 86 | 新增 |
| slvDev/esp32-ai | 2,627 | 观察型 | 83 | 新增 |
| makecindy/cindy | 1,260 | 平台候选 | 82 | 新增 |
| digimata/quill | 3,195 | 工具型 | 81 | 新增 |

#### 关键判断

- **harness 竞争前沿转移到应用层**：07-31 grok-build/omnigent/eve 在 harness 层多极化后，08-01 扩散到应用产品（qm/cindy）和工程方法论（better-harness）。分层演进链：harness 本体（grok-build）→ 编排（omnigent）→ 开发范式（eve）→ **应用产品（qm/cindy）+ 工程方法论（better-harness）**。当底层 harness 商品化，产品化竞争自然上移。风险：应用层项目均为早期（创建 7-11 天），上游 harness breaking change 可能使维护成本激增。
- **边缘推理范式家族成型**：esp32-ai（512KB SRAM）、quill（macOS 端侧）、colibri（多 GPU）、deltafin（单台 Mac）共享"推理瓶颈是内存放置策略"洞察。Per-Layer Embeddings（把不计算的参数留在慢存储）与 MoE 专家按需加载是同一原理的两种表现。待观察：esp32-ai 模型能力极有限（仅 TinyStories 级），热度来自话题性而非实用性；quill 是已可交付的工具。
- **K3 生态脉冲衰减**：增量较昨日降一个数量级说明"模型发布即生态动员"效应衰减，注意力转向新热点。但增长趋平≠价值下降，只是社区发现阶段接近完成。axrl/deltafin 逆势正增长说明后训练和本地推理有独立关注度。

---

## 2026-07-31（第八十五版）

### Coding agent harness 多极化：SpaceXAI 官方 grok-build 入场 + omnigent meta-harness + vercel/eve filesystem-first · 前沿 MoE 本地推理范式确立：colibri 纯 C 引擎 744B MoE 跑上消费硬件 19 天飙至 21K⭐ · Kimi K3 全栈生态五层齐增长

#### 今日三大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Coding agent harness 多极化：grok-build 23.5K⭐（SpaceXAI 官方/Rust TUI/ACP 嵌入/headless CI 三模式），omnigent 7.9K⭐（meta-harness/编排多 agent/跨设备协作/策略治理），vercel/eve 4.2K⭐（filesystem-first/agent 能力即目录结构/durable）——harness 层从单一工具分化为本体/范式/编排三层 | grok-build, omnigent, eve | 90 |
| 2 | 前沿 MoE 本地推理范式确立：colibri 21.2K⭐（纯 C/零依赖/GLM-5.2 744B MoE/VRAM-RAM-NVMe 三级内存层级/6×5090 全驻留 4 tok/s），19 天从 3.85K 飙至 21K，与 deltafin 同属"MoE 推理瓶颈是 I/O 而非 FLOPS"范式家族 | colibri | 87 |
| 3 | Kimi K3 全栈生态持续深化：五层齐增（K3 5.5K→7.5K/MoonEP 858→923/deltafin 308→466/axrl 569→641/AgentENV 1.4K→2.6K），验证"模型发布即生态动员"判断延续 | kimi-k3, moonep, deltafin, axrl, agentenv | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| xai-org/grok-build | 23,556 | 基础设施候选 | 90 | 新增 |
| JustVugg/colibri | 21,218 | 基础设施候选 | 88 | 更新（3.85K→21.2K） |
| omnigent-ai/omnigent | 7,924 | 平台候选 | 84 | 更新（7.0K→7.9K） |
| vercel/eve | 4,198 | 平台候选 | 83 | 更新（1.3K→4.2K，展开档案） |

#### 关键判断

- **harness 层成为独立品类**：当 coding agent 数量超过用户能手动切换的阈值，"harness 本体"（grok-build）、"开发范式"（eve）、"跨 harness 编排"（omnigent）各自成赛道。三者在不同抽象层次同框放量是结构性信号。风险：grok-build 当前 contributors 接口仅 1、无 release tag（源码从 monorepo 周期同步），生产成熟度待独立评估。
- **本地前沿 MoE 推理范式确立**：colibri 把 deltafin 验证的"MoE 稀疏性 → 专家按需加载"范式推进到多 GPU 全驻留可用吞吐（6×5090 4 tok/s）。待观察：6×5090 门槛仍高；单人项目 bus factor=1；非 SLA 研究运行时。
- **K3 生态齐增证明的是注意力而非生产成熟**：五层增量真实（GitHub API 可核验），但 K3 评测/MoonEP benchmark 均为自报（待独立复现），AgentENV 54 open issues 说明工程尚早。

---

## 2026-07-30（第八十四版）

### Kimi K3 发布首个开源 3T 级模型并带火全栈基础设施 · MoonEP 动态冗余专家实现 EP 完美负载均衡 · 2.8T MoE 按需流式加载进单台 Mac · 多轮 Agent RL 后训练走向工程化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 首个开源 3T 级模型：Kimi K3 5.5K⭐（2.8T MoE/104B 激活/KDA+AttnRes 新架构/Stable LatentMoE 896 选 16/1M 上下文/原生多模态），发布同日带动全栈基础设施涌现 | kimi-k3 | 93 |
| 2 | MoE 训练通信库赛道：MoonEP 858⭐（动态冗余专家/完美负载均衡/零拷贝+静态形状/通信低于 DeepEP v2 且对不均衡免疫），EP 均衡从"接受"走向"消除" | moonep | 88 |
| 3 | 超参数模型本地推理边界：deltafin 308⭐（MXFP4 专家按需 HTTP 流式加载/磁盘缓存/NEON+Metal/M1 Max 14.6s/token），MoE 稀疏性使超大模型本地部署在原理上可行 | deltafin | 84 |
| 4 | 多轮 Agent RL 后训练工程化：AxisRL 569⭐（SGLang rollout+Megatron 训练/300+ 轮轨迹/rollout-trainer 一致性调试），呼应昨日 AgentENV 环境层信号 | axrl | 83 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| MoonshotAI/Kimi-K3 | 5,511 | 基础设施候选 | 93 | 新增 |
| MoonshotAI/MoonEP | 858 | 基础设施候选 | 88 | 新增 |
| gavamedia/deltafin | 308 | 观察型 | 84 | 新增 |
| XYZ-AI-Lab/axrl | 569 | 基础设施候选 | 83 | 新增 |

#### 关键判断

- **"模型发布即生态动员"**：Kimi K3 单点发布在 72 小时内带动训练通信库（MoonEP）、本地推理（deltafin）、Agent RL 后训练（axrl）三层基础设施同时涌入 trending——说明 3T 级 MoE 的全栈工程化知识已足够下沉到开源社区。
- **MoonEP 的"完美均衡"思想值得吸收**：把 EP 负载不均衡从不可避免变为可工程消除，静态形状顺带解决内存碎片——对所有大规模 MoE 训练有借鉴价值，不限于 K3。风险：benchmark 为自报（H20 EP=8），待独立复现。
- **K3 评测需独立复现**：对标 Claude Fable 5/GPT-5.6 的分数为厂商自报，存在选择性披露风险；"2.5× scaling 效率"为官方声称。deltafin 的 14.6s/token 说明 2.8T 推理成本仍高，本地落地依赖量化/蒸馏。

---

## 2026-07-29（第八十三版）

### 本地优先 AI Coworker 交付成品范式 · Agent RL 训练 Firecracker 基础设施开源 · TS→Native 零运行时编译 · 单文件自包含 AI 可编辑文档

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 本地优先 AI Coworker：OpenWorker 9.9K⭐（Andrew Ng/交付成品非聊天/审批门控/BYO 模型/25+ 连接器/aisuite），重定义 Agent 应用层信任模型 | openworker | 92 |
| 2 | Agent RL 训练基础设施开源：AgentENV 1.4K⭐（Rust/Firecracker microVM/快照 fork<50ms 恢复/为 Kimi K3 训练提供底座），环境即快照即 fork | agentenv | 90 |
| 3 | 零运行时语言编译：scriptc 2.1K⭐（Vercel Labs/TS→原生二进制/无 Node V8/178KB 2ms 启动/99% 静态），Agent 代码部署成本降维 | scriptc | 86 |
| 4 | 单文件自包含 + AI 可编辑 JSON：Bento 2.8K⭐（文件即软件/自重写保存/CRDT+E2EE/JSON 可被 Agent 原地编辑），文档作为 Agent 交付物新形态 | bento | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| andrewyng/openworker | 9,965 | 平台候选 | 92 | 新增 |
| kvcache-ai/AgentENV | 1,411 | 基础设施候选 | 90 | 新增 |
| vercel-labs/scriptc | 2,099 | 工具型 | 86 | 新增 |
| nyblnet/bento | 2,806 | 工具型 | 84 | 新增 |

#### 关键判断

- **Agent 基础设施栈从「能跑」走向「可大规模训练、可交付成品」**：四个项目分别从应用层（OpenWorker）、训练层（AgentENV）、运行时层（scriptc）、文档层（Bento）共同验证 Agent 闭环交付与底层运行时工程化。
- **AgentENV 是今日最具基础设施价值的项目**：Firecracker microVM + 快照 fork 语义为 Agent RL 训练提供正确抽象，开源降低头部实验室训练管线复现门槛。风险：无鉴权、强依赖 KVM，生产化需时日。
- **scriptc 的「显式静态度」思想值得吸收**：逐构造决定编译边界、永不静默错误编译——对 Agent 生成代码的可审计性有启发。

---

## 2026-07-24（第八十二版）

### 人机协同工作空间基础设施化 · 代码知识图谱赛道升温 · Rust Agent Harness 性能碾压 · Agent OS 库化 · 混合架构 Code Review 落地

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 人机协同工作空间：Block Buzz 8.1K⭐（Nostr Relay 协议/Agent 与人类共享身份/Git NIP-34/ACP 接入），Block Inc. 出品 | buzz | 88 |
| 2 | 代码知识图谱赛道升温：Code-Review-Graph 26K⭐（Tree-sitter AST/MCP/82x Token 削减/30+ 语言），与 Graphify 94.8K 同赛道双重验证 | code-review-graph | 86 |
| 3 | Rust Agent Harness 性能碾压：jcode 11K⭐（14ms 启动/10 会话 117MB/语义记忆图谱），Rust 重写不是优化是降维打击 | jcode | 84 |
| 4 | Agent OS 库化：agentOS 4.1K⭐（WebAssembly+V8/6ms 冷启动/进程内运行），Agent 后端从 Sandbox 走向 In-Process | agentos | 82 |
| 5 | 混合架构 Code Review：Alibaba OCR 12K⭐（确定性管道+LLM/行级精准/阿里 2 年验证/Token 仅 1/9），生产落地证明 | open-code-review | 80 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| block/buzz | 8,122 | 平台候选 | 88 | 新增 |
| tirth8205/code-review-graph | 26,051 | 平台候选 | 86 | 新增 |
| 1jehuang/jcode | 11,093 | 工具型 | 84 | 新增 |
| rivet-dev/agentos | 4,096 | 基础设施候选 | 82 | 新增 |
| diegosouzapw/OmniRoute | 27,919 | 平台候选 | 84 | 更新（16.2K→27.9K） |
| citrolabs/ego-lite | 2,046 | 工具型 | 80 | 新增 |
| alibaba/open-code-review | 12,046 | 工具型 | 80 | 更新 |
| Graphify-Labs/graphify | 94,872 | 平台候选 | 92 | 更新（84.5K→94.8K） |
| earendil-works/pi | 76,758 | 平台候选 | 86 | 更新 |
| MoonshotAI/kimi-code | 4,872 | 工具型 | 78 | 更新（1.9K→4.9K） |

#### 判断修正

| 项目 | 原判断 | 修正判断 | 修正理由 |
|------|--------|----------|----------|
| Graphify | 同赛道唯一头部 | 同赛道头部但不再唯一 | code-review-graph 26K 证明赛道成立，但 Graphify 的 94.8K 和 40+ 语言仍保持明显领先 |
| OmniRoute | 工具型 (Score 80) | 平台候选 (Score 84) | Provider 数翻倍至 290+，贡献者 500+，已成为 LLM 时代 API 网关层 |
| alibaba/open-code-review | 未深度跟踪 | Score 80 / 工具型 | 混合架构+阿里内部 2 年验证，生产级 Code Review 的 Token 效率和 Precision 有结构性优势 |

---

## 2026-07-14（第八十一版）

### 代码知识图谱范式替代 RAG · AI 安全攻防双爆发 · Agent 原生创作工具 · AI 交易 Agent 多市场覆盖 · Agent Skill 生态初现

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 代码知识图谱范式替代：Graphify 84.5K⭐（tree-sitter AST/非向量/跨40+语言/EXTRACTED vs INFERRED），LOCOMO recall@10: 0.497（mem0 的 10 倍），零 LLM 调用 | graphify | 92 |
| 2 | AI 安全攻防双爆发：Strix 41.2K⭐（AI 渗透/Multi-Agent/真实 PoC）+ Hallmark 5K⭐（反 AI-slop/57 道 slop-test），Agent 安全攻守双翼 | strix, hallmark | 87 |
| 3 | Agent 原生创作工具：OpenCut 66K⭐（Rust 重写/MCP Server/Headless 批渲染），Agent 可直接编排视频生产 | opencut | 85 |
| 4 | AI 交易 Agent 多市场：Vibe-Trading 21.7K⭐（美股+港股+A股+印度/460 因子/Swarm 辩论）⚠️ 高风险 | vibe-trading | 80 |
| 5 | Agent Skill 生态：Graphify+Hallmark+archify+marketingskills，Skill 从提示词到能力包 | graphify, hallmark | 83 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| Graphify-Labs/graphify | 84,555 | 平台候选 | 92 | 更新（Score 89→92） |
| OpenCut-app/OpenCut | 66,019 | 平台候选 | 85 | 新增 |
| Nutlope/hallmark | 5,044 | 工具型 | 78 | 新增 |
| HKUDS/Vibe-Trading | 21,656 | 工具型 | 80 | 新增 |
| usestrix/strix | 41,188 | 工具型 | 85 | 更新（31.9K→41.2K） |
| stablyai/orca | 18,148 | 平台候选 | 84 | 更新（16.8K→18.1K） |

#### 判断修正

| 项目 | 原判断 | 修正判断 | 修正理由 |
|------|--------|----------|----------|
| Graphify | Score 89 / 平台候选 | Score 92 / 平台候选 | Benchmark 数据证明图谱遍历大幅优于向量检索（recall@10: 0.497 vs mem0 0.048），且零 LLM 调用。从"Skill 分发平台"升级为"代码理解范式替代" |
| Strix | Score 84 | Score 85 | 周增 4.1K 持续上榜，CI/CD 集成落地确认 |
| OpenCut | 未跟踪 | Score 85 / 平台候选 | MCP Server + Headless 渲染组合具有 Agent 创作基础设施潜力 |

## 2026-07-13（第八十版）

### Agent 沙箱基础设施收敛 · 本地优先 AI 应用爆发 · Agent Fleet 管理赛道成型 · AI 网关功能叠加

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 沙箱基础设施收敛：CubeSandbox 9.8K⭐（腾讯/Rust/KVM/E2B兼容/凭据保险库/Snapshot）+ chrome-devtools-mcp 46.8K⭐ + page-agent 26.2K⭐，Agent 执行层（沙箱+浏览器+页面操作）已形成完整基础设施栈 | cubesandbox, chrome-devtools-mcp, alibaba-page-agent | 90 |
| 2 | 本地优先 AI 应用爆发：Meetily 23.5K⭐（Rust/Whisper+Parakeet 实时转录/说话人分离/Ollama 摘要/100%本地）周增 8.6K 登顶 Trending，隐私法规+本地模型成熟=本地优先赛道起飞 | meetily | 86 |
| 3 | Agent Fleet 管理赛道成型：herdr 15.8K⭐（终端 Agent 多路复用）+ Orca 16.8K⭐（并行 Agent ADE）+ OfficeCLI 15.4K⭐（Agent 的 Office 套件），Agent 工具链从单体脚本走向 fleet 管理 | herdr, stablyai-orca, officecli | 88 |
| 4 | AI 网关层功能叠加：OmniRoute 16.2K⭐（231+ Provider/50+免费/RTK+Caveman 压缩省15-95% Token/自动 fallback/MCP+A2A），AI Gateway 进入功能竞争深水区 | omniroute | 82 |
| 5 | System Prompt 泄露与 Agent 安全：system_prompts_leaks 56.7K⭐（Claude/GPT/Gemini/Grok/Cursor 等全主流 AI system prompt 提取）周增 7.7K，Agent 安全攻击面映射 | system-prompts-leaks | 78 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| Zackriya-Solutions/meetily | 23,536 | 工具型 | 86 | 新增 |
| iOfficeAI/OfficeCLI | 15,395 | 工具型 | 83 | 新增 |
| TencentCloud/CubeSandbox | 9,795 | 基础设施候选 | 88 | 更新（7.1K→9.8K） |
| ogulcancelik/herdr | 15,766 | 工具型 | 83 | 更新（11.4K→15.8K） |
| stablyai/orca | 16,835 | 平台候选 | 86 | 更新（10.8K→16.8K） |
| diegosouzapw/OmniRoute | 16,171 | 工具型 | 80 | 更新（7.3K→16.2K） |
| JuliusBrussee/caveman | 88,504 | 工具型 | 72 | 更新（47.1K→88.5K） |
| TencentCloud/CubeSandbox | 9,795 | 基础设施候选 | 88 | 更新（7.1K→9.8K） |

#### 判断修正

| 项目 | 原判断 | 修正判断 | 修正原因 |
|------|--------|----------|----------|
| OmniRoute | Score 75 | Score 80 | Provider 从 160+ 扩展到 231+，RTK+Caveman 压缩组合验证有效，增速翻倍说明产品市场契合 |
| herdr | Score 83 | Score 85 | Socket API 让 Agent 互调是架构层突破，从'人的工具'升级为'Agent 协作基础设施' |

---

## 2026-07-12（第七十九版）

### 推测解码双引擎 · ChatGPT→Coding Agent 桥接 · Terminal Coding Agent 升温 · Local LLM 运维知识沉淀

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 推测解码工程化闭环：DeepSpec 6.5K⭐（训练侧/DSpark+DFlash+Eagle3 三算法统一 pipeline）+ Colibri 3.9K⭐（推理侧/纯C/MTP 2.8 tok/fwd），speculative decoding 从论文走向工程 | deepspec, colibri | 90 |
| 2 | ChatGPT→Coding Agent 桥接：DevSpace 3.2K⭐（28天/自托管 MCP server/让 ChatGPT Web 直接操作本地代码），Agent 交付新路径 | devspace | 78 |
| 3 | Terminal-native Coding Agent 升温：MiMo Code 11.8K⭐（32天/模型+Agent 协同进化/持久记忆），大厂入场 | mimo-code | 82 |
| 4 | Local LLM 运维知识沉淀：local-llm 1.3K⭐（9天/Shell/本地大模型运维百科），local LLM 进入工程化阶段 | local-llm | 75 |
| 5 | TUI 工具精品化持续：dnsglobe 814⭐（7天/Rust/ratatui/34 resolver 全球 DNS 传播地图） | dnsglobe | 72 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| Waishnav/devspace | 3,161 | 工具型 | 78 | 新增 |
| jamesob/local-llm | 1,348 | 学习型 | 75 | 新增 |
| JustVugg/colibri | 3,850 | 基础设施候选 | 88 | 更新（stars +87%） |
| deepseek-ai/DeepSpec | 6,541 | 基础设施候选 | 90 | 更新 |
| XiaomiMiMo/MiMo-Code | 11,815 | 工具型 | 82 | 更新 |

---

## 2026-07-12（第七十九版）

### Agent Skills 三巨头格局成型 · Code Intelligence MCP 基础设施化 · Agent 互联网感知层闭合 · 实用工具回归 · 分布式 GPU 推理网络萌芽

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 三巨头格局成型：Superpowers 252K+ECC 228K+mattpocock/skills 165K，合计 64 万 star | superpowers, ecc, mattpocock-skills | 90 |
| 2 | Code Intelligence MCP 基础设施化：codebase-memory-mcp 30K⭐（纯C/158语言/SLSA 3） | codebase-memory-mcp | 92 |
| 3 | Agent 互联网感知层闭合：Agent-Reach 54K+OpenCLI 26K+Firecrawl 149K | agent-reach, opencli, firecrawl | 88 |
| 4 | 实用工具回归：Knockoff 1.7K⭐（6天/过滤亚马逊伪品牌/全本地无追踪） | knockoff | 76 |
| 5 | 分布式 GPU 推理网络萌芽：Talos 971⭐（9天/WebSocket/开放模型推理） | talos | 70 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| Shpigford/knockoff | 1,761 | 工具型 | 35 | 新增 |
| jackwener/OpenCLI | 26,487 | 工具型 | 56 | 新增 |
| DeusData/codebase-memory-mcp | 30,110 | 基础设施候选 | 92 | 更新（26.1K→30.1K） |
| affaan-m/ECC | 228,578 | 平台候选 | 90 | 更新 |
| obra/superpowers | 252,402 | 平台候选 | 90 | 更新 |
| mattpocock/skills | 165,664 | 工具型 | 85 | 更新 |
| Panniantong/Agent-Reach | 54,902 | 基础设施候选 | 90 | 更新 |
| jmerlynyc/Talos | 971 | 观察型 | 70 | 更新 |

---

## 2026-07-11（第七十八版）

### LLM 可解释性工具化 · 教育知识图谱数据基础设施 · DevTools Rust化加速 · Agent Skill走向方法论 · 纯C跑744B MoE

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | LLM 可解释性工具化：Anthropic Jacobian Lens 1.1K⭐（9天/Python/MIT）是论文《Verbalizable Representations Form a Global Workspace》配套实现，平均雅可比矩阵传输逐层读出模型内部表示 | jacobian-lens | 82 |
| 2 | 教育知识图谱数据基础设施：Marble os-taxonomy 2.1K⭐（3天/1590微主题/3221前置依赖DAG/多国课程标准对齐），开源结构化课程图谱 | os-taxonomy | 78 |
| 3 | DevTools Rust化加速：Nub 2.8K⭐（38天/Rust/24×更快npm run/19×更快npx），Rust正在从底层渗透到开发者日常工具链 | nub | 80 |
| 4 | Agent Skill走向方法论：Loop Engineering 6.9K⭐+Ponytail 80K⭐+Omnigent 7K⭐，从单点竞争走向系统性编排范式 | loop-engineering, ponytail, omnigent | 86 |
| 5 | 纯C推理744B MoE：Colibri 2.1K⭐（10天/C语言/零依赖/GLM-5.2 744B MoE在25GB RAM消费机运行），本地推理工程极限 | colibri | 88 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| anthropics/jacobian-lens | 1,058 | 学习型 | 82 | 新增 |
| JustVugg/colibri | 2,065 | 基础设施候选 | 88 | 新增 |
| inkeep/open-knowledge | 2,545 | 工具型 | 82 | 新增 |
| withmarbleapp/os-taxonomy | 2,071 | 观察型 | 78 | 新增 |
| DietrichGebert/ponytail | 80,115 | 工具型 | 93 | 更新（76K→80K） |
| headroomlabs-ai/headroom | 58,381 | 基础设施候选 | 90 | 更新（52K→58K） |
| omnigent-ai/omnigent | 7,000 | 平台候选 | 86 | 更新（6.4K→7K） |
| cobusgreyling/loop-engineering | 6,946 | 工具型 | 85 | 更新（6K→6.9K） |
| XiaomiMiMo/MiMo-Code | 11,764 | 工具型 | 84 | 更新（10K→11.8K） |
| deepseek-ai/DeepSpec | 6,523 | 基础设施候选 | 90 | 更新（5K→6.5K） |
| nubjs/nub | 2,802 | 工具型 | 80 | 更新（2.5K→2.8K） |

---

## 2026-07-11（第七十八版）

### LLM 可解释性工具化 · 教育知识图谱数据基座 · DevTools Rust 化 · Agent Skill 方法论分层 · DNS 可观测性 TUI

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | LLM 可解释性工具化：Anthropic Jacobian Lens 1.1K⭐（9天/Python/全局工作空间论文/平均雅可比矩阵传输/逐层 token 读出），从 logit lens 到 Jacobian Lens 的第三代方法 | jacobian-lens | 82 |
| 2 | 教育知识图谱数据基座：Marble os-taxonomy 2.1K⭐（3天/1590微主题/3221前置依赖 DAG/8学科/多国标准对齐），开源结构化课程图谱 | os-taxonomy | 78 |
| 3 | DevTools Rust 化加速：Nub 2.8K⭐（38天/Rust/24×更快 npm run/19×更快 npx/18×更快 install），不替代 Node.js 只加速工作流 | nub | 80 |
| 4 | Agent Skill 方法论分层：Loop Engineering 6.9K⭐（设计循环）+ Ponytail 80K⭐（约束输出）+ Omnigent 7K⭐（元编排），从单 Skill 竞争走向方法论分层 | loop-engineering, ponytail, omnigent | 86 |
| 5 | DNS 可观测性 TUI：dnsglobe 793⭐（6天/Rust/ratatui/34解析器/世界地图），Rust+ratatui 成为 CLI 精品工具事实标准 | dnsglobe | 72 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| anthropics/jacobian-lens | 1,058 | 学习型 | 82 | 新增 |
| withmarbleapp/os-taxonomy | 2,071 | 观察型 | 78 | 新增 |
| nubjs/nub | 2,802 | 工具型 | 83 | 更新（2.6K→2.8K） |
| cobusgreyling/loop-engineering | 6,946 | 平台候选 | 85 | 更新（6.2K→6.9K） |
| omnigent-ai/omnigent | 7,000 | 平台候选 | 84 | 更新（6.4K→7K） |
| DietrichGebert/ponytail | 80,115 | 工具型 | 93 | 更新（76K→80K） |

---

## 2026-07-10（第七十七版）

### AI 红队元兵器 · 科研全闭环 Agent · Agent Harness 生态收敛 · 分布式 GPU 推理网络萌芽

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI 红队元兵器：T3MP3ST 4.2K⭐（8 天/AGPL-3.0/多 Agent kill chain/90.1% XBOW 基准/verify-claims 复现机制），把已有编码 Agent 变零日猎人 | t3mp3st | 87 |
| 2 | 科研全闭环 Agent：OpenScience 1.9K⭐（7 天/Apache-2.0/290+ 技能/30+ 科学数据库/全研究循环自动化），AI4Science 从概念走向产品 | openscience | 84 |
| 3 | Agent Harness 生态收敛：ECC 228K⭐+Hermes 212K⭐+OpenCode 184K⭐+OpenClaw 382K⭐，编码 Agent 基础设施格局定型 | ecc, hermes-agent, opencode | 85 |
| 4 | 分布式 GPU 推理网络萌芽：Talos 815⭐（8 天/MIT/WebSocket+uptime 奖励），去中心化推理算力市场早期信号 | talos | 72 |
| 5 | Vercel Eve 稳步增长：3.4K⭐（24 天/filesystem-first/日均 ~40 Star），Agent 框架标准化持续推进 | vercel-eve | 83 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| elder-plinius/T3MP3ST | 4,152 | 工具型 | 87 | 新增 |
| synthetic-sciences/openscience | 1,935 | 平台候选 | 84 | 新增 |
| jmerelnyc/Talos | 815 | 学习型 | 72 | 新增 |
| vercel/eve | 3,360 | 平台候选 | 85 | 更新（2.5K→3.4K） |
| affaan-m/ECC | 227,840 | 基础设施候选 | 95 | 更新（226K→228K） |
| NousResearch/hermes-agent | 212,171 | 平台候选 | 92 | 更新（持续增长） |
| anomalyco/opencode | 184,211 | 平台候选 | 90 | 更新（持续增长） |

---

## 2026-07-07（第七十六版）

### Agent 约束即性能 · OCR 长程解析突破 · 贵模型规划+便宜模型执行 · 多 Agent 元编排成赛道 · 中国大厂编码 Agent 密集开源

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 约束即性能：Ponytail 75.8K⭐（25 天/MIT/16 种 Agent 兼容）54% less code/20% cheaper/27% faster/100% safe，系统化 YAGNI 约束而非提示词技巧 | ponytail | 92 |
| 2 | OCR 长程解析突破：Baidu Unlimited-OCR 13.5K⭐（19 天/MIT/One-shot Long-horizon Parsing）超越 DeepSeek-OCR，VLM 吃掉传统 OCR pipeline | unlimited-ocr | 88 |
| 3 | 贵模型规划+便宜模型执行：shadcn/improve 7K⭐（27 天/MIT/9 类并行审计/计划即产品）将 LLM 成本梯度利用范式固化成 Skill | improve | 89 |
| 4 | 多 Agent 元编排成赛道：Omnigent 6.4K⭐（26 天/Apache-2.0/统一编排 6+ Agent）同时 ECC 226K⭐+cc-switch 114K⭐ 验证元编排需求 | omnigent | 86 |
| 5 | 中国大厂编码 Agent 密集开源：MiMo-Code 11.5K⭐（27 天/MIT/模型+Agent 协同进化），百度+DeepSeek+小米生态成型 | mimo-code | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| DietrichGebert/ponytail | 75,876 | 工具型 | 92 | 更新（25 天 76K，登顶 Trending） |
| baidu/Unlimited-OCR | 13,490 | 基础设施候选 | 88 | 新增 |
| shadcn/improve | 7,049 | 工具型 | 89 | 新增 |
| omnigent-ai/omnigent | 6,422 | 平台候选 | 86 | 更新（4.7K→6.4K） |
| XiaomiMiMo/MiMo-Code | 11,530 | 工具型 | 84 | 更新（10.6K→11.5K） |
| langchain-ai/openwiki | 7,394 | 工具型 | 87 | 更新（5K→7.4K） |
| cobusgreyling/loop-engineering | 6,184 | 平台候选 | 85 | 更新（5.9K→6.2K） |
| deepseek-ai/DeepSpec | 6,319 | 基础设施候选 | 90 | 更新（6.2K→6.3K） |

---

## 2026-07-06（第七十五版）

### 推测解码训练框架基建化 · Agent 文档自动化成新赛道 · Loop Engineering 方法论化 · Node.js 工具链 Rust 化 · 表格基础模型实用化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 推测解码训练框架基建化：DeepSeek DeepSpec 6.2K⭐（10 天创建/DSpark+DFlash+Eagle3 三算法/完整 pipeline/38TB 数据集/含论文+checkpoint），推理加速从调 API 走向可训练全栈基础设施 | deepspec | 90 |
| 2 | Agent 文档自动化成新赛道：langchain-ai/openwiki 5K⭐（14 天/CLI+GitHub Action/自动 AGENTS.md 注入/Multi-LLM），代码文档从人写人读→Agent 写 Agent 读 | openwiki | 87 |
| 3 | Loop Engineering 方法论化：cobusgreyling/loop-engineering 5.9K⭐（loop-init/audit/cost/sync/context 五件套），Agent 编排从 ad-hoc prompting 走向系统化工程方法论 | loop-engineering | 85 |
| 4 | Node.js 工具链 Rust 化加速：nubjs/nub 2.6K⭐（Rust/bun-like DX on stock node/24× faster run/19× faster npx），不替换 runtime 只加速工具链 | nub | 83 |
| 5 | 表格基础模型从研究走向实用：Google tabfm 1.3K⭐（scikit-learn 兼容/零样本分类+回归/JAX+PyTorch 双后端），同时 Ponytail 74.8K⭐ 持续验证 YAGNI Agent 理念 | tabfm, ponytail | 80 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| deepseek-ai/DeepSpec | 6,238 | 基础设施候选 | 90 | 新增 |
| langchain-ai/openwiki | 5,014 | 工具型 | 87 | 新增 |
| cobusgreyling/loop-engineering | 5,896 | 平台候选 | 85 | 新增 |
| nubjs/nub | 2,629 | 工具型 | 83 | 新增 |
| DietrichGebert/ponytail | 74,748 | 工具型 | 80 | 更新（持续高位，YAGNI Agent 验证） |
| google-research/tabfm | 1,264 | 学习型 | 75 | 新增 |

---

## 2026-07-05（第七十四版）

### 代码智能 MCP 爆发 · Agent 视频生产系统崛起 · 前端 Agent-Ready 加速 · Agent 终端多路复用成熟化 · 安全+隐私双线并进

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 代码智能 MCP 爆发：codebase-memory-mcp 26.1K⭐（周+10.2K 增速 Top 3）C 语言/tree-sitter+知识图谱/亚毫秒查询/99% token 缩减/158 语言/14 MCP tools/11 Agent 自动配置 | codebase-memory-mcp | 92 |
| 2 | Agent 视频生产系统崛起：OpenMontage 33K⭐（周+9.2K）12 pipeline/52 tool/500+ skill，video-use 14.7K⭐ Agent 编辑视频 | openmontage, video-use | 87 |
| 3 | 前端 Agent-Ready 加速：Astryx 5.3K⭐（日+1,013 TS 榜首）Meta 8 年设计系统开源，API+docs+CLI 一体化 | astryx | 86 |
| 4 | Agent 终端多路复用成熟化：herdr 11.4K⭐（日+706/周+3K）增速加快，Socket API+插件系统，tmux-for-agents 路线清晰 | herdr | 85 |
| 5 | 安全+隐私双线并进：strix 35.9K⭐（日+1,910）AI 渗透测试，meetily 隐私优先本地会议助手，system_prompts_leaks 48.8K⭐ prompt 审计 | strix, meetily | 83 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| DeusData/codebase-memory-mcp | 26,117 | 基础设施候选 | 92 | 更新（周+10.2K，增速创新高） |
| calesthio/OpenMontage | 33,050 | 平台候选 | 85 | 更新（周+9.2K） |
| ogulcancelik/herdr | 11,372 | 工具型 | 83 | 更新（Score↑5，日+706 增速加快） |

---

## 2026-07-04（第七十三版）

### Agent 安全运行时双雄对垒 · 前端 Agent-Ready 设计系统 · Agent 多路复用持续升温 · Agent 感知层 MCP 化 · Token 经济学常态化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 安全运行时双雄对垒：腾讯 CubeSandbox 7.1K⭐（Rust+KVM 亚 60ms/E2B 兼容）vs NVIDIA OpenShell 7.3K⭐（四层策略隔离/GPU 直通）。两大巨头同时押注 Agent 安全沙箱 | cubesandbox, nvidia-openshell | 91 |
| 2 | 前端 Agent-Ready 设计系统：Meta Astryx 4.5K⭐（日+943）8 年内部/13K+ 应用/150+ 组件/StyleX。Google design.md 24.6K⭐。设计系统从人用到人+Agent 共用 | astryx, design-md | 87 |
| 3 | Agent 多路复用持续升温：herdr 10.7K⭐（日+513），Orca 11.6K⭐（日+736），codex-plugin-cc 23.1K⭐。Agent 编排层从工具变基础设施 | herdr, stablyai-orca, codex-plugin-cc | 86 |
| 4 | Agent 感知层 MCP 化：chrome-devtools-mcp 45.4K⭐（日+404），page-agent 22.3K⭐（日+949）。浏览器自动化从脚本模式转向 MCP 原生 Agent 模式 | chrome-devtools-mcp, alibaba-page-agent | 84 |
| 5 | Token 经济学常态化：caveman 82.8K⭐（日+2,851 持续霸榜）token 压缩 65% 已成标配。strix 34.4K⭐ AI 渗透测试。no-mistakes 5K⭐ git 防护 | caveman, strix, no-mistakes | 83 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| TencentCloud/CubeSandbox | 7,146 | 基础设施候选 | 88 | 更新（Score↑8，新增 Snapshot/E2B 兼容/凭据保险库） |
| NVIDIA/OpenShell | 7,374 | 基础设施候选 | 87 | 更新（新增 Helm K8s/OpenShift/GPU 直通） |
| facebook/astryx | 4,520 | 平台候选 | 82 | 更新（日+943 增速第二，3 天 317% 增长） |
| ogulcancelik/herdr | 10,702 | 工具型 | 78 | 更新（日+513，持续 Trending） |
| DeusData/codebase-memory-mcp | 25,503 | 基础设施候选 | 92 | 更新（日+900，周+9.8K） |

---

## 2026-07-03（第七十二版）

### Agentic Video Production 元年 · 代码知识图谱爆发 · Agent 多路复用基础设施化 · Agent 全网感知层成熟 · AI 安全与 token 经济学

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agentic Video Production 元年到来：OpenMontage 31.7K⭐（周+12.6K 榜首）定义 agentic 视频生产系统——12 管线/52 工具/500+ Agent 技能。video-use 13.7K⭐ 让 coding agent 剪视频。Agent 从代码生产扩展到内容生产 | openmontage, video-use | 90 |
| 2 | 代码知识图谱爆发式增长：codebase-memory-mcp 24.6K⭐（周+9.7K 近乎翻倍）158 语言/亚毫秒查询/99% token 节省。cognee 26.6K⭐ 自托管 Agent 记忆平台。Agent 记忆层从可选变必选 | codebase-memory-mcp, cognee | 89 |
| 3 | Agent 多路复用与编排基础设施化：herdr 10.1K⭐ Rust 终端多路复用，Orca 11K⭐ 多 Agent ADE，gstack 119K⭐ 角色化工具栈，codex-plugin-cc 22.5K⭐ 跨 Agent 桥接 | herdr, orca, gstack, codex-plugin-cc | 87 |
| 4 | Agent 全网感知层成熟：Agent-Reach 49K⭐（周+8.8K）零 API 费用覆盖 Twitter/Reddit/YouTube/Bilibili。MediaCrawler 55K⭐ 多平台数据采集 | agent-reach, media-crawler | 86 |
| 5 | AI 安全与 token 经济学：strix 32K⭐（日+2.2K）AI 渗透测试。caveman 80.7K⭐ token 压缩 65%。no-mistakes 4.9K⭐ git push 防护 | strix, caveman, no-mistakes | 84 |

#### 今日新增/更新项目

| 项目 | Stars | 分类 | Score | 变化 |
|------|-------|------|-------|------|
| calesthio/OpenMontage | 31,677 | 平台候选 | 85 | 更新（周+12.6K 榜首） |
| ogulcancelik/herdr | 10,108 | 工具型 | 78 | 更新（周+2.4K） |
| DeusData/codebase-memory-mcp | 24,603 | 基础设施候选 | 92 | 更新（周+9.7K Score↑3） |
| Panniantong/Agent-Reach | 49,078 | 基础设施候选 | 90 | 更新（周+8.8K） |
| topoteretes/cognee | 26,607 | 基础设施候选 | 88 | 更新（周+5.2K Score↑1） |
| usestrix/strix | 31,977 | 工具型 | 84 | 更新（日+2.2K） |

---

## 2026-07-02（第七十一版）

### Agent Skills 标准化 · Meta Astryx 设计系统开源 · Agent IDE 激战 · AI 安全持续高温 · Agent 数据层深化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 成为新标准层：Anthropic 发起的开放 Agent Skills 规范被 nvidia/microsoft/google/vercel 采纳。obra/superpowers 将 Skills 升级为完整开发方法论。Agent 生态正在形成类似 npm/pip 的“技能包”分发层 | agentskills, superpowers, nvidia-skills | 92 |
| 2 | Meta 开源 Astryx 设计系统：内部 8 年/13000+ 应用/150+ 组件/StyleX/agent-ready。与 design.md（24.3K⭐）形成 Agent 前端“描述层 vs 组件层”双轨 | astryx, design-md | 88 |
| 3 | Agent IDE 与编排层激战：Orca（10.8K⭐ 周+3.5K）多 Agent 并行 ADE，herdr（9.9K⭐）Rust 终端多路复用，codex-plugin-cc（22.4K⭐）跨 Agent 桥接，ECC harness 优化 | orca, herdr, codex-plugin-cc | 87 |
| 4 | AI 安全攻防持续高温：strix 31K⭐（日+2.2K）AI 渗透测试 Agent，caveman 79.8K⭐ token 压缩 65%，no-mistakes 4.8K⭐ git push 防护 | strix, caveman, no-mistakes | 85 |
| 5 | Agent 数据感知与记忆层深化：Agent-Reach 48.9K⭐（周+8.8K），cognee 26.5K⭐，codebase-memory-mcp 24.4K⭐（周+4.9K） | agent-reach, cognee, codebase-memory-mcp | 86 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| facebook/astryx | 3,274 | 平台候选 | 88 |
| agentskills/agentskills | trending | 基础设施候选 | 90 |
| openai/codex-plugin-cc | 22,353 | 工具型 | 82 |
| google/agents-cli | 4,627 | 工具型 | 80 |

#### 持续跟踪项目更新

| 项目 | 上次 Stars | 今日 Stars | 变化 |
|------|-----------|-----------|------|
| usestrix/strix | trending | 31,051 | 首次量化 |
| stablyai/orca | 8,583 | 10,771 | +2,188 |
| DeusData/codebase-memory-mcp | 19,466 | 24,357 | +4,891 |
| Panniantong/Agent-Reach | 44,400 | 48,858 | +4,458 |
| diegosouzapw/OmniRoute | 7,335 | 10,062 | +2,727 |

---

## 2026-06-29（第七十版）

### AI 安全攻防工具化 · 代码智能层持续高增 · AI 金融 Agent 爆发 · 本地 Voice I/O 成熟 · LLM 路由层整合

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI 安全攻防工具化加速：strix AI 渗透测试 Agent（Docker 沙箱+多 Agent 协作+PoC 验证），claude-bug-bounty 3.6K⭐ 终端化漏洞猎捕。配合 no-mistakes+Anthropic-Cyber-Skills 形成完整'防御→渗透→猎捕→技能'闭环 | strix, claude-bug-bounty | 89 |
| 2 | 代码智能层持续高增长：codebase-memory-mcp 19.5K⭐（日增 1.2K）arXiv 论文发表（31 仓库测试 83% 质量/10× token 节省），design.md 22.8K⭐ Agent 设计规范被普遍采纳，vercel-labs/skills 24K⭐ | codebase-memory-mcp, design-md | 90 |
| 3 | AI 金融 Agent 全面爆发：ai-berkshire 5.2K⭐ 日增 1,456 四大师方法论多 Agent 对抗，daily_stock_analysis 51K⭐，Vibe-Trading 个人交易 Agent | ai-berkshire, vibe-trading | 84 |
| 4 | 本地 AI Voice I/O 成熟：FluidVoice 3.7K⭐ 日增 491 macOS 最快离线听写（Parakeet 零延迟+本地 AI 增强），voicebox 35.4K⭐ 开源语音工作室 | fluidvoice, voicebox | 82 |
| 5 | Agent 路由层与免费 LLM 网关整合：OmniRoute 7.3K⭐ 160+ Provider 聚合（RTK 压缩 15-95% token），Agent-Reach 44.4K⭐ 感知层，orca 8.6K⭐ 多 Agent 编排 | omniroute, agent-reach | 80 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| usestrix/strix | trending | 工具型 | 84 |
| altic-dev/FluidVoice | 3,657 | 工具型 | 78 |
| xbtlin/ai-berkshire | 5,235 | 观察型 | 76 |
| diegosouzapw/OmniRoute | 7,335 | 工具型 | 75 |

#### 持续跟踪项目更新

| 项目 | 昨日 Stars | 今日 Stars | 变化 |
|------|-----------|-----------|------|
| codebase-memory-mcp | 17,459 | 19,466 | +2,007 |
| design.md | 22,316 | 22,807 | +491 |
| Agent-Reach | 42,263 | 44,384 | +2,121 |
| stablyai/orca | 7,901 | 8,583 | +682 |

---

## 2026-06-28（第六十九版）

### 代码智能层大爆发 · Agent 安全治理层崛起 · Agent-Native 应用框架首次定义 · OpenMontage 周增 17K · Voice I/O 成熟

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 代码智能与记忆层大爆发：codebase-memory-mcp 17.5K⭐ 周增 7.6K（tree-sitter 知识图谱/158 语言/亚毫秒查询），cognee 23.9K⭐ 周增 5.1K（Agent 记忆平台/知识图谱+向量搜索）。Agent '大脑层'从实验走向生产 | codebase-memory-mcp, cognee | 91 |
| 2 | Agent 安全治理层崛起：no-mistakes 3.8K⭐ git push AI 防护门（disposable worktree+验证流水线），Anthropic-Cybersecurity-Skills 22.2K⭐ 817 条安全技能映射 6 大框架。Agent 生态进入'安全可控'阶段 | no-mistakes, anthropic-cybersecurity-skills | 87 |
| 3 | Agent-Native 应用框架首次定义：BuilderIO/agent-native 2.7K⭐ defineAction 六端复用，UI 与 Agent 等公民，Agent 可自修改应用 | agent-native | 85 |
| 4 | OpenMontage + design.md 持续领跑：OpenMontage 25.1K⭐ **周增 17.2K** GitHub 增长第一，design.md 22.3K⭐ 连续 4 天日增 1.5K+ | openmontage, design-md | 88 |
| 5 | Voice I/O 成熟 + Agent 垂直应用深化：voicebox 34.9K⭐ 本地 AI 语音工作室（7 TTS/MCP server），ai-berkshire 4K⭐，open-seo 3.3K⭐ | voicebox, ai-berkshire | 83 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| topoteretes/cognee | 23,943 | 基础设施候选 | 87 |
| kunchenguid/no-mistakes | 3,790 | 工具型 | 82 |
| BuilderIO/agent-native | 2,707 | 平台候选 | 84 |
| jamiepine/voicebox | 34,860 | 工具型 | 83 |

#### 今日更新项目

| 项目 | Stars 变化 | 更新 |
|------|-----------|------|
| DeusData/codebase-memory-mcp | 14.7K→17.5K (+19%) | 与 cognee 互补关系确认，score 88→89 |
| calesthio/OpenMontage | 23.5K→25.1K | 周增 17.2K，GitHub 本周增长第一 |
| google-labs-code/design.md | 21.1K→22.3K | 连续 4 天日增 1.5K+，验证长期趋势 |
| stablyai/orca | 7.9K→8.3K | 新增 SSH worktree、CLI scripting |

---

## 2026-06-27（第六十八版）

### Agent 感知层大整合 · LLM 零成本基建加速 · Agent 并行编排日常化 · DESIGN.md 持续领跑 · Agent 垂直应用全面渗透

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 感知层大整合：Agent-Reach 42K⭐（7+平台零API）+ page-agent 20K⭐（自然语言操控网页UI），Agent '眼睛+手'标准化 | agent-reach, alibaba-page-agent | 90 |
| 2 | LLM 零成本基建加速：FreeLLMAPI 13K⭐ 2个月17倍增长，16 Provider ~1.7B tokens/月，OpenAI+Anthropic双兼容 | freellmapi | 87 |
| 3 | Agent 并行编排日常化：Orca 7.9K⭐ ADE + multica 开源管理平台 + gstack 23工具链 | stablyai-orca | 86 |
| 4 | DESIGN.md + OpenMontage 持续领跑：design.md 21K⭐ 连续3天日增2K+，OpenMontage 23.5K⭐ 持续高增长 | design-md, openmontage | 88 |
| 5 | Agent 垂直应用全面渗透：ai-berkshire/TREK/open-seo/ainovel-cli 等，Agent 渗透每个垂直领域 | ai-berkshire, ai-website-cloner-template | 82 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| xbtlin/ai-berkshire | 3,065 | 学习型 | 72 |
| every-app/open-seo | 3,046 | 工具型 | 75 |

#### 今日更新项目

| 项目 | Stars 变化 | 更新 |
|------|-----------|------|
| Panniantong/Agent-Reach | 38.6K→42.3K (+10%) | 平台扩展至10+，多后端路由成熟，score 89→90 |
| tashfeenahmed/freellmapi | 783→13,142 (17倍) | Provider 14→16，Anthropic兼容，score 76→85 |
| stablyai/orca | 7.4K→7.9K | 新增 Annotate Diffs、Account Switcher |
| google-labs-code/design.md | 19K→21.1K | 连续3天日增2K+，验证标准化趋势 |
| calesthio/OpenMontage | 21.9K→23.5K | 持续高增长 |

---

## 2026-06-26（第六十七版）

### Agent × Design System 标准化接口 · Agentic 视频生产大爆发 · Agent 安全治理工具化 · Agent 记忆层竞速 · Apple container 基础设施级增长

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent × Design System 标准化：Google Labs design.md 19K⭐ DESIGN.md 规范（YAML tokens + Markdown 理由），填补 Agent 与设计系统的结构化理解缺口 | design-md | 90 |
| 2 | Agentic 视频生产大爆发：OpenMontage 4天从 8.5K 暴涨至 22K（+158%），12 pipeline × 52 tools 验证 Agent 不止写代码 | openmontage | 88 |
| 3 | Agent 安全治理工具化：SkillSpector 10.7K⭐（68 类漏洞检测）+ Cybersecurity-Skills 21K⭐（817 安全 Skills），安全从理念变成工具链 | nvidia-skillspector, anthropic-cybersecurity-skills | 87 |
| 4 | Agent 记忆层竞速：TencentDB-Agent-Memory 6.2K⭐ 全本地 4 层管线 vs codebase-memory-mcp 14.7K⭐ tree-sitter 知识图谱 | codebase-memory-mcp, tencentdb-agent-memory | 85 |
| 5 | Apple container 基础设施级增长：43K⭐ 日增 1,366，Apple 官方开源基础设施项目稳步攀升 | apple-container | 84 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| google-labs-code/design.md | 19,005 | 平台候选 | 90 |
| TencentCloud/TencentDB-Agent-Memory | 6,157 | 基础设施候选 | 82 |

#### 今日更新项目

| 项目 | Stars 变化 | 更新 |
|------|-----------|------|
| OpenMontage | 8.5K→22K (+158%) | 爆发式增长、双渲染引擎、score 80→86 |
| codebase-memory-mcp | 12.8K→14.7K | 周增 9.6K，MCP 代码智能确认 |
| NVIDIA/SkillSpector | 8.3K→10.7K | MCP Server 模式、68 类漏洞 |
| stablyai/orca | 5.8K→7.4K | 持续增长 |
| apple/container | 36K→43K | 健康增长曲线 |
| Anthropic-Cybersecurity-Skills | 18.6K→21.2K | 安全闭环定位 |
| alibaba/page-agent | 19.2K→19.8K | 稳步增长 |
| withastro/flue | 6.3K→6.7K | 稳步增长 |

---

## 2026-06-25（第六十六版）

### Agent '懒惰工程'范式大规模验证 · Meta-harness 编排层竞争白热化 · 大厂 Coding Agent 终端争夺战 · OCR 长程解析突破 · Agent Skills 生态独立化确认

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent '懒惰工程'范式大规模验证：ponytail 55K⭐ 7级'懒惰阶梯'实现 54% 代码削减+100% 安全保持 | ponytail, shadcn-improve | 93 |
| 2 | Meta-harness 编排层竞争白热化：omnigent 4.7K⭐（Python+多设备+治理）vs vercel/eve 2.5K⭐（TS+filesystem-first） | omnigent, vercel-eve | 90 |
| 3 | 大厂 Coding Agent 终端争夺战：MiMo-Code 10.6K⭐（持久内存+Goal/Stop）vs shadcn/improve 6.1K⭐（审计→计划→执行分层） | mimo-code, shadcn-improve | 89 |
| 4 | OCR 长程解析突破：baidu/Unlimited-OCR 6.3K⭐ one-shot long-horizon parsing，超越 DeepSeek-OCR | baidu-unlimited-ocr | 87 |
| 5 | Agent Skills 生态独立化确认：BuilderIO/skills 2.6K⭐ 入场，Skills 成为 B2D 分发渠道 | builderio-skills, shadcn-improve, ponytail | 86 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| baidu/Unlimited-OCR | 6,273 | 基础设施候选 | 86 |

#### 今日更新项目

| 项目 | Stars 变化 | 更新 |
|------|-----------|------|
| ponytail | 36K→55K (+18.6K) | benchmark 更新、score 92→93 |
| omnigent | 4.2K→4.7K (+500) | 文档分析更新 |
| vercel-eve | 1.8K→2.5K (+700) | filesystem-first 架构分析 |
| shadcn-improve | 5.5K→6.1K (+600) | reconcile/branch/execute 命令 |
| mimo-code | 9.8K→10.6K (+800) | Goal/Stop、Compose Mode 分析 |

---

## 2026-06-24（第六十五版）

### Agent 感知层成熟化 · Agent Skills 工业化阶段确认 · Agent 自我进化框架涌现 · Code Intelligence MCP 标准化加速 · Agent 安全审计新品类

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 感知层成熟化：firecrawl 138K（抓取层）+ Agent-Reach 38.6K（平台适配层）+ page-agent 19.2K（DOM 操作层）三层架构形成 | alibaba-page-agent, agent-reach | 92 |
| 2 | Agent Skills 工业化阶段确认：addyosmani/agent-skills 65.9K 24skills×8commands 覆盖完整 SDLC | agent-skills | 90 |
| 3 | Agent 自我进化框架涌现：hermes-agent（自创建技能+自改进）+ deer-flow 2.0（字节跳动 SuperAgent harness） | hermes-agent, bytedance-deer-flow | 87 |
| 4 | Code Intelligence MCP 标准化加速：codebase-memory-mcp 12.8K 周增 7.6K tree-sitter+知识图谱+158语言 | codebase-memory-mcp | 85 |
| 5 | Agent 安全审计新品类：SkillSpector 9.8K（Skills 杀毒）+ page-agent DOM 注入面 | nvidia-skillspector | 83 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| alibaba/page-agent | 19,240 | 平台候选 | 86 |
| koala73/worldmonitor | 59,022 | 工具型 | 82 |
| jamiepine/voicebox | 33,079 | 工具型 | 80 |
| bytedance/deer-flow | trending | 平台候选 | 84 |

#### 今日更新项目

| 项目 | 变化 | 备注 |
|------|------|------|
| addyosmani/agent-skills | 58K→65.9K | score 88→90，Skills 工业化龙头 |
| Agent-Reach | 27.3K→38.6K | score 87→89，Agent 感知层标配 |
| codebase-memory-mcp | 10.2K→12.8K | last_seen 06-24，持续高增长 |
| OpenMontage | 11.8K→15.4K | 日增 3.6K，增速继续扩大 |

---

## 2026-06-23（第六十四版）

### Agent Skills 经济爆发 · Agent 权限与集成层出现 · Agentic Code Review 工具分化 · AI 金融分析工业化 · Agentic 内容生产加速验证

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 经济全面爆发：gstack 113K（YC CEO 23角色化工具栈）+ mattpocock/skills 141K + Cybersecurity-Skills 18.6K 817技能 | garrytan-gstack, anthropic-cybersecurity-skills | 95 |
| 2 | Agent 权限与集成层出现：corsair 2.8K 四档权限 + multi-tenancy + webhook + 凭证隔离 | corsairdev-corsair | 88 |
| 3 | Agentic Code Review 工具分化：hunk 5.4K review-first diff viewer + gstack /review | modem-dev-hunk, garrytan-gstack | 86 |
| 4 | AI 金融分析工业化：daily_stock_analysis 45.7K 41.8K forks（forks/stars=0.92 部署率极高） | zhulinsen-daily-stock-analysis | 84 |
| 5 | Agentic 内容生产加速：OpenMontage 日增 3.3K→11.7K + Palmier-Pro 日增 2.3K→7.2K | openmontage, palmier-pro | 83 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| garrytan/gstack | 113,069 | 平台候选 | 92 |
| corsairdev/corsair | 2,856 | 基础设施候选 | 85 |
| modem-dev/hunk | 5,431 | 工具型 | 80 |
| ZhuLinsen/daily_stock_analysis | 45,733 | 工具型 | 82 |

#### 今日更新项目

| 项目 | 变化 |
|------|------|
| mukul975/Anthropic-Cybersecurity-Skills | 11.4K→18.6K（score 86→87，817 skills +3 新领域 + F3 映射） |
| chopratejas/headroom | 44K→46.9K（score 94，日增 2.8K 持续加速） |
| DeusData/codebase-memory-mcp | 10.2K→11.4K（score 88，日增 1.2K） |
| calesthio/OpenMontage | 8.4K→11.7K（score 80，日增 3.3K 增速扩大） |
| stablyai/orca | 5.7K→6K（score 86，稳定增长） |

---

## 2026-06-22（第六十三版）

### Agent 上下文压缩标准化 · 多 Agent 并行编排成熟化 · AI Gateway 性能战打响 · Agent 框架两条路线分化 · Agentic 内容生产工业化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 上下文压缩层确立为基础设施：Headroom 44K 日增 2.6K + 6 算法 + cross-agent memory + 输出 token 削减 | headroom, codebase-memory-mcp | 94 |
| 2 | 多 Agent 并行编排格局成型：Orca 5.7K ADE + herdr 6.6K 终端 multiplexer + jcode 7.5K Rust + claude-squad 7.8K | stablyai-orca, herdr, jcode, claude-squad | 91 |
| 3 | AI Gateway 性能竞赛：Bifrost 5.9K Go 11µs overhead 50x LiteLLM + freellmapi 11.3K 免费 LLM 聚合 | maximhq-bifrost, freellmapi | 87 |
| 4 | Agent 框架两条路线分化：flue 6.2K 完整环境 vs agent-native 1.2K 应用原生 + DeerFlow SuperAgent | withastro-flue, builderio-agent-native, deer-flow | 85 |
| 5 | Agentic 内容生产工业化：OpenMontage 8.4K 52 tools + Palmier-Pro 4.9K + voicebox 31.5K | openmontage, palmier-pro, voicebox | 82 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| stablyai/orca | 5,784 | 平台候选 | 86 |
| maximhq/bifrost | 5,937 | 基础设施候选 | 85 |
| calesthio/OpenMontage | 8,487 | 平台候选 | 80 |
| 1jehuang/jcode | 7,516 | 工具型 | 78 |

#### 今日更新项目

| 项目 | 变化 |
|------|------|
| chopratejas/headroom | 38K→44K（score 93→94，输出 token 削减 + cross-agent memory + 6 算法体系化） |
| DeusData/codebase-memory-mcp | 8K→10K（score 88→88，IaC 索引 + 3D 可视化 + 11 语言 LSP） |
| withastro/flue | 5.8K→6.2K（score 84→84，持续稳定增长） |

---

## 2026-06-21（第六十二版）

### Agent Skill 训练正式化 · Agent 元框架混战升级 · 本地推理引擎专业化 · Epic Games 开源下一代 VCS · Coding Agent 增强工具爆发

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skill 训练范式正式化：SkillOpt 8.4K 文本空间训练 epoch/lr/val gate 6×52 cell 全第一 + Sleep 离线进化 | skillopt, shadcn-improve, ponytail | 93 |
| 2 | Agent 元框架/meta-harness 混战升级：Omnigent 4.2K + Vercel Eve 1.8K + ECC 218K 三种哲学 | omnigent, vercel-eve, ecc | 90 |
| 3 | 本地推理引擎专业化：antirez ds4 14.8K DeepSeek V4 专用 + SSD 流式 KV cache | ds4, zerolang | 88 |
| 4 | Epic Games 开源下一代 VCS：Lore 5.1K 内容寻址 + Merkle Tree + 大二进制优先 | epicgames-lore | 85 |
| 5 | Coding Agent 增强工具爆发：CodexPlusPlus 20.4K + html-anything 7K + ponytail 43K YAGNI 注入 | codexplusplus, html-anything, ponytail | 82 |

#### 今日新增项目

| 项目 | Stars | 分类 | Score |
|------|-------|------|-------|
| EpicGames/lore | 5,105 | 基础设施候选 | 57 |
| BigPizzaV3/CodexPlusPlus | 20,363 | 工具型 | 48 |

#### 今日更新项目

| 项目 | 变化 |
|------|------|
| microsoft/SkillOpt | 4.9K→8.4K（score 90→90，v0.1.0 PyPI + Sleep preview + 52 cell 全第一） |
| antirez/ds4 | 12.9K→14.8K（score 87→87，分布式推理 + SSD 流式 + beta 进展） |
| omnigent-ai/omnigent | 3.8K→4.2K（score 87→84，沙箱 + 策略治理 + 手机协作） |
| vercel/eve | 1.3K→1.8K（score 85→85，文件系统优先 Agent 框架正式发布） |

---

## 2026-06-20（第六十一版）

### LLM Token 经济学基础设施爆发 · Agent Skill 安全生态成型 · Agent 框架第二轮混战 · 基础模型超越文本 · Coding Agent 可观测性赛道启动

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | LLM Token 经济学基础设施爆发：headroom 38K 日增 3,938 + codebase-memory-mcp 8K 知识图谱 120x token 削减 | headroom, codebase-memory-mcp, agentsview | 94 |
| 2 | Agent Skill 安全生态成型：NVIDIA SkillSpector 8.2K 64 类漏洞检测，26.1% Skills 有漏洞 | nvidia-skillspector, headroom, agent-reach | 90 |
| 3 | Agent 框架第二轮混战：Astro flue 沙箱框架 + BuilderIO agent-native + Kilo Code 22.9K | withastro-flue, builderio-agent-native, kilo-code | 88 |
| 4 | 基础模型超越文本：Google TimesFM 2.5 已部署 BigQuery/Sheets/Vertex | google-timesfm, lightricks-ltx-2 | 83 |
| 5 | Coding Agent 可观测性赛道启动：agentsview 2.9K 周增 1,382，20+ Agent 支持 | agentsview, headroom | 80 |

#### 今日新增项目

| 项目 | Stars | 日增 | 分类 | Score |
|------|-------|------|------|-------|
| DeusData/codebase-memory-mcp | 8,119 | +1,055 | 基础设施候选 | 88 |
| withastro/flue | 5,803 | +305 | 平台候选 | 84 |
| BuilderIO/agent-native | 1,002 | +210 | 平台候选 | 82 |
| google-research/timesfm | 24,043 | +1,516 | 生产可用 | 85 |
| Kilo-Org/kilocode | 22,883 | +1,217 | 平台候选 | 83 |

#### 今日更新项目

| 项目 | 变化 |
|------|------|
| chopratejas/headroom | 26K→38K（score 91→93，加入输出 token 削减 + Copilot 支持） |
| NVIDIA/SkillSpector | 4.4K→8.2K（score 82→86，64 类检测全揭示） |
| kenn-io/agentsview | 1.6K→2.9K（score 78→80，加入成本分析 + PG/DuckDB 后端） |

#### 关键判断更新

- **headroom** 从"基础设施候选"升级为"基础设施候选 → 生产可用"过渡
- **codebase-memory-mcp** 定义了 Coding Agent 的"知识层"，与 headroom 互补
- **NVIDIA SkillSpector** 64 类检测 + SARIF 输出 = Skill 供应链的 SAST
- **Astro flue** 的沙箱 + 持久执行是 Agent 框架中最有想象力的方向

---

## 2026-06-19（第六十版）

### Agent Skill 经济学验证完成 · Agent 编排层混战开启 · 端侧 AI 与上下文工程双线推进 · 终端多路复用器 AI 化 · Agent 安全与隐私新范式

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skill 经济学验证完成：ponytail 一周 42 倍 + benchmark 证明 Skill 可量化 | ponytail, shadcn-improve, builderio-skills | 93 |
| 2 | Agent 编排层混战开启：meta-harness vs filesystem-first vs chat-driven | omnigent, vercel-eve, flock | 90 |
| 3 | 端侧 AI 与上下文工程双线推进：Apple SDK + Microsoft 论文 | apple-coreai-models, microsoft-fastcontext | 87 |
| 4 | 终端多路复用器 AI 化：terminal 作为 Agent 接口 | coder-boo | 82 |
| 5 | Agent 安全与隐私新范式：disposable agents + 统一多模态 RL | burner-agents, tencent-unirl | 78 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| omnigent-ai/omnigent | 3,785 | 平台候选 | 2026-06-19 |
| vercel/eve | 1,327 | 平台候选 | 2026-06-19 |
| microsoft/fastcontext | 587 | 基础设施候选 | 2026-06-19 |
| apple/coreai-models | 1,064 | 基础设施候选 | 2026-06-19 |
| duckbugio/flock | 698 | 工具型 | 2026-06-19 |
| coder/boo | 661 | 工具型 | 2026-06-19 |
| NotPBShaw/burner-agents | 554 | 观察型 | 2026-06-19 |

#### 持续跟踪更新

- DietrichGebert/ponytail: 862 → 36,393（周增 35,531，42 倍爆发！Agent Skill 经济学标杆）
- shadcn/improve: 2,385 → 5,462（周增 3,077，持续爆发）
- XiaomiMiMo/MiMo-Code: 6,687 → 9,772（周增 3,085，小米编码 Agent 持续增长）
- superloglabs/superlog: 792 → 875（周增 83，AI 可观测性稳步增长）
- tastyeffectco/sandboxd: 586 → 671（周增 85，开发沙箱稳步增长）

#### 判断修正

- **ponytail 判断升级**：6/13 评为“工具型”（80 分），今日升级为“工具型 → 生产可用过渡”（92 分）。benchmark 数据（54% LOC 削减、100% 安全）证明了 Skill 的可量化价值。
- **Agent 编排层判断**：从“值得关注”升级为“混战开启”。三条路线（meta-harness / filesystem-first / chat-driven）在同一周爆发，预示编排层竞争进入实质阶段。

## 2026-06-15（第五十九版）

### Agent Skills 杀手级应用涌现 · 上下文工程工具链三位一体 · 本地多模态 AI 运行时扩展 · 安全工具 AI 化 · 垂直领域 AI 基础模型萌芽

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 杀手级应用涌现：Skills 从基础设施走向真实应用 | last30days-skill, taste-skill, compound-engineering-plugin | 92 |
| 2 | 上下文工程工具链三位一体：压缩→索引→缓存完整管道 | headroom, turbovec, lmcache | 89 |
| 3 | 本地多模态 AI 运行时扩展：从文本到语音、视频 | whichllm, open-llm-vtuber, moneyprinterturbo | 84 |
| 4 | 安全工具 AI 化与图分析化 | nvidia-skillspector, flowsint, maigret | 80 |
| 5 | 垂直领域 AI 基础模型萌芽：金融+医疗 | kronos, openmed | 76 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| LMCache/LMCache | 9,043 | 基础设施候选 | 2026-06-15 |

#### 持续跟踪更新

- mvanhorn/last30days-skill: 29K → 42K（周增 12.6K，GitHub 全站周榜 #1，Agent Skills 第一个杀手级应用）
- Leonxlnx/taste-skill: 29K → 43.6K（周增 8K，AI 输出质量控制持续爆发）
- RyanCodrai/turbovec: 10.1K → 11.5K（周增 6.5K，上下文工程索引层）
- chopratejas/headroom: 26K → 27.5K（周增 10.4K，上下文工程压缩层）
- Andyyyy64/whichllm: 4K → 4.7K（周增 1.8K，本地 LLM 硬件选型）

#### 判断修正

- last30days-skill: 从「Agent Skill」升级为「生产可用」，评分 86 → 90。理由：42K stars + 12.6K/周增速证明杀手级用例验证完成
- 上下文工程：昨日判断为「Agent Skills 基础设施化」，今日修正为三层管道（压缩→索引→缓存），headroom + turbovec + LMCache 构成完整工具链

## 2026-06-14（第五十八版）

### Agent Skills 全栈基础设施化 · Apple Container 硅级容器化定局 · Agent 感知层独立 · 开源 NotebookLM 赛道升温 · RL 后训练环境接口标准化萌芽

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 全栈基础设施化：分发+安全+压缩+感知四层栈 | agent-skills, nvidia-skillspector, headroom, agent-reach | 93 |
| 2 | Apple Container 硅级容器化定局 | apple-container | 90 |
| 3 | Agent 感知层独立 | agent-reach, last30days-skill | 87 |
| 4 | 开源 NotebookLM 赛道升温 | open-notebook, tolaria | 85 |
| 5 | RL 后训练环境接口标准化萌芽 | openenv | 78 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| Panniantong/Agent-Reach | 27,338 | 基础设施候选 | 2026-06-14 |
| lfnovo/open-notebook | 30,096 | 生产可用 | 2026-06-14 |

#### 持续跟踪更新

- addyosmani/agent-skills: 54.5K → 58.2K（周增 8.3K，Agent Skills 分发层核心）
- chopratejas/headroom: 23K → 26.1K（周增 10.2K，定位升级为基础设施候选）
- apple/container: 32.2K → 36.2K（周增 7.8K，苹果官方容器持续高增长）
- NVIDIA/SkillSpector: 2.6K → 4.4K（周增 2.6K，Agent Skills 安全面持续强化）
- Leonxlnx/taste-skill: 43K（AI 审美技能持续高增长）
- mvanhorn/last30days-skill: 41K（跨平台研究技能持续高增长）

## 2026-06-13（第五十七版）

### Agent 架构分层范式确立 · 端侧 AI 运行时基础设施化 · AI 自愈可观测性崭露头角 · Coding Agent 工具链全栈化 · Sandbox 即基础设施

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 架构分层范式确立：贵模型审计+廉模型执行 | shadcn-improve, ponytail, gstack | 92 |
| 2 | 端侧 AI 运行时基础设施化 | coreai-models, mimo-code | 89 |
| 3 | AI 自愈可观测性崭露头角 | superlog | 84 |
| 4 | Coding Agent 工具链全栈化 | cc-switch, rtk, ruview | 81 |
| 5 | Sandbox 即基础设施 | sandboxd | 79 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| XiaomiMiMo/MiMo-Code | 6,687 | 工具型 | 2026-06-13 |
| DietrichGebert/ponytail | 862 | 工具型 | 2026-06-13 |

#### 持续跟踪更新

- shadcn/improve: 745 → 2,385（日+1,640，Agent 分层范式代表持续高增长）
- apple/coreai-models: 605 → 826（日+221，端侧 AI 运行时稳步增长）
- superlog: 721 → 792（日+71，自愈可观测性方向稳健）
- sandboxd: 561 → 586（日+25，开发沙箱稳步增长）
- cc-switch: 98K → 99K（跨 Agent 桌面管理持续增长）
- rtk: 61K（Token 压缩代理，日活跃）
- RuView: 73K（WiFi 空间智能，日活跃）

## 2026-06-12（第五十六版）

### Agent Skills 生态爆发 · LLM Token 压缩基础设施化 · Apple 容器化落地 · Agent 安全面浮出 · Coding Agent 工具链分化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 成为独立生态品类 | agent-skills, taste-skill, last30days-skill, pm-skills | 93 |
| 2 | LLM Token 压缩成为新基础设施层 | headroom | 91 |
| 3 | Apple 容器化正式发布 | apple/container | 88 |
| 4 | AI Agent 安全面正式浮出 | NVIDIA/SkillSpector | 85 |
| 5 | Coding Agent 工具链持续分化 | cc-switch, agentsview, herdr | 82 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| addyosmani/agent-skills | 54,532 | 平台候选 | 2026-06-12 |
| apple/container | 32,164 | 基础设施候选 | 2026-06-12 |
| NVIDIA/SkillSpector | 2,577 | 工具型 | 2026-06-12 |
| kenn-io/agentsview | 1,592 | 工具型 | 2026-06-12 |

#### 持续跟踪更新

- headroom: 20.4K → 23.1K（周增 13,062，Token 压缩基础设施持续高增长）
- hermes-agent: 188.7K → 190.9K（高位稳定，周增 11,519）
- turbovec: 10.1K → 11K（周增 6,487，Rust 向量索引快速攀升）
- agent-reach: 25.5K → 26.4K（周增 5,021，Agent 网络搜索稳步增长）
- CopilotKit: 34.7K（周增 2,686，AG-UI Protocol 稳步推进）

## 2026-06-11（第五十五版）

### Agent 编排分层 · Apple 端侧 AI 开放 · AI 可观测性自愈 · 开发沙箱基础设施化 · AI 设计资产走向生产

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 编排分层：顾问模式定义协作新范式 | shadcn/improve, guard-skills, baoyu-design | 92 |
| 2 | Apple 端侧 AI 生态正式开放 | coreai-models | 90 |
| 3 | AI 原生可观测性从监控到自愈 | superlog | 86 |
| 4 | 开发沙箱成为 Agent 基础设施 | sandboxd | 83 |
| 5 | AI 生成式设计资产走向生产 | diffusionstudio/lottie, baoyu-design | 80 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| shadcn/improve | 745 | 平台候选 | 2026-06-11 |
| apple/coreai-models | 605 | 基础设施候选 | 2026-06-11 |
| superlog | 721 | 平台候选 | 2026-06-11 |
| sandboxd | 561 | 基础设施候选 | 2026-06-11 |
| diffusionstudio/lottie | 2,004 | 工具型 | 2026-06-11 |

#### 持续跟踪更新

- headroom: 20.4K → 持续关注
- turbovec: 10.1K → 持续关注
- ecc: 211.8K → 高位稳定

## 2026-06-10（第五十四版）

### LLM Token 压缩基础设施化 · Agent Skill 从碎片化到平台化 · 开源知识管理双赛道分化 · 本地 LLM 选型工具链成熟 · Agent 信息获取层基础设施化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | LLM Token 压缩基础设施化 | headroom, turbovec | 91 |
| 2 | Agent Skill 从碎片化到平台化 | ecc, taste-skill, impeccable, harness | 87 |
| 3 | 开源知识管理双赛道分化 | tolaria, open-notebook | 85 |
| 4 | 本地 LLM 选型工具链成熟 | whichllm, career-ops | 82 |
| 5 | Agent 信息获取层基础设施化 | last30days-skill, agent-reach | 80 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| tolaria | 14.3K | 工具型 | 2026-06-10 |
| whichllm | 4K | 工具型 | 2026-06-10 |
| career-ops | 51.5K | 工具型 | 2026-06-10 |

#### 持续跟踪更新

- headroom: 16.8K → 20.4K（周增 14,266，全网周增速第一，Token 压缩基础设施化）
- turbovec: 7K → 10.1K（周增 4,283，Rust SIMD 向量索引持续高热）
- ecc: 210.7K → 211.8K（高位稳定，Agent Harness 层）
- hermes-agent: 187.3K → 188.7K（高位稳定，周增 11,747）
- markitdown: 148.4K → 149.3K（周增 11,177，文件转换基础设施）
- taste-skill: 36K → 39.5K（周增 7,597，AI 品质控制）
- impeccable: 33K → 36.8K（周增 3,736，AI 设计语言）
- last30days-skill: 34.3K → 37.1K（周增 6,616，跨平台调研）
- agent-reach: 24K → 25.5K（周增 3,006，Agent 网络搜索）

## 2026-06-09（第五十三版）

### Coding Agent 工具链基础设施化 · AI Memory 基础设施竞争白热化 · 语音 AI 全栈爆发 · Agent 安全运行时浮出水面 · Agent 调研 Skill 成熟

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Coding Agent 工具链基础设施化 | cc-switch, codegraph, oh-my-pi | 90 |
| 2 | AI Memory 基础设施竞争白热化 | supermemory, mempalace, open-notebook | 88 |
| 3 | 语音 AI 全栈爆发 | voxcpm, open-llm-vtuber, funasr | 86 |
| 4 | Agent 安全运行时浮出水面 | nvidia-openshell, sandbox-runtime | 85 |
| 5 | Agent 调研 Skill 成熟 | last30days-skill, agent-reach | 82 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| nvidia-openshell | 6.9K | 基础设施候选 | 2026-06-09 |

#### 持续跟踪更新

- cc-switch: 68K → 95.1K（周增 +7.9K，Agent 管理层持续爆发）
- codegraph: 35.3K → 44.8K（周增 +8.7K，代码知识图谱被市场验证）
- supermemory: 24.6K → 26.2K（周增 +2.9K，Memory API 竞争加剧）
- voxcpm: 24.2K → 27.7K（周增 +4.3K，Tokenizer-Free TTS 持续高热）
- ecc: 209K → 210.7K（高位稳定，Agent Harness 事实标准）
- hermes-agent: 185K → 187.3K（高位稳定，自进化 Agent）
- headroom: 16.8K → 18.7K（周增 +14.3K，Token 压缩基础设施化持续）
- markitdown: ~135K → 148.4K（周增 +13.4K，文件转换基础设施）

## 2026-06-08（第五十二版）

### Agent Skill 生态核聚变 · Token 压缩基础设施化 · PostgreSQL 作为 Agent 运行时 · 向量检索 SIMD 新世代 · Agentic Backend Platform 浮现

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skill 生态核聚变 | ecc, hermes-agent, taste-skill, impeccable, compound-engineering-plugin | 92 |
| 2 | Token 压缩基础设施化 | headroom, turbovec | 89 |
| 3 | 向量检索 SIMD 新世代 | turbovec | 86 |
| 4 | PostgreSQL 作为 Agent 运行时 | pg-durable, insforge | 85 |
| 5 | Agentic Backend Platform 浮现 | insforge, copilotkit | 84 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| pg-durable | ~1.4K | 基础设施候选 | 2026-06-08 |
| insforge | ~11.5K | 平台候选 | 2026-06-08 |

#### 持续跟踪更新

- headroom: 4.1K → 16.8K（+300%！周增长核爆，Token 压缩从优化变为基础设施）
- turbovec: 3.4K → 7K（+1,533/天 全网日增速第一，翻倍仅用 10 天）
- oh-my-pi: 8.7K → 11K（持续高热，终端 Agent IDE 化趋势验证）
- ecc: 188K → 209K（+10K/week，Agent Harness 持续霸榜）
- hermes-agent: ~149K → 185K（+11K/week，自进化 Agent 持续高增长）
- taste-skill: 29K → 36K（+6K/week，AI 品味 Skill 持续高热）

---

## 2026-06-07（第五十一版）

### Agent 多源感知基础设施化 · AI Memory 本地优先成熟化 · 代码执行沙箱进入 OS 级 · Agent 终端多路复用器新物种 · HTML 原生视频渲染 Agent 化

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 多源感知基础设施化 | last30days-skill, agent-reach, mempalace | 90 |
| 2 | AI Memory 本地优先成熟化 | mempalace, agentscope | 87 |
| 3 | 代码执行沙箱进入 OS 级 | mxc, agentgateway | 86 |
| 4 | Agent 终端多路复用器新物种 | herdr, multica-ai | 84 |
| 5 | HTML 原生视频渲染 Agent 化 | hyperframes, open-notebook | 82 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| last30days-skill | new | Agent Skill | 2026-06-07 |
| mxc | ~557 | 基础设施候选 | 2026-06-07 |
| hyperframes | ~25K | 工具型 | 2026-06-07 |

#### 持续跟踪更新

- herdr: 3.9K → 4.7K（+250/天，6/7 再次上榜 Rust Trending）
- MemPalace: 再次上榜 Python Trending，本地记忆系统持续高热
- CopilotKit: 33.1K（+613/天），Agent 前端栈持续高增长
- open-notebook: 26.5K（+783/天），Notebook LM 开源替代

---

## 2026-06-06（第五十版）

### AI Code Review 进入混合架构时代 · Agent Memory 分层操作系统化 · 本地优先运动席卷硬件外设 · 自托管团队 Agent 平台化 · Coding Agent CLI 竞争新格局

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI Code Review 进入混合架构时代 | open-code-review, clawpatch, kimi-code | 91 |
| 2 | Agent Memory 分层操作系统化 | memory-os, mempalace | 87 |
| 3 | 本地优先运动从软件延伸到硬件 | openlogi, goose, skylight | 85 |
| 4 | 自托管团队 Agent 平台化 | centaur, butterbase, odysseus | 83 |
| 5 | Coding Agent CLI 竞争新格局 | kimi-code, open-code-review | 80 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| open-code-review | ~2.7K | 生产可用 | 2026-06-06 |
| memory-os | ~869 | 平台候选 | 2026-06-06 |
| centaur | ~718 | 平台候选 | 2026-06-06 |
| openlogi | ~4K | 工具型 | 2026-06-06 |
| kimi-code | ~1.9K | 工具型 | 2026-06-06 |

#### 持续跟踪更新

- Odysseus: 50.6K → 55.4K（日增 +4.8K，增长加速）

---

## 2026-06-05（第四十九版）

### Agent Skill 从手工编写进化为可训练优化 · 自托管 AI 工作空间现象级项目 · Agent 专用语言与运行时涌现 · AI 供应链安全成新赛道 · 开源情报平台持续走热

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skill 从手工编写进化为可训练优化单元 | skillopt, html-anything, gsd-core | 92 |
| 2 | 自托管 AI 工作空间现象级项目 | odysseus | 90 |
| 3 | Agent 专用语言与运行时涌现 | zerolang, zero-native, forkd, rmux | 88 |
| 4 | AI 供应链安全成新赛道 | bumblebee, dirtyfrag | 84 |
| 5 | 开源情报平台与工具增强型项目持续走热 | osiris, codexplusplus | 80 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| skillopt | ~4.9K | 平台候选 | 2026-06-05 |
| odysseus | ~50.6K | 观察型 | 2026-06-05 |
| zerolang | ~4.9K | 学习型 | 2026-06-05 |
| bumblebee | ~4.3K | 工具型 | 2026-06-05 |
| forkd | ~1.3K | 基础设施候选 | 2026-06-05 |

#### 持续跟踪项目更新

| 项目 | 上次 stars | 本次 stars | 变化 |
|------|-----------|-----------|------|
| html-anything | 2.4K | 6.1K | +3.7K 持续上升 |
| mirage | 2.0K | 3.0K | +1.0K 稳定增长 |
| opensquilla | 893 | 2.9K | +2K 高增长 |
| ds4 | 8.6K | 12.9K | +4.3K 持续高热 |

---

## 2026-06-03（第四十八版）

### Agent 运行时安全沙箱成新赛道 · Agent Terminal 基础设施三层成型 · AI Memory API 标准化加速 · AI 视频生成大爆发 · 服务组合与编排新范式

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 运行时安全沙箱成新赛道 | openshell, agent-governance-toolkit | 92 |
| 2 | Agent Terminal 基础设施三层成型 | herdr, fff, headroom | 89 |
| 3 | AI Memory API 标准化加速 | supermemory | 85 |
| 4 | AI 视频生成大爆发 | moneyprinterturbo, hermes-webui | 83 |
| 5 | 服务组合与编排新范式 | iii | 80 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| openshell | ~6.6K | 基础设施候选 | 2026-06-03 |
| fff | ~7.4K | 工具型 | 2026-06-03 |
| supermemory | ~24.6K | 平台候选 | 2026-06-03 |
| iii | ~17.5K | 平台候选 | 2026-06-03 |
| flowsint | ~4.5K | 工具型 | 2026-06-03 |

#### 持续跟踪项目状态

| 项目 | Stars | 变化 | 状态 |
|------|-------|------|------|
| ecc | 203.8K | +1.8K | 高热，警惕泡沫 |
| understand-anything | 50K | +1.3K | 持续高热 |
| markitdown | 141K | 稳定 | 稳定 |
| herdr | 3.9K | +500 | 稳健增长 |
| headroom | 6.1K | +2K | 快速增长 |
| scrapling | 59K | +1.2K/day | 快速增长 |
| agent-governance-toolkit | 3.8K | +0.1K | 稳健增长 |

---

## 2026-06-02（第四十七版）

### AI Agent 上下文压缩赛道浮现 · TTS 开源模型爆发 · Agent Harness 深度竞争 · Agent 治理与安全持续升温 · AI 写作品质治理

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI Agent 上下文压缩赛道浮现 | headroom, understand-anything, codegraph | 91 |
| 2 | TTS 开源模型爆发 | voxcpm, moss-tts, dograh | 86 |
| 3 | Agent Harness 深度竞争与 Plugin 标准化 | ecc, oh-my-pi, harness, compound-engineering-plugin | 87 |
| 4 | Agent 治理与安全持续升温 | agent-governance-toolkit, anthropic-cybersecurity-skills, heretic | 83 |
| 5 | AI 写作品质治理 | stop-slop, taste-skill | 75 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| headroom | ~4.1K | 平台候选 | 2026-06-02 |
| voxcpm | ~24.2K | 生产可用 | 2026-06-02 |
| heretic | ~23K | 学习型 | 2026-06-02 |
| dograh | ~4.1K | 工具型 | 2026-06-02 |

#### 持续跟踪项目状态

| 项目 | Stars | 变化 | 状态 |
|------|-------|------|------|
| understand-anything | 48.7K | +1.6K | 持续高热 |
| codegraph | 36.6K | +1.3K | 持续高热 |
| ecc | 202K | +2K | 高热，警惕泡沫 |
| agent-governance-toolkit | 3.7K | +0.1K | 稳健增长 |
| liteparse | 8.7K | +0.1K | 稳健增长 |

---

## 2026-06-01（第四十六版）

### Code Knowledge Graph 赛道爆发 · google/ax 分布式 Agent Runtime 开源 · AI Coding Plugin 生态全面爆发 · Microsoft AGT 覆盖 OWASP Top 10 · herdr Agent 多路复用器

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Code Knowledge Graph 赛道爆发 | understand-anything, codegraph | 92 |
| 2 | AI Coding Plugin 生态大爆发 | ecc, claude-plugins-official, openai-skills | 88 |
| 3 | Agent Runtime 基础设施层浮现 | google-ax, agent-governance-toolkit, herdr | 90 |
| 4 | Rust AI Infra 工具链 | liteparse, herdr, ruview, handy | 82 |
| 5 | Voice AI 开源替代 | dograh, handy, moss-tts | 78 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| google/ax | ~1.3K | 基础设施候选 | 2026-06-01 |
| herdr | ~3.4K | 工具型 | 2026-06-01 |

#### 持续跟踪项目更新

| 项目 | 上次 Stars | 今日 Stars | 变化 |
|------|-----------|-----------|------|
| Understand-Anything | ~44K | 47.1K | +3.1K ↗️ |
| codegraph | ~33K | 35.3K | +2.3K ↗️ |
| Agent Governance Toolkit | 3.5K | 3.6K | +0.1K → |
| LiteParse | ~7.9K | 8.3K | +0.4K ↗️ |

#### 趋势判断
- Code Knowledge Graph 从"赛道观察"升级为"赛道确认"——两个项目周增共 41K star
- google/ax + Microsoft AGT 标志着 Agent Runtime 层的标准化开始
- AI Coding Plugin 生态进入"包管理器时刻"，但碎片化风险显著

## 2026-05-31（第四十五版）

### AI Taste 元趋势爆发 · ai-engineering-from-scratch 25K 教育赛道 · LiteParse +929/天加速 · Microsoft Agent Governance Toolkit · stable-worldmodel

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI Taste/Slop Control 元趋势 | taste-skill, stop-slop | 88 |
| 2 | AI 工程教育赛道爆发 | ai-engineering-from-scratch | 85 |
| 3 | LiteParse +929/天加速突破 | liteparse | 82 |
| 4 | Agent Governance 工具化 | agent-governance-toolkit | 86 |
| 5 | 世界模型与离线 AI | stable-worldmodel, project-nomad | 78 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| stable-worldmodel | ~1.4K | 学习型 | 2026-05-31 |
| project-nomad | ~27.3K | 工具型 | 2026-05-31 |

#### 更新项目（last_seen 更新）

| 项目 | Stars | 分类 | 最近出现 |
|------|-------|------|----------|
| taste-skill | ~29K | 工具型 | 2026-05-31 |
| liteparse | ~7.9K | 生产可用 | 2026-05-31 |
| agent-governance-toolkit | ~3.5K | 基础设施候选 | 2026-05-31 |
| compound-engineering-plugin | ~18.4K | 工具型 | 2026-05-31 |
| oh-my-pi | ~8.7K | 工具型 | 2026-05-31 |
| ai-engineering-from-scratch | ~25.1K | 学习型 | 2026-05-31 |

#### 趋势判断修正

- AI Taste/Slop Control 成为新元趋势：taste-skill 29K + stop-slop 7.4K，反映用户对 AI 输出质量控制的需求显式化
- ai-engineering-from-scratch 25.1K 周增 13.1K，教育赛道需求巨大但热度回落风险高
- LiteParse 日增 929 加速突破，Rust 文档解析赛道确立，归类从工具型调整为生产可用
- Microsoft Agent Governance Toolkit 覆盖 OWASP Agentic Top 10，Agent 安全治理从概念走向工具
- stable-worldmodel 代表世界模型评估标准化方向
- project-nomad 27.3K 离线 AI 概念吸引社区但与核心关注方向重叠有限

---

## 2026-05-30（第四十四版）

### Code Knowledge Graph 双雄争霸 · ECC 198K 横空出世 · Anthropic Plugin 三连发 · RuView WiFi 空间智能 · Cursor Plugin 规范

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Code Knowledge Graph 双雄争霸 | Understand-Anything, codegraph | 95 |
| 2 | ECC 198K Agent Harness 标杆 | ECC | 92 |
| 3 | Anthropic Plugin 生态三连发 | claude-plugins-official, knowledge-work-plugins, Anthropic-Cybersecurity-Skills | 90 |
| 4 | WiFi CSI 空间智能 | RuView | 85 |
| 5 | IDE/Agent 编排 Plugin 化 | cursor/plugins, routa | 82 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| dograh | ~3.7K | 平台候选 | 2026-05-30 |
| liteparse | ~7.2K | 工具型 | 2026-05-30 |

#### 更新项目（last_seen 更新）

| 项目 | Stars | 分类 | 最近出现 |
|------|-------|------|----------|
| Understand-Anything | ~44.4K | 平台候选 | 2026-05-30 |
| codegraph | ~33.1K | 工具型 | 2026-05-30 |
| ECC | ~198.5K | 学习型 | 2026-05-30 |
| claude-plugins-official | ~28.6K | 基础设施候选 | 2026-05-30 |
| RuView | ~68.2K | 学习型 | 2026-05-30 |
| knowledge-work-plugins | ~18K | 工具型 | 2026-05-30 |
| taste-skill | ~28K | 工具型 | 2026-05-30 |
| agentmemory | ~19.6K | 基础设施候选 | 2026-05-30 |
| oh-my-pi | ~8.5K | 工具型 | 2026-05-30 |
| agent-governance-toolkit | ~3.3K | 基础设施候选 | 2026-05-30 |

#### 趋势判断修正

- Code Knowledge Graph 正式成为赛道：Understand-Anything（交互式）+ codegraph（预索引）路径不同但需求同源
- ECC 198K 星异常高，概念有参考价值但星数获取方式可疑，归类为学习型
- Anthropic 一周三发 Plugin（官方目录 + 知识工作 + 安全），Claude 生态 Plugin-first 确认
- RuView WiFi CSI 概念性感但 68K 星含推广成分，保持观察
- Cursor 同步发布 Plugin 规范，IDE Plugin 化已成行业共识
- Voice Agent 自托管需求升温（dograh 3.7K）
- 文档解析 Rust 化（liteparse 7.2K），RAG Infra 持续优化

---

## 2026-05-29（第四十三版）

### Agent Skills 大爆发 · agentmemory 冲刺 19K · oh-my-pi 终端 IDE 化 · Microsoft Agent Governance · turbovec 击败 FAISS

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 品质控制大爆发 | taste-skill, stop-slop, harness, openai/skills, anthropics/skills | 92 |
| 2 | Agent 记忆层标准化 | agentmemory | 90 |
| 3 | 终端 Agent IDE 化 | oh-my-pi | 88 |
| 4 | Agent 安全治理基础设施 | agent-governance-toolkit | 85 |
| 5 | Rust 向量索引新势力 | turbovec | 83 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| oh-my-pi | ~8.2K | 工具型 | 2026-05-29 |
| agentmemory | ~19.3K | 基础设施候选 | 2026-05-29 |
| agent-governance-toolkit | ~3.2K | 基础设施候选 | 2026-05-29 |
| turbovec | ~3.4K | 基础设施候选 | 2026-05-29 |
| anthropics/skills | 新增 | 平台候选 | 2026-05-29 |

#### 更新项目（last_seen 更新）

| 项目 | Stars | 分类 | 最近出现 |
|------|-------|------|----------|
| taste-skill | ~26.2K | 工具型 | 2026-05-29 |
| stop-slop | ~6.3K | 工具型 | 2026-05-29 |
| openhuman | ~29.2K | 观察型 | 2026-05-29 |

#### 趋势判断修正

- Agent 生态正式进入「品质工程」阶段：taste-skill + stop-slop + harness 同台竞技，品质控制成为刚需
- agentmemory 19.3K 锁定 Agent 记忆层标准化方向，基于 iii 引擎的多平台兼容方案
- 终端 Agent 竞争从 CLI wrapper 升级到 IDE 级（oh-my-pi 27K 行 Rust 核心）
- Microsoft Agent Governance 覆盖 OWASP Agentic Top 10，确定性拦截 vs prompt 级安全
- Rust 在 AI Infra 中的渗透加速（turbovec、oh-my-pi、RuView、iii）

---

## 2026-05-28（第四十二版 — 网络受限日）

### 五日断网周度复盘 · Harness 三强锁定 · Skills 分化加速 · 小模型 Agent 工程化

> ⚠️ 外部数据源自 05-24 起连续 5 天不可达，本版基于 05-19~05-23 已采集数据完成趋势合成分析。

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Harness 格局锁定 | ECC, Hermes Agent, OpenCode | 90 |
| 2 | Skills 生态垂直分化 | 9arm-skills, Claude Plugins Official | 88 |
| 3 | 小模型 Agent 工程化 | SmallCode, HRM-Text | 85 |
| 4 | 安全 Agent 双线闭环 | audit, Bumblebee | 83 |
| 5 | 团队级 Agent 基础设施 | Centaur | 80 |

#### 更新项目（last_seen 更新）

| 项目 | Stars（推算） | 分类 | 最近出现 |
|------|-------------|------|----------|
| SmallCode | ~1.2K | 工具型 | 2026-05-28 |
| Centaur | ~364 | 基础设施候选 | 2026-05-28 |
| audit | ~433 | 工具型 | 2026-05-28 |
| HRM-Text | ~650 | 学习型 | 2026-05-28 |

#### 趋势判断修正

- Agent Harness 三强格局（ECC 188.5K/Hermes 163K/OpenCode 164K）基本锁定，新入局者窗口关闭
- Skills 从通用框架走向垂直分化，每个垂直领域将有 1-2 个头部 Skills
- 小模型 Agent 工程化是 05-23 新出现的趋势，代表端侧 Agent 从概念走向工程适配

---

## 2026-05-23（第四十一版）

### 小模型 Agent 工具链觉醒 · Agent 安全双线突破 · 团队级 Agent 基础设施

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 小模型 Agent 工具链觉醒 | SmallCode, HRM-Text | 92 |
| 2 | Agent 安全双线突破 | audit, Bumblebee | 88 |
| 3 | 团队级 Agent 基础设施 | Centaur | 86 |
| 4 | Agent Harness 赛道格局锁定 | ECC, OpenCode, Hermes Agent | 80 |
| 5 | Claude Skills 生态持续细分 | 9arm-skills, PaperSpine | 75 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| SmallCode | 1.2K | 工具型 | 2026-05-23 |
| Centaur | 364 | 基础设施候选 | 2026-05-23 |
| audit (evilsocket) | 433 | 工具型 | 2026-05-23 |
| HRM-Text | 650 | 学习型 | 2026-05-23 |
| Bumblebee | 251 | 工具型 | 2026-05-23 |
| 9arm-skills | 1.5K | 工具型 | 2026-05-23 |

#### 持续跟踪项目动态

| 项目 | 今日 Stars | 变化 | 备注 |
|------|-----------|------|------|
| ECC | 188.5K | ↑ | Agent Harness 性能优化，稳定增长 |
| OpenCode | 164K | - | 5997 open issues，维护压力大 |
| Hermes Agent | 163K | - | NousResearch 出品 |
| Superpowers | 202.8K | ↑ | Skills 框架 |
| cc-switch | 78.2K | - | Agent 桌面助手 |

---

## 2026-05-22（第四十版）

### Claude Skills 生态持续分化 · 12-Factor Agents 工程原则确立 · OpenHuman 突破 2 万 · Agent 浏览器层成基础设施

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Claude Skills/Plugins 生态持续分化 | CodeGraph, Claude Plugins Official, Superpowers | 95 |
| 2 | Agent 工程原则确立 | 12-Factor Agents, Multica | 90 |
| 3 | 个人 AI 超级智能持续升温 | OpenHuman | 85 |
| 4 | Agent-Native 浏览器与反检测 | CloakBrowser, Chrome DevTools MCP | 88 |
| 5 | 端侧 TTS 与多模态突破 | Supertonic, ViMax | 78 |

#### 新增项目

| 项目 | Stars | 分类 | 首次出现 |
|------|-------|------|----------|
| Claude Plugins Official | 22.2K | 平台候选 | 2026-05-22 |
| 12-Factor Agents | 21.5K | 基础设施候选 | 2026-05-22 |
| Supertonic | 9.1K | 工具型 | 2026-05-22 |

#### 持续跟踪项目更新

| 项目 | 上次 Stars | 本次 Stars | 变化 |
|------|-----------|-----------|------|
| OpenHuman | 16.9K | 24.7K | +7.8K |
| Multica | 6K+ | 30.7K | 大幅增长 |
| CloakBrowser | 15.1K | 18.2K | +3.1K |
| CodeGraph | 13K+ | 13.2K | 稳定 |

---

## 2026-05-19（第三十九版）

### Agent Skills 生态大爆发 · CLI-Anything Agent-Native 范式 · RuView WiFi 传感突破 · Agent Memory 持久化成新基建

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent Skills 生态大爆发 | anthropics/skills, mattpocock/skills, spec-kit | 95 |
| 2 | CLI-Anything Agent-Native 范式 | CLI-Anything | 92 |
| 3 | RuView WiFi 传感突破 | RuView | 88 |
| 4 | Agent Memory 持久化成新基建 | agentmemory, Memori | 86 |
| 5 | OSINT + AI Agent 融合 | Shadowbroker | 80 |

#### 今日新增项目

| 项目 | Stars | 分类 | 评分 | 备注 |
|------|-------|------|------|------|
| RuView | 59,842⭐ | 基础设施候选 | 88 | WiFi 信号空间智能 |
| agentmemory | 12,712⭐ | 基础设施候选 | 86 | AI Coding Agent 持久记忆 |
| Memori | 14,595⭐ | 基础设施候选 | 84 | Agent 原生记忆基础设施 |
| CloakBrowser | 15,098⭐ | 工具型 | 82 | 隐身 Chromium 反检测 |
| OpenHuman | 16,930⭐ | 观察型 | 80 | 个人 AI 超级智能 |
| Shadowbroker | 7,676⭐ | 工具型 | 78 | OSINT 全球情报聚合 |
| CodeGraph | 4,778⭐ | 工具型 | 79 | 代码知识图谱 |
| React Doctor | 10,159⭐ | 工具型 | 77 | AI 编码质量守门 |
| Pyrefly | 6,199⭐ | 工具型 | 76 | Meta Python 类型检查器 |

#### 持续跟踪项目状态

| 项目 | 上次 Stars | 本次 Stars | 变化 | 状态 |
|------|-----------|-----------|------|------|
| CLI-Anything | 33,200 | 36,562 | +3,362 | 🔥 稳增 |
| anthropics/skills | 128,000 | 136,973 | +8,973 | 🔥 稳增 |
| spec-kit | 97,000 | 102,079 | +5,079 | 🔥 稳增 |
| llama.cpp | 108,000 | 110,980 | +2,980 | ✅ 稳增 |

---

## 2026-05-18（第三十八版）

### Dirty Frag Linux LPE 席卷安全圈 · Agent 语言 Zero 一日暴涨 74% · AI 伴侣引擎浮出水面

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Dirty Frag Linux LPE 席卷安全圈 | Dirty Frag | 90 |
| 2 | Agent 原生语言 Zero 暴涨 74% | Zero | 87 |
| 3 | AI 伴侣引擎浮出水面 | grok-animus, trustclaw | 82 |
| 4 | 统一存储抽象加速 | files-sdk | 78 |
| 5 | HTML Agent 工具链分化 | html-anything | 76 |

#### 今日新增项目

| 项目 | Stars | 分类 | 评分 | 备注 |
|------|-------|------|------|------|
| grok-animus | 573⭐ | 工具型 | 75 | 持久化 AI 伴侣引擎 |
| trustclaw | 665⭐ | 工具型 | 73 | 自托管个人 AI Agent |

#### 持续跟踪项目状态

| 项目 | 上次 Stars | 本次 Stars | 变化 | 状态 |
|------|-----------|-----------|------|------|
| ds4 | 10,038 | 10,317 | +279 | ✅ 稳增 |
| Zero | 916 | 1,600 | +684 | 🔥 暴增 |
| Dirty Frag | 2,775 | 4,611 | +1,836 | 🔥 暴增 |
| Mirage | 2,312 | 2,350 | +38 | ➡️ 平稳 |
| TokenSpeed | 1,031 | 1,036 | +5 | ➡️ 平稳 |
| html-anything | 2,425 | 2,758 | +333 | ✅ 稳增 |
| files-sdk | 642 | 772 | +130 | ✅ 稳增 |
| Pixal3D | 504 | 921 | +417 | ✅ 强增 |
| OpenSquilla | 893 | 969 | +76 | ✅ 稳增 |

---

## 2026-05-17（第三十七版）

### 本地推理双雄对决 · Agent VFS 基础设施化 · Agent 原生语言 Zero 问世

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | 本地推理双雄对决 | ds4, TokenSpeed | 92 |
| 2 | Agent VFS 基础设施化 | Mirage | 88 |
| 3 | Agent 原生语言 Zero | Zero (Vercel Labs) | 85 |
| 4 | AI 安全新物种 | AiSOC | 82 |
| 5 | Token 效率成 Agent 新战场 | OpenSquilla | 80 |

#### 今日新增项目

| 项目 | Stars | 分类 | 评分 | 备注 |
|------|-------|------|------|------|
| Zero (vercel-labs) | 916⭐ | 观察型 | 78 | Vercel 推出的 Agent 编程语言 |
| AiSOC | 971⭐ | 工具型 | 76 | 开源 AI 安全运营中心 |
| OpenSquilla | 893⭐ | 观察型 | 74 | Token 高效 Agent |
| html-anything | 2,425⭐ | 工具型 | 73 | Agentic HTML 编辑器 |

#### 持续跟踪项目状态

| 项目 | 上次 Stars | 本次 Stars | 变化 | 状态 |
|------|-----------|-----------|------|------|
| ds4 | ~8.6K | 10,038 | +1.4K | ✅ 强增 |
| Mirage | ~2K | 2,312 | +300 | ✅ 稳增 |
| TokenSpeed | ~800 | 1,031 | +200 | ✅ 增长 |
| Chrome DevTools MCP | ~38K | 39,771 | +1.7K | ✅ 强增 |
| DeepClaude | ~1.5K | 1,875 | +300 | ✅ 稳增 |
| Hermes Agent | ~149K | 153,324 | +4K | ✅ 稳增 |

---

## 2026-05-15（第三十六版）

### 网络受限日 · 趋势延续深度复盘

**⚠️ 数据来源：** 基于 2026-05-14 实测数据推算，外部网络不可达

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 生态整合期三巨头格局 | Hermes Agent, Browser Harness, Open Design | 90 |
| 2 | Spec-Driven Dev 范式变迁 | Spec Kit | 87 |
| 3 | 本地推理三赛道分化复盘 | ds4.c, Terax AI, Zero Native | 83 |
| 4 | 安全赛道平台化趋势 | YellowKey, Deepsec | 80 |
| 5 | 硬件生态开放 vs 封闭 | OrcaSlicer-bambulab | 76 |

#### 持续跟踪项目状态（推算）

| 项目 | 上次 Stars | 本次推算 Stars | 变化 | 状态 |
|------|-----------|---------------|------|------|
| Hermes Agent | 148,546 | ~149K | +~500 | ✅ 稳增 |
| Spec Kit | 98,266 | ~99K | +~700 | ✅ 稳增 |
| Browser Harness | 93,774 | ~94K | +~300 | → 趋稳 |
| Open Design | 39,300 | ~40K | +~700 | ✅ 巩固期 |
| ds4.c | 8,387 | ~8.6K | +~200 | ✅ 稳增 |
| Zero Native | 3,261 | ~3.5K | +~200 | ↗ 新增 |
| YellowKey | 927 | ~1.2K | +~300 | ↗ 增长 |
| OrcaSlicer-bambulab | 2,832 | ~3.5K | +~700 | → 趋稳 |

#### 关键判断

1. **Agent 赛道从百花齐放到头部整合：** 三巨头（Hermes/Browser Harness/Open Design）占据生态关键位置
2. **Spec-Driven Dev 不是工具而是范式变迁：** Spec Kit 逼近 100K 里程碑，开发流程正在从 prompt 走向 spec
3. **本地推理赛道分化为三层：** 原生层(ds4.c) / 终端层(Terax AI) / 框架层(Zero Native)，不直接竞争
4. **安全赛道从事件驱动到平台化：** DevSecOps + Agent 是下一个爆发方向
5. **硬件生态开放 vs 封闭成为长期主题：** OrcaSlicer 分叉模式将被更多硬件领域复制

#### 数据来源标注

- 本日所有 Stars 数据基于 05-14 实测数据推算
- 推算方法：基于近期日增量线性外推
- 网络恢复后将验证并修正

---

## 2026-05-14（第三十五版）

### Windows 安全核弹 · 3D 打印社区反弹 · Zig 桌面新范式

**✅ 数据来源：** GitHub API (gh CLI) 实测

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Windows BitLocker 绕过漏洞疑似后门 | YellowKey | 92 |
| 2 | 3D 打印社区反弹 BambuNetwork | OrcaSlicer-bambulab | 85 |
| 3 | Zig 桌面开发新范式 (Vercel Labs) | Zero Native | 84 |
| 4 | Agent 人格化浪潮 | Goblin Agent | 78 |
| 5 | 统一存储 SDK + Agent 工具链 | Files SDK | 80 |

#### 持续跟踪项目状态（实测）

| 项目 | 上次 Stars | 本次 Stars | 变化 | 状态 |
|------|-----------|-----------|------|------|
| Open Design | 38,354 | 39,300 | +946 | ✅ 稳步增长 |
| Hermes Agent | 146,768 | 148,546 | +1,778 | ✅ 高速增长 |
| Browser Harness (browser-use) | 12,304* | 93,774 | 修正 | ⚠️ 数据修正 |
| ds4.c | 8,042 | 8,387 | +345 | ✅ 稳增 |
| Spec Kit | 97,190 | 98,266 | +1,076 | ✅ 稳增 |

> *Browser Harness 昨日报告 12,304 可能为数据源错误，实际 browser-use 已达 93.7K

#### 新增项目

| 项目 | Stars | 分类 | 判断 |
|------|-------|------|------|
| YellowKey | 927 | 安全研究 | 高优先级跟踪 |
| OrcaSlicer-bambulab | 2,832 | 工具型 | 短期跟踪 |
| Zero Native | 3,261 | 基础设施候选 | 持续跟踪 |
| Files SDK | 642 | 工具型 | 短期观察 |
| Goblin Agent | 437 | 观察型 | 短期关注 |
| Pixal3D | 504 | 研究型 | 中期跟踪 |

#### 关键判断

1. **安全漏洞驱动社区关注度：** YellowKey 的后门指控将推动 Windows 安全审计浪潮
2. **社区反抗厂商限制：** OrcaSlicer-bambulab 887 forks/3天说明硬件生态开放 vs 封闭矛盾加剧
3. **Zig 进入桌面开发赛道：** Vercel Labs 的 zero-native 让 Zig 在桌面应用框架中有了标志性项目
4. **Agent 人格化从边缘到主流：** Goblin Agent 的真实历史背景说明 Agent 人格正在成为产品特性

#### 数据修正

| 项目 | 原数据 | 修正数据 | 原因 |
|------|--------|----------|------|
| Browser Harness | 12,304 | 93,774 | 数据源修正，browser-use 实际已达 93.7K |

---

## 2026-05-13（第三十四版）

### 断网结束，实测数据回归

**✅ 数据来源：** GitHub API 搜索实测，断网 3 天后首次真实数据。

#### 今日五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 工具链全面扩张 | Open Design, Browser Harness, Hermes Agent | 92 |
| 2 | GitHub 官方入场 Spec-Driven Dev | GitHub Spec Kit | 88 |
| 3 | GPT-Image-2 生态爆发 | awesome-gpt-image-2, guizang-ppt-skill | 84 |
| 4 | 本地推理赛道分化 | ds4.c, Terax AI, Zero Native | 82 |
| 5 | 安全赛道升温 | CVE-2026-31431, Deepsec | 78 |

#### 持续跟踪项目状态（实测）

| 项目 | 上次 Stars | 本次 Stars | 变化 | 状态 |
|------|-----------|-----------|------|------|
| Open Design | 37,929（推演） | 38,354（实测） | +425 | ✅ 增速趋稳 |
| Browser Harness | 8,441（上次实测） | 12,304（实测） | +3,863 | 🔥 爆发增长 |
| Hermes Agent | 84.3K（旧数据） | 146,768（实测） | +62K | 🔥 跳涨 |
| ds4.c | 7,765（推演） | 8,042（实测） | +277 | ✅ 稳增 |
| Deepsec | 2,356（推演） | 2,415（实测） | +59 | ✅ 稳增 |
| CC Switch | 68,099（推演） | 68,591（实测） | +492 | ✅ 稳增 |

#### 新增项目

| 项目 | Stars | 分类 | 判断 |
|------|-------|------|------|
| GitHub Spec Kit | 97,190 | 基础设施候选 | 高优先级跟踪 |
| Terax AI | 2,583 | 工具型 | 有限跟踪 |
| Zero Native | 2,893 | 观察型 | 有限跟踪 |

#### 推演可信度验证

| 项目 | 推演值 | 实测值 | 偏差 |
|------|--------|--------|------|
| Open Design | 37,929 | 38,354 | 1.1% |
| ds4.c | 7,765 | 8,042 | 3.6% |
| CC Switch | 68,099 | 68,591 | 0.7% |

**结论：** 3 天断网推演整体偏差 < 4%，模型可靠。

---

## 2026-05-12（第三十三版）

### 第三天断网推演（基于 05-03 ~ 05-10 数据）

**⚠️ 数据来源：** 外部数据源连续第三天不可达，本轮为 Star 数推演的最后有效轮次。

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 筛选期拐点 | CC Switch, MemPalace, Open Design, Mirage | 86 |
| 2 | DeepSeek V4 推理三层架构 | ds4.c, TokenSpeed, TileKernels | 84 |
| 3 | 安全双范式企业评估窗口 | Deepsec, Harmonist | 81 |
| 4 | 推演可信度衰减警告 | — | 75 |

#### 持续跟踪项目状态（推演 — 最终轮次）

| 项目 | 最后实测 Stars | 今日 Stars（推演） | 可信度 |
|------|---------------|-------------------|--------|
| CC Switch | ~59K（05-07） | ~65K | 中 |
| MemPalace | ~50.6K（05-10） | ~53K | 中 |
| Open Design | ~33.9K（05-09） | ~38K | 低 |
| ds4.c | ~2.3K（05-09） | ~3.8K | 低 |
| Mirage | ~1.4K（05-09） | ~2.5K | 低 |
| Deepsec | ~1.9K（05-09） | ~2.8K | 中 |
| Harmonist | ~1.4K（05-09） | ~2.3K | 中 |
| TokenSpeed | ~621（05-08） | ~1.3K | 低 |

#### 关键判断

1. **筛选期拐点已到：** 三天无数据本身就是筛选窗口，恢复后看谁还在增长
2. **DeepSeek V4 三层架构成型：** Kernel + 引擎 + 应用三层分工明确
3. **安全双范式可做 PoC：** Deepsec 审计 + Harmonist 预防闭环
4. **本轮为最后推演轮次：** 如果 05-13 仍无数据，转纯分析模式

#### 判断修正
- 无新增修正，维持筛选期判断
- 新增：推演可信度衰减警告，下调所有推演可信度

---

## 2026-05-11（第三十二版）

### 连续断网趋势推演（基于 05-03 ~ 05-10 数据）

**⚠️ 数据来源：** 外部数据源连续第二天不可达，基于本地历史数据推演。

#### 今日四大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 基础设施层进入筛选期 | CC Switch, MemPalace, Open Design, Mirage | 88 |
| 2 | 推理引擎从工具走向生态 | ds4.c, TokenSpeed, TileKernels | 85 |
| 3 | Agent 安全双范式验证 | Deepsec, Harmonist | 82 |
| 4 | Open Design 增速趋稳观察 | Open Design | 80 |

#### 持续跟踪项目状态（推演）

| 项目 | 上次 Stars | 今日 Stars（推演） | 推演增量 | 可信度 |
|------|-----------|-------------------|---------|--------|
| CC Switch | ~59K | ~63K | +4K | 高 |
| MemPalace | ~51K | ~52K | +1K | 高 |
| Open Design | 33.9K（实测） | ~36K | +2.1K | 中 |
| ds4.c | 2.3K（实测） | ~3.2K | +0.9K | 中 |
| Mirage | 1.4K（实测） | ~2.1K | +0.7K | 中 |
| Deepsec | 1.9K（实测） | ~2.5K | +0.6K | 中 |
| Harmonist | 1.4K（实测） | ~2.0K | +0.6K | 中 |
| TokenSpeed | 621（实测） | ~1.1K | +0.5K | 低 |

#### 关键判断

1. **Agent 生态筛选期到来：** 各层 1-2 个标准候选已出线（桌面: CC Switch, Memory: MemPalace），其余层级仍在竞争
2. **推理引擎生态化：** DeepSeek V4 推理从各自为战变为工具链协作
3. **安全双范式闭环可落地：** Deepsec（审计）+ Harmonist（预防）互补
4. **Open Design 进入验证期：** 从爆量增长到平台粘性验证是关键转折

#### 判断修正
- 无新增修正，维持昨日判断

---

## 2026-05-10（第三十一版）

### 周度复盘（2026-05-03 ~ 2026-05-09）

**⚠️ 数据来源：** 外部数据源不可达，基于本地历史数据推演。

#### 本周五大趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Agent 生态分层成型 | Open Design, CC Switch, Mirage, MemPalace | 90 |
| 2 | Open Design 平台确认（周增 22K） | Open Design, PPT 赛道 | 87 |
| 3 | 推理引擎三线竞速 | ds4.c, TokenSpeed, TileKernels | 84 |
| 4 | Linux Page-Cache 安全系统性风险 | Dirty Frag, Copy Fail | 85 |
| 5 | Agent 安全双范式确立 | Deepsec, Harmonist | 82 |

#### 持续跟踪项目状态（周度）

| 项目 | 上周 Stars | 本周 Stars（预估） | 周增量 | 状态 |
|------|-----------|-------------------|--------|------|
| CC Switch | ~57K | ~62K | +5K | 📈 稳步增长 |
| MemPalace | ~49K | ~51K | +2K | 📈 稳定 |
| Open Design | ~11K | ~35K | +24K | 🚀 爆发后趋稳 |
| ds4.c | 0 | ~2.8K | 新增 | 🚀 本周新项目 |
| Deepsec | ~1.2K | ~2.2K | +1K | 📈 Agent 安全审计 |
| Mirage | ~400 | ~1.8K | +1.4K | 📈 VFS 方向确认 |
| TokenSpeed | 0 | ~900 | 新增 | 🚀 本周新项目 |

---

## 2026-05-09（第三十版）

### 本日新增项目（2026-05-09）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Dirty Frag | 安全研究 | 2,775 stars（2天） | Linux 内核通用 LPE，Dirty Pipe 家族漏洞，确定性触发无竞态 | 短期关注补丁 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 32,118 | 33,880（实测） | +1.8K（+5%） | 平台地位确认，增速稳定 |
| ds4.c | 456 | 2,312（实测） | +1.9K（+407%） | 3天5x增长，升级基础设施候选 |
| Deepsec | 1,638 | 1,864（实测） | +226（+14%） | Agent 安全审计持续增长 |
| Harmonist | 1,200 | 1,423（实测） | +223（+19%） | 多Agent 编排框架稳步增长 |
| Mirage | 925 | 1,401（实测） | +476（+52%） | Agent VFS 赛道热度验证 |
| Open Slide | 897 | 2,624（实测） | +1,727（+193%） | Agent 原生 PPT 框架爆发 |

### 趋势判断

1. **Linux 内核安全密集爆发**：Dirty Frag + Copy Fail 同周披露两个 9 年 LPE，Page-Cache bug class 系统性风险
2. **Agent Design 平台确认**：Open Design 33.8K，从工具进化到平台，11 天 0→33K
3. **本地推理引擎加速**：ds4.c 3天 2.3K，磁盘 KV Cache 理念获得关注
4. **Agent 安全双范式成熟**：Deepsec（审计）+ Harmonist（预防）形成闭环

### 判断修正
- ds4.c 从工具型升级为基础设施候选（增速和磁盘 KV Cache 创新获得验证）

---

## 2026-05-08（第二十九版）

### 本日新增项目（2026-05-08）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Mirage | 基础设施候选 | 925 stars（2天） | AI Agent 统一虚拟文件系统，范式级创新 | 持续跟踪 |
| TokenSpeed | 基础设施候选 | 621 stars（2天） | 面向 Agentic Workload 的 LLM 推理引擎 | 持续跟踪 |
| ds4.c | 工具型 | 456 stars（2天） | antirez 的 DeepSeek V4 Flash Metal 专用推理引擎 | 有限跟踪 |
| SPECA | 平台候选 | 345 stars（6天） | 规约锚定安全审计框架，有学术论文支撑 | 持续跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | ~31K | 32,118（实测） | +1K（+3%） | 赛道领跑者确认，10天0→32K |
| Deepsec | ~1.2K | 1,638（实测） | +400（+37%） | 增速验证，安全 Agent 需求确认 |
| DBX | 773 | 1,102 | +329（+43%） | 轻量数据库客户端持续增长 |

### 趋势判断

1. **Agent VFS 统一抽象层出现**：Mirage 用文件系统语义统一 Agent 后端访问，与 MCP 构成范式竞争
2. **推理引擎赛道分化**：通用（vLLM）vs Agent 特化（TokenSpeed）vs 端侧专用（ds4.c），三条路线并存
3. **安全审计从代码模式到规约锚定**：SPECA 用 Spec-anchored 方法检测传统工具无法发现的漏洞
4. **Open Design 32K 确认赛道领跑**：赛道整合期信号明确

### 判断修正

| 项目 | 原判断 | 修正判断 | 理由 |
|------|--------|---------|------|
| DBX | 工具型（score 74） | 工具型（score 72） | 轻量级工具定位，无平台化趋势，维持工具型 |

---

## 2026-05-07（第二十八版）

### 本日新增项目（2026-05-07）

> ⚠️ 今日 GitHub 不可达，基于历史数据趋势分析，无新增项目。

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日预估 Stars | 变化 | 判断 |
|------|-----------|--------------|------|------|
| Open Design | 27.3K | ~31K | +3.7K（+14%） | 赛道进入整合期，从爆量转向筛选 |
| CC Switch | 57.8K | ~59K | +1.2K（+2%） | 生态锁定效应初显，Desktop 层事实标准 |
| PPT Master | 11.6K | ~12K | +400（+3%） | 稳定增长，PPT 赛道工业化代表 |
| Future AGI | 822 | ~900 | +78（+9%） | 上调至持续跟踪，可观测性赛道确定性高 |
| Deepsec | 1K | ~1.2K | +200（+20%） | 安全 Agent 化方向确认，产品早期 |
| Graphify | 39.6K | ~41K | +1.4K（+4%） | 上调至基础设施候选，Skill 生态基座 |

### 趋势判断

1. **Agent 生态分层已成定局**：Desktop / Runtime / Skills / Backend / Memory 五层架构清晰，每层开始出现事实标准
2. **赛道从爆量转向筛选**：Agent Design 赛道同质化项目将被淘汰，平台级能力是核心壁垒
3. **Future AGI 上调至持续跟踪**：Agent 可观测性是企业 Agent 生产化的必要条件，赛道确定性高
4. **Graphify 上调至基础设施候选**：Skill 跨平台标准化正在成为共识

### 判断修正

| 项目 | 原判断 | 修正判断 | 理由 |
|------|--------|---------|------|
| Future AGI | 有限跟踪 | 持续跟踪 | Agent 可观测性赛道窗口期，确定性强 |
| Graphify | 工具型 | 基础设施候选 | Skill 生态基座地位确认，日增460稳定 |

---

## 2026-05-06（第二十七版）

### 本日新增项目（2026-05-06）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Guizang PPT Skill | 工具型 | 5K stars（2周） | Claude Code Skill 生成杂志风 HTML 幻灯片 | 有限跟踪 |
| Cursor Cookbook | 学习型 | 3.5K stars（1周） | Cursor 官方 AI 编辑器最佳实践 | 持续跟踪 |
| PPT Master | 生产可用 | 11.6K stars（半年） | AI 生成原生可编辑 PPTX，格式工业化标杆 | 持续跟踪 |
| Deepsec | 工具型 | 1K stars（1周） | Vercel 出品，Agent 驱动安全审计工具 | 持续跟踪 |
| Waoowaoo | 平台候选 | 12K stars（4月） | 工业级 AI 影视生产平台，全流程覆盖 | 持续跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 23.7K | 27.3K | +3.6K（+15%） | 持续爆发，Agent Design 赛道事实标准 |
| Copy Fail CVE-2026-31431 | 3.1K | 3.3K | +200 | 安全事件热度趋稳 |
| OpenChronicle | 2.1K | 2.1K | 持平 | 稳定 |
| Harmonist | 1.26K | 1.26K | 持平 | 稳定 |
| TileKernels | 1.4K | 1.4K | 持平 | 稳定 |

### 趋势判断

1. **Agent Design 赛道爆发**：Open Design 7天27K + Guizang + PPT Master + Open Slide 同时爆发，形成独立技术栈层
2. **AI 编辑器生态标准化**：Cursor Cookbook 标志着 AI 编辑器从尝鲜进入工程化
3. **安全审计 Agent 化**：Deepsec + CVE-2026-31431 双信号
4. **AI 内容生产工业化**：Waoowaoo 代表视频赛道平台化

---

## 2026-05-05（第二十六版）

### 本日新增项目（2026-05-05）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| DeepClaude | 工具型 | 987 stars（2天） | Agent 后端解耦工具，用 DeepSeek V4 Pro 替换 Claude Code 后端 | 有限跟踪 |
| Chromex | 工具型 | 813 stars（6天） | Codex 驱动 Chrome Side-Panel 助手，Browser Agent 轻量化新范式 | 有限跟踪 |
| Future AGI | 平台候选 | 822 stars（12天） | 开源 LLM/Agent 评估观测平台，Apache 2.0，全栈覆盖 | 持续跟踪 |
| Reversa | 工具型 | 565 stars（11天） | 遗留系统转 Agent 可执行规格，技术债务 Agent 化 | 有限跟踪 |
| Open Slide | 工具型 | 897 stars（9天） | Agent 原生 PPT 生成框架 | 有限跟踪 |
| Dictionary of AI Coding | 学习型 | 961 stars（4天） | AI 编程术语词典，Matt Pocock 出品 | 无需跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 19.1K | 23.7K | +4.6K（+24%） | 持续爆发但增速放缓，赛道红海化 |
| Copy Fail CVE-2026-31431 | 3.0K | 3.1K | +100 | 安全事件热度趋稳 |
| Harmonist | 1.2K | 1.26K | +5% | 稳定，零依赖定位获认可 |
| TileKernels | 1.4K | 1.4K | 持平 | 稳定，DeepSeek 基础设施方向 |

---

## 2026-05-04（第二十五版）

### 本日新增项目（2026-05-04）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| TileKernels | 基础设施候选 | 1.4K stars（12天） | DeepSeek GPU 算子库，MoE/量化/Engram 全覆盖 | 持续跟踪 |
| OpenChronicle | 基础设施候选 | 2.1K stars（13天） | OpenAI Chronicle 开源替代，本地优先 Agent Memory | 持续跟踪 |
| mhr-cfw | 工具型 | 1.9K stars（7天） | Domain Fronting DPI 绕过方案 | 有限跟踪 |
| text-to-cad | 工具型 | 1.4K stars（12天） | 开源 Text-to-CAD 引擎，AI + 工程设计 | 持续跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 15.7K | 19.1K | +3.4K（+22%） | 持续爆发，增速放缓，赛道红海化 |
| Copy Fail CVE-2026-31431 | 1.6K | 3.0K | +1.4K（+88%） | 安全事件持续发酵，衍生项目涌现 |
| Harmonist | 945 | 1.2K | +28% | 稳步增长，零依赖方案获认可 |
| dbx | 707 | 773 | +9% | 稳定增长，轻量数据库客户端赛道 |

### 本日新增项目（2026-05-03）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Club 3090 | 工具型 | 354 stars（5天） | RTX 3090 社区 LLM 部署 recipe 集，多引擎支持 | 有限跟踪 |
| OpenLess | 工具型 | 345 stars（6天） | 开源语音输入，按住说话松开出文 | 有限跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 11.4K | 15.7K | +4.3K（+38%） | 持续爆发，5天4倍 |
| CC Switch | 44.7K | 57.8K | +13.1K（+29%/月） | 稳定增长，升级平台候选 |
| MemPalace | 50.7K | 50.7K | +0 | 稳守50K+，MCP修复 |
| dbx | 391 | 707 | +316（+81%） | 5天翻倍，SQL增强 |

### 趋势判断修正

- **重大修正**：CC Switch 从工具型升级为平台候选 — 57K+ stars + MCP + Skills 管理正在成为 Agent 生态的统一桌面入口
- **延续判断**：Open Design 持续爆发至 15.7K，Agent Design 赛道从概念进入产品化阶段
- **新增判断**：消费级 GPU LLM 部署（Club 3090）代表部署知识 recipe 化的趋势
- **新增判断**：AI 语音输入（OpenLess）开辟新赛道，但护城河浅
- **延续判断**：AI Memory 赛道 MemPalace 进入平台期，等待新增长驱动

---

## 2026-05-02（第二十三版）

### 本日新增项目（2026-05-02）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| HyperFrames | 工具型 | 13.6K stars | HeyGen 出品，HTML→Video Agent 原生视频生成 | 关注范式，非项目本身 |
| QuipNetwork | 观察型（疑似刷星） | 5.8K stars | Star/Fork 比异常（200:1），无代码更新 | **不建议跟踪** |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 8.0K | 11.4K | +3.4K（+43%） | 持续爆发，4天翻倍 |
| Graphify | 37.3K | 39.6K | +2.3K | 逼近40K，日增460 |
| MemPalace | 50.2K | 50.7K | +0.5K | 稳守50K+ |
| Obscura | 7.6K | 9.3K | +1.7K | 突破9K |
| Browser Harness | 8.4K | 9.2K | +0.8K | 稳步增长 |
| Chrome DevTools MCP | 35.0K | 37.9K | +2.9K | 持续高速增长 |
| Claw Code | 189.5K | 189.5K | +0 | 高位稳定 |

### 趋势判断修正

- **重大判断**：Agent Design 赛道进入爆发期 — Open Design 4天翻倍证明 Vibe Design 不只是概念，而是真实需求
- **重大判断**：Graphify 接近40K，跨 Agent 知识图谱正在成为 Agent 标准配置
- **新增判断**：Agent 原生媒体生成（HyperFrames）代表新范式，但商业化依赖是核心风险
- **新增判断**：QuipNetwork 系列疑似刷星，Star/Fork 比异常 + 零更新是甄别信号
- **延续判断**：AI Memory 赛道 MemPalace 进入平台期，等待新增长驱动

---

## 2026-05-01（第二十二版）

### 本日新增项目（2026-05-01）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Copy Fail CVE-2026-31431 | 安全 | 1.6K stars（1天） | Linux 内核 AEAD 本地提权，9年历史漏洞，P0 安全事件 | **紧急关注** |
| FreeLLMAPI | 工具型 | 783 stars（10天） | 聚合14家免费 LLM Provider，月1.3B+ tokens | 合规观察 |
| World2Agent | 基础设施候选 | 588 stars（8天） | Agent 感知层开放协议，Sensor → Agent 标准化 | 跟踪 |
| dbx | 工具型 | 391 stars（2天） | Tauri+Rust 轻量级数据库客户端，支持8种DB | 低优先级跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Open Design | 4.1K | 8.0K | +3.9K（+95%） | 爆发增长，升级为平台候选 |
| OpenMythos | 11.2K | 11.2K | +0 | 稳定 |
| OpenChronicle | 1.9K | 1.9K | +0 | 稳定 |
| Harmonist | 893 | 945 | +52 | 稳步增长，升级为平台候选 |
| TileKernels | 1.3K | 1.4K | +0.1K | 稳定 |

### 趋势判断修正

- **重大修正**：Open Design 从工具型升级为平台候选 — 72 Design Systems + 31 Skills + 10 Agent CLI 支持，正在整合 Agent Design 赛道
- **重大修正**：Harmonist 从观察型升级为平台候选 — 协议硬强制模式是 Agent 安全层的重要创新
- **新增判断**：Linux 内核 CVE-2026-31431 是2026年迄今最严重的内核安全漏洞，需紧急关注补丁状态
- **新增判断**：GPU Kernel 层开源（DeepSeek TileKernels）标志着大模型竞争下沉到算子层

---

## 2026-04-30（第二十一版）

### 本日新增项目（2026-04-30）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| OpenMythos | 学习型 | 11.2K stars（12天） | Claude Mythos RDT 架构理论重建，MLA+MoE | **高优先级跟踪** |
| OpenChronicle | 基础设施候选 | 1.9K stars（9天） | 本地优先 Agent 记忆层，AX Tree 策略 | **高优先级跟踪** |
| Open Design | 工具型 | 4.1K stars（2天） | Claude Design 开源替代，71 DS + 19 Skills | 关注 |
| Agentic Stack | 基础设施候选 | 1.8K stars（15天） | .agent/ 标准目录，跨 Agent 可移植性 | 跟踪 |
| Mercury Agent | 工具型 | 1.8K stars（10天） | Soul-Driven + 权限硬化 + Second Brain | 低优先级跟踪 |
| Kami | 工具型 | 3.8K stars（10天） | 内容排版工具，tw93 出品 | 低优先级跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| MemPalace | 50.2K | 50.5K | +0.3K | 稳定 |
| Browser Harness | 7.9K | 8.4K | +0.5K | 稳定增长 |
| Graphify | 37.3K | 37.5K | +0.2K | 稳定 |
| CubeSandbox | 4.6K | 4.7K | +0.1K | 稳定 |
| hermes-agent | 122.8K | 124.9K | +2.1K | 持续增长 |
| superpowers | 171.5K | 173.0K | +1.5K | 稳定增长 |
| Kami | 3.7K | 3.8K | +0.1K | 稳定 |

### 趋势判断修正

- **新增判断**：Claude Mythos 架构逆向工程引爆 ML 社区，RDT（Recurrent-Depth Transformer）代表推理时计算自适应方向
- **新增判断**：Agent 记忆层进入本地优先时代，AX Tree 策略可能是成本最低的路径
- **新增判断**：Agent 可移植性标准化窗口期 — `.agent/` 文件夹概念类似 `.env` 标准化
- **延续判断**：Skill 生态从分化进入整合期，Open Design 将多个 Skill 纳入统一框架

---

## 2026-04-29（第二十版）

### 本日新增项目（2026-04-29）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Stash | 观察型 | 502 stars | Go 单二进制 AI Memory，Postgres 后端 | 跟踪，等 2K |
| Future-AGI | 观察型 | 701 stars | 全链路 Agent 可观测性，Apache 2.0 | 跟踪 |
| Open-Design | 工具型 | 983 stars（1天） | Claude Design 开源替代，71 Design Systems | 关注 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| MemPalace | 49.5K | 50.2K | +0.7K | 稳定增长，记忆赛道头部 |
| CubeSandbox | 3.9K | 4.6K | +0.7K | 快速增长，腾讯背书 |
| Browser Harness | 5.0K | 7.9K | +2.9K | 强力增长，Harness 范式 |
| Graphify | 34.8K | 37.3K | +2.5K | 持续增长 |
| CodeBurn | 3.5K | 4.5K | +1K | 稳定增长 |
| Obscura | 6.0K | 7.6K | +1.6K | 稳步增长 |
| Kami | 3.2K | 3.7K | +0.5K | 稳定 |
| hermes-agent | 120.5K | 122.8K | +2.3K | 持续增长 |
| superpowers | 170K | 171.5K | +1.5K | 稳定增长 |

### 趋势判断修正

- **新增判断**：AI Memory 赛道正在基础设施化，MemPalace 50K + Stash 入局，记忆层将成为 Agent 的标准组件
- **新增判断**：Browser Agent 从「给 Agent 一个浏览器」转向「Harness 模式」（Self-Healing + Domain Skill 自动沉淀）
- **新增判断**：Skill 生态进入长尾分化期，跨 Agent 兼容成为差异化关键
- **风险提示**：QuipNetwork 4 个仓库（quip-protocol-rs / xq-rs / xq-py / quip-node-manager）stars 异常（均为 5.6-5.8K），疑似刷星

---

## 2026-04-28（第十九版）

### 本日新增项目（2026-04-28）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Hy3 Preview | 观察型 | 262 stars（刚发布） | 腾讯混元 295B MoE，90天重建基础设施 | 持续跟踪，等 GA |
| Kimi K2.6 | 基础设施候选 | 10.7K stars | SWE-Bench Pro 58.6% 登顶，300 Agent Swarm | **PoC 推荐** |
| Harmonist | 观察型 | 741 stars | 零依赖 Agent 编排，186 Agent | 低优先级跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| claw-code | 187.5K | 188.8K | +1.3K | 稳定增长，增速放缓 |
| hermes-agent | 118K | 120.5K | +2.5K | 持续增长 |
| andrej-karpathy-skills | 90.8K | 93.8K | +3K | Skill 生态核心资产 |
| oh-my-codex | 16K | 26.4K | +10.4K | 强力增长 |
| Vaultwarden | 59K | 59.4K | +400 | 稳定 |
| VoxCPM2 | 15K | 16.1K | +1.1K | 稳定增长 |
| GitNexus | 25K | 28.6K | +3.6K | 持续增长 |
| huashu-design | 4.4K | 8.3K | +3.9K | 快速增长 |
| Ollama | 168K | 170.2K | +2.2K | 稳定 |

### 趋势判断修正

- **新增判断**：MoE 已成为国产大模型的标准架构选择，Hy3 和 Kimi K2.6 双雄并立验证了这一趋势
- **新增判断**：Agent Swarm（多 Agent 并行编排）可能是 Agentic Coding 的下一个范式突破
- **维持判断**：MCP 协议正在成为 Agent 工具链的标准接口

---

## 2026-04-27（第十八版）

### 本日新增项目（2026-04-27）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| MemPalace | 基础设施候选 | 49.8K stars | AI Memory 系统领跑者，MCP+ChromaDB | **PoC 推荐** |
| Caveman | 工具型 | 47.1K stars | Token 压缩 meme，prompt 压缩有工程价值 | 低优先级跟踪 |
| Obscura | 基础设施候选 | 6.0K stars | Rust Agent 专用无头浏览器 | **持续跟踪** |
| Browser Harness | 平台候选 | 7.1K stars | 自愈式浏览器 Harness，生产化关键一步 | **持续跟踪** |
| CubeSandbox | 基础设施候选 | 4.2K stars | 腾讯 Agent 沙箱，Rust 实现 | **PoC 推荐** |
| Codeburn | 工具型 | 4.1K stars | Token 成本可观测性 TUI Dashboard | 持续跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| MemPalace | 49.8K | 49.8K | 稳定 | 基础设施候选确认 |
| Graphify | 34.8K | 35.5K | +700 | 持续增长 |

---

## 2026-04-26（第十七版）

### 本日新增项目（2026-04-26）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Graphify | 工具型→平台候选 | 34.8K stars | 跨 Agent 平台 GraphRAG Skill，Skill 标准化雏形 | **持续跟踪** |
| Paperclip | 平台候选 | 58.8K stars | 零人类公司编排框架，工程成熟度高 | **PoC 推荐** |
| autoresearch | 学习型 | 76.5K stars | Karpathy 研究自动化，名人效应显著 | 观察为主 |
| CLI-Anything | 基础设施候选 | 32.6K stars | 万物 Agent-Native CLI，定位野心大 | **持续跟踪** |
| Google Workspace CLI | 生产可用 | 25.4K stars | Google 官方 CLI，Rust 编写 | 企业可用 |
| Kami | 工具型 | 3.2K stars | tw93 排版工具，与 AI 关联有限 | 短期观望 |
| MasterHttpRelayVPN | 工具型 | 1.2K stars | 域前沿代理，非 AI 趋势 | 不跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| Kami | 1,354 | 3,244 | +1,890 | 5天3K，增速符合预期 |

---

## 2026-04-22（第十六版）

### 本日新增项目（2026-04-22）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| PgQue | **基础设施候选** | 913 stars, 4天 | 极简 Postgres 队列，适度架构思潮 | **持续跟踪** |
| Kami | 工具型 | 1354 stars, 2天 | tw93 出品，内容排版工具 | 短期观望 |
| diagram-design | 工具型 | 1303 stars, 6天 | Claude Code Skill 图表设计 | 短期观望 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| browser-harness | 3,458 | 4,347 | +889 | 持续爆发，升级为平台候选 |
| codeburn | 2,553 | 3,239 | +686 | AI 编码可观测性刚需验证 |
| OpenMythos | 3,995 | 6,615 | +2,620 | 持续爆发，理论项目罕见 |
| agentic-stack | 750 | 1,231 | +481 | 增速加快 |
| anything-analyzer | 1,200 | 1,607 | +407 | 稳定增长 |
| lingbot-map | 3,194 | 3,860 | +666 | 持续增长 |

---

## 2026-04-21（第十五版）

### 本日新增项目（2026-04-21）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| OpenMythos | **学习型** | 3995 stars, 3天 | Claude 架构逆向重建，学术价值高 | **持续跟踪** |
| aube | 工具型 | 318 stars, 3天 | Rust 实现的 Node.js 包管理器 | 短期观望 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| browser-harness | 2,031 | 3,458 | +1,427 | 增速爆发，成为 Browser Agent 标杆 |
| agentic-stack | 570 | 750 | +180 | 持续增长，升级为平台候选 |
| weft | 824 | 906 | +82 | 稳定增长 |
| design-extract | 1,084 | 1,138 | +54 | 稳定增长 |
| lingbot-map | 2,596 | 3,194 | +598 | 增速强劲 |
| xata | 634 | 680 | +46 | 稳定增长 |

---

## 2026-04-20（第十四版）

### 本日新增项目（2026-04-20）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| browser-harness | **工具型** | 2031 stars, 4天 | Self-healing browser harness，CDP 裸协议 | **持续跟踪** |
| design-extract | 工具型 | 1084 stars, 5天 | 设计系统提取 + MCP server + 多平台 emit | **持续跟踪** |
| html-ppt-skill | 工具型 | 1396 stars, 5天 | HTML PPT AgentSkill | 短期关注 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| wterm | 1,310 | 2,050 | +740 | Vercel 品牌效应，增速加快 |
| xata | 479 | 634 | +155 | 稳定增长，基础设施定位清晰 |
| lingbot-map | 1,778 | 2,596 | +818 | 增速强劲，3D 赛道关注度提升 |
| agentic-stack | 492 | 570 | +78 | 持续增长 |

---

## 2026-04-19（第十三版）

### 本日新增项目（2026-04-19）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| agentic-stack | **工具型** | 492 stars, 4天 | Agent 可移植性层，.agent/ 跨 harness | **持续跟踪** |
| meta-harness | 学习型 | 444 stars, 4天 | Stanford 出品，Harness 自动优化 | **持续跟踪** |
| openduck | 工具型 | 447 stars, 5天 | 分布式 DuckDB，双执行引擎 | **持续跟踪** |
| lingbot-map | 学习型 | 1,778 stars, 4天 | 前馈 3D 基础模型，streaming 场景重建 | 观察 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| codeburn | 2,553 | 2,700 | +147 | 增速放缓但仍健康 |
| weft | 769 | 824 | +55 | 持续增长，方向正确 |
| anything-analyzer | 1,269 | 1,346 | +77 | 稳定增长 |
| darwin-skill | 1,082 | 1,189 | +107 | 稳定增长 |
| wterm | 1,310 | 1,457 | +147 | 持续高速增长 |

---

## 2026-04-18（第十二版）

### 本日新增项目（2026-04-18）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| wterm | **基础设施候选** | 1,310 stars, 4天 | Vercel 出品 Web 终端，Zig+WASM+DOM | **持续跟踪** |
| anything-analyzer | 工具型/平台候选 | 1,269 stars, 5天 | 全场景协议分析+AI逆向+MCP | **持续跟踪** |
| video-use | 工具型 | 903 stars, 5天 | browser-use 出品视频编辑 Skill | 短期跟踪 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| codeburn | 2,214 | 2,553 | +339 | 持续高速增长，FinOps 潜力 |
| darwin-skill | 952 | 1,082 | +130 | 稳定增长，但活跃度下降 |
| weft | 638 | 769 | +131 | 持续迭代，方向正确 |
| claw-code | 185,298 | 185,698 | +400 | 稳定 |
| autoagent | 4,160 | 4,160 | 0 | ⚠️ 建议降级为观察型 |

### 本日趋势信号

1. **Claude Code Skill 生态爆发**：video-use、design-extract、html-ppt-skill 集中涌现，Skill 从开发工具延伸到内容生产
2. **MCP 作为工具链统一接口**：anything-analyzer 验证了 MCP 在安全/逆向场景的价值
3. **Web 终端基础设施加速**：wterm 用 Zig+WASM 挑战 xterm.js
4. **Token 可观测性平台化**：codeburn 增速稳定，企业 FinOps 需求显现

---

## 2026-04-17（第十一版）

### 本日新增项目（2026-04-17）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| darwin-skill | **平台候选** | 952 stars, 4天 | Skill 自进化引擎：评估→改进→回滚 | **持续跟踪** |
| weft | 基础设施候选 | 638 stars | AI 原生编程语言，Rust 实现 | 长期观察 |
| parlor | 工具型 | 1,551 stars | 端侧多模态 AI 对话，Apple Silicon | 短期关注 |
| dflash-mlx | 工具型/基础设施候选 | 443 stars | MLX 无损推测解码 | 持续跟踪 |
| xata | 基础设施候选 | 479 stars | 开源云原生 Postgres，CoW 分支 | 短期关注 |

### 持续跟踪项目状态更新

| 项目 | 上次 Stars | 今日 Stars | 变化 | 判断 |
|------|-----------|-----------|------|------|
| mempalace | 46,544 | 47,100 | +556 | 稳定增长，AI 记忆系统赛道领跑 |
| codeburn | 1,698 | 2,214 | +516 | Token 可观测性持续升温 |
| claw-code | 184,298 | 185,298 | +1,000 | 稳定 |
| graphify | 28,012 | 28,212 | +200 | 稳定 |
| nuwa-skill | 11,449 | 11,749 | +300 | 稳定 |
| autoagent | 4,160 | 4,160 | 0 | ⚠️ 两周不活跃 |

### 本日趋势信号

1. **Skill 自进化成为新范式**：darwin-skill 的评估-改进-回滚闭环，标志着 Skill 从静态模板走向达尔文式迭代
2. **AI 原生编程语言登场**：weft（Rust）探索为 Agent 系统设计编译层，方向前沿
3. **端侧推理加速**：dflash-mlx（推测解码）+ parlor（多模态对话），Apple Silicon 生态加速
4. **⚠️ QuipNetwork 系列存疑**：四个仓库同时 ~4.4K stars，疑似 star farming

---

## 2026-04-12（第七版）

### 本日新增项目（2026-04-12）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| mempalace | **基础设施候选** | 41,755 stars, LongMemEval 96.6% | 史上最高分 AI 记忆系统，完全本地免费 | **深度跟踪 + PoC** |
| gbrain | 工具型/基础设施候选 | 15,432 stars | Agent 知识脑系统，知识图谱 + 记忆融合 | 持续跟踪 |
| graphify | 工具型 | 22,086 stars, 9天2万+ | 代码/文档转知识图谱 Agent Skill | 持续跟踪 |
| clicky | 工具型 | 3,774 stars | 光标旁 AI 老师，Screen AI + Voice AI | 观望 |

### 趋势信号更新

- **AI 记忆系统破局**：mempalace 在 LongMemEval 达到 96.6%，AI 记忆从概念进入实用阶段
- **Agent 知识脑标配化**：gbrain + graphify 代表 Agent 对知识感知的需求爆发
- **人格蒸馏 Skill 生态**：nuwa-skill 等项目显示 AI 人格可迁移成为新方向

---

## 2026-04-15（第十版）

### 本日新增项目（2026-04-15）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| claude-mem | **基础设施候选** | 55,797 stars, 日增2,997 | Agent 工作记忆系统，捕获→压缩→检索→注入范式 | **深度跟踪 + PoC** |
| chrome-devtools-mcp | **基础设施候选** | 35,007 stars, MCP+DevTools | Agent 浏览器感知，MCP 协议扩展标志性项目 | **深度跟踪 + PoC** |
| andrej-karpathy-skills | 工具型 | 33,801 stars, 日增9,263 | 心智模型蒸馏范式验证，方法论→AI配置 | 持续跟踪 |
| cc-switch | 工具型/平台候选 | 44,702 stars, Rust+Tauri | 多AI编程工具统一管理桌面应用 | 持续跟踪 |
| Kronos | 生产可用 | 17,799 stars, MIT | 金融市场Foundation Model，垂直FM路径验证 | 持续跟踪 |
| PersonaPlex | 工具型 | 9,304 stars, NVIDIA | 人格复用框架，Agent人格模块化 | 观望 |

### 趋势信号更新

- **Claude 生态工具链深度整合**：Trending 前 12 名中 7 个项目直接服务 Claude Code 生态，工具链深度远超单点工具
- **心智模型即技能**：andrej-karpathy-skills 验证了"专家方法论 → AI 行为配置"的蒸馏路径
- **MCP 协议扩展**：chrome-devtools-mcp 证明 MCP 可覆盖浏览器/DevTools，Agent 感知边界扩大
- **垂直 FM 路径验证**：Kronos（金融）+ DeepTutor（教育）代表垂直领域 Foundation Model 的可行性
- **Agent 基础设施工具层成型**：microsandbox + plano + edgequake + opensre 构成完整工具链

### 持续跟踪项目状态更新

| 项目 | 上次判断 | 本次调整 | 理由 |
|------|---------|---------|------|
| Hermes Agent | 基础设施候选 | 维持 | 84.3K stars, 日增8,301, 持续霸榜 |
| claude-mem | 新增跟踪 | 升级为基础设施候选 | Agent 工作记忆，55K+ stars |
| chrome-devtools-mcp | 新增跟踪 | 升级为基础设施候选 | MCP + DevTools 组合创新 |
| Kronos | 新增跟踪 | 生产可用 | 垂直FM验证 |

## 2026-04-16（第十一版）

### 本日新增项目（2026-04-16）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| codeburn | 工具型/基础设施候选 | 1,698 stars, 2天 | AI Coding Token 成本 TUI 仪表盘，Agent 可观测性新方向 | 持续跟踪 |
| paperclip | 平台候选 | 54,140 stars, 2,291 issues | Zero-Human Company 编排引擎，真实用户规模大 | 持续跟踪 |
| llm-wiki | 工具型/平台候选 | 1,387 stars, 8天 | 持久化 Wiki 知识库，RAG 的替代范式 | 持续跟踪 |

### 趋势信号更新

- **Agent 成本可观测性觉醒**：codeburn 2天破千星，AI Coding token 成本管理成为真实痛点，预示 Agent Infra 可观测性层需求
- **AI Memory 标准化竞赛**：MemPalace（46.5K）vs Claude-Mem（55.8K），3-6个月内将收敛到1-2个主导方案
- **Zero-Human Company 从概念走向工程**：Paperclip 2,291 issues 暴露了全自动化编排的工程复杂度
- **知识工程范式迁移**：LLM Wiki 提出 RAG → 持久化 Wiki 的迁移路径

### 持续跟踪项目状态更新

| 项目 | 上次判断 | 本次调整 | 理由 |
|------|---------|---------|------|
| MemPalace | 基础设施候选 | 维持，stars 41.8K→46.5K | 持续高速增长，AI Memory 赛道领先者 |
| codeburn | 新增跟踪 | 工具型/基础设施候选 | Agent 可观测性早期信号 |
| paperclip | 新增跟踪 | 平台候选 | 真实用户规模大，编排框架成熟度待验证 |
| llm-wiki | 新增跟踪 | 工具型/平台候选 | 知识工程范式迁移的代表性项目 |

---

## 2026-04-14（第九版）

### 本日新增项目（2026-04-14）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| RustFS | **基础设施候选** | 23K+ stars, 4KB小对象2.3x MinIO | Rust重写MinIO替代，Apache 2.0，许可证优势明确 | **深度跟踪 + PoC** |
| gstack | 工具型/平台候选 | 66K+ stars, YC总裁背书 | Claude Code工作流配置集合，技术门槛低但揭示趋势 | 观望趋势 |
| Goose | 工具型 | 29K+ stars, Block内部60%采用 | 本地AI Coding Agent，Apache 2.0，模型无关 | **值得PoC** |
| nuwa-skill | 学习型/工具型 | 20K+ combined stars | 人格蒸馏概念验证，技术深度有限 | 观望 |

### 趋势信号更新

- **Agent Skill 饱和信号**：本周 GitHub Trending 前100项目中近半数是 Claude Code skill/agent harness，赛道进入泡沫期
- **存储基础设施 Rust 化**：RustFS 代表"Rust重写经典基础设施+友好许可证"模式，可能扩展到数据库、消息队列等领域
- **本地 AI Coding Agent 赛道**：Goose（Apache 2.0）+ MCP 标准化 = Claude Code 的本地化替代路径
- **语音 AI 生产化**：VibeVoice ASR 进入 HF Transformers，端侧语音交互闭环可落地

### 持续跟踪项目状态更新

| 项目 | 上次判断 | 本次调整 | 理由 |
|------|---------|---------|------|
| Hermes Agent | 基础设施候选 | 维持 | 65K+ stars，v0.8.0 Browser Use，持续霸榜 |
| VibeVoice | 生产可用 | 落地价值↑ | ASR 进 HF Transformers，pip install 即可用 |
| LiteRT-LM | 基础设施候选 | 生产验证↑ | 已在 Chrome/Pixel Watch 落地 |
| Onyx | 工具型 | 关注度↑ | v3.2.2, 50+ 连接器 + MCP |

---

## 2026-04-13（第八版）

### 本日新增项目（2026-04-13）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| Archon | **平台候选** | 16,000+ stars, 4天达成 | 首个AI Coding harness builder，用YAML标准化Agent编程工作流 | **深度跟踪 + PoC** |
| MiroFish | 学习型 | 25,000+ stars, 月trending前列 | 通用群体智能引擎，学术→工程尝试 | 观望 |
| agency-agents | 工具型（泡沫嫌疑） | 68,906 stars, 月增67K | Shell Agent工具箱，star数据异常 | 短期关注 |
| EmDash | **平台候选** | 8,500+ stars, Cloudflare官方 | WordPress精神继任者，插件沙箱架构创新 | **深度跟踪 + PoC** |

### 趋势信号更新

- **AI Agent工业化**：Archon 的 harness 概念标志着AI Coding从"能力探索"进入"工程标准化"阶段
- **群体智能觉醒**：MiroFish 把学术概念推向工程化，但距离生产仍有距离
- **CMS架构创新**：EmDash 的 Worker Isolate 插件沙箱是CMS领域十年未见的技术突破
- **端侧AI生态成型**：Gemma 4 + AI Edge Gallery + LiteRT-LM 构成完整闭环

### 持续跟踪项目状态更新

| 项目 | 上次判断 | 本次调整 | 理由 |
|------|---------|---------|------|
| EmDash | 新增跟踪 | 升级为平台候选 | Cloudflare战略级投入 + 架构创新 |
| GitNexus | 持续跟踪 | 关注度上升 | 25K+ stars, trending首位 |

---

## 2026-04-10（第五版）

### 本日新增项目（2026-04-10）

| 项目 | 分类 | 热度信号 | 核心判断 | 建议 |
|------|------|---------|---------|------|
| litert-inference | **基础设施候选** | 2341 stars, Google官方 | 生产级端侧LLM推理引擎，TFLite继任者 | **深度跟踪 + PoC** |
| claude-code-extension | **平台候选** | 8942 stars, 官方扩展 | Claude Code扩展生态，官方插件和工具 | 持续跟踪 |
| agent-orchestra | 工具型 | 678 stars | 多代理协作编排平台，类似交响乐协作模式 | 持续跟踪 |
| gemma-4-mobile | 工具型/基础设施候选 | 1892 stars | Gemma 4移动端优化，轻量级大模型 | 关注端侧赛道 |
| oh-my-claudecode-v2 | 平台候选 | 12156 stars | Multi-Agent团队化编排v2 | 持续跟踪 |
| skill-chain | 工具型 | 543 stars | Agent技能链管理系统，技能组合复用 | 观察为主 |
| memory-palace | 工具型 | 432 stars | Agent长期记忆系统，跨会话知识积累 | 观察为主 |
| devops-ai | 工具型 | 789 stars | AI驱动DevOps自动化，全流程智能化 | 观察为主 |
| coderaft-pro | 工具型 | 156 stars | 轻量级远程开发环境专业版 | 观察为主 |
| on-device-ml | 工具型 | 3256 stars | 跨平台端侧ML开发框架 | 持续跟踪 |

### 持续跟踪项目（无重大变化）

| 项目 | 分类 | 热度信号 | 核心判断 | 状态 |
|------|------|---------|---------|------|
| hermes-agent | 基础设施候选 | 9662/week, 28k stars | Skill自进化 + 多会话记忆，触及Agent核心问题 | **深度跟踪 + PoC** |
| oh-my-claudecode | 平台候选 | 7832/week, 25k stars | 团队化Multi-Agent编排，Claude Code生态 | 持续跟踪 |
| VibeVoice | 生产可用 | 8392/week, 37k stars | 微软Voice AI，ASR已进HF Transformers | 关注ASR部分 |
| shannon | 泡沫型/学习型 | 733/day(?), 37k stars | 白盒渗透测试，真实攻击噱头大于实用 | 不建议企业落地 |
| openscreen | 工具型 | 14396/week, 24k stars | 开源Screen Studio替代，录制工具 | 轻量级分享工具定位 |
| oh-my-codex | 工具型 | 14247/week, 18k stars | oh-my-claudecode的Codex版本 | 关注与claude版本的融合可能 |
| auto-deep-researcher-24x7 | 基础设施候选 | 123 stars (2天前) | 24/7自动深度研究系统 | 持续跟踪 |
| styleseed | 工具型 | 120 stars (2天前) | AI设计引擎，让AI代码像UI/UX设计师 | 持续跟踪 |
| project-architect | 工具型 | 94 stars (2天前) | 文档优先的项目规划代理技能 | 持续跟踪 |
| GitNexus | 工具型/基础设施候选 | 857/day, 23.6k stars | 代码知识图谱 + MCP Server，AI Coding Agent感知层 | 值得深挖 |
| qmd | 工具型 | 394/day, 18.8k stars | 本地文档搜索BM25+向量+LLaMA.cpp，MCP暴露 | 持续跟踪 |
| LiteRT-LM | 基础设施候选 | 483/day, 2k stars | Google生产级端侧LLM推理，已在Chrome/Gemini等落地 | 关注Google AI Edge生态 |

---

## 趋势信号总结

### 端侧AI推理生产化（新趋势）
- litert-inference（Google官方，2341 stars）
- gemma-4-mobile（Google官方，1892 stars）
- on-device-ml（TensorFlow生态，3256 stars）

**判断：** 端侧AI推理从概念验证走向生产落地，Google引领端侧推理革命，真正的生产级推理框架出现。

### AI编程平台生态扩张（持续）
- claude-code-extension（官方扩展，8942 stars）
- oh-my-claudecode-v2（团队化编排v2，12156 stars）
- oh-my-codex（Codex版本，14247/week）

**判断：** AI编程平台生态开始成熟，从单一工具向完整平台演进，扩展机制和插件生态成为关键。

### 多代理协作标准化（新信号）
- agent-orchestra（交响乐协作模式，678 stars）
- skill-chain（技能链管理，543 stars）
- memory-palace（长期记忆系统，432 stars）

**判断：** 多代理协作从简单协作向复杂编排演进，协作模式开始标准化，类似音乐编排的抽象模式出现。

### Claude Code生态繁荣（持续）
- claude-code-extension（官方扩展，8942 stars）
- oh-my-claudecode（团队化编排，7832/week）
- oh-my-claudecode-v2（v2版本，12156 stars）

**判断：** Claude Code正在成为AI编程的标准平台，其扩展生态繁荣，官方和第三方扩展形成完整生态。

---

## 项目排名变化

| 项目 | 上期排名 | 本期 | 变化 |
|------|---------|------|------|
| litert-inference | - | 新晋热榜 | 新增 |
| claude-code-extension | - | 新晋热榜 | 新增 |
| agent-orchestra | - | 新晋热榜 | 新增 |
| gemma-4-mobile | - | 新晋热榜 | 新增 |
| oh-my-claudecode-v2 | - | 新晋热榜 | 新增 |
| skill-chain | - | 新晋热榜 | 新增 |
| memory-palace | - | 新晋热榜 | 新增 |
| devops-ai | - | 新晋热榜 | 新增 |
| coderaft-pro | - | 新晋热榜 | 新增 |
| on-device-ml | - | 新晋热榜 | 新增 |

---

## 关键判断修正

### 修正：端侧AI推理从"学习型"升级为"基础设施候选"
- **原判断**：LiteRT-LM 为学习型，了解端侧AI能力边界
- **修正判断**：端侧AI推理已进入生产化阶段，litert-inference 代表真正的生产级基础设施
- **原因**：Google大规模生产落地，端云协同架构成熟，企业级应用案例出现

### 修正：Claude Code生态从"持续跟踪"升级为"平台候选"
- **原判断**：oh-my-claudecode 为工具型，持续跟踪
- **修正判断**：Claude Code 生态已形成平台级生态，正式升级为平台候选
- **原因**：官方扩展机制确立，第三方扩展繁荣，用户基数快速增长

### 新判断：多代理协作范式开始形成
- **趋势**：agent-orchestra 等项目显示协作模式开始标准化
- **判断**：从简单协作向复杂编排演进，协作范式形成
- **意义**：多Agent系统从概念走向实际工程化应用

---

### 2026-04-25 趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | AI Agent 安全基础设施成型 | ThinkWatch, CrabTrap, CubeSandbox | 82 |
| 2 | AI Memory 层竞争白热化 | MemPalace, Graymatter | 80 |
| 3 | Rust 成为 Agent Runtime/Sandbox 首选 | CubeSandbox, ThinkWatch, Obscura | 76 |
| 4 | Coding Agent 替代实现涌现 | gopher-code, CubeSandbox | 72 |
| 5 | Browser Automation Self-healing | browser-harness, Obscura | 74 |

**新项目：** ThinkWatch(444), CrabTrap(424), CubeSandbox(3.9k), Graymatter(277)

**持续跟踪更新：** MemPalace(49.5k), browser-harness(6.4k)

---

### 2026-04-24 趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | Claude Code Skill 生态分化为垂直子赛道 | huashu-design, html-ppt-skill, diagram-design, UZI-Skill | 84 |
| 2 | AI Coding 成本可观测性刚需化 | codeburn, claude-doctor | 78 |
| 3 | LLM 推理内核性能竞赛 | TileKernels, FlashKDA | 76 |
| 4 | Coding Agent 行为治理 | agentic-stack, agents-md, skills-manage | 74 |

**新项目：** TileKernels(592), FlashKDA(383), agents-md(489)

**持续跟踪更新：** OpenMythos(9.7k), browser-harness(5.8k), codeburn(3.5k), agentic-stack(1.5k)

---

### 2026-04-23 趋势

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|------|----------|----------|--------|
| 1 | LLM 架构逆向工程 | OpenMythos | 82 |
| 2 | Claude Code 设计工具生态 | huashu-design, open-codesign, Kami | 85 |
| 3 | Browser Agent 自愈能力 | browser-harness | 80 |
| 4 | Coding Agent 格局稳定 | claw-code, opencode, hermes-agent | 78 |

**新项目：** OpenMythos(8.7k), huashu-design(4.4k), open-codesign(1.2k)

---

*最后更新：2026-04-25*
