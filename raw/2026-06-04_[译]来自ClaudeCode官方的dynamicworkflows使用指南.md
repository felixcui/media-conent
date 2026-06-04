# [译]来自 Claude Code 官方的dynamic workflows使用指南

**作者**: AI技术立文

**来源**: https://mp.weixin.qq.com/s/1eSGt71P-PeaGszs2cikTw

---

## 摘要

Claude Code 官方发布的动态工作流功能允许 Claude 即时生成专属的 JS 执行框架来协调子智能体。该功能打破了默认框架在单一上下文中处理复杂任务的局限，支持自定义模型选择与独立工作树隔离，并具备中断恢复能力。它尤其适用于深度研究、安全分析、代码评审及大规模并行等复杂场景，能将性能发挥到极致，但需注意其较高的 token 消耗。

---

## 正文

AI技术立文 AI技术立文

在小说阅读器读本章

去阅读

ps: 文章来自 Claude Code 团队的Thariq Shihipar

---

上周，我们在 Claude Code 中发布了动态工作流（dynamic workflows） <sup>[1]</sup> 。现在，Claude 可以即时为手头的任务编写专属的执行框架（harness） <sup>[2]</sup> 。

Claude Code 默认的执行框架是为编程而生的，但它对许多其他类型的任务同样好用——因为事实证明，很多任务本质上都很像编程任务。不过，有些类别的任务，我们必须在 Claude Code 之上专门搭建定制的执行框架，才能把性能逼到极致，比如深度研究（Research） <sup>[3]</sup> 、安全分析 <sup>[4]</sup> 、智能体团队（agent teams） <sup>[5]</sup> 或代码评审（Code Review） <sup>[6]</sup> 。

动态工作流让你能够动态地创建执行框架，使 Claude 能够在 Claude Code 内部原生地解决上述所有问题，乃至更多。你还可以把这些工作流分享出去，供他人复用。

在这篇文章里，我会分享我使用工作流的初步体验和心得，帮你充分发挥它的威力。

话虽如此，最佳实践仍在不断成型中！动态工作流往往会消耗更多 token，所以要仔细斟酌何时、如何使用它。

注：本文也发布在 Claude 博客上 <sup>[7]</sup> 。

## 目录

- 一、示例提示词
- 二、动态工作流如何运作
- 三、为什么需要动态工作流
- 四、使用动态工作流时的实用模式
- 五、用例
- 六、构建动态工作流的技巧
- 七、一个全新的世界

---

## 一、示例提示词

在深入技术细节之前，我想先抛出几个示例提示词，帮你打开思路，想象一下工作流能做到什么：

- “这个测试大概每跑 50 次就会失败 1 次。建一个工作流来复现它，提出几种假设，并在不同的 worktree 里对它们做对抗式验证。/goal：在某一种假设被证实之前，不要停下来。”
- “用一个工作流，翻一遍我最近的 50 次会话，从中挖出我反复在做的纠正，把那些反复出现的归纳成 CLAUDE.md 规则。”
- “用一个工作流，翻查过去半年 Slack 里 #incidents 频道的内容，找出那些反复出现、却没人提工单的根因。”
- “拿我的商业计划书，跑一个工作流，让不同的智能体分别从投资人、客户和竞争对手的视角把它批得体无完肤。”
- “这里有一个装着 80 份简历的文件夹，用一个工作流按后端岗位给它们排名，并对排在前十的再复核一遍。用 AskUserQuestion 工具向我发问，整理出一套评分标准。”
- “我需要给这个命令行工具起个名字。用一个工作流头脑风暴一堆候选项，再跑一场锦标赛挑出前 3 名。”
- “用一个工作流，把我们代码里所有的 User 模型重命名为 Account。”
- “过一遍我的博客草稿，用一个工作流对照代码库逐条核实每一个技术论断——我可不想发出去任何有错的东西。”

---

## 二、动态工作流如何运作

