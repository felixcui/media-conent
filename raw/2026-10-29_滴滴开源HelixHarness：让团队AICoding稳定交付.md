# 滴滴开源 HelixHarness：让团队AI Coding稳定交付

**作者**: 金融技术

**来源**: https://mp.weixin.qq.com/s/N2AXnzXKYtaNy3rO9dFnKw

---

## 摘要

滴滴金融技术团队开源团队级 AI Coding 工程化基础设施 **HelixHarness**（源自内部 OpenHarness，GitHub: didi/helixharness），针对规模化落地的四个痛点：工程化支撑不足、过程不可观测、迭代缺评测、框架与团队不适配。核心做法是用 **Knowledge / Harness / Specs / Hooks** 四部分把工程知识结构化，并用标准化命令串起「初始化 → 方案设计 → 开发执行 → 结果归档」的端到端流程，同时记录工具调用与返工路径、支持持续评测和团队自定义扩展。已在滴滴内部 10 余个部门、上百个业务模块落地。

---

## 正文

金融技术 金融技术

在小说阅读器读本章

去阅读

## 一、前言

2025 年，随着大模型技术的持续突破，AI 迎来了新一轮发展热潮。尤其在软件研发领域，AI Coding 正在迅速改变开发者的工作方式。

从最初的代码补全、辅助编程、理解需求、设计方案、甚至执行测试，AI 已经开始参与越来越多的软件研发环节。但在真实的软件工程环境中，开发者需要解决的远不止代码生成，如何让 Coding Agent 理解真实项目、遵循团队规范，并在复杂的工程环境中稳定完成研发任务， **滴滴金融技术团队基于内部真实场景的探索实践，正式开源面向团队的 AI Coding Harness - HelixHarness。**

**项目地址** ：https://github.com/didi/helixharness

## 二、背景：从真实工程中淬炼出来的工具

**HelixHarness 最早起源于滴滴金融技术团队内部的 OpenHarness 项目。** Helix 意为“螺旋”，象征持续演进、循环迭代与不断向上的成长过程。正如 DNA 双螺旋承载着生命的遗传信息与进化密码，HelixHarness 也希望通过工程知识的持续积累、真实研发实践中的观测与评测反馈，不断优化 AI Coding 的工程化能力，让每个团队都能构建并持续进化属于自己的专属 Harness。

最初，我们也是从个人使用 AI Coding 开始的。借助 Coding Agent，开发者能够更高效地理解代码、完成开发任务。随着 AI Coding 的深入应用，我们开始思考：面对真实工程中复杂的业务知识、技术架构和研发规范， **如何让 AI 从提升个人开发效率，进一步走向支撑团队规模化的研发交付？**

**带着这一思考，我们开始将 AI Coding 引入团队中真实业务研发中，** 随着实践的深入，项目逐步从单个团队走向滴滴内部更广泛的推广应用， **目前已在公司内部推广至 10 余个部门和团队，累计应用于上百个业务模块。** 在企业团队的规模化实践中探索它的能力适用性，也逐渐发现了像“工程化支撑”、“过程可观测”、“能力评测”和“团队适配”等方面的挑战。

- **工程化支撑不足。** AI 缺乏对项目知识、业务逻辑和工程规范的完整理解，也缺少贯穿需求、开发、验证的统一工作流程，开发者仍需投入大量精力引导 AI。
- **过程数据不可观测。** AI 开发过程中的工具调用、代码修改和返工路径缺乏有效记录，难以准确分析研发效率与问题根因。
- **框架迭代缺少评测。** 知识、规则、Skills 和工作流持续迭代，但缺乏统一的评测体系，难以客观衡量改进效果。
- **框架与团队不适配。** 不同团队的技术栈、工程规范和研发流程存在差异，通用 Harness 难以直接适配，重复定制成本高、经验复用难。

经历这些实践后，我们逐渐意识到，AI Coding 在企业团队中面临的核心挑战，已经不只是如何让 AI 写出更好的代码，而是 **如何让 AI 在真实工程环境中，更稳定、更可控、可衡量地完成研发任务。**

这也让我们开始重新思考：能不能在现有 Coding Agent 之上，构建一套工程化基础设施，既能让 AI 理解项目、遵循团队规范，又能记录执行过程、评估实际效果，并支持不同团队根据自己的需求持续扩展？

