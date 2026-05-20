# QoderWork Design 上线，设计即代码，不输 Claude Design

**作者**: J0hn

**来源**: https://mp.weixin.qq.com/s/-aI2DldsCRSt5AoRXr4XdQ

---

## 摘要

阿里QoderWork最新上线AI设计工作台，主打用自然语言直接生成可交付的工程级设计产物，无需依赖Figma。作者实测体验认为其表现不输Claude Design，并总结出三大核心优势：执行前通过提问机制与用户充分对齐需求；生成设计计划供确认后再行动，减少推倒重来；内置140种知名产品风格参考作为设计锚点，有效避免了传统AI设计盲目生成的抽卡问题，显著提升了设计的精准度与交付效率。

---

## 正文

J0hn J0hn

在小说阅读器读本章

去阅读

产品体验

## QoderWork 上线 AI 设计工作台

Design Desk

阿里的 QoderWork 最新上线了一个设计工作台（Design Desk），定位是用自然语言做出可交付的专业设计，从想法到工程级产物，中间不需要 Figma。

![QoderWork 官网](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFl8Rh5WqdoVTRnQr3bYRmShAjtVDSuf4zNXzuzpfRfQ5E1lDIbnFwibvHUWExfnVwUbLyIveHKd5lMaEERKtp2OmHjSwUGDQtHg/640?from=appmsg)

这个产品是我一个前朋友所在的团队做的。我有些故作刁难地问他：和 Claude Design 比怎么样？

他的回答是：

接近平手，小有优点，自行体验。

好吧，这么说反而让我有点好奇了……那到底「小有优点」在哪里呢？既然他给我了一批「你放心用、很难用完」的额度，我自然是必须上手做点东西亲自体验一下子。

做个什么呢

那……我用来搞点啥呢？

最近有个现象叫 **Tokenmaxxing** ，就是开发者们主动或被动的，开始像马拉松朋友们在朋友圈晒跑量一样地晒起来了 token 消耗量。

Meta 内部甚至搞了个排行榜叫 Claudeonomics，8.5 万名员工按 token 用量排座次……（好像说是已经被砍掉了）

![Token 跑量大赛](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlsQia1R3HEZia0L0xVCOUPKLF6rbxnmY6aaruOZLoMqriawyDiaL2OicBkeaGZBjaqkK26icSuUgh0KVicOpo3lIGqxxF5WpTyaE4iccc/640?from=appmsg)

既然大家都在关注 token 用量，那我就用 QoderWork Design 做一个 **Token Farm Dashboard** ，一个 Claude Code / Codex 用量可视化的看板来上手小试一把吧。

看看这个工具到底顺不顺手。

问清楚，再动手

打开 QoderWork，输入需求「做一个 Token Farm 看板」。

它并没有马上开干，而是先抛了一组问题过来：目标平台是桌面端还是移动端？数据周期按年还是按月？

![追问界面](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkVC3iacIgR6icibibPFKvuS5X6Cad0icQxEDectnyX3Zw2jOkg0k9OQlUZyZHVFFCkjpNE6g1f962sSicuALPVxCE0Wa427iaOmLmRyc/640?from=appmsg)

这个机制你可能就有些眼熟了，它叫做 **Ask User Questions** ，信息不够的时候 AI 需要先追问，不瞎猜瞎干。

我回答完之后，它生成了一份 **Design Plan** ，把页面结构、风格方向、产物格式列出来，让我确认后才动手。

![设计计划](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFl7yXbib69TotTLicTOUZ5cO3DVBCstuyZF2c4yAZyc4pk0Dh7vxuYUxf17CsMAKXO0UkD1sFSejM1W7QH1HEXEIJjfkUibTcEhYY/640?from=appmsg)

虽然 QoderWork 多了「先对齐再执行」的这一步，但确实能省掉一些反复推倒重来的时间。

制定正确的目标，然后才行动，以终为始。

140 种风格参考

接下来是选风格。

QoderWork 内置了 **140 种风格参考** ，Airbnb、Apple、Figma 各种都有，每种都标注了视觉特征（圆角、配色、间距风格等）。

![风格参考库](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnWKfc82VkRNwUTj8Hjo569p3gicDKA4C1ib9IC1DnjVmbYgcIicv45muwn1lcaOTGpaicN8lgYIialcqNTLbnicNazicticXP9tyRmddk/640?from=appmsg)

