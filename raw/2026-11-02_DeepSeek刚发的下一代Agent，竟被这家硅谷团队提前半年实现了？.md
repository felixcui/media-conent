# DeepSeek刚发的下一代Agent，竟被这家硅谷团队提前半年实现了？

**作者**: ASI启示录

**来源**: https://mp.weixin.qq.com/s/Jk0G8CRyCRZxPcqUV-BqsQ

---

## 摘要

DeepSeek提出下一代Agent“Super-agent”理念，主张打破聊天窗口束缚，实现跨会话记忆与多任务并发，但硅谷华人团队AFK AI早在今年4月就已工程落地“单Session+多Worker”的超级架构，领先全球数月将这一顶层思维变为现实。

---

## 正文

ASI启示录 ASI启示录

在小说阅读器读本章

去阅读

### 新智元报道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWGxcbmnyYvqrSqhntcbPdelKBG0JLug4pEX8icjBSe5eib6PekswOSvrq8ybatQJRDr9Vib5WOKaUuibKfLb5qH3J4kEIYmC4NQJU/640?wx_fmt=png&from=appmsg)

最近，DeepSeek又来炸场了。

昨天，DeepSeek公布了下一代Agent Harness的理念—— **Super-agent** 。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYUXKH5paibgPJibT6pyWpCmbZvP6y7nY1VNzheiastTXeicJ2xToejVzuR88icOC9iaBTUAnc0uY4SQwEOOW89VyMAPHINlf5MpQAON8/640?from=appmsg)

这篇长文指明： **未来Agent的终极形态，将彻底打破「聊天窗口」的束缚，走向跨会话记忆、多任务并发的「真·Jarvis」时代。**

文章一出，业界沸腾。

许多开发者直呼：「这就是我们一直在苦苦寻找的下一代AI应用形态！」

然而，当我们在为DeepSeek的顶层架构思维拍案叫绝时，居然发现了另一个事实——

**早在今年4月，一个名为AFK AI（开源** **组织** **AFK-surf，产品名Comma）的** **硅谷华人** **团队，就已经在工程上完美实现了DeepSeek今天所描绘的几乎所有核心架构，并在时间上领先了全球几个月！**

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYWPBI7LJuOG5fXxm2RtuosViakZeoRrOldNZHKO6FGSAR9YdhMa535vZB7mXNoCZbBPLGUReHnCg74Wlib8jAW3Y5dgU4ncaibRhk/640?from=appmsg)

所以，当行业巨头还在发布「理念」时，这家神秘的团队是如何把「单 Session + 多 Worker」的超级架构变成现实的？

他们又将如何把超级智能带给每个人？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Rvq8Ow69CYUrKwUR1N5sXRbEejibu40P0QQoKC8mkFlxsKFdgsVqqHn8EZFewrGcib1wWGGSicxT7d1rMiaiaxroNtZ4FtsRQiaTjfYplu7BFbBkc/640?wx_fmt=gif&from=appmsg)

从此，再也没有多余的应用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**英雄所见略同：向「反人类」的单次Session开战！**

很多人都发现，用AI的时候经常崩溃：比如聊着代码，忽然想让它回一封邮件。

为了防止上下文污染，你必须手动建个新对话；等回完邮件切回来，你又要重新梳理上下文。

据统计，人类的大脑最多只能同时跟进3到5个活跃的Session。 **传统的AI产品，其能力的上限不是模型的智商，而是人类的注意力。**

在最新的文章中，DeepSeek一针见血地指出： **现有的Agent设计无法支撑多任务和团队协作，必须打破Agent与单次手动会话的绑定！**

系统应该是一个能够跨会话保持上下文、同时推进多项复杂任务且互不干扰的连续实体（Super-agent）。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYWpQkFCnicDaka3DGc7PJezT1jpIht4ajDGrDArc2f1yDfxyXzk4BBeZX0tyib0Mkh7Ynzw2O8pWBI4lzvy3CiaibmzeQBia8xrvQPk/640?from=appmsg)

**令人震惊的是，这与AFK团队在今年4月13日内部定下的核心方向如出一辙。**

AFK团队当时抛出了一个振聋发聩的理念： **「一个团队，一个对话」（Single session + Multi-worker）。**

他们认为，用户逐渐用IM（即时通讯）接入AI后，必然会变成主要使用「单Session」。不管是你、你的同事，还是在飞书、Slack、微信里的任何一句话，都应该汇聚到一个拥有长期记忆的「主脑」那里。

DeepSeek把这个痛点总结为理论，而AFK早已经在几个月前把代码提交到了GitHub，并做成了极其成熟的产品 Comma。

