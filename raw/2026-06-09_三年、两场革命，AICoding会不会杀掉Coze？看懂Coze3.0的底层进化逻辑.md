# 三年、两场革命，AI Coding 会不会杀掉 Coze？看懂 Coze3.0 的底层进化逻辑

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/9RnuvkwXY7QrERwVw995Kw

---

## 摘要

Coze3.0的发布展现了其三年迭代的两大底层进化逻辑：一是开发方式从低代码拖拽向自然语言编程的范式跃迁，二是协作方式从单Agent向项目级多Agent团队的升级。在1.0到2.0阶段，Coze凭借低门槛的Workflow编排、形成商业飞轮的活跃插件生态以及打通字节系等丰富的发布渠道快速出圈。理清这两条交叉演进路径，是解答AI Coding是否会淘汰Coze等低代码平台的关键。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

> AI训练营 **10期** ， **6月底** 开班，欢迎咨询

Coze在上周发布了3.0版本，这次比较大的变化是支持项目级多Agent协作，并且web、桌面、手机端能够同步协作。

我是从1.0用到3.0的老用户，根据我的观察发现，Coze这三年的迭代，其实是两条不同的跃迁路径在同时推进。

1. **一条是开发方式** ，从手动推拉拽搭建Chat bot到自然语言编程实现应用；
2. 另外一条是 **协作方式的升级** ，从单Agent到AI 团队。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQFcERasauC77b7skyNroPCVQM1V2VTziaOJgQBuOvCwP7bwRTespDvfHyNVuwzrHULWPckza1zajOaoM4qjtpT2SEwRmJjGK1w/640?wx_fmt=jpeg&from=appmsg)

这次更新的3.0版本只是第二条线走到今天的节点，而第一条线早在去年就已经完成了范式的升级。 **两条线交叉到一起，很容易混淆，但是拆开来看，每条线的逻辑都很清晰。**

我们之前讨论过： [《Agent 会不会淘汰 Coze、Dify、N8N 等低代码平台？》](https://mp.weixin.qq.com/s?__biz=Mzg2MzcyODQ5MQ==&mid=2247501435&idx=1&sn=642af5904bb631485301a3acfd90d00f&scene=21#wechat_redirect)

要回答这个问题，如果把上面两条结合起来就能很好的回答了，下面我们逐步展开来看，Coze这两条升级的路径具体是怎么样的。

## 开发方式的迁移

2023年底，大模型的能力已经很强大了，但是大部分人还不知道如何把模型能力变成可以使用的产品，或者说对普通用户而言实现的成本太高了。

而Coze1.0就是在这样的背景下诞生的，它尝试通过低代码的方式，把编程逻辑拆解成可视化的功能节点，用户像搭建积木一样把这些功能节点拖到画布上，用线连接起来，就可以构建出完整的工作流或者ChatBot，目标是让不懂技术的小白用户都能搭建AI应用：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySQ5r33pPkg0qHYaDaCiacRLIwLkqfnDIL9WXxQfe8Ho04Q4aKlkqaAOV24WMestQkglxhia7tjRJO1vMknUJQ2gPoDibibpsyXiaW8/640?wx_fmt=jpeg&from=appmsg)

同一时期，已经有很多平台在做类似的事情，只是每家的路线不同：

1. Dify走的是API优先、开放可控的企业路线；
2. FastGPT走的是专精RAG做知识库问答；
3. n8n则以极致灵活的自动化流程服务技术团队；

大家都在做Workflow编排，只是面向的用户人群不同、封装程度不同，但是Workflow是那个时间段大家都在实践的共同范式。

**在Coze1.0发布之后，到Coze2.0推出之前，这个时间段可以说是整个Coze产品的高光时刻，因为它的优势足够突出** ：

#### 第一，活跃的插件生态

除了官方提供的插件外，还有不少三方服务商以及个人开发者在持续提供优质的插件。

最重要的是，开发者通过发布插件是可以赚钱的，而coze平台本身又自带字节系的流量优势。

这让三方服务商也很愿意把自己的服务使用插件的形式接入进来， **最终形成正向循环：插件越多 → 平台越好用 → 用户越多 → 插件更有价值，让插件生态越来越繁荣** 。

同一时期，这个飞轮，其它平台还没有跑起来。

#### 第二，丰富的发布渠道并且很省事

它与抖音、飞书、豆包等字节旗下产品天然打通，用户可以把创建好的智能体或应用一键发布到多个渠道上，除了字节旗下产品还支持微信小程序、公众号等平台。

