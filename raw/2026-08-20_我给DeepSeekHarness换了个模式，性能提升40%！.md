# 我给 DeepSeek Harness 换了个模式，性能提升 40%！

**作者**: 程序员鱼皮

**来源**: https://mp.weixin.qq.com/s/Ao1PtMH5ioVfCTuTrLjt8g

---

## 摘要

本文介绍了 DeepSeek Harness 进阶玩法中的核心概念 Agent 预设，即决定 AI 工具选择、提示词遵守和工作方式的一整套模式配置。文章强调针对不同任务选对预设能显著提升效率，并详细拆解了官方内置的四种模式，其中默认的标准模式集成了二十多种工具，能像 Codex 一样全面应对绝大多数 AI 编程与自动化办公场景。

---

## 正文

程序员鱼皮 程序员鱼皮

在小说阅读器读本章

去阅读

大家好，我是程序员鱼皮。

DeepSeek Harness 是 DeepSeek 官方最新开源的 AI Agent 运行环境，你可以把它理解成一个高度可定制的 AI 编程工具，对标 Claude Code 和 Codex，核心理念是「一切皆插件」。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1G4C1JV3LNSjAfj1wylC8v0lKrlGtFJf3loxjo8VduhkROzapKHqjZqr6G5miavgajyyrytJOH9PNVDw6gBevotQDrxZaZm0SLw/640?wx_fmt=png&from=appmsg)

上一篇 [《DeepSeek Harness 的保姆级教程》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589503&idx=1&sn=1ac0c26c5bd834eb68060600038d0e23&scene=21#wechat_redirect) 中，我已经带大家从零上手了 DeepSeek Harness，覆盖了安装、实战、社区插件和自己写插件的基础用法。

接下来开始进阶教程，我会把 DeepSeek Harness 里那些更深入的玩法一个个拆开来讲。

本篇先从 Agent 预设开始。

## Agent 预设是什么？

很多 AI 编程工具都有模式切换功能，比如用过 Cursor 的同学应该对 Agent、Ask、Plan 这几种模式不陌生：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HY5FMwfB0RD1hZe2qo6O9FRS0aNTDMiariaOxkKoHicGwic14Eszo5Zms8JQE4tSib3EqyaIiatrMWms5oO07l98xGkh1sJMCAGJCQI/640?wx_fmt=png&from=appmsg)

DeepSeek Harness 同样有模式切换功能，官方把它叫做 Agent 预设。

所谓 Agent 预设，就是 AI 在一次会话中能用哪些工具、遵守什么系统提示词、以什么方式工作的一整套配置。不同的预设组合出来的 AI，干起活来风格完全不同。

DeepSeek Harness 内置了四种预设，对应四种运行模式，你可以在对话框上方的模式选择器里直接切换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EIF2RlSMkicjQNnLdYd91WEl7npX8r5wCRmetdH6iaCekhdwic4BR3R3gap2zqvtwOdRA7ZaBK0aOXqt4hu6BkrqacRB0DIniczT4/640?wx_fmt=png&from=appmsg)

选对预设很重要，写代码、做测试、修 Bug，不同类型的任务适合不同的模式，选错了可能事倍功半。

下面我先带大家了解一下这四种内置模式，然后再教你怎么自己定制。

## 四种内置模式

### 标准模式

标准模式是打开 DeepSeek Harness 之后的默认选项。

它加载了一个 AI 编程工具应有的全部能力，包括文件读写、终端命令、联网搜索、任务规划、Skills 技能、子 Agent、待办管理等等，加起来有 20 多个工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Hs7gDoFMxeyyAVEnlRzjG1mwH2UWbmeZbGxkKuBncYnNJ6RmN7PbDO7Ugd75dRibicmMhlmGkibBaN3YHa9GYhormqzCZ42mf7Jk/640?wx_fmt=png&from=appmsg)

绝大多数场景下用标准模式就够了，它的覆盖面足够广，遇到什么任务都能应对。

