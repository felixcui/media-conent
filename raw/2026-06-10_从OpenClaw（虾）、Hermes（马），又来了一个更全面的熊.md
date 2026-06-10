# 从 OpenClaw（虾）、Hermes（马），又来了一个更全面的熊

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/6GWUtXqTnvrZJa2lRmr9Yg

---

## 摘要

针对当前AI工具工具间割裂、云本地脱节及缺乏记忆等痛点，商汤出品的“办公小浣熊”桌面端2.0版本提供了低门槛的全面解决方案。它融合了OpenClaw的执行与Hermes的记忆能力，支持导入已有记忆，并通过“本地Claw”负责读文件和操控浏览器，结合“云端工作台”进行复杂创作。该产品打破了云与端的边界，在一个客户端内实现从规划、分析到生成、执行的全链路工作流，安装即用，真正解决了信息搬运问题。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

现在AI工具，各种claw满天飞，但有两件事一直没处理好。

一是 **割裂** ，而且是两层的：一层是工具各做一块，一个完整任务得在它们之间来回搬，每换一道工序掉一层信息；另一层更别扭——AI 待在云端、浏览器里，我的文件和应用却都在本地，每次都得上传、下载，把活在"云"和"端"之间来回倒腾。

二是 **没记性** ：今天交代清楚我是谁、什么文风，明天打开又是一张白纸——用了一百次，它还是第一次见你的那个它。

这两个问题，恰好是 AI 智能体这两年进化的两条主线。今天，笔者介绍一个国产小而美产品—— **办公小浣熊** ，它最近升级后的桌面端2.0版本很好的接住了这两个需求，并且门槛还相当的低，就像WPS一样安装即用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJic7IkibOxUMrhiav6icboErElfZ4rYlRA4eI51tbhbLyoOxonrSKRu2RcqDfnPR8iaLVRxbVtzhmGSAvCMGYgfQJ3ECV3TzzDfTAg8/640?wx_fmt=png&from=appmsg)

## 一、一条进化线：会执行 → 有记性 → 能用

- **OpenClaw** ：让 AI"长出了手"——能在本地跑命令、操控浏览器、读写文件，GitHub 星标 37 万+。突破是 **执行** ，但要自己配置，门槛极高。
- **Hermes** ：在"会执行"之上补了 **记忆与自我进化** ，越用越懂你。但同样得 curl 安装、自建服务器才能玩。
- **办公小浣熊·桌面端 2.0** （商汤出品）：把"执行 + 记忆"两块都接住，再补上前两者的共同短板—— **不用折腾、专为办公打磨、本地+云端一体、还做了一整套可控机制。**

最能说明这条线的，是一个细节：桌面端 2.0 **支持直接导入 OpenClaw / Hermes 的已有记忆** 。它不是另起炉灶，而是站在前两者肩膀上把这件事做完。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ9aKmC5C22Bn9tqzV4SVHTjVLQkicElPpHIFZ6NuBNhJGQOTLs8sgax73MnxbUrsh4ia5AM02oiaMQgzlUftDHGQXYLOBHvPE4RsQ/640?wx_fmt=png&from=appmsg)

## 二、它强在"全"：一条工作流，一个客户端跑完

桌面端 2.0 的客户端里同时装着两套能力：

- **本地 Claw** ：走进你真实的电脑环境——直接读本地文件（Excel/PDF/Word 等 20+ 格式，分目录授权）、一句话操控浏览器、 `⌘K` / `Ctrl K` 全局唤起、连接飞书、跑定时任务。负责 **执行** 。
- **云端工作台** ：承接强模型的复杂创作——数据分析、生成 PPT、任务规划、一图读懂、知识库问答、文案生成。负责 **创作** 。

于是从"规划任务 → 分析数据 → 写成报告 → 做成 PPT → 落地执行"，一条链路在同一个客户端里跑完，中间不用切工具、不用搬运结果。这也正好接住了开头说的两层割裂：横向上把分散的工具收成一条流水，纵向上让 **云端的 AI 能力和本地的文件、应用第一次在一个客户端里打通** ——不用再在"云"和"端"之间上传下载。这才是它和那些"各做一块"的智能体最大的不同—— **不是单点强，而是把一整条工作流接住了。**

具体来说，升级后的桌面端 2.0有下面几个高频能力：

