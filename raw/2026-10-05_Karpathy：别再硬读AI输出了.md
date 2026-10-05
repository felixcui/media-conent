# Karpathy：别再硬读AI输出了

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/xDQNZIKwK7Dx7c5ND9g4WQ

---

## 摘要

Karpathy指出，当AI生成内容的速度远超人类理解速度时，继续增加文字输出只会加剧瓶颈，因此他建议将模型输出转化为更易理解和验证的形式，包括用ASD-STE100约束语言、生成图表、生成可交互网页以及生成解释视频，以帮助人们更高效地判断AI产出的逻辑与可用性。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

Karpathy 潜水许久，最近发了条推，说了一个很多人忽略的问题：当 AI 的产出速度超过人的理解速度，继续让它写更多文字，只会把瓶颈越堆越高。

模型可以在几分钟内生成几万行代码、研究报告和复杂方案，但人仍然要判断它做了什么、逻辑是否成立、结果能不能用。于是 Karpathy 提了几个方案，把模型输出转换成人更容易理解和验证的形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ8zAy5za2ykkpzDCQWU55bgCuc406CdQU32ILGwx8CCmwHwFu5jjIfictu6Y6bAiaXb7iajzibGmYt1Y1glaZfs7pGyMkQiawgW0xz4/640?wx_fmt=jpeg)

**1️⃣ 用 ASD-STE100 约束文字。**

普通模型喜欢用长句、抽象词和模糊表达。同一个概念写很多字，读完抓不住重点。ASD-STE100 最初用于航空维修文档，限制词汇、句式和表达方式，要求每句话清楚、直接、含义唯一。可以这样提示模型："用 80% 的 ASD-STE100 风格解释这个问题。" 收益是降低语言噪声，减少歧义，让技术文档更容易检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ8NcRnXodoTCngyF3KuVs9usaH0nASPejT9w60iaEzt6YjEiccU3PtThblxmwb8SPTLlvxYpPthGGWYXTA91Y0b6Rwj7icdRSEj98/640?wx_fmt=jpeg)

**2️⃣ 生成图表。**

有些内容的难点来自关系复杂，比如系统架构、调用链、因果关系。线性文字很难同时展示这些结构。让模型生成流程图、架构图或概念图，可以直接看到节点如何连接、数据如何流动、问题可能出在哪。有人提到 UML，确实是一回事。但以前得自己画，现在 LLM 对着你的具体内容现画。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJicSGg7a3IWWuwSngCibRrCQHPiaK4IpFyj3kNcOwT3gO7aAcKRozEZ3uRribsKSWxPm8laspT7k1VOIj7OMkH9dpwQNMqGGbyhY7E/640?wx_fmt=jpeg)

**3️⃣ 生成交互式网页。**

如果问题包含状态、参数或动态变化，静态文字和图片都不够。可以让模型输出 HTML，通过按钮、滑块和动画展示：参数变化后结果会发生什么，系统在不同状态下如何运行。收益是把"阅读结论"变成"亲手验证"。有网友评论说："交互式小网页，参数能自己拨一拨，很多因果关系马上就露出来。比如我们翻译出品的这个免费课程，就可以交互式的学习。 [从零学习AI工程！海外跟学课程火了！](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461161451&idx=1&sn=e9a20599df3c1c5cd14707b2380eb0a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJibzMiacgZel6m02Ssl8jPbd37Tmer3IMkkYxIYjMFg0ibIWIMSy5KACvGGUniblIVqiaIJF4jISKwKyMg3qESRRDaUn9eagibrkrXao/640?wx_fmt=jpeg)

单纯把长文缩短，有时只是把模型的错误压缩得更顺滑。" 另一位网友建议，交互页还可以加个"先猜再看"：把结果暂时藏起来，先猜参数变化后曲线会升还是降，再揭晓。

有网友用模型生成了可视化的 Attention 论文：

**4️⃣ 生成解释视频。**

算法执行、物理过程和抽象概念都包含时间顺序。视频可以逐步展示变化过程，结合动画、旁白和重点标注。Karpathy 建议直接让模型制作 3Blue1Brown 风格的解释视频。有人用 Opus 5.5 跑了一段视频讲递归自我改进，4 分多钟。源 HTML 只有 13.8 MB，渲染出来 34 GB。Karpathy 点了个赞。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ9NGF4ZVUMVx3zJQlE3AakUVtVrXic1jex6qORpezIlXT3vdZK3p2udIialPeZxM8voXPrPl5Db8Ff2Y2qaziaZ9bZv4pBmv4b2Og/640?wx_fmt=jpeg)

还有人做了随机微积分的视频，同样接近 3b1b 风格。

这几个方案背后的真正变化，是"可丢弃软件"的成本正在接近零。过去，为一个问题单独制作网页、动画或视频不划算；现在模型可以根据你的知识水平临时生成，用完就扔。所以，别再硬读模型输出的所有内容了。让模型换种形式，把理解成本降下来。

不过，需要警惕的是，内容格式越容易理解接受，质量监督就会越难。一段文字有问题，扫一眼能发现。一个视频，画面、声音、动画都在分散注意力，错藏在好看的包装里更难发现。评论区有人说，一个好看的错误视频比一段错误文字更能说服人。交互论文那边也有人提，想要个"告诉我论文哪里说了这个"的按钮，动画太好看，容易不问出处就信了。

话说的这里，不得不说笔者和他的观点不谋而合。 LLM 能力不断增强，让内容的生产和表达变得越来越自由多样，同一件事，不同的人可以按自己习惯的格式来理解，有人喜欢读字，有人喜欢看视频，就算同样是文字观点，有人喜欢严肃的，有人喜欢幽默的，各取所需。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ94XEKV0ejRtiarjpYqe8Q5d1EwaulBoXg2kxQUPDvq9HIt1jlkmjGElV8bLxQ9scoFdlOyUSyaMqNMywWyDhDAE30qicKiabOSr8/640?wx_fmt=jpeg)

这两年，笔者一直在此方向上实践尝试，新闻资讯智能体 Wink Pings 便是实际落地的产物，它支持将各种杂乱的信息筛选整理成一篇篇自己喜欢易于理解的风格呈现。目前还以文字内容为主，随着图片、视频等推理成本持续往下走，产品能力还有很大空间。欢迎大家下载试试。

关注公众号回复“进群”入产品群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过