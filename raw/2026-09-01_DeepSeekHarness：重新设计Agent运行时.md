# DeepSeek Harness：重新设计 Agent 运行时

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/ihj-v64dHQR-HSzTUVBa3w

---

## 摘要

本文基于源码分析了 DeepSeek Harness（dsh）作为新 Agent 框架的核心设计。其基础循环与常规无异，但创新引入了两个特殊模式：PTC 模式将多次工具调用改写为单次程序执行以降低往返开销，创造模式允许模型在运行时动态增删自身工具。底层 Cordis 框架从时间与空间维度提供支撑。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | Cheer

导读

introduction

本文作者基于 dsh 0.1.1-rc.2 的源码阅读与试用，分享了对这一新 Agent 框架的思考。文章从最普通的 Agent 循环讲起，顺着两个"没看懂的模式"深挖：PTC 模式将模型对工具的多次调用改写为写一段程序，把五次往返压成一次；创造模式则让模型在运行中提交插件、动态增删自身工具。再往下，作者拆解了底层 Cordis 框架的时间与空间两个维度的设计。结论是：dsh 是为"持续学习"目标打造的运行时骨架，是自进化 Agent 的设计思路，尚未成为成熟的编码产品。

*全文 7559字，预计阅读时间 5 分钟*

**前言**

GEEK TALK

这篇文章不打算从架构图和源码模块开始逐项拆解，我更想沿着自己的阅读过程来讲：先从最普通的 Agent loop 看起，再顺着几个没看懂的设计一路追下去，最后聊聊我对 dsh 的一些判断。

DeepSeek Harness 发布当天，我正好在刷 X，看到后就拉下来跑了一遍。启动后看到的界面和 Codex 很像，单从 UI 上没有马上看出它的差异。也正因为这样，我开始往下翻源码，想弄明白 dsh 有什么不同。

> 阅读口径：本文基于 dsh `0.1.1-rc.2` 。除源码部分外，文中部分个人观点不等同于 DeepSeek 对 dsh 的官方定位。（也不一定对，hh）

看一个 Agent 实现，我习惯先找最本质的那一段：它的循环长什么样。

GEEK TALK

01

从 LLM loop 说起

**1.1 核心逻辑没变**

先把 Agent 说得简单一点：它本质上就是一个围绕 LLM 的循环。Agent 把工具交给模型，模型决定是否调用；如果调用，Agent 执行工具，把结果带回下一轮请求，直到模型给出最终文本。

```cs
const messages = [systemPrompt, userMessage]
while (true) {  const reply = await llm(messages, tools)  if (!reply.toolCalls.length) return reply.text  for (const call of reply.toolCalls) {    messages.push(await runTool(call))  }}
```

在一次调用里，Agent 会把规则、工具定义和对话消息一起发给 LLM；模型返回工具调用后，Agent 执行工具并将结果追加回消息，再进入下一轮请求。关于这部分，可以参考我之 [前一篇文章中的](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247606609&idx=1&sn=20ef8bf4ac3cae6de02209687b8fbdff&scene=21#wechat_redirect) 简单介绍。

把这个最小循环画出来，就是一个模型、一个工具执行器和一条回环消息链：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4eR8vZf9DMgxI0HClnHffoI0YMibk3RROWicCWUQ7QwYibpOwKJ1aEPC1Vb3du8zeYBX6m0Jjt9RovoZZ44NhUL6ldvgEdOp1CqM/640?wx_fmt=png&from=appmsg)

Codex、Claude Code，以及眼下大多数 LLM + Agent 架构，在这个最小抽象层上都差不多。

我在 `packages/core/agent-loop/src/agent.ts` 中找到了 dsh 的实现。它的基本循环并没有不同：外层按待处理输入推进 `turn` ，内层不断执行 `step` ，每一步请求模型并处理 tool call，直到模型不再调用工具。看到这里有点扑空，我本来想看看 DeepSeek 会把这段循环写成什么样。模型对外仍是“给工具、等调用、拿结果”这一套接口，单看 Agent loop，很难看出 dsh 的主要差异。

于是问题换了个方向。既然核心流程注定长一样，DeepSeek 为什么还要自己做一套 harness？

**1.2 Agent 之后要解决的是持续学习**

