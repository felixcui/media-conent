# “我把所有模型都换成了DeepSeek V4”：月账单降 90%，效果还更好

**作者**: Tina

**来源**: https://mp.weixin.qq.com/s/_k6tFQEKrvUiGh1RFDOUrQ

---

## 摘要

文章认为，DeepSeek V4 以开源、百万 token 上下文和约为 GPT-5.5 十分之一的价格，正在改变大模型竞争逻辑；在编码等场景中，它被部分重度用户认为效果更好、成本大降，迫使市场从单纯比性能转向同时比价格与实用性。

---

## 正文

Tina Tina

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNiax9B9dicdyKHDxTxPWewqGzIPBGok7erA4InsibyVy2I3icpcj4Bb4RDDn15grMaDwbfoaVH1hKO0qlMZMKjcb8KfQrCj42BfV3E/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_gif/YriaiaJPb26VPQqHC66RJFpttVIMWG83T3lWHahUD4bvhxlKSayjeV2ibvC5ydqklP9QHDPD3qHJM07TV3IfHstjA/640?wx_fmt=gif)

作者 | Tina

2026 年 4 月 23 日，OpenAI 做了两件事：发布了 GPT-5.5，并把价格翻了一倍。

按常理，这应该是属于 OpenAI 的一天。全新预训练架构“Spud”的首个公开版本，SOTA 级的基准测试成绩，SemiAnalysis 在第一时间给出了“GPT-5.5 已经抵达前沿”的评价。但翻看定价页面，开发者很难不算账：每百万输出 token 收费 30 美元，比前代 GPT-5.4 贵了一倍，甚至比一贯以昂贵著称的 Claude Opus 4.7 还要贵出一截。

而仅仅过了不到一天，4 月 24 日，DeepSeek 把 V4 的模型权重扔到了 HuggingFace 上。MIT 开源协议，100 万 token 上下文窗口，以及一个极其低廉的价格：输出 token 每百万 3.48 美元。

大概只有 GPT-5.5 的十分之一。

科技博主兼 AI 系统架构师 Sean Donahoe 在今天凌晨发了一条帖子。他写道：

> “DeepSeek V4 Pro 在编码基准测试中击败了 Claude Opus 4.6 和 GPT-5.4...... 今天早上，我把 Claude Code、Codex、Cursor、Aider，以及我用的所有其他编程智能体全部指向了 DeepSeek 端点。不用 OpenRouter，不用代理，原生 API。我的月账单将下降 90% 以上，而且效果比昨天还好。”

这条帖子实际上有两个看点。第一，发帖人是重度 AI 编程用户，却几乎一夜之间完成迁移，月账单会从几千美元降到几百美元。第二，他不只是说便宜，还强调效果没有变差，反而更好：“输出质量提高了，而不是下降，这一点已经通过内部测试以及多个公开基准验证”。 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNiaQasqJVgMFJHvQibuCeKMbv7TQFdL5tWewSAKTyvRPeJiaYCZhiba9yDrZE3lrhp64NfSb4mibdcXM2cSF4xvjgDrZ8CwZe4zxtV4/640?wx_fmt=jpeg&from=appmsg)

DeepSeek 出手之后，价格成了第一变量

过去三个月，模型竞争激烈。几乎每周都有一家头部模型厂商发布新的 coding checkpoint，GLM-5.1、Qwen3.6-Plus、Kimi K2.6、Composer 2、Gemini 3.1 Pro，都在强调同一件事：agentic coding、长任务、多步骤规划。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNjYU12ah3CEToCoI0IYs57Via8OcQCUfPtibcOfnlMHX9QHwBf9YU6trhWNgibMkozfaOIvibgicMwaDRsiboZgGCHnuY06PN9oI4V7c/640?wx_fmt=png&from=appmsg)

