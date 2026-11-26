# AIGC原生视频的双螺旋 Loop Engineering 实践

**作者**: 百度Geek说

**来源**: https://mp.weixin.qq.com/s/YMaj_9Rs6GyUPrfaNgO8dQ

---

## 摘要

百度 APP 研发中心用 Hermes Agent 搭了 Loopy，做 AIGC 视频产线的自我迭代。出发点是一组反例：RRSI 论文的消融实验里，让 Agent 不受约束地递归改进自己，它在演化用的那批题上拿到最高分 92.8，换一批题平均分从 43.6 掉到 40.3，每次试验 token 从 2.42M 涨到 3.80M——约束越少，在自己的考卷上越成功，换考卷越失败，还更贵。真实业务又没有固定考卷：一条视频要过剧本理解、分镜规划、逐镜头 Prompt、生成、合成多段，标准往往看到坏结果才补出来。Loopy 的解法是把产线和裁判拆成两条螺旋：效果螺旋在冻结的标准下修产线，标准螺旋从真实 Good/Bad Case 长出下一版标准；两者共享证据（Case、修复记录、回归结果），但不共享写权限，效果螺旋不能写标准，标准螺旋不能改效果螺旋的结论，单轮之内标准一字不改。早期 Demo 同批样本评估：分镜视频评分提升 7.5%，综合视频可用率从 92% 提升到 100%。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 百度APP研发中心-Link

导读

introduction

今年一篇 RRSI 论文里有一组消融实验：让 Agent 不受约束地递归改进自己的 Harness，它在演化用的那批题上拿到所有版本中的最高分 92.8，换一批题，平均分却从 43.6 掉到 40.3，每次试验的 Token 还多花了一半以上。不加约束的自我改进，学会的是在这场考试里拿分。

今天的自我改进 Agent 都在防这件事，而且押注在同一个前提上：考试本身固定且可信。编码有测试，Benchmark 有标准答案。可大多数真实业务没有这样的考试：客服回复得不得体，搜索结果相不相关，一段文案好不好，很少有人能在第一天写全标准，往往是看到一个坏结果，才发现标准里少了一条。我们做的 AIGC 视频产线也是这样，“人物站位清不清楚”“镜头衔接自不自然”，都是 Bad Case 出现之后才补进标准的。这时裁判必须跟着成长；可只要负责修复的 Agent 也能碰到裁判，最省事的“修复”就是把标准放宽。

本文介绍我们基于 Hermes Agent 构建的 Loopy。它把产线和裁判拆成两条螺旋：效果螺旋在冻结的标准下修复产线，标准螺旋从真实的 Good Case 和 Bad Case 中长出下一版标准。两条螺旋共享证据，不共享写权限；标准可以跨轮成长，单轮之内一字不改。在早期 Demo 的同批样本评估中，分镜视频评分提升 7.5%，综合视频可用率从 92% 提升到 100%。

*全文约 10000 字，预计阅读时间 10 分钟*

GEEK TALK

01

背景：自我改进系统都押注在一场固定的考试上

**1.1 一个反直觉的消融实验**

研究界用 RSI（Recursive Self-Improvement，递归自我改进）描述这样一类系统：AI 把经验和反馈转化为持久的改变，这些改变既提升自身能力，也改进未来的改进过程\[1\]https://arxiv.org/abs/2609.11873。这篇综述把通往 RSI 的路线分成几个阶段：先能执行给定的改进，再能自己制定改进策略、主动获取经验、适应新环境，最后改进“改进方法”本身。

RRSI（Regularized Recursive Self-Improvement）研究的是其中更具体的一层：模型冻结不动，让 Agent 递归地修改自己的 Harness，包括 Prompt、控制流、工具和记忆\[2\]https://arxiv.org/abs/2609.24972。论文在 8 个基准上报告了演化集最多 +6.0、分布外最多 +4.3 的提升。

值得细看的是它的消融实验。去掉全部约束的版本在演化集上得分最高（92.8），分布外平均分却从 43.6 降到 40.3，每次试验的 Token 消耗从 2.42M 升到 3.80M。 ****约束越少，系统在自己的考卷上越成功，换一份考卷越失败，花的钱还更多**** 。

这是 Goodhart 定律在 Agent 身上的样子：一个指标一旦变成优化目标，就不再是好指标。 ****一个能修改自己的系统，最先学会的往往是讨好它的评分方式**** 。