对于普通用户来说，这种做完即发布的体验，具有天然的吸引力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQaAHcaKsZhuTib0lL3eqls06aP6djonKW2zoibxHJkKuksxHWSUiaUys5paQEF7TzN8mk5U8d6y5V0kH5zYvb6Wx99kCCWtnFd5U/640?wx_fmt=jpeg&from=appmsg)

**简单的上手方式、大量优质的插件生态、再加上丰富的发布渠道，这几点叠加在一起，对小白用户是非常友好的，并加上字节的流量扶持，让这款产品快速出圈** 。

但是随着深入使用， **我们发现，搭建简单流程很爽，复杂流程就很痛苦** 。

#### Workflow 复杂度问题

我之前做个一个上百个节点的工作流，搭建过程非常痛苦，一个节点一个节点的编排， **最终整个画布看起来像一张密密麻麻的蜘蛛网，要在画布上找到目标节点做修改非常困难，你得从头梳理逻辑，顺藤摸瓜才能找到** 。 **并且修改一个节点的输出格式，下游的很多节点都要跟着调整才行** 。

因为工作流的这个运作机制，就是一系列节点的串联，每个节点都有明确的输入和输出，一个节点的输入依赖它前序节点的输出。

更难受的是调试，报错信息能看懂，但是不知道是哪一个具体的节点出了问题，只能逐个检测输入输出，像是在乱麻里面找线头。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS04uQLFIuofg5fGplx17rFMoWGPmicwNTnJMbbZbiaqW9Y6jDN7S4Jt4GiceJermUtn2chvr2aZwAHaxqunTv4kCqWt7FnBiakGBs/640?wx_fmt=jpeg&from=appmsg)

当我反复被复杂工作流折磨的时候，心里有一种越来越强的预感： **下一步一定是自然语言描述来替代手动编排和调试** 。

因为模型的能力一定会越来越强，在大模型能很准确的理解自然语言的情况下，为什么还要手动的一个个节点去拖拽呢？

## 自然语言实现AI应用

Coze1.0的核心痛点已经非常清楚，手动编排太麻烦，复杂工作流的搭建和维护成本太高。

正如我们之前预测的那样，在2025年12月，扣子编程正式发布， **开发方式从手动编排跃迁到自然语言驱动** ，我们不用在拖拉拽节点，只需要描述想要什么，AI就会自动帮我们生成工作流或者应用程序。

比如，我要实现一个HR简历筛选的工作流，需求提示词给到AI：

```
## 需求目标
实现一个工作流，帮助 HR 快速筛选简历，根据岗位评分标准对简历进行打分，并将简历信息及评估结果保存到飞书多维表格中。

## 业务流程
1. HR上传一批PDF简历、并填写这批简历的岗位名称
2. 使用PDF插件读取简历中的内容
3. 调用大模型提取简历中的基本信息，并结构化返回, 基本信息包括：姓名、电话、邮箱、学历、毕业学校、工作年限、求职岗位
4. 根据岗位名称拿到飞书多维表格（岗位表）中维护的岗位要求及简历评价标准
5. 在把简历和岗位信息及评价标准给到大模型，让大模型进行打分，总结评价，并结构化输出
6. 把简历基础信息、评价、得分、简历内容存入飞书多维表格（人才库）

## 飞书多维表格定义
1. 岗位表：岗位名称、岗位要求、岗位评分标准，均为文本类型
2. 人才库：姓名、电话、邮箱、学历、毕业学校、工作年限、求职岗位、简历内容、简历评分、总结评价，均为文本类型
```

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyTa1641jyhwk5afVIcxXW834EyMQMlGe9icGs6gokfStfiau66BlUDEggr6bibETfDj3Yfk310DeLMHiamJJIzrjYmUAuRPxwKnhXw/640?wx_fmt=png&from=appmsg)

通过自然语言编程，我们只需要负责描述意图，AI负责具体实现。

**从拖拉拽到自然语言编程的这个转变是必然的，这并不是产品经理拍脑袋决定的，而是技术成熟的必然结果。**

2025年，模型在编程能力上有了非常大的进步，在意图理解、指令遵循、代码生成、结构化输出的能力都上了新的台阶。

经过一段时间的使用，Coze的用户也清晰的感受到，我知道想要实现什么，只是搭建实在太麻烦了，用户的需求发生了变化。

加上Cursor、Claude Code、Trae等AI编程工具的竞争压力，自然语言搭建一定是工作流平台下一个演进的方向，并且也是整个编程领域不可逆的大趋势，如果Coze还停留在手动编排阶段，就会被这些工具抢走用户。

