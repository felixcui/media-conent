# OpenAI：FDE 的目标是让自己失业

**作者**: Colin Jarvis

**来源**: https://mp.weixin.qq.com/s/xku4E2vENNPl09ZyOyGBlw

---

## 摘要

OpenAI前线部署工程（FDE）团队负责人Colin Jarvis撰文阐释，FDE旨在弥合模型能力与工作可靠应用之间的“部署鸿沟”：对模型已胜任的任务，与产品团队打造可复制方案；对尚不能完成的任务，联合研究团队改进模型。其成功标准是让客户未来无需FDE也能解决问题，即不断让自己“失业”，再转向更难的问题。

---

## 正文

Colin Jarvis Colin Jarvis

在小说阅读器读本章

去阅读

刚刚，OpenAI 官方博客发了一篇长文《What FDE means at OpenAI》，作者是 OpenAI FDE（Forward Deployed Engineering，常译作「前线部署工程」）团队的负责人 Colin Jarvis。

![](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkJ0ZG7JJZgsk5sZws7VdqHdGMH52eiaO4eckmSScmlqch5m1IyC2biauhichojbQRwEjooiccK3iboicrfQkibgREJOzFPiaIZNVSBZBI/640?wx_fmt=png&from=appmsg)

文章讲了三件事：FDE 在 OpenAI 是做什么的、是如何开展工作的，以及怎么判断自己干得好不好。

Colin 发了一张 FDE 团队的合影，并配文：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 如果下一个客户不靠我们也能解决同样的问题，那我们 FDE 团队就算完成了任务。
> 
> 我写了一篇文章，讲在 OpenAI 当 FDE 是什么样的：我们把和客户一起做的事，变成更好的产品和模型，让下一个客户的起点更高。

![](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlORocia2YDSF3lmqeeicL9Bjh7R190BHNAgcWC76tkcZiag7loJsl5o8pH9WcUgojRZFxBattibUN4Ras7Iwa2ibQCYlvJwXiaPv4ss/640?wx_fmt=png&from=appmsg)

OpenAI FDE 团队合影

全文的核心，是一个叫「部署鸿沟」（deployment gap）的概念： **模型看起来能做到的事，和人们在工作中真正能可靠用上的东西之间，隔着一段距离。**

Colin 在 2025 年初创立这个团队，就是为了填这段距离。

具体的做法分两条路。模型今天已经能胜任的，FDE 和 Product 团队一起把方案做成可复制的；模型还做不到的，就拉上 Research 一起定义缺口、改模型。

而衡量成败的标准有点反常理， **如果每隔几个月就让自己「失业」一次，才说明 FDE 团队在好好干活。**

文章按四条原则展开，每条都配了真实案例：

• **从结果出发** ：约 15 名 FDE 为一家大型半导体客户做了 10 多个用例，3-6 个月内全部上线，定向测试生成省下约 48% 的时间，kernel 优化带来 22% 的性能中位数提升，几周的调试缩短到几个小时

• **让成功可复制** ：同一批用例迁到以 Codex 为核心的通用 harness 上，每个项目删掉约 90% 的定制代码，推广到第二个团队从两个月缩短到一天；OpenAI Presence 和 Thrive Holdings 的 Tax AI（试点处理 7000 份纳税申报，吞吐量提升约 50%）也是这么来的

• **补上智能缺口** ：一家大型电信客户要上语音客服，模型在关键 eval 上只有约 60%，FDE 拉上 Research，六个月做到 90% 以上，由此得到的语音模型又反过来服务了更多客户

• **去找更难的问题** ：Codex 能一次做出他们几个月的成果之后，答案就是继续往前，去找更难的问题

这篇其实也顺带回答了一个问题：模型越来越强，FDE 这种重人力、驻场式的岗位，会不会很快就被模型自己替代掉？

OpenAI 的回答很直接……被替代本来就是目标啊！替代完了，就去下一个更难的地方。

## 全文

01

作者：Colin Jarvis，OpenAI Forward Deployed Engineering 负责人

发布时间：2026 年 10 月 22 日

副标题：我们做什么、怎么做，以及如何解决企业最棘手的问题、带来真正的影响。

◇ ◆ ◇

Codex 刚出来的时候，团队里有人问我：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 如果 Codex 一次就能做出我们过去几个月才搭起来的那些用例，那我们还能干什么？

这个问题，正好问到了 FDE 在 OpenAI 最核心的地方。我们和客户并肩工作，弄清楚他们最难的问题，再做出他们靠得住的解决方案。

我们从中学到的东西，会反过来影响我们的产品，也会给 Research 团队带去具体要解决的问题。

这就是进步。

**如果我们每隔几个月就让自己「失业」一次，说明 FDE 团队在好好干活。**

