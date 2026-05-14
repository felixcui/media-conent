# 【深度拆解】OpenClaw vs Hermes：多 Agent 架构设计

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/0GvtgYRJBSietf24K-d7ug

---

## 摘要

1.  **Analyze the Request:**
    *   **Input:** An article titled "【深度拆解】OpenClaw vs Hermes：多 Agent 架构设计" (Deep Dive: OpenClaw vs Hermes: Multi-Agent Architecture Design) and its partial content.。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

> AI训练营 **10期** ， **6月底** 开班，欢迎咨询

无论是 OpenClaw 还是 Hermes 都是多 Agent 的架构，但大家不能“人云亦云”，为什么这么设计其实是很值得考虑的；

不能人家用什么，你也觉得什么好，比如就我去年的经历和学习的文章来看，多数场景下是用不到多 Agent 这种架构的，比如：

```
Cognition / Devin：《Don’t Build Multi-Agents》
```

> 生产级长任务 Agent 的关键是做好 Context Engineering
> 
> 多 Agent 最大的问题是上下文割裂、隐性决策丢失、错误复合、协调成本上升，所以很多场景下不如一个连续、线性的 Agent 流程稳定

只不过《Don’t Build Multi-Agents》也绝不是在否定多 Agent 架构的合理性，只不过他应该在表达这东西工程难度颇高，而多数公司还用不到这么复杂的架构，因为多 Agent 的好处和可以解决的问题是很清晰的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQZutoUoSY5LP85zFMRnMg4mibvtTibql4TvhCJfDeFoibnb5KYVC8MQr8BkpXPFXQyD5pdPAHqWver3azylwKcNGrSoSE2OAOvbc/640?wx_fmt=jpeg&from=appmsg)

毕竟，单个 Agent 在多数场景下表现良好，但随着任务复杂度升高，其局限性逐渐暴露：

- 上下文不断膨胀，关键信息被淹没；
- 工具数量变多，模型更容易选错工具或误用工具；
- 错误影响范围扩大，局部失误可能污染整个任务链路；
- 中间状态缺少边界，任务难以并行、隔离和收敛。

引入多 Agent 架构是解决上述问题的关键思路：将复杂任务拆分为多个拥有独立上下文和权限边界的执行单元，并由上层编排逻辑统一收敛结果。

而为什么 OpenClaw 和 Hermes 要这么设计，其实最大原因是因为他们是 **平台型** 产品，本来就要解决复杂问题，而你的产品要不要启用多 Agent，然后又如何做这类设计，也许今天可以给个答案：

我们会分两部分展开：

1. 多 Agent 的定义、使用动机和常见实现模式。
2. OpenClaw 和 Hermes Agent 的多 Agent 实现路径。

争取将多 Agent 架构给你说清楚，好吧让我们开始吧！

## 什么是多 Agent

在工程实现里，多 Agent 指的是：系统在一次任务处理中创建多个 Agent 实体，让它们分别处理不同子任务，再通过编排层汇总结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySb4ykOVtJHcOZ0IsicC9k4CLdWuCR6Gzt7n9uMTGCDoMFpy9VibnbgbtFqt3sxtwpFdwUlj6Eg63fozriar3vpDdNM6a0nTibicLfY/640?wx_fmt=jpeg&from=appmsg)

一个最小可用的多 Agent 系统，通常至少有这几个元素：

- 一个主 Agent：负责理解用户目标、决定是否拆分任务、最后向用户交付结果。
- 若干子 Agent：在隔离上下文里处理局部任务。
- 一套编排机制：负责创建子 Agent、限制权限、跟踪生命周期、收集结果。
- 一条回传链路：把子 Agent 的结果送回父 Agent，避免主上下文持续膨胀。

## 为什么需要多 Agent

在真实工程任务里，单 Agent 的瓶颈来自两个层面：

**第一个层面是模型自身的能力上限。**

当前模型在处理长序列时，容易在大量历史信息中混淆哪些结论仍然有效、哪些只是中间步骤。这会增加推理成本，也会提高误用旧信息的概率。

此外，长程规划、工具调用准确率、幻觉控制等基础问题仍然存在，并没有被完全解决。

**第二个层面是工程架构的耦合问题。**

