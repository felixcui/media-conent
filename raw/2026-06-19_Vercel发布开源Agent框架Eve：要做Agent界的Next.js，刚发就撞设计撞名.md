# Vercel发布开源Agent框架Eve：要做Agent界的Next.js，刚发就撞设计撞名

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/tuI9ocZdrBXbug87O6FUSA

---

## 摘要

Vercel发布开源AI Agent框架Eve，定位为“Agent界的Next.js”，旨在解决Agent底层能力重复搭建的痛点。其核心理念是“Agent即目录”，通过约定文件夹结构自动串联模型与工具，无需编写胶水代码。Eve内置了持久会话、隔离沙箱、人工审批、标准化工具连接、多渠道运行及完善的可观测与评估等生产级能力，致力于为开发者提供高效、规范的Agent开发标准。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

一年前，Vercel 的部署中只有不到 3% 来自 AI Agent。现在这个数字是 29%。不是 Demo，是生产环境。

所以 Vercel 把自己内部用来跟上这个节奏的框架开源了。名字叫 Eve。用他们自己的话说：Next.js，但给 Agent 用。

**Agent 就是目录**

Eve 最核心的设计理念是「Agent 即目录」。一个完整的 Agent 只需要一个按约定结构组织的文件夹：

```
agent/
  agent.ts                   # 配置运行的模型
  instructions.md            # Agent 的身份和规则
  tools/                     # 可调用的工具
    run_sql.ts
    post_chart.ts
  skills/                    # 内置的知识库
    revenue-definitions.md
  subagents/                 # 可调用的子 Agent
    investigator/
  channels/                  # 接入的渠道
    slack.ts
  schedules/                 # 定时任务
    monday-summary.ts
```

不需要写任何胶水代码。Eve 自动识别目录下的所有文件，把模型、提示词、工具、权限串成可用的 Agent。创建一个基础 Agent 只需要两个文件： `agent.ts` 里用一行代码指定模型， `instructions.md` 里写清楚身份和规则，剩下的框架自动完成。

**为什么造这个轮子**

Vercel 在官方博客里说得很直白：过去几年他们内部做了包括 v0 在内的上百个 Agent，但每个团队都在重复搭建一样的底层能力——状态管理、鉴权、日志、沙箱，没有任何复用性。

这和 Web 框架出现之前，所有人都在手搓 HTTP 服务器和路由的状态完全一致。Eve 就是把 Agent 通用的生产级能力全部内置到框架里。

**内置的生产能力**

**1.** **持久执行会话** ：每一步操作都会做 checkpoint，任务可以暂停、崩溃恢复、跨部署续跑，跑几天几周的长任务也不会丢状态，底层基于开源的 Workflow SDK 实现。

2\. **隔离沙箱** ：所有 Agent 生成的代码运行在独立沙箱中，和应用 runtime 完全隔离。支持 shell 命令、文件读写。部署时自动切换到 Vercel Sandbox，本地开发支持 Docker、just-bash 等，也可以自定义适配器对接其他沙箱。

**3\. 人在回路审批** ：任何工具调用都可以配置自定义审批规则。大体积 SQL 查询、数据写入等高危操作触发时，Agent 自动暂停等待人工确认，等待期间不消耗算力，审批通过后从断点继续执行。

4\. **标准化工具连接** ：支持对接所有符合 MCP 协议和 OpenAPI 规范的服务。内置 Slack、GitHub、Snowflake、Salesforce、Notion、Linear 等常用适配器，自动处理鉴权，模型全程不接触凭证信息。

![连接到常用工具的适配界面](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJiblonkqwQXua3khUXTWbgaZBlZAEhCCXolckKxjJQpUeAhwBxPRZmicibTj7mr3n1xmflFWria6PlR4m7z9HtVnG9xgL4Ou7fxNqg/640?wx_fmt=png&from=appmsg)

4\. **一次开发，多渠道运行** ：同一个 Agent 通过添加不同渠道适配器，快速接入 Slack、Discord、Teams、Telegram 等平台。会话支持跨渠道流转——HTTP 触发的告警任务，可以自动在 Slack 开启调查线程。

5\. **内置可观测与评估** ：每次 Agent 运行都会生成符合 OpenTelemetry 标准的链路追踪，所有模型调用、工具调用、沙箱内执行的命令都会被完整记录。同时支持编写评估用例，接入 CI 做回归测试，提示词或模型版本的改动影响在上线前就能发现。

![Agent 运行的链路追踪界面](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ8dNR2s4ROyMkHclAge5uibFMZZbu58E3VGxHJdbDcc9ekoBj75Rdqwzy85PxE9pJancjou32zvcJCNpJzVnbgUC5IWBcqpIjEc/640?wx_fmt=png&from=appmsg)

**扩展能力：加文件就行**

加工具就是在 `tools` 目录加一个 TypeScript 文件，加知识库就是在 `skills` 目录加一个 Markdown 文件，加子 Agent 就是在 `subagents` 目录下再建一个符合结构的子目录。所有组件都会被 Eve 自动加载，不需要手动注册。

Agent 还可以在沙箱内自主编写和运行代码，不需要预先定义所有工具。遇到临时的分析、数据处理需求，自己就解决了。

**开发和部署**

和普通 Vercel 项目完全一致的体验：

- 本地运行 `eve dev` 启动带终端 UI 的开发服务器，实时看到 Agent 每一步的执行动作
- 运行 `vercel deploy` 部署到生产环境，部署不会打断正在运行的 Agent 任务
- 接入 Slack 只需运行 `eve channels add slack` ，框架自动生成渠道配置文件
- 定时任务在 `schedules` 目录下加一个带 cron 表达式的配置文件即可

**Vercel 内部已经在跑的场景**

超过 100 个基于 Eve 的 Agent 在生产环境运行：

- **数据分析师 Agent** ：每月处理超过 3 万次数据查询，全员可在 Slack 使用，查询权限和用户自身权限对齐
- **自主 SDR Agent** ：24 小时自动跟进新销售线索，年运行成本约 5000 美元，带来 32 倍回报，仅需一名工程师兼职维护
- **销售驾驶舱 Agent** ：由 RevOps 团队在无工程师参与的情况下用 6 周搭建完成，Pipeline 覆盖率接近翻倍
- **支持工程师 Agent** ：自动处理 92% 的用户工单，剩余复杂问题自动转人工
- **路由 Agent** ：统一接收所有内部请求，自动路由到对应的专用 Agent

**社区反应**

发布后不到一小时，讨论已经炸开。有开发者指出 Eve 的 API 和核心设计与 Astro 团队前一日刚发布的 Flue 1.0 Beta 高度相似。也有人提到 Eve 将直接和 Mastra、OpenClaw 等现有框架形成竞争。

吐槽和玩梗也不少：有人觉得「一个 Agent 要六个目录还是太多了」，还有人拿 Next.js 的构建速度玩梗——「Eve 部署会不会也要 13 分钟才能构建完」。

最有话题性的是撞名问题：两个月前刚有一款同领域的 AI 编码云环境平台叫 Eva，发音几乎完全一致。EVE Online 的玩家也开玩笑说游戏公司可能会发起诉讼。

**现在就能用**

Eve 已经开放公开预览。运行一行命令即可在一分钟内初始化第一个 Agent 项目：

```
npx eve@latest init my-agent
```

官方文档在https://eve.dev/docs，代码仓库在https://github.com/vercel/eve。

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过