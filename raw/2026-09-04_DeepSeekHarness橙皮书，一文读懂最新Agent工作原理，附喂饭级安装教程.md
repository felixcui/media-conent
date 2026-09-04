# DeepSeek Harness橙皮书，一文读懂最新Agent工作原理，附喂饭级安装教程

**作者**: 智能体达人二师兄

**来源**: https://mp.weixin.qq.com/s/FrfdR9GaAIgEnM-LEO-eow?scene=1

---

## 摘要

文章介绍DeepSeek于2026年8月开源的智能体框架DeepSeek Harness，其核心理念是“万物皆插件”，将会话、沙盒、存储、调度、界面等功能全部作为插件运行。文章结合花叔发布的120页橙皮书，以“模型是厨师，harness是厨房”作类比，阐明Agent=Model+Harness的原理，并通过AI整理会议文件、统计信息并生成报告的实测案例，展示智能体查看环境、调用工具、逐步推进并验证。

---

## 正文

智能体达人二师兄 智能体达人二师兄

在小说阅读器读本章

去阅读

**关键词：** **DeepSeek Harness** ｜ **DeepSeek** ｜ **Agent** ｜ **智能体** ｜ **橙皮书** ｜ **工具调用** ｜ **Skill** ｜ **MCP** ｜ **插件**

原创｜WaytoAGI二师兄  
职场AI新视界｜2026年9月2日

![DeepSeek Harness 橙皮书与 Agent 工作台封面](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicnTO4cq06XLyricPLp2KIL6uXAvwuibL4yayGUQGsJ7D8HU9tjPxBy4BpLuhwVlLmBgI5cCQa50Eic1053eGQm0vIwz297bfDSm2w/640?from=appmsg)

## 初识DeepSeek Harness

2026年8月13日，DeepSeek 开源了 DeepSeek Harness，命令名取了三个首字母： `dsh` 。

我们大多数人平时会在浏览器打开 DeepSeek官网，或者手机APP，输入问题，页面返回答案。

这次发布的 **DeepSeek Harness** 处理的事情更接近“让 AI 到自己的电脑上做事”：它可以接触 **工作区里的文件** ，调用命令和工具，按照步骤推进任务，也可以在执行敏感操作前请求确认。

这和之前介绍的桌面端AI工具差不多。

既然都差不多，那有必要去尝试吗？

我觉得还是有必要的，因为 DeepSeek Harness 采用了一种全新的理念：

**Everything is a plugin**

全都都是插件。怎么理解呢？

官网的说明是：每项功能都是一种插件，会话、沙盒、存储、循环、调度以及用户界面。

开源后的第二天，花叔在Github上发布了名为:

《DeepSeek Harness：从开机到拆开》的橙皮书。

这份橙皮书对我们理解DeepSeek Harness有很大的帮助。

作者花叔把它装到自己的电脑上，从启动开始观察，一直看到工具调用、文件修改、权限审批、会话日志和异常复盘。

整份 PDF 实际有 120 页，里面还有完整系统提示词、 **129 行启动清单** 、三份原始会话日志，带读者“边理解边操作”。

对于刚开始接触 Agent 智能体的用户，要先了解Harness这个词。

橙皮书里有一句很适合入门的话：

> 模型是厨师，harness是厨房，会用厨房的不必是厨具工程师。

智能体要完成一项真实任务，需要模型、工具、文件、权限、记录和一套推进任务的方法。

插件工具、Skill 系统、会话管理、多 Agent调度、文件隔离、工作流等等，相当于一个智能体完成任务所需要的所有部件，或者说是形成了一种完整的功能体系。

而这种体系，就是 **Harness** 。

DeepSeek官网引用了一条著名的公式：

**Agent = Model + Harness**

而DeepSeek Harness，把这种功能体系种的各个模块，全都作为模型的插件来运行，形成了一套能为用户在自己电脑上自主完成任务的Agent智能体框架体系。

接下来，从书中的一个小场景开始，看懂这句话。

## 你让 AI 整理文件时，电脑里发生了什么

假设你的电脑里有三份会议记录，你想让 AI 做四件事：

- 找到这三份文件；
- 统计每份文件的行数和字数；
- 找出内容最多的文件；
- 把结果写成一份报告。

如果你只使用网页端的聊天平台，它可以告诉你一套整理方法，也可以给你生成一个报告模板。

它没有办法自动看到你电脑里的文件，也无法直接替你创建那份报告。

接入 **Agent** 以后，事情会多出一串实际动作：

- 它先查看当前工作区，确认里面有哪些文件。
- 接着读取文件内容，调用统计工具。
- 得到结果以后，它还要判断哪个文件最大。
- 最后创建 `report.md` ，再检查这份文件有没有真的生成。

