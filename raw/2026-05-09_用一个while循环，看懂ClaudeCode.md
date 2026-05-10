# 用一个 while 循环，看懂 Claude Code

**来源**: https://waytoagi.feishu.cn/wiki/JgDCwOw7eia8z4k9WoFcBY2Sn3b

---

## 摘要

Claude Code的核心是一个while循环：模型生成响应、执行工具调用、返回结果、再生成响应。它被工程化为模型加Harness的架构，其中Harness包含工具系统、上下文工程和自主循环。工具系统通过专用工具实现结构化日志和权限校验，上下文工程通过压缩策略、动态加载和子任务隔离降低认知负载。模型层面也在针对Agent行为做专项优化。

---

## 正文

原文：Barret李靖
<callout emoji="musical_score" background-color="light-orange" border-color="light-orange">
Claude Code 的核心是一个 while 循环：模型生成响应 → 如果包含工具调用，执行 → 结果返回 → 模型生成下一个响应 → 持续循环。
就这么一个循环，被工程化成一个完整的产品，写了将近 30 多万行代码。
从整体代码设计来看，可以认为，Claude Code = 模型 + Harness，而 Harness = 工具系统 × 上下文工程 × 自主循环。
其中，工具系统和上下文工程做了大量的设计。
CC 的工具系统有着自己的标准化设计，它会明确约束模型不要执行 find、grep、cat、head 通用操作，而是走 GrepTool、GlobTool 等专用工具，因为这些内建工具会输出可审计、结构化的日志，让操作更加透明可控。
同时，工具本身也带有权限级别和验证逻辑。例如 Edit 工具为了避免交叉覆盖，会要求先 Read；Git 工具对 push force 类高风险操作会做 prompt 约束和 UI 警告。
类似的设计很多，目的是在工具层建立清晰的边界和反馈机制，让模型在调用时有约束、有校验，减少越界操作和错误扩散。
而在上下文管理上，CC 的管控也无所不用其极。它通过多种压缩策略和动态机制，确保模型在任何时刻只接触当前任务最相关的信息。
压缩策略的核心机制包括 MicroCompact、AutoCompact，以及不同触发条件下的会话压缩、记忆替换和裁剪策略。
在文件加载机制上，针对工具定义与能力暴露，也设计了 Just-In-Time 策略，文件不预加载，只保留路径，需要时再通过工具读取。
此外，还有 Sub-Agent 的设计，它通过上下文隔离的方式，让不同子任务的相关信息互不干扰，进一步降低了主循环的认知负载，确保主循环逻辑干净且稳定。
Claude Code 不仅是在工具系统和上下文管理上做文章，模型为了 Harness 效果更好，也开始配合对 Agentic 行为做专项优化。
例如 Opus 4.7 在指令遵循上就明确提到 "Opus 4.7 takes the instructions literally"，这对 Agent 来说非常关键。Agent 的行为边界往往写在 system prompt 里，模型层做了增强学习后，模型在指令遵守方面会表现更出色，这对 Agent 的稳定性和可靠性会有极大提升。
OpenClaw/Hermes Agent/Claude Code 产生了大量 Agent 调用数据，这些数据也会继续反哺模型能力的迭代。
从当前发展趋势可以推断，未来模型的进化，一定也会逐步内化工具调用策略、上下文压缩策略，甚至学会自我约束行为边界。
那么，今天 CC 里写的这些 Harness 逻辑，注定也会被模型吃掉。也就是说，Harness 也是一个过渡性的产物。🐶
</callout>


<callout emoji="bulb" background-color="light-blue" border-color="light-blue">
**一句话先讲透：**Claude Code 看起来像一个会自己干活的程序员，其实核心是一台被工程化包起来的“循环机器”：模型想一步、工具做一步、结果再喂回模型，然后继续。
</callout>

# 1. 最核心的秘密：就是一个循环
如果把 Claude Code 拆到最小，它的心脏并不神秘，大概是这样：
```plaintext
while 任务还没完成:
    模型生成下一步
    如果下一步要调用工具:
        执行工具
        把工具结果放回上下文
    模型基于新结果继续思考
```

这就像你请一个实习生做事：他先说“我需要看一下文件”，你把文件给他；他看完说“我需要改这里”，你让他改；改完再看测试结果。一次次循环下来，任务就被推进了。
<callout emoji="pushpin" background-color="light-yellow" border-color="light-yellow">
**真正厉害的不是循环本身，**而是围绕这个循环搭出来的一整套工作台：工具怎么用、上下文怎么管、风险怎么拦、任务怎么拆。
</callout>

# 2. Claude Code = 模型 + Harness
可以把 Claude Code 理解成两层：

