# CodexFlow

中文 / English

## 1. 项目简介

### 中文

CodexFlow 是一个把 Codex 变成“外置大脑”的项目。

它的目标不是只提供几段提示词，而是提供一套可复用的 agent 工作流，包括：

- 新项目初始化
- 灵感澄清与规格收敛
- 多任务连续推进
- 长时间命令运行管理
- 任务状态落盘
- 阶段评测与复盘

你可以把 `aiAgnet` 视为中央脑仓库，把任意新项目视为接入这个中央脑的工作空间。

### English

CodexFlow turns Codex into an external brain.

Its goal is not just to provide prompts, but to provide a reusable agent workflow, including:

- new-project bootstrap
- idea clarification and spec shaping
- multi-task autonomous execution
- long-running command handling
- persisted task state
- milestone evaluation and review

You can treat `aiAgnet` as the central brain repository, and any new project as a workspace attached to that brain.

## 2. 核心理念

### 中文

CodexFlow 的设计原则：

- 不依赖聊天历史作为主要记忆
- 尽量把状态写入磁盘
- 用 Markdown 快照做主入口，用 append-only 事件流补充事实时间线
- 用薄本地入口连接中央脑，而不是让新项目“读取整个仓库”
- 用 skill 区分不同阶段：立项、执行、评测
- 用分层 TASTE 控制上下文，只加载当前激活的质量标准
- 用 roadmap 和 autonomy budget 降低不必要的暂停

### English

CodexFlow is designed around these principles:

- do not rely on chat history as the main memory
- persist state on disk whenever possible
- use Markdown snapshots as the main entrypoint and append-only events for factual history
- attach projects through a thin local entrypoint instead of asking Codex to read the whole brain repo
- use dedicated skills for inception, delivery, and evaluation
- keep taste layered so only active quality rules are loaded
- use roadmap and autonomy budgets to reduce unnecessary pauses

更完整的架构立场见 [ARCHITECTURE_PRINCIPLES.md](/home/zhibai/projects/aiAgnet/ARCHITECTURE_PRINCIPLES.md)。

For the fuller architectural stance, see [ARCHITECTURE_PRINCIPLES.md](/home/zhibai/projects/aiAgnet/ARCHITECTURE_PRINCIPLES.md).

默认执行方式见 [DEFAULT_OPERATING_MODE.md](/home/zhibai/projects/aiAgnet/DEFAULT_OPERATING_MODE.md)。

For the default execution behavior, see [DEFAULT_OPERATING_MODE.md](/home/zhibai/projects/aiAgnet/DEFAULT_OPERATING_MODE.md).

## 3. 快速开始 / Quick Start

### 中文

进入一个新项目目录后，直接运行：

```bash
codexflow-init
```

它会交互式询问你：

- 项目名
- 是否从粗略想法开始
- 如果是 inception 模式，会再问一句项目想法

初始化完成后，它会生成：

- 本地 `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- 如果提供了想法，还会生成 inception 包

然后在该项目目录中启动 Codex，并把 `START_Codex.md` 的内容作为第一条消息发给新对话。

### English

Inside a new project directory, run:

```bash
codexflow-init
```

It will ask for:

- project name
- whether the project starts from a rough idea
- if inception mode is selected, one sentence describing the project idea

After initialization, it creates:

- local `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- and an inception packet if an idea was provided

Then start Codex inside that project and use the contents of `START_Codex.md` as the first message.

## 4. 使用方式 / Typical Usage

### 中文

#### 4.1 从灵感开始

如果你只有一个模糊想法：

1. 运行 `codexflow-init`
2. 进入 inception 模式
3. 让 Codex 先澄清问题、识别歧义、收敛 phase 1
4. 生成 `SPEC.md` 和 `PLAN.md`
5. 再进入 delivery 阶段

#### 4.2 从明确项目开始

如果你已经知道大致要做什么：

1. 运行 `codexflow-init`
2. 进入 delivery 模式
3. 填写或调整 `ROADMAP.md`
4. 让 Codex 按 roadmap 连续推进

#### 4.3 轻量事件层与分层 TASTE

默认状态模型是：

- `PROJECT.md`、`TASTE.md`、`ROADMAP.md`、`TASK.md`、`STATE.md` 负责给人和新会话快速恢复上下文
- `.codex-agent/events/project-events.jsonl` 和 task `EVENTS.jsonl` 负责记录追加式事实
- `TASTE.md` 只是索引，真正的项目标准放在 `taste/project.md`
- 只有 `TASTE.md` 标记为 active 的 taste layer 才应该被读取

这意味着 CodexFlow 不走重数据库路线，也不要求每次启动都扫描全部历史。

#### 4.4 阶段复盘

如果你想知道 agent 工作得好不好：

