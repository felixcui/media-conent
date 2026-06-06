# [译] 95% 分析自动化：Anthropic 用 Claude 做数据分析的 4 层栈与避坑实战

**作者**: AI技术立文

**来源**: https://mp.weixin.qq.com/s/Hl2vuRfoRBHOyTGC1xU_Yw

---

## 摘要

Anthropic借助Claude实现了95%业务分析查询的自动化，准确率约达95%。文章指出，大模型驱动的分析准确性本质是上下文与验证问题，其核心难点在于将用户问题准确映射到数据实体上，主要面临概念实体歧义、数据陈旧和检索失败三大错误模式。为此，Anthropic搭建了包含数据基座、真相源、维护验证流程及Skills的智能体分析栈，有效应对上述挑战，从而将数据团队从机械重复的取数工作中解放出来，。

---

## 正文

AI技术立文 AI技术立文

在小说阅读器读本章

去阅读

## 目录

- 1 数据不是软件
- 2 我们的智能体分析栈
- 3 如何起步
- 4 附录

很多数据科学和数据工程团队都深有体会：要让业务方实现自助式分析，向来是一件苦差事。

为了让技术能力较弱的同事也能用上数据模型，常见做法是把数据摊平成又宽又反范式的大表。可随着业务规模扩大，这些表往往会衍生出大量定义不一致、相互重叠的视图（而且对那些根本没兴趣学 SQL 的员工来说，帮助也很有限）。另一条路是为用户搭建更封闭、更受控的环境，但这又常常照顾不到业务问题的长尾，并随着各团队各自为政，导致指标和看板不断膨胀。

大语言模型为自助式分析提供了一条能绕开上述难题的新路径。但如果只是把 Claude 接上数据仓库、放手让智能体自己去执行，反而会制造一种虚假的精确感。

刚摆脱临时取数请求时的那份解脱很快会变成焦虑——你会意识到，这种接法把业务方和底层基础设施、文档以及专业经验隔开了，而正是这些东西，过去一直在引导他们去用那些精心维护的数据集。

在 Anthropic，95% 的业务分析查询由 Claude 自动完成，整体准确率约为 95%。把这些往往机械、重复的活儿交给 Claude 之后，我们的数据科学团队就能腾出手来，专注于因果建模、预测、机器学习这类更具战略性的工作。

我们和数十位 Anthropic 内部的 Claude Code 重度用户聊过，也见识了形形色色的分析智能体设计模式，由此沉淀出了一些最佳实践，分享给同样在用 LLM 的数据团队。这篇文章会讲清楚我们如何最大化发挥 Claude 驱动自助式业务洞察的能力，包括：

- 为什么分析准确性是一个上下文与验证问题，而不是代码生成问题；
- 导致绝大多数错误的三种失败模式；
- 我们为应对这些错误而搭建的智能体分析栈；
- 我们如何衡量效果；以及
- 我们创建大多数 Skill 所用的一个基础模板（见附录）。

---

## 1 数据不是软件

LLM 的生成能力是一把双刃剑：那套能为复杂问题创造性求解的机制，同样可能凭空产出错误的结果。要彻底理解分析智能体的难点，不妨拿它和编码智能体做个对比。

编码是一个开放式的解空间，会奖励模型的创造力，而文档和测试天然为它提供了对抗幻觉的护栏。相比之下，在分析场景里，往往只有唯一正确的答案、对应唯一正确的数据源，而且没有一种确定性的办法来证明结果的正确性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IUJGIjicknic34Wk4dFwjYdpjfUszHW5m876PWgtepNxnC9dOYptHhMxRHHqpzfIE5P61Ohp1KhutT6pT9Slv9BhbG9dfZR9Ld4XCibdPw0jOc/640?wx_fmt=png&from=appmsg)

对自助式智能体业务分析来说，复杂性主要来自数据本身的歧义。问题的核心，归根结底在于我们 ***能否把用户的问题映射到数据模型中具体且最新的实体上，并知道与它们打交道的正确方式*** 。只要能做到这一点，后续的执行和 SQL 都会变得无足轻重。

我们识别出这个问题的三个特征，它们解释了绝大多数不准确的回答：

