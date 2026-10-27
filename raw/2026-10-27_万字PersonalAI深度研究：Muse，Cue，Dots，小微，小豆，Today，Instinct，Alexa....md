# 万字Personal AI深度研究：Muse，Cue，Dots，小微，小豆，Today，Instinct，Alexa...

**作者**: 言之

**来源**: https://mp.weixin.qq.com/s/xQA7y1YPus6gNVhkGAgTRQ

---

## 摘要

2026年下半年，Personal AI成为AI应用焦点，其核心变化在于AI产品的基本单位从“一次对话或任务”转向“一个长期被理解和服务的用户”，具备持续记忆、主动性、跨应用执行能力和长期运行环境。Meta Muse的爆发标志着AI私人助理开始从极客工具走向大众产品。Personal AI有望成为AI时代的“个人意图操作系统”，管理用户的时间、注意力、关系、任务、权限和金钱，并改变搜索、电商和生产力软件的入口结构。

---

## 正文

言之 言之

在小说阅读器读本章

去阅读

近期Personal AI接棒上半年的龙虾、年中的办公AI，成为下半年AI应用的焦点。

本文围绕目前市场上已有的热门 Personal AI 产品展开研究，覆盖：字节跳动小豆 / Spell、腾讯小微、LightVela、Handy Bot、Today、Manus Cue、Meta Muse、OpenAI Dots、Amazon Alexa+、Instinct。

## 核心结论

先给一个我认为最重要的判断：

2026 年这波 Personal AI，真正发生变化的地方，是 AI 产品的基本单位开始从“一次对话 / 一个任务”，转向“一个长期被理解和服务的用户”。

ChatGPT 时代的典型交互关系是：

用户提出问题 → AI 给出答案

第一代 Agent，包括 OpenClaw、Hermes、Manus 早期形态，进一步变成：

用户提出任务 → Agent 使用工具 → 完成任务

Personal AI 正在建立第三种关系：

AI 长期理解一个人 → 持续观察其目标和环境 → 主动发现需要处理的事情 → 获得授权后替用户执行 → 从反馈中进一步理解这个人

因此，我会把真正的 Personal AI 定义为：

以“用户本人”为长期状态中心，拥有持续记忆、主动性、跨应用执行能力和长期运行环境，并能够在权限边界内代表用户采取行动的 AI。

Today 自己对这一品类的定义非常接近这个框架：durable memory、proactivity、execution；Bill Gates 早在 2023 年对未来 Agent 的描述也包含相同三个核心：理解用户、主动介入、跨应用完成任务，并预言 Agent 最终会成为新的计算平台。

2026 年 9 月密集出现的产品则把这个概念从预测推向了真正的消费级产品竞争：Meta 9 月 8 日发布 Muse；Today 在 9 月发布；Manus 推出 Cue；OpenAI 9 月 29 日推出 Dots；同期字节和腾讯的 Personal Agent 项目陆续曝光。

我认为这一波有六个值得高度关注的结论：

| 变化 | Chatbot / 第一代 Agent | Personal AI |
| --- | --- | --- |
| 核心对象 | 一次问题、一个任务 | 一个人 |
| Context | 当前会话、项目资料 | 长期个人上下文 |
| Memory | “记得聊天内容” | 维护动态 user model |
| Trigger | Prompt 驱动 | Prompt + Event + Goal 驱动 |
| Execution | 执行指定任务 | 持续管理目标与承诺 |
| 时间尺度 | 分钟到小时 | 天、月、年 |
| 产品价值 | “帮我做这个” | “替我操心这件事” |
| 最终控制点 | Chat UI | 意图、授权、行动和交易入口 |

第二个核心判断是：

Muse 的爆发说明消费者第一次开始看到“AI 私人助理”有机会从极客工具变成大众产品。

Sensor Tower 估算 Muse 9 月 8 日上线后的前两周获得约 280 万下载，截至 9 月 24 日左右约 340 万下载；9 月 18 日升至美国 App Store 免费榜第一，次日登上 Google Play 榜首。上线前十天，其日下载量平均增速约 55%，而 ChatGPT 手机 App 上线前十天约为 24%。Meta 的内部导流确实非常强，但 Sensor Tower 估计截至 9 月 19 日，付费广告曝光仅占相关广告曝光约 6%，因此增长不能完全归因于买量。

第三个判断，也是我认为对产品战略最重要的一点：

Personal AI 很可能成为 AI 时代的“个人意图操作系统（Personal Intent OS）”。

这里的“OS”是一种产品与产业结构上的比喻。它并不运行在传统操作系统的内核层，而运行在 用户意图与数字服务之间的控制层：

你是谁 → 你在乎什么 → 你想完成什么 → 谁来完成 → 调用哪个 App / 服务 → 可以花多少钱 → 什么动作需要你确认。

传统操作系统管理 CPU、内存、文件和进程。

Personal AI 未来管理的资源可能是：

你的时间、注意力、关系、任务、信息、权限、账号和钱。

Bill Gates 2023 年已经明确提出“Agents will be the next platform”，并认为未来用户不必先判断该打开哪个 App，而是直接告诉 Agent 自己想完成什么；Agent 会改变搜索、电商和生产力软件的入口结构。2026 年正在发生的事情，越来越接近这个判断。

## Personal AI 的边界：从“小龙虾”到长期关系型 Agent

### “小龙虾”和 Personal AI 其实来自同一棵技术树

OpenClaw、Hermes 这批 2026 年初爆火的 Agent，在技术范式上已经非常接近 Personal AI。

OpenClaw 的定位就是运行在用户自己的电脑或服务器上的开源 AI assistant，可以接入 WhatsApp、Telegram、Slack、Discord、iMessage 等渠道，并通过一个 Gateway 长期运行；Hermes Agent 则强调 self-improving、自主创建和优化 Skills、跨会话记忆，并可以部署在自己的服务器或 VPS 上。Hermes 由 Nous Research 开源，2026 年发布。

所以从能力来看，“小龙虾”已经包含很多 Personal AI 原语：

Persistent runtime + Memory + Tools + Skills + Messaging + Computer Use。

真正发生变化的是产品化方式和目标用户。

可以把两代产品理解成下面这条连续谱：