这个问题我一时答不上来，倒是想起梁文锋在四小时投资人会议实录中的一些观点，里面提到 DeepSeek 实现 AGI 的路径，下一步是 Agent，再下一步是持续学习：

DeepSeek 的长期 vision 是 AGI。如果把实现路线比作爬楼梯，去年那级台阶是 CoT（Chain-of-Thought，思维链），今年这级是 Agent，Agent 之后要解决的问题就是持续学习。

实现持续学习之后，可能会来到一个渐进的奇点：模型可以完成人类能做的所有事情，包括自己开发更前沿的人工智能模型。即 AI 可以加速 AI 的研究。这一步走完才是具身智能。

这里我们先做一个假设：dsh 这套 harness，就是在为持续学习这个长期目标搭建运行时基础。模型现在能执行任务、能推理，却攒不下经验；一次会话结束后，这些经验并不会自动沉淀成下一次可复用的能力。如果 Agent 以后要持续学习，harness 该怎么造？从这个方向反推，dsh 的一些取舍会好理解不少。

这里的“持续学习”并不等同于模型训练层面的持续学习，我只是把它理解成 Agent 系统能够把新能力沉淀下来，并在后续运行中继续使用。顺着这个假设往下想，Agent loop 写得再巧也解决不了这个问题，和 Codex、Claude Code 不会有本质差别。要让模型自己开发更前沿的东西，运行时得先允许它修改自己的能力边界。

带着这个想法再翻一遍 dsh，我发现了一个和其他 Agent 不太一样的地方。它出厂带四个 Agent 模式：极简模式、标准模式、PTC 模式和创造模式。标准模式和极简模式看名字相对好理解，PTC 模式和创造模式却让人有些迷惑，就从这两个看不懂的开始。

GEEK TALK

02

两个我没看懂的模式

要看懂这四个模式，先看看 dsh 启动后的模式选择页面。它们不是四种完全不同的 Agent loop，而是四套预先组合好的能力配置，每套配置决定当前会话使用哪些工具、提示词和其他运行能力。页面中的名称和定位，来自 dsh 当前版本随附的默认配置。下面先从我一开始没看懂的 PTC 模式和创造模式展开。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7TuwJfIlNfjN71b3sd0gWbnpxC5Ozjon14YmkMAzBwk3qicgUStQibOdiaGgiaav3ptIg9Em9dXnqhhL7Bx2boSzAO58s8iamUpjBs/640?wx_fmt=png&from=appmsg)

**2.1 PTC 模式：多次往返压成一次**

PTC，也就是 Programmatic Tool Calling。模型用一段程序把已有的工具组合起来，改的是调用流程，不是工具本身。

标准模式下，每个工具都可以看成一个声明好参数的函数，模型发出一个调用，拿到结果后再发下一个。单步任务这样没问题，可一旦要在一批结果上循环、按中间值走不同分支，或者并发几路再汇总，每一小步都要占掉一次完整的模型往返。

举个具体任务：找出仓库里所有写了 TODO 的文件。标准模式下的流程是这样：

```perl
模型 → grep("TODO")            → 回来 40 个文件名模型 → read(文件 1)             → 回来整个文件模型 → read(文件 2)             → 回来整个文件...
```

每一趟往返都是一次完整的请求，而且无论后续是否需要，这些中间结果都会回到上下文，占用额外空间。

PTC 模式换了个呈现方式：不再让模型通过多轮调用反复组合 `grep` 和 `read` ，只给它一个写程序的入口，工具变成程序里可以调的函数。

```javascript
const files = await tools.grep({ pattern: 'TODO' })const hits = []for (const f of files) {  const text = await tools.read({ path: f })  if (text.includes('TODO')) hits.push(f)}return hits   // 只有这一行的结果回到上下文
```

把标准模式和 PTC 模式并排放在一起，变化会更直观：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy66ib7Q245bRBHyOggaa3EJvyiccTNRnN5hfvVIvicbs6KjzWcksDcKXSYZ9aXzxw5xrg3Sx7Iiae8I9OP4RuSb4MoVsrOduW9NZrk/640?wx_fmt=png&from=appmsg)

