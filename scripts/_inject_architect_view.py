#!/usr/bin/env python3
"""Inject ## 架构师速览 table (with 决策问题/研究判断/证据边界 rows) before ## 架构启发 in each profile."""
from pathlib import Path

TABLES = {
    "toolreplay.md": {
        "anchor": "## 架构启发",
        "table": """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Coding Agent 工具调用会话审计 CLI；输入 transcript (JSONL) + 可选 scope 文件；输出 finding 列表 + hash-chain sealed JSONL；零三方依赖零网络访问；五命令独立可组合 | 来自 README 关于「seal/replay/verify/scope/version 五命令」「Python 3.11+」「dependency-free」「no network access」「canonical JSON 编码」「state-change mutator 识别」「external scope file」的明示；具体 canonical JSON 编码细节、mutator 工具列表、scope 文件 schema 在 README 中未完全展开 |
| 主路径 | 输入 transcript → strict 解析 → canonical JSON 编码构建调用指纹 → replay 命令：第一次见到调用记录响应，重复见到不同响应判 non-determinism 且首个分歧索引即 divergence point；同指纹 + 中间无 mutator 判 redundant；scope 命令：外部 scope 文件比对每次调用的 tool name 是否在声明范围 | 主路径来自 README 描述的三个 finding 维度 + samples/session-dirty.jsonl 六行样本；三类 finding 的具体边界（canonical JSON 字段范围、mutator 判定规则、scope 文件 JSON schema）待核验 |
| 关键权衡 | 静态审计 vs 运行时插桩（零运行时开销 vs 漏掉未记录的调用）/ canonical JSON 编码 vs 原始字符串（精度 vs 鲁棒性）/ strict 解析 vs 容错（清晰 vs 易用）/ 外部 scope 文件 vs 内嵌声明（解耦 vs 紧耦合）/ 零三方依赖 vs 功能丰富（轻 vs 重） | 权衡五因素均从 README + repo 元数据推导；具体 canonical JSON 实现细节、scope 文件 schema 严格度、与其他 Coding Agent transcript 格式的兼容性待核验 |
| 最小 PoC | Python 3.11+ + samples/session-dirty.jsonl + samples/scope.json（已随仓库提供）；运行 `python -m toolreplay replay samples/session-dirty.jsonl` 观察三类 finding + divergence + exit code 1；再运行 `python -m toolreplay scope samples/session-dirty.jsonl samples/scope.json` 观察 permission-overreach；最后 `python -m toolreplay seal` 输出 hash-chain sealed JSONL + `python -m toolreplay verify` 重算 chain | PoC 由「五命令 + samples/session-dirty.jsonl 六行样本 + samples/scope.json 配套」路径推导；具体 scope 文件 JSON schema、canonical JSON 编码细节待核验 |

""",
    },
    "flashreinforce.md": {
        "anchor": "## 架构启发",
        "table": """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 论文参考实现 + Molt 异步训练 launcher；输入 prompt + 工具调用环境；输出 policy 更新；与官方 NVIDIA-NeMo/labs-molt 主仓形成「论文参考实现 + 生产训练栈」分工 | 来自 README 关于「standalone PyTorch reference loss + CPU update example + pinned Molt launchers + R1/Qwen2.5-Math + reasoning/Python tools/MoE/ALFWorld 实验设置」「docs/training.md 含 GPU setup + paper-to-code 映射 + 复现局限」的明示；具体 token IS 数学公式、sequence trust region 边界值、entropy filter 阈值在 loss.py 中可能给出，本档案未读源码 |
| 主路径 | 输入 prompt → 单 rollout（生成一次轨迹）→ token IS 修正（重要性采样）→ sequence trust region（序列级 trust region 控制累积 policy drift）→ sample mean 优化（用样本均值避免长失败轨迹主导）→ 可选 entropy-based failure-token filter（基于熵过滤失败 token）→ policy 更新 | 主路径来自 README 描述的三个核心机制 + loss.py 五个组件；每个组件的具体公式（trust region 阈值、sample mean 实现、entropy filter 计算方式）待核验 |
| 关键权衡 | critic-free（少一份算力 + 少一个失败点 vs 单 rollout 估计方差大）/ 单 rollout（算力省 vs 多 rollout 估计基线更稳）/ 异步（Molt 解耦吞吐 vs 同步训练更易调试）/ trust region（控制 drift vs 限制更新速度）/ sample mean（避免失败主导 vs 对长成功轨迹不公平） | 权衡五因素均从 README 推导；具体 trust region 数学形式、IS 重要性采样分布定义、sample mean vs weighted sum 的实际差距在论文中给出，本档案未读论文 |
| 最小 PoC | Python 3.11+ + PyTorch + Molt（NVIDIA-NeMo/labs-molt）→ `pip install -e '.[test]'` → `python examples/toy_update.py`（CPU 验证优化器更新 step）+ `python -m pytest -q`（单元测试）；再 GPU 跑 `python scripts/train_molt.py --dry-run` 预览 flags；最后用 R1 或 Qwen2.5-Math launcher 跑 reasoning 实验 | PoC 由「pip install + CPU example + pytest + Molt launcher + 4 实验设置」路径推导；具体 GPU 显存需求、CUDA 版本、Molt 集成细节待核验 |

""",
    },
    "airlift.md": {
        "anchor": "## 架构启发",
        "table": """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | iOS 27.0 RC + paired Mac + Books sync 启用场景；macOS 侧 MobileDevice.framework + AirTrafficHost.framework；iOS 侧 streaming_zip_conduit → afc → atc → AirTrafficDevice → Books sync client → ATLegacyAssetLink → ATAirlock → NSFileManager；沙箱逃逸 12 个目录写权限已验证；reads indirect（移动已知文件到 Media → AFC 读 → 移回） | 来自 README 关于「12 个目录」「- [ATAirlock processCompletedAsset:] 字符串前缀校验」「ancestor symlink 跟随」「iOS 27.0 RC 24A435 + final 24A437」「no iOS app required」的明示；具体漏洞利用代码（移动 symlink + 触发 Books sync 的 Objective-C 源码）、NSFileManager 默认行为细节、MobileDevice.framework 在 paired Mac 侧的具体调用在 README 中未完整给出 |
| 主路径 | paired Mac + Books sync enabled → 构造 symlink + Books 「Persistent ID」→ 触发 AirTraffic sync → ATAirlock `-[processCompletedAsset:]` 取 asset.identifier 无校验直接拼接到 source 路径 → 取 asset.path（FileComplete.AssetPath 控制）拼接到 destination 路径 → 仅校验 destination 字符串前缀未校验 source → `[NSFileManager moveItemAtPath:source toPath:destination]` 跟随 ancestor symlink → 写入 12 个目录之一 | 主路径来自 README 关于漏洞利用流程的明示；具体 Objective-C PoC 代码（移动 symlink + 触发 Books sync 的实现细节）在本档案未读取；每个步骤的具体函数调用待核验 |
| 关键权衡 | 公开 PoC（教育 + 推动修复 vs 给攻击者武器化）/ 仅 Books 同步场景（聚焦 vs 攻击面窄）/ 不工作于 MobileGestalt plist（数据读写可 vs 设备控制不可）/ iOS 27.0 RC + final（早期补丁窗口 vs 已公开补丁窗口）/ Objective-C 实现（Apple 栈原生 vs 复杂 PoC 工程） | 权衡五因素均从 README 推导；具体 Apple Security 是否已收到报告、ETA 修复时间、patched iOS 版本号、其他 Books 同步路径变种待核验 |
| 最小 PoC | macOS + Xcode + paired iPhone（iOS 27.0 RC 24A435 或 final 24A437）+ 启用 Books sync + Objective-C 编译 PoC；触发条件：构造 symlink + 触发 AirTraffic sync；验证：写入 `/var/mobile/Library/Preferences`（最敏感目录之一）+ 读取 indirect（移动已知文件到 Media → AFC 读 → 移回）；不应尝试 MobileGestalt plist（README 明示当前不工作） | PoC 由「12 个目录验证 + paired Mac + Books sync + Objective-C 漏洞利用代码」路径推导；具体 PoC 编译步骤、symlink 构造细节、AFC 命令行调用待核验 |

""",
    },
    "xiaoai-llm-router.md": {
        "anchor": "## 架构启发",
        "table": """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 智能音箱升级中间层；收音层（MiService 拦截小爱对话流）+ 思考层（LiteLLM 100+ 供应商统一接口 + 多轮对话记忆 session）+ 嘴层（MiTTS 切句播放回小爱原音色）；数据流：小爱收音 → MiService → XiaoAi-LLM-Router → LiteLLM/REST → DeepSeek/Ollama/OpenAI → Mi TTS → 小爱播放 | 来自 README 关于「三段拆分」「LiteLLM 100+ 供应商」「session 按 device + 时间窗 TTL 600s + max_turns 10」「唤醒词路由」「Ollama 模式链路不出局域网」「docker compose up -d」的明示；具体 MiService / MiTTS 接口稳定性、session 持久化机制、config.yaml schema 在 README 中未完全展开 |
| 主路径 | 用户对小爱说话 → 小爱收音 → MiService 拦截对话流 → 唤醒词判断（「请问 / 深思」命中才走 LLM，否则小爱原生应答）→ XiaoAi-LLM-Router → 多轮对话记忆 session 维护上下文 → LiteLLM 适配器调用 DeepSeek / Ollama / OpenAI / Claude → LLM 回复切短句 → MiTTS 播放回小爱原音色 | 主路径来自 README 描述的三段拆分 + 完整示例对话；MiService 抓包接口的具体协议、LiteLLM session 持久化机制、MiTTS 切句算法待核验 |
| 关键权衡 | 不拆硬件 / 不刷固件 / 不破坏厂商生态（兼容 vs 受限）/ MiService 抓包逆向（无官方支持 vs 可用）/ Ollama 模式链路不出局域网（隐私 vs 需用户自部署 Ollama）/ 唤醒词路由「请深入思考 / 请问」硬编码（避免 LLM 接管所有 vs 用户无法自定义）/ NOASSERTION 许可（开源 vs 企业合规） | 权衡六因素均从 README 推导；具体 MiService 接口稳定性、唤醒词可配置性、LiteLLM session 在 Docker 重启后是否丢失待核验 |
| 最小 PoC | Raspberry Pi / NAS / NUC + Docker + 现有小米小爱同学 + MiService 已部署 + LiteLLM 配置（deepseek API key 或 ollama 本地模型如 qwen2.5:7b）+ config.yaml 配置小爱账号密码 + docker compose up -d；触发条件：对小爱说「小爱同学，请深入思考：为什么月亮晚上才上班？」观察 LLM 回复切短句 MiTTS 播放回小爱 | PoC 由「Docker 一键部署 + MiService 拦截 + LiteLLM 适配 + 多轮对话记忆 + 唤醒词路由」路径推导；具体 MiService 部署步骤、LiteLLM 供应商配置示例、config.yaml schema 严格度待核验 |

""",
    },
    "claude-code-routing.md": {
        "anchor": "## 架构启发",
        "table": """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | plain Claude Code CLI 之上的 cheap model 路由层；输入 Claude Code 任务；输出低成本执行（Haiku 处理 reading/boilerplate，Claude Opus 5 处理 thinking）；含 bin/code-write + bin/bulk-read scripts + hooks/block-big-reads.sh PreToolUse hook + skills/code-write + skills/bulk-read Skills 调度指令 + benchmark/ 4 场景 | 来自 README 关于「bin/code-write Haiku 直写盘可预测代码」「bin/bulk-read Haiku 整文件读返回 bullets」「hooks/block-big-reads.sh PreToolUse 350 行阻断」「skills/code-write / skills/bulk-read」「benchmark/ 4 场景 psf/requests」的明示；具体 Haiku 模型版本、Opus 5 token 单价、Skills 调度协议细节待核验 |
| 主路径 | 用户提交 Claude Code 任务 → Claude Opus 5 orchestrator → skills/code-write 调度 bin/code-write（Haiku 写测试/type stub/config 直写盘）或 skills/bulk-read 调度 bin/bulk-read（Haiku 整文件读返回 dense bullets）→ PreToolUse hook 350 行阻断引导用上述 scripts → Claude Opus 5 用 ranged reads 精确取片段思考决策 → 回复 / 代码修改 | 主路径来自 README 描述的「cheap model 当 worker + Claude 当 orchestrator」模式 + Spotify Portal 公开博客复现；具体 Skills 调度协议、Haiku 调用参数、Opus 5 vs Haiku token 单价比待核验 |
| 关键权衡 | cheap model 当 worker + Claude 当 orchestrator（成本省 vs 增加路由复杂度）/ plain Claude Code 不需 Portal（不绑 SaaS 平台 vs Spotify Portal 集成度更高）/ PreToolUse hook 350 行阻断（保护 Claude context vs 可能误阻断大文件读）/ S2 反例诚实标注（实测 vs cherry-pick）/ benchmark/ 4 场景仅 psf/requests 仓库（可复现 vs 场景覆盖窄） | 权衡五因素均从 README 推导；具体 Spotify Portal 博客原文版权、Haiku 模型可用性、PreToolUse hook 阻断阈值 350 是否调整、更多 benchmark 场景待核验 |
| 最小 PoC | macOS / Linux + Claude Code CLI 2.1.270 + Opus 5 + Haiku 模型可用 + git clone + cd claude-code-routing && ./install.sh（自动复制 scripts + hook + skills 到 ~/.claude 并备份 settings.json）+ 重启 Claude Code + 跑 benchmark/ 4 场景（inventory 110/110 classes + raise-except 跨 1155+625 行）+ 对比 without 成本 vs with 成本 | PoC 由「git clone + install.sh + benchmark/ 4 场景」路径推导；具体 Haiku 模型可用性、benchmark/ 数字验证、S2 反例实测、Spotify Portal 博客原文版权待核验 |

""",
    },
}

for fname, cfg in TABLES.items():
    p = Path(f"projects/{fname}")
    text = p.read_text(encoding="utf-8")
    if "## 架构师速览" in text:
        print(f"SKIP {fname} (already has section)")
        continue
    if cfg["anchor"] not in text:
        print(f"ERROR {fname} anchor not found")
        continue
    new_text = text.replace(cfg["anchor"], cfg["table"] + cfg["anchor"], 1)
    p.write_text(new_text, encoding="utf-8")
    print(f"OK {fname}: inserted {len(cfg['table'])} chars")
