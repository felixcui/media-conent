# The Agent Loop Architecture

**作者**: AI技术立文

**来源**: https://mp.weixin.qq.com/s/0vELFAO3AM3Dw2YuZzSm8A

---

## 摘要

本文探讨了Agent Loop架构，强调其核心在于底层的耐久编排执行层。传统的单会话Agent Loop无法解决进程崩溃重启、长时间等待子代理等复杂场景下的状态丢失与重复执行问题。要构建可靠的Agent Loop架构，必须以耐久性为基础，将Loop视为由计划触发、LLM作为决策者的机制，并确保执行过程中的每一步都进行状态检查点保存与决策持久化，从而实现崩溃后从上一步无缝恢复。

---

## 正文

AI技术立文 AI技术立文

在小说阅读器读本章

去阅读

## 文章来自INNGEST CTO.

---

## 1 Agent Loop 架构

所有人都在问：“loop 到底是什么？”但很少有人追问：这个 loop 到底运行在哪里？

AI 领域的讨论已经把 loop 视为智能体系统的核心原语。Matt Van Horn（@mvanhorn）梳理了 agent loop 的演进脉络 <sup>[1]</sup> ：从 ReAct，到工具调用，到编排 loop，再到监督其他 loop 的 loop。Addy Osmani（@addyosmani）拆解了 loop 内部的构成模块 <sup>[2]</sup> ：自动化、worktree、skill、connector、sub-agent。Van Horn 最后把重点放在 durability，也就是耐久性上：不能在重启后继续运行的 loop，就不能算 loop。Osmani 的主线则是编排：设计一个替你提示 agent 的系统。

我想把他们的观点再往前推一步。耐久性不只是 loop 的一个属性。它属于支撑 loop 的整个执行层。要构建 agent loop 架构，耐久编排是基础。下面拆开看这个架构。

## 2 Loop 在哪里断裂

`/loop` 和 `/goal` 这类模式很适合处理单 agent、单会话的工作。agent 会持续循环，直到任务完成。这已经覆盖了很多场景。但下一阶段，也就是 Van Horn 框架里的 Stage 5，问题开始出现：

- 监督其他 loop 的 loop
- 按计划运行的 loop，而不只是由人触发
- 能在进程重启、部署和崩溃后继续运行的 loop
- 能创建 sub-agent 并等待结果的 loop，有时要等几个小时
- 事后可观测的 loop

这不是提示词问题。这是基础设施问题。

Van Horn 引用了 @runes\_leo <sup>[3]</sup> 的一句话：“AI 编程里成本最高的事情，已经不是写代码，而是管理 agent loop。”终端里的 `while True` 给不了这些能力。VM 或 sandbox 上的长进程也给不了。

想想在服务器上运行一个 agent loop 会发生什么。进程会死亡或重启。一次部署、一次 OOM、一次 spot instance 回收。loop 重新开始。但它刚才在做什么？执行到哪一步了？Slack 消息发过了吗？sub-agent 已经调用了吗？

你不知道。它从头开始。重新获取已经拿到过的数据。重新调用 LLM 做已经做过的决策。发送重复通知。创建重复的 sub-agent。你早上醒来，看到三条一模一样的 Slack 消息，团队一头雾水。

修复方式不是“更好的错误处理”。你需要一种执行模型：每一步都做 checkpoint，每个决策都持久化，恢复时从上一个成功步骤继续。

## 3 Agent Loop 架构的三层

这个架构可以分成三层，每一层都对应一个具体原语。

## 3.1 第一层：Loop

loop 是 cron 加决策者。它按计划或触发器运行，评估状态，然后决定下一步做什么。

这是 Van Horn 定义的具体化：cron 过去缺少的是中间的决策。做决定的是 agent，不是你。cron 是心跳。LLM 是决策者。步骤是耐久执行层，用来 checkpoint 进度。

