#!/usr/bin/env python3
"""Add 架构师速览 sections to new project files (idempotent)."""
import re
from pathlib import Path

files = [
    "projects/deepseek-ai-deepep-ascend.md",
    "projects/deepseek-ai-deepgemm-ascend.md",
    "projects/feder-cr-dots.md",
    "projects/opsafari-hypoarena.md",
    "projects/rehan-remade-universal-modder.md",
]

def deepseek_ai_deepep_ascend_brief():
    return """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 华为昇腾 NPU 上 MoE / GEMM 高性能通信库；公开 buffer API 与 NVIDIA 版 DeepEP 对齐 + Ascend C kernels 使用 HCCL/HCOMM + UBMEM + URMA + DeepJIT 运行时编译 | 仅基于 README 描述的 DeepEP Ascend 实现、HCCL/HCOMM/UBMEM/URMA、DeepJIT 运行时编译、Ascend 950DT EP8 90-95% 物理带宽；具体 Ascend C kernel 实现细节、DeepJIT 编译流程未在档案中给出 |
| 主路径 | 上层应用 → 公开 buffer API → MoE dispatch/combine all-to-all + FP8 dispatch + Pipeline/Context/Data Parallel Bucket collectives + Engram 远端内存（开发中）→ Ascend C kernels（HCCL/HCOMM + UBMEM + URMA）→ Ascend 950DT EP8 90-95% 物理带宽 | 主路径为档案语义抽象；具体 HCCL/HCOMM/UBMEM/URMA 调用路径未在档案中明示 |
| 关键权衡 | 国产 NPU 性能 + 公开 API vs 生态成熟度（NCCL vs HCCL）+ DeepJIT 运行时 vs 预编译 + License 状态（README 未明示 LICENSE 文件） | 档案明示 90-95% 物理带宽、完全 API 兼容 DeepEP、Ascend 950 (A5) + UBMEM connectivity + UBC_CTP/URMA channels + CANN 9.2.0 + Python 3.10 + PyTorch 2.13.0+cpu + torch_npu 2.13.0rc1 + C++20 std::format；License 状态未在 README 中明示 |
| 最小 PoC | 在 Ascend 950DT + CANN 9.2.0 + 32 ranks 上跑 DeepEP-Ascend demo EP8 dispatch 验证 373-375 GB/s + 验证公开 buffer API 与 NVIDIA 版 DeepEP 对齐 | PoC 范围由档案「性能 90-95% 物理带宽 + 公开 buffer API 与 NVIDIA 版 DeepEP 对齐」建议推导；具体 demo 入口、`aclnn_*` reference GEMM 未在档案中讨论 |"""
def deepseek_ai_deepgemm_ascend_brief():
    return """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 华为昇腾 NPU 上 DeepGEMM 完全 API 兼容的 GEMM kernel 库；BF16/FP8/FP4 GEMM + MQA logits + MegaMoE + 轻量抽象 over Ascend MAD | 仅基于 README 描述的 DeepGEMM Ascend 实现、轻量抽象 over Ascend MAD、稀疏数据加载、基于协程的流水线、Ascend 950 多矩阵形状接近 peak hardware performance；具体 Ascend C kernel 实现细节、tilelang HC prenorm kernel 实现未在档案中给出 |
| 主路径 | 上层应用 → DeepGEMM API（完全兼容）→ BF16/FP8/FP4 GEMM + MQA logits + MegaMoE → Ascend MAD（矩阵乘加原语）+ 轻量抽象（隐藏分形矩阵布局/对齐约束/地址计算/参数转换）→ 稀疏数据加载 + 基于协程的流水线 → Ascend 950 多矩阵形状接近 peak | 主路径为档案语义抽象；具体 MAD 调用路径、稀疏数据加载 + 协程流水线实现未在档案中明示 |
| 关键权衡 | 完全 API 兼容 DeepGEMM（NVIDIA 版）+ 轻量抽象 over Ascend MAD vs 性能 + MIT 商用清晰 vs 企业生态采用度 | 档案明示完全 API 兼容 DeepGEMM、BF16/FP8/FP4 GEMM、MQA logits、MegaMoE、轻量抽象、稀疏数据加载、协程流水线、多矩阵形状接近 peak hardware performance、2026.09.30 Initial release、CANN 9.20 + Python 3.10+ + C++20 <format> + tilelang HC prenorm kernel + tree-sitter + tree-sitter-cpp；License MIT 商用清晰 |
| 最小 PoC | 在 Ascend 950 + CANN 9.20 上跑 DeepGEMM-Ascend demo BF16 GEMM 验证「轻量抽象 over Ascend MAD」+ 验证 F8 GEMM + MQA logits 性能是否接近 peak hardware performance | PoC 范围由档案「多矩阵形状接近 peak hardware performance」建议推导；具体 demo 入口、`aclnn_*` reference GEMM 未在档案中讨论 |"""
def feder_cr_dots_brief():
    return """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | AI agent 专属浏览器；patched Firefox C++ 内核（fingerprint 决定在引擎里，page 看不到）+ 任何模型 on OpenRouter（`--model` 一键换）+ 任何 MCP 客户端（`invisible_playwright_mcp`） | 仅基于 README 描述的 patched Firefox C++ 内核、One identity per seed、No WebDriver/DevTools/automation globals、A person's hands（pointer travels + keys one by one）、`--profile-dir` 持久登录、`--proxy` 时区跟随出口、OpenRouter `--model` 一键换、uvx 一行启动、127.0.0.1:8765 左对话右浏览器 live、`invisible_playwright_mcp` 给 Claude Code/Codex/Gemini CLI/任何 MCP；具体 C++ patch 范围、`invisible_playwright_mcp` 协议未在档案中明示 |
| 主路径 | 用户 query → 127.0.0.1:8765 dots 调度 → patched Firefox C++ 内核（fingerprint 一致 + No WebDriver + No DevTools）→ 真实事件（pointer travels / keys one by one）→ 目标 page 信任事件 → OpenRouter 模型（`--model` 一键换）思考 → 浏览器执行 | 主路径为档案语义抽象；浏览器 ↔ 模型间的协议（是否为 MCP-style）未在档案中明示 |
| 关键权衡 | 反检测强度（fingerprint 一致 + 真实事件）vs 多 OS 兼容性 + 任何模型可换 vs OpenRouter 单一 provider + 任何 Agent Harness 可用 vs `invisible_playwright_mcp` 协议开放性 | 档案明示 patched C++ 内核、OpenRouter `--model`、uvx 一行启动、127.0.0.1:8765、`invisible_playwright_mcp` 给 Claude Code/Codex/Gemini CLI/任何 MCP、Not affiliated with OpenAI、MIT；多 OS 兼容性、C++ patch 维护成本、合规边界未在档案中讨论 |
| 最小 PoC | 在一台 Linux + uvx + `--seed 42` 启动 dots；用无头脚本访问 1 个高反爬网站验证「Same identity every run + trusted events」；再以 `--proxy` 切换出口验证 timezone 跟随 | PoC 范围、退出路径由档案「先单 fingerprint、最小 PoC、Seed 可复现」建议推导；具体 `invisible_playwright_mcp` 接口未公开 |"""
def opsafari_hypoarena_brief():
    return """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | fully offline scientific hypothesis-discovery workbench；AI co-scientist 流水线的 mechanism layer 分解为单独可测的组件：citation-bearing hypothesis/evidence graph + synthetic literature factory + span-level grounding verification + pluggable agent adapters + Bradley-Terry/Elo tournaments + MinHash LSH dedup + evolution operators + Bayesian belief updating | 仅基于 README 描述的 fully offline、generate-debate-evolve loop、citation-bearing hypothesis/evidence graph、synthetic literature factory (planted causal chains)、span-level grounding verification (citation existence + entity overlap + polarity consistency + numeric agreement)、pluggable agent adapters (scripted/replay/loopback-mock)、Bradley-Terry/Elo tournaments、MinHash LSH paraphrase dedup、evolution operators (scope narrowing/variable substitution/mechanism crossover/claim decomposition)、Bayesian belief updating + graded evidence、NumPy core + CPU-only torch extra；具体每个组件的实现细节、golden numeric tests 内容未在档案中明示 |
| 主路径 | corpus（合成文献工厂）→ generate（propose/critique/revise）→ verify（span-level grounding）→ dedup（MinHash LSH + TF-IDF）→ debate（generate-debate-evolve loop）→ rank（Bradley-Terry/Elo tournaments）→ evolve（scope narrowing/variable substitution/mechanism crossover/claim decomposition）→ accumulate（Bayesian belief updating + prior sensitivity analysis + contradiction policies）→ report（Markdown + self-contained HTML + honest limitations）→ canonical serializer | 主路径为档案语义抽象；具体每个 stage 的实现细节未在档案中明示 |
| 关键权衡 | mechanism layer 可逐组件测试 + fully offline + reproducible + 严肃工程化 vs 真实科学发现能力（README 明示「This is a mechanism demo and makes no claim about real scientific discovery capability」）vs NumPy core 性能限制 vs 商用清晰（MIT） | 档案明示 fully offline、reproducible、canonical serializer、golden numeric tests、hatchling/pytest/ruff/mypy、MIT 商用清晰；具体 golden numeric tests 内容、NumPy core 性能限制未在档案中明示 |
| 最小 PoC | `hypoarena demo --chains 2 --chain-length 2 --out /tmp/hya` 端到端离线跑验证 generate-debate-evolve loop + hypothesis-evidence graph + planted causal chains 恢复 + canonical serializer artifact 稳定性；再以 `make test-all` 跑全 suite 验证 golden numeric tests | PoC 范围由档案「`hypoarena demo` 端到端离线跑 + `make test-all`」建议推导；具体 demo 入口、golden numeric tests 内容未在档案中讨论 |"""
def rehan_remade_universal_modder_brief():
    return """## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | PC 游戏 modding 跨工作流工具；Claude Code plugin + AGENTS.md 兼容 Codex/Cursor + 12 engine playbooks + fal assets MCP + reverse engineering 全套（ILSpy/Cpp2IL/Ghidra/IDA/Cheat Engine/Frida/RenderDoc）+ `um` Python CLI | 仅基于 README 描述的 Claude Code plugin (`/plugin marketplace add rehan-remade/universal-modder` + `/plugin install universal-modder@universal-modder`)、AGENTS.md 兼容 Codex/Cursor、12 engine playbooks (Unity/Unreal/.NET XNA (Terraria/Stardew/Celeste)/Godot/Source 1-2/Bethesda/Minecraft/AoE2/RE Engine/native C++/indie engines/retro decomps)、ILSpy/Cpp2IL/Vineflower/Ghidra/IDA over MCP/Cheat Engine/Frida/RenderDoc、fal assets (sprites/pixel art/seamless textures/PBR/image-to-3D/auto-rigging/SFX/music/voice/cutscene)、asset-pipeline (art → engine-exact frames)、game-automation、showcase-video、mashup-mods、publish-mod、`um scan/fal/sprite/render3d/win/video/backup/publish` Python CLI、bundled fal MCP server、Python 3.10+ + ffmpeg + uv + Blender (3D → sprite renders)、Windows games driven natively or from WSL、topics 10 个覆盖、20 MB、MIT；具体 `mod-any-game` skill 与子 skill 边界、`um` 子命令边界未在档案中明示 |
| 主路径 | 用户 query → Claude Code plugin (或 AGENTS.md Codex/Cursor) → `mod-any-game` skill → `game-recon` 找引擎/版本/anti-cheat/loaders/save → MODDING_PLAN.md → `reverse-engineering` (ILSpy/Cpp2IL/Ghidra/IDA MCP/Cheat Engine/Frida/RenderDoc) + `fal-assets` (sprites/pixel art/seamless textures/PBR/image-to-3D/auto-rigging/SFX/music/voice/cutscene) + `asset-pipeline` (art → engine-exact frames) → build mod → `game-automation` (GPU-safe screenshot/windowed/crash-reporter cleanup) → `showcase-video` (窗口录制 + 音频 process-loopback) → `publish-mod` (lint/package/credits) → ship mod | 主路径为档案语义抽象；具体 `um scan/fal/sprite/render3d/win/video/backup/publish` Python CLI 子命令边界、`fal MCP server` 接口未在档案中明示 |
| 关键权衡 | 12 engine playbooks 覆盖广度 vs 单一引擎深度 + fal assets 在多素材类型 vs 严肃工程化承诺 + Claude Code plugin + AGENTS.md vs 单一 Agent Harness 兼容性 + 真实 Terra/AoE2 测试覆盖广度 vs PC 游戏 modding 合规边界 | 档案明示 12 engine playbooks、ILSpy/Cpp2IL/Vineflower/Ghidra/IDA over MCP/Cheat Engine/Frida/RenderDoc、fal assets、asset-pipeline、game-automation、showcase-video、mashup-mods、publish-mod、Python 3.10+、ffmpeg、uv、Blender (3D → sprite renders)、Windows games driven natively or from WSL、topics 10 个覆盖、20 MB、MIT；具体合规边界（自制 mod 个人使用 vs 商用分发 vs 反编译 vs 服务条款违反）未在档案中明示 |
| 最小 PoC | 在 Terra 上跑 universal-modder 的 homemade missile launcher + tactical nuke 验证 modding 全链路；再以 `um scan` 在 Steam install 上找引擎 + reverse engineering 验证 `MODDING_PLAN.md`；以 fal assets 生成 sprites + 3D rendered unique unit 验证资产自动化 | PoC 范围由档案「真实 Terra/AoE2 测试」建议推导；具体 fal MCP server 接口、`um fal` 子命令未在档案中讨论 |"""
for path in files:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if "## 架构师速览" in text:
        print(f"OK (idempotent: {path} already has 架构师速览)")
        continue
    # Insert before "## 架构启发"
    section_marker = "## 架构启发"
    if section_marker not in text:
        print(f"WARN: {path} missing 架构启发 — appending 架构师速览 to bottom of body")
        # find end of frontmatter
        parts = text.split("---", 2)
        if len(parts) < 3:
            print(f"FAIL: {path} has no frontmatter")
            continue
        # append after the main content
        body = parts[2]
        # Determine the architect brief based on project
        if "DeepEP-Ascend" in path:
            brief = deepseek_ai_deepep_ascend_brief()
        elif "DeepGEMM-Ascend" in path:
            brief = deepseek_ai_deepgemm_ascend_brief()
        elif "feder-cr-dots" in path:
            brief = feder_cr_dots_brief()
        elif "opsafari-hypoarena" in path:
            brief = opsafari_hypoarena_brief()
        elif "rehan-remade-universal-modder" in path:
            brief = rehan_remade_universal_modder_brief()
        else:
            brief = ""
        new_text = parts[0] + "---" + parts[1] + "---" + body + "\n\n" + brief
        p.write_text(new_text, encoding="utf-8")
        print(f"OK appended to {path}")
        continue
    if "DeepEP-Ascend" in path:
        brief = deepseek_ai_deepep_ascend_brief()
    elif "DeepGEMM-Ascend" in path:
        brief = deepseek_ai_deepgemm_ascend_brief()
    elif "feder-cr-dots" in path:
        brief = feder_cr_dots_brief()
    elif "opsafari-hypoarena" in path:
        brief = opsafari_hypoarena_brief()
    elif "rehan-remade-universal-modder" in path:
        brief = rehan_remade_universal_modder_brief()
    else:
        brief = ""
    text = text.replace("## 架构启发", brief + "\n## 架构启发", 1)
    p.write_text(text, encoding="utf-8")
    print(f"OK inserted into {path}")