1. **概念与实体的歧义：** 数据模型中有数百个可用选项（而潜在字段可能多达数百万个），智能体没法挑出最能回答用户问题的那个正确字段。比如要统计活跃用户数：哪些行为才算「活跃」？要不要把欺诈用户算进去？用多长的回溯窗口？
2. **数据陈旧：** 数据源、业务定义和表结构在不断变化；数据资产和智能体的知识会过期，开始返回一些细微出错的答案。
3. **检索失败：** 正确的信息其实就在数据模型里、也标注妥当了，但搜索空间太过庞大，智能体就是找不到它。

也可以阅读官方文档 <sup>[1]</sup> 。

---

## 2 我们的智能体分析栈

在 Anthropic，我们把这三类错误降到最低的主要手段，就是这套智能体数据栈。每一层的存在，主要都是为了攻克其中一个或多个问题：

1. **实体歧义：** 数据基座和真相源不断收缩候选实体的空间，直到只剩一个受治理的答案。
2. **陈旧：** 维护和验证流程让一切随业务变化而保持新鲜，不至于腐烂。
3. **检索失败：** Skills 确保智能体能可靠地找到那个答案，并正确地用上它。

这一节，我们会逐层讲讲它们是怎么搭起来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IUJGIjicknic0lVRMZC1hqjoNbl5xxmcXZjty2Niaj5LjBAjxZJNeROSXApHsCoDSH1ic4mXyS91LFD0vZsYYj3TOiaREbpydnb5aYVXXYXvep64/640?wx_fmt=png&from=appmsg)

维度建模这类标准数据工程实践，今天依然和过去一样重要。

### 2.1 数据基座

确保分析智能体准确，最重要的一环是打好坚实的数据基座——它包括数据仓库里的数据模型、转换、测试和表，以及描述它们的元数据。维度建模（dimensional modeling <sup>[2]</sup> ）、测试左移、对关键管道做新鲜度与完整性检查这些标准的数据工程和数据质量实践，全都依旧适用（这里就不再赘述了）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IUJGIjicknic31b5MSNoRcr9ia6CiaCdq69plGRdsQcgCicZc9sPPWUAJW6pXYynOlK3icRz3tlssRlr9sG8E4vOUeo9icDNWLu6hW9sHCKQUXEpNY/640?wx_fmt=png&from=appmsg)

维度建模这类标准数据工程实践，今天依然和过去一样重要。

### 2.2 真相源

如果说数据基座是数据仓库本身，那么真相源就是智能体在仓库里导航时所依据的一组参考资料。这一层负责消解概念与实体的歧义，把利益相关方口中的「周活跃用户」落实成数据模型里一个具体的、受治理的实体。下面这几类大致按可信程度从高到低排列：

- **语义层：**
	编译后的指标与维度定义。如果一个问题能干净利落地映射到某个已定义的指标，智能体就调用一个函数、得到一个数字——和公司里其他所有口径产出的数字完全一致。我们的智能体在结构上 *被强制要求* （通过 Skill 指令）首先使用语义层（见附录）。有一个我们试过但 *没成功* 的想法：让 LLM 从原始表和查询日志中自动生成指标定义，以此给语义层「冷启动」。结果它产出的定义看着挺像样，却把我们本想消除的那些歧义又编码了进去，在评测上相比一个更小、由人工精选的层反而是净负向。所以我们的建议是：用 Claude 生成 *文档* ，但让人来掌管 *定义* 。
- **血缘与转换图：**
	当语义层覆盖不到某个问题时，血缘和表排名（依据被引用次数）能让智能体推断出哪些上游模型供养了某个概念、哪些已被废弃、哪些共享同一粒度。这就把「我不知道用哪个指标」变成了「我知道该从哪个受治理的模型去聚合」。它也是我们在下文 **在线验证** 中所暴露的新鲜度与溯源信号的底层支撑。
