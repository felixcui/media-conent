# 从 Prompt Engineering 到 Harness Engineering：AI 工程体系的四次演进

**作者**: 烟花老师

**来源**: https://mp.weixin.qq.com/s/5tFXJCzmQ5SaaB-Y7vJRbA

---

## 摘要

如果把这些概念放到过去三年的技术演进中观察，会发现它们实际上描述的是同一件事情在不同阶段的关注重点。围绕 Agent 的 XXX Engineering 新概念会越来越多，因为作为应用侧本质上就应该关注工程层面上的创新和实践，类似过去 30 年传统软件生态沉淀出来的各种模式，术语，中间件等等，Agent 应用层也正在经历这样的过程，大家慢慢习惯就好。

---

## 正文

烟花老师 烟花老师

在小说阅读器读本章

去阅读

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/HR8kIomiaALShQFzOFbicHr6iaBUY5djfoRNic0lCKyRrNAMDibjCm0VCG7uRlE5Z2bdeLGSbM6Qyy5iafCLoslqz08weH160sibXbofatM1Ep0DLw/640?wx_fmt=png&from=appmsg)

Agent、Codex、Claude Code等产品的快速发展，让 AI 工程领域出现了一批新的术语：

Prompt Engineering

Context Engineering

Loop Engineering

Harness Engineering

新名词越来越多，边界越来越模糊。

如果把这些概念放到过去三年的技术演进中观察，会发现它们实际上描述的是同一件事情在不同阶段的关注重点。

整个过程可以理解为 AI 系统从单轮对话工具逐步发展为可持续执行任务的软件系统。

围绕 Agent 的 XXX Engineering 新概念会越来越多，因为作为应用侧本质上就应该关注工程层面上的创新和实践，类似过去 30 年传统软件生态沉淀出来的各种模式，术语，中间件等等，Agent 应用层也正在经历这样的过程，大家慢慢习惯就好。

## 第一阶段：Prompt Engineering

2023 年最流行的概念是 Prompt Engineering。

当时的主流工作模式非常简单：

Prompt

↓

LLM

↓

Response

工程师关注的问题主要是：

- Prompt 怎么写
- Few-shot 怎么设计
- Role Prompt 怎么组织
- Chain of Thought 怎么引导
- 输出格式怎么约束

那个阶段的核心目标是提高单次回答质量。

例如：

请扮演资深架构师

请分步骤思考

请输出 Markdown 表格

这些技巧在 GPT-3.5 和 GPT-4 早期阶段产生了非常明显的效果。

Prompt Engineering 推动了大量 AI 应用的诞生，也培养了第一批 AI 应用开发者。

不过随着模型能力快速提升，大家逐渐发现：

Prompt 解决的是单轮交互问题。

很多真实业务问题需要持续执行、多轮决策和长期状态管理。

于是第二阶段开始出现。

## 第二阶段：Context Engineering

2024 年开始，越来越多团队将注意力转向 Context Engineering。

因为大家发现：

模型能力越来越强。上下文质量开始成为主要瓶颈。

此时系统结构变成：

Context

↓

Prompt

↓

LLM

↓

Response

关注点发生变化：

- 检索什么内容
- 检索多少内容
- 如何排序
- 如何压缩
- 如何组织上下文

RAG 的兴起就是这一阶段的重要标志。

例如：

企业知识库问答：

用户问题

↓

向量检索

↓

知识片段

↓

模型回答

此时工程师关注的是：

模型应该知道什么。

Prompt 仍然重要。

但 Context 已经成为影响结果的主要因素。

OpenAI、Anthropic、Google 在这一阶段都不断扩大上下文窗口。

从 8K

到 32K

到 128K

再到百万级 Context。

整个行业开始认识到：

高质量 Context 本身就是一种能力。

## 第三阶段：Loop Engineering

2025 年后，Coding Agent 和 Autonomous Agent 的发展带来了新的变化。

大家发现很多任务已经超出了单轮回答范畴。

例如：

修复一个 Bug

完成一个 Feature

分析一个系统

撰写一个研究报告

这些任务往往持续几十分钟甚至几个小时。

系统结构开始演变为：

Think

↓

Act

↓

Observe

↓

Verify

↓

Iterate

这就是 Agent Loop。

有了 Loop 之后，怎么保证 Loop 的质量，可靠性？

## Loop Engineering 和 Agent Loop 需要区分。

Agent Loop 是 Think / Act / Observe / Verify / Iterate 这种执行循环；

Loop Engineering 是对循环进行设计、约束、验证和优化。

Agent Loop 是运行形态，Loop Engineering 是围绕这个运行形态建立的工程方法。

这就引出了 Loop Engineering。

虽然最近这个话题很火，但是它其实在业界已经实践蛮久了，只是没有单独作为独立概念提出来。

Loop Engineering 关注的问题包括：

