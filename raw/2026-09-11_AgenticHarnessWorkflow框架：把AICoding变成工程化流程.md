# Agentic Harness Workflow 框架：把 AI Coding 变成工程化流程

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/6t-NCpm0ucs53EO-rQb3Rg

---

## 摘要

针对把完整需求一次性丢给长上下文Agent所导致的结果漂移、跳过工程步骤、过程不可恢复、缺乏人工把关等问题，作者提出与其打造更聪明的Agent，不如为AI编程套上一副“工程框架”。其自研的Agentic Harness Workflow将开发拆解为需求澄清、方案设计、编码实现、审查验收、提交归档等固定流水线阶段，各阶段由只做一件事的子代理执行，主代理统一调度并管理状态，关键节点保留人工确认，配合状。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 李忠泽

导读

introduction

把整段需求直接丢给 AI 写代码，结果越写越偏、中途断了还接不上？本文作者给出的答案是：别去造更聪明的 Agent，而是给 AI 编程套上一副"工程框架"。他自研的 Agentic Harness Workflow，把一次开发拆成需求澄清、方案设计、编码实现、审查验收、提交归档等阶段，每阶段交给一个只干一件事的子代理，由主代理统一调度把关，关键节点留人拍板；配合状态落盘，中断、换人、换工具都能无痛续跑。文末还附上了完整实战复盘与踩坑清单。

*全文 8019 字，预计阅读时间 6 分钟*

GEEK TALK

01

为什么需要 Harness

相信大多数开发者都亲身体会过，如果把一个真实需求一次性丢给一个长上下文 Agent，会面临如下几个问题：

1. ****上下文膨胀与结果漂移**** ：需求、方案、代码、测试、日志全堆在一个上下文里，越到后面它越容易忘了前面说好的约定，慢慢偏离你最初想要的东西。
2. ****跳过必要的工程步骤**** ：Agent 可能直接写代码，遗漏需求澄清、方案评审或测试设计。
3. ****过程不可恢复**** ：会话被压缩、重启或中断后，很难可靠判断“现在在哪一步、正在等待什么、哪些任务已完成”。
4. ****自动化过程缺少人工门禁：**** 没有明确的门禁和人工确认点，错误方向可能一路运行到最后，之后返工会消耗更多的人力。

所以我的思路是， ****不是"再造一个很聪明的 Agent"，而是给 AI 编码套一副"工程框架"——把一个需求从提出到归档拆成一条固定的流水线，每个阶段交给一个只干一件事的 Sub-Agent，主会话 Agent 负责调度、管状态，并在每个要紧的地方停下来等人拍板。****

GEEK TALK

02

三类应用拓扑对比

从概念上来讲，目前有如下三种结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5mgFpEosaToYBQlCXMuRB4dQWFBy82Kl03x3bXAwxTQNblJsHZJtyzEaHEEwO3dZIb9sibnXtYlg5KMibJtQO3Ym9Cg1ADrzBMc/640?wx_fmt=png&from=appmsg)

我设计的这套 Harness： ****Workflow 为主，阶段级 Multi-Agent 协作，并保留 Human-in-the-loop**** 。

> 注：这里并不是真正意义上的 Multi-Agent，只是目前 Coding Agent 工具，比如 Claude Code、Codex 等自带的 Sub-Agent 能力。

GEEK TALK

03

总体架构

**3.1 一条完整的生命周期**

一个需求沿固定顺序推进：

```cs
init → specify → plan → tasks → test-plan → plan-review  → implement → code-quality → e2e-run → human-acceptance  → commit-push → archive
```

其中， `implement → code-quality → e2e-run` 是自动执行区；其余大多数阶段在完成后会停下来等待用户确认。 `human-acceptance` 和 `archive` 没有独立 Agent，由 Manager 负责呈现、验收和收尾。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy52SUxxsia8LIibSquHznu9S4fR5by4nRj4cia2lIw8OfrxorAgT09IT8xmeZ6THvpQyWJT90fo7UsM3wlMJzE7cLWmpj3KFuWlfI/640?wx_fmt=png&from=appmsg)

