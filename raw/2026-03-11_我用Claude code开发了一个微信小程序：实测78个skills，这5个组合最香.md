---
url: https://mp.weixin.qq.com/s/Uc5u1N4D8HVkKuILhe8EAQ
title: "我用Claude code开发了一个微信小程序：实测78个skills，这5个组合最香"
author: "R.Zen"
coverImage: "https://mmbiz.qpic.cn/sz_mmbiz_jpg/0hd8MxUumHNmYrjKQ9OGkLyicM7jskx8QlNDROgzBg3VUkfpias3DaNZLk07j43E7kicGpUWpAQsPKMLvwhtEk2uMeN29BUichFzibrMguQ3kib14/0?wx_fmt=jpeg"
captured_at: "2026-03-11T06:16:39.309Z"
---

# 我用Claude code开发了一个微信小程序：实测78个skills，这5个组合最香

Original R.Zen *2026年3月10日 14:40*

![Image](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qH0XkVXvKZTjHu2KEOcu6o260lH2JX5Y1Bpdnh9gFsmkE1UkDgrPKzKLNfChL4ldWQIrsYst2d0sg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

朋友们，先问你们个问题：你们的 Claude Code 里装了多少个 skills？

反正我那天随便一看，居然莫名其妙装了 78 个了。

![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHO1Oic2Ar6DGHNrO7wlUpoJ0hURMK6jZUoib1stbgicczodvj7uBmXeHEaEttTDlgszArHjKwooibfeLyMVt9m9wsCiatLYwgfBTxQM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

有多少人和我一样没事就去 skill.sh 逛逛，看到热门就下，管他有用没用，先装了再说。

skills 就是新时代的点赞收藏永不看。

但是呢，前几天我朋友在我帮他下载了 Claude code 之后，问我：

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/0hd8MxUumHOSHm8dyQKmRuD0q2ekkOleictrh3lrRWLrO4N2oPK5OVELIibMn5ue9hicZhWGtria9EEbgaON6BhWbibWtuxdosPFubeIkb1x19EI/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=2)

我想了想要是一股脑给他 78 个，估计他会骂我。。

我就问他要用 cc 干啥，他说他想 vibe coding。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0hd8MxUumHN2IHlOlhyM1EiaKDzuTKknOfupU3pBe8busYC2co31Sl09hKP4AEwsus7GpdeHk0jwg2Iuoewuf6zBhOibYHAJOeVyV2HgWNlSc/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=3)

好，这就有的聊了。

正好最近在开发一个「资产管理 + 人生目标」的小程序，我就借这个真实项目的过程，给大家整理一下不同开发阶段的 skills 组合拳。

## 阶段一：原型阶段

大家都知道，开发的第一个阶段，肯定得先想清楚再动手。

但问题是，一开始我也不知道该怎么做这个小程序。

只是觉得市面上那些记账软件功能都太单一了——记完账就完了，钱和目标是脱节的。我想做一个能把资产和人生目标可视化挂钩的东西。

可具体要做什么功能？目标用户是谁？和其他记账软件有啥区别？

一团乱麻。

这时候我就想到一个词「brainstorming」。

让 CC 帮我头脑风暴一下。调用一下 **brainstorming** 这个 skill。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHMTeMbkCIibHroFlRsacVdeLL5b1TjACqb8wChpIejc5Gdh5mSic0R58z1iaXIKo5jVpntMo98nxAqmMzu1SIhwa7SW0ibnA5UrpoA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

> npx skills add https://github.com/obra/superpowers --skill brainstorming

生成了超级长的一个回答。

一堆想法哗啦啦砸过来，什么“资产配置建议”、“里程碑庆祝动画”、“情景模拟器”……我承认我贪心了，全都想要。

但全都要等于全都没有。

我意识到问题出在哪了。也许我的问题太宽泛，AI 只能给宽泛的答案？

这时候我换了个思路，直接跟 CC 说：

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOPqE092odTFDQGbETEW3PSV2zUSpF6d91T020bkiaicvN1H2x1iapicYXkMTUnP6DA0W5NLia9RFVljb9lp9iaicMro5icmMqib1zoiaiaRQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

你看，这样一下就清晰多了。

CC 一共给了我十几道选择题，从产品定位、目标用户、功能范围到技术栈偏好，像做心理测试一样。

我一步步选下来，产品形态就自然浮现了：

