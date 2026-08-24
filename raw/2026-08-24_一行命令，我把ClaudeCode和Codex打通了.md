# 一行命令，我把 Claude Code 和 Codex 打通了

**作者**: GaKi

**来源**: https://mp.weixin.qq.com/s/7QCb1s6a77HMyOZ21j7UKg

---

## 摘要

本文介绍了国产初创团队MemoraX推出的MemoraX Code工具，它通过将长期记忆深度嵌入Coding Agent工作流，以一行命令安装并作为轻量级Skill运行，解决了在Codex与Claude Code等Agent切换时上下文无法共享的痛点。该工具在AML评测中获商业产品组第一，实际测试中能有效保留关键记忆，提升开发效率。

---

## 正文

GaKi GaKi

在小说阅读器读本章

去阅读

**关于无缝衔接 Claude Code 和 Codex 这件事。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/a16Y4PLxPqlpUcXX8K5rYhEoQr2OEHEPZwbibtPjgicWANtL2fnR6NO6YBXFAwn8IRdyxUibuzicEMHkVdOic36OOKjmuHbib4YEibbicZkmoZibbyOM/640?from=appmsg)

👦🏻 作者: GaKi

🥷 编辑: Koji

🧑🎨 排版: NCon

过去一年，Agent Memory 已经从一个偏学术的概念演变成了一条独立赛道。Mem0 在 GitHub 上已经有 4.8 万星，拿了 2400 万美元融资，做操作系统式记忆分层的 Letta 完成了同样规模的 A 轮。

身后还紧跟着 Zep、LangMem、Cognee 等一众玩家。

**短短一年时间，「如何让 Agent 拥有长期 Memory」，已经成为所有 Agent 开发者绕不开的必答题。**

在这场 Memory Infra 的竞争中，出现了一个国产团队新面孔。

