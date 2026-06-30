# 开源Bugu，解决胡彦斌的vibe coding困境

**作者**: AI沃茨

**来源**: https://mp.weixin.qq.com/s/hzZ87HG_qiZRYUs8ZIzm1Q

---

## 摘要

为解决Vibe coding时合盖电脑无法直观感知AI Agent任务状态的焦虑，作者开源了macOS菜单栏应用Bugu（布谷）。该应用具备防止盒盖休眠和监听Agent对话功能，能通过特色音效定时提示任务的接收、运行、完成、中断及需授权五种状态，并展示对话运行时间和摘要以供跳转。此应用是作者结合Codex与六倍速的Kimi Code共同开发完成的实用工具。

---

## 正文

AI沃茨 AI沃茨

在小说阅读器读本章

去阅读

## 有一件事我最近越来越受不了，

就是长时间Vibe coding的时候电脑是盒盖还是不合盖，

不合盖吧，纯哑铃来的，一只手捏着3斤的电脑，过于吸引周围人的视角了，合盖吧也有招，用Amphetamine能精确控制Codex或者Claude在运行的时候合盖不休眠，我把这个方法安利给了周围很多人，但他们还是担心合盖之后总有点忐忑之感，不知道程序是不是还在跑。

为了消除这种未知感带来的焦虑，我vibe coding出了一个macOS菜单栏应用，

Bugu，中文名叫布谷。

如果说这个App有什么功能是我最重视的，那一定是音效。尤其是我习惯性给Codex和Claude用Goal布置那种一跑跑几个小时甚至跑一天的任务，中间我又要带着电脑出门几个小时的时候，我就很希望不打开电脑也能直接确认任务的状态。

所以这就是bugu的主界面了，长度的原因分开截图了，实际上就是在一个界面。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fw0sG1Oflr5RzfgkLxbqel9TTgxwqPGZYORB3ib0klvPBaZ5zBcuv668XKPlzx5nnFavIOVyo9szmpDRnnxEeFfCZiaYicY8PenYQ/640?wx_fmt=png&from=appmsg)

🔗 github. com/LearnPrompt/bugu

用法很简单，开启「Keep Mac awake」，就是防止agent工作时电脑休眠。开启「Watch coding agents」，就是开始监听Agent们的对话，右边图就是最近对话，还戴上了运行时间和输入的提示语，当然是可以点击跳转到具体对话框的。接着就是选一个心跳间隔，我的建议是5分钟，选个音效包（System是苹果自带音，Bugu Pack是游戏音），最后合上Mac。去做别的事。

就这么简单，来看看我的超好看logo👇

Bugu会像布谷鸟一样，只要任务还在正常运行，它就可以每隔五分钟十分钟叫一声，那我们在合上Mac的时候也能通过声音知道Agent的五个状态。

Accept是接收任务，也就是说，如果我用手机发一个新的任务到Mac，我可以通过音效来确认有没有收到。Running就是固定时间间隔发出的任务正常运行提示声。剩下三个就是任务成功（Done），任务被意外中断（Interrupted）以及任务需要授权（Permission）了。

大家可以猜一猜，需要手动授权的时候用的音效是哪一个？猜对了的有奖。

当然，Bugu还有两个我搓了挺久的功能，

保持整台Mac处于唤醒状态，盒盖也不会休眠。

我没有做得像Amphetamine 那么复杂，是因为我觉得与其去设置触发器，低于什么电量自动关闭会话等一大堆，我更想把它做成一个简单的开关，点开就是唤醒，再点一下就是关闭。

还有就是在Bugu里会显示每个对话是在多少时间之前运行的，以及输入的简要内容。通过这个功能，我们可以看到正在运行的对话（运行中的对话会变成绿色），还可以点击这个对话，直接跳到正在跑的任务窗口。

