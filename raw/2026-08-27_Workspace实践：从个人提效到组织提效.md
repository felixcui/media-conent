# Workspace 实践：从个人提效到组织提效

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/B7gALfJJRDr8dvOObfXLIA

---

## 摘要

个人提效并不等于组织提效，单纯提升个人能力无法解决团队交付瓶颈。当前团队面临三大卡点：个人经验难以低成本复制传播、跨角色背景对齐沟通成本极高导致流程阻塞、以及工具生态各自为政导致技能无法跨Agent共享。为解决这些问题，作者提出了“Workspace”这一面向Agent的组织资产基座，旨在打破工具壁垒，沉淀组织经验，从而实现从个人提效到组织整体提效的跨越。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 何雪源

导读

introduction

个人提效不等于组织提效。一个人变成「超级兵」并不能提升团队的需求交付数据。本文讲清三件卡在中间的事，以及我们用 Workspace 这个「面向 Agent 的组织资产基座」怎么解。

*全文 16884 字，预计阅读时间 9 分钟*

GEEK TALK

01

业务提效的困境

三类卡点挡在团队吞吐前面： ****个人经验难以复制、跨角色背景对齐成本高、工具生态各自为政**** 。

**三类卡点：卡在哪里，代价是什么**

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy46agBjoMZnfyOVdroMibvjcfZdRRQR55UehCOhYTdNVIfvpRYZdwfC4UxugNshIFZGDeohJXuxjWHf2sIwsnyQ3Wg3GEtU8p2U/640?wx_fmt=png&from=appmsg)

三个卡点的共同点：它们都不是「模型不够强」造成的，换更强的模型也不会消失。

**1.1 个人经验难以复制**

前几天我用 iCafe 的 skill 批量获取卡片信息时遇到 403 权限错误，但我是空间管理员，肯定是有权限的，研究了一会儿发现其实等几秒再执行就好了。找 iCafe 的值班同学确认过，真实原因是 ****后端的接口限流，跟权限没关系**** 。所以我在自己的 CLAUDE.md 里加了一条规则：

> 当 iCafe 返回 403 时做最多两次重试，分别 sleep 3 秒和 5 秒，如果依旧报错则按失败处理。

其他人遇到同样的报错，得把我走过的流程以及踩过的坑重走一遍，甚至可能真以为是权限不够，然后 Agent 就卡在那里不动了。

****问题****

这种经验如果分享出去是可以解决效率问题的，但 ****我要怎么把这个经验低成本传播给团队里其他人？****

**1.2 更高效的沟通方式**

我们现在一个需求从前到后需要开很多对齐会议：PRD 评审、代码设计评审、前后端接口对齐会、测试同学的 case list 评审。只要涉及角色之间的配合就得约人，约之前还得先准备一堆文档，开完会还可能得再改几版然后再对齐，还没开始干活，人已经疲了。

从有效信息交流上看这些会真正在做两件事：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy56mwKxP5loQbmtFmBjhNqFascsRp1KOc8ykEBicVMiayMWl0LnXWiaKkCcWYNE3z4IdmMpaoSJPAHB6U2GjAyMWuocCoWTaZvJO4/640?wx_fmt=png&from=appmsg)

整个需求交付过程中， ****背景对齐这一段是最难压缩的**** 。如果事事对齐，那会消耗大量时间同时成为流程运转的主要瓶颈，如果不对齐，那么方案是否清晰、决策是否合理这些无法引入对抗视角，最后交付产出可能不符合预期。

****问题****

多角色之间如何高效沟通协作？

**1.3 割裂的工具生态**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy64HavI0g6XE5MGwXB9WkibrN1u8aLLTL667TTaf2PFPlJSmm5xSYz2wus8y4u0oHPlicicsmFEkpAONicOzszYvxMdhkic2SnxHb0U/640?wx_fmt=png&from=appmsg)

结果就是一个人在 Claude 上做了一套非常好用的 skill 集合，其他人在 Comate、Codex 上没法用，或者效果很差。

****问题****

能不能构建一套 ****与具体 Harness / Agent 无关的基座**** ，让各个 harness / agent 都能运行在上边？

GEEK TALK

02

我们早期的探索与尝试

**2.1 第一版尝试：Devflow**

一开始我们基于 SDD 理念，在内部的 Agent 平台上搭建了一套研发工作流，叫 devflow。那会儿公司内部的 agent、skill、mcp 这些基建都还不太成熟，模型上下文普遍才 128k，openclaw 也才刚火起来。但这套东西到现在来看依旧有两个地方我觉得很有价值：

#### ✅ 厂内生态接得比较深

通过提示词让 Agent 知道 iCafe、iCode、知识库、iAPI 这些都是干啥的，它能自己去取需求、取接口契约、写完代码提评审，可以理解为一个百度 Native 的研发工作流。

#### ✅ 工作流框架的约束力

讨论、设计、编码、测试、评审修改、合入、整理文档，每个阶段都有硬门禁，必须先做完这一步才能做下一步。这是在大模型能力不稳定的情况下，让交付质量相对稳定产出的有效方式。

并且在那个时候，我们就已经初步有了构建Workspace的概念。

**2.2 个人跑的飞快，但团队没有跟上**

有了devflow之后，写代码基本就可以自动跑起来了，我可以用tmux同时开三到五个终端会话去聊问题、评审设计，然后让他自己去开发，这一套下来我个人的产出量确实涨了，但从整个团队看，需求交付的数据没什么改善。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5LYlLkRfxnb62KhVDC7J9uEN2qUcmwZCtmb4E47yrNXkuBlO2WUQAshdK5ickm8lA4HmBr4DwsFufSXDVpxC17Nl3xsKXiax0Ss/640?wx_fmt=png&from=appmsg)

纵向的短板决定交付周期，横向的断点决定经验能不能变成组织能力。两条路都不通，个人产出涨了也传导不到团队数据上。

**2.3 组织提效要解决的四件事**

1\. 团队资产怎么攒起来

意识到上下文对LLM的重要性后，团队第一步工作就是文档工程，而且得找到一个低成本把每个人脑子里的经验记下来的办法。低成本这三个字是关键，不然它一定会被本职工作挤掉。

2\. 攒起来的东西怎么流动

前人写的文档、报告、代码和经验，后人得能用上；新产生的信息、经验、设计决策也得能及时写回去。东西要用起来才能产生新的价值，所以要怎么让这些资产流动起来？

3\. 流程和角色职责变化

当AI对不同角色的生产效率提升出现了明显的差异后，角色关系就需要进行调整以适应这样的变化。

这件事往往连着角色的重新划分 —— 谁写测试、谁做评审、谁对质量负责，这些边界在 AI 进来之后都会挪位置。

4\. 交付质量要持续稳定

让AI自由发挥，可能这一次写出非常完美的逻辑，但下一次写出来的东西完全没法用；不同人、不同Harness、不同Workflow、不同的模型对交付结果的影响可能很大，而我们需要构建的是一个在一定范围内产出相对稳定可靠的结果。

---

当然这些问题不仅仅是我们遇到了，很多在推进组织提效的团队都遇到了这样的问题，在各自摸索了一段时间之后，我们探索出来的解法大同小异 —— Workspace ****！****

GEEK TALK

03

殊途同归的解法：Workspace

**3.1 Workspace 是什么**