比如DeepSeek讲到的自动PR、自动观测跨端执行任务，AFK已经跑了大半年了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rvq8Ow69CYWXRKfmP3ueA93jjhy7Jj4JJ55DI1BMiaSrfw9JP4g4Pf9iaCeXajKtquxJsBGaUHfdCT44WIrh757BywjichsJnEh8VbEPCstyQ0/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**核心架构的「神同步」：双层架构与环境解耦**

如果你把DeepSeek的长文和AFK-surf的技术文档放在一起对比，你会产生一种「互相抄作业」的错觉。

但这其实是因为， **相似的设计约束，必然导出相似的架构选择** **。** 只有真正触碰到了当前Agent落地的天花板，才会不约而同地进化出这样的系统。

我们来看看他们令人惊叹的技术相似之处：

**1\. 双层架构：Router（主脑） + Worker（四肢）**

为了解决「既要记住所有事，又要同时干很多事」的矛盾，两者都抛弃了「一个大模型干到底」的思路，采用了经典的双层架构。

**DeepSeek设计了常驻的 Router 层和上下文隔离的 Worker 层。**

其中，Router负责统揽全局、承接人类交互与分派任务，但不亲自干脏活累活；具体的任务发给独立的Worker，Worker在隔离的上下文中疯狂干活，干完再向Router汇报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVUO2cxicxCIXjRv8LaLKGN9YicVJiamibqxy2G8AicGOXQEK5iaDVbVWCp2TrFhCusrNOmnnBy4vWrjjEOHkCm9Q41F0QlnPZcf9S8g/640?from=appmsg)

**而AFK Comma 的解法完全一致！AFK将其定义为 Lead Agent (Router) + Subagents (Workers)。**

用户或团队永远只跟那个长期在线的Router说话。Router就像一个人类主管，接到任务后，给对应的Worker开一个新Session。

Worker有自己的环境、提示词和工具，多个Worker并行运行互不干扰，繁杂的执行细节全留在Worker那边，只有结果才会汇总给Router。

**Router有一个长期存在的主上下文Single session（单 session）** ，代表「一个人」或「一个团队」，持续好几个月。

它记得之前发生过什么，也知道现在有哪些事在进行。Worker 是它派出去干活的手，而它自己就是那个一直在场、负责到底的「主人」。这就解决了「人和 AI 之间如何长期相处」。

**这种架构带来了革命性的产品体验——**

你不用再做「群主」去拉群，不用每次给AI设定人设。在Comma里，你只要说话就行了，剩下的路由和分发，Router会全权搞定。

**2\. 「灵魂出窍」：计算与执行环境的分离（BYOM）**

普通的AI只能在云端的虚拟沙箱里执行任务，一旦涉及到公司内网代码、你本地的私人文件，AI就成了瞎子。

**DeepSeek 提出，计算、状态与环境必须分离。**

Agent的「脑」在云端，但「手」可以伸向用户的本地机器。通过在端侧部署一个不保存状态的轻量Daemon，云端Agent可以按需读取本地环境，这被称为BYOM（Bring Your Own Machine）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYV6zOib7Wia1pMq9x1LPeFG3kVB9ldsecYgmsLFWDofwG2koPR3J4ZTXSNgicMc2DhmuZ0QUe0Fb6elibWHkaQ9rzyPEus0TeIagYk/640?from=appmsg)

**而AFK Comma 的落地，再次领先一步——Comma已经把这个理念做成了强大的企业级功能！**

通过在企业 IM 中 @Comma bot，Agent 可以请求员工终端执行任务。员工个人的 Personal agent 可以接管个人的电脑作为执行任务的节点。同时，企业中有人 @Comma bot 时，会触发 Agent 之间的调度与通信机制，继承人的权限与角色，在不牺牲信息安全的情况下，让 AI 替人协作并上班。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rvq8Ow69CYW2ibnjtGL0N4nZZYrhhjZMfyLHLYia5ppuMglk0wkib5xb15ibicjlAHqb01qZ4aDQia08whFLZicms2oGnLicSrQNKTwadkhcUAYyacI/640?wx_fmt=jpeg)

同时，这也意味着，Agent 组成的网络可以洞察企业细微的业务细节信息，并实现持续学习。

