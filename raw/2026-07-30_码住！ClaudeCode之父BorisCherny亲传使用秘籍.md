# 码住！Claude Code之父Boris Cherny亲传使用秘籍

**作者**: 傅盛和龙虾三万

**来源**: https://mp.weixin.qq.com/s/ZtPmKm_HnYAcp9xGFeilZQ

---

## 摘要

Claude Code之父Boris Cherny分享了四个核心使用技巧：一是开箱需完成基础配置，包括优化换行、调整主题、安装GitHub应用及设置免确认工具以提升体验；二是切忌直接派活，应先让AI通读并梳理项目整体结构，这能将新人熟悉代码的时间从数周缩短至几天；三是遵循先规划后动手的原则，要求AI先给出实现方案再编写代码以避免方向跑偏；四是强调接入工具才能形成真正的反馈闭环，发挥AI的最大效能。

---

## 正文

傅盛和龙虾三万 傅盛和龙虾三万

在小说阅读器读本章

去阅读

有朋友后台问我，你的CC我的CC好像不一样，怎么我安装了感觉没那么好用呢，是不是哪里没使对劲？

正好最近刷到Claude Code之父 **Boris Cherny** 做的实操分享，聊聊他每天都在用的小技巧。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Vauqib9kHbibXlsb4XxGria3SVcZ1cxnT6M03ib2RMAPGxebSyJ0xEW2nXXawdd9tQYBSOzgpoLFWJTibZuGibVyWC1FogTXKSotIofWXicECy1dSg/640?wx_fmt=jpeg&from=appmsg)

· · ·

## 开箱先做几件小事

第一，跑一下 /terminal-setup。

这个命令主要解决一个很小但很影响体验的问题：换行。

配置完以后，你可以用Shift + Enter换行，不用每次为了多行输入搞得很别扭。

第二，跑 /theme。

把主题调成你舒服的模式。暗色、亮色、色盲友好主题都可以。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibWia9c81RgsOjbuicmKTYxklIiaWDOvhjq2rYKhsJO0TTFCDA1DDojucFmYuOzlIByJhGK7oXkqNrIWwkeZaopQzwV1EJs53jYbxs/640?wx_fmt=png&from=appmsg)

第三，如果你在GitHub上工作，可以输入/install-github-app装GitHub App。

这样你就能在Issue或PR里直接@Claude，让它参与代码审查、问题分析、自动处理一些任务。

第四，自定义允许使用的工具集合。

对于经常要确认、但风险很低的操作，提前设置成允许。这样Claude不用每一步都等你点头。

· · ·

## 让AI认识你的项目

大多数人拿到AI工具，第一反应是直接派活。

Boris说这个顺序搞反了。

你都不太清楚自己项目的全貌，AI更不清楚。在这种情况下让它写代码，撞对了是运气，翻车才是常态。

他的做法是，先花时间让AI把整个代码库读一遍，然后问它问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vauqib9kHbibWQHPLBA9X5YpkPnzsshMleIs7j4Hx887n1VriaNuqxjhhWD7a6WfriaNhGgibm4ZpnocHlE5qtaxkjBJj2D8qk8wO32vFK4sico5c/640?wx_fmt=png&from=appmsg)

比如：

"帮我把这个项目的整体结构梳理一下，主要模块是什么，它们之间怎么配合？"

"如果我想给用户列表加一个排序功能，从哪里入手最合适？"

Claude Code会深入分析你的项目，给你一个像Wiki一样的解答。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vauqib9kHbibWmEVy6E2zBa53c9iavX2RA3TWDNamC640lM0YkD4fYBaVLOW8RgkJicTsG3TfztJKjQxFfyqjPdetGicWDLGzZagBDvRs7AzXNGA/640?wx_fmt=png&from=appmsg)

效果很直接， **Boris说Anthropic以前新人入职熟悉代码库要2到3周** ，到处问人、自己翻文档。现在Claude Code带着探索一遍， **2到3天就能上手干活** 。

· · ·

## 先规划再动手

凡事预则立不预则废。用AI也是一样。

很多人用AI Coding就是把所有需求一股脑扔给它，然后等结果。

这不许愿呢吗？

他的调整是：在你说"帮我做XX"之后，加一句"先给我一个实现方案，不要直接写代码"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vauqib9kHbibVaJpV9MonJ42WQA0lvib2ib0wMthCic7nIcBdbAJzVZKLbeAFgGHIph4jJwgUeSFFZCGibI8Trask1jDoSoPC1r2sYuk04GVWzn2w/640?wx_fmt=png&from=appmsg)

让AI先把它打算怎么做、分几步、涉及哪些部分说清楚，你确认方向没问题，再让它动手。这样即使中间出了岔子，你也知道问题出在哪个环节。

· · ·

## 有了工具才有反馈闭环

Boris 说，Claude Code真正开始发光，是接入工具以后。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibXrSFeNmtdaLZXj3rzBVqWscACX5aGFJ6AaYDiaGEpQSrZErazC5hiaiatSJglZHmaMY6OiafuD0PYbL4zwWNa11ukPibpwsiaOWdodI/640?wx_fmt=png&from=appmsg)

Claude Code接入团队工具，主要有两种方式：

