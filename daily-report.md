# GitHub 趋势研究 · 日报索引

> 每日 GitHub 趋势研究简报，持续跟踪不间断

---

## 2026-08-05

**核心主题：** 应用层第四日分化——qm 突破 10K 关口（9,458→11,092，+1,634，增速衰减至 +17%）但 crm 反超增速（+1,446/+46%）、genoffice 翻倍（+709/+125%）；"齐涨"结束、"分化"开始，多路线各自验证 PMF · K3 本地推理品类叙事分裂——kimi-k3-in-c 持续 +779 逼近 2K（极限低内存叙事延续），waste 增量骤降 +510→+145（可用速度叙事退潮），"最低 RAM"卖点持续压过"接近可用速度" · Agent 可观测性/治理品类出现——Perplexity 官方 numbat（684⭐，端点 agent 活动可见性 + 取证重建 + 可选 pre-action 阻断 + 单二进制，覆盖十余个 agent），与 ratchet/skill-recorder 构成三层 agent 质量基础设施栈（技能提取→执行约束→事后取证）· Agent 摄入层扩张——Firecrawl 官方 anydoc（2 天 1.1K⭐，Rust，office 文档→LLM-ready Markdown，单数毫秒）

**关键项目：**
- 👥 yc-software/qm (11,092, 更新 +1,634) — 多人协作 agent harness，突破 10K，增速衰减，被 crm 反超，Score 90
- 📋 trycompai/crm (4,569, 更新 +1,446) — Agentic-first CRM，增速反超 qm，垂直路线 PMF 强信号，Score 87
- 📄 genspark-ai/genoffice (1,273, 更新 +709) — AI-native 办公套件，翻倍 +125%，增速最快，Score 85
- 💠 FareedKhan-dev/kimi-k3-in-c (1,952, 更新 +779) — 便携 C99 跑全量 K3，逼近 2K，叙事分裂中持续放量，Score 83
- 🦝 perplexityai/numbat (684, 新增) — Perplexity agent 可观测性，覆盖十余个 agent，三层栈，Score 84
- 📑 firecrawl/anydoc (1,086, 新增) — Firecrawl office 文档→Markdown，agent 摄入层，Score 82
- 🎥 microsoft/skill-recorder (1,751, 更新 +385) — Microsoft 录屏→Skill，三层栈技能提取层，Score 84
- 🔧 0xwilliamortiz/ratchet (430, 更新 +7) — agent 规则闭环检查，285 watchers 保持，三层栈执行约束层，Score 83
- 💽 sqliteai/waste (1,665, 更新 +145) — 纯 C K3 推理，增量骤降，叙事分裂，Score 82
- 📐 openai/ten-proofs (470, 更新 +38) — OpenAI Lean 4 形式化，平缓符合预期，Score 82

---

## 2026-08-04

**核心主题：** 应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458，三日 +8,091，第三日 +2,443 反超第二日 +2,233 彻底排除脉冲假设）+ 多路线并行扩张（通用平台 qm 9.5K/垂直重写 crm 3.1K/AI-native 桌面 genoffice 564 同步放量） · K3 本地推理品类级爆发——kimi-k3-in-c 单日 +955（218→1,173，近 5.4 倍）引爆极端低内存（8.24GB）卖点，waste +510 续涨（连续三日增速递增 +342/+358/+510） · AI 推理边界外延——OpenAI 官方 ten-proofs 用 Lean 4 形式化十项数学/理论计算机成果（球填充/非 sofic 群/Connes 刚性反例等），每个可 `lake build` 独立验证，标志 AI + 形式化验证交叉品类出现 · agent 质量基础设施成型——ratchet 把 coding agent 极简规则从开环注入变闭环检查（PostToolUse hook 实时测复杂度/依赖/wrapper/yagni，285 watchers 高质量关注），与 skill-recorder 正交互补

**关键项目：**
- 👥 yc-software/qm (9,458, 更新 +2,443) — 多人协作 agent harness，三日连涨彻底排除脉冲，应用层趋势完全确立，Score 90
- 💠 FareedKhan-dev/kimi-k3-in-c (1,173, 更新 +955) — 便携 C99 跑全量 K3，8.24GB RAM，爆发性增长，Score 83
- 📐 openai/ten-proofs (432, 新增) — OpenAI 官方 Lean 4 数学形式化，AI + 形式化验证交叉品类，Score 82
- 📄 genspark-ai/genoffice (564, 新增) — AI-native 办公套件，字节保真往返，Score 84
- 🔧 0xwilliamortiz/ratchet (423, 新增) — agent 规则闭环检查，285 watchers，Score 83
- 📋 trycompai/crm (3,123, 更新 +1,392) — Agentic-first CRM，垂直路线持续确认，Score 86
- 🎥 microsoft/skill-recorder (1,366, 更新 +640) — Microsoft 录屏→Skill，与 ratchet 正交互补，Score 84
- 💽 sqliteai/waste (1,520, 更新 +510) — 纯 C K3 推理，品类持续放量，Score 83

---

## 2026-08-03

**核心主题：** qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→736 同步增），昨日"脉冲 vs 趋势"之问得到回应——应用层产品化确认非一日脉冲（增速 +250%→+47% 是健康衰减，绝对量级仍远超 K3 +75） · K3 本地推理第四极：kimi-k3-in-c 便携 C99 把 RAM 下限打到 8.24GB（176KB 引擎/0 GPU/8GB 与 224GB 字节一致输出/32s·token⁻¹），waste 652→1,010 续涨（v0.6.2 cgroup-aware budget） · 垂直应用层成型：trycompai/crm 1.7K⭐ 以 Vercel eve 为底座把 agent 做成 CRM 产品本体（"agent 是产品，数据库只是它记笔记的地方"/证据账本/工具不接受置信度/deny-all egress 沙箱/单租户内部） · Microsoft skill-recorder 726⭐ 官方入场（录屏→Copilot CLI 重建意图+步骤→生成可复用 SKILL.md 或定时 Automation） · decimen-optical-transfer 昨日 3,031→今日 3,620 几乎停滞，印证刷星判断

**关键项目：**
- 👥 yc-software/qm (7,015, 更新 +2,233) — 多人协作 agent harness，第二日续涨确认非脉冲，Score 90
- 📋 trycompai/crm (1,731, 新增) — Agentic-first 开源 CRM，以 eve 为底座，证据账本 + deny-all 沙箱，Score 86
- 💠 FareedKhan-dev/kimi-k3-in-c (218, 新增) — 便携 C99 跑全量 K3，peak RSS 8.24GB，Score 83
- 🎥 microsoft/skill-recorder (726, 新增) — Microsoft 官方录屏→Skill 生成，Score 84
- 💽 sqliteai/waste (1,010, 更新 +358) — 纯 C K3 推理，v0.6.2 cgroup-aware budget，Score 83

---

## 2026-08-02

**核心主题：** qm 单日爆发 +250%（1,367→4,782⭐，fork 125→469 同步暴涨，验证 harness 应用层产品化进入主流），qwen-audio-agent 1.2K⭐ 加入应用层（全双工实时语音 + 后台任务并行/经 ACP 接入 OpenCode/Claude Code/Codex/Hermes/Kimi Code，v1.0.0 已发布） · Agent 记忆独立成品类——OptMem 1.05K⭐（VictorTaelin/HVM 作者，426-token prompt + 单 Python 脚本/append-only log + 重建式树摘要/position-is-identity，1M 记忆 wake 0.03s） · Kimi K3 本地推理三极分化——waste 纯 C 零依赖跑全量 2.78T（0.62 tok/s/64GB Mac/trunk 驻内存 + expert 磁盘流式/作者自验 logits 3.6e-06），与 deltafin(Python)、colibri(C) 并立 · K3 生态斜率继续趋平（K3 +108/AgentENV +41，axrl +133 逆势） · decimen-optical-transfer 3K⭐ 疑似刷星（star/watcher 159:1）标记不推荐

**关键项目：**
- 👥 yc-software/qm (4,782, 更新 +250%) — 多人协作 agent harness，24h 爆发，Score 89
- 🧠 VictorTaelin/OptMem (1,058, 新增) — 426-token prompt + 单脚本极简 agent 记忆，Score 85
- 🎙️ QwenAudio/qwen-audio-agent (1,181, 新增) — 全双工实时语音 agent 运行时，Score 84
- 💽 sqliteai/waste (652, 新增) — 纯 C 零依赖跑全量 K3 2.78T，Score 82

---

## 2026-08-01

**核心主题：** Coding agent 应用层从 harness 扩散为完整产品形态——qm 多人协作 agent harness（1.4K⭐/Slack+Web/每人独立沙箱）、cindy 开箱即用多 harness agent 客户端（1.3K⭐/Claude Code+Codex 混合驱动/任务中途切换）、better-harness harness 工程化（1.3K⭐/loop engineering），harness 层从工具进化为多人协同平台 · 边缘推理边界推到极致——esp32-ai 在 8 美元 ESP32-S3 上跑 28.9M 参数 LLM（9.5 tok/s/Per-Layer Embeddings/flash 存储 25M 参数表/512KB SRAM），quill 全本地 macOS 会议录音转录（Parakeet TDT/系统音频+麦克风双轨/CAF 容错），"把模型塞进最小内存"从 MoE 下沉到微控制器 · Kimi K3 生态延续增长但斜率趋平（K3 7.5K→7.7K +189/AgentENV 2.6K→2.7K +95，较昨日降一个数量级）

**关键项目：**
- 👥 yc-software/qm (1,367, 新增) — 多人协作 agent harness for work，per-scope sandbox，Score 86
- 🔧 slvDev/esp32-ai (2,627, 新增) — 28.9M LLM on $8 ESP32-S3，Per-Layer Embeddings，Score 83
- 🎯 makecindy/cindy (1,260, 新增) — 开箱即用多 harness agent 客户端，中途切换，Score 82
- 🪶 digimata/quill (3,195, 新增) — 极简全本地 macOS 会议录音+转录，Score 81

---

## 2026-07-31

**核心主题：** Coding agent harness 多极化——SpaceXAI 官方 grok-build 23.5K⭐（Rust TUI/ACP 嵌入编辑器/headless CI 三模式/预编译三平台），omnigent meta-harness 7.9K⭐（编排 Claude Code/Codex/Cursor/Pi/Hermes + 自定义 agent/跨设备协作/策略治理/云沙箱），vercel/eve filesystem-first 4.2K⭐（agent 能力即目录结构/durable）三线并进，harness 层从单一工具分化为本体/范式/编排三层 · 前沿 MoE 本地推理范式确立——colibri 纯 C/零依赖 GLM-5.2 744B 引擎 19 天从 3.85K 飙至 21K⭐，VRAM/RAM/NVMe 三级内存层级，6×5090 全驻留 4 tok/s · Kimi K3 全栈生态持续深化——五层齐增（K3 5.5K→7.5K/MoonEP→923/deltafin→466/axrl→641/AgentENV→2.6K）

**关键项目：**
- 🛰️ xai-org/grok-build (23,556, 新增) — SpaceXAI 官方 coding agent harness 与 TUI，Rust，Score 90
- 🐦 JustVugg/colibri (21,218, 更新) — 纯 C/零依赖 GLM-5.2 744B MoE 推理引擎，Score 88
- 🤖 omnigent-ai/omnigent (7,924, 更新) — Agent meta-harness 编排层，Score 84
- 🌙 vercel/eve (4,198, 更新) — Filesystem-first durable agent 框架，Score 83

---

## 2026-07-30

**核心主题：** 首个开源 3T 级模型发布并带火全栈基础设施——Kimi K3 5.5K⭐（MoonshotAI/2.8T MoE/104B 激活/KDA+Attention Residuals 新架构/Stable LatentMoE 896 选 16/1M 上下文/原生多模态 MXFP4），对标 Claude Fable 5/GPT-5.6 · MoE 训练通信库赛道——MoonEP 858⭐（动态冗余专家/每 rank 完美负载均衡/零拷贝+静态形状/通信低于 DeepEP v2 且对不均衡免疫），EP 均衡从"接受"走向"消除" · 超参数模型本地推理边界——deltafin 308⭐（MXFP4 专家按需 HTTP 流式加载/磁盘缓存/NEON+Metal/M1 Max 64GB 实测 14.6s/token），MoE 稀疏性使超大模型本地部署在原理上可行 · 多轮 Agent RL 后训练工程化——AxisRL 569⭐（SGLang rollout+Megatron 训练/300+ 轮轨迹/rollout-trainer 一致性调试），呼应昨日 AgentENV 环境层信号

**关键项目：**
- 🧠 MoonshotAI/Kimi-K3 (5,511, 新增) — 首个开源 3T 级模型，2.8T MoE 新架构，Score 93
- ⚖️ MoonshotAI/MoonEP (858, 新增) — MoE 专家并行完美负载均衡通信库，对标 DeepEP v2，Score 88
- 🍎 gavamedia/deltafin (308, 新增) — 2.8T MoE 单台 Mac 按需流式推理，Score 84
- 🔄 XYZ-AI-Lab/axrl (569, 新增) — 多轮 Agent RL 后训练框架，rollout-trainer 一致性，Score 83

---

## 2026-07-29