1. 使用 `agent-eval`
2. 对 task、milestone 或 phase 进行评分
3. 把结论转成后续流程改进

### English

#### 4.1 Starting from an idea

If you only have a rough concept:

1. run `codexflow-init`
2. enter inception mode
3. let Codex clarify the problem, detect ambiguity, and shape phase 1
4. produce `SPEC.md` and `PLAN.md`
5. then move into delivery mode

#### 4.2 Starting from a defined project

If you already know what you want to build:

1. run `codexflow-init`
2. enter delivery mode
3. fill or adjust `ROADMAP.md`
4. let Codex continue through the roadmap

#### 4.3 Lightweight event layer and layered taste

The default state model is:

- `PROJECT.md`, `TASTE.md`, `ROADMAP.md`, `TASK.md`, and `STATE.md` are the main human and resume entrypoints
- `.codex-agent/events/project-events.jsonl` and task `EVENTS.jsonl` hold append-only factual history
- `TASTE.md` is an index, while actual project standards live in `taste/project.md`
- only taste layers marked active in `TASTE.md` should be loaded

This keeps CodexFlow away from a heavy database-first architecture and avoids loading every historical artifact on startup.

#### 4.4 Evaluating the agent

If you want to know whether the agent workflow is actually good enough:

1. use `agent-eval`
2. score a task, milestone, or phase
3. convert findings into workflow improvements

## 5. 三个核心 Skill / Core Skills

### 中文

- `idea-to-spec`
  - 用于：灵感澄清、问题重写、规格收敛、第一阶段计划
- `agent-dev-loop`
  - 用于：执行任务、验证、状态更新、连续推进
- `agent-eval`
  - 用于：评估 agent 的 autonomy、state、verification、interruption、output quality

### English

- `idea-to-spec`
  - for idea clarification, problem rewriting, spec shaping, and first-phase planning
- `agent-dev-loop`
  - for execution, verification, state updates, and autonomous delivery loops
- `agent-eval`
  - for evaluating autonomy, state quality, verification quality, interruption quality, and output quality

## 6. 项目结构 / Repository Structure

```text
aiAgnet/
├── AGENTS.md
├── MASTER_BOOTSTRAP.md
├── README.md
├── codexflow-init
├── scripts/
│   └── codexflow_init.py
├── bootstrap/
│   ├── first-message-template.md
│   └── project-agents-template.md
├── skills/
│   ├── agent-dev-loop/
│   ├── idea-to-spec/
│   └── agent-eval/
└── workspaces/
    ├── .gitkeep
    └── <local projects>
```

### 中文

- [AGENTS.md](/home/zhibai/projects/aiAgnet/AGENTS.md)
  - 根规则与推荐用法
- [MASTER_BOOTSTRAP.md](/home/zhibai/projects/aiAgnet/MASTER_BOOTSTRAP.md)
  - 中央脑单入口
- [codexflow-init](/home/zhibai/projects/aiAgnet/codexflow-init)
  - 启动器
- [scripts/codexflow_init.py](/home/zhibai/projects/aiAgnet/scripts/codexflow_init.py)
  - 初始化逻辑
- `bootstrap/`
  - 本地薄入口和首条提示词模板
- `skills/`
  - 核心 agent 能力
  - `agent-dev-loop` 现在还包含事件层与 taste 分层模板
- `workspaces/`
  - 本地项目沙箱；默认不推送到远程

### English

- [AGENTS.md](/home/zhibai/projects/aiAgnet/AGENTS.md)
  - root rules and recommended usage
- [MASTER_BOOTSTRAP.md](/home/zhibai/projects/aiAgnet/MASTER_BOOTSTRAP.md)
  - central-brain single entrypoint
- [codexflow-init](/home/zhibai/projects/aiAgnet/codexflow-init)
  - launcher
- [scripts/codexflow_init.py](/home/zhibai/projects/aiAgnet/scripts/codexflow_init.py)
  - bootstrap logic
- `bootstrap/`
  - thin local entrypoint and first-message templates
- `skills/`
  - core agent capabilities
  - `agent-dev-loop` now also carries event-layer and layered-taste templates
- `workspaces/`
  - local project sandboxes; ignored from remote by default

## 7. 新项目中会生成什么 / What Gets Generated in a New Project

### 中文

CodexFlow 会在目标项目中生成：

- `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- `.codex-agent/inception/...`（如果是 inception 模式）
- `.codex-agent/tasks/...`（后续 delivery 阶段）
- `.codex-agent/evals/...`（后续评测阶段）

### English

CodexFlow generates these files in the target project:

- `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- `.codex-agent/inception/...` if inception mode is used
- `.codex-agent/tasks/...` during delivery
- `.codex-agent/evals/...` during evaluation

