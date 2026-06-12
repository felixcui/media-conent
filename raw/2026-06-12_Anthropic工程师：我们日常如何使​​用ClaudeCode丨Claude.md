# Anthropic工程师：我们日常如何使​​用Claude Code丨Claude

**作者**: Capihom

**来源**: https://mp.weixin.qq.com/s/tTTprDfCq75h9sC2kaj1vQ?nwr_flag=1#wechat_redirect

---

## 摘要

Anthropic工程师Arno分享了日常使用Claude Code的高阶工作流，强调模型变强后需改变习惯，通过前置方向与验证机制避免长任务跑偏浪费token。其实践分三步：一是拒绝过早硬编码，让Claude通过交互式追问采访用户以提取真实需求；二是用HTML文件替代冗长Markdown作为规格稿，便于人机共同理解与校验；三是将验证框架直接嵌入产物中。

---

## 正文

Capihom Capihom

在小说阅读器读本章

去阅读

我们每天为你更新硅谷最新的 AI 创业与科技播客总结，让你与前沿保持同频。全文约 3900 字，如果你现在没有时间，试试转成播客稍后再听 晚点再听LaterCast

"模型越强，你越应该少约束它。"

"Agent 跑得越久，走错时烧掉的 token 越多。"

"目标是把验证嵌进产物本身。"

这期主讲人 Arno 是 Anthropic Applied AI 团队的架构师，他带来的是一场可跟做的 workshop：用一个真实 repo 演示 Anthropic 工程师怎样配置 Claude Code，怎样让它问问题、生成 HTML 规格稿、再把验证流程做进 React 组件和浏览器。官方简介里写到的项目上下文文件、custom commands、hooks 和 subagents，落到演示里都指向同一个主题：让 Claude Code 更像工程系统的一部分。它不像一篇“Claude Code 小技巧”合集，更像一份内部工作习惯的公开样本。

配套 repo 分成三个 phase。第一阶段让 Claude 采访人，避免需求一开始就漏掉；第二阶段把需求变成多个 HTML 设计方向，方便人类快速比较；第三阶段把验证框架嵌进一个小型 to-do app。三段连起来看，正好覆盖一次 Agent 开发从想法、规格、实现到验收的完整链路。

## Agent 变强后，工作习惯也要变

Arno 开场先讲为什么要重新设计工作流：模型越来越强，Agent 可以跑更久，也能接更复杂的任务。代价也随之变大。一个短任务跑偏，最多浪费几分钟；一个长任务跑偏，可能烧掉大量 token，还生成一堆难以复盘的中间产物。 **Claude Code 的进阶用法，不在多记几个命令，而在任务开始前把方向、验证和反馈通道布好。**

"如果你让 Agent 跑更长时间，它做错事时会烧掉很多 token。"

这也是他反复强调“改变习惯”的原因。过去写代码时，人可以边想边改；Agent 参与后，前置规格、交互式追问、可验证产物会变得更重要。团队把 Claude Code 放进真实工程，不只是让它改文件，还要让它在更少人类 touchpoint 的情况下知道自己有没有走偏。

这场 workshop 建在 Tarik 一周半前在旧金山讲过的版本之上，核心材料来自那篇《The Unreasonable Effectiveness of HTML files》。Arno 没有把 HTML 当作网页文件来讲，而是当作一种让人和 Agent 同时理解任务的中间产物。越长的 Agent run，越需要在开局就把“它应该怎样被检查”写进材料里。

## 别急着写需求，让 Claude 先采访你

第一层工作流是需求提取。Arno 借 Richard Sutton 的 bitter lesson 讲了一个判断：模型能力越强，人越应该抵抗“提前硬编码一切”的冲动。他认为 Claude 很可能比你更擅长从对话里提取需求。就像用户常常“看到才知道要什么”，产品和工程师也经常无法一次性说清自己想要的系统。

"Claude 可能比你更擅长提取你想要什么、需要什么。"

他现场用一个 bill splitting app 做例子。坏 prompt 是一句“make it better”；好 prompt 会给出领域、受众、开放式问题，并明确让 Claude 使用 ask user question 工具来采访自己。Claude 接着问：这是给朋友用，还是还有第二类用户？需求从一次性说明，变成一轮轮更接近真实产品访谈的收集过程。

Arno 还顺手展示了几项日常设置：fast mode、auto mode、effort 参数。他把 auto mode 说得很直白：如果还没用，就该开始用。effort 上，他推荐 X high，也可以把 effort 拉到 max。它们背后的意思并不玄：需求采访和规格探索需要快速来回，权限弹窗和低推理强度都会打断节奏。