如果用一个 Agent 同时完成资料检索、代码阅读、文件修改、验证执行和结果总结，所有中间结果都会堆积在同一个上下文里。状态管理、并发控制、权限校验、失败重试也全部绑在同一个执行单元上。

结果是， **任何局部任务的异常都可能拖垮整个流程，并发请求也难以安全隔离。**

这两个瓶颈性质不同，模型能力的缺陷需要通过模型迭代来缓解，但即使模型变得更强大，只要仍然把不同职责强行塞进一个 Agent， **就算我们从工程角度思考这一定都是正解，但他也一定会增加工程复杂度。**

多 Agent 的做法是把这些职责拆开。常见的结构是：一个父 Agent 负责调度和汇总，多个子 Agent 各自承担聚焦的局部任务，比如只负责检索、只负责阅读某个文件、只负责执行验证。

这样做有四个好处：

#### 1\. 控制上下文范围

子 Agent 可以在自己的上下文里完成局部任务。父 Agent 不需要接收完整执行过程，只需要接收结论、关键证据和必要的状态变化。

父 Agent 的上下文因此更稳定。父 Agent 负责决策和汇总，子 Agent 负责局部执行，中间过程不会全部写入同一个对话历史。

#### 2\. 拆分可并行任务

很多任务本身可以并行处理，例如：

```
边读需求，一边查代码，一边核对测试
同时分析多个模块
同时比较多个方案
让一个 Agent 实现，让另一个 Agent 审查
```

如果全部交给一个 Agent，系统只能按顺序推进，多 Agent 可以把这些工作拆成多个独立执行分支，再由父 Agent 统一汇总。

#### 3\. 按任务限制权限

不同子任务需要的工具不同。

比如：

```
资料检索的 Agent，不需要写文件
局部改动的 Agent，不需要发消息给用户
执行验证的 Agent，不需要继续派生更多 Agent
```

多 Agent 系统可以按任务类型分配工具集，子 Agent 只拿到完成当前任务所需的能力，权限边界更清楚。

#### 4\. 隔离局部失败

子 Agent 可能超时、偏离目标、权限不足，也可能只完成一部分任务。多 Agent 架构可以把这些问题限制在当前执行分支里，由父 Agent 决定重试、丢弃、合并，或者换一个执行策略。

因此，一个可用的多 Agent 实现需要处理：

```
子 Agent 生命周期
超时与中断
结果回传
清理与回收
```

## 常见的多 Agent 实现模式

我们之前也说了，多 Agent 架构会增加系统工程复杂度，所以实现起来是有多套没有固定形态。

工程实现里，常见模式主要有下面几类，实际系统通常会组合使用这些模式：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySUAGNibmgmjwz98P8CLsLuwxMpwPzdhApkx19K38slu1Rx1lkx7yygunIibce8BiaenTmAtkYCh1jL2nm8jJvGHNVl4WfUaiaEZnQ/640?wx_fmt=jpeg&from=appmsg)

#### 1\. 调度-执行模式

调度-执行是最基础的多 Agent 结构，主 Agent 保留用户目标和全局判断权，子 Agent 只处理被分配的局部任务。

```
主 Agent 分析用户请求，判断任务是否需要拆分。
主 Agent 为每个子任务生成明确的目标、上下文和输出要求。
子 Agent 在独立上下文中执行任务。
主 Agent 收集子 Agent 的结果，做冲突处理、信息合并和最终回复。
```

这种模式适合代码分析、资料调研、测试验证、方案比较等任务。它的核心要求是父子职责清楚：父 Agent 负责决策，子 Agent 负责执行。

工程实现时，核心要实现下面的功能

```
子任务描述必须足够具体，否则子 Agent 容易输出宽泛结论。
子 Agent 的返回格式要稳定，否则父 Agent 很难合并结果。
父 Agent 需要能处理失败、超时、结果冲突和部分完成。
```

#### 2\. 分层编排模式

分层编排是在调度-执行模式上继续扩展：子 Agent 不只执行任务，也可以继续拆分任务。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQPiaEEm7piaWurblibzfbeIFLGmLpqibpBOKibJGuP7ltyxS9rGMylcerUXsJczPh04X8Gqiast6dfnECicLBA7AxYCETYpMdlqNYMsM/640?wx_fmt=jpeg&from=appmsg)