| 维度 | OpenClaw / Hermes 型 Agent | 2026 Personal AI |
| --- | --- | --- |
| 目标用户 | 极客、开发者、AI 重度用户 | 大众消费者 |
| 部署 | 本地、自托管、VPS | 云端托管、开箱即用 |
| 配置 | 模型、API Key、Skills、渠道 | 登录授权即可 |
| 产品中心 | Agent 本身 | 用户本人 |
| 记忆 | Agent memory | Personal memory / user model |
| 主动性 | Cron / workflow / 用户配置 | 根据生活事件和目标主动介入 |
| 身份 | 工具账号 | Agent 可拥有邮件、电话、钱包、Computer |
| 执行 | Browser、Shell、API | 消费、预订、沟通、支付、生活服务 |
| UX | 技术工具 | 人格化、聊天化、消费级 |
| 信任机制 | 用户自行承担 | 权限、确认、审计、沙箱、支付限额 |
| 核心价值 | “给我一个万能 Agent” | “给我一个真正懂我的私人助理” |

LightVela 恰好位于两者中间。腾讯官方将其定义为“云端 Agent 托管产品”，当前提供 Hermes Agent：用户无需自行部署服务器，Agent 可以长期运行在腾讯云上，同时保留模型、Skills、渠道等配置能力。它更像云端托管的小龙虾，也是从 hacker agent 向 mass-market Personal Agent 过渡的一种形态。

### Personal AI 最重要的变化，是状态中心从 Task 转成 Person

一个普通 Agent 的数据结构可以简单理解为：

Task → Context → Plan → Tools → Result

Personal AI 多了一层长期存在的东西：

Person → Goals / Preferences / Relationships / Commitments / History → Events → Tasks → Actions

比如：

“帮我订周五晚上餐厅”

对于通用 Agent，这是一次 transaction。

真正的 Personal AI 理想情况下已经知道：

你周五几点下班；

你伴侣是谁；

这是你们的纪念日；

她不吃海鲜；

你最近说想控制预算；

上次你们喜欢哪家餐厅；

周五晚上已有一个冲突；

需要提前预约停车。

于是产品从 instruction following 进入 intent understanding。

Today 明确把这种产品能力称为 “living memory”：记住人、项目、偏好和长期承诺；同时监测 calendar、mail、notes 等变化，在适当时主动提醒，并在用户确认后执行。

ChatGPT 的 Memory 在 2025 年已经开始从显式保存记忆扩展到参考历史聊天，这说明“用户级连续上下文”早已成为主流 AI 产品的重要基础设施。Personal AI 又进一步把 Memory 和执行系统绑定起来。

### Personal AI 的真正“Personal”至少包含四层

我建议产品研究里不要把“Personal”简单等同于“有 Memory”。

第一层是 Preference Memory。

知道你喜欢什么、不喜欢什么。

第二层是 Relationship & Commitment Memory。

知道你和谁是什么关系，以及你曾经对谁承诺过什么。

第三层是 Behavioral Model。

逐渐知道“你通常怎么做决定”。

比如价格与品质之间如何权衡，什么时候愿意被打扰，哪些事情必须确认。

第四层是 Goal Model。

知道你持续几个月甚至几年的目标：

减脂、学语言、旅行计划、职业发展、资产计划、家庭事项、Side Project。

第四层才真正打开 Personal AI 与普通 Assistant 的巨大差距。

因为这里出现了一个过去软件产品很少拥有的能力：

软件开始维护关于“这个人正在走向哪里”的模型。

Today 把 fitness、learning、savings、relationships、projects 等“long arcs”明确列入 Personal Agent 场景；Muse 同样强调长期目标，用户给出目标后，它可以制定个性化计划并持续推进。

因此，我更倾向于用下面这个公式定义 Personal AI：

Personal AI = Personal Context × Persistent Memory × Proactivity × Execution × Trust

其中任何一项接近零，整体价值都会明显下降。

有 Memory 但没有执行，它是一个“懂你的 Chatbot”。

有执行但没有 Memory，它是一个“通用 Agent”。

有 Memory + Execution 但缺乏 Proactivity，它更像一个高级私人助理工具。

五个能力同时成立，才开始接近真正的 Personal AI。

## 为什么 Personal AI 在 2026 下半年突然爆发

“2026 上半场龙虾、中场办公 AI、下半场 Personal AI”这句话作为产业观察非常准确。但我会补充一点：

这是产品形态的三次迁移，底层技术是连续成熟的。

大致可以理解成：

上半场：证明 Agent 能干活

年中：证明 Agent 能承担专业工作

下半场：把 Agent 从工作环境带入一个人的完整生活

### 用户侧：人真正缺少的是“替我操心”，并非更多答案

过去三年的 AI 产品大部分围绕“知识劳动”：

写、问、搜、总结、Coding、画图。

消费者大量真实生活时间，却消耗在另一类事情上：

订餐厅、改航班、退货、订医生、找维修、比价、取消订阅、缴费、安排行程、协调家人、回邮件、调整日历、处理保险、跟客服沟通……

这些任务具有几个共同特征：

低认知价值、高流程摩擦、高碎片化。

它们经常散落在十几个 App、网页、电话和聊天记录里。

因此 Personal AI 的核心 JTBD，可以概括成一句话：

“把我脑子里持续悬着的事情拿走。”

Instinct 的典型任务就是旅行、买菜、票务、订阅管理以及替用户打电话；Muse 展示的是发邮件、订旅行、购物、管理持续目标；Alexa+ 已经覆盖家庭、购物、日程、智能家居和预订服务；Today 聚焦工作、生活、健康信号与长期目标。

这和传统 Copilot 的价值感很不一样。

Copilot 通常在告诉你：

“这里有一个更快完成工作的方式。”

Personal AI 提供的心理价值更接近：

“这件事情你可以不用再想了。”

我认为后者拥有非常大的消费级市场潜力。

它本质上是在民主化过去属于高收入群体的服务：personal assistant / chief of staff / concierge。Bill Gates 也把 Agent 描述为一种让更多普通人获得过去价格昂贵的个性化服务的技术。

### Muse 为什么能爆

Muse 的成功很值得产品经理仔细拆。

