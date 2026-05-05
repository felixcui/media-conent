# 这11个小技巧，GPT-5.5和Claude 4.7的Token 烧得更值 | 附官方指南

**作者**: 发现明日产品的

**来源**: https://mp.weixin.qq.com/s/vTC3KqRFjDdAD8IMQiYUUQ

---

## 摘要

新模型GPT-5.5和Claude 4.7发布后常被误以为降智，实际上是因为模型变聪明了，而用户仍沿用旧版手把手式的提示词。根据官方指南，旧提示词过度指定流程，在新模型上会增加噪音并限制其判断力。新模型不再需要被当作笨学生引导，而是需要更精简或更明确的指令来发挥真实能力，因此用户必须转变提示词策略才能让新模型发挥最大价值。

---

## 正文

在小说阅读器读本章

去阅读

新模型发布之后，除了发现能力变强。大部分人还是会觉得新版本的模型，好像不如旧版听话，第一反应就是降智了。

实际情况可能恰好相反。

OpenAI 和 Anthropic 几乎在同一时间发布自己的提示词文档，在 OpenAI 官网，从 GPT-4.1 到 GPT 5.5，每次新模型发布都有一份完整的提示词指南，告诉我们怎么用新的模型。

![](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfLRTpJia3tmQQFkqhm3a2AYdxqQdH1ycib6UrY1yHfOdzwlb8iaDYuCnXfjLppSBzhDiaJYpc2LVicy3ibpQSHD1rKhmpSOHOAcEmcFo/640?wx_fmt=png&from=appmsg)

链接：https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5

Anthropic 同样在每次模型发布之后，会提供一份迁移指南说明，详细说明新模型的，破坏性变化、行为变化等内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfLu70nS1PQwf7WKiaLNFOzWk5YeyINJxOEnoyDqjtRnHCpU9dNAD51ITsb8OiaBXMiaGibPRslpjBsAAnHvA0ynrMib1qDKQJNeYzkk/640?wx_fmt=png&from=appmsg)

链接：https://platform.claude.com/docs/en/about-claude/models/migration-guide

这两份文档核心信息都是在说： **我们沿用旧提示词的方式，在新模型上会出问题。**

模型没有退步，是因为模型变聪明了，但我们的提示词方式还停留在训练「笨学生」的阶段。

这次我们不谈上下文工程、Skill 工程、Harness 工程，回到日常生活中用的最多的提示词，大概是 AI 使用门槛上最有用的一份指南。

1

**旧的提示词，是给已经在坟墓的模型写的**

在 GPT-4o 和 Claude 3 的时代，一个好的提示词往往很长，要一步一步告诉模型先做什么、再做什么、最后输出什么格式。这套方法有效，因为那时候的模型确实需要这种手把手的引导。

![](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfIzGowR4oelKqBicibyGcdeT2P1EibTSFUgusMeT6uumJXPxEpM9vLzhg9HFYZwWvfiaiaKFjOpWzVlvhJ3bJXbZviaXnMm0FVkSEwp0/640?wx_fmt=png&from=appmsg)

在 GPT-5.5 的官方提示词指南里，OpenAI 非常直接地表示。

**旧提示词经常过度指定流程，因为早期模型需要更多帮助才能保持在轨道上。对 GPT-5.5 来说，这会增加噪音，缩窄模型的搜索空间，或者导致答案过于机械。**

翻译成人话：我们一步步手把手写的那套提示词，在新模型眼里就像在对一个本科毕业生说「先打开电脑，再打开 Word，再找到正文区域，再开始输入……」。

对方当然能执行，但直接把他限死了，他用不上自己的判断力。

不同的模型，还有不同的提示词更新方向。

![](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfIozeyZ99tdc5nrNBmm3QuM1n7ZgUL2EgzqWUg2ib6a2ZCh4N76rE1m1diavLojnD4UQ9WKVj9RWJULqJ3pgZI1EdKbmx0qMamBk/640?wx_fmt=png&from=appmsg)

Claude 那边是反其道而行之，Anthropic 提到， **Claude Opus 4.7 比 Claude Opus 4.6 更字面和明确地解释提示，特别是在较低的工作量级别。**

我们说什么，它就做什么，不再自动帮我们脑补「可能还想要」的部分。

这种字面性的优点是精确性和更少的混乱。官方也提到它通常对具有精心调整的提示词、结构化提取和我们想要可预测行为的用法表现更好。

但 Opus 4.7 的这项变化，对很多人来说也是个坏消息，因为不是每个人都能写出完整的、明确的提示词，大多数时候还是依赖模型「猜」我们的意图。

