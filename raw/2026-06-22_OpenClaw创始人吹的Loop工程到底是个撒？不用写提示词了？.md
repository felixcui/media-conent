# OpenClaw 创始人吹的 Loop 工程到底是个撒？不用写提示词了？

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/pwHamaHhTtWm2vgha0e5qw

---

## 摘要

近期AI领域新概念Loop Engineering引发关注，它主张通过设计循环来驱动Agent而非编写提示词。该概念与Agent内部的ReAct架构不同，ReAct是解决单步思考与交互的内循环，而Loop Engineering属于外循环工程，其核心在于解决如何持续驱动Agent的问题，即由谁为Agent提供目标、状态、反馈、验收和停止条件等，本质上是确保Agent持续有效执行外部任务的策略设计。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyQAjBhfrlrYC3ewRzgKKPLp21dxjv0ibVo0v2LAI5dQibc9x7icXA9rpP4aX0CRkkxWenPpU3kJqdbsRvoQ9hcqRcJoCTkG3f0ReA/640?wx_fmt=png&from=appmsg)

扩展阅读： [AI 原生的四层爬坡模型](https://mp.weixin.qq.com/s?__biz=Mzg2MzcyODQ5MQ==&mid=2247502472&idx=1&sn=d30ac250c98071c104928f1d674e2a5a&scene=21#wechat_redirect)

来，又来，AI 领域又来新名词了！这次是 Loop Engineering。

借此机会，大家也顺便复习下过去 3 年一些火过的名词，看还记得撒：

Prompt Engineering、RAG、Context Engineering、ReAct、Agent、MCP、Skills、Harness...

如果对 AI 工程有一定认知的同学会了解： **上述名词很多都是在炒冷饭，他们很有点对某个概念再包装的嫌疑** ，比如：

提示词工程往前走一步，做得更复杂、更系统一点就会变成上下文工程；而如果要维护好整个 Agent/AI 所依赖的上下文环境，就会变成 Harness 工程。

所以，这次出现的名词 Loop 大概率也不会是新的，因为 Agent 的经典架构 ReAct 本来就行一个循环执行框架。

所以，这个 Loop Engineering 到底是怎么个事呢？

## Loop Engineering

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyRtwD1zZdNvhP9vJYhlicFOn6wGicMBBk9HQrMr7cLzE33YXuDInSwKcB0B07Gicl25Ddt1d0fsIicuusQmFicj8mkRcBluBOkc5He4/640?wx_fmt=png&from=appmsg)

6 月 7 日，OpenClaw 创始人发了一条消息，大概意思是：

> **你不再需要为编码智能体编写提示词了，你应该设计循环来提示你的 Agent**

所以，对于我这种喜欢脑补的选手，我第一反应就是这人又在 **“胡吹”** 了，OpenClaw 在生产环境实际运行的 ***稳定性、效率和成本*** ，你自己心里没一点逼数吗，还在扯循环...

Peter 本身是某产品的负责人，他说话是带有立场和产品 IP 效应的，他跟我们在说的 **软件日抛** 是一个事，这只是观点、想法，并不是真的，大家不要说风就是雨

但这次有些不一样，他不是 **“一家之言”** ，Claude Code、Google 的 Addy Osmani 也在对 Loop Engineering 做各种补充说明

于是，Loop 又火了，他成功击中了 *人类想要更简单、想要大力出奇迹的美好愿望* 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQ2QJg5KqUYa8VUkGK8dcvS6UJibHUibkZqtqibN3D3PH7xbOf5NDQjDqI7GD1hdDbw9V0QDvunHfF1qWKeSFdxkAJiaXjgwbicFQrg/640?wx_fmt=jpeg&from=appmsg)

那么 Loop 的价值到底在哪，他为什么要出现，他出现是为了解决什么问题呢？

## Why Loop Engineering？

首先需要澄清的是： **ReAct 和 Loop Engineering 不是一个事，或者不是一个层面的事** 。

ReAct 是 Agent 内部经典的循环架构： **推理—行动—观察** 模式，他回答的是 Agent 每一步如何思考、如何和外部有效交互的问题；