它没有依赖某一个全新的单点 AI 能力，而是把近几年成熟的能力组合成了一个消费者能理解的产品承诺：

“Tell me what needs to get done.”

Meta 的官方定义中，Muse 可以持续执行工作，在用户关闭 App 后继续运行；每个用户拥有独立的 Muse Secure VM 和 Browser；它可以发送邮件、订旅行、填表、购物、处理长期目标，并通过 WhatsApp 直接交流。

这形成了几个重要的体验变化。

第一，“给答案”升级成“交付结果”。

用户不需要先问“纽约有什么好酒店”，然后自己打开 Booking。

他可以直接说：

帮我计划一个符合这些要求的纽约周末。

第二，云电脑解决了“持续工作”。

Chat 会话结束后，事情仍然在推进。

这对于 Personal Agent 很关键，因为生活任务天然大量异步：等邮件、等价格变化、等预约、等某个时间点。

第三，Personal Context 开始真正参与执行。

Muse 官方举的例子包括结合 Instagram 保存的食谱和饮食限制来处理个人需求，这说明 Meta 正尝试把过去用于 recommendation 的 personal signals 迁移到 agentic action。

第四，用户不需要学习 Agent。

Meta 刻意强调 Muse 面向 billions of people、out of the box 使用。这个差异非常关键——OpenClaw/Hermes 的能力可以很强，但“安装、配置、选择模型、管理 Skill、API Key”本身就筛掉了绝大多数消费者。

第五，免费极大降低了尝试成本。

这也意味着巨大的基础设施成本。Barclays 分析师 Ross Sandler 估算，提供免费 Personal AI Agent 的运行成本可能达到当前免费 ChatGPT 服务的约十倍；这只是分析师估算，却很好地解释了为什么 Meta、Google、Amazon、OpenAI 这类拥有大规模算力、现金流和商业化网络的公司在这一阶段具有明显优势。

### 投资人看到的是“Agentic transaction”

Instinct 是这个方向最典型的资本市场案例。

2026 年 9 月 28 日，Reuters 报道 Instinct 获得 10 亿美元融资、估值达到 100 亿美元，投资者包括 Sequoia、Benchmark、Coatue。公司创立于 2025 年，由前 Sierra 员工 Noah Shinn 创办，产品可以通过文字或语音处理旅行规划、买菜、票务、订阅，并开始提供替用户给商家打电话的 concierge 能力。

为什么这样一个非常早期的公司能获得如此激进的估值？

我认为 VC 押注的远远不只是“AI 助手订阅收入”。

它们看到了这样一条价值链：

Intent → Recommendation → Decision → Transaction

过去互联网巨头分别占据其中一段：

Google 控 Search。

Meta 控 Discovery / Attention。

Amazon 控 Commerce。

Apple / Google 控 OS 与 App distribution。

支付平台控制 Transaction。

Personal Agent 有机会坐到整个链路最上游。

当用户说：

“给我买一个适合下个月去北海道的行李箱。”

谁先收到这句话，谁就拥有一个极高商业价值的东西：

购买意图。

而当 Agent还能替用户完成购买，它拥有的进一步升级为：

transaction routing power。

2026 年支付基础设施已经明显朝这个方向演进。Stripe 的 Shared Payment Tokens 允许 Agent 在用户授权下发起支付，同时避免暴露底层支付凭据；Stripe 的 Agentic Commerce 产品则让商家能够直接面向 AI Agent 提供商品、Checkout 和支付能力。

这解释了为什么 Personal AI 对资本市场的想象空间远大于普通 Chatbot。

### 技术侧：六块拼图终于同时成熟

这轮浪潮的另一个关键原因是：过去缺一不可的几个技术模块，在 2026 年第一次同时接近可产品化水平。

#### Computer Use 从 Demo 进入可用区间

2024 年的 Computer Use 仍然非常实验性。

到 2026 年，OpenAI GPT-5.4 已把 computer use 作为 general-purpose 模型原生能力，并报告 OSWorld-Verified 成功率达到 75%，相比 GPT-5.2 的 47.3% 大幅提升；Claude Sonnet 4.6 也继续显著提高 computer use、agent planning 和长上下文能力。厂商自报 benchmark 需要谨慎理解，但趋势很明确：Browser / Desktop 操作可靠性已经跨过了一个重要阈值。

过去：

Agent → API available? → Yes 才能执行

现在增加了一条路径：

Agent → API unavailable → Browser / Computer Use → Execute

这使“整个互联网”第一次大规模成为 Agent 的潜在工具集。

#### 长时间运行的 Agent Runtime 成熟

个人助理很少能在三分钟内完成所有事情。

它可能需要：

今天发邮件；

明天检查回复；

三天后再次跟进；

下个月续订。

因此 Personal AI 需要一个新的产品基础设施：

Persistent Agent Runtime

Muse 给每个用户独立 Secure VM；Dots 给 Agent 自己的 Cloud Computer；Cue 给每个 Agent 自己的 Computer；LightVela 把 Hermes 持续托管在云端。

这其实是 Personal AI 相对于 Chatbot 最容易被低估的一次架构变化。

过去 AI 是一个 request-response 服务。

现在它逐渐变成一个：

长期存在的软件进程。

#### Memory 开始成为正式的产品基础设施

Memory 也经历了类似变化。

ChatGPT 已经从用户手动保存 Memory 逐步扩展到参考历史会话；Today 则进一步强调 living memory 和用户可查看、修改、删除的长期记忆。

Personal Agent 的下一步很可能不只是 RAG 一个聊天记录库，而是一套真正的：

Personal Knowledge / State Model

例如：

| Personal state | 示例 |
| --- | --- |
| Identity | 我是谁 |
| People | 我的家人、朋友、同事 |
| Preferences | 饮食、品牌、旅行风格 |
| Commitments | 答应过谁什么 |
| Goals | 今年减重 10kg |
| Habits | 周三通常健身 |
| Constraints | 周五要接孩子 |
| Resources | 时间、账号、预算 |
| History | 过去怎样处理类似事情 |

谁建立了最完整、最可信的 User Model，谁会拥有极其强的长期 switching cost。

#### Tool layer 开始标准化