这就是 Agent 和普通问答之间的差别：它要把一句话变成一组连续动作。

橙皮书里正好有一个类似的实测。

花叔准备了三个小文件，让 Agent 统计文件信息并写出报告。

标准模式用了 4 步、7 次工具调用、21.9 秒。

执行过程中，Agent 发现最大文件出现并列，于是在报告里补充了统计口径。

这个案例看上去很小，却把 Agent 的基本工作过程完整展示出来了：

**先理解目标，再查看环境；先做一步，再根据结果决定下一步；最后拿证据检查结果。**

如果把它画成流程，就是：

**你的要求 → 查看文件 → 调用工具 → 得到结果 → 继续判断 → 写出文件 → 检查结果**

这里的每一步都不复杂，和我们人工完成任务的步骤基本一致。

真正有变化的地方，是 **Agent 可以根据前一步的结果继续做下一步** 。

![小猪IP整理文件并生成报告](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicl5csibia6R0T0KXgmV1cSdQRzMuFoWW4066bM88Qws6hRDmeFMicEicd80icoYIpw7ssjGPoB31Nd7CHlJ00vh3BJBgHnGLYvgQXwU/640?from=appmsg)

## 分清楚Agent里的三个角色

到这里，先认识 Agent 里最基础的三个角色。

### 模型：负责想办法

模型负责 **理解你的话** ，也负责根据眼前的情况判断下一步。

你说“整理三份会议记录”，模型会把这句话拆成几个动作：找文件、读文件、做统计、写报告。

工具返回数据以后，它还要根据数据继续判断。

模型很像负责思考的那个人。

但模型本身不会凭空打开你的文件夹，也不会自动把报告保存到电脑里。

它需要一个可以行动的环境，换句话说，就是一个能让它读取文件、管理文件的操作路径和权限。

### 工具：负责具体动作

工具就是 **Agent 可以使用的具体能力** 。

打开文件、搜索内容、运行命令、创建文件，都可以被做成工具。

模型决定使用哪一个，Harness 负责把这个请求交给对应工具执行。

还是用整理会议记录来举例：

- 查看文件夹，是一个动作；
- 读取会议记录，是一个动作；
- 统计字数，是一个动作；
- 创建报告，也是一项动作。

这些动作组合起来，才让 AI 真正参与到任务里。

### Harness：负责把一切安排起来

Harness 可以理解成 **AI 的工作台** 。

它负责把模型和工具接起来，还要管理几件容易被忽略的事情：

- 当前任务使用哪个模型；
- 模型可以看到哪些内容；
- 哪些工具可以调用；
- 哪些文件可以修改；
- 敏感动作是否需要询问；
- 每一步过程怎样保存。

所以，Harness 不等于模型本身，也不等于某一件工具。它负责搭建一个让 Agent 工作的环境。

把三者放在一起，就很好理解了：

> 模型负责想，工具负责做
> 
> Harness 负责安排它们怎样一起工作

![小猪IP配置模型、工具与 Harness](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicn5ibdXlENYWia2UsHJ7xTfRknIkmSH8jrBtZlibjDJ8JuBqTniaViaQv55Cxl5RCuoSoERYfTrhG9s1AibQj5bsOggvP0nPXKfOGed4/640?from=appmsg)

这句话也能帮助你看懂 Codex、Claude Code、OpenClaw 和 DeepSeek Harness。

它们都可以使用模型和工具完成任务，差异集中在工作环境、扩展方式、权限设计和产品目标上。

## Agent 开始干活前，要先把工具准备好

前面那项“整理三份会议记录”的任务，在模型真正开始判断之前，还有一段准备工作。

DeepSeek Harness 要先连接模型，加载文件和命令工具，确定允许操作的 **文件夹** ，打开这次任务的 **会话记录** ，再把网页界面准备好。缺少其中一项，后面的任务就可能卡住。

花叔从“开机”开始观察，就是想把这段平时看不见的准备过程找出来。

橙皮书里，作者用下面这条命令导出了 DeepSeek Harness 的默认启动清单：

npx　@deepseek-ai/dsh　--profile　web　--dump-default-config　>　tree.yml

![导出 DeepSeek Harness 默认启动配置](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwiclTmwam5XcVDxRlICWJxOtIZz3NKRxCUBzGCw7rqyEJ2IXpWmrlOicgjzwpprmeKUxmkUhwGkTGibby5ibvtSAsINpHrftx7WeGQE/640?from=appmsg)

图：在终端导出默认启动配置，生成 `tree.yml` 文件

导出的清单有 **129 行** 。

你可以把它理解成“这次 Agent 开工前，系统需要准备什么”的清单。

里面有 **模型连接、会话记录、文件权限、工具、Skill、Agent Loop 和网页界面** 等内容。