基于上面这些因素，Coze这边不得做出重大的改变。这个阶段的Coze全面转向了AI编程，除了能够实现智能体和工作流之外，还增加了网页应用、移动应用、小程序，甚至后面还支持了一度爆火的Skill开发。

而拖拉拽的编排方式也从Coze产品体系中退出了历史舞台，旧版功能依然能够使用，但是入口明显做了弱化， ***这让很多老用户有点摸不着头脑，半天找不到原来的入口，网上吐槽的声音非常之大。***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyR0Wg1iaXyemDGOiayPAQmSichfQVeFib8P9FPmyibG5NwMwfGndVBj3V2Cc5ZXtIqgytYia92ypLetu2EjKrsicQ5ZpmicvnWU64EkHno/640?wx_fmt=png&from=appmsg)

**相比Dify、n8n这些平台的演进步伐，Coze产品的演变之路最为激进，它是直接去Workflow化**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTET3PwDcrRPq3HyibhnibR7BszBRzicJmg8w2l7LxrQh7wsSGUBkB2UHs2biaYiad9jiaC7MdzDdPnXmmHXlIIlonjavbciazCWVaGO0/640?wx_fmt=jpeg&from=appmsg)

Dify的路径最为保守，官方始终坚持可视化节点编排，最近两年的更新重点基本都是围绕着“Agent工作流能力增强、企业级集成、RAG能力升级、人工协同（HITL）以及可视化编排”在展开。

不过社区有相应的方案，通过自然语言描述让AI辅助生成Dify Workflow DSL，然后导入到Dify中使用。

n8n作为这几个平台的老大哥，依旧坚持 **一切皆节点** 的设计哲学，倡导没有什么是不能在一张画布上搞定的。

同时也在与时俱进，2025年10月就正式发布了 **AI Workflow Builder，** n8n官方对它的定义：使用自然语言描述目标，创建、优化和调试工作，自动完成节点选择、布局和配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyS0n8ibhFLK0SmkVmXPfTkcexuwI11wRBcEQwNZna8b3U0rohhHYXI934tT5y4LoAEOnrTwFuyIjRMtTlXsLMYubqd1SSv9ibxSg/640?wx_fmt=jpeg&from=appmsg)

**这里就出现了一个有意思的分化了，Coze在去Workflow，Dify官方没有动作但社区在发力做AI生成Workflow DSL，n8n则是推出AI Workflow Builder** 。

三条路径，本质上是三种对于未来开发方式的不同判断，Coze认为用户根本不用看到节点，Dify认为节点就是最好的交互方式，n8n认为用户想看到节点但是不想手拖。

当然这里的分歧，可能跟每个平台的定位不同，Coze定位是小白用户，Dify定位是企业开发者，n8n定位是技术极客。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySFVfUI8cM4zicEQibqnkbib0bU068XY1NQhJBI0smlk5hAqMpCIbcCRfjIWx96LFNbtswahZA07kh9Cl1gyCicTaibMgibLxVtJIMfI/640?wx_fmt=jpeg&from=appmsg)

> **但是殊途同归，都在借助AI辅助生成，减少手动拖拉拽节点的编排**

## Coze → AI Coding

我们继续回到Coze2.0的变迁上，Vibe Coding带来的感受确实是很爽的，以前搭建一个中等复杂的工作流至少要1天时间，现在花20分钟左右描述需求，AI在10-20分钟就能生成初版，在花1小时调试就能完事，效率确实提升了一个数量级，但是整体体验还是差了点意思。

AI的理解不总是准确的，这里可能跟平台提供的模型能力有关系，更麻烦的是调试，以前调试节点流程，至少能看到每个节点的输入和输出，报错了也明确的知道是哪个节点报错了。

但是现在出了bug你可能得去看代码，看控制台输出的日志，然后反馈给AI修复。并且这个过程并不是一下就能搞定，会持续的拉扯，尤其是对于普通小白而言，耐力有限。

因此，Vibe Coding降低了创建门槛，调试门槛反而更高了， **这个阶段的根本矛盾在于：自然语言的高层意图和代码级精准执行之间存在语义鸿沟。**

整体而言，Coze2.0的升级，已经脱胎换骨了，它的定位是自然语言编程，而不再是低代码开发平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQXycOc3uUjk5qd7vibFnoSeGgA4NPRJyIOhr9gMW8ibXCnkLZrKdib6bQJ53XCCV3IcGvia41icdCDF3BrtiaDCgEiciaQVq4Tq7UslD8/640?wx_fmt=jpeg&from=appmsg)

