# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-11-17.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-11-17

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 9 | 833 | 5 | 134k+ |

**今日核心判断：** 本日最硬的发现是**投放体的「账号队列」从一次性突击升级成了长期在编的产能** —— ⭐⭐⭐⭐⭐ `cheat client` 族的 **9 个仓库（ROB RUN ×3 / PUBG / GTA V / Apex Legends / Warzone / CoD MW4 / Marvel Rivals）共享同一套 README 模板（capsule-render 横幅生成器 + `readme-typing-svg` 打字动效 + shields.io 徽章 + 一张功能表），且其中 6 个统一指向同一条载荷域名 `modbay.live`**，⭐⭐⭐⭐⭐ **每个仓库的整棵树只有 2 个 blob（`LICENSE` + `README.md`），0 个代码文件，0 个 open issue**；⭐⭐⭐⭐⭐ 而**最关键的一条是「占位仓库指纹」首次被做成对照实验**：⭐⭐⭐⭐⭐ 本日报实测 **10/10 个投放账号**各持有一个「README 恰好等于 `# <仓库名>`、10 字节、1 个 blob、0⭐」的随机名占位仓库（`trckulpa` / `szoyxrqs` / `fzohpjud` / `cwjhmbpo` / `ugqbrkec` / `hrolzfoa` / `nuxtdjnj` / `upzuukrt` / `rqpylldg` / `khcmkgzv`），⭐⭐⭐⭐⭐ **对照组的 16 个普通账号里只有 1 个（`staryone/sanckut`）命中同一签名** —— 即 **6.25% vs 100%**，⭐⭐⭐⭐⭐ **这使「占位仓库」成为比「账号注册时间聚集」更硬、更便宜（一次 `users/{owner}/repos` 请求即可判定）的判据**。⭐⭐⭐⭐⭐ 与之并列的第二个发现是**投放方的账号是跨月常备的，不是当天现注册的**：⭐⭐⭐⭐⭐ 实测账号分三批创建 —— **2026-08-10 一批 6 个（`22:36:14Z–22:37:15Z`，跨度 61 秒）**、**2026-09-21 一批 2 个（`17:24:55Z–17:25:39Z`）**、**2026-06-15 一批 2 个**，⭐⭐⭐⭐⭐ **且 `2026-08-10` 那一批正好是 11-15 日报记录的 `2026-08-10T10:11:27Z` 账号队列的同一批注册窗口** —— ⭐⭐⭐⭐⭐ **即「账号注册聚集度」这条判据在 11-16 已被证明会被时间稀释（账号当天新建并不成立），而本日的证据表明：投放方干脆把账号提前 1–5 个月养好，等 payload 需要时才启用**。⭐⭐⭐⭐⭐ 第三个发现是**「release 数量」这条 11-16 刚被证伪的判据，在本日被一个真项目正面推翻**：`kajisho5/ffmpeg-skill`（6,630⭐ · 598 forks · MIT）**有 100 个 release、100 个 tag、100 个互不相同的 commit sha，且 100 个 release 与 100 个 tag 一一对应** —— ⭐⭐⭐⭐⭐ **但本日报逐个查了这 100 个 tag 的 commit：release commit 本身只改元数据（`package.json` / `plugin.json` / `CHANGELOG.md` / `docs/contract.md`，8 个文件 +16/-9），而它的父 commit 才是真正的代码变更（12 个 tag 抽样中 12/12 的父 commit 触及源码，触及文件数 2–17 个）** —— ⭐⭐⭐⭐⭐ **即「release 多」既可能是伪造的（11-16 的 `steam-library-bridge`：1 个 commit → 4 个语义无关的版本号），也可能是真实的（本日：每个版本号背后都有一个真实的功能 commit）；两者的区别不在 release 数量，而在「tag → commit → 代码 diff」这条链是否闭合**。⭐⭐⭐⭐⭐ 第四个发现是**「Agent Skills」已经从「一个技能格式」收敛成「一个跨 harness 的可移植包格式」**：⭐⭐⭐⭐⭐ 本日报实测 17 个相关仓库中 **15 个带 `SKILL.md`**，⭐⭐⭐⭐⭐ **`google/elephant-goldfish-model` 同时发布 6 套 harness 专属清单（`.claude-plugin/` / `.codex-plugin/` / `.cursor-plugin/` / `.plugin/` / `.gemini/config.yaml` / Windsurf 适配器）、`mvanhorn/last30days-skill` 与 `kajisho5/ffmpeg-skill` 各 4 套、`addyosmani/agent-skills` 3 套** —— ⭐⭐⭐⭐⭐ **且 17 个仓库里只有 3 个同时公开 `npx skills add` 与 `/plugin marketplace add` 两条安装命令，说明「安装协议」尚未收敛，而「包内多 harness 清单」已经收敛 —— 二者并置即本日最重要的架构判断：Skills 的竞争战场已经从「技能内容」转移到「分发适配层」。**

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [OceanChandlerSewer/rob-run-cheat-private](projects/rob-run-cheat-private.md) | 236 stars | 观察型（反例样本） |
| [hubchrysalisspanner/Call-of-Duty--Modern-Warfare-4-cheat-client](projects/call-of-duty-modern-warfare-4-cheat-client.md) | 53 stars | 观察型（反例样本） |
| [kajisho5/ffmpeg-skill](projects/ffmpeg-skill.md) | 6,630 stars | 生产可用 |
| [google/elephant-goldfish-model](projects/elephant-goldfish-model.md) | 20,347 stars | 工具型 |
| [NVIDIA/SkillEvaluator](projects/skillevaluator.md) | 2,623 stars | 平台候选 |
| [mvanhorn/last30days-skill](projects/last30days-skill.md) | 68,087 stars | 生产可用 |
| [vercel-labs/agent-browser](projects/agent-browser.md) | 51,996 stars | 生产可用 |
| [ag-ui-protocol/ag-ui](projects/ag-ui.md) | 18,912 stars | 平台候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **⭐⭐⭐⭐⭐ 投放体的账号是「长期在编的产能」而不是当天现注册的：cheat client 族 9 个仓库（ROB RUN ×3 / PUBG / GTA V / Apex / Warzone / CoD MW4 / Marvel Rivals）共享同一套 README 模板（capsule-render 横幅 + readme-typing-svg 打字动效 + shields.io 徽章 + 一张功能表），其中 6 个统一指向同一条载荷域名 modbay.live；⭐⭐⭐⭐⭐ 每棵树只有 2 个 blob（LICENSE + README.md）、0 个代码文件、0 个 open issue；⭐⭐⭐⭐⭐ 实测账号分三批创建 —— 2026-08-10 一批 6 个（22:36:14Z–22:37:15Z，跨度 61 秒）、2026-09-21 一批 2 个、2026-06-15 一批 2 个；⭐⭐⭐⭐⭐ 其中 2026-08-10 那一批正是 11-15 日报记录的 2026-08-10T10:11:27Z 账号队列的同一注册窗口 —— 即投放方把账号提前 1–5 个月养好，需要时才启用** · 相关项目：OceanChandlerSewer/rob-run-cheat-private, SandstoneShoutMoon/ROB-RUN-cheat-client, DiamondCockatooFlow/Apex-Legends-cheat-client · 强度：96
2. **⭐⭐⭐⭐⭐ 「占位仓库」成为比「账号注册聚集度」更硬也更便宜的判据，且本日首次被做成对照实验：10/10 个投放账号各持有一个 README 恰好等于 `# <仓库名>`、10 字节、1 个 blob、0⭐ 的随机名占位仓库（trckulpa / szoyxrqs / fzohpjud / cwjhmbpo / ugqbrkec / hrolzfoa / nuxtdjnj / upzuukrt / rqpylldg / khcmkgzv）；⭐⭐⭐⭐⭐ 对照组的 16 个普通账号里只有 1 个（staryone/sanckut）命中同一签名 —— 6.25% vs 100%；⭐⭐⭐⭐⭐ 该指纹只需一次 users/{owner}/repos 请求即可判定，不受账号闲置时间影响、也不受仓库命名词根相似性影响** · 相关项目：OceanChandlerSewer/rob-run-cheat-private, hubchrysalisspanner/Call-of-Duty--Modern-Warfare-4-cheat-client, Brandtrocontrol/Marvel-Rivals-private-cheat · 强度：94
3. **⭐⭐⭐⭐⭐ 11-16 刚被证伪的「release 数量」判据，在本日被一个真项目正面推翻 —— ffmpeg-skill 有 100 个 release / 100 个 tag / 100 个互不相同的 commit sha，release 与 tag 一一对应；⭐⭐⭐⭐⭐ 但逐个查这 100 个 tag 的 commit 发现：release commit 本身只改元数据（package.json / plugin.json / CHANGELOG.md / docs/contract.md，8 文件 +16/-9），而它的父 commit 才是真正的代码变更（12 个 tag 抽样中 12/12 的父 commit 触及源码，触及文件数 2–17 个）；⭐⭐⭐⭐⭐ 结论：判据不在 release 数量，而在「tag → commit → 代码 diff」这条链是否闭合 —— 11-16 的 steam-library-bridge（1 commit → 4 个语义无关版本号）是链断开的反例** · 相关项目：kajisho5/ffmpeg-skill, atlas7283/steam-library-bridge · 强度：92
4. **⭐⭐⭐⭐⭐ 「Agent Skills」已从「一个技能格式」收敛成「一个跨 harness 的可移植包格式」：实测 17 个相关仓库中 15 个带 SKILL.md；⭐⭐⭐⭐⭐ google/elephant-goldfish-model 同时发布 6 套 harness 专属清单（.claude-plugin/ / .codex-plugin/ / .cursor-plugin/ / .plugin/ / .gemini/config.yaml / Windsurf 适配器）、mvanhorn/last30days-skill 与 kajisho5/ffmpeg-skill 各 4 套、addyosmani/agent-skills 3 套；⭐⭐⭐⭐⭐ 但 17 个仓库里只有 3 个同时公开 `npx skills add` 与 `/plugin marketplace add` 两条安装命令 —— 「包内多 harness 清单」已经收敛而「安装协议」尚未收敛，说明 Skills 的竞争战场正从技能内容转向分发适配层** · 相关项目：google/elephant-goldfish-model, mvanhorn/last30days-skill, kajisho5/ffmpeg-skill · 强度：91

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-11-17](daily/2026-11-17.md) | 9 | 5 |
| [2026-11-16](daily/2026-11-16.md) | 9 | 5 |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |
| [2026-11-12](daily/2026-11-12.md) | 6 | 4 |
| [2026-11-11](daily/2026-11-11.md) | 2 | 2 |