**核心主题：** 本地优先 AI Coworker 交付成品范式——OpenWorker 9.9K⭐（Andrew Ng/交付成品非聊天/审批门控/BYO 模型/25+ 连接器/aisuite），重定义 Agent 应用层信任模型 · Agent RL 训练 Firecracker 基础设施开源——AgentENV 1.4K⭐（Rust/microVM/快照 fork<50ms 恢复/为 Kimi K3 训练提供底座），环境即快照即 fork · 零运行时语言编译——scriptc 2.1K⭐（Vercel Labs/TS→原生二进制/无 Node V8/178KB 2ms 启动/99% 静态），Agent 代码部署成本降维 · 单文件自包含 AI 可编辑文档——Bento 2.8K⭐（文件即软件/自重写保存/CRDT+E2EE/JSON 可被 Agent 原地编辑）

**关键项目：**
- 🧑‍💻 andrewyng/openworker (9,965, 新增) — 本地优先 AI Coworker，审批门控 + BYO 模型，Score 92
- ⚡ kvcache-ai/AgentENV (1,411, 新增) — Agent RL 训练 Firecracker 平台，基础设施候选，Score 90
- 🔷 vercel-labs/scriptc (2,099, 新增) — TypeScript→原生编译器，零运行时，Score 86
- 🍱 nyblnet/bento (2,806, 新增) — 单文件自包含办公套件，AI 可编辑 JSON，Score 84

---

## 2026-07-24

**核心主题：** 人机协同工作空间基础设施化——Block Buzz 8.1K⭐（Nostr Relay 协议/Agent 与人类共享频道/审计日志/Git NIP-34），Block Inc. 出品，把 Forge+Slack+CI 压缩为一个协议 · 代码知识图谱赛道升温——Code-Review-Graph 26K⭐（Tree-sitter AST/MCP/82x Token 削减/增量更新），Graphify 同赛道独立方案 · Rust Agent Harness 性能碾压——jcode 11K⭐（14ms 启动 vs Claude Code 3.4s/10 会话 117MB vs 2.3GB），Rust 重写 Agent 运行时 · Agent OS 库化——agentOS 4.1K⭐（WebAssembly+V8/6ms 冷启动/进程内运行），Agent 基础设施从 Sandbox 走向 In-Process

**关键项目：**
- 🐝 block/buzz (8,122, 新增) — 人机协同工作空间，Nostr 协议底座，Score 88
- 🔬 tirth8205/code-review-graph (26,051, 新增) — 代码知识图谱，MCP 集成，82x Token 削减，Score 86
- ⚡ 1jehuang/jcode (11,093, 新增) — Rust Agent Harness，性能碾压级，Score 84
- 🔧 rivet-dev/agentos (4,096, 新增) — Agent OS 库，WebAssembly 进程内运行，Score 82

---

## 2026-07-14

**核心主题：** 代码知识图谱范式替代 RAG——Graphify 84.5K⭐（tree-sitter AST/非向量/跨40+语言/LOCOMO recall@10: 0.497 = mem0 的 10 倍）重新定义 Agent 上下文理解 · AI 安全攻防双爆发——Strix 41.2K⭐（AI 渗透测试/Multi-Agent/真实 PoC）+ Hallmark 5K⭐（反 AI-slop/57 道 slop-test 门禁），Agent 安全攻守双翼 · Agent 原生创作工具——OpenCut 66K⭐（Rust 重写/MCP Server/Headless 批渲染），创作工具从 GUI-first 到 API-first

**关键项目：**
- 🕸️ Graphify-Labs/graphify (84,555, 更新) — 代码知识图谱 Skill，Score 92
- 🎬 OpenCut-app/OpenCut (66,019, 新增) — Agent 原生视频编辑器，Score 85
- ✨ Nutlope/hallmark (5,044, 新增) — 反 AI-slop 设计 Skill，Score 78
- 📈 HKUDS/Vibe-Trading (21,656, 新增) — 多市场交易 Agent，Score 80
- 🗡️ usestrix/strix (41,188, 更新) — AI 渗透测试 Agent，Score 85

---

## 2026-07-13

**核心主题：** Agent 沙箱基础设施收敛——CubeSandbox 9.8K⭐（腾讯/Rust/KVM/E2B兼容）成为 Agent 安全隔离标准方案 · 本地优先 AI 应用爆发——Meetily 23.5K⭐（Rust/纯本地/8.6K周增）引领隐私优先的 AI 会议助手赛道 · Agent 多路复用与编排成熟——herdr 15.8K⭐（终端 Agent 多路复用）+ Orca 16.8K⭐（并行 Agent ADE）+ OfficeCLI 15.4K⭐（Office 文件自动化），Agent 工具链从单体走向 fleet 管理

**关键项目：**
- 🎙️ Zackriya-Solutions/meetily (23,536, 新增) — 隐私优先 AI 会议助手，Score 86
- 📦 TencentCloud/CubeSandbox (9,795, 更新) — Agent 安全沙箱，Score 88
- 📊 iOfficeAI/OfficeCLI (15,395, 新增) — Agent 专用 Office 套件，Score 83

---

## 2026-07-12

**核心主题：** 推测解码双引擎——DeepSpec 6.5K⭐（训练侧/DSpark+DFlash+Eagle3 三算法统一训练 pipeline/38TB target cache/9 benchmark）与 Colibri 3.9K⭐（推理侧/纯C/744B MoE on 25GB RAM/MTP 2.8 tok/fwd）合流，speculative decoding 从论文走向工程 · ChatGPT→Coding Agent 桥接——DevSpace 3.2K⭐（自托管 MCP server/让 ChatGPT Web 操作本地代码）开辟 Agent 交付新路径 · Local LLM 知识沉淀——local-llm 1.3K⭐（9天/Shell/本地大模型运维百科）标志 local LLM 进入工程化阶段

**关键项目：**
- ⚡ deepseek-ai/DeepSpec (6,541, 更新) — 推测解码全栈训练框架，Score 90
- 🐦 JustVugg/colibri (3,850, 更新) — 纯C 744B MoE 推理标本，stars +87%，Score 88
- 🚀 Waishnav/devspace (3,161, 新增) — ChatGPT→Coding Agent MCP 桥接，Score 78

---

## 2026-07-12

**核心主题：** Agent Skills 三巨头格局成型——Superpowers 252K+ECC 228K+mattpocock/skills 165K，合计 64 万 star，Agent Skill 从'提示词技巧'升维为独立赛道 · Code Intelligence MCP 基础设施化——codebase-memory-mcp 30K⭐（纯C/tree-sitter 158语言/Hybrid LSP/v0.9.0/SLSA 3/5604 测试），从工具变为 Agent 必备底座 · 实用工具回归——Knockoff 1.7K⭐（6天/过滤亚马逊伪品牌/全本地无追踪），不蹭 AI 概念解决真实痛点获多家媒体报道

**关键项目：**
- 🧠 DeusData/codebase-memory-mcp (30,110, 更新) — Code Intelligence MCP 基础设施，Score 92
- 🛒 Shpigford/knockoff (1,761, 新增) — 亚马逊伪品牌过滤器，Score 35
- 🔌 jackwener/OpenCLI (26,487, 新增) — 任意网站→CLI + Browser Use，Score 56

---

## 2026-07-11

**核心主题：** LLM 可解释性工具化——Anthropic Jacobian Lens 1.1K⭐（9天/Python/全局工作空间论文/平均雅可比矩阵传输/逐层 token 读出），论文配套参考实现 · 教育知识图谱数据基座——Marble os-taxonomy 2.1K⭐（3天/1590微主题/3221前置依赖 DAG/8学科/多国标准对齐），开源结构化课程图谱 · Agent Skill 方法论分层——Loop Engineering 6.9K⭐（设计循环）+Ponytail 80K⭐（约束输出）+Omnigent 7K⭐（元编排），从单 Skill 竞争走向方法论分层

**关键项目：**
- 🔬 anthropics/jacobian-lens (1,058, 新增) — LLM 可解释性工具，平均雅可比矩阵传输，Score 82
- 📚 withmarbleapp/os-taxonomy (2,071, 新增) — 开源结构化课程知识图谱，Score 78
- 🐴 DietrichGebert/ponytail (80,115, 更新) — YAGNI Agent Skill，30天80K，Score 93

---

## 2026-07-10

**核心主题：** AI 红队元兵器——T3MP3ST 4.2K⭐（8 天/AGPL-3.0/多 Agent kill chain/90.1% XBOW 基准/verify-claims 复现机制），把已有编码 Agent 变零日猎人，安全 Agent 赛道正式从工具脚本走向元框架 · 科研全闭环 Agent——OpenScience 1.9K⭐（7 天/Apache-2.0/290+ 技能/30+ 科学数据库），从读文献到跑实验到写论文一站完成 · Agent Harness 生态收敛——ECC 228K+Hermes 212K+OpenCode 184K+OpenClaw 382K，编码 Agent 基础设施格局基本成型

**关键项目：**
- 🌩️ elder-plinius/T3MP3ST (4,152, 新增) — 多 Agent 攻击性安全元框架，Score 87
- 🔬 synthetic-sciences/openscience (1,935, 新增) — 开源 AI 科研工作台，Score 84
- ⚡ jmerelnyc/Talos (815, 新增) — 分布式 GPU 推理网络 worker，Score 72
- 🌙 vercel/eve (3,360, 更新) — filesystem-first Agent 框架，Score 85

---

## 2026-07-07

**核心主题：** Agent 约束即性能——Ponytail 75.8K⭐（25 天/MIT/54% less code/20% cheaper/27% faster/100% safe）系统化 YAGNI 约束而非提示词技巧，证明“约束输出”比“增强能力”带来更大收益 · OCR 长程解析突破——Baidu Unlimited-OCR 13.5K⭐（19 天/One-shot Long-horizon Parsing/超越 DeepSeek-OCR），VLM 吃掉传统 OCR pipeline · 贵模型规划+便宜模型执行——shadcn/improve 7K⭐（27 天/9 类并行子 Agent 审计/计划即产品），LLM 成本梯度利用范式固化成可安装 Skill · 多 Agent 元编排成赛道——Omnigent 6.4K⭐（26 天/统一编排 6+ Agent/云沙箱+策略治理），ECC 226K⭐+cc-switch 114K⭐ 验证元编排需求

**关键项目：**
- 🐴 DietrichGebert/ponytail (75,876, 更新) — YAGNI Agent Skill，54% less code，Score 92
- 📄 baidu/Unlimited-OCR (13,490, 新增) — One-shot 长程 OCR，Score 88
- 🔍 shadcn/improve (7,049, 新增) — 贵模型规划+便宜模型执行，Score 89
- 🎭 omnigent-ai/omnigent (6,422, 更新) — 多 Agent 元编排框架，Score 86

---

## 2026-07-06

**核心主题：** 推测解码训练框架基建化——DeepSeek DeepSpec 6.2K⭐（10 天创建/DSpark+DFlash+Eagle3 三算法/完整 pipeline/38TB 数据/含论文+checkpoint），推理加速从调 API 走向可训练全栈基础设施 · Agent 文档自动化成新赛道——langchain-ai/openwiki 5K⭐（14 天/CLI+GitHub Action/自动 AGENTS.md 注入/Multi-LLM），代码文档从人写人读→Agent 写 Agent 读 · Loop Engineering 方法论化——cobusgreyling/loop-engineering 5.9K⭐（loop-init/audit/cost/sync/context 五件套），Agent 编排从 ad-hoc prompting 走向系统化工程方法论 · Node.js 工具链 Rust 化——nubjs/nub 2.6K⭐（Rust/24× faster/不替换 runtime 只加速工具链）

**关键项目：**
- ⚡ deepseek-ai/DeepSpec (6,238, 新增) — 推测解码训练全栈框架，Score 90
- 📚 langchain-ai/openwiki (5,014, 新增) — Agent 文档自动化系统，Score 87
- 🔄 cobusgreyling/loop-engineering (5,896, 新增) — Agent 编排方法论+工具链，Score 85

---

## 2026-07-05

**核心主题：** 代码智能 MCP 爆发——codebase-memory-mcp 26.1K⭐（周+10.2K 增速 Top 3）C 语言编写/tree-sitter AST+知识图谱/亚毫秒查询/99% token 缩减/158 语言/14 MCP tools/单二进制零依赖，代码理解从文件搜索进化为图谱查询 · Agent 视频生产系统崛起——OpenMontage 33K⭐（周+9.2K）12 pipeline/52 tool/500+ agent skill 将 Coding Agent 变成视频工作室，video-use 14.7K⭐ 让 Agent 编辑视频 · 前端 Agent-Ready 加速——Astryx 5.3K⭐（日+1,013 TS 榜首）Meta 8 年设计系统开源 · Agent 终端多路复用成熟化——herdr 11.4K⭐（日+706 增速加快）tmux-for-agents · 安全+隐私双线并进——strix 35.9K⭐ AI 渗透测试，meetily 本地会议助手

**关键项目：**
- 🧠 DeusData/codebase-memory-mcp (26,117, 更新) — 代码智能 MCP，周+10.2K，Score 92
- 🎬 calesthio/OpenMontage (33,050, 更新) — Agent 视频生产系统，周+9.2K，Score 85
- 🦬 ogulcancelik/herdr (11,372, 更新) — Agent 终端多路复用，Score↑5 至 83

---

## 2026-07-04

