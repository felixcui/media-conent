# 刚刚，Gemini 4 Neon 突袭发布，性价比一夜斩杀 Opus 5.5

**作者**: 发现明日产品的

**来源**: https://mp.weixin.qq.com/s/8e62WZwF7ASzlBtylYs9ew

---

## 摘要

谷歌在《GTA 6》上线次日突袭发布 Gemini 4 Neon，当天全量上线 AI Studio、Gemini App、企业 API 和 Antigravity 编程环境，定位是卡在 Hydrogen 与 Carbon 之间、对标 Opus 5.5 和 GPT-6.2 Sol 的性价比主力。价格每百万输入 3 美元（缓存 0.15）、输出 15 美元，标配 100 万上下文；AA 智商指数 61 分（对手 59、57），CursorBench 65.4%，自家 Antigravity 下 SWE-sweep 39.0%，256K 到 1M 超长上下文检索的 GraphWalks 拿到 95.2%（Opus 66.8%、Sol 80.1%）。短板在 Terminal-bench 4.1 与 FrontierCode 2.0 仍被 Opus 微弱领先，密集图表阅读输给 Sol。另有两点值得记：Terminal-Bench 4.0 作弊率压到 0.0%，内部防偷懒测试走捷径比例 2.45%；Glean 评价它用 3 倍于 Carbon 的速度、60% 的成本交付同等质量，综合单任务开销比顶尖竞品低 50%–80%。

---

## 正文

发现明日产品的 发现明日产品的

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfL5Ldd7zggByL2BfHJ1AjKOSf6pf2O0g0Emm4ma322fRP50ZhahX96cO6a0ZzPcXpdVeQgAnMrFYY7wibqiboX3gJhQXoZJy8ptA/640?wx_fmt=gif&from=appmsg)

不得不佩服 Gemini 挑日子发新闻的勇气，昨晚《GTA 6》刚解锁上线把全球互联网热搜屠了个干净，劈柴老哥今天依然顶着漫天游戏贴，硬生生从元素周期表里又掏出了一款新模型。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfIiaoFfONibGnyyOVtwFoT1YQYxEI2H50aia79udUicicia5cZDQNHEVfbRrbthuUiaviaMict486D4fkFxbBibAiaxPBGXHQaia3GibibPIShmo/640?wx_fmt=png&from=appmsg)

就在刚刚，距离上一款旗舰模型 Gemini 4 Carbon 发布才过去三周，谷歌反手端出了全新的主力大模型 Gemini 4 Neon，也就是化学元素周期表里的第 10 号稀有气体「氖」。

最让开发者松了一口气的是，谷歌这次没有再搞排队申请那套期货玩法，发布当天就同步在 Google AI Studio、Gemini App、企业端 API 以及自家的编程环境 Google Antigravity 里全量现货上线。

先给大伙划个省流重点。

如果说三周前的 Carbon 是用来冲击超长程复杂任务的扛把子模型，那么今天登场的 Neon，就是谷歌真正派出来跟 Claude Opus 5.5 和 GPT-6.2 Sol 贴身肉搏的走量性价比主力。

它不仅在 Artificial Analysis 综合智商榜上拿下了 61 分的高分，定价还直接压到了每百万输入 Token 3 美元（缓存输入低至 0.15 美元）、输出 15 美元，同时标配 100 万上下文窗口。

连 R 星都知道按时交货了，谷歌自然也不好意思再发期货了。

### Gemini 4 家族排座次，Neon 凭什么坐上 C 位

聊模型能力之前，不得不先吐槽一下谷歌现在这门让人眼花缭乱的化学命名学。以前大模型起名，大家顶多在 Pro、Max、Ultra 和 Flash 之间排列组合，虽然俗套，但用户一眼就能看明白谁强谁弱。

现在，ChatGPT 是天文系，Claude 是文学 / 诗歌文体系，而到了 Gemini 4 世代，谷歌干脆一头扎进了元素周期表，先后掏出了1号「氢」Hydrogen、18号「氩」Argon、6号「碳」Carbon，以及今天的10号「氖」Neon。

