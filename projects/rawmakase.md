---
title: "pch/rawmakase"
slug: rawmakase
date_added: "2026-10-16"
last_seen_date: "2026-10-16"
category: "工具型"
emoji: "📷"
stars: "1199 stars"
stars_delta: "20 天 1199⭐ ⑂44 fork/star 3.7%（持续高增长，Omarchy/Homebrew/Linux desktop 需求强）"
language: "Rust"
score: 86
tags: ["rawmakase","pch","raw-photo-editor","lightroom","non-destructive","rust","libraw","little-cms","metal","vulkan","directx-12","mcp","midi","omarchy","homebrew","sqlite","lightroom-classic","lrcat","xmp-presets","dcp","gpu-color-tone","agentic-photo","mit"]
url: "https://github.com/pch/rawmakase"
---

# pch/rawmakase

## 一句话定位
RAWmakase 是一个 fast, non-destructive RAW photo developer for Linux, macOS and Windows, written in Rust——打开 LibRaw 支持的相机 RAW 文件，用 Lightroom-style 控制集 develop + export JPEG 或 16-bit TIFF；可导入 Lightroom Classic .lrcat 目录（rating / flag / label / keyword / 兼容 develop settings），不写原 catalog 或原照片；GPU color & tone stage（Metal macOS / Vulkan Linux / DirectX 12 or Vulkan Windows）+ CPU fallback；附 MCP server 给 agent 调整 running editor / inspect previews / save / export；MIDI controllers + scripts + CLI；Omarchy / Homebrew Cask / .deb/.rpm/Arch / Windows installer 多平台分发。

## 它解决的问题
2025-2026 年摄影师生态面临 Lightroom 闭源订阅 + Darktable 年久失修 + RawTherapee UI 不友好 + Apple Silicon 适配滞后 + Linux 缺乏原生 GPU 路径的多重痛点。RAWmakase 直击痛点：（1）**non-destructive RAW photo developer in Rust**——open RAW files from the cameras LibRaw supports + Lightroom-style controls + JPEG/PNG/TIFF 也能编辑；（2）**Lightroom Classic .lrcat import with folder relinking**——不写原 catalog 或原照片；（3）**SQLite catalogs + 26 built-in presets + Lightroom XMP + RAWmakase's own Standard/Color profiles + DCP + XMP camera profiles**——预设体系完整；（4）**GPU color & tone stage（Metal / Vulkan / DirectX 12）+ CPU fallback**——viewport size 实时预览；（5）**CLI + MIDI controllers + scripts + built-in MCP server for agents**——programmable + AI agent 集成；（6）**Multi-platform install**——Omarchy `omarchy pkg add rawmakase-bin` + Homebrew Cask `brew install --cask pch/tap/rawmakase` + .deb (Ubuntu 24.04+/Debian 13+) + .rpm (Fedora 43+) + Arch .pkg.tar.zst + Windows installer (x86_64 + ARM64) + From source (Linux/macOS)；（7）**Coming soon LUT support + AI object removal + Agentic features**——预告 LUT/AI/Agentic 集成。解决的是 **「Lightroom 闭源订阅 + Darktable 年久失修 + RawTherapee UI 不友好 + Apple Silicon 适配滞后 + Linux 缺乏原生 GPU + 缺 agent 集成」** 的工程化问题。

## 为什么值得关注（2026-10-16）
- **Stars:** 1199（截至 2026-10-16），20 天 1199⭐ ⑂44 fork/star 3.7%，**增长率** 3.7%（fork/star 反映个人项目类 fork 适度的常态）
- **Forks:** 44，社区贡献稳步
- **Size:** 47530 KB
- **License:** MIT
- **语言:** Rust（核心）+ LibRaw（raw 解码）+ Little CMS（color management）+ SQLite（catalogs）+ Metal/Vulkan/DirectX 12（GPU）+ MCP server（agent 集成）+ MIDI controllers（外部控制）+ .deb/.rpm/Arch（Linux 包）
- **活跃度:** created 2026-09-26，pushed_at 2026-10-15，持续高活跃
- **平台:** Linux (Ubuntu 24.04+/Debian 13+/Fedora 43+/Arch + aarch64) + macOS (15+ Apple Silicon + Intel) + Windows (10+ x86_64 + 11+ ARM64)