**核心主题：** Agent 安全运行时双雄对垒——腾讯 CubeSandbox 7.1K⭐（Rust+KVM 亚 60ms 启动/5MB 开销/E2B 兼容）vs NVIDIA OpenShell 7.3K⭐（Rust+四层策略隔离/GPU 直通），两大巨头同时押注 Agent 安全沙箱，microVM+Rust 路线成标准 · 前端 Agent-Ready 设计系统——Meta Astryx 4.5K⭐（日+943 8 年内部/13K+ 应用/150+ 组件/StyleX）开源，Google design.md 24.6K⭐，设计系统从人用到人+Agent 共用 · Agent 多路复用持续升温——herdr 10.7K⭐ Rust 终端多路复用，Orca 11.6K⭐ 多 Agent 并行 ADE · Agent 感知层 MCP 化——chrome-devtools-mcp 45.4K⭐，page-agent 22.3K⭐ · Token 经济学常态化——caveman 82.8K⭐ 日+2,851 持续霸榜

**关键项目：**
- 🧊 TencentCloud/CubeSandbox (7,146, 更新) — Agent 安全沙箱，Score↑8 至 88，E2B 兼容+凭据保险库
- 🛡️ NVIDIA/OpenShell (7,374, 更新) — Agent 安全运行时，Helm K8s+GPU 直通
- 🎨 facebook/astryx (4,520, 更新) — Meta 设计系统开源，日+943 增速第二

---

## 2026-07-03

**核心主题：** Agentic Video Production 元年——OpenMontage 31.7K⭐（周+12.6K 榜首）12 管线/52 工具/500+ Agent 技能，video-use 13.7K⭐ 让 coding agent 剪视频，Agent 从代码生产扩展到内容生产 · 代码知识图谱爆发——codebase-memory-mcp 24.6K⭐（周+9.7K 爆发式增长）158 语言/亚毫秒查询/99% token 节省，cognee 26.6K⭐ 自托管记忆平台，Agent 记忆层从可选变必选 · Agent 多路复用基础设施化——herdr 10.1K⭐ Rust 终端 Agent 多路复用器，Orca 11K⭐ 多 Agent 并行 ADE，gstack 119K⭐ 现象级 Agent 工具栈 · Agent 全网感知——Agent-Reach 49K⭐（周+8.8K）CLI 零 API 费用覆盖 Twitter/Reddit/YouTube/Bilibili

**关键项目：**
- 🧠 DeusData/codebase-memory-mcp (24,603, 更新) — 代码知识图谱 MCP，周增 9.7K 近乎翻倍，Score 92
- 🎬 calesthio/OpenMontage (31,677, 更新) — Agentic 视频生产系统，周增 12.6K 登顶榜首
- 🐏 ogulcancelik/herdr (10,108, 更新) — Rust 终端 Agent 多路复用器

---

## 2026-07-02

**核心主题：** Agent Skills 成为新标准层（Anthropic 发起的开放规范被 nvidia/microsoft/google/vercel 采纳，obra/superpowers 升级为完整开发方法论。Agent 生态“npm 时刻”到来） · Meta 开源 Astryx 设计系统（内部 8 年/13000+ 应用/150+ 组件/StyleX/agent-ready，与 design.md 形成“组件层 vs 描述层”双轨） · Agent IDE 激战（Orca 10.8K⭐ 多 Agent ADE，herdr 9.9K⭐ Rust 终端多路复用，codex-plugin-cc 22.4K⭐ 跨 Agent 桥接） · AI 安全持续高温（strix 31K⭐ 日+2.2K，caveman 79.8K⭐ token 压缩 65%） · Agent 数据层深化（Agent-Reach 48.9K⭐ 周+8.8K，cognee 26.5K⭐，codebase-memory-mcp 24.4K⭐）

**关键项目：**
- 🎨 facebook/astryx (新增) — Meta 设计系统开源，150+ 组件/agent-ready/StyleX
- 📋 agentskills/agentskills (新增) — Agent Skills 开放规范，多巨头联合采纳
- 🐬 stablyai/orca (10,771, 更新) — 多 Agent 并行 ADE，周+3.5K
- 🔌 openai/codex-plugin-cc (22,353, 新增) — 跨 Agent 桥接插件，Claude Code 调用 Codex
- ☁️ google/agents-cli (4,627, 新增) — Google 官方 Agent CLI + Skills

---

## 2026-06-29

**核心主题：** AI 安全攻防工具化加速（strix 开源 AI 渗透测试 Agent——Docker 沙箱+多 Agent 协作+真实 PoC 验证。claude-bug-bounty 3.6K⭐ 终端化漏洞猎捕。配合 no-mistakes+Anthropic-Cyber-Skills 形成'防御→渗透→猎捕→技能'完整闭环） · 代码智能层持续高增长（codebase-memory-mcp 19.5K⭐ 日增 1.2K，arXiv 论文发表 31 仓库测试 83% 质量/10× token 节省。design.md 22.8K⭐ 连续 5 天 Trending。Agent 认知基建三件套'代码理解+设计规范+技能注入'成型） · AI 金融 Agent 爆发（ai-berkshire 5.2K⭐ 日增 1,456 四大师方法论多 Agent 对抗。daily_stock_analysis 51K⭐。Vibe-Trading 个人交易 Agent） · 本地 Voice I/O 成熟（FluidVoice 3.7K⭐ macOS 最快离线听写 Parakeet 零延迟。voicebox 35.4K⭐ 开源语音工作室） · LLM 路由层整合（OmniRoute 7.3K⭐ 160+ Provider 聚合 RTK 压缩 15-95% token）

**关键项目：**
- 🗡️ usestrix/strix (新增) — AI 渗透测试 Agent，Docker 沙箱+多 Agent 协作+PoC 验证
- 🎙️ altic-dev/FluidVoice (3,657, 新增) — macOS 最快离线听写，Parakeet 零延迟+本地 AI 增强
- 📈 xbtlin/ai-berkshire (5,235, 新增) — AI 价值投资研究框架，四大师方法论多 Agent 对抗
- 🔀 diegosouzapw/OmniRoute (7,335, 新增) — 免费 AI 网关，160+ Provider 聚合+RTK 压缩
- 🧠 DeusData/codebase-memory-mcp (19,466, 更新) — 代码库知识图谱 MCP，持续高增

---

## 2026-06-28

**核心主题：** 代码智能层大爆发（codebase-memory-mcp 17.5K⭐ 周增 7.6K，tree-sitter 知识图谱让 Agent 理解全局代码——158 语言/亚毫秒查询/99% token 节省。cognee 23.9K⭐ 周增 5.1K，自托管知识图谱 Agent 记忆平台。两者代表 Agent '大脑层'从实验走向生产） · Agent 安全治理层崛起（no-mistakes 3.8K⭐ git push 防护门——disposable worktree + AI 验证流水线全绿才放行。Anthropic-Cybersecurity-Skills 22.2K⭐ 817 条安全技能映射 MITRE ATT&CK/NIST CSF 等 6 大框架。Agent 生态从'能跑就行'进入'安全可控'阶段） · Agent-Native 应用框架首次定义（BuilderIO/agent-native 2.7K⭐ defineAction 一次定义六端复用——UI/Agent/HTTP/MCP/A2A/CLI。UI 与 Agent 等公民的架构模式，可能定义 Agent 时代全栈应用默认架构） · OpenMontage 周增 17.2K（25.1K⭐ GitHub 本周增长第一，首个开源 Agentic 视频生产系统 12 pipeline/52 tools。design.md 22.3K⭐ 连续 4 天日增 1.5K+） · Voice I/O 成熟（voicebox 34.9K⭐ 本地 AI 语音工作室 7 TTS 引擎/MCP server/voice cloning，ElevenLabs 开源替代）

**关键项目：**
- 🧠 DeusData/codebase-memory-mcp (17,459, 更新) — 代码库知识图谱 MCP，tree-sitter 158 语言
- 🕸️ topoteretes/cognee (23,943, 新增) — 自托管 Agent 记忆平台，知识图谱+向量搜索
- 🛡️ kunchenguid/no-mistakes (3,790, 新增) — Git push AI 防护门，disposable worktree 验证
- 🏗️ BuilderIO/agent-native (2,707, 新增) — Agent-Native 全栈框架，defineAction 六端复用
- 🎙️ jamiepine/voicebox (34,860, 新增) — 本地 AI 语音工作室，7 TTS + MCP server

---

## 2026-06-27

**核心主题：** Agent 感知层大规模整合（Agent-Reach 42K⭐ 给 Agent 装上全互联网感知——7+平台零API费用统一CLI，多后端路由架构成熟。alibaba/page-agent 20K⭐ 让Agent用自然语言控制网页UI。aws/agent-toolkit-for-aws 1.3K⭐ 提供官方MCP servers。Agent技术栈正在分化出独立的“感知层”和“操作层”——类似自动驾驶感知/决策/执行分离） · LLM 零成本基建加速（FreeLLMAPI 从783⭐暴涨至13,142⭐，2个月17倍增长，聚合16家免费Provider ~1.7B tokens/月。OpenAI+Anthropic双兼容意味着Claude Code可直接对接免费pool。LLM调用的边际成本趋近于零） · Agent 并行编排日常化（stablyai/orca 7.9K⭐ ADE支持30+CLI agent并行+移动端监控。multica开源Agent管理平台。gstack提供Garry Tan的23个角色化工具。从“单Agent工具”到“多Agent编排平台”的跃迁） · DESIGN.md + OpenMontage 持续领跑验证（design.md 21K⭐连续3天日增2K+，验证Agent×Design System标准化不是一日热点。OpenMontage 23.5K⭐ Agentic视频生产持续高增长） · Agent 垂直应用全面渗透（ai-berkshire/TREK/open-seo/ainovel-cli等，Agent正在渗透每个垂直领域）

**关键项目：**
- 🌐 Panniantong/Agent-Reach (42,263, 更新) — Agent互联网感知层，7+平台统一CLI
- 🌊 tashfeenahmed/freellmapi (13,142, 更新) — 16家免费LLM Provider聚合，2个月17倍增长
- 🐬 stablyai/orca (7,901, 更新) — 并行Agent开发环境(ADE)，30+CLI agent兼容
- 🎨 google-labs-code/design.md (21,112, 更新) — Agent设计系统规范，连续3天日增2K+
- 🎬 calesthio/OpenMontage (23,506, 更新) — Agentic视频生产系统持续高增长

---

## 2026-06-26

**核心主题：** Agent × Design System 标准化接口（Google Labs design.md 19K⭐ 定义 Agent 的设计系统规范——YAML tokens + Markdown 理由 = Agent 可读的设计宪法，类似 ROBOTS.TXT 之于爬虫） · Agentic 视频生产大爆发（OpenMontage 4天从 8.5K 暴涨至 22K +158%，12 pipeline × 52 tools × 500+ skills，$0.15/视频成本验证 Agent 编排完整视频生产管线） · Agent 安全治理工具化（NVIDIA SkillSpector 10.7K⭐ 68 类漏洞检测 + MCP Server 运行时护栏 + Anthropic-Cybersecurity-Skills 21K⭐ 817 安全 Skills × 6 框架映射，形成事前扫描+事后执行安全闭环） · Agent 记忆层竞速（TencentDB-Agent-Memory 6.2K⭐ 全本地 4 层管线 vs codebase-memory-mcp 14.7K⭐ tree-sitter 知识图谱——会话记忆 vs 代码结构记忆分化） · Apple container 基础设施级增长（43K⭐ 日增 1,366，Apple 官方开源 Linux 容器运行时稳步攀升）

**关键项目：**
- 🎨 google-labs-code/design.md (19,005, 首日) — Agent 设计系统规范，YAML tokens + Markdown 理由
- 🎬 OpenMontage (21,941, 更新) — Agentic 视频生产系统爆发，4天 +158%
- 💾 TencentDB-Agent-Memory (6,157, 首日) — 全本地 Agent 长期记忆，4 层渐进式管线
- 🛡️ NVIDIA/SkillSpector (10,661, 更新) — MCP Server 模式，68 类漏洞检测
- 🍎 apple/container (43,151, 更新) — Apple 官方容器运行时持续高增长

---

## 2026-06-25

**核心主题：** Agent '懒惰工程'范式大规模验证（ponytail 55K⭐ 7级懒惰阶梯实现 54% 代码削减+100% 安全保持——'Agent 更克制 > Agent 更聪明'设计哲学确认） · Meta-harness 编排层竞争白热化（omnigent 4.7K⭐ Python+多设备+治理 vs vercel/eve 2.5K⭐ TS+filesystem-first——'Agent 的 Kubernetes'品类形成） · 大厂 Coding Agent 终端争夺战（MiMo-Code 10.6K⭐ 持久内存+Goal/Stop 自治 vs shadcn/improve 6.1K⭐ 审计→计划→执行模型分层协作） · OCR 长程解析突破（baidu/Unlimited-OCR 6.3K⭐ one-shot long-horizon parsing，超越 DeepSeek-OCR） · Agent Skills 生态独立化确认（BuilderIO/skills 2.6K⭐ 入场，Skills 成为 B2D 分发渠道）

**关键项目：**
- 🐴 DietrichGebert/ponytail (54,972, 更新) — 7级懒惰阶梯，54% 代码削减+100% 安全
- 🤖 omnigent-ai/omnigent (4,713, 更新) — Meta-harness，编排 CC+Codex+Cursor+Pi
- 🌙 vercel/eve (2,526, 更新) — Filesystem-first agent 框架
- 📄 baidu/Unlimited-OCR (6,273, 首日) — One-shot 长程 OCR
- 🔍 shadcn/improve (6,147, 更新) — 审计→计划→执行分层 Skill

