# 从0到1带你速通DeepSeek Harness。

**作者**: 数字生命卡兹克

**来源**: https://mp.weixin.qq.com/s/xkC1aenHFNSH2BxyzLDfcA

---

## 摘要

DeepSeek正式发布了其Agent产品DeepSeek Harness，该产品秉持“一切皆插件”的核心理念。与传统Claude Code等将底层组件封装在软件外壳内的产品不同，DeepSeek Harness基于“Agent=Model+Harness”公式，直接将工具、沙箱、工作流等底层架构暴露给用户。

---

## 正文

数字生命卡兹克 数字生命卡兹克

在小说阅读器读本章

去阅读

在昨天正式发布DeepSeek V4 Pro正式版之后。

预告了很久的，DeepSeek家自己的Agent产品终于也发出来了。

名字叫，DeepSeek Harness。

理念也很清晰，一切皆插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWsyllkoVib5U1haqPOzOQY1Q1lolbcG5Q5fLMV8n7eVA9ibKnyzmViaW8ywH73SOuLJL8j2icGZ8LA1u2kuMia02CEZrBcZaIQGPdY/640?wx_fmt=png&from=appmsg)

可能是有史以来最快的速度，截止到我写完文，它在Github上到了3万7的Star。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXlSqiaDYiczSGjRDiaBDiaXCmia4Q8cibLHaMIS1lUR04dHibkN8EhmlTpwv7aVu5rAJBDahojsXhWbGGR3sNTrHsJton5VGH7L6g80A/640?wx_fmt=png&from=appmsg)

说实话，我在体验完，又完整的扒了开发者文档，用了一些插件之后，我觉得这确实是一个很特别的产品。

这也必然是个二极管产品，喜欢的人会觉得，这就是未来，不喜欢的人会觉得，这玩意太糙了毫无用户体验谁用的明白啊。

所以，我也想用这篇文章，来试图聊聊几个问题，我理解中的DeepSeek Harness是什么？为什么不用DeepSeek Code要用DeepSeek Harness这个很工程的名字？以及这玩意到底应该怎么用。

先来聊聊，DeepSeek Harness到底该如何理解。

DeepSeek在官网上放了一条很重要的公式。

**Agent = Model + Harness。**

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVDCWghmvnxBQBSIsCZpSK6VlBv5WaLtx9JEElxTaZvhXdib8w6h1ibiaRBAdlPkAOtZKSQqDZ9icmCGdYIiaziaKJ1MOs1iaKIVy5duY/640?wx_fmt=png&from=appmsg)

这个公式，是LangChain之前在聊Agent Harness的时候提出来的，一个好的Agent，必然是由Harness和模型一起构成的，对Harness不了解的，可以去看看我之前写的一篇科普文： [一文带你看懂，火爆全网的Harness Engineering到底是个啥。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647681527&idx=1&sn=27dfac445fe88042e182ab3f3c6388b0&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqX7ia277ntK8GbGJOdzMWIaO86GxEWyAia4UZsdU0OibmU8Nl6fiaicfC5L9qRiaTqHXgT3BicnoMhArVv9iavbsajxeEjBTmIk2g6oaaQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

你用的Claude Code、Codex、Workbuddy这些，本质都是Harness，要跟模型比如Claude Fable 5、GPT 5.6-Sol这些搭配起来用才行，要不然就是个纯空壳。

而一个Harness的构成，其实还是蛮复杂的，东西特别多。

工具、Skills系统、会话、沙箱、存储、Agent循环、调度、子Agent、工作流等等等等。

在过去，这些所有的东西，都是被封装在一个以软件为名的壳里，比如Codex。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWVjr3SMkEVFiaZDjAvTibWgCLfMhIdGy61793fP3utFbcezvSWfDygvSXIqyaficbEZUHdpgrqB6OKFSicYmv9hQUzicQB1EneT5Jc/640?wx_fmt=png&from=appmsg)

我们上面所说的一切，几乎都是厂商自己做好的，我们更多的是在用对方持续不断提供给我们的软件服务，也就是一个产品，而那些东西，全都被藏在了后方，普通用户是看不到的，也不需要知道。