```typescript
export const infraHealthCheck = inngest.createFunction(
  { id: "infra-health-check" },
  { cron: "*/30 * * * *" }, // Every 30 minutes
  async ({ step }) => {
    const metrics = await step.run("fetch-service-metrics", async () => {
      return await fetchServiceMetrics(); // error rates, latency, memory, CPU
    });

    const assessment = await step.run("assess-health", async () => {
      return await callLLM({
        prompt: \`Given these service metrics, classify overall system health
                 as "normal", "degraded", or "critical". Explain your reasoning.
                 Metrics: ${JSON.stringify(metrics)}\`,
      });
    });

    if (assessment.status === "degraded" || assessment.status === "critical") {
      await step.invoke("triage-incident", {
        function: incidentTriage,
        data: { metrics, assessment, services: assessment.affectedServices },
      });
    }
  }
);
```

每周一上午 9 点，loop 被触发。它获取数据，询问 LLM 是否需要生成报告，如果需要，就调用一个 skill。如果进程在步骤之间重启，已经完成的步骤不会重新执行。这就是 loop。不是 LLM，而是围绕 LLM 的那个 loop。

## 3.2 第二层：Skill

在这里，skill 不是提示词。它是耐久 workflow。它可以有多个步骤，可以重试，可以组合，也可以独立部署。

Van Horn 说：“loop 是管道。它调用的 skill 才是资产。”这一层会复利。系统每学会一个新 skill，每个 loop 的能力都会增强。

```typescript
export const incidentTriage = inngest.createFunction(
  { id: "incident-triage", retries: 3 },
  { event: "infra.incident.triage" },
  async ({ event, step }) => {
    const details = await step.run("fetch-detailed-metrics", async () => {
      return await fetchDetailedMetrics({ services: event.data.services });
    });

    const deploys = await step.run("fetch-deploy-history", async () => {
      return await fetchRecentDeploys({ since: hoursAgo(2) });
    });

    const analysis = await step.run("correlate-incident", async () => {
      return await callLLM({
        prompt: \`Correlate these service metrics with recent deploys.
                 Identify the likely root cause and severity.
                 Metrics: ${JSON.stringify(details)}
                 Recent deploys: ${JSON.stringify(deploys)}\`,
      });
    });

    await step.run("post-triage-summary", async () => {
      await slack.postMessage({
        channel: "#incidents",
        text: formatTriageSummary({
          analysis,
          affectedServices: event.data.services,
          recommendedActions: analysis.recommendations,
        }),
      });
    });

    return analysis;
  }
);
```

这个 skill 会获取信息、分类并路由。它是一个带内置容错能力的工作单元。skill 可以是在中间调用 LLM 的 AI workflow，也可以是确定性的代码。

## 3.3 第三层：Orchestrator

orchestrator 是运行一切的引擎：调度 cron、执行步骤、管理重试、执行并发限制、存储运行历史，并在不打断已运行 workflow 的情况下热部署新的 function 或 workflow。

这一层没人怎么谈，因为它理应不可见。但它是基础。

大多数人把 agent 理解成“LLM + tools”。agent loop 架构把它重新表述为“loops + skills + orchestration”。LLM 和 tools 在 loop 内部。LLM 和 tools 可以替换或调整，架构保持不变。编排让这个架构成立。

## 4 出错时会发生什么

happy path 很简单。但这是跑在生产环境里的软件，事情真的会一直按计划发生吗？

你的 incident triage skill 被触发，metrics API 超时了。读取必须落到磁盘，内存缓存没有数据。调用这个 API 的 step 开始重试，再次命中 API。此时数据已经被部分缓存，API 完成。skill 像什么都没发生一样继续执行下一步。

有时不会这么简单。API key 过期，或托管服务商宕机 30 分钟。所有重试都耗尽了。接下来怎么办？你还必须处理失败。

```typescript
export const incidentTriage = inngest.createFunction(
  {
    id: "incident-triage",
    retries: 3,
    onFailure: async ({ error, event, step }) => {
      // The function failed after exhausting retries.
      // We still have the original event data. Nothing is lost.
      await step.run("notify-failure", async () => {
        await slack.postMessage({
          channel: "#agent-ops",
          text: \`⚠️ Incident triage failed: ${error.message}. \` +
                \`Will retry on next health check cycle. \` +
                \`Affected services: ${event.data.services.join(", ")}\`,
        });
      });
    },
  },
  { event: "infra.incident.triage" },
  async ({ event, step }) => {
    /* the same logic as the skill above */
  }
);
```