这里的调度子 Agent 承担中间调度角色，它接收父 Agent 分配的大任务，再继续拆成更小的执行任务。

这种模式适合任务层级明显的场景：

```
大型代码库分析：主 Agent 分配模块，调度子 Agent 再拆到文件或功能点。
多阶段开发任务：主 Agent 分配功能目标，调度子 Agent 再拆成实现、测试、文档。
复杂研究任务：主 Agent 分配研究方向，调度子 Agent 再拆成资料检索、事实核对、结论整理。
```

***分层编排的工程风险也更高*** ，系统必须限制递归深度、单个 Agent 可创建的子 Agent 数量，以及每层 Agent 能使用的工具。否则任务树会失控，结果回收也会变复杂。

实现这个编排通常需要记录下面的关系：

```
当前 Agent 的层级
当前 Agent 的角色
当前 Agent 的父子关系
当前层级是否允许继续派生子 Agent
```

#### 3\. 专家路由模式

***这个是我实际工作中在用的模式，并且还用得挺深的***

专家路由关注的是 **把任务交给谁** ，系统会根据任务类型，把请求分发给不同角色的 Agent。 例如:

```
搜索专家
代码专家
安全专家
文案专家
```

这些 Agent 的差异包括提示词、工具集、权限范围、上下文输入和输出格式。

专家路由常见于工具能力差异明显的系统，例如搜索类 Agent 需要检索工具和引用整理能力；代码类 Agent 需要文件读取、编辑和测试能力；安全类 Agent 需要更严格的只读权限和检查规则。

工程实现时，路由层通常要处理：

```
根据任务意图选择 Agent 类型。
根据权限策略裁剪工具集。
根据任务类型准备上下文。
根据角色要求检查输出是否合格。
```

这种模式的好处是职责边界清晰，缺点是路由规则需要维护。如果任务被路由到错误角色，后续执行质量会明显下降。

#### 4\. 生成-审查模式

一个 Agent 先产出结果，另一个 Agent 负责审查、校验和找问题，再由主 Agent 或原 Agent 修订。

这种模式常用于代码审查、推理校验和事实核对，主要是提高结果可靠性。

```
- 生成 Agent 输出初版结果。
- 审查 Agent 根据明确标准检查问题。
- 主 Agent 判断哪些问题需要采纳。
- 原 Agent 或主 Agent 根据审查结果修订。
```

这个模式对审查标准要求很高，审查 Agent 应该输出可定位的问题、原因和修改建议。代码任务里通常要包含文件位置、风险级别和复现方式，事实核对任务里通常要包含证据来源和不确定性说明。

生成-审查模式也可以和调度-执行模式组合：一个子 Agent 负责实现，另一个子 Agent 负责审查，父 Agent 负责决定最终合并方案。

#### 5\. Ensemble / Mixture-of-Agents 模式

这一类系统会并行运行多个模型或多个推理分支：

```
多个参考模型并行生成答案
再由一个聚合器做综合
```

它和前面几种模式的区别在于：这里的多个分支不一定是带工具的完整 Agent，也可以是多个模型调用或多个独立推理路径。系统关注的是候选结果的多样性，以及聚合器能否从多个候选中提取稳定结论。

```
多个参考模型或参考 Agent 并行生成候选答案。
系统过滤失败结果或低质量结果。
聚合模型读取候选答案，生成最终综合结果。
```

这个模式适合开放式问答、方案生成、写作改写、复杂推理等任务。它的优势是可以减少单一路径带来的偏差，成本是延迟和 token 消耗更高。

工程实现时，关键点在于聚合器设计，聚合器不能简单投票，而要能识别候选结果中的共同结论、冲突点和证据强弱。

## OpenClaw 的多 Agent 架构

OpenClaw是基于会话系统实现多 Agent 架构，要理解OpenClaw 的多 Agent，可以先看一个问题： **父 Agent 是怎么把任务 交给 子Agent？**

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRWNHSvJ3kbNYFNA33VAvKa7Q3XQAaUrbSiaAtOWEw3ibibXZ9ttI9J7Kk1JDIIKMe61S2zf7Foc2yScCTGIZvrJ4CUgb3d7hxE5E/640?wx_fmt=jpeg&from=appmsg)