## 8. 为什么不是“读取整个仓库” / Why Not “Read the Entire Repository”

### 中文

我们刻意避免让新项目里的 Codex “读取 aiAgnet 下所有文件”，因为这样会带来：

- 上下文膨胀
- 规则冲突
- 优先级不清
- 执行不稳定

CodexFlow 采用的是：

- 中央脑单入口
- 本地薄入口
- 按阶段按需读取 skill

### English

We intentionally avoid telling a new Codex session to “read everything” in the brain repository, because that causes:

- context bloat
- rule conflicts
- unclear priority
- unstable execution

CodexFlow instead uses:

- one central bootstrap file
- one thin local entrypoint
- skill loading on demand by phase

## 9. Git 与本地项目 / Git and Local Projects

### 中文

`workspaces/` 里的项目默认是本地沙箱，不应该自动进入 CodexFlow 主仓库的远程分支。

如果某个 workspace 需要独立版本控制，应在该目录内单独初始化它自己的 git 仓库。

### English

Projects under `workspaces/` are local sandboxes by default and should not be uploaded to the CodexFlow remote repository automatically.

If a workspace needs version control, initialize a separate git repository inside that project.

## 10. 真实示例 / Real Examples

### 中文

#### 示例 A：从零启动 `websiteToApp`

```bash
cd /home/zhibai/projects/aiAgnet/workspaces/websiteToApp
codexflow-init
```

如果你选择 inception 模式，初始化完成后会生成：

- `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- `.codex-agent/inception/...`

然后启动 Codex，把 `START_Codex.md` 中的内容作为第一条消息发给新对话。

这个新对话应先做：

1. 读取本地 `AGENTS.md`
2. 接入中央脑 `MASTER_BOOTSTRAP.md`
3. 继续 idea clarification
4. 产出 `SPEC.md` 和 `PLAN.md`
5. 再切入 delivery

#### 示例 B：进入已有项目 `NovelMatrix`

在已有项目目录中启动 Codex，然后发送：

```text
Read ./AGENTS.md and start this project.
```

Codex 应该先读：

- `AGENTS.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`（如果 `TASTE.md` 标记为 active）
- `.codex-agent/ROADMAP.md`

如果存在活跃的 inception packet，就先继续澄清和规格收敛。  
如果已经存在活跃 task，就直接按 `ROADMAP.md` 和 task state 继续推进。  
只有在近期历史不清楚时，才去读 `.codex-agent/events/project-events.jsonl` 或 task `EVENTS.jsonl`。

### English

#### Example A: starting `websiteToApp` from scratch

```bash
cd /home/zhibai/projects/aiAgnet/workspaces/websiteToApp
codexflow-init
```

If inception mode is selected, initialization will create:

- `AGENTS.md`
- `START_Codex.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md`
- `.codex-agent/ROADMAP.md`
- `.codex-agent/events/project-events.jsonl`
- `.codex-agent/inception/...`

Then start Codex and paste the contents of `START_Codex.md` as the first message.

That new Codex session should:

1. read the local `AGENTS.md`
2. connect to the central brain through `MASTER_BOOTSTRAP.md`
3. continue idea clarification
4. produce `SPEC.md` and `PLAN.md`
5. then move into delivery

#### Example B: entering an existing project like `NovelMatrix`

Start Codex inside the project root and send:

```text
Read ./AGENTS.md and start this project.
```

Codex should read:

- `AGENTS.md`
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/taste/project.md` if `TASTE.md` marks it active
- `.codex-agent/ROADMAP.md`

If there is an active inception packet, continue clarification and spec shaping first.  
If there is already an active task, resume directly from task state and continue under `ROADMAP.md`.  
Only consult `.codex-agent/events/project-events.jsonl` or task `EVENTS.jsonl` when recent history is unclear.

## 11. 当前状态 / Current Status

### 中文

目前 CodexFlow 已具备：

- 全局 `codexflow-init`
- 外置大脑启动层
- inception / delivery / evaluation 三阶段 skill
- roadmap 驱动的连续推进协议
- 轻量 append-only 事件层
- 分层 TASTE 加载模型
- 本地首条提示词生成

后续仍可继续优化：

- 更智能的 startup mode 判断
- 从 roadmap 自动创建下一个 task
- 更强的项目特定 skill 发现与组合

### English

CodexFlow currently provides:

- global `codexflow-init`
- external-brain bootstrap layer
- inception / delivery / evaluation skills
- roadmap-driven continuity
- lightweight append-only event logs
- layered taste loading
- generated first-message file for new Codex conversations

Future improvements may include:

- smarter startup mode detection
- automatic task creation from roadmap
- stronger project-specific skill discovery and composition

## 12. License

See [LICENSE](/home/zhibai/projects/aiAgnet/LICENSE).