`onFailure` handler 会在所有重试耗尽后触发。它往 ops channel 里发消息，让人知道出了问题。event 被保留下来，没有任何东西丢失。下一次计划运行时，系统可以从上次没能继续的地方接上。

耐久编排必须提供 step 级重试，用于处理瞬时错误；也必须提供失败处理 hook，用于处理不可恢复的错误。没有这些能力，系统迟早会坏掉，而且你可能几个小时甚至几天后才发现。

瞬时错误也很贵。如果你的 skill 或 agent 从头开始重试，就会多次调用 LLM，白白消耗 token。LLM 调用可以被 checkpoint。再把这个成本乘以系统里的 10 个、30 个 agent。开销很快会上去。

step 级 checkpoint 不只是正确性功能。它也能省钱。

## 4.1 会构建自己 Skill 的 Agent

这里开始更有意思。系统不是静态的。它被设计成可以演进和扩展自己。

agent 不只是运行在 loop 里。它会编写新的 loop，并把它们注册到编排引擎里。每个部署后的 function 都是一个耐久 skill，可以由 loop 或 agent 触发，也可以按计划运行，并有自己的重试逻辑。skill 会复利。

这就是 orchestration-aware agent，也就是具备编排感知能力的 agent。

工作方式是这样的：AI agent 可以把 orchestration SDK 当作工具使用。它能编写新的 function，把它们注册到引擎里，然后这些 function 立即开始运行。agent 进程可以热加载新 function，不需要重启，也不会打断正在运行的任务。

看一个具体例子：

1. 人提出需求。工程师说：“我们的服务总在夜里出现延迟尖峰，没人注意到，直到第二天早上。”这是触发点。agent 不需要从环境数据里猜一个模糊模式。它拿到了清晰指令。
2. agent 编写一个 skill。两个多步骤 function：一个 health check loop 每 30 分钟运行一次，拉取错误率、延迟和资源使用情况，用 LLM 把系统健康状态分类为 normal、degraded 或 critical；一个 incident triage skill 获取详细指标和近期部署历史，用 LLM 关联根因，并把带推荐动作的 triage 摘要发到 Slack。错误处理：如果 metrics API 挂了，就退避并重试。如果 LLM 失败，就回退到基于规则的严重程度分类。
3. agent 部署这个 skill。agent 写出的 function 代码由 sidecar 进程拾取。新 function 自动注册。它们立刻上线，不需要部署流水线，也不需要 PR。
4. skill 自主运行。每 30 分钟，引擎触发 health check。如果有问题，它调用 triage skill。没有人在 loop 里。全程耐久。
5. agent 基于信号迭代。这一点经常被轻描淡写，所以我具体说明“迭代”指什么。agent 不是神奇地注意到模式。它有一个独立的 review loop：一个由 cron 触发的 function，每周运行，读取 orchestrator 的运行历史，并评估表现：

```typescript
export const reviewSkillPerformance = inngest.createFunction(
  { id: "review-skill-performance" },
  { cron: "0 10 * * 5" }, // Every Friday at 10am
  async ({ step }) => {
    const runs = await step.run("fetch-run-history", async () => {
      return await getInngestRuns({
        functionId: "incident-triage",
        since: daysAgo(7),
      });
    });

    const analysis = await step.run("analyze-performance", async () => {
      const successRate = runs.filter(r => r.status === "completed").length / runs.length;
      const avgDuration = average(runs.map(r => r.duration));
      const incidents = await fetchIncidentOutcomes(); // Did incidents correlate with actual outages?

      return await callLLM({
        prompt: \`Review this skill's performance over the past week.
                 Success rate: ${successRate}
                 Avg duration: ${avgDuration}ms
                 Incidents correlated with real outages: ${incidents.confirmed}/${incidents.total}
                 False positives: ${incidents.falsePositives}
                 Team acted on alerts: ${incidents.actedOn}/${incidents.total}
               
                 Should we adjust thresholds or classification? What specific changes?\`,
      });
    });

    if (analysis.shouldModify) {
      await step.invoke("update-skill", {
        function: coreAgent,
        data: { prompt: \`Update the incident-triage skills based on the following proposed changes: ${analysis.proposedChanges}\` },
      });
    }
  }
);
```