MCP 等标准把“AI 如何访问数据和工具”逐渐抽象为统一连接层；Manus 也明确把 MCP 描述为连接外部数据源的标准化管道，与 Skills 这一工作流层配合。

这意味着未来 Personal AI 不需要为每一家服务设计完全不同的 Agent architecture。

它越来越像：

Personal AI Runtime ↓ MCP / APIs / Skills / Browser ↓ Gmail / Calendar / Notion / Spotify / Uber / Shopify / 银行 / 本地生活……

从产业结构看，这和 PC 早期从“每个软件自己控制硬件”转向“OS 提供标准 API”的逻辑非常相似。

#### Agentic Payment 打通“最后一公里”

过去一个 Agent 即使帮你找到商品，最后经常卡在：

“请自己完成支付。”

这意味着执行链条最终仍然断掉。

Stripe 等公司正在建立 Agent-specific payment primitive：授权范围、时间、金额、商户都可以约束，同时无需向 Agent 暴露原始卡号。

Cue 甚至已经直接把 Wallet 设计成 Agent identity 的组成部分：每个 Cue Agent 都可以拥有 email、phone number、wallet 和 computer，并在用户设定预算内支付。

这是一个非常重要的信号：

“Wallet”未来可能像 Browser 一样，成为 Agent Runtime 的标准组件。

#### Security 虽然仍未解决，但进入工程化阶段

Personal AI 最大的阻力其实是 Trust。

一个会总结邮件的模型犯错，影响有限。

一个拥有：

邮箱 + 云电脑 + 信用卡 + 日历 + 通讯录 + 社交账号

的 Agent 犯错，风险完全不同。

Anthropic 的 Browser Agent 安全研究明确指出，网页里的恶意内容可以通过 prompt injection 劫持 Agent；即使其内部测试中 Opus 4.5 已把攻击成功率降低到约 1%，Anthropic 仍强调这个问题远未解决。

Muse 上线后也迅速暴露出这一现实：安全研究人员发现其 VM 和 filesystem 相关的攻击面，Meta 随后进行修复和强化。

因此 permission、sandbox、credential isolation、human confirmation、audit trail 会成为 Personal AI 的核心产品能力，重要程度和模型能力接近。

## 产品版图：当前热门 Personal AI 产品逐一拆解

如果按照“用户入口 + Agent 运行方式”分类，我认为目前市场可以分为四类。

### 消费级独立 Personal Agent

代表：

Muse、Today、Cue，以及未来可能出现的小豆 / Spell、Handy Bot。

优势是拥有完整产品体验，可以从零围绕 Agent 设计。

### 消息与生活入口原生 Agent

代表：

Instinct、小微、Alexa+。

它们试图让 Agent 出现在用户已经使用的交互界面里：短信、电话、微信、语音。

### Always-on Agent / 工作到个人的融合路线

代表：

OpenAI Dots。

它明显带有 Codex 和 ChatGPT Work 的基因，目前使用场景仍明显偏专业工作，但底层形态已经是 Personal AI：always-on、Cloud Computer、长期学习用户偏好、多入口沟通。

### Agent Hosting / Personal Agent Infrastructure

代表：

LightVela。

它主要解决部署和长期运行问题，更接近 Personal Agent 的 runtime platform。

### 全产品横向对比

| 产品 | 公司 | 当前状态 | 入口 / 形态 | 核心特点 | 我的定位判断 |
| --- | --- | --- | --- | --- | --- |
| 小豆 / Spell | 字节跳动 / 豆包 | 内测，未官宣正式版 | 预计独立 App | 豆包手机助手能力延伸 | 消费级 Personal Agent |
| 小微 | 腾讯 / 微信 | 小范围灰度测试 | 微信原生 | 微信功能 + 小程序 + 生活服务 | 超级 App 原生 Agent |
| LightVela | 腾讯云 | 已公测/可体验 | 云端托管 | 云端 Hermes、7×24、Skills | Agent Runtime |
| Handy Bot | 腾讯 | 媒体曝光、未正式官宣 | 预计独立 App | 云端常驻 Personal Agent | 腾讯第二条独立产品路线 |
| Today | Today AI | 已上线 | Mac / iOS / Android / Web | Living Memory、主动性、Long Arcs | Memory-first Personal AI |
| Cue | Manus AI | Early Access | 独立 App / Desktop | 每个 Agent 有邮箱、电话、钱包、Computer | Agent identity-first |
| Muse | Meta | 已上线 | App + WhatsApp | Secure VM、主动、目标管理、消费级 UX | 当前大众市场标杆 |
| Dots | OpenAI | 正在 rollout | ChatGPT / Slack / Teams | Always-on、Cloud Computer、4000+ App | Work-first Personal Agent |
| Alexa+ | Amazon | 已上线并持续扩展 | Voice / Echo / Web / App | 家庭、购物、Smart Home、服务 | Ambient Personal AI |
| Instinct | Instinct | Invite / Limited Access | Text / Voice / Phone | 无 App 理念、代办生活事务 | AI Concierge |

### 字节跳动：小豆 / Spell

这是目前公开信息不确定性最高的产品之一，目前信息主要来自媒体报道，字节尚未正式发布“小豆”产品。

科创板日报等报道显示，豆包团队从 2026 年 4 月开始内测 Personal Assistant 探索项目，内部代号 Spell，主要由豆包手机助手团队主导；9 月 Muse、Instinct 等 Personal Agent 在海外引发关注之后，项目推进加快。9 月 30 日进一步有媒体报道称，独立产品可能命名为 “小豆”，计划推出独立 App，但最终版本仍可能调整。

值得注意的是，豆包已经先在手机侧训练自己的 Agent 能力。媒体报道显示，豆包手机助手的消费者版本已在 2026 年 9 月落地终端，因此小豆可以理解为将“手机 Agent”积累的能力抽离成一个跨终端 Personal Agent。

战略优势：

字节拥有强大的消费者产品能力、推荐系统经验、内容与兴趣数据，以及豆包已经形成的 AI 用户基础。它如果进入 Personal AI，最值得观察的是能否把原有的 Interest Graph 进一步转化为 Intent Graph。

### 腾讯：小微

小微是所有中国产品里我认为战略位置最高的一个。

截至 2026 年 10 月 1 日，小微已不再只是“筹备中”：小微于 6 月 20 日开始小范围内测。