![](https://mmbiz.qpic.cn/mmbiz_gif/VNz1x8bH8FycGpicEChAEniaibucaaAnmZicODIVfh7zATicJv3qFkHaUMG8Ujpjuhlxg6iaCicVnAdVm5GOiafdXjgdyLUEGAjahOHB8QjZRPMTxm4/640?wx_fmt=gif&from=appmsg)

本来想这样1个App，按照我过去的经验，用Codex开Goal，一晚上就能搓个七七八八。但最近OpenAI像是在24小时偷我的额度一样。我一个Pro，28号就把下个月6号之前的额度全部用完了，比便宜十倍的Claude Pro还不耐用。

积分损耗太快，我只能把它从1.5倍速、2.5倍积分的高速度模式切回慢速，再给Codex找了一个六倍速的coding搭子，Kimi Code来从零搭建原型。

前段时间，Kimi刚发了Kimi K2.7 Code Highspeed，性能不变的基础上速度提升6倍。中等长度编码任务180 token/s，短上下文任务260 token/s。这次我用多Agent做产品调研时候的速度，是完全没有加速的。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/VNz1x8bH8FzMSHVcQeb7rPceV5wawbvQGgmS9904198PjMhQ0muFcWW5ibKpes1picdzTTlOlt3h2CrXbXePQtAU0ZKxRX2HAaIfGs5ib9MEHI/640?wx_fmt=gif&from=appmsg)

关键是，Kimi Code跟Claude Code，Codex一样有goal模式和多agent能力，还能把Claude Code和Codex的skill和MCP都导入进来，不用我从零开始教它怎么跟我协作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwLUv2HcRYXSowBianJJ0p9CUzfzMQdA0SOgkW45CYH93UP4h710icpf1nrwsZh1jm8VEa4TRObh7g2VGTAYrYPKprFwib1m28PvI/640?wx_fmt=png&from=appmsg)

我给Kimi Code的第一个任务就是先接手Codex开发了一半的Bugu，再做了一轮信息收集，浏览器自动化搜索Mac防睡眠工具、Apple系统音、App Store上架要求，把搜索结果拿回本地整理成建议，再决定下一步怎么改。

这也是我最近非常喜欢用的信息搜索技巧，

我会在整个提示语的最后加一句，用浏览器自动化去我的 X上用Gork补充搜索。大家都知道X上帖子的时效性非常强，但API又特别贵，之前我都是手动去做，现在都成了我测Agent的标准case了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fw7CJJzszNgiaFHhH3OBs5mOzr4O6WmNXcaewrlh4ttMsicZ60H7xZI4JKNGwxwiahSDon4xkol6HqPyQ49JhqBqmm5PEzRmug0JY/640?wx_fmt=png&from=appmsg)

简单来说，这次信息搜索我得到的结论就是，我们最好在GitHub上发布Bugu。

因为如果要把它上传到App Store的话对话跳转的功能会要被删掉了，Bugu要知道你Mac上有没有agent在跑，靠的是扫描正在运行的进程。但App Store需要遵守一个叫沙箱的机制，用人话说就是商店里的app不应该知道你电脑上还跑着什么别的东西。

OK，边界有了，下面就是来个头脑风暴来补充App的细节了。

我常用的产品调研提示语现在已经是这这样子的，

💡

用superpower的头脑风暴，office hour，鲁班skill和last 30 day来看看这个app目前有啥值得优化的点，我觉得我们的优势可能就在于多音效，以及可以自定义。因为在合盖场景下，声音就是我们唯一的界面。

这个四个skill其实是有能力重叠的，不过我真的习惯饱和式做信息搜索了。

真的，每一页的信息量都超级多，所以我甚至都有点难选择，最后还是选择放了几张长图给大家看

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/VNz1x8bH8FxY6icBlL9wecLb8UIAziaPm9iaueEnL5L2DvCbb5vibXQQAIwGNAvdOnUMs1amBH8p4ibClxB1LYAM3d7hSQYSE9IHAAFOqo6fb3vQ/640?wx_fmt=jpeg&from=appmsg)

这里额外说一下goal这个功能我是怎么用的，

我们不需要在开头的第一句就给它一个你可能打磨了十几分钟的提示语，预计让它会开发一两天的指令，这大概率跑十几分钟就结束了，还不如直接对话。

