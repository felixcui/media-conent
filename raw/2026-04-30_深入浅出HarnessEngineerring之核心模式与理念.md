# 深入浅出Harness Engineerring之核心模式与理念

**作者**: 张碧泉

**来源**: https://mp.weixin.qq.com/s/8PwDQSX7ZX6HdDiW-H9Dzg

---

## 摘要

文章介绍了Harness Engineering的六种核心模式：持久化指令文件、作用域上下文组装、分层记忆、做梦整理、渐进式上下文压缩以及工作流与编排（含探索-规划-行动循环、上下文隔离子智能体和分支-合并并行），这些模式通过结构化上下文、任务拆解和记忆优化来提升AI智能体的处理质量和可控性，但每种模式均伴随维护成本、信息损失或流程变慢等代价，强调需要在效率与灵活性之间进行权衡。

---

## 正文

张碧泉 张碧泉

在小说阅读器读本章

去阅读

关注腾讯云开发者，一手技术干货提前解锁👇

## 01

Claude Code

1.1 持久化指令文件

没有这个文件时，每次对话都像从头开始，相同的规则和错误可能反复出现。

代价：文件需要随项目更新维护，否则可能误导智能体。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr67xxbnop6SH8C0zia5F3Sh1XpvEbjGMTnM2yygCDoGSLUua7C0Ric8bakHxkNgPgAicqXqYOvPekgtN6pVZ17FUiciaWy5hxgPibtsw/640?wx_fmt=png&from=appmsg)

1.2 作用域上下文组装

将指令按不同范围（如组织、项目）拆分，让智能体能动态加载最相关的规则。

代价：规则分散在多个文件，可读性变差，且不同范围规则可能冲突。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4ZictPgibv8ZL43z66zdRnNEHsrGSoHJ56t58NuHjicyjE7wdg0bFibib8GmQYjQJ6EDlHEL79SsOVafIrkic8C8kkzM7BJMTooAwicU/640?wx_fmt=png&from=appmsg)

1.3 分层记忆

将记忆分为三层：常驻的精华摘要、按需加载的细节、仅支持搜索的完整历史，以节省Token。

代价：实现更复杂。需设计信息如何分层、流动，并确保索引与实际数据同步。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr7Agia3EkAiaO7XqJ3CasiatIYub3n2ylTsDM9c66rflyxqLCicCEYWMVMVzNTZbF1f7zufKmdczFTAB0dibWkib1mMx6s51RgoPUnia4/640?wx_fmt=png&from=appmsg)

1.4 做梦整理

定期在后台对记忆进行去重、清理和重组，类似“垃圾回收”，以保持记忆整洁有效。

代价：整理本身消耗资源，且可能误删有用信息。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr40aosdqjglguhTpWGjpbQLdlIiahcIXfPicyntakFjmT6iaVqQQnmNncq6adicLnNJJRsIKczbibwPcIQMgibrnb9RMjfx9x4ib5VRD8/640?wx_fmt=png&from=appmsg)

1.5 渐进式上下文压缩

新的对话保留细节，稍旧的做轻量总结，更早的则压缩成简短摘要，适合长对话任务。

代价：压缩必有信息损失。后续需要细节时，智能体可能会“编造”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr6GyYAdamnmX2VjkZ7Bl2EX4r4AJcNJr2fzIM4omgyKqQ8wFbm6LdHAUau4epabjdVQuGUej5W0xRabl3Q9JO8HMDVcZJbpYXY/640?wx_fmt=png&from=appmsg)

1.6 工作流与编排

这类模式核心是“分离”，通过拆解任务流程来提升复杂任务的处理质量和可控性。

探索-规划-行动循环

严格分为三步：只读探索、与用户对齐的规划、拥有写权限的执行，避免盲目操作。适用于不熟悉的代码库或复杂修改。

代价：流程更慢，小任务会显得“笨重”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr4Riaujibc9g2oW1cQtSOyDM8794Pdb8rQzksGpTic2icS4zibl1BEFZUeUeIrvu5OiapjsHnIMo4ZddCOMDe51ibOztuxbb56NgCZ0TM/640?wx_fmt=png&from=appmsg)