一是通过Bash调用现有的CLI和脚本，比如查日志、跑测试、发版、生成报告的内部CLI。

如果AI临时不会用，可以让它先运行 --help 看说明，再根据说明选择参数。如果这个工具以后经常会用，可以把这段说明写进CLAUDE.md。

二是通过MCP接入结构化工具和外部系统，比如可以接数据库、浏览器、设计稿、内部平台。

新工程师入职，没有代码权限、没有日志权限、没有测试环境，再聪明也干不了活，Claude Code同理。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibXIl3nuH7ickvgSiakjL3N94um0IfmukTc2Pe2vXWzrdibTWUX4SsXbepXkibqqSbUTOEdI9jkH05bbwYhCkN7AY6Y36wRfa5EVbXQ/640?wx_fmt=png&from=appmsg)

工具接好之后，它才能自我验证，才有反馈闭环。

Boris举了个例子，只说"帮我做个页面"，它可能做到七八十分。但给它设计稿，让它用Puppeteer工具截图对比，自己改两三轮，结果往往接近九十分。

我在用Fable 5复刻红警的时候也是这样，AI写完代码会自动截图，看看截图再去调整，完全不用我手动测试。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Vauqib9kHbibWUMclKYM0JTsTxp1SsmfQejwRrWJVvoj4HqRiaurpS4cr37n0PejVozpAPXmJ47KicibyYIUJVQkxZCTmUjok0QtPCtia92vWcGgU/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

· · ·

## CLAUDE.md：AI的入职手册

Boris建议大家给Claude Code写一份入职手册，叫CLAUDE.md，专门用来告诉 AI 关于你和这个项目的所有关键信息。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibWZDknEQU7v3fejb2CP6hJ0NjtCqdw2ohvE6xIvYcYnCX8w6EPIyl3lYSuMwRzHW8K6MhLSIIYSjxDCE3KIwazSDqrQNZq2ZcA/640?wx_fmt=png&from=appmsg)

当然，上下文不是越长越好，你写得太长，它每次都要读一大堆，不仅耗token，还容易把重点冲淡。

所以我建议把CLAUDE.md写成“短、准、硬”的规则和索引，重点写Claude Code干活时最容易踩坑、最必须知道的东西：用什么命令启动，改完跑什么测试，哪些文件不能乱动，哪些规则不能破。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibV6w82NZkydxaicEZxQ0rjHeibEbs0MXwia51zuSqP3wnFiaFLZIj3icNAiaBWndyaVtYCj8CCpfggNKtQuM6ZK6UtGVwuyriadcUTxN8/640?wx_fmt=png&from=appmsg)

另外，CLAUDE.md不一定要放在根目录，也可以放在子目录里。

大型项目里，完全可以在不同子目录各放一份。前端目录写前端规矩，后端目录写后端规矩，移动端目录写移动端规矩。

![](https://mmbiz.qpic.cn/mmbiz_png/Vauqib9kHbibVfuXfnXibh4bc6B2UjcUkPpwHoqnYswAr031XibuEbHJufOlEEaVsricLH0CgzG9PI2uReeEJ2EvR8M9Nar2xIQ0DOicTzOnrzSys/640?wx_fmt=png&from=appmsg)

这就像公司培训新人，不可能第一天把财务、人事、销售、研发所有制度全塞给他。最好的方式是：他在哪个岗位，就看哪个岗位最相关的手册。Claude Code也是一样，需要什么上下文，就给它什么上下文。

· · ·

## 明显改变手感的快捷键

最后，Boris还分享了几个每天都能用上的快捷键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vauqib9kHbibXEPYjJUIoVasqYTicbCT18fv3ZYLUo5rBIBUeqZc8nZmU0WHhu8E7vqpjc0UB8ibD5noEPd72EDLcAibSlGn3FRzgtQ0scuOEGQg/640?wx_fmt=png&from=appmsg)
- 按Shift+Tab，开启自动接受编辑模式。AI写的代码修改会自动应用，不用一条一条反复确认。等它跑完你再统一检查，效率高很多。
- 按 # 让AI记住规则。如果AI哪个地方说错了或者理解偏了，可以敲一个"#"，它自动把这条记录写进CLAUDE.md，下次就不会再犯同样的错。
- 按Esc随时打断。如果你觉得 AI 方向跑偏了，或者突然想到新要求，直接按 Esc 就能打断它。不会丢数据，不会损坏文件，暂停完补充新指令它就接着走。
- Ctrl+R看原始对话。有时候用AI会疑惑"它到底看到了什么才会这么回"。这个快捷键能展开完整的对话记录，AI眼里看到的输入输出都在里面，排查问题特别好用。
- claude --resume恢复上次没聊完的。在命令行里输入 claude --resume，就能回到上一次中断的对话，接着往下聊。

· · ·

## 最后

工具这东西，最怕的不是不会用，而是以为自己会用了。

Claude Code也是一样。很多人装完之后，随手丢一个需求进去，发现效果一般，就觉得“也就这样”。

所以这篇别只放进收藏夹吃灰。上手试试，效果可能马上就不一样了。

今天就到这，如果觉得有帮助，欢迎转发关注~

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过