OpenClaw 的答案是： **先创建一个子会话，再把这个子会话纳入现有的会话、运行网关、运行时和权限策略体系。**

子 Agent 不是一个临时函数调用，而是一个带会话标识、生命周期状态和工具策略的子会话。

#### 4.1 一次子任务如何跑起来

OpenClaw运行子任务的完成链路:

```
1. 父 Agent 发起子会话创建请求。
2. 系统校验运行时、深度、并发数量、沙箱策略和目标 Agent。
3. 系统生成新的子会话标识。
4. 系统根据父子关系计算层级、角色和控制范围。
5. 子会话的父子关系、角色、工作目录等信息写入会话状态。
6. 运行网关启动这个子会话。
7. 子任务注册机制接管等待、结果捕获、事件回传和清理。
```

这条链路决定了 OpenClaw 的实现边界：子 Agent 不在父 Agent 的调用栈里直接跑完，而是交给会话系统管理。

这样做有两个直接效果：

- 适合跨渠道、跨线程和持久会话场景。
- 权限控制、事件广播、线程绑定、恢复和清理都可以放在会话系统内处理。

#### 4.2 整体架构图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTLtHoRuPfyJWCOBy6QpAO3UCBlMF3cYs4ceh57j3UZbPciambvn1dicJWFjbicBZXImricLF2ldoqeL22fiaRmLlmDuIF7ENPS9miaA/640?wx_fmt=jpeg&from=appmsg)

#### 4.3 处理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTRFXlbMPcgpcERkiaZn7OhcgrUyJ4t4W8Itial4lylxBbfPdybrKCv7ibbxfIyFnaCzLsJJoH68D1RkyY2uSiaS2caBON1M6MEIW0/640?wx_fmt=jpeg&from=appmsg)

接下来是关键设计：

#### 统一入口负责创建子运行时

OpenClaw 把子 Agent 启动收敛到一个统一入口，这个入口不只负责 创建一个子Agent，还会同时处理多Agent 启动所需的控制项：

```
- 子任务使用哪种运行时
- 子任务是一次性运行，还是保留为会话
- 子 Agent 使用隔离上下文，还是继承父上下文
- 子 Agent 是否继承沙箱策略
- 子任务是否绑定到当前线程
- 子 Agent 是否覆盖模型或推理配置
```

这些控制项放在同一个入口里，父 Agent 就不需要分别关心会话创建、线程绑定、沙箱设置和模型配置。

父 Agent 只提交任务和运行参数，后面的运行时准备由框架接管。

#### 角色信息会写入会话元数据

子 Agent 启动前，系统会先计算它在任务树里的位置和权限范围：

```
- 当前层级
- 当前角色
- 能控制哪些子任务
- 是否允许继续派生子 Agent
- 是否允许管理自己的子 Agent
```

OpenClaw 的默认只开放一层子 Agent，并限制单个 Agent 可创建的活跃子 Agent 数量。

默认配置只允许单层并行展开，不会直接放开多层递归委派。

角色推导规则如下：

```
- 第 0 层是主 Agent
- 中间层是负责继续调度的角色
- 最后一层是只执行任务的角色
```

然后这些能力会被写回会话状态，例如：

```
- 子 Agent 处在第几层
- 子 Agent 是调度角色还是执行角色
- 子 Agent 由哪个父 Agent 创建
- 子 Agent 对应的工作目录
```

后续的工具权限、恢复逻辑和生命周期管理，依赖的都是这些结构化元数据。

这些信息 解决了系统如何识别子 Agent 身份的问题。子 Agent 的角色、深度和父子关系进入会话状态后， 其他模块才能在运行时查询它能做什么、不能做什么、完成后应该通知谁。

#### 权限控制同时发生在提示词和运行时

提示词层面，系统会告诉子 Agent：

```
- 你是子 Agent，不是主 Agent
- 只完成分配给你的任务
- 是否允许继续派生子 Agent
- 不要主动轮询，等待完成事件回推
```

运行时层面，系统会根据角色裁剪工具。

