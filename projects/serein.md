---
title: "ViceVerse-cz/Serein"
slug: serein
date_added: "2026-10-16"
last_seen_date: "2026-10-16"
category: "工具型"
emoji: "💬"
stars: "789 stars"
stars_delta: "37 天 789⭐ ⑂46 fork/star 5.8%（持续高增长，Rust native Discord client 需求强）"
language: "Rust"
score: 82
tags: ["serein","ViceVerse-cz","discord-client","rust","egui","wgpu","native","immediate-mode","discord-gateway","discord-rest","os-keychain","webview","wkwebview","webview2","webkitgtk","flatpak","snap","homebrew","voice","opus","dave","sonora-aec","rnnoise","video-decode","multi-crate","replay-bench","xtask","mit-or-apache-2","unofficial-discord-client"]
url: "https://github.com/ViceVerse-cz/Serein"
---

# ViceVerse-cz/Serein

## 一句话定位
Serein 是一个 lightweight, native Discord desktop client written in Rust, powered by egui and wgpu——immediate-mode rendering + minimal idle CPU + low memory footprint + instantaneous launch + zero Electron / Node.js / web runtime overhead；Direct gateway & REST（active rate-limit cooldowns + heartbeat handling + reconnect/resume loops + partial payload patching）+ macOS Keychain / Windows Credential Manager / Linux Secret Service 存 session token + ephemeral WKWebView/WebView2/WebKitGTK 官方登录页（email/password + QR + MFA + origin-checked handoff + immediate webview termination）+ voice（Opus + RTP/UDP + DAVE v1 + Sonora AEC + RNNoise + video decode）+ multi-crate Cargo workspace（apps/desktop + 11 crates + 2 tools）+ Multi-platform Distribution（Windows NSIS / macOS HB/Nix / Linux Flatpak/repos/Gentoo/Nix/AppImage）。

## 它解决的问题
2025-2026 年 Discord 用户面临 Electron 庞大 + 隐私疑云 + 资源高占用 + 闭源 + 无法 hack + vendor lock 的多重痛点。Serein 直击痛点：（1）**Pure Native Performance**——built with pure Rust, egui, wgpu + immediate-mode rendering + minimal idle CPU + low memory footprint + instantaneous launch + zero Electron / Node.js / web runtime overhead；（2）**Direct Gateway & REST Transports**——Direct connection to Discord's official endpoints with active rate-limiting cooldowns + heartbeat handling + reconnect/resume loops + partial payload patching；（3）**Secure OS Credential Storage**——session tokens stored exclusively in macOS Keychain / Windows Credential Manager / Linux Secret Service，never plaintext；（4）**Ephemeral Authentication Webview**——sign-in uses Discord's official hosted login page inside temporary native webview (WKWebView / WebView2 / WebKitGTK) supporting email/password + QR login + MFA + origin-checked handoff + immediate webview termination；（5）**Voice**——Opus codec + RTP/UDP + DAVE v1 + Sonora AEC + RNNoise + video decode；（6）**Multi-platform Distribution**——Windows NSIS Setup.exe + .zip (x86_64 + aarch64) / macOS Homebrew Cask + .zip + Nix flake (signed + notarized .app bundle, Apple Silicon only) / Linux Flatpak (sandbox isolation + bundled GNOME/WebKit runtimes + 自动 background updates) + apt/dnf/zypper/pacman 签名 repo + Gentoo ebuild + Nix flake + AppImage；（7）**Multi-crate Cargo workspace**——apps/desktop 入口 + 11 crates (client-core / session-cache / ui / model / discord-protocol / discord-api / discord-gateway / discord-voice / local-store / platform / test-support) + tools (replay-bench / xtask)；（8）**Benchmarks vs Official Discord**——measure performance: idle CPU, memory footprint, launch time。解决的是 **「Discord 客户端 Electron 庞大 + 隐私疑云 + 资源高占用 + 闭源 + 无法 hack + vendor lock」** 的工程化问题。

