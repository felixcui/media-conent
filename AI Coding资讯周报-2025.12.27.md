## 编程实践

### [学习AI，助力开发--AI如何改变我的工作](https://mp.weixin.qq.com/s/N-dpx3z8zx9mFZ9D37CpPQ)

本文是京东物流郭忠强分享的学习AI助力开发的内容。他介绍多个开发案例，如后端功能、VUE前端开发等，指出AI辅助开发有70%左右完成度，但存在自动导入、国际化等问题。他总结使用心得，强调拆分需求投喂。此外，AI在报文分析、脚本生成等方面效果不错，未来AI将更懂人、易用。

### [GLM-4.7让我眼前一亮:居然能把Skill效率拉满](https://mp.weixin.qq.com/s/bKTuoEXDMcCzMiqUqb2rcQ)

本文介绍了使用 GLM - 4.7 运行 Skill 提升效率的方法。Skill 是完整技能包，执行快且稳。GLM - 4.7 针对 Agentic Coding 优化，代码能力强。文中给出安装 Claude Code、配置 GLM - 4.7 的方法，还介绍创建 Skill、用 Skill 做网站和写公众号的实践，其工具调用准、速度快，值得一试。

### [AI Coding 的核心:Context Engineering & Spec Driven Dev(BMAD 作为例子)](https://mp.weixin.qq.com/s/yfMziAdW9VhnW6zmnfXaqA)

本文围绕AI Coding核心——Context Engineering和Spec Driven Development展开。强调上下文工程重要性，如缺上下文会使棕地项目提效难。介绍使用AI的多种方式及SDD的RPI工作流。以BMAD框架为例，详述其使用步骤。核心要点为：上下文即一切，保持在Smart区，压缩真相与意图，关注高杠杆部分，选合适工具多练。

### [再见 Cursor!玩转 Antigravity 的 16 个实用小技巧，让 AI 真正帮你干活!!](https://mp.weixin.qq.com/s/bMdm89MXMl1pZl-FUyRlnQ)

本文介绍了 Google Antigravity 这一 AI 编程工具，它因可免费使用顶级大模型且功能强大，让 Cursor 相形见绌。作者分享 16 个实用技巧，如汉化、支持多语言开发、设置中文回复等。不过它也有弊端，如国内网络无法使用、需 Google 账户、稳定性欠佳。建议搭配其他工具使用，值得程序员尝试。

### [AI 辅助前端动画开发](https://mp.weixin.qq.com/s/ag2W9-rpQEyQB9RmDkywCQ)

本文围绕AI辅助前端动画开发展开，指出传统动画开发存在参数难获取、沟通成本高、反复返工等痛点。作者以AE为源头，构建MCP工具链+Cursor AI IDE工作流，介绍提示词设计和关键物料。通过多种尝试展示流程灵活性，还给出AI生成的动画技术方案、组件代码等，整体适配性与灵活性较好。

### [教你从零“手搓”一个大模型，别再只会调用API了](https://mp.weixin.qq.com/s/wcjYPzPq-lADvz-TeKZ7VQ)

文章介绍从零“手搓”小型大模型QDogBaby的过程。先提及动机与模型初尝试，接着阐述编码Tokenizer，重点介绍BPE算法。模型部分包含embedding、Attention等组件及实现。训练方面介绍推理、数据构造、预训练与SFT、采样策略。演示说明预训练与SFT后模型表现差异，还给出参考资料与数据集。

### [从CLI原理出发，如何做好AI Coding](https://mp.weixin.qq.com/s/QaE83XA6NQgyLXDP5n3n2w)

本文围绕CLI做好AI Coding展开。介绍了CLI产品美学，遵循Unix哲学，灵活轻量、可组合集成，不止用于代码编写。阐述其single agent技术原理及上下文工程方法。还给出用好CLI写代码的建议，如正确认识AI、学习Prompt工程、理解其局限等，强调人机协作提升代码质量。