---

## 2026-06-24

**核心主题：** Agent 感知层成熟化（alibaba/page-agent 19.2K⭐ 零依赖注入式 DOM 控制 + Agent-Reach 38.6K⭐ 一键全网读取 + firecrawl 138K⭐ 抓取层——三层架构 firecrawl→Agent-Reach→page-agent 形成） · Agent Skills 工业化（addyosmani/agent-skills 65.9K⭐ 24skills×8commands 覆盖 SDLC，Google Chrome 架构师方法论产品化） · Agent 自我进化框架涌现（hermes-agent 自创建技能+自改进+跨会话记忆 + deer-flow 2.0 字节跳动 SuperAgent：subagents+sandbox+memory+skills 全栈） · Code Intelligence MCP 标准化加速（codebase-memory-mcp 12.8K⭐ 周增7.6K tree-sitter+知识图谱+158语言+sub-ms查询 · arXiv 论文验证 83% 质量/10× 更少 tokens） · Agent 安全审计新品类（NVIDIA/SkillSpector 9.8K⭐ Skills 杀毒）

**关键项目：**
- 🎯 alibaba/page-agent (19,240, 首日) — 注入式 GUI Agent，纯 DOM 文本操作
- 🛠️ addyosmani/agent-skills (65,910, 更新) — 24 production-grade skills，SDLC 方法论产品化
- 🌍 koala73/worldmonitor (59,022, 首日) — 实时全球情报仪表盘，6 站点变体单代码库
- 🎙️ jamiepine/voicebox (33,079, 首日) — 开源 AI 语音工作室，7 TTS 引擎 + MCP
- 🦌 bytedance/deer-flow (trending, 首日) — 字节跳动 SuperAgent harness

---

## 2026-06-23

**核心主题：** Agent Skills 经济爆发（gstack 113K⭐ YC CEO 23角色化工具栈 + mattpocock/skills 141K⭐ + Anthropic-Cybersecurity-Skills 18.6K⭐ 817技能6框架） · Agent 权限与集成层正式出现（corsair 2.8K⭐ open/cautious/strict/readonly 四模式 + multi-tenancy + webhook——Agent 的 API Gateway with human-in-the-loop） · Agentic Code Review 工具分化（hunk 5.4K⭐ review-first diff viewer） · AI 金融分析工业化（daily_stock_analysis 45.7K⭐ 41.8K forks forks/stars=0.92 部署率极高） · Agentic 内容生产加速（OpenMontage 日增 3.3K→11.7K + Palmier-Pro 日增 2.3K→7.2K）

**关键项目：**
- 🏗️ garrytan/gstack (113,069, 首日) — YC CEO 的 Agent 软件工厂，23 角色化工具
- 🔐 corsairdev/corsair (2,856, 首日) — Agent 权限与集成层，四档权限模式
- 🛡️ mukul975/Anthropic-Cybersecurity-Skills (18,601, 更新) — 817 安全技能，+3 新领域
- 🔍 modem-dev/hunk (5,431, 首日) — Review-first terminal diff viewer
- 📈 ZhuLinsen/daily_stock_analysis (45,733, 首日) — LLM 多市场股票分析

---

## 2026-06-22

**核心主题：** Agent 上下文压缩层正式确立为基础设施（Headroom 44K⭐ 日增 2.6K——6 算法 + proxy/MCP/library 三模式 + 输出 token 削减 + cross-agent memory） · 多 Agent 并行编排格局成型（Orca 5.7K ADE + herdr 6.6K 终端 multiplexer + jcode 7.5K Rust + claude-squad 7.8K） · AI Gateway 性能战打响（Bifrost 5.9K Go 网关 11µs overhead 50x LiteLLM + freellmapi 11.3K 免费 LLM 聚合） · Agent 框架两条路线分化（flue 6.2K 完整环境 vs agent-native 1.2K 应用原生 + DeerFlow SuperAgent） · Agentic 内容生产工业化（OpenMontage 8.4K 52 tools + Palmier-Pro 4.9K + voicebox 31.5K）

**关键项目：**
- 🗜️ chopratejas/headroom (44,115, 持续跟踪) — Agent 上下文压缩层，基础设施级
- 🐬 stablyai/orca (5,784, 首日) — 并行 Agent 开发环境 ADE
- ⚡ maximhq/bifrost (5,937, 首日) — 高性能 AI Gateway，11µs overhead
- 🎬 calesthio/OpenMontage (8,487, 首日) — Agentic 视频生产系统
- 🔧 1jehuang/jcode (7,516, 首日) — Rust Coding Agent Harness

---

## 2026-06-21

**核心主题：** Agent Skill 训练范式正式化（SkillOpt 8.4K⭐ 微软出品——epoch/lr/val gate 文本空间训练 6×52 cell 全第一 + Sleep 离线进化 + shadcn/improve 强模型审计弱模型执行） · Agent 元框架混战升级（Omnigent 4.2K meta-harness + Vercel Eve 1.8K 文件系统优先 + ECC 218K 登顶） · 本地推理引擎专业化（antirez/ds4 14.8K DeepSeek V4 专用——SSD 流式 KV cache 重新定义“模型装入内存”边界） · Epic Games 开源下一代 VCS（Lore 5.1K 内容寻址 + Merkle Tree + 大二进制优先——游戏行业 VCS 基础设施候选） · Coding Agent 增强工具爆发（CodexPlusPlus 20.4K + html-anything 7K + ponytail 43K YAGNI 注入）

**关键项目：**
- 🎮 EpicGames/lore (5,105, 首日) — Epic Games 下一代开源 VCS，内容寻址 + 大二进制优先
- ⚡ BigPizzaV3/CodexPlusPlus (20,363, 首日) — CodexApp 增强，Rust 实现
- 🎓 microsoft/SkillOpt (8,448, 更新) — Agent Skill 文本空间训练器，v0.1.0 + Sleep preview
- 🔧 antirez/ds4 (14,770, 更新) — DeepSeek V4 专用本地推理引擎，SSD 流式 KV cache
- 🌐 omnigent-ai/omnigent (4,186, 更新) — Agent meta-harness 统一编排

---

## 2026-06-20

**核心主题：** LLM Token 经济学基础设施爆发（headroom 38K⭐ 日增 3,938——压缩即基础设施 + codebase-memory-mcp 8K 用知识图谱替代 grep 120x token 削减） · Agent Skill 安全生态成型（NVIDIA SkillSpector 64 类漏洞检测——Skill 供应链安全的 SAST 时刻，26.1% Skills 有漏洞） · Agent 框架第二轮混战（Astro flue 沙箱 + BuilderIO agent-native 应用框架 + Kilo Code 22.9K 开源 Coding Agent） · 基础模型超越文本（Google TimesFM 2.5 时间序列基础模型已部署 BigQuery/Sheets/Vertex） · Coding Agent 可观测性赛道启动（agentsview 2.9K 本地化 20+ Agent 分析）

**关键项目：**
- 🗜️ chopratejas/headroom (38,394, 持续跟踪) — Token 压缩基础设施，日增 3,938
- 🧠 DeusData/codebase-memory-mcp (8,119, 首日) — 代码知识图谱 MCP，120x token 削减
- 🛡️ NVIDIA/SkillSpector (8,251, 持续跟踪) — Agent Skill 安全扫描器，64 类检测
- 🌀 withastro/flue (5,803, 首日) — Astro 团队沙箱 Agent 框架
- 🏗️ BuilderIO/agent-native (1,002, 首日) — Agent 原生应用框架

---

## 2026-06-19

**核心主题：** Agent Skill 经济学验证完成（ponytail 36K⭐ 一周暴涨 42 倍——benchmark 证明 Skill 是可量化的生产力工具） · Agent 编排层混战开启（omnigent meta-harness + vercel/eve filesystem-first + flock chat-driven dev team——三条路线争夺 Agent 运行时标准） · 端侧 AI 与上下文工程双线推进（Apple CoreAI SDK 开源 + Microsoft FastContext 论文——端侧推理与上下文委托模式同步成熟） · 终端多路复用器 AI 化（coder/boo 基于 libghostty） · Agent 安全新范式（burner-agents 一次性身份 swarm）

**关键项目：**
- 🐴 DietrichGebert/ponytail (36,393, 持续跟踪) — Agent Skill 经济学标杆，一周 42 倍
- 🤖 omnigent-ai/omnigent (3,785, 首日) — Agent meta-harness 统一编排
- 🌙 vercel/eve (1,327, 首日) — Filesystem-first Agent 框架
- ⚡ microsoft/fastcontext (587, 首日) — Context 委托子模型
- 🍎 apple/coreai-models (1,064, 首日) — 端侧 AI 开发者基础设施

---

## 2026-06-15

**核心主题：** Agent Skills 杀手级应用涌现（last30days-skill 42K⭐ 周增 12.6K 全站周榜 #1——证明 Skill 有真实杀手级用例 + taste-skill 44K⭐ 周增 8K 质量控制 Skill 同样有市场） · 上下文工程工具链三位一体（headroom 压缩 + turbovec 向量索引 + LMCache KV 缓存——压缩→索引→缓存完整管道成型，LLM 推理成本优化进入系统工程阶段） · 本地多模态 AI 运行时扩展（whichllm 选型 + Open-LLM-VTuber 语音 + MoneyPrinterTurbo 视频——端侧 AI 从文本扩展到多模态） · 安全工具 AI 化（SkillSpector + flowsint + maigret） · 垂直领域 AI 基础模型萌芽（Kronos 金融 + openmed 医疗）

**关键项目：**
- 🔎 mvanhorn/last30days-skill (41,943, 持续跟踪) — Agent Skills 第一个杀手级应用
- ⚡ LMCache/LMCache (9,043, 首日) — LLM 推理 KV Cache 加速层
- 🎨 Leonxlnx/taste-skill (43,637, 持续跟踪) — AI 输出质量守门员
- 🚀 RyanCodrai/turbovec (11,493, 持续跟踪) — Rust 向量索引引擎
- 🖥️ Andyyyy64/whichllm (4,747, 持续跟踪) — 本地 LLM 硬件选型

---

## 2026-06-14

**核心主题：** Agent Skills 全栈基础设施化（agent-skills 58K⭐ 分发层 + NVIDIA SkillSpector 4.4K⭐ 安全层 + headroom 26K⭐ 压缩层 + Agent-Reach 27K⭐ 感知层——四层完整栈形成） · Apple Container 36K⭐ 硅级容器化定局（Swift 原生 + Apple silicon 优化，Mac 容器基础设施从社区走向官方） · Agent 感知层独立（Agent-Reach 27K⭐ 一个 CLI 聚合 7+ 平台数据零 API 费用） · 开源 NotebookLM 赛道升温（open-notebook 30K⭐ + tolaria 16K⭐） · RL 后训练环境接口标准化萌芽（HuggingFace OpenEnv 2.2K⭐）

**关键项目：**
- 🌐 Panniantong/Agent-Reach (27,338, 首日) — Agent 互联网感知层，多平台数据聚合
- 🗜️ chopratejas/headroom (26,091, 持续跟踪) — Token 压缩中间件，定位升级为基础设施候选
- 📓 lfnovo/open-notebook (30,096, 首日) — 开源 NotebookLM 替代，趋于成熟
- 🍎 apple/container (36,214, 持续跟踪) — 苹果官方轻量 VM 容器
- 🛡️ NVIDIA/SkillSpector (4,360, 持续跟踪) — Agent Skills 安全扫描器
- ⚙️ addyosmani/agent-skills (58,243, 持续跟踪) — Agent Skills 分发层

---

## 2026-06-13

**核心主题：** Agent 架构分层范式确立（shadcn/improve 2.4K⭐ 贵模型审计+廉模型执行 Advisor-Executor 分离 + ponytail 862⭐ YAGNI 极简主义 47% Token 节省 + gstack 109K⭐ 23 工具角色化） · 端侧 AI 运行时基础设施化（Apple CoreAI Models 826⭐ 端侧模型导出+Swift 运行时 + Xiaomi MiMo-Code 6.7K⭐ 三天爆发） · AI 自愈可观测性崭露头角（Superlog 792⭐ AI Agent+OTel 自动诊断修复） · Coding Agent 工具链全栈化（cc-switch 99K⭐ + rtk 61K⭐ Token 压缩 + RuView 73K⭐ WiFi 感知） · Sandbox 即基础设施（sandboxd 586⭐）

**关键项目：**
- 📋 shadcn/improve (2,385, 持续跟踪) — Agent 分层范式代表，贵模型审计+廉模型执行
- 📱 XiaomiMiMo/MiMo-Code (6,687, 首日) — 小米开源编码 Agent
- 🍎 apple/coreai-models (826, 持续跟踪) — Apple 端侧 AI 运行时
- 🐴 DietrichGebert/ponytail (862, 首日) — YAGNI 极简主义 Agent Skill
- 🔍 superlog (792, 持续跟踪) — AI 自愈可观测性
- 📦 sandboxd (586, 持续跟踪) — 自托管开发沙箱

---

## 2026-06-12

**核心主题：** Agent Skills 生态爆发（addyosmani/agent-skills 54K⭐ 日+3.3K 引爆工程技能标准化，taste-skill/pm-skills/last30days-skill 覆盖全品类） · LLM Token 压缩基础设施化（headroom 23K⭐ 周+13K 60-95% token 压缩 library/proxy/MCP 三模式） · Apple 容器化落地（apple/container 32K⭐ Swift Apple Silicon 原生 Linux 容器） · Agent 安全面浮出（NVIDIA/SkillSpector 2.6K⭐ 技能安全扫描） · Coding Agent 工具链分化（cc-switch 98K⭐ 多Agent桌面管理 + agentsview 会话分析）

