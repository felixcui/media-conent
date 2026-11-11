# 构建稳定的 AI Agent：Harness 工程的核心机制与实践思考

**作者**: 李彬

**来源**: https://mp.weixin.qq.com/s/4fp0WcVZqSPW8exB0VxpIg

---

## 摘要

一句话立论：**Agent = 模型 + Harness，模型负责聪明，Harness 负责稳**。Harness 原意是马具——缰绳、马鞍、护具，让模型“指哪打哪”。作者用团队 Agent 做 text2SQL 与流量分析时的翻车（上下文爆炸、超时、幻觉、权限乱）说明：光调提示词救不了，得管边界、调度和上下文。四个抓手：**约束动作空间**（skill/MCP/权限/重试熔断）、**管理 I/O 与上下文**（数仓分层降维：ODS/DWD 数 T 级 → DWS 百兆 → 按小时分区到几兆；1k+ API 按风险分级，高风险全量、中低风险 TopN 或抽样）、**调度交给确定性系统**（cron 会重复、漏跑、超时，改事件触发）、**状态与记忆持久化**（记忆当资产 + git 管提示词与配置）。落地细节很实：每个操作最多重试 2 次；查询改为导出一次快照、本地聚合；逻辑固化成脚本。效果是 Agent Loop 明显缩短，token 总量虽增但多在缓存读写，**缓存价只有普通输入价的 1/10**。

---

## 正文

李彬 李彬

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycabbn9jlcdBVRd8gOI19zZsnicYPu2F0W3X6f1YoDdKI61AgUgGFo03ljCcJPSz8micWNRqzQKHYchGq9WhgPRkke73MC7nAotF8/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycbZbrxCyEXOKR4a91gM73Bb03VQ7HvHv9c2eXRvU7TY3kKGJuYELtXibicbT9d5h5E4XvPmNshJ6ASamMnu59s5yvojHoS0gkhBM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycbwGicibyuqsKygKumYCKUhiaqWgicl0Nl4ENwTic8ElXad3fwXS6iatVkNpZ0D0s7k8ywKb9cZ1Fib2Sx0egg7u7qtGmOawWLxOoibXrA/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycYKIiaEcJMHyygYUP1LTP99ZYQmZFjwJg8Ycl6G9t7YURbyAWhYh5vzfSTwmNUFXtdQngxQH0BpAO0YtURxnulBzre66QJgBiaxI/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycal3GSfKqIj8jtJuc3xFH2EiacMvmgH5TsmuOFr4eS0ZQTvbjyr9JDE7QzbyGmYPzSu1wgJuMSSG74WLlYviagscyvL6n03tRzZM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycYYibX7V6Ccowpy3B8vMmpGos3JqE0nkaRQfFAzic4nOs1MDLXYcW7uF2Ffjysv76tbgFmICnlhn6KCkAQ4iccFGHgaNibGALjbRwo/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycYT2kVRwibyGNZ6hmWV2ZegG7M9cYWKicLkQlvNEjqVq9p0ehrL83rKcONBuB5SSf8RzsvMvursOS9ibxXaBRdpZmDrPAuA7h1ROc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycbE7amPhTHOrJgdLCfMG7zYvnXqIibqlbicywApRKg4ERn1AqcbwOfLLlsyBeLpibicVRw2gHBAU0SC8ozI6KCiauetQbMEVUtwibglg/640?wx_fmt=png&from=appmsg)<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" style="transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);box-sizing: border-box;" viewBox="0  0 383 263"><svg style="overflow: initial;box-sizing: border-box;" width="72.4096%" height="21.22%" x="13.7989%" y="33.866849397435004%"><foreignObject width="100%" height="100%" style="transform-origin: center center;-webkit-transform-origin: center center;-moz-transform-origin: center center;-o-transform-origin: center center;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);box-sizing: border-box;"><p style="background-image: linear-gradient(45deg, rgb(50, 76, 171) 0%, rgb(186, 211, 253) 100%);color: transparent;-webkit-background-clip: text;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">Harness工程的</span></strong></p><p style="background-image: linear-gradient(45deg, rgb(50, 76, 171) 0%, rgb(186, 211, 253) 100%);color: transparent;-webkit-background-clip: text;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="box-sizing: border-box;"><span leaf="">核心机制与实践思考</span></span></strong></p></foreignObject></svg></svg><svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" style="transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);box-sizing: border-box;" viewBox="0  0 383 263"><svg style="overflow: initial;box-sizing: border-box;" width="72.4096%" height="6.37%" x="13.8%" y="70.252391938587%"><foreignObject width="100%" height="100%" style="transform-origin: center center;-webkit-transform-origin: center center;-moz-transform-origin: center center;-o-transform-origin: center center;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">构建稳定的Al Agen</span></strong></span> <strong style="box-sizing: border-box;"><span leaf="">t</span></strong></p></foreignObject></svg></svg>