它是一张工作准备表，用来说明这次任务需要哪些东西。

模型负责理解任务，工具负责打开和修改文件，权限决定它能操作到哪里，会话记录把过程保存下来，Harness 负责把这些部分接在一起。

比如工具没有加载，Agent 就无法读取会议记录；工作区指错地方，它可能找不到你要处理的文件；权限只允许查看，它可以给出修改建议，却无法写回报告；过程没有记录，出了问题就很难知道它在哪一步走偏。

这就是橙皮书要从“开机”讲起的原因。

任务还没开始， **Agent 的工作范围和手边能力** 已经被这张清单决定了一部分。

![小猪IP检查 Agent 开工前的准备清单](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicmibTYicOKqMic9oWyV0IXZPGGc0vVNo5BPmHmlzE6tRE7jWV6MoJpPUO2GiaAGKzgsCMZ5R8EibhfUtHLicFpxiaibQXXdPPbflHGibbrM/640?from=appmsg)

下面是这条命令实际导出的配置文件，它把刚才那张“准备清单”落成了一个可以查看的文件。

你不需要逐行读懂它，先看它包含哪些部分，就能理解 Agent 为什么需要一套工作台来开工。

![DeepSeek Harness 导出的 tree.yml 配置文件](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicmNfxY7FDlE1o2CXpeYkZnicW05YicCtCU3eeKzOkR9nk5BXcB6Wibkf8RYpDxV0kgrC1mEibvCf0VgPOhNOcJ6uK2TBDUVibNyBNTU/640?from=appmsg)

## 任务变复杂以后，还需要几种帮手

刚才的三份文件可以直接处理。如果你每周都要整理会议记录，就会希望 Agent 记住你的做法。

如果文件放在云盘里，就会希望它能接上云盘。如果你想替换它的某个底层零件，就需要更深一层的扩展方式。

这些需求对应三个常见名词。

### Skill：把你的做法写下来

比如你整理会议记录时，总是先找日期，再提取参会人，然后整理待办，最后检查遗漏。

把这套做法写成一份工作说明，Agent 下次就能按照同样的顺序处理。

这份工作说明叫 **Skill** 。

它像一份可以反复使用的操作手册，重点是告诉 Agent“这类事情怎么做、哪里要小心、做完怎样检查”。

### MCP：给它接一条外部通道

如果会议记录放在云盘，待办要写进项目管理软件，Agent 就需要接触电脑以外的服务。

MCP 可以先理解成一条 **通用连接** 。它帮助 Agent 接入 GitHub、数据库、知识库、云盘或其他软件。

接入以后能看到什么、能执行什么，还要看外部服务提供的能力和你授予的权限。

### 插件：更换工作台里的零件

工具解决一个具体动作，比如统计字数。插件解决的范围更大，可以增加或替换模型连接、会话保存、文件能力，甚至改变 Agent 推进任务的方式。

DeepSeek Harness 用 `everything-is-a-plugin` 描述自己的架构，也就是 **“一切皆插件”** 。

橙皮书记录的版本里，模型适配器、会话、Skill、MCP 客户端和 Agent Loop 都可以用插件方式组织。

把它们放回刚才的任务里：工具负责打开文件，Skill 负责规定整理步骤，MCP 负责连接云盘，插件负责更换工作台零件。

![小猪IP配置 Skill、MCP 和插件](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicl5ibanoZSTxRTYIYpPxnM8b5EXia2g2410ibFp9yEVmgjz0l5GYSlL8lsT4Jdr2rBNvnsjV5YyBBDhpAtGWh3ricZ49I4RjbP9S9w/640?from=appmsg)

## Agent 要动文件，谁来把门

现在 Agent 已经知道整理步骤，也有了打开和写入文件的工具。

接下来有一个必须先回答的问题：它可以动哪些文件？

橙皮书记录了三种常见 **权限范围** ：

- **只读**
	可以查看，不能修改；
- **工作区可写**
	只能在指定文件夹里修改；
- **完全访问**
	可以接触更大的文件范围。

把它想成办公室门禁就行。

第一次试用时，给它一间单独的“测试房间”，里面放几份没有敏感信息的文件。它能在里面读取、统计和生成报告，走出这个范围就要先问你。

删除文件、覆盖原文、安装软件、发送消息、调用付费服务或修改线上数据时，也建议保留人工确认。

权限的作用，是让错误停在较小的范围里。Agent 可能把路径看错，也可能误解你的要求。给它一整台电脑的权限，错误就有机会扩大；给它一个专门的测试文件夹，修正起来会轻松很多。

这里还有一个边界需要留意：文件权限主要限制它能碰哪些文件，模型服务在哪里运行、哪些内容会传到远端、外部服务有哪些权限，都需要单独确认。