### [适合很多公司和团队的 AI Coding 落地范式(一)](https://mp.weixin.qq.com/s/7w8cpyyKSB3d7-hnDJOHEQ)

本文是适合公司和团队的AI Coding落地范式系列第一篇。作者有3年多前端AI落地经验，介绍了AI Coding生态现状，将产品分为平台类和基建类。阐述了不同产品形态侧重点、优缺点，指出平台类门槛低但灵活性有限，基建类门槛高、灵活性高，还分析了面向人群，下一篇将探讨落地范式。

### [从代码生成到自主决策:打造一个Coding驱动的“自我编程”Agent](https://mp.weixin.qq.com/s/STqpbGPYUG1sCfx0dbfi7g)

本文介绍构建“自我编程”的Coding驱动型Agent，基于ReAct架构优化。采用FIM代码生成格式、Py4j实现双向调用，设计分层记忆与模块化Prompt。阐述其系统设计、工程结构、上下文工程、记忆系统、代码驱动等。开发需合理设计Prompt与架构，让其自我积累学习。目标成“1.5线”答疑助手，后续待多方面优化。



## 工具动态

### [别再只写 CLAUDE.md 了:用 Rules 重构 Claude Code 的记忆系统](https://mp.weixin.qq.com/s/13a2dtx3OeNvkZGipMyBYg)

本文介绍用 Rules 重构 Claude Code 记忆系统。Claude 官方新增 rules 机制，将记忆拆成可组合规则文件。Claude Code 记忆有五层结构，Project rules 可解决规则混杂等问题。文中给出搭建 rules 实操步骤，还对比了其与 CLAUDE.md 的分工，最后提出不同团队策略及实践建议。

### [别再纠结用 Skill 还是 Subagent 了，这一篇讲透 Claude Code 的「分身术」](https://mp.weixin.qq.com/s/z4pbtJ0sCEb7aU67BS3kGA)

本文聚焦Claude Code的Skill与Subagent选择。二者的“工作说明书”内容本质相同，但执行环境有别。前者在主上下文，后者在独立上下文。从体验和成本看差异明显，通过对比表和Plan模式例子说明。还给出两步选型法，且二者切换成本低，建议先行动再校正设计。

### [释放 Claude Code 的终极潜力:Awesome Claude Plugins 全攻略!](https://mp.weixin.qq.com/s/k5sLsPq_0wImR-miO702zg)

本文介绍 GitHub 项目 Awesome Claude Plugins，旨在聚合优质 Claude 资源。它有强大自动化机制，能自动抓取、集成多源信息并智能分类。涵盖 DevOps、代码质量等多领域插件，可解决开发痛点。其高度集约、检索快、易扩展，开源且欢迎贡献，传送门：https://github.com/Chat2AnyLLM/awesome-claude-plugins 。

### [Repo Wiki/Zread/DeepWiki/Code Wiki，谁才是屎山代码的终极救星?](https://mp.weixin.qq.com/s/Q25UI6Qd4QRAg-pVw7kzkQ)

作者分享代码文档生成工具使用体验。Qoder编辑器Repo Wiki功能强大但有文件数量限制且需付费；Code Wiki有来源、中文支持等问题；Zread免费、中文友好，但不能内网部署和导出文档；DeepWiki - Open可本地部署，用Skill Seekers配合Claude Code部署后文档质量差。综合比较，作者选Qoder付费使用。

### [Google 这对组合拳太狠了!3 句话让我的 Idea 变成真 App，全程不写代码，爽翻!](https://mp.weixin.qq.com/s/H7tCOFkDudBPkBM_jsg34w)

博主实测 Google 的 Stitch + AI Studio 组合，无需设计与编程功底，5 分钟不写代码就做出能跑通业务闭环的 App。先在 Stitch 输入需求生成 App“全家桶”界面；不满意可随时用指令修改；再将设计稿导入 AI Studio 一键完成开发。这组合拳降低开发门槛，体验丝滑还免费，让人人都能做 App。