它不是文档库，不是 skill 库，也不是把几个仓库放在一起。它解决的是 ****组织资产用什么形式组织、怎么流动**** 的问题，文档、skill、代码库都算在里面。它是 ****面向 Agent 的组织资产基座**** ，Agent 通过它了解业务、参与业务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4wMibosrFljTRrHLkqyNHWp5EqYU96msLnJ1iarOL5icGVbXQj2nbGhjmmhZzq8XjicFWSIfFPz4N8HEJ5WGTtNV7v9leX1gfOWoY/640?wx_fmt=png&from=appmsg)

简单来说，它会把团队的如流知识库、代码库、iCafe 空间、skill 都放到一个代码库下面。Agent 在这个库里能访问到所有业务资产，还能自行验证产出是否正确。也正是因此可能很多人会把Workspace和知识库、Skill、代码仓库这些概念混淆。

另外有一个很重要的实践经验： ****Workspace不存知识的快照或者备份，只存摘要和索引。**** 所以其实不是把外部的知识库、代码库以及卡片内容整理成文本存储到Workspace中，而是构建外部资产的索引，让Agent知道查询某个问题应该去哪些平台上获取，也就是说，我们固有的流程和方式都没变，依旧是在知识库写文档、iCafe记录任务，这也是Workspace能推广起来的重要原因， ****Workspace不直接改变你的工作模式**** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7bicsjtWNtPdTApky80ep62ibBmwM7jbibmlESKR66gfGl4cm8Fx0cickgMibPYPZDHVteAyqb8SMI6mnWIaryyzlYmootH5T2e7AM/640?wx_fmt=png&from=appmsg)

**3.2 一个俄罗斯方块游戏的Workspace示例**

以下通过一个网页版俄罗斯方块游戏的 Workspace 来演示一个最小Workspace的结构原理。

组织结构

```cs
tetris-workspace/├── README.md# 唯一源：workspace 组织 + Agent 规则├── AGENTS.md -> README.md├── CLAUDE.md -> README.md├── .claude/# 三端桥接，只放软链│   ├── skills -> ../skills│   └── agents -> ../agents├── .codex/        （同上）├── .comate/       （同上）├── agents/│   └── tetris-playtester.md# 一个自动运行游戏并检查问题的 agent├── docs/│   ├── README.md# 路由表，不放内容│   ├── INDEX.md# 资产索引，一行一条，供精确检索│   ├── LOG.md# 资产维护日志，四次迭代各一段│   ├── knowledge/# 俄罗斯方块游戏相关的知识和概念等│   │   ├── sources.md# 外部平台入口│   │   ├── tetris-rules.md# 概念：SRS 旋转、消行判定、锁延迟│   │   └── experience-wallkick.md# 经验：踢墙表为什么不能自己编│   └── activity/# 研发活动记录│       ├── 20260701-iter1-mvp.mdand
│       ├── 20260718-iter3-fix-rotate-through-wall.mdand
├── skills/│   ├── ku-doc-manage/│   ├── icafe-official/│   ├── icode/│   └── summarize/# 完整正文，闭环关键└── repos/    └── tetris-game/# 游戏代码库，通过 git submodule 引入
```

可以看到，这个 workspace 把 docs 分成了 ****知识（knowledge）**** 与 ****活动记录（activity）**** 两个子目录：知识层放游戏术语、规则、经验等长期有效的内容，活动层按时间记录了四次研发迭代。

另外通过软链把 agents 和 skills 适配给 Claude / Codex / Comate 等 harness， ****新增 agent 或 skill 时只需要改一个地方，解决了多种工具生态问题**** 。

几个重要文件

## 四个文件各自解决什么问题

### README.md —— 规则唯一源·三端共读

```markdown
# Tetris Workspace
这是一个用于演示 Workspace 结构的示例项目。业务对象是一个俄罗斯方块小游戏，从立项到四次迭代的完整历史都沉淀在这个库里。> 重要：\`AGENTS.md\` 与 \`CLAUDE.md\` 都是指向 \`README.md\` 的软链。**规则只在 \`README.md\` 维护**，不要改软链、不要把软链替换成副本、不要在软链目标之外另写一份规则。
## 目录结构
\`\`\`tetris-workspace/├── README.md                          # 唯一源：workspace 组织 + Agent 规则├── AGENTS.md -> README.md├── CLAUDE.md -> README.md├── .claude/                           # 三端桥接，只放软链│   ├── skills -> ../skills│   └── agents -> ../agents├── .codex/     （同上）├── .comate/    （同上）├── agents/│   └── tetris-playtester.md├── docs/│   ├── README.md                      # 路由表，不放内容│   ├── INDEX.md                       # 资产索引│   ├── LOG.md                         # 资产维护日志│   ├── knowledge/│   └── activity/├── skills/└── repos/    └── tetris-game/\`\`\`
## 查询信息先读 docs/README.md
任何信息查询一律先读 \`docs/README.md\`，它是 \`docs/\` 的唯一入口与路由表。**不要凭印象直接猜文件路径。**外部平台是权威源，\`docs/\` 只是索引层与本地沉淀层。卡片状态、知识库正文、代码提交记录都以外部平台的实时数据为准。
## 改代码之前先读 repos/tetris-game/AGENTS.md
\`repos/\` 下的仓库以 submodule 引入，在本 workspace 内只读。修改代码要进入源码仓库自身的 checkout，并遵循它的 \`AGENTS.md\`。
## 一次迭代怎么结束
每次迭代走完设计、开发、测试、合入之后，必须调用 \`summarize\` skill 收尾。它负责判断这次产生的东西该进 \`knowledge/\` 还是 \`activity/\`，并同步 \`INDEX.md\` 和 \`LOG.md\`。**写回不靠自觉，它是流程里的强制阶段。** 一次迭代没有 \`summarize\` 就不算结束。
## 分层规则
\`docs/\` 下只有两层，按内容**会怎样失效**划分，不按主题划分：| 层 | 目录 | 放什么 | 什么时候会失效 ||---|---|---|---|| 知识层 | \`docs/knowledge/\` | 概念定义、外部系统入口、带条件的经验判断 | 被新证据推翻时；此时要**回头改旧页**，不是另写一页 || 活动层 | \`docs/activity/\` | 每次迭代做了什么、怎么做的、验证结果 | 不失效，只增不改 |两层都放不下时**停下来问用户**，不要硬塞进最接近的目录。
```

## docs/README.md —— docs 的唯一入口·管路由

```markdown
# docs 查询入口
本文件是 \`docs/\` 的唯一查询入口，只描述信息怎么找，不承载动态状态，不复制外部平台内容。外部平台（iCafe 空间、如流知识库、iCode）是权威源，\`docs/\` 只是索引层与本地沉淀层。
## 外部源
- iCafe 空间：\`TETRIS-DEMO\`（卡片、迭代、Bug）- iCode 仓库：\`demo/tetris-game\`- 如流知识库：\`https://ku.example-int.com/space/tetris-demo\`
## 场景路由
| 我要查什么 | 去哪里 ||---|---|| 精确找某份资产 | \`INDEX.md\`，用 ripgrep 命中关键词 || 某个约定当初为什么这么定 | \`LOG.md\`，按日期倒着翻 || 游戏规则、旋转判定、消行判定 | \`knowledge/tetris-rules.md\` || 外部平台入口、取数方式 | \`knowledge/sources.md\` || 某个坑踩过没有、某个做法为什么被否掉 | \`knowledge/\` 下 \`experience-*.md\` || 某个功能是哪次迭代做的、怎么验证的 | \`activity/\`，文件名带日期与主题 || 代码在哪、怎么跑测试 | \`../repos/tetris/AGENTS.md\` |
## 写入规则
- 长期有效的东西进 \`knowledge/\`，做过的事进 \`activity/\`。- 旧知识被新证据推翻时**回头改那一页**，并在 \`LOG.md\` 记一条为什么改。不要另写一页新的留着两份矛盾的真相。- 每次写入都要同步 \`INDEX.md\` 一行和 \`LOG.md\` 一段。这由 \`summarize\` skill 负责，不靠人记。
```

