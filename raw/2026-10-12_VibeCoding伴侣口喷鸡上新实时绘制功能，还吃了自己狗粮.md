# Vibe Coding 伴侣口喷鸡上新实时绘制功能，还吃了自己狗粮

**作者**: 尹John

**来源**: https://mp.weixin.qq.com/s/BZWcA_7VS_HdN3DrJqkGrQ

---

## 摘要

开源工具口喷鸡新增实时绘制功能，录制时按住⌃拖动鼠标即可在屏幕上画圈划线，笔迹同时录入视频并生成坐标数据供AI精准定位，3秒后自动消失。作者将电脑交给Claude Code自主完成案例，它浏览多个同类产品官网，圈出亮点并记录想法，为口喷鸡官网寻找参考。

---

## 正文

尹John 尹John

在小说阅读器读本章

去阅读

上次把口喷鸡 blurt 开源之后，陆续收到了一些 star、PR 和 issue，我都一一处理了一下。

也许你还不知道口喷鸡。它是我开源的一个小工具，你只需要对着屏幕边用边喷，它会把录屏和你说的话交给 Claude Code 或 Codex，整理成一条条有图有文的事项清单，从而花几分钟便能完成原来需要数小时的工作。

然后昨天，有位读者在文章下面留言：

![](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnymiaKtW8Zv877EdsE6DznrWUJTY7Swr7ibZrI6lJzQ6TvCaTGsKjzibjRKdnCHfvGibLAExOrvjoQvBcAJ52iaMZYyibz6rnrPv2xQ/640?wx_fmt=png&from=appmsg)

他提了两件事，一是 **用途不只是改 bug** ，二是 **最好能支持实时绘制** 。

用途这个我其实在上一篇里有写，只是放在了靠后的位置。

实时绘制我之前也有想，但觉得鼠标停在哪儿其实是有记录且能识别出来的，不画也能做好。

不过我现在觉得，确实可以加一下。因为画上一笔之后，用的人会知道自己已经明确给出了信号，这本身也是一种有用的反馈，对后面的处理来说，也会更方便、更精准。

于是我回复说，这个我来加。

## 按住 ⌃ 就能画

01

我把这条留言原样扔给了 Claude Code，让它看看该怎么支持，再找个有意思的案例出来实际跑一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFkiaoMEicib1QeibxJe3X2EyUM77cT70ib428AMIUvEFlaH9ic1G5bUaXGrogt0FGmpqABHKZLzdjoYe2D8iajAMKzaYsf31PKHibQiafMc/640?wx_fmt=png&from=appmsg)

忘了多久之后，功能做出来了。录制的时候 **按住 `⌃` 拖动鼠标** ，就可以直接在屏幕上画圈、划线。

![按住 ⌃ 画圈](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFn9ibcMQAUqPy8iaeJiaaQxn9SKw33N6FFYelfcIicdCQFcQfmjTGaqicBQuRLtYlD5xA81ia9tvfuhmIe9zjkPnZwnibbgibYtI3NI6fY/640?from=appmsg)

按住 ⌃ 画圈

嘴上说「这里」的时候，手上圈一下，AI 便能非常明确的知道你说的「这里」到底是哪里了。

悬浮条上也多了一个画笔按钮，点一下或者按 `⌥⇧D` 可以常开：

![悬浮条上的画笔按钮](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFllAgpUMWmqCMv36UP1ic42ZA3ib5t8weKQbrXicGPcNFpkuOhicSWGIh2cibm4qwhvucW7sC8My0n0Qxb0S1HiaZXn4l6f0KHHJfIibE/640?from=appmsg)

悬浮条上的画笔按钮

画下的笔迹会同时去往两个地方。一份直接录进视频里，所以抽出来的截图自带你画的圈；另一份则是每一笔的坐标和起止时间，存成数据给 agent 读，它可以照着这个位置放大去看。

笔迹过 3 秒会自己消失，不用你去擦。

这里它自己还踩了个小坑，最早是每一笔画完 3 秒后各自消失，结果连着圈两个地方时，第二个圈画完，第一个已经没了，两个圈凑不进同一张截图……后来改成了最后一笔画完 3 秒后，再一起消失。