### [Vercel AI SDK:构建现代 Web AI 应用指南](https://mp.weixin.qq.com/s/HlKUV-UE3F2WU5xCTBDfEw)

Vercel AI SDK旨在解决集成大语言模型到Web应用的复杂性，通过统一API、框架无关UI组件和多模型适配器封装调用和构建UI的难题。它有AI SDK Core和AI SDK UI两个核心模块，提供多个适用不同场景的库。通过示例展示快速上手流程，适合构建各类AI应用，是入门推荐。


### [ccmr已更新GLM-4.7和MiniMax-M2.1，国产模型也能有Claude Sonnet 4.5的体验](https://mp.weixin.qq.com/s/TciRwIdzmfEEY_H8BAFoGg)

鲁工介绍了自己开发的Claude - Code - Model - Router（简称ccmr）小工具，用于给Claude Code接入国产编码大模型，与官方订阅隔离。该工具已发布到GitHub和npm且有一定下载量。智谱和MiniMax更新旗舰模型GLM - 4.7和MiniMax - M2.1后，鲁工第一时间更新ccmr支持。还给出安装使用方式，欢迎大家尝试，可加微信交流。

### [不再一个人写代码:打造开发者专属的Claude Code子智能体团队](https://mp.weixin.qq.com/s/zcxJFGDK2Dn1Cb6lcOt7xw)

文章围绕Claude Code子智能体展开，介绍其特性与优势，提供快速入门指南。重点推荐10个实用子智能体，如代码审查员、调试专家等，涵盖开发各核心环节，展示实际效果。还说明了使用方法、进阶技巧，称其改变开发方式，提升效率与质量，可到GitHub查看完整列表。

### [实测丨全新的「扣子编程」，全新的 Vibe Infra](https://mp.weixin.qq.com/s/KK4B5EEFZiLZoPca0-oHaQ)

本文是对「扣子编程」的实测。其推出了「扣子编程」并拥抱 Vibe Coding，打造三大核心功能矩阵，提出 Vibe Infra 理念，提供从想法到上线的完整闭环。实测中，从想法到网站、定制版 flomo 应用都快速完成且可一键部署。它降低了软件开发门槛，覆盖多数生产力场景，目前在内测免费公测，值得一试。

### [Claude技能天花板来了!Anthropic 官方开源 16 个生产级技能库](https://mp.weixin.qq.com/s/hfXLyzx9wUiDmiAYQnzUkA)

2025年12月23日消息，Anthropic官方开源16个生产级技能库，展示从创意到企业级完整谱系，证明Skills系统可处理高度专业化重复任务。技能分为文档处理、创意与设计、开发与技术、企业与沟通等类别，还有元技能“技能生成器”，降低自定义门槛，扩展性强。项目链接：https://github.com/anthropics/skills/tree/main 。

### [终极指南:Claude Plugins 与 Skill 仓库汇总，助你打造最强 AI 助手!](https://mp.weixin.qq.com/s/dBbCnzVk-uMa0Il81v4c6g)

本文围绕Claude Plugins与Skill仓库展开，旨在助用户打造更强AI助手。汇总了compounding - engineering等多个热门实用的插件市场和技能库，介绍了其描述与仓库地址。还给出使用 <代码开始>code - assistant - manager (CAM)<代码结束>安装插件的指南，分特定助手和所有助手两种情况。鼓励大家访问CAM仓库，贡献插件或技能，会定期更新列表。

### [插件市场终于来了!Claude Code插件生态已成熟，直接拿来就用](https://mp.weixin.qq.com/s/bqiDgvimPIBMm8n771lLWw)

2025年12月17日Claude Code重大更新，官方插件市场上线。插件系统可将自定义命令等打包成可复用插件，安装简单、按需启用。社区已有多个优质插件市场，如官方及第三方平台等。Claude Code迈入“高度可定制化”阶段，插件能提升效率、实现标准化，作者还将继续探索其实用性。

