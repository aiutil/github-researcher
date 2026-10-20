# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-21.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-21

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 735 | 4 | 1815k+ |

**今日核心判断：** vercel-labs/fx0 把「durable agent」从「厂商私有 SDK 概念」推到「一行 createFxAgent() 即获得 agent loop + 流式 + tool calls + retries + durable sessions + Vercel Queues 崩溃后从最后一步继续」的可核验参考实现 + 用 Workflow World 存每一步 + 每 turn 记 funding 防止队列投递丢失计费归属 + 64 model steps 上限防 agent 死循环烧钱 + 十个 design.md 风格起步 + Agent 不明写终于是什么，由 Vercel 官方实验室出样本；opentrap/opentrap 把「拦截代理 + Web 安全扫描」从「Burp Suite 商业闭源 + ZAP 开源但界面不熟」拼成「Burp 风格工作流 + OWASP ZAP 成熟检测引擎 + 内置 Chromium 已走代理且信任其 CA 开箱 TLS 拦截 + Repeater/Intruder/Collaborator + AGPL-3.0 + Linux AppImage」的可运行样本；pengchujin/aerial-tv（524⭐ 36 fork，中文）把 Android TV 去广告从「海外机型 + 一句安装」推到「国产机型 + 五层接管模型（HOME 角色 → 无障碍桌面守护 → 通知监听被杀复活 → 开机自启 → ADB 常开）+ 逐机型笔记 docs/devices/ + 六款真机验证矩阵 + 不 root 不卸载 + 一条 curl 命令还原」；ELY-Open-Source/ElyOffice 把「本地办公套件」从「LibreOffice 巨型二进制 + 云端订阅」推到「Rust + GPUI + 逐个 fork 上游到 pinned commit 自己 build（LibreOffice 26.2.6.3 / MuPDF 1.28.5 / Git + LFS / tessdata）+ 文件留在本地文件夹、无账号无云 + MIT + macOS 已验证、Linux/Windows 配方存在但未在真机跑过」——今日主线是「**同一件事被多个团队并行严肃工程化**：durable agent 有官方样本、Web 安全工具有 AGPL 样本、电视桌面有国产机型样本、本地办公有上游自建样本；热度本身仍不等于价值，四个项目都处在 2 天内的早期信号区，需要后续 7–30 天数据才能判断是真实采用还是纯 star 波动

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [vercel-labs/fx0](projects/fx0.md) | 296 stars | 基础设施候选 |
| [opentrap/opentrap](projects/opentrap.md) | 177 stars | 工具型 |
| [pengchujin/aerial-tv](projects/aerial-tv.md) | 524 stars | 工具型 |
| [ELY-Open-Source/ElyOffice](projects/elyoffice.md) | 566 stars | 平台候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **vercel-labs/fx0 严肃工程化 durable design agent 公开参考实现：libfx 一行 createFxAgent() 即获得 agent loop + streaming + tool calls + retries + durable sessions + 每 turn funding 绑定防计费归属丢失 + 64 model steps 上限防烧钱 + Vercel Queues 崩溃唤醒续跑 + Workflow World 逐步落盘** · 相关项目：vercel-labs/fx0 · 强度：90
2. **opentrap/opentrap 严肃工程化 Burp Suite 免费开源替代：Burp 风格代理工作流 + OWASP ZAP 成熟检测引擎 + 内置 Chromium 已路由代理并信任其 CA 开箱 TLS 拦截 + Repeater/Intruder/Collaborator/Dashboard + AGPL-3.0 + Linux AppImage + Java 17+** · 相关项目：opentrap/opentrap · 强度：88
3. **pengchujin/aerial-tv 严肃工程化国产 Android TV 桌面：参照 tvOS + 无广告无推荐流 + 五层接管（HOME 角色/无障碍桌面守护/通知监听被杀复活/开机自启/ADB 常开）+ 逐机型笔记 + 六款真机验证 + 不 root 不卸载 + 一条 curl 还原** · 相关项目：pengchujin/aerial-tv · 强度：87
4. **ELY-Open-Source/ElyOffice 严肃工程化本地办公套件：Rust + GPUI + 自建上游（LibreOfficeKit 26.2.6.3 / MuPDF 1.28.5 / Git + LFS / tessdata 均 pinned commit）+ 无账号无云 + MIT + macOS 已验证而 Linux/Windows 配方未在真机跑过** · 相关项目：ELY-Open-Source/ElyOffice · 强度：84

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-21](daily/2026-10-21.md) | 4 | 4 |
| [2026-10-20](daily/2026-10-20.md) | 4 | 4 |
| [2026-10-19](daily/2026-10-19.md) | 4 | 4 |
| [2026-10-18](daily/2026-10-18.md) | 4 | 4 |
| [2026-10-17](daily/2026-10-17.md) | 4 | 4 |
| [2026-10-16](daily/2026-10-16.md) | 4 | 4 |
| [2026-10-15](daily/2026-10-15.md) | 4 | 4 |

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