**3.2 CLAUDE.md：框架入口与项目知识库**

`CLAUDE.md` 在这套框架里承担两件事：一是 ****框架的入口**** ，二是 ****项目知识库**** 。

****一、框架入口。**** Coding Agent 在会话开始时会自动加载 `CLAUDE.md` ，这是整条链上唯一会被"自动"读到的文件。所以它本身不写任何流程逻辑，只做三件事：点明阶段流程、指向三份规则文件（流转表 `state-graph.json` / 通信协议 `protocol.md` / 状态字段说明 `state-schema.md` ）、以及最关键的一句—— ****主会话必须始终遵循**** `****.harness/rules/manager.md****` 。Manager 的行为准则、状态机字段含义、阶段次序，全都在那几份文件里； `CLAUDE.md` 只负责把它们挂上来，harness 就算 Ready 了。

****二、项目知识库。**** Harness 本体是通用的，但它跑在什么项目上是特定的——有哪些代码库、怎么起服务、连哪个测试库、提交要建什么卡、代码库之间谁依赖谁。这些"项目事实"全部登记在 `CLAUDE.md` 的知识库索引里，目前分四块：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5gQVjYTEoeLrNprrgO9woWU0rIfCMFoWlUIzJHYh91QaCoOY69Ty9TLXcPR4dJt4voicsMgbDxlw56B04tV8iaTQZhfWfC2AZH0/640?wx_fmt=png&from=appmsg)

这里有一个约定： ****只有Manager读 CLAUDE.md，所有Sub-Agent一律不自己读。**** Manager 按当前需求的相关性，从知识库里挑出需要的片段，通过 input 的具名字段下发——比如把环境表相关内容装进 `environment_knowledge` 给 e2e-run，把建卡空间装进 `icafe_space` 给 commit-push，把文档链接装进 `knowledge_refs` 给 plan。

这么设计有三个好处：

1. ****不让每个 Sub-Agent 都把整个知识库吞进上下文**** ——它只拿到与自己这一步有关的那几行；
2. ****Sub-Agent 保持通用**** ——它只认 input 里的字段，不认某个项目的具体布局，所以换个项目只需要换一份 CLAUDE.md， `agents/` 和 `rules/` 一行都不用动；
3. ****知识变更只改一处**** ——新增一个代码库就在表里加一行，不用去改十个 Agent 文件。

还有一条是被实际测试坑出来的原则： ****不假设、缺就问。**** 不同代码库的配置位置和形态可能完全不一样（我们这里有一些服务的配置是在 `conf/servicer/*.toml` ，但那不是通用规则）。某种意义上， `CLAUDE.md` 就是 ****知识层插件**** ： `rules/` 是骨架、 `agents/` 是阶段，都是通用件。

**3.3 调度者：主会话 Manager**

这个 Harness 的核心是 ****主会话 Manager**** 。它一个人分饰三个功能：

- ****调度**** ——决定这一轮该派哪个阶段的 Sub-Agent 执行，是往前走还是往回退。
- ****状态管理**** ——它是唯一有权写 workflow-state 的人，也负责把需求在"进行中 / 挂起 / 已归档"几个目录之间搬来搬去。
- ****对话输出**** ——Sub-Agent 只跟它用结构化协议对话，你只跟它用自然语言对话，两边的话都由它来转。

Manager 有一条我设计的铁律： ****它只认 Sub-Agent 回传的那个结构化协议，不读任何产物的正文（spec、方案、任务、测试、报告），也不读业务代码。**** 它只从协议里取"结论"（通过 / 打回 / 要你确认），从状态文件里取"进度"。

因为 Manager 从不把一堆产物正文和代码吞进自己的上下文，主会话才能在一个需求走完十几个阶段、来回折腾很多轮之后，仍然是轻的、稳的、不飘的。你要是问它"刚才那条结论为什么这么判"，它也不会自己去翻代码回答你，而是把问题重新丢回给当初给出这个结论的子代理，让它来解释。

