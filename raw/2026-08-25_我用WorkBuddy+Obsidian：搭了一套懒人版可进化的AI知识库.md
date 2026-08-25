# 我用 WorkBuddy + Obsidian：搭了一套懒人版可进化的AI知识库

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/94wtoB0UCAO-NFvrtUMhuA

---

## 摘要

本文介绍了一种基于Obsidian和LLM wiki理念的懒人式AI知识库方案，通过让AI自动维护知识结构来解决传统RAG检索碎片化和人工维护成本高的问题，其架构分为存放原始资料的raw层、由AI编译生成结构化知识的wiki层，以及定义维护规范的schema层。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyRe1bp0A2m4Wy7kOgDxkbEq6b0M4AYaRgJP1m6vxKrDXShY4430LvUeIfoHu10dCkdI5Aco8dfq5k6uQOCN44Jo9VrjDzlxCSE/640?wx_fmt=png&from=appmsg)

书接上文： [《我用 WorkBuddy + Obsidian，搭了一个会自己生长的个人知识库》](https://mp.weixin.qq.com/s?__biz=Mzg2MzcyODQ5MQ==&mid=2247502653&idx=1&sn=bdd84e0cf18d88b06d6f5b1829f593f9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRXwc8RtVbRvIM307z8mvbOt9dhJglqW8cuEYvI3fhJ4fZPmib6se1zMNnEnRiam9ibKqOib25aDiccYL2MPwPL8debSiaBibyyb3ZJI0/640?wx_fmt=webp&from=appmsg)

AI非常聪明，但是要把它用好，却不容易！

核心原因在于，我们给的上下文信息不够，使得它并不充分的了解我们。

因为很多信息是在我们的脑子里面的，很难凭空让AI知道，比如：熟悉的业务领域、做过的项目、踩过的坑、经验判断、思维方式、表达方式等。

为了使其更好的完成任务，我们每次和 AI 对话时，都不得不重新交代这些上下文信息，一遍又一遍的复述就很麻烦。

那么这里的解法是，把这些信息维护到个人知识库，让AI在执行任务之前先去读取这部分信息，这样就能让AI更好的掌握充分的上下文信息了。

但是知识库维护起来是很麻烦的，维护成本甚至超过了收益成本，这也导致很多人没法持续坚持下去。

那么维护这个事情是否可以让AI来帮我们做？

因此，这里我们介绍一种针对于懒人的知识库方案，Obsidian + LLM wiki + Agent。

## 什么是LLM wiki ？

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTJkx5WiaGuf9Pk1qwC0OicQbqViaohUIejKonDTx5X7HWxqpymHBhfLQG2EySeicZmwrVC3rCJZmmKNbTSSGiaECGurul2BibNySNWY/640?wx_fmt=webp&from=appmsg)

LLM wiki 是karpathy今年4月在Github上公开的一份个人知识库构想文件，大致描述了个人知识库构建方案的架构和理念，但没有说明具体如何实现。

他指出了传统RAG检索的弊端，每次问答都是从海量的知识碎片里面去寻找相似的文档，然后在临时组装生成答案，知识和经验并没有被持续沉淀下来。

而LLM wiki则是提前把知识编译成一个可持续演化的知识结构， **一次编译，持续复用** 。它的核心是在知识整理这个环节去下功夫的，让大模型去做了人不想做的事情。

LLM wiki整体架构分为三层：

1. **raw层，用于存放采集的原始资料** ，比如我们收集的文章、论文、图像、数据文件、以及聊天记录等，这些内容是整个知识Wiki的事实来源，是不可变的，LLM只负责读取但是绝不能修改它们。
2. **wiki层，相当编译层** ，用于存放由LLM处理后的结构化知识，包含摘要、实体、概念、比较、概述、综合理解等，这一层主要是由LLM维护更新，基于raw层的知识编译而成，人仅负责审核。
3. **schema层，定义整个知识系统的维护规范** ，通常定义为CLAUDE.md或者AGENTS.md，它告诉大模型Wiki的结构、约定以及处理资料来源、问题回答或者维护wiki时应该遵循的工作流程。