**关键项目：**
- 🛠️ addyosmani/agent-skills (54,532, 首日) — Agent 工程技能标准化事实标准
- 🗜️ chopratejas/headroom (23,083, 持续跟踪) — LLM Token 压缩基础设施
- 🍎 apple/container (32,164, 首日) — Apple 原生 Linux 容器运行时
- 🛡️ NVIDIA/SkillSpector (2,577, 首日) — Agent 技能安全扫描
- 📊 kenn-io/agentsview (1,592, 首日) — Coding Agent 会话分析

---

## 2026-06-11

**核心主题：** Agent 编排分层（shadcn/improve 745⭐ 顾问模式引爆 Agent 工作流：昂贵模型审计+计划，便宜模型执行） · Apple 端侧 AI 开放（coreai-models 605⭐ 从模型导出到 Swift 运行时到 Agent Skills 全栈） · AI 可观测性自愈（superlog 721⭐ YC P26 OTel+ClickHouse+Agent 三层融合） · 开发沙箱基础设施化（sandboxd 561⭐ Go/Docker 为 Coding Agent 隔离） · AI 设计资产走向生产（diffusionstudio/lottie 2K⭐）

**关键项目：**
- 🔍 shadcn/improve (745, 首日) — Agent 顾问模式，audit→plan→execute 编排
- 🍎 apple/coreai-models (605, 3天) — Apple 端侧 AI 全栈工具链
- 🔧 superlog (721, 8天) — AI 原生可观测性，OTel + 自愈
- 📦 sandboxd (561, 8天) — Coding Agent 开发沙箱
- 🎬 diffusionstudio/lottie (2,004, 7天) — AI 生成 Lottie 动画

---

## 2026-06-10

**核心主题：** LLM Token 压缩基础设施化（headroom 20.4K 周增 14,266 全网第一，从优化变标配）· Agent Skill 从碎片化到平台化（ECC 211K + taste-skill 39.5K + impeccable 36.8K，质量分层出现）· 开源知识管理双赛道分化（tolaria 14.3K Git-first vs open-notebook 28.5K NotebookLM 替代）· 本地 LLM 选型工具链成熟（whichllm 4K 证据驱动匹配 + career-ops 51.5K AI 求职）· Agent 信息获取层基础设施化（last30days-skill 37.1K + Agent-Reach 25.5K）

**关键项目：**
- 🗜️ headroom (20.4K, 周增 14,266 全网第一) — Agent Token 压缩基础设施
- ⚡ turbovec (10.1K, 周增 4,283) — Rust SIMD 向量索引，超 FAISS
- 📚 tolaria (14.3K, 日增 821) — Git-first Markdown 知识管理
- 🎯 whichllm (4K, 日增 631) — 本地 LLM 硬件匹配
- 💼 career-ops (51.5K, 日增 1,114) — AI 求职系统

---

## 2026-06-09

**核心主题：** Coding Agent 工具链基础设施化（cc-switch 95K 多 Agent 管理 + codegraph 44.8K 代码知识图谱 + oh-my-pi 11.3K 终端 Agent，三层工具栈成型）· AI Memory 基础设施竞争白热化（supermemory 26K vs MemPalace vs open-notebook 28K，Memory API 进入战国时代）· 语音 AI 全栈爆发（VoxCPM 27.7K + Open-LLM-VTuber 10.5K + FunASR 17.5K）· Agent 安全运行时浮出水面（NVIDIA OpenShell 6.9K + Anthropic sandbox-runtime 4.4K）· Agent 调研 Skill 成熟（last30days-skill 34.3K + Agent-Reach 24K）

**关键项目：**
- 🕸️ codegraph (44.8K, +8.7K/周) — 代码知识图谱预索引，Coding Agent 优化层
- 🔀 cc-switch (95.1K, +7.9K/周) — 跨平台多 Coding Agent 统一管理
- 🧠 supermemory (26.2K, +2.9K/周) — AI 时代 Memory API 引擎
- 🛡️ NVIDIA OpenShell (6.9K, new) — Agent 安全会话运行时，Rust 实现
- 🎤 VoxCPM (27.7K, +4.3K/周) — 无 Tokenizer 多语言 TTS

---

## 2026-06-08

**核心主题：** Agent Skill 生态核聚变（ECC 209K + hermes-agent 185K + taste-skill 36K 同屏霸榜，Compound Engineering 进入基础设施阶段）· Token 压缩基础设施化（headroom 一周 4.1K→16.8K +300%）· PostgreSQL 成为 Agent 运行时（微软 pg_durable Durable Execution 原生嵌入）· 向量检索 SIMD 新世代（turbovec 日增 1,533 stars 全网第一）· Agentic Backend Platform 浮现（InsForge 11.5K MCP-first 全栈后端）

**关键项目：**
- 🗜️ headroom (16.8K, +300%/周) — Agent Token 压缩基础设施，从优化变为标配
- ⚡ turbovec (7K, +1,533/天) — Rust SIMD 向量索引，全网日增速第一
- 🐘 pg_durable (1.4K, new) — 微软 PostgreSQL Durable Execution 扩展
- 🏗️ InsForge (11.5K, new) — 面向 Coding Agent 的 MCP-first 全栈后端
- ⌨️ oh-my-pi (11K, +2.3K/周) — 终端 AI Coding Agent 持续高热

---

## 2026-06-07

**核心主题：** Agent 多源感知基础设施化（last30days-skill 跨平台信号聚合 + Agent-Reach 零 API 费全网读取）· AI Memory 本地优先成熟化（MemPalace 96.6% R@5 零 API 调用）· 代码执行沙箱进入 OS 级（Microsoft MXC 跨平台策略驱动隔离）· Agent 终端多路复用器新物种（herdr 4.7K +250/天）· HTML 原生视频渲染 Agent 化（HyperFrames 25K Agent 友好确定性 MP4）

**关键项目：**
- 🔎 last30days-skill (new) — Agent 跨平台搜索 Skill，实体感知路由 + 10+ 平台信号聚合
- 🧠 MemPalace (持续高热) — 本地优先 AI 记忆，96.6% R@5 基准 + MCP 29 工具
- 🛡️ Microsoft MXC (557) — 跨平台沙箱执行，策略驱动多后端统一抽象
- 🔀 herdr (4.7K, +250/天) — Agent 终端多路复用器，tmux + GUI 混合体
- 🎬 HyperFrames (25K, +257/天) — HTML 原生视频渲染，Agent 友好确定性 MP4

---

## 2026-06-06

**核心主题：** AI Code Review 进入混合架构时代（Alibaba open-code-review 2.7K 确定性流水线 + Agent 决策）· Agent Memory 分层操作系统化（Memory OS 869 stars 7 层架构 + Qdrant 向量记忆）· 本地优先运动席卷硬件外设（OpenLogi 4K 替代 Logitech Options+）· 自托管团队 Agent 平台化（Paradigm Centaur 718 K8s 沙箱 + Slack 原生）· Coding Agent CLI 新格局（Moonshot Kimi Code 1.9K 单二进制）

**关键项目：**
- 🔍 Alibaba Open Code Review (2.7K) — 阿里内部两年验证，确定性 + Agent 混合架构，生产可用
- 🧠 Memory OS (869) — Hermes Agent 7 层记忆操作系统，Qdrant + SQLite FTS5 + 信任评分
- 🐎 Paradigm Centaur (718) — 自托管团队 Agent 平台，Slack + K8s 沙箱 + iron-proxy 凭据隔离
- 🖱️ OpenLogi (4K) — Rust 实现 Logitech Options+ 本地替代，HID++ 协议
- 🌙 Kimi Code CLI (1.9K) — Moonshot 终端编程 Agent，单二进制 + 视频输入

---

## 2026-06-05

**核心主题：** Agent Skill 从手工编写进化为可训练优化（Microsoft SkillOpt 4.9K 文本空间技能优化器）· 自托管 AI 工作空间现象级项目（Odysseus 50.6K）· Agent 专用语言与运行时涌现（zerolang 4.9K + zero-native 4.1K + forkd 1.3K microVM）· AI 供应链安全成新赛道（Perplexity bumblebee 4.3K）

**关键项目：**
- 🎯 Microsoft SkillOpt (4.9K) — 文本空间技能优化器，轨迹驱动编辑 + 验证门控更新
- 🏠 Odysseus (50.6K) — 自托管 AI 工作空间，MIT 协议，5.9K forks
- 🔤 Vercel zerolang (4.9K) — Agent 编程语言，Vercel Labs 出品
- 🐝 Perplexity bumblebee (4.3K) — 开发者端点扫描器，AI 时代供应链安全
- 🍴 forkd (1.3K) — AI Agent 的 fork()，KVM microVM + CoW 快照

→ [查看完整日报](daily/2026-06-05.html)

---

## 2026-06-03

**核心主题：** Agent 运行时安全沙箱成新赛道（NVIDIA OpenShell 6.6K Rust 沙箱 + 策略引擎 + GPU 直通）· Agent Terminal 基础设施三层成型（herdr 3.9K + fff 7.4K + headroom 6.1K）· AI Memory API 标准化加速（supermemory 24.6K）· AI 视频生成大爆发（MoneyPrinterTurbo 78K +19K/week）

**关键项目：**
- 🔒 NVIDIA OpenShell (6.6K) — Agent 安全运行时沙箱，四层策略防御，GPU 直通
- 🔍 fff (7.4K) — AI Agent 专用文件搜索，Frecency 排序，MCP 原生
- 🧠 supermemory (24.6K) — AI 时代 Memory 引擎，长期记忆 API
- 🏗️ iii (17.5K) — Worker/Function/Trigger 三原语服务组合平台
- 🕸️ flowsint (4.5K) — OSINT 图谱调查平台

→ [查看完整日报](daily/2026-06-03.html)

---

## 2026-06-02

**核心主题：** AI Agent 上下文压缩赛道浮现（Headroom 4.1K 提供 60-95% Token 压缩、MCP 原生、CCR 可逆架构）· TTS 开源模型爆发（VoxCPM 24K Tokenizer-Free + MOSS-TTS 2.8K + dograh 4K 语音平台）· Agent Harness 深度竞争（ECC 202K + oh-my-pi 9.4K + harness 5.1K）· Code Knowledge Graph 持续高热（Understand-Anything 48.7K + codegraph 36.6K）

**关键项目：**
- 🗜️ Headroom (4.1K) — Agent 上下文压缩层，60-95% Token 节省，MCP 原生
- 🗣️ VoxCPM (24.2K) — Tokenizer-Free 多语言 TTS，OpenBMB 出品
- 🧠 Understand-Anything (48.7K) — 代码知识图谱标杆，+22.7K/week
- 🛡️ Agent Governance Toolkit (3.7K) — Microsoft Agent 治理，覆盖 OWASP Top 10
- 🎙️ Dograh (4.1K) — 开源语音 AI 平台，Vapi/Retell 替代

→ [查看完整日报](daily/2026-06-02.html)

## 2026-06-01

**核心主题：** Code Knowledge Graph 赛道爆发（Understand-Anything 47K + codegraph 35K 共享 41K 周增量，AI Agent 代码理解索引层成型）· google/ax 分布式 Agent Runtime 开源（Google 出品，K8s Native）· Microsoft AGT 覆盖 OWASP Top 10（确定性拦截而非 prompt 约束）· herdr Agent 终端多路复用器 · AI Coding Plugin 生态全面爆发（ECC 200K + 6 个 Plugin 项目同日 Trending）

**关键项目：**
- 🧠 Understand-Anything (47.1K) — Code Knowledge Graph 标杆，+25.6K/week
- 🕸️ codegraph (35.3K) — 预索引代码图谱，57% token 节省，+15.9K/week
- ⚡ google/ax (1.3K) — Google 分布式 Agent Runtime，基础设施候选
- 🛡️ Agent Governance Toolkit (3.6K) — Microsoft Agent 治理，生产可用
- 🐏 herdr (3.4K) — Agent 终端多路复用器，+923/week

→ [查看完整日报](daily/2026-06-01.html)

## 2026-05-31

**核心主题：** AI Taste 元趋势爆发（taste-skill 29K + stop-slop 7.4K 共享“反 AI 味”需求）· ai-engineering-from-scratch 25K 周增 13K 领跑教育赛道 · LiteParse +929/天突破文档解析天花板 · Microsoft Agent Governance Toolkit 3.5K 覆盖 OWASP Top 10 · stable-worldmodel 世界模型研究平台

**关键项目：**
- 🎨 taste-skill (~29K) — AI Taste 控制，+9K/week，元趋势代表
- 📚 ai-engineering-from-scratch (~25.1K) — AI 工程教育，周增 13.1K
- 📄 liteparse (~7.9K) — Rust 文档解析器，日增 +929 加速中
- 🛡️ agent-governance-toolkit (~3.5K) — Microsoft Agent 治理，基础设施候选
- 🌍 stable-worldmodel (~1.4K) — 世界模型研究平台
- ⚡ compound-engineering-plugin (~18.4K) — Compound Engineering 插件
- 🏕️ project-nomad (~27.3K) — 离线 AI 生存计算机
- ⌥ oh-my-pi (~8.7K) — 终端 AI Coding Agent