### 上下文隔离子智能体

为不同阶段（如调研、执行）创建拥有独立上下文和权限的子智能体，防止信息相互污染。适合长会话、多阶段任务。

**代价** ：需要额外协调信息传递，传多或传少都有问题。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4bUaJHLiaJnAKLTlpNPERWk5YqEmlmlLtMJlcUH6TP1PsVfxUkGic4s1wY50XFy85vdDedrbHqe1q1xRj5VME7VckwlrWGS9qjI/640?wx_fmt=png&from=appmsg)

分支-合并并行

将可并行的子任务分发给多个在独立环境中工作的子智能体，最后合并结果，以提升效率。

代价：合并更复杂，处理代码冲突的难度增加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr57E279qAtVx9MjUdO7jDbzWMhReFgfS6uq4vQgsrs7pjkgdibL2AbpduPKLZmGxGgzXCLltl5OszYH6iaUUyBWMDibmjiclib5uxicI/640?wx_fmt=png&from=appmsg)

1.7 工具与权限

这类模式关注如何安全、高效地管理智能体的能力。

渐进式工具扩展

开始时只提供最必要的工具，复杂工具按需动态加载，降低智能体的选择成本和出错概率。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4QmYhQAqwIZVZuXvEF64toAfVib5Ce2TC3dhaUDS3J8gRnibiaELKgutM1njYRL2VoeYMsQ2o0SQNoPhE4ic3cwzlDMmbxO38Vps0/640?wx_fmt=png&from=appmsg)

命令风险分类

根据命令类型、参数和影响，自动评估其风险等级（安全、有风险、危险），并采取自动执行、请求确认或直接拦截等不同策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr53an4dOaf1abvoQ8FJYEhMTKypicmwkuRuOhZgtbpPy9HesXibbPCibTWMKP853JParo3UkmdOicHickEZIBLwwx9jHYvKyuQoknZo/640?wx_fmt=png&from=appmsg)

单用途工具设计

将常用操作（如读文件、搜索）封装为专用工具，而非依赖通用Shell命令，以提高可理解性、可审查性和权限控制粒度。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4tz2hhcsEPcI7iaFibGoEiaYVXN50OrwDibzTkLwAZDzLrSJibwI5mhLdNvHQ4Td6gibc9RGHNQuhPgd2SPuibCibGib5lxeFfNtsYnkH4/640?wx_fmt=png&from=appmsg)

1.8 自动化

确定性生命周期钩子

在智能体生命周期的关键节点（如会话开始、工具调用后）自动触发预设动作（如代码格式化），由系统确保关键流程被执行，不依赖可能被模型遗忘的指令。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4z97QkZbicekvahnFqnC0mJp24M0HnFI2JK2Sic0pFuxQDlbIYDAUqElYeibLhspYjI0FWM1Z6GnFZtnSvVQtrEJfeUqKMP7XeTI/640?wx_fmt=png&from=appmsg)

## 02

Claude Managed Agents

2.1 宠物与牲畜基础设施哲学

- Session（会话）是宠物：精心培育、持久保存、不可丢失。
- Harness（控制器）和 Sandbox（沙盒）是牲畜：可以随时创建、销毁、替换。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr518ACnyU4p2lr1CtVr7e3CatNYkHskEfcAUOB4BL3WicAD0RJLAxFfDOOHyKLmdkWceziaPLXo7ibawl8ibCW18w8gzhWKFSciaOsE/640?wx_fmt=png&from=appmsg)

2.2 智能体三件套解耦

一个智能体由三个核心组件构成：

1. Claude（大脑）：负责推理和决策。
2. Harness（双手）：驱动运行循环，调用Claude API并将工具调用路由到执行环境。
3. Sandbox（工作台）：Claude在其中编写代码、编辑文件、运行命令的隔离环境。
![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4palszInQxwktbo2EZJjibiaiaYDHvmGNKqdIvjcIAsQgp4YCazVEiaI5S3KvxdCBeKgiaUwcuBdVa3JTaWUzyAt40ibIXc6043AyAY/640?wx_fmt=png&from=appmsg)

