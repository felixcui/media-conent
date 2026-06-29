# OpenAI悄悄放大招：Codex Security Plugin，一键扫爆你代码的安全隐患

**作者**: 刘小排

**来源**: https://mp.weixin.qq.com/s/Hq22zDap9adNOkPU8TK5sA

---

## 摘要

面对AI发现大量系统漏洞带来的安全焦虑，OpenAI低调发布了Codex Security Plugin。该插件能深度扫描代码库中的安全隐患并给出解决方案。用户只需输入简单指令即可启用，其后台会自动调度大量子智能体进行极其细致的排查，虽耗时较长且消耗大量Token，但全程自动化且未经授权绝不修改任何代码。作者认为该工具真正解决了在海量代码中精准定位漏洞的难题，极具实用价值。

---

## 正文

刘小排 刘小排

在小说阅读器读本章

去阅读

哈喽，大家好，我是刘小排。

前两周，Fable 5/Mythos 5发布前夕，Anthropic说

> Mythos Preview has already found thousands of high-severity vulnerabilities in every major operating system and browser

Fable 5/Mythos 5能在 OS / browser / open-source stack 中发现大量漏洞。在“玻璃之翼”内测项目中，Mozilla 用它发现 **Firefox 271 个漏洞。** AI已经能在多个系统中持续发现 previously unknown vulnerabilities。

这让一些参与内测的研究员吓得不轻，纷纷对Anthropic表示希望延迟发布这个模型。

Fable 5，某种意义上，就是这个能力的“对外收敛版本”。

我也被吓得不轻， **我在想，连Firefox这种成熟产品都有200多个漏洞，那我的小破产品岂不是漏洞更多？那可怎么办？**

**救星来了！**

过去一周大家都在关注Fable 5、ChatGPT-5.6、GLM 5.2等热门话题，不过，其实前天有一个非常有用的东西低调发布 —— OpenAI Codex Security plugin。 它可以帮助你以前所未有的能力，扫描你代码里的漏洞，并且给出解决方案。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6aOmBZKAbPPF9wEzw27PcqwJGAX9dxGXfQvlu2WVpmuYbe56Gy1WMYSrYLWNyAKw64TzxU8WyI66HPUgAvU2TVHVNS0MoW5C7XYbMwhzGY/640?wx_fmt=jpeg)

运行时间根据你的代码库大小不同。对于较大的项目库，它可以轻轻松松卷自己两小时，找到超乎你认知范围内的大量漏洞。

使用方法很简单，完全无脑： 只需要在你的Codex（最好是桌面版客户端）里说一句

> Run a Codex Security scan on this repository.

如果Codex检测到你尚未安装Security plugin，会提示你安装。

还有个好看的界面，让你选择扫描范围和一些参数。

注意：最新版本Codex 才有这个界面；如果不是最新版，扫描漏洞功能本身是完全可用的，只是没有这个专门的界面，用户体验差一些。

之后，它会以迅雷不及掩耳盗铃之势，不断启动和关闭大量的Sub Agent子智能体，相互协作来帮你排查问题。

即便有这么多Sub Agent，排查的流程会非常非常非常长，它会查得非常非常非常仔细（请看下面截图的进度条），消耗的Token也会非常非常非常多。 而我下面的截图，还仅仅是在准备阶段……

好在，它全程自动化，并不需要我们参与。我们只需要等待即可，该干啥干啥去。

在获得你的授权以前，它只会扫描漏洞，给出方案，不会修改你任何一行代码，请放心使用。

真的非常厉害，言之有物又证据确凿。

感谢有这么好的AI工具！

～～

之前我夸赞Fable 5的时候，有同学问：这有啥了不起的？其他模型做不到吗？ [GPT-5.5和Opus 4.8都搞不定的Bug，被Fable 5一晚上解决](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247502331&idx=1&sn=eac0d83d66e75f7e1bc19f99964033e7&scene=21#wechat_redirect)

我想，所谓 **「大海捞针」其实是两个动作：**

1. 准确知道针在哪里
2. 把针捡起来

这两个动作的难度是不可同日而语的。而当我们夸赞某个模型的智能水平的时候，我们在乎的是第一个。

这次Codex Security Plugin同理： 真正难的是，从茫茫大海一样的代码库里，准确找到针在哪里。至于具体怎么改，随便找个2026年的大模型，都能改了。

你试试看，用它查一查你代码库的漏洞情况？

欢迎评论区晒出截图和讨论互动。谢谢

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过