财联社向腾讯客服确认，小微是微信团队开发的原生 AI Assistant，可以通过文字、语音操作微信原生能力，包括调整设置、发消息、打电话；还能调用小程序完成挂号、买咖啡等生活服务，并支持内容搜索、图片生成等功能。

更关键的是：

小微可以调用小程序。

这给它带来了其他 Personal AI 很难复制的优势。

传统 Browser Agent 的路径是：

AI → 打开网站 → 看屏幕 → 点击 → 等页面 → 填表 → 再点击。

小微潜在路径是：

AI → 理解用户 Intent → 调用小程序服务 → 用户确认支付。

财联社报道还指出，微信在 6 月向开发者开放 AI 生态接入，并推出面向 AI 场景的支付基础设施。

如果这条链路真正成熟，微信可能拥有一个中国市场极强的 Personal Agent 闭环：

Social Graph + Communication + Mini Programs + Local Services + Payment + Personal Agent

这也是我认为腾讯在 Personal AI 时代拥有巨大“主场优势”的原因。

### 腾讯：LightVela

LightVela 是腾讯轻量云团队推出的 云端 Agent 托管产品。

官方文档显示，它当前提供 Hermes Agent，负责 Agent 的部署、运行与维护，用户可以配置模型、渠道和 Skills。相比本地部署 Hermes，LightVela 把服务器、运行环境和持续在线这些门槛全部拿掉。

所以它目前更接近：

Personal Agent PaaS / Cloud Runtime

而不是完整的消费级 Personal AI。

这条路线对于腾讯仍然很有意义。

因为未来一个用户可能并非只有一个 Agent：

Primary Agent + Travel Agent + Coding Agent + Research Agent + Finance Agent + Shopping Agent

这些 Agent 都需要长期运行环境。

LightVela 在抢的更像未来的：

Agent Cloud。

### 腾讯：Handy Bot

Handy Bot 目前公开信息非常有限。

媒体近期报道称腾讯内部正在开发名为 Handy Bot 的 Personal Agent，并可能推出独立 App；相关微信服务号曾出现“你的个人 AI 智能体”描述，但产品形态和正式发布计划均未得到腾讯官方确认，因此目前应当视为媒体曝光 / 内部探索阶段。

从产品组合来看，一个合理推测是腾讯正在同时探索三个不同控制点：

小微：微信入口 Handy Bot：独立消费产品 LightVela：Agent Runtime

这形成了从 Application 到 Platform 到 Infrastructure 的完整布局。这里属于基于公开产品组合的战略推断。

### Today

Today 是这轮 Personal AI 中非常典型的 memory-first 产品。

Today 官方把自己的核心能力定义为：

Knows you Acts before you ask Walks with you across months

产品强调 living memory、proactivity 和 execution；Memory 可以被用户查看、编辑和删除，涉及发送邮件、移动 Calendar、向其他人发消息等外部动作时，需要用户确认。Today 已提供 Mac、iOS、Android 和 Web 版本，目前产品处于免费阶段。

Today 的产品哲学和 Muse 有一个很有意思的区别。

Muse 更强调：

“我可以替你做很多事情。”

Today 更强调：

“我长期知道你在做什么。”

因此 Today 是观察 Personal AI “memory layer”最值得跟踪的产品之一。

它真正想建立的产品资产不是某一次 Agent execution，而是：

一个逐渐成长的 Personal Context Graph。

这会直接影响 Personal AI 的留存逻辑。

传统 SaaS 的 switching cost 来自数据和 workflow。

Personal AI 的 switching cost 可能来自：

“它已经认识我两年了。”

### Manus Cue

Cue 是我认为当前这批产品里 Agent architecture 最激进的产品。

Manus 在 Manus 2.0 中把 Cue 定义为面向手机和桌面的 Personal Agent 独立 App，并提出：

Every agent gets its own identity.

具体来说，每个 Cue Agent 都可以拥有：

Email

Phone number

Wallet

Computer

它能够发消息、在预算内支付、接电话并将摘要带回 Cue。

这很值得重视。

因为 Cue 正在尝试解决一个非常底层的问题：

Agent 如何在数字社会里成为一个可以行动的主体？

一个人之所以能在数字社会行动，是因为他有：

Email identity Phone identity Account identity Payment identity Device

Cue 在给 Agent 配置同样的基础设施。

这意味着 Personal AI 的架构有可能从：

AI uses my accounts

逐渐演化成：

My AI has its own delegated identity.

这很可能成为未来几年非常重要的一条产品路线。

Cue 同时支持多 Agent 协作，最终形态很可能类似：

用户

↓

Primary Personal Agent

↓

Specialized Agent Team

这与 OpenAI 对未来 “teams of Dots” 的设想高度接近。

### Meta Muse

如果只选一个产品作为 2026 年 Personal AI 品类真正出圈的标志，我会选 Muse。

Meta 9 月 8 日发布 Muse，将其定位为面向所有人的 Personal AI Agent。Muse 运行在每个用户自己的 Muse Secure VM 中，带有 Browser，可以跨应用完成任务；用户关闭 App 后任务仍然可以继续。它同时支持 Muse App 和 WhatsApp。

它最值得关注的能力组合包括：

长期用户理解

通过 conversations 和 connected context 逐渐理解用户。

Proactivity

主动提出建议并推进 Goal。

Persistent Computer

每个用户有专属云端运行环境。

Commerce

可以帮助购买商品、处理实际消费任务。

Human-in-the-loop

敏感动作保留用户确认。

人格化

Muse 将 Agent 包装成一个用户可以建立长期关系的角色，而非传统软件工具。

Meta 从 2025 年就持续公开强调 “personal superintelligence for everyone”，2026 年的 Muse Spark 模型也被明确描述为朝这一目标构建。因此 Muse 对 Meta 来说显然不是孤立产品实验，而是公司 AI 战略落地的一部分。

更重要的是 Muse 的 Distribution。

截至 9 月 24 日左右，Sensor Tower 估计下载约 340 万；Meta 已经利用 Facebook、Instagram 等自家产品推广 Muse。

Meta 是目前 Personal AI 领域最值得警惕的公司之一，因为它同时拥有四项资产：