这个我觉得是它比较实用的一个点。

用其他工具，风格全靠你在 prompt 里描述，AI 理解多少算多少，经常需要反复调，各种抽卡。QoderWork 做的是，让你从一堆现成的风格里挑一个起点，相当于给 AI 一个明确的设计语言锚点。

![选风格的两种方式](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFmgXthrslFplrAEre65YCHaQaIGM9CFRayAcia0GVnwToia4K5KmyfIEkh4Qkp2ib1zFBRibjyENm3aDvIibhFJqyCRRBoOJHEcY0iaU/640?from=appmsg)

对于不太擅长描述视觉风格的人（比如我），这个能省不少事。

我选了 Airbnb 的暖色圆角风，然后看着它在画布上一块一块地把看板搭起来。

![生成中](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFk7GibvgNzxWt8YtEfuZwOoDIEy6WBJg10ibfZ4GtibdjyKfibz4KiczZbZt4NoC154pWDjNJRfZFy4Fq6H4to1jwtaZJ10sp9eOpUQ/640?from=appmsg)

画笔 + Nudge

有过经验的都知道，你的想法永远不是一步到位的，这就会涉及到一个问题：生成之后……怎么改呢？

QoderWork 也考虑到了这样的实用场景，并提供了两种改法。一种是 **画笔标注** ：直接在画布上圈一块区域，旁边写上你想改什么。比如我发现模型版本号不对，就圈住那块写了句「现在是 4.6 Sonnet 和 4.7 Opus」。

![画笔标注](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFmq3kgqz2Om4OpTQF8QkfC1ToOaTZStYsLdbUeeHFJywxulHM10cKDp5iaQ60JjricMrYxUO8jGqR99b3QR2N5a05KRHmajIgtEo/640?from=appmsg)

它看到标注后，就会直接给改了。

![修改后](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnXFRzDjBZyWiaOmoSzia9mhdzr5rDHUU1G0kniagHDRqL6UxtSibIOnnBST16flnV9dKmS2pq1lwWicCiaibFhsrDCuPUmFviaQS95mYg/640?from=appmsg)

另一种是 **Nudge** 面板，可以对颜色、间距、圆角、布局这些参数做精细调整，不用打字，拉滑块就能搞定，更友好自然的交互，也更高效。

![Nudge 面板](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnSApAI0iapDyuVDeDDmDZicxMZTTEvNLAUJZJqpIyxgRlvsqeYhpSb3u6g4YNG5M0pGL38eR65FxSJQbygvutwazYInicShheZIQ/640?from=appmsg)

画笔解决「改哪里」，Nudge 解决「调什么参数」。这两搭配着用，会比纯靠打字描述修改意图要方便许多。

![画布全景](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFntwZrb6p3qPh4MvZRBUAFKicoia56bgvu2UyicTcF33KDibnBr64J7o3uyMU9GQGJkdk6ySqd5lpQHz25BpibdZg0VurkGlDxWDCiaw/640?from=appmsg)

产出是工程文件

做完之后的效果，大体是这样子的：

![Token Farm 预览](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFkqkibib27d32Wk0Af6fyVhE0ekCLuvjx6cx9aHLExHGhfb2jXaxnefrCNUMu6Gy1SVuFbBmujo4AVcuOEf3gRuiaFJQAVzxrHIN0/640?from=appmsg)

热力图、模型分布饼图、趋势折线、AI 同事人格卡片、排行榜……基本都有了。

这里还有个我觉得值得单独说一下的功能：右上角的 **Handoff to Qoder** 按钮。

![Handoff 按钮](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFkn1tIlk5H0FBicP90DXmro9yoVE78jZoYCYAYGglu8b8HoljicOaT6ia4qveKkCybmHcnZExibyBV0TG1RdHyKDZASACWHCKwUKQg/640?from=appmsg)

点一下，整个设计就变成了一个 React + Vite 的前端工程，在 Qoder IDE 里直接打开。

![Qoder IDE 目录](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlsu3HydoZ2xY71Iy62UpFM8ttPZEXkFfZjOJuUtQTQlbfzfAyGRubN2ibeiaIR7vwebmW8icKPS3Vn0TUmI5NAvyicGN61mbXdicGc/640?from=appmsg)