而 Loop Engineering 不解决 Agent 架构层面的事，他在回答另一个问题：

> 当 ReAct（Agent Loop）已经存在后，谁来持续驱动这个 Loop？
> 
> 谁来给它目标、状态、反馈、验收、停止条件和恢复机制？

所以，这里的 ReAct 是内部框架循环，他可能是 AI 工程师的活、隶属于 Agent RunTime 的范畴；

而 Loop Engineering 是外循环工程，他是需要让 Agent 持续干正事的策略、他解决的是外部任务如何持续的问题，这可以是 Agent 产品经理的工作：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQmzlewlTmzaoMd3l0NnOhmqB7CMd2MISD9A5Z3t4Sdk800Zg62IoWwYoFenld7qNMN90dB4g4PAmxs6Eft7icoCDDSLrxRWtkk/640?wx_fmt=jpeg&from=appmsg)

大家这里听起来应该是有点懵，我举个案例做说明。传统客服 BUG 反馈链路是这样的：

1. 客服在群里反馈一个问题，值班的测试看到后先判断这是操作问题、Bug 还是需求；
2. 如果是 BUG 就转给研发，研发看代码、看日志、然后开发上线；
3. 如果不严重（体验问题）且短时间改不了就变成 Todolist 第二天处理；
4. 我们这里只关注 BUG 链路，其他逻辑略去...

这是经常会发生的流程，而程序员对此也是很烦的，谁也不想爱爱的时候被打扰；如果这里按照 Loop Engineering 的定义，逻辑就变了：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTgPPoA6cfNfmHmfM607ToasiaT5IqAiaZj8S85AxiaQ6eWw19l9suYdgVaO6hYm4AZWoP9hTRAHqbMfXMt5kAn8S2rZ2TQiaf3oD8/640?wx_fmt=jpeg&from=appmsg)

客服在群里反馈问题后（甚至客服也可以用 Agent 替代，但我们这里不讨论那么复杂的场景），Agent 自动监听并接管后续链路。

它会先判断问题类型，再收集足够的上下文：

1. 如果问题简单、低风险，Agent 可以自己修改代码、上线，并同步给程序员和客服群。
2. 如果问题有一定复杂度，Agent 会先改好代码，但不直接上线，而是发给程序员确认；程序员确认后，再继续上线；
3. 如果问题不清楚或风险较高，Agent 就停止自动执行，转人工判断；

而整个这套机制，就是我们所谓的 Loop Engineering。

至此，我相信大家也看懂了，这跟我们各个企业在推行的 AI 原生，其实是一个事情，换句话说：

> Loop Engineering 不是个工程技术的事，他是个如何与 Agent 合作的事，并且这里的关注点要从人上升到组织

这个案例是我方便大家理解而类比做的说明，接下来我们看看国外大佬的案例：

## Loop 的五个组件

Addy 在他那篇长文里，把一个完整的 loop 拆成了五个组件 + 一个外部记忆：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTDqtNzvRlqn8bKIPrRwDLQ6N5giaibXvVo03EOhNzoO5iclSHjUDmGjzQeY5n1MRtjtgfibIH7aqVDeVBSl7UpGzyEQq0N7UxZlNQ/640?wx_fmt=jpeg&from=appmsg)

其实 Addy 也有个案例说明，但我读下来觉得太程序员了就没用，大家可以自己感受下：

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyRSmFrhDHcNzdLY07qYlUZEvqlCpJYicBicQa3Jlib8ENnhOCnrpe1PPfNT8QGiaDAWuogickZqNZj3BgrFA60gpotfpcg6Ticof5pTQ/640?wx_fmt=png&from=appmsg)

#### 一、Automations

Automations 解决的是：Agent 为什么会启动，也就是什么时候被触发的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQkv0icvXlqLyzoicwYicFT5uibicCQoQKCB2iaZ8uMP0spwYGC0PicdabyzP8Zj28pgaaliaUdKcnic6XOWdW4uPFwxCwyaDpChERJcwHc/640?wx_fmt=jpeg&from=appmsg)

比如传统链路里，客服在群里反馈问题，得等测试、研发或者负责人看到，才会有人处理。