![](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfJQ1RBTtqBfYaibjcEx8vjBWhJKzp8dp3fZRAGA6Nqfb3HZQeABZNFxU6B1cboxjJYzcqwsStm09RPhlGribQUQUrY6ofdial0YvM/640?wx_fmt=png&from=appmsg)

文章链接：https://x.com/Aina\\\_Ai2/status/2049490182211301527

**很多在 Opus 4.6 中行之有效的模糊指令，现在放到 Opus 4.7，让它回答，反而会降智般地，得到一些狭隘、死板，甚至更不相关的结果。**

1

**需要结果，还是流程**

无论是 GPT-5.5 要求不要太详细的结果，还是 Opus 4.7 希望更明确的指令，核心都可以被压缩成：描述我们想要的结果，而不是你希望模型走的流程。

GPT-5.5 指南给了一个对比。旧式写法是这样的：

先检查 A，再检查 B，然后对比每个字段，然后想清楚所有例外情况，然后决定调用哪个工具，然后调用工具，然后向用户解释整个过程。

新的写法是这样的：

端到端解决用户的问题。成功标准：资格决定要从现有的政策和账户数据中得出；所有允许的行动在回复之前完成；最终答案包含已完成的行动、用户消息和阻塞项；如果证据缺失，询问最小的缺失字段。

这两种写法的区别，旧写法在规定「怎么走」，新写法在规定「走到哪里算完」。前者更像是在给初级员工写 SOP，后者像在给高级员工定 KPI。

而这个切换对普通用户的实际含义是： **我们现在需要比以前更清楚地想明白自己要什么。模型可以帮你执行，但它越来越不会替你想清楚目标。**

1

**三件最值得马上改的事**

**删掉提示词里多余的「必须」「永远」「只能」。**

这些强制性词语曾经有用，是因为旧模型需要明确约束才不会「跑偏」。

新模型更善于理解我们的真实意图，但过多的绝对规则会让它在本该灵活判断的地方也变得僵硬。

OpenAI 的建议是：把「绝对规则」留给真正不能变通的情况，其他地方改成「决策规则」，例如说明在什么条件下做 A，在什么条件下做 B。

**明确说「什么情况下停」。**

这是新模型经常被忽视的一个设计点。旧模型需要你告诉它「做这些事情」，新模型需要你同时告诉它「做到什么算结束」。

GPT-5.5 指南里专门列出了「停止条件」的写法：每一步之后，模型会问自己「我现在能回答用户的核心问题了吗？」如果没有明确的停止规则，它可能停得太早，也可能一直搜索找证据。

**如果之前用 Claude，现在要重新审视提示词语气。**

Opus 4.7 变得「更直接、更有主见」，减少了原来版本里偏向「温暖确认型」的表达风格。

如果我们的提示词里包含某种隐含的「期待模型客气回应」的设计，它可能会失效。同时，Opus 4.7 不再自动给你跨条目泛化，我们告诉 Opus 4.7 处理 A，它不会默默顺手处理同类的 B。

我们需要显式说清楚覆盖范围。

1

**「个性化」现在需要自己定义**

GPT-5.5 的文档里有一个章节专门讲「人格」，核心逻辑是，新模型的默认风格是高效、直接、任务导向的。

这对效率来说是好事，但如果我们希望 AI 的回答有一种特定的质感，比如更暖、更有探索性、更愿意主动问问题。我们现在需要显式写出来，而不是依赖模型通过学习「自然而然地」呈现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfLy40zvicHH6sicMmCiaicN3aE18oialuicMKw3fg8r4x7H5iamA8sXwswK2ia0ibrQKgmJAr53Oe5ydIsiafL3oJ4cdgQ1sssfP34rqC7lU/640?wx_fmt=png&from=appmsg)

文档里给出了两种典型的「人格设定」模板：一种是「稳定、任务导向」的协作者风格，适合效率场景；另一种是「有主见、好奇心强、对话感强」的探索型风格，适合创作和思考类任务。

一个性格缺陷明显的、做事稳健的助理：

You are a capable collaborator: approachable, steady, and direct. Assume the user is competent and acting in good faith, and respond with patience, respect, and practical helpfulness.

Prefer making progress over stopping for clarification when the request is already clear enough to attempt. Use context and reasonable assumptions to move forward. Ask for clarification only when the missing information would materially change the answer or create meaningful risk, and keep any question narrow.

Stay concise without becoming curt. Give enough context for the user to understand and trust the answer, then stop. Use examples, comparisons, or simple analogies when they make the point easier to grasp. When correcting the user or disagreeing, be candid but constructive. When an error is pointed out, acknowledge it plainly and focus on fixing it.