进入 4 月，圈子里一直在讨论两个代号：Anthropic 的“Capybara”和 OpenAI 的“Spud”。4 月 23 日，GPT-5.5 正式发布，成为基于“Spud”的公开版本。对 OpenAI 来说，这是 GPT-4.5 之后一次很关键的预训练模型更新，外界期待很高，价格也不低。有分析指出，虽然 NVIDIA 和 OpenAI 都提到 GPT-5.5 在 10 万台 GB200 NVL72 集群上“训练”，但这里的“训练”更准确地说是强化学习的后训练阶段。真正的预训练，仍然是在 Hopper 平台上完成的。

但只过了不到 24 小时，DeepSeek V4 开源。模型竞争一下子不只是在比谁更强，也开始比谁更便宜。

OpenAI 的旗舰模型过去通常比 Anthropic 更便宜，但这一次不一样了：GPT-5.5 的 API 定价为每百万输入 token 5 美元、每百万输出 token 30 美元，比前代 GPT-5.4 贵了一倍，甚至比 Claude Opus 4.7 的输出定价还贵出一截。

更值得注意的是，OpenAI 为 GPT-5.5 设计了一套复杂的定价分层。除了标准 API 之外，OpenAI 还提供了一个优先级（priority）套餐，价格是标准档的 2.5 倍。如何为“更快的 token”收更多钱，正在变得越来越关键。这里需要说明的是，priority 和 fast mode 是两回事。fast mode 只是给出一些相对模糊的承诺，比如“价格贵 6 倍，速度大约快 2.5 倍”；而 priority 提供的是更保守但更明确的 SLA（例如：99% 的时间里吞吐量超过 50 tokens/s）。

这还没算 GPT-5.5 Pro——专为科学研究和长程推理设计的版本，输入 / 输出定价分别为每百万 token 30 美元和 180 美元，瞄准的不是日常编码场景，而是前沿科研用例。

标准版和 Pro 版都提供多档推理强度：xhigh、high、medium、low 以及 non-reasoning，本质是在成本与能力之间做取舍。从 strawberry/o1 那一代开始，这一点已经很明确了：推理强度越高，结果通常越好，但消耗的 token 更多，响应时间也更长。

在 GPT-5.5 发布前一周，Anthropic 刚刚推出 Claude Opus 4.7。相比 4.6，Opus 4.7 更像一次小幅升级，没有带来明显质变。

Token 计数方式的更新，是这次定价变化里最关键的一点。4.7 使用了新的 tokenizer，通过更细粒度的切分来换取性能提升，但代价是整体 token 用量会上升。官方也直接承认，这会带来最高约 35% 的 token 增长——换句话说，价格也等于变相上涨了 35%。

然后 DeepSeek V4 来了。

V4 系列包含两个模型：DeepSeek-V4-Pro 和 DeepSeek-V4-Flash。前者参数规模为 1.6T 总参数 / 49B 激活参数，后者为 284B / 13B。相比 V3（671B / 37B）是一次升级，而 Flash 是一个更轻量的下探版本。这使得 DeepSeek-V4-Pro 成为目前规模最大的开源权重模型。

把价格拉出来对比，差距大到让人无法忽视。简单算一笔账：同样处理一百万输入 token 和一百万输出 token，GPT-5.5 的合计成本是 35 美元，Claude Opus 4.7 是 30 美元。而 DeepSeek-V4-Pro 是 5.22 美元。如果输入命中缓存，输入价格进一步降至每百万 token 0.145 美元，同样这笔账就变成了 3.625 美元。

也就是说，在标准定价下，DeepSeek-V4-Pro 的成本大约是 GPT-5.5 的七分之一、Claude Opus 4.7 的六分之一。如果缓存命中，差距进一步拉大——大约是 GPT-5.5 的十分之一、Claude Opus 4.7 的八分之一。

