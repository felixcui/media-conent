# Obsidian构建个人知识库：基于LLM Wiki打造第二大脑

**作者**: Chen

**来源**: https://mp.weixin.qq.com/s/JnJFinnRrnz5hVd5dNS_7A

---

## 摘要

本文介绍了如何基于LLM Wiki理念在Obsidian中构建个人知识库以打造“第二大脑”。首先，将笔记迁移至本地化的Obsidian中，通过安装Terminal插件并调用本地的Claude Code或Codex工具，实现笔记库内直接使用AI。其次，引入Karpathy的LLM Wiki理念，区别于传统RAG检索，该理念让AI在理解语义的基础上持续维护一个结构化Wiki，将知识沉淀为可复用内容。

---

## 正文

Chen Chen

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/UsUOUEyCK4lpiawnTicjDFXkTSFQGUQtaYRTnH7oACV5jRbibRvbBhdOaOv50cGhuic366Dia0b63ART7q2FytX05cxSoHEZutjjicJZSb05iatqc8/640?wx_fmt=gif&from=appmsg)

最近把我自己积累的专业笔记，都汇总到了Obsidian里面，也用Karpathy LLM Wiki的思路做了整理。当我要做内容输出的时候，可以把它当成我的"第二大脑"，让AI根据我积累的内容，帮我直接输出分享的提纲和课件。我自己在实践的时候，使用Claude Code和Codex分别做了尝试，都可以达到目标。本篇内容，重点分享如何构建个人知识库、用好LLM Wiki的理念、以及用一个案例展示基于知识库，做内容生成。

01

在 Obsidian 中整理个人笔记

之前工作的时候，我会尝试用各类笔记软件做笔记。为了方便做内容管理，我就都迁移到了Obsidian里面。这是一款，基于本地文件内容的管理工具。可以把它理解为Markdown文档的合集，同时也可以存放图片（本地存放而非外部链接）、PDF文件等内容。

![](https://mmbiz.qpic.cn/mmbiz_png/UsUOUEyCK4lDHykP3o1tqFhH5FecpDfoLtKgac66IKia4LL45YeaUSgrX4DE8oyGKw4DloNLciat0ibwiafgXv17BpicsibKlba6EiaMkWJicPAkX3g/640?wx_fmt=png&from=appmsg)

整理完成之后，还需要做些准备工作：

1. 在Obsidian中安装Terminal插件，之后可以通过这个插件来使用AI工具。
2. 确认在本地电脑的Terminal/终端上，已经安装了Claude Code或者Codex的CLI。只有本地电脑安装了，在Obsidian的终端才可以使用。本质跟我们在电脑本地Terminal/终端里面，使用AI工具是同一个方法。
![](https://mmbiz.qpic.cn/mmbiz_png/UsUOUEyCK4kL9T14taErHCOnRp7f0bsm9RGQ9CAXC4Ym2ciclwsu0oIibEoib0mEib7dIKW9WHkKYwclRGuuvibRV7gBkQSibvgXpkqSDOR3W8ebU/640?wx_fmt=png&from=appmsg)

安装完成后，在Obsidian的左侧边栏打开Terminal，然后选择Integrated这个选项，终端页面就会展示出来。我们直接输入Claude或者Codex，开启AI工具的页面，就可以使用了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UsUOUEyCK4lY5u3uCWib9qX2RIyePIckcxMickEgae13S6rSKibYfNYKEZ5BCOibQy1gsOcVznuOyu9DZ8wL0yj1janzW48TkFboNhy8j7Ew7e4/640?wx_fmt=png&from=appmsg)

02

根据 LLM Wiki 理念整理知识库

LLM Wiki的理念，是Karpathy提出来的。使用之前，我先学习并理解它的全部内容。 **核心理念区别于传统的RAG方式，不是每次检索原文片段，而是让LLM持续维护一个结构化的Wiki。** 这个Wiki是LLM，在理解笔记语义之上，做的内容整理。每当笔记内容更新时，AI读取并总结笔记，更新对应页面。这样， **知识就可以沉淀为可复用的结构化内容。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UsUOUEyCK4kQRNlRlx3Qc0VlgzQXRXEHN9JiaOF2DzEVoKqxfpwT6e2xC83nUJHP2RBWO8n9IuG6ac3TaTaa4L8f4bqiaZoic5oibFYrISSCjuY/640?wx_fmt=png&from=appmsg)

来源：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

它的架构总共有三层，每层分别对应Obsidian里面的一个文件夹：

- **RAW：**
	存放我的原始笔记内容，AI只读取，不做修改
- **Schema：**
	可以理解为规范层，如果我们用Claude Code做内容整理，可以在这个文件夹里面添加 CLAUDE.md 文档，把规范写进去；如果是用Codex，可以添加 AGENT.md 文档。
- **Wiki：**
	LLM提炼出来的知识摘要等，我重点让它放我笔记里面的概念，以及概念之间的关联关系。这层级里面还有另外两个文档，index主要目的是做内容的检索，而log则是记录每次的操作，方便做追踪和调整。

当知识库规模较大时，再用index的方式做检索效率就会低很多。Karpathy 建议引入 QMD 等本地搜索工具，通过 MCP 让 AI 调用该工具，在海量内容中高效检索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UsUOUEyCK4lvednOaYCWFdmAA7ECvyqVfJFuUXmVY7nK0nkBBpkX4CibCpLKAdDviamJoz88wcpREibpCdzk2uyYgicSHtvsEqznaBZYEAhMU08/640?wx_fmt=png&from=appmsg)

具体操作步骤：