1）直接读电脑里的本地文件，不用上传。 我把一个堆了十几份月报、命名混乱的文件夹授权给它，一句"读一遍、按月汇总关键数据、告诉我哪个月异常"，它就在我授权的目录里自己读完、整理、给结果，没让我上传一个文件。它支持 Excel、CSV、PDF、Word、PPT、图片等 20+ 格式，权限分"工作区 / 家目录 / 自定义目录"三档，只在你点头的范围里活动。

2）一句话操控浏览器。 内置浏览器自动化，不用装插件、不用手动复制网页，直接在你电脑本地操控浏览器，不用云端中转，直接操作本机浏览器打开的网页，完成那些传统需要RPA工具才能完成的工作，这对于那些没有接口的系统非常方便，也更能适应一些边缘情况。

![](https://mmbiz.qpic.cn/mmbiz_gif/rY5icXvTTrJ9oSibdiawMaFxvJm02PDAuDKWOCOIzws1JPR3XrIdbs5owAXRd8ScAIoMeWtMW6lqu0Y9VaYHQ7rXibicgTFWgsWCJkGhfyicRutBk/640?wx_fmt=gif)

3）Quick Bar 全局唤起，还能写回 Excel。 不管开着什么软件，按一下 ⌘ + K（MAC / WIN 是 Ctrl + K），它立刻弹出来处理我选中的内容——翻译、总结、改写都行。最惊艳的是在 Excel 里：选中一片数据问"这组数有什么异常"，它分析完能把结果直接写回表格旁边，而不是丢给我一段话让我自己抄。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ9HE2VUNsHLo2x0Gibyu0qeR9exAYq5pSfeicy8lnrNuHsUvGSeBL3P5Qdu5iaRgQVgkGjibgI0QicFSkZsffGqIfrS32H3D4FyZWibo/640?wx_fmt=png&from=appmsg)

4）定时任务。 安装完pings技能，然后设了一条：每天早上给我推送Wink Pings的新闻。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJibBaYkkURGT9hpEWAvkNxecRMuPlNbOhIYHvOHcOD9Lp7zTNDGpM0t6KYxusibX766ofvNOFmpwaSQTQcPruvib7wDicUic4nOgYDk/640?wx_fmt=png&from=appmsg)

然后每天的最新AI资讯就全掌握了。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rY5icXvTTrJicQFziciabVaLbKibGJHdNuezzsDhMEYQSSkKqFpZYJPRRUfnouB8Krpzf2QnibeptL6cHOXKWt8fOceHbYQ7GTJJ7zX9mMib7VbvuA/640?wx_fmt=gif&from=appmsg)

此外它还能连接飞书（企业微信、钉钉即将支持），把 AI 结果一键沉淀成飞书文档、追加到已有文档、或搜飞书知识库——结果不再停在对话框里，而是直接进了团队协作流。

记忆与沉淀也一样开箱即给。它一边记住你的职业、行业、术语、文风和团队口径，一边把你的知识统一接入 **三类数据源——云上知识库、本地文件、第三方数据（如飞书）** 。

![](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJibJel8EDBnzBUlZBEpdnJz9M200licdVUaZCby7J0ryJRLyL8Y7lUO0WZxicarictTfxmN87Onn9V0GyBGsVRic8SIqgkJTEuUF18Y/640?wx_fmt=png&from=appmsg)

也就是说，它的"记性"不只存在一个本地文件里，而是横跨云、端、第三方一起沉淀（这本身又是对前面"云端割裂"的一次打通），越用越像"懂你的同事"——还不用你去搭服务器。

## 三、几个实测小场景

**一句话出报告** ：丢一份数据进去，让它分析各品牌、各车型走势，直接出图表 + 结论，整理成一份《新能源汽车销量分析》。

