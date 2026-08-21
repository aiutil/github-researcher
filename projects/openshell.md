---
title: "NVIDIA OpenShell"
slug: "openshell"
date_added: "2026-06-03"
category: "基础设施候选"
emoji: "🔒"
stars: "6.6K stars"
stars_delta: "+142/day, +1.4K/week, Rust 实现, Alpha 阶段"
language: "Rust"
score: 91
tags: ["agent-sandbox", "security", "nvidia", "rust", "policy-engine", "gpu-passthrough", "credential-isolation"]
url: "https://github.com/NVIDIA/OpenShell"
last_seen_date: "2026-06-03"
---

# NVIDIA OpenShell

## 一句话定位
NVIDIA 出品的 Agent 安全运行时沙箱——Rust 实现，四层策略防御（文件系统/网络/进程/推理），凭证隔离，GPU 直通，覆盖 OWASP Agentic Top 10。

## 它解决的问题
AI Agent 在执行任务时需要访问文件系统、网络、API 密钥等敏感资源。当前大多数 Agent 直接在宿主机运行，存在数据泄露、凭证暴露、未授权操作等安全风险。OpenShell 为每个 Agent 提供隔离沙箱，通过声明式 YAML 策略控制所有资源访问。

## 为什么值得关注（2026-06-03）
- **NVIDIA 官方出品**，背书强度高
- **Rust 实现**，性能和安全双重保障
- **四层防御体系**是目前最完整的 Agent 沙箱方案：文件系统（锁定）+ 网络（热重载）+ 进程（锁定）+ 推理路由（热重载）
- **GPU 直通**支持本地推理，这是其他沙箱方案没有的
- **凭证隔离设计**正确：凭证不进沙箱文件系统，环境变量注入
- 已有 Helm chart，K8s 部署路线正在开发

## 热度来源判断
- GitHub Trending Rust 排名前列，+142 stars/day
- NVIDIA 品牌效应 + Agent 安全刚需双重驱动
- Alpha 阶段已有 6.6K stars，说明市场期待度高

## 关键技术亮点亮点

### 策略引擎
- 声明式 YAML 策略，静态层（文件系统/进程）锁定，动态层（网络/推理）热重载
- L7 级别 HTTP 方法 + 路径粒度控制

### 凭证管理
- 自动发现 Claude/Codex/Copilot/OpenCode 凭证
- Provider 抽象，运行时注入，不落盘

### GPU 直通
- CDI 优先，回退 NVIDIA Container Toolkit
- 实验性但路线明确