- 我先在Obsidian知识库的根目录下创建这三个文件夹，然后把我的笔记内容挪到 RAW 文件夹里面去。
- 在Schema文件夹里面创建AGENT.md文件，稍后让Codex给我写入规则。
- 在 Terminal 中打开 Codex，将 Karpathy 的 GitHub 页面链接直接发送给Codex。让它先学习全部内容，然后给我生成一个策略，我审核之后觉得没问题了，就让Codex按照策略直接执行。
- Codex执行过程中，我会通过Obsidian的Graph View来查看它提炼出来的概念，以及概念之间的逻辑关系。过程中如果有问题，我就把要求直接告诉Codex，让它给我调整。
- Codex完成在整理过程中，会自动创建 Index 文档，以及在Log里面记录相关操作。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/UsUOUEyCK4ltAjJmdd72lrHd99DAW6icO4cO4xSOIynfaZRIAd7yHicicoKP2Cla9vUhqqvYEWPdCGfuFx7TrOibviayW8qJGHcRmLnibYADJ4uzk/640?wx_fmt=png&from=appmsg)

结果展示：

全部内容整理完成后，在Graphy View里面就可以看到类似这样的知识图谱。

- 每个圆圈都是一个笔记里面的概念
- 每个连线代表概念之间的关联关系
- 圆圈大小代表关联关系的多少，圆圈越大，跟其他概念之间的关联关系越多。

从整理完的内容来看，关键概念包括：AI产品经理、产品技术架构选型、个人品牌、内容杠杆、复利资产、系统能力、用户任务等，也是我笔记内容的一个缩影。

![](https://mmbiz.qpic.cn/mmbiz_png/UsUOUEyCK4nAaYOmdMqC9CFvU2Qh2MYWPfjowKeuG1yXY4iciaJ9jzLicTfuwxNmRNp0C3icUqse9PS0MAHHJgjEeJ3ArI8hOKWVZvW97Pia8usA/640?wx_fmt=png&from=appmsg)

03

知识库应用 —— 内容输出

笔记整理只是第一步，如果只是做知识沉淀，价值不大。 **最好是找各种机会，把内容充分利用起来，这也是做内容迭代跟优化的一个好机会。**

比如当我需要做一场AI内容分享的准备时，我会把背景都告诉Codex，让它结合我知识库里面的内容，生成分享大纲。我确认之后，就让它调用frontend skill生成HTML格式的PPT。 **内容和视觉效果，一次全部搞定。**

拿到结果后，如果需要微调，我会告诉AI具体的页码和详细的调整需求。方便它一次就给我改到位。

![](https://mmbiz.qpic.cn/mmbiz_png/UsUOUEyCK4nfibfnyho7bDsU4QibbsKJYHkkel7PXjoKwlYsDghyonTUnQLD7d1CadPnFc4DaYKhFNUxS5dfibggrfuZWsfzy7kFomibERq5PMc/640?wx_fmt=png&from=appmsg)

知识库内容更新

分享完成后，如果效果还不错，我也可以把这次生成PPT，放回到Obsidian笔记中，作为新的笔记内容。

内容除了日常记录的笔记外，我们可以用Obsidian的浏览器插件，收集网页上看到的高价值信息。它捕捉到信息之后，自动的帮我们放到Obisdian里，直接做信息收集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UsUOUEyCK4lPgf3XgAUqg7wMV5JdvgqbPL2kS1fYgdziaMExwyz996HbU1ytUSqzvwbn1LAZf1Ymakz7q3vCcPUaurscMWhTtZw50QhrZibm4/640?wx_fmt=png&from=appmsg)

04

复盘与思考

4.1 笔记按照主题内容做分类，而不是按照来源做分类

我最早在做笔记整理的时候，会把笔记按照来源做分类。比如有些是在线课程的笔记，有些是读书笔记。后来在让Codex帮我做内容核查的时候，它给我整理了五个主题。我瞬间觉得按照主题内容分类的方式更合理。

收集和积累笔记的目的，是为了提升我在某个知识领域的专业能力、加深对这个领域的理解和认知、以及找到更有效的落地方法。因此，在整理笔记的时候， **按照内容主题做分类，更合理。** 后续做知识查找的时候，让AI只从某个具体的文件夹里面做检索，效率也更高。

4.2 知识沉淀的目标：构建「第二大脑」，而非成为信息收藏家

AI可以帮助我们更好的收集和处理信息，但工具只是手段，不是目的。 **真正的价值，在于集合个人的实操经验，沉淀出来的洞察与判断。** 把这些内容记录到笔记里面，才是高价值内容。AI里面被训练了互联网上的信息，而我们自己的洞察，它是不知道的。知识库的价值之一，是持续提高内容的含金量，让它成为真正自己的「第二大脑」，而非单纯的笔记归档系统。另外，一定要找机会多去使用知识库，也是用更多应用场景，来帮我们做内容校准。

4.3 输入质量决定输出质量：只保留真正关键的内容

笔记里面的内容，是AI做知识加工和处理的基础。 **只有提供高质量的输入，AI才能输出高质量的结果。** 所以后面需要定期做内容的整理。那些随手记的浅显观点、已经过时的内容（不适用现在趋势和市场周期的信息）、与自己目标无关的资料，都可以被归档，甚至直接删掉。确保笔记里面的内容，全是高价值的知识。

本次我在Obsidian里搭建个人知识库，就顺利完成了。有了这个基础，后面会继续做内容补充跟迭代。在LLM Wiki架构和思路之上，根据应用场景调整Wiki里面的内容。让整个知识库的价值越来越大，用知识生成"复利效应"。

继续滑动看下一个

Chen的AI产品笔记

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过