## docs/INDEX.md —— 一行一条资产·供检索

```bash
# Workspace 资产索引
## Search Rule
1. 先读本文件，在资产表中找到对应资产；2. 读对应资产获取相关内容。签名列是内容摘要短哈希，用于判断本地缓存是否落后于权威源。
## 资产表
| 类型 | ID | 内容 | 签名 ||---|---|---|---|| 文件 | knowledge/tetris-rules.md | 俄罗斯方块规则：7 种方块、SRS 旋转、消行判定、锁延迟 | a3f19c || 文件 | knowledge/sources.md | 外部平台入口与取数方式：iCafe 空间、iCode 仓库、知识库 | 7b2e04 || 文件 | knowledge/experience-wallkick.md | 经验：踢墙表不能靠模型推导，必须取权威源 | c81d55 || 文件 | activity/20260701-iter1-mvp.md | 迭代一：MVP，方块下落与消行，能玩一局 | 2e90ab || 文件 | activity/20260710-iter2-hold-and-ghost.md | 迭代二：新增 Hold 暂存与 Ghost 落点预览 | 5fc731 || 文件 | activity/20260718-iter3-fix-rotate-through-wall.md | 迭代三：修复靠墙旋转穿墙，根因是踢墙表被编造 | 9d4e18 || 文件 | activity/20260725-iter4-score-and-difficulty.md | 迭代四：计分规则与难度曲线，playtester 取手感数据 | 6a07f2 || 代码 | repos/tetris/src/rotate.js | 旋转与踢墙实现，迭代三的修复落点 | f42b8e || 代码 | repos/tetris/test/rotate.test.js | 旋转回归测试，含迭代三新增的靠墙用例 | 1c6d93 || iCafe | TETRIS-DEMO#12 | Story：俄罗斯方块 MVP | - || iCafe | TETRIS-DEMO#31 | Bug：I 型方块贴右墙旋转后穿出边界 | - || Ku | https://ku.example-int.com/space/tetris-demo/design | 玩法设计文档，迭代一的输入 | 4b8f27 |
```

docs/LOG.md —— 按日期倒序变更日志·留依据

```markdown
# 资产维护日志
记录 \`docs/\` 与索引资产的变更。格式是 \`## YYYY-MM-DD\` 下挂条目，每条一句话说清改了什么、为什么。它的用处是半年后你还能搞清楚某个约定当初为什么这么定。
## 2026-07-25
- 新增 \`activity/20260725-iter4-score-and-difficulty.md\`  计分按 1/2/3/4 行给 100/300/500/800，难度按每 10 行提一档速度。  档位是 playtester 跑 20 局之后定的，不是拍的。- \`knowledge/sources.md\` 补一条：手感数据来自 playtester 输出的  \`artifacts/playtest-*.json\`，不是人工计时。
## 2026-07-18
- 新增 \`knowledge/experience-wallkick.md\`  迭代三根因：迭代一的踢墙表是模型按对称性推出来的，看着合理但与 SRS 不符。  结论是这类查表数据必须取权威源，不能推导。- **回头改了** \`knowledge/tetris-rules.md\` 的旋转小节  原文那张踢墙表整个是错的，替换为 SRS 标准表并注明来源。  这是本 workspace 第一次出现知识页被新证据推翻，保留这条记录作为范例。- 新增 \`activity/20260718-iter3-fix-rotate-through-wall.md\`
## 2026-07-10
- 新增 \`activity/20260710-iter2-hold-and-ghost.md\`  这次迭代**没有产生新的知识页**。Hold 与 Ghost 都是直接照设计文档实现，  没遇到需要判断的地方。不往 \`knowledge/\` 硬塞内容也是正常结果。
## 2026-07-01
- 建库。\`README.md\` 定下两层分法与 \`summarize\` 强制收尾规则。- 新增 \`knowledge/tetris-rules.md\`，从玩法设计文档提炼概念定义。- 新增 \`knowledge/sources.md\`，登记 iCafe 空间、iCode 仓库、知识库入口。- 新增 \`activity/20260701-iter1-mvp.md\`  MVP 范围定为下落、移动、旋转、消行、结束判定，不含计分。
```

最重要的一环：summarize skill

****Workspace 能不能越来越好用，关键就在于有没有这个 skill，以及这个 skill 设计得好不好。****

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6Tw0wuODcqDV7QRkAKfVdGC4SAb7KACGR50Bkb9tpMYaia30k4iaiaibJjc3n7l9rVtQNftj6riarbfT6BvKFDholaGs0qiaY5ibxMs0/640?wx_fmt=png&from=appmsg)

我们先来看这个 skill 的内容。

## skills/summarize/SKILL.md

