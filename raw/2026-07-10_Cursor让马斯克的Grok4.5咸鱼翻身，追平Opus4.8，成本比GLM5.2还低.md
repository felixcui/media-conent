# Cursor让马斯克的Grok4.5咸鱼翻身，追平Opus 4.8，成本比GLM5.2还低

**作者**: zzy

**来源**: https://mp.weixin.qq.com/s/WdVvpJWnbrUtQTbHG8hWEg

---

## 摘要

马斯克将xAI更名为SpaceXAI并发布旗舰模型Grok 4.5，该模型从内测到上线仅用11天，现可在Grok Build和Cursor中限时免费使用。Grok 4.5具备Opus级水准，在SWE Marathon、Terminal Bench等多项核心编程测试中超越或追平Opus 4.8，综合表现亮眼，且使用成本低于GLM-5.2。

---

## 正文

zzy zzy

在小说阅读器读本章

去阅读

马斯克这周打出了一套连招。

周一，xAI 改名 SpaceXAI，换上新 Logo，周三，也就是北京时间今天凌晨，SpaceXAI 正式发布 Grok 4.5。第一款以新身份亮相的旗舰模型这就来了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPGWRUk3P5xSULxBfuhibvjoa2vibKMp1l34lXIgHmF0bJdh7sFC2bWKmrBpNHa1KkGllQicDF22ub1sJ1M6HJvofV3zd7ibnXoLBw/640?wx_fmt=png&from=appmsg)

从 6 月 28 日 Grok 4.5 进入 SpaceX 和特斯拉内部内测，到今天开放，仅用了短短 11 天。

SpaceXAI 这次也直接放福利—— **限时免费开放** ，用户可在 Grok Build 和 Cursor 中直接白嫖 Grok 4.5。

## ◈Opus 级水准，成绩单亮眼

早在发布前，马斯克就预告了Grok 4.5 是 Opus-class 模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPaR6M2p5EvEcPiaYfYWavDliaz4UJysh3CpFiadm5gfrSsMJ69XW9cWhaFn9mXkB0M1ic3wYr2fjXa4bAbaTLHcm1vnQyx5vtIg9w/640?wx_fmt=png&from=appmsg)

发布页面上，SpaceXAI 公布了五项编程相关的成绩，对手列得很全，Fable 5、Opus 4.8、GPT-5.5、GLM-5.2 这些一线模型都放在同一张图表里对比。

先说 DeepSWE，考法很直接，把模型当成一个真的程序员，丢给它完整的开发任务，从理解需求到写完代码，全程自己干。1.0 这一版，Grok 4.5 拿了 62.0%，把 Opus 4.8 的 55.75% 甩开 6 个多点，离 GPT 5.5 的 64.31% 只差一步。

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNaB1PibqFWx2gneysG9C723xwJKDfazRoasgMJNsbbuLibhwDDUslgd4cuXFt5PRN7KZBPEhUxgdF7icklFX9icmUSTVP3EcWTjB0/640?wx_fmt=png&from=appmsg)

DeepSWE 1.1 跟 1.0 题差不多，但换了规矩，所有模型统一用同一套最简工具来跑，谁也别想靠自家顺手的工具链占便宜。这一改，Grok 4.5 掉到了 53%，被 Opus 4.8 的 59% 反超。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNkkvvSkSupAGbvbhl8zjQyRZwjzptGeJqeQq31s7sL8jWt9CbQzeq4iaT6tHNFHZKrfSd1Ixy8H2Tyd3IdpiaSF11CVAGOicXt64/640?wx_fmt=png&from=appmsg)

SWE Marathon 这一项考的是超长任务。不是修一个 bug 就收工，而是跨几十步、连续干很久的马拉松式工程活，而且一次过才算数，不许重试。这一项 Grok 4.5 拿了 29.0%，直接排第一，压过 Opus 4.8 的 26.0%，也超过Fable 5 的 24.0% 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOU1EMhqBibZUuNmLxm8bWlNibDjs9U473BZWEVWZd6woVFAZS2zbsvWImUZfwSicWVz8WtVWicTE8GamK3snntN6WuhmcJ7nJ0FiaQ/640?wx_fmt=png&from=appmsg)