这应该是 QoderWork 和其他 AI 设计工具最明显的差异（之一）了。

Claude 产出的是单个 HTML 文件，想真正用到项目里，你得告诉 Claude Code 自己拆组件、模块、对比、验证，耗费你的时间和 token 不说，还可能在过程中带来不一致和额外的调教工作量，而 QoderWork 则会直接给你一个可以继续开发的工程起点。

![设计产出物的区别](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlReVyFYs49uC8BQKua5TTdhCofeByHetIhEaqyWYRFCjZxntXNtgmFib2XJtMrMa6whSzzEmevovoUydnFzIQPRXiasBhqQrbv4/640?from=appmsg)

这也是进一步考虑到了真实的使用场景，这对于做 SaaS 产品或者内部工具的团队来说，会非常省事。

设计即代码

往多了想一步，这个产品背后其实藏着一个逻辑的变化。

以前做产品的流程大家都很熟悉了：设计师在 Figma 里画图，画完导出标注和切图，开发拿到标注再翻译成代码。中间要经历反复的沟通、对齐、验收、返工……设计稿和最终代码之间，永远隔着一层「翻译损耗」。

Figma 这类工具解决的核心问题，是设计师之间的云端协作。但设计到代码的那一步交接，到今天依然是有损的。

QoderWork 的思路不同的是，它从第一步开始，产出的就不是「图」，而是可运行的代码。设计师和开发操作的是同一份文件，不存在「交付」这个环节，因为压根就没有需要翻译的东西。

![设计交付的两种路径](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnuqBkvBLXcAjAuglYT0rBdwPLBNibibT27NviaJmpddc0ezlVPiaWQ9pXEYicmXPp2Drp3k1eHsQJddbQeKdyicxf3SPF5pENE9QKAQ/640?from=appmsg)

而当下正在发生的趋势是：「设计」和「前端」之间的边界，正在被 AI 一点点抹掉并融合。设计文件，正在变成团队一起维护的代码资产。

当然，复杂的交互逻辑、组件状态管理、和后端的数据对接，光靠 AI 还搞不定，还是需要开发者来接手。

但至少在「从零到一搭页面」这个阶段，设计和代码之间的墙，正在不断变薄，甚至最终会消失。

其他工作台

QoderWork 的设计工作台是它扩展机制的第一个落地场景。除了设计，还有 PPT Desk 和 Writing Desk，同一个入口切换不同模式。

![PPT 模式](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnP5wOsdkDxWsGicKLwVjctxeAJibSgVTfnXdhbkI8icEoAuajIsgs9TpqibiaUpfbutms1gIQyRibNfqjnkWiamKpzMndqk9tWq2Rnzo/640?from=appmsg)

它本身是桌面端应用，本地运行，也支持语音输入。

适合谁

说实话，如果你已经很习惯 Claude Design，并且主要做一些快速原型或单页面，那 QoderWork Design 的优势不会特别明显。

但如果你是这几类人，我觉得可以试试：

不太方便用 Claude Design 的

QoderWork 是本地桌面端，不依赖海外服务，且内嵌在产品之中，交互更丝滑体验更佳

做组件密集型页面的

SaaS 平台、数据看板这类场景，140 种风格参考 + Nudge 参数微调真会非常方便实用

不想反复「抽卡」的

选好风格参考，AI 会在你选的框架里出稿，省掉来回调教的时间

需要直接交付前端工程的

Handoff to Qoder IDE 能省不少从设计到代码的翻译成本

![接近平手](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlicyhhDXl7SianlwSDsILwicRE8aJnI5fc6dIOKg6S0xvKTWdcBJicZjic0ALUJDnBuyWKHZ9yYZu1JSzdDz2Iwm4yZvXkvibjykRtA/640?from=appmsg)

总结一下就是，朋友说的「接近平手，小有优点」还勉强算是中肯。它并没有说全面碾压谁、或要杀死谁，但在风格参考、参数微调和工程交付这几个点上，确实做了一些 Claude Design 目前还没做的事。

相关链接：

QoderWork：www.qoderwork.ai

Token Farm Dashboard：https://qwwzdyj.github.io/token-farm-dashboard/

继续滑动看下一个

AGI Hunt

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过