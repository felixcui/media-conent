# 我给 WorkBuddy 加了一个浏览器 Skill，它开始自己上网干活了

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/yH7-cbPDHNuzwuf9rxKcLA

---

## 摘要

作者在研究PC端智能体时发现，Agent自带浏览器工具在处理登录、动态加载等复杂网页操作时易出错中断，为此引入了开源的BrowserAct浏览器自动化工具。该工具可作为Skill安装到。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

最近我一直在研究 PC 端智能体。

包括 OpenAI Codex、Trae Work、WorkBuddy 这类工具。它们已经可以直接操作本地文件、运行命令、编写代码和调用各种 Skill。

不过在实际操作中，有一个容易出错的地方就是：浏览器。

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyTKWKjxrXWPk2mWCMYob7YjafUUv7ic5RA9VWMrX8WC7p9gYjCib50ic4tNsqTkiaolibdvicf34dxp0Al05ahFPSI77iczZWpSNDPd2A/640?wx_fmt=png&from=appmsg)

使用Agent避免不了，让Agent操作浏览器，打开一个普通网站，或者搜索一篇文章。这些都是Agent的基操。

但是如果涉及到稍微复杂一点的浏览器操作，那么Agent自带的浏览器工具可能就不行。

比如进入需要登录的网站、读取动态加载的数据、同时处理多个页面，或者遇到验证码和扫码登录，遇到这些情况任务就有可能中断。中断后再次进行跑任务就费时间，费token。

最近发现一个专门解决这类问题的浏览器工具：BrowserAct。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySHKhIxyJ6LMf4x3ugNYPf2Jicnmb2f4fX6MbKp8zFElWkD936UdXYXFrepE8Qgic7bxN0OBic3yIBkhnELDZdSUewQ7VUczMaibns/640?wx_fmt=webp&from=appmsg)

## BrowserAct 是什么？

它是一套面向 AI Agent 的浏览器自动化 CLI，可以作为 Skill 安装到 WorkBuddy 这类桌面智能体中。

内置三种浏览器模式，按需选用

1. chrome 模式（复用本地 Chrome 登录态）
2. stealth 隐私模式（每次会话全新指纹 + 代理轮换）
3. ③ stealth 固定身份模式（稳定指纹 + 稳定 IP + 稳定账号身份）
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQoSuBL3eJsJBP3gBJ4QeRveWULUyiasgfmh4321WAxYONJ5Wibhibq3oXY6xK30vZoE5WNMnlGq38n4xUibAvrxrRIoxu1IxiaJcxg/640?wx_fmt=webp&from=appmsg)

安装以后，WorkBuddy 不只是“能打开浏览器”，还可以在真实浏览器环境里继续执行任务。

简单来说，BrowserAct 相当于给 AI Agent 准备了一套专用浏览器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRnM5j2uQNIOVzXLFGbGBK49tOfyZ1CznXFALTiaqDkA41as0icMe1UK4ep5Mc4pH2Nj5PHnhGhGoFjuZl4Fv0OuYGKAtBMfy0XA/640?wx_fmt=webp&from=appmsg)

普通的网页读取工具，很多使用是直接通过接口获取到网页源代码。如果网页使用了JavaScript动态渲染，或者需要登录验证和复杂的交互，那么读取到的信息就并不完整。

BrowserAct 可以直接操控真实浏览器，并且可以做到点击网页元素，复用本地Chrome登录状态，管理浏览器的Cookie，Profile和Sesssion，多个网页并行运行，遇到登录验证这些必须人为操作交给用户接管，最后还可以把浏览器操作工作流制作为skill进行复用。

项目目前已经开源，支持 Windows、macOS 和 Linux，也能接入 Codex、Claude Code、Cursor、OpenClaw WorkBuddy等可以运行命令和加载 Skill 的 Agent。

## WorkBuddy 中安装BrowserAct

输入下面这段提示词，让workbuddy安装BrowserAct浏览器自动化skill。

> 请帮我安装 BrowserAct Skill。 Skill 地址： https://github.com/browser-act/skills/tree/main/browser-act
> 
> 完成安装后，检查运行环境并验证 BrowserAct 是否可以正常使用。 如果缺少依赖，请帮我完成安装，但涉及账号、代理、浏览器身份或安全配置时先征求我的确认。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySsiaWbDGEEg3sF3yeZEXH3aR8xAQA5bk7ZdNmxHibNh0jCtpXdUCc4KtFIzbGJVdgicib2Xs8TWKuHHzwyrfhmRaM1GNarTH7SLrw/640?wx_fmt=webp&from=appmsg)