### [被字节扣子的新功能戳到了。](https://mp.weixin.qq.com/s/I5lmW2mCDKF-LzsLa7q9pw)

2025 年被称为 Agent 元年，字节的扣子是国内 Agent 开发平台中最出圈的产品。扣子开发平台升级为扣子编程，转向 Vibe Coding 范式。它让用户用自然语言提需求，系统自动完成后续。上手体验显示，其操作简单、有版本管理，还能部署。这降低了构建负担，回归编程本质乐趣。

### [别再问“怎么写 SKILL.md”了，直接抄生产级的Skills 库](https://mp.weixin.qq.com/s/qy6ITfTx_dI6zl_37D55zA)

本文分享十几个优质 Skills 资源库。Skills 热度高，有望获大模型“内置支持”。推荐了 Skills 聚合网站，介绍开源仓库，包括官方的 anthropics/skills、ChatGPT/Skills，以及民间 500+star 仓库。还给出不同人群选择建议，最后称写 Skill 可先借助官方工具，初稿需调试优化，使用他人 Skill 也需验证调整。

### [史上最强 Claude Skills 全指南:从开发神器到知识大脑，这 30+ 插件建议收藏!](https://mp.weixin.qq.com/s/ZUoUklWoid8U3bLcZfz3og)

本文是 2025 年 12 月 20 日发布的 Claude Skills 全指南。Claude 官方技能之外，社区自建强大生态。文章介绍核心必装、开发者工作流、研究与知识管理等多类技能，给出资源汇总仓库。还提供避坑与上手建议，如不同用户选装推荐、安装资源中心及常见问题解决办法，邀读者分享使用开发经验。


### [一文看懂 Factory:面向规模化的软件开发智能体军团](https://mp.weixin.qq.com/s/lPnOboA9bWK9UXYnr6KHQQ)

本文介绍了面向规模化的软件开发智能体军团Factory，它以Droid智能体协作重构软件开发组织方式。其有五大核心Droid各司其职，采用两阶段工作流和多层上下文管理。支持多种使用方式、会话管理与团队协作，具备定制化扩展能力。能提升效率、保障质量、控制成本，推动开发模式变革。

## 编程模型

### [详解 & 实测 GLM-4.7 ，14个Skills、前端设计能力](https://mp.weixin.qq.com/s/kXynLrCDI75xu3r0xypb5g)

本文全方位解析 GLM - 4.7，其性能提升显著，在数学推理等方面竞争力强。训练揭秘涉及挑战、算力、工具链等。有 14 个核心 Skill，与 Claude 有异同，对开发者友好。UI 实测有亮点也有不足，与 Claude Opus 4.5 对比各有优劣，编码体验整体不错，期待智谱下一代多模态大模型。

### [MiniMax M2.1:更好的「多语言编程」](https://mp.weixin.qq.com/s/4X0OhuefhSOLNWokr-mtcQ)

2025年12月23日，MiniMax发布M2.1并即将开源。其核心升级是多语言编程能力，在软件工程核心榜单等表现提升明显。作者用M2.1在Claude Code完成傅立叶变换可视化教学视频任务，串联多个工具。M2.1在真实复杂任务表现佳，获多家头部AI平台好评。



### [开源编程新王诞生，对标Claude Sonnet 4.5?](https://mp.weixin.qq.com/s/YhMZBUzr-eMr7584ax6S9g)

2025 年 12 月 23 日消息，国产模型 GLM - 4.7 悄然发布。它可丝滑兼容 Claude Code 工具，在复杂任务生成、后端架构设计、前端审美重构三个场景实测表现出色。其背后有 Coding Plan 支撑，编程体感逼近 Sonnet 4.5，是“Claude 最佳平替”。智谱开启体验进化季，购套餐用户可邀好友免费体验。

### [我把Claude Code换成GLM-4.7用了6小时，我竟然没发现明显区别](https://mp.weixin.qq.com/s/TJZEE9POt15CPQrcgj0kew)