**1**

什么是Harness工程？

OpenAI在今年2月份提出 **Harness工程** 的概念，当时非常火爆。

Harness直译是“马具”，诸如 **缰绳、马鞍、护具就是马具** ，不难理解，“马具”是一种让“马”（模型）持续 **更好、更稳地奔跑** 的工具或者机制，Harness核心的诉求在于 **让模型“指哪打哪”。**

那么，什么是Harness工程？Harness工程的价值是什么？Harness工程如何做？

你需要Harness吗？在我看来，Harness一直有必要的。

首先，任务复杂程度，对可靠性、一致性要求高不高。其次，需要考虑的是成本，完成任务有很多种方式，但一定是成本合适的方式走得更远。最后，取决于你把Agent当作autopilot 还是copilot。

**情景一：** 如果你仅仅只需要短期、临时、少量单轮问答或者资料检索，那么一般的模型+System Prompts+RAG基本上就能满足需求，选择一个聪明合适的模型是首先需要考虑的，反而上Harness只会增加使用的复杂度。

**输入 → 处理 → 输出 Harness❎**

**情景二：** 如果你有充足的预算，直接上最强的模型，那么Harness或许只会降低你的上限。

**充足的预算 Harness❎**

**情景三：** 如果你的架构从一开始就是由AI驱动，核心价值直接建立在AI的推理、生成或决策能力之上，那么几个人的小团队不见得会比大公司的产出要低。而现实是，我们现阶段都是围绕模型制作辅助插件、提效工具。

**全套AI Native Harness❎**

相比简单的Prompts+RAG，Harness工程还包括哪些内容呢？在年初，我们围绕从手写SQL到对话Agent开展了提效探索，主要通过团队Agent尝试解决text2SQL和提示词工程执行分析任务两个问题，把人从写查询SQL、查数据、归因分析的重复性事务中剥离出来。

不过随着对团队Agent使用越来越频繁，上下文爆炸、任务执行超时、模型幻觉、权限管理等等各种问题纷纷出现，而通过继续优化提示词已经无法解决，我需要优化Agent约束边界、任务调度方式、管理Agent上下文，这些为了围绕保证模型正常、稳定、高效运行之外的确定层就是Harness工程的主要内容。

**解决问题 ✅ 搞清楚问题 ❎**

前不久，我们组织了一个跨业务线的团队参加了公司内部举办的Agent大赛，将近三个星期的赛程中发现，跑一个Demo很容易，使得模型具备良好的“视力”和“行动能力”，让模型能持续稳定输出才是整个比赛中占据时间最多的部分。

**Agent=模型+Harness，模型负责聪明，Harness负责稳。**

![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycZNUcMq4nVibibGRk16qVI7grLYLXkbbQ5Vo31bTvqLFNbqKmOLBo7aJIdEias0WU2RNk7ShLMJLicjTezCnCwMpJ3gM8pgnyZFhCU/640?wx_fmt=png&from=appmsg)

**图片由Al生成**

**2**

为什么需要 Harness 工程？

我希望大模型能够帮助团队检测恶意攻击、评估风险请求、管理团队记忆。

1.**检测恶意攻击** ：网关日志原始数据量仅一天就有数T，即便是做了数据清洗后也有将近T级别。显然，把这T级别的数据直接扔给大模型，先不说钱和时间，光是上下文就炸了。

2.**评估风险请求** ：没有MCP工具，大模型就没有眼睛。有了MCP工具之后，大模型的注意力应该集中在哪里？我是否应该每次都提醒它下一步应该如何做？