这里的调度不是单靠 Manager 自己的理解，我们把状态之间的流转设计成了一张“图”，存放在了 `state-graph.json` ，这样 Manager 就很清楚的知道下一个阶段该是什么，并且每一个后置的阶段都可以回退到上一个阶段，这里是通过 Sub-Agent 的“建议”，以及 Manager 对于用户输入的理解判断，共同决定。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy67DTicopKkPDNpNGq0tmCxnfQlPc5vmicapbibiaZR6ibVI2RF2NLxpfiauKCaWDKxXGE7vTBlB0YdK9Mic3zbzXdQSgMklXRqVHnfsg/640?wx_fmt=png&from=appmsg)

**3.4 执行者：阶段 Sub-Agent**

每个 Sub-Agent 有一个独立的 Agent.md 文件来控制这个 Sub-Agent 是做什么的。而每个阶段干什么、产出什么，列个表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7heZdSYeoDoicvfiaU3bDVnicI4YjxdKs2IQNDUfG09HsO7Q1ndqia9Relxe3GXHBQDglwta8icKaC4vLwKbGQnP6vvSKiaR8Qs5qDg/640?wx_fmt=png&from=appmsg)

每一个阶段都会通过定好的 ****结构化输出协议**** 来和 Manager 进行通信，Manager 会将 Sub-Agent 的输出整理呈现给用户，Manager 不用去读取每个 Sub-Agent 的阶段产物，只需要 Sub-Agent 定好一个对人可读性友好的输出即可。

而且这里有一个小设计，就是将“裁判员”和“运动员”分开设计，不让 Agent 自己设计自己评估，分成两个阶段 plan 和 plan-review，由一个 Sub-Agent 进行技术设计，另外一个 Sub-Agent 进行评估，整体设计参考了 ****对抗性**** 的思想，但凡涉及到审查的环节（比如技术设计、测试），都需要挑战设计中的假设，而不是确认正常流程能跑通。

**3.5 状态机：workflow-state**

流程状态不依赖聊天记忆，而是落在每个需求目录的 `workflow-state.json` 中。最重要的字段包括：

- `current_state` ：当前阶段；
- `pending` ：当前等待点，例如等待前进确认、澄清、回退确认、人工验收、推送确认或 CR 评审；
- `states` ：阶段历史、状态和产物路径；
- `review_findings` ：门禁发现的问题及其应跳转的阶段；
- loop 计数、涉及仓库、验收服务等运行数据。

其实这个设计思想就是，我们不应该让 Agent 完全依赖本身自己的上下文记忆，应该有一个 Handoff 机制，我举个例子，如果你当前在用 Claude Code 做到某一个阶段，接下来由 Codex 接手，如果 Codex 不具备 Claude Code 的记忆，那么他其实并不知道当前执行到哪里了，而且尽管在同一个 Coding Agent 内部，如果他的上下文压缩了、Memory 清空或者开了一个新的会话，都可以继续接手执行。

那么整体的交互如下：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6v1iaf2eKVQ0o5BrnOqgo5CrIn4pNBzA7jgU64LmXrXnG6VCZ5wWJSNaCVy65SPmlcQTvRj6tvrRiaM36D8HZkmlYl44wUNX8kc/640?wx_fmt=png&from=appmsg)

**3.6 协议：protocol**

Manager 与每个阶段 Sub-Agent 之间只使用一个协议对象，它是一个 ****双向协议**** ：派发时由 Manager 填请求侧字段，返回时由 Sub-Agent 返回响应侧字段。两侧共用同一套字段约定。

```json
{  "state":        "派给哪个阶段（Manager 填）",  "user_message": "用户这一轮的原话（Manager 填）",  "input":        { "本阶段所需上下文（Manager 填）": "..." },  "status":       "ok | needs_input | fail（Sub-Agent 填）",  "output":       { "结构化结果（Sub-Agent 填）": "..." }}
```

逐个说明：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5hibickib5GgXEDHmyhAAucYE9wAOqMuzjpIGDHr6X60xPWMY22ycxUSCwwO5WvKpBawDx2tHETLVbD1p49Z3H7Qn8AxHfG4pdOQ/640?wx_fmt=png&from=appmsg)