## 热度来源判断
RAWmakase 的热度是 **「non-destructive RAW photo developer 严肃工程化 × Rust + LibRaw + Lightroom-style × Lightroom Classic .lrcat import × SQLite + 26 built-in presets + Lightroom XMP + DCP + XMP × GPU color & tone (Metal/Vulkan/DX12) + CPU fallback × CLI + MIDI + MCP server for agents × Omarchy + Homebrew Cask + .deb/.rpm/Arch + Windows installer × MIT** 的组合。这与今日 trending `lexmount/moli`（standalone browser kernel for AI agents）+ 昨日 trending `outcrawlai/scout`（LLM-driven browser agent）+ `deeplethe/solid-glass`（AI 应用设计系统）+ `HeyPuter/everything`（mono-repo OSS 替代）+ `CoolkHz/gptibo`（self-hosted 数字商品商城）等一同指向「严肃工程化跨平台 native 桌面应用 + AI agent 集成 (MCP)」浪潮。MCP server 给 agent 调整 running editor 是 2026 年桌面应用严肃工程化的关键 stand。

## 关键技术亮点
1. **Develop engine：** white balance + picker + one-click Auto tone + Auto white balance + exposure + tone + Shadows/Highlights + Clarity + Dehaze + point curves + levels + HSL color mixer + three-way color grading + detail (denoise + sharpening) + crop + straighten + Transform + lens corrections + effects + calibration
2. **Spot removal and masks（experimental, early）：** Heal + Clone spots + brushed areas + brush + gradient + range masks + local adjustments, also imported from Lightroom；not yet measured against Lightroom
3. **Library：** SQLite catalogs + folders + ratings + flags + color labels + filtering + non-destructive Lightroom .lrcat import with folder relinking
4. **Presets and profiles：** 26 built-in presets + your Lightroom XMP presets + RAWmakase's own Standard and Color profiles for every camera with a usable color matrix + DCP + XMP camera profiles you import yourself
5. **Non-destructive：** originals never modified；edits live in catalog；all writes atomic
6. **Fast previews：** every change renders at viewport size + color & tone stage on GPU（Metal on macOS / Vulkan on Linux / DirectX 12 or Vulkan on Windows）+ CPU fallback
7. **Command line：** inspect / render / export thumbnails / import catalogs + profiles / benchmark without GUI
8. **External control：** MIDI controllers (`docs/midi.md`) + scripts (`docs/automation.md`) + built-in MCP server (`docs/mcp.md`) for agents to adjust the running editor / inspect previews / save / export
9. **Updates：** app checks GitHub for new releases；Apple Silicon + Windows installer builds update themselves；other installs pointed at release page
10. **Omarchy：** `omarchy pkg add rawmakase-bin` 一键装；`omarchy pkg add rawmakase-bin` from Omarchy menu → Install → Package
11. **Homebrew Cask：** `brew install --cask pch/tap/rawmakase`；更新 `brew upgrade --cask rawmakase`
12. **Linux packages：** .deb (Ubuntu 24.04+ / Debian 13+) / .rpm (Fedora 43+) / Arch .pkg.tar.zst（x86_64 + aarch64）；DEB/RPM 包 include LibRaw 和 Little CMS；Arch packages use system dependencies
13. **Windows：** installer (x86_64 + ARM64) signed and notarized；include imaging libraries
14. **macOS：** Homebrew Cask 或 DMG (`rawmakase-v<version>-macos-arm64.dmg` Apple Silicon / `rawmakase-v<version>-macos-x86_64.dmg` Intel)；DMGs signed and notarized + include imaging libraries
15. **From source：** `git clone` → `cargo build --release` for Linux/macOS
16. **Let your agent install it：** 给 coding agent 的 prompt 模板：Install the latest release of RAWmakase for my operating system from https://github.com/pch/rawmakase/releases. Pick the right package for my OS and CPU architecture, verify it against the release's checksums, install it, and tell me how to launch it.
17. **AUR paused：** Install Arch package directly, or (on Arch Linux ARM too) download and extract `rawmakase-<version>-arch-recipe.tar.gz` into an empty folder and build as a normal user: `makepkg -si`
18. **Camera support：** develops photos from almost every current camera；exceptions: Sigma Foveon cameras / monochrome cameras such as Leica Monochrom / DNGs that are already demosaiced ("linear" DNGs, such as merged HDR or panorama files)
19. **Rendering aim：** close, not exact, Lightroom parity（`docs/parity-gaps.md` 明示差距）
20. **1.0 之前 backwards compatibility not guaranteed：** early software in active development；originals are never modified, but keep exports of finished work
21. **Coming soon：** LUT support + AI object removal + Agentic features（如 culling assistance）
22. **4 topics：** linux-desktop + omarchy + photography + raw-editor