按当前实现，所有子 Agent 都会被禁止一部分系统级能力，例如：

```
- 直接控制运行网关
- 查看或控制其他 Agent
- 管理定时任务
- 主动向其他会话发送消息
```

而执行角色还会额外禁止会话浏览和继续派生子 Agent 等能力。

因此，角色不是展示字段，它会直接改变可用工具集。

这套设计把 行为约束 和 工具约束 分开处理。

系统提示词负责告诉子 Agent 应该如何行动，工具策略负责在运行时收窄它实际能调用的工具。前者影响模型行为，后者影响系统边界。

#### 子 Agent 结果通过事件链路回传

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRSWABcNNumqOMy55o1goA5bgsjibH2dBtjBDZlY4woNWMS4UxUbQQShwuibhaE8zM4DTarMTWLdhOtws4jaHL6ujaCvFic6G8kmU/640?wx_fmt=jpeg&from=appmsg)

OpenClaw 没有把子 Agent 的完成结果建模为普通函数返回值。

子 Agent 启动后，系统会把它纳入子任务注册表。后面这套注册机制负责：

```
- 等待子任务完成
- 捕获最终输出
- 判断是否需要投递完成事件
- 处理嵌套子 Agent 的后代完成情况
- 必要时唤醒上层调度角色继续收敛
- 最后清理会话和附件
```

完成事件投递时，系统还会区分两类目标：

- 如果请求者本身也是子 Agent，就把完成事件注入父子链内部
- 如果请求者是顶层主 Agent，并且需要用户可见交付，就走用户交付链路

OpenClaw 的子 Agent 完成后，结果会通过事件投递回目标会话，而不是作为普通返回值直接交给父调用者。

## Hermes Agent：多 Agent 架构

Hermes 是基于进程内委派实现多 Agent 架构，分析 Hermes 的多 Agent，需要换一个视角。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQh3pwjJTeMRRPoQXxibD0d5jHov8Z6vzPA2vwoFMtjDXrFzM33XoBlIIVPr3KvqN05tJgLibwuZXP3KNsib5ia7nwzcmr4egLwrBc/640?wx_fmt=jpeg&from=appmsg)

它没有围绕子会话展开，而是围绕一次任务委派展开：父 Agent 发起委派请求，当前进程里创建一组子 Agent，并行跑完后把结构化结果交回父 Agent。

#### 5.1 一次委派任务如何执行

一次 Hermes 委派会经过这条链路：

```
1. 父 Agent 发起任务委派请求。
2. 系统校验当前深度、并发上限和暂停状态。
3. 系统把一个目标或多个子任务规范化成任务列表。
4. 系统为每个子任务创建新的子 Agent。
5. 子 Agent 继承父 Agent 的工具上限，再按规则裁剪权限。
6. 多个子 Agent 通过线程池并行执行。
7. 所有结果汇总成结构化结果数组返回给父 Agent。
```

所以 Hermes 的多 Agent 更像一次进程内的批量委派。它不依赖独立子会话，核心状态都在当前进程里维护。

#### 5.2 整体架构图

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySVq8akqic4JOeobRxMCicqSdUiaSmGbPY58TQ1JEhLiahico0GMCMBqbv4llE4Siaz489C36NicZ3QHv5VDp3j3yLOcbZQCM7tJ5mHBQ/640?wx_fmt=jpeg&from=appmsg)

#### 5.3 处理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQaEmsu3MLpxd5csGDV6s9zv18BoaIZGVADjG6pREQfRh3xtRtnJAIrlU4fwVSakOKsJIeSauia988FpestSIskwQVJJugkOicto/640?wx_fmt=jpeg&from=appmsg)

接下来是 Hermes 的五个关键设计：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRBVIcPwciaG2UwpQFx1aNQEzcKwaXkYVc0CYhkEzJYqNw1ghWaGYVL6sfM1Pz1eO1FPgaxuIPjic7lP8iafsBYlDaEBklLWq2aUE/640?wx_fmt=jpeg&from=appmsg)

#### 多 Agent 能力封装为一个工具

Hermes 把多 Agent 的主入口定义成一个委派工具，这个工具不只描述参数，也写明了使用约束：