Session：不可变的事件流

Session核心接口只有两个：记录事件（ `emitEvent()` ）和读取事件(getEvents())。它是只追加的日志，天然支持重放和状态恢复，赋予智能体容错能力。

Harness：驱动循环

Harness是控制中心，它执行一个循环：从Session取上下文 → 调用Claude → 记录响应 → 如有工具调用则路由到Sandbox执行 → 记录结果 → 循环。Harness本身无状态，所有状态都在Session中，因此可随时替换或重启。

Sandbox：隔离的执行环境

每个Sandbox完全隔离，有自己的文件系统、进程和网络。关键特性是可隔离、可重建、可扩展。

核心安全设计：凭证永不进沙盒

采用保险库(vault) + 代理(proxy)架构：

所有第三方凭证存储在独立的保险库中，Harness和Sandbox都无法直接访问。

当需要调用外部工具时，通过代理从保险库按需获取凭证并执行请求。凭证始终不会暴露给Sand盒中的代码。

优势：遵循最小权限原则，所有外部调用可审计，凭证可统一轮换。

2.3 多智能体协作模式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr72LvAuwYDtJLXXtzz8icR3th3Pnvudb1TxgrtLN2fJoOibcQG52cG8E51N5hx8b5ESGRWuzdgAhSu1lic1HOR6lyxQVrLODJJs5o/640?wx_fmt=png&from=appmsg)

得益于三组件解耦，自然支持多种协作模式：

- 多脑一手：多个Claude实例共享一个Sandbox。适用于多角度分析同一份代码（如安全审查+性能优化）。
- 一脑多手：一个Claude实例控制多个Sandbox。适用于需在不同环境（如Python和Node.js）中同时执行任务。
- 多脑多手：多个Claude实例各有自己的Sandbox，通过共享Session协调。适用于最复杂的多步骤任务。

2.4 上下文工程：保持大脑专注

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6m1iblKGhnMcichGqF3UIiay42EznWicCpofOlNLYajC7u7wia1wDgrBlXCuFd3nEspXpRUiatnNVgUS08lgA4N3zCjHQeJ3wvqo2fc/640?wx_fmt=png&from=appmsg)

为管理长任务中的上下文窗口，引入多种技术：

- 上下文压缩：当上下文窗口将满时，将早期对话压缩成总结，腾出空间。原始数据仍完整保留在Session中。
- 记忆工具：让Claude能主动将重要信息写入持久存储，后续可主动检索，类似人类记笔记。
- 上下文裁剪：在发送给Claude前，智能地裁剪不相关的上下文，只保留当前任务需要的部分。

三者协同，确保Claude始终获得最相关的上下文。

2.5 性能优化：显著降低响应延迟

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr7EVZfn5wPzMP0KiayY99LJkduKEopuld0LticgEHpiaiba2rv3I8IpkyiamayIxPibE7jwwrxLROEvCERmWhQ7vPfj48A0DZkI8Dic3k/640?wx_fmt=png&from=appmsg)

关键在于将大脑（推理）从容器（Sandbox）中解耦。解耦前，每次推理都需等待Sandbox容器完全启动。解耦后，编排层从Session日志拉取事件后，推理可立即开始，使得首Token延迟降低60-90%。

## 03

Hermes：会进化的智能体

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr5jVXlSNuib1gibb1DxILBu0f0IXovXNia6ibPuPHzAuQ31m1g8UtvVuiaVOpb12nianic70WPVQEFIIZPIwxLn1Nmg93OjACfjwMSPEg/640?wx_fmt=png&from=appmsg)

3.1 五段式循环

规划 → 执行 → 观察 → 学习 → 适应

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr7fmGL1MrF0x65rjAiaKPq1cuIV7HhuIPoVibibUYcDdKHRkSJcRDVKYQqbsUKmDsV1WdibOmTKBcjibB9C4WyyMG9Aib3baV5vlQMc4/640?wx_fmt=png&from=appmsg)

