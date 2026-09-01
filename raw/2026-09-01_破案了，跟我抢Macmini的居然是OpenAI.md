# 破案了，跟我抢 Mac mini 的居然是 OpenAI

**作者**: 发布明日产品的

**来源**: https://mp.weixin.qq.com/s/tG7pSuU3zhcb5NBaNYkdOw

---

## 摘要

Mac mini和Mac Studio意外成为OpenAI、Anthropic等顶尖AI实验室大量采购的算力新宠，企业为降低成本倾向于用其替代昂贵的云端GPU来跑本地AI任务。这波意料之外的强劲需求不仅推动苹果Mac业务营收大幅增长，更促使苹果高层开始主动向企业客户推销Mac在本地AI和Agent场景中的价值。

---

## 正文

发布明日产品的 发布明日产品的

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfLWY21zoVKuX3fwEiae7KUibiciaJ3pSRQIZnj9RfxINgobfRalyVVnO6NuSgvib2fRP9XaKHSBC94fn0VLQZ7liaqzMrnUdlC8nicnCI/640?wx_fmt=gif&from=appmsg)

终于知道都是谁在跟我抢 Mac mini 了。

谁敢相信，当年被无数打工人当成入门廉价小主机的 Mac mini 和走专业路线的 Mac Studio，如今居然成了顶尖 AI 实验室成批采购的香饽饽。

![Apple unveils a more powerful Mac mini featuring the all-new M6 and M5 Pro  - Apple](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dCG7OC48IfLXtHYice78GYt4SaTYa2zBIN5uvK0VW5TJUkNGS7m0J3Zz17KSuwY8DpuAaiaB3Ebk162LvylvQliaSlQriburXTXu7wDAZHCLV30/640?wx_fmt=jpeg&from=appmsg)

Apple unveils a more powerful Mac mini featuring the all-new M6 and M5 Pro - Apple

就在刚刚，据 The Information 援引 OpenAI 内部知情人士报道，为了强化学习训练以及 Computer-use Agent 等任务，OpenAI 已经采购了数万台 Mac mini 和 Mac Studio，需求旺盛到公司频繁向苹果催促交付。

隔壁 Anthropic 也没闲着，正在通过亚马逊 AWS 大量租用 Mac 算力。曾经主要服务设计师、开发者和普通消费者的 Mac，莫名其妙成了硅谷 AI 圈的新宠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfJeXEicQqO7UmhzDEaSMVUGYWhtx5Jh8GGtia8VN8SiaRNKjlBlt2bYf53oqqh5zIIicVyagbhVGib603fpBCEcaHNWLypg8wt2SRq4/640?wx_fmt=png&from=appmsg)

🔗 https://www.theinformation.com/articles/apple-stumbled-ai-hardware-success-mac?rc=qmzset

受这波泼天富贵的影响，苹果最近一个季度的 Mac 业务营收同比增长 29%，达到 104 亿美元，增速甚至超过 iPhone，成为苹果硬件业务里增长最快的一块。

面对突然冒出来的企业需求，苹果也开始认真研究怎么解决这群 AI 客户的需求。

库克两个月前在 Apple Park 举办了一场名为 Business at the Park 的企业闭门活动，现场来了迪士尼、福特等大型企业的高管，Anthropic 联合创始人 Jared Kaplan 也亲自到场。

当时，即将卸任的库克和被视为接班热门人选的 John Ternus 双双现身，向企业客户推销 Mac 在本地 AI 和 Agent 场景中的价值。