![小猪IP确认 Agent 的工作区和权限](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwickgaRBuoYMoicRLQDfwblQ4D2qcSMmw23x7libHiaD6HZAIbeVkccaDOSNCHlNA4djHUptDOqibAXGnibzRy74KnGORSsZsaxsxA5sw/640?from=appmsg)

## 做完以后，怎么知道它真的做对了

任务跑完，Agent 可能告诉你：“报告已经生成。”

橙皮书记录了一次很典型的情况：Agent 修改网页以后，启动了另一台服务。

它访问这个地址得到了 HTTP 200，于是判断任务完成。

最后检查到的服务，和用户刚刚修改的目标不一致。

如果只看最后的回复，结果看起来像成功，把过程打开，才能发现它走错了地方。

这就要用到会话日志。

橙皮书里，一次很短的任务留下了 44 行记录，模型实际看到的只有 6 行。

系统把很多过程保存下来，模型每一轮只会看到当时判断所需要的那部分内容。

可以把日志想成监控录像，把模型看到的内容想成它当时站在现场看到的几段画面。

录像里可能有完整过程，现场的人只看到了其中一部分。排查问题时，两个范围都要看。

假如 Agent 总结错了一份文件，原因可能是文件没有读全、工具返回内容被截断、历史内容被压缩，或者它一开始就选错了文件。

**日志可以帮助你找到具体发生在哪一步**

因此，交给 Agent 的任务里，最好提前写清楚验收方式：

- 报告应该生成在哪个路径
- 页面应该打开哪个地址
- 哪些内容必须出现
- 哪条命令需要成功
- 最后要提供什么截图或结果。

“任务完成”是一句状态描述，文件路径、测试结果和页面截图才是可以检查的证据。

![小猪IP查看 Agent 日志和任务结果](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicnykXMXLmQBPuNFgEElhJP0ZGvnHzqgjT3F1jygHR5U3jX5pGoSFDPTWUgCtRrt2ay275UicPgCnkuKRJmVErkD47ADUtetjb7c/640?from=appmsg)

## 文件多了，它会换一种处理方式

刚才只有三份会议记录，逐个打开就够了。

假设现在有几百份日志，你只想知道哪些文件报错、每个文件出现了几次、最严重的问题是什么。

逐个把完整日志交给模型，会产生大量重复内容。

**PTC** 提供了另一种做法：让模型先写一小段程序，在电脑里批量扫描和筛选，最后只把整理后的结果交回模型。

橙皮书的一组实测里，模型直接调用工具 5 次，程序内部完成了 15 次操作。

很多中间细节留在程序里处理，模型最后接收的是更适合判断的结果。

这适合文件多、重复步骤多、最后只需要一个汇总结果的任务。

但三个小文件的对照又提醒了我们：标准模式用了 21.9 秒，PTC 模式用了 305.9 秒，两边结果都正确。

小任务没有多少重复内容，额外写程序和规划步骤反而拖慢了过程。

所以，PTC 可以理解成 **“让程序先替模型做批量筛选”** 。使用前先看任务规模，最终用实际耗时、Token 和结果质量来判断是否合适。

![小猪IP使用 PTC 模式整理文件](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwiclwJ3B5wyZkcHV9JPGRQ36riaWUcGNDxeQGYGSzRMylRictpRfl7Qnt2joVRsgtoicsLjZaL7iayGfpIvcRrKd537Q2cU6n291mibdQ/640?from=appmsg)

图：文件多、重复步骤多时，程序可以先做批量筛选

## 它可以临时多出一件工具

PTC 讲的是“让程序先处理重复步骤”。

橙皮书里还有一个更有意思的实验：Agent 能不能在任务中临时增加一件工具？

作者让 Agent 检查自己的环境，并现场制作一个叫 `count_chinese` 的工具，用来统计一段文字里的汉字数量。

任务开始时，工具清单有 **32 件** 。工具挂载完成后，清单变成 **33 件** 。

这个过程可以理解成：员工发现手边缺一把尺子，于是按照工作台的规则，临时做了一把出来，并马上用它完成当前任务。

但这把“尺子”还没有成为办公室的固定设备。它只存在于当前这次运行里：

- 没有自动生成正式插件文件；
- 没有修改长期配置；
- 重启以后不会保留；
- 没有自动进入下一次任务的工具清单。

所以，这个实验展示了 **Agent 临时增加能力** 的可能性，长期保存、测试、升级和回滚仍然需要人和系统参与。

官方提醒，创造模式里的动态代码能力应按 Bash 权限理解。

第一次尝试时，应该把它当成实验功能，在隔离目录里使用。