> Goodhart 定律：一句话，当一个指标被当成目标来考核，它就不再是一个好指标了。
> 
> 原话是经济学家 Charles Goodhart 1975 年研究货币政策时说的：任何统计规律，一旦被用作政策目标，就会失效。因为人会对这个指标做出反应，把指标做得好看，而真正的目标没有变好。
> 
> 典型例子：用代码行数考核程序员，结果代码越写越啰嗦；用点击率考核推荐，结果标题党横行。类似的还有 Campbell 定律、指标腐化（metric corruption）。所以做评估时通常得用多个指标互相制约，还要定期检查指标本身有没有被过拟合。

**1.2 RRSI 的解法，和它没有说出口的前提**

RRSI 在两侧加正则化：

- ****提议侧**** ：
- 每个候选允许的修改处数从 3–4 处逐步收紧到 1 处；
	- 每次修改记录依据的假设、diff 和得分，被证伪的想法作为负向证据保留；
	- 连续 3 轮进展落在噪声带内时，转为结构化探索。
- ****选择侧**** ：
- 泄漏审查拒绝写死任务名、数值或答案的修改，也拒绝加入不起作用的机制；
	- 新候选扣除噪声后的得分不能低于当前最优；
	- 同等效果下优先更简单的方案，并定期剪掉多余结构。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4Ue2sGL1nyHibDowbhyegrx0zms5jkmOQxrSsjvRbh5UfSPaAwjYXMxticLsJYiaVW59qRP2Aiac1S9mHj7UibFWMtMX07VevMjiaLc/640?wx_fmt=png&from=appmsg)

## △ RRSI 在提议和选择两侧加正则化，但评估所用的 Benchmark 本身是固定给定的

Loopy 在视频产线上迭代时，也一条条补上了类似的规则，其中不少是出过事故之后才加的（见第 06 节）。 **两边从不同的问题出发，落到了相近的约束上** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7JOd5YKn2tEWCNDoPx4a1epnrFUviaop2ruab82gDiaj7Uv8WMJdAnFajhufgT65WGQDGdC38ia5HDy44domhwT2WiaFRG19sfN9k/640?wx_fmt=png&from=appmsg)

表格最后一行是两者的分界。RRSI 的全部正则化都在防 Agent 钻考试的空子，前提是考试本身没有问题：SWE-bench 的对错不需要重新定义。 ****正则化管住了答题的人，出题的人默认可信**** 。

**1.3 Coding Loop 的考卷是现成的**

这个前提在 Agent 工程里几乎无处不在。Loop Engineering 是近期讨论较多的实践，Addy Osmani 将它概括为“让系统代替人去 Prompt Agent”：系统负责发现工作、分配任务、检查结果、记录进度，并决定继续、停止还是交还给人\[3\]https://addyosmani.com/blog/loop-engineering/。IBM 的介绍也采用了 Goal、Action、Observation、Adjustment 的基本划分\[4\]https://www.ibm.com/think/topics/loop-engineering。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6pz827BNPH3XQjvE9cahiaeAGAXfmQOfrobzDtLyxGZdp7IaHK1dibTgVyquNPBoUROnpcvFExFibtiasxsAZUYpbG62RN8xgnPEA/640?wx_fmt=png&from=appmsg)

## △ Loop 依据外部证据决定继续还是停止

和它配套的是 Harness Engineering：上下文、工具、工作区、权限、状态持久化和中断恢复。可以这样区分两者： **Harness 决定 Agent 在什么环境里工作，Loop 决定它如何依据结果反复改进** 。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy75RqJQWqJwnn1aXGQHTGxics1P7wryicYHYqic1ExdxqiaXjzPBoDYadeBUxOjZI0WcMRJT2pPf3z3xf6qx455vv3BEhRHuiclnlibI/640?wx_fmt=png&from=appmsg)

## △ Harness 负责上下文、工具、状态、权限和恢复

在编码场景里，Loop 的终点几乎是现成的：测试通过、类型检查无报错、性能达标。Agent 改代码、跑测试、看失败、再改，测试全绿时循环结束。按 RSI 综述的划分，今天大多数 Coding Loop 停在第一阶段：目标和测试由人给定，Agent 负责执行。

无论是 RRSI 还是 Coding Loop，Agent 都在学怎么答题。 ****考卷由人提前出好，并且默认正确**** 。

**1.4 真实业务往往没有现成的考卷**

离开编码和 Benchmark，很多业务的验收标准是边做边长出来的。比如一个智能客服，需求里写的是“回答准确、语气友好”；上线后发现用户第二次追问退款时，机器人还在复述政策原文，标准里才多出一条“追问时不能照搬原文”。搜索相关性、营销文案、内容审核都有类似的经历：结果好不好，人一看就知道，可 ****在看到那个坏结果之前，没人想到要把这一条写下来**** 。