### Agent 支持
- Claude Code / Codex / Copilot / OpenCode / OpenClaw / Ollama / Pi
- 社区可贡献新 Agent 镜像

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | OpenShell 是 Agent 与外部资源（文件系统、网络、进程、LLM 后端）之间的隔离编排层，NVIDIA 官方 + Rust 实现，目前仍为 Alpha 阶段。 | 仅依据档案中的项目描述、标签、热度数据；具体组件实现、协议、部署形态未在档案中给出源码级证据。 |
| 主路径 | Agent 启动 → Gateway/Sandbox 受理 → 四层策略引擎静态层（FS/进程）锁定 + 动态层（网络/推理）热重载放行 → 凭证通过 Provider 抽象运行时注入 → 可选 GPU 直通（CDI 优先，回退 NVIDIA Container Toolkit）执行推理。 | 路径描述来自档案"策略引擎/凭证管理/GPU 直通/Agent 支持"章节；未含具体协议、API 形态或会话持久化细节。 |
| 关键权衡 | 隔离强度（GPU 直通、四层策略、凭证不落盘）与灵活性（动态层热重载、多 Agent 镜像生态）之间的取舍；同时受 ELv2 引擎许可与 Alpha 阶段多租户缺位的商业化约束。 | 权衡判断基于档案"风险/局限"与"关键技术亮点"段落；性能数据、生产案例、可观测性细节档案未提供。 |
| 最小 PoC | 单租户本地部署，固定一个 Agent（Claude Code 或 Codex）+ 一组受限文件系统/网络 YAML 策略 + 仅启用静态层 + 走本地 Ollama 路径（关闭 GPU 直通），以验证沙箱拦截、凭证注入、热重载三个最小能力。 | PoC 设计仅引用档案中明示的 Agent 列表、策略分层、GPU 模式开关与 Docker/Podman/MicroVM 依赖；具体编排、监控、退出路径须自行核验。 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    Agent["AI Agent<br/>Claude Code / Codex / Copilot /<br/>OpenCode / OpenClaw / Ollama / Pi<br/>（待核验：实际接入清单）"]
    Gateway["Gateway<br/>控制面 API / Auth 边界<br/>（待核验：协议与鉴权细节）"]
    Sandbox["Sandbox<br/>容器隔离（Docker / Podman / MicroVM）<br/>Alpha 阶段 / 单租户"]
    Policy["Policy Engine<br/>声明式 YAML<br/>静态层：FS 锁定 + 进程锁定<br/>动态层：网络热重载 + 推理热重载"]
    Cred["Credential Provider<br/>运行时注入，不落盘<br/>覆盖 Claude/Codex/Copilot/OpenCode 凭证<br/>（待核验：Provider 抽象接口）"]
    Ext["外部资源边界<br/>L7 HTTP 方法+路径粒度 / 拒绝拦截"]
    GPU["GPU 直通<br/>CDI 优先 → 回退 NVIDIA Container Toolkit<br/>实验性 / NVIDIA 硬件绑定"]
    Risk["风险与状态边界<br/>ELv2 引擎许可（商业受限）<br/>SDK Apache 2.0<br/>Alpha / 多租户缺失 / K8s Helm 待开发"]

    Agent --> Gateway
    Gateway --> Sandbox
    Sandbox --> Policy
    Policy -->|允许 + 凭证剥离| Ext
    Policy -->|拒绝| Ext
    Cred --> Sandbox
    Sandbox --> GPU
    Sandbox --> Risk
    Policy --> Risk
```

**架构师启发：**
1. Agent 沙箱应该是 Agent 运行时的标准组件，不是可选安全加固
2. 策略热重载设计使 Agent 运行时可以动态扩展能力，无需重启
3. 推理路由（Privacy Router）是独特设计——Agent 的 API 调用经过审计后才转发
4. 与 Microsoft AGT 互补：AGT 定义策略，OpenShell 执行策略

## 定位判断
**基础设施候选。** 如果 Agent 成为标准开发模式，安全沙箱运行时就是必须的基础设施层。NVIDIA 的入场为这个品类提供了强有力的验证。

## 风险/局限/泡沫点
1. **Elastic License 2.0（引擎部分）**——商业使用受限，SDK 是 Apache 2.0
2. **Alpha 阶段**——单租户模式，企业多租户部署还需等待
3. **依赖 Docker/Podman/MicroVM**——对已有容器环境的团队友好，但增加了部署复杂度
4. **NVIDIA 生态绑定**——GPU 直通依赖 NVIDIA 硬件和驱动
5. **竞品风险**——Docker/Mozilla 等也可能推出类似方案

## 与同类项目的关系
- **Microsoft AGT**：互补关系，AGT 做策略定义，OpenShell 做沙箱执行
- **Docker/Podman**：底层运行时，OpenShell 在其上构建 Agent 感知层
- **Anthropic Cybersecurity Skills**：安全知识层，与沙箱运行时互补

## 是否值得持续跟踪
**是。** Agent 安全运行时是明确的中期趋势，NVIDIA 出品增加了成为标准的可能性。

## 后续观察点
1. 引擎 License 是否会调整（ELv2 → Apache 2.0？）
2. K8s 多租户路线的推进速度
3. 社区贡献的 Agent 镜像生态
4. 与主流 Agent Harness（ECC/Claude Code/Codex）的集成深度
5. GPU 直通的稳定性和生产就绪度

---

*档案创建于 2026-06-03 · 数据截止 2026-06-03 06:00 CST*
