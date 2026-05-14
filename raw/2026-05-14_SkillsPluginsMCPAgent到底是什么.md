---
title: "Skills、Plugins、MCP、Agent 到底是什么？"
author: "宝玉AI"
date: "2026-05-14"
source: "https://mp.weixin.qq.com/s/UJ20_cWYiM0XOTHTYQ1TXg"
summary: "用 claude-for-legal 开源仓库为实例，清晰解释了 Claude 生态四个核心概念：Skills（工作手册/说明书）、Agent（执行主体，含 Subagent 分身和 Scheduled agent 定时任务）、MCP connector（外部数据连接器）、Plugin（将 Skills/Agents/MCP 打包的容器）。"
---

# Skills、Plugins、MCP、Agent 到底是什么？

> 作者：宝玉AI
> 来源：[原文链接](https://mp.weixin.qq.com/s/UJ20_cWYiM0XOTHTYQ1TXg)

有网友问：这个 Claude 一会插件的，一会 Skills 的，一会这个 Agent 的，它他到底想干什么呀？

1. Skills 是技能，领域知识，工作流等等，相当于怎么干好一件事的说明书。

比如 https://github.com/anthropics/claude-for-legal 仓库里有个 skill 叫 nda-review，在 commercial-legal/skills/ 文件夹里。里面是一份 SKILL.md，写清楚：审 NDA 时先比对哪些条款、按团队 playbook 打绿黄红三档、什么情况要升级、输出格式是 Word 修订模式。

它就是一份给 Claude 看的工作手册，本身不干活。

2. Agent 是真正执行任务的主体，除了主要执行的 Agent，通常自定义的 Agent 分两种：Subagent 和 Scheduled agent

2.1 Subagent 是单独派出去干一摊子活的"分身"

举个仓库里的例子：corporate-legal:tabular-review 这个 skill 要对一个数据室里几百份合同做表格化尽调。如果让主对话一份份读，上下文很快爆掉。所以它派 subagent，一个 subagent 负责一份文档，并行跑，最后把结果汇总回主对话。

主 Agent 看到的只是最终表格，中间几百次读取的信息被隔离在外。

2.2 Scheduled agent 是定时自己跑的后台任务

renewal-watcher 这个就是。每周自动扫一遍合同库，把 90 天内到期的合同列出来，发到指定 Slack 频道。你不用记日子，它替你盯。

docket-watcher（盯法院案件动态）、reg-feed-watcher（盯监管新规）都是这种。

3. MCP connector 是把外面的数据接进来的连接器

Skill 写得再好，也得有合同可审。仓库里配了 Ironclad（合同库）、DocuSign（已签合同）、iManage（文档管理）几个 MCP connector。

Agent 通过这些 MCP connector 去读公司真实的合同库，而不是让你手动复制粘贴。

类似地，诉讼那个 plugin 接的是 Everlaw（电子取证）、CourtListener（联邦法院判决数据库）、Trellis（州法院数据库）。换个执业方向，换一套数据连接器。

4. Plugin 是把上面这些打包到一起的容器

commercial-legal 这个 plugin 文件夹里装着：

- 一堆 skill（nda-review、vendor-agreement-review、escalation-flagger……）
- 几个 scheduled agent（renewal-watcher、deal-debrief）
- 一份 .mcp.json，告诉 Claude 要连哪些外部系统
- 一份 CLAUDE.md 模板，用来记你团队的 playbook

你装上这一个 plugin，整套企业合同审查的能力就一次性配齐了。