动态工作流会执行一个 JavaScript 文件，其中包含若干特殊函数，用来生成并协调子智能体（subagents） <sup>[8]</sup> ：

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic2nyVZnAicu5QlFwGf7mRJ9VcWhIdy8MC92ibJ6GgaEQXBxMZfhmaWjoyCjwWELDAdCHwcnutjZU0bfbcweEhKfibSCM7t4icTdCCY/640?wx_fmt=jpeg&from=appmsg)

动态工作流也包含标准的 JavaScript 函数，比如 JSON、Math 和 Array，用来处理数据。

有一点尤其值得了解：动态工作流可以决定每个智能体使用哪个模型，以及子智能体是否运行在各自独立的 worktree（Git 工作树）中——这让 Claude 能够按需选择所需的智能水平和隔离程度。

如果工作流被中断了，比如被用户操作打断，或退出了终端，那么恢复会话时，工作流可以从上次停下的地方接着跑。

---

## 三、为什么需要动态工作流

当你让默认的 Claude Code 执行框架去做一项任务时，它必须在同一个上下文窗口里既做规划、又做执行。对许多编程任务而言，这非常有效；但面对长时间运行、大规模并行和／或高度结构化的对抗性任务时，它有时会力不从心。

这是因为，Claude 在单个上下文窗口里处理一项复杂任务的时间越长，就越容易陷入几种特定的失败模式：

- **智能体惰性（agentic laziness）：** 指 Claude 在一项格外复杂、由多个部分组成的任务还没干完时就停了下来，在只完成部分进度后就宣告大功告成——比如安全评审的 50 个条目里只处理了 20 个。
- **自我偏好偏差（self-preferential bias）：** 指 Claude 倾向于偏袒自己产出的结果或发现，尤其是在被要求对照评分标准来核实或评判它们的时候。
- **目标漂移（goal drift）：** 指在多轮交互中逐渐丢失对原始目标的忠实度，尤其是在上下文压缩（compaction）之后。每一次摘要都是有损的，像边界情况的要求、或者“不要做 X”这类约束，都可能在过程中丢失。

创建一个工作流，通过编排多个各自拥有独立上下文窗口、目标聚焦且彼此隔离的 Claude，就能有效对抗这些问题。

### 3.1 动态工作流 vs 静态工作流

你以前或许用 Claude Agent SDK 或 `claude -p` 创建过静态工作流，把多个 Claude Code 实例协调到一起。

但因为静态工作流需要应对所有边界情况，它们通常更通用、也更笼统。有了 Claude Opus 4.8 <sup>[9]</sup> 和动态工作流，Claude 现在已经足够聪明，能为你的具体用例量身编写一个定制的执行框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IUJGIjicknic2kxeDIFZoesL5Dv4NOdjPsZ7D9Cxw7aY1S8PRnC6QUw9tuhicAOticgG3ypsyrQosuKSR72NwcCcpoBCR7WWicvWP03AEBVsv4Hc/640?wx_fmt=png&from=appmsg)

---

## 四、使用动态工作流时的实用模式

你只需让 Claude 创建一个工作流，就能开始使用动态工作流；或者使用触发词 “ultracode” 来确保 Claude Code 创建一个工作流。

但是，建立起一套关于动态工作流如何运作的心智模型，会帮你理解何时该用它，以及如何通过提示词来引导 Claude。

Claude 在构建工作流时，可能会用到、并组合使用以下几种常见模式：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic1icia8KBv0ciaAGSOzlCZwoia90qyQxicQmyicxp2X6evwPa7bJgdNqDjkqsSYeaMVvAOhHjGiawWWNjIibjdickIicLJAO9Ko0JDL3ax2Q/640?wx_fmt=jpeg&from=appmsg)

#### 4.1.1 分类并执行（Classify-and-act）

用一个分类智能体来判定任务的类型，然后根据任务类型路由到不同的智能体或行为。也可以在末尾用一个分类器来决定最终输出。

#### 4.1.2 扇出并汇总（Fan-out-and-synthesize）

