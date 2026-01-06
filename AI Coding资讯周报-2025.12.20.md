## 编程实践

### [别再只写 CLAUDE.md 了:用 Rules 重构 Claude Code 的记忆系统](https://mp.weixin.qq.com/s/13a2dtx3OeNvkZGipMyBYg)

本文介绍用 Rules 重构 Claude Code 记忆系统。Claude 官方新增 rules 机制，将记忆拆成可组合规则文件。Claude Code 记忆有五层结构，Project rules 可解决规则混杂等问题。文中给出搭建 rules 实操步骤，还对比了其与 CLAUDE.md 的分工，最后提出不同团队策略及实践建议。

### [AI架构师的诞生:AI+传统DDD模式 = 实现开发效率提升75%](https://mp.weixin.qq.com/s/JSsdqt0EKubPhzZsWyq7fw)

本文以淘宝闪购服务包系统为例，探索 AI+DDD 模式提升开发效率。原架构开发成本高、耦合严重等问题突出，通过 AI 拆解、人工修正及细化限界上下文，完成代码生成与实现。重构后架构解耦，代码量减 52%，重复代码消除，开发成本降低，AI 架构升级价值显著，将成软件工程新常态。

### [使用 Claude Code 构建端到端项目:全栈开发实践指南](https://mp.weixin.qq.com/s/ZFNo8pyPnqOLRTWIZKRQKA)

本文介绍了Claude Code在全栈开发中的应用。它是专为编码优化的AI，能融入工作流。其优势体现在搭建项目、开发前后端等多场景。核心能力包括代码生成、调试等。通过构建任务管理器项目展示其威力，还能与多种工具集成。使用时要注意局限，遵循最佳实践，与AI协同提升效率。

### [银弹还是毒药:OpenSpec实践](https://mp.weixin.qq.com/s/wFC7TJSxZjDTc4Y-E8AOFw)

本文围绕 OpenSpec 实践展开，介绍 SDD 规范驱动开发模式。先阐述 OpenSpec 使用，包括项目初始化及三阶段工作流。接着说明能力扩展，修改文档并新增要求。以“加工单上架需求”为例，展示 SDD 开发流程。实践心得强调知识库等重要性，指出小需求更适配，要闭环迭代知识库，也吐槽 AI 编程有细节问题，提效有限。

### [我用2小时，做了个让AI自动剪视频的工具。](https://mp.weixin.qq.com/s/Qnga_PEg68RQ0BP0jMO5lA)

银海分享两小时做的 AI 自动剪视频工具。先提出痛点，后介绍工具三步流程，选择智谱 GLM - 4.6V 模型及 Coding Plan 搭建。详述前后端实现，强调让视频公网可访问题及解决办法。分享调优过的提示词，称工具提效且输出质量高，鼓励借鉴。

### [从规范到代码:OpenSpec驱动的可迭代AI开发实践](https://mp.weixin.qq.com/s/vTWG8Gg--FGsRYB4QWaWYw)

OpenSpec是轻量级规范驱动开发方法论，解决AI编程失控问题。安装初始化简单，核心是“提案→实施→归档”闭环。与其他工具相比更适合持续演进，可与多种AI工具配合。通过实战示例展示其使用流程，还介绍常用技巧、团队采用指南等，能提升开发效率，让AI潜力更好发挥。

### [AI编码实践:从Vibe Coding到SDD](https://mp.weixin.qq.com/s/xVff9O2DPLssbfzp_GRwXQ)

本文介绍淘特导购团队AI编码实践，从代码智能补全到Agent Coding，再到Rules约束和SDD。各阶段有价值也有局限，如代码补全局限局部，Agent Coding缺乏规范。SDD理念先进但落地难。当前采用融合策略，用Rules约束、技术方案指导、Agent Coding迭代、AI汇总文档，持续探索更适配的AI辅助编程模式。

### [使用Qoder实战:13小时开发一个可商用的AI皮肤检测系统全过程](https://mp.weixin.qq.com/s/CMT4_MiocBzGQlXLnu3lcQ)

本文记录了13小时用Qoder和豆包视觉大模型开发“SkinAI”皮肤检测系统的过程。先介绍背景、核心工具，接着阐述架构设计、数据库模型，又说明前端UI、商业逻辑、后台管理搭建，最后完成部署交付。此项目展现了新技术结合带来的质变，为开发者和从业者提供了低成本启动SaaS业务的范例。

