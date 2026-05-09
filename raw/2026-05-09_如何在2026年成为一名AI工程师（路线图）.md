# 如何在 2026 年成为一名 AI 工程师（路线图）

**来源**: https://waytoagi.feishu.cn/wiki/NvoNwg9wRijPRpkWtPwci3I6nzb

---

## 摘要

本文指出成为2026年AI工程师的关键不在于盲目追逐新框架，而在于掌握agentic AI与harness engineering的核心能力。作者提供了一份基于一手资料的六阶段、十七周实战路线图，强调必须深入学习上下文工程、工具编写、评估体系构建及生产环境交付等底层技能，从而摆脱无效的“框架旅游”，最终达到能独立负责并落地生产级智能体系统的专业水平。

---

## 正文

<quote-container>
原帖链接：https://x.com/Av1dlive/status/2052063154423898603
</quote-container>




## 你可以在一个周末用 AI 搭出下一家 10 亿美元公司
而你真正需要学习的唯一技能是
> TLDR；如果你不想读这份长达 7,862 字的路线图，那你可以直接把这个链接交给你的 agent，让它为你个性化生成一份路线图 ➡️[https://raw.githubusercontent.com/codejunkie99/agent-roadmap-2026/main/AGENT.md](https://raw.githubusercontent.com/codejunkie99/agent-roadmap-2026/main/AGENT.md)
**agentic AI 与 harness engineering**
问题在于，大多数工程师并不清楚自己到底该学什么。
有人因为 CrewAI 在 Twitter 上那些角色分工式 demo 看起来很炫，就去学 CrewAI。
有人会追着每一个新发布的框架跑，最后却什么真正可落地的东西都没做完。
还有人一上来就扑进 multi-agent system，却根本没搞懂 context、tools、harnesses 或 evals。
结果通常都一样：框架旅游一大堆，真正能上生产的能力却很少。
如果你的目标是在 2026 年成为一名 agent engineer，你并不需要学 12 个框架。
你需要学会的是，如何在生产环境里构建、搭建 harness、评估，并交付真正的 agent system。
这意味着你要学会如何：
- 在像 LangGraph 这样的真实 orchestration runtime 上构建 agents
- 把 Claude Agent SDK 当作参考 harness 来使用
- 用 Write、Select、Compress、Isolate 正确完成 context engineering
- 写出模型会正确选择的工具
- 为生产流量补上 memory、durability 和 sandboxing
- 构建 evals、trajectory checks 和 CI regression gates
- 交付那些在真实用户和真实成本面前仍然能活下来的 agents
这份指南是一条 6 个阶段的路线图，建立在 2025 年末到 2026 年初真正已经发布的东西之上。
**全文超过 7,000 字，而且只引用一手资料。**
**但它真正的价值在于：每个阶段都有一个具体项目、一份规范阅读清单，以及你真正需要的确切资源。**
**也就是说，只要大约 17 周的高强度投入，你就能达到“可以独立负责一项生产级 AI 功能，从头做到尾”的 agent engineer 水平。**
**为了写这篇内容，我花了 60 多个小时，阅读一手工程博客、论文和一线工程师的交付调查。**
现在开始读这份路线图 ⬇️
---

## 2026 年，Agent Engineer 实际在做什么
很多人一听到 “AI agent engineer”，脑子里想到的还是那种把 CrewAI 角色拼起来、然后就宣布“已经交付”的人。
但现实里，大多数现代 agent engineer 做的事要务实得多。
他们是在 frontier models 之上，构建、搭 harness、并运营 agent systems。
这通常包括：
- 设计 agent loop 和 tool dispatch
- 用 Write、Select、Compress、Isolate 做 context engineering
- 编写模型会正确选择的工具
- 用隔离上下文窗口的方式编排 sub-agents
- 增加 skills、memory、durability 和 sandboxing
- 接上 evals、traces 和 CI gates，让“更好”这件事变得可测量
同一个模型，不同的 harness，结果会完全不同。
Anthropic 自己的测量结果是：Opus 4.5 在 Claude Code 里，核心得分是 78%；而在 Smolagents 里只有 42%。
同一个模型，到此为止。
这个差距就是 harness engineering，而这份路线图讲的就是这个。
每个智能体构建者都需要了解的四个上下文原语：写入（便笺本、内存文件），选择（在使用时检索），压缩（在上下文窗口的85 - 95%处进行摘要），隔离（给 sub-agents 分配各自独立的上下文窗口）。
Anthropic的多智能体研究系统在使用完全相同模式的广度优先研究中，以90.2%的优势击败了单智能体Opus 4，同时消耗的token数量约为其15倍。
在 2026 年，真正值得深入学习的栈，其实只有两套：LangGraph 1.0 + Deep Agents，以及 Claude Agent SDK。
剩下那些，不是正在衰退、正在被吸收掉，就是在生产环境里只是这两套的弱化版本。
---

## 在整条路线图里都值得持续跟进的免费资源
这些博客、课程、频道和 newsletter，会持续免费提供真正有信号的内容。
先订阅它们，后面的整个路线图就会一直有新的文章、案例研究和一手资料更新源源不断地喂给你。
这里没有付费墙，而且它们里的大多数更新速度都比任何一本教材快。
### 值得订阅的工程博客
**参考资料：**
- [**Anthropic engineering blog**](https%3A%2F%2Fwww.anthropic.com%2Fengineering)** (免费，官方)** — 如果你只读一个博客，就读它。Context engineering、harness design、multi-agent research、advanced tool use、evals，全部都有。全是一手资料，而且这份路线图会反复引用它。
- [**LangChain blog**](https%3A%2F%2Fwww.langchain.com%2Fblog)** (免费)** — harness、middleware 和 Deep Agents 这套方法论，就是在这里被公开系统化的。把 Lance Martin、Vivek Trivedy 和 Harrison Chase 写的都读一遍。
- [**OpenAI Cookbook**](https%3A%2F%2Fdevelopers.openai.com%2Fcookbook)** (免费，GitHub)** — 覆盖每一种 API 特性的可运行 notebook。Tool use、structured outputs、evals、agents，都在里面。别只看，跟着敲。
- [**Hamel Husain's blog**](https%3A%2F%2Fhamel.dev%2F)** (免费)** — “Your AI Product Needs Evals” 是几乎所有人都会引用的那篇 eval 文章。这个站上其他内容也是同一个水平。如果你要做 evals，这个站值得读两遍。
- [**Eugene Yan's blog**](https%3A%2F%2Feugeneyan.com%2F)** (免费)** — “Patterns for Building LLM-based Systems & Products” 是所有实践者都会引用的总结文章之一。观点鲜明，而且确实经过真实交付校准。
- [**Lilian Weng's blog**](https%3A%2F%2Flilianweng.github.io%2F)** (免费)** — 关于 agents、prompt engineering、hallucination、alignment 的长篇深度文章。这个领域里综合表达最清晰的写作者之一。
- [**Simon Willison's blog**](https%3A%2F%2Fsimonwillison.net%2F)** (免费)** — 一位持续交付的一线资深工程师的每日记录。适合用来给 hype 降温，也适合最早捕捉那些奇怪边界问题。
- [**Chip Huyen's blog **](https%3A%2F%2Fhuyenchip.com%2F)**(免费)** — 从第一性原理讲 ML systems。她那篇 “Building LLM applications for production” 是你进入 Phase 5 之前必须读的。
- [**Phil Schmid's blog**](https%3A%2F%2Fwww.philschmid.de%2F)** (免费)** — HuggingFace、Gemini、fine-tuning、deployment 的端到端实战指南。代码总是给得很实。
- [**Cameron Wolfe writes Deep (Learning) Focus**](https%3A%2F%2Fcameronrwolfe.substack.com%2F)** (免费)** — 长篇论文拆解。想快速补一整个研究方向，看他一篇就够。
---

### 值得认真完成的免费课程
**参考资料：**
- [<text underline="true">**DeepLearning.AI Short Courses **</text>](https%3A%2F%2Fdeeplearning.ai%2Fshort-courses)** (免费)** — 大多数课程只有 1 到 2 小时，而且基本都免费。Phase 0 里一定要完成 LangGraph 课程（由 LangChain 联合打造）和 Andrew Ng 的 “Agentic AI” 课程（涵盖 Reflection、Tool Use、Planning、Multi-Agent design patterns）。
- [<text underline="true">**LangChain Academy: Introduction to LangGraph **</text>](https%3A%2F%2Facademy.langchain.com%2Fcourses%2Fintro-to-langgraph)** (免费)** — 官方免费课程。State、memory、human-in-the-loop、multi-agent，全都系统讲。Phase 2 做。
- [<text underline="true">**Anthropic Interactive Prompt Engineering Tutorial **</text>](https%3A%2F%2Fgithub.com%2Fanthropics%2Fprompt-eng-interactive-tutorial)**(免费，GitHub)** — 用 Claude API 跑的 9 个 Jupyter notebook 章节。建立 prompting 肌肉记忆最快的方式。
- [<text underline="true">**HuggingFace Agents Course **</text>](https%3A%2F%2Fhuggingface.co%2Flearn%2Fagents-course)** (免费)** — 端到端覆盖 agents、smolagents、MCP 和 evaluation。还有免费证书。
- [<text underline="true">**HuggingFace LLM Course **</text>](https%3A%2F%2Fhuggingface.co%2Flearn%2Fllm-course)** (免费)** — 基础部分：tokenization、transformers、fine-tuning。即便你只打算基于 API 搭系统，这些背景也很值得补。
- [<text underline="true">**MCP Fundamentals on FreeAcademy **</text>](https%3A%2F%2Ffreeacademy.ai%2F)**(免费)** — 学会构建 MCP servers、把它们接到 Claude 上，以及编写自定义工具。入门 MCP 最快的路径之一。
### YouTube 频道和演讲
**参考资料：**
- [<text underline="true">**Andrej Karpathy **</text>](https%3A%2F%2Fyoutube.com%2F%40AndrejKarpathy)** (免费)** — Neural Networks: Zero to Hero 这套课会用原生 Python 从零把 GPT 搭出来。他在 2026 年 Sequoia AI Ascent 上关于 “Vibe Coding to Agentic Engineering” 的演讲，是解释为什么 harness engineering 现在如此关键的最佳版本之一。
- [<text underline="true">**AI Engineer **</text>](https%3A%2F%2Fyoutube.com%2F%40aiDotEngineer)**(免费)** — 所有 AI Engineer Summit 和 World's Fair 的演讲基本都在这里。重点搜 Hamel Husain、swyx、Anthropic engineers 和 Erik Schluntz 的分享。
- [<text underline="true">**LangChain **</text>](https%3A%2F%2Fyoutube.com%2F%40LangChain)** (免费)** — 每周都会更新 LangGraph、Deep Agents、middleware 和 integrations 的教程。很多新功能第一次以视频形式出现，就是在这里。
- [<text underline="true">**Anthropic **</text>](https%3A%2F%2Fyoutube.com%2F%40anthropic-ai)** (免费)** — Anthropic 工程师的演讲。Multi-agent research walkthrough、Claude Code internals、Skills 等内容都值得看。
- [<text underline="true">**Yannic Kilcher **</text>](https%3A%2F%2Fyoutube.com%2F%40YannicKilcher)** (免费)** — 论文拆解高手。能替你省下自己逐篇啃 arXiv 的时间。
- [<text underline="true">**Lex Fridman Podcast on YouTube **</text>](https%3A%2F%2Fyoutube.com%2F%40lexfridman)** (免费)** — 与正在构建和研究 AI 的那些人做长访谈。Karpathy、Schulman、Sutskever、Amodei 都在这里出现过。
### 值得订阅的 newsletter
**参考资料：**
- [<text underline="true">**Latent Space by swyx and Alessio **</text>](https%3A%2F%2Flatent.space%2F)** (免费)** — AI engineers 最该订阅的技术 newsletter。包括每日 AINews、播客，以及每年的 “AI Engineering Reading List”。如果你只订一个，就订这个。
- [<text underline="true">**The Batch by Andrew Ng **</text>](https%3A%2F%2Fdeeplearning.ai%2Fthe-batch)** (免费)** — 每周广谱更新，适合用来发现有哪些新东西正在真正起势。
- [<text underline="true">**Import AI by Jack Clark, Anthropic co-founder **</text>](https%3A%2F%2Fimportai.substack.com%2F)**(免费)** — 政策加研究综述的组合。很像这个领域的战略上下文简报。
- [<text underline="true">**Ben's Bites **</text>](https%3A%2F%2Fbensbites.com%2F)**(免费)** — 5 分钟看完每日 AI 新闻。适合扫读，帮你避免错过重要发布。
- [<text underline="true">**TLDR AI **</text>](https%3A%2F%2Ftldr.tech%2Fai)** (免费)** — 每日摘要，噪音比较低。适合搭配上面那些更深的 newsletter 一起看。
- [<text underline="true">**AI Engineer Pack by swyx **</text>](https%3A%2F%2Faiengineerpack.com%2F)**(免费)** — 持续更新的 AI engineer 免费 credits、工具和资源合集。
### 值得研究的开源仓库
**参考资料：**
- [<text underline="true">**Anthropic Cookbook **</text>](https%3A%2F%2Fgithub.com%2Fanthropics%2Fanthropic-cookbook)** (免费，GitHub)** — 各类工作流模式的参考实现。Phase 0 已经列过，但建议每完成一个阶段就再回来看一遍。
- [<text underline="true">**OpenAI Cookbook **</text>](https%3A%2F%2Fgithub.com%2Fopenai%2Fopenai-cookbook)** (免费，GitHub)** — 同样的思路，只不过是 OpenAI 侧。Tool use、structured outputs、evals、agents 都有。
- [<text underline="true">**deepagents by LangChain **</text>](https%3A%2F%2Fgithub.com%2Flangchain-ai%2Fdeepagents)** (免费，GitHub)** — 建在 LangGraph 之上的参考开源 harness。等你在 Phase 3 自己做 harness 时，一定要去读它的 middleware 文件。
- [<text underline="true">**LangGraph examples **</text>](https%3A%2F%2Fgithub.com%2Flangchain-ai%2Flanggraph%2Ftree%2Fmain%2Fexamples)**(免费，GitHub)** — 可直接运行的 LangGraph 模式库。Supervisor、hierarchical teams、planning、customer support agent 等都在里面。
- [<text underline="true">**inspect_evals **</text>](https%3A%2F%2Fgithub.com%2FUKGovernmentBEIS%2Finspect_evals)** (免费，GitHub)** — 一个 Python 包，内置 200+ 个标准 evals。包括 GAIA、SWE-bench、Cybench、BFCL。
- [<text underline="true">**awesome-agentic-engineering-resources **</text>](https%3A%2F%2Fgithub.com%2FEthicalML%2Fawesome-agentic-engineering-resources)**(免费，GitHub)** — 社区维护的 agent engineering 资源索引。可以拿来补这份路线图没覆盖到的空白。
### 通勤路上值得听的播客
**参考资料：**
- [<text underline="true">**Latent Space **</text>](https%3A%2F%2Flatent.space%2F)** (免费)** — 与这个领域真正交付的人做长访谈。Anthropic、OpenAI、LangChain、Modal、E2B 等团队都上过节目。
- [<text underline="true">**Dwarkesh Podcast **</text>](https%3A%2F%2Fdwarkeshpatel.com%2F)**(免费)** — 围绕 AI 战略、能力和政策的长访谈，信息密度高，而且多是一手来源。
- [<text underline="true">**The TWIML AI Podcast by Sam Charrington **</text>](https%3A%2F%2Ftwimlai.com%2F)** (免费)** — 每周和研究人员、工程师做技术访谈。
- [<text underline="true">**Practical AI **</text>](https%3A%2F%2Fchangelog.com%2Fpracticalai)** (免费)** — 明显偏工程。少一点 hype，多一点真实交付。
- [<text underline="true">**The MAD Podcast by Matt Turck **</text>](https%3A%2F%2Fmattturck.com%2Fthemadpodcast)** (免费)** — 从创业者和投资人的视角看数据与 AI 生态，适合跟踪谁真在做事，谁只是融资。
### 值得加入的社区
**参考资料：**
- [<text underline="true">**LangChain Discord **</text>](https%3A%2F%2Fdiscord.gg%2Flangchain)** (免费)** — LangGraph 和 Deep Agents 核心团队就在这里，`#help` 频道也很活跃。
- [<text underline="true">**HuggingFace Discord **</text>](https%3A%2F%2Fhf.co%2Fjoin%2Fdiscord)** (免费)** — 最大的 open-weights 和 ML 社区之一。
- [<text underline="true">**r/LocalLLaMA **</text>](https%3A%2F%2Freddit.com%2Fr%2FLocalLLaMA)** (免费)** — open-weights 模型新闻、benchmark 和 tooling 更新，经常比官方渠道还快。
- [<text underline="true">**AI Engineer World's Fair **</text>](https%3A%2F%2Fai.engineer%2F)**(免费，注册即可)** — 这个领域的职业网络。职位、招聘频道、工作组，都能在里面找到。
- [<text underline="true">**Anthropic Discord **</text>](https%3A%2F%2Fanthropic.com%2Fdiscord)** (免费)** — Claude 开发者社区，适合看 Skills 分享、hooks 模式和 MCP servers。
*重点关注：* 在阶段 0 里，先选 1 个博客、1 个 newsletter、1 个播客和 1 个社区。不要试图一次性跟完这 40+ 个资源。
只有当你已经订阅的那些内容不再让你感到“有新东西可学”时，再逐步加新的。
这份清单的意义是给你足够的广度，让你能自己挑选，而不是让你把它当成一份必须清空的待办。
---

## 阶段 0：基础打底（1–2 周）
**这一阶段的目标：** 建立正确的心智模型。除了临时脚本外，先不要写任何真正的 agent 代码。
大多数新手都会跳过这一阶段，直接冲进框架教程，最后得到一堆一旦出错自己都解释不清的代码。别跳。
### 学什么
#### 1. 增强型 LLM，以及 workflow 和 agent 的区别
在你碰任何框架之前，你必须先理解 Anthropic 总结出的五种 workflow pattern（prompt chaining、routing、parallelization、orchestrator-worker、evaluator-optimizer），以及为什么 workflow 和 agent 根本不是同一回事。
workflow 的控制流是你事先写死的。
而 agent 会在一个循环里自己决定控制流。
这个区别会帮你避免“本来应该做成 chain，却硬做成 agent”的错误。
**参考资料：**
- [<text underline="true">**Building Effective Agents by Anthropic (Erik Schluntz and Barry Zhang) (Dec 2024) **</text>](https%3A%2F%2Fanthropic.com%2Fresearch%2Fbuilding-effective-agents)**(免费，官方)** — 五种 workflow pattern 加 augmented LLM 概念。几乎所有人都会引用这篇。第一篇先读它。
- [<text underline="true">**Anthropic Cookbook (patterns/agents folder) **</text>](https%3A%2F%2Fgithub.com%2Fanthropics%2Fanthropic-cookbook)** (免费，GitHub)** — 每一种 workflow pattern 的参考实现，都是可运行 notebook。别只读，要跟着敲。
- [<text underline="true">**Simon Willison's annotations of Building Effective Agents **</text>](https%3A%2F%2Fsimonwillison.net%2F2024%2FDec%2F20%2Fbuilding-effective-agents%2F)** (免费)** — 一位资深工程师对同一篇内容的批注和 sanity check。
*重点关注：* workflow 和 agent 的区别、augmented LLM 的心智模型、orchestrator-worker pattern、为什么 parallelization 往往比 sequential reasoning 更强，以及 Anthropic 明确提醒过的那些 failure modes。
#### 2. 把 context engineering 当成一门纪律
到 2026 年，prompt engineering 已经不再是一项可以单独成立的技能。它的替代品是 context engineering：在循环的每一步，决定哪些 token 应该被放到模型面前。
**参考资料：**
- [<text underline="true">**Effective context engineering for AI agents by Anthropic (Sep 29, 2025) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Feffective-context-engineering-for-ai-agents)** (免费，官方)** — 这篇至少读两遍，把其中的 framing 记住。
- [<text underline="true">**Context Engineering for Agents by Lance Martin (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fcontext-engineering-for-agents%2F)**(免费)** — Write、Select、Compress、Isolate 框架。你最需要的那个心智模型就在这里。
- [<text underline="true">**How we built our multi-agent research system by Anthropic (Jun 2025) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fmulti-agent-research-system)** (免费，官方)** — orchestrator-worker 的参考架构、breadth-first research 上 90.2% 的提升，以及那条 15× token 开销的提醒，都来自这里。
- [<text underline="true">**Simon Willison's annotations of the multi-agent research post **</text>](https%3A%2F%2Fsimonwillison.net%2F2025%2FJun%2F14%2Fmulti-agent-research-system%2F)**(免费)** — 从另一个角度帮你看清这套架构和它的成本权衡。
*重点关注：* Write、Select、Compress、Isolate 在代码里分别意味着什么；为什么 sub-agents 首先是一种隔离原语，而不是并行原语；以及你什么时候该用 compaction，什么时候该用 offloading，什么时候该用 summarization。
#### 3. 把 harness 看成一个操作系统
你需要有一份足够清晰的解释，能说明 “harness” 到底是什么。
**参考资料：**
- [<text underline="true">**The Complete Guide to Harness Engineering (ClaudeCodeLab) **</text>](https%3A%2F%2Fclaudecode-lab.com%2Fen%2Fblog%2Fclaude-code-harness-engineering%2F)**(免费)** — 三层 harness 升级路径，还带可运行代码。
- [<text underline="true">**Inside the Claude Agents SDK (ML6) **</text>](https%3A%2F%2Fml6.eu%2Fen%2Fblog%2Finside-the-claude-agents-sdk)**(免费)** — 用 CPU / RAM / OS / App 的比喻解释整个系统，也给出了那个推动整条路线图成立的数字：78% vs 42%。
- [<text underline="true">**Building agents with the Claude Agent SDK (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fbuilding-agents-with-the-claude-agent-sdk)** (免费，官方)** — 讲清楚 SDK 为什么存在，以及它为什么从 Claude Code SDK 更名而来。
- [<text underline="true">**Effective harnesses for long-running agents by Anthropic (Nov 26, 2025) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Feffective-harnesses-for-long-running-agents)**(免费，官方)** — Anthropic 自己的 harness primer。建议和 Vivek Trivedy 的文章对照着读，看看不同团队是如何讲同一组思想的。
- [<text underline="true">**Harness design for long-running application development by Anthropic (Mar 24, 2026) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fharness-design-long-running-apps)**(免费，官方)** — 上一篇的续作。重点讲 session 被拉长到数小时甚至数天时，设计会发生什么变化。Phase 3 里也会再次用到。
- [<text underline="true">**How to think about agent frameworks by Harrison Chase (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fhow-to-think-about-agent-frameworks%2F)** (免费)** — orchestration framework 和 abstraction 之间到底有什么区别。你在选任何东西之前，都应该先读这篇。
*重点关注：* loop、tool dispatch、context curation、persistence、hooks、sub-agent orchestration、observability，以及这些东西分别是如何在不同 harness 中被实现出来的。
#### 4. 2026 年这个领域的真实状态
**参考资料：**
- [<text underline="true">**State of Agent Engineering (LangChain) **</text>](https%3A%2F%2Flangchain.com%2Fstate-of-agent-engineering)** (免费)** — 2025 年 11 月到 12 月、共 1,340 名受访者的数据。把这些数字记在脑子里：57% 的团队已经上生产，89% 做了 observability，52% 做了 evals，而质量（32%）是第一大障碍。
- [<text underline="true">**How to Build an Agent (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fhow-to-build-an-agent%2F)**(免费)** — 用 “smart intern” 来界定一个 agent 应该做什么、不该做什么。
- [<text underline="true">**Continual learning for AI agents by Harrison Chase (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fcontinual-learning-for-ai-agents%2F)**(免费)** — agent 真正会学习的三个层次：weights、prompts、memory。在你碰 fine-tuning 之前，先用这篇把脑子校准好。
*重点关注：* 团队在生产环境里最常卡在哪里（质量、成本、可靠性）、中位数团队的真实技术栈长什么样，以及你额外投入的每一个小时，最应该投在哪里才最值。
**实践项目：** 手写一份 2 页的个人文档，用你自己的话定义这些概念：workflow vs agent、augmented LLM、四个 context-engineering primitives、orchestrator-worker pattern、harness / model / framework 三者的区别，以及你预期会在自己代码里遇到的三个最大 failure modes。
这份文档才是真正的交付物。
如果你脱离原文写不出来，就说明你读得还不够细。
### 阶段 0 成果检查
完成这一阶段时，你应该能够：
- 不借助框架黑话，解释什么是 agent，以及它和 workflow 的区别
- 说出四个 context-engineering primitives，并分别给出一个代码层面的例子
- 解释为什么到了 2026 年，harness 的贡献比模型本身更大
- 解释 orchestrator-worker pattern 以及它那条 15× token 成本权衡
- 基于架构理由，而不是基于“感觉”去选框架
## 阶段 1：构建你的第一个简单 agent（2–3 周）
**这一阶段的目标：** 把一个 tool-using agent 写两遍。第一遍用 Anthropic 的原始 SDK，第二遍用 Claude Agent SDK harness。亲自感受“自己从零写 loop”和“站在一个真实 harness 上写”之间的差别。
这是理解 harness 到底给了你什么的最便宜方式。
### 学什么
#### 1. 从零写 agent loop
这个 loop 并不神秘。你带着 messages 和 tools 去调用模型，解析返回里的 `tool_use` blocks，执行这些 tools，把 `tool_result` 追加回去，再一直循环，直到 `stop_reason` 等于 `end_turn`。
只要你自己用大约 100 行代码把它写出来，之后几乎所有框架都会立刻变得可读。
**参考资料：**
- [<text underline="true">**Tutorial: Build a tool-using agent (Anthropic docs) **</text>](https%3A%2F%2Fdocs.anthropic.com%2Fen%2Fdocs%2Fbuild-with-claude%2Ftool-use)**(免费，官方)** — `tool_use`、`tool_result`、parallel tool calls 和 response loop 的标准参考文档。
- [<text underline="true">**Writing tools for agents (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fwriting-tools-for-agents)** (免费，官方)** — 在你设计任何 tool 之前先读它。Tool 自己的描述，以及它参数的描述，就是 LLM 的“用户手册”。
- [<text underline="true">**Equipping agents for the real world with Agent Skills (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fequipping-agents-for-the-real-world-with-agent-skills)** (免费，官方)** — 由编写这套规范的团队亲自解释 progressive-disclosure pattern。
*重点关注：* request / response loop 是如何结束的、`stop_reason` 的不同取值意味着什么、parallel tool calls 在协议里是怎么编码的、tool 抛错时如何恢复，以及怎样写 tool description 才能让模型更容易正确选择它。
**实践：** 用 `anthropic.messages.create` 和 tool spec，从零搭一个约 100 行的 agent。给它三个工具：通过 Tavily 或 Firecrawl 做 `web_search`、`read_file`、`write_file`。不要用框架。让它去跑一个 research task，并且把 trace 的每一步都读一遍。
#### 2. 把 Claude Agent SDK 当成规范参考 harness
Claude Agent SDK 本质上就是 Claude Code 背后的那套 harness。
你要把它当成参考实现来研究，同时也把它当成你 day-1 就要上手的工具。
**参考资料：**
- [<text underline="true">**Claude Agent SDK docs **</text>](https%3A%2F%2Fplatform.claude.com%2Fdocs%2Fen%2Fagent-sdk)**(免费，官方)** — Python 和 TypeScript 两套 SDK、hooks、sub-agents、skills，以及 Task tool 都在这里。
- [<text underline="true">**Claude Agent SDK, Skills reference **</text>](https%3A%2F%2Fcode.claude.com%2Fdocs%2Fen%2Fagent-sdk%2Fskills)**(免费，官方)** — `SKILL.md` 是怎么工作的、metadata frontmatter 怎么写、progressive loading 怎么实现。
- [<text underline="true">**claude-code-best-practices by Muhammad Usman GM **</text>](https%3A%2F%2Fgithub.com%2FMuhammadUsmanGM%2Fclaude-code-best-practices)**(免费，GitHub)** — 可以扫读，但别整套照搬。它的价值在于让你看到真实用户是怎么用的。
- [<text underline="true">**claude-code-best-practice by Shan Raisshan **</text>](https%3A%2F%2Fgithub.com%2Fshanraisshan%2Fclaude-code-best-practice)** (免费，GitHub)** — 方向不同的 companion compendium，可以互相对照看。
- [<text underline="true">**Evaluating Skills (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fevaluating-skills%2F)** (免费)** — LangChain 是怎么衡量一个 Skill 到底在帮忙，还是在添乱的。等你在这个阶段写出第一个 Skill 之后，这篇就很有用了。
*重点关注：* `CLAUDE.md` 这种 system-prompt pattern、Skills 是怎样渐进式加载的、`PreToolUse` 和 `PostToolUse` hooks、如何用 Task tool 拉起 sub-agents，以及 SDK 如何处理 permission prompts。
**实践：** 把你在上一个主题里做出来的 agent，用 `claude-agent-sdk` 重新做一遍。加一个 `CLAUDE.md`，写清项目约定。再加一个 Skill（也就是一个带 `SKILL.md` 的文件夹），定义一个 “research-summary” 输出格式。再加一个 `PostToolUse` hook，让 agent 每写一个文件都自动格式化一次。最后，再用 Task tool 拉起一个 sub-agent 去完成某个子任务。
#### 3. 交付一个足够小、但真的在运行的东西
光做教程不算。你得交付一个会按计划运行、而且你真的会去读它输出结果的东西。
**实践项目：** 做一个 daily-briefing agent。它读取你本地的 Markdown 笔记和几个 RSS feeds，生成一份带引用的摘要 briefing，并把它写到磁盘上。用 `launchd` 或 `systemd` 把它 cron 起来。连续跑一周。看它出错。修它。
### 阶段 1 成果检查
完成这一阶段时，你应该能够：
- 不借助任何框架，在 100 行以内写出一个 tool-using agent loop
- 解释 `stop_reason` 的不同含义，以及 parallel tool calls 是如何工作的
- 基于 Claude Agent SDK 构建同样的 agent，并且加上 1 个 Skill、1 个 hook 和 1 个 sub-agent
- 用 200 字说明：相较于你从零写的版本，harness 到底帮你白送了哪些东西
---

## 阶段 2：构建一个架构正确的真实 agent（3–4 周）
**这一阶段的目标：** 用 LangGraph 1.0 + LangChain `create_agent` + Deep Agents，构建一个多步骤、持久化、有状态的 agent。
这很可能就是你最终会放到生产环境里的那套栈。它背后的概念模型（nodes 和 edges 组成的状态机、middleware、checkpointer）在其他地方也都是通用的。
**为什么选这套栈，而不是 Pydantic AI、OpenAI Agents SDK 或 CrewAI：**
- 在 Alice Labs 和 Channel.tel 那几份 “真正能交付什么” 的排名里，LangGraph 是唯一一个同时把 durable execution、checkpointing、human-in-the-loop、一流 observability（通过 LangSmith）和 middleware 都整合起来的框架。
`create_agent`（LangChain 1.0，2025 年 10 月）现在已经是建立在 LangGraph runtime 之上的默认 agent factory。`create_react_agent` 已经被废弃了。
Deep Agents（LangChain 于 2025 年 8 月发布，2026 年 4 月到 v0.5 alpha）则是一层 batteries-included harness。Planning、virtual filesystem、sub-agents、summarization、skills，它都带着。它也是最接近 Claude Code harness 的开源对应物，只是模型无关。
### 学什么
#### 1. LangGraph runtime
一个由 nodes 和 edges 组成的 state graph，再加上一个能让你 resume、rewind、fork 的 checkpointer。
**参考资料：**
- [<text underline="true">**LangGraph docs **</text>](https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2F)** (免费，官方)** — runtime 的官方参考。先看 concepts page，再看 quickstart。
- [<text underline="true">**Doubling down on Deep Agents (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fdoubling-down-on-deepagents%2F)** (免费)** — 把 harness、framework、runtime 三者之间的关系讲得很清楚。
- [<text underline="true">**Context Management for Deep Agents (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fcontext-management-for-deepagents%2F)**(免费)** — 20K-token tool-response offload 模式，以及在上下文窗口使用率达到 85% 时触发压缩的策略。
- [<text underline="true">**On Agent Frameworks and Agent Observability (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fon-agent-frameworks-and-agent-observability%2F)**(免费)** — 解释 LangSmith 为什么对 OTEL 友好、为什么即使你不用 LangChain 也仍然能配合它工作。
- [<text underline="true">**Deep Agents v0.5 (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fdeep-agents-v0-5%2F)** (免费)** — 2026 年 4 月发布说明。包含异步 sub-agents、更多模态的 filesystem 支持、async TODOs。在你的项目里 pin `deepagents` 版本前，先读这篇。
*重点关注：* state schemas、nodes、edges、conditional edges、`PostgresSaver` checkpointer、time-travel debugging、human-in-the-loop interrupts，以及 middleware 是如何组合起来的。
#### 2. Middleware 是最关键的自定义层
middleware 就是你在不 fork 一个打包好 agent 的前提下，对它进行深度定制的方式。
**参考资料：**
- [<text underline="true">**How Middleware Lets You Customize Your Agent Harness (LangChain) (Mar 26, 2026) **</text>](https%3A%2F%2Fblog.langchain.com%2Fhow-middleware-lets-you-customize-your-agent-harness%2F)**(免费)** — `before_agent`、`wrap_model_call`、`before_tools`、`after_tools` 这些 hooks 的最佳入口文档。
- [<text underline="true">**Introducing ambient agents (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fintroducing-ambient-agents%2F)**(免费)** — background-agent 的交互模式：notify、question、review。
*重点关注：* 每一个 hook 在 agent 生命周期里的触发时机、`SummarizationMiddleware` 和 `FilesystemMiddleware` 是如何组合的、如何用 30 行写一个自定义 middleware，以及什么时候该用 middleware，什么时候应该直接写一个新 node。
#### 3. Tools、MCP，以及“代码执行”模式
那种“把所有 MCP tools 全部加载进上下文”的天真做法，是行不通的。正确模式是：通过代码执行来使用 MCP。
**参考资料：**
- [<text underline="true">**Code execution with MCP (Anthropic) (Nov 2025) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fcode-execution-with-mcp)** (免费，官方)** — 把 token 开销从 150K 降到 2K 的关键文章。你在接任何 MCP server 之前都应该先读它。
- [<text underline="true">**Introducing advanced tool use (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fadvanced-tool-use)**(免费，官方)** — `defer_loading: true` 让 tool token 消耗降低了 85%，同时把 Opus 4.5 的 MCP eval 从 79.5% 提高到了 88.1%。
- [<text underline="true">**Scaling Managed Agents (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fmanaged-agents)** (免费，官方)** — session、harness 和 sandbox 分离的设计。即使你不打算使用 Managed Agents，也值得读。
- [<text underline="true">**Composio docs **</text>](https%3A%2F%2Fcomposio.dev%2F)**(免费)** — 提供 200+ 个 SaaS 集成，自带 MCP gateway，并且能帮你 broker 凭证，让它们不必进入模型上下文。
- [<text underline="true">**Arcade docs **</text>](https%3A%2F%2Farcade.dev%2F)** (免费)** — 当你需要面向“每个用户”的细粒度身份，而不是服务级别认证时，用它。
*重点关注：* `defer_loading`、把 code execution 当作 tool surface 的思路、为什么让模型来回倒腾 JSON 很贵，以及 Composio / Arcade 是如何在不把密钥暴露给模型的前提下 broker SaaS 认证的。
#### 4. 不依赖 vector DB 的 memory 选择
**参考资料：**
- [<text underline="true">**Letta MemFS benchmark on LoCoMo **</text>](https%3A%2F%2Fletta.com%2F)**(免费)** — 2026 年 4 月的结果：基于 filesystem 的 memory，在 GPT-4o-mini 上能在 LoCoMo 里打到 74%，甚至超过很多专门做 memory 的工具。
- [<text underline="true">**Mem0 docs **</text>](https%3A%2F%2Fmem0.ai%2F)** (免费)** — 用户级知识记忆。如果你需要跨 session 保留用户事实，这是不错的选择。
*重点关注：* 三层 memory（线程级的 `PostgresSaver`、用户级的 Mem0 / Zep、自我管理型的 Letta）、为什么 filesystem 应该是默认起点，以及在真正测量出 recall 问题之前，为什么不要着急上 vector DB。
**实践项目：** 做一个 “research analyst” deep agent。
输入：一个研究问题。
主 agent 负责规划，把 TODO list 写进 virtual filesystem，然后并行拉起 3 个带隔离上下文的搜索 sub-agents。
这些 sub-agents 调用 Tavily 或 Firecrawl，把结果写进文件，然后只把简短摘要返回给父 agent。绝对不要把原始搜索结果直接塞回父 agent 的上下文。
再做一个 citation sub-agent，负责拿检索到的来源去验证 claims。
再做一个 writer agent，输出一份带行内引用的最终 Markdown 报告。
所有 state 都通过 `PostgresSaver` 持久化。你要能做到：进程在中途被杀掉之后，还能从断点继续。
Human-in-the-loop interrupt：当 token 花费将要超过 1 美元时，agent 必须先询问确认。
把整个流程包进一个统一的 `make demo` target 里，确保它能端到端完整跑通。
README 必须明确写清楚：你用了哪些 middleware、为什么这样用；哪些 sub-agents 处于隔离上下文；你的 context-compression 策略是什么；以及在进程被杀时，你的 durability story 是什么。
同时还要在 README 里放一条完整运行的 LangSmith trace URL。
### 阶段 2 成果检查
完成这一阶段时，你应该能够：
- 构建一个多步骤的 LangGraph agent，并具备 `PostgresSaver` durability 与 human-in-the-loop interrupts
- 把 Deep Agents middleware（planning、filesystem、sub-agents、summarization）当作一层打包好的 harness 来使用
- 拉起带隔离上下文的 sub-agents，并且只向父级返回压缩后的摘要
- 清楚阐述你的 context-compression 策略，以及在进程被杀后的 durability story
- 给出一条 LangSmith trace URL，展示完整的多步骤 trajectory
---

## 阶段 3：亲手构建 harness 层（3–4 周）
**这一阶段的目标：** 不再依赖打包好的 harness，而是自己做一层轻量 harness。只要你没有亲手做过一次，你在生产环境里就永远无法做出真正正确的 harness trade-off。
这是整条路线图里杠杆最高的一个阶段。
### 学什么
#### 1. “harness” 到底可以拆成哪些部分
把 Deep Agents 的 middleware 列表、Claude Agent SDK 的架构，以及 Vivek Trivedy 关于 harness engineering 的总结综合起来看，harness 其实是这些组件的并集：
- loop control：驱动 model → tools → model 的 while-loop
- tool dispatch：注册表、schema 校验、并行调用、错误恢复、重试
- context management：system prompt 组装、在上下文窗口用到 85–95% 时进行 message-history 压缩、在 tool 响应超过约 20K tokens 时做 offload、prompt caching
- persistence：在每个 node 后 checkpoint 状态，这样你就能 resume、rewind、fork
- sub-agent orchestration：拉起带隔离上下文的子 agent，并把压缩摘要路由回父级
- skills 与 progressive disclosure：只有在相关时才加载能力
- hooks：`PreToolUse`、`PostToolUse`、`PreCompact`、`Stop`、`SessionStart`（Claude Code 那组 hook 列表基本可以视为事实标准）
- observability：给每一次 model call、tool call、sub-agent invocation 都打 OTEL spans，并带上 token 数和延迟
- sandboxing：代码执行和 MCP tool calls 都必须发生在容器里，模型不能直接碰到真实凭证
- auth 与 secrets brokering：凭证永远不要进入模型上下文（Anthropic Managed Agents 的模式）
**参考资料：**
- [<text underline="true">**The Anatomy of an Agent Harness (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fthe-anatomy-of-an-agent-harness%2F)** (免费)** — 公开资料里对 harness 组件拆解得最清晰的一篇。这个阶段的整篇参考文本。写任何一行 harness 代码之前先读它。
- [<text underline="true">**Improving Deep Agents with harness engineering by Vivek Trivedy (LangChain) (Feb 17, 2026) **</text>](https%3A%2F%2Fblog.langchain.com%2Fimproving-deep-agents-with-harness-engineering%2F)**(免费)** — 只改 harness、模型固定在 GPT-5.2-codex 不变，就能把 Terminal-Bench 2.0 的名次从第 30 提到第 5。配方就在文里。
- [<text underline="true">**Better Harness: A Recipe for Harness Hill-Climbing with Evals by Vivek Trivedy (LangChain) (Apr 29, 2026) **</text>](https%3A%2F%2Fblog.langchain.com%2Fbetter-harness-a-recipe-for-harness-hill-climbing-with-evals%2F)** (免费)** — 上一篇的直接续作。讲如何用 self-verification 和 tracing，自主改进 harness。紧接着 2 月 17 日那篇读。
- [<text underline="true">**Inside the Claude Agents SDK (ML6) **</text>](https%3A%2F%2Fml6.eu%2Fen%2Fblog%2Finside-the-claude-agents-sdk)** (免费)** — CPU / RAM / OS / App 的比喻，以及 78% vs 42% 这个 harness 对比数字。
- [<text underline="true">**everything-claude-code (Cerebral Valley × Anthropic hackathon winner) **</text>](https%3A%2F%2Fgithub.com%2Faffaan-m%2Feverything-claude-code)** (免费，GitHub)** — 适合作为“功能该加到什么程度就停”的灵感参考。
- [<text underline="true">**deepagents source **</text>](https%3A%2F%2Fgithub.com%2Flangchain-ai%2Fdeepagents)** (免费，GitHub)** — 一边写你自己的 harness，一边把它当作参考源码来读。middleware 文件就是整个 harness pattern 的核心。
*重点关注：* 哪些 harness 组件值得自己写，哪些可以直接引入，以及功能回报顺序应该怎么排：先 loop 和 tool dispatch，再 sub-agents，再 durability，再 observability。
#### 2. Durable execution 是一个附加层，不是锦上添花
**参考资料：**
- [<text underline="true">**Inngest docs **</text>](https%3A%2F%2Finngest.com%2Fdocs)** (免费)** — durable steps 和 checkpointing 在 2025 年 12 月正式 GA。对 Python harness 来说，这是最容易接上 durability 的路线之一。
- [<text underline="true">**Temporal Python SDK **</text>](https%3A%2F%2Fdocs.temporal.io%2F)** (免费)** — OpenAI Agents SDK 与 Temporal 的集成在 2026 年 3 月已经发布。可以把每一次 tool call 都看成一个 durable step。
*重点关注：* 每一步的 idempotency key、retry policy、进程被杀时正在飞行中的 tool call 会发生什么，以及你的 checkpoint boundary 应该放在哪里（应该是每个 node，而不是每个 token）。
**实践项目：** 用大约 1,500 行 Python 写一个 mini-harness。
要求包括：
一个基于 `anthropic.messages.create` 的 loop，或者为了实现模型无关性而包在 LiteLLM 上也行。
一个通过 Python decorator（`@tool`）实现的 tool registry，并自动生成 JSON schema。
一个类似 `CLAUDE.md` 的 system-prompt loader，从 `./harness/rules/*.md` 里按 path-glob 规则读取内容。
一个 `SKILL.md` progressive-disclosure loader，目标是每个 skill 在上下文里只占不到 50 tokens 的 metadata。
一个带隔离上下文的 sub-agent spawn primitive，只把 summary string 返回给父级。
Filesystem offload：任何超过 20K tokens 的 tool result，都写到 `./workspace/<id>.txt`，并在上下文里只保留路径加 10 行预览。
当上下文窗口使用率达到 85% 时，自动做 compaction：把最近 10 轮以前的消息做摘要。
一个可插拔 hook system（`pre_tool`、`post_tool`、`stop`）。
用 `opentelemetry-sdk` 做 tracing，并导出到 LangSmith 或 Phoenix（两者都支持 OTEL）。
Durable resume：每一步都把 message history 和 state 持久化到 SQLite，并能通过 run ID 重新加载。
可选增强项：再用 Inngest 或 Temporal 把整套东西包起来，让每一次 tool call 都成为一个 durable step。
### 阶段 3 成果检查
完成这一阶段时，你应该能够：
- 列出一个现代 harness 的十个组成部分，并解释每一个是在什么时候开始真正产生回报的
- 写出一个大约 1,500 行的 Python harness，包含 loop、tool dispatch、context compression、sub-agents、hooks 和 OTEL traces
- 用 Inngest 或 Temporal 接上 durable execution，让“进程被杀”变成一种可恢复状态
- 写出一篇 1,000 字的 post-mortem，比对你自己的 mini-harness 与 Claude Agent SDK、Deep Agents：你哪里做对了、哪里删掉了、如果重来会改什么
- 那篇 post-mortem 才是真正的交付物。代码只是证据
---

## 阶段 4：构建 eval 与 regression harness（3–4 周）
**这一阶段的目标：** 让你的 agent 可测量。如果做不到这一点，所有“改进”都只是感觉。
大多数工程师都会卡在这里：他们可以构建出一个很强的 agent，却无法判断下一次修改到底让它变好了，还是变差了。
### 学什么
#### 1. 只选一个 observability 平台
不要同时上两个。真正值得考虑的只有这五类：
- LangSmith：如果你主要用的是 LangGraph 或 LangChain，就选它。原生 tracing。2026 年 3 月还增加了 Sandboxes、Polly 调试助手、Skills 和 Fleet（agent 身份 / 共享）。
- Braintrust：如果你想要 framework-agnostic 的 CI 质量门禁，就选它。2026 年 2 月刚完成 8,000 万美元 Series B。它的商业模式是无限用户统一 249 美元 / 月，而 LangSmith 是 39 美元 / seat。
- Arize Phoenix（开源）和 Arize AX（托管）：如果你想要原生 OpenTelemetry、drift detection，以及从 OSS 平滑迁移到托管版的路径，就选它。
- W&B Weave：如果你的 ML 基础设施本来就在 Weights & Biases 上，就选它。现在它已经有完整的 agent trace 视图、MCP auto-logging，以及即将上线的 A2A tracing。
Inspect（UK AISI）：如果你追求的是 benchmark 级别的 eval rigor，就选它。GAIA、SWE-bench、Cybench、BFCL 都可以作为 `inspect_evals` 包直接用。Anthropic、DeepMind、Grok 内部都在用它。
**参考资料：**
- [<text underline="true">**LangSmith docs**</text>](https%3A%2F%2Fdocs.smith.langchain.com%2F)** (免费，官方)** — 生产 tracing、online evals、experiments，以及新的 Polly 调试助手。
- [<text underline="true">**Inspect AI annotated notes by Hamel Husain **</text>](https%3A%2F%2Fhamel.dev%2Fnotes%2Fllm%2Fevals%2Finspect.html)** (免费)** — 这是非常强的实践者视角笔记。建议在安装 Inspect 之前先读它。
- [<text underline="true">**Inspect docs **</text>](https%3A%2F%2Finspect.aisi.org.uk%2F)**(免费，官方)** — 框架参考文档本体。
- [<text underline="true">**inspect_evals **</text>](https%3A%2F%2Fgithub.com%2FUKGovernmentBEIS%2Finspect_evals)** (免费，GitHub)** — 200+ 个标准 evals，打包成 Python package。GAIA、SWE-bench、Cybench、BFCL 全都有。
- [<text underline="true">**Braintrust docs **</text>](https%3A%2F%2Fbraintrust.dev%2F)** (免费)** — framework-agnostic 的 experiments、CI gates 和 golden datasets。
- [<text underline="true">**Agent Evaluation Readiness Checklist (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fagent-evaluation-readiness-checklist%2F)** (免费)** — 17 分钟就能看完的实战清单：error analysis、dataset construction、grader design、offline / online evals、production readiness。建议直接打印出来贴在显示器边上，整个阶段都盯着它做。
- [<text underline="true">**Quantifying infrastructure noise in agentic coding evals (Anthropic) (Feb 05, 2026) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Finfrastructure-noise)** (免费，官方)** — 光是 flaky sandbox 和 network jitter 就足以让 eval 分数上下波动几个点。在你相信任何一个 agent benchmark 数字之前，不管是你自己的还是别人的，都该先读这篇。
*重点关注：* trace sampling strategy、online evals 与 offline evals 的区别、metric 和 guardrail 的区别，以及为什么“CI gating”能把 evals 从一块仪表盘壁纸，变成真正的开发工具。
#### 2. 你必须实现的四种 eval
按照 Anthropic 在 “Demystifying evals for AI agents” 里的分类，你至少要覆盖这四种：
- Single-turn evals：给定这个输入，输出是否正确？这是最便宜的 eval，能做确定性 grader 的地方就尽量做，而且要频繁跑。
- Trajectory evals：agent 是否按正确顺序、用正确参数调用了正确工具？要覆盖单步、完整单轮和多轮三种变体。
- LLM-as-judge：适用于开放式输出，比如研究报告、代码评审。每周都要拿人工打过分的样本去校准。Anthropic 自己在 research-agent rubric 里用的是 0.0–1.0 打分，维度包括 factual accuracy、citation quality、completeness、source quality、tool efficiency。
End-state evals：适用于有状态 agent，比如会写数据库、会修改文件。直接把环境的最终状态和 ground truth 对比。这就是 τ-bench 的做法。
**参考资料：**
- [<text underline="true">**Demystifying evals for AI agents (Anthropic) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fdemystifying-evals-for-ai-agents)**(免费，官方)** — Anthropic 在这个主题上最好的一篇入门文章。
- [<text underline="true">**Evaluating Deep Agents: Our Learnings (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fevaluating-deep-agents-our-learnings%2F)**(免费)** — single-step、full-turn、multi-turn 这几类 trajectory eval 的实践指南。
- [<text underline="true">**How we build evals for Deep Agents (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fhow-we-build-evals-for-deep-agents%2F)** (免费)** — 上一篇的配套文章，讲他们是如何准备数据、设计指标和运行窄范围 eval 的。
- [<text underline="true">**Eval awareness in Claude Opus 4.6's BrowseComp performance (Anthropic) (Mar 06, 2026)**</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Feval-awareness-browsecomp)<text underline="true">** **</text>** (免费，官方)** — 模型会察觉自己正在被评估，并因此表现不同。设计 eval suite 之前要先读它，否则你会把偏差直接固化进去。
- [<text underline="true">**Designing AI-resistant technical evaluations (Anthropic) (Jan 21, 2026) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2FAI-resistant-technical-evaluations)** (免费，官方)** — 另一个配套问题：怎样设计出不容易被模型“刷分”的评测。如果你打算自己设计 benchmark，这是必读。
- [<text underline="true">**τ²-bench repository **</text>](https%3A%2F%2Fgithub.com%2Fsierra-research%2Ftau2-bench)**(免费，GitHub)** — 带政策合规性的多轮客服类 eval。
- [<text underline="true">**Establishing Best Practices for Building Rigorous Agentic Benchmarks (arXiv) **</text>](https%3A%2F%2Farxiv.org%2Fabs%2F2507.02825)** (免费)** — 在你设计任何原创 benchmark 之前先读它。SWE-bench、KernelBench、WebArena 都被证实会高估 5–33%。
*重点关注：* 能否写出确定性 grader、如何把 LLM judge 校准到接近人工评分、什么时候 pass^k 比 pass@1 更有意义，以及怎样发现并剔除被污染的 benchmark。
**实践项目：** 给你在 Phase 2 做的 research agent 外面包一层 regression harness。
建立一个 30–50 条、人工打过分的 golden dataset，覆盖三个难度等级（可以借鉴 GAIA 的 Level 1 / 2 / 3）。
凡是可以确定性判分的地方，就用确定性 grader（比如事实性问题的 exact match）；开放式输出则使用 LLM-as-judge，并配一套 5 个维度的评分 rubric。
做一套 trajectory eval：agent 是否做了规划、是否拉起了至少 2 个 sub-agents、是否给出 sources、是否在预算内完成？
接入 GitHub Actions：每一个 PR 都跑完整套 eval suite。只要 golden-set pass rate 掉了 3 个点以上，或者任一 `pass^4` 指标下降，就阻止合并。
加 production sampling：每天晚上自动用 LLM-as-judge 给 1% 的线上 trace 打分。监控 drift。
至少用 Inspect 把 agent 跑一次公开 benchmark：GAIA Level 1 或 τ²-bench retail 都可以。把你的结果和公开 leaderboard 对比。
再做一个 `make eval` target，让它产出三样东西：CI pass / fail summary、LangSmith experiment URL，以及一份带 canonical benchmark score 的 Inspect log file。
### 阶段 4 成果检查
完成这一阶段时，你应该能够：
- 选定一个 observability 平台，并基于架构理由为这个选择辩护
- 实现四种 eval：single-turn、trajectory、LLM-as-judge、end-state
- 维护一个会随着生产失败不断增长的 golden dataset，而不是靠 synthetic data 凑出来
- 在 eval 分数回退时，让 CI 直接阻止 PR 合并
- 做出一个 `make eval` target，产出 CI pass / fail summary、LangSmith experiment URL，以及包含 canonical benchmark score 的 Inspect log file
- 把你在自己的 agent 上发现过的 failure modes 全部文档化。那份文档才是真正的产品
---

## 阶段 5：生产加固（持续进行）
**这一阶段的目标：** 把你构建出来的一切，真正打磨到能扛住真实用户、真实成本和真实故障。
这不是一个会“结束”的阶段。
### 学什么
#### 1. 成本纪律
尽可能激进地使用 prompt caching。Anthropic 的 caching 可以让重复前缀的成本节省高达 90%。你的 `CLAUDE.md`、system prompt、tool definitions，都应该被缓存。
按难度做模型路由：简单轮次用 Haiku 4.5 或 Sonnet 4.6；规划与高难推理才上 Opus 4.7。
“advisor tool” beta（Anthropic，2026 年 3 月）允许你在生成过程中，让一个执行模型临时请教一个更高 IQ 的 advisor。
注意 Opus 4.7 的 tokenizer：虽然标价和 4.6 一样，但相同文本的 billable tokens 可能会多出大约 1.0–1.35×。每次迁移后都要重新测一遍 cost-per-task。
对非实时 workload，用 Batch API 可以打 5 折。
对 multi-agent（尤其是 Anthropic 那种 research 模式），你应该默认它大约会是 single-agent chat 的 15× token 开销。只有当答案的价值足以覆盖这笔成本时，才值得开 multi-agent。
**参考资料：**
- [<text underline="true">**Open Models have crossed a threshold (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fopen-models-have-crossed-a-threshold%2F)**(免费)** — GLM-5 和 MiniMax M2.7 在核心 agent 任务上（文件操作、tool use、instruction following）已经追平 closed frontier models。在你锁定模型选择与路由策略前，先读这篇。
*重点关注：* prompt caching 的边界、model routing 的规则、batch 和 real-time 的取舍，以及一个会被持续监控的硬性 cost-per-task 预算。
#### 2. 延迟
尽可能用 parallel tool calls。Anthropic 在研究系统的 prompt 里甚至会直接写明：“当你要创建多个 sub-agents 时，必须使用并行工具调用。” 你自己的 agents 也一样适用。
通过 LangGraph 的 `stream_mode="updates"` 向 UI 持续推送部分结果。
Sub-agent fan-out 是延迟优化里最大的杠杆：一个需要 60 步串行跑完的 agent，经过拆分后，可以变成“1 个 10 步 lead agent + 5 个并行的 10 步 sub-agents”。
*重点关注：* 哪里并行是安全的、哪里 streaming 会显著改善 UX，以及 fan-out 和 cost 之间是怎样相互作用的。
#### 3. 安全与沙箱
所有代码执行都必须在 sandbox 里：Modal、E2B、Daytona，或者 LangSmith Sandboxes（2026 年 3 月还在 private preview）。永远不要在主进程里直接 `exec()` 模型生成的内容。
所有 credentials 都必须在模型上下文之外被 broker 掉（Anthropic Managed Agents 的模式；如果是 SaaS auth，Composio 能直接帮你处理）。
Guardrail 要落在 hooks 上：用 `PreToolUse` hooks 阻止危险的 Bash、通过正则拦截 secrets、校验文件写入路径。
对于任何不可逆操作，都必须有 human-in-the-loop interrupts（LangGraph 的 `interrupt()` + `HumanInTheLoopMiddleware`，或者 Claude Agent SDK 的 permission prompts）。
**参考资料：**
- [<text underline="true">**Modal docs **</text>](https%3A%2F%2Fmodal.com%2Fdocs)** (免费)** — 默认首选的 Python 代码执行 sandbox。
- [<text underline="true">**E2B docs **</text>](https%3A%2F%2Fe2b.dev%2F)**(免费)** — 专门为 AI agents 设计的 code-execution sandboxes。
- [<text underline="true">**Beyond permission prompts: making Claude Code more secure and autonomous (Anthropic) (Oct 20, 2025) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fclaude-code-sandboxing)**(免费，官方)** — 关于 sandboxing 的基础文章。Claude Code 是如何对安全操作不再频繁请示、对危险操作进行隔离的。你的 harness 应该照着它的模式抄。
- [<text underline="true">**Claude Code auto mode: a safer way to skip permissions (Anthropic) (Mar 25, 2026) **</text>](https%3A%2F%2Fanthropic.com%2Fengineering%2Fclaude-code-auto-mode)**(免费，官方)** — 后续更新。重点是：当你允许 agent 无人值守地跑时，哪些设计会随之变化。在生产环境打开任何 “skip confirmation” 选项前，都先把这两篇读掉。
*重点关注：* 哪些动作是可逆的、哪些必须有人类批准，以及如何保证模型永远看不到它正在使用的那枚凭证。
#### 4. 监控与 drift
低规模阶段，可以 100% 采样 traces；高规模后则降到 1–10%，并对报错案例做分层采样。
你至少要对这些指标报警：token cost per request、tool-call failure rate、LLM-as-judge 的夜间均值、p95 latency、eval regression。
每次升级模型之后，都要重新做一次 eval baseline。
Anthropic 自己的工程博客已经明确提醒过：**“harness 往往编码了许多关于 Claude 自己做不到什么的假设；随着模型变强，这些假设会逐渐过时。”** 他们举的例子就是 Sonnet 4.5 → Opus 4.5 之后，context anxiety 相关的一些旧设计开始失效。
*重点关注：* 哪些东西应该报警，哪些只需要记录日志；怎样发现 prompt cache 失效；以及当模型已经走到 harness 前面时，你该如何识别出 harness ossification。
#### 5. 韧性
只要你的 agent 运行时间会超过 60 秒，durable execution（Inngest、Temporal 或 LangGraph `PostgresSaver`）就不是“可选”，而是必须。
每一个 node 后都要 checkpoint。你必须能 rewind，也必须能 fork。Pydantic Deep Agents 和 LangGraph 都支持这一点。Claude Agent SDK 的 session log，本质上也是等价物。
**参考资料：**
- [<text underline="true">**How My Agents Self-Heal in Production (LangChain) **</text>](https%3A%2F%2Fblog.langchain.com%2Fproduction-agents-self-heal%2F)**(免费)** — 一条真正能用的 pipeline：每次 deploy 后自动检测 regression，自动分析原因，自动开 fix PR，直到需要 review 之前都不必人工介入。这个模式值得直接拿来用。
*重点关注：* 哪些故障能自动恢复，哪些必须升级为人工处理，以及怎样在生产流量逼你面对问题之前，就先把 resume path 测清楚。
### 阶段 5 成果检查
这个阶段没有“结束”。但你至少应该具备：
- 在 system prompt、`CLAUDE.md` 和 tool definitions 上都接好了 prompt caching
- 有一层 model-routing，并配好硬性 cost-per-task 预算与报警
- 所有代码执行都进入 sandbox，并且有 credential broker 确保 secrets 永远不进上下文
- 有 hooks 阻止破坏性动作，并强制不可逆操作必须有人类批准
- 有 trace sampling、drift alerts，以及每次模型升级后的 re-baselining 仪式
- 有 durable-execution 层，让“进程被杀”不再是事故
---

## 建议
*这些都是你今天就可以直接采取行动的判断。*
如果你只深入学习一个 framework：LangGraph 1.0 + Deep Agents。
它是泛化能力最强的那一个，而且它的 runtime story 目前最成熟（`PostgresSaver`、time-travel debugging、durable execution、通过 LangSmith 实现对 OTEL 友好的 observability），模型无关，而且它的抽象方式（state graph + middleware）本身就是一套可迁移的通用心智模型。
就这样。
如果你只把一个 harness 当作参考对象来研究：Claude Agent SDK + Claude Code。
它就是参考标准。`CLAUDE.md`、Skills、sub-agents、hooks、plan mode、filesystem-as-memory pattern。到 2026 年，几乎所有其他 harness 都在向这些 primitives 收敛。
每天都用 Claude Code，读它的文档，再去研究那些开源 harness compendiums。
如果你只读一篇 context 相关的文章：
Anthropic 的 “Effective context engineering for AI agents”（2025 年 9 月）。
如果你只读两篇：再加上 LangChain 的 “Context Engineering for Agents”，把 Write / Select / Compress / Isolate 这套框架补齐。
如果你只学习一个 observability 工具：
如果你会继续待在 LangGraph 栈上，就选 LangSmith。
如果你想要 framework-agnostic 的 CI gating，就选 Braintrust。
如果你追求 benchmark 级 rigor，就选 Inspect（而且你迟早应该会上它）。
### 2026 年应该跳过的东西
AutoGen v0.4（已经并入 Microsoft Agent Framework，社区分支是 AG2，两边都不是强默认项）。
OpenAI Swarm（官方已经明确表示被取代，并且在 README 里直接写了“not production-ready”）。
Assistants API（将在 2026 年中退出）。
在你还没测出真实 recall 问题之前，就先去自己搭 vector store 或 memory 层。
除非你只是做一次性产物，否则不要上 no-code agent platforms。
### 只有在明确有理由时才使用
CrewAI。最快从点子到原型，但到了生产环境会非常脆。适合 hackathon 和 demo。
OpenAI Agents SDK。如果你是明确 OpenAI-locked，可以用。2026 年 4 月更新后加上了 sandboxing 和 harness，但你仍然被绑定在 OpenAI 模型上。
Pydantic AI / Pydantic Deep Agents。如果你的团队是严格类型驱动的 FastAPI 店，可以选。
Mastra。只有当你的团队是纯 TypeScript、而且没法用 Python 时才选。v1.0 于 2026 年 1 月发布，YC W25，22k+ stars，出自 Gatsby 团队。
Smolagents。最适合教学，用来理解 code-agent pattern 很好（它 1,000 行左右的代码库很容易 hack）。但生产能力弱。
DSPy 3.0 + GEPA。当你已经拥有一套明确指标，并且想用程序化方式去优化 prompts 和 agent topology 时再上。GEPA 在 ICLR 2026 oral 中，以 35× 更少的 rollouts，拿到了比 RL 高 6% 的结果。
Letta / MemGPT。如果你需要跨 session、像操作系统一样由 agent 自己管理 memory，可以用。否则 filesystem + Mem0 通常更简单。
### 值得收藏的 benchmarks（2026 年 5 月数据）
SWE-bench Verified：Claude Opus 4.7 ≈ 87.6%，GPT-5.5 ≈ 88.7%，Gemini 3.1 Pro ≈ 78.8%。
Terminal-Bench 2.0：GPT-5.5 82.7%，Opus 4.7 约 70%，Gemini 3.1 Pro 约 68%。
τ-bench：Claude Mythos Preview 以 89.2% 领先。
BrowseComp：GPT-5.5 90.1%，Gemini 3.1 Pro 85.9%，Opus 4.7 79.3%（比 4.6 的 83.7% 反而退步了。Web research 路由到 GPT-5.5 更合理）。
GAIA / Princeton HAL：Sonnet 4.5 以 74.6% 领先。
### 对技术底子不错、但 agent 经验为零的工程师来说，时间线大致应该是这样
第 2 周：Phase 0 完成。你已经能用大白话解释 harness。
第 5 周：Phase 1 完成。一个基于 Claude Agent SDK 的 agent 已经交付，至少带 1 个 Skill、1 个 hook、1 个 sub-agent。
第 9 周：Phase 2 完成。一个带 `PostgresSaver` durability 和 LangSmith traces 的 LangGraph deep-agent research analyst 已经跑起来。
第 13 周：Phase 3 完成。一个 1,500 行的 mini-harness 已经写完并文档化，在能力上可以和一个精简版 Claude Agent SDK 对比。
第 17 周：Phase 4 完成。你已经有 golden datasets、CI gates，以及至少一次通过 Inspect 跑出的公开 benchmark 结果。
然后永远进入：Phase 5。
如果你是边上班边做、每周只能投入 10–15 小时，那整个时间轴大概要乘以 2.5 倍。
会真正改变你计划的几个 benchmark 信号是：
如果 3 周之后你还没把 Phase 1 做出来，说明你的 tool design 出问题了（回去重读 “Writing tools for agents”）。
如果 Phase 2 超过 5 周还没做完，说明你正在试图“自己先把 harness 搭出来”。这时应该退回去，直接用 Deep Agents，不要跟它对着干。
---

## 注意事项
*如果你提前看不到这些坑，它们一定会把你绊住。*
Benchmark 是移动靶，而且其中不少已经被“游戏化”了。
SWE-bench Verified 的分数，在两年时间里已经从 1.96% 飙到了 80%+。
τ-bench 会加入 `pass^k` 这种一致性指标，正是因为单次运行准确率已经不再足够说明问题。
所以，当你看到任何 “X 模型拿到 Y%” 的说法时，都应该把它理解成：模型 + harness + scaffold + retry budget + system prompt 的联合结果，而不是模型自己单独的成绩。
对大多数用例来说，multi-agent 被过度神化了。
Anthropic 报出的 90.2% 提升，特指 breadth-first research 这类任务。
对于 coding 或那些强耦合任务，multi-agent 往往比 single-agent 更差，而且会多烧 15× tokens。
默认应该从 single-agent + sub-agents（用于有范围边界的探索）开始。只有当任务天然可拆时，才把它升级成 full multi-agent。
值得特别记住的反例是：Anthropic 那篇 2026 年 2 月 5 日的 “Building a C compiler with a team of parallel Claudes”https://anthropic.com/engineering/building-c-compiler它展示了一个 coding 任务，在正确拆分后，parallel sub-agents 的确带来了收益。Multi-agent 并没有在代码任务里彻底失效，它只是需要正确的 decomposition。
### 2026 年资料里的“推测性标记”
有几篇 “AI 2027” 风格的预测（比如 OpenBrain 450 亿美元营收）本身就是明确写着 fiction 的，却经常被别人当统计数字引用。忽略它们。
新品发布周的反应文章更多只是 anecdotal，它们能反映的是开发者情绪，而不是 benchmark。
### 框架格局仍然可能再次变化
LangChain 自己在 18 个月里已经换过两次 framing（chains → graphs → harnesses-on-graphs）。
Pydantic AI、Mastra、Deep Agents 里的任何一个，在未来 12 个月都可能进一步放大。
所以，请押注在抽象上：loop、tools、context、sub-agents、durability、traces。这些会迁移；某一个库的 API 细节未必会。
### MCP 在生产环境里的 rough edges 是真的存在的
Streamable HTTP 走过 load balancer、多租户认证、rate limiting、audit logging，这些都还明确写在 2026 年 MCP roadmap 上，意味着它们现在都还没有彻底解决。
你应该预期下一代 transport SEPs 会在 2026 年后半落地，所以不要把你的系统和当前 session model 绑得太死。
### 模型在小版本更新之间也会变
Opus 4.7 更严格的 instruction-following 和新的 tokenizer，意味着你给 Opus 4.6 写的 prompts，到了 4.7 可能不仅行为不同，而且在相同文本上最多还会多花 35% tokens。
每一次模型升级，都要重新回放一遍真实流量。
### 你的 eval suite 一定会老化
今天搭出来的 golden dataset，只要模型继续进步，几个月内就会被“做穿”。
要计划好每个季度从生产失败案例里新增 10–20%，而不是靠 synthetic data 去填。
对 LLM-as-judge 的人工校准，也必须长期持续进行。
### 这份路线图里的一些来源本身带有 vendor 营销属性
能用一手资料时，尽量回到一手资料：Anthropic engineering blog、LangChain blog、OpenAI announcements、arXiv。
那些 “best of 2026” 排名型文章（Alice Labs、Channel.tel、GuruSup、Morph、Vstorm）是有参考价值的，但每一家都有商业激励。
当它们彼此结论一致，并且又和一手工程资料吻合时，这种共识就相对可靠。
---

## 结语
走完这条路线图之后，你大概可以期待什么？
我想非常坦诚地告诉你，不加糖衣。
这份路线图不会在 17 周里把你变成 principal AI engineer。
但它会把你变成那种能够构建并交付 agent systems，而且这些系统真的能在生产流量里活下来的工程师。
而这恰恰就是公司现在真正愿意为之付费的能力。
对于能够交付 production agents 的工程师，需求并没有在放缓。
LangChain 的 State of Agent Engineering 报告里，已经有 57% 的团队把 agents 上到了生产，其中 89% 已经接了 observability。
质量是第一大障碍（32%），这意味着整个行业现在真正卡住的，不是那些会调一个 LLM API 的工程师，而是那些能搭 evals 和 harnesses 的工程师。
Anthropic 自己的那个数字最能说明机会在哪里：同一个模型，不同 harness，78% vs 42%。
这个差值，就是你的工作。
harness-engineering 这个转向，是当前软件招聘市场里被低估最严重的一块机会。
很多公司还在发 “prompt engineer” 的 JD。
但他们真正需要的，是那种能把 frontier model 变成一个可测量、可持续、可交付生产系统的工程师。
现在，我真正希望你从这一切里带走的是这些：
- 每个阶段选 1 个项目，亲手把它做出来。不是“读完”。而是亲手去做、去搞坏、去修、去部署，然后把 LangSmith trace 和 benchmark score 放进你的 README。最终被雇佣的工程师，是能给你看 trace 的人，而不是能背框架对比表的人。
- 开始公开分享你的学习过程。写出你的 mini-harness post-mortem。发布你对 golden dataset 的发现。把 benchmark 数字连同对应的 harness configuration 一起发出来。教学是学得最快的方式，而且它还能同步建立你的声誉。最好的机会往往来自“被看见的工程师”，而不是海投了 500 个岗位的人。
- 也请不要等到“感觉自己准备好了”才开始。你永远不会真的有这种感觉。很多工程师永远卡在 “我在读 LangChain 博客” 和 “我已经交付了一个带 `PostgresSaver` durability 的 deep agent” 之间的那条缝里。
- 只要你有一个能跑通的 agent，就立刻开始申请、开始公开构建、开始交付。哪怕它很小。市场不会奖励完美主义。市场奖励的是那些能让模型做成一件真实事情，而且还能证明它没有退化的工程师。
17 周足够改变很多事，只要你真的把这些工做下去。
而我相信每一个读到这里的人都能做到。
继续构建，也继续测量你构建出来的东西。
---

*这篇文章基于作者自己的内部笔记，以及过去 2 到 3 个月持续整理出的记录写成，并由 Minimax 2.7 进行编辑。
我在 Obsidian 里维护了一条内容生产流水线，它会调用这些材料，并按照我的风格，用我手写和手打的笔记来完成写作。*