3.**管理团队记忆** ：哪些信息值得被写进长期记忆？假如要扩展Agent平台，记忆如何迁移？

4.**......**

**3**

如何做 Harness 工程？

**·** **约束动作空间** （工具/skill/权限/重试熔断）

**·** **管理 I/O 与上下文** （分层降维、成本）

**·** **调度与触发** （“何时干活”交给确定性系统）

**·** **状态与记忆持久化** （记忆、git 版本）

**01**

**外部工具** **：** **skill&MCP**

出于数据安全考虑，现有的Agent一般运行在沙箱环境。检测恶意流量的第一步是需要让Agent能够 **“看得见”、“够得着”** 真实的数据，对于小规模的数据量，临时地可以用简单粗暴的方法比如手动复制粘贴、上传附件，而对于重复性的任务则需要通过构建稳定可靠skill和MCP工具来实现。固化后的工具可以提升大模型的缓存命中率，降低使用成本。

现阶段，很容易创建一个技能，然而技能不是越多越好，以解决问题为导向，添加、迭代所需要的技能，社区有开发者反馈装了上万个skill，Agent的效果反而变得很差。

比如，通过idp-mcp工具查询Hive数据，ES查询分析技能分析即时的流量，威胁情报技能获取IP情报等等，沉淀 **原子化的能力** 相当于给模型提供了趁手的工具，确保模型能够高效完成任务而不是每次临时现场推理，并且这些工具都是可以重复使用或者很方便复制到另外一个Agent内。

![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycaptVsGvyTrPO8t7Fv8XY7oSeMU2KPbuXiaGGIGicjFerrcS7fSP8pfcW1iapRjp38ibOMWbTsM8Dg1w1wicSR8BH7M6vAMYKrrZa2c/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycYLHlsY9hUxWTlUIWrwvnglC7mKYkseECPJZ8RRnZEk2d4Lq6JuQCKq7b3V0Ev7E4GwSRhBJzVlKKOicnKmvkqRahEPyqxltrk4/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/T6owctB6ycbKkx63IickWzgp7QFUcCHCtsVpx0iasue92Gb1cj0IINXVFUg3eeC7HVEL76NrzDLAib3uSibgDO67LNGHJ7s001tgdZ8DWcT9Lfg/640?wx_fmt=png&from=appmsg)

**02**

**管理上下文 ：** **Manage Context**

开头我们说过，把大量的数据直接扔给模型会导致上下文爆炸，分析的任务要么根本跑不起来，要么耗时巨长。并且长期来看，Agent 平台限制任务执行时间、思考轮次是必然的，在这种背景下，有效的上下文管理是非常有必要的。

那么，有哪些管理上下文的方法呢？以下是我们的经验：

**1）**

数据预计算 / DATA PRECOMPUTATION

**|** **不要把低信息密度的数据直接交给模型，让模型去做高价值的推理、归因。**

我们现在数仓分层模型主要分为三层，其中ods和dwd层的数据都不太适合直接给大模型去分析，我们需要在Agent之外通过数据清洗、特征加工等技术手段分别给这两层数据做清洗、降维处理，而到了dws层，天级别的数据只到了百兆大小的规模，再把百兆规模的数据按小时分区，规模就小了很多。

dws层已经是加工好了的维度指标、事实指标，此时让大模型去处理分析几兆大小的数据就没有多大的问题了。另外，做数据加工并不意味着 dwd层的数据就没有其他作用了，对于dws层细粒度的数据往往还需要专门结合dwd层的明细数据分析。

***程式码区块***

***ods（原始日志）T 级别***

***|***

***dwd（数据清洗、特征提取）T 级别***

***|***

***dws（统计维度）百 M 级别***

**2）**

成本控制 / COST CONTROL

**| 降低 context 压力。**

上面我们提到第一步是让Agent有了原子化的工具，有了工具之后，我们会指挥模型去做相对复杂的任务。我们当然希望模型处理的数据更多、持续干活的时间更长，然而当前阶段如果模型的注意力发散会降低执行效率，token也不是无限消耗的， **在实际中需要模型在注意力方面做取舍。**

**• 被动限制（外部）**

￮ 工具层面：mcp 工具返回有限行数数据、会话连接时长