- **查询语料库：**
	来自看板、notebook 和过往分析的历史 SQL。直觉上这应该很有价值：它记录了每一个已被正确回答过的问题。 *但实践中我们发现，给智能体开放对成千上万条历史查询的原始检索权限，准确率的提升还不到一个百分点* （这次消融实验我们会在后文细讲）。非结构化检索没法把一个新问题映射到正确的先例上。真正有效的，是把这个语料库提炼成结构化的、按域组织的参考文档，以及在 **Skills** 中描述的可复用分析范式。要把查询历史当作供人精选的原材料，而不是让智能体直接去读的真相源。
- **业务上下文：** 这是大多数团队会跳过的一层，也是我们低估最久的一层。一个不懂你业务的智能体，会回答用户「问了什么」，却答不出用户「想问什么」。它不会知道「Q2 那次发布」指的是某个特定产品，不会知道两个团队对同一个词有不同定义，也不会知道某个问题之所以被问，是因为周四要开董事会。我们接入了一张公司知识图谱，由索引后的文档、路线图、决策日志和组织架构构成，好让智能体能够解析这些隐含的指代，并提出更好的澄清式提问。

这四者共同的失败模式，和数据基座层是同一个： **文档缺失或陈旧。** Claude 在弥合这道鸿沟上极为有用（起草列描述、根据查询模式提出指标文档、在 CI 里标记出未记录的模型），但精选和权属仍由人来掌管。

接下来两节，我们会讲如何把这份「权属」的成本压到足够低，低到它真的会被落实。

### 2.3 Skills

如果说真相源是智能体的 *陈述性* 知识（即一个指标意味着什么），那么 Skill 就是它的 *程序性* 知识：按什么顺序查阅哪些数据源、如何在歧义数据中导航、一份完成的分析长什么样。

在 Claude Code 里，一个 Skill <sup>[3]</sup> 就是一个由若干 markdown 文件组成的文件夹，智能体按需读取。在 Anthropic，我们开发的 Skills 带来的增值极大。没有 Skills 时，Claude 准确回答分析问题的能力在我们的评测上不超过 21%；加上 Skills 后，这个数字稳定保持在整体 95% 以上，在某些域里更是经常达到 99% 左右。我们用来创建大多数 Skill 的骨架见附录。

几条最佳实践：

**成对地创建 Skill：** 一个 ***knowledge*** skill 充当一个轻量的顶层路由器，让额外的领域细节按需加载。它的逻辑是「先试语义层，但如果没覆盖到，这里有大约 30 个针对本域的参考文件，描述了相关的表、列、连接和坑」。这个路由器实际上就是我们对检索失败的回应：与其让智能体在一个百万字段的仓库里大海捞针，不如在写出任何一条查询之前，先把空间收窄到几十个精选文件上。而 ***unbook*** skill 则编码了一位资深分析师会遵循的流程：澄清问题、找数据源（通过 knowledge skill）、跑查询，然后把结果丢进对抗式审查子智能体里循环把关。它还打包了十几种可复用的分析范式（留存曲线、比率分解、漏斗分析），这样常见请求就不必每次都从头造轮子。

**写出像样的参考文档：** 要为「被 LLM 检索」而写。我们的参考文档会描述表（粒度、范围、排除项）、各种坑的处理机制（例如「排除已知的免费邮箱域名，但保留 anthropic.com 这类自定义域名」），以及明确的路由触发条件（例如「如果问题是关于实验增益的……不要用于原始事件计数」），同时避免写那种很快就会过时的死板配方。我们创建参考文档所用的骨架见下。

```markdown
# [域] 表

## 快速参考
### 业务背景 — [用大白话讲清这个域是什么意思]
### 实体粒度 — [一行代表什么]
### 标准清洗过滤 — [本域每条查询都要加的过滤条件]

## 维度
- [关键维度如何编码，以及同一概念在不同表里
  是如何被叫成不同名字的]

## 关键表
### [table_name]
- **粒度**：[...] · **范围 / 排除项**：[...]
- **用法**：[何时用、何时不用、连接键、必加过滤]
[... 每个受治理的表写一小节 ...]

## 坑
- [一位资深分析师会提醒你注意的那些出错模式]

## 最佳实践 / 常见查询范式
- [默认选择、标准切分维度、那些「查询写法本身才是难点」的
  实战范式]

## 交叉引用
- [掌管相邻问题的邻近域文档]
```

