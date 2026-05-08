# 12 天 4.2K 的 Star，我的 GPT-image2 开源项目火了！

**作者**: 苍何

**来源**: https://mp.weixin.qq.com/s/IR87TTG3XA9WRVIjqcRNZg

---

## 摘要

作者分享了其 GPT-image 2 开源项目在 12 天内获得 4.2K Star 的经历，特别指出该项目及配套可视化网站均是在医院陪护期间，全程不碰电脑仅靠手机远程指挥 Codex APP 完成的。作者认为，相较于黑盒式的 Agent 模式，Codex APP 凭借强大的浏览器和电脑自动化控制能力，在代码编写和功能测试方面表现更加智能丝滑，展现了全新 Agentic Coding 体验的巨大潜。

---

## 正文

苍何 苍何

在小说阅读器读本章

去阅读

这是苍何的第 530 篇原创！

大家好，我是苍何。

说实话这几天都挺郁闷的，放假 5 天就有 4 天在医院。

我家娃一生病起来，就不要爸爸，只要妈妈，我就只能干些辅助工作。

看看针啊，拿拿药啊啥的。

其他时间，我就拿着手机连上我的 Mac mini，指挥 Codex 帮我搜集提示词，并迭代 GPT-image 2 开源项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zw8bZHsVSaBlJuQAJLB2r2bgOx7iceERDdOA9ceDM7HHdPFxY1cyc5TyqrXaVU6ahM8Py3JAXBps0ooXftPgSLDSvoZLleIyTZcjricpvfOfA/640?from=appmsg)

我今天去看了下，现在已经 4.2 k 的 Star 了，而且还在涨。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDicMy2xnh0Ek9eniaiaTEqCn8V6Mb9icJichib4A7rWcmv0NG1lIo4LuGc6SZWQFnBWtkBPSD3X7TLNQ1kS9A90VBDxw42XIsKjicSPQ/640?from=appmsg)

从发布到今天刚好是 12 天时间。所以我打算写一篇文章，好好装装比。

呸，是好好分享下，我是怎么在医院不碰电脑的情况下指挥 Agent 做到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAIoXEhxWibHqOEhMGicYibLaGic9NmibggicIteTrxj5dtRibsTRicFibEzGdDiaT7cdWhDKG4Hzje0q07uEAHEQ24497YbPOxqibcFIzGqI/640?from=appmsg)

除了用来做提示词的挖掘，我还指挥 Codex 帮我完成了配套可视化网站的开发。

他是长这个样子的。

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAmhpFvnowP47vpYV5zCTfWiaHfZ6QfFRfnYE56WZr2f5sjMfw39lawicIgkDK6ZEjEH8TjNrvm6eydQUibPiaU1Eo980CE1YF0iaWY/640?from=appmsg)

我稍微录了下功能视频，你可以大概看下：

对于分类场景下，找提示词也更方便了，选择分类、风格、场景，你就能快速找到想要的提示词：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDbgJcrUd9OvR1bR6qQ64ID7SOBqWywoTbaSiaGYnRAoXVg1j5biasphIibia2nCDfgEcia6kHVfh4MPT3icXjZ9crq18cZLvJUicxnYI/640?from=appmsg)

开源地址和网站地址在这，你完全可以毫不留情的收藏点赞，以备不时之需。

> 毕竟我这几天已经迭代了不少版本了。

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAYmWI02XeUx5pwY3xuQNhMp7Hzic6s4VXERAkuyBDAf5RqicDSgQ7PcsaGia9IWtywhFthauFAC1w69m364OUbiaJXnzCdYZzibnIU/640?from=appmsg)

```
开源地址：https://github.com/freestylefly/awesome-gpt-image-2可视化网站地址：https://gpt-image2.canghe.ai/
```

这次的全新 Agentic Coding 体验，让我意识到一点，OpenClaw 的黑盒子式的 Agent 模式，可能还不及一个远程指挥 Codex APP 来的丝滑。

我通过飞书去连接龙虾，然后让龙虾指挥 Claude Code 来 Coding，我已经跑了一段时间，我发现，对于功能性校验测试太不丝滑了。

我发现 Codex APP 在 Browser Use（浏览器自动化）和 Computer Use（控制电脑 APP）太智能了，它能自行打开 web 页面，查看 bug，还能自行打开电脑里面的 APP，用 Agent 控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAHWPltcLr14ePL3KnKe2OxGuRI0VnvM9LrGaKAbrl6kdDSvg62lCwhkfibKp8v6MRxtenhnuBriahjbvUjiaxtEibOz7qQr9u96tI/640?from=appmsg)

就比如搜集 X 上最近 24 小时 GPT-image 2 的提示词，这个就不一定要配 API 了，配合 Codex 的 Browser Use 能力，它能自动打开 X，搜索并浏览相关信息，找到有 Prompt 的帖子，然后下载图片，提取提示词。

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBuVSS1ibV9LaVIO1cIibN1HmYKzETSmC57z3YRH2MZlAtaiaGSXON8v4nxVzpNPJTq6CVB3B8NXU44cnGnwyCicibnplgGO2DPUrGI/640?from=appmsg)

然后按照我 GitHub 项目的分类规则，自动放到分类下，如果有值得提取的模板会给建议。然后给到我做确认。

> 我还在这里设置了个 10 分钟之内不确定，自行决策是否发布的规则。

最后通过 GitHub 到 Vercel 实现自动部署，网站也能实时展示最新的 case 案例和提示词。

你会发现，这个流程我搭建好后，我全程只需要做最后的确认工作，看看这个图怎么样啊，分类对不会啊，值不值得提炼出模板啊。

其他都交给 Codex 就好了。