根据LLM Wiki的理念，一个简陋的主体目录文件结构大致设计如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQI96f8GOaIEsX1JjTxS6YxMnicjUHbUnxxsiarfwPiaWf0R7fN8bIIGkCn181u8USib9z3NUAjibc07W5LUUT9R4AXpBIBTN539cXA/640?wx_fmt=webp&from=appmsg)

目录文件按职能可以分两类：

**一、主流程目录，承载知识从源到产物的状态流**

1. raw存放原始资料，供下游编译使用。
2. wiki就是经过AI编译完成后的结构化页面，按照摘要、实体、概念、比较、概述、综合理解 进行组织。

其中raw和wiki内部的目录结构没有固定标准，可以结合实际的应用场景调整，不一定要遵循这一套规则。

**二、支撑目录，服务于编译过程本身**

1. AGENTS.md就相当于Schema层，是指导 LLM 维护整个知识库的工作原则，文件命名取决于我们用的Agent是什么，如果是Codex则是AGENTS.md，如果是Claude Code 则是CLAUDE.md，如果是Workbuddy，则是.workbuddy/MEMORY.md，遵循Agent的记忆规则定义即可。
2. templates用于给AI生成wiki时参照的模板文件，与wiki下面的目录结构一一对应，确保生成的同一种类型文件结构都是一样的，便于维护管理。
3. index.md是wiki内容的索引文件，它相当于一本书的目录结构，便于快速找到目标内容，
4. log.md、\_reports共同提供了可观察性，log记录操作日志，\_reports记录健康检查报告。

三个核心操作包括知识编译、知识查询、健康检查，具体的规则均维护在Schema 层中。

以上就是LLM wiki的核心机制，而整个知识的载体是用的Obsidian。karpathy在方案中也做了一个形象的比喻，Obsidian 就像是集成开发环境（IDE），LLM 是程序员，而wiki则是代码库。

## 为什么要用Obsidian？

然后我们看为啥要用Obsidian这块笔记软件，用Notion、IMA、NotebookLM不行吗？

Obsidian的优势是完全本地化和数据自主，不被平台绑定。它所有的笔记都以Markdown格式保存在电脑本地，而不是保存在厂商的服务器上，完全不用担心数据泄漏、或因平台停止服务而迁移笔记等问题。

并且这种文件形态非常适合 Agent 工作。WorkBuddy / Codex / Claude Code 可以直接读取目录、创建页面、修改链接和维护索引，每次变化都能定位到具体文件，还可以通过 Git 留下记录。

而云端笔记如果要接入本地 Agent 进行管理，通常只能通过官方提供的命令行工具或者 MCP 服务来完成，执行链路更长，耗时更久。

Obsidian另一个重要的优势是， **支持用双向链接去关联知识，通过 `[[笔记标题]]` 语法，就能在两篇笔记间创建双向链接，形成一个非线性的、发散的网状知识结构，像我们大脑联想的方式。** 我们在做知识检索的时候，就能通过这些关联链接，查询到相关的知识。

而且 Obsidian 的插件生态非常丰富、并可定制化，进一步提供了扩展空间，从模板、查询、版本管理到发布和可视化，都可以按需添加。

在整套系统中，Obsidian 同时承担存储底座、人机操作界面和知识观察窗口三种角色；

对于一套需要长期使用的个人知识库，本地自主、结构开放、变更可追踪和能力可扩展，Obsidian是非常有优势的。

## 看一个案例实践

通过上面的介绍，大家应该大致了解了整个知识库的运作原理以及Agent、Obsidian等工具承担的职责。下面通过一个具体的案例来看整个搭建的流程。

这里我们会用到一个开源项目叫claude-obsidian，它是基于LLM wiki架构实现的一整套个人知识库搭建工作流插件，提供了全流程Skill，包括项目初始化、知识摄入、知识查询、知识治理，另外还提供自主研究、知识回写、热查询、本地向量检索方案等。