你看，标准模式下的 DeepSeek Harness 是不是跟 Codex 这种 AI 编程工具很像？

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FpOPvp0NIicvVibm8LXYuGdcxGeb20tzAznuzG23YL2X3cXLiarM9bVHWmYOQCmM7hYrIts4LllpyPZU3icywQ1oqSX63fOIEX368/640?wx_fmt=png&from=appmsg)

没错，你就把标准模式当成国产版的 Codex 来用就好了，AI 编程、自动化办公等任务，都能搞定。

不过工具多也有代价，模型每走一步都要先从这 20 多个工具里挑一个来用，光是做这个选择就要占用一部分推理能力。而且所有工具的说明书都会塞进上下文里，模型能分给你真正那道题的注意力就被摊薄了。

标准模式下，光是跟 AI 说个「你好」，就要占用 1 万多 tokens 上下文！

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GUe0s0kXYcPtXkwSLiayREFAx5cruicGwr9XjFGvtMkSJHZicibrQJgCsoh8haJLEoYJ4jKXWmc7iaic39ibGbuDDC5JpAQfTVEF2E1U/640?wx_fmt=png&from=appmsg)

### 极简模式

极简模式就朴素多了，官方只保留了两个工具，一个能持续运行的终端和一个文件编辑器，其他能力全部关掉。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Eiaz2FYTiaiaTj30Hl6jTUGrY9Tbsds7PlDCORUziazRCSbklzBWxEOuy7pShBeuu1aq3dZexGUy9rkeIOGn3ibLA2uUic0gAahpdyU/640?wx_fmt=png&from=appmsg)

不只是工具少了，极简模式的系统提示词也被锁成了一句「You are a helpful software engineer assistant」，上下文压缩、任务规划、Skills 技能、子 Agent 这些统统没有。

同样跟 AI 说一句「你好」，极简模式只占用 1000 多 tokens 上下文，比标准模式少了 10 倍！

工具说明书少了，模型能分给任务本身的注意力自然就多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EosVIcTp4aibaeWeEhrK90k9PtALzLOLF5oas8WhtXrRAthoLZ0z6I91aniaNBOmzcdib5JhbK5gHg4QM8kW4S3Eicxp75jREE1q4/640?wx_fmt=png&from=appmsg)

在这个模式下，AI 就像个闷头干活的老师傅，不跟你汇报进度、不做花哨的规划，拿到活儿直接动手嘎嘎写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Gunsv4BEnTWluRfB017baqAnZAMjYjsGHEDON90Xoos6YQGee360GrhXQ8k1rHoOvgCJkey9oZp2fpOE2gjD6Q4DCiaTcNK3mE/640?wx_fmt=png&from=appmsg)

官方对它的定位很明确，是专门拿来跑模型基准测试的。把环境削到最干净，让不同模型在同一个标准下公平比较。

DeepSeek V4 Pro 的跑分成绩用的就是极简模式，你仔细看跑分图最下方的小字：V4-Pro 使用 DeepSeek Harness 极简模式作为框架进行测试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1EwmMaiaHNJN0Uct9Ulj21uHXT9YNRPr6Jpg7NrPaAQGf9bVXavv8X5KN9pCeopPlChfWsiaINt6Imf7VzpX1n1EWH4AQ3VOjKAQ/640?wx_fmt=jpeg&from=appmsg)

那把《考试》模式拿来干活，效果会怎么样呢？后面我们会跑一个 Demo 来实际对比。

### PTC 模式

PTC 是 Programmatic Tool Call 的缩写，翻译过来就是「程序化工具调用」。

在标准模式下，AI 是一步一步调用工具的，执行完一个再决定下一个做什么。每一步都要等模型思考、选工具、返回结果，来来回回要经历非常多轮。

PTC 模式换了一种思路。模型不再一步步调用工具，而是直接生成一段 TypeScript 代码，把多步工具调用串联起来一次性执行完。