在今年 7 月底由清北等高校与研究机构联合发起的 AML（Agent Memory Leaderboard）评测中，商业产品组的第一名被一个成立不到半年的初创公司拿下 —— **MemoraX** **[Agent Memory 走到十字路口：技术路线、评测方法与 AML 首榜》](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649110650&idx=1&sn=d82e16bee45a6e18576bdd3945e3cd2f&scene=21#wechat_redirect)** 一文中，详细介绍过其技术路线。

与纯通用 Memory 框架有些许不同， **该团队最近推出的 MemoraX Code 选择将长期 Memory 深度嵌入 Coding Agent 工作流，在会话关闭、上下文压缩及多 Agent 协同时，保留「关键 Memory」。**

🚥

MemoraX Code 的这一方法在做本地的 Vibe Coding 开发项目时，价值很明显。

比如，我们一般习惯先用 Codex 搭配 GPT 5.6 Terra 这个比较经济实惠的模型，快速把骨架搭建出来，再转给 Claude Fable 5 审查、规划。但转换 Agent 的过程中，上下文无法共享，让Agent直接读源码是很费 Token 又容易丢失关键信息的。

为了验证 MemoraX Code 能否缓解这个痛点，我们找了一个真实开发场景做实测：

**使用 MemoraX Code 配合 Codex 和 Claude Code 协同工作，完整迭代了一轮此前开发的「实时语音聊天 → 社交平台推文」App。**

在这个开发过程中，我们或许能理解 Memora X Code 的实际价值。

「轻量化」的 Memory Skill

这回我们拿来实测的，是团队里其他同学此前 Vibe Coding 并长期在用的一款「 **AI 语音采访与内容生成** 」工具。

它的核心逻辑其实很简单：

**按住快捷键说话，通过本地 Whisper 或豆包语音 API 完成实时转录；接着由 DeepSeek 根据我的回答逐句追问、模拟语音采访；最后将整场对谈的内容提炼成适合微博、朋友圈或小红书的图文草稿。**

但这个项目一开始做得比较粗糙，这回正好用 MemoraX Code 这个为 Agent 提供记忆层的工具，看看它在改善整个开发工作流的过程中，能带来什么样的价值。

MemoraX Code 的安装非常简单，只需要下面这一行命令：

**npm install -g @memorax/memorax-code --foreground-scripts**

输入到 Claude Code 或 Codex 里即可，它会自动完成安装。

安装完成后，日常调用它的方式是 Skill，不需要像其他一些方法那样单独下载应用或再装一层 Harness。当你执行 Memory 相关任务时，Agent 会自动运行这个 Skill，非常轻便。

如何无缝衔接 Claude Code + Codex？

当我们在日常主力开发 Agent （比如 Codex）将项目的骨架搭建完成后，如果要转到 Claude Code，用 Fable 5 讨论下一步、看看整个骨架有什么问题，MemoraX Code 的用处就出现了，而且非常大。

因为我在搭建骨架时经历了多轮对话，整个上下文已经很长，也经历过上下文压缩。这时如果让 Claude Code 里的 Fable 5 直接读整个项目的上下文，非常消耗 token，Claude 的 Max 订阅额度可能也不太够用。

另外，这么长的上下文读下来，Fable 5 效率低，太长的上下文它也未必处理得好。

MemoraX Code 会在日常开发中，直接从 Claude Code、Codex 这些 Agent 的开发过程里提取关键 Memory，等于已经对 Memory 做过一次精简。

所以这时可以直接在 Claude Code 里对它说「我们继续 Codex 里刚刚关于这个语音项目的讨论吧」，它会直接调用 MemoraX Code 的 Skill：

MemoraX Code 也有一个网站，会记录你日常开发中整个 Agent 工作时的 Memory，按条按 ID 储存。

里面所有开发时的日常信息都经过一轮一轮的精简，会自动储存为一个个 Project，每个 Project 里有 Memory Summary 或一些 Facts。

这个 Skill 本身的规范还明确要求，把 MemoraX Code 的 Memory 当作假设，用当前代码作验证，而且验证不做全部上下文的扫描。

这样既保证了 Memory 使用时的效率，也保证了质量。

创建 Repo Memory

开发这个项目时，我们肯定会有很多 issue、PR、commit。这时可以直接让 Agent 使用 MemoraX Code 技能，帮我们构建 Repo Memory，拉取最近的 issue、PR 和 commit。

这个 Repo Memory 就自动构建完成了，里面有所有相关记录，比如搭建本地语音聊天与 DeepSeek 调用骨架的一些 commit。

我们在 Codex 里开发时，还可以让它直接回顾整个 Repo Memory 最近的 issue。

这些 issue 是我一开始用 Claude Code 做的，现在可以直接用 Codex 去问，因为这两个 Agent 已经通过 MemoraX Code 打通了。

日常开发时还可以直接让你的主力开发 Agent 使用 MemoraX Code 技能，帮你记住这次的代码开发经验，做一个项目级的开发 Memory 库。

比如我在 Codex 里建立了这个项目级的开发 Memory 库后，可以直接新建一个会话，甚至可以进入 Claude Code 新开一个对话，让 MemoraX Code 直接回忆这些开发经验，看看还有哪些按优先级从 P0 到 P10 排列的建议。

因为 Memory 可以跨 Agent 调用，这样就实现了用 Codex Terra 这个性价比比较均衡的模型快速搭建骨架，转到 Claude Code 的 Fable 5 做项目审查和下一步规划，最后再无缝转回 Codex，继续用 Terra，甚至用 Luna 去完成整个项目的开发。

回到这个 App 本身。

像现在我在实时语音互聊中说的所有内容，以及与 AI 互相采访的内容，都会自动存入我制作的这个 App 的记忆里，再通过 DeepSeek 转化为朋友圈、微博、小红书的稿件，帮我做头脑风暴。

整体来说， **MemoraX Code 在日常开发中可以通过一个中间的 Memory 层打通 Codex 和 Claude Code。**

Claude Fable 5 有最前沿的智能，适合做项目规划和审查。GPT 的 Terra、Luna 也比较优秀，适合作为子 Agent 或日常开发的主力模型。对普通开发者或 Vibe Coder 来说还有订阅额度的问题。

因为，你总希望把 Fable 5 留给真正关键的事情，日常开发用 GPT 的便宜模型。

**但实际上，两者之间的桥接非常麻烦，先用 GPT 做完一轮再让 Fable 5 审查，上下文消耗会很高。从 0 开始就用 Fable 5 做规划，效率也不高。所以很多开发者虽然知道两边模型各有所长，也不会去做这种协作开发。**

开发完一个小项目后，所有 Memory 都会保存到 MemoraX AI 平台这个云端，之后某些特定的开发经验会越来越方便复用，可以说是一个 Memory 的数据飞轮。

最终做出来的效果是这样的：

**点击左下侧的语音输入，会有一个动态的音波交互，随后它会调用我本地的 Whisper 模型或豆包语音 API 做转录，DeepSeek 理解完以后，再根据这些内容提问，我俩实现一种语音采访的效果，后续还可以加强为自动的双工对话。**

所有记忆会存入这个 App 内部，再转化成微博、小红书、朋友圈。

整体使用下来，你会感觉 MemoraX Code 确实比较轻便。

这种轻量感反映在日常开发中，就是调用起来比较容易。如果是 Claude Code 和 Codex 这样两个 Agent 穿插交替协作，整个 Memory 的交互接近实时，体感上和在同一个 Agent 里连续开发差别不大。

根据官方信息，我也做了一些技术性的了解，MemoraX Code 背后其实是一个双回路系统，分为两个部分。

上半部分是推理时的在线 Memory 流水线，下半部分是离线的 Memory 模型训练飞轮，两者通过 MemoraX Cloud 形成一个数据闭环。

下面拆开说说。

先说 **在线回路，也就是意图 → 记忆 → 执行。**

这个回路的入口是我们日常用自然语言让 Agent 做 Coding 任务，比如说「继续修复这一组相关 Bug」。入口这里会先经过一层 LLM 的意图理解，再去做检索，不会直接拿原文文本去检索。

其次，记忆部分由 MemoraX Local 和 MemoraX Cloud 两块组成。MemoraX Local 负责整个代码仓 Memory 的冷启动，比如一些关键入口、历史 PR 和 Issue、重要决策、当前实现等。

MemoraX Cloud 负责跨 Agent、跨端的动态沉淀，里面会有关于你的偏好、Procedure、Cross Session 经验、失败经验等。所以整个 Memory 层并不绑定某一个 Agent，属于一个与 Harness 无关的中间层。

整个方案里，Memory 不会全量灌入上下文，只会按需裁剪，做上下文精简，这是一个比较核心的点。

再说离线回路。除了前面说的数据闭环之外，另一个比较重要的部分是它的 Reward 设计。

训练时一共有三类奖励。首先是写入奖励，判断这条记忆该不该存储；然后是召回奖励，判断检索到的记忆对不对；最后是任务结果奖励，判断这条 Memory 是否真正促进了任务的成功。

整个底座是一整套 Agentic RL 训练基础设施，包括沙箱、Reward 计算、评测、分布式训练等。线上用户的使用轨迹还会反哺训练，所以用得越多，Memory 模型就越强，前面说的数据飞轮就是这么形成的。

🚥

Andrej Karpathy 在 2025 年 6 月提出「上下文工程」（Context Engineering）时，用过一个被反复引用的类比。

大致意思是：

**大模型好比 CPU，上下文窗口则是它的内存。**

顺着这个逻辑推导，Memory 系统本质上要解决的是操作系统层面的调度问题。比如，到底哪些信息该放进内存、哪些该被置换出去、哪些又值得写进磁盘长期留存。

而在今年 Sequoia AI Ascent 上，他又进一步提出「Agentic Engineering」这个概念，以此区分 「系统化 Coding」与随意的 Vibe Coding。也就是说，认真用 AI 写代码的关键是要做好需求设计、看懂代码改动、做测试和把关安全。

而这些深度工程环节，几乎全重度依赖 Agent Memory。

所以，这也正是 Agent Memory 的真正价值所在。

Agent Memory 这条路线上现在有很多尝试性的解决方案，有轻量方案，有开源框架，也有 MemoraX Code 这类国产团队的产品。

哪一种最后会成为标准答案仍未可知，但接下来的 1 年，这条赛道上应该还会出现更多这样的国产团队名字。

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过