# 刚刚，Anthropic 宣布弃用Git，统治编程20年的工具顶不住AI了

**作者**: 发现明日产品的

**来源**: https://mp.weixin.qq.com/s/PeC8nvufZ8r4BXBpUktNbA

---

## 摘要

Anthropic因Claude生成代码速度过快导致Git版本控制系统成为瓶颈，其内部代码合并量四个月内暴涨12倍至日均3万次，传统Git的去中心化设计无法承载AI时代的高频操作，因此组建7人团队用Claude耗时5个月从零打造了全新代码版本控制系统并完成仓库迁移。

---

## 正文

发现明日产品的 发现明日产品的

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfIJwqdt61xsdHhESWkV0VwbLfmjqPuBibsKJVPevgC3zeE3T3YiaTefMe6827tbVQNvVBjsoSddJQzcXRibQ9MdvtrE3H4hJa72AE/640?wx_fmt=gif&from=appmsg)

在 AI 圈，几乎所有人都在讨论 AI 什么取代我，取代数学家、设计师、经济学家，但被「杀死」最多次的一定是程序员。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfIoe46s3IhjMftyfFBlvSk7bBuxZeRpFbmG0tic8iavibYWZgibJfueOG4FekjZBHgeNFFIo6I4AEXf6m4YcIDb40WzEg7SO8MWLjg/640?wx_fmt=png&from=appmsg)

Anthropic 给出了一个谁都没料到的答案：在 *程序员* 被取代之前，先替换掉是程序员用了二十年的工具。

由于 Claude 写代码的速度实在太快，在 Anthropic 内部真正的瓶颈反而是人类过去几十年发明的软件工具，它们已经开始处理不了 AI 7x24 生产力的代码。

图｜https://www.anthropic.com/engineering/redesigning-source-control

没办法，Anthropic 用一个 7 人团队，还是用 Claude，用 5 个月的时间，从零打造了一套全新的代码版本控制系统，把整个大仓库迁过去。

### 平均每 3 秒合入一次代码

所以，过去几个月里，Anthropic 内部究竟产生了多少代码。

今年 5 月，Anthropic 整个公司平均每天合并（Merge，即代码通过审核正式入库）的代码变更大约是 2500 次，这完全是一家大型科技公司相当活跃的水平。

但到了今年 9 月，短短四个月后，这个数字暴涨了 12 倍，达到了每天 30000 次。

图｜2026 年 1 月至 9 月，每天合并到 Anthropic 单体仓库的更改。

如果换算成时间，意味着 24 小时不间断，平均每 2.8 秒，就有一段经过测试和审查的新代码被放进 Anthropic 的核心代码库里。

更可怕的是 「我们预计这种增长速度短期内根本不会放缓。内部对合并代码的潜在需求几乎是无限的，我们每扫除一个基础设施瓶颈，代码产量就会立刻迎来下一波暴涨。」

这套旧的代码版本控制系统到底怎么了。

### 统治编程界 20 年的 Git，接不住 AI

很多非技术背景但关注 AI 的朋友，可能经常听说 GitHub 上多少多少个 Star 的项目，GitHub 就是全球最大的开源社区，也是无数 AI 项目的发源地，Meta 的 Llama、DeepSeek 的开源模型，代码都托管在上面。

GitHub 里的「Git」，就是全球几千万程序员每天都在用的版本控制系统。

或者如果你让 Cursor、Claude Code、Codex 改代码，最后「提交」（commit）走的也是这套系统。

图｜类似这种 Diff 是 Git 常见的功能

如果把公司的代码库是一份所有人共同编辑的「超级在线文档」，那么 Git 就是底下的历史版本「时光机与管理员」。

它由 Linux 之父 Linus Torvalds 在 2005 年发明，负责记录谁在哪一秒改了哪一行字，确保几千人同时修改不会互相覆盖，随时还能一键回退。

图｜git 会存储每个文件与初始版本的差异以及存储项目随时间改变的快照

在过去 21 年里，Git 是当之无愧的工业界绝对标准。它的底层基因里，写着一个属于 2005 年的假设：程序员可能在任何地方（主要是没有网络的地方）写代码。

为了让人在没网的飞机或咖啡馆里也能翻看历史记录、对比修改，Git 采用的是「去中心化」设计。每当我们要干活，它默认把整个代码库的所有历史（在 Anthropic，这个包接近 100 GB），完完整整地复印一份下载到你的电脑上。