> 注： `protocol.md` 、各阶段模板、业务代码，都是 ****Sub-Agent 自己读**** 的，不由 Manager 传。

3.6.1 请求侧：input

各阶段的 `input` 专属 Key 是提前定义好的，这也是"Sub-Agent 保持通用"的关键：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6AaxOyFwqHhn3X8uUe3KEdpIPYAc3sVBM4zrYrnEj04V5WORBU5mKEmdXrb5R7tibGiaI27cXyrtibD7q8IMIs64lfePcIlBiaWGU/640?wx_fmt=png&from=appmsg)

请求侧三个字段： `state` 是派给哪个阶段， `user_message` 是 ****用户原话逐字透传**** ， `input` 是这一阶段需要的上下文。 `input` ****中每个阶段的 Key 由**** `****manager.md****` ****的调度规则定义**** 。

而且协议里有三个通用可选 Key，只在特定情形出现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6q5v1FBTmA7VX4QsG7zhS8VNJ6tTkgcRRo9UufOaKe14rszbBo1K3bKnYvybEOy4LyC9IpuMpgGPic2enUp0pHbVwuD9XVtq0g/640?wx_fmt=png&from=appmsg)

3.6.2 响应侧：status + output

响应侧只有三种 `status` ：

- `ok` —— 这一阶段做完了，等用户确认后前进；
- `needs_input` —— 没做完，需要人介入（多轮澄清、环境卡住、或要回退到上游补东西）；
- `fail` —— 阶段失败， `output.next_state` 给出建议打回的目标（比如 e2e-run 不过 → `implement` ）。

`output` 里有 ****四个通用字段**** （几乎每个阶段都有），加上各阶段自己的小字段：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4FEsVYFscLMlIOCNOwH2uiaKFfyrLIAP0B8DK8icmicwibKZkAe3XetBib1Y7iby9VsJO2GIhEicnvIFjPYqMoGGpVb8CNhuP5hozWvw/640?wx_fmt=png&from=appmsg)

个别阶段的 `output` 也有自己的专属 Key：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5QAA5T6dlLTqglVWs5loUDIPu58lJnOeghnx54Thibty0G1GbTrUkLmEDc5I7YPaibDKOoNAtzicMo6yAGgB8urWu2hx8hRmvfNk/640?wx_fmt=png&from=appmsg)

> 注：响应侧的信息会包装在一个 `control-result` 里面，这是让阶段 Sub-Agent 结构化输出，Manager 去解析的一个规则。

**3.7 执行到测试的 Loop Engineering**

之前 Codex 发布了 `/goal` 这个命令，实现一个需求，直到 Agent 做完它才会停止，后面也推出了 Loop Engineering 的概念，我的这里其实也参考了这个 Loop 的设计。

Agent 可以自动连续完成 ****“implement 写代码 → code-quality 静态审查 → e2e-run 跑系统测试 → implement 定向修复”**** ，但自动化不是无限循环。我给每条自动修复的循环都设了 ****次数上限**** ，达到阈值后还没过，就停下来把问题呈现给用户，让用户三选一：继续修、直接放行、或者有疑问要阶段 Sub-Agent 解释。

**3.8 阶段回退：判根因、过门禁**

这套框架里 ****所有回退都走同一套机制**** ，不管触发它的是谁：

1. ****用户主动推翻上游**** （做到 plan 才想起需求说漏了）；
2. ****下游 Sub-Agent 报出上游缺口**** （test-plan 发现 plan 没定义接口路由，写不出可执行用例）；
3. ****门禁打回**** （plan-review 审出问题，指向最早出问题的那个阶段）；
4. ****自动执行区的测试打回**** （code-quality / e2e-run 不过 → 回 implement）。

人工验收不通过、或者 CR 评审有意见时，Manager 照一张固定的映射表判目标：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5wA03KKpU1A5DDKGvkA8nYR2E1nzqSqhzw2MyoxGKuVbWtIHxFWLwwvT73H9eWu0xPA1XMrDwibG9wBe1azE4IyCNXibRBGUz0g/640?wx_fmt=png&from=appmsg)

