#!/usr/bin/env python3
"""Append 2026-09-14 section to trend-index.md at the top of content (after frontmatter)."""
from pathlib import Path

p = Path("indexes/trend-index.md")
text = p.read_text(encoding="utf-8")

# Idempotency
if f"## 2026-09-14" in text:
    print("OK (idempotent: today's section already present, skipping)")
    raise SystemExit(0)

# Find end of frontmatter
lines = text.split("\n")
fm_end = 0
for i, l in enumerate(lines):
    if i > 0 and l.strip() == "---":
        fm_end = i + 1
        break

new_section = """

## 2026-09-14

### zorrobyte/asset-studio（33 stars · fork 8）· ivyfan-toowell/IvyClaw（52 stars）· Speedstu/CUDA-for-AMD-Windows（55 stars）· Dr-TSNG/altdb（53 stars · fork 5）

> 证据边界：项目名称、星标、tags、description 来自 2026-09-14 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license）+ 各项目 README 公开摘录（API readme 字段 base64 解码）。"X 天 Y⭐"基于 created_at→2026-09-14 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**今日观察窗为 2026-09-13 创建且截至 2026-09-14 仍在快速增长的 4 个非游戏类高质量项目**；09-14 当日新创仓库 API 暂返回 0 条命中（亚洲时区多数仓库刚过 12 小时曝光窗口）。**今日最大事件是 `zorrobyte/asset-studio` 1 天 33⭐ / fork 8 / fork/star 24.2% — 端到端本地文本→3D 游戏资产生成管道**——Qwen-Image-2512 文生参考图 → Pixal3D / TRELLIS.2 高细节 3D → Blender / meshoptimizer 自动简模 + LOD + 碰撞烘焙；三接口接入（FastAPI + CLI + MCP）；单卡 RTX 5090 全离线；manifest.json 任务级追溯；三个完整 sample（pump 19803 tris / crate 7998 tris / mug 6000 tris）证明不是 PoC；0BSD 极宽松许可。**`Speedstu/CUDA-for-AMD-Windows` 1 天 55⭐ 是本批星标最高 — 跨 GPU 厂商 CUDA 兼容层 Windows 复现模板**——ZLUDA v6-preview.69 + AMD HIP SDK 6.4 + LibTorch 2.3.0+cu118 + AMD Radeon RX 9060 XT gfx1200 单卡验证；五个 CUDA 入口（nvcuda / cuBLAS / cuBLASLt / cuSPARSE / cuFFT）全 pass cuda_check；220 万参数 PPO 网络 forward / inference / learning / optimizer 全链路验证；65,536 timesteps 单次 validation；install.ps1 自动 detect + verify + download + 校验；GitHub Actions verify.yml CI；NOASSERTION license（合规风险）。**`Dr-TSNG/altdb` 1 天 53⭐ / fork 5 / fork/star 9.4% — KernelSU 无线 ADB 模块**——六位配对码 + TLS 加密；IPv4 局域网（Wi-Fi / 热点 / Ethernet），排除蜂窝与 VPN；shell / file / install / logs / reboot / forward-reverse port 全套；系统 USB / 无线调试开启自动暂停，恢复后自动续连；WebUI 状态 / 连接命令 / 已配对设备 / 诊断 中英双语；连接端口 1024–65535 可固定；不动系统 adbd 授权；Android 11+ ARM64 + KernelSU v3.2.5+；Rust；Apache-2.0；fork/star 9.4% 处于企业 fork 信号下限。**`ivyfan-toowell/IvyClaw` 1 天 52⭐ / fork 3 / fork/star 5.8% — 中文生产级多智能体软件研发 Agent 系统**——DeepAgents + LangGraph 五角色编排（Planner / Researcher / Coder / Tester / Reviewer）；多模型路由；Git / pytest / Web Search / MCP 真实工具调用；Docker / Daytona 双沙箱；PostgreSQL + LangGraph Checkpointer/Store 状态持久化；Redis + ARQ Worker 异步长任务；HITL 高危工具人工审批；多渠道 CLI / FastAPI / 飞书 WebSocket / Webhook；API Key + 租户 + 限流 + 幂等 + 审计多租户治理；LangSmith + Prometheus + Grafana 可观测；Mermaid 架构图完整；docker-compose.prod.yml 一键部署；**无 license**（最大合规风险）。**「端到端本地 + agent-callable」范式从 AI Coding 工具栈扩张到资产生成领域**——asset-studio 的 MCP 接口把「文本→3D 资产」变成 coding agent 可调用的函数，是 tracecrate / birdview / ccompactor 形成的 AI Coding 可观测栈之外的第四条线（资产生成）。**「中文 Coding Agent 双层栈」完整化**——Baize（agent loop 协议层）+ IvyClaw（多租户生产工程层）构成中文 AI 工具栈追赶 LangChain / Anthropic / OpenAI 阵营的清晰路径。**「单点灵感到工程闭环」是 2026-09 趋势的明显特征**——asset-studio（资产生成）+ CUDA-for-AMD-Windows（AMD 训练）+ altdb（KernelSU ADB）三个项目都不是宏大叙事，而是解决一个具体工程问题。11+ 个游戏外挂 / 私服 / Mod 工具（fortnite-xp-map-codes-windows / nba-2k27-mycareer-badge-planner / blox-fruits-trade-calculator / monster-hunter-wilds-dps-meter-overlay / kingdom-come-deliverance-2-save-editor / blue-lock-rivals-auto-goal-script-reference 等）元数据信号异常，本简报不列入核心趋势；`Abomination81/copybot`（65⭐ / 36 forks / 无 license / Rust / Polymarket 跟单交易执行）虽 fork/star 55.4% 极端高，但定位与昨日已观察过的去中心化交易机器人同类，本批重点放在更可工程复现的项目；`MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks`（74⭐ / 6 forks / AGPL-3.0 / EXL3 2.9 bpw 量化包）虽是「DeepSeek v4.1 Flash 量化 + DGX Sparks 双卡」具体硬件绑定，但作为模型权重资源发布而非工程系统，亦不列入核心趋势。

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|---:|---|---|---:|
| 1 | local-text-to-3d-pipeline / 端到端本地文本→3D 游戏资产生成管道——zorrobyte/asset-studio 1 天 33⭐ ⑂8 fork/star 24.2%（Python · 0BSD · Qwen-Image-2512 → Pixal3D/TRELLIS.2 → Blender/meshoptimizer 三阶段管线 · FastAPI + CLI + MCP 三接口 · RTX 5090 单卡验证 · Godot/Unity/Blender drop-in · manifest.json 任务级追溯 · 76 MB repo · 三个完整 sample pump/crate/mug） | zorrobyte/asset-studio | 90 |
| 2 | production-multi-agent-swe / 中文生产级多智能体软件研发 Agent——ivyfan-toowell/IvyClaw 1 天 52⭐ ⑂3 fork/star 5.8%（Python · 无 license · DeepAgents + LangGraph 五角色 Planner/Researcher/Coder/Tester/Reviewer · 多模型路由 · Docker/Daytona 双沙箱 · PostgreSQL + LangGraph Checkpointer/Store 持久化 · Redis + ARQ Worker 异步 · HITL 高危工具审批 · 多渠道 CLI/FastAPI/飞书 WS/Webhook · API Key + 租户 + 限流 + 审计 · LangSmith + Prometheus + Grafana · Mermaid 架构图 · docker-compose.prod.yml） | ivyfan-toowell/IvyClaw | 86 |
| 3 | cross-vendor-cuda-compat / 跨 GPU 厂商 CUDA 兼容层——Speedstu/CUDA-for-AMD-Windows 1 天 55⭐ ⑂1 fork/star 1.8%（PowerShell + ZLUDA v6-preview.69 · NOASSERTION · AMD HIP SDK 6.4 · LibTorch 2.3.0 + cu118 · Windows x64 · AMD RX 9060 XT gfx1200 唯一验证 · nvcuda/cuBLAS/cuBLASLt/cuSPARSE/cuFFT 全 pass cuda_check · 220 万参数 PPO 网络 forward/inference/learning/optimizer 全链路 · 65 536 timesteps 单次 validation · install.ps1 自动 detect/verify/download/check · GitHub Actions verify.yml） | Speedstu/CUDA-for-AMD-Windows | 84 |
| 4 | kernelsu-wireless-adb / KernelSU 无线 ADB 模块——Dr-TSNG/altdb 1 天 53⭐ ⑂5 fork/star 9.4%（Rust · Apache-2.0 · KernelSU v3.2.5+ · Android 11+ ARM64 · 六位配对码 + TLS · IPv4 局域网 Wi-Fi/热点/Ethernet 排除蜂窝 VPN · shell/file/install/logs/reboot/forward-reverse port · 系统 USB/无线调试开启自动暂停恢复 · WebUI 中英双语 · 连接端口 1024–65535 可固定 · 持久化配对记录 · 不动系统 adbd 授权） | Dr-TSNG/altdb | 82 |

#### 当日重点项目

- 🎨 zorrobyte/asset-studio (1 天 33⭐ ⑂8) — 端到端本地文本→3D 游戏资产生成管道，三阶段管线 Qwen-Image-2512 → Pixal3D/TRELLIS.2 → Blender/meshoptimizer，FastAPI + CLI + MCP 三接口，RTX 5090 单卡验证，0BSD，fork/star 24.2%，Score 90
- 🦞 ivyfan-toowell/IvyClaw (1 天 52⭐ ⑂3) — 中文生产级多智能体软件研发 Agent 系统，DeepAgents + LangGraph 五角色，Docker/Daytona 双沙箱，PostgreSQL + Redis + ARQ，HITL + LangSmith + Prometheus/Grafana，无 license（合规风险），Score 86
- 🪟 Speedstu/CUDA-for-AMD-Windows (1 天 55⭐ ⑂1) — 跨 GPU 厂商 CUDA 兼容层 Windows 复现模板，ZLUDA + HIP SDK 6.4 + LibTorch 2.3.0+cu118，RX 9060 XT gfx1200 验证，220 万参数 PPO 训练全链路，NOASSERTION（合规风险），Score 84
- 📱 Dr-TSNG/altdb (1 天 53⭐ ⑂5) — KernelSU 无线 ADB 模块，六位配对码 + TLS + IPv4 局域网，WebUI 中英双语，Rust + Apache-2.0，Score 82


"""

# Insert new_section after frontmatter
new_lines = lines[:fm_end] + [new_section] + lines[fm_end:]
# Update last_updated in frontmatter
for i in range(fm_end):
    if new_lines[i].startswith("last_updated:"):
        new_lines[i] = "last_updated: '2026-09-14'"

new_text = "\n".join(new_lines)
p.write_text(new_text, encoding="utf-8")
print("OK")