安装完成后，测试一下。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS9jQtPnTuM7RGpiaPTqb25gfFoAjnA4QySbQ9KymKPK7QeHMJv3sJ9jLGH08FBF9mBvatco7WefdCauq3OaJ9Dx6Fj28iajPmkU/640?wx_fmt=webp&from=appmsg)

这里提示我们需要密钥才可以继续。根据AI的提示信息，点击链接去获取即可。

把密钥给到工具装填后，就可以继续操作了。

这里需要初始化一下浏览器。因为小红书（有反爬检测），需要创建一个反指纹识别的隐身浏览器

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySjibTWyWxAHiagzhQPE4iaEibGEq1P6UKd5kjygSlddqUuM2se5bxSxRVicdTfCR9xVqQU7IO8bF35ccbE2SjkFDAWM2uDtB2ZuNRg/640?wx_fmt=webp&from=appmsg)

同样根据提示信息中的链接去创建就行了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQlpKSzBv3RJH2V0eqN16SciamWJElamxQMoksp667V5cGRO3BOZwCfniaIPgd1gR6ia8vKWUGJbax5yx5BOPll0UGu83jRRNFjRU/640?wx_fmt=webp&from=appmsg)

创建完成了，现在就可以去获取相关信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyStVcfyARkl02AhWWBibObgTfbN43aq6cDhhiaNe7icR65pfZEIRsIO89jGiaBpf3v19ZhcnqseoQLIBfAoZm89kY64DLax5OFqku0/640?wx_fmt=webp&from=appmsg)

这个是BrowserAct工具与众不同的地方，因为检测到网站需要登录，那么BrowserAct会控制浏览器，等待用户登录再继续往下面执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQiaHh1iaebQPVjCbiaKrqNkeRpYeocczFAcF2C4WDLKOOhxYg6yHazxra74zHeviaZEicHrEYuNibpbxR1JV5zDm3j43H4jJ4hOwkiag/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRxibretJ1JiarhCFoIaMWGsNSpukkCibL1tBzlDiciagPdNtABYjHib6NqBKhUGBA173N9I5R9YM2CHia31yFxB3iaoeLsrSDtTdfL6e0/640?wx_fmt=webp&from=appmsg)

登录完成后，BrowserAct就开始操作浏览器收集信息了。可以截图的最上方看见，任务一直是处于等待状态，没有中断。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySZKOn0CIPSDcSRRbczQib0Ih7Oic8wb6SvCmlUkiaHWxsIuRSWJH2J44NgAxQ3pUy48nmhcMIGpAutkC7x8pacdHObic0yibzWiaDbE/640?wx_fmt=webp&from=appmsg)

后续就是收集的结果了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQ4u27JvG9BXuge5VZU89ia03xyeqJmRib6hQ83DScyV9LEZcpWvzrBgbUsFK7SKBux4VqSBltVYZ80SyM7msuiaKr5WIGlbWsU6c/640?wx_fmt=webp&from=appmsg)

可以看见收集到的数据还是挺多的，多个方面的信息收集。

### 获取排行榜信息

把提示信息给到workbuddy。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRudb0ibicH8B7EF3fB0wiaJdUsrVgIVlA9SicVB0lWX7MQ6kGedT8VVWlK1Q8CYWKS4ZsmpvsZlvibcsiblHV2hGqRqZicGWNk3SlDsE/640?wx_fmt=webp&from=appmsg)

然后BrowserAct成功打开网站，完成github的人机检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRLVYiboibzYgJ7dl713Rc31WdicIIsUdUOPqDJqU8PsBGvWMIvMgNQrflv3EJEO6icfsMoY7koJgNxMP7foxZ5FSic664Oiae8MxGFo/640?wx_fmt=webp&from=appmsg)

识别到了今天在github上面开源热度排行榜信息。

随便把收集到的信息整理为一个HTML。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQgKlVCCVtXVBYnpVFLL01IdN1HunLkYbLxZgzxhjW1u8Zy2CKCysVsxFxsjdOxN8bUENP1mTaEPMpEKN0JXdvNRIo7NAdBf8I/640?wx_fmt=webp&from=appmsg)

可以更直观的了解到热度排行信息。

除此之外。

BrowserAct 有个功能叫 Skill Forge，说白了就是把 Agent 已经学会的网页操作“存成模板”，方便下次调用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRGTEAOGuchr9dqm8fNQicq0EEAmCZL1H7ictfdySicMYpD11FLviaYjBkJb8sLMBcG3niaXzu4cmzuiaIYkORkVJiaBLwdyDhZ2w2bNo/640?wx_fmt=webp&from=appmsg)