“review” 本身就是一个 function。它读取运行历史，检查 incident 是否和真实故障相关，然后把这个信号交给 LLM。如果 health check 总是把某个服务标为 degraded，但团队一直忽略，因为阈值太敏感，review loop 会捕捉到这一点，然后更新 skill，调整分类逻辑。没有魔法。只是一个把 LLM 放在决策位上的 cron job。

验证怎么办？agent 写代码的质量取决于它周围的护栏。代码可以做类型检查。agent 可以自己调用 function 来测试，因为它也能和 orchestration engine 交互。虽然这不是万无一失，但你让 core agent 可以在自己运行的系统里原生调试它写出的 skill。review loop 会捕捉初始调试没发现的问题。

再进一步，agent 可以使用 `onFailure` hook 触发自己，让自己评估某个失败。这是一个持续改进的反馈 loop。

冲突怎么办？flow control，尤其是 concurrency control 或 singleton，可以处理简单情况： `concurrency: [{ limit: 1, key: "event.data.service" }]` ，意思是每个服务同一时间只运行一个 incident triage。但更深的问题是：如果两个 health check 同时发现同一个服务有问题，会怎样？orchestrator 会把它们排队。第二个 triage 等第一个完成。没有重复告警，没有竞态条件。这不是理论。它和任何 job queue 里会用到的并发原语是同一类东西。

agent 不只是在执行任务。它在为自己构建基础设施。每个 skill 都会留存在创建它的那次对话之后。杀掉 agent 进程再重启，skill 继续运行。替换底层模型，skill 继续运行。agent 是短暂的，它的产物是耐久的。

