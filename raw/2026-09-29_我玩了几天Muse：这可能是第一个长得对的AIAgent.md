# 我玩了几天 Muse：这可能是第一个"长得对"的AI Agent

**作者**: AI小范儿

**来源**: https://mp.weixin.qq.com/s/9FOcLgsQSucEw2HNSEttXw

---

## 摘要

Meta推出的消费级AI Agent Muse上线两周下载约280万并登顶美区App Store免费榜，其极简聊天界面、仅限美加地区使用及后续公布的硬件与生态集成，显示出Meta从基础模型转向AI Agent战略后，试图以“长得对”的产品形态抢占个人AI入口。

---

## 正文

AI小范儿 AI小范儿

在小说阅读器读本章

去阅读

要说这几天，整个 AI 圈最火的是什么？那一定是 Muse。

9 月 8 日上线，不到两周冲上美区 App Store 免费榜第一，把 ChatGPT 甩在身后。

我折腾了两天，从安装、聊天、连接到翻它的「底层」，这篇把体验、坑和真相一次讲透。

## 00 先说背景：Muse 从哪来

我们有看到一个 APP、一个可爱的吉祥物，一个可爱的智能硬件，甚至连眼镜里面都可以使用。

▲ 图：Muse Charm

这一切都来源于 Muse，它是 **Meta** （Facebook 的母公司）出品的个人 AI Agent。

元宇宙折戟之后，Meta 把筹码 all in 到 AI 这边：开源模型 LLaMA 当年带火了一大批开源模型。

但后面翻车了，Meta 彻底调整方向。

今年 4 月又发布了 Muse Spark，直接冲进第一梯队。但光有模型没掀起太大水花，Meta 干脆换了打法：从「做基础模型」转向「做 AI Agent」，Muse 就是这个战略的头炮。

这玩意火到什么程度？

据 Sensor Tower 数据，Muse 上线两周下载约 280 万，日均下载增速 55%（ChatGPT 当年是 24%）；9 月 18 日登顶美区 App Store 免费榜，19 日登顶 Google Play。

9 月 23 日的 Meta Connect 发布会上，Meta 又一口气公布了头像视频聊天、Mac 支持、专属邮箱、眼镜集成和 Muse Charm 硬件，发布会后日活直接涨了 27%。

