# Claude Code 团队官方：如何设计 Agent Loop？

**作者**: ClaudeDevs

**来源**: https://mp.weixin.qq.com/s/_NqXsu7dx_LkZSBmZMFqRw

---

## 摘要

Claude Code 团队指出，使用 coding agent 的重点正从写提示词转向设计 Agent Loop，即 Agent 反复执行工作直到满足停止条件的循环过程。设计 Loop 需关注触发方式、停止条件及任务类型等维度，应从简单解法起步。

---

## 正文

ClaudeDevs ClaudeDevs

在小说阅读器读本章

去阅读

作者：ClaudeDevs

原文：

https://x.com/ClaudeDevs/status/2074208949205881033

本文看点

01

导读

02

从 loop 开始理解 coding agent

03

Turn-based loop：每一次提示词都是一次手动循环

01

SECTION

### 导读

最近很多人在讨论一个变化：使用 coding agent 时，重点正在从“写一个更好的提示词”，转向“设计一个更好的 loop”。

这句话听起来很抽象，但 Claude Code 团队给了一个非常工程化的定义： **loop 是 agent 反复执行一组工作循环，直到满足停止条件。**

这篇帖子有价值的地方在于，它没有把 loop 讲成玄学。它把 loop 拆成几个可以落地的维度：如何触发、如何停止、用哪个 Claude Code primitive、适合哪类任务、怎样控制 token，以及怎样保证代码质量。

对开发者和团队负责人来说，这篇文章真正想提醒的是：当你把 agent 用到日常研发里，提示词只是入口， **可验证的停止条件、任务边界、检查机制和调度方式** ，才是让 agent 稳定工作的关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HR8kIomiaALSXq9Siaz7bO31pY1EqDmn9vNHlmTtkgxFN9Il1US16KcUN8VYhV58AML7GBJhSSpI8JSYqZdHLXCOCxarT0FIUFCMWbLMwWSPM/640?from=appmsg)

— 原文封面

02

LOOP CODING AGENT

### 从 loop 开始理解 coding agent

现在有很多人在说，与其不断提示 coding agent，不如开始设计 loop。

如果你花一点时间在 X 上寻找 loop 的定义，会看到很多不同答案。

在 Claude Code 团队内部，他们把 loop 定义为：agent 重复一轮又一轮工作，直到某个停止条件被满足。

Claude Code 团队会从几个维度给 loop 分类：

• 它是怎样被触发的；

• 它是怎样被停止的；

• 它使用了哪个 Claude Code primitive；

• 它最适合处理哪一类任务。

下面会覆盖几类主要 loop：每一种什么时候使用，以及在管理 token 使用量的同时，怎样维持代码质量。

需要注意的是，很多任务并不需要复杂 loop。应该从最简单的解法开始，只在合适场景里选择性使用这些模式。

03

TURNBASED LOOP

### Turn-based loop：每一次提示词都是一次手动循环

![](https://mmbiz.qpic.cn/mmbiz_jpg/HR8kIomiaALSKOH8JBowa2ic30zwc0qPiaSrLCaibaaiaQUHdsBeguFwELAT1SUYLfKdG1ObMAR49R1sbxCuXeBMt4mREV49qUElBOvxzYfthAd8/640?from=appmsg)

— Turn-based loop

• 触发方式：用户发出提示词。

• 停止条件：Claude 判断任务已经完成，或者需要更多上下文。

• 最适合：较短任务，尤其是那些不属于固定流程或固定日程的任务。

• 管理使用量：写更具体的提示词，并通过 skills 改进验证步骤，减少来回轮次。

你每发出一个提示词，都会启动一个由你手动指挥的 loop。

Claude 会收集上下文、采取行动、检查自己的工作；如果需要，它会继续重复；最后再回复你。

Claude Code 团队把这个过程称为 agentic loop。

举个例子，你让 Claude 创建一个点赞按钮。

它会读取代码、做出修改、运行测试，然后把它认为可用的结果交回来。

接着，你会手动检查这份工作，再写下一个提示词。

你可以把自己的手动检查步骤写进 SKILL.md，从而增强验证环节。这样 Claude 就能更完整地检查自己的工作，甚至端到端验证结果。

这个 skill 应该包含工具或 connector，让 Claude 能看到结果、测量结果，或者直接与结果交互。检查越量化，Claude 越容易自我验证。

比如，你可以在 SKILL.md 里这样写：

...markdown

\---

name:　verify-frontend-change

description:　Verify　any　UI　change　end-to-end　before　declaring　it　done.

\---

#　Verifying　frontend　changes

Never　report　a　UI　change　as　complete　based　on　a　successful　edit　alone.　Verify　it　the　way　a　human　reviewer　would:

1.　Start　the　dev　server　and　open　the　edited　page　in　the　browser.

2.　Interact　with　the　change　directly.　For　a　new　control　(button,　input,　toggle):　click　it,　confirm　the　expected　state　change,　and　screenshot　before/after.

3.　Check　the　browser　console:　zero　new　errors　or　warnings.

4.　Use　the　Chrome　Devtools　MCP,　run　a　performance　trace　and　audit　Core　Web　Vitals.

If　any　step　fails,　fix　the　issue　and　rerun　from　step　1　—　do　not　hand　back　partially　verified　work.

这段例子的重点很明确：不要把“代码改了”当成“任务完成”。前端变化必须启动页面、实际点击、检查状态、看控制台、跑性能检查。

04

GOALBASED LOOP

### Goal-based loop：把“完成”的定义交给系统

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HR8kIomiaALS1seeH3P5Sd5Ah1u7oKlGurUnklyXpmvpkXPSt1cqBDZI30R12cAK041g0wWTNnB8ZY8ickGWwDk9bGIuhA2eHQNKp96LhpjuU/640?from=appmsg)