这种采访式 prompt 对 PM 和工程师都很实用。人不用把所有边界一次性说完，只要告诉 Claude 领域、受众和想探索的问题，再让它逐轮追问。Arno 的例子里，分账应用从“给谁用”开始收敛，随后再进入规格稿。长任务开跑前，多花几轮问答，通常比事后返工便宜。

## Markdown 太长时，HTML 规格稿更像产品

第二层工作流是规格稿形态。Arno 引用了同事的一句话：Markdown 文件是 AI-native 软件开发生命周期的通用语。但他也指出，Markdown 一长就开始失效。超过两百行以后，人很难认真读完，同事也很难基于它给出具体反馈。HTML 在这里承担了新角色：它能把更多信息压进一个可看、可点、可截图的产物。

"Markdown 文件是 AI-native 软件开发生命周期的通用语。"

在 demo 里，他让 Claude 为分账应用生成四个 HTML 设计方向，包括 brutalist 和 Tokyo fintech 等不同视觉路线。人不再靠想象阅读需求文档，而是直接点击、比较、截图，再把视觉反馈交回 Claude。对前端、产品和设计协作来说，这种规格稿比一长串文字更容易对齐。

他还问现场有多少人会用截图给 Claude 反馈，随后明确建议大家这么做。前端里的“稍微有点歪”“层级不对”“这里太挤”，很难只靠文字表达。Opus 4.7 的视觉能力比过去更好，把截图和 HTML 规格稿一起交给 Claude，能让反馈从抽象意见变成可定位的改动。

Arno 对 HTML 的定位很清楚：把人原本会在规格阶段做的验证前置进去。它既能被人读，也能被 Agent 使用；既能表达布局和状态，也能承载后续验证入口。Markdown 仍然有价值，但当任务开始涉及界面、状态和视觉反馈，HTML 会让 Claude 少猜很多东西。

## 验证要从事后检查，前移到产物里

视频最有价值的部分，是第三阶段的 verification framework。Arno 特意区分 test 和 verify：普通测试关注代码能否通过，verify 关注产物是否能被人和 Agent 原生检查。演示项目换成一个 React to-do app，里面有组件、fixtures、testing library、data emissions、attributes 和 Playwright MCP。

"让验证原生存在于事物本身，这样 Agent 可以和人一起驱动它。"

Arno 的目标很明确：未来 Agent 会越来越多地自己运行、自己检查、自己提供证据。团队要做的，是把产物设计成可被 Agent 原生验证。 **当验证成为 artifact 的一部分，Claude Code 才能从“会改代码”走向“会证明改动有效”。**

这一步的工程味很重。它不满足于“跑一遍测试”。Arno 要的是在组件旁边写清楚已知状态、数据合同、必须保持的 invariant，以及可以推动边界条件的 probes。Claude Code 接手任务时，看到的不只是源代码，还有一套能告诉它“哪里算对、哪里算错”的验证地图。

## DOM 也可以成为 Agent 的数据合同

在 to-do app 里，组件会把 total、done、active 等状态发布到 DOM。Arno 现场添加、勾选、删除任务，浏览器里的 data verify unit 随之变化。这样一来，Agent 不必艰难地 scrape 页面，也不必猜 React 内部状态；它可以直接读取公开的 DOM contract，再运行验证。

"如果把状态发布出来，就能独立于应用状态运行验证。"

每个组件都有 schemas、fixtures、known states 和 invariants。Arno 还故意放入一个会失败的验证：3 + 4 被硬编码成不等于 10。普通测试矩阵可能仍然通过，但 verification dashboard 会把失败暴露出来。Agent 随后可以用浏览器和 Playwright MCP 查到是哪条 contract 出错。

他还现场做了一个更极端的动作：删掉 to-do app 里的 total stats contract。应用本身还能跑，但一批验证马上失败。这个场景很典型：用户界面看起来没坏，Agent 需要依赖的数据合同却断了。把 contract 显式写出来，才能让 Claude Code 发现“看不见的断裂”。

更妙的是，Arno 演示了“测试通过但验证失败”的情况。运行 bun verify 时，测试矩阵可以通过，因为普通测试没有覆盖那条故意写错的业务验证；浏览器里的 verification dashboard 仍然能抓到 4 + 3 不等于 10 的错误。测试负责代码层安全网，verification 负责产物层可信度。

## 同一套验证，要给人、Agent 和 CI 用

Arno 把验证分成三个表面：人看的 dashboard，Agent 从浏览器里驱动的方式，以及 CI 里 headless 跑的命令。三者围绕同一份 manifest、同一批 probes 和同一组 invariants 工作。人在页面上能看见的失败，Agent 也能读到；CI 可以用 run bun verify 跑完整矩阵。