## 架构师速览

（详见各趋势的架构师速览表 + Mermaid 架构图。系统边界、主路径、关键权衡、最小 PoC、证据边界、待核验均见下表与图。）

## 架构启发
RAWmakase 的核心启发是 **「non-destructive RAW photo developer 不一定要 Lightroom 闭源订阅或 Darktable / RawTherapee 旧栈——Rust + LibRaw + Lightroom-style + .lrcat import + SQLite + GPU color & tone + MCP server for agents + Omarchy + Homebrew + .deb/.rpm/Arch + Windows」**。当前所有主流 RAW photo developer 要么是闭源订阅（Lightroom / Capture One）、要么是年久失修的开源（Darktable / RawTherapee）、要么是 Apple Silicon 适配滞后、要么是 Linux 缺乏原生 GPU。RAWmakase 走另一条路：Rust 严肃工程化 + LibRaw 跨相机支持 + Lightroom-style UI 减少学习曲线 + Lightroom Classic .lrcat import 让 Lightroom 用户无缝迁移 + SQLite catalogs + 26 built-in presets + Lightroom XMP + DCP + XMP camera profiles + GPU color/tone（Metal/Vulkan/DX12）+ MCP server 给 agent。这与 `outcrawlai/scout`（昨日 trending 636⭐，LLM-driven browser agent on Outcrawl cloud）+ `lexmount/moli`（今日 trending 18659⭐，standalone browser kernel）+ `ViceVerse-cz/Serein`（今日 trending 789⭐，native Discord client in Rust + egui + wgpu）形成 2026 年「严肃工程化跨平台 native 桌面应用 + AI agent 集成 (MCP)」浪潮。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[Photographer<br/>Linux + macOS + Windows] --> App[RAWmakase<br/>Rust + GUI]
  User --> CLI[Command line<br/>inspect / render / export<br/>import catalogs + profiles<br/>benchmark]
  User --> Agent[Claude Code / Codex<br/>coding agent]
  Agent --> MCP[MCP server<br/>docs/mcp.md<br/>adjust running editor<br/>inspect previews<br/>save + export]
  MCP --> App
  User --> MIDI[MIDI controllers<br/>docs/midi.md]
  MIDI --> App
  User --> Script[Scripts<br/>docs/automation.md]
  Script --> App
  App --> Raw[LibRaw<br/>raw 解码<br/>almost every current camera<br/>except Sigma Foveon / monochrome / linear DNG]
  App --> CMS[Little CMS<br/>color management]
  App --> DB[SQLite catalogs<br/>folders + ratings + flags + color labels<br/>filtering + non-destructive .lrcat import<br/>folder relinking]
  App --> Develop[Develop engine<br/>white balance + picker<br/>Auto tone + Auto WB<br/>exposure + tone<br/>Shadows/Highlights + Clarity + Dehaze<br/>curves + levels + HSL + color grading<br/>detail + crop/Transform + lens corrections<br/>effects + calibration]
  App --> Masks[Spot removal and masks<br/>experimental, early<br/>Heal + Clone + brush + gradient + range masks<br/>local adjustments<br/>imported from Lightroom<br/>not yet measured against Lightroom]
  App --> Presets[Presets and profiles<br/>26 built-in<br/>Lightroom XMP presets<br/>RAWmakase Standard/Color profiles<br/>DCP + XMP camera profiles]
  App --> GPU[GPU color & tone stage<br/>Metal macOS<br/>Vulkan Linux<br/>DirectX 12 or Vulkan Windows<br/>+ CPU fallback]
  App --> Export[Export<br/>JPEG + 16-bit TIFF<br/>originals never modified<br/>atomic writes]
  App -.Update.-> Update[GitHub release check<br/>Apple Silicon + Windows installer 自更<br/>other pointed at release page]
  App -.Multi-platform.->[Omarchy `omarchy pkg add rawmakase-bin`<br/>Homebrew Cask `brew install --cask pch/tap/rawmakase`<br/>.deb Ubuntu 24.04+ / Debian 13+<br/>.rpm Fedora 43+<br/>Arch .pkg.tar.zst<br/>Windows installer x86_64 + ARM64<br/>From source]
  App -.Coming soon.-> Future[LUT support<br/>AI object removal<br/>Agentic features<br/>e.g. culling assistance]