举个例子，假设你要把 128 张照片批量重命名，重命名工具每次只能处理一张图片。标准模式下 AI 要一张一张调用重命名工具，每张都要等一个来回。但在 PTC 模式下，AI 直接写了 5 行 TypeScript 脚本，用一个循环把 128 个文件全部重命名了，只需要跟模型交互 1 次。

> 注意，实际情况标准模式应该也不会这么干，这里只是举个例子便于大家理解区别

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GMiaI0BNJTcnwxMrHbickicyjcvu99PBxgWibuWXgdZbWgribEibpzfHZhIgmK2fktiaQTpT6q5LnthKvRHLn6vvH3mBKs5Uc5kfbY5w/640?wx_fmt=png&from=appmsg)

PTC 模式适合那种步骤很多但逻辑清晰的任务，比如批量重命名文件、跑一整套自动化流程，效率比一步步确认要高得多。

有意思的是，PTC 模式和标准模式在配置上其实只差一行，就是把工具呈现模式从默认的 `native` 切换成了 `code` 。本质上它拥有标准模式的全部工具能力，只是模型调用工具的方式不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1H3JqlCz8lMoCchnN6VTru7jI5ibgia0nD5bpuHL0AgGmB6CmSWttw8r14QMAA3AFL159TibzsarJYZ04XVQFlMonYESd0LHUjA5A/640?wx_fmt=png&from=appmsg)

### 创造模式

创造模式是四个预设里最特殊的一个。

它继承了标准模式的全部能力，在此基础上还额外提供了一组用于操作 Cordis 插件系统的专属工具，让 AI 可以检查当前运行时有哪些插件在跑、在内存里试验新的插件组合、甚至自己创作出一个全新的模式预设。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FlrqNLRucs4tr0bezVWEEUsuQKAFDssos000aLiciaicye9clYQRKWeMBlfJZICEPaJ6XKU24ia95BSG7B6Q0DX3icxQDsiaqtu6rz4/640?wx_fmt=png&from=appmsg)

简单来说，这个模式就是用来改造 DeepSeek Harness 自身的。

在 [之前的教程](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589503&idx=1&sn=1ac0c26c5bd834eb68060600038d0e23&scene=21#wechat_redirect) 中，我就是使用创造模式来开发了一个 Harness 桌宠插件。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H4ELvMQIrBlicjV4ric0bHWbiaY77JnCvxiaXoztjeaedzw15XfpeCiaYH8YVhSicY6Zp5fUyAyLCaDv6jVVe3JGOJSQoBcMWyl7K7k/640?wx_fmt=png&from=appmsg)

不过创造模式的权限非常高，按官方的话来说，你要像对待 Shell 访问一样对待它的权限范围。

所以日常干活不建议长期开着这个模式，需要开发插件或者定制预设的时候再切换过来就好。

## 选哪个模式好？

介绍完了四种模式，总结一下它们的核心区别。

这四种模式本质上就是「当前会话加载了哪些工具和配置」的不同组合。

极简模式只留两个工具，标准模式配齐全套能力，PTC 模式换了一种工具调用方式，创造模式还能让 AI 自己查看和改装当前的插件配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HzwPCEPnoaxbZO69fynwKSoIA1zLPlP4D7iaqPwLBopywUicI1FZHkdTjdVDyWD2SnySzs6iaqy5UBEBzlbMibReWooYyUaRAkRv0/640?wx_fmt=png&from=appmsg)

之前有社区的大佬发现，切换到极简模式之后，模型在纯编码任务上的速度和表现反而更好了。于是我专门做了一期实测，用同一个 3D 射击游戏的任务在标准模式和极简模式下各跑了一遍。

先看看标准模式的成品效果：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FTENs5iaPOanJtWNdSHhkgOubFXLfiaUFF5VE9QYbLEpnmWEiapyT64on7whicoicvJta5JRthbGo1SZLAO8eq7uKytdIsr2PTaO3c/640?wx_fmt=png&from=appmsg)

