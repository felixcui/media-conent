# 用 Subagents 保持 Claude Code 上下文干净（译）

**来源**: https://waytoagi.feishu.cn/wiki/Fq5lw2ZDVi0oNeku7ZCcaMk5nxb

---

## 摘要

这篇文章会直接切入重点：subagents 是什么、如何创建一个、Claude Code 自带了哪些内置 subagents，以及如何通过 `CLAUDE_CODE_FORK_SUBAGENT=1` 来 fork 上下文。

---

## 正文

<quote-container>
原帖链接：https://x.com/dani_avila7/status/2048486242321662189
</quote-container>




长时间使用 Claude Code 时，上下文会很快变得一团乱。每一次 `grep`、`find`、`ls` 都会留在你的上下文里，占掉大量你之后根本不会再读的空间。Subagents 就是为了解决这个问题：它们会在自己的窗口里完成工作，最后只把结果带回来。
这篇文章会直接切入重点：subagents 是什么、如何创建一个、Claude Code 自带了哪些内置 subagents，以及如何通过 `CLAUDE_CODE_FORK_SUBAGENT=1` 来 fork 上下文。
## 什么是 subagent
subagent 是一个专门化的助手，它运行在自己的上下文窗口里，拥有自己的 system prompt、工具集合和权限配置。
主代理调用它，subagent 在隔离环境里完成工作，然后返回一份摘要。


你可以通过一个 Markdown 文件加 frontmatter 来创建它：
```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability. Use after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer. When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Start the review immediately

```

Claude Code 会自动识别它，并在 `description` 与任务匹配时调用它。
## subagents 放在哪里
你可以根据作用范围，把文件放在不同的位置。如果两个 subagent 同名，那么优先级更高的位置会生效。


大多数情况下，你会使用 `.claude/agents/`，把它提交进版本控制并与团队共享；或者使用 `~/.claude/agents/`，作为你个人级别、在所有项目里都可用的配置。


## 问题所在：所有事情都塞进一个窗口
如果没有 subagents，主代理就得在单一上下文里处理所有事情。你让它 review 一个 controller、查找一个模式、验证某个问题，它会不断触发 `grep`、`find`、`ls`、`glob`、`cd`、更多的 `grep`、再来一次 `find`，而每一次调用都会残留在你的上下文里。


30 分钟之后，你的上下文里就会堆满 80k tokens 的噪声，而这些内容你根本不会再读。
当 Claude 对上下文做 compact 时，这些信息会被压扁成摘要，真正重要的细节也会在这个过程中被一起磨掉。


## 内置 subagents：Explore 和 Plan
Claude Code 已经为一些常见场景内置了 subagents。你最常用的通常是这两个：
**Explore**：在不污染主上下文的前提下搜索代码库。它会在自己的窗口里跑完所有 `grep` 和 `find`，然后只把相关发现返回给你。
**Plan**：负责调研并产出实现方案。它会读文件、理解架构，然后返回一份 step-by-step 的计划文档。你的主上下文完全看不到那些中间读取过程。
整个流程大致是这样：


你不再需要在主窗口里看到 50 次工具调用，而只会得到 3 行真正有用的答案。其余部分会被直接丢弃。
## Fork 上下文
默认情况下，subagent 会从一个空白上下文启动。这样做对保持整洁很有帮助，但如果你已经在主窗口里花了 100k tokens 建立起对代码库的理解，而你又希望 subagent 继承这些上下文，那么默认行为就不够用了。


forking 就是为了解决这个问题：subagent 会在 fork 的那一刻，拿到父级上下文的一份完整拷贝。
**export CLAUDE_CODE_FORK_SUBAGENT=1**
## 它是如何工作的
一旦设置了 `CLAUDE_CODE_FORK_SUBAGENT=1`，每次启动 subagent 时，它都会默认继承父级的完整上下文。
你也可以通过 `/fork` 这个 slash command 按需进行 fork：


fork 出去的工具调用依然保持隔离，只有最终结果会回到你的主对话里。


fork 出来的 subagent 会：
- 继承 fork 时刻父级的完整对话上下文
- 与父级共享 prompt cache prefix，因此第 2 个到第 N 个子进程的输入 token 成本通常能便宜约 10 倍
- 在隔离环境里运行，它的工具调用不会污染父级上下文
- 最后只返回最终摘要
## 实时观察：context-timeline hook
仅凭控制台去跟踪主代理的上下文和并行运行的 subagents，其实很难看清。我为此做了一个 hook：`context-timeline`。
链接：
[https://www.aitmpl.com/component/hook/monitoring/context-timeline](https://www.aitmpl.com/component/hook/monitoring/context-timeline)


安装方式：
```bash
npx claude-code-templates@latest --hook monitoring/context-timeline

```

它会在你打开会话的那一刻就开始工作，并展示一条时间线：包括主代理的上下文窗口，以及 subagents 如何在各自独立的上下文中启动和运行。
你正在运行的每一个 subagent 都会实时显示出来，以及它结束时到底把哪些上下文结果带回主代理。
我的建议是：先从 `.claude/agents/` 里放一个最简单的 subagent 开始。你会在第一次长会话里就明显感觉到差别。