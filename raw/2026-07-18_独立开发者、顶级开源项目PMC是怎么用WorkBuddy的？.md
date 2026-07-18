# 独立开发者、顶级开源项目PMC是怎么用WorkBuddy的？

**作者**: 刘宏宇

**来源**: https://mp.weixin.qq.com/s/TR6gDpCpfTw_FgKGR5BtyQ

---

## 摘要

Apache开源项目PMC刘宏宇分享了使用AI工具WorkBuddy的经验。尽管它曾因提示词歧义导致代码审查方向错误，但在排查线上OOM故障时，能仅凭日志精准推断出Sentinel导致的内存泄漏，并输出可复用的排查SOP。此外，它还能协助撰写专业的英文安全漏洞邮件。凭借强大的上下文推理能力，WorkBuddy极大缓解了开源开发者的脑力带宽压力，成为高价值的辅助工具。

---

## 正文

刘宏宇 刘宏宇

在小说阅读器读本章

去阅读

关注腾讯云开发者，一手技术干货提前解锁👇

上个月我差点干了件蠢事。

让WorkBuddy评估一个开源项目PR的代码质量，它给了我一份极其专业的输出：

> 架构耦合严重，核心模块职责边界模糊，建议拆分为独立子模块。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr5u7VnzWkMH9dEUCkVgQq3icxAzCdyj517yiaWhkQeaCG2TP9hnTP2cplJaFI5zHfmSI9JmB1MntNiajmto1wLS6libktian27nPUdE/640?wx_fmt=png&from=appmsg)

分析得有理有据，我差一点就在Apache社区邮件列表里引用了。后来发现，它分析的是错误的模块。因为我在描述时有一处表达歧义，它顺着歧义走了，头头是道但方向不对。

这个故事的教训后面再说，先说说为什么我没弃用它，还越用越离不开了。

我是刘宏宇，坐标北京，后端架构研发方向，写了近10年代码。白天在公司做平台产品研发及项目交付工作，业余时间主要泡在开源社区，目前是Apache ShenYu、Apache Hertzbeat、Spring AI Alibaba三个项目的PMC。一个人同时维护三个顶级开源项目是什么体验呢？大概就是永远有处理不完的Issue、Review不完的PR、回不完的英文邮件，发不完的版本，偶尔还得处理安全漏洞报告这种高压活儿。

说白了就是脑力带宽长期不够用。

## 01

“你们有没有用Sentinel？”

上个月ShenYu项目线上出了一个OOM。jstat看堆内存走势，Arthas抓线程快照，Old Gen持续攀升，Full GC频率异常——判断是内存泄漏没什么难度，做了十年Java的人闭着眼睛都能看出来。难的是定位泄漏源头，尤其是在一个网关项目里，流量路径复杂，可疑对象一大堆。

我随手把jstat的输出和Arthas的thread快照贴给WorkBuddy，就问了一句“你觉得问题在哪”。它确认了Old Gen增长趋势异常，然后追问了一个让我愣住的问题：

> 你们有没有用Sentinel？如果资源名是动态拼接的字符串，每次请求都会注册一个新的SlotChain，这个泄漏在流量高峰下会线性放大。

我根本没提过Sentinel这个词。

它是从ShenYu的技术栈上下文里自己推断出来的：

API网关大概率接限流组件，Sentinel是Java生态最常见的选择，而动态资源名导致SlotChain泄漏是这个组合下的经典坑。这个推理链条完全正确，而且它还顺手画了一张完整的排查流程图，从jstat确认趋势到Arthas定位增长对象，再到检查SlotChain注册逻辑、修复资源名为静态枚举、验证GC回落，每一步标注了具体命令、关键指标和判断条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr4iave9WQn5VssaqvXb6JgibumppYYnUNU5VKxJpBW8EBqfCJwxWBBLC8xyhOyLuia1240yYFgzDcj0ZRmcArgjjDKGU2tcCWdjkE/640?wx_fmt=png&from=appmsg)

