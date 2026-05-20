# Hermes 登顶 OpenRouter 之后，我才发现它最缺的那一块，被这个插件补上了

**作者**: 未知作者

**来源**: https://mp.weixin.qq.com/s/6XNlc9YKj1py44p__dINSw

---

## 摘要

## Hermes遗漏了一件事 Hermes Agent，核心思路就一句话： **一个部署在你自己设备上的 AI Agent，用得越久越强。在小说阅读器读本章 去阅读 就在上周，Hermes Agent 在 OpenRouter 应用 Token 消耗榜上单日 2710 亿，第一次把 OpenClaw 的 2450 亿挤下来，拿下总榜第一。

---

## 正文

在小说阅读器读本章

去阅读

就在上周，Hermes Agent 在 OpenRouter 应用 Token 消耗榜上单日 2710 亿，第一次把 OpenClaw 的 2450 亿挤下来，拿下总榜第一。

从开源到登顶，仅仅三个月。

这件事在中文圈被各种角度解读。在媒体和社区题目都是这样的：「快速蹿红的 Hermes 会不会成为下一个 OpenClaw」、「Agentic AI 时代不可逆转」。但比起这些宏观叙事，我更在意的是 Nous Research 这帮人在宣传里反复念叨的一句话—— **the agent that grows with you** 。

跟你一起成长的 Agent。

听上去像口号。但你真把 Hermes 装上之后会发现，它确实在认真做这件事——只是只做了一半。

## Hermes遗漏了一件事

Hermes Agent，核心思路就一句话： **一个部署在你自己设备上的 AI Agent，用得越久越强。**

整体来说 Hermes 确实好使， Skill 自动生成那个功能很实用，做过的活儿不用再教第二遍。

换句话说，你跟 Agent 聊得越多，它积累的信息就越多，但这些信息之间的关系它处理不了。

重复的、过时的、矛盾的内容全部堆在一起， **时间长了记忆库就变成了一个大杂烩。**

就好比，你雇了一个员工，他会把你你交给他做的活儿，你跟他闲聊时说过的偏好统统记下来。你跟他说「我喜欢喝美式」，他记得。你说「我要做一个关于瑞幸咖啡冰美式新品的设计方案」，它也会记进去，但当你俩昨天一起改冰美式设计案改到凌晨四点，最后是怎么定位问题的、踩了什么坑、走了什么弯路，他下次见你可能就会和冰美式少冰混在一起甚至完全不记得冰美式设计方案最后怎么改的。

这种员工有用吗？有点用。值钱吗？不值钱。

我真正想要的是后面那种记忆，把过程记下来的记忆。Agent 跟我配合干活的整个过程，哪一步是对的、哪一步是错的、什么情况下应该走捷径、什么情况下不能走捷径，这些东西如果能沉淀下来，那它才算是真的「在我身边长大」。

然后我就在想，有没有什么东西能帮 Hermes 把记忆管起来。

结果还真让我找到了。

记忆张量 MemTensor 团队出了 **一个 Hermes 本地记忆插件。**

![](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJ8xDrv2CdO8Krib07xFicCYJQOL3cHKgqUwFXfeoyzGFGKKX5IfibH0d5tPkVfpcogkO0eicHc41KI3pyrquDibEC2pW8TpRC1cA37k/640?wx_fmt=png&from=appmsg)

我看了一眼他们后台，感觉到：这玩意，可能真的不一样。

但一个问题也出现了。

## Hermes已经有记忆了，为什么它还需要一个记忆系统

这个问题很重要。

于是我重新翻了 Hermes的系统文件 `~/.hermes/memories/` 。

里面就两个文件。

`MEMORY.md` ，2200 字符上限，大概 800 token，用来记环境信息、项目约定、它自己学到的东西。 `USER.md` ，1375 字符上限，大概 500 token，是用户画像，记你的偏好、沟通风格、对它的期待。

两份加起来，3575 个字符，比一条公众号文章长不到哪儿去。

我盯着看了挺久。

Hermes 做记忆的方式是——给你两份 Markdown，硬性上限定死，每次 session 开始当成「冷冻快照」整个塞进 system prompt 最前面。

它的逻辑是，记忆不是数据库。记忆应该像大脑那样，小、精炼、随时在线。所以它干脆不要 retrieval pipeline、不要向量库、不要 per-query 延迟。前缀缓存完美命中，速度快、成本低、可控性高。

Nous Research 做产品，确实比市面上大部分知识图谱、RAG、多模态融合等要好，要轻。

但是。

用了大概十天，我开始觉得不对劲。