上面这段是模型写的一段程序，dsh 在本地执行它，再把程序打印或返回的结果交回模型。这个例子里，中间读文件的结果只在程序内部使用，最终数组才交回模型。PTC 模式那份配置文件的注释写得更直白：a sequence that would be five round trips becomes one。

本质上变的不是工具，而是工具呈现给模型的方式。标准模式下每个工具都作为一个可调用的函数进请求，各自带一份参数说明，模型每一步从这张表里挑一个来调。Code Mode 为当前 Agent 提供一段类型声明放进系统提示：一个 `tools` 对象，每个工具在参数表和返回值表里各占一行，工具描述作为注释挂在旁边。请求里真正可调用的只剩一个 `run_code` ，它收两个参数，一个是程序体，一个是一句话说明这段程序要干什么。

于是模型的动作从挑一个工具发调用，变成照着那份声明写一段程序。上面那段程序里能写出 await tools.grep(...)，就是因为声明里有 grep 这一行。

这个思路来自 Cloudflare 的 Code Mode，理由是：模型见过几百万行真实代码，见过的 tool-calling 轨迹要少得多，所以它写程序比发调用更顺手。

需要留意的是，程序里的子调用没有绕过 dsh 的工具管线，仍会经过前置钩子、监控守卫、执行和结果处理；程序本身则在一个新开的 Worker 线程里运行，权限上按 bash 同级对待，并发也受到上限控制。

PTC 让模型在一次请求里把已有的能力组合起来。再往前一步，是让它往运行时里加一个原来没有的能力。

**2.2 创造模式：把挂载口交给模型**

一句话说，创造模式允许模型在运行过程中提交一个插件，把原本不存在的工具注册进当前运行时；用完或需要替换时，再停止并撤销这个插件。

整个过程可以概括成四步：先检查当前运行时，再提交插件，随后显式启动某个版本，新工具从下一轮模型请求开始可用；如果启动失败或需要改版，再停止当前版本并按需恢复旧版本。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4KV3lKmH4udEeX3dNPrRbfzibjaJTE68AvOfonic6a83iaby61ueaiaas2aic1xm7yMWaRQA0P5qbxlicOqCdTkJPEfvygWYTg44og0/640?wx_fmt=png&from=appmsg)

创造模式在标准模式的工具之外，再提供一组操作当前运行时的工具。模型先查看已有的插件和能力，发现缺口后提交一段插件代码，再显式启动需要运行的版本。

这里有个关键限制：dsh 不能单独提交一个工具，提交的单位是插件。工具只有在插件启动时才会被注册，因此插件停止时，工具也会随插件一起从工具列表中撤销。

提交和运行分成两步。提交时，运行时先保存并检查插件代码，但不会立刻执行；模型显式启动某个版本后，插件才真正运行，里面登记的新工具从下一轮模型请求开始可用。

同一个插件可以提交多个版本，运行时会记录当前启动的是哪一版。更新时先停止旧版本，再启动新版本；如果新版本失败，旧版本还保留着，但需要显式重新启动，不能自动恢复。这样模型可以先查看失败诊断，再决定继续修改还是切回旧版本。这里能回退的是插件版本和运行时登记，不是已经发生的文件、数据库或外部服务副作用。

和常见 Agent 在会话开始时固定工具表不同，dsh 允许会话进行中增加、替换和撤销工具。不过这些动态插件只存在于进程内存里，重启 dsh 后就会消失；想把结果留下来，仍然需要按常规流程把它整理成正式插件。

**2.3 先让它编排工具，再让它造工具**

两个模式并排看，方向就出来了。PTC 让模型把已有工具当函数用，自己决定怎么串、串几次，改的是编排方式；创造模式让它提交一个插件，把原来不存在的工具挂进运行时，改的是可用能力。先让 Agent 编排已有能力，再让 Agent 新增自己的能力，这可以看成自进化的两个台阶。

如果要让模型修改自己的能力边界，运行时就得允许插件在进程不重启、Agent 继续工作的过程中被加入、替换和撤销。改坏时要能清理已登记的运行时资源，换一版失败时还要保留旧版本并允许手动恢复。这样的能力不能只靠 Agent loop 里的几行逻辑补出来，得由装插件、卸插件和重新连接依赖的机制共同保证。接下来要看的，就是承载这些动态变化的插件机制。