```
- 什么情况下适合委派
- 什么情况下不适合委派
- 子 Agent 不会继承父对话历史
- 输出语言、上下文和事实校验要求要在任务说明里说清楚
```

Hermes 将多 Agent 能力接入现有工具调用框架，没有单独设计会话协议。

这个选择让 Hermes 的多 Agent 接入成本很低，对父 Agent 来说，委派和调用其他工具一样，都是一次工具调用；对框架来说，只需要在工具分发层识别委派请求，再把它转成子 Agent 执行。

#### 子 Agent 是新的 Agent 实例

Hermes 会为每个子任务创建新的 Agent 实例。

Hermes 会创建新的执行单元，但这个执行单元仍然是同一进程内的对象，不是独立会话。

这里的重点是执行上下文隔离，子 Agent 有自己的任务提示词、工具集、任务标识和进度回调，执行过程和父 Agent 分开；运行形态仍然是同一个 Python 进程内的对象，结果最终通过函数返回链路交回父 Agent。

#### 权限继承

如果委派请求里要求额外工具，Hermes 会先与父 Agent 当前可用的工具做交集：

- 父 Agent 没有的工具，子 Agent 无法获得。
- 子 Agent 的权限上界由父 Agent 当前工具面决定。

然后系统还会执行一层强制裁剪，默认会剥离一些不适合下放给子 Agent 的能力，例如：

```
- 继续委派子任务
- 向用户追问
- 写入长期记忆
- 主动发消息
- 执行脚本代码
```

这样处理后，子 Agent 主要通过常规工具执行任务，不会额外嵌套脚本执行层。

这套规则保证了一个边界：子 Agent 的权限不会超过父 Agent。父 Agent 没有的工具，子 Agent 也拿不到；父 Agent 有但不适合下放的工具，也会被强制裁掉。

#### 调度角色

Hermes 对子 Agent 定义了两种角色：

- 执行角色：只执行当前任务
- 调度角色：可以继续拆分任务

调用方传入的角色还会经过运行时校验。

系统会做一次角色降级判断：

- 当前 child depth 是否还没到深度上限
- 是否开启了继续委派能力

只有同时满足，调度角色才会保留继续委派能力；否则就自动退化成执行角色。

按当前默认配置，Hermes 也是单层并行展开。如果不显式提高最大派生深度，调度角色只是一个可选能力，默认不会形成多层递归委派。

这个设计让 Hermes 保留了递归委派能力，但默认不打开深层任务树。对于代码任务来说，这个默认值比较务实：先保证一层并行委派可控，再由配置决定是否允许更复杂的层级结构。

#### Hermes 以同步返回为主，不依赖事件回传

一次委派调用之后：

```
- 单任务：直接运行一个子 Agent
- 多任务：放进线程池并行执行
- 所有子 Agent 完成后，返回结构化结果数组
```

在 Hermes 里，子 Agent 的调用语义更接近同步子调用，不是异步会话加事件回传。

调用顺序如下：

```
- 父 Agent 发起委派
- 等待结构化结果数组返回
- 再继续后续推理
```

这种实现方式缩短了调用链，但更多状态管理需要在当前进程内处理。

这也是 Hermes 调用链更短的原因，OpenClaw 要把结果放进会话生命周期和完成事件投递流程；Hermes 直接等待子 Agent 返回结果数组。链路缩短后，中断、进度、文件状态这些运行期问题需要在进程内补齐。

---

然后说说 Hermes 的运行期保障：观测、中断、文件协调

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySo8evGPHTbVicHLQlSmdg1lQF9pl8wzMh7RNoEhibmctUiaXd1vYacoyhpzhtCXFmBABWpicIQlwnKDUPdx3pKN7RWMHecqQYt5Kg/640?wx_fmt=jpeg&from=appmsg)

Hermes 的子 Agent 都跑在当前进程内，所以运行期保障也必须在进程内完成。这里重点处理三类问题：子 Agent 现在跑到哪了，父 Agent 中断时子 Agent 怎么停，多子 Agent 同时改文件时如何避免覆盖。

#### 记录子 Agent 运行状态

Hermes 会维护一个子 Agent 运行状态表。

它记录：