- 目标用户：刚工作的年轻人（22-28 岁）
- 核心痛点：有买房/旅行/学习的目标，但不知道每个月该存多少，也管不住自己乱花钱
- 差异化玩法：资源分配博弈——像玩策略游戏一样，在多个目标之间分配有限的资金

只能说如果没有 brainstorming，我可能会做一个什么都有的大杂烩，最后四不像。但通过选择题逼自己做决策，产品定位从模糊到清晰只需要几分钟。

而且，像“资源分配博弈”这种选项，反正我是想不到。这就是 brainstorming 的价值，它帮你跳出思维定式。

## 阶段二：UI 阶段

确定完产品方向，按理说该写代码了？

别急。

这时候我的脑子里已经有一个产品概念了，但是它具体长什么样？用户怎么玩？我还是模糊的。

直接写代码很容易跑偏，写到一半发现这个交互逻辑不对，再改就很痛苦还浪费 token。

所以我先做一个 **playground** 。

啥是 playground？简单说就是：用来实验、测试、随便玩的地方。

一个不用担心出错、可以自由尝试各种功能的实验环境。

这里是我从我的偶像「张咋啦」那里学到的。确实很有用，有效提升效率。

但 playground 就得有界面吧？UI 设计成了第一大难关。

那我肯定是不会。所以这个阶段我也找了几个专业设计 uiux 的 skills。我用下来对我帮助最大的是 **ui-ux-pro-max。**

> npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max

这个 skill 内置了 50 多种样式、97 种配色方案、57 种字体组合、99 条用户体验准则以及涵盖 9 种技术栈的 25 种图表类型。

一开始我也踩了坑。因为上面的对话并没有特别多的涉及审美。第一次出来的样式就很普通。

我需要给 AI 足够的设计约束。

于是我换了个引导方式，把我的产品定位翻译成设计语言：

> 这是一个游戏化的人生 RPG 小程序。核心交互是'资源分配'——用户像玩策略游戏一样，在买房、旅行、学习等目标之间分配资金。
>
> 设计风格要：年轻、有游戏感、但不幼稚。用色要清新，避免传统理财软件那种'严肃的蓝绿色'。参考风格：Monument Valley 的极简几何 + Duolingo 的激励感。"

这段话里就包括了：产品调性（游戏化 RPG）、核心交互（资源分配）、目标用户（年轻人）、参考风格（具体游戏）和要避开的雷区（传统理财软件的严肃感）

这样 AI 才能 get 到你的设计意图。

微调过后，生成效果就是这样啦。

我感觉很不错，尤其是这个配色特别清新。

现在 idea 的模样是清晰了，但具体怎么做？先做哪个后做哪个？

这时候我会召唤 **planning-with-files** 。

> npx skills add https://github.com/othmanadi/planning-with-files --skill planning-with-files

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNF5wpca780Z31jDK8GsiaicQOaQUaSvQriaYwBUDiaVkM3Hzhk9JZ1HoG0CoXAtgYaGpj1kYQsnYpu4OR1OQzmfiaGbX18Y1SROdzk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

这是 Manus-style 的规划方式，会帮你创建 task\_plan.md、findings.md、progress.md 三个文件。

亲测建议：小项目别用，大项目必用。

我这个小程序虽然不大，但涉及到云开发、数据库设计、UI 设计、审核上架几个环节，用 planning-with-files 梳理完之后，整个项目的里程碑特别清晰。

