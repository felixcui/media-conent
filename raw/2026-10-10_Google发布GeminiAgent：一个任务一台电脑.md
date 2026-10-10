# Google发布Gemini Agent：一个任务一台电脑

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/arEg3qohVq7k6XYtySl5XA

---

## 摘要

Google Cloud在Gemini at Work 2026发布Gemini Agent，以任务而非机器为基本单位，每个任务获得独立计算资源并由Gemini协调。它提供统一API支持聊天、自主任务和代码生成，可动态创建拥有独立Workspace身份的协作者agent，覆盖全设备与无头模式，云端7x24运行，具备四层记忆、企业工具注册表、多模型路由及类似员工的治理机制。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

Google Cloud 在 Gemini at Work 2026 上发布了 Gemini Agent。

CEO Thomas Kurian 的原话很直接：work now starts in the prompt window。

过去我们讨论 agent，不管是 AutoGPT 还是当前流行的grokbot，muse这些个人agent，都是在想"怎么让一个 agent 管好一个实例"。Google 的选择是把任务变成基本单位，机器不再是边界。每个任务获得独立计算资源，可以跑几个小时甚至几天，任务之间由 Gemini 协调。

顺着这个思路，所有设计都不一样了。

**一个 API，三种工作模式**

聊天、自主完成任务、代码生成，全在一个接口里。你可以派活、定时任务、让它响应事件。Kurian 的表述是：你给的是目标，不是指令。你委派一个结果，回来时工作已经完成了。

**协作者 Agent 有自己的身份**

Gemini 可以动态创建子 agent，每个都有独立身份和独立计算机，并行或串行跑。

这件事的细节比听起来更具体。每个协作者 agent 拥有专属的 Workspace 账号：@agents.company.com 邮箱、独立日历、独立 Drive，甚至出现在公司通讯录里。同事在 Chat 里 @ 它，它在文档评论里回复，版本历史里显示的是它自己的名字。它用自己的身份行事，而不是你的。你分享什么，它就看到什么。

有两种形态。一种是临时性的子 agent，为特定任务而生，任务结束就消失。另一种是持久化的 coworker agent，像一个真正的团队成员，有自己的角色定义，跨天、跨会话、跨多种职责持续运作。

**设备全覆盖，包括无头模式**

Web、iOS、Android、Windows、Mac、命令行、Google Workspace、Microsoft 365、Slack。也可以作为无头 agent 跑，不绑定任何界面。

**云端 7x24，合上电脑继续跑**

所有设备共享同一套记忆、上下文和个性化图谱。不需要在不同设备上重新交代背景。跑几小时或几天的任务，合上电脑也不会中断。

这一点对实际使用的影响比看起来大。过去用 agent，你得惦记着"我在哪台机器上跟它说的"，现在不用了。

**四层记忆**

会话记忆：当前任务的上下文，即使跑几天也不丢。

语义记忆：读文档、跟人交流、和其他 agent 协作时构建的结构化知识库。

程序性记忆：完成任务的方法，包括 agent 自己写的技能。

情景记忆：做过的一切。

Google 的说法是它像新员工一样自己 onboarding，在实际干活之前先了解你、你的工具、你的团队。

**不等指令**

收件箱里有人让你做 PPT，Gemini 会识别出这是可以委派的任务，点一下就能交接。邮件排序不是按到达时间，而是按重要程度，并且告诉你为什么。

**工具和技能有企业注册表**

Salesforce、ServiceNow、Jira、Git、Confluence、Microsoft 365、Slack、BigQuery、Databricks、Postgres、Snowflake、桌面文件，任何企业网络内外的 MCP 服务器。团队可以把自建工具和技能发布到共享注册表，全公司复用。

技能在这里的定义是：可复用的指令、知识或工作流，以模块化 prompt 的形式存储。Gemini 自带一套全球技能库，团队可以自建，个人也可以。

**模型不锁定**

每个任务自动匹配最合适的模型。目前支持 Gemini 系列（Argon、Flash）和 Anthropic 的 Claude 系列（Opus 5.5、Sonnet 5.5），未来会接入更多私有和开源模型。

这个设计的逻辑是：最好的模型每几个月就会变一次。把 agent 和模型解耦，你的上下文、技能、数据都不需要跟着模型换而迁移。简单任务用小模型省钱，复杂任务上大模型保质量。PayPal 已经在这样跑了，每周路由 1000 万次多模型请求。

**治理像员工，不像是脚本**

每个 agent 有加密签名的独立身份，最小权限原则。审计日志归属到 agent 本人，而不是某个自然人。所有 agent 跑在 Agent Sandbox 里，有自己的网络边界。所有流量进出和 agent 间通信都经过 Agent Gateway——一个 AI 网络防火墙。策略写一次，"agent 不得打开标记为 Need to Know 的文档"，应用到所有 agent。

有人问审计归属的问题：agent 做了错事，谁负责？Shubham Saboo 在回复里解释，如果是个人 agent，日志显示"我的 agent 在我授权下做了某件事"。如果是团队共用的 coworker agent，责任在管理员加上分享数据给它的人，就跟员工出了事追责一样的逻辑。

**成本可控，设硬上限**

Smart Routing 自动把每个任务交给性价比最高的模型。在 Cloud Billing 里设置支出上限，超了项目自动暂停，一键恢复。按项目追踪，可以精确到部门的成本核算。

下面跑的是 TPU 8i，比上一代价格性能提升 80%。

**Workspace 内联：在文档里、邮件里、聊天里**

Gemini 不只是独立窗口里的对话工具。它直接嵌入 Gmail、Drive、Docs、Slides、Sheets、Chat、Calendar。同一个记忆、同一套技能、同样的控制策略。

举个例子：你可以让它"约下周跟区域活动负责人开会"，不用提供任何名字或邮箱。Gemini 自己从你的 Chat 群组成员和上次活动的邮件线索里判断出这些人是谁，检查日历，发起邮件协调时间，包括外部参会者也没问题。

跨应用也能连续作业：研究市场趋势、在 Sheets 里建财务模型、然后生成包含两者的演示文稿，不需要在每个步骤重新解释项目背景。

**行业化、数据化**

金融行业版集成了 FactSet、LSEG、S&P Global、SEC 文件，50 多个基础技能，带置信度评分、方法论展示、完整数据血缘和可核查的引用。法律版从 NetDocuments 和 iManage 继承案件级权限和道德防火墙。

数据方面，Knowledge Catalog 把"净利率""可寻址市场"这类业务定义映射一次，所有 agent 共用。Bloomberg Media 试下来，SQL 查询准确率提升了 63%。Smart Storage 直接在非结构化数据的存储对象上写入上下文，不用搬数据。Borderless Lakehouse 可以跨 Amazon S3、Azure Data Lake、Databricks、Snowflake 做联邦查询，不收出口费。

**一个感受**

整个发布会看下来，Google 不是在做"更好的 ChatGPT"，也不是做"又一个 agent 框架"。他们是在把 agent 当成企业基础设施来建。身份、权限、审计、沙箱、防火墙、成本控制——这些东西单看每一项都不性感，但缺了任何一项，企业都不敢把 agent 真正放进业务流程。

一个任务一台电脑，任务成为基本单位，agent 之间用身份和权限协作而不是靠 prompt 拼接。这个方向如果跑通，企业软件的工作方式会有很大变化。至少，Google 把工作智能体的形态往前推了一步。

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过