— Goal-based loop

• 触发方式：实时发出一次手动提示。

• 停止条件：目标达成，或者达到最大轮次。

• 最适合：有明确、可验证退出条件的任务。

• 管理使用量：设定具体完成标准和明确轮次上限，例如“最多尝试 5 次”。

有些任务单轮很难完成，尤其是更复杂的任务。

agent 在能够迭代时，往往表现更好。

你可以通过 /goal 定义“完成”长什么样，让 Claude 继续迭代更长时间。

当你定义成功标准以后，Claude 就不需要自己判断什么叫“足够好”，也不容易过早结束 loop。

每当 Claude 试图停止时，一个 evaluator model 会检查你设置的条件。

如果条件还没满足，它会把 Claude 送回去继续工作，直到目标达成，或者达到你定义的轮次上限。

这也是为什么确定性标准特别有效，比如测试通过数量，或者某个分数达到阈值。

例如：

...bash

/goal　get　the　homepage　Lighthouse　score　to　90　or　above,　stop　after　5　tries.

这条命令的关键不在于“优化首页”，而在于它定义了非常清楚的出口：Lighthouse 分数达到 90 以上，最多尝试 5 次。

05

TIMEBASED LOOP AGE

### Time-based loop：让 agent 按时间间隔重复工作

• 触发方式：指定的时间间隔。

• 停止条件：你取消它，或者工作完成，例如 PR 合并、队列清空。

• 最适合：重复性工作，或者需要和外部环境、外部系统交互的任务。

• 管理使用量：设置更长时间间隔，或者尽量基于事件响应，而非高频轮询。

有些 agent 工作是重复发生的：任务本身相同，只是输入不断变化。

比如每天早上总结 Slack 消息。

还有一些工作依赖外部系统。一个简单的做法，是按固定时间间隔检查系统状态，并根据变化作出反应。

比如，一个 PR 可能收到代码评审，也可能 CI 失败。

这些场景可以用 /loop 来触发 Claude 定期运行。比如：

...bash

/loop　5m　check　my　PR,　address　review　comments,　and　fix　failing　CI

/loop 运行在你的电脑上，所以如果电脑关掉，它也会停止。

如果想把 loop 移到云端，可以用 /schedule 创建 routine。

06

PROACTIVE LOOP

### Proactive loop：把固定流程组合成长期运行的系统