- 如何规划任务
- 如何拆解任务
- 如何执行任务
- 如何验证结果
- 如何进行下一轮迭代

例如

Codex：

查看代码

↓

修改代码

↓

运行测试

↓

分析结果

↓

继续修改

Claude Code：

搜索文件

↓

读取代码

↓

修改代码

↓

执行命令

↓

验证结果

OpenHands：

Plan

↓

Act

↓

Observe

↓

Reflect

这些系统都围绕 Loop 展开。

Loop Engineering 的核心目标是：

提高任务完成率。

Prompt Engineering 关注回答质量。

Loop Engineering 关注任务完成质量。

这是 Agent 时代的重要分界线。

### 在企业 Agent 系统里，可以把 Loop Engineering 放在 Harness Engineering 之下理解。

### Loop 负责单个任务如何持续推进，Harness 负责运行时、工具、权限、评测、记忆、可观测性和安全边界。这个划分不是统一标准，但它更符合工程落地。

## 第四阶段：Harness Engineering

最近一年开始，越来越多团队把讨论重心放到了 Harness Engineering。

原因很简单,当 Agent 开始持续工作时，新的问题出现了：

- 如何管理多个 Agent
- 如何管理工具
- 如何管理记忆
- 如何管理评测
- 如何管理成本
- 如何管理安全边界
- 如何管理长期运行状态

这些问题已经超出了单个 Loop 的范围。

于是 Harness 的概念开始出现。

如果用软件工程的视角看：

Prompt Engineering 关注函数调用。

Loop Engineering 关注业务流程。

Harness Engineering 关注整个运行平台。

一个典型 Harness 包含：

Goal

↓

Orchestration

↓

Agent

↓

Tools

↓

Loop

↓

Evaluation

↓

Memory

↓

Observability

↓

Guardrails

此时 Loop 已经成为 Harness 的一个组成部分。

因此Harness Engineering 包含 Loop Engineering。

两者并不是平行关系，更准确的理解是：

Harness Engineering包含

├─ Loop Engineering

├─ Evaluation

├─ Memory

├─ Observability

├─ Guardrails

└─ Orchestration

Loop 是发动机。Harness 是整辆车。

## 为什么会出现这样的演进？

这背后对应的是 AI 系统能力边界的不断扩展。

第一阶段：

模型回答问题。

第二阶段：

模型利用知识回答问题。

第三阶段：

模型执行任务。

第四阶段：

模型参与软件系统运行。

因此整个行业的关注点不断向系统工程迁移。

越来越多团队开始关注：

- Trace
- Evaluation
- Agent Runtime
- Memory
- Tool Use
- Observability

这些传统软件工程概念重新回到了 AI 世界。

## 推荐阅读

## Loop Engineering

Addy Osmani

https://addyosmani.com/blog/loop-engineering/

Firecrawl

https://www.firecrawl.dev/blog/loop-engineering

Oracle Agent Loop

https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems

## Harness Engineering

OpenAI Harness Engineering

https://openai.com/index/harness-engineering/

Martin Fowler

https://martinfowler.com/articles/harness-engineering.html

Anthropic Long-running Agents

https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## 推荐论文

ReAct

https://arxiv.org/abs/2210.03629

Toolformer

https://arxiv.org/abs/2302.04761

Reflexion

https://arxiv.org/abs/2303.11366

Agentic Harness Engineering

https://arxiv.org/abs/2604.25850

From Agent Loops to Structured Graphs

https://arxiv.org/abs/2604.11378

## 推荐开源项目

Codex CLI

https://github.com/openai/codex

OpenHands

https://github.com/All-Hands-AI/OpenHands

OpenAI Agents SDK

https://github.com/openai/openai-agents-python

PydanticAI

https://github.com/pydantic/pydantic-ai

LangGraph

https://github.com/langchain-ai/langgraph

## 推荐视频

Andrej Karpathy：Software Is Changing

https://www.youtube.com/watch?v=LCEmiRjPEtQ

Anthropic Developer Day

https://www.youtube.com/@AnthropicAI

OpenAI DevDay

https://www.youtube.com/@OpenAI

LangChain Agent Engineering 系列

https://www.youtube.com/@LangChain

过去几年，AI 工程领域经历了一条非常清晰的发展路径：

Prompt Engineering

↓

Context Engineering

↓

Loop Engineering

↓

Harness Engineering

Prompt 决定模型如何开始工作。

Context 决定模型能够获得哪些信息。

Loop 决定任务如何持续推进。

Harness 决定整个系统如何稳定运行。

今天的 Agent 已经逐渐从聊天机器人演化为长期运行的软件系统。

未来几年最有价值的能力，将越来越集中在系统设计、评测体系、记忆管理、可观测性和运行时工程这些方向。

模型能力仍然重要。

工程体系正在成为决定上限的关键因素。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过