要注意的是，大家不要被其名称误导，它不仅支持在claude code中使用，还支持在Codex、Pi等Agent中使用。

### 项目初始化

首先我们打开 Obsidian，点击【创建】，在指定文件夹下创建一个新的仓库，这里命名为llm-wiki-claude-v2，并使用Git版本管理工具初始化仓库，便于后续管理变更。

然后在该仓库路径下启动Claude-Code 或者 Codex会话，并输入 `/claude-obsidian:wiki` 指令初始化项目。

在这一步，它会询问我们创建知识库的主要用途是啥？并罗列出了6种模式让我们选择， **每一种模式对应的目录结构设计是不同的** 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQHeWFaibHpOVO2e8HjrVEjmGZAjXCbtG4vcBObhEg77CkBEgIscjORyDmpnD8Pa8x72CyRib4aunoEFY9JCUqicg0dibAoiadqWXicQ/640?wx_fmt=webp&from=appmsg)

这里我们选择项目研究，最终搭建出来的项目结构如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS18Eam4FNnQXSjQa5YgELUvNTTMbRO8HGBVAmx8jBOaZGic6VztXXJ2WeThdAPBbxENFP8Oe7voqL5U6JwETxz66A6g6tS4dwU/640?wx_fmt=webp&from=appmsg)

如果选择其它的模式，wiki这一层的目录结构会存在差异 **，因为它是由标准基础结构+模式特有层组合而成的** 。

下面是标准的基础结构：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRyvvF9L50MVd6Hb7bGGBpxSZSaUnzNyicAM3T44J6jZW01XwlV1JYnJIdNAj0VmbC1hD7yGoXMhFl2bTwXpRjMmoQtGgjOHVS4/640?wx_fmt=webp&from=appmsg)

**wiki内部的目录结构的设计本质上是对知识的抽离模型的设计，不同应用场景的知识库结构存在很大不同的。**

因此直接创建套用karpathy提出的标准化结构，并不一定适合所有场景。

Claude Obsidian这个项目它内置了6种知识库场景，每种模式的具体的目录结构可以看项目源码中的wiki这个skill下的modes文件，这里不做展开。

### 知识摄入

通过上一步，我们完成了仓库的初始化操作，就可以进行知识的摄入了。

这里我找一篇之前写过的公众号文章《向量检索、知识图谱与 LLM Wiki：RAG 被嘲笑了三年，但企业还是离不开它》，作为知识源，先加入.raw文件夹中，然后进行知识编译。

这里我们可以借助 **Obsidian Web Clipper** 浏览器插件快速采集网页端的文章内容，它会把网页主体内容以markdown的格式直接添加到当前打开的Obsidian Valut 中的指定目录中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS7e4YpsKtWczxI4icibsYMKyObIS6cLg0BST5J7kzzOksjyeMlRyBV5WfE56ak3M1aCjCJ6UpHvBJjZlefVibdnIdlHicDd2ic21Iw/640?wx_fmt=webp&from=appmsg)

知识摄入操作使用如下命令：

> /claude-obsidian:wiki-ingest

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQPMzG9M8KsFGfU9ONIj0s8tuyPTSaCDicuib4vJM5TLSulILTfknMoVjm4ZecfjTAhgV6Le1Hfae7ZLcgEA0iaxqtvrAqh5v7gpo/640?wx_fmt=webp&from=appmsg)

基于单篇文章最终新建了16个页面，主要抽离了6个核心概念、5个实体对象、并抽离出文章中的重要观点、以及下一步知识补足建议。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRzGuP6bkojsqvQdVTfeSPwxqSRAf6deBuDu5AHLVkSLEAyY8hp1dLtMrcIJeB8jJufUW85eCtJz0Mj6QfNfwuDnkhqFiazweVY/640?wx_fmt=webp&from=appmsg)

结合原文内容以及编译结果，整体质量还是很不错的，实体和概念以及观点都能一一对应。