![誰是Apple 下一任CEO John Ternus？Tim Cook 9 月卸任，見證蘋果權力交接！](https://mmbiz.qpic.cn/mmbiz_jpg/dCG7OC48IfJ9iaPXfghGCxaadc0gLyKykJLObyfaM65v0CWGUJiaib1OJfxSI2pASLsrQ0gljYOSSpQqhsn3k6Id5wRlEcWuCWkyvlyn9oFV2A/640?wx_fmt=jpeg&from=appmsg)

誰是Apple 下一任CEO John Ternus？Tim Cook 9 月卸任，見證蘋果權力交接！

简言之，与其一直给昂贵的云端 GPU 交钱，不如买几台大内存 Mac，把一部分 AI 任务留在自己办公室里跑。

尴尬的是，苹果自己似乎都没有提前意识到，Mac 会突然被 AI 行业捧起来。

今年 4 月离开苹果的前 AI 企业营销经理 Todd Dailey 就毫不客气地表示，苹果过去并没有专门面向企业 AI 客户的工程团队，甚至缺少成熟的开发者关系体系。

换句话说，这波纯属老天爷追着喂饭吃。

我们之前也分析过很多次为什么 2026 年的 AI PC 依旧是 Mac。原因很大程度藏在 Apple Silicon 的统一内存架构，也就是 UMA。

![What is Unified Memory and how does it work on Apple Silicon?](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dCG7OC48IfK7u12msNU2qpnTch3RE9J2zC3tiaLnlSWXXtKoUWEOAgqLv7HopSce9oxeA7N3nPBlxXd5J1DYicibZuNdPNp6Fv1uxkfNkC08Ug/640?wx_fmt=jpeg&from=appmsg)

What is Unified Memory and how does it work on Apple Silicon?

传统 Windows AI PC 通常会把 CPU 系统内存和独立 GPU 显存分开管理，消费级独立显卡显存普遍只有 16GB、24GB 或 32GB。模型一旦超过显存容量，就需要频繁通过 PCIe 在系统内存和 GPU 之间搬运数据，性能和体验都会明显下降。

Apple Silicon 的思路完全不同。

CPU、GPU 和 Neural Engine 共享同一块统一内存池，模型参数和中间数据不需要在不同内存区域之间反复复制，因此一台 Mac 能够把非常大比例的整机内存直接用于 AI 推理。

M6 Mac mini 最高支持 32GB 统一内存，M5 Max 可以来到 128GB，而 M5 Ultra 更是直接把统一内存容量推到了 512GB。

![Apple announces the M5 Ultra Mac Studio with up to 512GB of RAM | Macworld](https://mmbiz.qpic.cn/mmbiz_jpg/dCG7OC48IfJ9oQFWDricfl4NTicjzSTsk7BImKUMY4S2XG718zdzzYiaSp4sTMJJibaJd559KdlOWLUTRcde2GjzMW8OgR8pWcPcic75a13ibdztM/640?wx_fmt=jpeg&from=appmsg)

Apple announces the M5 Ultra Mac Studio with up to 512GB of RAM | Macworld

同样几万元预算，普通 PC 用户可能还在研究怎么把模型塞进 24GB 或 32GB 显存，一台高配 Mac 已经能够直接加载几十亿、几百亿，甚至部分上千亿参数的量化模型。

此外，苹果 MLX 还原生围绕 Apple Silicon 和统一内存设计，LM Studio、Ollama 等主流本地模型工具也已经完整支持 Mac。

近两年大量开发者和论文都在围多模态推理以及 Apple GPU 优化做探索，MacBook 甚至可以在电池供电状态下持续运行本地 LLM。

![MacBook Pro - Apple (香港)](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfI9Cia6GNCuSXiaJJaaRgeHqWjApBicJltZ5RvI8DibFx4A6XmspxrVzeuxwo46RHl43TpR5ON6uiabFW2afKaHfMzPmgNRb2fQTAdA/640?wx_fmt=png&from=appmsg)

MacBook Pro - Apple (香港)

基于此，桌面 Mac 的价值因此变得有些微妙。

过去买 Mac mini，考虑的是办公、编程、影音和轻量创作；今天买一台大内存 Mac mini，很可能顺便就多了一台能够 24 小时挂着跑 Agent 的本地 AI 节点。

苹果还在进一步放大这个优势。

EXO Labs 等开源项目已经可以把多台 Mac 联成集群，通过多机协同运行单台设备装不下的大模型。苹果自己也在今年 WWDC 特别活动上演示过通过多台 Mac Studio 运行超大模型。

一台 Mac 放桌上是电脑，几十台 Mac 塞进机房以后，那就已经越来越像小型 AI 集群了。

英伟达显然也看见了这个变化。

据内部人士透露，英伟达已经开始把苹果视为端侧和本地 AI 市场头号竞争对手，去年年底推出的 DGX Spark，就是一个很明显的信号。

![NVIDIA DGX Spark: great hardware, early days for the ecosystem](https://mmbiz.qpic.cn/mmbiz_jpg/dCG7OC48IfKPRNmnlWX91rOhlT9jwL6iatns0mXhTUQIHicu9rMclY5tQYeaiaFsNibXXfdJ4KZ300jUh2ULdasChMAIMyNMVtZ66lL2njp82qE/640?wx_fmt=jpeg&from=appmsg)

NVIDIA DGX Spark: great hardware, early days for the ecosystem

英伟达把原本属于数据中心的 AI 计算能力塞进了一台桌面小主机，从方盒子造型到体积，都很容易让人联想到 Mac mini。产品定位也不言而喻：让开发者在桌面上拥有一台可以本地运行大模型的 AI 机器。

不过，问题在于，好不容易站上 AI 风口的苹果，很快又碰到了另一个麻烦：内存缺货。

全球 AI 数据中心正在争抢 DRAM 和 NAND，内存供应持续紧张，IDC 甚至预计部分存储和内存供需压力可能延续到 2027 年乃至 2028 年。

Mac 恰好又是一个极其依赖大容量内存的产品。

高配 Mac mini 和 Mac Studio 很快开始出现漫长交付周期，大内存版本尤其抢手。有企业等不到货，只能转向现货更充足的 DGX Spark 等替代方案。

面对爆棚的需求与居高不下的成本，苹果顺势掏出了 Mac 幅度较大的一套涨价组合拳：

M4 Mac mini 刚发布时，16GB+256GB 国行价格只有 4499 元。到了 2026 年 6 月，256GB 版本的官方价格同样变成 5999 元，相比 M4 首发时足足贵了 1500 元。

8 月 25 日，新款 M6 Mac mini 正式发布。

M6 采用台积电 2nm 工艺，每个 GPU 核心加入独立神经网络加速能力，AI 性能相比 M4 大幅提升，但 16GB+256GB 起售价也进一步来到 6999 元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfJ4IWwDYcG7ElWbzU1zjkaaAqFzzwSWaYUfzzNicU3NbL72UZtxOF0Ypribtiaetjx8ibXQEzP8yMSKVjfHBI8SYFTAqO9ggw7mP7s/640?wx_fmt=png&from=appmsg)

短短两年，Mac mini 已经从苹果生态里最亲民的小主机，逐渐变成一台价格越来越像生产工具、高门槛的 AI 生产力硬通货。

得益于 Mac 的优异表现，市场也甚至因此催生了一系列过去难以想象的骚操作。

前 OpenAI 算力架构员工 Peter Voell 创立的 Mount Thor，正在机房里部署大量 Mac，专门提供基于 Apple Silicon 的 AI 云服务。

包括前不久，为 AI 编程 Agent 提供云端开发环境的 Namespace Labs 也在 X 上发布了一段机房扩容视频。视频中的工作人员正在成批拆箱 Mac，然后一台接一台塞进服务器机柜。

更抽象的是，由于 Mac mini 和 Mac Studio 实在缺货得厉害，为了满足 GitHub Actions、Xcode 编译以及 AI Coding Agent 对完整 macOS 环境的需求，Namespace Labs 甚至直接把带屏幕、带键盘、带电池的 MacBook Pro 都装进机架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfJsEqpApnria7G7gyNmNjyMNFXTVRmtQJUG4ghdtIcKZ9xyTr7pJ48plFwOfNX62iaEWHDlC7OW5pvfovyVEYLUY8hdsOTZksLO4/640?wx_fmt=png&from=appmsg)

冷知识，苹果也曾大规模涉足企业服务器市场，

2002 年到 2011 年，苹果曾经销售 Xserve 服务器；后来随着服务器业务退出，苹果逐渐把重心转回消费电子。如今苹果自研芯片服务器主要服务于 Private Cloud Compute 等内部云基础设施，并不单独向外销售。

不管是 Mount Thor 还是被逼到用笔记本搭机房的 Namespace Labs，在风口上的 Mac 还是在 2026 年以一种近乎野蛮生长的方式，重新杀回了全球企业级机房的核心舞台。

至于那些当年还在犹豫要不要入手的等等党们……现在默默看了一眼连二手平台都跟着全面涨价的 Mac mini，整个人已经两眼一黑了。

我们正在招募伙伴

**📮 简历投递邮箱** hr@ifanr.com

**✉️ 邮件标题** 「姓名+岗位名称」（请随简历附上项目/作品或相关链接）

[更多岗位信息请点击这里🔗](https://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2652396877&idx=2&sn=dfef25453a6bf0dca147b0adca3deaf7&scene=21#wechat_redirect)

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/dCG7OC48IfJEkBSvibnp043w2NhQZzwDQQKb8MRnJcsjIOL5paicbJC9wW94ZbIH2zsx0fSTZJic0UkOTGrL5ksP97Mda498JK6U0kKj37ARg8/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过