比如每天固定时间导出后台数据，找菜单、设日期、点下载，这一套动作让 Agent 从头学一遍太费劲了。有了 Skill Forge，这些操作能一键复用。以后遇到同类型任务，Agent 连脑子都不用动，直接套模板执行，轻轻松松把“一次性实验”变成“永久性工具”。

比如对于文字创作者，需要再网上找类似于爆文的方向进行创作。 那么这个流程就可以用Skill Forge来完成。

在官网点击 `复制给Agent` 。把复制的信息直接丢给workbuddy。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTLomX2GU6VMp6GMTYUia3l43jdKAZMyQIvBoCibqTrVw3hJfODNvic3dcGeiaUApoFvEm8xtRKA5XMWS8hOJiaD4ehExA9vDerUqaY/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySGMk54qr96gPCqQia78NuC646XmV2NagzILfbtqLvuKuJsz8yKdRooqIthEoNXS8ZfUYerQFFZgmf9djU6ssOZFiaqruP3IZK7k/640?wx_fmt=webp&from=appmsg)

收集文章排行榜中的信息。 Skill Forge开始工作，收集需要自动化的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyRq3Hon3oPYephvPFQALWicibMVNicjqvYYSHhX7EEhFwZ9Q02eD6QKMpSYK0OMpHyASAh47Jxk2ibPAicSZiaMp51dJknzibTU5Qtd7c/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyT7PyTHAwrMjXn2icaF0Nmxhc0078b2IicxYquo6txQ42yHtaypXibyotSYbcI0gic6bauXQFluM7WMzYL2TpnYcJAH9ZsFIUF1pfw/640?wx_fmt=webp&from=appmsg)

生成的结果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS32YfXdNPicAmelX2Jl9ic4xIvUrsv353USAriaqaM928G4aWMTiaC95N3Oqn6QdhBge8Fdum8vFC8iawsjYNh5y2k9oW65qNuwOVw/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRcM4y9TJVwYSALwJOcU7ltHMNkhTVwOK343ZyAKJjYDfjJYfHuRFJhFmVWA4PV7fAlCKLmWic2iaPtFsmp3xYpt1uzsMVLhID5g/640?wx_fmt=webp&from=appmsg)

这样一个AI热点爆文收集的skill就完成了，不用每次都编写提示词来进行收集，也不用担心登录鉴权。

### 50+ 标准化浏览器操作指令

browser-act 模块内置了50多个浏览器指令，覆盖了大部分网页交互的需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyReniaMZTXpibtYe0ggn72Sd2HeJYIgMOjovDE8gMRY7k6zcsdXeO6dHVHpKTpuxwhAI7DicnTqtWgn7XkGVcx1mhGFFuHKicM3z9Y/640?wx_fmt=webp&from=appmsg)

感兴趣的朋友可以去了解一下。这个是官网地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyR9Zia8MnO1qY4ISX7JHIYFOB5O6A1EyZdjq5iaoT917vzjOg1osqFXZZ9OlSeictRcQUVhtxX2jNYXz8JoI11IdZas10YicUEtsBo/640?wx_fmt=webp&from=appmsg)

也可以直接去github获取skill。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQF9fXXm5terq2vmD7fwKPYKyEgiboMib1fZ7o8JL0oU9NzlhaichWCwIqFk2yaZXGYXJ9rODSyW1dahZpUjIl3e2WEpOYYEVwnMg/640?wx_fmt=webp&from=appmsg)

现在越来越明显的一点是，PC 端智能体的发展方向，已经不只是让 AI 帮我们聊天、写代码。

真正提高效率的地方，是让 AI 拥有更多专业能力。

以前我们使用软件，需要自己学习每一个功能；现在通过 Skill，可以把这些成熟的操作流程直接交给 Agent，让它像一个不断成长的数字助手一样工作。

浏览器自动化、UI设计、PPT生成、内容排版，这些都是日常工作中高频出现的场景。

而像 BrowserAct 这样的工具，解决的是 Agent 在真实互联网环境中的执行问题。让 AI 不只是停留在“给建议”，而是可以真正进入网页、处理数据、完成任务。

> browseract官网： https://www.browseract.ai/Ye
> 
> browseract在github上开源地址： https://www.browseract.com/?co-from=Ye&redirect=https://github.com/browser-act/skills/tree/main

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过