**把 Skill 维护当成一等公民：** Skill 文档描述的是一个每天都在变的数据模型，所以没有主动维护，它们几周内就会变错。我们曾眼睁睁看着离线准确率在一个月里从上线时的约 95% 漂移到约 65%，之后才把它当成一个工程问题来对待。这意味着要把 Skill 的 markdown 文件和我们的转换模型放在同一个仓库里，于是「改模型的那个 PR」就是「更新对应文档的那个 PR」。一个代码评审钩子会标记出任何「改了报表模型却没动 Skill 文件」的改动。如今，我们大约 90% 的数据模型 PR 都会在同一个 diff 里附带 Skill 改动。随着模型变强、过去的失败模式不再适用，我们也会定期修剪 Skill 里的脚手架。

**在所有触面上提供一致而无缝的体验：** 同一个 Skill *必须* 对 Slack 里、IDE 里、看板工具里、独立智能体会话里的同一个问题给出同一个答案。我们的做法是确保只有一个标准源（数据仓库），并让 Skill 的改动自动同步。合并时，Skill 会同步到插件市场（供 IDE 用户使用）、同步到云存储 blob（供那些读取单个文件的托管应用使用），并通过 MCP 直接作为资源对外提供。我们从一开始就为可移植性做了设计，避免写死仓库路径和触面专属的命名空间。

### 2.4 验证

最后，验证是你弄清三种失败模式中哪一种仍在漏过去的手段。

#### 2.4.1 离线评测

我们常看到一种模式：数据团队搭起了精巧的分析环境，却没有任何流程去了解自家分析智能体的准确率。

弥补这道缺口的一种办法是离线评测，也就是简单的问答对。你可以把离线评测类比为机器学习模型的离线测试——它们不会告诉你线上智能体的真实表现，但能让你大致判断是否存在关键缺口。

我们在 Anthropic 部署了两类离线评测。 **基于看板的评测** 由 Claude 自动生成（再经人工校验），覆盖最常见的利益相关方问题。 **长尾评测** 则是把业务上下文（路线图、表文档）喂给 Claude，让它在该域的其余部分生成一些合理的问题。我们还会持续收割每一次利益相关方在会话串里纠正智能体的瞬间，因为这样一次纠正就是一条候选评测。

其他最佳实践包括：

- **锚定标准答案，使其无法漂移：**
	针对实时数据写的评测，底层数字一变就立刻过期。把每条评测钉死在某个快照日期上，或针对一张稳定的事实表来写，或让评分器去判断智能体的 *查询* 而非它给出的数字。把整套评测接入 CI，这样一旦某个 PR 触碰到依赖，相关评测就会被重跑。
- **把结果当遥测数据存，而不是当测试日志存：** 每一次运行都落进一张仓库表里，带上 Skill 版本、git SHA、模型 ID、逐条断言的通过 / 失败、token 数和墙钟时间。「那次改动到底有没有帮助？」于是变成了一条查询，你还能拿到时间序列，从而抓到单次 CI 跑不出来的缓慢回退。
- **按域逐一为发布把关：**
	在某个域所属的评测集越过某个阈值（我们最初用约 90%）之前，该域的负责人不能向其利益相关方宣告智能体可用。这逼着大家 *在* 用户看到失败 *之前* 就把参考文档修好。
- **创建数量合适的评测：** 你该有多少条评测，取决于业务领域的复杂度和底层数据模型的复杂度。校准的办法是跟踪离线准确率对线上准确率的预测能力有多好：我们发现，每个主题（比如「增长」）超过几十条之后就会边际递减，而且这个上限会随着每一代新模型的到来而下降。
- **离线评测准确率应当约为 100%；** 每一个正确答案也都应当命中你的语义层（如果你有的话）。再强调一遍，这种水平的准确率并不能说明你的系统不会产出错误答案，只能说明——在你有恰当评测覆盖的前提下——没有明显的缺口。

#### 2.4.2 消融技巧

