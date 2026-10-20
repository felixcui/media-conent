# 当Coding Agent开始动态并行，软件开发变得更好了吗？

**作者**: 新智元

**来源**: https://mp.weixin.qq.com/s/lKMrDnDkdi60dUF02W2YOw

---

## 摘要

南京大学和UIUC的研究人员对Codex、Claude Code和Kimi Code三种前沿Coding Agent进行大规模配对实验，覆盖354个软件工程任务、2124次执行，发现动态并发在部分长周期任务中收益明显但不稳定，短周期任务中甚至显著降低成功率，并归纳出4大类13子类28种并发失败模式及并发有效的三类机制，旨在探讨Coding Agent应如何协作才能将并行计算转化为软件开发收益。

---

## 正文

新智元 新智元

在小说阅读器读本章

去阅读

### 新智元报道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWGxcbmnyYvqrSqhntcbPdelKBG0JLug4pEX8icjBSe5eib6PekswOSvrq8ybatQJRDr9Vib5WOKaUuibKfLb5qH3J4kEIYmC4NQJU/640?wx_fmt=png&from=appmsg)

Coding Agent正在进入新的发展阶段。过去，它们主要修复Bug、解决GitHub Issue或实现相对独立的功能，SWE-bench等Benchmark已为此建立了成熟评测范式；如今它们开始承担从完整代码仓库生成、跨语言迁移，到需要持续探索与验证的长周期软件工程项目，任务规模和执行时间不断增长，单个Agent的上下文容量、推理能力和执行效率逐渐成为限制。

一种自然的解决思路是让多个Agent同时工作。近年来，Codex、Claude Code和Kimi Code等前沿Coding Agent开始支持动态并发（Dynamic Concurrency）：主Agent在执行过程中自主决定是否创建子智能体、何时创建，以及如何协调它们的工作。

理论上，这种方式能将复杂任务拆分，让不同Agent并行探索、实现和验证。

但问题也随之而来——多个Agent重复调查同一问题，是否只是增加计算开销？不同Agent同时修改相同文件，最终实现是否仍然可靠？子智能体已完成工作而主Agent没有及时整合，并发又是否真正产生了价值？

南京大学和UIUC的研究人员对三种前沿Coding Agent进行了大规模配对实验，覆盖354个软件工程任务、2124次执行，并结合完整的主智能体与子智能体执行轨迹进行分析。

研究发现：动态并发在部分长周期任务中能带来明显收益，但并不稳定，在部分短周期任务中甚至会显著降低成功率；轨迹分析进一步归纳出4大类、13个子类别、28种具体并发失败模式，以及并发真正发挥作用的三类典型机制。

研究想回答的不仅是并发是否有效，更关注Coding Agent究竟应该如何协作，才能真正将并行计算转化为软件开发收益。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYUgS506al2Cl6Cg735ft7gVnE3rzCkYRFD7KlaqXD8iaofeRBiaWoReLkZjjZLCLjl6L5lXgdNfpDveicz9vTCCntX7ibXAzdHgcJs/640?wx_fmt=png&from=appmsg)

论文：https://arxiv.org/abs/2610.10263

研究数据与代码：https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**从静态工作流到动态并发**

多智能体协作并非全新概念。

此前，ChatDev、MetaGPT等系统已探索让多个Agent承担不同角色共同完成软件开发，但通常采用固定协作流程——预先规定由一个Agent规划、另一个实现、还有一个测试，并提前确定信息传递与同步方式。

这种方式被称为静态并发（Static Concurrency），它在任务结构清晰时能提供稳定的执行流程，却要求系统在任务开始前就确定如何拆分和组织工作。

然而，真实的软件工程任务往往具有较强的不确定性：大型代码仓库存在大量隐藏依赖，某些功能看似独立，只有实际探索后才会发现它们需要共享接口、修改相同文件或依赖其他模块的执行结果。

因此，越来越多的Coding Agent从预定义工作流转向动态并发——主Agent根据不断变化的任务状态，自主决定如何委派工作、组织执行和整合结果。