￮ 模型层面：思考轮次、思考时长

￮ 成本层面：token plan

**• 主动介入（内部）**

￮ 控制查询：技能文档中规定时间范围、查询范围、查询深度；提示词规定

￮ 层次分析：按照优先级，高优先级优先全部分析，中优先级分析 TopN

￮ 抽样分析：低优先级抽样检查

我们的分析任务接入覆盖了 1k+ API，我不能指望模型把所有的接口流量都过一遍，从方法论得需要分个轻重缓急，让它有指向性地去干活。所以，前置地我们利用廉价资源把 dwd 层的流量预先计算出风险等级，然后按照风险等级层次分析的思路，高风险结合 es 全量查询分析，中低风险做层次分析。

**03**

**规划与决策：** **Planning And Decision-Daking**

**1）**

指令系统 / INSTRUCTION SET

最简单的做法是在系统层面注入提示词，比如在 CLAUDE.md 以及./prompts 中做好清晰的定义，这样最大程度上可以保证模型每次都可以按照预先的定义去运行，这类的提示词不需要经常做调整，经常调整反而会让输出不稳定，如果一次性定义好收益是最高的。

**duties.md：**

**￮ 工作模式：** 接收问题后，先思考是否需要调用工具 → 制定分析计划 → 执行工具调用 → 基于结果给出结构化回答

**￮ 内容呈现要求：** 结构化的、约定好的格式

**￮ 工作原则：** 使用什么工具、方案对比、信息来源

**￮ 其他禁止事项**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycauB7J17RJ4Sye4Ca56bEGtd4eMoZNEuOAoSWHaNeibldobwERtORHpiaR1zls5ufQvh2tQmQzxlrKzzhuA3xVcoOa9kOf6eky5w/640?wx_fmt=png&from=appmsg)

**rules.md：**

￮ 防止模型在运行中产生的中间文件随意放在工作空间目录，在 rules.md 中添加提示词，保持工作空间是干净有序的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/T6owctB6ycZtP5NTickdsB40k4sDdAkkicriaeXW0iaEz1n78QBt9NN8NianRtQKrbiaDibHI2n5edLTu4WgOpVCp8WaIc4It0Gsr1ibEe7d27lm8Jg/640?wx_fmt=jpeg&from=appmsg)

￮ 不自作聪明，在没有被 @ 的情况下保持沉默。模型的幻觉有时候不受控制，即便是通过写入记忆也难以根治，对于边界性的约束问题可以在 rules.md中特别声明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycYRDyofGFyR6tIUiaNnXlFlRCyBXianboaib4byhAzbMzSF5MyGh9lWPbdF9ye6np3luoKHpw1BhjgLqjJbA3rhNamQ7TdMNxnVOM/640?wx_fmt=png&from=appmsg)

**2）**

任务调度 / TASK SCHEDULING

**| Agent 不负责判断“什么时候该干活”，调度尽量交给外部确定性系统，分析、推理、归因这些交给模型处理。**

任务调度决定模型何时行动，通常的办法是设定 cron 定时任务，在约定的时间触发执行对应的任务。但是在实际的任务执行过程中，Agent 外围上游的任务完成时间是不确定的，通过定时任务触发往往会造成重复执行、漏执行、超时，造成整体的成功率很低。

我们有尝试过 A2A 方式调用（前期不支持），定时数据探针方式，能解决一部分问题。

后来，我们把任务调度的方式调整为事件触发形式，上游的任务完成之后，再通过事件任务调起模型执行任务，这样模型不再需要去猜测上游什么时候就绪。