博主刘小排分享GLM - 4.7使用体验。它编程能力进步大，省钱可平替Claude Code，中等难度任务近乎无区别，高难度任务易健忘。在LMARENA盲测榜排第六，前端能力强，完成“金门大桥测试”。可通过MCP补齐多模态和联网搜索能力，包月套餐性价比高，值得一试。

### [MiniMax M2.1:多语言编程SOTA，为真实世界复杂任务而生](https://mp.weixin.qq.com/s/QOv0GLq5-T--gKGIF912RQ)

2025年12月23日，MiniMax开放模型更新MiniMax M2.1。它致力于提升真实世界复杂任务表现，有卓越多编程语言能力等亮点，基准测试表现显著提升。内测获多方好评，还展示多领域应用案例。其API已上线，通用Agent产品开放使用，将全面开源，提供不同版本API，Coding Plan用户推理更快。

### [智谱开源GLM - 4.7](https://mp.weixin.qq.com/s/YlAwHPl2pUbF_2Z3qdnXGg)

2025年12月23日智谱开源GLM - 4.7，官方数据亮眼，多个榜单成绩优异，LMArena用户评测也超GPT - 5.2和Claude Sonnet 4.5。作者实测五大案例，在制作PPT、海报、网页、原型设计及自动化写作中表现出色，Coding、Agentic和审美能力强。后端稳定，是开源新标杆，还给出使用建议及活动信息。

### [别人在测 Demo，我已经用MiniMax M2.1跑通了整个产品开发流程](https://mp.weixin.qq.com/s/8g5KgDTb9NUaW0zUNL_emQ)

2025年12月23日，AI产品黄叔用自研产品“降噪”实测MiniMax M2.1。从Skills优化、页面组件实现、交互动效、智能搜索四维度测试，结果惊喜超预期。M2.1优势明显，如Skills支持领先、前端审美在线等，但也有不足。它为开发者提供国产替代，90%日常开发够用，值得一试。


### [MiniMax M2.1 首发评测:专治祖传屎山，这种爽感谁用谁懂](https://mp.weixin.qq.com/s/rB6vxjvQ1KYXdCp6IcUqog)

本文是 MiniMax M2.1 首发评测。它瞄准 AI 维护旧代码难的痛点，在 LegacyShop 项目测评中表现出色，优化性能、重构代码、建设工程基建都有亮眼成果，还能从零构建太阳系模拟系统。不过，它在复杂任务规划上存在不足。M2.1 有能力接管存量治理，值得开发者一试。

### [智谱GLM-4.7:更强的代码，更好的美学](https://mp.weixin.qq.com/s/5qunqkvHsffvrdxcfaWmLg)

2025年12月消息，智谱GLM - 4.7开源，编程能力再度加强。它针对多款代码工具专项优化，支持“先思考、再行动”。其最大提升在审美，生成内容版式更优。编码数据表现出色，多个测试排名领先。具备交错、保留、轮级三种思考模式。使用途径有API（BigModel.cn）和在线体验（z.ai），开源于GitHub和Huggingface。

### [实测字节豆包1.8，我用Trae和MCP搓出了实时装修Agent](https://mp.weixin.qq.com/s/r6-IKYyMf53Hz6wLdkjYSQ)

作者在视频创作清晰度优化到极致后，想用 Agent 规划创作空间。借加强版豆包 1.8 能力，花两周在 Trae+MCP 实现实时装修 Agent。该 Agent 可读取视频图片、生成效果图、更新进度、搜索对比等。流程跑通后，作者将琐事交给它，专注创意与决策，还想到用它解决买按摩椅的空间规划难题并激情下单。

## 行业观点

### [Agent 元年复盘：从 Claude Code 到 Deep Agent，Agent 的架构之争已经结束](https://waytoagi.feishu.cn/wiki/MojDwfYrMi6K1nklAcZcuVU5nZb)

