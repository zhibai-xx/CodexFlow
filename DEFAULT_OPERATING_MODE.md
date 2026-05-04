# CodexFlow Default Operating Mode

中文 / English

## 1. Purpose

### 中文

这份文档定义 CodexFlow 在没有额外项目特例时的默认工作方式。

它回答的是：

- 新对话默认先读什么
- 默认继续还是暂停
- 默认什么时候问用户
- 默认什么时候读取更多上下文

它不是 skill 手册，也不是架构讨论文档。  
它是 CodexFlow 的默认执行宪法。

### English

This document defines CodexFlow's default working behavior when no stronger project-specific override exists.

It answers:

- what a fresh session should read first
- whether the default is to continue or pause
- when the user should be interrupted
- when more context should be loaded

It is not a skill manual or an architecture essay.  
It is the default execution constitution of CodexFlow.

## 2. Default Read Order

### 中文

默认只按这个顺序读取：

1. 本地 `AGENTS.md`
2. `.codex-agent/PROJECT.md`
3. `.codex-agent/TASTE.md`
4. `TASTE.md` 标记为 active 的 taste layers
5. `.codex-agent/ROADMAP.md`
6. 当前阶段需要的一个 skill
7. 当前活跃的 inception packet 或 task directory

默认不要：

- 读取整个 CodexFlow 仓库
- 读取所有 skills
- 读取所有历史 task
- 读取全部 event logs

### English

By default, read only in this order:

1. local `AGENTS.md`
2. `.codex-agent/PROJECT.md`
3. `.codex-agent/TASTE.md`
4. the taste layers marked active by `TASTE.md`
5. `.codex-agent/ROADMAP.md`
6. the one skill needed for the current phase
7. the active inception packet or task directory

By default, do not:

- read the entire CodexFlow repository
- read every skill
- read all historical tasks
- read all event logs

## 3. Default Execution Behavior

### 中文

默认行为是“继续推进”，不是“每完成一步就汇报”。

标准节奏：

1. 收集足够上下文
2. 形成短计划
3. 执行一个有意义的批次
4. 做最窄验证
5. 更新状态
6. 继续下一个批次

默认不要：

- 跑一条命令就停
- 改一个文件就停
- 因为完成一个小切片就把控制权交还用户

### English

The default behavior is to continue, not to report after every micro-step.

Standard cadence:

1. gather enough context
2. form a short plan
3. execute one meaningful batch
4. run the narrowest useful validation
5. update state
6. continue into the next batch

By default, do not:

- stop after one command
- stop after one file edit
- hand control back just because one clean slice finished

## 4. Default Stop Rule

### 中文

默认只有下面这些情况才应该暂停并找用户：

- 需要审批
- 需要密钥、凭证、付费访问或额外权限
- 涉及破坏性操作
- 出现用户必须拍板的产品或设计选择
- 用户已有改动与当前方向冲突
- `ROADMAP.md` 已经不足以安全决定下一步
- autonomy budget 已耗尽

除了这些情况，默认应继续。

### English

By default, the user should only be interrupted when:

- approval is required
- secrets, credentials, paid access, or extra permissions are needed
- a destructive action is involved
- a user-owned product or design choice must be made
- existing user changes conflict with the current direction
- `ROADMAP.md` is no longer enough to choose the next step safely
- the autonomy budget is exhausted

Outside these cases, the default is to continue.

## 5. Default Context Discipline

### 中文

默认上下文策略是“按需读取”。

这意味着：

- `TASTE.md` 是索引，不是全文标准库
- 只有 active taste layers 才应被加载
- event log 只有在近期历史不清楚时才应被读取
- skill 只加载当前阶段需要的那个

如果一个文件不会明显改变当前判断，就先不要读。

### English

The default context strategy is selective loading.

That means:

- `TASTE.md` is an index, not the full standards dump
- only active taste layers should be loaded
- event logs should be read only when recent history is unclear
- only the skill needed for the current phase should be loaded

If a file would not materially change the current judgment, do not load it yet.

## 6. Default State Discipline

### 中文

默认要求把状态写回磁盘，而不是留在聊天里。

项目级最少包括：

- `PROJECT.md`
- `TASTE.md`
- `ROADMAP.md`

任务级最少包括：

- `TASK.md`
- `STATE.md`
- `DECISIONS.md`
- `EVIDENCE.md`
- `RESULTS.md`

可追加的事实历史包括：

- `.codex-agent/events/project-events.jsonl`
- task `EVENTS.jsonl`

快照文件负责让人快速恢复，事件流负责保留材料事实。

### English

By default, state must be written back to disk rather than left in chat.

Minimum project-level state:

- `PROJECT.md`
- `TASTE.md`
- `ROADMAP.md`

Minimum task-level state:

- `TASK.md`
- `STATE.md`
- `DECISIONS.md`
- `EVIDENCE.md`
- `RESULTS.md`

Optional append-only factual history:

- `.codex-agent/events/project-events.jsonl`
- task `EVENTS.jsonl`

Snapshots exist for fast recovery by humans and future sessions; event streams preserve material facts.

## 7. Default Review Rule

### 中文

默认在宣布完成前，要经历两步：

1. execution pass
2. review pass

如果没有 review pass，就不算真正完成。

### English

Before declaring completion, the default flow is:

1. execution pass
2. review pass

Without a review pass, the work is not truly complete.

## 8. Default Escalation Rule

### 中文

如果项目有更具体的本地规则，优先级高于这份文档。

优先级顺序：

1. 用户当前明确指令
2. 本地项目 `AGENTS.md`
3. 当前 task / roadmap / state 文件
4. 当前 phase 对应的 skill
5. 这份默认模式文档
6. 更高层的架构原则文档

### English

If the project has more specific local rules, they override this document.

Priority order:

1. the user's current explicit instruction
2. local project `AGENTS.md`
3. current task / roadmap / state files
4. the skill for the current phase
5. this default operating mode document
6. the higher-level architecture principles document

## 9. Short Version

### 中文

一句话版本：

先读最少必要文件，按 roadmap 和 active taste layers 工作，完成有意义的批次后继续推进，只在真正的硬阻塞时才停。

### English

One-line version:

Read the minimum necessary files, work under the roadmap and active taste layers, continue after each meaningful batch, and stop only for real hard blockers.