Frontier AI + Social / Relationship Graph + Distribution + Ads / Commerce monetization

这四项组合起来非常强。

### OpenAI Dots

OpenAI 在 9 月 29 日发布 Dots，动作明显带有对 Muse 的回应意味。

Dots 是 always-on agent，由 GPT-6 Astra 驱动，每个 Dot 有自己的 Cloud Computer，可以长期执行 Goal，并通过 ChatGPT、Slack、Teams 与用户互动；OpenAI 表示未来还将支持短信。

Dots 还可以连接大量应用，并支持用户创建 primary Dot，长期则计划形成多个 specialist Dots 的团队。

不过当前 Dots 的产品气质和 Muse 有明显差异：

Muse：生活优先。

Dots：工作优先。

OpenAI 官方及媒体展示的大量案例包括：

软件开发、Bug 修复、科研分析、销售、内容生产、项目管理等。Reuters 也将其描述为 OpenAI 加深 enterprise AI 布局的重要产品。

因此 Dots 很像一个有趣的交叉点：

Work Agent → Always-on Agent → Personal Agent

这也符合 OpenAI 的结构性优势：ChatGPT + Codex + Enterprise ecosystem。

### Amazon Alexa+

Alexa+ 是当前这批 Personal AI 产品中最容易被低估的玩家。

Amazon 在 2025 年发布生成式 AI 驱动的 Alexa+，2026 年持续扩展，其定位已经从传统 Voice Assistant 转向能理解用户、采取行动的 Personal AI Assistant；产品跨 Echo 等设备、Alexa App 和 Web 工作，并与 Amazon 的购物、音乐、日程、智能家居以及第三方服务结合。

Alexa+ 的独特价值不在于做出一个新的 Chat App。

它控制的是：

Ambient Computing。

你的厨房、卧室、客厅、汽车和各种设备都是它的入口。

因此未来 Personal AI 很可能出现两种主要交互范式：

Screen-first

Muse / Today / Cue / Dots。

Ambient-first

Alexa+ / Siri / Glasses / Earbuds / AI wearable。

Alexa+ 在家庭环境里拥有非常长时间积累的设备、语音、Smart Home 和 Commerce 基础，这是初创公司很难短期复制的。

### Instinct

Instinct 是这一轮最值得研究的 Startup。

它有一个非常大胆的产品选择：

尽量减少 App 本身。

用户主要通过 text、voice 或 phone 与 Agent 沟通，让 AI 去处理旅行、买菜、票务、订阅、预订等事情。Reuters 报道公司 2025 年由前 Sierra 员工 Noah Shinn 创办，2026 年 9 月完成 10 亿美元融资，估值达到 100 亿美元。

这背后的产品哲学非常值得思考：

一个真正的私人助理，本来就不需要你每天打开一个“私人助理 App”。

现实里的 executive assistant 不会要求老板：

“请打开我这个软件。”

老板发一句消息：

帮我安排一下。

事情就完成了。

所以 Instinct 代表一种 interface-less AI 思路。

这可能是 Personal AI 的长期方向：

AI 不再是 Destination App，而成为随处可达的 service。

不过它也暴露了 Startup 与大厂竞争时一个非常现实的问题：算力和 Agent Runtime 成本。9 月下旬已有用户报告 Instinct 出现延迟和任务遗漏，其有限的基础设施能力被认为是一个因素；相比之下，Meta 可以依赖自有大规模 AI 基础设施支持 Muse。

这说明 Personal AI 可能会成为一个极度 compute-intensive 的消费产品赛道。

## 大厂为何争夺：Personal AI 正成为用户与数字社会之间的“意图操作系统”

从产业结构来看，一个值得重视的判断是：

争夺 Personal AI，争夺的不只是新的流量入口，更是一层架设在用户与数字社会之间的专属操作系统。

但我会把这个概念进一步精确化为：

Personal AI = Personal Intent & Action OS

它控制的并非传统 Device OS 的系统资源，而是人的数字意图和行动权。

### 下一代竞争从“Attention”进入“Delegation”

过去二十年互联网最核心的资源是：

Attention

谁占据用户更多 Screen Time，谁掌握广告和流量分配权。

Google 抢 Query。

Facebook / TikTok 抢 Feed。

Apple 抢 Home Screen。

Amazon 抢 Shopping Search。

微信抢通信和服务入口。

Personal AI 带来一个更高阶的变量：

Delegation——用户愿意把多少决策和行动委托给你。

这是一个比 DAU 更有战略价值的变量。

因为：

Attention = 用户在看谁

Intent = 用户想做什么

Delegation = 谁有权替用户去做

当 Agent 从：

“我建议你买 A”

走到：

“我已经按照你的偏好选好 A，价格在预算内，确认后购买”

互联网价值链就开始改变。

### Personal AI 的技术栈最终可能长这样

| 层 | Personal AI OS 中对应能力 |
| --- | --- |
| Interface Layer | Chat / Voice / Glasses / Earbuds / Messaging |
| Personal Context Layer | Memory / Relationship / Preference / Goals |
| Intent Layer | 理解真正目标 |
| Planning Layer | 拆解任务、资源规划 |
| Permission Layer | 什么可以自动做、什么必须确认 |
| Execution Runtime | Cloud Computer / Browser / Code |
| Tool & Service Layer | MCP / API / Skills / Mini Programs |
| Identity Layer | Email / Phone / Accounts |
| Transaction Layer | Wallet / Payment / Commerce |
| Audit & Trust Layer | History / approval / rollback / security |

现在再看 Cue：

Email + Phone + Wallet + Computer。

看 Muse：

Memory + Secure VM + Browser + Payment + WhatsApp。

看 Dots：

Cloud Computer + Long-running goals + thousands of apps。

看微信小微：

WeChat + Mini Programs + Payment + Social Graph。

这些公司其实正在拼同一张图的不同部分。

### Apps 的角色会逐渐变化

传统移动互联网的产品路径：

人产生 Intent → 想应该用哪个 App → 打开 App → 学习 UI → 找功能 → 输入信息 → 完成任务

Agent-native 世界可能变成：

人产生 Intent → 告诉 Personal AI → Agent 选择服务 → 调 API / Browser / Mini Program → 请求必要确认 → 完成

