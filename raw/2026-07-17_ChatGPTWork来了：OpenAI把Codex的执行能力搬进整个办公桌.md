# ChatGPT Work 来了：OpenAI 把 Codex 的执行能力搬进整个办公桌

**作者**: 烟花老师

**来源**: https://mp.weixin.qq.com/s/4rwGzm0fCA2a_564YWhguQ

---

## 摘要

OpenAI发布由GPT-5.6驱动的新智能体ChatGPT Work，将Codex的执行能力从代码领域拓展至通用办公场景。Work与负责问答的Chat和负责代码的Codex形成互补，能读取跨平台文件与应用数据，将目标拆解为多步骤任务并持续执行数小时，最终输出可编辑的文档、表格等成品，实现了从“给答案”到“接走一整段工作”的产品边界跨越。

---

## 正文

烟花老师 烟花老师

在小说阅读器读本章

去阅读

一支烟花AI · PRODUCT NOTE

ChatGPT Work 来了：OpenAI 把 Codex 的执行能力搬进整个办公桌

QUOTE

聊天框负责给答案，Work 要接走一整段工作。

—— Bard强

本文看点

01

Codex 走出代码世界

02

Work 的运行机制

03

安全边界与竞争

7 月 9 日，OpenAI 发布了 ChatGPT Work。

官方帖很短：一个由 GPT-5.6 驱动的新 agent，可以进入你的文件和应用执行操作，陪着一个项目跑上几个小时，把目标变成完成的工作。

这几句话很容易被看成一次常规功能更新。把 OpenAI 同期放出的文档、模型说明和管理员 FAQ 连起来看，产品边界已经变了。过去一年在 Codex 上积累的长任务、工具调用、文件操作、权限审批和结果验证，正在被搬进 ChatGPT 的通用工作入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HR8kIomiaALSssv7D9lpf0BNcXPCpOXfVmkR7lcicPM08t9rDcTUKsUgmTc0Gdgt8wEYic3PEibQKJ8O89UtKUZOTRxz0uqYXmQ7433fic7rLQJI/640?from=appmsg)

— OpenAI 官方演示画面：Introducing ChatGPT Work

图源：OpenAI 官方 ChatGPT Work 演示视频。

01

PRODUCT MAP

### OpenAI 把 Codex 搬出了代码世界

OpenAI 对 Work 的定义很直接：把一项真实工作委派给 ChatGPT。

普通 Chat 适合提问、搜索、讨论和短草稿。Codex 继续处理代码库、终端、测试、Git 和 PR。Work 接住中间那块长期被低估的区域：做一份 brief，整理一套 deck，分析多份表格，追踪一个项目，生成周期简报，或者把一堆分散材料做成可以交给同事继续编辑的成品。

OpenAI 的新产品结构由三条工作流组成：

• **Chat** ：围绕问题展开对话，结果通常是一段回答。

• **Work** ：围绕目标组织材料、步骤和工具，结果是一件可审阅的交付物。

• **Codex** ：围绕软件系统执行修改与验证，结果是代码、diff、测试或 PR。

这个划分很像一家小型工作室。Chat 是讨论桌，Work 是项目经理和执行团队，Codex 是工程车间。三者共享模型和一部分工具基础设施，但验收方式完全不同。

对一支烟花 AI 的读者来说，最值得盯住的是 Work 背后的 runtime。OpenAI 在管理员 FAQ 中写得很清楚：Work 把 Codex 背后的技术带进 ChatGPT，用来处理更长、更复杂的多步骤任务。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALQN7LSf6ylDT8feCibicmfn2bEJXjj3khXUibga9FXjdDeOETpxmVJqQibUReX8S3icBpnKTzVynicrOA8IG2It1nTbjRZDgVIrxgD60/640?from=appmsg)

— OpenAI 官方演示画面：Work 读取项目文件并在关键操作前请求批准

图源：OpenAI 官方 ChatGPT Work 演示视频。界面同时展示项目文件、权限策略和 GPT-5.6 Sol。

02

CAPABILITIES

### Work 到底能做什么

目前公开的能力可以分成四层。

获取上下文

Work 能读取当前对话、项目文件、用户上传材料和插件连接的数据。插件覆盖 Slack、Google Drive、SharePoint、邮件、日历、CRM、项目管理工具等常见工作系统。

在桌面应用里，它还能使用经过授权的本地文件、浏览器和桌面应用。这里的“使用”已经超出读内容：Computer Use 可以看屏幕、点击、输入、切换窗口和操作已登录网页。