3.2 五层记忆架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr7RUUiaq7Hiak5RZsiaZKicHaZ96EQibibSccPWyQW49TibQdfzp1CkrJKibZLvcLTLOd08EEC0ZbZ6Om2GiawAvAKBeqrEibHRt8giaQZbGA/640?wx_fmt=png&from=appmsg)

L1 短期记忆（便利贴）：

当前对话的临时信息。

L2 技能手册（肌肉记忆）：

完成复杂任务（如涉及5次以上工具调用）后，自动生成SKILL.md文件，记录完整的解决步骤，形成可复用的流程。

L3 知识库（语义记忆）

如何理解语义记忆？

简单讲就是利用向量存储这个技术，来实现模糊检索，原理是：即使字面不同，但语义相近的文本，其向量在数学空间中的位置也很接近。

举例查询进度报告技能：

“进度报告” vs “项目周报” → 相似度 0.92（很高！）

“进度报告” vs “预订机票” → 相似度 0.15（很低）

返回结果：返回最相关的技能：生成项目周报.md

L4 对你的了解（用户建模）

首先什么是黑格尔“辩证式”：

黑格尔“辩证式”就是AI内部在讨论：“我对用户的理解对吗？新证据说明了什么？怎么更新我的理解？”

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6Pvkgbe67YISScDpy8pLnOjHXpxQbEXnVwPSCC1A76k5uV55a8QQHLJqma00ebFZ2jN0joDs2cy4Ixxiav4OUBBgicQY02g7bDg/640?wx_fmt=png&from=appmsg)

越来越懂你的朋友：

不是一次判断就定终身，允许你改变、允许情况复杂，通过不断观察、思考、调整，越来越懂真实的你。

这就像最好的朋友：知道你“通常”怎样，但也理解你“有时”会例外

比喻：

- 旧版本：“林总喜欢喝美式”
- 新发现：今天林总点了拿铁
- 冲突：旧版本 和 新证据矛盾
- 解决方案：不直接覆盖成“喜欢拿铁”，而是升级：
- “林总平时喝美式，但周三下午会换拿铁”

L5 工作日志（长期档案）

FTS5全文检索+LLM摘要：跨会话搜索历史对话，永久存储

- LLM 摘要（写读书笔记）：每次长谈后，AI 会自动用一两句话总结核心结论，写在笔记本的“摘要区”。
- FTS5 全文检索（给笔记本加智能目录）：AI 会给笔记本的每一页（包括详细对话和摘要）的所有关键词，自动生成一个超快的电子索

\-End-

原创作者｜张碧泉

感谢你读到这里，不如关注一下？👇

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95UnhD9f7ia4T3ufXM1liaxxffiaEy41n0icohEC2qDS05icapaN4iaTVfsClibPRmqOjNW6q33PZicAVoSOg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

你对本文内容有哪些看法？同意、反对、困惑的地方是？欢迎留言，我们将邀请作者针对性回复你的评论，欢迎评论留言补充。我们将选取1则优质的评论，送出腾讯云定制文件袋套装1个（见下图）。5月6日中午12点开奖。

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe96Ad6VYX3tia1sGJkFMibI6902he72w3I4NqAf7H4Qx1zKv1zA4hGdpxicibSono28YAsjFbSalxRADBg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

扫码领取腾讯云开发者专属服务器代金券！

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4nU3obq4B4URKhzJMmibw1uR1ZehOtyeel5hYevARgDqdKxqXvtzclLhu7g28g6PBib8M2uaQegic6MrCdBic0SdHh4XUQODQkmKk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe979Bb4KNoEWxibDp8V9LPhyjmg15G7AJUBPjic4zgPw1IDPaOHDQqDNbBsWOSBqtgpeC2dvoO9EdZBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95pIHzoPYoZUNPtqXgYG2leyAEPyBgtFj1bicKH2q8vBHl26kibm7XraVgicePtlYEiat23Y5uV7lcAIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

继续滑动看下一个

腾讯云开发者

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过