我在 2025 年初创立了这个团队，为的是填补我们所说的「部署鸿沟」：模型看起来能做到的事，和人们在工作中真正能可靠用上的东西之间的距离。

![部署鸿沟](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFkVAiaAtdicTVuGEsgeveSZRS5TvnsPQZGTAPoNCnyZzh7zKPm0tJeCjHSZssM8ULLMJribv7HRXDiboq46sOmia9So5zLwv4Gg9aIU/640?from=appmsg)

部署鸿沟

模型能力进步得太快，而把它们真正用起来所需的系统和流程，还没跟上。

有时缺的是一个产品；有时一个模型在 benchmark 上表现很好，可一碰到真实世界里的各种变量和约束，就干不了活了。

我们专注于客户最难的问题。

我们的模型今天就能胜任的，我们和 Product 团队、客户一起把方案做成可复制的；模型还做不到的，我们就和客户、Research 一起把缺口定义清楚，再推动改进。

我们的目标，是让每一次合作都给下一个客户留下一个更好的起点。 **如果底线被我们抬到了这样的高度，下次客户再遇到这类问题时已经用不着 FDE，那就说明我们的工作做好了。**

John Deere 是一家有 200 年历史的农业企业，它面对的挑战，是怎么把个性化的建议规模化地提供给农民。

其中一个例子是它的精准除草技术 See & Spray：用摄像头和机器学习识别出杂草，只对杂草喷药，而不是整片田地都喷， **最多能减少 70% 的化学药剂用量。**

但要真正拿到这些好处，前提是农民知道怎么配置这项技术、怎么规划种植季，以及在情况变化时怎么调整做法。

于是 John Deere 部署了 OpenAI 的 API，让这类支持变得既个性化，又能规模化。

AI 可以用自然语言回答农民的问题，给出量身定制的设置指导和建议，发现设备什么时候没有发挥出全部潜力，还能帮农民看清他们从这项技术里到底得到了多少价值。

机会也不止于某一次交互，而是在农民使用产品的全过程中持续给出相关的指导，帮他们用好设备，同时提升效率和可持续性。

这正是 OpenAI 的 FDE 要解决的那类挑战：帮助组织从「AI 有这个能力」，走到「系统能在复杂的真实环境里交付实际价值」。

但这些问题往往是完全开放的，可能没有公认的标准答案（ground truth），也没有现成的打法。

人人都想做出前所未有的东西，而愿意为此付出必要代价的人，就少得多了。

要找到有才华的 FDE，同时还要不断抬高「足够好」的标准，为此我们一直在不停地试验和实践。

## 从结果出发

02

每次 FDE 团队开会，我都会先放一页幻灯片，上面只有一条核心价值观：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 从结果出发，不惜一切把事做成，然后再去规模化。

![从结果出发](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFkMEsqEfE5qp9vtbs0A4KWqwgITtJqcTtibjicU5wcHw4ia8M7L4T3gUVBwAsk49dew3ksufZ19UWHAc4wjV4X31MibBzK3MDOJkm0/640?from=appmsg)

从结果出发

配图里是英国钟表匠约翰·哈里森（John Harrison）的两代航海钟：1735 年的 H1 写着「先让它存在」，1759 年的 H4 写着「之后再把它做好」。

一个惊艳的 demo，往往能撑上很久，才会有人问起：它在真实世界里到底能不能用？

而我们的工作，是把客户的问题解决到我们敢在生产环境里为它背书的程度。

2025 年年中，我们有大约 15 名 FDE 在为一家大型半导体客户做 10 多个用例，目标是让他们的验证流程变成 AI 原生的，覆盖：

• 定向测试生成

• 根因分析与调试

• 一个架构助手

在这个行业， **验证可能占到一个项目约 70% 的工作量** 。机会巨大，能下手的地方也很多。

有些 FDE 几天前才刚加入 OpenAI，从来没在半导体行业干过。

他们直接嵌进了客户的验证团队，利用业余时间学芯片设计，并和工程师一起构建 eval，来测试 AI 能不能生成有用的测试、能不能正确诊断芯片故障。

边学的同时，我们为每个用例分别构建了定制的 harness。在最初的 3-6 个月里，所有用例都进入了生产环境，也有了第一批用户。回报体现在这些指标上：

• **AI 定向测试生成节省了约 48% 的时间**

• 通过 kernel 优化，性能中位数提升了 22%

• 几周的调试缩短到了几个小时

我们给客户复盘这一切的时候，他们的首席硬件官问：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 你们来这儿之前，是做芯片设计的吗？

**我们的 FDE 不需要第一天就懂这个行业，但把它学会，是他们的责任。**

编程助手让软件越做越快，理解客户的业务也就变得更加重要。所以我们的团队里既有通才，也有领域专家。

你需要足够的知识来做出靠谱的判断，也需要足够的好奇心，去质疑那些关于现状的默认假设。