GEEK TALK

03

dsh 的运行时设计藏在 Cordis 里

我也还在学习和研读相关设计ing。如果其中有明显的问题，欢迎指正。

**3.1 从一篇论文开始理解 Cordis**

更底层的答案不在某一个 `packages/` 插件里，而在 `vendor/` 中那套名为 Cordis 的框架；仓库里还配着一篇题为 **A Programming Paradigm for Spatiotemporal Composability** 的论文，作者来自北大和 DeepSeek。做一套 harness 为什么要配一篇论文，这件事比 loop 有意思。

Cordis 的整体设计相对复杂，本文不打算把论文和源码逐项展开，只沿着 dsh 的使用场景，分析它试图解决什么问题、核心机制如何工作，以及我对这套设计的理解。

翻开摘要，第一句就把动机说清了：

> Modern software—from plugin systems to self-evolving agent harnesses—increasingly requires dynamic composition, yet its formal foundations remain underdeveloped.

论文列了两个动机场景，一个是插件系统，另一个是会自我演化的 Agent harness。读到这里，我又想起前面引用的那段愿景：Agent 之后要解决持续学习。沿着这个方向看，自我演化的 harness 就不只是让 Agent 调用工具，还要允许它在运行过程中增加、替换和撤销自己的能力。

它把动态组合这件事拆成两个正交的维度。时间维度问的是，一个组件被移走时，它对环境做过的改动能不能全部退回去。空间维度问的是，组件之间的依赖能不能写明白、被找到，并且在依赖换人时自动重新接上。创造模式要的正是这两条：中途撤掉一个插件不能留残骸，换掉一个别人在用的组件不能把用它的人弄坏。下面两节分别顺着这两个维度看，各自的问题出在哪，Cordis 怎么答。

把这两个问题合在一张图里，Cordis 的关注点就比较清楚了：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6jySjtBFmlvECNpmXY9b8RlzU5ZFJjM6zkGhd7WoeyHWqRNDMhRjoCRA88S1OibDI9kcXND1hvCoqzLGQp1X1V0vicgZpRnZjZ0/640?wx_fmt=png&from=appmsg)

先看一个具体场景。假设有一个插件负责提供数据库，另一个插件依赖它：

```javascript
const databasePlugin = {  apply(ctx) {    const db = createDatabase()    ctx.provide('db', db)    return () => db.close()  },}
const queryPlugin = {  inject: ['db'],  apply(ctx) {    ctx.db.query('select ...')  },}
```

第一个插件启动时创建数据库连接，并把它命名为 `db` ；第二个插件声明自己需要 `db` ，启动后通过 `ctx.db` 使用它。在传统服务里，数据库升级或依赖替换，常见做法是先停掉服务，更新配置，再整体重启。进程重启会把内存中的组件和依赖一起清空，新的服务从头装配，很多运行期协调问题也就被粗粒度地绕开了。

Agent 的动态场景不总能这样处理。它可能正在等待模型返回，执行一串工具调用，或者维护着一轮还没有结束的任务。为了替换一个插件就重启整个进程，会连同这些进行中的状态一起打断。插件可能在运行中被加入、移除或替换，Cordis 要处理的就是这类进程内变化。

**3.2 时间维度：组件做过什么，如何撤销**

插件装上时可能注册事件、工具和服务，也可能创建定时器、连接或子进程。传统写法通常要求作者在另一个地方手动补齐卸载逻辑，漏掉一项，插件被移除后就可能留下仍在运行的资源。

Cordis 的做法，是要求那些需要随插件生命周期回收的操作通过 `ctx` 登记。每个插件实例都有自己的运行记录，插件通过自己的 `ctx` 注册的操作会被归到这个实例。插件卸载时，运行时就能找到这批操作并执行对应的清理函数。

```javascript
export function apply(ctx) {  ctx.on('message', handler)  ctx.effect(() => {    const timer = setInterval(poll, 1000)    return () => clearInterval(timer)  })  ctx.tools.register(myTool)}
```

这段代码里，监听器、工具和定时器都属于当前插件。插件停止时，监听器和工具登记会被撤销，定时器则执行 `ctx.effect()` 返回的清理函数。论文把这种“执行改动时，同时把对应的撤销动作交给运行时管理”的机制称为可撤销效应（revertible effect）。