并且，在Obsidian中可以看到整个wiki知识的图谱关系，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRDlFXqsXZgjz4eOahDFfkDH48VnsdNMic7yoyaEVltBA0IkqYDfGO4crYABAvrcBgF2Idwo5HblxBTO2uhjMnC6GicrFJqnARxw/640?wx_fmt=webp&from=appmsg)

### 增量编译

知识摄入不是一次完成的，那么在多次摄入时，如何实现增量编译，而不是全量编译呢？

增量编译的功能，其实在摄入命令内部已经实现了。即使我们重复的执行这个编译命令，也不会反复编译知识。只有有新的文件加入时才会真正触发编译逻辑。

**因为每次执行摄入命令时都会为参与本次编译的文件生成内容hash值** ，然后在.raw/.manifest.json 文件中检查是否存在相同 hash；如果命中则跳过该文件编译，未命中则正常处理。

编译完成后，在把本次摄入的源文件hash值记录到.manifest.json中，下次再 摄入时会直接跳过。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQBnauIuaQkm9VgwVzPY843ousAiaoC5ueS1SVIvOxGSRdwibNULkYicwkOibibLCeF8KxVmjnwPGWlyVd8Uq3CsFVT97dVibRiaAgicaA/640?wx_fmt=webp&from=appmsg)

### 问题查询

知识查询操作使用如下命令：

> /claude-obsidian:wiki-quey rag有哪些检索技术？

检索结果如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTKOvaicxJO7WibW5QOD47nlo0uanEoJ1ImctOzacP4cicR2VusrKV3SJrACkiczu75pSwJkObh6GgbJqXJ5v8J1Eib0jRMtqOkmYzM/640?wx_fmt=webp&from=appmsg)

其中红框中的答案是高度符合原文表达的。

如果我们采用RAG的检索策略，先把原始文章进行分块、向量化、入向量库中，然后按照语义和关键词检索知识片段，这样是没有办法达到这种效果的。因为原文中并不直接存在这种可以回答问题的结论，相关的知识是分散在各个段落中的。

而LLM wiki这种方式能够找到，是因为它经过LLM的消化理解，对原文的内容进行了一次编译，生成了一系列的核心结论、实体关系等知识。

比如编译后的wiki中就存在一份可以用于直接回答这个问题的知识。在编译阶段就把所有的检索技术跟RAG检索这个domains建立了关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTjZduSsZ9KibXUnKLZ4Fg6icRoNibtUtzgJ7sm6OuumpzOlhOwjpo4ku7XWs2JfIQ0j3NJlnS9ICickl3oug5OIdSrWRKSibHESbrs/640?wx_fmt=webp&from=appmsg)

它的检索链路，是先查wiki/index.md这个索引文件，然后在按需查找下一层级相关页面，这里跟Skill的渐进式披露机制类似。

避免把所有的wiki加载到上下文中，导致上下文爆炸。这种机制可以提升检索效率、同时能减少Token的消耗。

Claude Obsidian还做了一个优化措施，每次操作后，无论是写入还是查询，都会把本次关键上下文写入到hot.md文件中，大约500词，注意这里写入是直接覆盖。

**后续会话过程中，无论是新开会话还是跨项目使用，都会优先读取hot.md的缓存内容，相比直接读index + N 个页面，单次 query 能省下 70%+ 的 token。**

它是通过本地文件把会话关键信息持久化保存，确保上下文在不同会话中能够被衔接，无需我们重复解释，让下一次 query 不必从零开始，从而节省很多的Token消耗。

### 高价值答案归档

如果这个回答质量高，具有沉淀价值，我们可以把对话内容归档到wiki中去，使用如下命令：

> /claude-obsidian:save

结果如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQlj9daIIdusscpJg5xkLjQhUCdWpxCcuHVqnKBPFxUdyL1icx9Hd9kOwl50suh5OvwRzO0Jh2nSBPAia4AzkdygD9FHQ2fShmiac/640?wx_fmt=webp&from=appmsg)