Terminal Bench 则是直接把模型扔进命令行终端，让它自己敲命令、装环境、跑脚本、修报错，全程没人搭手，考察独立操作电脑的能力。这一项 Grok 4.5 拿了 83.3%，压过 Opus 4.8 的 78.9%，几乎追平 GPT 5.5 的 83.4% ，离第一名 Fable 5 的 84.3% 也就一个身位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPjz2cJYajib6Nd0YXlXBm9DhbKiazQkXvGhIDcPmYxpM47wvYOH5ETYNZE75kJvEjvIyn0lpB9frBZziaNVlmhicJgUtSTbA60BlY/640?wx_fmt=png&from=appmsg)

还有 SWE-Bench Pro，这是业内公认最接近程序员日常的测试，题目全是从真实开源项目里挖出来的真 bug 和真需求，模型得直接上手改代码，改完还得跑通项目原本的测试才算数。这一项 Grok 4.5 是 64.7%，Opus 4.8 是 69.2%，差了四五个点，不过反手压了 GPT 5.5 的 58.6% 一头。

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHMgd6XRku6v3S437QQstADTiaseP7QwlHxpYaKHB6FLhqst4tacnKuNqBKx1dCPQ7JUCsWdlp7NPzfKXRySpiaTtkUrmakv1YcQQ/640?wx_fmt=png&from=appmsg)

有意思的来了，Open AI 紧接着发布推特，称 SWE-Bench Pro 这项测试并不可靠，还要撤回之前关于研究界把它作为评估工具的建议。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPsLD6hqgDibibXHQwtxCQul4Q46ZhfqmThYOOKKuT9icDd8uqFMx10BW2rhD8Prnia9XficEzicNZnMFPnJGSTmpYymIzQNzu0A79PU/640?wx_fmt=png&from=appmsg)

无论如何，从目前官方发布的数据来看，五项测试Grok 4.5 对 Opus 4.8 三胜两负，马斯克之前说Grok 4.5是“Opus 级别”的模型，也不算吹牛。要是把定位更高的 Fable 5 拉进来，还有一些差距，但那是完全不同价位的产品。

官方成绩单之外，独立评测机构 Artificial Analysis 也放出了自己的跑分。

在 GDPval-AA v2 基准测试中，Grok 4.5 拿了 1543 分，全球第四。但真正的看点在成本，跑完一个 GDPval 任务， **Grok 4.5 平均只花0.49美元，不仅比排在它前面的模型便宜近 90%，甚至还低于 GLM-5.2 和 Kimi K2.6 这些国产模型。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHO54oKia375IpmWSRbeg8HXPict8SLXwQ4ibots1JXHakibq3xqKsLw9ZmxarvryI4KicaWU7NbcXrzMrR9a8NO9nicYz2WmAjZxUa3I/640?wx_fmt=png&from=appmsg)

## ◈更快、更便宜，性价比拉满

跑分只是敲门砖，Grok 4.5 最打动人的是使用感，又快又省。

- 更高效的 Token 。同一个 SWE-Bench Pro 任务，Opus 4.8 需要 6.7 万 token，而Grok 4.5 平均只需约 1.6 万 token——仅为对方的四分之一。这意味着实际使用时，成本大幅降低。
![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNF8iavibXMibUYdebydgbBiaMOK5Wk2l3mBAruTAfM3A62NMkOdB6Uib8YtS1VMJyDaulWO1dBaPQW7tzPlcdMqNIFYOR7Srgu4fibk/640?wx_fmt=png&from=appmsg)
- 更快的输出速度。速度达到 80 token/s，这个以往属于轻量模型的水平，如今出现在旗舰身上。上下文窗口更是拉到 50 万 token，据马斯克自己预告，到下周，这个数字还将升级到100万。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHN3sg15RIOr4RhECupZVdK2c9p8wjloQJdzIfQ5R1bhpDzEMv2xIptXaCsVbNHwibPjPiakTuOL4ic1nxnwabBxahGaHbJjJzX4YY/640?wx_fmt=png&from=appmsg)
- 更具性价比的价格。输入2美元 / 百万 token ，输出6美元 / 百万 token。外媒 *The Decoder* 直言，这个价格让基准上那点差距几乎可以忽略。再把更低的 token 用量算进去，实际账单相当于打了双重折扣，性价比拉满。