![](https://mmbiz.qpic.cn/mmbiz_jpg/HR8kIomiaALSJPqM5RroWBWk7zzHwgd0mBREd9dK7iaae4KXy9OdNwicyfRoq4L41IjP2icbPIDuBGKgBzHVV583ryg1qXTF0hPPldIucKYicZRI/640?from=appmsg)

— Proactive loop

• 触发方式：事件或日程触发，不需要人在实时参与。

• 停止条件：每个任务在目标达成时退出；routine 本身会一直运行，直到你关闭它。

• 最适合：持续流入、定义清楚的重复工作，例如 bug report、issue triage、迁移、依赖升级等。

• 管理使用量：把 routine 路由给更小、更快的模型，把最强模型留给需要判断的环节。

前面这些 primitive，加上 Claude Code 的其他功能，例如 auto mode 和 dynamic workflows，可以组合成一个用于长期工作的 loop。

例如，要处理不断进入的用户反馈，可以这样组合：

• 使用 /schedule 定期运行 routine，检查新的 report；

• 使用 /goal 定义什么叫完成，并用 skills 记录如何验证；

• 使用 dynamic workflows 编排多个 agent，分别 triage 每个 report、修复问题、评审修复；

• 使用 auto mode，让 routine 运行时不需要每一步都停下来请求许可。

组合起来，一个 prompt 可能长这样：

...bash

/schedule　every　hour:　check　the　project-feedback　channel　for　bug　reports.　/goal:　don't　stop　until　every　report　found　this　run　is　triaged,　actioned,　and　responded　to.　When　fixing　a　bug,　use　a　workflow　to　explore　three　solutions　in　parallel　worktrees　and　have　a　judge　adversarially　review　them.

这类 proactive loop 的本质，是把 agent 从“你问我答”的助手，推进到“按固定规则处理输入流”的系统。

07

SECTION

### 怎样维持代码质量

loop 输出质量取决于它周围的系统。

在设计系统时，需要关注几件事。

• 保持代码库本身干净。Claude 会遵循代码库里已经存在的模式和约定。

• 给 Claude 一套自我验证的方法。用 skills 写清楚你和团队认为什么叫好。

• 让文档容易触达。框架和库的文档通常包含最新最佳实践。

• 使用第二个 agent 做 code review。带着新上下文的 reviewer 更不容易受主 agent 推理过程影响。你可以使用内置的 /code-review skill，或者 GitHub 的 Code Review。

当某次结果不达标时，不要只修复这个单点问题。

更好的做法，是把这次失败编码进系统，让未来所有迭代都受益。

这其实就是 agent 工程里最重要的一条经验： **不要只修提示词，要修系统。**

08

TOKEN

### 怎样管理 token 使用量

要管理 token 使用量，loop 必须有清楚边界。

• 为任务选择合适的 primitive 和模型。小任务不需要多个 agent 或复杂 loop，有些任务可以用更便宜、更快的模型。

• 定义清楚的成功条件和停止条件。具体说明什么叫完成，能让 Claude 更快抵达解法，同时避免过早停止。

• 大规模运行前先小范围试跑。Dynamic workflows 可能启动数百个 agent，应该先用较小任务切片估算使用量。

• 对确定性工作使用脚本。运行脚本比让模型推理每一步更便宜。例如，一个 PDF skill 可以自带填表脚本，让 Claude 每次直接运行，而不是重新推导代码。

• 不要让 routine 运行得过于频繁。间隔应该匹配被观察对象的变化频率。

• 定期检查使用量。/usage 会按 skills、subagents 和 MCPs 拆解最近使用情况；不带参数的 /goal 会展示当前轮次和 token 用量；/workflows 会展示每个 agent 的 token 用量，并且你可以随时停止某个 agent。

09

SECTION

### 怎样开始

总结一下：

• Turn-based loop：你交出去的是检查动作。适合探索或决策阶段。优先使用自定义验证 skills。

• Goal-based loop：你交出去的是停止条件。适合你明确知道什么叫完成的任务。优先使用 /goal。

• Time-based loop：你交出去的是触发机制。适合发生在项目外部、按时间或系统状态变化推进的工作。优先使用 /loop 和 /schedule。

• Proactive loop：你交出去的是完整 prompt 和运行规则。适合重复发生、定义清楚的工作流。需要综合使用前面所有能力，以及 dynamic workflows。

如果想开始使用 loop，可以先回看你已经在做的工作。

找一个你自己总是成为瓶颈的任务，然后问三个问题：

• 哪一部分检查可以交给 agent？

• 目标是否已经清楚到可以被验证？

• 这件事是否按某种日程或输入流反复发生？

有了初步想法以后，先运行一个 loop，观察它在哪里卡住、在哪里越界，然后继续迭代。

更多信息可以阅读 Claude Code 文档中关于 parallel agents、loop、schedule、goal 和 dynamic workflows 的页面。

这篇文章由 @delba\_oliveira 撰写。

END

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过