这意味着用户对很多 App 的需求将逐渐从：

Interface

转成：

Service Endpoint。

Bill Gates 在 2023 年就预言，Agent 会降低用户在不同 App 之间切换的必要性，并可能改变搜索、电商和生产力软件。

2026 年已经能看到现实迹象。

Google 正把 Agent、Personal Intelligence 和 Search 融合，使 Search 从“返回信息”走向“帮助执行”；Apple 在 2026 年发布新的 Siri AI，强调 personal context、onscreen awareness 和 systemwide actions，可以跨 Messages、Mail、Photos 等个人数据和 App 工作。

这说明传统 OS 厂商也已经意识到：

如果 Personal AI 成为用户意图的第一入口，操作系统原本拥有的部分中介权力可能向 Agent 层上移。

### 为什么 Meta 特别激进

Meta 的动机尤其强。

Apple、Google 天然拥有 Device OS。

Amazon 拥有 Commerce。

腾讯拥有微信超级 App。

Meta 长期缺乏手机操作系统这一层。

Personal AI 给 Meta 一个新的机会：

绕过 OS，在“人”这一层建立新的平台。

Meta 从 2025 年开始公开推动 “personal superintelligence for everyone”，2026 年持续投入巨额 AI 基础设施，并将 Muse 作为消费者端落地。

如果用户未来首先告诉 Muse：

“给我安排周末。”

那么 Muse 可以决定：

搜索什么；

推荐什么；

联系谁；

调用哪个商家；

买什么；

在哪里支付。

此时它拥有过去分散在：

Google + Yelp + Expedia + Amazon + App Store

之间的部分分发权。

因此 Muse 的真正终局不只是：

“Meta 有一个很厉害的 AI App。”

更可能是：

Meta 尝试建立一个在传统 mobile OS 上方运行的 Personal OS。

### 腾讯可能拥有中国市场最特殊的结构优势

如果 Personal AI 的关键竞争力是：

Context + Distribution + Execution + Payment

微信几乎天然拥有这四个部分：

Context

通讯、群聊、公众号、朋友圈等生活上下文。

Distribution

微信巨大的用户规模。

Execution

数百万小程序形成服务生态。

Payment

微信支付。

这使微信有机会形成非常短的 Agent loop：

“周五帮我和 Alex 找个地方吃饭”

小微潜在可以：

识别 Alex → 看时间冲突 → 找餐厅 → 调用小程序 → 发消息 → 建群/确认 → 订位 → 支付

整个流程可能不需要用户离开微信。

财联社报道显示，小微当前已经能够调用小程序完成咖啡购买、挂号等服务，并由用户完成关键支付确认。

这是一种 Browser Agent 很难匹敌的“生态级执行权”。

### Amazon 的防御逻辑也完全成立

Amazon 面对 Muse 这样的产品存在一个非常直接的战略风险：

过去：

用户想买东西 → Amazon Search

未来：

用户告诉 Muse “帮我买最适合我的东西” → Muse 比较多个商家 → Amazon 只是供应商之一。

Amazon 因此有强烈动力让 Alexa+ 自己占据用户购买 Intent 的第一入口。

市场分析也已经开始讨论 Muse/Dots 是否会影响 Amazon 的购物入口与广告业务；相关报道同时指出 Amazon 正发展自己的 AI shopping assistant，并对第三方 Agent 抓取 Amazon 采取防御措施。

这就是 Personal AI 战争最核心的一层：

谁拥有用户 Intent，谁就可能重新分配下游流量。

## 竞争格局、风险与我的产品判断

### Personal AI 会形成新的护城河：Memory Lock-in

搜索引擎护城河来自：

Index + Distribution

社交网络来自：

Social Graph

SaaS 来自：

Data + Workflow

Personal AI 很可能形成一种以前很少见的护城河：

Personal Context Lock-in

假设 Muse 已经陪你三年：

它知道：

你的家庭关系；

所有重要朋友；

饮食习惯；

旅游风格；

过去购买；

过去健康计划；

工作习惯；

长期目标；

如何替你写邮件；

什么情况应该打扰你；

哪些决定你通常会同意。

这时候迁移到另一个 AI 的成本非常高。

因此真正值得关注的产品指标不应该只看：

MAU、DAU、Session Length。

我会重点看：

| Personal AI 核心指标 | 意义 |
| --- | --- |
| Delegated Tasks / WAU | 每周用户真正委托多少件事 |
| Task Completion Rate | Agent 能真正完成多少 |
| Proactive Acceptance Rate | 主动建议有多少被认可 |
| Confirmation → Execute Rate | 用户多信任它的判断 |
| Permission Expansion Rate | 用户是否愿意开放更多权限 |
| Memory Correction Rate | User Model 准确程度 |
| Autonomous Task Duration | 能持续管理多久 |
| Repeat Delegation Rate | 一件事成功后是否继续交给它 |
| Human Intervention Rate | 需要用户救场多少次 |
| Trust Incident Rate | 错发、误买、越权等严重事故 |

最终最重要的 North Star Metric，我甚至会考虑：

Hours / Decisions Delegated per User

即：

一个人有多少生活认知负担真正交给了 AI。

这比“用户和 AI 聊了多久”更符合 Personal AI 的真实价值。

### 最大竞争壁垒其实是 Trust

Personal AI 会出现一个非常特殊的增长飞轮：

Agent 第一次把事情做好 ↓ 用户相信它 ↓ 给更多数据 ↓ 给更多权限 ↓ Agent 得到更多 Context ↓ 判断更加准确 ↓ 用户委托更重要的事情

这是：

Trust Flywheel

但它同样可能反向：

错发一封邮件 → 用户关闭邮件权限 → Context 变差 → Agent 更难发挥价值 → 用户停止使用。

Personal AI 对错误的容忍曲线会非常不对称。

回答一道知识问题错一次，用户可能重新问。

替用户给老板发错邮件，是另一种级别的事故。

Anthropic 已明确指出 Browser Agent 仍然面对 prompt injection；Muse 上线后的安全事件也说明 Personal Agent 一旦连接真实账户、浏览器和数据，攻击面会急剧扩大。

因此未来 Personal AI 的竞争，很可能出现一个反直觉现象：

