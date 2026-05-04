# CodexFlow Architecture Principles

中文 / English

## 1. Purpose

### 中文

这份文档定义 CodexFlow 在架构上的长期立场，尤其是：

- `CLI` 与 `MCP` 的角色
- 为什么 CodexFlow 要保持轻量、外置、低耦合
- 哪些方向应该吸收
- 哪些方向应该明确拒绝

它不是功能清单，而是做取舍时的判断基线。

### English

This document defines CodexFlow's long-term architectural stance, especially around:

- the roles of `CLI` and `MCP`
- why CodexFlow should remain lightweight, external, and low-coupling
- which directions should be absorbed
- which directions should be rejected

It is not a feature checklist. It is the baseline for architectural tradeoffs.

## 2. Core Position

### 中文

CodexFlow 的核心不是“把一切做进 agent 平台”，而是：

- 让 Codex 更容易接入项目
- 让上下文和状态落在磁盘上
- 让能力以轻量工具和 skill 的形式存在
- 让 agent 更像路由者和判断者，而不是吞掉所有工程职责的大管家

### English

CodexFlow is not trying to become an all-in-one agent platform. Its core is to:

- make Codex easier to attach to projects
- keep context and state on disk
- express capability through lightweight tools and skills
- keep the agent closer to a router and judge than a giant all-owning workflow manager

## 3. CLI Before MCP

### 中文

CodexFlow 优先选择 `CLI` 作为能力本体。

原因：

- `CLI` 更容易调试
- `CLI` 更容易接入 shell、Python、CI 和人工排查流程
- `CLI` 更容易被审计和复现
- `CLI` 不要求系统先依赖某个特定集成层

我们的默认判断是：

- 先把能力做成稳定 CLI
- 再视需要决定是否暴露为 `MCP`

换句话说：

- `CLI` 是能力本体
- `MCP` 是可选暴露层

### English

CodexFlow prefers `CLI` as the primary form of capability.

Reasons:

- `CLI` is easier to debug
- `CLI` fits naturally into shell, Python, CI, and human troubleshooting
- `CLI` is easier to audit and reproduce
- `CLI` does not require the system to depend on a specific integration layer first

The default rule is:

- build the capability as a stable CLI first
- expose it through `MCP` only if that later proves useful

In short:

- `CLI` is the capability body
- `MCP` is an optional exposure layer

## 4. What MCP Means Here

### 中文

CodexFlow 不反对 `MCP`，但反对把 `MCP` 放到架构中心。

`MCP` 在这里更适合做：

- 外围适配层
- 多客户端访问层
- 能力暴露层

而不适合做：

- 核心状态源
- 核心流程控制面
- 项目初始化的唯一入口

如果未来引入 `MCP`，它应该包裹现有 CLI / 文件化状态，而不是反过来让 CLI 变成 MCP 的从属物。

### English

CodexFlow does not reject `MCP`, but it does reject putting `MCP` at the architectural center.

Here, `MCP` is a better fit for:

- an outer adapter layer
- multi-client access
- capability exposure

It is a poor fit for:

- the core source of truth
- the core workflow control plane
- the only entrypoint for project bootstrap

If `MCP` is added later, it should wrap existing CLI tools and file-based state, not force those layers to become subordinate to MCP.

## 5. External Brain, Not Embedded Platform

### 中文

CodexFlow 的定位是外置大脑，而不是内嵌平台。

这意味着：

- 中央脑仓库保持小而清晰
- 新项目通过薄本地入口接入中央脑
- 项目本身仍保有自己的代码、结构和节奏
- CodexFlow 只负责启动、路由、状态约定、skill 选择、评测和少量辅助工具

不应该：

- 吞掉项目内部架构
- 变成 IDE 专属插件系统
- 强迫所有项目接受同一套重型基础设施

### English

CodexFlow is positioned as an external brain, not an embedded platform.

That means:

- the central brain repo stays small and legible
- new projects attach through a thin local entrypoint
- each project still owns its own code, structure, and pace
- CodexFlow focuses on bootstrap, routing, state conventions, skill selection, evaluation, and a small set of helper tools