![Agent loop architecture system overview](https://mmbiz.qpic.cn/mmbiz_png/IUJGIjicknic04c33NGLZRbR8BhzmA0g4YNziaygIzwrKt1WULQMWW7WAKKyjSZQrWdViaUR3T5xd7mXqIQpBBBOgXiaxafiaia59jOYVvBGaJ1oBE/640?wx_fmt=png&from=appmsg)

## 4.2 开发者视角

这件事很重要。开发者如果看不到 agent 部署了什么、无法调试哪里坏了、无法审计凌晨 3 点运行了什么，整个架构就会变成很大的运维风险。

编排引擎会存储每一次运行、每一个 step、每一份输入、每一份输出、每一次重试。agent 上周二部署的某个 skill 在凌晨 4 点失败了？你可以精确看到哪个 step 失败、输入是什么、抛出了什么错误、放弃前重试了多少次。step 级完整 trace 是编排引擎自身的输出。

这不是事后补上的 dashboard。它内建于耐久执行。每个 `step.run()` 都是一个 checkpoint。每个 checkpoint 都是可观测的。当写代码的不是人时，可观测性不是锦上添花，而是信任层。

日常开发者工作流大概是这样：早上查看 runs dashboard。看看昨夜哪些 skill 运行了，哪些成功，哪些失败。如果某个 agent 写的 skill 表现异常，你可以直接读代码、编辑它、删除它，或让 agent 修复它。skill 是 agent 写的，但所有权在你。agent 和它生成的 skill 仍然需要持续维护。

## 5 为什么耐久性是基础

Van Horn 说：“这些东西必须能在重启后继续运行。”

耐久性在实践里意味着：

| Requirement | What it means | Why basic while loop fails |
| --- | --- | --- |
| **Independent step retry** | 如果 5 个 step 里的第 3 个失败，只重试第 3 个，而不是重跑第 1、2 个 | loop 重启会从头执行所有内容 |
| **Sub-agent lifecycle** | 创建子任务，等待它完成，可能要等几小时；父任务取消时，子任务也要能取消 | 没有内置的父子生命周期管理 |
| **Guaranteed event delivery** | agent 下线时触发的 event，也应该在恢复后被处理 | 进程不运行时，event 会丢失 |
| **Post-hoc observability** | 事后看到发生了什么：每个 step、每个决策、每次重试 | 你只能依赖日志，而日志是短暂的 |
| **Hot-deploy without downtime** | 部署新的 function 版本时，不杀掉正在运行的任务 | 进程重启会杀掉所有任务 |
| **Concurrency control** | 限制某个 skill 同时最多运行 N 个实例 | 没有内置并发原语 |

“放进容器里跑”只能给你 uptime。它不能给你正确性。容器在崩溃后重启，进程是回来了，但所有进行中的 loop 都会从头开始。每个 step 会重新执行。每个 LLM 调用会重新发起。loop 看起来在运行，其实是在盲跑。

## 6 和现有工具相比如何

有些工具会给你一个“漂亮”的 turnkey 方案，帮你搭这类系统；你也可以把一些更底层的工具拼在一起，自己做系统。两种选择都没错。但正确的架构层应该允许你和你的 agent 持续演进。它需要灵活、动态、耐久。

适合 agent 的耐久执行原语，应该是 agent 可以轻松编写的原语；同时要有可观测性和 API，让 agent 自己也具备编排感知能力。

## 7 复利 Loop

Satya Nadella 在 最近的一篇帖子 <sup>[4]</sup> 里说出了整个行业已经感受到的一点：护城河不是模型，而是 loop。

他的框架是：有两类资本。第一类是人力资本，也就是你的团队多年积累的知识和判断力。第二类是他称为 token capital 的东西，也就是一家公司基于基础模型构建出的 AI workflow、决策模式和已学习 skill。

核心观点是：这两者会一起复利。每个被改进的 workflow 都会产生更好的信号。更好的信号会带来更准确的 AI 行为。更准确的行为会把人的注意力释放出来，让人处理更依赖判断的工作。这是一台爬坡机器。

agent loop 架构把这件事具体落地：

- agent 部署的每个耐久 skill，都是被编码成可执行基础设施的组织知识。它会持续存在。无论有没有人盯着，它都会运行。
- 一个由 cron 触发的 review loop，会评估 skill 表现并迭代。这就是变成现实的爬坡机器。不是 deck 里的飞轮图，而是一个带 cron trigger 的 function。
- 如果你的 skill 在进程重启后就死掉，复利会归零。耐久性让投入能保留下来。

Nadella 的关键点是：“一家公司应该能够替换掉一个‘通用型’模型，而不失去它的学习系统里积累出的‘公司老兵’经验。”这就是 skill library 模式。耐久 function 不关心是哪一个 LLM 在调用它。

## 8 按这个方向构建

之前的讨论一直集中在 agent 做什么：loop、工具、推理、上下文工程。下一轮讨论应该转向：Agent 在何处运行。

三层：loop、skill、orchestrator。loop 是工作单元。skill 是资产。orchestration engine 让两者变得耐久。sidecar 模式是具体模型：agent 编写自己的耐久 skill，部署它们，回顾它们的表现，并持续迭代。这不是思想实验。它是一个可运行的模型。

这个架构模式比任何单一工具都更大。如果你正在生产环境里构建 agent loop，请先定义这三层：loop、skill、orchestrator。

## 参考链接：

\[1\]https://x.com/mvanhorn/status/2063865685558903149

\[2\]https://addyosmani.com/blog/loop-engineering/

\[3\]https://x.com/runes\_leo

\[4\]https://x.com/satyanadella/status/2066182223213293753

![图像](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic20K8lD5EDqYtj3MgHo52cm98lJfOtEkvR9foVeTPNtMJHTaHcwlxfDHyVFfRnVtF2ZVmpYbCDasoMUPofbqVb7E2NK6FTgqXE/640?wx_fmt=jpeg&from=appmsg)

继续滑动看下一个

AI技术立文

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过