最强模型未必直接等于最好的 Personal AI。

胜负还取决于：

Memory architecture；

Permission architecture；

Identity；

Security；

User control；

Recovery / rollback；

Agent UX。

### “越主动越好”会是一个危险误区

Personal AI 很容易走向：

多提醒 = 更主动 = 更智能。

实际体验很可能相反。

一个真正优秀的人类助理最大的能力之一是：

判断什么时候值得打扰老板。

Today 对这一问题的描述很有意思：Proactivity 的难点在 restraint，过多 false positives 很快会摧毁用户信任。

因此 Personal AI 的“主动性模型”将成为一种新的 Recommendation System。

过去推荐系统解决：

What should I show you?

Personal AI 解决：

Should I interrupt you? Should I act now? Should I ask first? Should I stay silent?

这比 Feed Ranking 更复杂，因为它涉及行动。

### Personal AI 可能最终只剩一个 Primary Agent

未来用户当然可以拥有多个 Specialist Agent。

但我不认为普通用户愿意每天管理二十个 Agent。

更合理的长期结构可能是：

One Primary Personal Agent

↓

Travel / Shopping / Research / Coding / Finance / Health / Work Specialist Agents

↓

Services / Apps / APIs / Humans

这一点已经开始出现在产品设计上。

OpenAI 明确提出 primary Dot 和未来 teams of Dots；Cue 已经支持多个具有独立身份的 Agent 协作。

所以真正决定平台地位的问题可能不是：

谁拥有最多 Agent？

而是：

谁成为用户的 Primary Agent？

因为 Primary Agent 拥有：

Personal Context；

Intent；

Permission；

Routing。

它相当于 Agent Economy 的“默认入口”。

### 下一场平台战争可能围绕 Agent Access 展开

这里也必须给“Personal AI = OS”的判断加一个重要限定。

今天的 Muse、Instinct、Dots 仍然高度依赖其他平台：

Amazon 可以阻止 Agent；

银行可以限制 Agent；

Apple 可以限制系统权限；

网站可以禁止自动访问；

社交平台可以阻止自动发送。

因此它们现在还没有真正意义上的 OS sovereignty。

未来几年很可能出现一场非常重要的产业战争：

Should apps/services allow third-party agents to act for users?

过去平台战争围绕：

App Store；

浏览器；

默认搜索；

Cookie；

支付。

未来可能围绕：

Agent Access Agent Identity Agent Authorization Agent Payment Agent-to-Agent Protocol

展开。

Stripe 的 Agentic Commerce Protocol、Shared Payment Token 等技术已经开始搭建这套新基础设施。

### 对“2026 上半场龙虾，中场办公 AI，下半场 Personal AI”的进一步理解

我认为这句话背后其实隐藏着一条非常漂亮的 Agent 产品演进路径：

第一阶段：Agent as Tool

OpenClaw / Hermes。

核心问题：

AI 到底能不能自己干活？

答案逐渐变成：可以。

第二阶段：Agent as Worker

Coding Agent、Cowork、WorkBuddy 等工作型 Agent。

核心问题：

AI 能不能在一个明确的专业环境中承担工作？

答案也越来越肯定。

第三阶段：Agent as Assistant

Muse / Today / Instinct / Cue / Dots。

核心问题：

AI 能不能持续理解一个人，并帮这个人管理工作之外的整个数字生活？

2026 年下半年正在集中验证这个问题。

而我认为再下一阶段会是：

Agent as Representative

届时 Agent 不仅知道用户是谁和想做什么，还可以稳定地：

替你沟通；

替你谈判；

替你购买；

替你预订；

替你维护关系；

替你长期管理目标；

在有限预算和规则内自主做决定。

Cue 给 Agent 配 email / phone / wallet / computer，已经非常像这一方向的早期形态。

再往后一步，则是：

Agent as Digital Twin / Personal Operating Layer

它将成为你与数字世界长期交互的一层代理。

### 最终判断：真正的入口从“App”转向“Intent”

过去十五年，移动互联网的核心问题是：

用户打开哪个 App？

生成式 AI 的第一阶段把问题变成：

用户问哪个 AI？

Personal AI 进一步改变为：

用户首先把自己的意图告诉谁？

这一步看起来很小，产业后果非常大。

因为谁拿到用户最原始的 Intent，谁就有机会决定：

搜什么 找谁 打开什么服务 推荐什么 买什么 用什么支付 什么事情自动完成 什么事情需要询问用户

因此，我会把未来 Personal AI 的核心竞争资源从互联网时代的 流量，升级为三个层次：

Attention → Intent → Delegation

第一层是用户看你。

第二层是用户把需求告诉你。

第三层是用户允许你代表他行动。

Personal AI 真正争夺的是第三层。

这也是为什么 Meta、OpenAI、Amazon、腾讯、字节、Google、Apple 都很难缺席。

Google 已经把 Personal Intelligence、Search Agent 和 proactive assistant 逐渐融合；Apple 2026 年新的 Siri AI 直接依托 OS 级 personal context 和 systemwide actions；Meta 则公开把 Personal Superintelligence 定义为未来方向。

从这个角度回头看 Muse、Cue、小微、Dots：

它们表面上是几个新的 AI 助手。

产业更深层正在争夺的是：

谁来维护关于“我”的数字模型；

谁第一个听到我的需求；

谁拥有调用整个数字社会替我办事的权限；

谁最终成为我默认信任的 Primary Agent。

所以可以把前面的判断再推进一步：

Personal AI 的终局不只是架设在用户与数字社会之间的一层专属操作系统，它更接近一个“个人意图、身份、权限与行动的控制平面”。传统 OS 管理设备，Personal AI 有机会管理人的数字生活。

在这个体系里，App 逐渐成为工具，网站成为资源，支付成为能力，AI Agent 成为新的交互主体，而用户本人第一次拥有一个可以持续代表自己行动的软件代理。

这也是为什么，2026 年下半年 Personal AI 的爆发，很可能比又一轮 AI App 热潮更重要。

它对应的是 AI 产品范式从：

Chatbot → Agent → Personal Agent → Personal Operating Layer

的迁移。

而这条链路的最后一步，有潜力成为移动互联网之后下一场真正的平台战争。

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过