Loop 里第一件事，就是让 Agent 有自己的任务入口。比如客服群出现 **报错、打不开、支付失败、提交不了** 这类信息，Agent 自动监听、自动识别、自动创建任务。

所以 Automations 就没那么神秘，他就是一个规则，只要规则合理，代码就是分分钟的事情，

#### 二、Connectors

Connectors 解决的是：Agent 如何接入真实业务系统？也就是连接机制的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySEeP8ngETox1DuIhwibHl0JQwnVJRib5AhUxuDrbVqXOBGNbJoqCxsD3sZmIaDKKfPArHYBs9GSjNESJZowTneC3PZMA0p66lTo/640?wx_fmt=jpeg&from=appmsg)

这东西的背后其实很不简单的，往小了说需要构建整个研发团队的信息流、往大了说需要构造整个公司体系的信息通道。

比如，客服简单一句： *用户说按钮点不动* ，这句话本身不够处理问题。

我们去处理的时候可能需要，查订单、查日志、看用户截图、看最近发布记录...

Agent 要处理问题也是一样的，所以它必须能连接客服群、订单系统、日志系统、监控系统、代码仓库、工单系统和发布系统。

所以 Connectors 的本质是信息通道和动作通道，并且在这里大家就可以看出来了： **Addy 举的案例太狭窄了，如果一般企业要用好他这个所谓的 Loop，其实需要做很多工作的** 。

#### 三、Worktrees

Worktrees 解决的是：多个 Agent 或多个任务同时执行时，怎么不互相污染？

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTV7JkQ5g0hy1XmGZvOiaoUiahQGTChRlBxjTPUOOdPUXOtpLlVv0NZr1ewtaMDjdoxB1s3iam3mXpkxzP2NmNV7A1UYxhyfgJ2YU/640?wx_fmt=jpeg&from=appmsg)

比如客服群同时反馈三个问题：支付失败（ **这个会直接升级为人工** ）、优惠券不展示、订单状态异常，Agent 不能在同一个环境里乱改。

在代码场景里，Worktrees 是独立分支和独立工作区；放到业务场景里，就是每个问题独立工单、独立分支、独立测试、独立发布判断。

Worktrees 是系统的隔离机制、也是边界的控制，我相信无论 Agent 多智能，这两年也一定不会有人胆敢用他在支付系统上面去搞事情。

#### 四、Skills

Skills 解决的是：Agent 做事时依据什么经验、规范和 SOP？这也是我们常见的朋友了，我们知道他承担的是团队工作流的执行：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRM9fyKUaOUVt05vu6egvyZAvBPa4Ul4CGXVf9DNx67vPPo9UF8ekmGrPxSLrZY20BzLTp6okGle4mwO714W1G2OLQYHAVTibhQ/640?wx_fmt=jpeg&from=appmsg)

Agent 从怎么去拿上下文到拿到上下文如何去做，这都要依赖与公司的处理规则，这个规则就是 Skills：

1. 比如什么问题算 BUG，什么问题是操作问题，什么问题是需求；
2. 什么问题可以自动修，什么问题只能提方案；
3. 哪些模块低风险，哪些模块涉及支付、订单、权限、资金，必须人工确认。

在 Loop 的真实使用过程中，大家多数的工作都会变成准备各种 skill。

#### 五、sub-agents

Sub-agents 解决的是： **一个 Agent 不应该既当运动员又当裁判。** 其实就是工程解耦的思维，有点之前提示词一事一议的感觉，核心逻辑是分工：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRQ7ot5mzOV5dgqUibj9v3svoOd8n0GpFIJnRLamh8htvCS0FqibABGNaVbx3WibwTK0SwVXrcIr58Y3oM8cCJ52HB75OcQZpImhc/640?wx_fmt=jpeg&from=appmsg)

传统流程里，本来就有分工：客服反馈、研发修复、测试验证......

Agent 接管链路后，也不能让同一个 Agent 自己判断、自己修改、自己验证。

更合理的是：一个 Agent 做问题分诊，一个 Agent 做修复，一个 Agent 做测试或 Review，复杂场景再交给程序员确认。