关于 Skill 的每一个结构性决策（比如暴露哪些数据源、某个子智能体是否值得它带来的延迟、要不要把两个 Skill 合成一个），都是在固定住我们的离线评测集的前提下做出的。

我们每次只改动一个组件，比较通过率。每次运行只花一个小时，却能省下大量空谈。方法论本身比任何单个结果都更重要：

- **为「零结果」而设计。**
	我们最有用的一次消融恰恰是个负向结果。我们给了智能体对整个看板、转换层和分析师 notebook 中 SQL（成千上万个文件）的直接 grep 权限，然后在会话记录里确认它在每次回答前确实读了这些文件。准确率在两个方向上的变化都不到一个百分点。我们接着排查了那些显而易见的混淆因素：对于它答错的那些问题，答案究竟在不在语料库里？大约 80% 的情况下，在。那么「答案存在」能否预测「现在答对了」？不能，翻转率是平的。信息就在那儿，智能体也看到了，可它还是没用上。这一个实验就告诉我们：我们的瓶颈不是对既往成果的 *访问权限* ，而是 *结构* （即把问题映射到正确实体）。这个洞见改写了我们好几个月的路线图。
- **以 PR 为粒度做消融。**
	每一次有意义的 Skill 编辑，都会在相关评测切片上跑一次「改动前 / 改动后」，并把差值写进 PR 描述里。这让「我把文档改好了」这句话变得诚实，也能抓住一种意外地常见的情况——某个出于好意的添加反而让事情变糟了。
- **保留一份「什么没用」的简短清单。**
	我们的清单里有两条：超过某个程度后再叠加几轮文档精修（我们连着撞上三次净负向迭代：文档是越来越长，而不是越来越好），以及把对抗式审查者换成更便宜的模型以削减延迟（它丢掉了大部分准确率收益，却没换来真正的提速）。负向结果记录起来很便宜，还能避免下一个人重跑同样的实验。

#### 2.4.3 在线验证

最后一步，是确保线上系统的实际表现尽可能准确。我们采取的部分措施包括：

- **对抗式审查：** 我们发现，用一个 Claude skill 去激进地挑战一个潜在最终答案背后的所有假设，能让评测集内的准确率提升 6%，但代价是多消耗 32% 的 token、延迟高出 72%。
- **溯源页脚：** 每条回答都带一个页脚，注明它来自哪个数据源层级（语义层 › 精选参考 › 原始表）、底层数据有多新鲜、谁拥有这个模型。它不会让答案变得更正确，但能帮消费者判断这份回答有多可信。一个「原始表，新鲜度未知」的页脚，就是在提示你「往上转发之前先核实一下」，而这也是我们为数不多的、能对付静默失败的手段之一。
- **数据质量检查：** 有可能智能体用对了字段、也用对了方式，但数据本身就是错的。加上一些基础的数据质量检查，确保被引用的字段是最新的、完整的、没有异常，通常是个好习惯。
- **被动监控：** 我们持续追踪两个生产信号——智能体查询中通过语义层解析的占比，以及回答中使用纠正性措辞（「那张表用错了」「你漏了欺诈过滤」）的占比。两者都汇入一张每周复盘的看板，与离线通过率并排查看。
- **主动收割纠正：** 这是闭环的关键一环。一个定时智能体每隔几小时扫描一遍利益相关方的频道，寻找类似的纠正性措辞，给相关参考文档起草一行修复，并开一个 PR、指派给域负责人。这条修复路径被刻意设计得很无聊——改一个 markdown 文件、合并、自动同步到各处——好让域负责人不必在这件事上花太多时间。同样这些纠正，也会回流进离线评测集。

这一切都没法完全兜住的那个失败模式，是 **静默** 的那种：答案是错的，却看上去合理，于是被人毫无异议地用掉了。我们的缓解手段有溯源页脚、对任何上达管理层的内容要求人工显式签字确认，以及为每个域的头部 KPI 设一个常驻评测，每天对照那张「开过光」的看板做一次合理性核对——尽管我们还没有一套足够稳健的解法。

---

## 3 如何起步

如果你从零开始，那么少数几个标准数据集、几十条离线评测，再加一个轻量的 knowledge skill，就能拿下大部分收益；这篇文章里的其他一切，都是我们在把这些建好之后才加上去的。