把目标拆成步骤

用户不需要把所有操作写成一份超长 Prompt。Work 会先理解交付目标，再拆解任务、寻找材料、调用工具并持续推进。执行期间可以补材料、回答问题、调整方向，也可以在关键动作前要求它暂停。

OpenAI 特别强调“work for hours”。这句话描述的是任务形态：上下文和执行状态可以持续更久。它没有承诺 agent 连续跑几个小时仍然保持零偏差。任务链一旦变长，错误传播、权限等待、工具失败和材料过期都会累积。

生成可继续编辑的成品

Work 第一批重点交付物包括文档、演示文稿、电子表格、报告、项目计划和 Sites。

官方示例里，用户可以把研究材料和 campaign template 交给 Work，让它先找出缺失信息，再生成 launch brief，并把确认后的内容改成三个市场版本。整个过程围绕同一个结果继续推进，不需要把每一步复制到另一个工具。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALT9Vgd26CMaem8drrSxdUmiaPuibfic7rhQwibhChOD6GFoTRaHiaaqHoia7Xt1lWrTRAvZRpA2ywV3iaUZuUl7cvGTS5UaWnGEl1oibHg/640?from=appmsg)

— OpenAI 官方文档截图：ChatGPT Work 生成演示文稿

图源：OpenAI《Get started with Work》。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALQHBKo3iaD6m9BJUtK8qobFiaYtKZrIJcKVMzUZQWu1nqDLrxPDlWoFWvSsUTKG3f76dvO7e9Fic9VNcLiaxcCUFSav3CeiawOTgg5U/640?from=appmsg)

— OpenAI 官方文档截图：ChatGPT Work 生成比较表格

图源：OpenAI《Get started with Work》。

让任务按时间继续运行

Scheduled tasks 支持单次运行、周期运行、事件触发和变化监控。一个项目更新可以每周自动读取 Slack 与 Drive，刷新议程、决策、阻塞项和负责人，最后把草稿交给人审。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALQuZ8ANWsz2NedRMV0udTmGlg5fKCR4Mazfg0pmbZzpibLKwzkZC3fNzaYfOc0ktdAfpU1zbATdpe5cg83cP88yPqGXe1Fg8MSk/640?from=appmsg)

— OpenAI 官方文档截图：在 ChatGPT Work 中设置周期更新

图源：OpenAI《Get started with Work》。

定时任务让 Work 进入了轻量业务自动化的范围。稳定性也会在这里接受现场考验：无人值守时碰到空数据怎么办，插件超时要不要重试，连续两次没有新内容是否应该停止，写入失败从哪一步恢复。这些细节决定它能否从 demo 进入生产。

03

MODEL RUNTIME

### GPT-5.6 是这套系统的推理底座

ChatGPT Work 首发接入 GPT-5.6 家族：

• **Sol** 面向复杂研究、编码、Computer Use 和安全任务。

• **Terra** 在能力、速度和成本之间取平衡，适合日常工作。

• **Luna** 处理轻量、高频和批量任务。

默认 Power 设置使用 Sol 和 medium reasoning。

GPT-5.6 的 API 版本公开了 105 万 token context window，以及 web search、file search、hosted shell、Computer Use、MCP、skills 和 tool search 等工具能力。它还加入 Programmatic Tool Calling、persisted reasoning、显式 prompt caching、max reasoning 与 multi-agent beta。

这些参数解释了 OpenAI 为什么能把 agent 的工作链拉长。它们不能直接换算成 ChatGPT Work 每个任务的实际额度。产品层还要经过项目权限、检索策略、工具返回、历史上下文、账号计划和服务策略，OpenAI 没有公布 Work 单任务的固定有效上下文。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALSr7yDibZia6CtPEHZ1w4LeMH2QFLf9F18jHtuveiab2ianictibJw2zahQa41uT1cdrkefEibrMNoD6uqm85yJvOh9Ye6EBdBRZ06lNM/640?from=appmsg)

— OpenAI 官方文档截图：ChatGPT Work 插件库

图源：OpenAI《Get started with Work》。插件把 Work 接入文件、消息与业务系统。

04

BOUNDARIES

### 它离“虚拟员工”还有多远

我更愿意把现阶段的 ChatGPT Work 看成一个 **带执行能力的数字工作台** 。

