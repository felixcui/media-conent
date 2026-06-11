# Loop Engineering：设计一个循环让Agent自己跑

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/StYj_Z3ieUB7nWMzRE1isQ

---

## 摘要

Loop Engineering标志着AI编程Agent的使用从手动写提示词转向设计自动化循环系统，让Agent自主找活干、检查结果并推进进度。该系统由五个构建块与一个记忆层组成：自动化实现持续执行，工作树解决多Agent并行文件冲突，技能通过固化意图避免冷启动以累积知识，插件和连接器使Agent能操作真实外部工具，子Agent则处理细分任务。这彻底改变了人机协作模式。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

Addy Osmani 发了一篇长文，讲的是一个新名词：Loop Engineering。他指出一个正在从"写提示词"转向"设计循环系统"的趋势。

> "你不应该再手动给编程 Agent 写提示词了。你应该设计一个循环，让循环去提示 Agent。"

在此之前boris就表达过这样的观点： [Claude Code 作者Boris：我已经不写 prompt 了，我写 loop](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461159971&idx=1&sn=e2bc19c9e13cfd493b89a0194440457c&scene=21#wechat_redirect)

今天这篇文章更系统的介绍了这一观点。

## 之前和现在

过去两年，你用编程 Agent 的方式很简单：写一条好提示，塞够上下文，等它输出，你再写下一条。Agent 是工具，你全程握着它，一轮接一轮。

现在不一样了。你构建一个小系统——它自己找活干、分配任务、检查结果、记录进度、决定下一步。你不再亲自戳 Agent，系统替你做这件事。

Osmani 把这件事分成 **五个构建块 + 一个记忆层** 。有意思的是，Codex 和 Claude Code 现在都支持这全部六样东西，只是名字不同。

## 五个构建块

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ8TZ6XZxokMJRvTuhHxXfOAjLWuq6f1hrpicE52VqAZXQD6CbcQ5rRKibX5icIrMZenpvLyNojrDvHfyzaPGhP02yyFQk4Begd0Jk/640?wx_fmt=jpeg)

**1\. 自动化（Automations）——心跳**

让循环真正循环起来的东西。不是跑一次就完事，而是按计划自动执行。

Codex 的 Automations tab 里，你选项目、写提示、设频率，跑出结果进 Triage 收件箱，没结果自动归档。OpenAI 内部用它做日常 issue 分类、汇总 CI 失败、写 commit 简报、抓上周引入的 bug。

Claude Code 通过 `/loop` 、cron 任务、hooks 和 GitHub Actions 实现同样的事。 `/goal` 更狠——你写一个条件（比如"test/auth 下所有测试通过且 lint 干净"），它一直跑到条件满足才停，而且每次迭代由一个独立的小模型判断是否完成，不是写代码的那个自己打分。

**2\. 工作树（Worktrees）——并行不打架**

同时跑多个 Agent 时，文件冲突是最大的坑。两个 Agent 写同一个文件，跟两个工程师改同一行代码没区别。

git worktree 解决这个问题——每个 Agent 有自己的独立工作目录，共享同一个仓库历史，但编辑互不干扰。Codex 内建支持，Claude Code 用 `--worktree` 标志或 `isolation: worktree` 配置实现。

但 Osmani 提醒： **工具解决了机械冲突，你才是真正的瓶颈** ——你的审查带宽决定了能并行跑多少个，不是工具。

**3\. 技能（Skills）——不用每次都从头解释项目**

每次新会话都要重新解释项目上下文，像金鱼一样。Skill 就是干这个的。

格式很简单：一个文件夹，里面放 `SKILL.md` 描述指令和元数据，再加可选脚本、参考文件、资源。Codex 用 `$` 或 `/skills` 调用，Claude Code 也一样。

Osmani 之前提过"意图债务"（intent debt）——Agent 每次启动都是冷启动，你的意图有漏洞它就自信地猜。Skill 就是把意图写在外面，写一次，每次运行都读到。没有 Skill，循环每次从零推导整个项目；有了 Skill，知识会累积。

