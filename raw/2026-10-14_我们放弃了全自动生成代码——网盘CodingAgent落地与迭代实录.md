# 我们放弃了"全自动生成代码" —— 网盘 Coding Agent 落地与迭代实录

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/ax_eh5s3Z7ROgqj6n_Rvkg

---

## 摘要

网盘团队在将Coding Agent接入真实研发链路后，发现一次性全自动流水线虽能跑通流程却无法保证结果正确，于是转向Agentic Engineering Loop的人机多轮反馈循环模式，通过执行前需求调研与不确定项挂账、执行中分轮验证与全程可观测、人机与工程工具各司其职，来平衡自动化与可控性。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 三石

导读

introduction

"全自动最大的风险，不是它会犯错，而是它错了还在自信地往前跑。"网盘团队在把 Coding Agent 接入真实研发链路后，彻底想明白了这句话：流程能从头跑到尾，不代表跑出来的东西是对的。本文作者复盘了他们从"一次性全自动流水线"转向 **Agentic Engineering Loop** （人机多轮反馈循环）的完整过程——执行前先做需求调研、把不确定项挂账；执行中分轮验证、过程全程可观测；人、Agent 与工程工具各司其职。这不仅是技术方案的迭代，更是对"自动化与可控性如何平衡"的工程思考。

*全文 3693 字，预计阅读时间 4 分钟*

> 从一次性全自动，到人机多轮的 Agentic Engineering Loop，我们为什么要这样改

GEEK TALK

01

流程能跑通，不代表结果是对的

网盘很早就在探索 Coding Agent 怎么融入"需求进、代码出"的研发链路，也搭了一套从需求分析到质量检查的自动化流程。可一旦接上真实的迭代需求，问题就来了：流程能从头跑到尾，不代表跑出来的东西是对的。

有的需求做到一半，被还没就绪的服务接口卡住；有的任务把所有阶段都走完了，代码却建在一份没人确认过的需求理解上。等到验收才发现对不上，只能回头返工，改规格、改设计、改实现。更麻烦的是，过程记录一旦不全，连偏差最早是在哪一步跑偏的都说不清。

慢慢我们想明白：能不能生成代码，其实不是最难的；难的是让它在真实、复杂、一直在变的研发环境里，靠可靠的上下文把活干对。早期做法太指望每个阶段的输入都完整、都可靠，可现实里的需求、历史知识和外部依赖，往往都带着没确认的部分。流程得有本事把这些不确定性先认出来，再处理掉。

**最初的五阶段流程**

原来的流程按需求规格、技术设计、任务拆分、代码生成、质量检查一路往下走，每个阶段自动接住上一阶段的产物，中间没有专门确认关键假设的节点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy7FmszrmHNYc4uphsK7ZE1pPia8XxBM5WZnapEFpXB1vPRWayR7lOhmyORXQqvC1QI3tye7WlaQeBk0SHG8dicOdDOjh2icpMlNes/640?wx_fmt=jpeg)

问题在于：只要上游产物里混进了没验证的判断，这种一路传递就会把偏差带到后面。

GEEK TALK

02

真实迭代里暴露的七类问题

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy5uZOXOqENBcFhP8S7JOj26ribsUC7eibf79ypLJPtiad9a2wyGndDQYJA7tPPzYPfW7ia8qsaLc4hs3quRSUBHSmvKSiaIX9WG1mlk/640?wx_fmt=jpeg&from=appmsg)

把踩过的坑摊开看，大致是两类：一类出在执行过程——看不见、也难追溯；另一类出在任务输入——信息和依赖条件不够。

#### 执行过程：信息越堆越多，出了问题却难定位

上下文堆起来之后，关键事实反而更难保持一致。一个任务要穿过好几个阶段，原始资料、中间结论、临时推断不断往上叠。我们碰到过字段引用错、接口判断失准，也碰到过把早期的推断当成确定事实继续用。光是把上下文喂得更多并不解决问题，还得把事实、约束和待确认项分清楚。

偏差一旦出现，往往缺少定位的抓手。运行记录只留了各阶段的结果，排查的人很难还原：当时到底用了哪些输入、做了哪些判断。结果常常只能扩大排查范围，或者干脆把流程重跑一遍，排查和返工的成本都上去了。

执行状态也没有一个统一的视图。任务进度、卡在哪、质量检查结果、模型资源消耗，分散在各处，研发同学很难及时判断该不该介入，团队复盘也没有一个共同的依据。

#### 任务输入：需求、经验和依赖都还不到位

需求描述常常有歧义。一句话需求，或者一份不完整的产品文档，可能既没写清业务口径，也没覆盖异常分支和验收标准。要是 Agent 自己把空白补上，而后面的设计和测试又都沿用这同一套理解，就会出现实现和测试彼此自洽、却整体偏离业务目标的情况。