这里也能回答我们之前讨论过的一个问题： **AI Coding现在能力这么强，是不是就能干掉可视化编排的这类Workflow平台？**

之前我们预测是不太可能，但是会给这些平台一些压力，倒逼平台升级，通过自然语言描述的方式来实现Workflow的搭建，不再需要手动去拖拉拽这些节点来实现流程编排。

目前从各个平台的情况来看，也印证了我们的结论基本一致。

## 协作方式的跃迁

我们在看另外一条演进的路线，无论是Coze1.0还是Coz2.0都是单Agent的架构设计，存在三个明显的瓶颈： **上下文断裂、设备割裂、能力单一。**

换句话说就是，单次对话无法推进长期任务，换设备就丢失进度，单个AI难以覆盖调研、开发、创作等全流程工作。

这次Coze3.0给出的解法是，以项目为载体、以Agent为单元、以多端为入口，让不同职能的AI 像真实团队一样分工协作，用户只需要定目标、控制方向、验收结果，对复杂的任务自动拆解并推进执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySVVV2mparIibH47NETcYjptwuKFjgUOhqHRsKKKW5PXjGwauoZqahr51q3QRmE3UmTtjzH3wKzzlWJKqMapTBbHJegibPoEJkQE/640?wx_fmt=jpeg&from=appmsg)

这里对3.0版本升级的功能点就不做具体展开了，感兴趣的可以自行前往官网体验。

这里重点讨论一个更深层的问题： **每一次版本升级，其实都是在减少人类参与执行层上面的事情，在决策层参与越来越重了，那么什么才变得更加重要呢？**

之前Coze1.0把复杂的代码逻辑抽象为可视化编排的节点，Coze2.0用自然语言实现减少手动拖拉拽，Coze3.0让专业的Agent干专业的事，并拉上一个Agent团队帮你做。但是"要做什么"和"做到什么标准"始终得你自己决定。

比如我们前面实现的HR简历筛选，实现方式可以是拖拉拽节点编排、可以是Agent Skill、也可以是AI Coding，但最终决定 HR 简历筛选效果的，并不是具体的实现路径和工具平台，核心还是在于岗位的评分标准，这些判断标准就是业务KnowHow。

其实Coze的技能商店已经明确了这个方向，官方内置了投资顾问、自媒体达人、调研分析师等很多职业模版，每个职业模板背后都是一套行业KnowHow。

这里可以预见的是，未来的Agent工具平台功能一定是趋同的，但是真正分化的是谁的业务KnowHow沉淀得更深。

## 总结

现在我们回看Coze产品的两条路径：开发方式从拖拉拽跃迁到自然语言编程，协作方式从单Agent升级到AI团队。用户的心智模型也从“我怎么实现这个功能”变成了“我怎么让我的团队完成这个任务”，再到“我该做什么、做到什么标准”。

从1.0到3.0，Coze用了不到三年的时间。迭代速度非常之快，每个版本的变化都非常巨大，很多老用户都有点跟不上看不明白，现在仍然有不少用户还在用1.0的思维在看待Coze的产品。

当然，这也是这几年AI能力爆发带来的必然结果，从基础模型能力提升、Agent应用的爆发，用户需求的提升，让Coze这类AI应用层产品不得不在浪潮中自我颠覆。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySpGPHLwpMYW8PrwBGxyPrv3oCGYvo2Zib0mmD2LzgyTnE8MiahbNE82NyqCLuZ6OkZyDvKuez19VibXeeAiannFmIHRz0Br4bgkgU/640?wx_fmt=jpeg&from=appmsg)

我相信，3.0还不是终点，它仍然有很多的问题需要持续探索和解决。 **但下一个节点的竞争焦点，很可能不再是谁的工具更强，功能更多，而是谁的KnowHow更深** 。

大家都能用自然语言让AI团队做事情的时候，最稀缺的，是要知道要什么、标准是什么、边界在哪里。而这些才是最终的护城河，也是是AI最不可能替代人类做的事情。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRYhk8SbJLV78yHWSpkGNgDic8sHG7CiaibbQ2zmzFeS3cTMM8HymDc71YmXOb0UlaeuWYQibCNMbbWKGYy4DGyicPYObwrMTg6uEKM/640?wx_fmt=jpeg&from=appmsg)

继续滑动看下一个

叶小钗

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过