这里倒不是说 Agent 能力不行，多 Agent 架构是为了符合我们的习惯，毕竟单 Agent 维护起来要简单很多。

#### 六、Memory

Memory 解决的是：Agent 如何不失忆，如何接力，如何恢复？

其实无论对于 Agent 架构，还是对于机制流程，做 **状态机制** 都是很烧脑细胞的事情。

一个 BUG 从客服反馈到最终上线，中间会经历很多状态：已监听、已分类、已查日志、已定位、已修复、测试通过、等待人工确认、已上线、已通知客服、已沉淀规则...

这里应该是 Connectors 的延续，或者说整个企业信息通道建设在这个场景可以被打散为 Memory 与 Connectors。

好了，上述就是 Addy 关于 Loop 的实践方法论。

## Loop 到底是什么？

综上，我们在这里就可以为 Loop Engineering 下一个真正的定义了：

> **Loop Engineering 可以被看作一次 AI 原生研发团队的实践案例**
> 
> **或者说，是 AI 原生在研发协作场景里的一个具体切面**

它甚至都不是一次完整的 AI 原生组织实践，这里切的是已从 **个人使用 AI 工具** 进入了 **团队流程被 Agent 接管** 的阶段，大家可以参考这张图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRcDySHyWC1bNP7b8ScLTnVBsINwSfbeEzE3jNTiceEN5qzhdmB8Iibpx507lT6jplHVmmROXRr1afchtevEdNBe7NN3TbsVMIGQ/640?wx_fmt=jpeg&from=appmsg)

所以，你如果问我对 Addy 《Loop Engineering》

`https://addyosmani.com/blog/loop-engineering/`

这篇文章怎么看？我会说如果就我这几个月的企业咨询视角的话：

> Addy 巧妙的用了一个 coding agent 的案例，展示了一次 **AI 原生研发团队的雏形** ，并给这个案例取了一个名字 Loop Engineering

然后大家也就知道了，这个案例居然 TMD 火了：

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyQGOZ7vVib2T2yto439rgX705WBnqeHLUs5rDfWduy2bJ3Aj9vaQ3E6L2yWhkshhZkNCbzEvaApqGLbXUKjuHq3LlFaGQkTTUKU/640?wx_fmt=png&from=appmsg)

而我真正打开去看了下，貌似大家并不了解他的内涵，甚至有人说什么提示词已死， ***这个犊子就扯大了***......

## 结语

那么问题来了：为什么一个 **AI 原生研发团队雏形** 的案例，能在国内外技术圈引发如此广泛的讨论？

答案或许有些反直觉：因为绝大多数人还停留在第一层，而 Addy 已经把镜头拉到了第三层。

当前多数开发者还停留在第一层（个人工具适配层），他们的目光还聚焦在：怎么写提示词让 Agent 把代码写对；

而 Addy 在思考 **如何设计一套系统，让 Agent 在无人值守的情况下持续产出可用代码** ，这是接近第三层（组织适配）要考虑的问题。

这侧面说明当前 AI 行业的认知差距可能还是不小的，依旧是鱼龙混杂啊！

所以， ***为什么Loop会火？因为它踩中了一个沉默的痛点***

> AI Coding工具普及后，团队效率并没有等比提升

为什么会这样呢，因为机制没有匹配、因为组织结构没有匹配，而这里 Loop 的本质，还是在走机制流程的爬坡，他的目标是把 **隐性流程** 变成 **显式代码** 。

什么意思呢？意思是把每一步隐性的判断标准显性化，比如：

1. 什么样的问题算BUG？什么样的算需求变更？
2. 哪块代码可以快速修复？哪块必须经过Code Review？
3. 什么情况可以自动上线？什么情况必须等人工确认？

因为 Agent 必须依赖完整的规则和上下文才能能力最大化，所以这里 Loop 真正在做的事其实是在构造 AI 需要的舒适环境。

最后也吐槽一句，Loop Engineering 又在炒冷饭，我觉得这个概念是没必要存在的...

继续滑动看下一个

叶小钗

向上滑动看下一个

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过