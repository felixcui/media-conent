# 如何用 Codex 强兼 Claude Code 生态（并被它教做人）

**作者**: EstreWolf

**来源**: https://mp.weixin.qq.com/s/d_0sQkWWrb5iuGF4ZI5VVg

---

## 摘要

本文介绍了作者将Codex接入已有Claude Code生态的方法与背景。为解决两个Agent私有配置导致的状态分叉问题，作者设计了三层分离架构：Claude私有层、Codex私有层以及中间的共享契约层，核心铁律是严禁跨写对方私有层，所有协作均通过共享层完成。

---

## 正文

EstreWolf EstreWolf

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/wKzK3OYjZQeRLPlbhnKq3NqSjgnU1hoAd72A6Uzf3oso4ZHTtS8FqvcjXmicHaEtJKG2KEYu68WgZnEHgd5DJhzajHQQNyOpVx0V7XeRvq1U/640?wx_fmt=png&from=appmsg)

## 写在前面：

\- 我的 Claude Code 已经攒了一整套生态：memory、skills、vault、hooks，全是过去几个月一点点搭起来的。

\- 但Codex在模型和产品的更新下，体感和Claude Code五五开，甚至在某些领域更强，但它对我之前搭好的生态一无所知。这篇文章记录我怎么把 Codex 接入这套生态，以及把设计文档丢给它做 review 时，它怎么三次抓出我自己看不见的设计漏洞。

\- 你甚至可以把这篇文章丢给Codex，让它自动强兼Claudecode

---

## 1\. 背景：为什么需要两个 Agent

我日常用 Claude Code 做产品思考、知识管理这类需要深度判断的工作。但伴随着opus降智，codex迭代，我感觉，有些时候Opus4.7真不如Gpt 5.5好用吧，并且我开始产生大量的coding工作了；

问题来了：两个 Agent 各有一套私有配置（`.claude/` 和 `.codex/` ），但它们服务的是同一个人、同一套知识库、同一批任务。如果不做协调，Claude 刚做的决策 Codex 不知道，Codex 改完的代码 Claude 下次开会问"上次改到哪了？"。两边各自维护一份"用户画像"，两周后就分叉了。更麻烦的是两个 Agent 可能同时改同一个配置文件，谁覆盖谁没有规则。

云端的多 Agent 编排（LangGraph、CrewAI）解决的是不同问题，它们协调的是同一个运行时里的多个角色。我的场景是两个独立运行时，各有自己的启动链路、记忆系统和工具集，但需要共享部分状态。更接近微服务间的 API 契约，而不是同一进程内的线程协调。

这套协作层跑起来之后，最直接的变化是不用每次手动跟 Codex 同步「我们做到哪了」，它启动时自动拿到 Claude 最新的任务列表和当日进展。但真正让我觉得值得搭的是另一件事：第二个 Agent 变成了独立审查者，视角和我手上的 Claude 不一样，抓到了几个我自己 review 时没看出来的设计缺陷。这部分后面会展开。

长期知识归 Claude、执行验证归 Codex 这个分层，反而是搭完回过头才看清楚的结果，不是一开始的设计目标。

---

## 2\. 架构核心：三层分离

```bash
最终落地的架构是三层：┌─────────────────┐   ┌─────────────────┐│  .claude/       │   │  .codex/        ││  (Claude 私有)  │   │  (Codex 私有)   ││  rules/skills/  │   │  config/auth/   ││  memory/hooks   │   │  sessions/logs  │└────────┬────────┘   └────────┬────────┘         │    不跨写对方私有层    │         │                      │    ┌────┴──────────────────────┴────┐    │       ~/.agents/ (共享契约层)    │    │  contracts/  共治协议           │    │  manifests/  边界定义           │    │  shared/     中立数据接口       │    │  handoff/    异步交接           │    └───────────────┬────────────────┘                    │         ┌──────────┴──────────┐         │     vault (知识SSOT) │         │  长期知识的唯一来源   │         └─────────────────────┘
```