再看看极简模式下的成品效果，差别不大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FWL1uAEmE9icTjTX7x2zWoR1Bnhmp452RVlR8rUkHRXbMx9hryWLVhyJ9PWhWyZibE1icp9VtKphXicvIHAdU5ux0ywE4erOVJ4jU/640?wx_fmt=png&from=appmsg)

但是，标准模式跑了 33 分钟，极简模式只用了 23 分钟，快了将近 10 分钟！

不过极简模式的短板也很明显，没办法联网搜索、没有上下文压缩、没有任务规划，你对成品质量的要求越高，极简模式越容易掉链子。

完整的对比测评可以看我之前发过的那篇 [《DeepSeek Harness 极简模式性能暴增？》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589550&idx=1&sn=aacb16f8ffe68e6b0a930101e5fdc324&scene=21#wechat_redirect) ，这里就不展开了。

我还用 PTC 模式跑了同样的任务。比标准模式快了 7 分钟，而且整个任务只用了 1 轮 18 步，比标准模式精简了很多。Tokens 消耗也低了不少，输入只用了 150 万，不到标准模式 520 万的三分之一。

PTC 模式的成品效果也是我觉得三种模式里最好的：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FVkdJByGQiaRb5TFIYuu8IMhoQ44NGDu5yibN66KduNhYe22y3P9zaEVXyqKCunD7OabmXicRzEMkMOvWOozd2eHBFNibcWkfWoTU/640?wx_fmt=png&from=appmsg)

总结就一句话，图快就用极简模式，图稳就用标准模式，步骤多的自动化任务试试 PTC 模式。

## 自定义 Agent 预设

除了使用四种内置模式外，如果你有特定的工作习惯或者经常做某一类任务，可以给自己量身定制一个专属的 Agent 预设。

举个例子，Cursor 有一个很受欢迎的 Debug 模式，它会让 AI 先生成假设、插入日志、让你复现 Bug、再根据运行时数据来定位根因，整个排查过程非常有章法。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Fjn0kFC1ho5diaTaG1HsK6skeCA4ZWD8vxUAnML0FxFVQAp74CgclR4Vl87toUFLuO8JI9K47j8XytnngZNHOeJaCIH1h18qIM/640?wx_fmt=png&from=appmsg)

这套思路完全可以搬到 DeepSeek Harness 上来。

DeepSeek Harness 支持自定义预设，可以切换到 **创造模式** ，让 AI 帮你创建想要的预设。

比如我要让 AI 创建一个「Debug 模式」，只需要给 AI 提供 Cursor Debug 模式的官方文档作为参考，让它据此来编写预设就行了。

提示词可以这样写：

```
基于标准模式创建一个自定义 Agent 预设，名称为「Debug 模式」。
要求复刻 Cursor IDE 的 Debug 模式工作方式。
必须参考 Cursor 官方文档来设计：https://cursor.com/docs/agent/debug-mode
```

提交任务后，可以看到 AI 自动加载了编辑预设的技能，然后通过终端抓取了 Cursor Debug 模式的官方文档页面，提取出了 Debug 模式的核心工作流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HIG5bXG1Y7tX4VjHkZ1oq5ianJEyTIHUe0a4icnrGVKQrR6ibibia3Dg8lnLiczrYbwGYA9EoKU93ibfSicoOKPqRHIfI1gbmlLyWVkKU/640?wx_fmt=png&from=appmsg)

几分钟后，AI 完成了任务。它从标准模式复制了一份预设，然后修改了两个文件，一个是存放预设名称和描述的 `preset.yml` ，另一个是定义 Agent 工具和角色人设的 `agent.cordis.yml` ，把 Debug 模式的六步工作流和硬性规则都写了进去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GMVgnCFNja9E2iap6UQtQrd7hqAwfzX7JEqnrWa72t0oLR1TibMV8ykcicFg5ckWdm4C5BcIPibCRbTibnXIaUhSvBps5hJloB8Ficc/640?wx_fmt=png&from=appmsg)