```

## 定位判断
**工具型（non-destructive RAW photo developer + Lightroom Classic .lrcat import + GPU color & tone + MCP server for agents）。** RAWmakase 不只是 RAW developer，更是 2026 年桌面应用严肃工程化的 **「Lightroom-style + .lrcat import + SQLite + GPU color/tone + MCP server for agents + Omarchy + Homebrew + MIT」** 严肃工程化路径——在 Lightroom 闭源订阅 + Darktable 年久失修 + RawTherapee UI 不友好的常态，提供「Rust + LibRaw + Lightroom-style + Lightroom Classic .lrcat import + SQLite + 26 built-in presets + Lightroom XMP + DCP + GPU color/tone (Metal/Vulkan/DX12) + CLI + MIDI + MCP server + Omarchy + Homebrew + .deb/.rpm/Arch + Windows installer + 个人项目 + 1.0 之前 backwards compatibility not guaranteed」的严肃工程化方案。1199⭐ ⑂44 + 4 topics（linux-desktop / omarchy / photography / raw-editor）+ MIT + 20 天稳步增长已显示这是跨桌面平台 non-destructive RAW photo developer 的关键 stand。能否成为「Linux/macOS/Windows 摄影师默认 non-destructive RAW photo developer + AI agent 集成」取决于：GUI 框架选型（Tauri / egui / iced / Slint / 自绘 待核验）+ DCP/XMP 解析深度 + Heal/Clone 算法成熟度 + AUR 暂停原因 + 个人项目维护节奏 + 商业模式（订阅/一次性付费/赞助）+ 与 Darktable / RawTherapee 实测对比 + GPU color/tone stage 在不同显卡上的稳定性。

## 风险 / 局限 / 泡沫点
- **GUI 框架选型（Tauri / egui / iced / Slint / 自绘 待核验）：** README 未明示 GUI 框架；Rust 桌面 GUI 选型与 Lightroom-style UI 实现难度相关
- **DCP / XMP 解析深度：** DCP / XMP camera profiles 解析深度决定跨相机兼容性；与 Adobe DNG Converter / Lightroom Classic 的实测差距
- **Heal / Clone 算法实验性边界：** README 明示 "experimental, early" + "not yet measured against Lightroom"；与 Lightroom Classic Heal/Clone 算法的实测差距
- **AUR 暂停原因：** README 明示 "AUR publication is paused"；Arch 用户需 install Arch package directly 或 makepkg -si from arch-recipe.tar.gz
- **个人项目维护节奏：** README 明示 "personal project in active development" + "1.0 之前 backwards compatibility not guaranteed"；渲染引擎可能从一版到下一版改变，已编辑的照片升级后可能 look different
- **商业模式：** 个人项目 + MIT + 1.0 之前 backwards compatibility not guaranteed；订阅/一次性付费/赞助模式未明示
- **与同类对比：** vs Lightroom 闭源订阅 + Darktable 年久失修 + RawTherapee UI 不友好 + Apple Silicon 适配滞后 + Linux 缺乏原生 GPU
- **Camera support 边界：** develops photos from almost every current camera；exceptions: Sigma Foveon cameras / monochrome cameras such as Leica Monochrom / DNGs that are already demosaiced ("linear" DNGs, such as merged HDR or panorama files)
- **Lightroom .lrcat 跨 OS/编码的 folder relinking：** Lightroom Classic .lrcat 在不同 OS / 编码的 catalog 上的 folder relinking 行为；Windows-1252 vs UTF-8 的兼容性
- **GPU color/tone stage 在不同显卡上的稳定性：** Metal macOS / Vulkan Linux / DirectX 12 or Vulkan Windows 在不同显卡（Intel / AMD / NVIDIA）上的稳定性
- **Coming soon 预告：** LUT support + AI object removal + Agentic features（如 culling assistance）尚未实现

## 与同类项目的关系
- **vs Lightroom 闭源订阅：** Lightroom 月费订阅 + Adobe 生态锁定；RAWmakase 是 MIT + 个人项目 + 1.0 之前 backwards compatibility not guaranteed + Coming soon LUT/AI/Agentic
- **vs Darktable：** Darktable 年久失修 + C 实现 + UI 不友好 + Apple Silicon 适配滞后；RAWmakase 是 Rust + Lightroom-style UI + SQLite + GPU color/tone (Metal/Vulkan/DX12) + MCP server
- **vs RawTherapee：** RawTherapee UI 不友好 + Apple Silicon 适配滞后；RAWmakase 是 Rust + Lightroom-style UI + Lightroom Classic .lrcat import + MCP server + Omarchy + Homebrew + .deb/.rpm/Arch + Windows
- **vs Capture One：** Capture One 闭源订阅 + Phase One 生态锁定；RAWmakase 是 MIT + 跨平台 + MCP server for agents
- **vs outcrawlai/scout（昨日 trending 636⭐，LLM-driven browser agent）：** scout 偏 AI browser agent；RAWmakase 偏 non-destructive RAW photo developer + MCP server for agents——两者在「agent 调度」与「agent 集成桌面应用」分工不同但互补
- **vs lexmount/moli（今日 trending 18659⭐，standalone browser kernel for AI agents）：** moli 偏 AI browser kernel；RAWmakase 偏 non-destructive RAW photo developer + MCP server——两者都是 2026 年「严肃工程化跨平台 native 桌面应用 + AI agent 集成」浪潮

## 是否值得持续跟踪
**值得跟踪（non-destructive RAW photo developer + Lightroom Classic .lrcat import + GPU color & tone + MCP server for agents）。** RAWmakase 代表了 2026 年桌面应用严肃工程化的「Lightroom-style + .lrcat import + SQLite + GPU color/tone + MCP server + Omarchy + Homebrew + MIT」严肃工程化路径——在 Lightroom 闭源订阅 + Darktable 年久失修 + RawTherapee UI 不友好的常态，提供跨桌面平台的严肃工程化方案。建议关注：GUI 框架选型 + DCP/XMP 解析深度 + Heal/Clone 算法成熟度 + AUR 暂停原因 + 个人项目维护节奏 + 商业模式 + 与 Darktable / RawTherapee 实测对比 + GPU color/tone stage 在不同显卡上的稳定性 + Coming soon LUT/AI/Agentic features 落地节奏。对摄影师 / Linux desktop 用户 / Apple Silicon 用户 / 想要 non-destructive RAW developer + Lightroom Classic .lrcat 兼容 + AI agent MCP 集成的团队 / 个人，这是 2026 年严肃工程化跨平台方案的代表，值得直接采用。

## 后续观察点
- GUI 框架选型（Tauri / egui / iced / Slint / 自绘）+ 与 Lightroom-style UI 实现的实测表现
- DCP / XMP camera profiles 解析深度 + 跨相机兼容性 + 与 Adobe DNG Converter / Lightroom Classic 实测对比
- Heal / Clone + brush + gradient + range masks 算法成熟度 + "not yet measured against Lightroom" 何时给出实测数字
- AUR 暂停原因 + Arch 用户安装路径稳定度
- 个人项目维护节奏 + 1.0 之前 backwards compatibility not guaranteed 实际如何兑现 + 商业模式（订阅/一次性付费/赞助）
- Coming soon LUT support / AI object removal / Agentic features（如 culling assistance）落地节奏
- Lightroom Classic .lrcat 跨 OS/编码的 folder relinking 行为 + Windows-1252 vs UTF-8 兼容性
- GPU color/tone stage 在 Intel / AMD / NVIDIA 不同显卡上的稳定性
- 与 Darktable / RawTherapee / darktable 实测对比

---
*首次记录：2026-10-16*