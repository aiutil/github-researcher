# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-10-22.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-10-22

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 739 | 4 | 86k+ |

**今日核心判断：** PHP 核心 RCE（php2shell / CVE-2026-109618 + CVE-2026-109619）在补丁发布后 24 小时内长出一整套开源响应生态：ikow/php2shell-poc 13 小时 859⭐ ⑂308（fork-star 35.9%，本批最高）给出 5 条 RCE 链 + Docker 靶场 + 5 套检测规则（Suricata/Snort · Sigma · ModSecurity · OpenResty Lua）；openai/php2shell-checker 310⭐ Apache-2.0 且主动声明「不独立验证安全修复、UNKNOWN 不等于已打补丁」；NCSC-NL/php2shell 以 EUPL-1.2 + TLP:CLEAR 发出国家级处置建议并明确「嵌入家电/网络设备/管理界面的 PHP 无法直接升级」；HOSTED-POWER/php_uploadprogress_guard 53⭐ 写出本日唯一非 PoC 项目——把缓解措施本身做成可安装 PHP 扩展，逐组件镜像官方补丁、自检到已打补丁就自动让位、12 个预编译二进制全部构建在 GLIBC_2.14 以下、Ansible 幂等部署在 cPanel EA4 / DirectAdmin / AWX 上实测 failed=0 二次 changed=0；NVIDIA/flare-local-inference 485⭐ ⑂47 用 AGENTS.md 明文列出「拒绝范围蔓延 / 拒绝架构违规 / 拒绝削弱保证」并自称「不是也不会是 vLLM 的替代」；dominikmartn/harp 527⭐ ⑂29 把 Warp 非官方 fork 的 tab bar 换成 agent 状态侧边栏 + 双 provider 限额环 + tmux 状态同步——今日主线是「**一个 PHP 补丁被开源社区拆成四层职责各自认领：谁解释漏洞、谁检测、谁国家层面处置、谁在等补丁期间先保住机器**；而 Flare 与 Harp 共享另一种信号——**把『我不做什么』写进代码仓库的制度文件，而不是只写在 README 卖点里**。热度本身仍不等于价值：php2shell 生态是 CVE 驱动的注意力洪峰而非技术突破，Flare 是明示的研究原型，Harp 是 4 个 release / 2 天的 fork，所有这些都需要后续 7–30 天数据才能判断是真实采用还是事件余温。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [ikow/php2shell-poc](projects/php2shell-poc.md) | 859 stars | 观察型 |
| [HOSTED-POWER/php_uploadprogress_guard](projects/php-uploadprogress-guard.md) | 53 stars | 生产可用 |
| [NVIDIA/flare-local-inference](projects/flare-local-inference.md) | 485 stars | 基础设施候选 |
| [dominikmartn/harp](projects/harp.md) | 527 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **php2shell（CVE-2026-109618 / CVE-2026-109619）补丁发布 24 小时内长出完整开源响应生态：ikow/php2shell-poc 5 条 RCE 链 + Docker 靶场 + 5 套检测规则（Suricata/Snort · Sigma · ModSecurity · OpenResty Lua）+ openai/php2shell-checker 版本判定 skill + NCSC-NL 国家级处置建议（EUPL-1.2 / TLP:CLEAR）** · 相关项目：ikow/php2shell-poc, openai/php2shell-checker, NCSC-NL/php2shell · 强度：92
2. **HOSTED-POWER/php_uploadprogress_guard 把『等官方补丁』这段空窗期做成可安装软件：PHP 扩展逐组件镜像官方补丁 + 拆掉 session upload-progress handler + 自检到已打补丁就自动让位 + 12 个预编译二进制全部 GLIBC_2.14 以下 + Ansible 幂等部署在 cPanel EA4 / DirectAdmin CustomBuild / AWX 实测 failed=0 且二次 changed=0** · 相关项目：HOSTED-POWER/php_uploadprogress_guard · 强度：89
3. **NVIDIA/flare-local-inference 严肃工程化研究原型的发布方式：AGENTS.md 明文列出『拒绝未批准的范围扩张 / 拒绝架构违规 / 拒绝削弱保证』三类驳回标准 + README 自称不是也不会是 vLLM 替代 + 编译期 PyTorch（Ignition）→ 运行期纯 Rust（Helios）的硬边界 + 发版前必须走 docs/design-review.md 的 staged-diff 复核** · 相关项目：NVIDIA/flare-local-inference · 强度：86
4. **dominikmartn/harp 严肃工程化多 agent 终端的状态管理：Warp 非官方 fork 把 tab bar 换成 agent 状态侧边栏（working / waiting for you / done / inactive + 未读标记 + 后台小圆点 + 置入暂存月亮）+ Claude/Codex 双限额环 + tmux 会话名/分组/顺序跨重启持久化与 @warp_adopt 1 收养 + 明示『Harp 不自建任何服务器 / 通过 Harp 登录未测试』** · 相关项目：dominikmartn/harp · 强度：84

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-10-22](daily/2026-10-22.md) | 4 | 4 |
| [2026-10-21](daily/2026-10-21.md) | 4 | 4 |
| [2026-10-20](daily/2026-10-20.md) | 4 | 4 |
| [2026-10-19](daily/2026-10-19.md) | 4 | 4 |
| [2026-10-18](daily/2026-10-18.md) | 4 | 4 |
| [2026-10-17](daily/2026-10-17.md) | 4 | 4 |
| [2026-10-16](daily/2026-10-16.md) | 4 | 4 |

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
