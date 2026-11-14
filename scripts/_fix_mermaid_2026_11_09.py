#!/usr/bin/env python3
"""Insert the missing 架构图（MMD） sections into the 7 profiles flagged by
validate.py on 2026-11-09.

Insertion point: immediately before the `## 定位判断` heading, matching the
order used by headroom.md / brotli-checker.md (架构师速览 → 架构启发 → 架构图).
"""

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

DIAGRAMS["ghostclick-mouse-double-click-fix"] = """flowchart LR
  M[物理鼠标开关抖动<br/>switch bounce] --> C[系统级输入采集<br/>hook 机制 待核验]
  C --> A[时序分析<br/>两次脉冲间隔测量]
  A --> L[阈值学习<br/>从用户真实双击采样]
  A --> S[条带图渲染<br/>每键一支笔 毫秒级标注]
  L --> F[系统级过滤<br/>抑制第二次脉冲 注入方式 待核验]
  F --> T[托盘常驻 UI]
  S --> E[RMA 证据导出<br/>可提交厂商的凭据材料]
  S --> V[复查入口<br/>修复前后逐笔对照]
  A --> R[风险边界<br/>可能误吞合法双击<br/>README 未说明]
  F --> X[权限面<br/>全局输入拦截<br/>可能触发杀软误报]
"""

DIAGRAMS["minecraft-afk-bot"] = """flowchart TB
  subgraph Claim[README 宣称的系统]
    C1[Node.js Mineflayer 客户端] --> C2[Minecraft 服务器]
    C3[Express Socket.io Web 面板] --> C1
    C2 --> C4[模拟轻微移动与自动重连]
  end
  subgraph Actual[仓库实际内容]
    A1[language 字段为 Python] --> A2[utils.py<br/>build 函数返回 0 2 4 递增占位数据]
    A3[main.py 从 utils import build] --> A2
    A4[无 JS TS 文件<br/>无 Mineflayer Express Socket.io]
  end
  subgraph Evidence[可核验证据面]
    E1[README 两处索取 star<br/>⭐ Star the repo if it helped you]
    E2[fork 间隔中位数 4.0 秒<br/>全部落在 9.9 分钟内]
    E3[helpers.py md5 8470fd5b<br/>与 11-06 农场簇逐字节相同]
    E4[.gitignore md5 e18f025c<br/>跨日复用]
  end
  Claim -.无对应实现.-> Actual
  E1 --> S[subscribers_count 35<br/>本日候选中最高]
  E2 --> S2[fork 数 260<br/>fork/star 61.2%]
  E3 --> S3[模板血缘链<br/>11-06 至 11-08 跨日复用]
  Actual --> X[观察型反例样本<br/>收录目的是保留可证伪样本]
"""

DIAGRAMS["phoneuse"] = """flowchart LR
  P[iPhone 17 Pro<br/>手机侧零安装零越狱] -->|AirPlay 视频| U[UxPlay 接收端]
  U --> G[GStreamer GTK4<br/>镜像窗口]
  G --> H[Hyprland IPC<br/>窗口几何与光标位置]
  H --> M[mirror_input<br/>坐标映射到触摸]
  M --> D[HID daemon<br/>root systemd 常驻]
  D -->|Bluetooth HID| P
  G --> V[截图 OCR grounding]
  V --> A[Agent 决策]
  A --> C[CLI 与 MCP Server<br/>phoneuse / phoneuse-mcp]
  C --> D
  D --> R[安装副作用边界<br/>关闭 bluetoothd 输入与 hostname 插件<br/>本机不再接受蓝牙键鼠]
  M -.前置条件.-> T[手机侧 AssistiveTouch 开<br/>Dwell Control 关]
"""

DIAGRAMS["satmux"] = """flowchart LR
  App[笔记本应用<br/>git gh 等] --> SOCK[本地 SOCKS5 与 HTTP CONNECT<br/>0-RTT 开流]
  SOCK --> POOL[12 条常驻载波池<br/>:8444 按最近字节负载调度]
  POOL --> SAT[卫星链路<br/>客舱 PEP 与 cwnd 崩塌]
  SAT --> GV[地面站 VM<br/>阿姆斯特丹 等]
  GV --> GROUND[地面侧服务<br/>DNS 与 TLS 1.3 终止与 zlib 压缩]
  GROUND --> O[Origin<br/>光纤 2 至 5 ms]
  POOL --> HUD[HUD 监控面板]
  SOCK --> US[gh 的 Unix socket 桥<br/>/tmp/satmux-gh-tls.sock 权限 0600]
  US --> GROUND
  SAT --> LIM[物理下界<br/>单跳 RTT 约 580 至 650 ms<br/>不可消除]
"""