## 为什么做这个项目

GitHub Trending 展示注意力，不等于长期价值。本项目记录带日期的仓库事实，阅读代码、文档和 Release，对比跨日变化，区分事实与推断，并保留 Benchmark 未复现、许可证变化或异常 Star 等风险。

## 研究工作流

```mermaid
flowchart LR
  A["采集公开仓库信号"] --> B["阅读代码、文档、Release 与元数据"]
  B --> C["对比跨日变化"]
  C --> D["判断价值与风险"]
  D --> E["发布日报"]
  E --> F["更新项目档案与趋势账本"]
```

- `daily/`：带来源快照的每日研究报告。
- `projects/`：可持续修订的项目档案。
- `indexes/`：跨项目、跨日期的趋势记录。
- `docs/`：生成后的公开站点。
- `scripts/generate_readme.py`：从已提交数据生成双语 README 和活动图表。

## 证据边界

Star、Fork、Release、许可证、语言与时间戳属于采集时可观察的 GitHub 事实；产品质量、架构意义、市场方向和疑似刷星属于研究判断。作者自述在独立复现前会明确标注，后续修正保留在带日期的记录里。

## 生成与验证

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

定时研究任务运行在 AIUtil 私有自动化环境中，Token、私有运行记忆和运营状态不进入仓库。

## 安全

请勿提交访问令牌、私有仓库内容、用户级活动数据或未经脱敏的运营记忆。安全问题请通过 [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new) 私下报告。

## 开源协议

Apache License 2.0，详见 [NOTICE](NOTICE)。