这样就把刚刚对话的问题和答案以及参考的wiki页面写入到wiki/questions中去了。

当我下次再问同样的问题时，这里我打开一个新的会话询问问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRXrYCzxjGXeyePXhDiaIRsLvfL7tra5WRqXGFRFkwSNrztKk7oTxQ8PMk9qTObV0YeCOjuWOjQwnsIDlJFhVKRwWHRL3TkHOLc/640?wx_fmt=webp&from=appmsg)

从结果可以看出，它没有重新去wiki里面找相关的页面然后在组织答案，而是直接基于现成答案进行回答的，回答的内容与前面完全一致。

### 自动研究

知识摄入处理流程是：我们提供资料，Agent帮我们整理。但是实际情况是，我们提供的资料难免会有空缺。

比如前面我只加入了一篇文章，关于RAG知识体系还差很多内容，我想补足Agentic RAG这部分知识到wiki中来，但是又没有高质量的知识摄入，这时候就可以用autoresearch的能力，自动补足缺口知识。

使用方式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQEB4ZlzeSsdwbYRCjruX70aoNTuQlGZukgMiafHiabSKO0SvWE34Bc1JdasHj9NCUZSMKoxUwgJeHiaVaZaGZqnMB1ISiaFAiayVOo/640?wx_fmt=webp&from=appmsg)

它的工作流程是，根据我们输入的Topic，分解成3-5个搜索角度，跑3轮大约45次webSearch。

第一轮，围绕主题从不同角度分别去找资料；第二轮，基于第一轮发现的空白和矛盾，在做针对性搜索；第三轮，如果仍然存在关键缺口，就继续补充，否则就进入整理阶段。

最后把结果沉淀到wiki中。

过程听起来很好，但是实践下来你会发现效果很糟糕，这里我的经验是：

**autoresearch仅适合补足空白知识，并且主题范围越小，结果越好。因为它是联网搜索去抓取内容，你主题定得太大，它可能抓回来一堆主题分散的资料，并且这里还要限定抓取的信息源，优先抓官方文档，避开营销软文。**

在编写提示词的时候，就需要花些功夫，把研究主题聚焦、研究范围写明确、约束条件写清楚，像上面的示例一样。

### 健康检查

通过前面可以发现，整个知识摄入过程完全取决于大模型的处理，一开始笔记少的时候，靠人工确认没啥问题，但是知识库页面增长后，人工也审核不过来，问题就会开始出现，比如：孤立页面、死链接、过期结论、缺失页面、交叉引用缺失、元信息缺失、索引漂移等。

这时候就需要定期检查知识是否健康状态，可以执行如下命令进行健康检查：

> /claude-obsidian:wiki-lint

这个skill会帮我们完成上面这些维度的检查，检查完成后，它会在 `wiki/meta` 下面生成一份检测报告，告诉当前知识库哪里有问题，哪些可以自动修，哪些需要人工判断。

这一步很重要，建议定期检测，比如每周就执行一次健康检查，让知识库wiki保持健康状态。LLM wiki是一个会长期生长的系统，只要持续摄入，就需要持续治理。

## 数据采集

原始信息是整个知识系统的源头，知识采集这个动作就是知识进入编译的第一步。

这一步主要看我们的搭建知识库的目的是什么，这决定了我们需要采集哪些数据。

如果是用于构建个人第二大脑，那需要采集的数据要求就很多，比如我们每天看过的重要文章、视频、参与过的会议、聊天、通话、文字记录等信息；如果是做专题研究学习，那么仅收集查阅过的优质论文、文章、报告即可。

而收集的这些数据可能存在多个平台上，非常分散，想要把这些信息放入到项目的raw目录中，还是很费劲的，这里我们可以借助IMA和Obsidian Web Clipper用来收集整理数据。