真正把价格压到“近零地带”的，是 DeepSeek-V4-Flash。V4 Flash 的 API 输入价格每百万 token 仅 0.14 美元，输出价格 0.28 美元，合计 0.42 美元。缓存命中后进一步降至 0.308 美元。同等输入输出量下，Flash 的成本不到 GPT-5.5 和 Claude Opus 4.7 的 2%——便宜了 98% 以上，几乎只有对方的百分之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNiaiaERsxia7WEhFsc25bbPNFVPOSwaLsEGheaDIGzVMZ2QoZqMrFBN58VyoC2oZsaiaibRHEoicSMtaALeue33ODzjJPepqiadVTLiaxo/640?wx_fmt=jpeg&from=appmsg)

如果把当前主流模型的定价放在一张表里看，这种分化更加直观：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNgkE1d0NLGXTpyic2CEnhIUV5SYFlyh9Gh1iaeRhO4ebj6xP4CbUQ4214XHbhsl7HHuNbd2ZxrF0Xy1bXo9F707ABVBVMV2MOicJc/640?wx_fmt=jpeg&from=appmsg)

更重要的是，DeepSeek V4 走的是 MIT 开源协议。这意味着开发者完全可以把模型部署在自己的服务器上，不走 API 调用，直接绕开 token 计费逻辑。对于有合规要求、数据不能出域的场景，这个选项的权重甚至超过价格本身。

V4 相比 V3 的核心进展，是上下文窗口从 128k 提升到了 1M。因此，这一代的技术优化几乎都围绕长上下文展开，包括：

- Compressed Sparse Attention（CSA）：压缩稀疏注意力
- Heavily Compressed Attention（HCA）：高压缩注意力
- Manifold-Constrained Hyper-Connections（mHC）：流形约束超连接

对应的效果是：“在百万 token 上下文场景下，DeepSeek-V4-Pro 的单 token 推理 FLOPs 仅为 V3.2 的 27%，KV cache 仅为 10%。”也就是说，KV cache 减少了 90%。这个幅度甚至超过了上个月 Google TurboQuant 的论文，对 NAND Flash 产业链来说，是个需要警惕的信号。

在工程层面，DeepSeek 还在 DeepGEMM 中开源了一个 Mega-Kernel，宣称支持 NVIDIA GPU 和华为 Ascend NPU。可以看出，他们的目标之一，是未来在 Ascend 上承载一部分推理流量。官方 API 页面还提到，受限于高端算力，目前 V4-Pro 的服务吞吐仍有限，预计下半年昇腾 950 超节点批量上市后，Pro 价格会大幅下调。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNhGjrm1hsQxP9yjT3HrCEgqrHhMRGXicjaq8s9suULIYRlXpva9MOKsmCscrd0urao6T4BGTgvSQh2Iao7hMN8QibCRqWeoibfBRU/640?wx_fmt=jpeg&from=appmsg)

业界实测效果

三款模型，三种定价逻辑：OpenAI 在涨，Anthropic 在偷偷涨，DeepSeek 则直接掀桌。如果只看数字，选择几乎没有悬念。

不过，DeepSeek 自己也承认，和顶尖选手之间还有距离。他们在技术报告里写道：“通过增加推理 token 的使用量，DeepSeek-V4-Pro-Max 在标准推理基准上优于 GPT-5.2 和 Gemini-3.0-Pro，但仍略逊于 GPT-5.4 和 Gemini-3.1-Pro，距最前沿模型大约还有 3 到 6 个月的差距。”

那么，实际效果如何呢？

在 Sean 宣布全面迁移的同一天，AI 研究员 Rohan Paul 和他的团队做了一个测试：给 DeepSeek V4 Pro 和 GPT-5.5 同一份提示词，开发一个完整的卡丁车竞速游戏，全部塞进一个 HTML 文件。

提示词严苛到像一份游戏策划需求书：Canvas 渲染，方向键和 WASD 双套操控，加速、刹车、漂移、倒车一个不能少。物理引擎从零手写，摩擦力、最高速度、转向灵敏度全部要调。赛道有路面、草地、弯道和窄路，冲上草地减速，撞墙弹回。至少 3 辆 AI 对手，自动沿赛道行驶，速度各异。道具系统要有金币、加速板和随机道具箱。画面全用 Canvas 形状手绘，漂移拖痕、加速尾焰、屏幕震动，一个视觉效果都不落。音效用 Web Audio API 合成，倒计时、碰撞、冲线都要出声。UI 要完整：标题画面、3-2-1 倒计时、实时 HUD、结束排名。