→ [查看完整日报](daily/2026-05-31.html)

## 2026-05-30

**核心主题：** Code Knowledge Graph 双雄争霸（Understand-Anything 44K + codegraph 33K 共享 45K 周增量） · ECC 198K 横空出世定义 Agent Harness 标杆 · Anthropic 三发 Plugin 生态 · RuView 68K WiFi CSI 空间智能 · Cursor 发布 Plugin 规范

**关键项目：**
- 🚀 ECC (~198.5K) — Agent Harness 性能优化系统，198K 星异常高需冷静
- 🕸️ codegraph (~33.1K) — 预索引代码知识图谱，Agent 索引层
- 🔌 claude-plugins-official (~28.6K) — Anthropic 官方插件目录
- 📡 RuView (~68.2K) — WiFi CSI 空间智能，概念性感但需验证
- 🎙️ dograh (~3.7K) — 开源语音 AI 平台，Vapi/Retell 自托管替代
- 📄 liteparse (~7.2K) — run-llama 出品快速文档解析器

→ [查看完整日报](daily/2026-05-30.html)

## 2026-05-29

**核心主题：** Agent Skills 大爆发（taste-skill 26K + stop-slop 6.3K）· agentmemory 冲刺 19K 锁定 Agent 记忆层 · oh-my-pi 8.2K 定义终端 Agent IDE 化 · Microsoft Agent Governance 覆盖 OWASP Top 10 · turbovec 3.4K 用 Rust 击败 FAISS

**关键项目：**
- 🎨 taste-skill (~26.2K) — 让 AI 有好品味，阻止生成无聊通用内容
- 🧠 agentmemory (~19.3K) — Agent 持久记忆服务，全平台 MCP/Hooks/Plugin
- ⌨️ oh-my-pi (~8.2K) — 终端 AI Coding Agent，IDE 级能力内置
- 🛡️ agent-governance-toolkit (~3.2K) — Microsoft Agent 治理工具包
- ⚡ turbovec (~3.4K) — Rust 向量索引，击败 FAISS

→ [查看完整日报](daily/2026-05-29.html)

## 2026-05-28

**核心主题：** 五日断网周度复盘 · Agent Harness 三强格局锁定（ECC 188.5K/Hermes 163K/OpenCode 164K）· Skills 垂直分化加速 · 小模型 Agent 工程化破局（SmallCode/HRM-Text）· 安全 Agent 攻防双线闭环

> ⚠️ 外部数据源自 05-24 起连续 5 天不可达，Stars 为最后实测推算值。

**关键项目：**
- 🔬 SmallCode (~1,209 stars) — 专为 8B-35B 小模型优化的终端编码 Agent
- 🐴 Centaur (~364 stars) — Paradigm 出品多人自托管 Agent 平台
- 🔍 audit (~433 stars) — 8 阶段漏洞发现 Agent
- 🧪 HRM-Text (~650 stars) — $1000 预训练基础模型

→ [查看完整日报](daily/2026-05-28.html)

---

## 2026-05-23

**核心主题：** 小模型 Agent 工具链觉醒：SmallCode 1.2K⭐ 专为 8B-35B 优化 · HRM-Text 650⭐ $1000 预训练基础模型 · Agent 安全双线突破：audit 433⭐ + Bumblebee 251⭐ · Centaur 364⭐ 团队级 Agent 基础设施

**关键项目：**
- 🔬 SmallCode (1,209 stars) — 专为 8B-35B 小模型优化的终端编码 Agent
- 🐴 Centaur (364 stars) — Paradigm 出品的多人自托管 Agent 平台
- 🔍 audit (433 stars) — 8 阶段漏洞发现 Agent，基于 Cloudflare Glasswing
- 🧪 HRM-Text (650 stars) — $1000 预训练 1B 基础模型
- 🐝 Bumblebee (251 stars) — Perplexity 供应链安全扫描器
- 🦑 9arm-skills (1,487 stars) — Claude Code 技能集合

→ [查看完整日报](daily/2026-05-23.html)

---

## 2026-05-22

**核心主题：** Claude Skills 生态持续分化与专业化 · 12-Factor Agents 21.5K⭐ 定义 Agent 工程原则 · OpenHuman 24.7K⭐ 突破 2 万 · Agent-Native 浏览器层成基础设施

**关键项目：**
- 🕸️ CodeGraph (13,173 stars) — 预索引代码知识图谱，降低 Agent token 消耗
- 🔌 Claude Plugins Official (22,237 stars) — Anthropic 官方插件目录
- 📐 12-Factor Agents (21,551 stars) — Agent 工程化 12 条原则
- 🧬 OpenHuman (24,770 stars) — Rust 个人 AI 超级智能，本周 +19K
- 🤝 Multica (30,664 stars) — 开源托管 Agent 平台
- 🎭 CloakBrowser (18,174 stars) — 隐身 Chromium，30/30 反检测
- 🔊 Supertonic (9,142 stars) — 设备端多语言 TTS

→ [查看完整日报](daily/2026-05-22.html)

---

## 2026-05-19

**核心主题：** Agent Skills 生态大爆发 · CLI-Anything Agent-Native 范式 · RuView WiFi 传感突破 · Agent Memory 持久化成新基建

**关键项目：**
- 🖥️ CLI-Anything (36,562 stars) — Agent-Native 桌面控制，CLI-Hub 市场
- 📡 RuView (59,842 stars) — WiFi 信号空间智能，零视频零摄像头
- 🧬 OpenHuman (16,930 stars) — Rust 个人 AI 超级智能
- 🧠 agentmemory (12,712 stars) — AI Coding Agent 持久记忆
- 💾 Memori (14,595 stars) — Agent 原生记忆基础设施
- 🎭 CloakBrowser (15,098 stars) — 隐身 Chromium，30/30 反检测

→ [查看完整日报](daily/2026-05-19.html)\n
---

## 2026-05-18

**核心主题：** Dirty Frag Linux LPE 席卷安全圈 · Agent 语言 Zero 一日暴涨 74% · AI 伴侣引擎浮出水面 · 统一存储抽象加速 · HTML Agent 工具链持续分化

**关键项目：**
- 🔴 Dirty Frag (4,611 stars) — 通用 Linux LPE 提权，确定性逻辑 bug，9 年影响窗口
- 0️⃣ Zero (1,600 stars) — Vercel Labs Agent 语言单日暴涨 74%，市场验证
- 🧠 grok-animus (573 stars) — 持久化 AI 伴侣引擎，人格/记忆/梦境/演化
- 🤝 trustclaw (665 stars) — 自托管个人 AI Agent，向量记忆 + Composio + Telegram
- 📁 files-sdk (772 stars) — 统一存储 SDK，Web 标准 I/O 抽象

→ [查看完整日报](daily/2026-05-18.html)

---

## 2026-05-17

**核心主题：** 本地推理双雄对决 · Agent VFS 基础设施化 · Agent 原生语言 Zero 问世 · AI 安全新物种 AiSOC · Token 效率成 Agent 新战场

**关键项目：**
- 🔥 ds4 (10,038 stars) — antirez 打造 DeepSeek V4 Flash 专用推理引擎，磁盘 KV 缓存范式
- 🗂️ Mirage (2,312 stars) — Agent 统一虚拟文件系统，Unix 语义抹平多后端
- 0️⃣ Zero (916 stars) — Vercel Labs 面向 Agent 的系统编程语言
- ⚡ TokenSpeed (1,031 stars) — 光速 LLM 推理引擎，Blackwell MLA 极致性能
- 🛡️ AiSOC (971 stars) — 开源 AI 安全运营中心

→ [查看完整日报](daily/2026-05-17.html)\n
---

## 2026-05-15

**核心主题：** 网络受限日 · Agent 生态整合期深读 · Spec-Driven Dev 范式变迁架构分析 · 本地推理三赛道分化复盘 · 安全赛道从漏洞驱动到平台化演进

> ⚠️ 外部网络不可达，Stars 数据基于 05-14 实测推算，趋势分析基于近 5 日连续数据。

**关键项目：**
- 🤖 Hermes Agent (~149K stars) — Agent 框架头部地位巩固
- 📋 Spec Kit (~99K stars) — 逼近 100K 里程碑，开发范式级项目
- 🌐 Browser Harness (~94K stars) — Agent-Web 交互基础设施化
- 🎨 Open Design (~40K stars) — 从爆发期进入平台巩固期
- ⚡ Zero Native (~3.5K stars) — Zig 桌面框架持续跟踪
- 🔧 ds4.c (~8.6K stars) — 本地推理原生层代表
- 🔑 YellowKey (~1.2K stars) — 安全赛道持续升温
- 🖨️ OrcaSlicer-bambulab (~3.5K stars) — 硬件开放运动标志

→ [查看完整日报](daily/2026-05-15.html)

---

## 2026-05-14

**核心主题：** Windows BitLocker 绕过漏洞引爆安全社区 · OrcaSlicer 恢复 BambuNetwork 驱动 3D 打印社区反弹 · Zero Native 3.3K Vercel 用 Zig 重定义桌面开发 · Files SDK 统一存储 API + Agent 工具链 · Agent 人格化 Goblin Agent 登场

**关键项目：**
- 🔑 YellowKey (927 stars) — Windows BitLocker 绕过漏洞，疑似 WinRE 后门
- 🖨️ OrcaSlicer-bambulab (2,832 stars / 887 forks) — 3D 打印社区反弹，恢复 Bambu Lab 完整功能
- ⚡ Zero Native (3,261 stars) — Vercel Labs Zig 桌面应用框架
- 📁 Files SDK (642 stars) — 统一存储 SDK + AI Agent 工具封装
- 👺 Goblin Agent (437 stars) — Hermes Agent 人格层，Agent 文化标志
- 🎨 Pixal3D (504 stars) — 腾讯 SIGGRAPH 2026，图像到 3D

→ [查看完整日报](daily/2026-05-14.html)

---

## 2026-05-13

**核心主题：** 断网结束实测回归 · Agent 工具链全面扩张 · GitHub Spec Kit 97K 官方入场 Spec-Driven Dev · Browser Harness 12.3K 突入核心 · GPT-Image-2 生态爆发

**关键项目：**
- 🎨 Open Design (38.4K stars) — 平台地位确认，增速趋稳
- 🌐 Browser Harness (12.3K stars) — Agent 浏览器交互基础设施
- 📋 GitHub Spec Kit (97.2K stars) — 官方入场 Spec-Driven Development
- 🤖 Hermes Agent (147K stars) — Agent 从工具走向伙伴
- 🔧 ds4.c (8K stars) — 本地推理 Metal+CUDA 双轨

→ [查看完整日报](daily/2026-05-13.html)

---

## 2026-05-12

**核心主题：** 第三天断网推演 · Agent 筛选期关键拐点 · DeepSeek V4 推理三层架构成型 · 安全双范式企业评估窗口 · 推演可信度开始下降

> ⚠️ 外部数据源连续第三天不可达，本轮为 Star 推演最后有效轮次。

**关键项目：**
- 🎛️ CC Switch (~65K stars) — 桌面基座，筛选期大概率通过
- 🧠 MemPalace (~53K stars) — Memory 基础设施级，高位稳定
- 🎨 Open Design (~38K stars) — 验证期关键观察，增速是否跌破 1K
- 🔧 ds4.c (~3.8K stars) — Metal-only 天花板待突破
- 🗂️ Mirage (~2.5K stars) — VFS 方向确认，后端适配器是关键
- 🛡️ Deepsec (~2.8K stars) — 安全审计代表，可做 PoC
- 🎭 Harmonist (~2.3K stars) — 协议强制范式，价值密度需长期验证
- ⚡ TokenSpeed (~1.3K stars) — 服务端推理引擎方向确认

→ [查看完整日报](daily/2026-05-12.html)

---

## 2026-05-11

**核心主题：** 连续断网模式下的趋势推演 · Agent 基础设施层进入筛选期 · 推理引擎从工具走向生态 · 安全赛道验证双范式闭环

> ⚠️ 外部数据源连续第二天不可达，本报告基于 2026-05-03~10 已采集数据完成趋势推演分析。

**关键项目：**
- 🎛️ CC Switch (~63K stars) — 桌面基座标准候选出线
- 🧠 MemPalace (~52K stars) — Memory 基础设施级确认
- 🎨 Open Design (~36K stars) — 爆发趋稳，进入平台粘性验证期
- 🔧 ds4.c (~3.2K stars) — 本地推理引擎持续增长
- 🗂️ Mirage (~2.1K stars) — Agent VFS 方向确认增长
- 🛡️ Deepsec (~2.5K stars) — Agent 安全审计稳步增长
- 🎭 Harmonist (~2.0K stars) — 零依赖协议强制范式获认可
- ⚡ TokenSpeed (~1.1K stars) — Agentic 推理引擎方向确认

→ [查看完整日报](daily/2026-05-11.html)

---

## 2026-05-10

**核心主题：** 周度复盘：Agent 生态分层成型 · Open Design 领跑设计平台 · 推理引擎三线竞速 · Linux 安全警钟 · Agent 安全双范式确立

> ⚠️ 外部数据源不可达，本报告基于 2026-05-03~09 已采集数据完成周度综合分析。