后来我把这张图截下来，直接拿去给团队做了一次内部分享。一个“帮我看下日志”的随手一问，变成了一份可复用的故障排查SOP。这种事以前只有你运气好、碰上一个经验丰富的同事、恰好还看过类似案例才可能解决。现在好了，凌晨两点也能问，还不用欠人情。

一手交token，一手交方案，童叟无欺。

## 02

安全漏洞这封邮件有多难写

做Apache项目PMC有个逃不掉的活儿：安全漏洞triage。有人提交了一个漏洞报告，你得判断它到底算不算漏洞，查CVE、翻Apache Security规范、对照代码看trust boundary，然后用英文写一封措辞精准的邮件发到安全邮件列表。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6mNfpgBwG9bKH5jmqmgx2Z3LuPjxGm0wtQTGjUpNWQAh926cM8nu7b4dtczC4wMiatFzekHYqpRg1icuhMfdic1FT3lUAC6xiaU4w/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr5BazlNMXibCCEh11iakno0kLBIcmpTX5DGSVvgJo6miaKD4c5TrpTqEwHOoQ0RRtyRuh36zVfEO0GXNibNf2vDnZOw8yvicmZH4miaY/640?wx_fmt=png&from=appmsg)

这封邮件的分量比很多人想象的重：

措辞太强会得罪报告者，太弱显得项目不重视安全，语气不对会被老外politely但firmly地教育一顿。Apache社区有自己的一套潜规则和tone，做了几年PMC我大致摸清了，但每次写还是得反复斟酌，尤其是用英文表达“这个不算漏洞，谢谢你的好意但请回”这种微妙语境的时候。

以前处理一个漏洞报告，从看懂到邮件发出去，2-3小时打底。现在我把漏洞描述和复现步骤扔给WorkBuddy，它判断是否属于调用方可控行为，生成一封符合Apache社区语气的英文拒绝邮件，顺带列出Security Model文档里需要补充的条目。20分钟搞定，邮件质量比我自己吭哧吭哧写的还面面俱到，情商感人。

但这里有一条铁律：涉及开源社区的对外表达，永远是WB起草、我审。顺序不能反。Apache社区的潜规则和人际关系网它判断不了，这个审核权我不会外包给任何AI。

## 03

Cursor管"手"，WorkBuddy管"脑"

这两个工具我都在深度使用，解决完全不一样的问题。

Cursor和Claude Code是在IDE里直接改代码的，生成样板、重构方法、写测试，适合"我已经知道要做什么，帮我写出来"的场景。WorkBuddy是在我还没想清楚的时候用的：技术方案怎么选、线上报错背后的根因是什么、社区邮件这个措辞会不会踩雷、需求拆解有哪些我没想到的盲区。

打个比方吧，以前开发者群体里流行一句话叫"面向Stack Overflow编程"，有问题先去搜，搜到答案直接抄。Cursor干的事本质上是这个逻辑的究极进化版，你甚至不用搜了，它直接帮你写。但Stack Overflow从来解决不了"我该不该用这个方案"的问题，Cursor也不行。WorkBuddy 可以。

我的工作流现在固定了：先跟WB把方向确认清楚，再切Cursor落地。顺序很重要，方向错了，Cursor帮你写得越快，返工成本越高。

前段时间在Apache社区有个技术方案讨论，开会之前我先把对方可能的反驳都跟WB过了一遍。后来讨论的时候果然被challenge到了那几个点，但因为提前想过，接得很从容。朋友有一次看我用，愣了半天说了句“你这不就是找了个架构师陪你聊吗”，然后沉默了几秒，“链接给我，我也去注册一个。”

## 04

回到开头那个翻车

现在可以讲讲那个翻车故事的后续了。

它分析错了，原因是我没把问题描述清楚。我说的“核心模块”在那个项目的语境下其实指的是另一个东西，但我没有给够上下文，它就按字面意思去理解了。分析过程完全自洽，逻辑链条没问题，就是前提错了。

