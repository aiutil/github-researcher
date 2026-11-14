#!/usr/bin/env python3
"""Insert 架构图（MMD） into the 4 new 2026-11-09 profiles."""

import io
import os

BASE = "/home/lohasle/aiutil-github-researcher/projects"

BANNER = (
    "## 架构图（MMD）\n\n"
    "> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。\n\n"
    "```mermaid\n"
)
TAIL = "```\n\n"

DIAGRAMS = {}

DIAGRAMS["lag-doctor"] = """flowchart LR
  G[游戏进程 CS2 VALORANT 等] --> CONN[读取游戏自身连接表<br/>确定真实服务器 IP]
  CONN --> FALLBACK[无游戏运行时<br/>退回 1.1.1.1]
  CONN --> TRACE[逐跳探测<br/>src/icmp.rs 与 src/trace.rs]
  TRACE --> STATS[每跳 丢包与抖动统计<br/>src/stats.rs]
  STATS --> PERSIST{丢包与抖动<br/>是否持续到服务器}
  PERSIST -->|是| BLAME[归因 verdict<br/>src/diagnosis.rs]
  PERSIST -->|否 判为 ICMP 限速<br/>不归咎该跳| IGNORE[忽略该跳<br/>经典 MTR 误读规则已内置]
  BLAME --> VERDICT[your Wi-Fi / router / ISP / game server<br/>加置信度与各段延迟贡献]
  STATS --> SPIKE[延迟尖峰日志<br/>路由器同秒尖峰则判为本地]
  MON[实时监控 src/monitor.rs] --> SPIKE
  GRAPH[缓冲膨胀测试<br/>空闲与负载延迟差] --> GRADE[bufferbloat 评级 A+ 至 F<br/>并区分 Wi-Fi 与以太网]
  VERDICT --> REPORT[会话报告<br/>三行可直接粘进客服工单]
  SPIKE --> REPORT
  GRADE --> REPORT
  VERDICT --> HUD[游戏内叠加层 HUD]
  TRACE --> GRAPH
  REPORT --> USER[玩家 结论与处置建议]
"""

DIAGRAMS["drift-doctor"] = """flowchart LR
  PAD[手柄 Xbox DualSense Switch Pro 8BitDo] --> XI[原始 XInput 采集<br/>src/input.rs 不施加死区]
  XI --> REST[10 秒静置窗口<br/>用户需真的放下手柄]
  REST --> CLOUD[每根摇杆的散点云<br/>src/widgets.rs]
  CLOUD --> OFF[中心偏移量]
  CLOUD --> NOISE[99 分位噪声半径]
  OFF --> ANGLE[偏移方向角]
  OFF --> SCORE[Drift Score 0 至 100<br/>src/stats.rs]
  NOISE --> SCORE
  SCORE --> BAND[严重度分档<br/>No drift Trace Mild Moderate Severe]
  BAND --> DIAG[诊断句<br/>Mild drift left stick 4.1% toward 37 度]
  NOISE --> DEADZONE[推荐最小内死区<br/>每根摇杆独立 可调安全余量]
  DEADZONE --> CORRECT[漂移修正 src/correction.rs<br/>实现方式待核验]
  CORRECT --> HIST[修正历史 src/store.rs]
  HIST --> VERIFY[修正前后对比复核]
  DIAG --> USER[用户 可直接转述给客服或维修]
  DEADZONE --> USER
"""

DIAGRAMS["research-loop-skills"] = """flowchart TB
  Q[研究问题] --> FRAME[research-frame<br/>界定问题与范围]
  FRAME --> EV[research-evidence<br/>映射证据与来源]
  EV --> HYP[research-hypothesize<br/>选一个能区分假设的检验]
  HYP --> EXEC[research-execute<br/>在预算内执行]
  EXEC --> VER[research-verify<br/>核验主张]
  VER -->|证据改变了问题| FRAME
  VER -->|还值得再做一次检查| HYP
  VER -->|证据足够 或 触发停止条件| SYN[research-synthesize<br/>收口并留下下一步]
  SYN --> OUT[来源 主张 检查 局限 下一步]
  OUT --> CHK[scripts/research_run.py<br/>零依赖校验器 11 KB]
  OUT --> TEST[tests/test_research_run.py<br/>校验器自带测试]
  CHK --> AUDIT[可审计的留痕<br/>格式正确 不等于 实质正确]
  AGENT[宿主 Agent<br/>带来推理 检索与工具] -.提供执行能力.-> FRAME
  STOP[停止规则<br/>最多 3 轮迭代<br/>且下一步不太可能改变答案就提前停] -.约束.-> VER
  NEG[负面或不确定的结果<br/>是合法的结束方式] -.允许.-> SYN
  NOTE[本仓库只提供方法<br/>不调度 不检索 不计时 不联网] -.边界.-> OUT
"""

DIAGRAMS["livewall"] = """flowchart TB
  subgraph Declared[README 宣称的架构 分层与实现均不可核验]
    V[用户自有视频或内置素材库] --> L1[壁纸视频层<br/>渲染在桌面图标之后<br/>任务栏与窗口保持在上]
    L1 --> L2[组件层<br/>时钟 天气 音乐<br/>独立绘制于壁纸之上]
    L2 --> L3[可见性门控<br/>桌面被遮挡时停止播放以省资源]
    DL[下载安装程序<br/>livewall.lol 或 GitHub release] --> L1
  end
  subgraph Repo[仓库实际内容 仅 2 个 blob]
    ZIP[LiveWallLauncher.zip<br/>21,859,851 字节<br/>闭源 二进制 未解压核验]
    RM[README.md 3,173 字节<br/>无索取 star 的话<br/>20 个 topics 多与内容无关]
    ZIP --> RM
  end
  ZIP -.用户被引导安装.-> DL
  RM -.声称.-> Declared
  subgraph Signals[可核验的注意力信号]
    S1[subscribers_count 420<br/>高于 stargazers_count 311]
    S2[30 个 fork 全部落在<br/>3 分 51 秒内<br/>间隔中位数 5 秒]
    S3[29 个 fork 账号<br/>public_repos 恰好 3<br/>followers 恰好 0]
  end
  S1 -.污染.-> Repo
  S2 -.污染.-> Repo
  S3 -.污染.-> Repo
  AUTH[作者另外 28 个公开仓库<br/>本日报未逐个核验] -.待观察.-> S1
"""

ORDER = ["lag-doctor", "drift-doctor", "research-loop-skills", "livewall"]


def main():
    for slug in ORDER:
        path = os.path.join(BASE, f"{slug}.md")
        with io.open(path, encoding="utf-8") as f:
            text = f.read()
        if "```mermaid" in text:
            print(f"SKIP {slug}: already has mermaid")
            continue
        anchor = "\n## 定位判断\n"
        if anchor not in text:
            raise SystemExit(f"{slug}: anchor not found")
        block = "\n" + BANNER + DIAGRAMS[slug] + TAIL
        text = text.replace(anchor, block + anchor, 1)
        with io.open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"OK   {slug}")


if __name__ == "__main__":
    main()