```
- 子 Agent 标识
- 父 Agent 标识
- 当前层级
- 任务目标
- 使用的模型
- 启动时间
- 工具调用次数
- 当前状态
```

配合进度回调，这些状态可以实时转发到界面或上层网关，例如：

```
- 子 Agent 已启动
- 子 Agent 正在调用工具
- 子 Agent 正在推进任务
- 子 Agent 已完成
```

这样父 Agent 和前端界面都能知道子 Agent 是否已经启动、正在调用什么工具、是否已经完成。对于并行委派来说，这个能力很重要，否则多个子 Agent 同时运行时会缺少可观测性。

#### 中断会向子 Agent 递归传播

当父 Agent 被中断时，系统不会只停止父 Agent 自己，还会把中断继续传给正在运行的子 Agent。

父 Agent 一旦被打断：

```
- 当前线程会收到中断信号
- 并发工具线程会收到中断信号
- 运行中的子 Agent 也会收到中断信号
```

这可以避免父 Agent 已经停止、子 Agent 仍在后台继续执行。

#### 记录文件状态，避免并发覆盖

Hermes 还实现了一套进程级文件状态登记，核心是：

```
- 记录每个任务读过哪些文件
- 记录某个文件最后是谁写的
- 在写之前检查当前内容是否已经过期
```

这套机制处理的是典型的并发写问题：子 Agent B 已经写回文件，但子 Agent A 仍然基于旧内容继续修改。

这套机制会提醒父 Agent：

```
- 哪些文件在它读过之后，被别的子 Agent 改了
- 需要先重新读取文件，再继续编辑
```

Hermes 的多 Agent 同时处理两类问题：如何并行启动子 Agent，以及并行执行后文件状态是否还能保持一致。

#### MoA

Hermes 里还有一个单独的 Mixture-of-Agents 工具。

它不属于层级委派，而是 MoA 结构：首先让多个参考模型并行生成各自的候选答案，然后由聚合模型读取所有这些候选答案，最后基于综合对比输出一个融合了多方优点的最终结果。

Hermes 同时支持两类多Agent：

```
层级式任务委派：负责任务拆分和执行
Mixture-of-Agents：负责并行候选结果加聚合综合
```

最后，我们简单说下两个流行 Agent 平台的差异：

## 结语

今天不写结语了，就说说两个架构的差异：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyToc8GodiciamTtiafv3rBzwk0NsXLeVXHnWOXrWQwLQYdxIDUdp9P2w5xnhz0iaibeBopLwiaOUGBpjxn6WKFo1CxuPLshzd6ePRMNQ/640?wx_fmt=jpeg&from=appmsg)

**OpenClaw 把子 Agent 放进会话边界。**

父 Agent 发起子会话创建请求后，系统创建的是一个新的子会话。这个子会话有自己的会话标识、会话状态、生命周期状态和交付上下文。后续的权限裁剪、结果回传、线程绑定、清理策略，都围绕这个子会话展开。

**Hermes 把子 Agent 放进进程边界。**

父 Agent 发起委派请求后，系统创建的是同一个 Python 进程里的子 Agent 对象。这个对象有自己的任务提示词、工具集、任务标识和执行状态，但它不是独立会话。子 Agent 跑完后，结果以结构化数组返回给父 Agent。

这个边界差异会继续影响结果回传方式，OpenClaw 需要子任务注册和完成事件投递，因为子 Agent 是一个被会话系统接管的运行单元，完成结果要投递回正确的目标会话。Hermes 的路径更短，父 Agent 等待委派调用返回即可拿到结构化结果。

多层委派的实现方式也不同，OpenClaw 把层级、角色和控制范围写进会话状态，再由工具策略按角色裁剪工具。Hermes 则根据当前层级、最大派生深度和开关配置，判断子 Agent 是否还能继续委派。

两者默认都没有放开深层递归委派，OpenClaw 和 Hermes 默认都是单层并行展开。这个默认值说明，两套系统都先保证一层并行可控，再通过配置决定是否允许更复杂的多层任务树。

至于优劣不好评价，因为整体多 Agent 框架我觉得还要进行迭代，现在最优范式还没出来，我个人的话喜欢专家模型。

继续滑动看下一个

叶小钗

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过