```markdown
---name: summarizedescription: 把一次迭代产生的可复用内容写回 workspace。每次迭代收尾必须调用，是资产流动闭环的最后一环。用户说「收尾」「总结一下」「沉淀」，或一次迭代的开发、测试、合入都已完成时使用。---
# 迭代收尾写回
**这是 workspace 中最重要的 skill。** 前面几个 skill 负责查，这一个负责写回。没有写回，Agent 每次都从零开始，workspace 就退化成一个静态文档库。
## 前置条件
调用前确认这次迭代的开发、测试、合入都已完成。中途调用会写进未定型的结论，比不写更糟 —— 错的结论会被下次检索命中并当依据用。
## 自主原则
**默认自己决策，不问用户。** 写什么、放哪层、叫什么文件名、\`LOG.md\` 那句话怎么写，全部自行判断并直接落盘。用户已经在这次迭代里给过足够信息，收尾阶段再回头逐项确认，等于把成本从 Agent 转回人身上 —— 写回一旦变成一道需要人配合的手续，它就会被跳过，闭环也就断了。
判断不确定时按「先写下来，标明不确定」处理，不要为了求稳而不写。写进去的内容可以被下一次迭代修正，没写下来的东西下次就不存在了。
只有两种情况停下来问用户：
1. **要做的事违背 \`README.md\` 里的分层规则或本 skill 的边界** —— 比如内容两层都放不下、需要新建 \`docs/\` 一级目录、需要改分层规则本身。2. **要写进 knowledge 层的结论与用户在本次会话中明确表达的判断相冲突** —— 这种冲突不能由 Agent 单方面裁决。
除此之外一律自行决定。**分不清该进哪一层不是提问的理由**，按第 2 步的分流表判断；表里给不出唯一答案时进 activity 层，那里的内容不失效，代价最小。
## 步骤
### 1. 判断这次产生了什么
逐项过一遍，别凭印象：
- 有没有遇到需要判断的地方，判断依据是什么- 有没有踩坑，坑的触发条件是什么- 有没有推翻之前的某个结论- 有没有新的外部数据来源- 具体做了什么、怎么验证的
### 2. 分流
| 这次产生的东西 | 落点 ||---|---|| 客观事实、概念定义、规则 | \`docs/knowledge/\` 对应概念页 || 带条件的判断、踩过的坑 | \`docs/knowledge/experience-<主题>.md\` || 外部系统入口、取数方式 | \`docs/knowledge/sources.md\` || 这次做了什么、怎么验证的 | \`docs/activity/<日期>-<主题>.md\` || 本版实现的参数、阈值、数值 | **留在 activity 页**，不进 knowledge |
最后一条容易做错。参数会随下一次调整而变，进知识层会立刻过期，还会被当成规则引用。
**这次没有产生新知识是正常结果。** 照文档实现、没遇到判断的迭代，只写 activity 记录就够。往 knowledge 里硬塞内容会增加以后的检索噪声。
拿不准某条内容值不值得记时倾向于记下来 —— 一条略显多余的经验页只是噪声，一条丢掉的经验是下次重新踩一遍。但「值得记」不等于「必须进 knowledge」，拿不准就写进 activity。
两层都放不下时**停下来问用户**，不要硬塞进最接近的目录。这是自主原则的第一种例外。
### 3. 旧页被推翻时回头改原页
新证据推翻了某个知识页的内容，**改那一页**，不另开一页。
否则库里会同时存在两份矛盾的真相，下次检索命中哪一份是随机的。改完在 \`LOG.md\` 记一条为什么改。
活动层不改。历史记录里的错误决定原样保留，它是经验页的来源证据。
### 4. 同步索引与日志
- \`docs/INDEX.md\`：新增或修改的资产各一行，含类型、ID、一句话内容、签名- \`docs/LOG.md\`：在 \`## YYYY-MM-DD\` 下挂条目，每条一句话说清改了什么、为什么改
日志的用处是半年后还能搞清楚某个约定当初为什么这么定，所以「为什么」不能省。
### 5. 补双向引用
新页的 \`## Related Docs\` 指向相关页，同时**回到被指向的页补一条反向引用**。单向引用等于没引用 —— 从另一头进来的人找不到它。
## 完成标准
- [ ] 这次的判断依据与踩的坑都有落点，或已确认这次确实没有- [ ] 参数类数值留在 activity 页，没有混进 knowledge- [ ] 被推翻的旧页已改，不存在两份矛盾内容- [ ] \`INDEX.md\` 与 \`LOG.md\` 已同步，日志写了为什么- [ ] 双向引用成对- [ ] 全程没有为了确认落点、命名或措辞而打断用户
最后向用户报告时给结论，不给选项：列出写了哪几个文件、各写了什么、以及本次判断中不确定的地方。用户看完可以纠正，但不需要在写之前替 Agent 做决定。
## 边界
不新建 \`docs/\` 的一级目录，不改 \`README.md\` 里的分层规则。这两件事需要用户授权。
```

****这个 skill 的三条设计取舍****

1\. 强制执行

summarize 被设计为在会话的最后必须执行，用于把会话中的决策判断、踩坑经验、结论变更、新的外部源以及活动记录都写回 Workspace。写回不靠自觉。

2\. 尽可能不打扰用户

让 summarize 自动记录，再配合定期的资产治理来维护质量，而不是在收尾阶段频繁让用户判断哪些东西需要被记下来。减少人的决策，经验沉淀的成本才会更低。

3\. 宁多记不漏记

一条略显多余的经验页只是噪声，一条丢掉的经验是下次重新踩一遍。拿不准就写进不会失效的 activity 层。

---

但以上这些都不是钉死的规则 —— docs 下的组织结构、summarize 的具体内容，在不同的 Workspace 下都可能不一样，不同的业务下可能会进行微调。

GEEK TALK

04

基于 Workspace 的实践

**4.1 组织级 Workspace：RocketMQ Workspace**

这是我们核心的产品 Workspace，所有产品和业务相关的信息都可以在这上面查询。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy41qP5QGdLCicWzeBKPTux8ic8pPLTTUqxhHNfF8HTwO3ibMHq2kGmCkMT7oXqqO22uHO5sLle9lTDTX9oAYaHKzNh4C97maPUkvo/640?wx_fmt=png&from=appmsg)

## △ Workspace 底座：左侧平台输入，经 Agent + LLM 按构建约束落成结构化 Product Wiki，右侧支撑六类工作流能力

#### 文档组织结构

RocketMQ Workspace 的文档组织分为三层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6gc4nvKoGJ2OQqOhqYDpDOxQUricZ2ZibUc6CZcmOdnvWzJPwibyUajZMibbyoib0bqKLiaC0lNWK32pbVkHQibWEW8pYtlLM68zrVicE/640?wx_fmt=png&from=appmsg)

#### Skill：20个能力，六组覆盖完整链路

Workspace 下沉淀了 20 个 skill，按用途分为六组，覆盖从需求讨论、开发验收到排障、封线、资产沉淀的完整链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7krtvqnl4nPfHVEic1NRrPxsgW7ibDSQbuFkC1shibXltsfYTgfcQy2EnJvgar3NibbsJEU2rlDD2ibx1AnvEjY9oF65WOIKTnD3lM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4rJWZo3bf561FHzm8kpV22KvuGibBq5CM4O95o6r343lT0ZxU6V11VomnfuPrhicXibtCZN6DTBpUViaCxgwsY8BrQYF3hfPKb6IE/640?wx_fmt=png&from=appmsg)

#### Workflow：四阶段 Spec Driven Development

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7Zr7zic6eFSsqicUX1P1G69xaDBBZibsjlpksD6wNFTY6L0SHMVoj3wk7ewELficXiaMJk7Iba4UoaU3jtOyyf1wUYnB9cWb3afn4o/640?wx_fmt=png&from=appmsg)

在这个流程设计下，我们常见的几种研发活动流程是这样组织的：

🐞 Bug 修复

1. 客户反馈一个问题现象，在 Workspace 上打开新会话，把问题描述、截图输入进去并调用 diagnosing-bugs。它基于历史 bug 分析、现象描述、日志、代码以及社区 issues 定位原因，确认是产品 Bug 后调用 to-icafe-card，按规则创建卡片并写入已确定的信息；
2. 调用 spec-workflow <iCafe-ID>，以新建卡片为输入，走完方案设计、开发、验收、收尾四步，最终得到 Bug Fix 的 Patch 和一份完整交付报告。

✨ 新功能开发

打开一个新会话，调用 spec-workflow <iCafe-ID>，以 Story 卡片作为输入，执行方案设计、子卡片拆分、开发、验收和收尾，最终得到交付这个功能的多个 Patch 以及一份完整的功能交付报告。

#### 任务规约（Spec）模版设计

任务规约（Spec）的目的，是让 ****Agent 向人澄清它对这个任务的理解是否到位（PM 关注）、代码设计方案是否合理（RD 关注）、测试验收是否完善（QA 关注）**** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy46SZlVy3kXGuT9EI7YYgHJxCCB1e6QbljnhKnZjZwQoOmaS6WSOib4icX3rLTePUicX0XZfnzBs5GYt3Og5FZpT5hGwXSe0dVSZo/640?wx_fmt=png&from=appmsg)

一份 Spec 报告产出后，把它发给相关角色，或者拉一个评审会议进行评审。需要调整的地方记录下来，让 Agent 进行第二轮调整；所有问题都确认后，这份任务规约就可以交给 Agent 去实现。实现之后，Agent 会给出一份验收报告， ****验收报告的目的是让我们能通过报告中的数据，知晓Agent交付的结果有没有解决任务规约中的任务：****