这也是橙皮书从“工具增加”继续往前追问的地方：Agent 可以现场解决眼前的问题，怎样把一次有效做法变成可靠、可复用、不会乱跑的长期能力，才是下一步。

![小猪IP观察 Agent 临时增加工具](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwickf1ic0LBeiaV83how1BzBE0BicIjsA8lBX0YnlbSU5nLe9y9sxsjv0BfM2hZXcpvlqib7zc0Axeh0UI4WxlHPZz2IOLMzusHKLCJs/640?from=appmsg)

## DeepSeek Harness 和 Codex、Claude Code、OpenClaw 的差别

这几个名字经常被放在一起讨论，但它们的产品目标并不相同。

### Codex：把编码任务放进准备好的工作环境

Codex 主要围绕代码库和开发任务工作，和ChatGPT合并后，工作和编码两者都能适用。

当你提出目标，它帮助查看代码、修改文件、运行检查，并把结果交付出来。

它更像一辆已经调校好的车。使用者关注的是任务能否完成，底层零件通常由产品替你准备。

### Claude Code：在终端里持续协作

Claude Code 以终端中的代码协作为主。它可以围绕项目规则、Skill、MCP 和 hooks 进行扩展，让 Agent 逐渐贴合某个代码库和工作方法。

它给使用者的自由，集中在“怎样教它工作”和“怎样把外部服务接进来”。

### OpenClaw：长期运行的个人助手

OpenClaw 更接近个人助手。它可以运行在自己的电脑或服务器上，连接聊天渠道、技能和长期工作流。

它关心代码库，也关心消息、文件、日程和持续自动化。它的重点是让 Agent 进入日常使用入口。

### DeepSeek Harness：把工作台本身交给开发者研究

DeepSeek Harness 的重点位置更底层。

它可以作为带 Web UI、工具和 Agent Loop 的开发者预览版使用，也可以作为一套可拆解的插件化框架研究。

官方把架构写成 `everything-is-a-plugin` ，模型适配器、会话、工具、Skill、MCP 客户端和 **主循环** 都被放到了可装配的结构里。

它打开的空间，集中在“怎样造一个 Agent”这一层。

这就是它最有价值的地方：开发者可以研究一个 Agent 的内部组成，甚至重新安排它的模型、工具、会话和任务循环。

代价也很清楚：

- 官方当前仍标为 Developer Preview；
- 兼容性可能发生破坏性变化；
- 第三方插件生态还在早期；
- 使用者需要自己面对更多配置、版本和权限问题。

因此，这里没有必要做一个简单的能力排名。

- 想直接完成编码任务，已经成熟的产品更省心；
- 想研究 Agent 的底层组成、开发插件或搭建自己的工作台，DeepSeek Harness 才是更值得看的对象。

说到底，需要从终端安装并启动的web端（浏览器）操作页面，始终没有一个安装包来的更省事儿

![小猪IP比较四类 Agent 的工作方式](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicnYLJUuQicut9UbQ8cmyMRpNkBfnJKNYHoJZsDxf8Oy6giamgwveq26I06xqbew7zlPeO8iaU7Vvn5c4dgMIBYg1Wx3hzGEqjKqjs/640?from=appmsg)

## 从DeepSeek Harness看 Agent 的下一步

DeepSeek Harness真正有价值的地方，还在于它让我们看见 Agent 的发展方向。

### 从回答问题，走向完成任务

聊天机器人给你一段文字，Agent 需要把结果放进文件、网页、表格或业务系统里。

以后判断它有没有用，重点会越来越接近任务是否落地，不能只看回复是否听起来聪明。

### 从固定工具，走向按需组合

Agent 会根据任务选择工具，也可能临时写程序，把多个工具组合起来使用。

工具数量多并不代表工作效果好。怎样选择、怎样组合、怎样控制错误，才是更重要的问题。

### 从临时执行，走向方法积累

Agent 做完一次任务以后，能不能把有效方法整理成 Skill、插件或工作流，会决定它能否越用越顺。

一次成功的操作只是结果，一套可以复用的方法才是积累。

### 从单次对话，走向长期协作

当 Agent 开始处理文件、消息、日程和项目，它就会遇到记忆问题：

哪些事情需要记住？哪些信息已经过期？什么时候需要重新问你？不同任务之间怎样避免互相干扰？

这些问题会决定 Agent 能不能长期进入工作和生活。

### 从“能做”，走向“出错时能停下来”

真正可靠的 Agent，需要在权限、审计、回滚和人工确认上继续进步。

它可以帮你完成大部分步骤，也要知道什么时候应该暂停，什么时候需要向你确认，什么时候应该把过程和证据交出来。

我认为，Agent 最终会同时具备两种特点：使用起来足够简单，内部过程足够清楚。用户不需要每天研究底层配置，但在任务出错时，必须有地方可以查看、判断和恢复。