****回退的目标阶段必须在流转表**** `****order****` ****里位于当前之前，且在这个需求的历史里已经真正完成过**** 。这防止"回退"变成乱跳。

校验通过、用户确认之后，Manager ****在同一次写入里**** 完成状态转移：当前阶段落终态、目标阶段由"已完成"改回"进行中"、 `current_state` 指向目标阶段，并把刚才那个回退原因作为 `rollback_reason` 放进目标 Sub-Agent 的 input，让阶段 Sub-Agent 知道这次回来要做什么、补什么。

这里有个细节： ****等待用户确认的期间，当前阶段一直是"进行中"，终态只在真正转移的那一次写入里才落到状态及文件。**** "已完成"严格意味着"用户已经拍板、流程已经离开它"，绝不在等确认的时候提前写。这是为了让 ****冷启动恢复时状态永远是正确的，**** 任何时刻至多一个阶段处于"进行中"，且它必然等于 `current_state` 。

**3.9 Human-in-the-loop：人需要确认的地方**

状态文件里有一个 `pending` 字段，它表示的是每个阶段都要停下来等人拍板， ****每一个类型都明确记着"在等什么、用户确认后去哪个阶段"**** ：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy671icqCsH9h06ib4JpexW4X4ZXRvkuu8FibUdlbZtCR8pSbZc9WHNBzDPFuXH9admHBQu7TrDYdN65FgkiaZues2icMg8KW817pcKM/640?wx_fmt=png&from=appmsg)

GEEK TALK

04

从 Worktree 到验收：多需求如何具备隔离性的工作

**4.1 工作目录结构**

Harness 工作空间目录结构

```perl
<工作目录>/                              ← 主会话（Manager）的 cwd│├── CLAUDE.md                            ← 框架入口 + 项目知识库索引│                                          （环境表 / 研发流程 / 依赖顺序，Manager 从这读取作为 input 下发）├── .mcp.json                            ← MCP 服务（Playwright，给 e2e-run 跑前端）│├── .harness/                            ← ★ 框架主目录│   ├── rules/                           ← 规则与模板（"插件"里的规则层，可替换）│   │   ├── manager.md                   ← Manager 规则（always active，主会话必遵守）│   │   ├── protocol.md                  ← 通信协议（协议结构 + message 话术规范）│   │   ├── state-schema.md              ← workflow-state.json 字段与状态置位时机│   │   ├── state-graph.json             ← 流转表：order（阶段次序）+ next│   │   ├── spec-template.md             ← ↓ 各阶段产物模板│   │   ├── plan-template.md│   │   ├── tasks-template.md│   │   ├── test-plan-template.md│   │   ├── plan-review-template.md│   │   ├── code-quality-template.md│   │   └── e2e-run-template.md│   ││   ├── active/<index>-<slug>/           ← 正在做的需求，全局至多一个│   ├── process/<index>-<slug>/          ← 已开始、挂起的需求│   ├── archived/<index>-<slug>/         ← 已完成归档的需求│   └── worktrees/<index>-<slug>/        ← 本需求的 git worktree 根│       ├── <仓A>/                       ← 每个涉及仓一个子目录（implement 在此施工）│       └── <仓B>/│├── .claude/│   ├── agents/                          ← ★ 阶段（"插件"里的阶段层，加/删/改即改流程）│   │   ├── init-agent.md│   │   ├── specify-agent.md│   │   ├── plan-agent.md│   │   ├── tasks-agent.md│   │   ├── test-plan-agent.md│   │   ├── plan-review-agent.md│   │   ├── implement-agent.md│   │   ├── code-quality-agent.md│   │   ├── e2e-run-agent.md│   │   └── commit-push-agent.md│   │                                    ← human-acceptance / archive 无 agent（Manager 自己管）│   └── skills/                          ← ★ 可插拔能力（"插件"里的能力层）│       ├── huibo-test-mysql/            ← 连测试库│       ├── huibo-test-redis/            ← 连测试缓存│       ├── icafe-card-assistant/        ← 建 iCafe 卡│       ├── icode/                       ← 建远程分支 / 推 CR│       └── get-ugate-token/│├── <业务仓A>/                            ← 主仓（各自独立 git 仓；顶层不是 git 仓）└── <业务仓B>/
```