下面是一份 ****脱敏后的示例**** 验收报告，业务对象换成了前文那个俄罗斯方块 Workspace，卡片号、评审号、分支名、环境标识均为虚构，字段结构与真实报告一致。

****① 基本信息与验收结论****

- 验收单元：DEMO-TETRIS-102（连续消除四行时动画掉帧）
- 验收方式：本地沙盒环境 + 自动化用例
- 执行时间：示例日 10:49 — 13:46
- 验收结论：共 5 项验收目标，5 项通过 / 0 项失败 / 0 项未覆盖

****② 操作时间线****

- 10:49　读取卡片与规格，确认执行边界
- 11:20　完成代码修改并提交本地分支
- 12:05　打包并部署到沙盒环境
- 13:10　执行自动化用例，产出测试报告
- 13:46　回写活动记录并提交

****③ 逐项验收结论与证据****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7d1QCPadUG04yOWyZd8yBQS0TnL0pnqtdD6FhMRcVo0NhgUcNzqUoSc4F7APor0l3GH3BQcS8XlYD4m9H9bfL28YZaaaua6jA/640?wx_fmt=png&from=appmsg)

****④ 交付产物与关联资产****

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7bqxHjx2m3Xyf4HxqItiaa0QIJqjS7gz466mm0IuTnqSdYLjfgNDByvgpHfcpkTmicHUIj6ianib94KjtwO75UMHbpMU05rA8ickibs/640?wx_fmt=png&from=appmsg)

#### AI提效的量化效果分析

RocketMQ在2026年2月份开始建设Workflow，然后在6月份开始建设Workspace，我们以 2026年2月引入AI 辅助研发为分界，对比前 17 个月（AI 前）与后 6 个月（AI 后）的产研提质增效。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5wf83qObfMg1FJJ3vZiatVSYXpv3wYkIdsxaS9HF9CKpFnhribBeX80abtIQvIENUnq2UJJJIOrw3SztxoUpHBHSYmKiafFdF7Xk/640?wx_fmt=png&from=appmsg)

#### 除了开发，在这个 Workspace 上还可以做些什么

Workspace 沉淀的资产和 skill 并不只服务于写代码。同一套底座上，这几类工作同样能跑起来：

****需求讨论与澄清****

基于业务模型层里的概念、行为与约束，和 Agent 讨论一个需求该不该做、边界划到哪里，直接产出可评审的规约草稿。

****问题排查与值班****

历史排查路径、常见根因、系统拓扑都在库里，新一次排查从上一次的终点开始，而不是从零复现。

****版本封线与发版****

按封线清单核对卡片状态、代码合入情况与验收报告，汇总出这个版本改了什么、风险在哪。

****资产治理与体检****

定期检查互相矛盾的结论、孤儿页、失效索引，并把活动层里重复出现三次的坑提炼成一条经验。

**4.2 每个人都可以尝试：个人 Workspace**

Workspace 并不是组织专属，个人也可以搭建自己的 Workspace，把自己的 skill 和工作经验沉淀下来。我平时有不少调研和写作的需求，比如调研某个 Agent 产品、学习 ReAct，以及本次分享的稿件编写，所以我也在研究怎么让 AI 帮我更高效地干这些事儿，这个的出发点其实还是个人提效，但依旧可以基于 Workspace 来做。我基于公司工程效能团队推出的通用 Workspace 方案搭了个人 Workspace，并实现了调研和写作两个 Workflow。

个人 Workspace 是每个人都可以尝试的切入点：先以解决一个具体问题为目标（比如定时自动写周报），再逐步向 Workspace 补充内容、建设自己的 Skill 与 Prompt。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5ibYzD6keGn5lhuNPS840vNrM4XB8C0edOCSCgsSVKCOtxNkVU5AutXCofRXedaIuZhEPibIs4o0ibIB2nTrJXh5mTbR6cyXweYw/640?wx_fmt=png&from=appmsg)

包含哪些资产：

- 个人如流知识库
- 个人周报
- OKR
- 本地知识库
- 常用的Skill（调研、写作、学习新内容等）
- ......

可以做什么：

- 调研某个新概念或者产品
- 学习某个技术
- 把收集的材料以及自己的一些感悟写成文章发布到个人知识库
- 收集个人的每周活动记录自动写OKR周报
- ......

GEEK TALK

05

如何在自己的业务上尝试

对于不想过多折腾或者技术能力有限的团队，可以直接使用工程效能团队开发的 Roma Workspace；如果想要自己一步一步地去构建 Workspace、对 Workspace 有更深入的了解，那么参考以下步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6icJWyPkE7hVC8R82uvInkE87wXhAKCiakxrjPTdL3OvqCKIG0w5YK9icNbeX2aQA2aUP3b61wIDqqB7eUl4CRUxK3S98wsVGLWc/640?wx_fmt=png&from=appmsg)

第一步：初始化一个 Workspace

创建一个空仓库，clone 到本地，然后打开任意一个 agent，把文末 ****附录：Workspace 参考骨架与初始化 prompt**** 整节内容丢给它，让它按说明去初始化即可。这一步会构建基础结构，包括几个重要文件以及一个简单的 summarize skill。

第二步：确定一个你想解决的问题并给出解决问题的流程

比如服务在沙盒环境自动化部署，流程是：

第三步：在这个 Workspace 中实现流程

这一步你可能需要补充很多资产、Skill 和脚本，比如沙盒环境的部署文档、在沙盒环境执行命令的 skill、更新脚本和服务检查脚本。

第四步：逐步迭代和优化这个流程

在你的实际工作中使用这个流程，去发现和解决问题，然后用 summarize 记录下来。一开始可能会遇到很多情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy54rebl6uLv2kM37HPlyYfeenn3WjXejiaYZjfeYDlm6HIWbW4ppaxmJJ2LY9Pu6nB6eOUhsIfWWmAksbOtRCS56k4MMmKjhFJw/640?wx_fmt=png&from=appmsg)

经过几轮迭代调整后，你就可以得到一个稳定的 Workflow、结构清晰的资产结构以及多个常用的 skill。

一个健康的Workspace的三个特点：

- Workspace资产越来越厚，能做的事情越来越多
- 流程和产出越来越稳定
- 人的决策越来越集中并且准确

GEEK TALK

06

总结

Workspace是我们探索出来的一个可以有效推动并且解决组织级资产形成的路径，并且也看到很多团队也和我们一样有类似的想法，所以在6、7月份的时候TSC的同学把这些不同业务但有相同想法的同学的思路和想法做了整合推出了Roma Workspace，但不一定适合所有的团队，我之前也看到有些团队还会考虑Agent运行安全性问题，所以会把Workspace构建在一个镜像中，相关的工具、skill和资产都在docker中去组织，适合于执行环境相对特殊并且组织资产变动不那么频繁的业务。

不论是分层的资产组织还是Workflow的构建，本质上都是在 ****用结构化的上下文工程与流程去驾驭非结构化的AI能力**** ，从而产出质量相对稳定可靠并且能长期维护的资产。AI让编程的门槛变的很低，但从Vibe Coding到HarnsessEngineering还有很长的路要走，而我们工程师新的要求是能够去构建出这样一套能稳定交付并且可长期维护的Harness Engineering。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5JoO3zXe3HjcEqenqresTiabUgxtXXOluecXTayJiaDUPhEwxycLd8ceCxuft5UdwkYxyhwAucdW6OI6hgNcqVg9B438kya5cqU/640?wx_fmt=png&from=appmsg)