它的能力边界也很明确：Cordis 能回收通过 `ctx` 登记的运行时资源，但不会自动回滚插件已经写入文件、数据库或外部服务的业务副作用。清理函数是否真的能恢复状态，仍然由插件作者负责。

**3.3 空间维度：组件依赖谁，依赖变化如何驱动生命周期**

再看数据库插件。普通依赖注入通常解决启动时“调用方拿到哪个实现”，但如果插件已经通过 `get()` 拿到了 `db v1` ，容器后来换成 `db v2` ，原插件手里的旧引用不会自动更新。

Cordis 把依赖写成插件的一条声明：

```javascript
export const inject = ['db']export function apply(ctx) {  ctx.db.query('...')}
```

`inject` 不是一次性取值，而是插件的一张运行条件清单。 `db` 还没准备好时，插件不会先启动再报错，而是保持等待； `db` 被撤销或替换时，运行时会找到声明了这项依赖的插件，让它们重新检查自己的运行条件。

这条过程可以概括成：

```shell
提供者注册 db  -> 找到声明了 db 的插件  -> 重新检查依赖是否满足  -> 依赖失效，卸载旧运行  -> 新依赖可用，重新执行插件
```

因此，数据库从 v1 换成 v2 时，Cordis 不会把新对象直接塞进旧插件，而是先结束旧的一次运行，清理旧资源，等 v2 可用后再重新执行插件。使用方重新建立的依赖视图来自新的提供者，也不会继续握着已经失效的旧连接。

这就是 Cordis 和普通依赖注入的关键差异：它不只负责“把实现交给调用方”，还把依赖变化纳入插件生命周期，负责通知使用方、停止旧运行和重新建立新运行。论文把这种机制称为响应式余效应（reactive coeffects）：组件先声明自己依赖什么，运行时在环境变化后重新判断这些依赖是否满足，并据此启动、停止或保持组件状态不变。

**3.4 回到 dsh**

dsh 的动态工具、工具表、模型服务和 Agent loop，都可以放进这种“提供能力、声明依赖、随组件生命周期装卸”的模型里。创造模式提交的不是一个孤立工具，而是一个插件，插件启动时登记工具，停止时撤销工具。

从设计上看，如果未来模型能力、调用协议或 Agent 的工作方式出现破坏兼容性的变化，dsh 可以通过替换对应插件来承接新实现，而不必把整个 Agent 运行时一起推倒重来。这里的灵活性不在于简单地换掉一个函数，而在于把变化收束到组件及其依赖关系中。

Cordis 负责的是插件如何装入、拆出、替换和重新连接，给 dsh 提供了承接这些变化的运行时机制。它不会自动解决 Agent 的提示词、工具质量、模型适配和默认工作流，这也是我把 dsh 看成“先把 Agent 的运行时骨架搭起来”的原因。

不过，论文里描述的能力模型和 dsh 当前的实际运行方式，还需要分开看。论文虽然把动态组合、撤销和依赖重连讲得很完整，但我个人试用下来，dsh 目前还没有完全实现生产意义上的热插拔。

在当前版本随附的默认配置中，只有创造模式预装了 dsh 的 Cordis 插件工具，因此模型只有在这个模式下，才能直接在运行过程中定义、启动和停止动态插件。普通的插件安装流程并不会让已经运行的 `dsh web` 自动发现并挂载新插件，通常仍然需要重启 `dsh web` 才能生效。也就是说，Cordis 在框架层面为热插拔和依赖协调提供了基础，但这套能力还没有完全贯通到 dsh 的常规插件安装和部署流程中。

距离生产意义上的“安装即生效、替换不重启、依赖变化能够自动协调”，目前还有一段距离。这也是我认为 dsh 现在更像运行时骨架，而不是成熟产品的一个原因。

**3.5 回头看四种 Agent 模式**

回到开头的模式选择页面，四个模式其实不是四套不同的 Agent loop，而是四套预先组合好的能力配置。每套配置会列出当前会话要使用的工具、提示词和其他会话能力，实际形式通常是一个目录加一份配置文件：

```bash
- id: tool-bash  name: '@deepseek-ai/dsh-tool-bash'- id: tool-presentation  name: '@deepseek-ai/dsh-agent-tool-presentation'  config:    mode: code
```