## 为什么值得关注（2026-10-16）
- **Stars:** 789（截至 2026-10-16），37 天 789⭐ ⑂46 fork/star 5.8%，**增长率** 5.8%（fork/star 反映社区参与度，Rust native Discord client 类项目 fork 多因 fork = 自托管定制）
- **Forks:** 46
- **Size:** 212992 KB（Rust 编译产物 + assets）
- **License:** MIT OR Apache-2.0
- **语言:** Rust 1.98.1 pinned + egui + wgpu + 11 crates + 2 tools
- **活跃度:** created 2026-09-09，pushed_at 2026-10-15，持续高活跃
- **平台:** Windows (NSIS Setup.exe + .zip; x86_64 + aarch64) / macOS (Homebrew Cask + .zip + Nix flake; signed + notarized .app bundle, Apple Silicon only) / Linux (Flatpak 推荐 sandbox isolation + bundled GNOME/WebKit runtimes + 自动 background updates + apt/dnf/zypper/pacman 签名 repo + Gentoo ebuild + Nix flake + AppImage)

## 热度来源判断
Serein 的热度是 **「Discord 客户端 Electron 庞大 + 隐私疑云 + 资源高占用 + 闭源严肃工程化 × Rust 1.98.1 pinned + egui + wgpu × immediate-mode + zero Electron/Node.js/web runtime × Direct gateway & REST × OS Credential Storage (Keychain/CredManager/SecretService) × Ephemeral WKWebView/WebView2/WebKitGTK login (email/password + QR + MFA) × voice (Opus + RTP/UDP + DAVE v1 + Sonora AEC + RNNoise + video decode) × multi-crate Cargo workspace (apps/desktop + 11 crates + 2 tools) × Flatpak sandbox + apt/dnf/zypper/pacman 签名 repo + Gentoo + Nix + AppImage × Benchmarks vs Official Discord × MIT OR Apache-2.0** 的组合。`fork/star 5.8%` 适中说明 fork = 自托管定制 / 二次开发候选。Unofficial and not endorsed by Discord + Automating normal accounts outside the official OAuth2/bot API violates Discord's ToS + carry risk of account termination 是关键风险——README 明示但 Serein 通过 "Communicates directly with Discord's public gateway and REST endpoints for your existing account" 强调这是「client-side normal user」而非「account automation」。