<lark-table rows="3" cols="3" header-row="true" column-widths="122,195,328">

  <lark-tr>
    <lark-td>
      组成
    </lark-td>
    <lark-td>
      像什么
    </lark-td>
    <lark-td>
      负责什么
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **模型**
    </lark-td>
    <lark-td>
      大脑
    </lark-td>
    <lark-td>
      理解任务、判断下一步、生成代码或指令
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **Harness**
    </lark-td>
    <lark-td>
      工作台和安全带
    </lark-td>
    <lark-td>
      提供工具、管理上下文、控制循环、限制危险动作
    </lark-td>
  </lark-tr>
</lark-table>

所以更准确地说，Claude Code 不是“一个模型直接在电脑里乱跑”，而是“模型坐在一个被精心设计过的驾驶舱里干活”。
# 3. Harness 里最重要的三件事
<grid cols="3">
  <column width="33">
    <callout emoji="bulb" background-color="light-green" border-color="light-green">
    ### 工具系统
    让模型通过标准工具读文件、搜代码、改文件、跑命令，而不是随便操作。
    </callout>

  </column>
  <column width="33">
    <callout emoji="brain" background-color="light-purple" border-color="light-purple">
    ### 上下文工程
    只把当前最相关的信息放进模型视野，避免越看越乱、越想越偏。
    </callout>

  </column>
  <column width="33">
    <callout emoji="repeat" background-color="light-orange" border-color="light-orange">
    ### 自主循环
    让模型可以“想一步、做一步、看结果、再想一步”，持续推进任务。
    </callout>

  </column>
</grid>

# 4. 为什么工具不能随便用？
普通命令比如 `find`、`grep`、`cat` 很自由，但也容易失控：输出太多、结构不清、日志不好审计。Claude Code 会倾向让模型使用内建的 GrepTool、GlobTool、Read、Edit 等专用工具。
这背后的目的不是“换个名字”，而是把每次操作变得更可控：
- 工具输出更结构化，模型更容易读懂。
- 操作过程可记录、可审计，用户更容易知道模型做了什么。
- 工具可以附带权限、校验和风险提示。

<lark-table rows="4" cols="2" header-row="true" column-widths="256,482">

  <lark-tr>
    <lark-td>
      例子
    </lark-td>
    <lark-td>
      为什么要这样设计
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Edit 前要求先 Read
    </lark-td>
    <lark-td>
      避免模型基于旧内容改文件，减少交叉覆盖。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Git 高风险操作会提示
    </lark-td>
    <lark-td>
      例如 force push 这类动作，需要额外确认。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      搜索走专用工具
    </lark-td>
    <lark-td>
      输出更干净，减少无关结果挤爆上下文。
    </lark-td>
  </lark-tr>
</lark-table>

# 5. 上下文管理：让模型只看“该看的东西”
Agent 最容易出问题的地方之一，是上下文太多。就像一个人桌上摊满了旧聊天、旧日志、旧代码，他很快就会分不清重点。
Claude Code 的上下文工程，本质上是在帮模型整理桌面：
- **MicroCompact：**小范围压缩，把局部过程整理成更短的记忆。
- **AutoCompact：**当会话变长时，自动把历史压成摘要。
- **裁剪与替换：**不相关的信息移走，重要信息保留。
- **Just-In-Time 加载：**工具定义、文件内容不提前全塞进来，需要时再读。
<callout emoji="white_check_mark" background-color="light-green" border-color="light-green">
这件事可以类比成“开卷考试”：不是把整座图书馆塞进脑子，而是知道什么时候去翻哪一页。
</callout>

# 6. Sub-Agent：把任务分给不同小房间
有些任务会天然分叉：一个人查测试，一个人看 UI，一个人读数据库逻辑。如果所有信息都塞给主模型，它会越来越累。
Sub-Agent 的价值，是把不同子任务放进相互隔离的小房间。每个子代理只拿到自己需要的上下文，做完后把结论交回主循环。
这样主循环就不用背着所有细节跑，只需要做调度和整合。
# 7. 模型本身也在配合 Harness 进化
过去，很多 Agent 能力靠外部 Harness 硬搭：提示词写边界，工具层做校验，上下文系统做压缩。现在模型也开始针对 Agent 行为优化，比如更严格地遵守指令、更稳定地理解工具调用、更少越界。
这意味着未来有些今天写在 Harness 里的能力，可能会慢慢被模型“内化”：
- 更自然地判断该调用哪个工具。
- 更主动地压缩和整理上下文。
- 更懂得在危险操作前停下来确认。
- 更像一个能自我约束的执行者。
# 8. 最后的判断：Harness 是过渡层，但现在非常关键
今天的 Claude Code，厉害之处不只是模型聪明，而是模型被放进了一个很成熟的工程系统里。这个系统给模型工具、边界、记忆、循环和反馈。
未来模型越来越强，确实会“吃掉”一部分 Harness 的逻辑。但在当下，Harness 仍然是 Agent 从“会聊天”变成“能干活”的关键桥梁。
<callout emoji="checkered_flag" background-color="light-yellow" border-color="light-yellow">
**记住这个公式就够了：**Claude Code = 模型 + Harness；Harness = 工具系统 × 上下文工程 × 自主循环。
</callout>