存量经验还没显式化。历史代码为什么这么设计、有哪些兼容要求、团队有哪些约定，有一部分还装在研发同学脑子里。Agent 拿不稳这些知识，写出来的实现可能局部逻辑没错，却漏掉了系统长期演进中沉淀下来的约束。

知识图谱的覆盖也还不全。自动检索能补上下文，但结果受制于知识覆盖面、更新是否及时、关联关系是否完整。没检索到相关约束，不等于约束不存在。

外部依赖会直接把执行卡住。部分接口还没就绪，或者状态不稳定，流程就没法做真正的验证。原来的实现缺少足够的暂停、恢复和替代验证手段，一处局部阻塞，很容易拖累整条链路。

这些问题最后都指向同一件事： ****全自动流水线把"不确定"当成"确定"一路往下传，而错误偏偏会在最贵、最靠后、最难定位的地方才冒出来。****

> 全自动最大的风险，不是它会犯错，而是它错了还在自信地往前跑

GEEK TALK

03

重新划分人、工具和 Agent 的分工

对着这些问题，我们重新界定了确定性工具、Agent 和研发人员各自管什么。

路径、分支、编译、校验、日志上报这类有明确规则可查的事，交给脚本和质量门禁去做，省得每次任务都重复判断一遍。当然，这些检查结果也受规则本身是否正确、测试覆盖够不够、执行环境稳不稳定的影响，不能拿来当完整的业务验收。

而需求口径、方案取舍、历史兼容、体验好坏这些要结合业务背景拿主意的事，还得人来定。Agent 可以把证据理清楚、把候选方案摆出来，真正有分歧的地方交给对应责任人拍板。人只在重要决策节点上介入，范围清楚的常规执行还是自动往前推。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6Srn9N1Z6DbDxbUYsFNE6PzEMUhpnhy4fwcBhonWibwHhSFH2f0VN0LHYh2ibX5kAZicyZ5Iec8l58WvWOBoibeRM38KhCrIuYpU0/640?wx_fmt=png&from=appmsg)

在这个基础上，我们把一次性执行改成了多轮反馈：每一轮围着一个明确目标做修改和验证，再决定下一步怎么走。

这就是我们从一次性全自动流水线，转向 Agentic Engineering Loop 的起点。

GEEK TALK

04

Agentic Engineering Loop：把一次性执行改成多轮反馈

新的工作方式我们叫它 Agentic Engineering Loop——人机协作的工程反馈循环。它保留了规格驱动开发（Spec-Driven Development，SDD）的核心思路：先把目标、约束和验收标准定清楚，再去组织实现和验证。

任务进来，先理解需求、确认方向，然后围着"观察—决策—修改—验证—复盘"转：看当前的代码和反馈，定下这一轮要达成什么，在边界内动手改，跑对应的检查，再根据结果决定下一轮。等满足验收条件，交给研发人员反馈确认，这才算交付完成。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6ZOCtWQJS4cwuTzQ0wBBibwP5Xl8AZ20xts78elRaES5L4fMyE7Mv59rxH9n433pGNt4I2ciaFN6lqBvWgsLDdD6ZeYdOQpia2HA/640?wx_fmt=png&from=appmsg)

和原来的做法比，变化主要在这几处：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7Fz0lgicnjHCfBwp7nvqzAshmrFxCwibSS15ZykGYKyRClI6kX03PxP1tG3R3JCWrF7uKv7Qvztg0bjKpbpAibk4oU9f015hbRgI/640?wx_fmt=png&from=appmsg)

需要说明的是，这里变的是工作的组织方式，并不是说"循环天生就比流水线好"。一条完善的流水线一样可以有反馈、有可观测；反过来，换成主 Agent 来协调，也不会自动把长上下文的问题解决掉——事实来源、任务边界、每一轮需要哪些信息，这些照样得管。

GEEK TALK

05

循环之前，先把需求打磨成可验证的起点

多轮反馈要真起作用，得先有一个能讨论、能验证的起点。输入里的关键歧义要是没澄清，循环也可能围着一个错误前提反复打转。

所以我们在执行前加了一道需求调研：研发人员借助调研工具，把业务描述整理成目标、工程约束、改动范围和验收标准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6Htwr9MVedjwpQboKicRwvibxu6XicibVQgkNJpq4icUc4ibMUy6XMalJkRMMujSC5mCCzyKUHyIYibvPicpIr1hgX7RZPkKfr8uyC8Z0/640?wx_fmt=png&from=appmsg)

调研不只是梳理文字，还要去对真实实现：找到相关的文件和调用关系，顺着提交历史理解当初为什么这么设计，核对可能的原因，划清楚哪些范围要改、哪些行为必须保持不变，再拆成一个个能独立验收的单元。需求、验收标准和改动计划各自编号，方便在实现和验证时一一对上。