一条铁律：不跨写对方私有层。Claude 不碰 `.codex/` ，Codex 不碰 `.claude/` 。所有协作通过中间的 `~/.agents/` 共享层完成。

这条规则看似简单，但在设计过程中被违反了两次（后面会讲），每次都是 Codex 在 review 时抓出来的。

---

## Phase 0-2：从目录到验证

### Phase 0：建共享层

创建 `~/.agents/` 目录结构，包括契约文件、边界定义、symlink（临时方案）、交接区。

关键设计决策：用 symlink 暴露 Claude 内部文件给 Codex 只读消费。这是 Phase 1 的权宜之计，Codex 需要知道我的用户画像、当前任务、行为规则，但不应该直接读 `.claude/` 内部路径。symlink 提供了一个稳定的别名。

### Phase 1：接入口

在两个 Agent 的启动链路上挂钩子：

- Claude 的 `CLAUDE.md` 增加一行： `Read ~/.agents/contracts/claude-shared.md at session start.`
- Codex 的 `~/.codex/AGENTS.md` 引导到 `codex-global.md` ，再加 `config.toml` 的 `model_instructions_file` 双保险

### Phase 2：烟雾验证

三个测试：

1. Codex 在 home 目录启动 → 确认读到共治契约
2. Codex 在 vault 目录启动 → 确认 vault 级规则叠加生效
3. Claude 新开 session → 确认检测到 Codex 留下的交接信息

全部通过。到这里，"两个 Agent 能感知到对方的存在"算是成立了。

---

## Phase 3：从 symlink 到中立接口（这里翻车了）

Phase 0-2 用 symlink 暴露 Claude 内部文件是能跑的，但 Codex 在 review 时指出了核心问题：

> "契约层暴露了 Claude 的内部结构。Phase 1 的 symlink 方案如果不迭代，会固化成事实标准。"

翻译一下：如果 Codex 一直通过 `refs/claude-memory/today.md` 读 Claude 的内部文件，那 Claude 的文件格式就变成了双方的契约。Claude 改自己的文件结构，Codex 那边就会坏掉。实质上 Codex 变成了 Claude 内部实现的消费者。

### 解法：投影层

在共享层增加三个 **agent-neutral** 文件：

| 文件 | 来源 | 用途 |
| --- | --- | --- |
| `shared/profile.md` | 从 `working-with-me.md` 投影 | 用户画像（稳定信息） |
| `shared/tasks.json` | 从 `active-tasks.json` 投影 | 活跃任务（热数据） |
| `shared/today-summary.md` | 从 `today.md` 投影 | 当日进展（每日覆盖） |

"投影，不复制"，shared 文件是 Claude 私有层的精简版，不是完整镜像。Claude 在每次 session 结束时自动同步，Codex 读 shared 而不是读 Claude 内部文件。

听起来很干净？

### 第一次翻车：Source Drift

第一组 shared 文件生成之后，Codex 看了一眼回话：

> "这三个 shared 文件都开始'比 source 知道得更多'。"

翻译一下： `profile.md` 里我加了一个 "Current Focus" section，写了"4月汇报准备"这些当前任务信息。问题是这些信息根本不来自 profile 声称的源文件 `working-with-me.md` ，它们的真正源头在 `active-tasks.json` 和 `today.md` 里。

投影过程混入了其他来源的数据，而 Codex 读这个文件时会以为这些信息都来自声称的源头。一旦真正的源头没更新但投影里冒出了"新数据"，信任链就断了，而且断在哪一环都查不到。

改法很直接：删掉 Current Focus section。当前任务信息已经在 `tasks.json` 里了，profile 只放稳定的用户画像。投影层不做合成。

### 第二次翻车：我以为我在做幂等同步，其实没在同一轮 review 里，Codex 还顺手指出 today-summary.md的生成规则太自由：

> "形式上是覆盖式写入，语义上不是幂等。"