作者周星星在“Agent 元年”2025年结束之际进行复盘。技术上，Agent 架构之争收敛至以 Claude Code 和 Deep Agent 为代表的「通用型 Agent」形态。Claude Code 3月推出时虽为编程助手但应用广泛，社区开发者用其做知识库整理等，“薅羊毛”玩家称有 SOP 它就能执行任务，9月官方更名其 SDK，转向 Agent 开发。

### [没学过编程也能做游戏?亲测YouTube新功能，这简直是魔法!](https://mp.weixin.qq.com/s/iao9afNNlB-qBjgjvOnZ-g)

2025年YouTube基于Gemini 3发布Playables Builder，标志着从「语法编程」到「直觉编程」范式转移。Vibe Coding加速落地，其终极形态是“Vibe即源码”。创造者方法论重构，转向「意图思维」，以多模态为新API，形成零延迟反馈闭环。技术壁垒消除后进入审美竞争，实现想法成本降低，创造者黄金时代开启，可体验👉https://www.youtube.com/playablesbuilder 。

### [为什么要拥抱Claude Code，抛弃N8N](https://mp.weixin.qq.com/s/TFkP1Mwnm19Xe_FRGLbs2Q)

文章对比N8N与Claude Code，指出N8N低代码优势不再。对程序员，它是换语法；对非程序员，门槛换形式。其剩余优势如可审计性、确定性执行是防守性的。而Claude Code是积累型学习，可培养数字助手，回报有复利效应，边用边学，交互双向，成本可控，值得拥抱。

### [Coding Agent:为什么有的像“神队友”，有的却只能写 Demo?](https://mp.weixin.qq.com/s/3XALOKtw6TyeoS74Jt-78w)

本文从工程视角探讨 Coding Agent 成为“严肃工程工具”的差距。它大致分 IDE 内、自主、企业级三类，干活包含任务拆解等多层。技术分水岭在看懂代码库等 5 处，问题关键在上下文。未来 1 - 2 年，分水岭在工程上下文等方面，能否成工具取决于是否“活在工程系统里”。

### [独家 | AutoCoder.cc 获博华、力合连续融资，AI 初创自研基模仍有机会](https://mp.weixin.qq.com/s/77SWtEKk7cgfk_jqI7uYBQ)

AI Coding 创业公司 AIGCode 获博华、力合等融资。其创立于 2024 年 1 月，首款产品 AutoCoder.cc 表现良好。该公司坚持自训练基础模型，在模型层面有三项创新，提出生成式软件架构。当下 AI Coding 竞争激烈，创业公司仍有突围机会。

### [无限代码危机!奈飞AI工程师曝自家上下文工程秘诀:三阶段方法论!AI不能理解软件为什么会失败!每一代工程师都会撞上一堵墙!](https://mp.weixin.qq.com/s/NypEPA5TgUQl_xkTMz2Wzw)

Netflix工程师Jake指出，AI虽让代码生成加速，但也带来“无限软件危机”，因它放大“容易”诱惑，使复杂度失控。他分享“上下文压缩”三阶段方法论：研究梳理系统、规划设计方案、实现完成编码。强调人要保留对系统的理解和思考能力，避免认知鸿沟。

### [“Cursor的bug太多了，他们直接买下一家代码评审公司来修!”](https://mp.weixin.qq.com/s/o0tLCSUeCOEbdb5YKBcu4A)

2025年12月19日，Cursor宣布收购代码评审初创公司Graphite。AI加速代码编写，代码评审成瓶颈，交易旨在组合“创建、评审、合并代码”工具。Graphite继承Meta工程方法论，采用stacked diffs模式。收购或助Cursor打磨产品、拉顺流程。

### [Martin Fowler 谈 AI 如何改变软件工程](https://mp.weixin.qq.com/s/56r5BksoOgGW6Q5-6BE6pw)