把一项任务拆分成许多更小的步骤，对每个步骤跑一个智能体，再把这些结果汇总起来。当步骤数量很多，或者每个步骤都能从自己干净的上下文窗口中受益（避免互相干扰或交叉污染）时，这种模式尤其有用。汇总步骤是一道屏障——它会等待所有扇出的智能体全部完成，再把它们的结构化输出合并成一个结果。

#### 4.1.3 对抗式校验（Adversarial verification）

对每一个被生成的智能体，再跑一个单独的智能体，对照评分标准或评判准则，对它的输出做对抗式校验。

#### 4.1.4 生成并筛选（Generate-and-filter）

围绕一个主题生成若干想法，再用评分标准或校验来筛选它们，去除重复项，只返回质量最高、经过验证的想法。

#### 4.1.5 锦标赛（Tournament）

不是把工作分摊出去，而是让智能体们就同一件工作展开竞争。生成 N 个智能体，每个都用不同的方法尝试同一项任务。然后由提示词或模型借助一个评判智能体，以成对比较（pairwise）的方式评判结果，直到决出优胜者。

#### 4.1.6 循环至完成（Loop until done）

对于工作量未知的任务，不要用固定的遍数，而是循环生成智能体，直到满足某个停止条件（不再有新发现，或日志里不再有错误）为止。

---

## 五、用例

请发挥创意，去想象何时、如何让 Claude Code 创建动态工作流。我发现，工作流有时在非技术性的工作上甚至更有用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IUJGIjicknic1XcJYibGM2PmCkicLKD9icpR0TJFaNwQKJ4fVuXofNcVBcKkaZt5UpQ5uwoORpWJ8yT3naBcWyibDsDG3Z0A16wZORw8ibRDdzdwY8/640?wx_fmt=png&from=appmsg)

### 5.1 迁移与重构

Bun <sup>[10]</sup> 就是用工作流从 Zig 重写为 Rust 的。关于具体怎么做的，你可以在 Jarred 的 X 帖子 <sup>[11]</sup> 里读到更多。

关键在于把任务拆解成一系列需要逐个处理的步骤，比如各个调用点、失败的测试、各个模块等等。为每一处修复在一个 worktree 里分出一个子智能体去做修改，然后让另一个智能体做对抗式评审，最后合并。可以考虑告诉智能体不要使用消耗资源的命令，这样你就能最大化并行，而不至于把机器的资源耗尽。

### 5.2 深度研究

我们在 Claude Code 内部发布了一个深度研究技能（ `/deep-research` ），它就用到了动态工作流。具体来说，它会扇出多路网络搜索、抓取信息源、对它们的论断做对抗式校验，最后汇总成一份带引用的报告。

但你做这类研究，未必只针对网络搜索。比如，你可以让 Claude 从 Slack 的上下文中整理出一份状态报告，或者通过深入探查代码库来研究某个功能是如何运作的。

### 5.3 深度核查

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic2xszecxmAVGKs9aA6TuTDPbFc9IGibEbMxj1HASgMBf1hsnDSgLXJ9d8wne1gNMtfa0mGm035IB34ruTRDBxLduaJk4aMvrGlE/640?wx_fmt=jpeg&from=appmsg)

反过来说，如果你有一份报告，想要核对并溯源它引用的每一个事实性论断，那么你可以生成一个工作流：让一个智能体识别出所有的事实性论断，然后为每一条分出一个子智能体去逐一详细核查。你还可以让一个校验智能体去检查那个溯源的子智能体，确保它找到的信息源质量过硬。

### 5.4 排序

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic18O77KorWpiabLLj8uhmVQVXiccXAWuG5wbrJqM62sXZMia9zxaVl1NPFYxUUL2O4x5iczlqjnVm3CuZzT5bBytDv1LyXL0TjiccJU/640?wx_fmt=jpeg&from=appmsg)