![](https://mmbiz.qpic.cn/mmbiz_gif/rY5icXvTTrJ8EqgsFyKsN0TD10fFEFwSn0OWIRVR8BnwCShibqrygsrG2ibEGTWPR4cYo5MPCtf5AJaC9MicPSBTLGmlDR5nMINxXuZBw9HibOyg/640?wx_fmt=gif&from=appmsg)

这里面的图表还可以编辑：

![](https://mmbiz.qpic.cn/mmbiz_gif/rY5icXvTTrJ9gAs7HXfOf4WKjbzFpsn1DdaIia8VB7xnsEtBzS3uklwmliaATDneuwjiaArmo6LOsnt5HhrkxT93YiaZs7RXcS2XzuhTUZrr6dpA/640?wx_fmt=gif&from=appmsg)

**报告一键转 PPT** ：上面这份不用重做，直接生成 PPT，单页还能对话式微调、导出.pptx。

![](https://mmbiz.qpic.cn/mmbiz_gif/rY5icXvTTrJ9bxfzldHibgegw9WL6LqfHhoWZO1vwktlL0DyPp57iczeXN3LTWWgwDDah9KcVXrFEf8IYrAEeFBWrIyVNSia3WIp1lcP3ibUz5Bo/640?wx_fmt=gif&from=appmsg)

这是生成的PPT：

![](https://mmbiz.qpic.cn/mmbiz_gif/rY5icXvTTrJic5Es2D9FBYs3xQb0wDjh2g5cy63iaJ5fYPMkC53MZVIsCc8Mru3SMCSoibq3ic8DLKib8E4b3FPGbmonpDU0SprzJCdu6DeiaIm8F0/640?wx_fmt=gif&from=appmsg)

**四、功能很全面，你能用到的他都有**

对标Workbuddy这些的 **专家中心、技能库、记忆中心等它都有， **专家中心**** 预置了行业研究员、数据分析师、PPT 设计师、飞书文档助手、写作主编等角色（还能组"专家团"），挑一个就能直接执行，不用自己调 prompt； **技能** 把 pptx、docx、xlsx、pdf、research、邮件等常用办公能力做成开箱即启的"技能"，还能自建 Skill；底层还藏着双引擎架构、本地模型离线（Ollama / llama.cpp）、MCP 工具生态、AI 动文件一键回滚等硬功能——前沿 agent 玩过的它基本都有，只是被收进了一个不用折腾的客户端里。

![](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJ8diaFKI8mlEibia9KQ0nQFjV6nOoSQanU86P5NV05MCmNL8Z9f9QRB3Rj1yykJUbY6G4VbfyibJ9woiaTbN4N6dJ09m9Omfze1JaR4/640?wx_fmt=png&from=appmsg)

## 🎉 彩蛋：专属桌宠

它还藏了点小心思——内置 **桌面宠物** ，能挑一只常驻屏幕陪你干活：招牌小浣熊、戴紫色工牌的像素小浣熊、赛博朋克红熊猫 Neon、3D 小鸭、芝士猫……干活间隙瞄一眼，一天没那么干巴。能在细节里讨人喜欢，是另一种用心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJibOU2uyG06UpEiaZWNTCk0tYZ3LyGWsbutLVINAXPQToicsdJAbtd0kWvZ1Ycd3omwPGWtTfG15VdibjR4ITV8SEndtJd6MbHcoOw/640?wx_fmt=png&from=appmsg)

## 现在上手，还有 75 万 + 奖池

办公小浣熊正在办「真实任务挑战季」：

- **🏆 OPC 能力挑战赛** ：总奖池 ¥ 300w+、最高单项 ¥100w。新手出道赛——用它完成一次真实任务、发到小红书/知乎/公众号即可参与，赛季 5 轮、每周抽奖、越早参与轮次越多；高手创造赛——围绕真实行业场景做完整作品，并同步推出 **全国首个 OPC 能力认证体系** 。报名：https://community.xiaohuanxiong.com/2026-spring/detail
- **📅 21 天真实任务打卡挑战** ：200W+ 奖池，连续 21 天养成 AI 高效办公习惯，奖励一并拿走 😎 入口：https://community.xiaohuanxiong.com/2026-spring

## 想试试

桌面端 2.0 现在公测，支持 Windows / macOS：

👉 **下载：https://office.xiaohuanxiong.com/download**

想先在网页玩玩，直接开 **office.xiaohuanxiong.com** 注册免费用；微信搜 **Raccoon智能助手** 可用小程序版。

AI 卷了这么久，大家都在比谁更聪明。但真正决定它能不能进入我日常工作的，是几件朴素的小事—— **能不能从头帮我干到尾、会不会越用越懂我、出错能不能撤回、以及，能不能不折腾就用上。**

办公小浣熊·桌面端 2.0，把这几件事一次给齐了。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过