It should not:

- swallow the project's own architecture
- become an IDE-exclusive plugin system
- force every project into the same heavy infrastructure

## 6. File-Based State Over Heavy Platforms

### 中文

CodexFlow 优先使用文件化状态，而不是重平台化状态系统。

当前偏好的状态模型是：

- Markdown 快照作为人类入口
- JSONL 事件流作为追加式事实历史
- 脚本负责初始化、追加、恢复和少量校验

这比一开始就引入数据库、控制台或复杂服务更符合项目目标。

### English

CodexFlow prefers file-based state over heavy platform-style state systems.

The preferred state model is:

- Markdown snapshots as the human entrypoint
- JSONL event streams as append-only factual history
- scripts for bootstrap, append, resume, and light validation

This fits the project better than introducing databases, dashboards, or complex services too early.

## 7. Layered Context, Not Read-Everything

### 中文

CodexFlow 反对“让新对话读取整个脑仓库”。

我们偏好的方式是：

- 一个中央入口
- 一个本地入口
- 按阶段选择 skill
- 按 active layers 读取 taste
- 只在必要时读取 event log

目标是降低：

- 上下文膨胀
- 规则冲突
- 噪音判断
- 模型负担

### English

CodexFlow rejects the pattern of telling a fresh session to read the entire brain repository.

The preferred model is:

- one central entrypoint
- one local entrypoint
- phase-based skill selection
- active-layer taste loading
- event-log reads only when needed

The goal is to reduce:

- context bloat
- rule conflicts
- noisy judgment
- model load

## 8. Progressive Enhancement

### 中文

CodexFlow 应该按层增强，而不是一步做成重系统。

合理顺序是：

1. 薄本地 `AGENTS.md`
2. `codexflow-init`
3. roadmap + autonomy budget
4. event layer + layered taste
5. 可选 adapter，例如 IDE 集成或 MCP 暴露层

高阶能力应该建立在稳定基础上，而不是靠一次性大集成。

### English

CodexFlow should grow by progressive enhancement, not by becoming heavy all at once.

A sensible order is:

1. thin local `AGENTS.md`
2. `codexflow-init`
3. roadmap + autonomy budget
4. event layer + layered taste
5. optional adapters, such as IDE integration or MCP exposure

Higher-level capabilities should sit on top of stable fundamentals, not on a giant one-shot integration.

## 9. Explicit Rejections

### 中文

CodexFlow 当前明确不把这些方向当作默认核心：

- 数据库优先的状态中心
- 重型插件市场
- 深度绑定单一 IDE
- 通过模型输出标签正则驱动主状态机
- “Everything agent platform” 式的大而全控制面

这些方向不是永远不允许，而是不应该成为默认架构中心。

### English

CodexFlow explicitly does not treat these as default core architecture:

- database-first state centers
- heavyweight plugin marketplaces
- deep binding to a single IDE
- driving the main state machine through regex over model output tags
- an "everything agent platform" style control plane

These are not banned forever, but they should not become the default center of the system.

## 10. Decision Rule

### 中文

当未来遇到架构分歧时，优先问这 5 个问题：

1. 这个方案会不会让系统更重？
2. 这个方案能不能先用 CLI 和文件状态实现？
3. 这个方案是不是把控制权从工程执行层移回了集成层？
4. 这个方案会不会让新项目更难接入？
5. 这个方案是否真的提高了判断质量，而不只是增加了机制数量？

如果前 4 个问题大多是坏答案，这个方案大概率不适合 CodexFlow。

### English

When future architecture disagreements appear, ask these five questions first:

1. Does this make the system heavier?
2. Can this be done with CLI tools and file-based state first?
3. Does this move control away from the execution layer back into the integration layer?
4. Does this make new projects harder to attach?
5. Does this truly improve judgment quality, rather than just increasing mechanism count?

If the first four answers are mostly bad, the proposal is probably not a good fit for CodexFlow.