我们也分享了许多最佳实践，但并非每一条都适合每个数据团队。请和你的组织对齐几条会影响你做法的原则，问问自己：

- **当下答对一个问题有多重要，相对于未来？**
	AI 模型正在飞速进步。我们经常看到一些公司投入大量基础设施去弥补当前模型的不足，可一旦模型变强，这些投入就变得多余了。看清模型在哪儿不行、然后等模型升级来填上缺口，开销要小得多——但这未必符合你公司的风险承受度。
- **你预期自己业务的复杂度会随时间如何变化？**
	我们讨论的某些流程可能是杀鸡用牛刀——比如你产出的数据不多、输出的消费者只有寥寥几个，或者你的数据模型大概率会一直很简单。
- **输出的目标受众有多技术？**
	换个说法：如果你这套分析系统是给那些一眼就能看出答案不对的数据科学家用的，那相比受众对底层数据模型一无所知的情形，你或许能容忍更多错误。
- **你愿意为提升准确率花多少钱？**
	我们发现，对抗式验证这类流程能显著提升准确率，但往往伴随更高的成本和延迟。
- **你对访问控制和内部数据隐私的接受度如何？**
	智能体掌握的上下文越多，往往越好用；可是宽泛的数据访问权限，又与大多数公司的治理姿态相冲突。这会决定你是在造一个智能体，还是造许多个各有权限边界的智能体。

无论你走哪条路，我们最大的收益都来自直面那三种失败模式：把歧义收敛成唯一一个受治理的答案、让这个答案易于被发现，并在二者之一变陈旧时及时报警。

*本文作者为数据科学与数据工程团队成员 Chen Chang、Clement Peng、Justin Leder、Johanne Jiao、Josh Cherry。作者感谢 Michael Segner 的贡献。*

---

## 4 附录

### 4.1 Skill 文件骨架

下面是我们主力仓库 Skill 的骨架：真实文件的结构原样保留，内部具体内容替换成了 \[方括号占位符\]。它不是用来照搬的，而是用来展示我们觉得值得写下来的那些章节类型。