你可能有一份条目清单，想按某种定性的标准来排序——你相信 Claude Code 擅长做这类评估，比如：按 bug 的严重程度对工单排序。但如果你想在一个提示词里排 1000 多行，质量就会下降，而且也塞不进上下文。换个做法：跑一场锦标赛，搭一条成对比较智能体的流水线（比较式判断比绝对打分更可靠），或者并行做分桶排名再合并。每一次比较都是一个独立的智能体，因此那个确定性的循环掌控着整个对阵，只有当前的排序结果停留在上下文里。

### 5.5 记忆与规则遵循

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic3JuKUGcGkc9JRuRh3picO1dpwakenBqRvR5Diao0icf5gdibvAAhPTicEHLibBRGo12kNiaH4ZWOdNtuB8Q55HFkPf1tPc2kOSZPiaS0w/640?wx_fmt=jpeg&from=appmsg)

如果有某一套规则是你发现 Claude 总是漏掉或难以遵守的——哪怕已经写进了 CLAUDE.md——那就创建一个工作流，列出必须由校验智能体逐条检查的规则，一条规则配一个校验者。再创建一个“怀疑论者”人设的子智能体去复核这些规则，确保它们合情合理，有助于避免太多误报。

反方向也行得通：从你最近的会话和代码评审意见中，挖出你反复在做的纠正，用并行的智能体把它们聚类，对每个候选规则做对抗式校验（这条规则真能避免一个真实的错误吗？），然后把幸存下来的提炼回 CLAUDE.md <sup>[12]</sup> 里。

### 5.6 根因排查

调试的最佳方式，是提出几个相互独立的假设并逐一验证；但如果你只用一个上下文窗口，Claude 就容易陷入自我偏好偏差。

工作流可以从结构上杜绝这一点：生成多个智能体，让它们从互不相交的证据中提出假设。比如，分别为日志、文件和数据各设一个智能体。然后，每个假设都要面对一组校验者和反驳者的检验。

这不只适用于代码。工作流也能用于销售（为什么三月份销售额下滑了？）、数据工程（这条数据管道为什么失败了？），或任何复盘场景。

### 5.7 规模化分流

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic2t9UzK5xkSq910AqbDfCEg0D5VFWKcFAILZsF6V4BhnndH7BicRtVez7fia7ZRmtvkWokvTjsqQ0ia0flb15yw7oew80N7gnhKqI/640?wx_fmt=jpeg&from=appmsg)

每个团队都有一个支持队列、bug 报告，或其他靠人力无法完全处理的积压工作。

一个分流（triage）工作流会对每个条目分类、与已跟踪的内容去重，并采取行动。这可能意味着尝试修复，或者上报给人类用户。

分流工作流有一个实用模式叫“隔离区（quarantine）”：禁止那些读取不可信公开内容的智能体执行高权限操作，这些操作改由负责处理信息的智能体来完成。

把分流工作流和 `/loop` 配合使用，就能让 Claude 持续不断地做这件事。

### 5.8 探索与品味

当你在探索某个解决方案的不同路径时，工作流会很有用——尤其当它偏向品味判断（比如设计或命名），并且能从一套评分标准中受益时。

不妨让 Claude 探索一堆解决方案，并给一个评审智能体一份评分标准，说明什么样的方案才算好。当评审智能体认为已满足这些标准时，任务即告完成。方案也可以基于评分标准，通过锦标赛来排序或挑选。

### 5.9 评测

你可以为特定任务跑一些轻量级评测：在一个 worktree 里分出几个独立的智能体，再分出一些比较智能体，对照评分标准来比对并给具体的产出打分。比如，针对某个特定标准，评估并随后改进你创建的一个技能。

### 5.10 模型与智能路由

创建一个针对你的任务调校过的分类智能体，由它来决定使用哪个模型。当你的任务会涉及大量工具调用时，这会很有帮助——在执行之前先做一番研究，就能为这项工作找出最合适的模型。