论文研究了三种代表性机制：Codex Multiagent V2在主Agent继续执行的同时动态创建子智能体，并通过消息交换协调；Claude Code Dynamic Workflow动态生成工作流脚本，组织多个具有依赖关系的执行阶段；Kimi Code AgentSwarm批量委派一批不同任务目标的子智能体并行执行，批次完成后返回结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVVbpZcK76ZzGd4XmLpqsxTRC8FY8WF2V2r3ibd8rOplsuGcg4K34CBnBjzUQafVFn3iagPlwMfZZXdvhYBo7XXhnoMM9aqBxNhc/640?wx_fmt=png&from=appmsg)

图1｜三种Coding Agent的动态并发机制（原论文Fig.1）

三种机制都希望利用多个独立的模型上下文扩大执行能力，但也引入了新的系统性挑战：主Agent不仅需要理解软件开发任务，还需要判断哪些工作可以并行、哪些存在依赖，以及不同子智能体的结果能否正确集成。

因此，评价动态并发不能只看系统创建了多少个Agent，更重要的是这些Agent是否真正推进了关键任务，以及它们的工作结果能否有效汇合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**实验设计**

为了系统评估动态并发，研究团队选择了Codex、Claude Code和Kimi Code三种前沿编程智能体，分别比较启用和关闭动态并发时的表现，采用各系统原生支持的并发机制而非统一的外部多智能体框架；对于同一个任务，尽可能保持基础模型、任务要求、执行环境和时间预算一致。

研究主要关注四个长周期软件工程Benchmark：RepoZero涉及代码仓库的跨语言重建，ProgramBench要求根据参考程序和文档重新实现完整程序，NL2Repo关注根据自然语言描述生成代码仓库，LoopsBench则考察需要持续推进、维护任务依赖的软件工程过程。

为了观察任务规模对并发收益的影响，研究还引入SWE-bench Verified作为相对短周期、目标明确的软件修复任务，并按任务难度分层采样，最终选取354个任务。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXNrxiaQorR8ZEGBeEKiaLX3PjnbE9xyzFJfvc7M6ANnDIDCvQzibJdULmlBCxebz8UqmcA1UHIYq7O77icONbcmkfMXjicTP8ODSEY/640?wx_fmt=png&from=appmsg)

图2｜不同软件工程Benchmark的参考实现规模（原论文Fig.3）

每个任务由三种Coding Agent分别在并发和顺序模式下执行，共形成2124次执行，整个实验记录了约112亿Token，按标准API价格计算对应约20,780美元的成本。

除最终任务完成率外，研究还记录测试通过率、执行时间、Shell调用次数与Token消耗，并保存主Agent和所有子智能体的完整执行轨迹。

论文围绕四个研究问题展开：动态并发是否带来收益？Agent如何组织并行工作？并发为什么会失败？什么样的协作能够真正发挥并发的价值？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**RQ1**

**动态并发究竟能带来多大的收益？**

第一个研究问题关注动态并发对Coding Agent整体表现的影响。实验结果显示：动态并发并不是一种能够稳定提高任务成功率的通用策略，但在部分长周期任务中展现出了明显潜力。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVia7icn9fKyDjTicTNaWS7xx8Xd9AJ8Sq5wdbL9HnhsOibL0943306jTo7SMdGBLDlI0UvV3XuguzNX7Zd5JibnChLTGnteySKXqJ4/640?wx_fmt=png&from=appmsg)

表1｜并发与顺序执行下的任务效果和资源消耗（原论文Table 2；Conc.为并发，Seq.为顺序）

## 长周期任务：并发开始展现优势

在LoopsBench上，动态并发带来了较为明显的收益：Claude Code的任务完成率从顺序模式下的7.1%提升至21.4%（提高14.3个百分点），Codex从21.4%提高至25.0%，Kimi Code的完成率保持在25.0%，但平均测试通过率从62.5%提高至66.6%；在NL2Repo上，Codex同样从34.6%提升至57.7%。

然而，这种优势并不稳定：同样在NL2Repo中，Kimi Code的任务完成率反而从57.7%下降至46.2%，不同Coding Agent的并发机制面对相同任务也可能产生截然不同的结果。

## 短周期任务：更多Agent可能适得其反