我当时还以为他在抠字眼。再读一遍才反应过来：summary 里有一条规则是"提取当日的关键 decision"，但"哪些条目算 decision"是个语义判断，不同的 Claude session 完全可能挑出不同的东西。我声称的是幂等同步，实际跑出来同样的输入会产出不同的 summary。这种"形式上覆盖、语义上不稳定"的同步比明确的增量同步还危险——你以为它每次都从头来过，但其实它每次都重新猜了一遍。

改法：把提取规则从"语义摘要"收紧到"信号词匹配"，只有包含"结论/确认/里程碑/通过/决定"这类词的条目才算 decision，每个 section 最多 3 条，没有就显式写 `None` 。不追求完美摘要，只追求每次跑都一样。

### 第三次翻车：deadline 字段

这次是我自己先想到要做的，也是最离谱的一次。

`tasks.json` 我新加了一个 `deadline` 字段，设计文档写的是"从 context 提取"。看起来挺合理对吧？但源数据里的日期格式根本是混乱的：有的写"月底"（模糊），有的写"4/24"（明确），有的根本不是 deadline 而是某件事的发生日期。如果投影层把这些猜出来的日期写进结构化字段，消费方会当成可信数据来用，尤其是排优先级的时候。

改法： `deadline` 改为可选字段，只在源数据里有明确日期格式时才写入。"月底"不提取，有多个候选日期的不提取。再往后真正的解法是去上游修 `active-tasks.json` 的格式，让源头本身就带结构化日期，而不是靠下游瞎猜。

---

## Cutover：切读路径

三轮修复后，Codex 给了绿灯。切换过程：

1. `codex-global.md`
	的 session-start 读取路径从 `refs/claude-memory/` 改为 `shared/`
2. `must-share.json`
	新增 `shared_layer` 为 primary， `memory_core` 降级为 fallback
3. fallback 规则写明：shared 文件不存在，或文件内 `schema_version` 不等于 manifest 期望值时才降级
4. symlink 保留，不删除，等下一个 Phase 评估

Codex 做了最终启动链路验证，确认新路径生效。

---

## 3\. 两个 Agent 是怎么互相 review 的

这次最有意思的部分不是架构本身，而是 **两个 Agent 互相审查对方设计** 的过程。

流程是这样的：

1. Claude 出设计文档（schema 定义、字段、权限、同步规则）
2. 用户把文件路径给 Codex，Codex 做独立 review
3. Codex 输出修改建议（写成结构化文档，包含问题描述、建议改法、替换文案）
4. 用户把 Codex 的建议给 Claude，Claude 判断采纳/拒绝，写回契约文档
5. 重复 2-4 直到双方无 blocking issue

这里有两件事我后来想了想。

两个 Agent 的视角确实不同。Claude 出的设计偏"完备"，想把所有信息都投影给 Codex 用。Codex 的审查偏"保守"，每多一个字段都在问"源头在哪？不一致时怎么办？"。这跟人类团队里"产品想多做、工程想少做"的张力一模一样。如果两个 Agent 的审查视角完全一致，就不需要两个了。

当前限制：需要人做中转。同一轮对话里让两个 Agent 实时来回，必须靠人复制粘贴。跨 session 的信息流转是自动的（Claude session-end 写 shared，Codex 下次读；Codex 写 handoff，Claude 下次检查），但高频协作轮还是手动。

---

## 最终分工模型

跑完这次从零到上线，沉淀出一个分工模型：

| 环节 | 谁做 | 为什么 |
| --- | --- | --- |
| 定义问题、收敛需求 | Claude | 需要深度判断和上下文积累 |
| 方案设计、RFC 起草 | Claude | 需要知识关联和架构思维 |
| 独立 review、验证 | Codex | 不同视角 + 执行验证能力 |
| 代码实现、批量操作 | Codex | 并行执行优势 |
| 沉淀知识、更新记忆 | Claude | 负责长期记忆一致性 |