本文整理自 Martin Fowler 访谈，他认为 AI 让软件开发从确定性转向非确定性，是重大技术变革。开发者要从逻辑可预测转向“容错”思维，警惕氛围编程风险。软件工程实践需调整，如拆分任务、严格审查代码。AI 可助力遗留系统理解，但工程师要保持核心技能。

### [你的团队还需要产品经理吗?](https://mp.weixin.qq.com/s/GWHwzcpAvTZq31jUge7atA)

本文从产品经理与工程师协作关系变化探讨AI时代团队是否还需产品经理。传统分工模式有沟通成本高、迭代周期长等问题，AI让协作模式转变。产品经理未来或独立落地想法，或被工程师替代。判断团队是否需要，关键看需求决策、沟通成本等。产品工作必要，但岗位非必需，应提升核心能力拥抱变化。

### [AI取代不了程序员，明年全流程上AI!谷歌工程负责人自曝:2026年AI编程完整工作流!经典软件工程纪律没过时，在AI时代更重要](https://mp.weixin.qq.com/s/fK9C3r_CfDeearnTZ-XskQ)

谷歌工程负责人Addy Osmani分享2026年AI编程完整工作流：先规划方案，拆分任务小步迭代，提供充足上下文，选合适模型；开发各阶段用AI但人要监督验证、测试审查；频繁提交，用规则定制AI行为，强化自动化；用好AI加速成长，经典软件工程纪律更重要。

### [aiXcoder:超越Vibe Coding，构建以人为主的可靠开发流程](https://mp.weixin.qq.com/s/Lxlq0CTgETFUCHJFyeKXKg)

2025年12月13日，硅心科技（aiXcoder）黄宁在大会演讲指出，Vibe Coding难适配企业级项目。aiXcoder将AI与软件工程融合，通过拆解任务、构建可验证系统、提取隐知识形成开发范式。该范式已获实践验证，未来行业将向定义开发模式进化，aiXcoder正横纵发力提效企业级AI开发。

### [Andrej Karpathy 年度总结:Nano Banana最为震撼， 指向下一代 AI GUI 的雏形](https://mp.weixin.qq.com/s/DqlL-DpWu3QDOc9YNYOgAg)

2025年是大型语言模型领域蓬勃发展之年，有诸多范式转变。基于可验证奖励的强化学习成新成员，提升了模型推理能力；LLM智能呈“锯齿状”，基准测试受质疑。Cursor揭示新应用层，Claude Code带来新交互范式，Vibe coding让编程更普及，Nano Banana现LLM GUI雏形，行业潜力巨大。

### [首发!建议你一定要看的《AI 生成代码在野安全风险研究》](https://mp.weixin.qq.com/s/sI_LKPnA-BeCVYr9Ko4sqg)

腾讯安全悟空代码安全团队联合高校开展《AI 生成代码在野安全风险研究》。研究发现，AI 生成代码呈阶段性演进，不同语言渗透不均，它在漏洞生命周期角色不固定，引入的漏洞有模式化特征。建议从建立评测基准、增强模型安全、人机协同治理构建防护体系，推动安全可控的 AI 编程。

### [AI 编程更需要一场思想革命](https://mp.weixin.qq.com/s/lxwf5s0s52v9lcwjjs1ibQ)

本文指出AI编程需思想革命。当前团队有人对AI Coding存怀疑抗拒态度，这是思维陷阱。AI革命核心是从“能不能用”到“怎么用好”，从“AI辅助”到“AI First”。通过实例说明要实践探索，还介绍AI First两层意义及闭环方案。强调思想转变、实践探索和持续学习，主动拥抱变化。

---

![](https://files.mdnice.com/user/121853/fbbb3fb0-d8a3-4d8d-a5b9-ceac585e3e41.png)


- AICoding 基地: devmaster.cn
- 专为开发者打造的一站式 AI 编程情报站。这里汇聚了最前沿的 AI 编程工具导航、编程模型动态及深度实战案例等，旨在帮助每一位开发者跨越技术周期，掌握 AI开发核心生产力，提升开发效率。