与长周期任务不同，在SWE-bench Verified上动态并发没有带来整体优势：Codex启用并发前后的任务完成率均为71.0%，Claude Code从83.0%下降至59.0%，Kimi Code从77.0%下降至59.0%。对于目标相对明确、修改范围较小的软件修复任务，额外的任务拆分、通信和协调成本可能抵消并行带来的潜在收益。

从全部354个任务的整体结果看，Codex在并发模式下多完成了8个任务，但提升未达到统计显著水平；Claude Code和Kimi Code的任务完成数分别减少42个和19个，下降具有显著性。

不过，研究也发现即使整体任务完成率没有提升，并发仍可能帮助系统完成某些顺序模式无法解决的任务——例如在LoopsBench上，Claude Code有4个任务仅在并发模式下成功完成。并发虽然未必能稳定改善整体表现，但仍可能提供顺序执行难以获得的额外能力。

## 并发的资源成本同样不容忽视

除了任务成功率，动态并发还显著增加了计算资源消耗，而且并不一定缩短任务完成时间：并发模式的Token消耗达到顺序模式的1.41至3.31倍；15组Agent与Benchmark的组合中，有14组在启用并发后平均运行时间反而增加，例如在SWE-bench Verified上，Claude Code的平均运行时间从17.5分钟增加至27.8分钟，同时任务完成率还出现下降。

不过并发加速并非完全不存在：在366组两种执行模式都成功完成任务的配对结果中，有102组的并发模式运行得更快，其中46组的执行时间至少缩短了20%。

因此，真正的问题不是并发能否提高执行速度，而是当前系统能否稳定地将并行工作转化为端到端收益。

RQ1的核心发现是：动态并发的收益具有明显的任务依赖性——在部分长周期任务中它能改善结果，但额外的计算资源和协调成本，也可能使并发变得低效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**RQ2**

**Coding Agent究竟是如何组织并行工作的？**

第二个研究问题关注：不同Coding Agent究竟如何创建、调度和协调子智能体？研究团队分析了1062条并发执行轨迹，重点观察子智能体的创建数量、实际并发程度，以及它们在任务执行过程中的活动时间。

## 创建更多Agent，不等于实现更多有效并行

研究首先区分了两个容易混淆的概念：累计创建的子智能体数量，与同时存在、执行时间发生重叠的子智能体数量。一个系统可能先后创建20个子智能体，但如果它们基本按照顺序执行，实际上并没有形成充分的并行工作；另一个系统可能只创建5个子智能体，却能让它们同时推进不同任务。因此，仅仅统计Agent数量并不能完整反映系统的并发行为。

研究发现，三种Coding Agent在子智能体调度上存在明显差异：Codex通常维持规模较小的子智能体群组，Claude Code更倾向于通过多个工作流阶段持续创建子智能体，Kimi Code则可以一次性启动较大规模的子智能体批次。

这种差异在高难度LoopsBench任务上尤为明显——Claude Code平均创建约134个子智能体，Kimi Code平均创建约67个，但在子智能体同时存在的数量上，Kimi Code的平均峰值反而更高。此外，任务越难，系统通常越倾向于创建更多子智能体，但这一趋势并不适用于所有Agent和Benchmark。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVYIAsP2PY4he7Oib4WdpqFvB3oe1LmSDwxSvk7Rviaiarx5lbkxeXsAFdI3ftl1N2XFrahfsLBt41yGkYT8Mfttn4J1qCrH2VzfU/640?wx_fmt=png&from=appmsg)

图3｜不同任务难度下的子智能体创建数量及并发峰值（原论文Fig.5）

## 并发什么时候开始，同样重要

除了创建规模，研究还分析了子智能体的启动时间和重叠时长。在确实创建子智能体的执行中，Codex的首次委派通常发生得更早，首次子智能体启动时间的中位数约位于整个执行过程的4.0%，而Claude Code和Kimi Code分别为22.1%和26.0%——因为Codex可以在主Agent继续执行的同时直接启动子智能体，后两者往往需要先组织工作流或任务批次。

但更早启动并不意味着更充分的并发：如果观察至少两个子智能体同时存在的时间占整个任务执行时间的比例，Codex的中位数为23.9%，Claude Code为52.7%，Kimi Code为15.6%——Claude Code虽然启动委派较晚，却维持了更长时间的子智能体执行重叠。RQ2的核心发现是：Agent数量并不等于并发效率，创建规模、执行时机和任务调度方式共同决定了多个子智能体如何协作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWMH4p3fiaSibAoicdia3oKfsgMO8xmwsXeiaeib3NUKkhmibQupBII77l2sRMIPRriaicd94Rd4xiciccQT0I2J0icbzpYIRd9j1knyjWzGIg/640?wx_fmt=png&from=appmsg)