普通用户真正要做自定义管理的，其实就是Skill、MCP之类的，其他的所有东西，全部都是Codex封装好的，你改不了，没事也不会去改。

而在DeepSeek Harness中，所有所有所有的这些东西，全部都被包装成了插件，也就是说，你全部都可以自定义。

就很像我们以前玩过的所谓的模块化手机，所有的硬件部分都可以我们随便改。

DeepSeek Harness也类似，真正的核心只有一个东西，叫Cordis的内核，这个内核的作者加入了DeepSeek，然后这一次，他们甚至发了一篇88页的论文。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXr7I6dUibGicB4sxppZqZibicMgtRogM10R0WRl0qXdKpv25aA5iaeC6bfKsxGbzchPZvVoSDg66lIatLDRvhcYwK0xq7cdiajsp3aI/640?wx_fmt=png&from=appmsg)

这个内核干的事情极其克制，只负责插件的加载、卸载和依赖管理，其他的什么都不管。

最牛逼的是，可以在Agent运行的过程中，随时更换插件，还能保证Agent运行状态不崩。

核心是两个特性：

**Temporal composability，时间可组合性，也就是** 一个插件卸载之后，它之前产生的副作用能不能完整撤销。

**Spatial composability，空间可组合性，** 一个插件如果依赖其他插件，当其他插件出现、消失、改变时，它能不能动态地重新处理自己的依赖

所以你看这两个特性你就懂了。

整个Cordis的内核本身，是为了让Agent在运行过程中不断的给自己开发、安装卸载插件，不断的插拔自己给自己添加和删除能力，从而形成某种意义的自进化。

这就是DeepSeek Harness的底层机制。

所以与其说它是一个Agent产品，不如说这是一个为了展示Cordis内核给大家预设了100多个一方插件的科研成果。

这也就是DeepSeek反复强调的理念：

**一切皆插件。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVgUkt1y54wnM0TIFWjsbEUTtWDgnK0uObO5Wl4eHibhmo59NcmGSQzTFL90icuibTPUbk92tcdtWqosowAeHDhr6eAapAWlYTkMs/640?wx_fmt=png&from=appmsg)

所以，现在你也知道，DeepSeek为啥叫Harness，不叫Code和Build之类的，为啥这次的版本，也叫开发者预览版。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWAzPr11McCzwMoy4ubIicLx7GtDAQRbia9krkhicu0zZXw0Xt5fojh7wRf6DDYPcj4JCHE3dTWSrYMwdwbstTOEGS0T6a9GKZN6w/640?wx_fmt=png&from=appmsg)

因为人做的不是Agent产品，人做的是一个基建，是Harness系统。

它需要全世界开发者进来，来一起插拔，帮他做各种各样的插件出来，丰富整个DeepSeek Harness的生态，从而形成一个新时代的平台，同时完成Agent的自进化。

所以，整个社区，才会吵得不可开交。

一边说这个理念太牛逼了太好了，另一边说这玩意鬼才用，我为什么没事要插拔。

一个新事物诞生必然有他的争议，但是无所谓，我觉得对于大家来说，最好的方式，还是上手用一用。

官方网址在此：

https://www.deepseek.com/harness/

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVxpgQ2ibcCOiaeXhMsrzfIgxuibIqw3t9aSujkWObIP4jhcAOjtkeV9unOns5ABL2Fice1jSjiadW5V9jVf5Uib9zDmUGam0IVJCRsk/640?wx_fmt=png&from=appmsg)

安装命令：

```nginx
npx @deepseek-ai/dsh web
```

你要是看不懂，不知道咋运行，那就把这个命令随便扔给任何一个你的本地Agent产品，让它帮你装。

装好以后，就会给你弹出一个本地网址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWFsvicEY8AribraC0Aj6vUxicVMUGuiatBHYNrIsvJs2A5gCVUVvSpjyuLYeQIwjKD0ibhVhE6ibMWICotRQqTvbtM7kMMtrbRtDXNM/640?wx_fmt=png&from=appmsg)

你直接复制到浏览器打开就行。

第一次运行会让你填上你的DeepSeek API，你去官网搞一个就行，记得充一点钱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXV2k8wfJIjZN2d53fb8vUVY1DLPWOWwEia6gHcd00VkUyBJj4saaEaujrVpH6ns0raRZclpqibwibjwB5jiavH8HLIbwImBTNqmsM/640?wx_fmt=png&from=appmsg)