创建完成后，你在模式选择器里就能看到这个自定义的「Debug 模式」了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HURh127tbdRFzyTDLE6FiaDcHWS4vribA4HRDZwkmFcqo5vPej48b58AjWw6Wg3tBeGwkWTYphfksUWTPCWIZ6q8nZKVjMv5vjw/640?wx_fmt=png&from=appmsg)

以后遇到那种能复现但是找不到原因的疑难 Bug，切换到这个模式修复就行，AI 会按照「假设 → 插桩 → 复现 → 分析 → 修复 → 清理」的流程来帮你排查，比直接让 AI 凭着经验来改要靠谱得多。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Ey6qhfGUoiapyn61IDYvzicV4Ecx0rJYJXREpLwI4ic4shIrwwIo0woD3epmXdvLawenx3bR0xh3iaucKSHoeA9wguyaynzyM7ZE4/640?wx_fmt=png&from=appmsg)

## 更多玩法

同样的套路，你可以复刻各种专用模式。

比如创建一个「代码审查模式」，让 AI 只做代码审查不做修改，从安全性、性能、可读性等维度逐一检查，最后输出一份审查报告。

或者创建一个「文档模式」，让 AI 专注于给代码写注释、生成 API 文档、更新 README 项目介绍文档。

又比如搞一个「重构模式」，让 AI 先分析项目中的冗余代码和重复逻辑，再制定重构计划，最后逐步执行，每一步都跑通测试才往下走。

本质上，自定义预设就是给 AI 设定一套固定的工作 SOP，你把自己做某类任务时的最佳实践写进系统提示词里，AI 就会每次都按这个流程来执行。如果你之前接触过 AGENTS.md 或者 CLAUDE.md，应该会觉得很熟悉，它们的思路是一样的，都是通过配置文件来约束 AI 的行为方式。

OK 就讲到这里，之后我还会继续讲解 DeepSeek Harness 的更多进阶玩法。

想系统学习 AI 编程的同学，可以看看我免费开源的 [《AI 编程零基础入门教程》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=2&sn=91ab9714bff9eb6e26d5c03081ec765f&scene=21#wechat_redirect) ，上千张图、几十万字，带你从 0 开始快速学会 AI 编程，做出自己的产品、跑通变现全流程，一次拿捏。

![鱼皮的 AI 编程教程](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Gq3aSes9GH9QsgmnE2KebbFRgy17RibPibTtEpYp4RRShhrzWQZnIusibP0DV6ZWdVBtFKmicgPibF1kno50JJUerD5HYjiaia7kFdd0/640?wx_fmt=png&from=appmsg)

鱼皮的 AI 编程教程

我是鱼皮，持续分享 AI 编程干货。觉得有用的话记得点赞收藏和关注~

评论区聊聊：你有没有自定义过 Agent 预设？都做了哪些模式？

往期推荐

[又一个新项目完结，用 DeepSeek 搞了个微信小程序！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589708&idx=1&sn=2cb6852d0faba977c076d178a887f5a7&scene=21#wechat_redirect)

[把 GLM-5.3 接入到 DeepSeek Harness，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589671&idx=1&sn=4f6229ee831bf78969bc9df7be33450a&scene=21#wechat_redirect)

[完全免费的 AI 资源网站，起飞！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589107&idx=2&sn=0cb64c8664643099430e40b85e8881bd&scene=21#wechat_redirect)

[全体码农做好涨薪的准备吧！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588976&idx=1&sn=df3bea7d357480751a77b77b6c7194f5&scene=21#wechat_redirect)

[27 届秋招，巨能打的 AI 智能体项目来了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588930&idx=2&sn=f5d157d911f02f17b2131307e6afe953&scene=21#wechat_redirect)

[还学不会 AI 编程？我出手了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588292&idx=2&sn=75d57645c0f7d910574677f9d0e14d18&scene=21#wechat_redirect)

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过