# Claude Sonnet 5.5：性能逼近 Opus 5.5，价格只要一半

**作者**: AI小范儿

**来源**: https://mp.weixin.qq.com/s/TY_tFHFfsekwweI8199OoQ

---

## 摘要

Claude Sonnet 5.5 正式发布，价格仅为 Opus 5.5 的一半，与上一代 Sonnet 5 持平，但同任务可少花 30% TOKEN 且生成速度快 30%。其性能逼近 Opus 5.5，在 Terminal Bench 上甚至反超，编码、知识工作和电脑操控等指标均表现优异，第三方 AA 数据显示其在各推理级别碾压 GPT-6 Sol，性价比极高。

---

## 正文

AI小范儿 AI小范儿

在小说阅读器读本章

去阅读

Claude Sonnet 5.5 终于发了！

前不久发的 Claude Opus 5.5 毫无疑问是我最想用的模型，各方面都是最优的，但问题是太贵了。

且非常的不经用，才发几天我就把它一周额度蹬完了，后面一直靠着 Codex 在苦撑，所以我急需那款性价比更高的。

今天它终于来了，先看看价格，它是 Opus 5.5 的一半，也是目前 Claude 5 系里面最便宜的。当然，更便宜的 Haiku 官方透露也会在几星期之内发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIiaYtKyaNlGG80Gviabf5qtDebSzZlcmn0zv2jaxWicb0prdxDJVice5YWPQic9bGy8TZUtXicyqHyqLAllyCUG6PIiaVJlbVzcJCJBk/640?from=appmsg)

▲ 图：AA 榜单的模型指数与价格

除了价格减半，它跟上一代 Sonnet 5 的价格其实是一样的。但是官方称，做同一件事情，它能少花 30% 的 TOKEN，生成的速度也会快 30%。所以这真的可谓是加量不加价。

而且还有点啊，就是 Sonnet 5.5 其实对标的是 GPT-6 Sol，所以它们的价格也是完全一样的。

从第三方 AA 的数据来看，Sonnet 5.5 在各个推理级别都是碾压 GPT 6 Sol 的，我画了一个斩杀线，可以看到，不管 GPT 6 Sol 也好，还是 Kimi K3、Opus 5，甚至是 Claude Fable 5.1，都在它的斩杀范围之内。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLor8uSr1td41NjbbzTuECdW4ia679Nt7ibIXm8gYB2PJz1MicgTEopqahicC6oqpeOqUKiauibJIFsTSwzpxMd1HibYOBJrOIAgD4ED8/640?wx_fmt=png&from=appmsg)

▲ 图：AA 指数与费用散点图

图上我选的是 Max 档，我对比过其他档也类似，只有 Medium 是 Sonnet 5.5 和 GPT 6 Sol 是接近的，这么看用 Sonnet 5.5 起码得从 High 起步，才能拉开差距。

性价比之外，具体的能力到底怎么样，我还没深度测试，先看看官方介绍？

## 01 性能直逼 Claude 旗舰 Opus 5.5

每次发布都会有一堆的 benchmark 值，这次当然也不例外了。我们还是从这个表格开始吧。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLjPpDs5YB8j4OgEwEZ1pvYptIxw3olUQWRbph9L75O1CZDjnShib49JictF94FtsYW66tRXL0yWELSTUpPlia0rMh0VB0A4zaUoc/640?from=appmsg)

▲ 图：官方基准测试对比表

从官方列出这个表格来看啊，只要瞄一眼你就会发现，Sonnet 5.5 这几个关键指标基本上都已经接近 Opus 5.5 了，甚至在 Terminal Bench 方面，它比这个旗舰的 5.5 还要厉害。

Terminal-Bench 4.0 看模型能否在命令行里完成多步骤任务（官方注明 Opus 用的是 Xhigh 档的最高成绩）。

CursorBench 4.0 测真实编码任务，Sonnet 5.5 拿到 55.5%，接近 Opus 5.5 的 57.8%。编码能力的提升，是它接手 Claude Code 日常工作的主要依据。