我们的 AIGC 视频产线也是如此，而且链路更长、要判断的维度更多。一条视频要经过剧本理解、分镜规划、逐镜头 Prompt 生成、视频生成和合成多个阶段，每个阶段都可能由大模型完成。用户反馈“第三个镜头里两个人的位置对调了”，我们要找齐原始输入、中间产物和日志，判断问题出在分镜、Prompt 还是视频模型，改完重跑，再看新视频里问题有没有消失、别处有没有变差。下次遇到“人物换了衣服”，又从头来一遍。

把这条链路交给 Agent，会碰到三个编码任务里不常见的特征：

1. ****质量判断带有主观性，且标准会变**** 。 动作是否自然、构图是否舒服、人物关系是否清楚，很难一开始就写成完整规则。业务方向、模型能力和审美要求变化后，标准也会跟着变。
2. ****Bad Case 列不完**** 。 今天是动作问题，明天是站位或镜头衔接问题。新的 Bad Case 不仅暴露产线能力的不足，也常常暴露现有验收标准的盲区。
3. ****模型输出有随机性**** 。 有的问题每次都出现，有的只是偶发。一次结果变好，可能来自代码修改，也可能只是这次运气好。

前两条合起来，意味着视频产线和前面那些业务一样， ****最关键的那份考卷，在开始修复时往往还不存在，或者只写了一半**** 。

**1.5 两难：裁判必须成长，又不能被收买**

视频产线同样需要自动发现、隔离执行、独立检查和持久状态。难点落在裁判身上：

- 如果让负责修改产线的 Agent 同时修改验收标准，它可能通过放宽裁判来获得成功。这正是 RRSI 消融实验里的那种失败，只是换成了改考卷；
- 如果永远冻结一份不完整的标准，系统又可能陷入一个永远无法通过、或者通过了也没意义的修复循环。

所以，问题要往前挪一步。产线不仅要回答“是否已经修好”，还要回答“我们凭什么判断它修好了”，也就是谁来评估评估者。

Loopy 要解决的就是： ****当验收标准本身也需要迭代，甚至一开始就不存在时，怎样让裁判成长，又不让它被正在接受评判的一方改写**** 。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7bPqCs6LN5oicFfQicibN0mgI142MOiaeqYiag9gz8KVK26CiaIYia9k85eaqHJlFxiaIyveuK9t6I5K9gsS7yBOGziaYvHicRJJhOnic9DQ/640?wx_fmt=png&from=appmsg)

## △ 编码任务的测试相对稳定；生成式产线的产线能力和验收标准都可能变化，需要分别演进

GEEK TALK

02

双螺旋：产线和裁判分开进化

Loopy 的答案说出来很简单： **把产线和裁判拆成两条螺旋，各自进化，用证据互相推动，谁都不能改写对方** 。

名字借自 DNA 的结构。两条链各自成链，靠碱基对连在一起。Loopy 的两条螺旋也是如此：连接它们的是 **证据** ，包括 Case、修复记录和回归结果；但效果螺旋不能写标准，标准螺旋也不能改写效果螺旋已经做出的结论。

Loopy 的基本判断是：标准不必在项目开始时一次写完，它可以从真实的 Good Case 和 Bad Case 中逐步长出来；但产线修复和标准演化必须走两条相互关联、权限隔离的路径。

> Loopy 这个名字取自 Loop 和 why（y）。
> 
> 普通的 Loop 关心「做完了没有」，Loopy 要求每一圈先回答「为什么（WHY）」：为什么认为问题存在，为什么是这个原因，凭什么判断修好了，为什么还值得再试一轮。答不上来，循环就停下，交给人。
> 
> y 也可以读成坐标系里的第二条轴。普通的 Loop 沿一条轴优化产线效果，Loopy 多了一条 y 轴，留给标准本身。两条轴各自成长，对应第 02 节的效果螺旋和标准螺旋。

**2.1 效果螺旋：在固定标准下修复**

```nginx
Case → 复现 → 冻结 → 修复假设 → 修复 → 工程审查 → 独立验收 → 更好的产线 / 继续决策
```

效果螺旋关心一个具体问题有没有被真正解决。Bad Case 先复现，确认问题确实存在；复现成功后，本轮使用的原始输入、产物、代码版本、验收标准和 Evaluator 全部冻结。修复 Agent 在独立分支中修改允许范围内的产线组件，结果由固定版本的独立 Evaluator 判断。

****这条螺旋的重点在于每一轮都要减少不确定性**** 。验收没通过时，系统不会简单地再试一次，而是要求提出一个新的、可证伪的因果假设；没有新假设，就停下来交给人。