**关键项目：**
- 🎨 Open Design (~35K stars) — 平台地位巩固，周增 22K
- 🎛️ CC Switch (~62K stars) — 生态锁定效应增强
- 🧠 MemPalace (~51K stars) — 基础设施级稳定增长
- 🔧 ds4.c (~2.8K stars) — 本地推理新范式
- 🛡️ Deepsec (~2.2K stars) — Agent 安全审计代表
- 🎭 Harmonist (~1.8K stars) — 协议强制执行范式
- 🗂️ Mirage (~1.8K stars) — VFS 抽象层方向确认
- ⚡ TokenSpeed (~900 stars) — Agentic Workload 推理引擎

→ [查看完整日报](daily/2026-05-10.html)

---

## 2026-05-09

**核心主题：** Linux 内核安全漏洞密集爆发 · Open Design 33.8K 确认平台地位 · antirez/ds4 本地推理引擎赛道加速 · Agent 安全工具走向成熟

> ✅ 今日通过 GitHub API（`gh`）成功获取实时数据，star 数均为实测值。

**关键项目：**
- 🔴 Dirty Frag (2,775 stars) — Linux 内核通用 LPE，确定性触发无竞态
- 🎨 Open Design (33,880 stars) — 平台地位确认，11 天 0→33K
- 🔧 ds4.c (2,312 stars) — 3 天 5x 增长，磁盘 KV Cache 创新
- 🛡️ Deepsec (1,864 stars) — Agent 安全审计持续增长
- 🎭 Harmonist (1,423 stars) — 186 Agent 多 Agent 编排框架
- 🗂️ Mirage (1,401 stars) — Agent VFS 赛道热度验证
- 📊 Open Slide (2,624 stars) — Agent 原生 PPT 框架爆发

→ [查看完整日报](daily/2026-05-09.html)

---

## 2026-05-08

**核心主题：** Agent VFS 统一抽象层出现 · AI 设计赛道 32K 确认 · 推理引擎赛道新玩家入场 · 安全审计 Agent 学术化突破

> ✅ 今日通过 GitHub API（`gh`）成功获取实时数据，star 数均为实测值。

**关键项目：**
- 🗂️ Mirage (925 stars) — AI Agent 统一虚拟文件系统，范式级创新
- 🎨 Open Design (32,118 stars 实测) — 赛道领跑者确认
- ⚡ TokenSpeed (621 stars) — 面向 Agentic Workload 的推理引擎
- 🔧 ds4.c (456 stars) — antirez 的 DeepSeek V4 Flash 本地推理引擎
- 🔍 SPECA (345 stars) — 规约锚定安全审计框架
- 🛡️ Deepsec (1,638 stars) — 安全 Agent 增速验证

→ [查看完整日报](daily/2026-05-08.html)

---

## 2026-05-07

**核心主题：** Agent 生态分层加速：Agent Design 进入平台整合期 · Agent 后端解耦工具链成熟 · 安全 Agent 化从概念到落地 · AI 视频赛道平台化竞争加剧 · Open Design 预估突破 30K

> ⚠️ 今日 GitHub 完全不可达（VPN/代理 TLS 握手失败），分析基于 5/2-5/6 历史数据趋势外推。Star 数为预估。

**关键项目：**
- 🎨 Open Design (~31k stars 预估) — Agent Design 赛道领跑者，赛道进入整合期
- 🎛️ CC Switch (~59k stars 预估) — Agent Desktop 基座，生态锁定效应初显
- 📊 PPT Master (~12k stars 预估) — AI PPT 工业化标杆
- 📊 Future AGI (~900 stars 预估) — Agent 可观测性，上调至持续跟踪
- 🛡️ Deepsec (~1.2k stars 预估) — Vercel 出品安全 Agent
- 🕸️ Graphify (~41k stars 预估) — 上调至基础设施候选

→ [查看完整日报](daily/2026-05-07.html)

---

## 2026-05-06

**核心主题：** Agent Design 赛道爆发：Open Design 7 天 27K 重新定义设计工具链 · Cursor 官方 Cookbook 出炉 · Linux 内核 9 年 LPE 漏洞曝光 · AI PPT 生成工具集中爆发 · Vercel Deepsec 用 Agent 找漏洞

**关键项目：**
- 🎨 Open Design (27.3k stars) — Agent Design 赛道事实标准，7天从0到27K
- 📽️ Guizang PPT Skill (5k stars) — Claude Code Skill 生成杂志风 HTML 幻灯片
- 📖 Cursor Cookbook (3.5k stars) — Cursor 官方 AI 编辑器最佳实践
- 🔓 CVE-2026-31431 (3.3k stars) — Linux 内核 9 年本地提权漏洞
- 📊 PPT Master (11.6k stars) — AI 生成原生可编辑 PPTX
- 🛡️ Deepsec (1k stars) — Vercel 出品，Agent 驱动安全审计
- 🎬 Waoowaoo (12k stars) — 工业级 AI 影视生产平台

→ [查看完整日报](daily/2026-05-06.html)

---

## 2026-05-05

**核心主题：** Agent 后端解耦趋势加速：DeepClaude 替换 Claude Code 后端 17x 降本 · Browser Agent 新形态 Chromex 入局 · Future AGI 开源 Agent 评估观测平台 · Reversa 遗留系统 Agent 化 · AI 编程术语标准化萌芽

**关键项目：**
- 🔀 DeepClaude (987 stars) — 用 DeepSeek V4 Pro 替换 Claude Code 后端，17x 降本
- 🌐 Chromex (813 stars) — Codex 驱动 Chrome Side-Panel 助手
- 📊 Future AGI (822 stars) — 开源 Agent 评估观测平台，Apache 2.0
- 🔄 Reversa (565 stars) — 遗留系统转 Agent 可执行规格
- 🎨 Open Design (23.7k stars) — Agent Design 赛道领跑者，持续爆发
- 📽️ Open Slide (897 stars) — Agent 原生 PPT 生成框架
- 📖 Dictionary of AI Coding (961 stars) — AI 编程术语词典

→ [查看完整日报](daily/2026-05-05.html)

---

## 2026-05-04

**核心主题：** Agent Design 红海化 · Linux 内核 CVE-2026-31431 席卷安全社区 · Harmonist 协议级 Agent 编排至 1.2K · DeepSeek TileKernels 定义 LLM 底层算子新方向 · DPI 绕过方案激增

**关键项目：**
- 🎨 Open Design (19.1k stars) — 开源 Claude Design 替代，6天从 4K 到 19K
- 🔴 Copy Fail CVE-2026-31431 (3.0k stars) — Linux 内核提权漏洞 PoC，衍生项目涌现
- ⚡ TileKernels (1.4k stars) — DeepSeek GPU 算子库，MoE/量化/Engram
- 🎵 Harmonist (1.2k stars) — 零依赖 Agent 编排，186 agents
- 🌐 mhr-cfw (1.9k stars) — Domain Fronting DPI 绕过方案
- 📝 OpenChronicle (2.1k stars) — OpenAI Chronicle 开源替代
- 🗄️ dbx (773 stars) — Tauri+Rust 轻量数据库客户端
- 📐 text-to-cad (1.4k stars) — 开源 Text-to-CAD 引擎

→ [查看完整日报](daily/2026-05-04.html)

---

## 2026-05-03

**核心主题：** Agent Skills 生态进入工具整合期：CC Switch 57K+ 稳守桌面基座 · Open Design 突破 15K · 3090 社区 LLM 部署方案崛起 · AI 语音输入 OpenLess 开辟新赛道

**关键项目：**
- 🎛️ CC Switch (57.8k stars) — Agent 桌面基座，统一管理 Claude Code/Codex/OpenCode/OpenClaw/Gemini CLI
- 🎨 Open Design (15.7k stars) — Claude Design 开源替代，5天从 4K 到 15.7K
- 🎮 Club 3090 (354 stars) — RTX 3090 社区 LLM 部署方案，多引擎 recipe
- 🎙️ OpenLess (345 stars) — 开源语音输入，按住说话松开出文
- 🧠 MemPalace (50.7k stars) — AI 记忆系统，MCP 集成修复
- 🗄️ dbx (707 stars) — Tauri+Rust 轻量数据库客户端，SQL 增强

→ [查看完整日报](daily/2026-05-03.html)

---

## 2026-05-02

**核心主题：** Agent Design 赛道爆发：Open Design 4天翻倍至 11.4K · Graphify 跨 Agent 知识图谱逼近 40K · HeyGen HyperFrames 定义 Agent 原生视频生成范式

**关键项目：**
- 🎨 Open Design (11.4k stars) — Claude Design 开源替代，72 DS + 31 Skills，4天翻倍，平台化加速
- 🕸️ Graphify (39.6k stars) — 跨 Agent 知识图谱 Skill，逼近 40K
- 🎬 HyperFrames (13.6k stars) — HeyGen 出品，HTML→Video，Agent 原生视频生成
- 🧠 MemPalace (50.7k stars) — 稳守 50K+，AI Memory 赛道领导者
- 🕵️ Obscura (9.3k stars) — Rust 无头浏览器突破 9K
- ⚛️ QuipNetwork (5.8k stars) — 疑似刷星，Star/Fork 比异常

→ [查看完整日报](daily/2026-05-02.html)

---

## 2026-05-01

**核心主题：** Linux 内核 CVE-2026-31431 本地提权曝光 · Open Design 近 8K Stars 领跑 Agent Design 赛道 · DeepSeek TileKernels 输出 GPU Kernel 基础设施

**关键项目：**
- 🔴 Copy Fail CVE-2026-31431 (1.6k stars) — Linux 内核 AEAD 本地提权漏洞，影响主流发行版，P0 安全事件
- 🎨 Open Design (8.0k stars) — Claude Design 开源替代，72 DS + 31 Skills，平台化加速
- ⚡ TileKernels (1.4k stars) — DeepSeek 出品 GPU Kernel 库，MoE/量化/Engram 全覆盖
- 🔒 Harmonist (945 stars) — 协议硬强制 Agent 框架，186 Agent + 零依赖
- 🌐 FreeLLMAPI (783 stars) — 聚合14家免费 LLM Provider，OpenAI 兼容
- 🌍 World2Agent (588 stars) — Agent 感知层开放协议，Sensor 标准化

→ [查看完整日报](daily/2026-05-01.html)

---

## 2026-04-30

**核心主题：** Claude 架构逆向工程引爆 ML 社区 · AI Agent 记忆层进入本地优先时代 · Coding Agent Harness 标准化加速

**关键项目：**
- 🧬 OpenMythos (11.2k stars) — Claude Mythos RDT 架构理论重建，MLA+GQA+MoE
- 📜 OpenChronicle (1.9k stars) — 开源本地优先 Agent 记忆层，AX Tree 策略
- 🎨 Open Design (4.1k stars) — Claude Design 开源替代，71 DS + 19 Skills
- ♞ Browser Harness (8.4k stars) — Self-Healing 浏览器 Harness，持续上升
- 🧳 Agentic Stack (1.8k stars) — .agent/ 标准目录，跨 Agent 可移植
- ☿ Mercury Agent (1.8k stars) — Soul-Driven Agent，权限硬化 + Second Brain

→ [查看完整日报](daily/2026-04-30.html)

---

## 2026-04-29

**核心主题：** AI 记忆层基础设施竞赛升温 · Agent Skill 生态进入长尾分化期 · Browser Agent 向 Harness 模式收敛

**关键项目：**
- 🧠 MemPalace (50.2k stars) — 最强开源 AI 记忆系统，LongMemEval 96.6%
- 🕸️ Graphify (37.3k stars) — 跨 Agent 知识图谱 Skill，10+ 平台兼容
- 📦 CubeSandbox (4.6k stars) — 腾讯云 Rust+KVM 沙箱，60ms 冷启动
- ♞ Browser Harness (7.9k stars) — Self-Healing 浏览器 Harness，CDP 直连
- 🎵 Harmonist (825 stars) — 186 Agent 零依赖编排，机械协议执行

→ [查看完整日报](daily/2026-04-29.html)

---

## 2026-04-28

**核心主题：** 国产大模型 MoE 密集发布（Hy3 + Kimi K2.6）· Code Intelligence 走向 MCP-Native · Claude Code Skill 生态爆发

**关键项目：**
- 🔮 Hy3 Preview (262 stars) — 腾讯混元 295B MoE，90 天重建基础设施
- 🌙 Kimi K2.6 (10.7k stars) — SWE-Bench Pro 58.6% 登顶，300 Agent Swarm
- 🕸️ GitNexus (28.6k stars) — Zero-Server Code Intelligence，MCP 原生
- 🎨 Huashu Design (8.3k stars) — Claude Code HTML 原生设计 Skill
- 🎵 Harmonist (741 stars) — 零依赖 Agent 编排，186 Agent

→ [查看完整日报](daily/2026-04-28.html)

---

## 2026-04-27

**核心主题：** AI Memory 系统走向产品化 · Token 效率成为 Agent Skill 新焦点 · Agent 沙箱基础设施升温

**关键项目：**
- 🧠 MemPalace (49.8k stars) — 最高 benchmark 开源 AI 记忆系统
- 🪨 Caveman (47.1k stars) — Token 压缩 Skill，prompt 效率新维度
- 🕵️ Obscura (6.0k stars) — Rust Agent 专用无头浏览器
- 🌐 Browser Harness (7.1k stars) — 自愈式浏览器 Harness
- 📦 CubeSandbox (4.2k stars) — 腾讯 Agent 沙箱

→ [查看完整日报](daily/2026-04-27.html)

---

## 2026-04-26

