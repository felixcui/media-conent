# 如何构建一个 Deep Researcher（译文）

**来源**: https://waytoagi.feishu.cn/wiki/QVjbwk5bYiAT9Jk5cDlcC7g0nBd

---

## 摘要

文章主张，用 Onyx、CrewAI 和 Voxtral 可构建一套完全开源、可自托管的 Deep Research 技术栈，在保护查询、内部文档、索引和审计控制权的同时，不牺牲研究质量。高质量研究不能只靠单次搜索加总结，而需要阶段隔离、推理型检索、循环反思、统一检索公开与内部来源，并加入语音交互层，才能处理多来源综合、矛盾识别和多跳推理等真实研究问题。

---

## 正文

原帖链接：https://x.com/akshay_pachaar/status/2047395420935229724


一套 100% 开源、可自托管的 Deep Research 技术栈，实测表现超过 OpenAI、Gemini 和 Perplexity。
如果你今天想让 AI 替你做研究，大概率会用 ChatGPT Deep Research、Claude 或 Perplexity。它们三个都确实很强。
但它们三个也都属于运行在别人云上的闭源 SaaS。
你发出的每一个查询、接入的每一份内部文档，最终都落在它们的服务器上，而不是你的基础设施里。
对大多数团队来说，这一直都是默认的交换条件：要么接受这一点，要么就别把 AI 用在严肃研究上。
这篇文章会给出第三种选择：一套完全开源、运行在你自有基础设施上的 Deep Research 技术栈。
三款工具，全部开源：**Onyx** 负责检索，**CrewAI** 负责编排，**Voxtral** 负责语音。
下面是这套系统完整跑通的效果，从语音提问一路到带讲解的研究报告：


这篇文章接下来会拆解它的工作原理，并带你一步步搭出同样的技术栈。不过在此之前，先讲清楚一件事：为什么这件事值得做。
# 为什么自托管很重要
几乎所有主流 AI 研究工具，本质上都是闭源云服务。这会带来非常现实的后果：
- **你的查询会发往它们的服务器。** 你问的问题本身，就暴露了你正在做什么。
- **你接入的数据会在它们的基础设施上建立索引。** 接入很方便，但索引不在你这边。
- **保留策略、日志和审计由它们决定。** 企业版可以缓和这一点，但无法真正消除。
- **配额和定价按它们的节奏变化。** 你今天依赖的工具，明天就可能涨价或限流。
对于受监管行业、处理 IP 敏感工作的团队，或者受数据驻留规则约束的组织来说，这些都不是纸面问题。
这也是为什么，对很多严肃场景而言，AI 辅助研究依然显得遥不可及。
除非你能把整套系统自己跑起来，而且不需要在质量上做任何妥协。


# 为什么现有研究工具会失效
大多数研究工具只跑一遍流程：搜索、收集返回结果，然后交给 LLM 写出一份结果。
对于浅层查询，这种方式是能工作的。
但只要问题开始要求跨来源综合、识别矛盾、或者进行多跳推理，它就会立刻失效。
它在实际中的失败方式通常是这样的：
- Agent 找到一个来源，又找到一个相互矛盾的来源。它选其中一个继续往下走，矛盾本身从未被显式提出。
- 两个来源用不同措辞表达同一件事，报告却把它们当成两份独立证据引用。
- 一个关键的连接性事实藏在没有被检索出来的文档里，因为关键词匹配并不知道 “cloud migration” 和 “把 PostgreSQL 集群迁移到 AWS” 其实是同一件事。
这些不是边缘案例。
它们恰恰是现实研究问题最常见的形态。
而它们背后的共同根因也一样：**研究不是一个单一步骤的任务。**


# 真正高质量的 Deep Research 需要什么
无论具体工具怎么选，核心都离不开五件事：
**1. 阶段隔离。** 信息收集、分析、写作之间要有明确边界。每个阶段只能接收上一个阶段清洗后的输出。
**2. 会推理的检索。** 关键词搜索太脆弱，向量相似度在多跳问题上又会失效。你需要并行查询变体、智能重组，以及在综合前加入一次 LLM 选择步骤。少了最后这一步，幻觉就会混进来。
**3. 在循环中的反思。** 静态计划无法应对真实发现。系统应该在出现新信息时动态转向，同时跟踪原计划的覆盖情况。
**4. 统一搜索公开与内部来源。** 研究层应该能在同一条 pipeline 里同时查询开放网络和内部知识，并对每个文档执行权限控制。索引究竟跑在你的基础设施上，还是跑在厂商那里，决定了数据归谁掌控。
**5. 语音层。** 对查询来说，说比打字快；对长报告来说，听比读更高效。这样工具不只是“能用”，而是真正“可达”。