知识工作方面这里用了我们常用的那个指标 GDPval-AA，这个指标测试涵盖 44 个职业和 9 个主要行业，主要用来评估模型在实际任务中的表现。

这一项 Sonnet 5.5 只比 Opus 5.5 低 2 分，而隔壁 OpenAI GPT 6 Sol 是什么级别呢？它竟然低了近 20%，所以 Sonnet 5.5 基本上已经是天花板级别的了。

自从 GPT 6 Astra 出来之后呢，我会大量使用到电脑操控。

在这项里，Sonnet 5.5 的提升非常明显，它提升了有 40%，已经和 Opus 5.5 持平了。也就是说，在电脑操控方面，Sonnet 5.5 也是非常能打。

第三方的 Artificial Analysis 智能指数可以看到它的各档都非常强。Max 档已经超过了 GPT 6 Astra，它的 High 档呢？也接近 GPT 6 Sol 的 Max 档。

所以还是前面我说的这个，如果要用 Sonnet 的 5.5，看来至少得从 High 档起步。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKCicTEibqSZgcXWgca6CzQfFaUmPgXDcTEknupPTSP3ABW3V6ZKyRRib4DHckx6QK9xn8h1dqxV9SFVo1abXqcCX8raAibf8BMe9Q/640?from=appmsg)

▲ 图：AA 智能指数各推理档位

官方的资料里面给了很详细的各个指标在每个档的表现，大家可以去看一下。比如我下面这个图，就是 Terminal Bench 在它的各个档位下的表现。

可以很明显的看到，换一个档位，它的性能提升是非常明显的。不管从 Medium 到 High，还是 High 到 X High，这种提升效果会比 Opus 5.5 还要更夸张。Opus 5.5 实际上来讲到了 High 之后，后面的两个档好像就没什么太大变化了。

不过这里要注意的是，这个参数它对比的 GPT 5.6，不是 6-Sol。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJLibGzpG6HswH84IgibFmLJkx7JWcfjbyFiaPPyXe58gXibianmVqrqXAlRbTBibdv1nruztibicq3MDXMHhicAhuwzq1DzicKebjzTJIiceY/640?from=appmsg)

▲ 图：Terminal-Bench 4.0 成本对比

另一项参数就是知识工作里面呢，看来很明显，Sonnet 5.5 是碾压 GPT 6 Sol，它的 Med 甚至就已经是 GPT-6 Sol 的天花板，看来它是打工人的新旗舰。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIMianmsj8ic7Ve5iacpDX7g1S75RUoAg57LOZibVlvKE9eZ81ROcKwpeRWt7qG9MNSKJodTt05qmBuOZZ6fBo4MwZR8HXMyPbZsNc/640?from=appmsg)

▲ 图：AA-Briefcase 成本对比

我们可以根据自己的需要来调整推理的级别，这样来取得一个最佳的性价比。在 Claude Code 和 Claude APP 里面呢，它的默认推理级别都是 Medium。

更低的推理级别就意味着响应速度更快，使用的 Token 也更少，适合日常的工作。那在更高的设置下面，Claude 的推理时间就更长，检查也会更彻底。

## 02 Sonnet 5.5 是来接日常工作的

Anthropic 给两个模型分的工很清楚。

Opus 5.5 处理需要长时间判断、边界模糊的复杂工作；Sonnet 5.5 更适合范围已经说清楚的日常任务：修 bug、改代码，以及做文档、幻灯片、表格。官方还特别强调了它的界面设计能力。

这个定位很好理解，就是目标、任务都很清楚了，在执行方面 Sonnet 5.5 最适合不过了。

比如项目里已经确定要改什么，让模型定位问题、修改文件、检查结果；或者材料已经齐了，让它整理成一份可以继续编辑的文档。

这样的工作不需要每一步都调用最贵的模型。任务目标本身还不清楚、需要在几个方案之间持续权衡时，再交给 Opus 5.5 更合适。Sonnet 5.5 已经全平台上线了，现在打开 Claude 就能使用了，快去蹬吧！

## 03 参考资料

01｜Anthropic：Claude Sonnet 5.5 发布说明

https://www.anthropic.com/claude-sonnet-5-5

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过