图4｜子智能体在归一化执行时间内的活跃情况（原论文Fig.6）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**RQ3**

**动态并发为什么会失败？**

前两个研究问题揭示了动态并发在性能和调度行为上的差异，但仍没有直接回答：当多个Coding Agent协作失败时，问题究竟发生在哪里？

为此，研究团队深入分析完整的执行轨迹——与仅根据最终测试结果判断任务是否成功不同，研究同时检查主Agent与所有子智能体的任务分配、执行时序、文件修改、信息交接以及最终产物。

团队对全部1062条并发执行轨迹进行人工标注，并结合相同任务的顺序执行轨迹对照，经独立标注与分歧复核，最终形成了一套三级并发失败分类体系：4大类、13个子类别、28种具体失败模式，出现在650条执行轨迹中，共记录804次实例。

需要注意的是，出现失败模式并不等于任务最终失败——部分任务虽然成功完成，但执行过程中仍然存在重复工作、文件冲突或额外集成成本等协作问题。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVGM5fibJasvLormpGmrkQ3yLywObGo6bMHLkZo4ib8NrlIm0xNMvDsxbxN4af4XO6GricOmJl9ybFb5UstujStbqQ8dF8Opy99DQ/640?wx_fmt=png&from=appmsg)

表2｜动态并发的4大类、13个子类别和28种具体失败模式（原论文Table3）

## 任务编排问题：多个Agent同时工作，却没有推进关键任务

任务编排问题（Task Orchestration Problems）主要发生在工作拆分和任务分配阶段，包含三种子类别：Missing Owner（任务缺少负责人）、Pseudo-Concurrency（伪并发）和Load Imbalance（负载不均衡），占全部失败模式实例的28.5%。其中，伪并发是一种具有代表性的现象：系统虽然创建了多个同时工作的子智能体，但真正决定任务能否完成的工作仍然沿着串行路径推进。

例如，在Kimi Code执行ProgramBench中的tailspin程序重建任务时，系统创建了17个子智能体并行调查程序的不同行为，但这些子智能体主要负责调查，没有被安排实际的代码实现任务；主Agent等待调查结果全部返回之后才开始规划具体实现，最终任务在实现规划阶段结束，没有生成可正常工作的替代程序，官方测试结果为0/785。研究还观察到，主Agent过度创建子智能体、将大量执行预算消耗在调查和委派上，最终没有足够资源完成关键实现，是同一类问题的常见表现。

## 执行治理问题：子智能体正在工作，主Agent却没有及时管理

任务分配并不意味着协作已经完成。当多个子智能体开始工作后，主Agent仍然需要持续监控执行进度，决定什么时候接收结果、什么时候介入、什么时候结束任务。执行治理问题（Execution Governance Problems）包括错误的启动或结果汇合时机、失败后的工作丢失，以及主Agent缺少主动监控，占全部失败模式实例的29.0%。

研究中的一个典型案例，是Kimi Code在ProgramBench上重建seqtk（一个用于处理生物序列数据的命令行工具）的过程：主Agent首先完成部分基础代码，随后将22项命令功能分配给20个子智能体并行实现，所有子智能体在11秒内启动。然而，主Agent随后开始等待整个子智能体批次完成，并设置了一个长达两小时的等待时间——而整个任务的执行预算只有40分钟。尽管部分子智能体已经完成工作，主Agent仍然没有及时进入结果集成和最终验证阶段，最终一些关键功能未能实现，程序只通过了440项测试中的92项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYViccOudLHADePW7aQJqWrgibMF4qoo2bxqg7Q2IxwrBm1BPtd3exO19euPH6icHAJneT85mCpv5zurJ4tKMxicLicasKNFicSlq0w78/640?wx_fmt=png&from=appmsg)

图5｜Kimi Code在seqtk重建任务中的动态并发及结果回收问题（原论文Fig.2）

