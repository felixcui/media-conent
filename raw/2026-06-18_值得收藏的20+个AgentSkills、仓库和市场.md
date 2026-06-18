# 值得收藏的 20+ 个 Agent Skills、仓库和市场

**来源**: https://waytoagi.feishu.cn/wiki/BLpDwvdheiDduqkXf26cHYYjnqg

---

## 摘要

本文介绍了20多个值得收藏的智能体技能仓库、市场及工具。文章指出Skill是编码智能体的复用单元，通常通过包含SKILL.md的文件夹一次性教会智能体特定能力以避免重复解释。文中列举了GitHub上按受欢迎程度排名的热门技能库，包括obra/superpowers、anthropics/skills、mattpocock/skills等，涵盖智能体框架、工程配置、UI/UX设计、知识图谱生成、求职。

---

## 正文

# 值得收藏的 20+ 个 Agent Skills、仓库和市场

原文链接：https://generativeprogrammer.com/p/20-agent-skills-repos-and-marketplaces

![图片展示了GitHub上最热门的智能体技能排行榜，统计了1,119个技能。其中，olbrw/superpowers以21个技能、22.7k星标数居首；anthropics/skills有17个技能、150k星标数排名第二；mattpeacock/skills、garrytan/gstack等技能库也榜上有名。绿色技能库代表是真实合集，橙色条形图代表总星标数，红色火焰图标表示增长速度。该图与文档中介绍值得收藏的智能体Skill等内容相关，直观呈现了技能的受欢迎程度。](https://feishu.cn/file/MCs2bkSkXohkuwxerzucZDAXnWb)

一张粗略的受欢迎程度排行榜，不是质量排名。

| 排名 | Star 数 | 说明 | 仓库 |
|-|-|-|-|
| 1 | 228,740 | 智能体 Skill 框架与开发方法论。 | [obra/superpowers](https://github.com/obra/superpowers) |
| 2 | 151,088 | Anthropic 官方公开 Agent Skills 仓库。 | [anthropics/skills](https://github.com/anthropics/skills) |
| 3 | 130,016 | Matt Pocock 的真实世界 Skill 配置。 | [mattpocock/skills](https://github.com/mattpocock/skills) |
| 4 | 110,407 | 面向高管、设计、工程、文档和 QA 的 Claude Code 配置。 | [garrytan/gstack](https://github.com/garrytan/gstack) |
| 5 | 92,040 | 用于改进 UI/UX 的设计智能。 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| 6 | 60,442 | 把代码转成可交互知识图谱。 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) |
| 7 | 60,265 | 面向编码智能体的生产级工程 Skill。 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| 8 | 53,903 | 使用 Claude Code Skill 模式驱动的 AI 求职系统。 | [santifer/career-ops](https://github.com/santifer/career-ops) |
| 9 | 44,469 | 让智能体远离泛化输出的品味 Skill。 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| 10 | 42,815 | 研究 Reddit、X、YouTube、HN 和网络上的趋势。 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |

这是一份带有主观取舍的清单，收录了值得安装、收藏，或作为自建模板参考的智能体 Skill、合集、市场和相关工具。

Skill 是编码智能体的复用单元。它通常是一个包含 `SKILL.md` 的文件夹，用来一次性教会智能体某种能力，这样你就不必在每次会话里反复解释；只有当任务需要时，智能体才会加载它。如果你想了解背景，Anthropic 的 [《为真实世界配备 Agent Skills》](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) 和 [Claude Code Skill 文档](https://code.claude.com/docs/en/skills) 是最值得先读的两个一手来源。

这篇文章是 [《智能体编码阅读清单》](https://generativeprogrammer.com/p/the-agentic-coding-reading-list) 的配套篇。那份清单整理了值得关注的人，而这一篇整理值得安装的能力。

核心判断是：最好的 Skill 通常是你为自己的代码库写的那个。但你不该从空文件夹开始。先安装那些已经被验证过的 Skill，学习它们的形态，然后再写自己的。下面每个链接都已经被验证过。这就是资源库。



## 短版路径

如果你只想知道安装顺序，可以按这个来：

1. 从官方仓库开始，学习一个好的 `SKILL.md` 应该长什么样。
2. 收藏市场和精选列表，用来发现新东西。
3. 在收集单个Skill之前，先安装一个工作流框架。
4. 为你实际使用的技术栈添加厂商 Skill。
5. 当你第三次重复同一条指令时，把它写成自己的 Skill。

> Skill 正在变得可移植。它们起源于 Claude 生态，但 `SKILL.md` 格式正在扩散。OpenAI 现在也记录了 [ChatGPT 里的 Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) 和 [面向 Codex 的 Agent Skills](https://developers.openai.com/codex/skills)，这里的几个合集已经可以跨 Claude Code、Codex、Cursor 和 Gemini 运行。选择 Skill 时，看它能做什么，而不是看它属于哪一家厂商。

## 从哪里获取

在讨论任何单个 Skill 之前，先知道它们在哪里。先从源头开始，再向外扩展。

- [anthropics/skills](https://github.com/anthropics/skills) 是 Claude 官方仓库，也是正确的第一站。它包含 Claude 自带的文档 Skill、`mcp-builder` 和 `skill-creator`，后者还会在文章末尾再次出现。读几个这里的 Skill，是学习优秀 `SKILL.md` 形态最快的方法。
- [openai/skills](https://github.com/openai/skills) 是另一边的同类仓库：Codex 的官方 Skill 目录，里面包括 [Linear Skill](https://github.com/openai/skills/blob/main/skills/.curated/linear/SKILL.md) 这样的现成集成。它的存在是一个很清晰的信号：Skill 正在成为跨智能体格式，而不只是 Claude 的惯例。
- [Claude Skills Marketplace](https://skillsmp.com/) 是社区 Skill 的可搜索目录。当你心里有一个具体任务，想在自己动手写之前看看是否已有现成方案时，就去这里。
- [Smithery](https://smithery.ai/) 是 Skill 和 MCP server 的注册表，支持一条命令安装。适合你想快速接上某个东西，而不是手动克隆和复制文件时使用。
- [Agensi](https://www.agensi.io/) 补上了市场这一层，里面也包含付费 Skill。即使你大多数时候安装的都会是免费资源，也值得知道商业层已经存在。

## 我会收藏的合集

![](https://feishu.cn/file/P9pRbLhKFoCSG0xK0ICchmyyn26)

真正有用的启发不是“安装最大的盒子”，而是“研究什么东西正在获得关注，以及它为什么会获得关注”。

三个精选列表会帮你做过滤。当一个新 Skill 开始流行，它通常会先出现在这些地方，然后才进入官方仓库。

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) 是 Claude Skill、资源和工具的广义精选列表。当我想快速了解整个版图时，这是我第一个查看的地方。
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) 收集了来自官方开发团队和社区的一千多个 Skill，并标注了它们能在哪些智能体上运行。如果你不是只用 Claude，它在跨 CLI 覆盖上更强。
- Murat Can Koylan 的 [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) 更聚焦：它收录面向上下文工程、多智能体架构和生产级智能体系统的 Skill。当你是在构建智能体，而不只是使用智能体时，可以优先看它。

## 先装框架，而不是单个 Skill

最高杠杆的动作不是安装某一个 Skill，而是安装一个连贯的合集，让它带来一整套工作方式。下面是我自己在用的一个，加上两个被广泛关注、值得研究的合集。

- Jesse Vincent 的 [superpowers](https://github.com/obra/superpowers) 与其说是一堆零散的Skill，不如说是一个智能体 Skill 框架和开发方法论。它给智能体建立有纪律的习惯：先头脑风暴再构建、测试驱动开发、系统化调试、编写并执行计划，以及在正确时机请求评审。这是我每天都在运行的那个，因为它改变的是智能体的工作方式，而不只是智能体知道什么。
- [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) 把 Andrej Karpathy 关于语言模型写代码时容易出错之处的观察，浓缩成一个可以直接放进去的护栏。我这里也安装了它。它很小，但效果不成比例地大：在问题进入你的代码差异之前，就先拦下了常见失败模式。
- Garry Tan 的 [gstack](https://github.com/garrytan/gstack) 把他自己的 Claude Code 配置打包给任何人采用：几十个带立场的工具，分别充当 CEO、设计师、工程经理、发布经理和 QA。当你想要一套完整、预接线的工作方式，而不是自己组装零件时，可以用它。
- Matt Pocock 的 [mattpocock/skills](https://github.com/mattpocock/skills) 是“真实工程师的 Skill，直接来自我的 `.claude` 目录”。一个实践者的真实设置，往往比那些专门为了分享而构建的东西更有用。

## 面向你技术栈的最佳实践

最有用的类别之一，是来自你本来就在使用的工具的官方 Skill。这指向了团队发布知识的真实变化。过去是发布一个希望你阅读的文档站；现在越来越多团队会发布一个由智能体运行的 Skill：把最佳实践变成规定性、可执行的东西，而不是留成一份希望别人会遵守的指南。

这些是我会安装来匹配自己技术栈的 Skill。

- PlanetScale 的 [database-skills](https://github.com/planetscale/database-skills) 教智能体正确处理数据库、schema、查询和迁移，而不是编造看起来正确但会静默出错的 SQL。你可以把它和 [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) 配合使用，后者面向 Neon 的无服务器 Postgres，还包括一个会给智能体分配真实数据库的 [claimable Postgres](https://github.com/neondatabase/agent-skills/blob/main/skills/claimable-postgres/SKILL.md) Skill；再加上 [redis/agent-skills](https://github.com/redis/agent-skills)，把缓存也做对。
- Vercel 工程团队的 [next-skills](https://github.com/vercel-labs/next-skills) 覆盖前端这一半，其中 [next-best-practices](https://github.com/vercel-labs/next-skills/tree/main/skills/next-best-practices) 会让智能体保持在框架预期的模式内。[supabase/agent-skills](https://github.com/supabase/agent-skills) 对 Supabase 平台做了类似的事。
- 厂商名单现在读起来就像一张技术栈图：[Stripe](https://github.com/stripe/ai) 负责支付，[Cloudflare](https://github.com/cloudflare/skills) 负责边缘，[HashiCorp](https://github.com/hashicorp/agent-skills) 负责 Terraform，[Hugging Face](https://github.com/huggingface/skills) 负责模型，[Trail of Bits](https://github.com/trailofbits/skills) 负责安全，旁边还有 Netlify、Sanity、WordPress 和 Expo。检查一下你依赖的工具有没有发布 Skill。越来越多工具已经有了。

## 按你的工作选择 Skill

越过框架之后，剩下的就更偏角色。你做什么，就抓和工作匹配的 Skill。这类 Skill 远不止下面这些，但这四个正好对应四种工作。如果你沿着这条路走得足够远，迟早会想要一个还不存在的 Skill，那就是下一节。

- 软件工程师会想要 Addy Osmani 的 [agent-skills](https://github.com/addyosmani/agent-skills)：一组生产级工程 Skill。它不像单个Skill，更像是一套关于谨慎、可维护代码如何被写出来的框架。
- 设计师会想要 Nexu 的 [open-design](https://github.com/nexu-io/open-design)：一个本地优先、开放的 Claude 设计工具替代方案，可以把智能体变成能在多个智能体 CLI 中生成界面、原型和幻灯片的工具。
- 写作者会想要 [humanizer](https://github.com/blader/humanizer)，它会去掉 AI 生成文本中的痕迹：那些让草稿读起来像机器写出来的措辞和节奏。
- 研究者和永远好奇的人会想要 Matt Van Horn 的 [last30days-skill](https://github.com/mvanhorn/last30days-skill)。它会跨 Reddit、X、YouTube、Hacker News、Polymarket 和开放网络研究任意主题，然后综合出有根据的摘要。它不是在写代码，而是在你写代码之前收集当前的信源。

## 如果这些都不合适，就自己构建

沿着这份清单走到这里，你迟早会遇到那个“应该存在但还不存在”的 Skill。一旦你已经看过一个好的 `SKILL.md` 应该是什么形状，你自己那些反复出现的指令，就是下一批应该被捕获的东西。现在已经有两个 Skill 能帮你做这件事。

- [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 是 Anthropic 用来构建 Skill 的 Skill。它会生成一个新的 Skill，并且按照这套方法论让你在信任它之前，先用几个测试案例跑一遍。
- Yusuf Karaaslan 的 [Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) 从另一个方向切入：它会把文档、GitHub 仓库和 PDF 自动转换成 Skill，并带有冲突检测。当你想要的知识已经以文档形式存在，只需要被打包成Skill时，这是最快的路径。

## Skill 和 MCP 的边界正在变模糊

并不是所有有用能力都已经被打包成 Skill，而且 Skill 和 MCP server 之间的边界正在变薄。下面两个工具，比再给一个定义更能说明这一点。

- Upstash 的 [context7](https://github.com/upstash/context7) 会把某个库最新、版本正确的文档和代码示例直接拉进模型上下文，让智能体不再根据训练中记得的 API 写代码。同一种能力，被打包成 MCP server、CLI 和 Skill 三种形式。你喜欢哪种安装方式，就用哪种。我会一直开着它。
- Playwright 则是这种分裂正在现场发生的例子。Microsoft 的 [playwright-mcp](https://github.com/microsoft/playwright-mcp) 是一种广泛使用的方式，可以给智能体真实浏览器控制能力，用于自动化和测试；它是一个 MCP server。Jordan Lackey 的 [playwright-skill](https://github.com/lackeyjb/playwright-skill) 则把同样能力重建为一个由模型调用的 Skill，让它自己编写并运行浏览器自动化。两个都可以试：如果你今天想要成熟选项，用 MCP；如果你想要 context7 所指向的“只在需要时加载”行为，用 Skill。

## 要点

市场会用成千上万的 Skill 诱惑你。这个数字是陷阱。少数几个你真正理解并信任的 Skill，会比一个你从不打开的目录更能改善你的工作；就像一份短而耐用的来源清单，胜过无穷无尽的信息流。

收藏这个合集，运行一个能改变智能体工作方式的框架，添加与你技术栈匹配的厂商 Skill，抓住那个适合你工作的 Skill，然后写出那个还不存在的 Skill。最后这一步，才是前面所有东西的意义。

订阅 Generative Programmer，可以获得面向 AI 编码智能体和智能体开发工具的实用地图、模式目录和生产经验。

这是一份动态文档。最后检查时间：2026-06-14。如果这里某个 Skill 已经迁移，或者你认为缺了什么关键内容，请告诉我，我会更新。