标准模式、PTC 模式、极简模式、创造模式，都是这样的能力配置。切换模式，切换的是当前会话要装入哪一套能力，而不是在一份大配置里逐项开关功能。PTC 模式额外选择了 Code Mode，创造模式则增加了操作运行时的工具，那两个一开始看不懂的模式，落到配置文件上，其实就是能力组合的差别。

这里还要区分三个层次：模式配置决定当前会话一开始带哪些能力，插件机制负责这些能力在运行过程中如何增加、替换和撤销，Agent loop 则是程序里负责驱动模型请求和工具执行的共享运行部分。切换模式只会改变能力配置，不会替换 Agent loop；如果未来要更换 loop，需要调整程序的运行配置。一份模式配置通常在程序运行期间建立一套共享的插件注册，多个会话可以复用这些工具和提示词贡献；需要按会话区分的运行状态仍由各自的 Agent 和 Session 独立保存。

**3.6 最后的判断**

最后回到持续学习这个问题：模型是否具备真正的持续学习能力，取决于训练方式、记忆机制以及模型本身的演进。dsh 目前提供的是另一层能力：让 Agent 在运行中临时增加、替换和撤销能力。动态插件只活在进程内存里，改起来快，重启后就消失；preset 则以目录和配置文件保存，后续创建的会话仍能发现和使用。两者都能改变 Agent 的能力，但生命周期不同。

这也解释了我对 dsh 当前产品状态的理解。本文分析的 `0.1.1-rc.2` 仍是预发布版本，从当前版本呈现出的完成度看，它更侧重运行时的组合和替换，距离 Codex 和 Claude Code 的完整使用体验还有差距。

不过把镜头拉回实际使用，我个人试用下来，dsh 目前的完成度和日常体验还是不如 Claude Code 和 Codex，任务执行的顺滑度、默认能力的完整性、工具组织方式以及整体可用性，前两者都更成熟。从 Agent 的核心 loop 看，大家的基本逻辑并没有拉开太大差距，体验差异更多来自工具质量、提示词、默认工作流以及各种细节的补齐和打磨。这些工作不像重写一套运行时那么显眼，却都需要长期投入。对目前还处在早期阶段的 dsh 来说，在时间有限的前提下，很难迅速追上 Codex 和 Claude Code 积累出来的完整体验。

所以我现在更倾向于把 dsh 看成面向未来的一种设计思路，而不是已经可以替代其他编码 Agent 的成品。它先把插件化、动态组合、可撤销和可重连这些基础能力的骨架搭好，后续真正决定使用感的插件内容、preset、模型适配和默认工作流，还需要继续迭代。

我的判断是，这套基础设施很适合承接未来的自进化 Agent。

如果未来的持续学习包含系统层的能力沉淀，留下来的不一定只有模型参数，也可能是一个新工具、一段角色设定、一套工作流，甚至是一整套插件组合。到那一步，自我迭代就可能表现为插件树的持续演化。

当然，这只是我基于源码阅读和实际试用形成的个人看法，不代表 dsh 的官方定位。

我的结论不是 dsh 已经实现了持续学习，而是它已经把“模型修改自己的运行时能力”做成了一个可以实际运行、撤销和替换的机制。Agent loop 只是表面上最容易看到的那一层，真正值得看的，是它周围那套允许能力持续变化的运行时。至于它什么时候能把这套骨架变成足够好用的产品，我更期待后续模型迭代，或者 dsh 正式版本发布后再重新体验。

END

**推荐阅读**

[Workspace 实践：从个人提效到组织提效](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607508&idx=1&sn=f604f409314f249297faae6d83bd3382&scene=21#wechat_redirect)

[商业客户端Harness资产管理与应用实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607453&idx=1&sn=0d0dc5f97c286cb80c48a42a7bbf654f&scene=21#wechat_redirect)

[小度为什么越来越懂你？一套 Agent 研发闭环的诞生](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607435&idx=1&sn=f3d5edccff2fbb03206fcb232246959c&scene=21#wechat_redirect)

[从分散提效到 AI Native 组织的实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607411&idx=1&sn=5cb281a28a76a39ea5556059164d102b&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过