```markdown
---
name: [warehouse-skill]
version: [x.y.z]
description: "IF the user asks to query [the company]'s data warehouse for any
  [list of business domains] question — THEN invoke this skill. DO NOT invoke
  for [adjacent engineering tasks] or questions with no data-warehouse component."
---

# [Warehouse] Skill Instructions

## Description
The single source of truth for safe and effective [warehouse] querying.
Referenced by other skills [listed] for query execution guidance.

Act as a Data Analyst, providing strategic insights and data-driven
recommendations but seek guidance along the way.

**Out-of-scope decisions**: [product areas, etc.] → surface data only,
state "decision is [owning team]'s call", do NOT take a position or author
code fixes.

## Executing queries
Priority:
1. **[Managed connection]** (if available): [query tool] / [schema tool]
2. **[CLI fallback]** (if installed): [default project, fallback project]
3. **Neither** — ask the user to authenticate, then stop

---

# Semantic Layer (REQUIRED first step)

The governed semantic layer is the **mandatory default path** for every data
question — same numbers as [the BI tool], joins/grain/filters baked in. Raw SQL
via the reference docs below is the **fallback**, used only after the
semantic-layer path is shown not to cover the ask.

## Required workflow
1. **Load** — [how to load the semantic layer in each runtime, with fallbacks]
2. **Discover** — search measures/dimensions by keyword; **always check
   segments** (the named canonical population filters — hand-rolled WHERE
   clauses for these are the dominant wrong-answer mode)
3. **Compile + run** — build the spec → compile to SQL → execute
4. **Fallback** — only if discovery finds no relevant metric or compile fails
   → raw SQL via \\`references/*.md\\` (PART 3 below)

> **Don't bail early.** Do NOT fall back to raw SQL on these grounds:
> - "[custom date filtering / cohorts]" → [covered by time-dimension specs]
> - "[needs a join]" → [the metric layer already encapsulates its joins]
> - [3–4 more pre-rebutted excuses agents use to skip the semantic layer]

### Date windows & timezone — decide before you query
- **As-of date vs trailing-N days**: [convention for each]
- **"Last week/month"** → the last *complete* calendar week/month, not trailing-7/30
- **Timezone default**: [TZ]; [exception for certain reporting rollups]
- **Freshness lag**: [some] tables settle late — anchor on MAX(date), not "yesterday"

---

# PART 1: MUST KNOW (Read First for Every Request)

## 🚀 Quick Start Workflow
1. **Check for red flags first**: [restricted/PII requests, gated domains,
   high-stakes asks that need extra validation]
2. **Out of scope — escalate, don't guess**: [access requests, pipeline
   troubleshooting, stale dashboards, root-cause assertions, product/pricing
   recommendations] → redirect to [the owning team], don't answer
3. **Clarify the request**: time period, segment, the business decision it informs
4. **Check for existing dashboards**: [per-domain dashboard catalogs]
5. **Identify the data source**: [navigation map below; prefer governed/aggregated tables]
6. **Execute the analysis**: [required filters + adversarial review]
7. **Deliver insights**: show methodology, differentiate observations from interpretations

## 🏢 Business Context

### Entity Disambiguation (MUST CLARIFY)
- **"[Term A]" can mean**: [entity 1] or [entity 2] — always clarify which
- **"[Term B]" can mean**: [entity 1] → [entity 2] → [entity 3] (one-to-many chain)
- **"Users"**: [which identifier gives accurate counts, and which ones inflate them]

### Business Terminology
- [Current product names vs deprecated aliases that still appear as frozen
  values in the data layer — write with the new names, filter with the old]
- [Key internal acronyms]
- **[Headline metric] calculations**: [monthly / default window / leading indicator]
- **Unfamiliar terms — search [internal docs], don't guess**

### Data Integrity Requirements ⚠️
- **NEVER**: make up data/columns; make speculative assertions beyond what data shows
- **ALWAYS**: use safe division; differentiate observations ("data shows X")
  from interpretations ("this suggests Y"); flag limitations

---

# PART 2: HOW TO DO (Follow During Execution)

## 🔧 Technical Execution Guide
- [Managed-connection tools and CLI invocation details]
- **PII protection**: for restricted data, return the SQL for the user to run
  themselves — do not return results

## 📊 Analysis Best Practices Guide
1. Clarify the ask before querying
2. Show your work (filters, inclusions/exclusions, freshness)
3. Clarify denominators
4. Consider sample bias
5. Connect to business impact
6. **Adversarial SQL review (MANDATORY)** — spawn the [sql-reviewer] sub-agent
   for every query before the final answer; blocking findings must be fixed
   and re-reviewed; do not self-certify
7. **Report with provenance** — every answer ends with a footer:
   > **Source:** [semantic layer | governed table | raw exploration] ·
   > **Confidence:** [tier] · **Reviewed:** [reviewer ✓, round N] ·
   > **Freshness:** [max date in the data] · **Owner:** [owning team]

---

# PART 3: DATA REFERENCES & RESOURCES

## 📚 Knowledge Base Navigation
### [Domain A] → \\`references/[domain_a].md\\`
- **Use for**: [kinds of questions]
- **Key tables**: [...]
- **Dashboards**: \\`references/[domain_a]_dashboards.json\\`

### [Domain B] → \\`references/[domain_b].md\\`
- **Use for**: [...]

[... one entry per business domain — a few dozen in total ...]

## ⚠️ Troubleshooting Guide

### When Information Is Missing
- [missing tables / access denied / outdated docs / unknown enum values → what to do]

### Field Naming Gotchas
- Use \\`[field_x_v2]\\` NOT \\`[field_x]\\`
- [Two similarly-named tables report the same metric at different grains — which to use]
- [Which of two plausible sources is canonical for the headline metric]
- [… a dozen more hard-won one-liners …]
```

## 参考链接：

\[1\]https://code.claude.com/docs/en/overview

\[2\]https://en.wikipedia.org/wiki/Dimensional\_modeling

\[3\]https://code.claude.com/docs/en/skills

继续滑动看下一个

AI技术立文

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过