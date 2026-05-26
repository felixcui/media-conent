# 开源版 Claude Code，我拿它造了个 AI 分身

**作者**: 苍何

**来源**: https://mp.weixin.qq.com/s/AGnz7xYE88o5D1ef9TCdng

---

## 摘要

里面包括了我常用的 skill、公众号文章整理、还有我这几年沉淀的知识库。比如问公众号文章相关问题，调用 `/wechat-article-qa` 技能。苍何 苍何 在小说阅读器读本章 去阅读 这是苍何的第 537 篇原创。之前也折腾过 Claude Code、Codex、OpenClaw 这些，能力确实强，但有个共同的问题：你自己用可以，想把能力组合打包一次性给别人用，不好做到。

---

## 正文

苍何 苍何

在小说阅读器读本章

去阅读

这是苍何的第 537 篇原创！

大家好，我是苍何。

不瞒你说，最近后台积了一堆消息没回。

「生成视频的提示词是什么？」「这个功能需要哪些技能？」「怎么打通海外收费？」

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAYkdjYDFVicPEV4w13hM2Px5qZuIu7eBiaWXicboKYSdnHjm639s3866RVibMcJuElVWpWxldjfrv71fiaiaJuhFEpfrFxvmOELYIF4/640?from=appmsg)

说实话，每条我都想认真回。

但真回不过来，麻了。

我寻思着，不如造个「苍何分身」？

之前也折腾过 Claude Code、Codex、OpenClaw 这些，能力确实强，但有个共同的问题：你自己用可以，想把能力组合打包一次性给别人用，不好做到。

再加上要么闭源订阅，要么配置门槛高，Token 账单还吓人。

直到前阵子在 GitHub 上刷到一个很有意思的开源项目，OpenClacky。

![](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBqBU5zBdDHaXm0lZIQBn6KbO5BfvFczDvKUPvHNAjM452vTflIKOJvh9hy2sxdT3EtjLyXyRhqQ4nDZo0NMhJQDanRzjbPTLk/640?from=appmsg)

100% 开源，MIT 协议，本地运行，更省 Token，关键是它的 Skill 机制很不一样，不只是自己能复用，还能加密、分发、授权，直接打包给别人装着用。

我一看，这不就是我要的东西吗？

说干就干。

我基于 OpenClacky，搭了一个属于自己的 AI 分身，起名叫 CANGHECLAW。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaD2B5yJDPibAUWzOHAoJkGk6F9fTDs4eyNJKfRb3ibY60JTt99PibeRUHeOrMQR4zCiaSVlAxBYMkwRRwErwt80lQhyppArV4ZABib8/640?from=appmsg)

说白了，就是把我平时做内容的那套流程，用 Skill 的方式打包进去了。

里面包括了我常用的 skill、公众号文章整理、还有我这几年沉淀的知识库。

内容配图、AI 生成、格式处理、文档解析、平台发布、视频素材、笔记集成……

做内容会遇到的场景，基本都覆盖了。

还加了一些平台技能。

不知道该用哪个 skill？

有个 `find-skills` 工具，问它，它帮你找。

输入「/」，选对应技能就行。

比如问公众号文章相关问题，调用 `/wechat-article-qa` 技能。

回答简洁，还附原文链接，找源头很方便。

讲真，它比我回得快，因为它「读过」我写过的所有文章，YYDS。

我顺手让它给我做了一个内容生产自动增长的 PPT。

好家伙，整体风格和内容都挺能打。

我还让它写了一篇小红书帖子。

安装也很简单。只需要打开我给你提供的安装地址即可。

> 安装地址大家可以点头像私信回复获取，暗号：CANGHECLAW

下载对应版本，mac、windows、linux 安装包都有，也可以用命令行装。

懒的话，还能直接让 AI 帮你装。

![48b4ba694e8a4d61b5979ff784c753b7.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDvvsKuQgJvLkoLY5iayAqnAnWTjRLQoRJCykrU6xLTvY9Psd51uHY4briaYicvrder3NoMQtsWfvhgXUmFqQictABkxZqNZlib0icmI/640?from=appmsg)

