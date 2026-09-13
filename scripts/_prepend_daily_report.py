#!/usr/bin/env python3
"""Prepend 2026-09-14 section to daily-report.md (newest first)."""
from pathlib import Path

p = Path("daily-report.md")
text = p.read_text(encoding="utf-8")

# Idempotency
if "## 2026-09-14" in text:
    print("OK (idempotent: today's section already present, skipping)")
    raise SystemExit(0)

# Find the first H2 line (## YYYY-MM-DD) to insert before it
lines = text.split("\n")
insert_at = None
for i, l in enumerate(lines):
    if l.startswith("## 2026-"):
        insert_at = i
        break

if insert_at is None:
    insert_at = 4

new_section = """## 2026-09-14
**核心主题：** zorrobyte/asset-studio 1 天 33⭐ ⑂8 端到端本地文本→3D 游戏资产生成管道（Python · 0BSD · Qwen-Image-2512 → Pixal3D/TRELLIS.2 → Blender/meshoptimizer 三阶段管线 · FastAPI + CLI + MCP 三接口 · RTX 5090 单卡离线验证 · Godot/Unity/Blender drop-in · manifest.json 任务级追溯 · 三个完整 sample pump/crate/mug · fork/star 24.2%）· ivyfan-toowell/IvyClaw 1 天 52⭐ ⑂3 中文生产级多智能体软件研发 Agent 系统（Python · 无 license · DeepAgents + LangGraph 五角色 Planner/Researcher/Coder/Tester/Reviewer · 多模型路由 · Git/pytest/Web Search/MCP 真实工具调用 · Docker/Daytona 双沙箱 · PostgreSQL + LangGraph Checkpointer/Store 状态持久化 · Redis + ARQ Worker 异步长任务 · HITL 高危工具人工审批 · 多渠道 CLI/FastAPI/飞书 WS/Webhook · API Key + 租户 + 限流 + 幂等 + 审计多租户治理 · LangSmith + Prometheus + Grafana 可观测 · Mermaid 架构图 · docker-compose.prod.yml 一键部署）· Speedstu/CUDA-for-AMD-Windows 1 天 55⭐ ⑂1 跨 GPU 厂商 CUDA 兼容层 Windows 复现模板（PowerShell · NOASSERTION · ZLUDA v6-preview.69 + AMD HIP SDK 6.4 + LibTorch 2.3.0+cu118 · AMD RX 9060 XT gfx1200 唯一验证 · nvcuda/cuBLAS/cuBLASLt/cuSPARSE/cuFFT 全 pass cuda_check · 220 万参数 PPO 网络 forward/inference/learning/optimizer 全链路 · 65,536 timesteps 单次 validation · install.ps1 自动 detect/verify/download/check · GitHub Actions verify.yml）· Dr-TSNG/altdb 1 天 53⭐ ⑂5 KernelSU 无线 ADB 模块（Rust · Apache-2.0 · KernelSU v3.2.5+ · Android 11+ ARM64 · 六位配对码 + TLS · IPv4 局域网 Wi-Fi/热点/Ethernet 排除蜂窝 VPN · shell/file/install/logs/reboot/forward-reverse port · 系统 USB/无线调试开启自动暂停恢复 · WebUI 中英双语 · 连接端口 1024–65535 可固定 · 持久化配对记录 · 不动系统 adbd 授权 · fork/star 9.4%）

**证据边界：** 星标、总星数与增速取自 2026-09-14 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license）+ 各项目 README 公开摘录（API readme 字段 base64 解码）；"X 天 Y⭐"基于 created_at→2026-09-14 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**今日观察窗为 2026-09-13 创建且截至 2026-09-14 仍在快速增长的 4 个非游戏类高质量项目**；09-14 当日新创仓库 API 暂返回 0 条命中（亚洲时区多数仓库刚过 12 小时曝光窗口）。**今日最大事件是 `zorrobyte/asset-studio` 1 天 33⭐ / fork 8 / fork/star 24.2% — 端到端本地文本→3D 游戏资产生成管道**——Qwen-Image-2512 文生参考图 → Pixal3D / TRELLIS.2 高细节 3D → Blender / meshoptimizer 自动简模 + LOD + 碰撞烘焙；三接口接入（FastAPI + CLI + MCP）；单卡 RTX 5090 全离线；manifest.json 任务级追溯；三个完整 sample（pump 19803 tris / crate 7998 tris / mug 6000 tris）证明不是 PoC；0BSD 极宽松许可。**`Speedstu/CUDA-for-AMD-Windows` 1 天 55⭐ 是本批星标最高 — 跨 GPU 厂商 CUDA 兼容层 Windows 复现模板**——ZLUDA v6-preview.69 + AMD HIP SDK 6.4 + LibTorch 2.3.0+cu118 + AMD Radeon RX 9060 XT gfx1200 单卡验证；五个 CUDA 入口全 pass cuda_check；220 万参数 PPO 网络全链路验证；install.ps1 全自动；GitHub Actions verify.yml CI；NOASSERTION license（合规风险）。**`Dr-TSNG/altdb` 1 天 53⭐ / fork 5 / fork/star 9.4% — KernelSU 无线 ADB 模块**——六位配对码 + TLS 加密；IPv4 局域网（Wi-Fi / 热点 / Ethernet），排除蜂窝与 VPN；shell / file / install / logs / reboot / forward-reverse port 全套；系统 USB / 无线调试开启自动暂停，恢复后自动续连；WebUI 中英双语；不动系统 adbd 授权；Rust；Apache-2.0。**`ivyfan-toowell/IvyClaw` 1 天 52⭐ / fork 3 / fork/star 5.8% — 中文生产级多智能体软件研发 Agent 系统**——DeepAgents + LangGraph 五角色编排；Docker / Daytona 双沙箱；PostgreSQL + LangGraph Checkpointer / Store 状态持久化；Redis + ARQ Worker 异步长任务；HITL 高危工具人工审批；多渠道 CLI / FastAPI / 飞书 WebSocket / Webhook；LangSmith + Prometheus + Grafana 可观测；Mermaid 架构图完整；**无 license**（最大合规风险）。**「端到端本地 + agent-callable」范式从 AI Coding 工具栈扩张到资产生成领域**——asset-studio 的 MCP 接口把「文本→3D 资产」变成 coding agent 可调用的函数，是 tracecrate / birdview / ccompactor 形成的 AI Coding 可观测栈之外的第四条线（资产生成）。**「中文 Coding Agent 双层栈」完整化**——Baize（agent loop 协议层）+ IvyClaw（多租户生产工程层）构成中文 AI 工具栈追赶 LangChain / Anthropic / OpenAI 阵营的清晰路径；IvyClaw 把 Baize 关注的「Agent 协议层」推到「Agent 工程化落地层」。**AMD GPU + CUDA 训练栈首次有可复现 Windows 实现**——CUDA-for-AMD-Windows 不是新发明 ZLUDA，而是「把 ZLUDA + HIP SDK + LibTorch 在 Windows + AMD 上端到端跑通」并把脚本自动化 + 验证公开。**KernelSU 无线 ADB 模块填补 Android root 用户刚需**——altdb 是 KernelSU 生态里少数「无线 ADB 替代」模块；Apache-2.0 + Rust + 131 KB + WebUI 中英双语都是 KernelSU 模块生态的工程严肃度信号。**「端到端本地 + agent-callable」三个项目形成新组合**——asset-studio（本地 3D 资产生成）+ 昨日 `FankChen/tracecrate`（本地 AI Agent trace 解析）+ 昨日 `xiaYuTian11/maskit`（本地 LLM 出网隐私脱敏）形成「本地 AI Coding 工具链三件套」——本地算、本地存、本地隐私。11+ 个游戏外挂 / 私服 / Mod 工具（fortnite-xp-map-codes-windows / nba-2k27-mycareer-badge-planner / blox-fruits-trade-calculator / monster-hunter-wilds-dps-meter-overlay / kingdom-come-deliverance-2-save-editor / blue-lock-rivals-auto-goal-script-reference 等）元数据信号异常，本简报不列入核心趋势；`Abomination81/copybot`（65⭐ / 36 forks / 无 license / Rust / Polymarket 跟单交易执行）虽 fork/star 55.4% 极端高，但定位与昨日已观察过的去中心化交易机器人（Argona7/stampede 等）属于同类，本批重点放在更可工程复现的项目；`MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks`（74⭐ / 6 forks / AGPL-3.0 / EXL3 2.9 bpw 量化包）虽是「DeepSeek v4.1 Flash 量化 + DGX Sparks 双卡」具体硬件绑定，但作为模型权重资源发布而非工程系统，亦不列入核心趋势。

**关键项目：**
- 🎨 zorrobyte/asset-studio (1 天 33⭐ ⑂8) — 端到端本地文本→3D 游戏资产生成管道（Python · 0BSD · Qwen-Image-2512 文生参考图 → Pixal3D/TRELLIS.2 高细节 3D → Blender/meshoptimizer 自动简模 + LOD + 碰撞烘焙 · 三接口 FastAPI + CLI + MCP · RTX 5090 单卡全离线 · manifest.json 任务级追溯 · 三个完整 sample pump/crate/mug 各跑通到 20K/8K/6K 三角预算 + contact_sheet 对照图 · 输出 master.glb + LOD1/LOD2/collision.glb + previews + textures · Godot/Unity/Blender 无缝集成 · fork/star 24.2%），Score 90
- 🦞 ivyfan-toowell/IvyClaw (1 天 52⭐ ⑂3) — 中文生产级多智能体软件研发 Agent 系统（Python · 无 license · DeepAgents + LangGraph 五角色 Planner/Researcher/Coder/Tester/Reviewer · 多模型路由 · Git/pytest/Web Search/MCP 真实工具调用 · Docker/Daytona 双沙箱 · PostgreSQL + LangGraph Checkpointer/Store 状态持久化 · Redis + ARQ Worker 异步长任务 · HITL 高危工具人工审批 · 多渠道 CLI/FastAPI/飞书 WS/Webhook · API Key + 租户 + 限流 + 幂等 + 审计多租户治理 · LangSmith + Prometheus + Grafana 可观测 · Mermaid 架构图完整 · docker-compose.prod.yml 一键部署 · 无 license 是企业合规最大风险），Score 86
- 🪟 Speedstu/CUDA-for-AMD-Windows (1 天 55⭐ ⑂1) — 跨 GPU 厂商 CUDA 兼容层 Windows 复现模板（PowerShell · NOASSERTION · ZLUDA v6-preview.69 官方 upstream + AMD HIP SDK 6.4 + LibTorch 2.3.0+cu118 · AMD Radeon RX 9060 XT gfx1200 单卡验证 · nvcuda/cuBLAS/cuBLASLt/cuSPARSE/cuFFT 五个 CUDA 入口全 pass cuda_check · 220 万参数 PPO 网络 forward/inference/learning/optimizer 全链路验证 · 65,536 timesteps 单次 validation · install.ps1 自动 detect/verify/download/校验 · GitHub Actions verify.yml CI · NOASSERTION 是企业合规风险 · 53 KB repo · fork/star 1.8%），Score 84
- 📱 Dr-TSNG/altdb (1 天 53⭐ ⑂5) — KernelSU 无线 ADB 模块（Rust · Apache-2.0 · KernelSU v3.2.5 (32525)+ · Android 11+ ARM64 · 六位配对码 + TLS 加密 · IPv4 局域网 Wi-Fi/热点/Ethernet 排除蜂窝与 VPN · shell/file/install/logs/reboot/forward-reverse port 全套 · 系统 USB 调试或无线调试开启自动暂停，恢复后自动续连 · WebUI 状态/连接命令/已配对设备/诊断 中英双语 · 连接端口 1024–65535 可固定或随机 · adb root / adb unroot / su 权限独立开关 · 持久化配对记录 · 模块升级保留设置，卸载时移除数据 · 不动系统 adbd 授权 · fork/star 9.4%），Score 82

**关键判断：**
- **「Agent-callable 本地管线」范式扩散到资产生成领域**：asset-studio 的 MCP 接口把「文本→3D 资产」变成 coding agent 可调用的函数；这是 tracecrate / birdview / ccompactor 形成的 AI Coding 可观测栈之外的第四条线（资产生成）；Coding Agent 现在不仅能「读」「改」「可视化」代码，还能「产出」3D 资产
- **中文 Coding Agent 从「协议层」推进到「工程层」**：Baize 关注 agent loop / skills / hooks 协议；IvyClaw 关注多租户 / 异步 / 沙箱 / 可观测 / HITL 等生产工程能力；两者构成「中文 Coding Agent 双层栈」——底层 Baize（agent loop 协议）+ maskit（出网隐私）+ routeVSCODE（模型路由），上层 IvyClaw（多租户生产系统）；与昨日 Baize 偏个人开发者 / 自部署不同，IvyClaw 面向企业 / 团队 / SaaS 化
- **AMD GPU + CUDA 训练栈首次有可复现 Windows 实现**：CUDA-for-AMD-Windows 不是新发明 ZLUDA，而是把 ZLUDA + HIP SDK + LibTorch 在 Windows + AMD 上端到端跑通并把脚本自动化 + 验证公开；这是「开发者现在可以在 Windows + AMD GPU 上跑 CUDA-target 训练」的可复现证明——对 AMD GPU Windows 用户（消费级 RDNA3/RDNA4 用户）有直接价值
- **KernelSU 无线 ADB 模块填补 Android root 用户刚需**：altdb 是 KernelSU 生态里少数「无线 ADB 替代」模块；Apache-2.0 + Rust + 131 KB + WebUI 中英双语都是 KernelSU 模块生态的工程严肃度信号；KernelSU 模块生态在 2026 年持续壮大，altdb 是其中一个清晰填补空白的具体工具
- **「端到端本地 + agent-callable」三个项目形成新组合**：asset-studio（本地 3D 资产生成）+ 昨日 tracecrate（本地 AI Agent trace 解析）+ 昨日 maskit（本地 LLM 出网隐私脱敏）形成「本地 AI Coding 工具链三件套」——本地算、本地存、本地隐私；本地化是 LLM 应用层的反向 SaaS 路径，与 iOS 端 Chuloo/mural（自带 API key 原生 iOS 语言学习）同构但推到「本地 + 可被 agent 调用」层级
- **游戏资产 / AI 训练 / Android 系统级模块三个「工程级具体问题」同日被各自解决**：asset-studio（游戏资产生成）+ CUDA-for-AMD-Windows（AMD 上跑 CUDA 训练）+ altdb（KernelSU 无线 ADB）三个项目都不是宏大叙事，而是解决一个具体工程问题——这是 2026-09 趋势的明显特征：单点灵感到工程闭环的项目比「AI 平台 / 框架」类更易爆
- **企业合规风险普遍存在**：本批 4 个项目中 IvyClaw（无 license）、CUDA-for-AMD-Windows（NOASSERTION）、asset-studio（0BSD 缺 license 文件）三个都有合规问题；提醒「开源不自动意味着可商用」

---
"""

# Insert at the position of the first ## date header (push it down)
new_lines = lines[:insert_at] + [new_section] + lines[insert_at:]
new_text = "\n".join(new_lines)
p.write_text(new_text, encoding="utf-8")
print("OK")