这个设计在「人写代码」的时代堪称完美，直到 AI 开始写代码。Git 引以为傲的「离线可用、人人持有完整副本」，在这个场景下纯属浪费。

每天 2500 万次的 Checkout，即在不同的分支之间切换、恢复文件、创建新分支等，每一次都要去拉取庞大的代码包，如果不加特殊优化，每天会产生超过 600 PB 的数据流量，这相当于每天在公司内网里来回搬运 1.2 亿部 4K 高清电影。

为了让 Git 服务继续，Anthropic 巅峰时期在内部维护了数百台 Git 镜像服务器做分流。但因为每秒钟都有新代码合入，镜像同步的速度根本赶不上 Claude 写代码的速度。

Anthropic 也发现我们为什么要用一套为「断网人类」设计的系统，去服务一群「永远在线」的 AI 智能体？

### 为 AI 量身定制的 Scion

想通这一点后，Anthropic 决定不再给 Git 打补丁，直接重造轮子，推出了自研版本控制系统 Scion。

图｜Scion 中变更集的形状

既然 AI 智能体永远在线，那就没必要在本地存 100 GB 的历史记录。谁最后改了这一行？两个版本差在哪？Agent 直接发个 API 请求问服务器就行，甚至连代码文件都不用下载到本地。

现在的 Scion 支持「虚拟化 checkout」，AI 改哪个文件夹，就只拉取哪个文件夹；甚至只有当程序真正去读取某一行文件时，数据才会从内存缓存里流式传过去。

同时，Scion 砍掉了繁琐的本地打包和全局锁，AI 提交一次代码的耗时，只跟它改了多少行字有关，跟整个代码库有几百个 G 毫无关系。

图｜Scion 的 checkout 架构

相比之前那几百台支撑的 Git 镜像集群，Scion 消耗的 CPU 和内存规模降低 200 倍，各级缓存命中率超过 99%。

AI 和测试任务拉取代码要从几分钟缩短到了几秒钟。单单这一项提速，就帮整个公司的持续集成（CI）系统直接省下了 25% 的算力。

图｜2026 年 1 月至 9 月期间，Scion 和 Antique 代码库每周合并的更改。

### 造这个系统的，也是 AI

如果放在五年前，一家科技巨头想要替换掉底层的代码控制系统，还要顺带手重写代码审查平台，Anthropic 同步自研了名为 Antique 的审查工具、代码搜索和权限系统，这意味着什么？

当年 Google 搞内部的 Piper 系统，Meta 搞 Sapling 系统，无一不是动用了数十甚至上百人的顶级基础架构团队，耗费数年时间才完成迁移。

但在 Anthropic，整个项目的团队配置是：7 个工程师，5 个月。

秘诀自然又是 Claude 深度参与了开发，他们使用一个内部早期模型把工程师手写的数据迁移管道重写了一遍，最终做到了内存占用降到原来的 1/20，速度快了 4 倍。

图｜在原生 Scion 代码库上的性能提升

Anthropic 还在博客中说，这是一场奇妙的闭环：正是 Claude 强大的写代码能力把他们逼到了系统崩溃的绝境，也正是靠着 Claude 疯狂写代码，这 7 个人才能在 5 个月内造出这套高并发的分布式系统。

更有意思的是人的角色转变，未来人类顶尖工程师的真实工作状态会是怎么样呢。

这 7 位人类工程师既不用敲代码，也不是来审核 AI 写的代码，他们要搞清楚 AI 为什么要改动

他们发现，自己最常对 Claude 说的一个字，是「不」。

让 Claude 互相进行「对抗性代码审查」时，AI 往往会变得过于偏执，为了防范一些极小概率的假设性风险，写出过度复杂、过度工程化的代码。这时候，必须由人类架构师出手叫停，帮 AI 做减法。

Anthropic 表示，他们并不打算把 Scion 拿出来当商业软件卖，之所以把这套架构公开，是因为他们看到了不远处的未来。

当代码由成百上千个 Agent 在后台并行生成、测试、修复时，所有为「人类手速」设计的软件工程工具，从版本控制、代码审查，到测试流水线，全都会在瞬间成为创新的障碍。

Anthropic 最近已经发了太多「警告」，这次也不例外：随着 AI 编程工具在各行各业的渗透，其他公司也不需要等太久，大概在未来 6 到 12 个月内，就会撞上同一堵墙。

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

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过