出现等待，你就默默去喝个茶，等等就好。

![cead4f9811743718e5cc136835e7fb87.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCB2B96YxAYHBNxIqsiaB9dxQTLvC1hNeARibdRn90RexD2LOlRwYCvVqLS7ZgAXpvSfavGe4HD6zMmJWvZEEBmW0vBhStiagUzZE/640?from=appmsg)

服务跑起来就是装好了，点击在浏览器打开。

![b855aa6bbe1fd019977f781be46d4d58.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCx5OpoObZwvsx1Vc2bibD8w77sU8p2gItyhnAOAfwsnVLDaiagZ4VwA2y5CZdMgZ7Oex6sxgl8uib7MrMDlaKeyCZdu3KicAfCJ24/640?from=appmsg)

出现 welcome 页面，就能直接用。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaCrF8S98rnkJDibT68AzTOLKVUpJkTBfmJA7ibG661mWEUJAnl5E1oiaXib3ras9t95rSiaib2h69t8xypAJ6icBtH6TSPNuJSO4iaovWY/640?from=appmsg)

在品牌技能里，能看到我给大家准备的所有 skill。

![79c83c613036e1b333f0c41c5220400c.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAxJ2uCYJFw2a9Ex4b3eDAhFcawQbARXnNmibV0IBKuMNrWJaVulVKEhtGlxO5I6kkKTib8gy6A1vcOjEia6HUwJBib54hH1kAaBn0/640?from=appmsg)

有朋友问，这玩意儿到底咋做出来的？

其实没那么神秘，因为 OpenClacky 本身就是开源的，所有能力都摆在那。

第一步，把我 skill 仓库里的 28 个 skill 全装进去。

> 仓库地址我放评论区啦，自取哈。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAee9qZE31WB8kP8mn4JPY7vsLgiaJ0kTWUPZlhw57SYrDTn8WnsRvJ6OxjjEsgmmXG07mGMYGsVhBBrp25TvTnUqu9vhJdbeNc/640?from=appmsg)

然后就直接下达指令，让 Agent 开始装。

第二步，让 AI 把我公众号文章整理提炼，沉淀进知识库。

就这两步，成型了。比如当有人问：苍何，你的封面配图怎么做的？

开源的好处就在这，你想怎么折腾怎么折腾，不用看平台脸色。

整体成本也不大。

讲真，这是我选它最重要的原因之一。

之前用其他 Agent 跑任务，动不动一天二三十刀，心疼得不行。我还专门做了个压力测试，同时跑 PPT、营销任务、社媒任务。

结果出来我还挺意外的，三项任务跑完总共才 $5.10。

我好奇翻了一下它的底层，发现省钱不是靠砍功能，是架构层面的设计。

它只保留 16 个核心工具，长尾能力全交给 Skill 按需调用，不像有些 Agent 塞了五十多个工具，每次请求都带一堆用不上的 schema，白白烧钱。

再加上空闲期自动压缩上下文、Cache 命中率做到 90% 以上，几个因素叠在一起，成本就下来了。

不过客观说，它不是每个指标都最优。

Claude Code 在部分任务里的 Cache 命中率比它高，OpenClaw 在社媒任务里请求数更少。但最终看的是总账单，OpenClacky 胜在均衡，不偏科。

还有一点我很喜欢的是 BYOK，用什么模型自己说了算。复杂任务上 Claude，轻任务走 DeepSeek，成本控制权在自己手里。

加上 100% 开源、本地运行、数据不出门，对我这种做内容的人来说，安全感拉满。

做内容这件事，我想了很久一个问题。

为什么很多人明明有想法，却总是产出不稳定？

不是因为懒，是因为一个人扛所有环节，太多精力消耗在「执行」上了，留给「思考」的时间越来越少。

现在开源社区已经把工具铺好了，门槛比以前低太多。

你不需要会写代码，也能用开源 Agent 搭一个属于自己的 AI 分身，把重复的执行交出去，把时间留给真正重要的事。

遇到问题，评论区留言，或者直接问问 CANGHECLAW~

继续滑动看下一个

苍何

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过