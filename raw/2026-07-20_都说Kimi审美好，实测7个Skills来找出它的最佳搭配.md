# 都说Kimi审美好，实测7个Skills来找出它的最佳搭配

**作者**: AI沃茨

**来源**: https://mp.weixin.qq.com/s/MkqpZv3fsCcnlpQu2tGM1A

---

## 摘要

为探究审美出色的Kimi K3是否还需要额外设计Skill，作者使用同一提示词和相同技术栈，对比测试了纯K3与7个设计Skill的搭配效果。结果显示，纯K3首稿表现惊艳，具备独立的视觉逻辑且动效丝滑，仅存在信息过载的瑕疵。相比之下，首个测试的高星Skill“Web Design Guidelines”反而出现重复模块、排版不等宽和空白页等翻车情况，实际生成效果不如纯K3本身。

---

## 正文

AI沃茨 AI沃茨

在小说阅读器读本章

去阅读

昨天去逛了一圈WAIC，一万步起。

回来一看时间，Kimi K3模型参数大家也都了解的差不多了。

大家聊Kimi K3，最直观的感受根本不止什么2.8万亿，也不是896个专家，就是好看，打开X，到处都是K3做出来的网页。

一些页面的字体，留白和画面节奏，已经不是完全没有那种AI帮我东拼西凑拼出来一个网站的感觉了。

Kimi官方放出来的两个视频也很夸张，一个是可以直接在浏览器里玩的3D开放世界，一个是带大量交互和视觉变化的网页体验。

这时候，一个很现实的问题就冒出来了。

Kimi K3自己的审美都那么强了，那我们还有必要给它装设计Skill吗？也就是说，装完以后页面是真的会变好，还是只是换一套颜色？具体又是哪一个设计Skill会是Kimi K3的最佳搭配呢？

我直接跟我钱包和睡眠时间一拍即合，199的K3直接冲了，参考了X上我看到动效、UI设计、文风都挺好的一个复杂Kimi Case，我给到Kimi K3同一份Prompt，用同样的技术栈，前后换了7个设计Skill，

来看下他们能给我们呈现的汇报什么效果。

关于测试的提示词，

```css
请使用本轮 Design Skill：{{SKILL_NAME}}，以 Next.js、React、TypeScript、GSAP、ScrollTrigger 与 Lenis 构建 Kimi K3 网站。项目目标是呈现“FROM FRAGMENT TO SYSTEM”，将文档、代码、数据与决策连接成长上下文，并转化为可推理、构建与验证的工作系统。内容需包含产品介绍、能力、流程、系统参数、导航与 CTA。验收要求：设计 Skill 明显影响 UI、交互与动效，支持响应式、键盘操作和 Reduced Motion，且无报错、无模板化卡片堆叠。
```

而且我在长时间测试 Kimi K3 的过程中，会发现它做一个任务的时间特别长，

所以它比较适合像目标模式这样的任务。

大家可以看一下，我这7个skill测试完下来，我一周所有的用量都被烧完了，平均生成一个这样的网页大概会在40分钟到一个小时的样子。

![Image](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8Fx2dRNmrick7nic9oOEW4mOHkXsLXpWRDJMtCmSiaMqicX33EHgaPLGhuhicmhy0tF5rXoticWoSQBBQKiapuJ7RoTiaiclbqpJ5hDfEQPc/640?wx_fmt=png&from=appmsg)

首轮先看一下在完全没有其他Skills的情况下K3的表现，第一稿出来的时候就已经惊讶到我了，

前面的橙黑主题，出现一个零散着K3各种优点的组件的画布，随着鼠标滑动会慢慢汇聚到一起，中间还有橙色大横线做了一个文本扫描的动效，再然后就是切换到米白色动效少一点主题，

能看得出来K3做这个网页之前是有自己的视觉逻辑在的。

这种完成度在其他模型里真的很少见，让它们做一个页面或者一份HTML PPT时候的滚动，转场和画面衔接没有K3这么丝滑。

如果说从页面上看它有什么问题的话，就是它有点太想证明自己了，字塞得太多。部分内容和装饰也稍微有些累赘，需要我再帮它做一次减法。

OK，紧接着，模型不换，任务不换。只换设计Skill，每组只跑一轮，不追问，不返工，保证公平。这里叠个甲，这不是一张设计Skill永久总榜。我测的是它们跟Kimi K3搭在一起，谁更合拍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FweMhMHx3TRL4Pj4pUM5wFicI2e1JtGhS8EHGtibgOvCK8iahj3OVdfYYJHZLEZ0QJGTGibA0XricsjUmic3aCMrzRGX2sKxnT0ib7ib1w/640?wx_fmt=png&from=appmsg)