**HelixHarness 正是在这样的背景下逐步诞生的。**

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSopJiamibWruUGPh4nmdfZ6zeDAx2icicQHBmUy14rgR0EoNiagKTbt23cmWHMcibYic9IJMAlXxycnMFTcW4eQmNRSiahvgBicnnju1MYM/640?wx_fmt=png&from=appmsg)

HelixHarness 整体架构与工程化能力

## 三、HelixHarness 的设计和思考

### 3.1 核心工作流设计

在工程开发场景中，一个需求从理解、方案设计、代码开发到测试验证，往往需要经过多个相互关联的环节，所以我们基于内部真实研发项目的实践经验，将日常研发流程中的关键环节抽象为一套标准化研发命令，贴合项目初始化、需求方案设计、开发执行、结果验证和归档沉淀等阶段。让 Coding Agent 在工程约束下有序完成任务。

#### 通过标准化命令，组织端到端研发工作流

HelixHarness 将研发过程拆解为初始化、方案设计、开发执行和结果归档等阶段，并通过统一命令驱动执行。

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSphMonpNCRRwicGHUXDJ6icL6CUibhmMicHqzmSGvzosO0kicZ7ibQzHoSP0u4dYbGoxibiaUm5zyWAhPh99xYxF6ghRXkzFCXefgjDicbI/640?wx_fmt=png&from=appmsg)

通过标准化命令启动工作流

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSqVIXGN6xo4DMriaCe3jK3mxACjdLMHlUCTG6Or4ZKlj6H98ichjViaUgxuW2khLMlJo7Y6bjSJBRIRe8jJJcWIIoVa3Co4Juh0fg/640?wx_fmt=png&from=appmsg)

初始化、方案设计、执行开发和归档沉淀

### 3.2 工程上下文管理：让项目知识成为可复用资产

在真实企业团队的日常研发中，项目知识往往分散在代码仓库、技术文档、工程规范和开发者经验中。这些知识既包括系统架构、模块职责、业务逻辑，也包括代码规范、安全要求和历史设计约束。如果完全依赖开发者在每次对话中补充，不仅增加 AI Coding 的使用成本，也难以保证不同开发者、不同任务之间的一致性。

因此，HelixHarness 将工程上下文进行结构化组织，通过 **Knowledge、Harness、Specs、Hooks** 四个部分，为 Coding Agent 提供相对完整的工程环境。

#### 通过标准化目录，将工程知识沉淀到项目中

HelixHarness 将工程知识、规范约束、需求契约和检查规则统一组织在项目目录中，与业务代码共同维护。

通过标准化目录结构，让原本分散在文档和个人经验中的工程知识，转变为可管理、可复用、可持续更新的项目资产。

```
business-project/           业务仓库根目录
├── src/                    业务源码（示例）
├── tests/                  业务测试（示例）
├── config/                 业务配置（示例）
├── docs/                   HelixHarness 上下文与交付工件
│   ├── harness/            工程约束与索引
│   ├── knowledge/          项目知识与索引
│   ├── specs/              需求规格、任务及验证工件
│   └── hooks/              检查规则
└── AGENTS.md               宿主上下文入口
```

#### 通过四层工程上下文，让知识真正参与 AI Coding

工程知识的结构化存储只是第一步，更重要的是让这些知识能够在 AI Coding 的实际执行过程中发挥作用。

HelixHarness 通过四层工程上下文，将项目知识、工程约束、需求契约与自动化检查机制相结合，并融入从需求分析、方案设计到开发验证的完整工作流。让 Coding Agent 在理解项目的基础上，遵循团队规范，明确开发目标，通过检查保障质量，最终完成交付闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSr5iaRzYqicvZr4gjYblOWEPCzQIicOvW7xWiagOuibEJMT7Wga3yD5yibxiaS2yyn8ibiav3ypa0x7aicRYJskWyQqsZaKnz8B3yWfSz6EU/640?wx_fmt=png&from=appmsg)

Knowledge、Harness、Specs、Hooks 四层工程上下文

### 3.3 可观测、评测、自进化

随着团队持续使用框架，会不断积累真实研发过程中的执行数据、问题反馈和工程经验，Knowledge、Rules、Skills、Workflow 等框架能力也需要随之持续优化。这就需要我们是针对 HelixHarness 自身的工程化能力不断进行迭代升级，包括项目知识、工程规范、技能工具和研发工作流等，让框架更好地适应团队的实际研发需求。