上周我让 Hermes 帮我把一个 Pydantic 模型从 v1 的 `dict()` 迁到 v2 的 `model_dump()` 。这事我俩前面已经做过两次了，每次都折腾了快一小时才发现 v2 下 `dict()` 失效。

第三次，它写出来的代码里还是 `.dict()` 。

我打开 `MEMORY.md` 一看，里面写着「项目使用 Pydantic v2」，仅此一句。 `USER.md` 里压根没相关条目。

它知道项目用 v2，但「v2 下 dict() 失效要换 model\_dump()」这条经验，没进记忆。

翻完官方文档才理解为什么。Hermes 的记忆系统骨子里是「策展式」——记什么、不记什么，是 Agent 自己事后判断的。每次 session 结束它会想一下「这次有什么值得长期记住的」，调用 memory 工具写一行进 `MEMORY.md` 。如果它判断不值得，就什么都不记。

这套机制保证 `MEMORY.md` 永远不会膨胀，每条都是 Agent 主动认为有长期价值的「事实」。

但它的盲点也在这里。

**它记的是事实，不是过程。**

本质上，Hermes 原生记忆解决的是两件事： **环境约定** （这个项目用 pnpm、入口在哪）和 **用户画像** （你喜欢短回答、讨厌过度解释）。这两件它做得真的很好。

但它做不到第三件—— **把跟你一起干活的过程沉下来** 。

因为那玩意根本塞不进 3575 个字符。

**MemOS Local Plugin 2.0的做法，他们称之为「执行即学习」**

这就是我两周后又装上 MemOS Local Plugin 2.0 的原因。

记忆张量（MemTensor）这帮人 5 月 9 号发布 2.0 的时候，通告里有一句话：

> Agent 在为你做事的同时，把执行链上的每一步，动作、观察、反思、你的反馈，都沉淀为可审计、可归因、可复用的学习信号。

翻成一下就是，不只记你说了什么，记你俩一起干了什么、哪一步走对了、哪一步翻车了、为什么。

我用做饭打个比方。L1 是厨房日记，记每次炒菜每一步。L2 是从日记里归纳的规律，「炒青菜油温八成下蒜末刚好」。L3 是对自己这个厨房的全局认知，灶火偏大、酱油在第三个柜子。Skill 是肌肉记忆，番茄炒蛋闭眼都能做。

## 记忆的「保险机制」

聊到这儿，我得稍微往技术层面探一探，但放心，我尽量讲人话。

2.0 这次架构重做里有一个我特别欣赏的设计，叫「双层反馈」。

记忆有个老问题，你记了一堆东西，但你怎么知道哪条是对的、哪条是错的？

举个最简单的例子，我跟 Hermes 调代码，它写了一个方案，跑通了。这个方案进了记忆库。但「跑通」并不等于「这是最优解」，可能它跑通的过程巨慢、巨丑、有性能隐患，我心里其实是不满意的，但因为已经能跑了，我没说什么。

如果记忆系统只看「跑没跑通」，它就会把这个糟糕的方案当成正确答案沉淀下来。下次类似问题，它继续给你掏这个垃圾方案。

MemOS 2.0 的做法是把反馈拆成两层。

**第一层是步级反馈，模型对环境** 。每一步执行之后，环境的客观结果立刻进系统，比如代码跑通了、命令报错了、文件创建成功了。这一层是「这一步在客观上做没做对」。

**第二层是任务级反馈，模型对用户** 。任务做完之后，你这个真人对最终结果给出主观评价，可以是显式的点赞点踩，也可以是隐式的，比如你接受了它的方案就是隐性认可，你立刻让它重做就是隐性差评。这一层是「我作为用户，对这个最终结果满不满意」。

两层一合，记忆系统才知道「跑通了 + 用户满意 = 这个解法是真的好」，「跑通了 + 用户不满意 = 这个解法能用但是有问题」。

这种东西，挺反人类直觉的，但又特别合理。我们人类在公司里学经验也是这么学的，光看老板有没有过你的方案不够，还得看他过的时候是「好，就这样」还是「就这样吧」。语气不一样，记忆的权重就不一样。

## 一份核心，OpenClaw 和 Hermes 都能用

2.0 这次发布最关键的产品决策是—— **Hermes Agent 和 OpenClaw 用的是同一份核心** 。

记忆张量的架构图是这样的：最底层是 Reflect2Evolve 核心，宿主无关；往上是 agent-contract 的稳定契约；再往上是各家 Agent 的适配器，OpenClaw 走 TypeScript 进程内，Hermes 走 Python MemoryProvider + JSON-RPC。