先来看看Kimi K3+Web Design Guidelines，vercel出的agent-skills里的其中一个skill，Github star数29.2k。

从Readme上看把网页设计里那些该注意的规范能一股脑全塞给了模型，感觉怎么着也不至于犯什么大错。结果，第一个翻车的偏偏就是它。

首先在整体风格上，开头选择了蓝白风格，但在中间多个离散文本片段随着鼠标滚动要聚合在一起的时候，做了两个重复模块，也就是说第一个模块其实不会动，后面那个模块才会动。接着是盘点Kimi K3能力的列表也，这左右两个列表甚至都不是等宽的。然后中间甚至还出现了一个完全空白的页面。

整体上来说，效果反而是比纯Kimi K3自己跑的要差。

我后面复盘再仔细看的时候，发现字体居然还会有溢出，就这种非常低级的错误反而会出现在这里，完全不应该啊！

![Image](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwNtz5enAvEYW32YgwU0w3WIAlHJfwQdoYQSNcGpiaprE2gqgBEo8ov7Dj7x1oMnRvIkPSn4ciae13nALlzrqwOXdFYhBGoAIxZc/640?wx_fmt=png&from=appmsg)

我给模型装skill加设计规范，是想让Agent少犯点错。怎么加完以后，连页面都给我干没了。。。

所以这就是为什么GPT 5.6上来了之后，大家都在删Superpower，

Skill它不是万金油，不是说装上就自动加分升级的。里面的规则写得再正确，如果没办法把它们顺利转成设计和代码，最后交出来的东西，依然可能还不如模型自己琢磨。

OK，下一组，Kimi K3+emil-design-eng，Github 16k，直接把分数拉了一大把。

这一版最明显的变化，就是在数字出现时会有滚动的特效，凌乱的主题文字通过鼠标的滚动聚合在一起的时候，还会从浅到深。也就是说，我们在滚动的时候，不会看到一大堆同样颜色同样强调的东西。画面在移动的过程中，始终是有视觉焦点的。从浅色主题往深色主题转换的时候，也会做一个渐变的动效过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/VNz1x8bH8FxGo5gcUoBu4NUwVQvyEqxwFDOeubmeMjcjeiafQNfKOibLBZH4ib52ia9icw99ia6GtQeKGjXvRVXochtpqB2BTRviaBs49rlIVkfYgU/640?wx_fmt=gif&from=appmsg)

（压缩了一下没那么丝滑，还是看看上面视频）

从配色，字体，到动效节奏，emil-design-eng都在往一个更克制更完整的品牌系统里收。其实没有非常在堆叠交互和特效，我觉得这一点特别重要。

比起追求炫酷的效果，我更想看到整个页面的交互和特效是同一种思路，不要出现上面明明已经是由浅入深，下面却突然加一个爆炸效果，再下面又加一个火光效果，这其实打乱了我看信息的视线。

我觉得更好的方式是，先通过前面的效果吸引注意力，当我们的注意力从无序状态，过渡到看见由浅入深的设计时，我们会下意识地去预测接下来的变化。就像你看到我走在大马路上不小心被东西绊了一下，你会预测我下一秒的动作应该是摔倒。

同理啊，当我们在页面一开头就已经知道由浅入深是一个强调的过程，后面再看到这个动向时就会有预期。这样一来，越往后刷越能够集中在文字或内容本身。

这是我自己很喜欢的舒服的表达节奏。

然后是熟人UI UX Pro Max+Kimi K3，Github 107k。

表现一如既往的稳定，

因为UI UX Pro Max在实现的过程中，是会去主动搜索和参考一些设计规则和场景的。所以很多时候字体，间距，对比度，组件状态，移动端这些都会兼顾到。

简单来说，它很像一个做过很多项目的老设计师，我给它多少模型算力，它就能给我一个多大的活。

![Image](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwfK7drqefbA6RVibeYX9IMOGaua0np7sd7LIO11pria7u7OWu0AO8O9bVS1Rv2JRibj2iciaepOJNI1d7O3TPaq8JnWrtgQI7G1rt8/640?wx_fmt=png&from=appmsg)

所以如果你的目标是稳定，如果你不想每次都抽卡，甚至希望团队里不同的人都能拿到差不多的完成度，它依然是非常稳的兜底选择。

OK，下一个下一个，Kimi K3+Frontend Design，这就属于是元老级了，A社自己的Skill，Github 162k。

这一版明显感觉头脑风暴了更多，在左侧做出了一个新的目录，页面与页面之间的连接关系，以及跟随鼠标变化的效果，都做了更大幅度的改变。

