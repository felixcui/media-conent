# 我给 Codex 和 Cursor 接了一条自动记忆总线

**作者**: 烟花老师

**来源**: https://mp.weixin.qq.com/s/MnqO-ueTU0yyRb-vUY-maQ

---

## 摘要

为解决 Codex 与 Cursor 协作时频繁切换导致的重复沟通与信息冗余问题，作者搭建了一条本地自动记忆总线。该机制通过 Markdown 与 JSON 文件及桥接脚本，仅共享提炼后的工作状态与稳定规则，而非完整聊天记录。阶段卡负责收束任务范围与停止条件，让 Agent 专注推理，配合严格的数据边界控制和基于文件协议的恢复点，实现了安全、高效的多 Agent 自动化协同。

---

## 正文

烟花老师 烟花老师

在小说阅读器读本章

去阅读

CODEX × CURSOR / LOCAL MEMORY BUS / AGENT ENGINEERING

最近我在用 pi agent 的源码做一组小练习。Codex 负责规划阶段、设计练习和最终 review，Cursor 留在代码现场，陪我读源码、跑测试、完成实现。

真正消耗注意力的是两边的交接。每次切换都要复制对话、重讲目标、再提醒一次边界。聊天越长，临时判断和失效信息越多，另一个 Agent 反而更难看清当前要做什么。

我在 pi-agent-practice 里加了一条本地记忆总线：几份 Markdown 和 JSON 文件、一段桥接脚本，再加上 Continue 与项目规则。它传递的是经过收束的工作状态，不传递完整聊天。

这套机制已经用于当前练习。Cursor 正在只读分析 pi-mono 的 runLoop()；我回答完理解问题后，Codex 再根据源码和报告决定是否推进下一阶段。切换应用时，不需要重新拼一段提示词。

FIELD NOTE 01

共享工作现场，不共享整段聊天

完整聊天不适合当执行合同。里面混着排查过程、错误猜测、已经过期的路径，也可能保留与最新指令冲突的旧建议。

共享层只留两类信息：

•当前阶段：正在做什么、范围到哪里、何时停止、用什么证据验收。

•稳定规则：学习偏好、模型策略、安全边界和 review 习惯。

前者放在 handoff/CURRENT\_STAGE.md，后者放在 handoff/SHARED\_MEMORY.md。优先级依次是用户最新指令、阶段卡；旧历史只在确有需要时补充。API key、token、原始 session 和其他项目背景不会进入共享层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HR8kIomiaALTo8t7eluobgLQIibWmXabpGY73Hht6YjgHNNe48GY9eojS0jjlLhU0XzFNJgNjibupicicQwhfWGxDcGOofUzZN9ycTMA4Zs1iaF8w/640?from=appmsg)

架构图：共享状态层连接 Codex 规划审查与 Cursor 工程执行

这张图概括了整套设计：Codex 和 Cursor 不需要拥有彼此的聊天记录，只要围绕同一个可读、可审查的状态层工作。

FIELD NOTE 02

阶段卡负责收束，Agent 负责推理

CURRENT\_STAGE.md 是这条总线的中心。它把目标、源码范围、当前任务、停止条件和 acceptance gate 放在同一张卡上。

当前阶段要求 Cursor 解释 runLoop() 的状态转换，并向我提出三个理解问题。卡片也写明了边界：不改代码，不解除 test.skip，不提前实现下一项练习。

这样的约束不会把 Agent 变成固定脚本。它只把推理限制在当前阶段，避免模型顺手把后面的任务也做完。对于学习场景，这一点很重要：问题要由我回答，代码要由我动手，Agent 提供解释、反例和 review。

Cursor 通过 Continue 读取项目规则与阶段卡。本地模型服务接入 Continue 后，左侧保留文件树，中间看源码，右侧放 Agent 对话。提到某个函数、tool-call id 或测试时，证据仍在同一个视野里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HR8kIomiaALQQUoiaKz44iaiboczbvIxCmvJ2iaiaCm4IgI4XYvAfzjsVsQVKowkZwqs0QK3pqs0kiboZaGKH6HOP5iaicUhZkhuicJUHnxBNRhx8syDc/640?from=appmsg)

实战布局：左侧代码，右侧 Continue，中间由共享阶段与项目规则连接

阶段结束后，Cursor 写出一份结构化 STAGE\_REPORT，列出状态、源码证据、未决问题和建议的下一道 gate。Codex 会重新检查代码、测试与事件记录，再决定推进或退回。报告只是审查入口，不能代替证据。

FIELD NOTE 03

自动化必须保留边界和恢复点

记忆自动流动以后，数据边界更需要写清楚。桥接脚本只读取经过提炼的共享文件，工具输入按不可信数据处理；发布、push、删除、读取凭证和无关网络请求都被项目规则禁止。

恢复也依赖文件协议。CURRENT\_STAGE.md 保存当前合同，SHARED\_MEMORY.md 保存稳定规则，state.json 记录 owner 与阶段，events.jsonl 留下同步事件。即使 Codex、Cursor 或插件重启，下一轮仍能从这些文件重建现场。

![](https://mmbiz.qpic.cn/mmbiz_png/HR8kIomiaALQKmQcibXpBkmdsOnOV0Lxia00CGClQJm7jZVA52eBRxpGxIL7xU0FVsic2jLapEGlmWNY7IdC160w2AXyibROvDHu8MMh0mLHl4vo/640?from=appmsg)

分层图：阶段状态、长期共享记忆、事件账本与私有边界

这里仍有一个明确的边界：Codex 到 Cursor 的阶段同步、模型路由和规则加载已经跑通；Cursor 的宿主是否稳定触发反向 hook，要看具体版本。hook 没有触发时，就退回 STAGE\_REPORT.md。没有文件或日志回读，就不宣称双向自动同步完成。

这次实践让我更确定一件事：多 Agent 协作先要统一工作状态，再考虑共享多少上下文。Markdown 和 JSON 足够朴素，diff 清楚，错误容易定位，也方便以后迁移到更复杂的状态系统。

如果你也在多个 coding agent 之间切换，可以先写一张 CURRENT\_STAGE.md：目标、范围、停止条件、验收证据。先让一次交接可执行，再决定要不要增加 hook、事件账本或模型路由。

Agent 之间值得共享的，是下一步可以继续执行的工作现场。

烟花老师 · Agent Engineering Notes

把理念落进协议、状态、测试与可恢复的工作流。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过