**2.2 标准螺旋：从案例长出验收能力**

```sql
Good / Bad Case → Case Bank → 标准与 Rubric 归纳 → 元评估校准 → 人工晋升 → 新版 Quality Gate
```

Good Case 和 Bad Case 在这里分工不同：

- ****Bad Case**** 告诉系统什么结果不能接受，给出需要修复的负向边界；
- ****Good Case**** 告诉系统人认为什么是好的，以及哪些已有能力在修复中不能被破坏。

这颠倒了通常的顺序。一般是先出考卷再考试； ****在标准螺旋里，考卷是从答卷里长出来的**** 。每个 Bad Case 划掉一片不可接受的区域，每个 Good Case 钉住一处被认可的效果，标准在两者之间逐步收敛。没有人需要在第一天写出完整的质量规范，只需要在看到具体结果时说出“这个不行”或“这个可以”。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7iamicBHiaAvhJcqHU0Vf2yljFRnicJ2yS9PXDnJBleq5iaeVqDZN9THTUobjiapwJBbj4ibkPybSRYVjiaVGLHhPbg28J19XibeZp0T7E/640?wx_fmt=png&from=appmsg)

## △ Bad Case 从上方划出不可接受的边界，Good Case 从下方积累被认可的效果，两者共同收敛出产线标准

我们把标准拆成两层：

- ****Standard**** 描述什么是好的，例如「相邻镜头中同一角色的相对位置应保持一致，除非剧情明确交代了移动」 ****；****
- ****Rubric**** 描述具体怎么判断一份产物，例如从哪些关键帧、哪段 Prompt 中取证，什么情况判 fail，什么情况判 inconclusive。

新 Case 暴露了现有标准没有覆盖的问题时，Loopy 不会在缺少依据的情况下硬评，而是先进入评估能力迭代：基于真实正反样例生成 Rubric 候选，再由独立的元评估器（Meta-Evaluator）检验它能否正确区分 Good 和 Bad。

**2.3 交界处：共享证据，隔离权限**

两条螺旋通过证据相互推动。效果螺旋不断产出新的 Case、修复证据和回归结果；标准螺旋把这些经验整理成更稳定的 Quality Gate；新的 Gate 再回到下一轮修复中。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6icGicBibNdjwZjzWqZmEFMC5WyPcpHqe4f6slNJZJQaibPIo6K2Akib0UCCObV7l9wXvWWAF39ckYYc7yI86kYxv9SZnLLhDnwsnQ/640?wx_fmt=png&from=appmsg)

## △ 效果螺旋把真实案例沉淀进 Case Bank，标准螺旋把晋升后的 Gate 用于未来冻结的评估。产线不能修改裁判，标准不能改写本轮冻结结果

临床试验里有类似的做法，叫预注册：在看到数据之前登记终点指标，事后不能换指标。Loopy 对每一轮修复做的是同一件事。裁判可以变，但只能在下一轮生效， **修复 Agent 永远无法在看到结果之后再挑一把对自己有利的尺子** 。

落到实现上，这是三件互相隔离的事务：正向样例的成长、验收能力的成长、生产代码的成长。每个阶段只拿到完成它所需的最小权限， **跨域操作由服务端合同直接拒绝，不依赖 Agent 自觉** ，也不需要人事后从结果里猜它有没有越权。

GEEK TALK

03

Loopy 的设计与实现

这一节讲 Loopy 怎样把两条螺旋落到工程里。下文会反复出现几个说法，可以对照考试来理解：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy52vB1triaraicm7WgialSyRnoczPicGGk8LsRcjvcFmn9ODy59C0W2vwOxGKBTm0Hy4kXI1HYQBV2xWjOSgsUNPaGJT9fUfeOPouc/640?wx_fmt=png&from=appmsg)

**3.1 整体架构：基座之上的质量合同**

让 Agent 长时间跑起来，今天已经不是难事：Agent Loop、工具调用、记忆、任务调度和跨会话恢复，成熟的开源框架都能提供，Loopy 选用了 Hermes Agent 作为 Agent 基座。 ****真正难的是让一个会自我修改的系统给出可信的结论**** ：Case 以什么证据进入，什么时候冻结，谁能改什么，什么证据才算通过。这些规则如果只写在 Prompt 里，Agent 有能力也有动机绕开它们。Loopy 把它们做成服务端强制执行的合同：冻结包绑定产物哈希和版本摘要，写权限按阶段限定，越权操作在服务端直接被拒绝，不依赖 Agent 自觉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy60Emlpsw6yPpzea0CcYMDq1ic2ibEV5UuyvbM8NsoV7JOlU4DrnFfFc5vd1OpBMtC25ISgwKbic9ZnCdicKOe9dhZCOvG5t3WnX3I/640?wx_fmt=png&from=appmsg)