API开放平台官网：

https://platform.deepseek.com/

贴好以后，就可以进入到首页了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXwKaQ94gllVicBgGvSzIXkibhMyMMXgxiaJs7A8JcRmlvibuMXfaUH1f0KV2cf5RHj9H2jGcmbHURpY2ErX950UEWRy4dPRAm4cw4/640?wx_fmt=png&from=appmsg)

一个标准的WebUI界面，甚至这个界面本身，也是一个UI插件。

所以这个UI界面，你也是可以随便改的。

比如群友@黑哥小黑子（blake，随手就做了皮肤插件。。。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVm7wjSRswFNmh7PymibolxbLEceU5ahEZ2736FgicUVEFpQT4hFQNVic7DtzzHxqj2HzKPj6Hq2cFv5It7Bjic7mZdmXL8hf6g93k/640?wx_fmt=png&from=appmsg)

然后模型这块，可以选两个，Flash和Pro。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWHmXViakTWdvxvmAawfuH6ne0I2vGXAGL9mDEhfnZiapOUQKLEgqzic6ESwG5Mv4riak4RukCtpibpUiakOSOqKXYBL8jiazxCwP7W04/640?wx_fmt=png&from=appmsg)

也可以选思考强度。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWypeF5qvmjQEAzQ7UicYfz9KB71VMdIYfR1o7aVnSqmZkEmP5yDUGaD4pIk7h4eAkAvGwRlXJElpGAeAHJgf6ibdyxVtAQegBws/640?wx_fmt=png&from=appmsg)

这里模型需要注意一下，DeepSeek也正式官宣涨价了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVib9hXjuYk6hDiaeZuRtcDBPzB8g0BeQLj9voBkiczwrU6eesbwc51dq3hv0cA1DkUKJWVLhicmzRytfn503Wma6IWe8QZMUqFFiac/640?wx_fmt=png&from=appmsg)

而且涨的不是一丁点两点，这个涨幅说实话，是有一点离谱的。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWzmic2tAc1YZJribldL8REXhwNQwICYTia4dIyzT9HewnxjqNnNEewDpMiaqWSVficGXQRPGjbNf3lqprAWx701uiaVya7gXlPyHgrc/640?wx_fmt=png&from=appmsg)

V4 Pro的缓存命中价格，直接涨了12倍。

高峰期的输出价格，直接来到了离谱的27块钱。

这个价格的性价比配合DeepSeek V4 Pro的性能，我是觉得从曾经的价格屠夫一下子少了很多的吸引力，我之前预测就是2倍左右，结果高峰期涨价实在有点太狠了，起步都是3倍。

给大家对比一下现在其他主流模型的价格。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqURvH9hSBU2u8elH5o6TicLmSFYtvYRHE4MsSMBx9U6aiaYYsROYfsxxBdKtR3HnRLQ6ow39t1NEAkUdXLL4OUzyic5OiaxFX1yRnQ/640?wx_fmt=jpeg)

其实跟GLM、Qwen 3.8 Max已经不是特别能拉开差距了。

更别提GLM-5.3应该马上也要发了，价格大概率是不变的，能力基本上又是个开源SOTA，那DeepSeek V4 Pro的性价比，单从API角度来说，就可能比不过GLM了。

而在DeepSeek Harness里，其实也并没有把你锁死在DeepSeek模型上。

它支持添加目录里的模型提供方，也支持自定义提供方、Base URL、协议和模型列表。以后你完全可以把别家的模型接进来。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVjcBtbvIAedTcE3CqDOnfze6IDtX02kV7foHBqQ6qmibZ1E2AzEKD6j8Xen1d3xBdicOGcDbgK432U3BlJiagrL0E4olF9FEkFNY/640?wx_fmt=png&from=appmsg)

比如，你就完全可以在DeepSeek Harness里用GLM。

然后回到首页，点击“选择工作区”，添加一个项目目录，这就是你的Agent，能操作的项目文件范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV5c8Rh2aK0LJUS0lsbRWcyaoy1wPoa9eDroT5UHlKYg8YTQKMicMPwAE5buTicRQEXR66EBZZaRrOed3OTMugM6icFYnF9jsEzDU/640?wx_fmt=png&from=appmsg)