## 附：喂饭级安装教程

前面的内容讲的是橙皮书和 Agent 的运行原理。

读完以后，如果你想在自己的电脑上复现，可以按照官方仓库目前给出的 Web UI 方式启动。

### 1\. 安装 Node.js

DeepSeek Harness 通过 npm 发布，电脑上需要先安装 Node.js。

打开 Node.js 中文官方下载页（浏览器搜索Node.js 即可），按照电脑系统选择安装包。

Windows、macOS 和 Linux 都可以在这个页面找到对应版本。

![Node.js 中文官方下载页面](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicnicuiaibeicCKxmzgicvrkYT3olIDw8W65ibt1v1pMcAMan5jGCuGToNk7fwGnXD5JDmNeqkmIchdUHicN22AibroCElYlOQ3LuVU2n30/640?from=appmsg)

安装完成后，打开终端（Windows电脑点击开始→搜索栏输入powershell，MacOS在应用程序中找到终端），输入：

node　-v

npx　-v

两条命令都能显示版本号，就说明基础环境已经准备好。

![在 PowerShell 中检查 Node.js 和 npx 版本](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicnWVUuDDOzaWIw2Geaic64JGicA9dtBhDf3V8dsSQbzCyFIoyvhBpU07sCXdiaKxO6z5qldFgtTTiaSKp5DpFzCFuQwnq6KltPYfpY/640?from=appmsg)

### 2\. 启动 Web UI

在终端输入：

npx　@deepseek-ai/dsh　web

第一次运行会下载所需文件，等待时间取决于网络。启动成功后，官方默认地址是：

http://127.0.0.1:3080

![确认安装 DeepSeek Harness](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicndd87xnib2spyN8kicbm6R6AJryiaKH2qAmfZlLZuz4Z1qRZUuDMws7jj6nhWb8jiaibHVo9m0h7EONoCiaGEqZgddpHUdH5SX3y7h4/640?from=appmsg)

首次启动时，终端会询问是否安装 DeepSeek Harness，输入y，按回车即可

你这次截图中实际安装的是 `@deepseek-ai/dsh@0.1.1-rc.2` 。这个版本号属于本次安装记录，后续版本可能变化。

![DeepSeek Harness 启动成功](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicm5hzYptKvllfQe7DS4CtJ29fhZQa21ae5LHMXtRrP06yQUxFu1L0aoSVeecnPRkx40Wkpmib3wjTpQUmNHmXZuIAf3Mia2VSaa0/640?from=appmsg)

终端显示本地地址 `http://127.0.0.1:3080` ，说明服务已经启动

如果浏览器没有自动打开，复制这个地址手动访问。

希望启动服务但不自动打开浏览器，可以输入：

npx　@deepseek-ai/dsh　web　--no-open

### 3\. 配置模型和 API Key

自动打开 Web UI （浏览器页面）后，根据当前版本页面提示配置可用的模型服务和 API Key。

![DeepSeek Harness 内测声明](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwickJNr2Nu6UER5ibPc1W9KmRZuyoia7q2TtSx56P4SaSItRSVLZT4P09c8Gp34L09U3Wzm6lfZHfC4WCW99AWUXz9pSYMkXib7Up4A/640?from=appmsg)

首次进入时看到的内测声明。当前项目仍处于快速迭代阶段

![在 DeepSeek Harness 中输入 API Key](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwiclX6RNe7e5aF7Xn4vavia7JicvfwiaywicMQiaibaKLD0INE3H76rAJTVqn8JDcN1I8x7FfuhW78OeDkbxDqP7I2yckjBkiaV7qEY1p4U/640?from=appmsg)

在 Harness 中添加 DeepSeek API Key

如果你还没有 Key，可以打开 DeepSeek API Keys 页面 登录并创建。API Key 只在创建时完整显示一次，复制后妥善保存，不要发到聊天窗口或提交到公开代码仓库。

![DeepSeek 网页端首页与模式入口](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwiclmPjWu9cPmvBMhnV6O69HxyVzoR2b2iciagfAdbopKq3x7njqcgiba2aSuP4rMMWWAJmKXic5rxasibDMbYdfFks3Z9YeRIRrB75hs/640?from=appmsg)

DeepSeek 网页端首页。API Key 需要在开放平台创建，网页端账号和开放平台的使用场景要分开看

![DeepSeek 开放平台首页](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwiclBrybicMREAut9rFnzOV99ovBpZx5khdlCoFrA1Zn7mfwR9MQJvTM5R5I915Fh2AN7Q7ibQYgzUBfSqLia9K8TZB8UERgFriaDwbM/640?from=appmsg)

从 DeepSeek 开放平台进入 API 相关功能