![](https://mmbiz.qpic.cn/mmbiz_gif/Rvq8Ow69CYU1UQnuyvVNMxC9Pz5Cm29WDkGdCFjlraXaav6nXpO8dtLJlSuEk59UquaNwEmdxkicr2Vm0yupe8krZSct43diaYSuqCjfN1UsY/640?wx_fmt=gif&from=appmsg)

同时，系统内置了信息流控制的安全防护机制(ifc)，对敏感数据的访问与传输进行管控，保障信息安全。

这就相当于，DeepSeek刚刚论证了「脑手分离」的可行性，而AFK Comma已经把这套「云脑+本地手」的系统卖给企业用了！

![](https://mmbiz.qpic.cn/mmbiz_gif/Rvq8Ow69CYWykxtV5zdqBTtB1vpKD1lN8SPr48DZBzRS62j1E3l3SNJcGklPa3OyhibxDuJp8FpAtibHLnSWibqskVRGUWaIHicrYc8WE0vFNYE/640?wx_fmt=gif&from=appmsg)

**3\. 事件驱动与多端并发：真正的「全双工」**

人类的工作不是「一问一答」的，而是异步的。

为此，DeepSeek 提出，引入事件驱动（Event-driven）和全双工交互（异步ReAct Loop）。模型在后台跑任务，前台依然可以秒回你的新消息。

**而AFK Comma的客户端，直接打通了Telegram、Signal、微信、iMessage、飞书、Slack！**

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXKdrel9CD9Nexzcs1mjibxzXZhWt83VfpLhVIjVn139S2CgF37FwvjLPqX3HraBBRGyZDDCqVmunHiclgRnb2hRPdHiaDPiaBpC0Y/640?from=appmsg)

zanweiguo 直言：从此，啥App都不用开了。

它是一个真正的「工作站」。你在飞书里交代的事情，Router在后台派Worker去干；同事在Slack里追问进度，Router已经能同步回答。

甚至，从这些各大平台产生的Task，全都在Comma客户端统一管理；反过来，Comma也可以去第三方平台创建和管理Task。

这，就是真正的Jarvis。它无处不在，多端记忆绝对一致，不被任何一个App绑定，却能掌控所有的信息流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**多个Demo展示**

以下，就是Comma的更多惊艳demo。

它可以帮你管理Slack。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rvq8Ow69CYX5NSRd3liaSibMxDrVrxqqSvGib249DwLqZv0a4vicWOZhZFKImqiatnqdIyohKBHibTBDVrHpPZPHD7LYib8XHdroZw2UTyFXicgdCHI/640?from=appmsg)

它还自己修自己:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXzWLSZJ2nWia1qgOiaHpgQ9Nq5yfYLXvEE2BtT5ZJh24ic928L4wCE7OPjb1jHK5G8GW25Vo0o5DCicXQf66yIVPHAQbvOUZC4OyI/640?wx_fmt=png&from=appmsg)

古风3D麻将，它也能轻松搞定。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXyO9icoqySH3d7soQEkE2wvv0MeU7qgbL5MJ591wTcN4SFkTYWsRjBcH5mN6e8nKvVCM65893DficSUf9Vq3MWN0ufeIjIiaczZY/640?from=appmsg)

甚至还能一起玩儿3D麻将，绝了！

![](https://mmbiz.qpic.cn/mmbiz_gif/Rvq8Ow69CYWGgMISf9ZnajjXtcyC5WGqmB91LPmlzKice9KfXmdicgVZplGoB4bpmw1xR9hNJNce4jgp7M3iad6wXBVV365X9m5XMyyExMqnoA/640?wx_fmt=gif&from=appmsg)

它可以帮你盯机票。

![](https://mmbiz.qpic.cn/mmbiz_gif/Rvq8Ow69CYUGKSbG3yBKgNqo2AaKynObyBK2qRJQcOQKHOfiaeA9qLCynloUsfTBa3WiaxDOOR70RViaTALPwo0mTvhmOInH0xhx3Z4qk7wibBA/640?wx_fmt=gif&from=appmsg)

路上随手拍一张iPhone DUO的广告牌，让Comma做出个复古滤镜app，一键梦回2012。

还能管理其他平台，比如Linear，可以帮你详细安排日程：

![](https://mmbiz.qpic.cn/mmbiz_gif/Rvq8Ow69CYVzEapLgzPJ5JsgPXXJTfFrWSmxTLWD1yWvwOSDnHI78pwYDulaCtNjGApAwZibEE15xqtSRVMlAHKcMzPkd2thXyIvBczeiaYTI/640?wx_fmt=gif&from=appmsg)

让它查局域网、看邮件、总结最近的新闻，通通搞定：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Rvq8Ow69CYVpvtic6d6YtlNFwY8ZEfZx68R61frq5dSuRKoEG0uicwEf8mPLQLMxAvHMgnhBzvpVP3q5kxeiaSvG0IdRyHziaPSQiascYBwDiciaCI/640?wx_fmt=gif&from=appmsg)

甚至可以让它修视频、拍视频。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXWqTARZvIWsLvWNDWKCicx85cny02hyvlJYqJgr2azPjGeiaaNpqfYJmZjkoTGr8mucED6iaqDnk9KOzSpsJibyWgdLzWl7LM5uibI/640?from=appmsg)

**走在时代前面—— 一份硬核的时间线证明**

当 DeepSeek 刚刚把 Super-agent 作为下一代方向抛出时，AFK AI 团队已经在工程实践的泥坑里摸爬滚打了大半年。

翻开 AFK AI 团队公开的工程记录和代码 Commit 历史，你会看到一条清晰的探索之路。

早在今年上半年，他们就已经把「单 Session + 多 Worker」架构推向了生产环境。

还在2025年9月时，硅谷出现了个人助理产品Poke，证明了「一个人，一条连续对话」的模式是成立的。但它仅仅局限于个人。

今年4月13日，团队内部拍板，敲定了「日常聊天的主 Agent + 干活的 Agent」的底层设计。

今年4月28日，Comma 的前身 Bridge 公开发布，博文明确写道：「Bridge is a lead agent... sub-agents are integrated automatically.」

**今年5月20日，是历史性的一刻。他们在** 代码层面正式确立了「团队级单 Session」。每个团队拥有了一个稳定的 Router Session。

**今年6月3日，** 固定的Bridge对话和 delegate\_task 正式上线。用户只跟Router说话，Router全自动把任务派给Worker。

**而现在，在今年10月底，** DeepSeek 发布 Super-agent 架构长文，全行业开始瞩目这一方向。

复盘整个时间线，你会发现AFK AI团队对技术趋势的嗅觉极其敏锐。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYWkwvM23ib3DxOTvSGgNHOQP4MF4h6q7Eias2XibsSltMTVibpypAWhXEwANIOP0XhdOySuviaMvsdED2ATUKhWial7ibDah4y5ed9R7I/640?from=appmsg)