这也带来了一个关键问题： **每次对 HelixHarness 进行改造升级后，我们如何判断这些改动是否真正有效？是否会引入新的问题？**

举 2 个例子来说，例如我们调整某个 Rule，它可能在规范 AI 行为的同时可能引入额外的执行约束；或者我们在框架中新增一个 Skill，虽然可能提升特定场景下的开发效率，却未必适用于其他研发场景。

**因此，HelixHarness 希望建立一套基于真实工程数据、面向框架能力升级的可观测、可评测、可持续进化机制，让每一次框架调整都有数据依据、效果验证和风险控制，而不是单纯依赖经验判断。**

其整体思路是：

> 可观测 → 形成假设 → 候选修改→ 统一评测 → 受控采纳 → 持续迭代

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSqGNRZ8OA8ZYyp72G5tnicB480TibbvhQ1yNll5iaf9OPuiahKYw0t8cpibibib0KpEtw3XyiaUVkra1WK1YkTm7SvAviazGv6cicZZVe2Rc/640?wx_fmt=png&from=appmsg)

可观测、统一评测与持续进化闭环

## 四、与同类框架的差异

当前，AI Coding 生态中已涌现出丰富的工具与框架。有的项目能提供代码理解、任务规划和工具执行能力；有的项目提供 Skills 和 MCP 等机制支持能力扩展；还有的项目从开发流程和任务规范等方向提供了各自的解决方案。

我们框架的核心定位，是在现有 Coding Agent 的能力基础上，进一步组织真实工程所需的项目知识、团队规范、研发工作流以及验证评测机制。HelixHarness 希望在已有生态基础上，重点解决工程能力如何在团队中统一组织、复用和持续改进的问题。 **HelixHarness 不仅提供完整的 AI Coding 工程化基础能力，更支持不同企业团队结合自身的业务知识、工程规范和研发流程，持续构建和演进属于自己的专属 Harness。**

## 五、未来规划：构建持续进化生态

HelixHarness 计划分阶段扩展 Agent 支持、开放工作流程配置，并围绕真实企业团队研发场景持续迭代，让框架更好地适配不同团队的开发工具与研发方式。

### 5.1扩展 Agent 支持

在现有支持的基础上，调研开发者使用的其他 Agent，并推进相应的适配开发，逐步覆盖主流 Agent，让更多团队能够在熟悉的开发工具中使用 HelixHarness。

### 5.2支持工作流程自定义

针对不同企业团队在研发流程上的差异，提供工作流程顺序的配置能力。团队可以根据自身的流程要求调整工作流，使 HelixHarness 更好地适配企业团队实际的研发过程。

## 六、写在最后

希望通过这篇介绍，大家对 HelixHarness 的设计思路、核心能力，以及它如何帮助企业团队打造专属 Harness，有了更清晰的认识。如果你的团队正在探索 AI Coding 的落地方式，希望让 AI 更好地理解项目知识、遵循工程规范，并融入日常研发流程，HelixHarness 可以作为一个值得尝试的选择。

也欢迎大家结合自己的业务场景和使用体验，与我们探讨交流。无论是使用中的疑问、希望补充的能力，还是已经验证有效的工程经验，都欢迎分享。期待和更多开发者一起，在真实研发实践中不断完善 HelixHarness，让它更好地服务团队的实际需求。

**项目地址：**

https://github.com/didi/helixharness

![](https://mmbiz.qpic.cn/mmbiz_png/bVeicaqGia4S4eiapQIRd3TDuzeZAf6c0ux8rH0gvib7mwgSibvbcXuIXvicYRcKSokoDpAGdocKzzMCO2xWMIpOp0pg/640)

往期推荐

- [滴滴技术团队的三场专题分享](https://mp.weixin.qq.com/s?__biz=MzU1ODEzNjI2NA==&mid=2247575548&idx=1&sn=cc4d557c6165632ec973dbdbc0a7a197&scene=21#wechat_redirect)
- [从真实问题出发，他们如何成长为全球开源社区核心成员？](https://mp.weixin.qq.com/s?__biz=MzU1ODEzNjI2NA==&mid=2247575506&idx=1&sn=79203aaf729b082187f9d06ccc281365&scene=21#wechat_redirect)

点击阅读原文，跳转项目

阅读原文 不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过