![DeepSeek 开放平台 API Keys 页面](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwickVkQF4fLOuAibY03ka90u9nBG1wISXrsmtalz6fCdrlTFw7OHIDG7jjUnzZhZiagjb74dfSQ3qUfNFkdgvm2l9wicdiadBaMgkNBw/640?from=appmsg)

在 API Keys 页面创建新的 API Key

![DeepSeek API Key 已创建](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwickNNNukvd6M0ylqfnhiaG6ToT6QhicXEf4Fllx4uzQlicdgKBz4TSTCEj2BW5XoNibK1yHjaagk0dsmJI0tIU2ejZbSxooCIKOf1F0/640?from=appmsg)

填写自己的 API Key

配置页面中还可以继续查看模型、自定义 Provider、API 地址和协议等选项。

初次使用先把官方支持的模型连接跑通，确认能正常对话后，再尝试自定义配置。

![DeepSeek Harness 模型与 Provider 设置](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicmRUOZ8b3QEHNrBx5or14fpdJ3szIGXpSL31IRLEbHpEJTvUBVCGKsIHR6R5FX4eKDVfcslt8grmFQju2acp3OlAIqA47Uicx5w/640?from=appmsg)

模型设置页面，可以查看模型、自定义 Provider、API 地址和协议等配置项

### 4\. 用测试文件夹完成第一次任务

新建一个单独的测试文件夹，名为deepseek harness，开始第一次对话

![DeepSeek Harness 新建会话](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicn4KE4HdLnenxgvxcyS8zG6v7aiajrpsUiaIZpqCGPe6OfTicmicbg9efc07JC7nhjeVDpNUb89PKs9nJ3fyfxiaO7unHXT1LiarFQkM/640?from=appmsg)

选择新会话，准备开始第一次任务

![选择 DeepSeek Harness 工作区目录](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicmkTx6cBI6PT3zA7AibdFicyc5EIb97R1tvjITYV4MVQX0DH3rYnlMU4Ka2picxCibQQKiaXgtxpFeMhNk3DHDe2sRu8yg6UUzxGluY/640?from=appmsg)

选择要交给 Agent 使用的工作区目录

![DeepSeek Harness 已选定工作区](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicnWqT2ab1O0dsgnDuvaNP9hib587OnkkyG9UZicOmaxia8YkfPGJr3mP7ia052AE6oo9iaEUhHXkPRPEqaUwtHxAzicBxmESXvcMerfU/640?from=appmsg)

工作区选定后，输入框和当前工作区信息会显示在页面中

### 5\. 观察这几个界面区域

当前版本仍在快速更新，实际页面以你安装后的截图为准。可以重点观察：

- **对话区**
	输入任务，查看模型回复和工具执行结果；
- **运行轨迹**
	查看它执行了几步、调用了哪些工具、花了多长时间；
- **模式选择**
	橙皮书记录了标准、PTC、极简和创造四种模式，第一次建议先用标准模式；
- **权限提示**
	它准备做超出当前范围的操作时，页面会要求你允许或拒绝。

通用设置里还可以看到 Agent 预设、权限、语言、外观和回车行为等选项。这些设置会影响你和它协作的方式，第一次体验建议先保持默认值，遇到具体需求再调整。

![DeepSeek Harness 通用设置](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwiclw0UDiaJXxZUnBicVuiatAaQj9yADeu3ozRQ5R2dlia4Vuic6t22BAk52O8MkaW5lbX9Kp2o7O84D66hFxzzpNU8JYsZGR3r6OqvOM/640?from=appmsg)

通用设置页面，包含 Agent 预设、权限、语言、外观和回车行为

![DeepSeek Harness 模式选择](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicn2fGtIqYHjWn5ynvB218OdjqvRFxVhruoicribVIDptw4FIYPgDqTFILdFoRc4xMRFsibcEUSGMpLKkOPHzfueFK1Eflmh7oWl0A/640?from=appmsg)

模式菜单中可以看到标准模式、PTC 模式、极简模式和创造模式

![DeepSeek Harness 模型与推理等级菜单](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicnlx9gZemwwVj516cYeqXU7MiagkI6beUfBPeLMJo7g4RuibctDiajehgVnhictjl4TatLvaviaBlDoATHOpmNQTStYcobTB2oRj0qs/640?from=appmsg)

从输入框右下角选择模型和推理等级

插件页面可以查看终端、Agent 循环、网页搜索等能力的配置，也可以浏览当前已经加载的插件。插件数量多，并不等于每个任务都需要打开；先确认任务需要什么，再决定是否调整。