注：插个有趣的八卦，AFK AI 最初的产品形态叫 cue，结果没想到Manus发布了类似名字的东西，因此，团队才改名叫 Comma。

而作为对比，Anthropic直到 今年 6 月 23 日，才在 Slack 推出类似理念的 Claude Tag。

**在这个路线上，Comma 的公开发布比 Claude Tag 早了将近 2 个月，而底层架构的落地则早了整整 5 周！**

**比起DeepSeek 的理论公开，他们更是早了半年就完成了工程落地。**

不仅如此，AFK-surf 坚持了开源、安全、支持自部署、支持BYOK。你可以自由地接入你自己的 Codex 或是 Claude，而 Comma Agent 能监督你的 Codex 和 Claude 干活。

这种开放性和架构的前瞻性，让 Comma 已经是下一代AI操作系统。

而且，DeepSeek在文章提到——「要突破限制，需要打破 Agent 与单次手动会话的绑定……并在长期运行中遇到异常时自动恢复。」

这些坑，Comma早就踩过，还给出硬核的解法，比如按任务隔离的 Worker，绝不污染主脑；系统级的信息流隔离；原子级的 Session 切换与 TLA+ 建模登顶等等。

这些，是真正把计算机系统的经典设计思想融入到了 Agent 架构中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**从AFK和DeepSeek的共识，看未来Agent的终极趋势**

读懂了AFK Comma的底层逻辑，再结合DeepSeek的长文，我们其实已经看到了未来3到5年AI Agent的发展终局。

**趋势一：单点Session的消亡，「一团队一主脑」成为标配**

未来，你的公司、你的生活，都将只会拥有「一个」超级助理（Router）。所有成员、所有App（微信、Slack、飞书）的信息全盘汇入这个主脑。

**趋势二：AI将从「被动响应」模型变为「主动推进」模型**

基于双层架构和后台静默Worker的设计，未来的AI会持续观察公共群聊、GitHub、邮件，成为一个主动推进者。

**趋势三：云端大脑 ，万物皆可Agent**

由于环境和计算分离，未来的执行节点会下沉到每一个员工的电脑、每一台手机甚至每一台智能家居上。AI的脑子在云端，用「手」来操控本地资源。

昨天，DeepSeek用一篇长文告诉我们，对于未来的超级智能体，底层系统的革命才是真正的关键。

令人兴奋的是，在这个关键的转折点，这次在硅谷的华人团队跑在了最前面。

编辑：大卫 Aeneas

**秒追ASI**

**⭐** **点赞、转发、在看一键三连** **⭐**

**点亮星标，锁定新智元极速推送！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UicQ7HgWiaUb1y6B5OM79TFzpkceWtUkI6LEwv0uYicSoM5Q3I3kDNJhxWdL3tQvbOpU3Ty7icBqnDDNd4CCu4ibiaHw/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVMuHfFGD1mFMfc5284R22LkqUkpItsc62vpgD4gUNm74S0DFlRWMg0ANo2ia5h3KXHoDYubJUcrJYBHXqYEFlibCHQxVDddZe3s/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过