坦白讲，这件事反而让我更信任它了。因为它暴露了一个我自己都没意识到的问题：我的描述有歧义。如果是跟一个人类同事沟通，对方大概率会追问一句“你说的核心模块是指哪个”，但AI不会。它会直接给你一个自洽的答案，流畅到你不会去怀疑它。

这就是我重度体验以后总结出来的核心心得：把上下文给够，别把它当搜索引擎用。遇到问题先花30秒把现场描述清楚再问，这30秒换来的回答质量远超直接抛一句“为什么报错”。技术决策必须让它给理由，不接受“建议你用XX”这种没有推理过程的回答，一定要逼它摊开思考链条，我来判断是否适用我的约束条件。

以前作为独立开发者，很多事情不是不会做，是不敢轻易开始。因为一旦方向走错，纠偏的成本全部自己扛。所以倾向于只做自己有把握的事，遇到陌生领域会拖，等到想清楚了再动。

现在的心态变了：遇到没做过的事，第一反应不再是「我要先研究清楚」，而是「先跟 WB 捋一遍」。把不确定性外包给它做第一轮过滤，我来做最终判断。决策的起点从「我能想到什么」变成了「我能判断什么」，这个转变让我开始愿意碰更复杂的事情。

说白了，它是0延迟的第二意见。不是用来替我决策的，是在我拍板之前帮我把没想到的漏洞找出来的那个角色。工作里最难找的不是执行力强的人，是愿意在你思考过程中给你泼冷水还不带情绪的人。

现在我有了。

如果明天它没了呢？我会失去的是“随时可以开始想”的状态。这不仅仅是回到效率低一点的日子，是回到很多事情又开始拖着不想碰、每次求助都要从头解释一遍背景的状态。它记得我在做哪几个项目、我的技术偏好、我上周方案讨论到哪了。

这些context积累下来，确实没法迁移。

期待未来 WorkBuddy有更加让人惊喜的更新，但至少，现在这个阶段，我的脑力带宽终于够用了。

\-End-

原创作者｜刘宏宇

感谢你读到这里，不如关注一下？👇

![图片](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe951ia9iadG3cGPp3OjMQBY8jUDyMQB9NRlcpN0NbibgksMBfHCS5aeo3P2y0RInfFicPmeIqibvgic9wBxA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

📢📢来抢开发者限席名额！点击下方图片直达👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZRhjO8xAWr4cGdkdKp6UCUOqxiaHSE5iaqOxjOOYR26w1enbE34o79I0IlhhC6q9Sy8ia0POUvqvPbD6UHDaKMcEwdpkULiaPngGRZljYDrKicsM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95UnhD9f7ia4T3ufXM1liaxxffiaEy41n0icohEC2qDS05icapaN4iaTVfsClibPRmqOjNW6q33PZicAVoSOg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

你对本文内容有哪些看法？同意、反对、困惑的地方是？欢迎留言，我们将邀请作者针对性回复你的评论，欢迎评论留言补充。我们将选取1则优质的评论，送出腾讯云定制文件袋套装1个（见下图）。7月24日中午12点开奖。

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe96Ad6VYX3tia1sGJkFMibI6902he72w3I4NqAf7H4Qx1zKv1zA4hGdpxicibSono28YAsjFbSalxRADBg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

扫码领取腾讯云开发者专属服务器代金券！

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4nU3obq4B4URKhzJMmibw1uR1ZehOtyeel5hYevARgDqdKxqXvtzclLhu7g28g6PBib8M2uaQegic6MrCdBic0SdHh4XUQODQkmKk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe979Bb4KNoEWxibDp8V9LPhyjmg15G7AJUBPjic4zgPw1IDPaOHDQqDNbBsWOSBqtgpeC2dvoO9EdZBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95pIHzoPYoZUNPtqXgYG2leyAEPyBgtFj1bicKH2q8vBHl26kibm7XraVgicePtlYEiat23Y5uV7lcAIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过