比如，在电脑端浏览器中，看到一篇优质的文章，想把它加入我的知识库项目原始资料中，就可以使用Obsidian Web Clipper插件把网页内容以markdown的格式直接添加到项目的raw目录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQl2uetSztQ9yIXv2MsxQibvTmiaQHKqA6CPYviby48J3GFjxSSoV5HfVnzicTsuuZEbFrYbKiaBN3MAu9w4ibwbS9iarVibZlOx5QZCN8/640?wx_fmt=webp&from=appmsg)

而在移动端，我的大多数内容来自微信公众号，我想把优质的内容加入项目中，操作路径就相对更长，得先把这篇公众号链接发送到电脑端，然后在电脑端用浏览器打开，在用Obsidian Web Clipper插件收藏到raw中。整个操作流程是断裂的，有时候还会忘记在电脑端进行操作，有价值的文章内容就流失掉了。

这里可以使用IMA知识库作为中转，用来收集移动端的信息，把在微信中看到的各类信息一键收藏到IMA知识库中，这个方法对于微信生态的内容尤其友好。

操作路径：点击分享 -> 用小程序打开 -> 选择IMA，这样内容就自动被解析并保存到IMA知识库中去了。

然后我们还在借助Workbuddy的定时任务，定期从IMA知识库中把新增的有价值的内容同步到Valut 目录中来，自动化任务设置大致如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRo1rHnabRPqde6rZiczhkiamcJaw0I8x4Hgr4wh8zk1rDFibTlg1aMbVpfbNx3wQ8UibVMhMuVkZ9lo5o6z4jtA204nLTTWMBFQiaw/640?wx_fmt=webp&from=appmsg)

这样我们就能同时收集到电脑端和移动端看到的多数优质内容了。

除了上面提到的两种情况外，内容可能存在其它平台上，比如飞书文档或钉钉文档中，我们可以借助这些平台的CLI工具 + 自动化任务来实现数据的同步，方式方法很多，就不一一列举了。

此外，我们收集数据格式可能存在多样性，有文档、图片、视频、音频、PPT、PDF、聊天记录等，关键是要把这些格式的内容识别为文本，这里可以借助多模态模型进行解析，便于后续模型加工处理。

需要注意的是，原始资料的质量决定了Wiki的质量，这里的核心原则是，只收集高质量的内容，宁缺勿滥，否则我们的知识库就变成了垃圾进垃圾出。

## LLM wiki 衍生的问题

### 人的判断权不能交出去

上面的这套流程执行下来，刚开始的时候体验非常好，感觉一切都很美妙，我们只需要负责筛选、往里面投喂信息，LLM 自动就把知识编译到wiki中去，知识库仿佛拥有了“自动生长”的能力。

但是随着深入使用，问题也开始浮出水面。

全流程中，人做的唯一的事情的就是往知识库中喂信息，其它事情大模型帮我们全干完了，这些知识并没有经过我们大脑的理解、判断、加工，这些知识严格来说就并不属于我们，随着时间的推移，知识库中的知识越累越多，我们对这些知识反而越来越陌生。

并且知识的质量我们是没法保证的。因为LLM并不知道哪些信息重要，哪些结论值得保留，哪些内容应该被丢弃。

回到开头提到的问题，个人知识库太难维护下去了，LLM 能不能帮我维护？

现在 LLM确实 能降低了维护成本，但如果维护过程完全自动化，知识库的质量就别指望有多高。

**这里其实存在一个不可能三角关系，要同时做到低成本维护、高质量知识、个人内化，是不太可能的** 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQS2blvLmFeoM0w40CMkwBqTnvgGQBhDicFFzZ4siam4iaCqz3nZy6WrLeIvmJNSzZib3fEerqNHBd85RnVMo5gCsfDUsV7fqrInjU/640?wx_fmt=webp&from=appmsg)

因此，关键问题是：LLM 可以帮我维护到什么程度？哪些环节可以自动化，哪些环节必须由人参与？

**我认为两个环节人一定要把好关，第一是信息筛选环节，人要判断什么样的知识能流入知识库中；第二是知识编译阶段，需要指导大模型关注重点，并review生成的结果。**