单个需求目录（ `<index>-<slug>/` ）内部

```xml
.harness/active/<index>-<slug>/├── workflow-state.json                  ← ★ 状态文件（Manager 独占写）│                                          current_state / pending / 各阶段 status /│                                          repos / skip_gates / acceptance_services /│                                          review_findings / 三个 loop 计数├── spec.md                              ← specify 产物├── spec_user_message.md                 ← 用户原话存档（抗上下文丢失）├── plan.md                              ← plan 产物├── plan_user_message.md                 ← 用户原话存档（抗上下文丢失）├── tasks.md                             ← tasks 产物（可勾选清单）├── test-plan.md                         ← test-plan 产物└── reports/                             ← 审查与测试报告    ├── plan-review.md                   ← 惰性：只有打回过才产    ├── code-quality.md                  ← 每轮追加    ├── e2e-run.md                       ← 每轮追加    └── screenshots/                     ← e2e-run 前端 TC 的 Playwright 截图        └── TC-003-xxx.png
```

**4.2 需求空间隔离**

我们设计这个框架，本质是希望可以兼容多需求并行的场景，所以这里的设计是用了 `git worktree` ，在 `Implement` 阶段之前，Manager 根据 `tasks` 阶段产出的仓库集合，为每个业务仓建立同名特性分支和独立 worktree。实现、静态审查和 e2e 都复用同一 worktree；修复轮不重建，归档时才清理。这样就让多个需求之间完全隔离，我们的根目录下面，只需要有全部的代码库，而且每个代码库都及时同步 master 分支保证最新的代码，每个需求会根据当前最新代码新建 `git worktree` ，而且每个需求下都有自己的 `workflow-state.json` 及阶段产物。

这个设计有三个直接收益：

1. 主工作区不被临时产物污染；
2. 代码审查看到的是同一份改动，而不是每轮重新推导的快照；
3. 中断或回退后可以继续已有任务，已勾选的 task 不需要重复执行。

**4.3 提交代码的依赖关系**

`commit-push` 分为两段：

1. `prepare` ：整理改动、建立 iCafe 卡、生成提交确认表；
2. `execute` ：用户确认后才真正 commit、push 和创建 CR。

CR 评审由人工完成，Harness 只根据评审结果继续下一层或归档，不代替评审者合入主分支。归档阶段负责停掉验收服务、迁移需求目录、删除 worktree 和已合入分支。

多仓代码库一般会有一个公共库的设计，这样避免同一份代码文件散落到不同代码库中需要多份维护，所以我们在 `commit-push` 做了一个特别设计，我们的代码库依赖关系会写到 `CLAUDE.md` ，Manager 会把这部分内容带给 `commit-push` ， `commit-push` 会先提交依赖代码库的 CR，然后等待用户反馈是否合入（因为目前 icode CR 还需要人工 +2，或者如果有 Skill 能直接去 icode 拉取评分，这块可以改成自动化），合入了之后，会派发 `implement` 去修改其他代码库的依赖关系（比如 `go get xxx@latest` ），这里有一个设计就是在 `implement` 阶段加了一个可选 Key `skip_gates` ，这样刚才介绍的“执行到测试的 Loop Engineering” 就可以只执行然后直接跳过测试（因为本身也存在一些自测需求或者小的改动，不需要进行复杂的 e2e 测试）。等这部分准备好后， `commit-push` 会继续提交其他仓的 CR。

GEEK TALK

05

DeepSeek Harness："Everything is a Plugin"

DeepSeek Harness 是 2026 年 8 月开源的一套 Agent 框架（MIT 协议，命令行叫 `dsh` ），它最核心的一句话就是 ****"everything is a plugin"（一切皆插件）**** ：模型、工具、技能、会话、沙箱、存储、循环、调度、连 UI，全都是可以随意替换的插件；甚至 ****驱动每一轮对话的那个 agent loop 本身，也是一个能从配置里换掉的插件**** 。它的哲学被总结成一句很妙的话——"从一个已经能用的完整 Agent 出发去替换零件，而不是从一堆零件出发去攒一个 Agent"。底层它还有一条 append-only 的会话日志，resume、fork、replay 都基于这条事件流。