DIAGRAMS["solo-to-team-skills"] = """flowchart TB
  H[宿主 Agent<br/>Claude Code Codex Cursor 等八家] --> S1[派活收活技能<br/>写待收登记行]
  S1 --> CK[到点查<br/>触发方式依赖宿主]
  CK --> S2[记已接单 与 已收到成果]
  S2 --> EV[evidence-before-done 技能<br/>没有对得上当前版本的有效证据就不说做好了]
  EV --> J{证据是否足够}
  J -->|够| OK[记已验收并放行]
  J -->|不够| RT[退回或只补核受影响部分]
  RT --> S2
  OK --> CASE[ops-case-notes<br/>踩过的坑写入案例库]
  CASE --> S1
  EV -.豁免条款.-> EX[普通进度不触发全套重验]
  H --> DA[危险动作分栏<br/>须本人亲自完成的步骤只写请本人来]
  DANGER[不可逆动作] --> DA
  HOOK[插件清单 hooks 为空<br/>不带定时与叫醒] -.职责上移.-> H
"""

DIAGRAMS["steam-idler"] = """flowchart TB
  subgraph Claim[README 宣称的能力]
    C1[无需 Steam 客户端<br/>headless 直连 Steam 服务器] --> C2[模拟游戏活动用于挂机]
    C2 --> C3[退款资格与安全免责声明]
  end
  subgraph Actual[仓库实际内容]
    A1[4 个 commit 19 秒内完成<br/>Add config.py Add helpers.py Add README.md]
    A2[helpers.py 97 字节<br/>仅换 docstring 主语与常量]
    A3[config.py 与 roblox-studio-mcp 结构一致<br/>仅 docstring 与两个常量不同]
    A4[无任何 Steam 协议或游戏活动模拟代码]
  end
  subgraph Evidence[可核验证据面]
    E1[README 两处索取 star<br/>⭐ Star the repo if it helped you]
    E2[fork 间隔中位数 5.0 秒<br/>99 个间隔中 98 个不超过 10 秒]
    E3[helpers.py md5 8470fd5b<br/>与 crypto-portfolio-tracker 等逐字节相同]
    E4[.gitignore md5 e18f025c<br/>与 11-06 四家完全相同]
  end
  Claim -.无对应实现.-> Actual
  E1 --> S[subscribers_count 25]
  E2 --> S2[fork 数 313<br/>fork/star 73.6% 本日最高区间]
  E3 --> S3[模板血缘链<br/>可参数化批量生成]
  Actual --> X[观察型反例样本<br/>与同模板 Minecraft-AFK-Bot 构成跨日复用证据]
"""

DIAGRAMS["zero-breach-toolkit"] = """flowchart TB
  U[普通用户 双击 App] --> LANG[首次运行选择语言<br/>27 种语言与 GUI]
  LANG --> K[检测内核<br/>继承上游 interplains/zero-breach<br/>scan/adint_scan]
  K --> K1[7 个本地只读证据通道<br/>浏览器历史 cookies 缓存 连接记录 文件指纹 自启动 已知恶意路径 DNS 解析器缓存]
  K --> K2[可选 pinned YARA-X]
  K1 --> REP[报告<br/>找到什么 加 证据强度]
  REP --> LIM[哪些不能检查<br/>明确列出不可覆盖范围]
  REP --> M[指标与规则层<br/>build/emit 生成六种格式指标集]
  M --> GAP[iocs/VALIDATOR-GAP.md<br/>哪些指标条目未被验证过]
  M --> FMT[adblock dnsmasq hosts MISP STIX]
  REP --> UPD[--update 受控联网<br/>仅此一处联网 来源固定允许清单]
  UPD -.受限出口.-> NET[GitHub release 查询]
  K -.本地只读 不联网.-> BOUND[隐私边界<br/>扫描期零网络请求]
"""

ORDER = [
    "ghostclick-mouse-double-click-fix",
    "minecraft-afk-bot",
    "phoneuse",
    "satmux",
    "solo-to-team-skills",
    "steam-idler",
    "zero-breach-toolkit",
]


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
            raise SystemExit(f"{slug}: anchor '## 定位判断' not found")
        block = "\n" + BANNER + DIAGRAMS[slug] + TAIL
        text = text.replace(anchor, block + anchor, 1)
        with io.open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"OK   {slug}: inserted 架构图（MMD）")


if __name__ == "__main__":
    main()