![DeepSeek Harness 插件配置页面](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicm2HVWZc13CibVhRGEYbRfWWx80HDcHnzYLO6WZkcO5IwAxWIdZWN4sKc47SxzVLk56NwTMwL5nuhYc7KMEg2s4E9cmP8sCFcHU/640?from=appmsg)

插件配置页面，可以查看终端、Agent 循环和网页搜索等能力

![DeepSeek Harness 插件列表](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicnr5niaeMg06GzRf686ZWJbhEUWHkEnxemgmxy4UPI5lZpdISxPSgyibsHKXNMFeuqoX67C3K5VtGyUF8P0jh5MOPASTF9n6o5SM/640?from=appmsg)

插件列表页面。当前版本显示的数量和具体项目会随版本变化

Agent 预设页面可以切换标准、PTC、极简和创造等模式。

它们代表不同的工作方式，初次使用先从标准模式开始更容易判断结果。

![DeepSeek Harness Agent 预设](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwicnMFNG5dmSAv6nJjY9oYf6gbQHMSJPVyAAmWBaRFXM7dfjVIiaPfH4V0xIBZgq4JQ59FUPNNInfia0hhq19VCWrxjGloWJ8qkOBs/640?from=appmsg)

Agent 预设页面，可以切换不同的工作方式

![DeepSeek Harness 对话运行界面](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwiclo4v5F1ib0TwmdTHecnJH4kicXVTJHtXft6Qic7CElGLS6VkJiaIwCje138qicVzdVyl0icp6shMLyfia464qZpUn6RqYbQkJib2NmibQE/640?from=appmsg)

输入任务后，页面会显示模型回复和运行过程

### 6\. 停止服务

回到启动它的终端，按 `Ctrl+C` 停止本地服务。

![使用 Ctrl+C 停止 DeepSeek Harness 服务](https://mmbiz.qpic.cn/mmbiz_png/uiarRXYBYwickWhKFZ9xZH1V7QnjU2I7nrgAV1ibIYgYJcbI352MyDNVYIIQGfRE351icB39v0qg180Bo9DAZRjn7oIOt7tB7zJsD0pDXIeLicdg/640?from=appmsg)

在启动服务的终端按 `Ctrl+C` ，停止本地 Web 服务

如果你要从源码研究或开发插件，官方提供下面的方式：

git　clone　https://github.com/deepseek-ai/deepseek-harness.git

cd　deepseek-harness

pnpm　install

pnpm　run　build

pnpm　dsh　web

第一次体验直接使用 `npx` 就够了。等你确认产品适合自己的任务，再考虑源码和插件开发。

## 写在最后

《DeepSeek Harness：从开机到拆开》把 Agent拆成了一条可以理解的工作过程：

你提出目标，它查看环境； 它选择工具，执行动作； 它根据结果继续判断； 它可能遇到权限限制，也可能走错路径； 最后，它需要用文件、页面、数据和日志证明自己做了什么。

对于刚开接触 Agent 的人，这本书像一张地图。

你不需要先成为程序员，先看懂模型、工具、工作台、权限和记录分别负责什么，就已经迈过了最重要的一步。

对于已经在使用 Codex、Claude Code 或 OpenClaw 的人，它也提供了一面镜子：

你手里的 Agent，哪些能力由产品替你准备，哪些地方可以自己配置，出错以后能不能找到过程，值得重新检查。

DeepSeek Harness 仍处在早期阶段，使用方便程度不如其它桌面端AI工具。

严格意义上本篇内容算不上完整的教程，在往后的内容中，会给大家持续分享应用场景的实践案例

如果需要橙皮书文件，可在公众号留言

这里是「职场AI新视界」。

我是 WaytoAGI二师兄。

希望和你一起，看懂 AI 时代，也把 AI 真正用起来。

如果这篇文章对你有帮助，欢迎点赞、在看、转发。

![职场AI新视界品牌结尾卡片](https://mmbiz.qpic.cn/sz_mmbiz_png/uiarRXYBYwicliaLqrLAliaeOV0lXicmy8c5ZznpqZSbNhnAQjw85hsyERsllOlEan1QkxckzGCLicU79SVXOtEibOyQA7pF99iaaYaZfLrYNb9988Y/640?from=appmsg)

## 来源与阅读说明

1. DeepSeek Harness 官方仓库：https://github.com/deepseek-ai/deepseek-harness
2. DeepSeek Harness 官方文档：https://deepseek-harness.github.io/deepseek-harness/
3. DeepSeek Harness 橙皮书仓库：https://github.com/alchaincyf/deepseek-harness-orange-book
4. Cordis 论文入口：https://arxiv.org/abs/2608.25512

版权说明：橙皮书仓库采用 CC BY-NC-SA 4.0。若使用橙皮书封面、图表或原文截图，请保留作者与来源署名，仅作非商业使用，并按相同协议共享改编内容。

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过