设置一个自动化规则，每天让他去跑，我来做决策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaBqQxiaTegVJ9A1qnojv7lLHTUZeL3eJTP275EEEZOwfslDggDtJGvQKCDGmr1bEYbiaibU7DOpSPHxuicT5hEMIKnKMrjLCTOtzto/640?from=appmsg)

我的 Codex APP 泡在 Mac Mini 上，电脑、手机或者 Ipad 可以直接连上，24 小时指挥他干活。

截个电脑控制的图吧，也非常丝滑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaB81iaibkNSvxD4pugTdo0bUWMTicrIlUibmq9TeyzdBRib2YFXocPa5VUH5icKgHzMhkq4iaWzzgSWCfusdROyEAvHu9yW2m9xicibDARk/640?from=appmsg)

要想实现这个工作流，第一步，是需要安装必要插件：GitHub、Vercel、Browser Use、Computer Use。

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaChiajBHialuic6O4rOrE7TBGkiclibbusqhkhegSeM1iajBXmfiaOpAzPtqgu1kMmUKLzTTx1EnHHgthN8LrO09gmh545NaM7IovbjEI/640?from=appmsg)

> 当然，这里如果你本地有 GitHub cli 或者 Vercel cli，也可以不安装插件，做的事情是一样的。

然后在 Codex APP 中你要选择你的项目文件夹，以后所有的改动都是基于该文件夹的，而且该项目后面是会直接和 GitHub 项目连接的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAaXUzB3wxXDWicaUUFkibwkGqp4rJ9cHibEekpy3giblz54ibZic7aT012tWibDm1TOVsrXcUDAQRyFk9yDD0De5fKXz8dLbpWDrHcVw/640?from=appmsg)

这里如果自己电脑是非工作机，可以直接放任 Codex，开启完全访问模式，这样，你就不用每次都点击确认授权了，直接开干。

我用的是 mac mini，本地也没啥隐私数据，直接就让它放飞自我好了。

然后是描述需求，OpenAI Codex 团队在分享他们如何构建 Codex 的时候，有个观点特别有意思。

**「少写规格文档，多做原型」**

Codex 团队不是传统 roadmap + 大 PRD 模式，而是短期判断 + 长期方向，中间靠原型探索收敛。

他们甚至很少写 Spec 文档：

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBxedsZP74gLzJE0f0mLbbTictyGhaSibVuVAadLPwlIibxTUAlro9m10e2eyl4VybFuULTlXXfS4BfafL0eOlA5ia6BPicfgk048mc/640?from=appmsg)

基于该观点，直接向 Codex 描述你的初始需求，让 Codex 理解你的意图后，再开始开发，你可以反复和他确认方案，而不是一上来就让他执行。

建议分开任务层级做不同的 Chat，比如我这个项目中的搜集 Prompt 和网站的开发，是放在不同的任务的，当然跨项目也可以通过工作树的方式串连起来。

你看我的需求描述，其实还是通过 typeless 语音直接下达的指令，不够复杂，但足够精准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAiaV9KHSGjaFrKCI0jbcKIVlIVJOAKqJib5sgCR9VvMG5oqc0yia4envmFYKbv3AfpwwVXNsLHPjHRoiaMLSz4zXf7PIcrzOicZ9yM/640?from=appmsg)

如果你遇到比较好的网站或者开源项目，你可以直接丢给 Codex APP，他会帮你打开页面，然后学习，之后模仿，最后按照你的要求改造成你喜欢的样子。

对于网站，搞个域名，然后解析一下，通过 Vercel 自动就能部署好。

全套流程大概就是这样子的，为了方便你理解，我让 GPT-image 2 花了个图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAIoXEhxWibHqOEhMGicYibLaGic9NmibggicIteTrxj5dtRibsTRicFibEzGdDiaT7cdWhDKG4Hzje0q07uEAHEQ24497YbPOxqibcFIzGqI/640?from=appmsg)

最近用这套流程搞了不少事情，除了开源项目，还重构了 Wesight。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zw8bZHsVSaCQIE1omRcYzTj6HGh3geJpkUXxOE5mbm6TmRzPA80rgywKMTcsGW7wqFaHgAicRm1BVH7fPkoD3WmlQjdiajj7IDjm9g7IKu5R4/640?from=appmsg)

重新梳理了个人网站：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDouNQfRfuJM3mLQ4Jp5B2RFDfcfhJe6tp59LDEw4T3Ud5qRU2EoIYFS2ZZ5sos5D9ESuk5LFFic5fb5Ye1iclYEsiasCHmu2Bmtc/640?from=appmsg)

当然了，还有在实践 Codex 深度使用后，也做了另外一个开源项目 CodexGuide，域名也已经买了，就叫 CodexGuide. ai。

开源项目也悄悄放上去了：

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaCYe8y2unLibJwDe3TSLoF2WPhyBSTvicxCP2oddI8WgDaJTRiciafpnbnP2l4piccno6gFocaRePOL1OlzhhzUTSh6RILAh9qHYVHM/640?from=appmsg)

他是Codex 从入门到精通 · 面向中文开发者的系统化开源教程知识库，目前还在努力完善中。

> 如果你看到了这里，可以顺手 star 收藏下，这个开源项目也会持续更新，更多 Codex 的实践教程也会放上来，毕竟域名都狠下心买了，野心不可能小的。

所以，这就是我的五一假期。

在医院里，通过一个手机，指挥 Codex 帮我完成的这些工作。

说实话，这些任务加起来，以前至少要花个十天半个月的，现在，几天时间就可以了。

而且，也取得了阶段性的成果。

我分享这个工作流给你，希望你也能，充分利用好自己的碎片化时间。

一起通过 AI 做点有意思的事情。

如果觉得有帮助，可以毫不留情的点赞、转发，哈哈哈。

阅读原文

继续滑动看下一个

苍何

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过