它适合接手资料密集、步骤明确、产物可检查的工作。比如把访谈和调研做成一份内部汇报，清洗几张表后给出决策比较，或者定期从多个项目源汇总周报。这些任务有清楚的输入，也能在最后打开文件逐项验收。

风险集中在四个位置。

Prompt injection 会进入工作链

agent 读取网页、邮件、文档和第三方工具返回时，恶意内容可以伪装成指令，诱导它泄露数据或执行越权动作。OpenAI 的 MCP 安全文档明确提醒：即便是只读工具，也可能通过返回内容设计数据外传路径。

GUI 操作比 API 更脆

Computer Use 能覆盖没有 API 的尾部场景，也会受到窗口变化、登录状态、页面改版和错误点击影响。结构化插件可以返回对象 ID、错误码和读回结果；视觉点击很难提供同等级别的确定性。

长任务会放大状态漂移

一次错误检索可能进入后续分析，一次错误写入可能污染下一轮数据。任务运行时间越长，越需要明确的 source、observed\_at、停止条件、重试上限和 readback。

企业审计目前还有缺口

OpenAI 当前的 Compliance Logs Platform 会记录用户 Prompt 和 agent response。官方管理员 FAQ 同时写明，它还不追踪文件、动作或 tool calls，日志默认保留 30 天。

对于受监管业务，聊天记录远远不够。企业需要知道 agent 读了哪个文件、调用了什么工具、修改了哪条记录、谁批准了分享动作、最终结果能否回滚。这部分仍要由源系统日志、插件审计和企业自己的控制面补齐。

05

MARKET

### 竞争已经打到执行层

Claude Cowork 是 ChatGPT Work 最直接的对手。Anthropic 把 Claude Code 的 agent 架构带到知识工作，支持本地文件、subagents、长任务、专业文档、表格、演示和定时任务。两家走的是同一条路线：先在代码世界训练 agent 的执行能力，再把 runtime 扩展到整个办公桌。

Google 和 Microsoft 手里有另一种优势。

Google Workspace Studio 能直接调用 Gmail、Drive、Chat、Docs、Sheets 和 Slides，Workspace Intelligence 又把组织邮件、文件、项目和协作关系变成实时语义上下文。Microsoft 365 Copilot 则在 Word、Excel、PowerPoint 与 Outlook 内完成原生编辑，沿用既有的权限、敏感标签、版本和合规体系。

OpenAI 的强项是横向：本地文件、Web、插件、MCP、开发环境和各种交付物可以放进同一个 agent runtime。Google 与 Microsoft 的强项是纵向：它们已经掌握企业日常工作的原生文件、身份和数据关系。

接下来两年的办公 agent 竞争，不会只比模型答题分数。谁能稳定读取正确材料、获得最小权限、生成可继续编辑的成品，并在写入后留下完整证据，谁才有机会成为工作主入口。

06

CANARY

### 先拿三类任务测试

如果你的账号已经出现 Work 入口，可以先跑三个 canary：

1

把一组非敏感研究材料做成 8 页内部汇报。

2

清洗一组表格，生成带公式和推荐结论的比较表。

3

每周读取 Slack 与 Drive，只生成项目周报草稿，不自动发送。

不要先看它调用了多少工具，也不要被“运行了两个小时”打动。应该记录的是：最终文件能不能用，人工修正用了多久，数字和引用错了多少，权限有没有越界，失败能不能从原阶段恢复，外部写入能不能通过 readback 证明。

我的判断很明确：ChatGPT Work 会把大量 AI 使用习惯从“问一句、答一句”推向“给目标、交付结果”。它距离稳定的虚拟员工还有一段工程路，已经足够改变我们分配工作的方式。

先把它当作一个执行团队来管理：给清楚的材料、权限、停止条件和验收标准。

然后检查它交回来的每一件东西。

07

SOURCES

### 官方资料

• OpenAI What's new：https://learn.chatgpt.com/docs/whats-new#take-on-ambitious-work-with-chatgpt-work

• Get started with Work：https://learn.chatgpt.com/docs/get-started-with-work

• ChatGPT Work Admin FAQ：https://learn.chatgpt.com/docs/enterprise/work-admin-faq

• GPT-5.6 model guide：https://developers.openai.com/api/docs/guides/latest-model

• Codex / Work pricing：https://learn.chatgpt.com/docs/pricing

• Computer Use：https://learn.chatgpt.com/docs/computer-use

END

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过