## Onyx：一个在基准测试中胜出的开源检索层
[Onyx](https://github.com/onyx-dot-app/onyx) 是一款围绕这些原则构建的开源 AI 平台。它开箱即用地为任意模型提供 RAG、Web Search、代码执行、Deep Research 和自定义 Agents。
它可以完全自托管，因此你的数据不会离开自己的基础设施。
而且这并不意味着能力上的妥协。
Onyx 参加了 DeepResearch Bench，这是一项独立学术基准测试，覆盖 22 个领域的 100 个博士级研究任务，评估维度是报告质量和引用准确性。
**它拿到了第 1 名，超过 OpenAI Deep Research、Gemini 2.5 Pro 和 Perplexity Deep Research。**
团队最近也分享了他们参赛过程中的经验。他们的 prompt 哲学可以浓缩成一句话：
*在研究上宁可更彻底，也不要只是更“有帮助”。*
这套哲学在架构层面是这样落地的。
## 三个阶段，而不是一个循环
**阶段 1：澄清。** 对简短或模糊的查询，最多提出 5 个有针对性的问题；对于已经足够具体的查询则自动跳过。
**阶段 2：规划。** 把查询拆解成最多 6 个探索方向。关键设计点在于：规划器没有工具访问权限，所以它输出的是计划，而不是答案。
**阶段 3：迭代执行。** Orchestrator 和 Research Agents 最多交替 8 个循环，每轮最多并行派发 3 个 agent。


## 两个关键隔离点
- Orchestrator 从不直接执行搜索。
- Research Agents 永远看不到完整查询或完整计划。
这样可以强制任务说明保持自包含，避免上下文泄漏。
## 自适应策略
Onyx 会根据实际发现偏离原始计划。每次派发之间，系统都必须执行一次反思步骤，并产出结构化结果：
- 哪些内容已经覆盖
- 还存在哪些缺口
- 出现了哪些新的探索方向
- 是否值得再跑更多循环来获取新信息
这个步骤每次都会执行。
最终表现出来的就更像一个研究者，而不是一台检索引擎。
## 六阶段检索流水线
每个 agent 在让 LLM 做综合之前，都会先跑完这 6 个步骤：
1. **查询生成。** 并行生成多种查询：语义改写、关键词变体、宽泛搜索。多段式问题会被自动拆分。
1. **搜索与重组。** 使用混合索引（vector + BM25），再通过 Reciprocal Rank Fusion 组合结果，并合并相邻 chunk。
1. **LLM 选择。** 由 LLM 复查所有 chunk，只保留真正相关的部分。跳过这一步，幻觉就会开始出现。
1. **上下文扩展。** 对每份被选中文档，LLM 会继续读取周边 chunk 来判断需要多大上下文窗口。按文档并行执行。
1. **Prompt 构建。** 把最终选中的片段与引用、聊天历史一起组装进 prompt。
1. **答案综合。** 生成带行内引用、可直接回链到来源的 grounded answer。


## 引用完整性
- Agents 在撰写中间报告时就会内联插入引用。
- 并行 agents 产生的引用会被合并并重新编号，形成一套统一引用体系。
- 每一个最终结论都可以追溯到某一份明确的源文档。
## 内部来源索引，跑在你的基础设施上
Onyx 可以连接 40+ 企业数据源：Slack、Confluence、Jira、GitHub、Salesforce、Google Drive、SharePoint、Notion、Zendesk、HubSpot、Gong 等等。


它和专有工具的差别，不在于“能不能接”，而在于“索引在哪里发生”。
Onyx 会在你自己的基础设施上持续预索引所有内容，近实时同步正文、元数据和权限。
**这会带来什么：**
- 一次查询即可同时覆盖开放网络和所有内部来源。
- 用户只能看到自己有权限访问的文档结果。
- 权限会从各个数据源自动同步。
- 没有任何内部数据会离开你的网络，被第三方厂商索引或存储。


# CrewAI：编排层
Onyx 负责检索。
CrewAI 负责协调。
大多数开发者最自然会采用的默认模式，是用一个 agent 承担 3 个顺序任务，并不断共享同一个持续增长的上下文窗口：
- Writer 在 Analyst 还没处理完之前就已经开始写。
- 原始搜索噪声会一路污染到最终报告。
- 源材料在输出前会被重新解释两次。
**CrewAI 通过三个原语解决了这个问题：**
- **Flows**：把彼此独立的 Crews 串起来，每一阶段只接收上一阶段的干净输出，不共享累积上下文。
- **Skills**：通过 `SKILL.md` 在运行时向 agent 的 prompt 注入领域特定指令，在动作发生的当下给出约束。
- **MCP Integration**：通过 `mcps` 字段把 MCP servers 直接挂到 agent 身上，不需要适配层，也不需要额外的 context manager。
Onyx 的接入只需要一段声明：
```python
from crewai import Agent

researcher_agent = Agent(
    role="Senior Research Analyst",
    goal="Gather information on research query with source URLs",
    backstory="You are a disciplined analyst. Record every source URL.",
    mcps=[
        f"{ONYX_MCP_URL}?token={ONYX_TOKEN}"
    ]
)

```

Researcher agent 会立刻获得三个工具：
- 搜索知识库
- 搜索网络
- 抓取任意 URL 的完整页面内容
不需要手工连工具。
Schema 会被缓存，连接按需建立，即便服务器不可达也能优雅失败。
# Voxtral：语音层
[Voxtral](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) 是语音层。
每一套研究工作流都有一个摩擦点：键盘。
AI 工具里的语音能力通常只是外挂件：输入端包一层 Whisper，输出端再挂一个基础 TTS，不同方向用不同模型，整体没有统一设计。
Voxtral 不一样。
它是 Mistral 原生的音频模型家族，从底层就是为语音理解与生成构建的，并且同一家族同时覆盖输入和输出两个方向：
- 转录在口音、背景噪声和专业术语场景下依然保持准确。
- 朗读听起来更自然，而不是机械播报。
**它给研究体验带来了两点变化：**
- **语音输入。** 你可以直接说出问题，而不是敲字。转录结果会直接流入整条 pipeline。
- **报告朗读。** 整份 Markdown 报告都可以通过 Voxtral TTS 朗读出来。对于长报告而言，听往往比盯着屏幕读更有效。


# 整套系统如何协同
**完整流程如下：**
1. 通过输入文字、语音，或上传 PDF 作为研究查询。
1. **Researcher Agent** 通过 Onyx MCP 搜索网络和你的文档。
1. **Analyst Agent** 对结果去重、标记矛盾并归类发现。
1. **Report Writer Agent** 生成带引用支撑、结构化的 Markdown 报告。
1. 点击 **Play Report**，通过 Voxtral TTS 进行语音讲解。
## 三个 mini-crews，而不是一个
最自然的第一版设计，往往是一个 Crew 里放 3 个顺序任务。
不要这么做。
跨阶段共享上下文会破坏 ground truth。Onyx 团队把这种现象叫作 *deep frying*：
- 事实会被不断重新解释。
- 矛盾会被悄悄抹平。
- 等 Writer 真正看到材料时，原始来源已经面目全非。
这个系统采用的是 Flow：由三个相互独立的 Crews 组成，每一阶段只接收上一阶段清洗后的输出。


**Researcher Agent。** 通过 CrewAI 的 MCP integration 接入 Onyx，执行 Web Search、读取完整 URL、搜索上传 PDF。每一条发现都带引用。
**Analyst Agent。** 接收原始 findings，并完成：
- 对重叠事实做去重
- 合并表达相同结论的多个来源
- 标记显式矛盾
- 归并为连贯主题
它的输出是一份结构化摘要，而不是一堆搜索结果。
**Report Writer Agent。** 把摘要转成一份精炼、带引用支撑的 Markdown 报告。它还挂载了一个在生成时动态注入的 CrewAI Skill（`SKILL.md`），以保证结构一致。
```plaintext {wrap}
deep-research-report/
├── SKILL.md       # Formatting rules, evidence standards, structure
├── scripts/       # Optional
└── references/    # Optional
```

`SKILL.md` 采用 YAML front matter + Markdown body 的形式：
```markdown
---
name: deep-research-report
description: >
  Guidelines for writing high-quality, publication-ready deep research reports.
  Covers structure, tone, evidence standards, and formatting rules.
metadata:
  author: deep-research-agent
  version: "1.0"
---

Instructions for the agent go here.
This markdown is injected into the agent's prompt when the skill is activated.

```

下面是整条流程一次成功执行的实际效果：


# 在这里获取全部代码并亲自试跑
你可以在 [LightningAI Studio](https://lightning.ai/lightning-ai/templates/multi-agent-deep-researcher-powered-by-gemma-4?utm_campaign=akshay&utm_medium=twitter) 找到这个项目的全部代码：
[从这里开始 →](https://lightning.ai/lightning-ai/templates/multi-agent-deep-researcher-powered-by-gemma-4?utm_campaign=akshay&utm_medium=twitter)
# 构建这套系统后，你真正得到什么
这里真正的重点，并不是某个开源工具终于“追平了”大厂产品。
**Onyx** 让 Deep Research 运行在一套你可以检查、可以自托管、也可以修改的基础设施上。再加上 CrewAI 强制执行的阶段隔离，以及 Voxtral 的原生语音层，你最终得到的是这样一套研究栈：
- **能力。** 具备有竞争力甚至更强的研究质量，同时保持完整的引用可信度。
- **控制权。** 你的查询和内部数据中的每一个字节都留在自己的基础设施里。
- **透明性。** 代码完全开源，可读、可审计、可扩展。


所以，一个真正值得从这里开始的问题是：
**如果数据主权不再是约束，你们团队的研究工作流会长成什么样？**
就从这个问题开始。
That's a wrap!
如果你喜欢这篇内容：
Find me → [@akshay_pachaar](https://x.com/@akshay_pachaar) ✔️
我每天都会分享关于 AI、Machine Learning 和 vibe coding best practices 的教程与洞察。