在这一案例中，任务分工本身具有合理性，多个子智能体也确实实现了并行执行，但由于结果汇合时机不合理，已有工作未能及时转化为完整的软件产物。并发系统不仅需要分配工作，还需要在正确的时间管理和回收工作成果。

## 全局上下文管理问题：信息传递了，却没有真正被利用

多个子智能体通常在相互独立的上下文中执行任务，这种方式能让不同Agent专注于各自的工作，但也意味着它们无法天然共享完整的任务状态。全局上下文管理问题（Global Context Management Problems）包括任务要求缺失、接口约定不明确、信息交接负担过重、缺乏全局验证，以及重试时没有继承已有进展五个子类别，占全部失败模式实例的9.3%。

其中，信息交接失败是一个值得关注的问题。例如，在Claude Code执行RepoZero的一个base58迁移任务时，工作流将大量调查结果汇总为一份约8万字符的实现说明，但接收到这些信息的子智能体并没有直接推进代码实现，而是重新开始了部分环境检查、源代码分析和错误调查，最终执行在生成要求的输出文件之前就被中断。这个案例反映出：传递更多上下文并不一定意味着信息能够被更有效地利用——如果交接内容缺少清晰的任务状态、已完成工作和下一步目标，新的Agent仍然可能重复此前的探索；类似地，当不同子智能体独立实现相互依赖的模块时，如果没有提前约定接口名称、数据格式和返回值，也可能导致最终集成失败。

## 共享状态与代码集成问题：局部工作正确，整体协作却出现冲突

这是研究中占比最大的失败模式类别，在804次失败模式实例中占33.2%。共享状态与代码集成问题（Shared State and Merge Problems）主要包括Concurrent Writes（并发写入冲突）和Shared Environment Contamination（共享环境污染）。当主Agent与多个子智能体同时修改同一个代码仓库时，它们可能基于不同版本的文件进行开发，即使每个Agent都在完成自己的任务，修改之间仍然可能发生冲突。

例如，在Codex执行RepoZero的一个Clipper迁移任务时，主Agent已经编写并构建了部分Rust文件，随后一个子智能体又在共享输出目录中替换了相关源代码文件和项目配置，主Agent不得不重新检查当前代码并协调不同实现之间的差异；虽然该案例最终通过了官方测试，但并发写入仍然使主Agent先前掌握的代码状态失效，产生了额外的集成工作。

共享执行环境也会引发类似问题：在Claude Code的clog-cli重建任务中，两个子智能体分别为自己的测试创建临时目录，却使用了相同的路径，其中一个重新创建目录后，另一个原本使用的测试数据随之发生变化，导致它在不知情的情况下继续使用错误的测试环境。

这些问题与传统并发程序中的数据竞争（Data Race）具有一定相似性，但不同的是，在多智能体软件开发中，冲突不仅发生在程序线程之间，还可能发生在多个自主编写和修改代码的Agent之间。这意味着，随着Coding Agent从单智能体走向并发协作，文件所有权、环境隔离和结果集成也逐渐成为影响整体可靠性的重要因素。RQ3的核心发现是：动态并发中的许多问题，并不单纯来自模型自身的编程能力，而是发生在任务分配、执行时序、上下文传递和共享状态管理等协作环节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**RQ4**

**什么时候，动态并发才能真正发挥价值？**

前面的分析揭示了动态并发可能遇到的各种问题，但研究并没有因此否定并发本身的价值。研究团队筛选了131组具有并发收益的配对执行轨迹——这些配对满足至少一个条件：并发模式取得更高的测试通过率、完成了顺序模式未能解决的任务，或者在不降低测试通过率的情况下显著缩短执行时间。通过对照两种执行模式的完整轨迹，研究总结了三类典型的有效协作机制。

## 互补工作：让多个子智能体完成相互补充的工作

当一个软件工程任务能够拆分为多个相对独立、且可正确集成的部分时，并发就可能有效缩短执行时间。例如，在Kimi Code执行NL2Repo的justext任务时，主Agent负责实现核心文本提取算法，8个子智能体分别负责不同的交付文件和检查工作；并发和顺序模式都通过了全部测试，但并发模式将执行时间从约734秒缩短至468秒——互补分工加上主Agent的有效整合，能在保持质量的同时提高效率。