用下来的感觉是，双 Agent 适合的场景比我一开始想的要窄。高风险架构变更、产品定义后接落地实现、复杂排查、大改动前要第二意见，这几类值得花切换成本。剩下的场景——纯聊天、明确的小实现、一次性改配置、或者要在两个 Agent 之间来回 5 分钟以上的小事——单 Agent 做完就行，拉第二个进来反而让总耗时变长。

---

## 适用边界

这套方案解决的是一个很具体的问题：一个人在本地用两个 CLI Agent，串行使用，需要共享部分状态。

它不是：多人协作平台、企业级权限系统、并发 Agent 编排器、跨机器状态总线。如果你的场景涉及多个用户同时操作、Agent 并行写同一个文件、或者需要跨网络同步，这套方案不适用，需要真正的分布式协调。

适用的场景：个人工作流里有两个或以上的 AI Agent（不限于 Claude 和 Codex），它们各自独立运行，但你希望它们能读到彼此的关键输出而不用你每次手动复述。

---

```perl
技术细节：给想复现的人目录结构~/.agents/├── contracts/     # 共治协议（claude-shared.md / codex-global.md / vault-ops.md / shared-schema.md）├── manifests/     # 边界定义（must-share.json / optional-share.json / private.json）├── shared/        # 中立数据接口（profile.md / tasks.json / today-summary.md）├── handoff/       # 异步交接（latest.md）├── refs/          # symlink 到 Claude 内部（Phase 1 临时方案，Phase 3 后降级为 fallback）└── state/         # 各自的 last_seen 时间戳
```

### 同步机制

不用 watcher，不用 daemon，不用 MCP。前提是单人使用、本地串行、两个 Agent 不并行运行。满足这个前提的话，每次 session 重新读文件就是最新的，文件系统本身就是同步机制。

```sql
Claude session-end → 投影到 shared/（全量覆盖）Codex session-end → 写 handoff/latest.mdClaude session-start → 检查 handoff → 合并 → 下次 session-end 再投影
```

### 关键设计原则

跑下来发现真正起作用的设计有三条。一是投影不是完整镜像——shared 文件只是 Claude 私有层的精简版，不是全量复制，这样 Claude 改自己内部结构不会立刻 break 掉 Codex。二是每个 shared 文件只有一个写入方（Claude），Codex 想影响内容只能通过 handoff 间接表达，避免两个 Agent 同时改一个文件、谁也说不清谁覆盖了谁。三是同步规则用信号词匹配而不是语义摘要，这一条是上面那次"幂等性假象"翻车之后才补上的。

剩下两条算是边角约束：每次全量覆盖不追加（避免历史污染），字段定义本身是稳定接口、内部实现可以变（避免 Codex 直接耦合到 Claude 的内部存储格式）。这两条出场不多，但少了哪条都会有别的麻烦冒出来。

---

## 回头看

搭完这次最大的体会其实不是架构本身，是中间那三次被 Codex 抓出来的设计假设。Source drift、幂等性假象、deadline 字段，这三类问题我在单 Agent 系统里也犯过，只是没有第二个消费者去对它们较真，就一直挂在那。

有了第二个 Agent 之后，我自己"差不多能用"的判断会立刻被检验。这是双 Agent 的真正收益，也是任何引入第二个独立消费者都会带来的——是 AI 也好，是人也好。

所以如果你也在搭这种本地多 Agent 协作，我建议从一个问题开始：你的两个 Agent 之间，哪些信息你打算明确定义成契约，哪些你只是想"顺便让对方看看"？后一类一旦被对方依赖，就变成了你没承认过的隐式契约。这种隐式契约我踩了三次，大概率你也会踩。

---

*这是我用 Claude Code + Codex 搭建本地 AI 工作流的一部分记录。后续如果 MCP server 或本地 daemon 跑通了，再写一篇。*

*以上，是一篇存货，如果有更好的处理方法可以发在评论区，我们一起交流*

如果你想看更多关于 “工具使用 x AIGC”的分享，欢迎关注我的公众号。

如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。

继续滑动看下一个

EstreWolf

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过