![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHMQKibJeApPN8QNR7r6wGWiaVnzIlFZXMcHX73h0fqpUtFRHzQ7pV7ffphydDLO7m7Tiapu79CCGAibXVsu1jyQpzG7oCj3yBFn9a8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

而且最爽的是，你可以随时丢给 AI 一句“我现在做到哪了”，它能准确告诉你进度。

这对于我这种间歇性老年痴呆很管用。

## 阶段三：开发阶段

playground 跑通了，规划也有了，终于进入正题：写代码。

但先别急着 cmd+N 新建文件。

微信小程序的开发有个特点：它既是前端，又不是纯粹的前端。

我还要考虑：

- 微信特有的 API（登录、支付、分享、扫码）
- 云开发还是自建后端？
- 分包加载（小程序有体积限制，不能超过 2MB）
- rpx 适配各种屏幕
- 审核规范（有些功能会上架被拒）

最可怕的是调试成本。

每次改完代码要重新编译，真机测试还要扫码预览。如果没有测试兜底，你就是在裸奔。

所以我这个阶段用了 **test-driven-development** ：

> npx skills add https://github.com/obra/superpowers --skill test-driven-development

先写测试用例，再写功能代码。

![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHPkWVnUv27SbNaLPaQFEFuWkUwmfKxhicjwnob7woKmz7oRkj3JS6SFUKrmmB1RqiaDKp8v8bTfcVibkNUeF4rPhXZKm1Dhm7icWow/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

比如核心的“资源分配计算”——用户拖动滑块调整买房/旅行/学习的资金比例，系统要实时计算各目标的完成时间。

![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHMU2jB3sgdCeB0uqy7icccVvlq0fuQbctKia4jcDibNmedvckwAibWmTCaIdviaz0hicpEu0nbwoiaBknnjJeNVh0IxE7icjYjKribNibia1g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

这个算法我写了三遍：

- 第一版：简单平均分配
- 第二版：考虑目标优先级权重
- 第三版：加入“资金池冻结”机制（已存的钱不能随意挪用）

因为有测试，每次重构我都能秒级验证对不对，而不是手动输入一堆数据去试。

测试有了，可以开始写小程序代码了？

对，顺便分享一下我在这里摸索出来一个小技巧。

当我直接跟 Claude Code 说：现在根据 playground 的演示，生成真正的小程序代码，前端设计完全按照 playground 来不要自己改。

因为 Playground 是 HTML+CSS+JS，小程序是 WXML+WXSS+JS。第一遍生成的代码，大几率会有 bug。

这时候我 PUA 了一下 AI：你一定要以一个完整成熟的小程序产品的角度去修改代码，不要从简。有什么困难先自己上网搜解决，我相信你有这个能力。

它真的去搜了微信小程序的官方文档，自动修复了几个问题。

折腾了一天，最后的成果就是这样的：

做个前期的 demo 还是绰绰有余吧。

## 阶段四：沉淀阶段

项目做得差不多了，但还有最后一个骚操作。

和 Claude Code 的对话先别 exit，来和我一起发这句话：

> 基于我们刚才写小程序的对话，结合 insights 报告给我整理一下我以后可能需要生成的 skills

这就是我们这套组合拳里最后一个 skills。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHMuoVGwAwWiaENiaxNpEPyEWVRkKnd1g9xacyq8hRicdBxmwnEJkNS3WYzhGiaYTR11lfiar2Y7d6wDfJcn4aZ2fWkyloLRibiaEu5ozo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

当然，这里可能生成的就不只是 1 个 skills 了。你可以基于自己的开发习惯，提炼出专属的 skills。

五个 skills 表格总结如下：

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHO8WkThqBjYBeqUMDGHUQqQkkibXlFh6ntjggrUdewRBIG9KfpEQYa09iaaHBDY7r666nd1K4X3hNfvPl7wPIgU3TicCIhdCDMPsI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

最后说几句。

其实 skills 这东西，真的不是越多越好。

我朋友听完我的推荐，只装了这 5 个，昨天跟我说：“够用了，很清爽。”

我想了想我那 78 个 skills，很多可能从头到尾就没打开过。

所以这篇文章，也是写给我自己的。工具是为了解决问题，不是满足自己的收集癖。

找到适合你当前阶段的 skills 组合拳，比拥有一整个军火库更重要。（当然，看到新的 skill 我还是会忍不住点 install，这是病，得治。

你的 Claude Code 里装了多少 skills？欢迎在评论区晒出来，让我看看谁是真正的 skill 收藏家

![Image](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qEyDKnkjcT4bd38ljNdEGscMzUYibunoJ8KWC3aUv6EUpdes1rbU2Kp7TQXqFwMicLuciaz9q7tiaI3UQ/640?wx_fmt=png&from=appmsg#imgIndex=12) ![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHOhnBXibubciaUofvVWWmibdfCgzy4pzSbsPICBPicvJeF1x0GfhawodKNkb5fiayZzyCWetBuDCCF2EG8ic7WfeJFvptV8uVHt2lIYA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13) ![Image](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHMFBkE4rnibaI8AsAaUpf6iaVBgicUZjdGQTLOEwpZ97WCqWNkD1n6aKb4Oz5LBf3AX317SNXFFxib4ricJqicqAaT9mSIur1MhZWHsk/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

继续滑动看下一个

夕小瑶科技说

向上滑动看下一个