## △ Loopy 整体框架。Hermes 提供 Agent 基座，质量合同在服务端约束两条螺旋；两条螺旋通过 Case Bank 和 Quality Gate 交换证据，各自的写权限互相隔离

选择 Hermes 的首要原因是 ****长期学习能力**** 。对一条要迭代几个月的产线，学习至少有三层：

1. ****会话延续**** ：任务中断后能恢复，知道已经做到哪里；
2. ****长期记忆**** ：跨会话保存产线信息、历史问题和有效经验；
3. ****行为进化**** ：把验证过的经验整理成可复用的方法，在相似任务中自动取用。
![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy41liazZLbGaSH75DQZkOhtgTSpIePQwGnVqiaQsrd91yroIITUkFxibZlm9g7y45t8USR7MDFCybxdmhRKz75FWrP8NAsMWJalOI/640?wx_fmt=png&from=appmsg)

## △ 从会话延续到行为进化。每一层产出的都是候选，生成候选不等于自动晋升

Loopy 关心第三层。Hermes 把这一层需要的部件放在同一个运行时里：Agent 的长期身份和产线背景、每次会话都要带上的关键事实、按需加载的方法（Skill）、回查完整历史的搜索，以及后台的整理、归档和回滚\[5\]https://hermes-agent.nousresearch.com/docs/user-guide/features/memory。Agent 可以把新方法写成 Skill，写入前可以设人工审批。

LangGraph、OpenAI Agents SDK、CrewAI 等框架同样能编排 Agent，适合输入输出明确的一次性任务；要让同一个 Agent 长期理解一条产线，身份、记忆和经验归纳都得自己重新组装。选 Hermes，我们可以把精力放在证据、独立验收和知识准入上。

**3.2 接入：读懂产线，写一份说明书**

早期我们为每条产线单独写一段适配代码。很快发现这条路走不通： ****每接一条新产线，都要再开发一套专属代码，运行方式、能改的范围和验收逻辑散落在各处**** 。

后来换了思路： ****产线之间的差异不写成代码，而是让 Agent 读懂产线之后，写成一份带版本的说明书**** 。

接入一条新产线，只需要给出产线路径、入口和几组输入输出示例，有现成标准也可以一并提供。Loopy 先做一次摸底（Discovery）：Hermes 在只读环境里读代码、跑样例，然后写出一份 ****产线说明书**** （Runtime Contract），回答这几个问题：

- 产线怎么跑，依赖什么环境；
- 经过哪些阶段，每个阶段的代码在哪里；
- 日志、中间产物和最终输出放在哪里；
- 修复时允许改哪些代码，哪些验收和基线文件不许碰；
- 用什么命令跑测试和回归；
- 还有哪些地方没摸清楚。

说明书带版本号，每次重新摸底都保留历史。之后提交 Case 时直接引用当前版本，用户只需要描述问题。

**3.3 复现：先确认问题存在**

对一个会自我改进的系统，最容易被误认的进步来自随机波动。如果不先确认问题稳定存在，后面的问题修复可能只是这次运气好。

Bad Case 在进入任何修复之前，先在原始版本上独立跑 3 次，看问题是否出现：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4dRZ09sKg4MUYUoWXu9v2q81giaDDRVeTLId8QUUXUib15Le5Exs9UVyWxZqc4w5rXiaaRpNHNpzM2wxGdyCHwibeblFa4J6klHzg/640?wx_fmt=png&from=appmsg)

区分“没复现”和“没跑起来”很重要。 ****运行失败不能被解释成质量结论；没复现也不等于用户报告的问题从未存在**** 。

**3.4 冻结与修复：每轮只验证一个假设**

复现成功后，Loopy 把这一轮要用到的东西全部冻结：原始产物、代码版本、产线说明书、评估器和验收标准的版本，以及这次允许改的范围。每样东西都记下指纹，事后可以核对修复前后用的是不是同一套条件。冻结前还有一道检查： ****当前的验收标准必须能明确判这个 Bad Case 不通过**** 。如果它本来就判通过，或者判不出来，说明考卷还没准备好，先不修（见 3.6）。

修复在一份独立的代码副本里进行，不碰主线。动手之前，修复 Agent 要先交一份 ****修复策略**** ，说清楚：问题最早出在哪个阶段，依据是什么，为什么认为是这个原因，还有什么别的可能，怎样能证明自己猜错了，以及改完后怎么验证效果和回归。