但它同时也出现了一些Bug，个别布局和交互状态没有完全收住，然后就会导致动效反而把字体完全覆盖掉了。

所以Frontend Design+Kimi K3给我的感觉很像一个脑洞很快的前端设计师。

让它自由发挥的话，它能给你一些没想到的东西，代价就是后面最好留一点时间做返工。

再来是qiaomu-design，

向阳乔木这一版的特效和交互特有意思。

它做了一个一直有效的漂浮卡片的设计，卡片会持续参与不同场景之间的变化，把原本分散的内容带进下一段。

我看到以后研究了半天，都没完全确认这到底是一个设计，还是一个碰巧挺好看的Bug。。。

但反正只有一轮测试，我们没有继续追问，也没有让它改。出来什么，就展示什么。这些漂浮卡片路过其他模块的时候，确实颜色也会变浅，不像是写错了生效范围。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwLMibiaD42eoLJbfMwvUlQ9ZgBDlN1m0ug4mwmyrxia5rW5lHK9wya5EZyQac6sb1e0lYqRW3RVF0XXZjRvgfWCo9ViaVjcAZmLv0/640?wx_fmt=png&from=appmsg)

我的想法是如果喜欢探索型页面，喜欢滚动叙事，实验排版和比较强的画面变化，qiaomu-design+kimi k3的组合可以多试试看。

再再再然后是Impeccable，Github 47.6k。

它的配色应该是这次所有版本里最大胆的一个，也符合Skill的定位跳出固定的色块想法。

白色底，近黑色文字，再加一条非常强的莓红色轨迹，整个页面的视觉存在感很强。

![Image](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwyleG2N2uNsE2kFM1BlKGkK6QcRRguS7jZICnu32wiacaORepAoNpHNibEmVYSYvibxTUicdrXgqkhI9Aow313OV1D8HCyZZtuIcc/640?wx_fmt=png&from=appmsg)

整体没有发现bug，移动端和Reduced Motion也做了处理。

颜色很有意思，能让我第一眼很容易记住，莫名有种微软的三件套的风格。

它其实更适合那些希望页面有明确风格，愿意承担一点视觉风险的项目。

那这次我最喜欢的是kimi k3+design-taste-frontend的搭配，

先说结论，我觉得这是目前跟Kimi K3搭得最好的一组，非常像是模型公司会做出来的主页。

它没有上大胆的颜色，也没有给每一个区域都塞满特效。但就是该有的交互又都有，还有几处挺好玩不会压过文字的动态画面。重要的是，这一轮完全没有测出任何Bug。

在惊喜和稳定之间，找到了舒服的平衡。

总的来说，七个Skill全部跑完了，还有Open Design都没有额度测试了。

如果一定要排，我会分成三个梯队。

第一梯队是design-taste-frontend和Impeccable，一个克制，一个大胆，但都明显放大了Kimi原本的能力。

第二梯队是UI UX Pro Max，qiaomu-design，和Frontend Design。表现稳定稳，敢玩动效，内容都可以根据场景参考。

剩下的emil-design-eng和Web Design Guidelines，我觉得更看项目和个人口味。

但测完以后，K3放在这些版本里居然还是很能打，甚至比部分加了Skill的版本更顺。

所以做页面，不一定非得给K3加个设计Skill。

它本身已经会设计了。

Skill更像是给它换一个创意总监，

让它更稳定地做成你喜欢的样子。

在模型越变越强的今天，过时的规则，冲突的审美，写得太满的流程

都可能让一个原本很聪明的模型变得束手束脚。

好的Skill不应该像护栏，把模型困在里面。

它更像是一张我们自己画了很久的地图。

哪些路我们已经走过，哪些坑我们已经掉过。

然后当一个更强的模型来了，

我们把这张地图交给它。

它不用再从原点开始。

Kimi K3这次带来的，是个万亿的模型，是个更大的脑子。

当它读懂我们过去留下来的所有Skills，

它最后就是能慢慢变成，

我们习惯的好用的样子。

@ 作者 / 卡尔 & yc星辰

---

最后，感谢你看到这里👏

如果喜欢这篇文章，不妨顺手给我们

*点赞｜在看｜转发｜评论 📣*

如果想要第一时间收到推送，不妨给我个星标🌟

如果你有更有趣的玩法，欢迎在评论区聊聊🤝

更多的内容正在不断填坑中……

![](https://mmbiz.qpic.cn/mmbiz_jpg/YEhakvKZjXmCDLEEW1wClZOVGFURjmibJmciaYLNhp0N55Y6mPiaCj01eV8yzACqDvWDhicbPm07Wu7bboATuKgAbA/640?wx_fmt=jpeg)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过