在这几个月我逐渐研究 Harness Engineering 的时候，我觉得这个东西也应该是一个 ****“框架”，**** 如果这个 workflow 实现了，那么其中所有的 ****“组件”**** ，不管是需求澄清还是实现代码的 Agent 都可以被替换，用户也可以根据自己的设计添加 Hook、Tools、Skill 包括 `CLAUDE.md` ，这些 ****“组件”**** 都可以根据业务自身去做定制化，包括这套设计， ****中间是一个极简、几乎不动的核心（Manager），外面的一切都是可以替换、可以定制的"文件插件"。****

具体到能换什么：

- ****每个阶段都是插件。**** 一个阶段就是一个 markdown 定义的 Sub-Agent 文件。你想改某个阶段的行为，就改那个文件；想加一个新阶段（比如插一道"安全审计"），就加一个 agent 文件、在流程表里排上；想去掉某个阶段，删掉就是。
- ****能力（skill）是插件。**** 查库、连缓存、建 iCafe 卡、推 iCode CR、用 Playwright 驱动浏览器……这些都是按名字挂上去的 ****可插拔**** 技能。
- ****规则和知识是配置。**** 通信协议、流程次序、状态字段、各阶段模板、以及项目知识库（哪些仓、怎么起服务、连哪个库），全是框架外的文件。流程次序想调整，就改流程表那个文件；换个项目，就换一份知识库，核心逻辑照旧。
- ****进度也是可恢复的。**** 前面说的"状态全落盘"，本质上和 DeepSeek 那条 append-only 会话日志是同一个诉求——让流程能被恢复、被接续。

当然也有不一样：DeepSeek Harness 是个通用的 Agent 运行时，连 agent loop 都能换；我这套是 ****专门为"编码这件事的生命周期"定制的、带固定阶段流水线的 Harness**** 。但在这条流水线内部，阶段、能力、规则、知识确实都是可替换、可定制的插件—— ****Manger 极简、阶段技能皆可换**** ，这一点是共通的。

GEEK TALK

06

一次真实的冒烟测试

我按一个真实需求，把整条流水线从头到尾跑通的记录。我特意覆盖了各种路径：正常前进、多轮澄清、中途改需求回退、门禁打回后逐级复审、自动执行区的打回-修复循环、冷启动恢复、提交建 CR、最后归档。这是一张总览：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4yhLJYpo9niaAyNIt7oId60oRPUzZvbMmSFkI6fzK6eyIAYLc6SZW4ganCGG7fkC2LZiasOISn0JccLGmZ7rvOVfIhZGLNx5K2E/640?wx_fmt=png&from=appmsg)

具体耗时：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4Ao1R4CPAsSzB1GAzQJ22bm6wJhAQtGs0KxV2y7KrK9Y1ZMfp1QUEWsHFficaL3DBcwz2Pt3fGO9dhZJeVVoRc2Dv3VM8ibaoCM/640?wx_fmt=png&from=appmsg)

GEEK TALK

07

还没解决的问题，和接下来想做的

跑下来也踩到不少坑，如实记在这儿，也是后面要改的方向。

****1\. Sub-Agent 每轮都在重新加载上下文。**** 那些需要多轮澄清的阶段（比如 specify、plan），子代理每一轮都得把 ****它默认要读的那批东西重新加载一遍**** ，挺浪费。想法是复用类似"Sub-Agent 会话 ID"的机制，这一点其实我发现在使用 Claude Code 的时候，如果在某一阶段，提问类话术，Manager 会自动找到上一个 Sub-Agent 的会话 ID 继续，让同一阶段的多轮交互延续同一份上下文，而不是每轮重来——这其实也是 Multi-Agent 架构可以解决的，只是现在的调度还没做到这一层。