有两类捷径一律拦下：

- ****拿假数据（Mock）证明效果**** 。 假数据只能说明流程没跑坏；Prompt 或模型的表现有没有变好，必须用真实调用或真实录制的结果来证明。
- ****上游缺信息时，下游编一个**** 。 例如上游根本没有给出人物位置，下游就不能补一个默认站位假装修好了。

**3.5 独立验收：修复 Agent 不能宣布成功**

****修复 Agent 只能提交「我认为修好了」的改动和证据，不能自己把 Case 标成已解决**** 。之后有两道独立检查：先由独立的工程审查（Engineering Reviewer）看真实的代码改动，判断改法是否健康、有没有绕开问题；再由固定版本的评估器按冻结的验收标准打分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5NboVFCqQwIcV6mn9Zcphdm8cibibusksCyMwbnK2Ijy9FW4WbtoqkaPqg14zhKMFTvoZl6cHibcNRJibodZURicNOHFkGcoxqxvfU/640?wx_fmt=png&from=appmsg)

## △ 修复 Agent 能改规划、Agent 和 Prompt 等生产组件，碰不到校验器、评估器、阈值和冻结的基线

### 全局回归会回放 Case Bank 里可执行的历史 Good / Bad Case，确认新问题解决了，原来做得好的能力也没被破坏。3.6 补标准：先出考卷，再修产线

这是裁判成长的唯一通道，也是 Loopy 和 Coding Loop 差别最大的一步，我们内部叫 Evaluator Evolution。问题确认存在、却没有一条现成的标准能判它时，Loopy 不硬评，也不放行，而是 **先补一把尺子，再修产线** 。流程分四步：

1. ****起草评分细则**** 。 Hermes 根据质量诉求和已有的正反案例，写出一版评分细则的草稿。
2. ****找一个好样本**** 。 如果手里没有人认可的 Good Case，就在隔离的临时空间里先做一份「好的样子」出来。这一步只产出样本，不改生产代码。人看过并认可后，它才成为第一个 Good Case。
3. ****检验细则能不能分清好坏**** 。 元评估器拿新细则去判这批正反案例：坏的能不能判不通过，好的能不能判通过，有没有只是记住了某个样例的字面内容。没通过时先找原因：细则写错了就改细则，好样本本身有问题就修样本。修样本时保留原有的正确部分，不能另造一个无关的样本。
4. ****人工晋升**** 。 检验通过后，由人决定是否启用，启用后成为新版本的验收标准。

之后，原 Case 回到最初冻结的生产代码上开始正式修复。 **临时做出来的好样本只是参照答案，永远不作为修改的起点** 。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4k62IJdFPKamYp8zPF6ibPmEos6PrnhPGbqm3sgyPoUb96hAuiaH8WdVHDCg5pmLA2uyPbE7B1BNQMOaiahWS5OcJ2JhOyytTCKw/640?wx_fmt=png&from=appmsg)

## △ 好样本在隔离空间生成，只产出样本、不改产线；人工确认和人工晋升各把一道关，元评估通过不等于自动生效

**3.7 继续还是停止（Continuation Gate）：不设固定轮次**

验收没通过时，上一轮完整的评估结果会作为证据交给下一轮。Loopy 不设固定修复次数，也不会因为连续几轮没改善就强制结束。每一轮开始前，Hermes 需要先回答一个问题： **是否还存在一个新的、可证伪、值得再花一次生成成本去验证的因果假设？**

有，就继续；没有，或者缺依赖、需要产品或架构层面的取舍，就停下来交给人，并列出已经试过、被排除的假设。

这和 RRSI 在“进展落入噪声带”时转为结构化探索是同一个判断： **继续的理由必须是新的信息，不能是“再试一次也许就好了”。**

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6oO3iar9pVibEnEVnLsoaoOho9WdiaQUibuQ8JnBYEiaHVm2rU5LiaQhJoXMg20PSXkzqyjHqib6QMGyOBeHpXktHDdQL6gicPrK7zc1k/640?wx_fmt=png&from=appmsg)

## △ 左侧是换措辞、换 few-shot、再跑一次的空转；右侧从失败证据出发，提出新的因果假设，经真实验证后支持或推翻它

**3.8 经验沉淀：通过验收的结果才能进入长期知识**

Case 解决后，Loopy 把完整证据交给 Hermes，整理成候选的记忆、技能或产线知识。只有通过固定评估的结果才有资格成为候选；失败的 Case 只记下已经排除的假设，避免下次重复探索，不当作成功经验。候选还要单独审核，不会因为一次通过就自动生效。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6xUYzlPQdR8avtn8xYvAtC0OKJuzDEvOicyVZDo3nVWdmLjx4mAobbeBT8Kp2hjt08H9sHako7azawdCr5JsfSbmPTTqDTpwp4/640?wx_fmt=png&from=appmsg)