举例来说，“讲讲 auth 模块是怎么工作的”这个任务，最适合用哪个模型，取决于 auth 模块里有多少文件、以及代码库的形态。一个分类智能体可以先做这番调研，再根据任务的预期复杂度路由到 Sonnet 或 Opus。

### 5.11 什么时候不该用动态工作流

工作流是新东西。虽然在许多用例上它会带来超额的成效，但并非每个任务都需要它，而且它可能最终会消耗多得多的 token。

最好把工作流创造性地用在那些你以前没能尝试过的、推动 Claude Code 更进一步的地方。对于常规的编程任务，不妨先问问自己：它真的需要更多算力吗？比如，大多数传统编程任务并不需要一个由 5 位评审者组成的小组。

---

## 六、构建动态工作流的技巧

### 6.1 提示词

为动态工作流编写详尽的提示词，并运用我们上面描述的那些具体技巧，能带来最好的结果。

工作流不只是为大任务准备的。你可以提示模型使用一个“快速工作流”。比如，你可以针对某个假设，快速跑一轮对抗式评审。

### 6.2 与 /goal 和 /loop 配合

当使用那些可重复的工作流（比如分流、研究或核查）时，把它们与 `/loop` 配合，让其按固定间隔运行；再用 `/goal` 设定一个硬性的完成要求。

### 6.3 token 用量预算

你可以为动态工作流设定明确的 token 用量预算，限制一项任务能消耗多少 token。你可以用一个预算来提示它，比如“用 10k token”，这就会设下上限。

### 6.4 保存与分享动态工作流

在工作流菜单里按 “s” 即可保存工作流。你可以把它们签入 `~/.claude/workflows` ，或者通过技能（skill）来分发。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic30zcE0lrXy9wevaIhO0iciaAW4MribIdIRrjtDfD7F9Fg3UoTDBvGEHENUD0ibRuWJFic23xm6zph8eibaZ39PBIwfIH0H2quWmfjqE/640?wx_fmt=jpeg&from=appmsg)

要通过技能来分享它们，就把你的 JavaScript 工作流文件放进技能及其文件夹，并在 SKILL.MD <sup>[13]</sup> 中引用它们。为了获得更大的灵活性，你或许想提示 Claude：把技能里的工作流当作模板，而不是一个必须逐字运行的脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic270WfQYEeb1HHgZOA47Fib1NDfPft9Ry28etPM5sGCNxfMibBt9x4ypXcbGQbbicvmmNGZ5wP4FDNynTM0lYHvZP4m6fDheEtqeg/640?wx_fmt=jpeg&from=appmsg)

---

## 七、一个全新的世界

工作流是扩展 Claude Code 的一种好用的新方式。我鼓励你把它当作一个起点——关于如何最好地使用它们，还有很多有待发掘。期待听到你的发现。

Thariq Shihipar 与 Sid Bidasaria（@sidbid）是 Anthropic 的技术团队成员，负责 Claude Code。

![图像](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic2MicRPoN2IagMB1h6HbbH8DwzzXBM3A4mNcowEL8ZzSz0CpOWNTpKCeiaqxwKcTAwlMel3ncJPpo98UiaffKbickTrIrCTHIG63OE/640?wx_fmt=jpeg&from=appmsg)

## 参考链接：

\[1\]https://code.claude.com/docs/en/workflows

\[2\]https://code.claude.com/docs/en/glossary #agentic -harness

\[3\]https://support.claude.com/en/articles/11088861-using-research-on-claude

\[4\]https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code

\[5\]https://code.claude.com/docs/en/agent-teams

\[6\]https://code.claude.com/docs/en/code-review

\[7\]https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code

\[8\]https://code.claude.com/docs/en/sub-agents

\[9\]https://www.anthropic.com/news/claude-opus-4-8

\[10\]https://bun.com/

\[11\]https://x.com/jarredsumner/status/2060050578026189172

\[12\]http://claude.md/

\[13\]http://skill.md/

继续滑动看下一个

AI技术立文

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过