****2\. plan 阶段没有搜索边界，容易超时。**** plan 实测跑到过一个小时，严重超时（这里声明不是每次，而且有的时候是模型首包延迟过长）。plan 的活确实需要读代码，但现在的规则只是让它"自己去 Grep/Read"，没划边界。 ****得给它补上知识库，利用渐进式索引，让 Agent 能快速定位、定位的准、读得少**** ，本次允许读哪些仓、最多翻多少文件、调用链最多追几层、多久没收敛就该停、范围太大时该反过来问用户什么。

****3\. 产物和状态不是原子完成的。**** 实测碰到过：test-plan.md 已经在、也标了 Ready，但重新进流程时 Manager 很难判断——文件到底完整不完整？是 Sub-Agent 其实做完了只是结果丢了？该不该覆盖？能不能直接往下走？ ****得把"写产物"和"改状态"做成原子的、可校验的一步**** ，重入时才能可靠判断某阶段到底完没完成。

****4\. Manager 越界替用户答疑。**** 审查类阶段（比如 plan-review）会把打回结论和理由抛给用户；用户一有疑问，Manager 有时会自己跑去读代码来解答。这其实破了"Manager 不读正文/代码"的规矩，正确做法是把疑问回灌给出结论的 Sub-Agent 去解释（这条后来已经在规则里收敛掉了，经过几次测试发现不会产生）。

****5\. 前端设计需要更多能力兜底。**** 研发自己做页面，难免缺前端设计的详细描述，又不能全交给 AI 自由发挥。我实测第一次 AI 设计的界面就过度复杂了——功能是实现了，但交互和样式都不够简洁。这块可能得让前端或设计介入，提供一些前端实现/设计规范类的 Skill 来约束。

****6\. 云端 memory 的自进化还没做。**** 我理想中的 Harness Engineering，应该是每跑完一次流程，就把这次遇到的实现问题、测试 bug 沉淀下来——我之前看到过一个说法大概是这个意思，面对 bug， ****第一优先级不该是让 AI 去想"怎么修这个"，而是"怎么让下次不再产生"。**** 现在虽然跑完会往本地 memory 里存，但换台机器这部分就丢了，得做一个 ****云端共享的 memory**** ，让经验能跨机器、跨会话攒起来，真正形成自进化的闭环。

****7\. 工作目录的结构设计对团队使用不友好。**** 目前虽然我将所有内容都放在了一个 git 仓库，但是使用却不是这么用的，曾经看了其他团队的文章，使用了 `git submodule` 的方式， ****本项目的这个设计放在 git 上是作为云端存储，在本地，当前工作空间的根不能是一个.git 目录**** ，后续应该维护成一个团队友好的 WorkSpace 目录。

****8\. 未建立完善的线上运行的可观测性日志与监控。**** 现在框架的产物其实只有两类：一是各阶段的产物与报告（spec / plan / 审查报告 / 测试报告 / 截图），二是状态机文件里的状态快照（当前在哪、在等什么）。这两样可以做到"单个需求怎么走完的"， ****但无法观测某个阶段是否执行的正确，调用链路、读取内容是否符合预期，就跟传统线上业务，需要有监控、日志、报警一样，Agent Workflow Framework 同样需要具备这些能力**** （可以自定义 Hook 或者 Coding Agent 内部的 Hook 去采集）。

END

**推荐阅读**

[什么样的业务经验值得做成 Agent：从个人工具到组织资产](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607581&idx=1&sn=521aae445a57ce0d9bd885654b09bea4&scene=21#wechat_redirect)

[都在开源 Harness，Codex 和 DeepSeek 到底有什么不一样？](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607560&idx=1&sn=377945189293dcd34a7b23fd6256e40d&scene=21#wechat_redirect)

[dsh 还不够成熟，但它重新设计了 Agent 的运行时](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607525&idx=1&sn=7b241ae844be1da555047bb61d581e1e&scene=21#wechat_redirect)

[Workspace 实践：从个人提效到组织提效](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607508&idx=1&sn=f604f409314f249297faae6d83bd3382&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过