Match the user's tone within professional bounds. Avoid emojis and profanity by default, unless the user explicitly asks for that style or has clearly established it as appropriate for the conversation.

一个善于表达、乐于合作的助理的性格特征示例：

Adopt a vivid conversational presence: intelligent, curious, playful when appropriate, and attentive to the user's thinking. Ask good questions when the problem is blurry, then become decisive once there is enough context.

Be warm, collaborative, and polished. Conversation should feel easy and alive, but not chatty for its own sake. Offer a real point of view rather than merely mirroring the user, while staying responsive to their goals and constraints.

Be thoughtful and grounded when the task calls for synthesis or advice. State a clear recommendation when you have enough context, explain important tradeoffs, and name uncertainty without becoming evasive.

**很明显，现在和 AI 打交道，越来越像是在管理一个有能力，但需要明确方向的协作者，而不是在操作一个等待命令的工具。**

我们给的指令越模糊，结果越不可控；给的指令越精准，它能发挥的空间也越大，但要注意是精准的结果，而不是详细的过程。

总结一下，如果你正在使用 GPT-5.5，下面这六条小 Tips 会非常有用。

![](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfITdvorFZmBoibyGRy3RB8RYewlxJol6cC4OhdJ7voamh3CvWIojX2WXLhyjKME2IWKYwoY9PYksdU9Pt7Oxke6t2CM48pC0uqA/640?wx_fmt=png&from=appmsg)

1.

用结果定义任务，不用步骤定义任务。不要写「先做 A，再做 B，然后 C」，写「完成标准是：X 已完成，Y 已包含，Z 不存在」。

2.

谨慎使用绝对词 「ALWAYS / NEVER / 必须 / 只能」。留给安全规则和必填字段。其他地方改成条件句：「如果……则……，否则……」，绝对词的滥用会让模型在本该判断的地方也变僵。

3.

给搜索加预算上限。不加限制，模型会一直搜到「更好」为止。明确写出「以下情况才发起第二次检索：核心问题没有答案、缺少必要参数、用户明确要求全面覆盖」，其他情况，有足够证据就回答。

4.

多步任务先给一句可见的进度更新。用户等待时什么都看不到，体验差。只需要在系统提示里加一条：「多步任务开始前，先用一两句话告诉用户你在做什么」，感知响应速度会明显提升。

5.

格式指令要说「为什么」，不只说「怎么做」。「用短段落，不用列表」是指令。「这是一份给高管的简报，阅读时间 2 分钟，结论优先，省去推导过程」才是让模型真正理解格式意图的写法。

6.

推荐的提示词骨架。从以前松散的长指令变成了固定结构：角色 Role → 性格 Personality → 目标 Goal → 成功标准 Success criteria → 限制条件 Constraints → 输出 Output → 停止规则Stop rules，每个模块尽量短，只写真正改变行为的内容。

如果是 Opus 4.7 的话，可以参考这五条 Tips。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfJmH5Hsq1dfTthrT1f17XDpVfl1Lx8JgYgqEfBo7VVticf591ZIHqgubNQc5s5vA7TAgbU0GQAsbDPRyhJwQiciaxKyhAOyL0iaInc/640?wx_fmt=png&from=appmsg)

1.

模型不再替你泛化，覆盖范围必须显式写清楚。Opus 4.6 遇到任务 A，会顺手帮你把同类的 B 也处理了；但 4.7 绝对不会。如果任务涉及多个同类项，必须逐一说明，或者明确写明「请对所有同类情况执行相同处理」。

2.

低 effort 下它只做你说的，不做你想的。在low 和 medium 模式下，模型严格按字面执行，不会主动扩展。如果任务涉及多步推理，在提示词里加一句「这个问题需要分步思考，请在回答前理清逻辑」，比调高 effort 更省成本。

3.

它的默认风格变直接了，「温暖感」要显式定义。4.7 的语气比 4.6 更干、更有主见，减少了确认型的铺垫。如果你的产品需要特定语气，更暖、更有探索性、更愿意反问，要在系统提示里写出来，不能靠模型默认呈现。

4.

内置进度更新，不用再强制要求。之前很多 agent 提示词里会写「每调用 3 次工具后总结一次进度」，4.7 已经内置了这个行为。

5.

图片分辨率上去了，token 也跟着涨了。4.7 支持最高 2576px 长边，每张图最多消耗约 4784 tokens，是旧版上限的 3 倍。如果你的工作流要批量处理图片，发送前可以先做压缩，否则成本会在翻倍。

好了，现在 AI 的瓶颈又回到了写提示词的人，而不是模型。

文章转载于APPSO，欢迎点击下方卡片关注。

继续滑动看下一个

硅星人Pro

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过