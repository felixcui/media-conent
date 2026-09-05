# Agent做视频第三弹：一句话生成教程视频，Codex+豆包语音+Hyperframes全自动

**作者**: 点这里关注→

**来源**: https://mp.weixin.qq.com/s/p_wUsCCXY4DlYDHfOQD51A

---

## 摘要

文章介绍了用Agent全自动制作教程视频的优化工作流：先与Codex沟通改良思路，引入A/B Role概念，通过主讲人画面与辅助素材卡片交替出现增强视频动态感，并建立模板库、统一动效语法以便复用；随后敲定10步流程，先输出20-30秒样片验收再批量完成以避免返工；最终将整套流程封装为名为Guokeai Video的Skill，默认组合Codex、豆包语音与Hyperframes，实现从一句话需求到。

---

## 正文

点这里关注→ 点这里关注→

在小说阅读器读本章

去阅读

大家好！我是AI实战博主过客，用系统化专栏拆解 AI 核心玩法，目前《Agent实战》连载中，工具、案例、教程一站式学习平台：guokeai.com.cn，记得关注哦！

之前已经写过两篇用Agent做视频的文章，上一篇是 ["公众号文章秒变视频"](https://mp.weixin.qq.com/s?__biz=Mzk2OTA4OTM5OQ==&mid=2247490339&idx=1&sn=ec76d434beb2fda782fc37e01d19e68b&scene=21#wechat_redirect) 。这两天我又对整个流程做了一波优化，效果比之前更好了。

话不多说，先看这次优化后的视频效果。

> 这次的视频节奏比之前流畅很多，还加入了A/B Role的对话形式，配上了豆包的语音，整体效果我个人还是很满意的。

GUOKEAI

第一步：先跟Codex沟通总体的改良思路

我先给Codex一些方法论上的引导，然后让它帮我做一个"如何用Codex做视频"的教程视频。

![跟Codex沟通改良思路](https://mmbiz.qpic.cn/mmbiz_png/bh9XUZB5jhr81zdtRaaXIcpoOO1LS5IeLy8x3r0Mpby73hNFZVjebUSn3vLaY3JxrjicVY6VEtj8dKvOcnyulgZIedtd3X7kHCAOjqufyJcY/640?from=appmsg) GUOKEAI

第二步：引入A/B Role的概念，加强动态效果

**A/B Role** 是这次优化的核心——A-roll是主讲人画面，B-roll是辅助说明的素材卡片、对比图、局部放大等。通过两者交替出现，视频的动态感和信息量都大幅提升。

![模板库与动效语法](https://mmbiz.qpic.cn/mmbiz_png/bh9XUZB5jhryjHdiaGSzEkSgCboF1MRE0DrcPUNczIe1OmrdgkibPaibWibiaicffePSDwfKNUsAggic019YIkfpib94RACJlZTHEjDxr9SldFlwOIs/640?from=appmsg)

这里也建议大家建立自己的模板库：先做少而精的几类B-roll（核心观点卡、两方对比、步骤流程等），再统一动效语法（卡片进入、局部放大、数字跳动等），这样每次做视频都能复用，效率翻倍。

GUOKEAI

第三步：敲定改进后的工作流程

这里也建议大家像我一样， ==先让Codex输出20-30秒样片，确认没有问题之后再继续下一步== ，避免后期返工。

![改进后的10步工作流程](https://mmbiz.qpic.cn/sz_mmbiz_png/bh9XUZB5jhoBGQfibWPRDawGfvvP3zzDwBbThJTqu8AQcpsepfShPrECsohkuyaVFr021GWE9ib2mO221yNjMk5t1ialEEk2hhqerqibA7SdAHk/640?from=appmsg)

整个流程共10步：从定稿文案生成配音，到短语级声学对齐，再到按语义拆镜、确定每个镜头的核心信息、选择A/B roll、标记真实素材位置，最后先做样片验收、再批量完成、补BGM和字幕动画。

GUOKEAI

第四步：记得封装成一个Skill，方便后续调用

最后，把整个流程封装成一个Skill，以后只需要一句话就能调用。

![Guokeai Video工具说明](https://mmbiz.qpic.cn/sz_mmbiz_png/bh9XUZB5jhq6M61z5r51ySibACQcrUWfNuevH0hKlmUdK7XUvrY39yAWU2N6QGP5GrxNqORNG9wTJ8pwGaUJBtgSoeZyMEUibeGp2wCGesvwk/640?from=appmsg)

我封装的这个工具叫 **Guokeai Video** ，核心功能是把你的资料和参考样片，转成可看懂、跟读、修改的过客AI讲解视频。默认工具组合就是 Codex + 豆包语音 + HyperFrames，除非你明确指定，否则不会引入其他剪辑器。

> 从"一句话需求"到"完整教程视频"，中间你不需要操作任何一步。这就是 Agent 工作流的威力。

建议你也试试把自己常用的工作流封装成 Skill，一次搭建，永久复用。

我是 AI 实战博主过客，用系统化专栏拆解 AI 核心玩法

我们都是这个世界的过客。既然来了，总得留下些什么。这趟旅程里，我只想认真做一件事 —— 和你一块学习 AI。

不追风口，不制造焦虑，也不装大佬。只挑真正有用的工具，讲普通人听得懂的方法，分享自己亲自踩过的坑。

一个人走太累，一块走得才远。欢迎找我加入过客 AI 年度陪伴群，大家一块学习 AI

关注后回复"见面礼"，即可免费领取10+实用工作流、25+提效skill、4万字经典提示词

![过客AI见面礼](https://mmbiz.qpic.cn/mmbiz_png/bh9XUZB5jhrZhichHJvibQIueUSZBjNEBBkR8QWSHGjsQjQibxAFEU6hbibXicIb3cheVO23t9GArnwJG9d4G5ic4c8hmnG8FicdQTbqGGpUTMX8aQ/640?from=appmsg) ![关注过客AI并加入交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/bh9XUZB5jhqbDIKnXT6yguxXxfzBTOo9gcHPkB6StISaO1PL793aiaBia6ql3dRibZWClibuQks8cnZItDdGBpdUX4sliaCjOGPNg22WVorCOOLU/640?from=appmsg)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过