适配器各自不同，底层算法、存储、检索、Skill 生命周期全是同一份。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ9icqd04tR5OsjQpMNrdbUF8cZaQa8oruVyjX0h4MQdIVZnVFc6ITammwqYia8sPHmFenzfSXrCEc5XnMs1bjWXM11pFMEXiaFABw/640?wx_fmt=jpeg&from=appmsg)

这事一开始我没当回事。直到那天我同时开着 Hermes 和 OpenClaw 干两件活，OpenClaw 那边在查资料，做统计。Hermes这边在写公众号。中间Hermes忽然给我来了一句，「要不要按照之前的产品测评方案写一个大纲」。

我愣了一下。

这条经验是我之前用OpenClaw写文案攒出来的，Hermes怎么也知道？

于是我又问了Hermes一个问题，是否记得之前跟他说过的事情，它给出了如下回答：

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJiclQzqPsiargPx7p7Rhgm3nAjicKEs4ObnxmmKqTJQfMdgP1j75HLhU88aLhDvsGWjkeic8KKibibzlVB7jaWBVrQA9QVgEv0uMQjNM/640?wx_fmt=jpeg&from=appmsg)

这个问题是我之前之前注入OpenClaw用来测试的问题，仅有OpenClaw知道，大家可以对照一下

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ9VfPWeZvnpl0zRibF8X0AOlCmToN2B5Y9E6Qbo62yqM3EOEnYjOu2a81NMe2vfZ7u9yFtYDnZXubORKAwKfOjtrJjpVA9KxPY8/640?wx_fmt=jpeg&from=appmsg)

之后我又研究了一下后台的Viewer，它可以导入Herme原生记忆或者把本地形成的md文件变成记忆。

![](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJ9aGyInE24ETRBcyL758sciatiaYMbB5z0wylMIetM97ozt2FnqusTtfjpm4vLES4icRov6P7KubLkYnehhfCRaVyBxKGUH6RGtXo/640?wx_fmt=png&from=appmsg)

这是我第一次真切体会到「 **记忆资产可携带** 」是什么意思。同一份经验，OpenClaw 学到，Hermes 用到。

我们这几年用 AI 工具的最大痛点，从来不是工具不好用，是工具切换的时候经验全没了。MemOS 想干的事，是把记忆从 Agent 里抽出来，做成一层独立的、可携带的资产层。 **Agent 是工具，记忆是你的。**

## 实操

如果你已经在用 Hermes，叠一层 MemOS 就一行命令：

```
curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.sh | bash
```

脚本会自己检测机器上的 Agent，谁在就给谁装适配器。Hermes 那两个原生 md 文件不会被动，它们继续以原来方式工作，MemOS 在上面再开一个 Viewer。

这里我再讲两句自己的使用心得：

- **冷启动期长** 。前一周你基本感觉不到差别，trace 还在攒、Skill 还没结晶。预期得是「装上之后持平，两周后开始上扬」。
- **Viewer 上手有点信息过载** 。建议前两天只看记忆和技能标签，最有体感，Traces 和 Policies 等你想搞清楚某个行为「来源」时再翻。

## 写在最后

回到最开头那张 OpenRouter 榜单。

Hermes 单日 2710 亿 Token 把 OpenClaw 挤下去，最直白的信号是—— **足够多的用户相信，把长期使用、持续积累这件事押注在它身上是值得的** 。这是一种完全不同的用户关系：越用越回不去的搭档，而不是即用即走的体验。

但 Hermes 那 3575 个字符能装下的，只是「你是谁、这个项目长什么样」那一半。剩下「你跟 Agent 一起趟过的每一条河」，得靠 MemOS 那套 L1 / L2 / L3 / Skill 接住。

两个加起来，才是一个完整的 AI 同事。

通用大模型已经够强了。从 GPT-4 到 Claude Sonnet 4.5，从 Gemini 2.5 到国内一票模型，通用推理能力早就不是瓶颈。下一步真正决定 Agent 好不好用的是什么？

是它能不能 **在你自己的本地世界里学起来** 。

互联网上所有公开的代码、文档、Stack Overflow，模型预训练阶段都看过了。但你的代码库长什么样、你团队的 CI 怎么走、你之前在 Alpine 镜像里踩过哪些坑、你这个项目为什么有个奇怪的 `utils-legacy` 目录，这些互联网上没有，预训练学不到，微调来不及。

剩下能填补这一公里的，只有一个 **在你身边长大的记忆系统** 。

如果大家想自己研究一下AI记忆，开源链接在这儿：

GitHub：https://memos-docs.openmem.net/cn/openclaw/local\_plugin

技术文档：https://memos-docs.openmem.net/openclaw/hermes\_local\_plugin

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过