"可以用人类可读的方式验证，也可以用 Agent-first 的方式验证，还可以 headless 地跑。"

他强调 probes 要能推离 happy path。只验证顺利路径，Agent 很容易给出看似漂亮、实际脆弱的结果。把边界状态、错误状态、状态不一致都做成可运行验证，Claude Code 才能在修改后自己找到问题，而不是等人肉 QA 兜底。

这套设计也解释了为什么 Playwright MCP 在演示里重要。Claude 可以直接从浏览器跑验证、读取 DOM contract、查看失败详情，再回到代码里诊断原因。人类 dashboard 和 Agent-first browser 共享同一种观察方式，减少了“人看到一套、机器看到另一套”的错位。

这也是“agent native”的实际含义：把 manifest、state、schema 和 replay 能力交给 Agent，而不是只让它模仿人眼到处点。人可以在 dashboard 上点 Run all；Agent 可以从浏览器拿到同样的验证清单；CI 可以在命令行里跑同样的矩阵。三条路径互相对齐，排查问题才不会分裂。团队越依赖并行 Agent，越需要这种统一观察面，否则每个任务都会留下不同格式的“口头解释”。

## 证据也要自动留下来

验证只告诉你 pass 或 fail，还不够。Arno 现场演示了 recording：验证步骤可以被录成 clips，打包下载，放到 S3，或者分享给同事。Claude Code 团队现在会记录很多代码变更，尤其是前端变更，用来证明验证确实跑过。这一点很像把“我看过了”变成机器能复现的证据包。

"你可以下载全部 clips，或者单独下载，它们就是证明验证跑过的 bundle。"

对团队协作来说，证据包会改变 code review 的颗粒度。Reviewer 不必只看 diff 和口头说明，可以看到 Agent 怎么跑、哪里失败、怎样修复。 **当 Agent 开始提交越来越多代码，验证记录会成为团队信任它的基础设施。**

Arno 说得很具体：Claude Code 团队会记录很多代码变更，至少前端改动会被纳入这样的节奏。视频里可以看到每段 clip 单独下载，也可以打包下载。它像一份可交付的验收材料，帮团队在高速 shipping 时保留可追溯性。

## 多花一点规格 token，少返工很多轮

最后 Arno 回到一个实际问题：HTML spec 会不会更费 token？他的回答偏向否定。单次生成 HTML 可能更贵，但如果规格更丰富、更好读、更容易截图反馈，长期会减少迭代次数。他也建议用 Opus 4.7 做这类视觉和规格工作，fast mode 用来快速迭代 spec，auto mode 用来减少中途权限打断。

"长期来看，如果 HTML spec 足够好、足够丰富，你会少迭代。"

这期 workshop 的重点，其实是把 Claude Code 当作团队工程系统来对待：先让它问清楚，再让它生成可看的规格稿，最后让产物自己带着可验证的 contract 和证据。会用 Claude Code 的团队，差距会慢慢从“谁更会写 prompt”转向“谁更会设计 Agent 可以工作的环境”。

这对产品、设计和工程共同协作的团队尤其重要。产品要把模糊需求交给 Claude 追问，设计要把视觉方向变成可反馈的 HTML，工程要把可验证状态暴露给浏览器和 CI。Claude Code 介入得越深，协作对象就越不只是代码文件，还包括规格、状态、证据和工作节奏。

官方简介提到的 context files、commands、hooks、subagents，在这条主线里也能找到位置。context files 帮 Agent 理解项目；commands 让常见动作可复用；hooks 把检查和上下文插入时机自动化；subagents 可以承担更专门的诊断和验证。这些能力共同组成一套工程环境，让 Claude Code 有信息、有入口、有检查，也有留下证据的方式。

## 写在最后

“How we Claude Code”的价值，在于展示 Anthropic 如何把 Claude Code 放进工程闭环。下次让 Agent 做长任务前，可以先问三件事：需求有没有被采访清楚，规格能不能被人快速看懂，结果能不能被 Agent 自己验证。先把这三件事补齐，再谈规模化，也别让 Agent 在黑箱里奔跑、独自猜答案。

内容来源："How we Claude Code"丨Claude

原视频：https://www.youtube.com/watch?v=IlqJqcl8ONE

如果你喜欢深度好文，试试用小程序将不方便立刻阅读的文章转成播客，用「听」的方式，稍后阅读，不再错过好文章⇣

⇣ 关注我，每天为你更新硅谷最新的 AI 创业／科技播客总结，让你与前沿保持同频 ⇣

继续滑动看下一个

晚点再听LaterCast

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过