比如在生命科学领域，我们的 FDE 有科学背景，所以能赢得研究人员的信任。这些研究人员做的是临床前药物发现，包括靶点验证与优先级排序、基因表达分析，以及化学合成路线重建。

有了这些专业知识，FDE 才能对这些工作流可以怎么改进，给出有分量的判断。

## 让成功可复制

03

我们已经证明了这些工作流能创造价值，但每一个都还需要太多的定制集成，很难推广到另一个团队。下一个挑战，就是在保住这些成果的同时，让软件更容易部署和维护。

![把难题变成可复用的能力](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFmRMJ0CDZ1PNLGAdvicFWnqoSrrJGhkibF9HnyElJLZK5y6DdwLBRUzeiaKbG3XcHMOicGKUibtzDULLdIMQenmEfhlVAFDThtuBFXw/640?from=appmsg)

把难题变成可复用的能力

那时，Codex 的能力已经提升了不少。一位 FDE 试着围绕 Codex 重建了他们的应用，随后又和团队一起，把这些用例迁到了一个以 Codex 为核心的通用 harness 上。

原先的定制应用，变成了基于 Codex 通用原语构建的 plugin 和 skill。Codex 本身也成了交互界面，我们便下线了那些为单个用例单独写的终端 UI 和 CLI。

**我们从每个项目里删掉了大约 90% 的定制代码** ，而这也改变了我们构建、维护和扩展这些工作流的方式：

• Codex 的每次集中改进，我们都能直接受益，每个用例需要的胶水代码少了很多

• 关键功能被打包成 skill 和 plugin，既方便互相分享，也能交给 AI 卓越中心（AI CoE）统一管控。于是从一个团队推广到下一个团队，可以简单到只需换上新的连接器 / MCP 服务器、构建一套新的 eval（这一步我们也有现成的 skill），然后就能跑起来

在 2026 年 8 月的一个例子里，最初的部署花了两个月， **推广到第二个团队只用了一天** 。规模越大，后面的团队上手也越快，这个趋势一直延续到了现在。

