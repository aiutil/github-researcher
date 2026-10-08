---
title: "storytold/gridcraft"
slug: gridcraft
date_added: "2026-10-09"
category: "工具型"
emoji: "📊"
stars: "498 stars"
stars_delta: "2 天 498⭐ ⑂227 fork/star 45.6%"
language: "Rust"
license: "Apache-2.0"
score: 86
tags: ["gridcraft", "storytold", "microsoft-excel", "clean-room", "100-percent-rust", "spreadsheet", "mcp-server", "wasm", "artcraft-team", "discord", "getartcraft-com", "apache-2", "2-days"]
url: "https://github.com/storytold/gridcraft"
---

# storytold/gridcraft

## 一句话定位
Microsoft Excel 的 Rust 100% clean-room 重实现——把「Excel 严肃工程化替代」从「LibreOffice Calc（部分兼容）+ OnlyOffice + 闭源 Excel Online」推到「GridCraft Excel-style 严肃工程化 + 跨平台 + MCP server + WebAssembly + ArtCraft 团队 + Discord + getartcraft.com + Apache-2.0」严肃工程化形态。

## 它解决的问题
2026 年「Excel 严肃工程化替代」的痛点是 **「绝大多数 Excel 替代要么严肃翻页格式（Google Sheets）+ 闭源（Excel Online）+ 部分兼容（LibreOffice Calc）+ SaaS 强制订阅（Microsoft 365）+ 无 MCP server + 无 agent 可编程化」**。GridCraft 直击这一痛点：把「Excel 严肃工程化替代」从「LibreOffice Calc + OnlyOffice + 闭源 Excel Online」推到「GridCraft Excel-style 严肃工程化 + 跨平台 + MCP server + WebAssembly + Apache-2.0」严肃工程化形态。解决的是 **「Excel 严肃工程化替代 + 100% Rust clean-room + 跨平台覆盖广度 + WebAssembly + MCP server 多 tool 严肃工程化 + Apache-2.0 商用清晰 + agent 可编程化」** 的 Excel 严肃工程化替代问题。

## 为什么值得关注（2026-10-09）
- **Stars:** 498（截至 2026-10-09），2 天 498⭐，fork 227，fork/star 45.6%（fork/star 高，反映社区强烈参与）
- **Forks:** 227（典型高 fork 严肃工程化持续关注信号）
- **License:** Apache-2.0（明确许可，商用清晰）
- **语言:** Rust（100% Rust + Native + No Electron no Tauri）
- **活跃度:** created 2026-10-07，2 天内冲到 498 推严肃工程化承诺
- **规模:** 4490 KB（严肃工程化典型规模）
- **Topics:** gridcraft / microsoft-excel / clean-room / 100-percent-rust / spreadsheet / mcp-server / wasm / artcraft-team / discord / getartcraft-com / apache-2 / 2-days（覆盖广）

## 热度来源判断
GridCraft 的热度是 **「Excel 严肃工程化替代刚需 × ArtCraft 团队 12 库全家桶严肃工程化 × MCP server agent 可编程化 × Apache-2.0 商用清晰 × StoryTold 个人 + ArtCraft 团队 + Discord 社区」** 的强劲组合。Excel 是装机量最大的桌面表格软件之一，但「严肃工程化 100% Rust + 跨平台 + clean-room + WebAssembly + MCP server + Apache-2.0 商用清晰」替代品几乎空白。GridCraft + 同源 11 库同步严肃工程化反映 ArtCraft 团队正从「单 alpha 半成品」推到「12 库全家桶 + 跨平台 + WebAssembly + MCP server + Apache-2.0 商用清晰」严肃工程化全家桶形态。热度**真实且具网络效应潜力**——但需警惕：12 库覆盖广度虽猛但各库成熟度参差；Apache-2.0 商用清晰但与 Microsoft 商业关系需关注（clean-room 是合规底线）；StoryTold 个人 + ArtCraft 团队治理可持续性需观察。

## 关键技术亮点
1. **100% Rust clean-room:** Microsoft Excel 的 Rust 100% clean-room 重实现
2. **Spreadsheet 严肃工程化:** Excel-style 严肃工程化（cells, formulas, charts, pivot tables 真实支持范围待核验）
3. **跨平台覆盖广度:** 跨平台 + MCP server + WebAssembly
4. **Apache-2.0 商用清晰:** ArtCraft 团队 + Discord + getartcraft.com + Crafting Apps series
5. **同源 Crafting Apps 系列:** 与 wordcraft / cadcraft / soundcraft / deckcraft / photocraft / filmcraft / lightcraft / pdfcraft / vectorcraft / effectcraft / designcraft 11 库共享 crates 抽象

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 跨平台的 Excel 严肃工程化替代，仓库是 spreadsheet crates 而非运行时 | 仅基于档案描述的 Excel-style + Rust clean-room + Apache-2.0；具体业务功能实现（cells, formulas, charts, pivot tables）、wargo.toml 依赖治理、与 wordcraft crates 复用程度未在档案中给出 |
| 主路径 | 贡献者 → GridCraft spreadsheet crates → Native + Web WebAssembly + MCP server → 多端输出 | 主路径为档案语义抽象；具体命令实现细节、各层接口契约、agent SDK 形态均待核验 |
| 关键权衡 | Excel 严肃工程化替代覆盖广度 vs 真实完成度 vs Apache-2.0 商用与 Microsoft 商业关系 vs 12 库维护可持续性 | 档案明示覆盖广度（Excel-style）、商业模式（Apache-2.0）；与 Microsoft 商业关系、各库质量评测、StoryTold 治理可持续性未给出 |
| 最小 PoC | 安装 GridCraft 打开 1 个 .xlsx 文件（需自备），执行 1 个非破坏性命令（修改 cell 数值），通过 MCP server 验证同一引擎可驱动 UI 与 agent | PoC 范围、退出路径由档案「单渠道、最小命令、可审计」建议推导；具体测试 .xlsx、benchmark、SLO 指标待核验 |