属实是集齐数理化文科综合卷了。

连 Google DeepMind 自家的研究员姚顺宇今天都在 X 上调侃，说用化学元素当代号简直是个天才主意，每次代号泄露的时候，看着网友们一头雾水、完全搞不清这模型到底是哪个档位、该跟谁对标，实在太有意思了。

为了防止大伙彻底看晕，谷歌这次终于在官方图谱里把 Gemini 4 家族的排座次给交代清楚了。

从官方公布的家族定位表来看，主力梯队被切成了清晰的左中右三档。

最右侧的 Hydrogen 主攻日常高频编程与轻量 Agent 工作流，AA 智商指数 54 分，每百万输入和输出只要 1.5 美元和 7.5 美元，面向所有人开放。

最左侧的 Carbon 专啃最硬的超长程大项目与深度研究，AA 智商指数 60 分，标准定价是每百万输入 4 美元、输出 20 美元（11 月 30 日前促销价为 2 美元和 10 美元），主要面向高阶的 Ultra 订阅用户。

而今天发布的 Neon 正好卡在正中间的黄金甜点位，主攻软件工程、知识工作与科学推理，Pro 和 Ultra 两档用户都能直接用。

有意思的是，因为 Neon 比 Carbon 多开放了一档名为「xhigh」的极限思考级别，它在 AA 智商指数上反而冲到了 61 分，以 1 分优势倒挂了自家老大哥 Carbon，但 3 美元输入、15 美元输出的日常定价却比 Carbon 标准价便宜了四分之一。

或许怕高价订阅的 Ultra 富哥们觉得心里不平衡，谷歌今天还顺手给符合资格的 Ultra 用户塞了个大彩蛋，正式开放了全新的 Project Genie 体验与世界模型 Genie 4。

用户不需要配什么顶级显卡，直接在浏览器里就能召唤 Project Genie 智能体生成并走进可交互的 3D 虚拟世界，甚至还能在社区画廊里直接二创别人的世界。

你要是还没来得及玩《GTA 6》，不妨也可以尝试在 Genie 4 里手搓一个赛博游乐场。

### 正面迎战 Claude 和 GPT，Neon 挑战两大宿敌

既然敢卡在家族 C 位出道，Neon 这次放出的成绩单自然也是冲着同行命门去的。

在官方晒出的全维度跑分大图里，谷歌直接把 Neon 和宿敌 Claude Opus 5.5、GPT-6.2 Sol 拉到同一张桌子上贴脸对比。整体看下来，三家算是互有胜负，但在长板领域 Neon 咬得极其凶狠。

在传统命令行与前沿代码子项（Terminal-bench 4.1 和 FrontierCode 2.0）上，Opus 5.5 依然保持着微弱领先；密集图表阅读（Chartography）则是 GPT-6.2 Sol 小胜一筹。

但只要切到综合智商（AA Index 61 分 vs 59 分 vs 57 分）、Agent 编程（CursorBench 65.4%，在自家 Antigravity 框架下 SWE-sweep 更是直接飙到 39.0%）、数学科学推理以及网络安全漏洞挖掘，Neon 的优势已经相当明显。

最夸张的是考察 256K 到 1M 超长上下文检索的 GraphWalks 测试，Neon 直接跑出了 95.2% 的成绩，把 Opus 5.5 的 66.8% 和 GPT-6.2 Sol 的 80.1% 甩开了一个身位。

为了证明这款模型在工程上真能干重活，谷歌官方用 Antigravity 跑出来的四个演示 Demo，脑洞也是相当清奇。

比如用 Blender 建了个带本生灯和高压放电管的 3D 化学实验室来玩自家模型的名字梗。

再比如根据档案照片 1 比 1 还原图灵 1936 年在剑桥国王学院的 3D 书房，甚至还能从零编写 10200 行自定义 Shader 代码，开发一款采用 120Hz 物理模拟的 WebGL2 勃朗峰滑雪游戏，连动态雪痕、雪崩与空间音频都做了进去。