## 关键技术亮点
1. **Pure Native Performance：** built with pure Rust + egui + wgpu + immediate-mode rendering + minimal idle CPU + low memory footprint + instantaneous launch + zero Electron / Node.js / web runtime overhead
2. **Direct Gateway & REST Transports：** Direct connection to Discord's official endpoints with active rate-limiting cooldowns + heartbeat handling + reconnect/resume loops + partial payload patching
3. **Secure OS Credential Storage：** session tokens stored exclusively in macOS Keychain / Windows Credential Manager / Linux Secret Service；never plaintext
4. **Ephemeral Authentication Webview：** sign-in uses Discord's official hosted login page inside temporary native webview (WKWebView / WebView2 / WebKitGTK) supporting email/password + QR login + MFA + origin-checked handoff + immediate webview termination
5. **Voice：** Opus codec + RTP/UDP + DAVE v1 (Discord's E2EE protocol) + Sonora AEC (acoustic echo cancellation) + RNNoise (recurrent neural network noise suppression) + video decoding
6. **Multi-platform Distribution：**
   - **Windows：** NSIS Setup.exe (per-user recommended) 或 standalone .zip；x86_64 + aarch64
   - **macOS：** Homebrew Cask + .zip + Nix flake (signed + notarized .app bundle, Apple Silicon only)
   - **Linux：** Flatpak (sandbox isolation + bundled GNOME/WebKit runtimes + 自动 background updates) + apt/dnf/zypper/pacman 签名 repo + Gentoo ebuild + Nix flake + AppImage
7. **One-Click Repository Install (Flatpak)：** `flatpak install --user https://viceverse-cz.github.io/Serein/flatpak/serein.flatpakref` → 自动 sandbox + bundled GNOME/WebKit runtimes + 自动 background updates via GNOME Software / KDE Discover / `flatpak update`
8. **Standalone Offline Bundle (Flatpak)：** `flatpak install --user ./Serein-linux.flatpak` + `flatpak run cz.viceverse.serein`
9. **Native Package Repositories：** `sudo apt install serein` (Ubuntu/Debian) / `sudo dnf install serein` (Fedora) / `sudo zypper install serein` (openSUSE) / `sudo pacman -S serein` (Arch)
10. **Gentoo：** source or binary
11. **Nix：** flake
12. **Standalone AppImage (Portable)：** portable
13. **Multi-crate Cargo workspace：**
    - `apps/desktop/` —— Application entrypoint, CLI flags, window lifecycle
    - `crates/client-core/` —— Client state coordinator, generation tracking, events
    - `crates/session-cache/` —— In-memory bounded cache and state reconciliation
    - `crates/ui/` —— egui widgets, message virtualizer, themes, design tokens
    - `crates/model/` —— Strongly-typed Discord domain entities
    - `crates/discord-protocol/` —— Wire protocol serialization and partial payload patches
    - `crates/discord-api/` —— HTTP/2 REST client with rate limiting and backoff
    - `crates/discord-gateway/` —— WebSocket gateway client with heartbeat and resume
    - `crates/discord-voice/` —— Opus codecs, RTP/UDP transport, DAVE v1, Sonora AEC, RNNoise, video decoding
    - `crates/local-store/` —— Bounded SQLite database for history, drafts, settings
    - `crates/platform/` —— OS credential store (Keychain/CredManager/SecretService)
    - `crates/test-support/` —— Deterministic synthetic fixtures and mocks
14. **Tools：**
    - `tools/replay-bench/` —— Benchmarking harness for state reducers
    - `tools/xtask/` —— Workspace automation tasks (packaging, checks, linting)
15. **Workspace Commands：** `Run full workspace validation (formatting, Clippy, tests, policy checks)` / `Run release reducer benchmark` / `Run authentication bridge JS test harness` / `Package release including voice (macOS .app bundle, Linux .deb by default)`
16. **Benchmarks vs Official Discord：** measure performance: idle CPU, memory footprint, launch time
17. **Compatibility Matrix：** `docs/discord-compatibility.md` 明示与 Discord 协议版本的兼容状态
18. **Authentication Guide：** `docs/authentication.md` 明示登录流程
19. **Security & Storage Policy：** 明示 session token 存储策略与 Ephemeral Webview 策略
20. **Rust 1.98.1 pinned：** 锁版本确保 reproducibility
21. **Discord community：** `https://discord.gg/UqTDGCENaN` (Join our Discord server for updates)
23. **Unofficial and not endorsed by Discord：** README 明示 + Automating normal accounts outside the official OAuth2/bot API violates Discord's ToS + carry risk of account termination；Technical interoperability does not imply platform approval
24. **MIT OR Apache-2.0：** 双许可

## 架构师速览

（详见各趋势的架构师速览表 + Mermaid 架构图。系统边界、主路径、关键权衡、最小 PoC、证据边界、待核验均见下表与图。）

## 架构启发
Serein 的核心启发是 **「Discord 客户端不一定要 Electron——Rust + egui + wgpu + immediate-mode + multi-crate Cargo workspace + Direct gateway/REST + Ephemeral Webview login + OS Credential Storage + Multi-platform Distribution」**。当前所有主流 Discord 客户端（Discord official / WebCord / ArmCord / Vesktop / Vencord）都基于 Electron 或 webview wrapper——资源占用高、隐私疑云、闭源、无法 hack。Serein 走另一条路：Rust 1.98.1 pinned + egui + wgpu + immediate-mode rendering + Direct gateway & REST + OS Credential Storage + Ephemeral Authentication Webview（用 Discord 官方 hosted login page in WKWebView/WebView2/WebKitGTK + email/password + QR + MFA + origin-checked handoff + immediate webview termination）+ Voice（Opus + RTP/UDP + DAVE v1 + Sonora AEC + RNNoise + video decode）+ Multi-crate Cargo workspace（apps/desktop + 11 crates + 2 tools）+ Multi-platform Distribution（Windows NSIS / macOS HB/Nix / Linux Flatpak/repos/Gentoo/Nix/AppImage）+ Benchmarks vs Official Discord。这与今日 `lexmount/moli`（18659⭐ standalone browser kernel）+ `pch/rawmakase`（1199⭐ Rust + LibRaw + Lightroom-style + MCP server for agents）+ 昨日 `outcrawlai/scout`（636⭐ LLM-driven browser agent）形成 2026 年「严肃工程化跨平台 native 桌面应用 + 隐私友好 + 开源 + 可 hack」浪潮。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[Discord user<br/>Windows + macOS + Linux] --> Distribution[Distribution layer]
  Distribution --> Win[Windows<br/>NSIS Setup.exe + .zip<br/>x86_64 + aarch64]
  Distribution --> Mac[macOS<br/>Homebrew Cask + .zip + Nix flake<br/>signed + notarized .app bundle<br/>Apple Silicon only]
  Distribution --> Linux[Linux<br/>Flatpak + apt/dnf/zypper/pacman<br/>Gentoo + Nix + AppImage]
  Win --> App[Serein app<br/>apps/desktop<br/>Rust 1.98.1 pinned<br/>egui + wgpu<br/>immediate-mode<br/>zero Electron / Node.js / web runtime]
  Mac --> App
  Linux --> App
  App --> Webview[Ephemeral Authentication Webview<br/>WKWebView / WebView2 / WebKitGTK<br/>Discord's official hosted login page<br/>email/password + QR + MFA<br/>origin-checked handoff<br/>immediate webview termination]
  Webview -.session credential.-> CredStore[OS Credential Storage<br/>macOS Keychain<br/>Windows Credential Manager<br/>Linux Secret Service<br/>never plaintext]
  App --> Gateway[discord-gateway<br/>WebSocket client<br/>heartbeat + resume<br/>reconnect loops]
  App --> REST[discord-api<br/>HTTP/2 REST client<br/>active rate-limiting cooldowns<br/>backoff]
  App --> Protocol[discord-protocol<br/>wire protocol serialization<br/>partial payload patches]
  App --> Voice[discord-voice<br/>Opus codec<br/>RTP/UDP transport<br/>DAVE v1 (Discord E2EE)<br/>Sonora AEC<br/>RNNoise<br/>video decoding]
  App --> ClientCore[client-core<br/>state coordinator<br/>generation tracking<br/>events]
  App --> SessionCache[session-cache<br/>in-memory bounded cache<br/>state reconciliation]
  App --> UI[ui<br/>egui widgets<br/>message virtualizer<br/>themes + design tokens]
  App --> Model[model<br/>strongly-typed Discord domain entities]
  App --> LocalStore[local-store<br/>bounded SQLite database<br/>history + drafts + settings]
  App --> Platform[platform<br/>OS credential store abstraction]
  App --> TestSupport[test-support<br/>deterministic synthetic fixtures<br/>mocks]
  App -.Benchmarks vs.-> Official[Official Discord Electron app<br/>measure performance:<br/>idle CPU + memory footprint + launch time]
  App -.Unofficial.-> ToS[Discord ToS risk<br/>Automating normal accounts<br/>outside official OAuth2/bot API<br/>violates Discord's ToS<br/>carry risk of account termination]
  Tools[tools/<br/>replay-bench<br/>xtask] -.wsbench.| WS[Benchmarking harness<br/>state reducers]
  Tools -.xtask.-> Workspace[Workspace automation<br/>packaging + checks + linting]
  Discord[Discord public gateway + REST endpoints<br/>user's existing account] --> Gateway
  Discord --> REST
```

## 定位判断
**工具型（native Discord desktop client in Rust + egui + wgpu + multi-crate Cargo workspace）。** Serein 不只是 Discord 客户端，更是 2026 年 desktop 客户端严肃工程化的 **「Rust + egui + wgpu + immediate-mode + zero Electron + Direct gateway/REST + OS Credential Storage + Ephemeral Webview login + Voice (Opus + DAVE + AEC + RNNoise) + multi-crate Cargo workspace + Multi-platform Distribution」** 严肃工程化路径——在 Electron 庞大 + 隐私疑云 + 资源高占用 + 闭源 + vendor lock 的常态，提供「Rust + egui + wgpu + immediate-mode + zero Electron + Direct gateway/REST + OS Credential Storage + Ephemeral Webview login + Voice + multi-crate + Flatpak + MIT OR Apache-2.0」的严肃工程化方案。789⭐ ⑂46 + 37 天稳步增长已显示这是 Discord 客户端的关键 stand。能否成为「Discord 用户默认 native 客户端」取决于：Unofficial and not endorsed by Discord + Automating normal accounts outside the official OAuth2/bot API violates Discord's ToS + carry risk of account termination + Discord 官方对其 non-endorsement 后续动作 + Flatpak sandbox permissions 与用户的兼容性 + macOS 签名与公证的稳定性 + 11 crates 之间的依赖图 + Bound SQLite 的具体 schema + Sonora AEC 与 RNNoise 的实测效果 + 与 WebCord / ArmCord / Vesktop / Vencord 等其他 native Discord client 的实测差异。

## 风险 / 局限 / 泡沫点
- **Unofficial and not endorsed by Discord：** README 明示 + Automating normal accounts outside the official OAuth2/bot API violates Discord's ToS + carry risk of account termination；Technical interoperability does not imply platform approval；Review the compatibility matrix (`docs/discord-compatibility.md`) and authentication guide (`docs/authentication.md`) before use
- **Discord 官方对其 non-endorsement 后续动作：** Discord 可能更新 API / 反自动化策略 / 封禁 normal account automation 行为；client-side normal user 风险相对较低但持续存在
- **Flatpak sandbox permissions 与用户的兼容性：** sandbox isolation + bundled GNOME/WebKit runtimes 与用户的兼容性问题（文件系统访问 / 网络访问 / 摄像头 / 麦克风 / 屏幕共享）
- **macOS 签名与公证的稳定性：** signed + notarized .app bundle 依赖 Apple Developer ID + notarization 流程；Nix build 是 unsigned
- **11 crates 之间的依赖图：** apps/desktop + 11 crates + 2 tools 的依赖图与 bounded SQLite database 的 schema 未在 README 明示；具体 client-core / session-cache / discord-voice / local-store 的 API 边界未公开
- **Bound SQLite 的具体 schema：** local-store 的 bounded SQLite database for history / drafts / settings schema 未明示
- **Sonora AEC 与 RNNoise 的实测效果：** 声学回声消除 + 循环神经网络噪声抑制的实测效果；与官方 Discord 的实测对比
- **Benchmarks vs Official Discord：** measure performance: idle CPU, memory footprint, launch time；具体数字与持续 benchmarks 未在 README 明示
- **与 WebCord / ArmCord / Vesktop / Vencord 等其他 native Discord client 的实测差异：** WebCord (Electron wrapper) / ArmCord (ArmCord mod) / Vesktop (Vencord mod) / Vencord (client mod) 各自的实测差异
- **Apple Silicon only：** macOS 仅支持 Apple Silicon (aarch64)；Intel Mac 用户需 Nix flake (unsigned)

## 与同类项目的关系
- **vs Discord official (Electron app)：** Discord official 是 Electron 庞大 + 资源高占用 + 闭源 + vendor lock；Serein 是 Rust + egui + wgpu + immediate-mode + zero Electron + Direct gateway/REST + OS Credential Storage + Ephemeral Webview login + Voice + multi-crate + MIT OR Apache-2.0
- **vs WebCord / ArmCord / Vesktop / Vencord：** WebCord (Electron wrapper) / ArmCord / Vesktop (Vencord mod) / Vencord (client mod) 都基于 Electron 或 webview wrapper；Serein 是 Rust + egui + wgpu + immediate-mode + zero Electron + multi-crate + 独立仓库
- **vs outcrawlai/scout（昨日 trending 636⭐，LLM-driven browser agent）：** scout 偏 AI browser agent；Serein 偏 native Discord client——两者无直接竞争，但都是 2026 年「严肃工程化跨平台 native 桌面应用」浪潮
- **vs lexmount/moli（今日 trending 18659⭐，standalone browser kernel for AI agents）：** moli 偏 AI browser kernel；Serein 偏 native Discord client——两者都是 2026 年「严肃工程化 native 桌面应用」浪潮
- **vs pch/rawmakase（今日 trending 1199⭐，non-destructive RAW photo developer）：** rawmakase 偏 photo developer + MCP server for agents；Serein 偏 Discord client——两者都是 2026 年「严肃工程化跨平台 native 桌面应用 + 隐私友好 + 开源 + 可 hack」浪潮
- **vs agentswha/herdr-web-ui（今日 trending 1022⭐，Claude Code and Codex, from your phone）：** herdr-web-ui 偏 coding agent 远程控制 client；Serein 偏 Discord client——两者无直接竞争

## 是否值得持续跟踪
**值得跟踪（native Discord desktop client in Rust + egui + wgpu + multi-crate Cargo workspace）。** Serein 代表了 2026 年 desktop 客户端的「Rust + egui + wgpu + immediate-mode + zero Electron + Direct gateway/REST + OS Credential Storage + Ephemeral Webview login + Voice + multi-crate + Flatpak + MIT OR Apache-2.0」严肃工程化路径——在 Electron 庞大 + 隐私疑云 + 资源高占用 + 闭源 + vendor lock 的常态，提供 Discord 客户端的严肃工程化方案。建议关注：Discord 官方对其 non-endorsement 后续动作 + Flatpak sandbox permissions 与用户的兼容性 + macOS 签名与公证的稳定性 + 11 crates 之间的依赖图 + Bound SQLite 的具体 schema + Sonora AEC 与 RNNoise 的实测效果 + Benchmarks vs Official Discord + 与 WebCord / ArmCord / Vesktop / Vencord 实测差异。对 Discord 用户 / 隐私敏感用户 / Linux desktop 用户 / Apple Silicon 用户 / 想 fork 改造 Discord 客户端的开发者，这是 2026 年严肃工程化跨平台 native Discord 客户端的代表，值得直接采用。

## 后续观察点
- Discord 官方对其 non-endorsement 后续动作（API 变更 / 反自动化策略 / 封禁 normal account automation）
- Flatpak sandbox permissions 与用户的兼容性 + 摄像头 / 麦克风 / 屏幕共享的实际可用性
- macOS 签名与公证的稳定性 + Apple Developer ID + notarization 流程
- 11 crates 之间的依赖图 + client-core / session-cache / discord-voice / local-store 的 API 边界
- Bound SQLite 的具体 schema（history / drafts / settings）+ 跨 OS 编码兼容性
- Sonora AEC + RNNoise + DAVE v1 + Opus + RTP/UDP + video decoding 的实测效果
- Benchmarks vs Official Discord 数字（idle CPU + memory footprint + launch time）
- 与 WebCord / ArmCord / Vesktop / Vencord 等其他 native Discord client 的实测差异
- Apple Silicon only 限制 + Intel Mac 用户 Nix flake (unsigned) 路径
- Multi-platform Distribution 实际分发渠道（Flatpak / Homebrew Cask / apt/dnf/zypper/pacman 签名 repo / Gentoo / Nix / AppImage / Windows NSIS）

---
*首次记录：2026-10-16*