## 并行探索：同时尝试不同方案，再选择更好的实现

动态并发的价值并不仅仅在于将任务拆分为不同部分，有时让多个Agent同时探索同一个问题的不同解决方案，也能够改善最终结果。例如，在Codex执行ProgramBench的Halite程序重建任务时，主Agent和一个子智能体分别尝试构建不同的替代实现：主Agent发现子智能体在地图行为方面的实现具有优势，而自身编写的代码在协议处理方面表现更好，于是将两种实现中的有效部分结合起来，形成了最终解决方案。结果显示，并发版本通过了391项测试中的292项，而顺序版本未能成功构建程序，通过测试数为0。真正带来收益的并不是重复生成多份代码，而是主Agent能够正确比较、选择和整合不同方案。

## 独立验证：通过独立检查发现并修正错误

除了任务分工和方案探索，动态并发还可以通过独立验证改善软件实现质量。例如，在Codex执行LoopsBench的一个安全实验任务时，主Agent负责实现整体实验功能，与此同时一个密码学子智能体独立检查相关实现，并识别出了ECDSA nonce reuse场景中关于P-256椭圆曲线阶数的关键要求；主Agent随后利用这一发现，对整体恢复算法进行了修正，最终并发版本通过了全部检查，而顺序版本未能完成任务。在这个案例中，子智能体并不是简单地替主Agent分担代码编写工作，而是提供了主Agent原本缺少的关键证据，使最终实现能够得到纠正。

需要注意的是，这三类机制来自对具有并发收益案例的轨迹分析，并不意味着它们在所有任务中都能稳定提升成功率。但它们共同揭示了一个特征：并发只有在多个Agent的工作能够被有效利用时，才真正转化为系统层面的收益——无论是互补工作、方案选择还是独立验证，关键都在于主Agent能否将多个执行过程产生的结果整合为更好的最终产物。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**Coding Agent的下一步是什么？**

随着Coding Agent开始承担更加复杂的软件工程任务，多智能体协作正在成为一种重要的系统设计方向。但这项研究表明，支持创建多个Sub-agents，并不意味着系统已经具备可靠的协作能力——一个系统即使能够同时运行大量智能体，也可能因为任务拆分不合理、关键工作缺少负责人、执行结果回收不及时，或者共享代码产生冲突，而无法获得预期收益。

与此同时，实验也说明动态并发并非没有价值：当任务具有清晰的可拆分结构，当多个智能体能够提供不同的候选方案，或者当独立验证能够帮助主Agent修正错误时，并发确实有机会改善任务质量和执行效率。

因此，动态并发的核心问题可能并不是How many agents can work in parallel?，而是 How can agents work effectively together?——也就是如何让多个智能体真正形成有效协作。

从系统设计的角度看，Coding Agent的能力发展正在从单个模型的推理、规划和代码生成，进一步扩展到多个执行上下文之间的任务组织与协调：未来的Coding Agent不仅需要判断如何实现一个功能，还需要理解任务之间的依赖关系，识别哪些工作适合并行，并在执行过程中管理资源、信息和共享状态。

从评测角度看，仅仅观察最终任务是否完成，也不足以理解动态并发的实际价值，还需要分析主Agent如何分配任务、子智能体是否真正推进了关键工作、多个执行过程是否形成有效重叠，以及不同Agent的结果能否被及时整合。当Coding Agent从独立执行走向多智能体协作，真正值得追求的可能不再是更多的Agent，而是更有效的协作。

参考资料：

https://arxiv.org/abs/2610.10263

编辑：LRST

**秒追ASI**

**⭐** **点赞、转发、在看一键三连** **⭐**

**点亮星标，锁定新智元极速推送！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UicQ7HgWiaUb1y6B5OM79TFzpkceWtUkI6LEwv0uYicSoM5Q3I3kDNJhxWdL3tQvbOpU3Ty7icBqnDDNd4CCu4ibiaHw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXslp8AjpoEWRBI3k1eWnQuRPs5PsKZvcRG2BhcQGYXbCN1GoQ5IW6PiaibpNn3M1Al8DvHp5CEZuI9a7cysXduulnTFecmI6xbk/640?wx_fmt=png&from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过