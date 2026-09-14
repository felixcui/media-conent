# 《Deep Agents实战》项目正式发布，一起走向生产级Agent！

**作者**: Datawhale

**来源**: https://mp.weixin.qq.com/s/BfXRjdU02miFDRrBsbm50Q

---

## 摘要

Datawhale团队联合LangChain官方大使沧海九粟发布《Deep Agents实战》开源项目，这是一门基于LangChain/LangGraph生态的中文智能体开发教程，聚焦生产级Agent的工程实践。课程围绕Agent Harness运行骨架，讲解任务规划、上下文管理、工具调用与子Agent协作等核心问题，按认知、核心、进阶、实战路径逐步展开，目前已发布8章正文和2讲准备内容并持续更新。

---

## 正文

Datawhale Datawhale

在小说阅读器读本章

去阅读

Datawhale干货

**作者：Datawhale deepagents-in-action团队**

一、开源初心

随着 Agent 逐步进入真实业务场景，开发者开始面对更多工程问题。长流程任务如何组织、上下文如何管理、多个 Agent 如何协作，这些都需要在具体项目中反复实践。构建生产级 Agent，也因此成为越来越多学习者希望深入的方向。

框架迭代很快，学习资料和示例代码也需要不断维护。我们希望围绕生产级 Agent 开发，整理一套可以持续更新、动手实践的中文教程，让学习者有一条清晰的进阶路径。

为此，我们与LangChain官方大使沧海九粟一起发起了《Deep Agents 实战》开源项目，希望把生产级 Agent 开发中的关键问题拆开讲清楚，并通过课程和可运行示例，帮助学习者逐步完成从 Demo 到真实应用的实践。

二、Deep Agents 实战：系统性的生产级AI Agent开源教程

《Deep Agents 实战》是一门基于 LangChain / LangGraph 生态的智能体开发课程，重点介绍 Deep Agents 的设计思路与工程实践。

课程围绕 Agent Harness，也就是智能体运行骨架展开。它负责组织任务规划、上下文管理、工具调用、子任务委派和执行过程中的状态变化，让 Agent 能够处理更复杂、更长流程的工作。

![](https://mmbiz.qpic.cn/mmbiz_png/zW6S9vt0cSibjegicNUkdEz8OyiarydaQfj0z3JpX2047oicIovdzibZqxOfYWCcv5kLJZljeibg8lpPRicthDxkpoNF4XQE6QtspP881xXzHdFCXg/640?wx_fmt=png&from=appmsg)

```bash
课程网站：https://datawhalechina.github.io/deepagents-in-action/GitHub：https://github.com/datawhalechina/deepagents-in-action/配套视频：https://space.bilibili.com/28357052/lists/7757577?type=season
```

课程配套提供在线文档、示例代码、讲义 PDF 和视频内容，帮助学习者边理解原理，边运行和修改代码。

三、项目受众

本项目适合希望系统学习 AI Agent 开发的学习者，尤其是已经运行过简单示例、希望继续深入工程实践的开发者。

如果你正在使用 LangChain 或 LangGraph，可以通过本项目进一步学习上下文工程、任务规划和子 Agent 协作。刚接触 Agent 的同学，也欢迎从准备篇开始，跟着章节和示例逐步上手。

四、学习指南

课程按照“认知、核心、进阶、实战”逐步展开，配有准备篇。目前已发布 **8 章正文和 2 讲准备内容** ，后续持续更新。

**准备篇：搭建开发环境**

使用 AgentSeek CLI 快速搭建模板应用，安装开发辅助 Skills，为后续实践准备好环境。先把项目运行起来，再逐步理解其中的设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zW6S9vt0cS81gFhOpChpnoc9qd6qViaeDSNkLBk5z9vlVa1xQNj9VV2ALgh9exlACfSiaG9RerkX7fNVO0gL2PToBARVKTgYogOZznz0xYAGI/640?wx_fmt=png&from=appmsg)

**认知篇：认识 Agent Harness**

从 Agent Framework 到 Agent Harness，理解 Deep Agents 的诞生背景与设计思路，并动手构建第一个 Deep Agent，建立对整个系统的基本认识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zW6S9vt0cSicbuHyXkOkQhcc3wicnicmrYqoHo4QCzx4gIicope5JMShBgPkaratANLsCGCP1OESm5gkyW2tq9D6B84WDQ0a0ZHFv7BHUMXQPqs/640?wx_fmt=png&from=appmsg)

**核心篇：组织复杂任务的执行**

这一部分将深入虚拟文件系统、任务规划与分解、子 Agent 和上下文隔离，以及异步子 Agent。你将学习如何保存和按需读取任务材料，如何把复杂工作拆给子 Agent，以及如何控制不同任务之间的信息传递。

![](https://mmbiz.qpic.cn/mmbiz_png/zW6S9vt0cSicoJY1rIkHT8KO9EAicFh6cNTOe7kAEkfj3nt5O58KHicsa4icPxryAQ5ic7RQ0sD7RhQxzrBxLlazyTR5iclL9NyQkBE0Eb3gm2iaIg/640?wx_fmt=png&from=appmsg)

**进阶篇：积累可复用的能力**

通过 Skills 将操作流程和专业知识整理为可复用的能力包，再结合长期记忆，让 Agent 在后续任务中使用已经积累的信息。Human-in-the-Loop（人工介入）和沙箱执行也已纳入后续规划，将进一步介绍人工接管与执行环境的管理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zW6S9vt0cSib1s8frKW74LSraPtG2Bt9zCcFYLAyWUrhf8fVU9cibweYbQDgaQ7GPTibCAzssdhN9ntrIVUz5Y4giazp1gfiarnibKncAMuibn78Fw/640?wx_fmt=png&from=appmsg)

**实战篇：构建完整应用，持续更新中**

规划中的实战内容包括实时流式前端、数据分析 Agent、CLI 与生产部署，并将结合 AgentSeek 提供应用模板。我们会在完整项目中串联前面的知识，逐步补齐应用开发与部署环节。

## 写在最后

《Deep Agents 实战》会继续更新课程内容和实践案例，补充更多面向真实开发的主题。欢迎访问课程网站，运行示例代码，也欢迎把学习过程中遇到的问题和实践经验带到项目中。

希望这门课程能帮助你更系统地理解 Agent 的运行机制，并逐步构建出真正能完成复杂任务的智能体应用。

```ruby
开源地址：https://github.com/datawhalechina/deepagents-in-action/
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/vI9nYe94fsGxu3P5YibTO899okS0X9WaLmQCtia4U8Eu1xWCz9t8Qtq9PH6T1bTcxibiaCIkGzAxpeRkRFYqibVmwSw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

开源贡献， **点** **赞** 在看↓

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过