**4\. 插件和连接器（Plugins & Connectors）——触达真实工具**

只能看文件系统的循环是弱小的。基于 MCP 的连接器让 Agent 读 issue 跟踪器、查数据库、调 staging API、往 Slack 发消息。

Codex 和 Claude Code 都支持 MCP，所以给一个写的连接器通常另一个也能用。插件把连接器和技能打包，队友一次安装就能用上你整套配置。

这决定了 Agent 是说"这是修复方案"，还是自己开 PR、关联 Linear 工单、CI 绿了自动在频道里@人。

**5\. 子 Agent（Sub-agents）——写代码的和检查的分开**

循环里最有价值的结构设计。写代码的模型给自己打分太宽容了。第二个 Agent 用不同的指令、甚至不同的模型，来抓第一个自己骗过自己的地方。

Codex 用 `.codex/agents/` 下的 TOML 文件定义子 Agent，可以指定模型和推理强度。Claude Code 用 `.claude/agents/` 和 agent teams。

通常的分工：一个探索，一个实现，一个对照规范验证。在无人值守的循环里，一个你信得过的验证者是你敢走开的唯一理由。

**+1. 状态（State）——第六样东西**

一个 Markdown 文件，或者 Linear 看板——任何活在单次对话之外的东西，记录做了什么、下一步做什么。

听起来太简单了，但每个长期运行的 Agent 都依赖这个技巧。 **模型在两次运行之间会忘记一切，所以状态必须存在磁盘上，而不是上下文里。** Agent 会忘，仓库不会。

## 一个循环长什么样

Osmani 分享了一个他常用的模式：

每天早上自动化跑一次。提示词调用一个 triage skill，读取昨天的 CI 失败、打开的 issue、最近的 commit，把发现写进 Markdown 或 Linear。每个值得做的发现，开一个独立的工作树，派子 Agent 起草修复，第二个子 Agent 对照项目 skills 和现有测试审查。连接器让循环自己开 PR、更新工单。循环处理不了的，进 Triage 收件箱等你。

你只设计了一次。你没有手动提示任何一步。

## 循环解决不了的事

Osmani 很清醒地列出了三个会变得更尖锐的问题：

**验证还是你的责任。** 无人值守的循环也是无人值守地犯错。把验证者从写代码的分开只是让"做完了"更有意义一点，但"做完了"是声称，不是证明。

**你的理解会退化。** 循环越快地产出你没写的代码，你实际理解的东西和代码库之间的差距就越大。这是"理解债务"（comprehension debt），顺畅的循环只会让它增长更快——除非你读循环产出的东西。

**认知投降。** 循环自己跑的时候，很容易停止有自己的判断，拿什么是什么。设计循环，如果你带着判断力去做，它是解药；如果你用它来逃避思考，它是催化剂。

小结  

这篇文章最有价值的部分不是那五个构建块——这些东西文档里都有。它真正点破的是： **杠杆点已经移动了。**

Bcherny 说"我不再提示 Claude 了，我写循环"，不是说工作变轻松了，是说发力点变了。两个不同的人搭出完全一样的循环，结果可能完全相反。一个用它加速自己深度理解的工作，另一个用它逃避理解工作本身。循环不知道区别。你知道。

这就是为什么循环设计比提示工程更难，而不是更容易。

最后 Osmani 的结语很克制，我直接引用：

> Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go.（设计循环。但要像一个打算继续当工程师的人那样去设计，而不是一个只负责按按钮的人。）

附：关于 token 成本，之前文章就有争议，这是模型厂商为了卖token融资上市造势！

有人说"这是让钱从你账户里流出去的好方法"，有人说"有无限 token 的人教大家搞循环，其他人被 Pro 计划的周限额逼到用 API"。Osmani 承认自己也是有限计划用户，说需要现实一点：循环能推多远，取决于你的 token 预算。

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过