接下来就是最特别的了，也是普通用户最难理解的，大家搞得最懵逼的，四种模式。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWRwyz6Zl9m0HlicmN2fBibJ1GhKcTP2CZVu4jgu9kUM7tSVQcUshkLuPXq1vNmf8JKZSrjpd2aD5VOiaL0AIUcWSxAxLfY1xCd48/640?wx_fmt=png&from=appmsg)

我觉得大家在前面知道了DeepSeek Harness的内核Cordis之后，千万不要把它当成是DeepSeek Haness真正的模式来去理解。

这就是他们给你的几种模板预设，对，就是纯粹的模板，方便你开箱即用的。

然后我简单的说一下四种模式的区别。

1\. 标准模式

你如果是第一次使用，或者对底层机制没有那么了解的，相信我，无脑选择标准模式就可以了，标准模式拥有完整的代码Agent能力，包括文件读取与编辑、Shell、文件搜索、网页搜索、Skills、计划、目标、后台任务、子Agent和工作流等等，这些插件都已经给你预设好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVI7yFs5gXPBL0lwPMfHyHWtg16o9NibGCaW6O1xFibh7XuKqRwAt8ldmLGwib1kLP2p1OLYhQl5Ns64SLj6OgZNC9eD6hTFqibQ6E/640?wx_fmt=png&from=appmsg)

2\. PTC模式

PTC模式拥有标准模式的全部能力。

区别出现在工具呈现方式上。

标准模式里，模型通常发起一次工具调用，拿到结果，再决定下一步。PTC模式会给模型一套Code Mode SDK，让模型写一段TypeScript程序，在一次 `run_code` 里组合多个工具操作。

原来可能需要五次模型往返的读取、搜索、筛选、并行调用和结果整理，有机会被压进一次程序执行，这会减少模型与工具之间来回对话的次数，也更适合结构化、多步骤、可并行的操作，同时也更省Token。

但是这就需要模型具备足够稳定的代码规划能力，调试难度还挺高的，小白先不用碰，就用标准模式就行。

等你遇到大量重复工具往返，或者想测试DeepSeek模型的程序化工具调用能力，再开PTC。

### 3\. 极简模式

极简模式只给模型两个核心工具：一个持久Bash，一个 `文件编辑器。`

它还会把系统提示词固定成一句非常简单的“你是一个有帮助的软件工程助手”，去掉上下文压缩和大量额外能力。

这个模式主要用于最小环境下的模型基准测试。

就比如你想比较两个模型裸Agent能力时，它非常好用。

`但是没事别日常用，你会发现根本没法用。。。`

### 4\. 创造模式

这个才是DeepSeek Harness最特别的地方。

创造模式拥有标准模式的完整能力，还能检查自己正在运行的Cordis环境，在内存中试验插件，帮助你创建新的Agent和插件。

就是说，它能让Agent直接改造自己。

比如，你可以告诉它：

“帮我做一个只允许读代码、不允许改文件，专门负责安全审计的模式。”

也可以告诉它：

“帮我做一个接入公司内部搜索、固定使用某个模型、拥有三种专属Skills的研究Agent。”

甚至你可以先让Agent来检查自己身上已有的插件和能力，如果你发现它没有某个插件的话，可以直接创造一个插件，然后直接挂到自己正在运行的流程中。

用一个比喻来说，就是Agent发现自己没有扳手，于是现场造了一把扳手，插到自己手上，接着用这把扳手继续干活。

这个是整个DeepSeek Harness的最核心的特点，也是Cordis内核最棒的体现。

然后DeepSeek Harness还有一个对开发者很友好也是很特别的一点。

就是他们把会话设计成一份只追加的事件日志。

模型看到的系统提示词、用户消息、推理内容、工具调用和结果、权限变化、上下文注入、压缩、子Agent调度，都会成为日志里的事件。

下一轮模型看到的历史，也是从这份日志重新推导出来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU8fpu6fAlmtjenAg2VboY5BicqJMBxP5TrpTF65kTMcGz97sibOKSpLUn85bOzicB7fbAq0dGgibia51fzvVMU9kQt8ShEZz4jmNRg/640?wx_fmt=png&from=appmsg)

