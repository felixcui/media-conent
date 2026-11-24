# 十分钟生成 Vibe 知识大赏爆款视频，OiiOii完整工作流分享。（附提示词）

**作者**: 大刘

**来源**: https://mp.weixin.qq.com/s/FSbuUo_7XQaICbtbxL79jw

---

## 摘要

讲的是抖音上“Vibe 知识大赏”这类知识动画视频怎么做：用代码把硬核内容做成动效，信息密度高、流量好，但过去基本只能靠 Claude Opus 写代码，国内用户光“用上 Claude”就被挡在门外。作者的解法是 OiiOii 的 Motion 功能：模型里可直接选 Opus 5.5，也有价格约它二十分之一的 DeepSeek V4.1 Flash，效果够用，适合低成本做知识讲解；成片可导出 4K、最长 180 秒，正好覆盖抖音上一两分钟的知识视频。工作流很简单：素材要么自己备好、要么在提示词里写清让 AI 去搜；有合适的风格模板就选，没有就让模型自己发散；填主题、选 180 秒和模型、生成、一路点确认，最后导出 4K MP4。作者自己的总结是全程只干了两件事：给提示词、点确认。

---

## 正文

大刘 大刘

在小说阅读器读本章

去阅读

![大刘品牌动图](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc0ibI1LxwZWLmXHvbmRHFibaf7jBHIvQEPptcMDh9RV7URcOhJKvZxPibFMp3NM0g1mr4YrFjuyDzibInBMgL0gNwpr8t431bMYbOc/640?wx_fmt=gif&from=appmsg) ![DALIU · AI 品牌字标](https://mmbiz.qpic.cn/mmbiz_png/J1Cdba5GUc2rYkJbOvcbibofkATHibyA2ib0msKP5ypnlk6SLaR8sC4ESFBvrxh3ewF814t4oMOKAiajhhnibEeFZnSmNPfaH8PZcciatjEfrRiaqI/640?wx_fmt=png&from=appmsg)

Vibe 知识大赏，可能是现在抖音上最简单的起号方式了。

相信你也刷到过，讲军事的、讲大模型原理的、讲生化危机编年史的，反正就是各种各样的知识科普视频。。。

给不知道的朋友简单解释一下，就是用代码，把一些硬核的干货知识做成动画讲出来。

这些视频动则几万几十万甚至上百万的点赞。

![抖音上两三条 Vibe 知识大赏类视频的播放页，如算力科普、生化危机编年史](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1JTwVI3hniaK4CmQx8E3YJCjWg5hrJcUvuhQYS6pSos4w0pxTBI8YKc3TkEYlNFcTIZN9icOEOKaQ58mPEU6ME7CxNjEBLHtJ9U/640?wx_fmt=jpeg&from=appmsg)

我前阵子刷到停不下来，一条一两分钟，信息密集得要命，而且页面也很清晰，看完真觉得自己学到了点东西。

但是这类视频，绝大多数都得靠 Claude Opus 这样的顶级模型来写代码效果才好，对我们国内的朋友来说，光是用上 Claude 这一步，就已经把一大半人挡在门外了。

直到前两天，我发现 OiiOii 也上线了 Motion 动画功能，专门做这种视频的。

模型里 Opus 5.5 直接就能选，还有一个价格只要它二十分之一左右的 DeepSeek V4.1 Flash，在保持效果也不错的情况下，很适合低成本做知识讲解类视频。而且做完能直接导出 4K，最长 180 秒，抖音上那种一两分钟的知识视频，完全够用。

![本篇成片视频（视频位），或成片里信息最密的一帧](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2CUkWhB65blEkN2iake87lLbUytF74DF14FUVlrTdo2veAMWoh1iaRB1hl7tCdXMz32CVeYy9g630oXCL7XgIxUFAqLhxEC1NOM/640?wx_fmt=jpeg&from=appmsg)

所以作为 AI 科技博主，我也必须上手开始做知识视频了。

就拿之前大家都比较喜欢的一篇文章为主题，用 OiiOii Motion 功能给大家出个 Obsidian + WorkBuddy 教程的 Vibe 知识视频。

最后做出来的成片是这样的。

你看一看，这个效果，放在抖音上刷到，我是会停下来看完的。

所以今天这篇，我就带你从头到尾梳理一下做这样的 Vibe 知识视频的全流程工作流。

手把手教程，现在开始。

1.

素材准备和生成。

知识大赏这种视频，说到底要给观众输出的是干货和观点。

可这偏偏是 AI 视频模型最拿不住的。每个画面又是字又是图表又是数字，直接让视频模型生，文字和数字肯定是错的，画面和讲的内容还经常各说各的。

OiiOii Motion 用一句话就能生成一个视频。Agent 会自己去搜资料，然后配上 2D、3D 的动效，做成一条完整的讲解视频。

具体做起来，第一步，就是确定我们的主题之后，准备需要的素材。

素材的来源主要两个方向，要么是准备好，要么就在提示词里面非常清晰的写清楚，让AI帮我们广泛的搜索资料。

比如我这里，直接用那篇 ima + WorkBuddy 的教程。拿来做知识视频再合适不过了。

打开 OiiOii，🔗： OiiOii.tv。

在首页选 Motion 这个 Tab。

![OiiOii 首页的 Motion Tab 和输入框](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc0KPSFSibYZppQmVEdeaY27JRurPricdTQufnQU0Wq2icf7mqiaF7HguQ04krAEsQC1XDqet4JLD2GeCGANPSGH2qqPciaaCDalpM0Y/640?wx_fmt=jpeg&from=appmsg)

在输入的这里，OiiOii提供了很多的模板可以选择，比如说手绘风格、贴纸风格等等。

![](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc0rP87wV9mocj4SnGgnnJBVp2YhNhaW1yLImYbNRYkDnw5xPJnmvpxw1zRV3rRSg7TcqkcAxOB4RSZicalArAicQ1gAkTDd4NYXw/640?wx_fmt=gif&from=appmsg)

如果选择了模板，那提示词部分就会准备好，然后有一些留空，我们填上自己的主题和信息，就可以直接生成对应风格的动效视频。

比如，如果我们选择手绘风格。就会自动填充手绘的提示词。

![OiiOii 首页的 Motion Tab 和输入框](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2ruUQkVHTEtpbL7A0STnicbQnlqViaEQKOaIZJxZ6BgZic8wmmXEB40Ymy0dhN9rqL1xgs5xv9ZBhWolQbajevDb47fmufxiaG5fQ/640?wx_fmt=jpeg&from=appmsg)

这里，我的经验是，如果你有觉得和主题很适配的风格就直接选，如果没有，就直接让Opus自己发散风格，最后产出的视频会更适配内容。

我这里就没有选择风格，直接把我们想做的主题输入进去就可以了，这是我给到的提示词。

●●●

现在我想制作一个知识讲解视频，主题是：ima + WorkBuddy 的教程。  
  
请主要参考我给到的教程文档进行逻辑的梳理和搭建，你也可以根据相关的内容搜索大量的资料进行丰富。  
  
制作知识讲解视频！

然后这里我选择的是180s 和 Opus 模型。

直接发送。

在整个过程中，OiiOii 艺术总监会调用非常多内置的专业视频功能来分析我们的需求、资料，并且从专业的角度来制定整个视频的风格、动效和分镜。

以及，会提醒我们进行配音的确认。

最后，一路确认下去。

生成完了之后，就已经可以在整个界面中看到。

主要分几个板块，左边是Agent，中间是成片，下面是时间轴，字母、视频、音轨都划分了，可以手动剪辑，右侧还有每个页面的具体素材。

先简单看一下所有的页面，一次成片，整体完整性已经超出我的预期了。

每个页面的风格都非常一致。其中的动效也和讲解的逻辑完美契合。

![](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc14iavVlhvMgibibKGyKXWTVT7aHibWPVOCkZfXfjEPGtw4s60ib6vb3NnjiaXKgcsbMQ62TbJx6gciaNvibXmSaflFmlfLWLJMjvpDyoE/640?wx_fmt=gif&from=appmsg)

回头看一下整个生成的过程，我自己其实就干了两件事，给提示词，再一路点确认，就获得了这样一条视频。

理逻辑、定风格、拆分镜、写动效、配音，全是 OiiOii Motion 功能一次性做完的。成片，不说完美，我觉得百分之八九十，是完全达到了的。

2.

Agent 对话修改。

当然还是会有一些需要二次修改的地方。

OiiOii 的 Agent 支持通过对话的方式修改视频，不满意的地方可以直接让Agent调整，完全不需要像传统视频生成一样重新抽卡。

比如说，我就发现字幕有点问题，一个字幕太长了，会让观众看着不舒服，甚至还出现了没法展示完全的问题。

![OiiOii 首页的 Motion Tab 和输入框](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc0YKanNlqR8005TKqFkvFibur6DKLuGKsTbBzpDibO7VGBMELS9lLQekEJQc37L1dHujl0xlIaetMO7569UibnicOnv1nw3fTR1YoU/640?wx_fmt=jpeg&from=appmsg)

对于这种问题可以直接在左边的 OiiOii Agent 里面发修改意见，大白话就行。

Agent自动修改之后，就会是非常细的字幕了。

在时间轴上，之前是大块的字面，现在已经很细了。

这一步要是放在 AI 视频模型里，字幕一出问题，基本只能整条重新抽，抽完说不定别的地方又崩了。

OiiOii Motion 就可以通过 Agent 调整视频后面的代码，来完成精细化的调整。

这里也总结下我的经验。

对于整只视频都存在的问题，可以一口气进行调整的，通过Agent的方式，表达清楚，基本可以一次性修改到位。

3.

元素级别精准修改。

对于我这种完美主义，其实很多细节我都想抠一抠。

比如说字体大小啊，某些标题的表达之类的。

OiiOii Motion 的编辑器恰好可以解决这个问题。编辑器会把每个页面中的所有内容都抽取出来，列在右边，文字、滤镜、背景音乐，都是单独的元素，可以一个一个改。

比如这里，我觉得「架子」这个词太 AI 了，会让观众看起来有点反感。

就可以直接手动修改了。

当然除此之外，还可以调整滤镜等等。

以及在素材里面添加背景音乐，加入到视频中。

其实用编辑器修改和上面用Agent修改，都是针对视频内容进行调整。只不过稍微使用的场景有点不一样，我自己的用法是，整条视频的通病就用 Agent 改，等它改完，再进编辑器，把那些只有我自己在意的小地方，一个一个细节抠好。

4.

4K 导出，字放大了也不糊。

至此，整条视频完全满意！可以导出了。

点右上角的导出，可以选 1080P 或者 4K，它会把动效、视频和音频合成一个 MP4，我直接选了 4K。

最终的成片就是文章开头的那个。

这里我觉得值得讲的是清晰度。真 4K。比如说这个页面，图、文字都非常清晰。

![4K 成片截一帧，放大到文字边缘的局部](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc0o8XE6N0zZQicbgPyTqDsf4bRCEYicRZP8cpLib3QChupibhMAGjZw4ibmMOhiagVGznqP0YNTFhE6J2dJTc5UZfDWNAy96oOu31dRs/640?wx_fmt=jpeg&from=appmsg)

能这么清楚，其实是因为它根本就没通过生成视频的方法，而它们干的活其实是写代码，每一帧都是一个带文字、图形和动画的网页，最后再一帧一帧渲染成视频。

我们在各种视频平台看到的 Vibe 知识科普视频，基本全是用的这个方法。

而这个方法，之前需要 Claude Opus模型 + 动效Skill，再加上自己的审美。

现在 OiiOii Motion，直接全包了。

以上。

就是从零做出整套 Vibe 知识视频的工作流。

实际上 OiiOii Motion 的能力不只是这样的 Vibe 知识大赏视频，还包括公司的宣传片、App 的功能演示也都是可以一次性出片的。

比如，OiiOii 和观猹最近在搞一个联合招募，面向企业、品牌和团队，用 OiiOii Motion 给自家公司或者产品做宣传片，OiiOii 来提供算力支持。给观猹做的宣传视频就是这样的。

效果还是很惊艳的。

最后。

真的很感慨啊，一两年前我是对视频制作一窍不通的。但是这半年以来，我也逐渐逐渐变成了做视频的老法师。

到现在我其实还是不会用AE那些专业工具，但是在 OiiOii、Seedance、Motion 这些AI工具的加持下，我已经做出了很多不错的视频。

Vibe知识大赏也好，短片短剧也好。

能够把自己对知识的理解分享给更多人，真的很有成就感。

好玩多玩儿。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章你的关注是我持续更新的动力～

我是谁

我是 AI大刘，北大毕业，大模型研究方向，腾讯犀牛鸟，先后在腾讯、百度的大模型研发部门。现在斜杠青年：给多家国企做AI顾问 \\ OPC \\ 研究员 \\ 产品独立开发者 \\ Vibe Coder

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过