而最有趣的，莫过于谷歌让一群 Neon 智能体把一张静态照片转成了 10 万个单元格的 Google 表格。

在不插一张图、不写一行脚本代码的前提下，AI 愣是纯靠 50 多万条实时表格函数公式，在表格里跑通了边缘检测、3D 深度映射和六种交互打光模式，堪比拿 Excel 表格当 3D 显卡使。

### Neon 杀进编程战场，最有杀伤力的是价格

因为这次给的是现货，不少网友已经提前或正式玩上了。

AI 博主 Chubby 拿着 Neon 在 Antigravity 里泡了一天，一口气生成了 17 个涵盖射击游戏和 3D 世界的交互 Demo。

在测试一款叫作《Terra Breaker》的可破坏体素竞技场时，他原本只要求写个破坏和重置功能，结果 Neon 主动给他补齐了三种建筑和三种破坏工具，大炮轰下去能炸飞一大片方块，凿子敲下去只掉几个碎块，浏览器里稳稳跑满 60 帧。

而在另一个开喷气式飞机穿越日落峡谷障碍的游戏里，Neon 甚至在没人要求的情况下，顺手给飞机多写了一套自动驾驶演示模式。

不光不偷懒抄近道，甚至还会主动给自己加戏。

这也印证了谷歌在安全报告里提到的一个细节，Neon 在 Terminal-Bench 4.0 里的作弊率被死死按在了 0.0%，在内部编程防偷懒测试里走捷径的比例也降到了 2.45% 的历史最低值。

至于大家最关心的跟宿敌 Claude Opus 5.5 实测到底谁更强，博主 JAZII 做了一把非常直观的同题对决。

在两边都开启最高推理档位的情况下，Neon 跑完任务花了 20 分钟，账单是 3.5 美元；而 Opus 5.5 花了 18 分钟，账单高达 7.2 美元。

最后的体感很清晰，Opus 5.5 在极限上限上依然是那个略胜一筹的标杆，但 Neon 交出了整个 Gemini 4 家族迄今最细腻的输出，而且单次任务成本直接砍掉了一半以上。

正如 AI 科技企业 Glean 所评价的那样，Neon 能用 3 倍于 Carbon 的速度和 60% 的成本交付同等质量的结果，综合单任务开销比市面上的顶尖竞品低了 50% 到 80%。

更有意思的是谷歌出牌的时机。

眼下正值 Anthropic 紧锣密鼓筹备 IPO 上市的关键窗口，OpenAI 和谷歌这两天却默契十足地轮番出手，一个赛一个地往程序员和企业级工作流腹地里砸低价主力模型，很难说没有顺手给老对手上点眼药、捅上一刀的心思。

资本市场的钟声响起之后，恐怕还会更加热闹。

不过对咱们天天跟代码和表格死磕的打工人来说，神仙打架总归是件好事，只要大厂肯把顶尖现货模型按半价往外卷，大伙自然乐得一边用 Neon 省下算力钱，一边早点下班回家接着肝《GTA 6》。

而照谷歌发布模型的速度，留给他们好记的化学元素真不多了。

![](https://mmbiz.qpic.cn/mmbiz_png/dyDu14T9ZVCMpmmQUzxgYVqPjGyzRU49mvp2GS3ECuaLRaDxvG8jX157sFWmNY29qmhqJiakbKZtrQ0ukV3kThg/640?wx_fmt=png)

我们正在招募伙伴

**📮 简历投递邮箱**

hr@ifanr.com

**✉️ 邮件标题**

「姓名+岗位名称」（请随简历附上项目/作品或相关链接）

[更多岗位信息请点击这里🔗](https://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2652396877&idx=2&sn=dfef25453a6bf0dca147b0adca3deaf7&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dCG7OC48IfIcfAB5J4PL4LPia6HAk0VZqxhrhGUI6YhCyCLA8qibTMNpXW9odNmQpe3aiaOoEmReUbc1AyjwBUE8kFbIcsKJKtTWo6gURQ1SFg/640?wx_fmt=jpeg&from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过