![Meta 设备合集示意图](https://mmbiz.qpic.cn/mmbiz_jpg/8TRTn7cvcJLvqQ4FHo5cbyrWZIuCwKHN4A2A9k3xMFb25TibkbibOo3Bic1CYEIXDLbQUeib0WlAphQmvfYlasFvaP7X3wChSflyRNxHSzTHwdQ/640?from=appmsg)

Meta 设备合集示意图

▲ 图：Meta 设备合集示意图。

你可能会问，现在市面上的 AI Agent 很多啊，我们用到的 ChatGPT、Claude、OpenClaw、小龙虾，以及国内的 WorkBuddy 其实都是 Agent。

Muse 为什么突然又火起来了？只是因为它新鲜吗？还说它有一些独特的地方？

## 01 怎么安装：第一步就能卡住一半人

这篇主要讲 Muse 的 APP，而不是智能硬件。在正式介绍之前，第一步肯定就是安装，这事简单但却会卡住很多的人。

到 muse.ai 去注册个账号，网页端直接用，或者下载 iOS / Android / Mac 的 App 也行。

**不用装 CLI，不用 npm，会用手机就会用** 。

它是个消费级产品，不是开发者工具。

但有个坑：Muse 目前只在 **美国和加拿大** 开放。国内 IP 注册完大概率进等待列表，提示区域不支持。

网上已经有不少野路子教程，我实测下来最简单的就是换个国外 IP，成本一块多钱就能搞定。

![Muse 当前地区暂不可用，用户已加入等候名单](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKYuX8lJXqegrVia8yfxwaPRQDmOSzNGiafojfW37rYQ4wc5ibXVGzF78TwRyOiaUibo4PN2NrJT0XAf4JBnOVVGKpHibic0Qa6uq5Ha8/640?from=appmsg)

Muse 当前地区暂不可用，用户已加入等候名单

▲ 图：Muse 当前地区暂不可用，注册后可加入等候名单。

## 02 聊天：反常识的极简，处处是心机

现在的 Agent 界面早就约定俗成了：选项目、设权限、挑模型，千篇一律。

我以为 Muse 也一样，结果它反其道而行： **就一个聊天框，加左边一排功能按钮** 。

不能选项目，普通用户也没有模型切换入口，默认就是 Muse Spark。

这感觉像梦回最早的 ChatGPT，简单到不像个 Agent。

![Muse 首次对话中的个人助理介绍和应用连接引导](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKXMPuJPl2xVekiajUKKUvGen2SibJlJabVOOOCHNnECtLsIhSIuaIwDdTta5s9KWyQa2vwJ09qQ0U8wrB166DwaUjKDYAvBvIiao/640?from=appmsg)

Muse 首次对话中的个人助理介绍和应用连接引导

▲ 图：Muse 首次对话介绍了个人助理定位，并引导连接 Gmail、日历等应用。

我以为 Muse 也不能免俗，结果发现它还真的不一样。

![WorkBuddy 与 Muse 的主要操作区域左右对照](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJI2LO4EjltYZaA7S6hmJYzXhJiaYgUYFAicnm3I449tOZlo4lt4azutVgZ6iauYCvuRWwShzdtiaNOPNWIk1zsicVEYaEibbWoMug39U/640?from=appmsg)

WorkBuddy 与 Muse 的主要操作区域左右对照

▲ 图：WorkBuddy 与 Muse 的主要操作区域左右对照。

### 主聊+旁聊

聊天仍然是所有AI工具最常用的功能。本来我以为这个东西也没什么好讲的，结果发现这里面也有文章。

我相信大家在用AI工具的时候，很少会一直在同一个聊天框里面聊吧？

大部分应该是会根据不同的任务开不同的聊天窗口？因为我们其实也不能够在一个聊天对话里面一直在聊，因为它有上下文的问题，聊多了可能就会失忆。

Muse 只有一个主聊天，删不掉、归档不了；其他话题都开在「旁聊」里，随开随删。

![Muse 对话搜索面板](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJJqrEpicM3oiaSBen7tiaug1QSic9ysRsz7tjnewDQiaPMNtVksLq1hSA8JwcicJRheHNh57KaKtpuicvgJjEdFelNZiaqiafMRlHtMlmN8/640?from=appmsg)

Muse 对话搜索面板

▲ 图：Muse 对话搜索面板，可按关键词查找历史聊天。

这设计一开始让人看不懂。

别的 Agent 里（比如Codex、Claude Code）旁聊是主线任务中的临时分支，问完就消失。但 Muse 的旁聊其实就是一个普通的新对话。

习惯之后倒也清爽： **一个主聊管长期关系，无数旁聊管一次性任务** 。

### 不用等它说完

现在大部分 AI 还是一问一答的回合制，它没回完你就只能干等。但人类聊天不是这样的，微信里你不用等对方回复就能连发十条。

Muse 默认就是这种模式： **你可以随时打断、连续输出，它也会一次性回你一串** 。

比如我让它画图，画崩了几次，我一顿疯狂输出，它也一顿疯狂输出。

那一刻真的像两个真人在吵架。

![Muse 主聊与旁聊的对话界面](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKpiaqEOTP0AgicRUJKs8PQVMCEWk8Qf9FuKpuehAEqkG2A39km9MsoqiatdFvEZdVteVB9ruypHGkiczYkuySfUoibw6YxmIeib0zxE/640?from=appmsg)

Muse 主聊与旁聊的对话界面

▲ 图：Muse 的主聊与旁聊界面，以及对话中生成的图片内容。

它还支持 **引用某句话再回复** （跟微信里一样），长按消息可以 **删除** 自己发出去的内容。

注意，是删除，不是编辑： **发出去的话改不了** ，这点挺让人不爽的。

![Muse 对话中的消息操作菜单](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJL7EnUMiaZ7qIkOsEDwhondGbhGrldRGOWtDoEs6QSHf3Ixo6u5rgwuS1yHL8cbvmviblkPib0TZaibAibWy72E6ILwGjp5lMP7K6LI/640?from=appmsg)

Muse 对话中的消息操作菜单

▲ 图：Muse 对话中的消息操作菜单。

另外所有对话都支持全文搜索（Cmd+K），主聊旁聊、归档的都能搜到。

### 多模态拉满

识图、生图、改图都不在话下，生图用的是 Meta 自研的 **Muse Image** 模型，个人感觉比 GPT Images 和 Nano Banana 还是要逊一筹。

![Muse Image 图片生成示例](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJI9yBiaAZjMXYLYbRbICiaiaibdzqvSDlKR5O410cIZBluHAgrEwCdYz44nTF506WrBQS1DqmkZK0rQXg38CHuF5lajoWV7RK7PsJE/640?from=appmsg)

Muse Image 图片生成示例

▲ 图：Muse Image 根据对话指令生成图片的示例。

它还能语音转写、生成语音，甚至生成 **最长 15 分钟的多人播客** ，直接下载。

![Muse Podcasts 播客生成界面](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLtdH1fNEI47Om4W1Xx5WjmGJat4yBGEa6aBupvG5gKmIThVHhhyEh7wJgpiaveiczKSicO0JUibibZ7UBB4O3qH74CxJ2WcuX26feo/640?from=appmsg)

Muse Podcasts 播客生成界面

▲ 图：Muse Podcasts 播客生成与播放界面。

▲ 音频：Muse 生成的播客。

我体验下来中文语音质量非常高，几乎没有 AI 味。

视频每次能生成约 10 秒，带合成音效，要长就多段拼接。

▲ 视频：Muse Video 生成示例。

## 03 点开头像：动态、审批、定时、身份全在这

点击顶部那个吉祥物头像，右边会滑出一个状态栏，四个 Tab，设计得相当贴心：

![Muse 头像侧边面板功能入口](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIqmW9vibEUGQI3PhRGmy68oukOAjVvPQLjRGiayibjNDAiaBRq1jJnjxq5TJxCZRQOpnSxtE9oh97jib5l5ohYzCbsrYF11pGEwVCE/640?from=appmsg)

Muse 头像侧边面板功能入口

▲ 图：Muse 聊天界面与头像侧边面板中的功能入口。

📋 **动态（Activity）：** 它帮你做过的事，按时间一条条列出来。

点进去能看到极细的工作记录：比如一段音频是用什么工具生成的、文件存在哪条路径。对 Agent 重度用户来说，这就是审计日志。

![Muse Activity 动态记录](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIsrmmjVRicSmT6PCUdT5rwyPcYgzKxfKLWEJkku9wbEGkYpIZcK1bX21fv8YABIxUuXQM0FUkvr6qRuWy2KnND1h2SJvxVUEas/640?from=appmsg)

Muse Activity 动态记录

▲ 图：Muse Activity 展示任务执行记录和所用工具。

✅ **审批（Approvals）：** 统一审批中心。

发邮件、花钱、删数据这类敏感操作，都要你点一下允许。审批还能推送到手机锁屏，不用打开 App 就能点允许 / 拒绝。

![Muse 审批中心的操作记录](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLTk5k129YR4KNADVTWd6je0qia1yMlISl0jibicYTlxfq5REEkyqR1kwdnFI4ksLmJBoiaIPGkVSSbme5znTj11LekqCp67RBvBQo/640?from=appmsg)

Muse 审批中心的操作记录

▲ 图：Muse 审批中心列出的待确认操作记录。

⏰ **定时（Upcoming）：** 定时任务和提醒都在这儿管，比如每天早上 8 点给你播报新闻。

👤 **身份（Identity）：** 改它的名字头像、调性格、改记忆。

玩过 OpenClaw 的人一眼就懂：这对应的就是 SOUL.md（性格）和 MEMORY.md（记忆），文件可以直接改。

![Muse 身份设置及 SOUL、记忆卡片](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLR9q6oLMwuZES13pFBJN5jGdBO30rFywPkXEIK7dx6VHRM9jXhAIZJA0yWb7zQkaSbMKdN83RFzlia3vmibeU4oJ6D7BH95B3yg/640?from=appmsg)

Muse 身份设置及 SOUL、记忆卡片

▲ 图：Muse 身份设置中的头像、名称、编辑区、SOUL 与记忆卡片。

顺带补一下左边栏：

![Muse 左侧导航栏功能入口](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLpG0NxtvBOTicPB1ozJqAVFIxsltQ6WZ0NDlZrKlAUMLMibMibQ2IiacF3nEfHPFDsNhZ1pP4OBaZgZeeCo5QmlIvwa9GHic9oaZx0/640?from=appmsg)

Muse 左侧导航栏功能入口

▲ 图：Muse 左侧导航栏中的聊天、搜索和功能入口。

这些其实看名字就一目了然了，很多在别的 Agent 里面也能看到。

其中 **Ideas** 特别有意思：Muse 会主动观察你，发现你重复在做一件事，就弹一张卡片问你要不要设成定时任务，或者每天给你推一条 Tips。

它不是等你下指令，而是在主动替你省事。

## 04 文件与本地：它最大的本事是 7×24 在线

用过 Codex/Claude 或者小龙虾、WorkBuddy等 Agent 的人都知道，除了聊天，它更强大的是处理本地文件，甚至完全接管本地电脑进行工作。

muse 理论上也可以，只要打开访问权限就行。

![Muse Mac 应用的文件系统访问权限](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKLXuNwm4cbib4X6aNqBqjMsjRp86ujF63rc83IgzxM5KbOSzSOOYfgOMUD9kgwwthZ3ZGgicia8w9icuqep6vVAckdYZEmTocI6lw/640?from=appmsg)

Muse Mac 应用的文件系统访问权限

▲ 图：Muse Mac 应用的文件系统访问权限设置。

但实话实说，我折腾半天没调通，问它自己，它说聊天和数据走的是不同通道。

早期版本，糙是糙了点。

![Muse 早期版本界面示例](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKf4LxjafujibfaJfwX3US8PurJSTNfT8UVjRbicLeTv6OuzMfETYPu1pY5SNMibZ25n9Jrutn77IytocXK4SZbssCbM700XAIz8k/640?from=appmsg)

Muse 早期版本界面示例

▲ 图：Muse 早期版本的界面与对话示例。

不过这恰恰说明： **Muse 的核心卖点根本不是替你管本地文件** 。

它是一个 **云端 Agent** ：Meta 在云上给每个人配了一台专属主机，7×24 小时在线。

你随时召唤它，它全天候帮你干活：定时任务、监控、播客都在云上跑，你关机了它也不停。

**对比一下：** 想在 Claude Code、OpenClaw 上实现同样的 7×24，你得自己备一台常开的机器（我为此刚入坑了一台 Mac Mini 放家里）。

而 Muse 把这台机器直接送你了，想当个全年无休的「牛马」，云端 Agent 再合适不过。

## 05 连接外部世界：从 Gmail 到「嘴炮建连接器」

Agent 的看家本事是连接外部世界，Muse 里这叫「连接器」。

比如连上 Gmail，设好权限（只读 / 允许起草 / 允许发送），之后查邮件、回邮件一句话的事。

9 月 23 日发布会上 Meta 还宣布： **每个 Muse 都会有一个专属邮箱地址** ，别人给你这个邮箱发信，它能直接收。

![Muse 连接器页面中的应用服务](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIIoIXQ0Ktu6icAGBQc30QRIhANaATUuuOficzaicoDFhYE2Pobz6KLnicYXFJMltmQsYA2ToRLGHA9Ps2A1IRvT96iaEnicrT59ia9yY/640?from=appmsg)

Muse 连接器页面中的应用服务

▲ 图：Muse 连接器页面中已连接或可添加的应用服务。

**最重要的连接器是浏览器。**

注意，是它在 **云端的浏览器** ，不是你本地那个。

比如我让它打开 Bilibili，远端浏览器会直接显示在侧边栏；需要登录点击的地方，它自己操作，你也可以随时接管（右上角有控制按钮）。

浏览器权限是细粒度的：访问网站、提交表单、下载、上传、填密码，每项都能设允许 / 询问 / 拒绝。

![Muse 操作浏览器](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIJU4G6AwtAqoL2rDC27tM8NXdRS70icGn2BIReUyt4no8RfaRkhiaNSAIN44y2lBPznGY7ic02WvZktKQgPUSgDFSgIKg9bQGOz4/640?wx_fmt=png&from=appmsg)

Muse 操作浏览器

▲ 图：Muse 操作浏览器。

有了云端浏览器，野路子玩法就多了。

大家头疼的 Claude 账号注册，据说它也能办。我试了下，卧槽，真的分分钟搞定， **连人机验证都自己过了** ！

![Muse 完成人机验证](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJJ2bKvDf7ib6pt906cN2tKdIXlpuXib1bkzJJrHhllcz54IBFOUnUbyHUs6aehdF75WE5wguWW59skjtQ5PVHUdDh57JZVVzhaeg/640?wx_fmt=png&from=appmsg)

Muse 完成人机验证

▲ 图：Muse 完成人机验证。

**它还能连钱包（Stripe Link），替你在网上下单。** 但每笔付款都要你审批，它不能自己刷你的卡。

有意思的是，前不久 **亚马逊把 Muse 屏蔽了** ，不让它在站内代购。原因也直白：太多订单来自 Muse，平台觉得这动了它的奶酪。

目前它还不支持国内支付方式。

![Muse 账户支付相关页面](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIdf8ibjGSwjeiavtxpIBmYtbn75H0seLeLO6mIq5FC3n8aFhqDGouFnyYJM1Cp1GZIgRYwOgCRCmiadWTLN2icNmFR5zKesur2wG0/640?from=appmsg)

Muse 账户支付相关页面

▲ 图：Muse 账户中的支付或订阅相关页面。

坦诚讲，它默认的连接器不算多，还偏海外。

但 Muse 有个让我震惊的能力： **嘴炮自建连接器** 。你跟它说需求就行，一行代码都不用写：建连接器通常要对方提供 API 或 MCP，这些我也不懂，但它会自己用浏览器等各种方式去搞定。

比如我说想随时看豆瓣有什么新剧，它 2 分钟就建好了，还给了个链接让我一键直达豆瓣；我又让它连上 DeepSeek，现在直接在 Muse 里跟 DeepSeek 对话。

![Muse 通过对话创建连接器](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJISvsKgRAwdSACOxdVPmZ3CnF6PrdarWuHq3NhuK7uhGG5FqrFwvH2qFdyvz6uSECmiaaIhV46EAC9pdgoCp2yp2dXialb7bISzU/640?from=appmsg)

Muse 通过对话创建连接器

▲ 图：Muse 根据自然语言需求创建自定义连接器的对话过程。

它甚至还提供了链接，我能一键点到豆瓣上去，这太他妈强大了。

![Muse 创建连接器后的结果和访问链接](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIMxfGMibjrx2e9yTiaILgziasTKzRt0v6ZQGXaibQth541vlEt37ebYo11u1gyGEZtE735lwOKPteRmGLK0Vian4icS8DARicP687oN0/640?from=appmsg)

Muse 创建连接器后的结果和访问链接

▲ 图：Muse 完成连接器设置后返回的结果与访问链接。

![Muse 中 DeepSeek 连接器配置](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKDTQPxAnHn6icYtlQE7IkEpJ480n8cV3B465Z6482zHRhSX2NnFRVC2lFicCXEzm0icmSsphdcuDkoMOCc7oHQbWIDBtXeTR2E9E/640?from=appmsg)

Muse 中 DeepSeek 连接器配置

▲ 图：Muse 连接 DeepSeek 的连接器配置页面。

有些自建的连接器在设置里看不到，问了它才知道：它是直接给我写了个 **Skill** ，效果等同于连接器，装在云主机里。这就引出下一个话题。

## 06 Skills：全内化了，斜杠调不出来

我相信很多人跟我一样，在用Agent的时候会大量使用到Skills，会把大量的重复的任务都做成Skills。

我们习惯了在聊天框里面使用斜杠来把一些Skills调出来。

Muse 默认集成了不少 Skill（生成文档、整理资料等等），但你用斜杠只会看到系统命令， **一个 Skill 都调不出来** 。

![Muse Skills 页面中的内置技能](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIUWpOS3wia3wAOhhqcicIG95ibsib0Ufyj66jHyQ3jYmQqEPiacvTJD9KXkicVicic5EepSyneQBG7CUibtB7TiaVj7icmpBC0hqyFFicnzHg/640?from=appmsg)

Muse Skills 页面中的内置技能

▲ 图：Muse Skills 页面展示的内置技能与可用状态。

这是 Muse 的一个大不同： **Skills 全部内化了** 。

你不需要指名道姓调哪个 Skill，它自己判断这个活该让谁干。

我倒觉得这才是对的：用户只管说人话，调度的事交给它。

Muse 的 Skill 遵循业界标准格式，别处的 Skill 也能装，统一放在 **~/workspace/skills** 目录下。

## 07 连接方式：App 只是其中之一

除了网页和 App，Muse 还能通过 **WhatsApp** 直连。Meta 亲儿子嘛，聊天会进到一个旁聊里，相当于把 Agent 塞进口袋。

![Muse WhatsApp 对话示例](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIFDoiatPvAsMbwvW3C562bf8YOdn7d8uiaic9b1b09hD4HFHaT5ibLfgKQZabxKf6hwibIq3WJAYstmaPoM5N3DFdZcenP89VQLRjg/640?from=appmsg)

Muse WhatsApp 对话示例

▲ 图：Muse 在 WhatsApp 中的一轮提问与回复。

真正让人眼前一亮的是硬件。

**Muse Charm** ：钥匙扣大小，2 英寸小屏幕，内置 5G，按一下角落的指纹键就能直接跟 Muse 语音对话，不用掏手机、不用解锁。

屏幕上住着你的专属形象（默认那只吉祥物叫 Jolly），活脱脱一个 AI 版电子宠物。计划 12 月发货，价格还没定。

![Muse Charm 智能硬件实拍](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKqVw3onicyOgWMhPMXzA6bfezKUb5ptBomA2Bkvwa3MYzObuYSlM77vszm4qLDtx2IL8icoayXX5VXE0bhialo42XcVoNHVXhRPU/640?from=appmsg)

Muse Charm 智能硬件实拍

▲ 图：手持 Muse Charm 智能硬件的实拍图。

▲ 视频：Muse Charm

Meta 的算盘很清楚： **手机之外的每一个触点，都塞一个 Muse 进去** 。

**头像视频聊天：** 9 月 23 日发布会上最科幻的一幕。

Meta 推出了 **Muse Realtime Avatar** ：你可以给自己的 Muse 定制一张脸、定制一把声音（直接描述就行，比如"说话慢一点、带点英音"），然后跟它 **实时视频通话** 。

注意不是播一段录好的动画，而是一张会动、有表情的脸，跟你面对面聊天；你边跟它聊，它边在后台替你干活。

这一步，等于把 Agent 从「聊天窗口」变成了「视频那头的一个人」。

▲ 视频：Muse Realtime Avatar 实时视频通话演示。

Mac 用户还有两个小甜点： **Option + 空格** 随时唤出快速聊天， **按住 fn 键** 能在任何 App 里听写。

9 月 23 日发布会还宣布了 Mac 电脑的正式支持和头像视频聊天，Muse 正在从「聊天窗口」变成「无处不在」。

## 08 Computer Use：电脑操控

最近大家都被GPT 6 Astra的电脑操控给震惊了吧？这个功能Muse也支持。

![Muse Computer Use 权限设置](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJJelRWVTN0qLx9vlttNL8pNY3AYCkrLKyFO4n4ajjKSHZqIRwk7h0UbMZPdtXQXs4cZkKjcicvkU7Ua16qmZLAOtTvDEB8DGicibU/640?from=appmsg)

Muse Computer Use 权限设置

▲ 图：Muse Computer Use 的电脑操作权限设置。

配置项里面的 **Computer control** 和 **Browser automation** 默认都是 **"Ask every time"（每次询问）** 。

还有个 **Blocked apps 黑名单** ，加进去的 App 它看不见也用不了，比如银行、密码管理器这类，建议第一时间加进去。

但实际情况嘛……跟第 04 节的本地文件访问 **一个德行** 。

我兴冲冲让它"用我的电脑打开 Keynote"，结果我的 Mac Mini 在它那儿显示离线，根本用不了。。。

早期版本，糙是真的糙。

## 09 收费吗？适合谁？

**大部分功能免费** ，重度用户有付费计划（用量 / 订阅）。现阶段先用免费版完全够折腾。

![Muse 计划与用量信息](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKYUkm37Ez4CiaGbY5PQu19v6AicibccqTVEdKsBq2vGMWViaJ2VYoFrbficFq4JybaxBQm0o5vLtZKElqgY8VM1micD9iaO0nPztkF6I/640?from=appmsg)

Muse 计划与用量信息

▲ 图：Muse 当前计划的用量或订阅信息页面。

Meta 不愧是做社交出身的，把裂变这事玩的明明白白。现在每个人可以发 30 个邀请码，每个邀请码会给双方带来 10 亿的Token。(只用来薅 token，不能通过它来注册)

我这个邀请码：ZIIBN5 还可以用，需要的话拿去用吧。

![Muse 邀请好友奖励页面](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIoqIWTGLBfjweTaMGx5OGKqNrMs9mc4JiaDicBm7xApxuNoP99qSpSRePWtUibDMSZic1xM72cUNa5IsyAwcs5IrNToE1jIEMHY9g/640?from=appmsg)

Muse 邀请好友奖励页面

▲ 图：Muse 邀请好友页面及对应奖励说明。

Muse 到底适合谁？

✅ **适合：** 想要个 7×24 待命的数字助理的人；重度依赖 Gmail、日历、浏览器办事的人；愿意折腾连接器和定时任务的极客。

❌ **不适合：** 想让它管本地编程项目的人（Claude Code 更对味）；国内用户（先等区服开放）；对 Meta 有信任心结的人。

一句话总结：Muse 赢的不是模型，而是「替你把事办完」的完整体验：云端 7×24 待命、嘴炮建连接器、内化的 Skills，再加上 Meta 把 Instagram / WhatsApp 的流量往里灌。

## 10 翻到底层：一个「公开的秘密」

在 Muse 里乱点，点出一个疑似没藏好的界面：它的文件结构长这样。

![Muse 云端文件目录列表](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJLsUYpDmvx4MQYK3Fg5gLHgGBX4wHN1rtcoTLQfUdUDIkJqkr9ErvnTgnGRkCSTGeGwJE9vibgEvJnyKPS2nPicia1uCz7I2wk5NI/640?from=appmsg)

Muse 云端文件目录列表

▲ 图：Muse 云端环境中的文件目录列表。

📁 **memory** ：长期记忆库，记着你的偏好、做过的事、重要的人  
📁 **workspace** ：工作区，它创建的文档图片音频都在这，你收到的文件也从这来  
📁 **user** ：你传给它的东西，比如截图和文件  
📁 **hooks** ：事件触发的自动化（比如「收到某类消息就提醒我」）  
📁 **channels** ：消息通道配置，比如刚连上的 WhatsApp  
📁 **docs / agents** ：产品文档、它的「分身」（子智能体）干活用

几个.md 设定文件每次对话都会加载： **MEMORY.md** （长期记忆）、 **USER.md** （你的基本信息）、 **SOUL.md** （性格和说话风格）、 **IDENTITY.md** （它是谁）、 **AGENTS.md** （工作手册）、 **TOOLS.md** （工具备注）。

这些文件 **都可以直接改** ，想给它换个性格，改 SOUL.md 就行。

熟悉开源项目 OpenClaw 的人一看这结构就懂了。

Meta 官方自己也承认，Muse 深受 OpenClaw 的启发（"heavily inspired"），但强调是从零构建的。

所以这可能也不是什么 bug 泄密，而是一个公开的致敬。文件结构像，是因为本来就师出同门。

我在开头的时候说了，Muse提供了一台云主机给了我们，这不是吹的。很多人已经就是破解甚至进去了。

对于我们大部分人来说，可能你不需要这个功能，但是你可以了解一下。其实也不神秘，你可以直接问它，它是一台什么样的机器。

![Muse 对云端环境的说明与 Linux 操作示例](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJK2JkXw2DffWZniacDmjGWn5Pd5xLBteWKPAibp5yIoKKuRfIayicCbnAxG1Nnn2F1zheSqyx8yUoQBHtdqUSD9kq93qt2k179hlE/640?wx_fmt=png&from=appmsg)

Muse 对云端环境的说明与 Linux 操作示例

▲ 图：Muse 对话中解释云端环境并展示 Linux 操作指令。

你也可以运行一些Linux命令。

![Muse Linux 命令输出示例](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJK5UD83xAA4vwf6kZhefeQEyH5kZdQjMBsWkH1mytgtAicvshLMH5dZJOaeHK7vjGjmNId2gZ0ycYPzaMeVDFVq1vLiaX9S6rY8I/640?from=appmsg)

Muse Linux 命令输出示例

▲ 图：Muse 返回的 Linux 命令执行结果示例。

## 12 写在最后：为什么 Muse 让我惊喜

折腾了几天，总的来说： **体验非常好，产品设计也非常好** 。

但最让我惊喜的不是某一个功能，而是：这是为数不多的、没有复刻之前东西的产品。

现在的 AI 产品大多长一个样：聊天框、模型选择器、插件市场，换皮不换骨。Muse 偏不，它很多地方是重新想过的。

随便数数它的创新点：

💬 **微信式聊天** ——可打断、连续输出、引用回复，把"回合制 AI"变成了"人类式聊天"；  
🧠 **Skills 全内化** ——你只管说人话，调度的事交给它，斜杠命令可以进博物馆了；  
🔌 **嘴炮建连接器** ——不会写一行代码，也能把豆瓣、DeepSeek 接进来；  
💡 **想法卡片** ——AI 主动观察你、替你省事，而不是坐在那等你下指令；  
☁️ **每人一台云主机** ——7×24 待命，你关机了它还在替你干活；  
🛡️ **统一审批 + 动态审计** ——敏感操作先问你，做过的事有据可查。

更不一样的可能是 **理念** 。

别的 Agent 在卷"更聪明的模型"，Muse 在卷"更近的距离"：手机、网页、WhatsApp、Mac、眼镜、Charm 钥匙扣、视频通话里的那张脸。

它想变成一种无处不在的存在。你不用去找它，它就在你身边。

Zuckerberg 说目标是 personal superintelligence，听着像画饼，但当硬件矩阵摆出来之后，这个饼至少有了形状。

当然，糙的地方也得认：本地文件和Computer Use都用不了、Meta 背了多年的信任包袱（只有 8% 的人愿意把密码交给它）。

但瑕不掩瑜。方向对了，糙可以迭代；方向错了，再精致也只是复刻。

如果你问我值不值得折腾，我的答案是： **值得** 。

不是因为它现在完美，而是因为它可能是第一款让你觉得"AI Agent 就该长这样"的产品。

iPhone 时刻有没有到来我不知道，但用完 Muse，我似乎很难再回头去忍受那些只会一问一答的聊天框了。

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过