最终的数据对比是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhaJ4beMaTEKtic7dweuaTGsunA2tvwB8pNQIhhusWm7TXsD1FAdc9onXu57l6Dhl8eG6qK5ua1Z9T0I2gXtkoL3KAsnfsC3sCE/640?wx_fmt=png&from=appmsg)

DeepSeek V4 Pro 输出了近两倍的 token，但便宜了 4.3 倍。至于两个游戏跑起来分别是什么样子，我们直接上视频，你自己体验。

如果说卡丁车测试考察的是“能不能做一个完整产品”，那同一天另一个测试考察的则是更微妙的东西——审美。做出来的页面“好不好看”，任何人都能一眼判断。

中文技术社区的一位开发者用同样的提示词、同样的工具，让 DeepSeek V4 Pro 和 GPT-5.5 各自生成一个 Apple 风格的天气界面。提示词给了一个很高的起点：

> “你是 Apple Inc 的顶级 UI 设计师，以 iOS 18 的设计风格（毛玻璃效果、高斯模糊、动态渐变、细腻阴影）创建一个单个 HTML 文件。实现横板天气页面，包含 4 个并排的动画天气卡片：晴天（太阳光线、动态光晕）、大风（飘动云朵、摇曳树木、风线）、暴雨（下落雨滴、形成水洼、闪电）、暴雪（下落雪花、堆积效果）。卡片需深色背景，支持按钮切换天气状态，实现流畅交互和微动效。代码必须可直接运行，美观度优先。”

工具也完全统一，两个模型生成时，用的都是 Claude Code。你猜哪个是 DeepSeek 的？

生成结果 1 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNh6t8SUJDeTQcNSRUib4w91pOkpscKprP10J93A4uuPVDPTszoWIPgdXvcicKkicSJkXDnujpXTx7fWKqbD6HKbtpTjmr9E0o8WC8/640?wx_fmt=png&from=appmsg)

生成结果 2 如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNgVIeCzZpmalNMTaCBlgW64ib4RwFZ2iajKxVe0qdslNh3GmqYY8icWRw2gQ9F0YJf413uZU3YuBfoI37pSDGyAyyhZyXWGDYZB00/640?wx_fmt=png&from=appmsg)

不过，在日常问题上，DeepSeek 确实更强：

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhibpvcdKvxb0DD7mmpFMNofv90OgCn0wuvjYdUUpr4Jibvp9KxAe0OSEKUkhpXPdRUbyg8wFuhDQ8TgBxarfEC3yelfZsjK4fNQ/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNhF7Kmcic8ibngcibUfHZl3aqZzNzBLKIhptg262zOj2WbWhEiaUVEtzr82vdSwSOV1jlgz0z7R4pT2fdKyDLBKlcB85ia05a4FGrhY/640?wx_fmt=png&from=appmsg)

科技博主 Simon Willison 有一个习惯：每次 DeepSeek 发布新版本，他都会用同一句提示词 “Generate an SVG of a pelican riding a bicycle”，生成一张鹈鹕骑自行车的 SVG。这次 V4 发布，他照例做了一遍，也照例把历代结果放在一起。

从 2025 年 3 月的 V3，到 8 月的 V3.1，再到 12 月的 V3.2，以及现在的 V4，每一版都比上一版更像样。早期的鹈鹕歪歪扭扭，脚踏板对不准，自行车架子也松散。到了 V3.2，车架结实了，鹈鹕也开始像个正经骑手。这次 V4-Flash 又往前走了一步：链条画出来了，前轮加了反光片，翅膀搭在车把上，脚也踩到了踏板上。总之，是一次比一次好。

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNjBSktUEXw7xKOE5myvFzTtQdQ8Qx91HHYeHMKqef78SzwlVFbwWOpUfPKlgyjeNNdsU1Vk7grYc60iahEEd910RcgGckyeICBY/640?wx_fmt=png&from=appmsg)