## △ Case 解决后，可信的证据整理成记忆、技能、标准三类候选，经单独审核才生效。代码合入发布和知识晋升是两件独立的事

GEEK TALK

04

实践：一次从零开始的双螺旋

我们选了一条此前没有系统整理过质量标准的产线做接入演示。提交的问题是： ***多人镜头中，分镜 Prompt 只写了角色和动作，没有写清每个人站在哪、彼此是什么关系，相邻镜头里同一角色的位置也没有延续。***

Hermes 先把这段描述拆成两条可观察的质量诉求：镜头内角色位置是否明确，相邻镜头间位置是否发生了无依据的变化。确认后在原始版本上复现 3 次，问题稳定出现。

**标准螺旋先转** 。 现有验收标准里没有任何一条管跨镜头的人物站位，产线也没有可用的 Good Case。Hermes 在隔离空间里做了一份补上站位信息的好样本，经人确认成为第一个 Good Case。第一次元评估没有通过，系统修订样本和评分细则后再次检验通过，验收标准从 v1 升到 v2。 **到这一步，产线代码一行没改，系统获得的是判断这类问题的能力** 。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5uDxtuafztp5NJJNfFdZ4ZonzkTd2pqMCJz2qBrj6OicspOpSjb2fL4rOPo3SxOibMCDtnFn5Y3SOjUay7gzhAW4BWPwZvLsLf0/640?wx_fmt=png&from=appmsg)

## △ 发现标准没有覆盖后，Case 进入补标准阶段，Hermes 正在生成第一个好样本，等待人工确认

**效果螺旋接着转** 。 原 Case 按新标准冻结，在独立副本中修复。前几轮没有通过验收，每一轮的评估结果都作为证据进入下一轮：第 3 轮的反馈指出，某几个时间段的描述缺少身体朝向，同一角色的几个别名也没有对应到唯一的角色形象，第 4 轮据此提出新的修复假设。最终改动通过工程审查和固定评估，Case 标为已解决，人工审核后合入主线。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5D16S2W5P7ewxYafBhdB3n0ia7rtsib1A8ficmYSpLtszqDgZwNPnrqjI2OxQypzMpM4C2uicnkJJPImPmxU1PdwEGCmtGRmS8SN8/640?wx_fmt=png&from=appmsg)

## △ 每轮修复分别记录改动内容、工程审查结论和固定评估结果，上一轮的失败反馈直接成为下一轮假设的依据

整个过程中，人做的决定集中在几处：确认问题，认可第一个 Good Case，元评估失败后选择修订，晋升新标准，决定是否合入。中间的复现、取证、修复和验收由系统推进。

GEEK TALK

05

踩过的坑：哪些约束不能只靠 Agent 自觉

下面几个问题都来自 Loopy 自身的迭代过程，前文的不少规则就是在这些事故之后补上的。它们的共同点是：单看每一步都“合理”，串起来结论却是错的。

**5.1 裁判也会误判：一次分数尺度事故**

一次元评估中，一个已经被人确认的 Good Case 被判为不通过。翻记录发现，模型自己给的结论是“通过、没有问题、score=1”，汇总时却变成了不通过。原因是打分程序按 0-100 的阈值判断，模型用的是常见的 0-1 尺度，1 代表满分，中间没有做换算。

这个错误顺着流程生成了一份错误的复盘结论，系统差点因此去重写评分细则或 Good Case。这件事说明了权限隔离为什么必要： ****裁判自己也会出错，而且错得很像“标准不够好”**** 。如果修复 Agent 能顺手改评分细则，这次换算错误就会被“修”成一份更宽松的标准，而且结论看上去完全正常。

修正时我们刻意没有动评分细则和样例：打分程序在汇总前统一换算分数，同时保留原始分数和尺度；每次元评估同时记下评分细则和评估器的版本；然后用同一份细则、同一组正反样例和修正后的评估器重新跑一次。旧的错误结论保留下来备查。这样才能确认结论变化来自换算修正，而不是换了样例和标准之后得到了一个更容易通过的结果。

****教训：评估器也需要校准和版本管理**** 。 模型写出的结论、结构化的分数和最后的汇总必须一致，修正错误不能抹掉历史。

**5.2 回归通过了，目标没改善，系统却开始下一轮**