GEEK TALK

07

附录：Workspace 参考骨架与初始化 prompt

```perl
LLM Workspace
# 构建 Workspace一种让 Agent 持续参与业务、而不是每次从零开始的组织资产组织方式。
这是一份想法文件，设计上就是拿来直接粘给你的 Agent（Claude Code、Codex、Comate 等）。它的任务是把模式讲清楚，具体的目录名、页面格式和约定由 Agent 跟你一起长出来。文档中段给了一份可以直接照着建的最小骨架，末尾给了一段可以直接用的启动 prompt。
## 核心思想大多数人用 Agent 做业务开发是这样的。开一个会话，把需求文档链接、接口设计、代码规范、部署方式、集群标识一条条贴进去。中途发现它没遵循代码规范，再补一句「按 xxx 规范来」。任务结束，会话关掉，这些上下文全部消失。下一个任务从零开始，同样的信息再贴一遍。
Agent 每次都在重新发现同一批事实。没有任何东西被累积下来。
Workspace 的想法不一样。把业务资产收进一个代码库，Agent 在里面能查、能改、能验证，**并且每次任务结束把这次得出的东西写回去**。下一次任务开始时，上一次想清楚的判断、踩过的坑、定下的约定都还在。
跟几样容易混淆的东西对比一下。
||里面是什么|给谁读|能不能执行|谁来更新||-|-|-|-|-||团队知识库|文档|人|不能|人手动写||skill 集合|可执行能力|Agent|能，但不知道业务|人手动写||代码库|代码|人和 Agent|能编译能跑|靠提交||Workspace|文档 + 能力 + 代码 + 卡片 + 环境|主要给 Agent|能查、能改、能验证|每次任务结束由流程写回|
最后一列是关键差异。前三样都得有人专门去维护，Workspace 的维护是任务流程的一部分。人会因为维护负担超过收益而放弃一个知识库，这是知识库腐坏的常见原因，也是 Workspace 把写回做成强制阶段而不是良好习惯的原因。
比纯知识库多出来的三件事，值得单独说清。
**它可以执行。** Agent 不只是读文档，它能跑测试、起本地环境、查日志、部署到测试机。这决定了它能不能自己发现问题并收敛。一个只能读写文档的 Agent 永远需要人告诉它做对了没有。
**能力本身也是资产。** 重复三次以上的操作序列写成 skill 存进 Workspace，下次不用重新描述。文档沉淀的是「知道什么」，skill 沉淀的是「会做什么」。
**外部平台是权威源，Workspace 只存入口。** 卡片状态、知识库正文、代码提交都在各自的系统里，Workspace 记的是去哪里取、怎么取。把外部正文拷进来会立刻产生两份不一致的真相。
适用范围比研发交付宽。
* **研发交付**。需求到设计到开发到验证到交付报告，全流程在一个库里，产出统一。* **值班与排障**。历史工单、排查路径、集群拓扑、常见根因，让下一次排查从上一次的终点开始。* **个人工作**。自己负责的几个项目、常用仓库、反复用到的操作流程，一个人用的 Workspace 成本最低。* **任何需要 Agent 反复参与同一摊业务的场景**。判断标准是同样的上下文你有没有贴过第三遍。
## 五层结构一个 Workspace 由五层组成，各层的所有权和失效方式都不同。
**规则层** —— 根目录一个 \`README.md\`，说明这个 Workspace 怎么组织、Agent 该守什么规矩。\`AGENTS.md\` 和 \`CLAUDE.md\` 都做成指向它的软链，不同 Agent runtime 读到同一份说明，不用维护多份。这是最关键的一个文件，它决定 Agent 是一个守规矩的资产维护者还是一个普通聊天机器人。你和 Agent 一起把它养出来。
**知识层** —— \`docs/knowledge/\`。概念定义、外部系统入口、带条件的经验判断。Agent 写，你读。它会被新证据推翻，**推翻时要回头改原页，不是另写一页**。库里同时存在两份矛盾的真相，比只有一份过期内容更糟 —— 下次检索命中哪一份是随机的。
**活动层** —— \`docs/activity/\`。每次任务做了什么、怎么做的、验证结果。只增不改，不失效。历史记录里的错误决定要原样保留，它是经验页的来源证据。
**能力层** —— skill 和 subagent。一处定义，通过软链适配多个 Agent runtime。重复三次以上的操作序列往这里沉淀。
**源码层** —— 业务代码库，用 git submodule 引进来，在 Workspace 内只读。改代码进源码仓库自身的 checkout，遵循它自己的 \`AGENTS.md\`。多个仓库并列引入，Agent 就具备了跨仓工作的能力。
\`docs/\` 下就这两个目录，**不要再往下预设分类**。分层依据是内容**会怎样失效**，不是主题 —— 「iCafe 是什么」进知识层，「这次用 iCafe 建了 6 张卡片」进活动层，同一次任务里的这两句话属于不同层。本版实现的参数、阈值、具体数值也留在活动层，进知识层会立刻过期，还会被后来的人当成规则引用。按主题分（设计文档、会议记录、排障记录）在第三次任务时就会发现哪一类都能塞进两个目录。
页面怎么命名、要不要再开子目录、经验页写多细，这些都留给具体业务。规则定得越少，Agent 越不容易在边界上纠结，你也越不容易在半年后发现当初的分类不合适。真到某一层撑不住了再加，那时候你已经知道该按什么加。
## 最小骨架下面是一份可以直接照着建的结构。业务对象换成你自己的。
\`\`\`your-workspace/├── README.md                    # 规则层，唯一源├── AGENTS.md -> README.md├── CLAUDE.md -> README.md├── .claude/                     # 适配 Claude Code，只放软链│   ├── skills -> ../skills│   └── agents -> ../agents├── .codex/                      # 适配 Codex，同上├── .comate/                     # 适配 Comate，同上├── agents/                      # 多 Agent 公共 subagent├── docs/│   ├── README.md                # 查询入口，场景路由表│   ├── INDEX.md                 # 资产索引，一行一条，供精确检索│   ├── LOG.md                   # 资产维护日志│   ├── knowledge/               # 知识层│   └── activity/                # 活动层├── skills/                      # 多 Agent 公共 skill└── repos/    └── <your-repo>/             # 源码层，submodule，只读\`\`\`\`docs/\` 下三个文件各有分工，这里最容易做错。
\`docs/README.md\` 是**路由表**，只说信息怎么找，不放内容。一张「我要查什么 → 去哪里」的表，加上外部权威源清单。任何信息查询一律先读它，不要凭印象猜文件路径。
\`docs/INDEX.md\` 是**内容索引**，一行一条资产，含类型、ID、一句话内容。设计目标是能被 ripgrep 精确命中。规模到几百页时它仍然够用，不需要向量检索。
索引可以分级。资产多到一份 INDEX 读起来费劲时，在子目录下放一份自己的 \`INDEX.md\`，顶层那份只留一行指向它。Agent 从顶层往下逐级钻， 每次只读需要的那一份。分级的时机是某一类资产多到你自己都要翻半天， 不用预先设计。
\`docs/LOG.md\` 是**时间线**，追加式，\`## YYYY-MM-DD\` 下挂条目，每条一句话说清改了什么、为什么改。「为什么」不能省 —— 这个文件的用处是半年后你还能搞清楚某个约定当初为什么这么定。用统一前缀开头就能被 unix 工具解析，\`grep "^## " LOG.md | head -5\` 给出最近五次变更。
\`docs/knowledge/\` 和 \`docs/activity/\` 一开始都可以是空的。它们在第一次任务收尾时自然长出内容。空目录比预先编好的目录结构好 —— 预设的分类往往在第三次任务时就发现不合适。
## 三个操作**查。** 任何信息查询先读 \`docs/README.md\` 路由到具体位置，再读 \`INDEX.md\` 找到资产，最后读资产本身。三跳。外部平台的实时数据（卡片状态、知识库正文）每次现取，不用本地缓存。
这个顺序要写进规则层强制约束，否则 Agent 会凭印象猜路径 —— 猜错了它不会报错，它会给你一个基于错误前提的答案。
**做。** 正常的业务工作。设计、开发、测试、修 bug、排障、上线。Workspace 在这里的作用是 Agent 开工前能自己查齐上下文，收工前能自己验证结果。
**写回。** 任务结束把这次产生的东西沉淀进去，并提交。这是整个模式里最关键的一步，单独一节讲。
## 写回写回决定这个模式成不成立。前两个操作只是让 Agent 用得更顺，写回才让资产累积。
**写回必须是流程里的强制阶段，不能是良好习惯。** 做成一个 skill，规则层里写明「任务没走完这一步就不算结束」。依赖自觉的写回不会发生 —— 任务做完的那一刻，人和 Agent 的注意力都已经在下一件事上了。
**写回过程不要请求用户决策。** 放哪一层、文件叫什么、日志那句话怎么写，Agent 自己定，直接落盘。用户在任务过程中已经给过足够信息，收尾时再逐项确认等于把成本从 Agent 转回人身上。写回一旦变成一道需要人配合的手续，它就会被跳过。
只有两种情况该停下来问：要做的事违背规则层定义的分层规则，或者要写进知识层的结论与用户明确表达过的判断冲突。分不清该放哪一层**不是**提问的理由 —— 兜底规则是放活动层，那里的内容不失效，代价最小。
**写完直接提交。** 只落盘不提交，等于没写回。逐个显式 \`git add\` 本次改动的文件，不要 \`git add -A\`（工作区可能有无关改动）。commit message 单行，写清沉淀了什么。不 push —— 提交是本地动作可以回退，push 是对外动作需要授权。
**这次没有产生新知识是正常结果。** 照文档实现、过程顺利、没遇到判断的任务，只写一条活动记录就够。往知识层硬塞内容会增加以后的检索噪声。反过来，拿不准某条经验值不值得记时倾向于记下来 —— 一条略显多余的经验只是噪声，一条丢掉的经验是下次重新踩一遍。
写回 skill 的完整步骤：判断这次产生了什么 → 按分层规则分流 → 旧页被推翻时回头改原页 → 同步 \`INDEX.md\` 和 \`LOG.md\` → 补双向引用 → 提交。
双向引用容易漏。页面之间靠 \`## Related Docs\` 串联，新页指向相关页时，要回到被指向的页补一条反向引用。单向引用等于没引用，从另一头进来的人找不到它。
**初始化时先建一个最简版本就够。** 一句话：
\`\`\`md
---name: summarizedescription: 把会话中有价值的决策、结论、资产、经验写入 docs 下合适位置。任务收尾时调用。
---
把会话中有价值的决策、结论、资产、经验等写入到 \`docs/\` 下合适位置，按照 Workspace 根 \`README.md\` 里的 docs 组织规则进行记录，写完提交。\`\`\`这样就能跑。上面那些约束不用一开始全写进去 —— 它们是跑过几次任务、发现具体做错在哪之后再往里补的。开头就写一份详尽的 skill，约束的多半是你想象中的问题。
## 定期体检Workspace 会腐坏，腐坏方式是可以枚举的，所以可以定期让 Agent 自己查。
* 两个页面互相矛盾* 某个结论已经被后来的证据推翻，但页面没改* 孤儿页，没有任何页面指向它* 单向引用* 反复被提到但没有自己页面的概念* \`INDEX.md\` 里的条目指向已经不存在的文件* 活动层里同一个坑出现了三次，说明它该被提炼成一条经验
这件事人不会做，Agent 做起来成本几乎为零。给它一个 lint 脚本或者一个 checklist，跑一遍报告问题。
顺带一提，Agent 在体检时很擅长提出「这里缺一份什么」的建议，这些建议往往比它发现的问题更有价值。
## 建得好不好，看四件事1. **业务资产齐不齐**，Agent 能不能找到它需要的东西。2. **查询路径高不高效**，一次查询花多少 token、几次工具调用。3. **查出来的信息准不准**，事实和结论能不能直接当依据用。4. **新知识能不能写回**，这次想清楚的东西下次还在不在。
这四个问题的解法各不相同，同一个问题在不同业务场景里解法也不同。第四条是唯一一条决定这个模式成不成立的 —— 前三条做得再好，没有写回就只是一个查得比较顺的文档库。
## 可选：能力层往上长基础骨架跑通之后，按需要加。这些都是可选的，缺了不影响模式成立。
**平台接入 skill。** 卡片系统、知识库、代码库各一个，让 Agent 自己去取实时数据而不是等你粘贴。这是收益最直接的一类。
**执行与验证能力。** 让 Agent 能起本地环境、跑测试、查日志、连测试机执行命令。这一类决定 Agent 能不能自己收敛。设计上参考负反馈系统 —— 一个只能输出不能观测结果的 Agent 永远需要人来判断做对了没有。给它执行能力时用白名单控制每台机器上能跑什么，挡住危险操作。
**subagent。** 边界清楚、输出能独立评审的调研或验证任务可以委派出去。判断标准是任务说明能不能写成自包含的 —— 如果你已经能在任务说明里写出具体的检索关键词和目标文件名，那自己查更快。
**工作流。** 把「设计 → 开发 → 测试 → 写回」这类固定序列显式定义出来，包括每步的产物和人工确认点。规模小的时候不需要，几个 skill 靠规则层串起来就够。
**检索工具。** \`INDEX.md\` 在几百页规模内够用。再往上考虑本地检索工具。不要一上来就上向量检索，一行一条的索引配 ripgrep 能撑很久，而且结果可解释。
## 四份初始文件的模版初始化时要写的就这四份。占位处按自己的业务填，能删的删。
### \`README.md\`\`\`\`md# <Workspace 名>
<一句话说清这个 Workspace 服务什么业务>。它是业务资产、可复用能力和源码访问的统一入口。
> \`AGENTS.md\` 与 \`CLAUDE.md\` 都是指向本文件的软链。**规则只在 \`README.md\` 维护**，> 不要改软链、不要把软链替换成副本、不要在软链目标之外另写一份规则。
## 目录结构
\`\`\`<workspace 名>/├── README.md          # 本文件，规则唯一源├── AGENTS.md -> README.md├── CLAUDE.md -> README.md├── .claude/           # 适配 Claude Code，只放软链├── .codex/            # 适配 Codex├── .comate/           # 适配 Comate├── agents/            # 多 Agent 公共 subagent├── docs/              # 见下├── skills/            # 多 Agent 公共 skill└── repos/             # 业务代码库，submodule，只读\`\`\`
## 查询信息先读 docs/README.md
任何信息查询一律先读 \`docs/README.md\`，它是 \`docs/\` 的唯一入口与路由表。**不要凭印象直接猜文件路径。**
外部平台是权威源，\`docs/\` 只是索引层与本地沉淀层。卡片状态、知识库正文、提交记录都以外部平台的实时数据为准。
## 改代码之前先读 repos/<repo>/AGENTS.md
\`repos/\` 下的仓库以 submodule 引入，在本 workspace 内只读。修改代码要进入源码仓库自身的 checkout，并遵循它的 \`AGENTS.md\`。
## 一次任务怎么结束
走完开发、验证之后必须调用 \`summarize\` skill 收尾。它负责把这次产生的东西写进 \`docs/\` 合适位置，同步 \`INDEX.md\` 和 \`LOG.md\`，并提交。
**写回不靠自觉，它是流程里的强制阶段。** 一次任务没有 \`summarize\` 就不算结束。落点判断、命名和措辞由 Agent 自己定，不回头找人确认。
## 分层规则
\`docs/\` 下只有两层，按内容**会怎样失效**划分，不按主题划分：
| 层 | 目录 | 放什么 | 什么时候会失效 ||---|---|---|---|| 知识层 | \`docs/knowledge/\` | 概念定义、外部系统入口、带条件的经验判断 | 被新证据推翻时；此时**回头改旧页**，不是另写一页 || 活动层 | \`docs/activity/\` | 每次任务做了什么、怎么做的、验证结果 | 不失效，只增不改 |
两层都放不下时**停下来问用户**，不要硬塞进最接近的目录。\`\`\`### \`docs/README.md\`\`\`\`md# docs 查询入口
本文件是 \`docs/\` 的唯一查询入口，只描述信息怎么找，不承载动态状态，不复制外部平台内容。
外部平台是权威源，\`docs/\` 只是索引层与本地沉淀层。
## 外部源
- <卡片系统>：<空间标识>- <代码库>：<仓库路径>- <知识库>：<空间地址>
## 场景路由
| 我要查什么 | 去哪里 ||---|---|| 精确找某份资产 | \`INDEX.md\`，用 ripgrep 命中关键词 || 某个约定当初为什么这么定 | \`LOG.md\`，按日期倒着翻 || 概念、术语、平台是什么 | \`knowledge/\` || 某个坑踩过没有、某个做法为什么被否掉 | \`knowledge/\` 下经验页 || 某件事是什么时候做的、怎么验证的 | \`activity/\`，文件名带日期与主题 || 代码在哪、怎么跑测试 | \`../repos/<repo>/AGENTS.md\` |
## 写入规则
- 长期有效的东西进 \`knowledge/\`，做过的事进 \`activity/\`。- 旧知识被新证据推翻时**回头改那一页**，并在 \`LOG.md\` 记一条为什么改。  不要另写一页新的留着两份矛盾的真相。- 每次写入都要同步 \`INDEX.md\` 一行和 \`LOG.md\` 一段。  这由 \`summarize\` 负责，不靠人记。\`\`\`### \`docs/INDEX.md\`\`\`\`md# 资产索引
## Search Rule
1. 先读本文件，在资产表中找到对应资产；2. 读对应资产获取相关内容。
## 资产表
| 类型 | ID | 内容 ||---|---|---|| 文件 | knowledge/<页面>.md | <一句话说清里面有什么> || 文件 | activity/<日期>-<主题>.md | <一句话说清做了什么> || 卡片 | <空间>#<编号> | <卡片标题> || 文档 | <知识库链接> | <文档标题> |\`\`\`初始化时资产表是空的，只留表头。一行一条，\`|\` 分隔，方便 ripgrep 命中。
### \`docs/LOG.md\`\`\`\`md# 资产维护日志
记录 \`docs/\` 与索引资产的变更。格式是 \`## YYYY-MM-DD\` 下挂条目，每条一句话说清改了什么、为什么。
它的用处是半年后你还能搞清楚某个约定当初为什么这么定。
## <建库日期>
- 建库。\`README.md\` 定下两层分法与 \`summarize\` 强制收尾规则。\`\`\`倒序排列，最新的在最上面。统一用 \`## YYYY-MM-DD\` 开头，\`grep "^## " LOG.md | head -5\` 就能看最近五次变更。
## 怎么让 Agent 帮你建把这份文档丢给 Agent，加上一段这样的话。
\`\`\`参考这份文档，在当前目录建一个 Workspace。
业务背景：<一句话说清这个 Workspace 服务什么业务>要接入的代码库：<仓库地址，可以留空>外部平台：<卡片系统 / 知识库 / 其它，可以留空>
按文档的最小骨架和四份模版建，具体要求：1. README.md 按我的业务背景填模版，不要照抄示例文字2. docs/ 下只建 knowledge/ 和 activity/ 两个空目录，   不要预设更细的分类3. INDEX.md 只留表头，LOG.md 只写建库那一条4. summarize skill 按文档里的最简版本建，先不要写复杂约束5. 平台接入 skill 先只留目录和一行说明，我确认接哪几个之后再补6. 建完告诉我哪些地方你做了假设、哪些需要我补信息\`\`\`Agent 建完之后，先跑一次真实任务再评价这个结构。空的 Workspace 看不出问题，第一次任务收尾时才会发现分层规则哪里定得不合适。前三次任务是调整期，改规则层比改已经写进去的内容便宜得多。
## 为什么这样可行维护一个知识库的累人之处不在读和想，在记账。更新交叉引用、保持摘要同步、发现新证据与旧结论冲突、维护几十个页面之间的一致性。人放弃知识库是因为维护负担增长得比价值快。
Agent 不会觉得记账无聊，不会忘记更新一个交叉引用，能在一次任务里改十几个文件。维护成本降到接近零，知识库就能一直活着。
人的工作是给方向、提出好问题、判断这些东西意味着什么。剩下的交给 Agent。
## 注意这份文档故意是抽象的。它描述模式，不描述某个具体实现。确切的目录名、页面格式、skill 划分、工具选择，都取决于你的业务、你的习惯和你用的 Agent。上面提到的东西都是可选的、可拆的 —— 有用的拿走，没用的忽略。
比如：你可能没有需要接入的外部平台，那三个平台 skill 就不需要；你可能只管一个仓库，\`repos/\` 下就只有一个条目；你可能不需要 subagent 和工作流，几个 skill 加一份规则层就够。
正确的用法是把这份文档交给你的 Agent，一起做出一个符合你需要的版本。这份文档的唯一任务是把模式讲清楚，剩下的 Agent 能自己想明白。
```

END

**推荐阅读**

[商业客户端Harness资产管理与应用实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607453&idx=1&sn=0d0dc5f97c286cb80c48a42a7bbf654f&scene=21#wechat_redirect)

[小度为什么越来越懂你？一套 Agent 研发闭环的诞生](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607435&idx=1&sn=f3d5edccff2fbb03206fcb232246959c&scene=21#wechat_redirect)

[从分散提效到 AI Native 组织的实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607411&idx=1&sn=5cb281a28a76a39ea5556059164d102b&scene=21#wechat_redirect)

[图灵平台：万亿级轨迹数据的秒级检索实战](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607355&idx=1&sn=dd9eeee98d0b139ee34597ae0ba2cfd3&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过