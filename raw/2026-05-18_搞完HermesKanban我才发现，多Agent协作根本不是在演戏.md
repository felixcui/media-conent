# 搞完 Hermes Kanban 我才发现，多 Agent 协作根本不是在演戏

**作者**: 林月半子聊AI

**来源**: https://mp.weixin.qq.com/s/Bk4IlfT2sG4X5jFXxPd8iQ

---

## 摘要

林月半子聊AI 林月半子聊AI 在小说阅读器读本章 去阅读 关注 「 **林月半子的AI笔记** 」，设为「 **星标** 」 我是林月半子，教你用AI干掉90%的重复劳动 **。最近 Hermes 更新后，出了一个 Kanban 的功能。

---

## 正文

林月半子聊AI 林月半子聊AI

在小说阅读器读本章

去阅读

关注 「 **林月半子的AI笔记** 」，设为「 **星标** 」

我是林月半子，教你用AI干掉90%的重复劳动 **！**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OYSztZEeXwlDhjoKLhqYzTJFfvVibCia1orw39pREbhLvtyItE1WjpMGIwibK4M1eKiaJPUEEDuNOHIib6ERrcClWkklOD8nxhkLNU9uI2K0GKmg/640?wx_fmt=jpeg&from=appmsg)

上个月我分享过一篇 ，有好评也有讽刺，在我看来有争议才是好事，都是流量。

最近 Hermes 更新后，出了一个 Kanban 的功能。做过敏捷开发的同学应该秒懂——每天站会盯着那块白板，谁的卡片卡在哪一列，一眼就知道。

但这个 Kanban 可不是给人用的。

移动卡片的不是人，是 Agent。状态流转、失败重试、Agent 交接——全自动。思路跟之前一样，不让一个 Agent 干所有的事，把大任务拆小，分给不同角色，各干各的。

上一篇我提过，协作是能力的放大器，不是补丁。放到 Kanban 里也一样。

说实话这个操作，真的有点像团队里项目经理拆完需求，往看板上一贴，各人领各人的活。

只不过这次领活的全是 AI。

## 两个入口，同一块看板

Hermes Kanban 有两套操作方式：Agent 那边通过内置的工具函数（kanban\_create、kanban\_complete、kanban\_block 等）自动驱动看板；你这边通过 hermes kanban... 命令行或者 /kanban 斜杠命令来操作。

两套入口读写的是同一个 kanban.db，数据完全一致——Agent 在里面干活，你在外面看进度、留言、解除阻塞，互不冲突。

飞书、Discord、Telegram 这些网关里也能直接用 /kanban list、/kanban create 操作看板，不用切到终端。

🎯

如果你用过飞书的话，想象一下，你在飞书群里发一句 /kanban create "写一篇Kanban教程" --assignee writer，然后切到浏览器看 Dashboard，任务已经在看板上了，Agent 正在认领、执行。这个体感，跟你在飞书里给同事派活没什么区别。

## 从零开始：先跑通一个最简单的任务

别着急搞什么多 Agent 并行、任务依赖链。我们先从最基础的开始：创建一个任务，让一个 Agent 把它做完。

### 第一步：准备 Profile

Hermes 里的 Profile 就是你给 Agent 准备的"岗位说明书"。你想让它干什么活，就给它配什么身份。

如果你还没创建过 Profile，先建几个常用的：

```
hermes profiles create researcher   # 调研员
hermes profiles create writer       # 写手
hermes profiles create coder        # 开发者
hermes profiles create video-worker # 视频创作者
```

每个 Profile 可以配自己的技能（Skills）、工具（Tools）和记忆（Memory）。这不是今天的重点，知道有这回事就行。

### 第二步：初始化 Kanban + 启动网关

```
hermes kanban init       # 创建 kanban.db（其实这步可以省，第一次跑任何 kanban 命令都会自动初始化）
hermes gateway start     # 启动网关，里面内置了 Dispatcher（调度器）
```

💡

Dispatcher 你可以理解成一个"工头"。它每隔 60 秒扫一遍看板，看看有没有 Ready 状态的任务，有的话就分配给对应的 Agent 去干。Agent 崩了、超时了，它也负责回收和重新分配。

```
hermes dashboard         # 打开浏览器看看 Kanban 长什么样
```

六列状态从左到右：Triage（待梳理）→ Todo（待办）→ Ready（就绪）→ In Progress（进行中）→ Blocked（阻塞）→ Done（完成）。

### 第三步：创建一个任务

```
hermes kanban create "make a video about kanban" \
    --assignee video-worker \
    --tenant video-pipeline
```

这条命令做了三件事：

1. 1.在看板上新建了一张卡片
2. 2.指定 video-worker 这个 Profile 来干活
3. 3.用 --tenant 给任务打了个标签，方便按项目筛选

跑完之后，Dispatcher 下一次扫描（最多等 60 秒）就会把这个任务分配给 video-worker，然后自动启动一个 Agent 进程来执行。

你也可以点 Dashboard 上的"Nudge dispatcher"按钮，让它立刻调度，不用等。

### 如果任务被 Blocked 了

新手最容易在这里懵。你兴高采烈地创建了任务，结果一看状态——blocked。

```
hermes kanban list
Board: default (1 other board — \`hermes kanban boards list\`)

⊘ t_058c4d9c  blocked   video-worker   [video-pipeline]  make a video about kanban
```

别慌，Blocked 不是报错，是 Agent 在等你的输入。

我只说了"make a video about kanban"，Agent 不知道要什么角度、多长、给谁看，它就主动 Block 自己，在评论区留下了问题。

用 context 命令看看它到底在问什么：

```
hermes kanban context t_058c4d9c
```

输出大概长这样：

```
hermes kanbancontextt_058c4d9c
# Kanban task t_058c4d9c: make a video about kanban

Assignee:video-worker
Status:   blocked
Tenant:   video-pipeline
Workspace:scratch@/Users/<USERNAME>/.hermes/kanban/workspaces/t_058c4d9c

## Prior attempts on this task
### Attempt 1 — blocked (video-worker, 2026-05-10 20:59)
"make a video about kanban"—need spec:whatangle(intro/tips/comparison/tutorial)?duration?audiencelevel?existingsourcematerial?isthereanarticleorblogposttoconvert,orstartfrom scratch?"
```

Agent 问得挺具体的：什么角度？多长？受众什么水平？有没有现成素材？

回答它：

```
hermes kanban comment t_058c4d9c "做一个入门教程视频，时长1分钟左右，受众是完全不懂kanban的小白，基于我们之前的讨论内容来讲"
```

再解除阻塞：

```
hermes kanban unblock t_058c4d9c
```

Dispatcher 会重新调度这个任务，@video-worker 拿到你的回答后继续工作。

💡

踩坑提醒：