![](https://mmbiz.qpic.cn/mmbiz_jpg/T6owctB6ycZM9CdfOfZrAywAGyMq6icE0pI0UeIxAEoRLBG0XyPyoMUUvlYJu6nLygk1mPRb6VKmeIJr4icZnyMsMJkU9JGwKCmI3JeWSiawicE/640?wx_fmt=jpeg&from=appmsg)

**04**

**知识管理** **：** **‌Knowledge Management‌**

重新构建数字分身、Agent 很方便，但如何保证模型的行为一致性却很难，仅仅是复制模型、工具、提示词、知识库会导致模型的行为一致性很差，那么如何帮助模型快速渡过“试用期”呢？

**1）**

记忆管理 / MEMORY MANAGEMENT

在跟大模型交互的过程中，人类更多的是承担 reviewer 的角色，这其中包含了大量带有个人色彩的业务判断、使用偏好、处理流程等私域信息。从业务导向的角度，没有这些前置沉淀的记忆，人类和大模型的“磨合期”会很长，为了让模型能够稳定发挥，建议从一开始就留意记忆管理，并作为长期的资产。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycYFrbponH0TRdWUR7IDWicvibbXaw6s2jL4Ub1QcZUqsOfdjDpaURZyOMCSmrJPiaEwr3jzibkeIPc77RrBn2vCM5VbIiaQWs50r8Mw/640?wx_fmt=png&from=appmsg)

**2）**

版本控制 / VERSION CONTROL

使用 git 管理 agent 的基础文件：系统提示词、记忆文件、启动脚本等等，保证 agent 在迭代中可回溯、团队共享、沙箱重建不丢。

**05**

**运行指标对比** **：Operation Indicator Comparison**

下面，我们对比同模型 qwen3.7-plus 同时段数据的运行指标：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T6owctB6ycYibXSJhGiaqaZH6aX9PlqvVEZQ1PruXCzzuTsG4IFIfu3hqxFbnMhgZEfnOkUiaCJx1t39CvCW6qXAEhQaiaWCznFfAwFcVjEicu9k/640?wx_fmt=jpeg&from=appmsg)

工具调用次数对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T6owctB6ycaLXMHlmxFUVWAU6Nqa4dYt529O8WUHqt8x65ZVQohNT2ibffg1GyhMQ0LQxTmODfLEiaGRb5FiaqPSjDibfo7u6mUJt9oT8UPCZoY/640?wx_fmt=jpeg&from=appmsg)

那么，是哪些调整导致了两次的变化差异呢？

**• 运行调度方式：** 运行改为了事件管线驱动，不依赖 Cron。Agent 不再需要管理和修改自身的调度状态，减少了工具调用步骤。

**• 重试次数熔断：** 新规则中明确指示“每个操作最多重试 2 次，不要反复尝试不同参数格式”。之前任务执行 token 爆炸、运行时间很长，主要是模型把时间和注意力大量花费在解决工具调用失败。

**• 调整查询方式：** 将反复查询的方式调整为导出一次数据快照到工作空间，后续全部本地聚合，消除了重复 Hive 读写和错误重试。

**• 逻辑固化为脚本：** 脚本优先，优先把需要输出一致性高的任务固化为稳定脚本和命令，防止出现口径不一致，还可以节省大模型现场推理的时间。

对比两次同时段的执行任务，第二次任务执行的 Agent Loop 显著缩短、稳定性提高，执行效率明显改善。另外，整体的 token 消耗量有增加，但大部分的增量都来自缓存读取和缓存创建，单任务的 token 成本效率有很大的提升， **缓存命中价格只有普通输入价格的 1/10，** 用少量的成本换取效率的大大提升是划得来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T6owctB6ycYZdeLVDABKG5uKrCQ4KkV52XSAtdQ3zKr5a1VRenh8nFjBuzz4ic245xglvA0LNwWwLgaqWo6UVUvoJ59R63mIQzfhh7U25DqI/640?wx_fmt=png&from=appmsg)

**任务完成率评估**

本质上，还是回到了我们开头提到的： **让模型聚焦于解决问题而不是搞清楚问题。**

**4**

现有的问题

![](https://mmbiz.qpic.cn/mmbiz_jpg/T6owctB6ycbBLTG0uDkzXLTG2Vibd0nQYTbq89mCYyWP29LVp5SWvePHTYXP9naj9oHhK2JJJN7IPmicWf3nq94D03vhy136qMAcVIDpGD3EE/640?wx_fmt=jpeg&from=appmsg)

**5**

展望

除了让模型可以持续稳定地跑起来，Agent 如果一味输出而收不到来自人类的反馈，它有可能会不断自我强化，陷入“死胡同”出不来，如何收集人类真实的反馈、纠正，让 Agent 总结避免再次踩坑是我们下一步的聚焦点。

参考阅读：

1.Harness Engineering for Self-Improvement

2.https://openai.com/index/harness-engineering/

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过