## 把电脑交给它

02

功能有了，而我正好要去吃饭了，便直接把电脑扔给了它，让它自己来把案例完成就好。

等我吃完饭回来的时候，它已经把事儿全部干完了。

它给自己挑的案例是： **给口喷鸡自己的官网找一些好的参考** 。

理由是项目的 TODO 里一直躺着一条「Project homepage」没做，场景也正好是留言里说的那一种。

于是它像一个真要做官网的人那样，打开浏览器，一顿逛了各种同类产品的网站：Jam、Cap、Wispr Flow、Screen Studio、Raycast、superwhisper……看到好的地方就圈出来，再说上一句自己的想法。

![圈出导航栏的 star 数](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFkwKhScCrlmaabIfg0tD78OaBwHDsr84vUhibZRHgtfJSSxlfvJK2vnL9QsJDyqkvo7iaDxTEs2GmH9wnLGskLiaLMkPCUsFXQvAA/640?from=appmsg)

圈出导航栏的 star 数

巧妙的是，这里完全没有我的参与，全是 Claude Code 和口喷鸡自己来完成的。鼠标和画笔是它写脚本驱动的，旁白是用 macOS 自带的 TTS 合成后混进视频的，对各个站的评价，也都是它自己的看法。

录制、语音识别、读笔迹、抽帧、整理等工作链路，则是照着口喷鸡的正常路径真实跑出来的。

换言之，它用自己刚做好的新功能，录了一段自己逛网站的口喷，再交给自己去整理，吃自己的 dogfood。

全程 4 分 56 秒，画了 19 笔，合成 16 处标记，全都正确地落在了目标点上。