![改造前后的架构](https://mmbiz.qpic.cn/mmbiz_jpg/ZKqVLiaIpzFn2hvOoYmjT1l9b0HYk0ndzTmGPxeK3HbWlksgFLzEnKbIqjlJepaeRGTXVjQJ1ffAu0JHnSGwJA4iaCa3riaF3DzxpMSpy5ZaeQ/640?from=appmsg)

改造前后的架构

图中左边是改造前的多 Agent 架构，靠一堆专用 Agent 和定制工具拼起来；右边是改造后的架构，围绕 Codex、skill、MCP 和代码仓库，简单了很多。

这是让自己「失业」的一种方式。我们为了上生产所做的那些工作，帮我们确定了什么才是关键；底层产品变强之后，我们就能替换掉大部分定制实现，同时保住它带来的价值。

这也是为什么顺序很重要。LLM 让我们能很快地把东西做出来， **那就用这份速度，先把有价值的东西交到用户手里，看清楚实践中什么经得住考验，再把行之有效的部分规模化。**

同样的原则，适用于我们所有的合作项目。

OpenAI Presence 是我们面向企业的语音和聊天 Agent 产品，它就是从真实的客户部署里长出来的。这项工作始于 Swarm，后来演进到 Agents API，如今 **已经有一家客户超过一半的来电由 AI 处理。**

把这些部署推进到生产环境，让我们知道了哪些问题需要定制方案，哪些构建模块别的团队也能用。我们把这些构建模块放进了 Presence，开发者便不用重建底层基础设施，也能更轻松地把受监管的工作流自动化。

每一次部署都在塑造这个产品，也给下一个客户留下了更好的起点。

在和 Thrive Holdings 的合作中，OpenAI 的 FDE 和研究员与工程师、会计师一起，为 Crete 旗下的会计事务所构建了 Tax AI。 **试点期间，Tax AI 处理了 7000 份纳税申报，吞吐量提升了约 50%。**

![同样的人手，处理更多申报](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFkrFeKN4ibu44j0w5jTbMEicib3kuKlMv7HoxdGbCricxteFF0icZh7y6g8ds8DNQIicnEzZpmmlHv8YxHbppmrpOjZWrt2Rxek27iaOU/640?from=appmsg)

同样的人手，处理更多申报

其中最难的挑战之一，是自动处理出租房产的纳税申报，这花了六周的工程开发和从业者审核，才把精确率和召回率做到 90%。而这项工作沉淀下来的可复用模式，让 Tax AI 更容易扩展到其他复杂的税表上。

这些团队如今正把同样的方法用到记账、审计和 IT 支持上，构建能通过从业者反馈和真实使用不断改进的系统。

## 补上智能缺口

04

有时，更好的产品能让我们简化已经做好的东西；但也有时候，模型本身还干不了这个活。

如果我们只做今天的模型已经能做到的事，就发现不了 Research 下一步需要补上的智能缺口。

所以， **我们很多重要的合作，一开始就站在这些极限上** ，客户、FDE 和 Research 一起投入，共同攻克。

我们之前已经和一家大型电信客户一起开发了一个客服平台，他们想把它扩展到语音。

语音占了他们客服总量的约 90%。相比聊天，这类来电要靠 AI 自行解决的成本更高，还带来了一系列新的技术挑战：口音、语气，以及延迟和准确率，都要做到生产级。

做好了，会给他们的业务带来实实在在的改变。

在前期评估阶段，我们的模型在关键 eval 上只拿到了约 60% 的分数，而这些 eval 正是用来判断它能否在生产中胜任的。 **我们已经碰到了它的能力极限** ：客服场景下的函数调用和指令遵循，都需要提升。

我们把情况如实告诉了客户，并把 Research 拉进了这项工作。

FDE 和客户一起搭建平台，并定义模型需要做到什么；Research 则负责补上能力缺口，每一版新的模型快照，都能让我们对照客户的要求检验进展。

**六个月里，关键 eval 上的表现从约 60% 提升到 80%，再到 90% 以上** ，达到了上生产所需的水平。

![实时音频推理的进步](https://mmbiz.qpic.cn/mmbiz_jpg/ZKqVLiaIpzFkGTLyXJs901gGouQoyxpcqVTsibicF4UicMgyCUTKPEia6WrG2wM0BcX5XGq8jrTwtHR1UC4Au4jzhZaBt6iatH1u5b0URpleyR2HU/640?from=appmsg)

实时音频推理的进步

配图是 Audio Big Bench 准确率的变化：从 2024 年 12 月 GPT-4o Realtime 的 65.6%，到 2025 年 8 月 GPT-Realtime 的 82.8%，再到 2026 年 5 月 GPT-Realtime 2 的 92.29%。

由此得到的语音模型，如今不仅支撑着这家客户的部署，也支撑着其他定制的客服部署，以及通过 Presence 提供的托管部署。 **一个客户业务里遇到的问题，帮我们找到了能服务许多其他客户的改进。**

每一方都缺一不可。

客户愿意投入，去解决一个模型还解决不了的问题；FDE 离得足够近，能把问题定义清楚、把平台搭起来，并从头到尾推动这次合作；Research 则提升了底层模型的能力。

这是让自己「失业」的另一种方式：帮着把今天的模型解决不了的问题，变成未来的模型能够交付的能力。我们工作的回报，也远不止我们在某一个客户身上花的那些时间。

## 去找更难的问题

05

我加入 OpenAI，是为了让 AI 在人们的日常工作中真正有用，这一点到现在也还是这个团队的方向。

我经常跟团队说，在大多数 LLM 开发的场景里，奥卡姆剃刀都适用：最简单的方案就是最好的。

在一家以前沿研究著称的公司里，在一个充斥着夸大宣传的行业里， **我们想做的，是能稳定工作、让一线的人可以依赖的东西。**

我们的目标，是让每一次合作都让下一次变得更好：一个更容易部署的产品，一个能处理更难任务的模型，或者给下一个客户少一些定制工作。

如果你有想解决的难题，我们很乐意和你合作；如果你想帮忙解决这些难题，欢迎加入我们。

那么，当 Codex 已经能搞定我们花了几个月才做出来的东西时，我们该做什么呢？

**去找更难的问题。**

## Anthropic 的 FDE

06

![Anthropic](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFlPMNiaOuUuRDNpeVPwyhxNnXgjicxGsn43hKAxicJjAd1AeGa4OhmrqeHnCj5H2uDiam2zqMcliazVHibibV0dophfSBPIYuvEf0sTM0/640?from=appmsg)

Anthropic

Anthropic 也设有 FDE（Forward Deployed Engineer）岗位，归在 Applied AI 团队下。

按它的招聘 JD， **FDE 要直接嵌入最重要的客户，在客户的系统里用 Claude 做出生产级应用** ，交付 MCP 服务器、sub-agent、agent skill 这类会进入生产工作流的东西，再把可复用的部署模式总结出来，反馈给产品和工程团队。

需要注意区分的是，Anthropic 10 月初宣布的 Claude Frontier Academy 里也有个「FDE」，但 **那里的 F 是 Frontier（Frontier Deployed Engineer）** ，培养的是客户和合作伙伴自己的工程师，和 Anthropic 自己的 FDE 岗位不是一回事。

◇ ◆ ◇

![](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFnia2kLibNf3ymf7Zf8Mnia5MhopBr9qqd1kH8ELxYqUpiciaXuogtoIIATXyQW88MbNcrk4mDIkTWquBSN7Dick22ZAHp7OqBqW5Rps/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过