其实karpathy自己也有提到，他倾向于单篇知识摄入，并且会全程参与进去，会去阅读LLM生成的摘要，并检查更新的内容，指导LLM关注重点知识。

有价值的知识库，是不太可能自动长出来的，还是需要依靠人和 LLM 在协作中逐步长起来，LLM负责降低知识整理和结构化的时间成本，但是人仍然要参与筛选、判断、提问和内化。

### 体量变大后的性能瓶颈

**这套方案的性能瓶颈在于，知识体量大起来以后，每次的编译成本和查询成本都会变大。**

前面讲的查询流程，默认是先查wiki中索引文件 `index.md` ，然后再渐进式加载相关页面。这种方式对于几十到几百个 Wiki 页面的知识库是没啥问题的，但当 wiki 持续变大之后，检索效率就会下降，Token 消耗也会变大。

要持续的维护大体量知识库，需要充足的Token预算。

要解决查询的性能瓶颈，可以集成 qmd 本地检索方案。它的核心流程是：

1. 先把 wiki 页面拆分为小的 chunk；
2. 给每个 chunk 生成上下文前缀，确保这个 chunk 脱离原文也能被理解；
3. 基于这些 chunk 构建 BM25 关键词索引；
4. 查询时先用 BM25 召回候选片段，再用向量相似度做语义重排；
5. Agent 读取命中的原始页面，再生成最终答案。

可以看到这里其实是使用了RAG检索的策略，也可以看出LLM wiki 和RAG并不是互斥的。

即使有了 LLM Wiki 仍然是需要 RAG的，他们两者定位其实完全不同。

这里可以用 **编译时 和 运行时** 来理解。LLM Wiki 是编译时产物，把原始材料预处理成高质量的知识页面；RAG 是运行时手段，在查询时刻做精准召回。

Wiki 在构建阶段就把散落的材料固化为完整的语义单元，每个页面自带元数据、关系使用双链符号记录、层级结构支持渐进式披露。

RAG 的重心是检索链路，它不会帮忙理解并整理这些内容，原来分散的资料依然分散，矛盾的还是矛盾的，过期的还是过期的。

## 适用的场景

从第一性原理出发，我们创建知识库的最终目的一定是为某个场景服务，是要有用的。

LLM wiki 更适合需要长期积累、反复复用、并且依赖个人判断的知识场景，而不是一次性问答场景。

第一类是专题研究，当我们持续研究 RAG、Agent、AI Coding、行业趋势等主题时，会不断收集文章、论文、报告和实践案例，用 LLM wiki 编译成概念、实体、观点、问题和关系，就能逐步形成自己的研究地图。

第二类是工作经验沉淀。比如产品经理、研发、运营、咨询顾问、投资研究等岗位，日常会产生大量项目文档、会议纪要、复盘记录、方案判断和踩坑经验。这些信息分散在聊天、文档和脑子里，平时很难被复用。通过 wiki 把它们结构化后，后续写方案、做决策、回答问题时，AI 就可以先读取这些背景信息，给出更贴近自己业务语境的结果。

第三类是内容创作。对于长期写公众号、做课程、做视频的人来说，之前写过的文章、表达习惯、常用案例、核心观点都很重要。把这些内容维护成 wiki 后，AI 就能基于你已有的知识体系做延展，减少风格漂移和重复解释。

## 结语

到这里，我们已经介绍了LLM wiki这套个人知识库构建方案和实践过程，并分享了存在的一些问题和应用场景

最后，还是建议先从一个高频、明确的小场景开始，人参与进去，把它做深、做稳，能真正用起来。

然后对 AI 深度学习感兴趣的可以点击：

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyTCQhJHOsXm47dGViaYFsFuuDwa5fdWE9C6gPtic8amSwGhm3aIhNyK1sCWOOiaicicwG7WpKibf6wgXcjve3eeT5n8EyE5thonzBFyk/640?wx_fmt=png&from=appmsg)**

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过