早期版本中，固定评估判不通过之后，框架会无条件开下一轮修复，只在任务描述里提醒 Agent 自己判断是否值得继续。结果是它可能沿着同一类 Prompt 改法一直付费跑下去，每一轮都在换措辞。另一个问题是，工程审查要求返修也被记成一次新的修复尝试，次数虚增，工程返修被当成了新的效果探索。

这促使我们把「要不要继续」从修复中拆出来，变成独立的一步（即 3.7 的 Continuation Gate）： ****先复盘已有证据和已经排除的假设，再决定是否开下一轮**** ；工程返修留在同一轮内，单独计数。

**5.3 基础设施故障不是质量结论**

长期运行中，执行任务的进程崩溃、启动失败、超时，评估模型的网络错误，曾经被当成普通的修复失败或需要人决策的问题，白白消耗重试次数。多个调度进程同时调度同一个任务看板时，还出现过任务被互相回收、重复启动的情况。还有一次，修复 Agent 申请了独立副本之外的写权限，污染了主仓库的测试文件。

后续的修正包括：只保留一个调度者，并隔离每个任务的生命周期；统一停止入口；基础设施错误走单独的恢复路径；写权限按阶段由服务端强制限定。只有把 ****质量失败、评估缺陷和执行中断**** 分开，反馈才能流向正确的下一步。

GEEK TALK

06

总结与下一步

**6.1 核心经验**

回到开篇的问题：当产线需要改进、判断质量的方法也需要建立时，怎么组织工作？我们的经验可以压缩成三条：

- ****先造尺子，再修产线**** 。 视频产线的完成条件往往不能预先给定。缺少标准时，先从真实正反样例写出评分细则，经过元评估检验和人工晋升，再进入修复。
- ****裁判跨轮成长，单轮冻结**** 。 两条螺旋共享证据，但不共享修改权限。修复 Agent 不能改裁判，裁判的修正走独立版本，只在下一轮生效。
- ****按证据循环，不按信心循环**** 。 每一轮继续都要有新的可证伪假设；Agent 说完成了不算完成，固定的评估器判通过才算。

回头看，整套设计都从一个判断出发：一个能自我改进的系统，必须同时改进它判断“改进”的方式，而这两件事不能交给同一个执行者。Coding Loop 和 RRSI 可以把考卷当作给定条件；AIGC 产线，以及更多标准边做边长的业务，要让考卷和答卷一起成长，同时保证答题的一方碰不到考卷。

**6.2 下一步**

后续验证会沿两条螺旋分别展开。效果侧，在固定条件下比较重复生成的结果，同时检查目标效果、历史能力和资源消耗；标准侧，比较评估器与人工判断的一致性，观察误判及其适用范围。

人在这个系统里的责任没有消失：提供质量锚点，判断关键取舍，决定什么可以进入生产\[6\]。我们希望积累下来的是一套能持续使用的能力：新问题出现时，有证据可查，有标准可校准，有假设可验证；一次任务结束后，下一次工作可以从已经确认的认识继续往前走。

****参考资料****

\[1\] *The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement*, arXiv:2609.11873, 2026

- https://arxiv.org/abs/2609.11873

\[2\] *RRSI: Regularized Recursive Self-Improvement of Agent Harnesses*, arXiv:2609.24972, 2026

- https://arxiv.org/abs/2609.24972

\[3\] Addy Osmani, *Loop Engineering*

- https://addyosmani.com/blog/loop-engineering/

\[4\] IBM, *What is loop engineering?*

- https://www.ibm.com/think/topics/loop-engineering

\[5\] Hermes Agent 文档：Persistent Memory / Skills System / Curator

- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory

\[6\] Addy Osmani, *Own the Outer Loop*

- https://addyosmani.com/blog/own-the-outer-loop/

END

**推荐阅读**

[System 1 决策模型在Feed场景的应用](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607860&idx=1&sn=1f04106b3b4d662432c293597aa459d4&scene=21#wechat_redirect)

[从代码生成到需求交付：DarkFactory 的工程实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607833&idx=1&sn=46122dcf464df97a601d62e805c5e617&scene=21#wechat_redirect)

[研发Loop的上下文优化与多Agent协作实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607822&idx=1&sn=aff3817a60d009e1427b8ea14823c07a&scene=21#wechat_redirect)

[AI 内容核查怎么做：智能内容 AI 核查系统实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607774&idx=1&sn=fe90aff1e78ff6f023dabeb9dcf2ad63&scene=21#wechat_redirect)

[QCon上海2026：百度 SRE Agent 规模化落地实践解读](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607755&idx=1&sn=936783445cb9453c62b22c7aeb92014b&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过