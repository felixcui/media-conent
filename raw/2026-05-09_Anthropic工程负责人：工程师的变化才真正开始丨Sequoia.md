# Anthropic 工程负责人：工程师的变化才真正开始丨Sequoia

**来源**: https://waytoagi.feishu.cn/wiki/JbDxwmNVKioHl3kl7EocfuqZnwc

---

## 摘要

Anthropic工程负责人及Claude Code创建者Boris表示，自己今年未亲手写代码且单日可处理150个PR，揭示了工程师工作形态的剧变。Claude Code诞生于模型能力未被产品接住的时期，历经半年失败后随模型能力追上而成功。Boris指出，AI编程工具的成功是模型与产品体验的结合，但随着模型对齐能力增强，当前依赖权限和提示词构建的安全外壳将变轻，护城河不能仅靠wrapper。

---

## 正文

> 🔗 原文链接： [https://mp.weixin.qq.com/s/wQK0nR07...](https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FwQK0nR077ApwCL9-vVy01w)
原创 Capihom Capihom 晚点再听LaterCast*2026年5月8日 20:56  北京*
我们每天为你更新硅谷最新的 AI 创业与科技播客总结，让你与前沿保持同频。 全文约 3900 字，如果你现在没有时间，试试转成播客稍后再听
<text bgcolor="light-yellow">*"我今年还没有写过一行代码。" *</text> {align="center"}
<text bgcolor="light-yellow">*"上周有一天，我一天做了 150 个 PR。" *</text> {align="center"}
<text bgcolor="light-yellow">*"我觉得 loop 是未来。"*</text> {align="center"}
Boris 是 Claude Code 的创建者，也是一位很典型的“工程师的工程师”：他写过 TypeScript 教材，早年甚至给 TI-83 Plus 计算器写过 BASIC 指南。可在这场对话里，最刺耳的一句来自主持人的介绍：Boris 今年到目前为止没有亲手写过一行代码。对习惯把编码能力当作职业护城河的工程师来说，这期比工具测评更重，它讨论的是软件开发工作形态的提前变化。
## <text bgcolor="light-yellow">Claude Code 起点是产品过剩</text> {align="center"}
Boris 回忆，Claude Code 最早诞生在 Anthropic Labs，一个内部孵化团队。这个小团队后来做出了 Claude Code、MCP 和桌面应用，完成任务后曾经解散，现在又由 Anthropic 首席产品官 Mike Krieger 重新组织起来。Boris 说，当时他们看到的是“product overhang”：模型已经能做很多事，市面上的产品还没有把能力接住。2024 年底，AI 编程的主流体验仍然停留在 IDE 里按 Tab，一次补一行代码。Sonnet 3.5 让 typeahead 变得可用，但 Boris 觉得还能往前走一步，让 Agent 直接写完整代码。
<text color="gray">*"模型能做所有这些事，只是还没有产品把它捕捉下来。"*</text>
最早的 Claude Code 并不顺。Boris 说，前 6 个月它几乎不好用，他可能只用它写 10% 的代码。即便初版发布，也没有立刻爆掉。转折来自模型逐步追上产品想象力。对做 AI 产品的人，这段经历很有参考价值：产品有时会先于模型成熟，早期体验糟糕并不等于方向错了。团队要判断的是，模型曲线会不会在未来几个月追上来。
## <text bgcolor="light-yellow">六个月失败之后，模型追上来了</text> {align="center"}
主持人问他，Claude Code 的成功到底来自模型，还是来自产品决策。Boris 的答案是混合的：如果在 6 个月前问，他会说大概 50/50。他的创业经验来自 YC，也记得 YC 反复强调的那句话：build something people love。模型再强，最后仍然要做出人愿意整天使用的东西，所以 Claude Code 团队会抠很多小细节，让工具在全天使用时有好体验。可随着模型变强，harness 的重要性会下降，今天用来防 prompt injection、静态验证命令、权限模式和 human-in-the-loop 的很多机制，未来会变轻。
<text color="gray">*"你最终还是要做出人们热爱的东西。"*</text>
他甚至给了一个很激进的预测：一年以后，模型会更好地对齐，很多今天围绕安全和权限搭出来的外壳会变得没那么重。对开发工具公司来说，这意味着护城河不能只押在 prompt 和 wrapper 上。随着模型本体把更多正确行为内化，产品需要继续寻找新的一层：如何运行更多 Agent，如何让 loop 成为一等能力，如何让多人团队共享上下文。
现场有人追问，两年后模型和产品各占多少。Boris 没有给确定比例，只说他们现在按一周规划，而不是按几年规划。这个细节很真实：AI 产品的路线图已经短到以周为单位。今天花很多工程力做出的权限、验证和提示词结构，几个月后可能被新模型能力吃掉。产品团队要接受这种不稳定，把迭代节奏调到足够快。
## <text bgcolor="light-yellow">手机上同时跑几百个 Agent</text> {align="center"}
Boris 的个人工作流是全场最有冲击力的部分。他说，自己现在大部分工作都在手机上做。打开 Claude app，左侧有一个 code tab，他会同时开 5 到 10 个 session；每个 session 里又有一堆 agents，所以当前可能有几百个 Agent 在跑。夜里，他通常会让几千个 Agent 做更深的工作。主持人问他具体设置时，Boris 拿出手机展示，台下很多人其实看不清，但数字已经足够说明问题：他已经不把编程当作坐在电脑前敲键盘的连续动作。
<text color="gray">*"我通常有 5 到 10 个 session，里面可能有几百个 Agent 在跑。"*</text>
他还给了一个产出数字：上周有一天，他做了 150 个 PR，只是想看看自己能推到多远。他补充说，这在他的代码范围里已经“solved”，但并非所有地方都一样。大型复杂代码库、模型不擅长的语言、怪异工具链，仍然会卡住。Boris 的经验提供了一个极端样本：当任务能被拆小、上下文清楚、验证闭环完整，人的角色会从写每一行代码，转向组织一大批 Agent 干活。
## <text bgcolor="light-yellow">Loop 把 PR 和 CI 交给后台</text> {align="center"}
Boris 最推荐的功能叫 loop，本质上是让 Claude 用 cron 设一个未来任务，而且可以重复运行。任务可以每分钟、每 5 分钟、每天跑一次。他现在有几十个 loop 在同时运行：一个照看 PR，自动修 CI、自动 rebase；一个保持 CI 健康，碰到 flaky test 就处理；另一个每 30 分钟抓 Twitter 反馈并聚类。Claude Code 还推出了 routines，把类似能力放到服务器上，即使合上电脑，任务也会继续跑。
<text color="gray">*"我有一个 loop 在照看 PR，修 CI，自动 rebase。"*</text>
这段对团队管理者尤其有用。很多工程工作并不需要创造性突破，只是需要有人持续盯着：CI 红了、依赖过期、测试 flaky、反馈散落在社交平台、数据查询不断变化。以前这些事靠值班、脚本或 PM 催促；loop 让 Agent 变成一个会定时回来汇报和修复的后台同事。Boris 说，他感觉 loop 是未来。真正改变工作密度的，可能是后台持续推进，而不只是一次性生成代码。
观众还问到并行化：什么时候应该让模型自己开 10 个 sub-agent，而不是靠人类判断哪些任务能并行。Boris 说，产品层面现在主要靠 prompting，但模型变强以后会自然做这件事。4.7 已经会在数据随时间变化时主动开 loop，并询问是否通过 Slack MCP 发报告。多 Agent 不会永远停留在手动编排阶段，模型会越来越主动地拆任务、排队列、找回报路径。
## <text bgcolor="light-yellow">团队会长出跨学科通才</text> {align="center"}
谈到未来团队，Boris 的判断是会出现更多 generalists。今天人们说 generalist，常常指工程内部的通才：能写 iOS、web、server。Boris 看到的变化更大：跨学科通才会变多。工程师会懂产品、设计和数据；设计师、PM、数据科学家、财务、用户研究员也都会写代码。他说 Claude Code 团队已经这样运转：团队里每个人都写代码，包括工程经理、产品经理、设计师、数据科学家、财务和用户研究员。
<text color="gray">*"我们团队里的每个人都写代码，工程经理、产品经理、设计师、数据科学家、财务、用户研究员，全都写。"*</text>
这不是说每个人都变成传统意义上的工程师。更准确的变化是，代码从专业边界变成表达手段。产品经理能直接改原型，设计师能直接实现交互动效，数据科学家能改后台查询，研究员能把访谈反馈聚类成内部工具。团队里的专长还在，只是“能把想法变成可运行软件”的门槛降了很多。
## <text bgcolor="light-yellow">大公司要先改流程</text> {align="center"}
Boris 也谈到创业公司的机会。他认为很多大公司会受到冲击，因为它们不只是换一套工具，还要改变业务流程、工作方式，重新训练所有人使用技术，还会遇到内部阻力。新公司没有这些负担，可以从第一天就按 AI native 的方式搭组织。Sequoia 场子里坐着很多 builder，Boris 直接说，这是最适合创业的时间，因为大量 disruption 正在到来。
<text color="gray">*"如果你从零开始，就可以从底层按 AI native 的方式构建。"*</text>
这段也解释了为什么 AI 工具会让组织差距变大。技术本身会普及，模型和平台也会开放给外部开发者使用。Anthropic 自己 dogfood 的东西，也会尽量放给开发者。真正拉开距离的地方，可能是组织结构和流程：谁能把 PR、CI、反馈、数据、设计和发布拆成 Agent 能处理的任务；谁还把 AI 当成单人提效插件。
他还提到一点：Anthropic 的技术领先未必来自“别人拿不到的模型”。Claude Code 本身是平台，开发者能用到和 Anthropic 内部相同的技术。更大的差别在组织流程。一个团队如果仍然把代码审查、CI、发布、客户反馈都放在老流程里，Agent 很难释放全部能力。一个新团队从第一天就按多 Agent 协作设计工作流，速度会完全不同。
## <text bgcolor="light-yellow">印刷机是他给软件的类比</text> {align="center"}
有观众问，软件构建会不会变成像 Microsoft Office 一样人人会用的技能。Boris 的回答更夸张：会更像“会发短信”那样普遍。他给出的历史类比是 15 世纪欧洲的印刷机。印刷机出现前，欧洲大约 10% 的人识字，读写是专门职业；印刷机出现后，50 年内出版的文献超过此前 1000 年，书的成本下降约 100 倍。软件在他眼里也会经历类似变化：原来写软件是少数人的专业能力，Agent 会把“生成软件”的成本打下来。
<text color="gray">*"印刷机出现后，50 年里欧洲出版的文献超过了此前 1000 年。"*</text>
这个类比最有意思的地方在于，印刷机没有让写作消失，反而让文字的生产和传播规模暴涨。Boris 对软件的判断也类似：当更多人能表达需求、创建工具、修改工作流，软件数量会变多，形式会变碎，很多本来不值得排期的小工具都会被做出来。工程师的稀缺性会从“会不会写”迁移到“能不能定义正确问题、组织 Agent、建立验证标准”。
现场提问者把这件事类比成 Microsoft Office，问未来会不会人人都会构建软件。Boris 直接说会超过 Office，更接近“会发短信”。这个比喻很准确：Office 仍然是工具技能，发短信则是日常表达。软件如果变成日常表达，很多公司内部的小问题不会再等待工程排期，业务人员会直接生成能跑的工具，再交给工程团队治理和扩展。
## <text bgcolor="light-yellow">MCP 让知识工作接上工具</text> {align="center"}
最后几个问题把话题从代码拉到知识工作。有观众问，Claude Code 的成功部分来自开发者工具和工作流都在本地；知识工作常在 Salesforce、Google Docs、Calendar 这类云工具里，Co-work 要怎样获得足够访问权限。Boris 的回答很简单：MCP。用户在 Claude AI 里接上的 MCP connector，比如 Salesforce、Google Docs、Google Calendar，Co-work、Claude CLI、Claude Code 都可以使用。对没有 MCP 的系统，computer use 就会成为补位能力。
<text color="gray">*"对我们来说，最简单的答案就是 MCP。"*</text>
他还预测，本地模型还是云端模型、MCP 还是 API，几年后可能都不由工程师直接决定。模型会自己选择工具、启动 Agent、搭环境，必要时用本地模型，必要时用云端能力。对使用者来说，重要的是把目标、约束和验证讲清楚。工具选择会被模型消化成人看不见的执行细节。
Boris 还点名了几个会继续变强的方向：Claude Design、loop、batch、海量并行 Agent，以及 computer use。Claude Design 今天已经不错，未来会更强；Claude Code 也会在接下来几周继续落地新东西。换句话说，今天看起来还笨重的环节，可能正处在“模型快要追上产品”的前夜。
## <text bgcolor="light-yellow">写在最后</text> {align="center"}
Boris 的表达很激进，但落点很具体：先别急着讨论工程师会不会消失，先检查自己的工作能否被拆成 Agent 可执行、可验证、可循环的任务。谁能更早学会编排、验收和持续运行 Agent，谁就更可能站在下一轮软件生产方式的前面。今天先改一条 CI、一个反馈流、一个定时报告，就已经开始练这项能力，也会更早看见团队瓶颈和新机会，从小处开始即可，先跑起来。

内容来源："Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next"丨Sequoia Capital
原视频：https://www.youtube.com/watch?v=SlGRN8jh2RI

<text bgcolor="light-yellow">**如果你喜欢深度好文，试试用小程序将不方便立刻阅读的文章转成播客，用「听」的方式，稍后阅读，不再错过好文章⇣**</text> {align="center"}

<text bgcolor="light-yellow">**⇣ 关注我，每天为你更新硅谷最新的 AI 创业／科技播客总结，让你与前沿保持同频 ⇣**</text> {align="center"}