DeepSeek-V3-0324

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNgg9GdggSxrQSRVXbL6joVns9KpIBvaibteGqNRHrttRZp48YEvy17j11iaCb2d6gsCiae8NEiavCHtCxjQqcTiaSEXy5SDDXnof6EI/640?wx_fmt=png&from=appmsg)

DeepSeek-V3.1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNgZyyGibRicB3sL5BILu6OhIhibLLgnia8XHOwtq45LuF6yE9CAPKk613z9Zl8QwicaJSR8J4ic7bfnXiapXbpdic8bVDYlE2bgzRZdoUE/640?wx_fmt=png&from=appmsg)

DeepSeek-V3.2

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhulYFjG88hCJB6qZ8ANZjPKGy33TlWHRmw252Y1PAkgH3sqCLYV5icoH3N6qvKEkWm2f7gWYxo42HTIJYvCicrvr2lTKVKGUd4c/640?wx_fmt=png&from=appmsg)

DeepSeek-V4 Flash

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhoNCCrTGmMmJGHFx04PW1CJNUnhAZ7fxPHcwvJ2iczJHtmtLicoVB0x2veKk4KaCA0XtV0ltxOZIBjL8FYlVsEbuw3rAew8PItQ/640?wx_fmt=png&from=appmsg)

DeepSeek-V4 Pro

DeepSeek 在 V4 发布当天，用一句话表明了他们对这些讨论的姿态——“不诱于誉，不恐于诽，率道而行，端然正己。”

这也恰好解释了这只鹈鹕一年来的轨迹。

参考链接：

https://x.com/rohanpaul\_ai/status/2047762509474726285

https://simonwillison.net/2026/apr/24/deepseek-v4/

https://linux.do/t/topic/2045480

https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhLSIh1ZduDjRDsU8OGQRmwBscMG7ZHucztXRKWAnNP0CUNKw8iaicn4SeFxlwNS07wa4gf3OQKrj0ic3XMmkaZN9GdIOALYlPC70/640?wx_fmt=png&from=appmsg)

今日好文推荐

[Claude变笨，Anthropic发报告认了：为优化3个Harness层bug，不小心改崩了](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651282551&idx=1&sn=07b3929fa6460a65c616ad07d53c2f19&scene=21#wechat_redirect)

[DeepSeek V4 重磅开源！首次打通华为Ascend，也没丢掉英伟达，百万上下文夺回国产模型话语权](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651282476&idx=1&sn=d7d2f23cdba9f0f29ceec9e7dc119314&scene=21#wechat_redirect)

[GPT-5.5 赢了 Opus 4.7 和 Mythos？奥特曼晒黄仁勋内部信：英伟达全员用上 Codex！](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651282425&idx=1&sn=ae5b6309ff238600b778056a95d492c5&scene=21#wechat_redirect)

[姚顺雨腾讯模型首秀！不卷参数只做 “听话打工人”，Hy3 preview登场 | 附实测](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651282364&idx=1&sn=e250bbd705d8eac17ed74a3ec8313ba5&scene=21#wechat_redirect)

会议推荐

世界模型的下一个突破在哪？Agent 从 Demo 到工程化还差什么？安全与可信这道坎怎么过？研发体系不重构，还能撑多久？

AICon 上海站 2026，4 大核心专题等你来：世界模型与多模态智能突破、Agent 架构与工程化实践、Agent 安全与可信治理、企业级研发体系重构。14 个专题全面开放征稿。

诚挚邀请你登台分享实战经验。AICon 2026，期待与你同行。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNhBrcIaQon6ZfGlCyGPZibzv52ud1cJFOFd8KILnicE9w8YZck1sdb921l8J3Y555QX3IK4zdyRKKFRY3mFhI4wIS6ibJ9ANia9x9o/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

继续滑动看下一个

InfoQ

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过