![16 处标记总览](https://mmbiz.qpic.cn/mmbiz_jpg/ZKqVLiaIpzFlMxX5DXzRV5hy3flAHUDugulxqvINic6iaTLGwoacTCEMXicQm1E4wLhy5obcPmL9abLgfDMZZg59icvkoA17vjvpPX5vVibdSiaAFI/640?from=appmsg)

16 处标记总览

## 逛出来的需求文档

03

那这段不到 5 分钟的口喷，能整理出些什么呢？

最后出来的是 **16 条事项** （13 个想法、1 个设计决定、2 个待办），外加一份 12 条需求的需求文档，和一份设计文档。

![整理出的 16 条事项](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFm16VaX5g3dGpePeRxzlIeWO4D5h1bHphuPZNxTrD6msZvWgt65jBUFZVthvtGibFdicPd8UapnejqBauLUlygx2SicG9uticSkNNA/640?from=appmsg)

整理出的 16 条事项

点开每一条，都带着当时圈过的那张截图、说的原话，以及想法是什么、为什么、灵感来自哪里。

![单条事项的审核页](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFn9GWlFfAicvQaBDmy9alQDCdsxMO23iaPDQTyicj1g8OZm3sgBNOn5F8amOxSpkBKKgAI2booPfskwiayV4KO95BJDibcfPQMDSDtg/640?from=appmsg)

单条事项的审核页

比如看到 Cap 把 GitHub 的 star 数直接放进了导航栏，它圈了一下，说我们是开源项目，这个必须学。

看到 Wispr Flow 用「键盘每分钟 45 个词，语音 220 个」把价值讲清楚，便有了后来官网上的「2 天」对「半小时」。

看到 Screen Studio 把隐私分成「留在本机的」和「你选了才上传的」两栏，决定隐私那一屏就照这个来做。

![隐私分成两栏](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFmUicm8QqjnFfRrIgsYo0EOakp1pYgtyMdD4CCjkLWfdqOTw2Sz0tjSCDdQVS2bCJHLXEiaIk7ejHicWMZQBU5H0rPmr9RYVQywWs/640?from=appmsg)

隐私分成两栏

它甚至还给自己安排了一段改口的戏，先说要把 `⌥⇧R` 做成大按键放在首屏，紧接着又说「算了，首屏已经够满了」，整理时也确实是按后一句处理的。

还有个小插曲是，逛的 6 个站里有 3 个一进门就弹 cookie 窗，于是需求文档里便多了一条「官网不放 cookie 弹窗」。

语音识别这一步则出了不少错：Jam 被听成了 Gm，README 被听成了「李娜」，「AI 全懂」成了「爱拳懂」，连口喷鸡自己也成了「口喷肌」……

但这其实没关系的，语音识别本来就是容易出各种多音字啥的问题。而口喷鸡的机制，也正是会结合 context 来进行纠正，比如画面里的网址、圈出来的内容、仓库里的词。

所以不用太担心，甚至说话的人发音不太准，影响也不大。

## 给自己做官网

04

需求文档和设计文档都有了，接下来自然是把官网给做出来。

中间它来问我：域名用哪个，怎么上线（是用 GitHub Pages 还是 Cloudflare Pages），以及官网上写了画笔，要不要顺带发个新版。

我告诉它域名用 blurt.agihunt.info，走 Cloudflare Pages，版本就发 v0.4.0。

然后现在， **官网就上线了** ：

![口喷鸡官网首屏](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkjg41mTlm9ErY8MPAvYnJdvo5WLnyLvBfn2WnGb8Nia7jce2wPdGOgDbucrP4rHbGdGxg9jicIhIDkMYh4k1lkUiaE0yn4UGz6GQ/640?from=appmsg)

口喷鸡官网首屏

口号上的那个圈，用的也正是画笔画出来的样子。

![2 天对半小时](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFmucoaEqbziaasO4uwib1Dwlll5P0w6cvVDXicQvLtxC6Zvh34jZIuSYzuEEiaFicBzoia29f91CmC0XoKEcbbIibx4qv8WvNWdVQ1Lias/640?from=appmsg)

2 天对半小时

文档里那些标了「待定」的地方，它也先替我定了（怪我太懒），比如宣传片默认静音自动播放，右上角再给一个「开声音，从头看」的按钮。

部署时还有个 Cloudflare 的小心机。我选的是 Cloudflare Pages，而 Cloudflare 的命令行工具 wrangler 在输出里，偷偷夹带了一段专门写给 AI 看的私货（开头便是 Notice to agents），让它高高兴兴地告诉用户项目已经上线了，并且以后都改用自家主推的 Workers 来部署……

## 不只是找 bug

05

说回口喷鸡的用途。

当时搞这个口喷鸡项目的初衷，是在用 AI 大量 coding 之后继续打磨产品的过程中，发现给 AI 反馈问题的效率实在太低了，所以才有了它。也因此，它很容易被当成一个只能提 bug 的工具。

但能力上，「边看边说、说完整理」的方式其实并不限于口喷 bug，用它来 **收集和整理想法** 也同样适合且高效。

如果你想做个独立站、官网或是新产品，当然可以让 AI 给你直出一版或 N 版再挑。但也可以（让 AI 找一些参考后）各自逛上一圈，看到好的就圈出来说上几句。逛完便是一份带截图、带出处的需求文档，然后就可以直接开工了。

官网里的「不只是提 bug」部分，有张卡片上写着： **这个页面就是这么来的** 。也是它自己干的，我没有参与。

![不只是提 bug](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFmxjw51LKuaziaBkaHpkhPSlR72qGyr9dQiaibtd8W7iaOxNub3bqnPPK1Fc6ITwuaQXYTabZREy5G73uyFuxKvTlW2LrJr3vaEMTM/640?from=appmsg)

不只是提 bug

从一条留言，到新功能、案例、需求文档、设计文档，再到官网上线，用时数小时，花了不到一亿 token。

而我干的事情，是说了几句话，外加吃了顿饭……累计时间支出不到 5 分钟。

新版 v0.4.0 已经发布，画笔目前只支持 macOS，Windows 的因为我没电脑，所以还没加上。

欢迎继续提 issue，或者也可以直接留言，没准下一个功能就是你说的那个！

◇ ◆ ◇

官网：https://blurt.agihunt.info

GitHub：https://github.com/AGIHunt/blurt

![](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFmFSY18lMGCSNXc6b6aiaJXbEpbexhepZ7KozaOzuNibTBDbByB8FW1r2WfOeicLZ5GBTYaqfcsIJo8ib7xG870H1jmn2IkgEHLDGk/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过