官方总结称“Grok 4.5 在单位时间和成本下提供了最高的智能水平”，放在这组数据面前，并不算夸张。

Grok 4.5 的进步并非偶然。

算力端，Grok 4.5 基于 1.5 万亿参数的 V9 基础模型，在数万张 NVIDIA GB300 GPU 上训练。

数据侧，Grok 4.5 与 Cursor 联合训练，注入了海量真实开发者的行为数据：如何一步步定位 bug、跨多文件修改代码、人类如何修正 AI 错误等。直接治好了 Grok 过去“跑分强、实战弱”的老毛病，尤其在前端和复杂工程场景的表现有了明显提升。

## ◈限时免费，现在就能上手白嫖

这次官方给了一个福利，限时免费开放 Grok 4.5，两个入口，一个是 Grok Build，一个是 Cursor，而且 Cursor 是所有档位的订阅都能用，不挑会员等级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOqUSQpyVbsuibTib5by53AgDF1ZRsSYAoFiaK1iaxMKQicUsS1vmbdicd1eia3jZBZjaD4xMO5IzCzG95yWoOwrXKypoeoDeQkibglvAk/640?wx_fmt=png&from=appmsg)

Grok Build 可能有小伙伴还没听过，这是 SpaceXAI 自家的命令行 AI 编程工具，对标 Claude Code 那种，在终端里敲一行安装命令就能装上，装完直接跟它对话干活。这次 Grok 4.5 也成了它的默认模型。

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNNmW7afg6BjcF4EJINWzduRzQNavL1qZSv5BormKHa7D2MTjOFsck6ibvibGWfduYl41ceqIzPkicmQPX7Fial7mZ3SsKka65Zees/640?wx_fmt=png&from=appmsg)

具体能用Grok 4.5做些什么？官方给了案例。

编程这边是主战场。官方放了一个演示，仅需一句话，就能打造出设计精良、功能完备的应用程序。

> 制作一个精美的宇宙和太阳系模拟程序。模拟速度应可调节，并包含逼真的运动、轨道和恒星。使用 Three.js 开发。界面设计应美观，并符合现代设计原则。

办公方面也很能打。

可以搭建复杂的 Excel 模型，一边联网查资料一边写跨表公式，甚至还会在单元格里留便签备注，方便你以后回来看。Word 和 PowerPoint 也一样，在 Word 中撰写清晰易懂的文字、用 PPT 原生图形设计复杂的架构图都不在话下。

> 拟定一份包含5张幻灯片的季度业务回顾报告。

推特上也有网友放出了自己实测的 case，效果很不错。游戏大神 Danny Limanseta 第一时间在 Cursor 里用上了 Grok 4.5，让它给自己在做的游戏搓出了第一幕 Boss 战，从构思、规划到实现一条龙，动画效果很出彩。

趁目前限时免费窗口还在，感兴趣的朋友不妨现在就去试试 ，很可能带来超出预期的体验。

Grok 4.5 只是一个开始。

6月28日，马斯克在推特上放出预告， **今年剩下的时间里，SpaceX 每月都会发布一个完全从头训练的新模型。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOHHuTj6ibwzaR6TgwRfQ0RTeLseTicxyOYzbGO31zWicGRaca9tWKtlnqEVSziaHJRsqvM1rn6dwENrR4sibwZh2UIia4VibXK4hUUrg/640?wx_fmt=png&from=appmsg)

按照行业常规，从头训练前沿模型的预训练周期通常以月计，这份承诺如果兑现，将给整个 AI 行业带来前所未有的冲击。

作为围观群众，这种月更节奏，想想就兴奋。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过