这件事还是挺有意义的，价值很大。

很多Agent失败以后，你只能看到任务失败或者无限循环，根本不知道它在哪一步开始跑偏的。

Harness里的轨迹视图可以按来源查看每一次运行，对开发者来说，这意味着可观测、可审计、可复现，非常适合做研究。

目前官方的第一方插件，你都可以在设置页面的插件里面看到，看不懂也不用管，你直接用就行了。

如果你觉得缺什么，你也可以用创造模式自己造。

跟DeepSeek Harness一起上线的，还有社区插件入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUzDKufsnaZ3TZ3q36u9Dph9Ryj88aRjJDIH1N0OzocbC0qYaeX5NyuI8ncoefbegqe2Yay34pbsHgWCJN1qzlrrUSMaibbgiaqI/640?wx_fmt=png&from=appmsg)

有很多开发者开发的三方插件。

我挑了一下，有些不错的，我觉得可以推荐大家装上，能大大的增强你的使用体验。

1\. dsh-at-file

https://github.com/omdsh-dev/dsh-at-file

装完后直接在输入框@就可以调用文件了，很方便。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVvrNllYFBoj12ANoh6FHib18e7nW6PcqGw4h2QEOcVNqcbbw6Ezjhr6H2ZCOh4OTEh9dVNSZp6tBBv8A5KaAH4zeLcVM1jIpkw/640?wx_fmt=png&from=appmsg)

2\. dsh-genui

https://github.com/omdsh-dev/dsh-genui

允许模型在回复里直接渲染图表、表格、表单、Diff、Mermaid、交互面板之类的，很有用。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXia2y80Kv1xk90zCEyraZb3pkhicXXzVl9fL1zVt5CLIZYictxGyOCNZKCumWEfZ2kNibdjvgDsopJgugZaukqk02iaxn58dYWJbXk/640?wx_fmt=png&from=appmsg)

3\. dsh-automation

https://github.com/titanwings/dsh-automation

给DeepSeek Harness补上了自动化的能力，刚需，就是这个交互感觉做的稍微有点问题= =

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqURTDxDwddIqBCKJ9O6ibK09XYaLbehszftTJufBBOpyuEmKRiaU3CpxamFScJiavj7p9DtrP6cQgWVkVJ6sOLybbQk9LnnXtQz3Q/640?wx_fmt=png&from=appmsg)

4\. DSH-better-sidebar

https://github.com/omdsh-dev/DSH-better-sidebar

直接给 DSH 补上了一套类似 VS Code 的工作台，文件管理、代码编辑、真实终端、Git、Diff、内嵌浏览器、后台任务和子代理状态，全都塞进了侧边栏里，能让功能更多，也更好用一点。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXsBD3TcIcYX1h6niasvOf6H6aM1148vljdiaH7hfMw9Ob3RKNmAgMiaDVeSNiaymGWbgJJTIYco4QWkTZyvWpz2fGG4Ydia2r4NANk/640?wx_fmt=png&from=appmsg)

5\. ModLens

https://github.com/liustack/modlens

给纯文本的DeepSeek模型补上视觉能力，配置好视觉通道以后，直接往对话里粘贴图片，模型就可以读图了，刚需。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVgibkk2icqIWCmNM0vvF5tJXsiabKfWlR5lwmBA3Ww6v0ZrnBIibHggvWVPJTOEkc1CKmict1U4cE56g6o2LjibNg6dCepicxgYFhATc/640?wx_fmt=png&from=appmsg)

总之，这个Hanress的其他有趣的地方，就交给大家去探索了。

最后，我还是想说。

DeepSeek Harness是一个非常有趣的系统，插件插拔的概念也很棒，但是从产品角度来说，其实对普通用户还是非常不友好的。

过多的开发者术语、过高的使用门槛、过少的功能、过差的用户体验，每一步其实都是会让普通用户劝退的。

但是DeepSeek可能本身就是这么一个更加注重科研和探索的团队吧。

就像他们的Slogan所说的。

探索未至之境。

加油，DeepSeek。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过