这样做，能在动手之前就把需求歧义和知识缺口暴露出来。研发人员负责把业务目标和现有系统的约束对齐，Agent 则在这些划好的边界里继续分析和执行。暂时确认不了的信息，就先挂成待确认项，而不是直接当成实现前提写进去。

GEEK TALK

06

让执行过程看得见、可回溯

为了能及时介入、事后也能复盘，我们把执行过程接进了一个统一的观测视图。

本地执行通过上报机制，把每一轮的事件、指标和迭代记录汇到远端平台，整理成运行、任务、事件、产物这些结构化记录。"SDD 运行记录"看板就靠这些数据，展示任务阶段、执行耗时、token 消耗与成本、质量门禁结果，还有上下文占用等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5jib58jTBCJxbD3MRF2ZktZ2aghDTGfW9IQ03XkjQPv1IwapVJ9LZowNHe1ib1gxcNtac9aYVL2nsSnsgaggLrbUDue4jSzYvbw/640?wx_fmt=png&from=appmsg)

这些记录在三个层面上帮到我们：

- 执行过程落进日志和看板，复盘时每一步都能回看；
- 交付结果沉淀成产物和报告，出了问题能追回源头；
- 记录攒下来形成趋势，慢慢就成了团队的经验资产。

看板给了我们一个理解任务过程的入口。但真要复盘，还得结合记录是否完整、验证覆盖到哪、具体产物是什么，把执行完成、检查通过、业务验收通过这三件事分开看，别拿其中一个状态当成交付结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4Qf8ibsYiaUvAskt0xibuaXNCpru3ov9HjBsZc5ORxJx3ztIBRC2icYhnvbnez83EIMFAzsKTqRhtB1yv5IQZiabicTria6wruiaEP64A/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy6ibg117FSvTpGyv6PibvUNADiagtkHkXowo5ia62XDhPsQyZPENS8icW3RjQ0a5wsMVfc87uxeQuTuBaowfBtAVBqa5OfIDgfrndDo/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy6Cc2IO9nIhibxmicVbg4cwuPKkFQib8dFQy09XCPCGAeo3xSzKj5bbw6Y0zFUQUia7VdPUor3Tn70ybWLkFVTfJpmlszKOEKiaLxj4/640?wx_fmt=jpeg&from=appmsg)

GEEK TALK

07

现在走到哪一步，接下来做什么

这套工作方式已经用进了网盘的日常研发。下面说说目前攒下的能力和还没解决的问题——这里讲的是能力建设的进展，不等于已经量化验证过的效率收益。

#### 已经跑起来的环节

- 需求进循环之前，先做一遍证据化的成熟度打磨；
- 把一次性全自动，改成了人机多轮、随时能停下来纠偏的循环；
- 执行过程能上报到平台、看得见，也能回头复盘。

#### 还没解决的问题

- 需求相关的知识图谱覆盖还不全，Agent 自己检索上下文的能力也被这个卡着；
- 一部分依赖的服务接口后置，仍是瓶颈；
- 把存量经验沉淀成能复用的能力（Skills），还在慢慢攒；
- "自动化程度"和"可控性"之间的平衡点，也还在不断调。

GEEK TALK

08

结语：从"生成代码"到"可验证的交付"

这次调整，把我们的关注点从"生成一次代码"拉到了整个交付过程上。需求理解得准不准、改动有没有越界、验证能不能撑住结论、出了问题能不能回溯——这些才是自动化能不能真正发挥价值的前提。

需求确认、分轮验证、过程记录这些确实会多花一些功夫，值不值得，得放到完整的交付周期里看。接下来我们会结合不同的任务类型，持续盯着人工介入、端到端耗时、返工和验收结果，看看这些机制在不同场景下到底带来多少收益。

对网盘团队来说，这次迭代也把人、Agent 和工程工具的协作关系理得更清楚了：

> Agent 负责组织分析和执行，工程工具落实那些能被检查的规则，研发和业务责任人确认关键的取舍与验收结果。

这条路我们会继续走下去：让生成的代码更容易被检查，让执行过程更容易被看懂，也让每一次交付都留下一份清晰、可复查的依据。

END

**推荐阅读**

[Agentic Harness Workflow 框架：把 AI Coding 变成工程化流程](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607615&idx=1&sn=bb329b7e9dbec5b0c37a805dada3f04e&scene=21#wechat_redirect)

[什么样的业务经验值得做成 Agent：从个人工具到组织资产](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607581&idx=1&sn=521aae445a57ce0d9bd885654b09bea4&scene=21#wechat_redirect)

[都在开源 Harness，Codex 和 DeepSeek 到底有什么不一样？](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607560&idx=1&sn=377945189293dcd34a7b23fd6256e40d&scene=21#wechat_redirect)

[Workspace 实践：从个人提效到组织提效](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607508&idx=1&sn=f604f409314f249297faae6d83bd3382&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过