## 工具动态

### [还在为代码格式化烦恼?Claude Code Hooks一键解决](https://mp.weixin.qq.com/s/4XcilL2qxwCn1Nzf_N88pA)

本文由靈吾靈分享，介绍了Claude Code Hooks。它是特定时刻自动执行的命令，有8个Hook事件，分4个能“拦住”和4个不能“拦住”的。可在不同级别配置，以记录命令日志为例介绍新建配置步骤。还给出代码格式化、任务完成通知等场景示例，能实现代码审查等更多创意。

### [OpenSkills让所有AI 代码工具用上Anthropic同款技能库](https://mp.weixin.qq.com/s/Xif7AfcTzptiyUEciLxo_Q)

2025年12月18日消息，OpenSkills是能让所有AI代码助手用上Anthropic技能系统的CLI工具。它可从GitHub安装技能，实现跨助手共享、用版本控制管理。能解决Claude Code及其他助手用户痛点。Anthropic官方技能实用，还能自创。文中给出5个实战案例展示其提效能力。[https://github.com/numman-ali/openskills](https://github.com/numman-ali/openskills)

### [Youware 解决了目前 Vibe Coding 最棘手的问题!](https://mp.weixin.qq.com/s/VAf12RpFWgT3XZ2SpoHPDQ)

2025年12月17日消息，Youware解决了Vibe Coding最棘手问题。它打造专门服务于Vibe Coding的后端服务YouBase，除传统储存，还有登录服务、AI的API选择与储存服务、网站数据监测、自定义域名功能。测试构建CRM顺滑，有可视化界面管理内容。开普通会员可得AI编写的前后端，完爆类似产品，可尝试测试：213uegskvw.youware.app 。

### [一夜爆火🔥的1300+星的GitHub内容库，把 Vibe Coding 全套免费知识库](https://mp.weixin.qq.com/s/v9SnN-6HINoYPWhYjXQGyg)

2025年12月17日消息，GitHub上有个超火的1300+星的开源仓库vibe - coding - cn，它是中文vibe coding工作站，打包了“可复用的脑子”。其强调规划重要，不让AI随意规划以防代码库失控。给入门者建议：选Claude Code或Codex CLI开干；抄system_prompts；建memory - bank喂AI上下文再写代码。仓库链接：https://github.com/tukuaiai/vibe-coding-cn/tree/main 。

### [OpenSkills](https://github.com/numman-ali/openskills)

OpenSkills是匹配Claude Code技能系统的实现，可将Anthropic技能系统引入各类AI编码代理。通过CLI命令操作，能从GitHub、本地路径或私有仓库安装技能并同步到AGENTS.md。它与Claude Code在多方面兼容，仅调用方式不同。支持多安装模式，具备多种命令和标志，还能创建、发布和本地开发技能，要求Node.js 20.6+和Git。

### [深夜炸场!Manus 1.6 突然发布，史诗级进化暴力实测](https://mp.weixin.qq.com/s/8gsfjMHOiadZMrRUUo4ZRw)

2025年12月15日23:07，Manus 1.6 Max 突然发布。此次更新是从“辅助工具”到“独立承包商”的质变，它引入新旗舰 Agent，能处理复杂 Excel 模型、端到端开发移动 App，还有精准可控的修图功能。AI 进化超人类学习速度，对普通人既是危机也是机会。

### [OpenAI偷装Anthropic Skills实锤，ChatGPT、Codex已植入!开发者实测11分钟造PDF:比MCP强!](https://mp.weixin.qq.com/s/5AoeTWqK-jv1RyOkaprKLw)

近日开发者发现 OpenAI 悄悄支持 Claude 构建的 Agent Skills 机制，在 ChatGPT、Codex 中植入。其与 Anthropic 理念相似，能处理 PDF 等文档。Skills 是有组织文件集合，可解决传统工具缺陷。它与 MCP 互补，未来 Anthropic 还将在开发支持、版本控制等方面探索。

### [Claude Skills|将 Agent 变为领域专家](https://mp.weixin.qq.com/s/bwFGcomH6BfkBzhFMiiH1g)

2025年10月Anthropic推出Claude Skills，可在其多产品使用，有望成工业级Agent标配。它是基于文件系统、可复用知识包，向Agent注入内部知识。由元数据、指令、资源构成，按渐进式披露原则加载。Claude Skills与MCP协同，前者提供领域知识，后者提供工具，还有实现方案供其他Agent使用。

### [下一代全能终端，暴涨 15000+ GitHub Star!](https://mp.weixin.qq.com/s/86J8kZeaYhN_kt5gIcf6Xg)

Wave Terminal 是一款开源全能终端工具，已获 15000+ GitHub Star。它将浏览器、编辑器和 AI 集成，可自由拖拽功能块布局。内置 Monaco 编辑器，AI 助手有上下文感知能力，支持多模型。还解决文件预览、SSH 连接等痛点。支持全平台，安装简单，但内存占用较高，适合追求 All-in-One 工作流的开发者。[项目地址]:https://github.com/wavetermdev/waveterm

### [【万字长文】 最强 AI Coding:Claude Code 最佳实践](https://mp.weixin.qq.com/s/M3xA7zTBCv8HXVL9XjOBNA)

本文围绕Claude Code最佳实践展开。介绍作者基于CC的工作流，含提需求和Review等环节。详细阐述6个部分：初始环境配置、MCP与常用命令、核心工作流程、上下文管理、自动化与批处理、多Claude并发干活。还给出参考文档，助力开发者高效使用Claude Code辅助编程。

### [截图=代码?GLM-4.6V真能帮我写前端了](https://mp.weixin.qq.com/s/hToF2ZpIarQWu18f6OcFyA)

作者在做前端项目时希望有截图转代码工具，恰逢智谱发布GLM - 4.6V。测试发现它能像素级复刻前端、支持交互式修改；可根据截图实时全网搜索商品购买渠道；还能将长文档提炼总结、优化图文排版。智谱GLM Coding Plan性价比高，推荐使用。


## 行业观点

### [首发!建议你一定要看的《AI 生成代码在野安全风险研究》](https://mp.weixin.qq.com/s/sI_LKPnA-BeCVYr9Ko4sqg)

腾讯安全悟空代码安全团队联合高校开展《AI 生成代码在野安全风险研究》。研究发现，AI 生成代码呈阶段性演进，不同语言渗透不均，它在漏洞生命周期角色不固定，引入的漏洞有模式化特征。建议从建立评测基准、增强模型安全、人机协同治理构建防护体系，推动安全可控的 AI 编程。

### [AI 编程更需要一场思想革命](https://mp.weixin.qq.com/s/lxwf5s0s52v9lcwjjs1ibQ)

本文指出AI编程需思想革命。当前团队有人对AI Coding存怀疑抗拒态度，这是思维陷阱。AI革命核心是从“能不能用”到“怎么用好”，从“AI辅助”到“AI First”。通过实例说明要实践探索，还介绍AI First两层意义及闭环方案。强调思想转变、实践探索和持续学习，主动拥抱变化。

### [Vibe Coding 火了，Vibe PM 还会远吗?分享一套自创的“不写文档”的工作流](https://mp.weixin.qq.com/s/u_naXf0akmD8KoW4vfMfsQ)

2025年12月19日消息，随着Vibe Coding流行，“不写文档”的「Vibe PM」工作流值得关注。其核心是以视觉为高带宽输入语言：放弃从零码字，用截图或草图作“源代码”；将图片喂给AI并配提示词生成产品需求文档；再让AI将文档反向“翻译”成视觉成果。该工作流可避免低效“翻译”，让机器完成标准化交付。

### [别把 AI 写代码当赌博:从 Vibe Coding 到 Vibe Engineering](https://mp.weixin.qq.com/s/0gRj09n7uBmnSW5yIhY93Q)

本文编译整理了Kitze演讲内容。前端近年仍在基础问题上挣扎，LLM写代码能力强但人类爱抽象。vibe coding像赌场，管理者早就在做。vibe engineering强调怀疑，给出工程常识建议。社区分层明显，使用AI易踩坑。当下学计算机正当时，岗位底部会变薄，新岗位vibe code fixer出现。

### [裁掉初级程序员太蠢了!AI不会带来大规模失业!AWS CEO的三个理由引燃开发圈大讨论!网友绷不住了:到底谁为工程负责](https://mp.weixin.qq.com/s/14C7Hrp1A2COJ91YfPwE4g)

2025年，AWS CEO Matt Garman 反对用AI换掉初级开发者，给出三个理由：初级开发者更懂AI工具，使用更频繁；他们成本低，裁掉节省有限；不培养新人会使人才管道断裂。他认为AI不会致大规模失业，创造机会将多于取代的，此观点引发开发圈大讨论。

### [OpenAI Codex 负责人:为什么 AI 已经够强了，我们的效率却没有明显提升?丨Lenny’s Podcast](https://mp.weixin.qq.com/s/6fQ98k5IAY0aUM9xiC5rrA)

本期播客中，OpenAI Codex负责人Alexander分享观点。Codex增长源于协作方式校准，Sora项目体现AI改变交付资格。限制AGI生产力的是人类输入速度，AI应成主动队友。构建被AI接管后，判断成关键，写代码仍是AI行动底座，未来人类需提升判断能力。

### [仅4人28天!OpenAI首曝Sora内幕:85%代码竟由AI完成](https://mp.weixin.qq.com/s/8C2jHhAsxejKScR26gqrrA)

OpenAI揭秘安卓版Sora APP搭建内幕：4人团队28天完成，约85%代码由AI（Codex）完成。团队借助Codex应对高压发布任务，其能自我迭代。Codex有擅长与不足，团队立规矩、先规划，让其在框架内工作，多AI并行协作，提升开发效率与严谨性，望启发开发者。

### [AI编码工具变 “格式化神器”?Claude CLI半年频当“系统杀手”，多位开发者痛斥:心血都没了!](https://mp.weixin.qq.com/s/dkRxkQHvkdwZxxT4wQBfjQ)

近日，Reddit上一则对Claude CLI的控诉帖引发关注。一位开发者用其清理软件包时，它意外执行包含“~/”的shell命令，清空Mac系统，多位开发者也有类似遭遇。“删库”成AI工具通病，资深专家建议使用时“人在环路”，采取沙箱化配置、用容器环境等措施，强化安全意识。此外，12月19 - 20日AICon 2025将在北京举办。

### [深度|AI编码黑马Sourcegraph华裔联创:我们的理念不是以模型为核心，而是以Agent为核心](https://mp.weixin.qq.com/s/qkzKOCyLKuVLpSoNML2dMQ)

本文是对Sourcegraph联合创始人兼CTO Beyang Liu的访谈。他介绍公司从代码搜索到编码代理的发展，如推出Amp产品。强调理念以Agent为核心，开源模型关键在于后训练。还谈到行业权衡、评测问题，对未来开发环境做展望，指出美国开源生态受监管影响，需统一监管促发展。

### [等待AI写代码的时候，我该干点什么好?](https://mp.weixin.qq.com/s/AJ2dw_xZcPREfzzkKsdvkg)

本文分享了等待AI写代码时可做的事。如看可随时打断的电子书，和朋友聊天，写公众号等社交媒体内容，进行微运动，深度编程，做数字保洁，冥想，玩实体玩具，疯狂切屏，与AI聊天等，强调要利用好等待时间，避免成为被AI取代的人。

### [下一场革命:Vibe Engineering|OpenAI 内部分享](https://mp.weixin.qq.com/s/dnyG27ReM4UJF6M11n7uoQ)

2025年12月14日OpenAI内部分享“Vibe Engineering”，内部技术人员Codex采用率超92%，使用它的工程师合并PR产出多70%。Codex能12小时从零重写项目，7小时迭代200多轮产出约500行有效代码。OpenAI用其开发自身，非工程师也能用。它有“Best of N”功能，重要能力转向设计、判断等方面。


---

![](https://files.mdnice.com/user/121853/b1334415-e0c7-48bf-a869-5ca9584cc93c.png)

- AICoding 基地 devmaster.cn
- 专为开发者打造的一站式 AI 编程情报站。这里汇聚了最前沿的 AI 编程工具导航、编程模型动态及深度实战案例等，旨在帮助每一位开发者跨越技术周期，掌握 AI开发核心生产力，提升开发效率。