我用goal就是在长期对话过程中，明确了开发方向，积累了足够上下文之后，从对话里输出的一个长时间任务。

比方说，在做UI设计的时候，我就把自己用下来觉得印象很深刻的几个UI界面发给Kimi Code，让它去设计Bugu的整体页面，这里有些界面挺复杂的，但它能根据我们前面的调研结果判断，我想要Bugu整体来说是比较克制的。毕竟在开关那里我们就已经做了取舍，不想要复杂的触发器，只想要一个按钮开关。

所以我们的对话挑战和音效的切换，也是持续「能在一个界面，就都在一个界面」的想法。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FzKicFBicWvrgVOHBNwMEJhuj364emUKCp02F6ibc9jPab0Taic7icdlwMjcpteV4sUXCibmLBj7NaXqNZP1CWsX4jyPV8NxtRJDu8tk/640?wx_fmt=png&from=appmsg)

上面这些都不是开发时间最久的。

真正占了Kimi Code开发大头的部分，是怎么去识别Agent的进程，让它能够精准地跳到对话的界面。

这个功能做起来一堆坑。简单来说，Mac上同时开着好几个终端或者codex app，claude app，每个界面里跑着不同的任务。Bugu要做的事情是，知道在哪个窗口里，然后切过去。

我本来想用macOS的脚本去查「终端现在开着吗」，结果macOS的逻辑是，你一问它就直接给你拉了个新窗口出来。

这种情况也适合用Goal，

让Kimi Code去读macOS的文档，去试不同终端的行为差异，去一个一个排查哪种方案在哪种情况下能用，加上有六倍速，这种试一个方案不行、换一个再试的循环跑得飞快。所以最终的方案是Bugu会在对应的Agent里加一个钩子hook，这样对话激活的时候就能第一时间收到输入，运行时间和状态了。

最后想说说为什么会有做Bugu这个念头。

之前用的是Amphetamine，我设了非常多的触发器，直到一次我把Claude Code打开后没关，也没调音量，结果有人打我电话的时候，铃声自动接到了电脑扬声器上。

我当时正在电梯里，

那是我今年最漫长的10秒钟，也是打开电脑最快的10秒。

在那之后我就想，我需要一个专门为Agent设计的提醒工具。

它一定不是一个通用的防休眠软件，也不是系统通知，这些都有了，

要就要做一个能让我不打开盖子也能知道Agent状态的App，声音可以单独调，行为可预期，不会在电梯里社死。

所以就有了Bugu。

这次用Kimi Code接手Codex开发的一半的项目也是让我想清楚了一件事，

鸡蛋还真不能放在一个篮子里，

Fable 5现在都需要我们有美国护照才能用了，别提还有我们看得见摸不着的GPT-5.6了，

既然有些过程可以被国产模型和国产Agent框架代替，那为什么不呢？

Kimi Code可能不是我的主力开发agent。

但在目前Claude Code只能省着点用，甚至不敢把额度打满，Codex额度究极不耐用的情况下，

它是一个非常好的补充位，

能导入各种skill，能跑goal，还有六倍速。

这次Bugu的开发过程已经证明了，

拿它来推进一个真实的小项目，完全够用。

之前开源了那么多skill，

我发现其实还是可以有一些小应用，

来提升日常幸福度的，

不用大而全，

像Bugu一样小而美就挺好。

@ 作者 / 卡尔

---

最后，感谢你看到这里👏

如果喜欢这篇文章，不妨顺手给我们

*点赞｜在看｜转发｜评论 📣*

如果想要第一时间收到推送，不妨给我个星标🌟

如果你有更有趣的玩法，欢迎在评论区聊聊🤝

更多的内容正在不断填坑中……

![](https://mmbiz.qpic.cn/mmbiz_jpg/YEhakvKZjXmCDLEEW1wClZOVGFURjmibJmciaYLNhp0N55Y6mPiaCj01eV8yzACqDvWDhicbPm07Wu7bboATuKgAbA/640?wx_fmt=jpeg)

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过