**核心主题：** AI Agent Skill 生态爆发 · 零人类公司编排走出概念 · CLI 成为 Agent-Native 标准接口

**关键项目：**
- 🧠 Graphify (34.8k stars) — 跨 Agent 平台 GraphRAG 编排 Skill
- 📎 Paperclip (58.8k stars) — 零人类公司开源编排框架
- 🔬 autoresearch (76.5k stars) — Karpathy 研究自动化 Agent
- 🔌 CLI-Anything (32.6k stars) — 万物 Agent-Native CLI
- 📁 Google Workspace CLI (25.4k stars) — Google 官方统一 CLI

→ [查看完整日报](daily/2026-04-26.html)

---

## 2026-04-25

**核心主题：** AI Agent 安全基础设施成型 · Memory 层竞争从 API 转向嵌入式 · Rust 正在成为 Agent Runtime 首选语言

**关键项目：**
- 🛡️ ThinkWatch (444 stars) — 企业级 AI 堡垒主机，Rust 实现
- 🦀 CrabTrap (424 stars) — LLM-as-a-Judge 安全代理
- 📦 CubeSandbox (3.9k stars) — 腾讯出品 AI Agent 轻量沙箱，Rust
- 🧠 Graymatter (277 stars) — 三行代码 Agent 持久记忆
- 🏛️ MemPalace (49.5k stars) — 开源 AI 记忆系统逼近 50K

→ [查看完整日报](daily/2026-04-25.html)

---

## 2026-04-24

**核心主题：** Claude Code Skill 生态分化为垂直子赛道 · AI Coding 成本可观测性成为刚需 · LLM 推理内核性能优化进入白热化

**关键项目：**
- 🔥 codeburn (3.5k stars) — AI Coding Token 消耗可观测性 TUI Dashboard
- ⚡ TileKernels (592 stars) — DeepSeek tilelang 推理内核库
- 🚀 FlashKDA (383 stars) — Moonshot Kimi Delta Attention 内核
- 📋 agents-md (489 stars) — 让 Coding Agent 表现如资深工程师的 AGENTS.md
- 🧳 agentic-stack (1.5k stars) — 跨平台可移植 .agent/ 配置

→ [查看完整日报](daily/2026-04-24.html)

---

## 2026-04-23

**核心主题：** OpenMythos 重建 Claude 架构引发研究热潮 · Claude Code 设计工具生态全面爆发 · Browser Harness 验证自愈浏览器成为 Agent 标配能力

**关键项目：**
- 🧠 OpenMythos (8.7k stars) — 基于 RDT 重建 Claude Mythos 架构
- 🎨 huashu-design (4.4k stars) — HTML 原生 Claude Code 设计 Skill
- 🖌️ open-codesign (1.2k stars) — 开源多模型 BYOK 设计 Agent 平台
- 🌐 browser-harness (5.0k stars) — 自愈浏览器 Harness
- 🦞 claw-code (187.5k stars) — Rust Coding Agent 持续领跑

→ [查看完整日报](daily/2026-04-23.html)

---

## 2026-04-22

**核心主题：** Browser Harness 持续爆发验证 Browser Use 赛道 · Claude Code Skill 生态进入设计工具细分 · PgQue 代表极简主义基础设施思潮回归

**关键项目：**
- 🌐 browser-harness (4347 stars) — Self-healing 浏览器自动化框架
- 📊 diagram-design (1303 stars) — 13 种编辑级图表 Claude Code Skill
- 📄 Kami (1354 stars) — 内容优先的纸张设计工具
- 🐘 PgQue (913 stars) — 零臃肿 Postgres 队列
- 🔥 codeburn (3239 stars) — AI 编码 Token 成本追踪 TUI

→ [查看完整日报](daily/2026-04-22.html)

---

## 2026-04-21

**核心主题：** OpenMythos 逆向重建 Claude 架构引爆关注 · Agentic Stack 定义跨 Harness 可移植 Agent 规范 · Weft 探索 AI 原生编程语言

**关键项目：**
- 🧠 OpenMythos (3995 stars) — 从公开文献逆向重建 Claude 架构的理论项目
- 🔄 agentic-stack (750 stars) — 可移植 .agent/ 规范，跨 Harness 运行
- 🧵 weft (906 stars) — AI 系统专用编程语言，Rust 实现
- 🎨 design-extract (1138 stars) — 设计系统提取 + MCP + 多平台输出
- ⚡ aube (318 stars) — Rust 实现的快速 Node.js 包管理器

→ [查看完整日报](daily/2026-04-21.html)

---

## 2026-04-20

**核心主题：** Browser Use 推出 Self-Healing Browser Harness · Vercel 开源 Web 终端 wterm · Agent Skill 生态持续爆发（设计提取/PPT/诊断）

**关键项目：**
- ♞ browser-harness (2031 stars) — Self-healing browser harness，agent 自写缺失函数
- 🖥️ wterm (2050 stars) — Vercel Labs 出品 Web 终端模拟器
- 🎨 design-extract (1084 stars) — 一键提取网站完整设计系统，MCP server
- 📊 html-ppt-skill (1396 stars) — HTML PPT Studio AgentSkill
- 🐘 xata (634 stars) — 云原生 Postgres 平台，CoW branching

→ [查看完整日报](daily/2026-04-20.html)

---

## 2026-04-19

**核心主题：** Agent 可移植性与Harness互操作成新焦点 · AI原生编程语言Weft首次进入视野 · 分布式DuckDB与云原生Postgres数据基座演进加速

**关键项目：**
- 🧠 agentic-stack (492 stars) — Agent 可移植性层，.agent/ 跨所有 harness
- 🧵 weft (824 stars) — AI 系统编程语言，LLM/Human/API 作为一等原语
- 🦆 openduck (447 stars) — 分布式 DuckDB，双执行引擎 + 差分存储
- 🗺️ lingbot-map (1,778 stars) — 前馈 3D 基础模型，streaming 场景重建
- 🔬 meta-harness (444 stars) — Stanford 出品，Harness 自动优化框架

→ [查看完整日报](daily/2026-04-19.html)

---

## 2026-04-18

**核心主题：** Claude Code Skill 生态爆发 · 全场景协议分析+AI逆向成新范式 · Web终端基础设施加速 · Token可观测性进入平台化前夜

**关键项目：**
- 🖥️ wterm (1,310 stars) — Vercel 出品 Web 终端，Zig+WASM+DOM 渲染
- 🔍 anything-analyzer (1,269 stars) — 全场景协议分析+MITM+AI+MCP
- 🔥 codeburn (2,553 stars) — Token 可观测性仪表盘，6天持续高速增长
- 🎬 video-use (903 stars) — browser-use 出品视频编辑 Skill
- 🧬 darwin-skill (1,082 stars) — Skill 自进化系统
- 🧵 weft (769 stars) — AI 系统编程语言，持续迭代

→ [查看完整日报](daily/2026-04-18.html)

---

## 2026-04-17

**核心主题：** Agent Skill 自进化范式成形 · AI原生编程语言登场 · Token可观测性持续升温 · 端侧多模态推理加速

**关键项目：**
- 🧬 darwin-skill (952 stars) — Skill 自进化引擎：评估→改进→回滚
- 🧵 weft (638 stars) — AI 系统编程语言，Rust 实现
- 🔥 codeburn (2,214 stars) — Token 可观测性仪表盘，5天破2K
- 🗣️ parlor (1,551 stars) — 端侧多模态 AI 对话
- ⚡ dflash-mlx (443 stars) — MLX 无损推测解码
- 🐘 xata (479 stars) — 开源云原生 Postgres

→ [查看完整日报](daily/2026-04-17.html)

---

## 2026-04-16

**核心主题：** Agent成本可观测性觉醒 · AI记忆系统标准化竞赛 · Zero-Human Company编排框架落地 · 知识工程从RAG走向持久化Wiki

**关键项目：**
- 🔥 codeburn (1.7K stars) — AI Coding Token 成本 TUI 仪表盘，2天破千星
- 🏛️ mempalace (46.5K stars) — 最佳 benchmark AI 记忆系统，11天4.6万星
- 📎 paperclip (54.1K stars) — Zero-Human Company 编排引擎，2,291 issues
- 📚 llm-wiki (1.4K stars) — 持久化 Wiki 知识库，RAG 替代范式

→ [查看完整日报](daily/2026-04-16.html)

---

## 2026-04-15

**核心主题：** Karpathy Skills现象级爆发 · Claude生态工具链深度整合 · AI金融模型入场 · Agent基础设施工具层成型

**关键项目：**
- 🧠 andrej-karpathy-skills (33.8K stars) — 心智模型即技能，日增 9,263 stars
- 💾 claude-mem (55.8K stars) — Agent 工作记忆基础设施，会话捕获+压缩+注入
- 🔧 chrome-devtools-mcp (35K stars) — MCP 协议操作 Chrome DevTools
- 📊 Kronos (17.8K stars) — 金融市场 Foundation Model

→ [查看完整日报](daily/2026-04-15.html)

---

## 2026-04-14

**核心主题：** Hermes Agent 65K星霸榜 · Agent Skill生态饱和信号 · 存储基础设施Rust化 · 语音AI开源破局

**关键项目：**
- 🦀 RustFS (23K+ stars) — Rust S3 兼容存储，Apache 2.0 MinIO 替代
- 🔷 gstack (66K+ stars) — YC 总裁的 Claude Code 虚拟团队工作流
- 🪿 Goose (29K+ stars) — Block 本地 AI Coding Agent，Apache 2.0
- 🏺 nuwa-skill (20K+ stars 生态) — 人格蒸馏 Claude Code Skill 框架

→ [查看完整日报](daily/2026-04-14.html)

---

## 2026-04-13

**核心主题：** AI Agent工业化 · Harness工程新范式 · 群体智能觉醒 · 端侧AI生态成型

**关键项目：**
- 🏗️ Archon (16,000+ stars) — 首个AI Coding harness builder，YAML工作流标准化
- 🐟 MiroFish (25,000+ stars) — 通用群体智能引擎
- 🎭 agency-agents (68,906 stars) — AI Agent工具箱（泡沫嫌疑）
- 📐 EmDash (8,500+ stars) — Cloudflare的WordPress继任者，插件沙箱架构

→ [查看完整日报](daily/2026-04-13.html)

---

## 2026-04-12

**核心主题：** AI记忆系统破局 · Agent知识脑标配化 · 人格蒸馏Skill生态爆发

**关键项目：**
- 🧠 mempalace (41,755 stars) — 史上最高分 AI 记忆系统，LongMemEval 96.6%
- 🕸️ graphify (22,086 stars) — 代码/文档转知识图谱的 Agent Skill
- 🧠 GBrain (15,432 stars) — Agent 知识脑系统
- 👆 clicky (3,774 stars) — 光标旁的 AI 老师

→ [查看完整日报](daily/2026-04-12.html)

---

## 2026-04-11

**核心主题：** AI Agent 技能框架爆发 · 托管式 Agent 平台兴起 · Copilot Workspace 多仓库上下文

**关键项目：**
- ⚡ superpowers (121K stars) — AI 编程 Agent 技能框架，强制 TDD
- 🤝 multica-ai (6,000+ stars) — 开源托管式 Agent 平台
- 🦙 ollama (167.7K stars) — 本地 LLM 部署工具

→ [查看完整日报](daily/2026-04-11.html)

---

## 2026-04-10

**核心主题：** 端侧AI推理生产化 · AI编程平台生态成熟 · 多代理协作标准化

**关键项目：**
- 🚀 litert-inference (2,341 stars) — Google 生产级端侧 LLM 推理引擎
- 🔧 claude-code-extension (8,942 stars) — Claude Code 扩展生态
- 🎼 agent-orchestra (678 stars) — 多代理协作编排平台

→ [查看完整日报](daily/2026-04-10.html)

---

## 2026-04-09

**核心主题：** 自主 AI Agent 系统爆发 · AI 原生开发工具革新 · 科研自动化

**关键项目：**
- 🚀 auto-deep-researcher-24x7 (123 stars) — 24/7 自动深度研究系统
- 🎨 styleseed (120 stars) — AI 设计引擎
- 📋 project-architect (94 stars) — 文档优先的项目规划代理技能

→ [查看完整日报](daily/2026-04-09.html)

---

## 2026-04-08

**核心主题：** claw-code 爆炸式增长 · Edge AI 加速落地 · Claude Code 生态持续扩张

**关键项目：**
- 🔥 claw-code (168.7K stars) — 史上最快突破 100K stars
- ⚡ oh-my-codex (18K stars) — Claude Code Codex 版
- 🧙 hermes-agent (28K stars) — Agent 自进化 + MCP Gateway
- 🌐 LiteRT (2K+ stars) — Google 端侧 ML 框架

→ [查看完整日报](daily/2026-04-08.html)

---

## 2026-04-07

**核心主题：** MCP 协议扩散 + 端侧 LLM 推理生产化

**关键项目：**
- 🧠 GitNexus (23.6K stars) — 代码知识图谱 + MCP Server
- 🧙 hermes-agent (28K stars) — Agent 自进化 + 跨会话记忆
- 📋 oh-my-claudecode (25K stars) — Multi-Agent 编排平台

→ [查看完整日报](daily/2026-04-07.html)

---

*数据来源：GitHub Trending、MapoDev、GitTrends、ByteIota、OSSInsight*
*持续跟踪 · 每日更新 · 架构视角*
