#!/usr/bin/env python3
"""Prepend 2026-09-15 section to indexes/trend-index.md + update last_updated."""
import re
from pathlib import Path

p = Path("indexes/trend-index.md")
text = p.read_text(encoding="utf-8")

# Idempotency
if "## 2026-09-15" in text:
    print("OK (idempotent: today's section already present, skipping)")
    raise SystemExit(0)

# Update last_updated
text = re.sub(r"(last_updated:\s*)'[\d\-]+'", r"\g<1>'2026-09-15'", text, count=1)

# Find first ## YYYY-MM-DD to insert before
lines = text.split("\n")
insert_at = None
for i, l in enumerate(lines):
    if l.startswith("## 2026-"):
        insert_at = i
        break

if insert_at is None:
    insert_at = 6

new_section = """## 2026-09-15

### Matthew0822/ToolReplay（171 stars · fork 18）· yifanzhang-pro/FlashREINFORCE（39 stars · fork 3）· 0xjohnnydev/airlift（33 stars · fork 2）· FelixQiu1/XiaoAi-LLM-Router（20 stars）· ToolMonsters/claude-code-routing（19 stars · fork 3）

> 证据边界：项目名称、星标、tags、description 来自 2026-09-15 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license）+ 各项目 README 公开摘录（API readme 字段 base64 解码）。"X 天 Y⭐"基于 created_at→2026-09-15 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**今日观察窗为 2026-09-14 创建且截至 2026-09-15 仍在快速增长的 5 个非游戏类高质量工程型项目**；本轮抓取中 GitHub Search API 未鉴权速率限制，部分 09-15 当日新创仓库可能未返回，本批重点放在 09-14 创建且仍持续增长的项目。**今日最大事件是 `Matthew0822/ToolReplay` 1 天 171⭐ / fork 18 / fork/star 10.5% — Coding Agent 工具调用会话审计 CLI**——hash-chain 封存 seal + 确定性 replay 检测 non-determinism（同一工具同一 canonical JSON 编码参数两次调用返回不同响应则首个分歧索引即 divergence point）+ state-change mutator 识别 redundant call（仅当两次相同调用之间没有 mutator 或不同调用时算冗余）+ 外部声明权限 scope 文件比对 permission overreach（tool 不在 agent 声明 scope 中）；Python 3.11+ 零三方运行时依赖无网络访问；samples/session-dirty.jsonl 单一六行样本同时覆盖三类 finding（index 2 read_file 重复判 redundant + index 5 search 返回 7 hits 与 index 3 的 3 hits 不同判 non-determinism + index 4 write_file 不在 docs-reader 声明 scope 中判 permission-overreach）；finding 排序固定（按 index 再按 kind）保证 byte-identical 输出；exit code 1 标记有 finding 便于 CI / pre-commit hook 集成；MIT 许可 + 464 KB repo 是「可独立部署的最小审计内核」形态；与昨日 tracecrate（时序层）/ birdview（架构层）/ ccompactor（session 互操作层）形成 AI Coding 工具链 7 件套「session 层审计」补齐。**`yifanzhang-pro/FlashREINFORCE` 1 天 39⭐ / fork 3 — NVIDIA 2026-09 论文开源参考实现**——Jian Hu, Yifan Zhang, Hao Zhang, Binfeng Xu 等 NVIDIA 团队发布；「单 rollout per prompt + token importance sampling 修正陈旧行为 + Sequence Trust Region 控制累积 policy drift + Sample-Mean Optimization 防止长失败轨迹主导」四件套；flashreinforce/loss.py 含 batch centering + token IS + sequence trust + sample mean + 可选 entropy-based failure-token filter；scripts/train_molt.py --dry-run 预览所有训练 flags；pinned Molt launchers 提供 R1 与 Qwen2.5-Math；examples/ 4 类实验设置（reasoning / Python tools / MoE / ALFWorld）；docs/training.md 明示「CPU example 不复现论文基准」「Tool/ALFWorld 设置需兼容 agent 与环境」复现局限；官方代码仓 NVIDIA-NeMo/labs-molt 形成「论文参考实现 + 生产训练栈」分工；Apache-2.0 许可 + 701 KB repo + NVIDIA 团队背书是「工业级严肃度的论文参考实现」。**`0xjohnnydev/airlift` 1 天 33⭐ / fork 2 / fork/star 6.1% — iOS 27.0 RC AirTraffic 沙箱逃逸 PoC**——漏洞根因清晰到 `-[ATAirlock processCompletedAsset:]` 仅校验 destination 字符串前缀（`[destination hasPrefix:@"/var/mobile/Media/"]`）未校验 source + destination 跟随 ancestor symlink + Books「Persistent ID」作为 asset.identifier 直接拼接路径无校验；已验证 12 个目录 fresh-file 写权限（/var/mobile, /var/mobile/Documents, /var/mobile/Library, /var/mobile/Library/Preferences, /var/mobile/Library/Caches, /var/mobile/Library/SpringBoard, /var/mobile/Library/SMS, /var/mobile/Library/Safari, /var/mobile/Containers, /var/mobile/Containers/Data/Application, /var/mobile/Containers/Shared/AppGroup, /var/tmp）；reads 是 indirect（先移动已知文件到 Media → 通过 AFC 读 → 移回）；MobileGestalt plist 当前不工作（无法绕过 Activation Lock）；触发条件「paired Mac over Wi-Fi or USB, no iOS app required」是普通用户默认 Books 同步场景；测试环境 iOS 27.0 RC 24A435 + final 24A437；Objective-C + 123 KB repo + 不 burn for clout 立场是「安全研究 PoC」典型形态。**`FelixQiu1/XiaoAi-LLM-Router` 1 天 20⭐ / fork 0 — 老旧小米小爱同学升级 DeepSeek / Ollama / OpenAI / Claude 本地智能管家网关**——「不拆硬件、不刷固件、不改原音色」中间层路径；MiService 拦截小爱收音 + LiteLLM 100+ 供应商统一接口 + MiTTS 切句播放回小爱；唤醒词路由「请问 / 深思」命中才走 LLM 否则小爱正常应答避免「所有对话都先问 LLM」；多轮对话记忆 session 按 device + 时间窗 TTL 默认 600s + max_turns 10 让「它刚才说的那个东西再大一点」指代也能接住；Ollama 模式链路不出局域网（隐私敏感家庭用户关键卖点）；config.yaml 切换 deepseek/ollama/openai/claude 同套唤醒词同套记忆零代码改动；docker compose up -d 一键部署；20 KB repo 是极简配置 + 一键部署形态。**`ToolMonsters/claude-code-routing` 1 天 19⭐ / fork 3 / fork/star 15.8% — Spotify Portal 90% Claude Code token 削减 plain Claude Code 复现**——「A cheap model does the reading and the boilerplate. Claude keeps the thinking」；bin/code-write Haiku 写可预测代码（测试 / type stub / config）从 spec + 参考文件直写盘 + bin/bulk-read Haiku 整文件读返回 dense bullets 带行号 + hooks/block-big-reads.sh PreToolUse 350 行阻断 hook + skills/code-write / skills/bulk-read Claude 调度指令；benchmark/ 4 场景 psf/requests 复现（S1 inventory 110/110 classes / S2 raise-except 跨 1155+625 行 / S3 与 S4）；Claude Code 2.1.270 + Opus 5 实测；README 主动标注「The numbers are below, including the ones that don't flatter it」S2 反例 with 比 without 略贵（$0.85 vs $0.74）——诚实信号的工程化；MIT 许可 + 193 KB repo + 4 个公开 benchmark 是「可直接复现的成本优化工具」标准形态。**`agentscope-java/agentscope-java`（32⭐ / 0 forks / 33 MB / Java NOASSERTION / 09-14 创建）经核验为 Alibaba 官方 `agentscope-ai/agentscope-java`（5,600⭐ / 1,359 forks / 2025-09-23 创建）的同名镜像/重定位账号**——README 与 News 区段完全一致（含 2026-07 v2.0.0 GA + 2026-08 AgentScope Service + 2026-05 v1.1.0 + 2026-06 RC2/3/4 + 2026-07 RC5 完整时间线），本简报不列入核心趋势但作脚注——这是「库方在 GitHub 重新注册账号」一类组织性事件的信号，非新工程；它反映 AgentScope Java 2.0 GA（2026-07）+ AgentScope Service（2026-08）仍在推进企业 Java Agent 框架演进（双层 agent 架构 + 事件流 + 权限系统 + 中间件 + 工作空间沙箱 + 多 Agent 编排 + 分布式部署 + Agent Evolution）。**`nilbuild/page-mascot`（209⭐ / 8 forks / Python MIT / 176 MB / 「a mascot that watches the cursor and blinks when you poke it」）为可执行 demo 类项目而非工程系统**，本简报不列入核心趋势；**`callbacked/kinesis`（51⭐ / 1 fork / Swift NOASSERTION）虽 fork/star 较高但需要 Meta Neural Band 硬件 + 仅 macOS 14+**，本批优先选入可独立验证的工程类项目。**「AI Coding 工具链 7 件套」今日补齐**：maskit（出网层隐私 9-12）+ routeVSCODE（模型层路由）+ Baize（agent loop 层 9-13）+ tracecrate（时序层 9-12）+ birdview（架构层 9-13）+ ccompactor（session 互操作 9-13）+ **ToolReplay（session 层审计 9-15）**——session 层审计是企业 SDLC 合规（hash-chain 篡改可见 + permission overreach 权限越权）的硬需求；MIT + Python 3.11+ 零三方依赖便于作为合规管线步骤集成。**「NVIDIA agentic LLM RL 训练范式」 critic-free + 异步化**：FlashREINFORCE 的「critic-free + 单 rollout + 异步 + trust region」四件套是 REINFORCE 类方法在 agentic LLM 上的回归——不依赖 critic 模型意味着少一份算力预算 + 少一个失败点；与 Molt 异步训练栈整合意味着可扩展到生产规模；这是 NVIDIA 在 2026-09 给出的工业级 RL 训练替代方案。**iOS 27.0 公开沙箱逃逸**：airlift 是 2026 Q3 公开的最具体 iOS 27 沙箱绕过案例；漏洞根因清晰到 ATAirlock 字符串前缀校验 + ancestor symlink 跟随；Apple Security 团队可直接对应修复；**对企业**：iOS 27.0 设备 + Mac 配对 + Books 同步启用 = 暴露面（应暂时关闭 Books 同步直到补丁）。**「不拆硬件 + LiteLLM 中间层」智能音箱升级模式**：XiaoAi-LLM-Router 与昨日 tracecrate / maskit / mural 同构「本地 + 反 SaaS + 自带 key」范式但推到「硬件受限设备的 LLM 升级」这一新场景——不拆硬件、不刷固件、不改原音色，仅通过中间层加 LLM 思考回路；Ollama 模式链路不出局域网是隐私敏感家庭用户关键卖点。**「cheap model 当 worker + Claude 当 orchestrator」AI Coding 成本优化标准模式**：claude-code-routing 是 Spotify Portal 公开博客的 plain Claude Code 复现——cheap model（Haiku）处理「读 / 写 boilerplate」，Claude 处理「thinking」；PreToolUse 350 行阻断 hook + Skills 组合是 Claude Code 扩展机制的清晰示范；S2 反例（with 比 without 略贵）说明路由策略需根据 workload 实测。

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|---:|---|---|---:|
| 1 | agent-transcript-audit / Coding Agent 工具调用会话审计 CLI——Matthew0822/ToolReplay 1 天 171⭐ ⑂18 fork/star 10.5%（Python · MIT · seal/replay/verify/scope/version 五命令 · hash-chain 封存 + canonical JSON 编码比较 deterministic + state-change mutator 识别 redundant + 外部声明权限 scope 文件比对 overreach · Python 3.11+ 零三方依赖无网络访问 · samples/session-dirty.jsonl 单一六行样本覆盖三类 finding · finding 排序 byte-identical · exit code 1 标记有 finding · 464KB repo · 与昨日 tracecrate/birdview/ccompactor 同构 AI Coding 可观测栈第七件套「session 层审计」） | Matthew0822/ToolReplay | 92 |
| 2 | async-agentic-rl-framework / NVIDIA FlashREINFORCE Asynchronous Agent RL 框架——yifanzhang-pro/FlashREINFORCE 1 天 39⭐ ⑂3（Python · Apache-2.0 · flashreinforce/loss.py 参考实现含 batch centering + token IS + sequence trust + sample mean + entropy-based failure-token filter · scripts/train_molt.py Molt 异步训练 launcher --dry-run 预览 flags · R1 / Qwen2.5-Math pinned launcher · reasoning / Python tools / MoE / ALFWorld 实验设置 · docs/training.md GPU setup + paper-to-code 映射 + 复现局限 · pip install -e '.[test]' + pytest · 701KB repo · 官方代码仓 NVIDIA-NeMo/labs-molt） | yifanzhang-pro/FlashREINFORCE | 86 |
| 3 | ios27-airtraffic-sandbox-escape / iOS 27.0 RC AirTraffic 沙箱逃逸 PoC——0xjohnnydev/airlift 1 天 33⭐ ⑂2（Objective-C · NOASSERTION · MobileDevice.framework + AirTrafficHost.framework 链路 · com.apple.streaming_zip_conduit → afc → atc → AirTrafficDevice → Books sync client → ATLegacyAssetLink → ATAirlock → NSFileManager 12 个目录写权限已验证 · -[ATAirlock processCompletedAsset:] 仅校验 destination 字符串前缀未校验 source · ancestor symlink 跟随 · Books 「Persistent ID」无路径校验 · 仅声明 PoC 给开发者与安全研究者 · iOS 27.0 RC 24A435 + final 24A437 验证） | 0xjohnnydev/airlift | 84 |
| 4 | xiaoai-local-llm-gateway / 老旧小米小爱同学升级 DeepSeek/Ollama 本地智能管家网关——FelixQiu1/XiaoAi-LLM-Router 1 天 20⭐（Python · NOASSERTION · MiService 拦截小爱收音 + LiteLLM 100+ 供应商统一接口 + MiTTS 切句播放回小爱 · 多轮对话记忆按 device + 时间窗 TTL 默认 600s + max_turns 10 · 唤醒词路由「请问 / 深思」命中才走 LLM · Ollama 模式链路不出局域网 · docker compose up -d 一键部署 · config.yaml 切换 deepseek/ollama/openai/claude 同套唤醒词记忆 · 20KB repo · 与昨日 tracecrate/maskit 本地 AI Coding 工具链三件套同构「本地 + 自带 key」反 SaaS 范式推到智能音箱领域） | FelixQiu1/XiaoAi-LLM-Router | 78 |
| 5 | spotify-portal-claude-code-routing / Spotify Portal 90% Claude Code token 削减开源复现——ToolMonsters/claude-code-routing 1 天 19⭐ ⑂3（HTML · MIT · bin/code-write Haiku 写测试/stub/config + bin/bulk-read Haiku 整文件读返回 dense bullets 带行号 + hooks/block-big-reads.sh PreToolUse 350 行阻断 hook + skills/code-write + skills/bulk-read Claude 调度指令 · benchmark/ 4 场景 psf/requests 复现 + S1 110/110 classes inventory + S2 raise/except 跨 1155+625 行 · Claude Code 2.1.270 + Opus 5 实测 · 与昨日 ToolMonsters/claude-code-routing 同构 AI Coding 成本优化工具链） | ToolMonsters/claude-code-routing | 80 |

#### 当日重点项目

- 🧾 Matthew0822/ToolReplay (1 天 171⭐ ⑂18) — Coding Agent 工具调用会话审计 CLI，hash-chain 封存 + 确定性 replay + 权限越权 scope 检查，Python MIT 零三方依赖，fork/star 10.5%，Score 92
- ⚡ yifanzhang-pro/FlashREINFORCE (1 天 39⭐ ⑂3) — NVIDIA 2026-09 Critic-Free Single-Rollout Asynchronous RL 框架，batch centering + token IS + sequence trust + sample mean，Apache-2.0，Score 86
- 🪂 0xjohnnydev/airlift (1 天 33⭐ ⑂2) — iOS 27.0 RC AirTraffic 沙箱逃逸 PoC，ATAirlock 字符串前缀校验漏洞 + ancestor symlink 跟随，Objective-C NOASSERTION，Score 84
- 🔊 FelixQiu1/XiaoAi-LLM-Router (1 天 20⭐) — 老旧小米小爱同学升级 DeepSeek/Ollama/OpenAI/Claude 本地智能管家网关，MiService + LiteLLM + MiTTS + 唤醒词路由，Python NOASSERTION，Score 78
- 🚦 ToolMonsters/claude-code-routing (1 天 19⭐ ⑂3) — Spotify Portal 90% Claude Code token 削减 plain Claude Code 复现，bin/code-write Haiku + bin/bulk-read Haiku + PreToolUse 350 行阻断 hook，MIT，fork/star 15.8%，Score 80



"""

out_lines = lines[:insert_at] + [new_section] + lines[insert_at:]
p.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Inserted {len(new_section)} chars at line {insert_at}")