## 架构启发
GridCraft 的核心启发是 **「Excel 严肃工程化替代应该跨平台 + agent-driven，正如 LibreOffice Calc 之于 Excel，但增加 MCP server 让 agent 可编程化」**。Excel 是装机量最大的桌面表格软件之一，但 SaaS 强制订阅 + 闭源 + 单平台 + 无 MCP server 的现实让「Excel 严肃工程化替代」是清晰刚需。GridCraft + 跨平台 + WebAssembly + MCP server 让 Excel 严肃工程化对象成为「agent 可编程化」的严肃工程化对象。能否持续，取决于 StoryTold 个人 + ArtCraft 团队治理可持续性 + 与 Microsoft 商业关系应对。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Contributor[StoryTold + ArtCraft 团队 + 社区贡献] --> Crates[GridCraft spreadsheet crates<br/>wordcraft crates 抽象跨套件复用 待核验]
  Crates --> Native[Native 跨平台<br/>egui on GPU]
  Crates --> Web[Web WebAssembly]
  Crates --> MCP[GridCraft MCP server]
  Native --> Engines[Spreadsheet commands<br/>cells/formulas/charts/pivot 真实完成度待核验]
  Web --> Engines
  MCP --> Engines
  Engines --> XLSX[.xlsx read/write<br/>真实格式支持范围待核验]
  Engines --> Family[同源 Crafting Apps 系列<br/>wordcraft / cadcraft / soundcraft / deckcraft<br/>photocraft / filmcraft / lightcraft / pdfcraft<br/>vectorcraft / effectcraft / designcraft]
  Engines -.边界.-> Risk[Apache-2.0 与 Microsoft 商业关系<br/>Excel 真实完成度待核验]
```

## 定位判断
**工具型项目（Excel 严肃工程化替代 + agent 可编程化）。** GridCraft 不仅是 Excel 替代品，更试图成为「Excel 严肃工程化替代 + agent 可编程化」的双重工具。2 天 498⭐ + fork/star 45.6% 已显示市场关注。但「Excel 真实完成度」+ Apache-2.0 商用与 Microsoft 商业关系的应对是长期可持续性的关键。目前定位是「最有影响力的 Excel 严肃工程化替代 + agent 可编程化工具」，向「ArtCraft 12 库全家桶成员之一」演进是合理路径。

## 风险 / 局限 / 泡沫点
- **Excel 真实完成度有限：** 与 wordcraft 87% ribbon + 62% real parity 不同，GridCraft 未给 parity 数字
- **12 库覆盖广度 vs 各库成熟度参差：** wordcraft parity 数字明示，其余 11 库未给 parity 数字
- **Apache-2.0 商用与 Microsoft 商业关系：** clean-room 是合规底线，但 .xlsx 文档格式的兼容性需长期测试
- **StoryTold 个人 + ArtCraft 团队治理：** 12 库同步维护但核心维护集中度高
- **MCP server 同步维护成本高：** 与 wordcraft 共享同一 mcp crate 但各自维护工具定义

## 与同类项目的关系
- **vs LibreOffice Calc:** LibreOffice Calc 仅 UI + 部分兼容；GridCraft 增加 MCP server + 跨平台 + WebAssembly
- **vs OnlyOffice:** OnlyOffice 是 SaaS 强制订阅；GridCraft 是 Apache-2.0
- **vs Microsoft Excel Online:** Excel Online 是闭源；GridCraft 是 100% Rust + Apache-2.0
- **vs Google Sheets:** Google Sheets 是 SaaS 严肃翻页；GridCraft 是 desktop native + 跨平台
- **vs ArtCraft 同源 11 库:** 同源 Crafting Apps 系列 + Apache-2.0 + crates 抽象跨套件可复用

## 是否值得持续跟踪
**值得跟踪（Excel 严肃工程化替代 + agent 可编程化）。** GridCraft 代表了「Excel 严肃工程化替代 + agent 可编程化」的诉求。建议关注：Apache-2.0 商用与 Microsoft 商业关系应对、StoryTold 个人 + ArtCraft 团队治理可持续性、12 库完成度统一披露、MCP server 在表格软件领域的应用采纳。

## 后续观察点
- Excel 真实完成度（vs 数字）
- Apache-2.0 商用与 Microsoft 商业关系（clean-room 是合规底线）
- StoryTold 个人 + ArtCraft 团队治理可持续性
- MCP server 在表格软件领域的应用采纳
- 12 库 parity 数字统一披露
- 企业采用（团队是否将此作为 Excel 严肃工程化替代默认来源）

---
*首次记录：2026-10-09*