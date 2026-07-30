# Sif + Claude Code + 飞书 → 搭一个电商 Agent

**作者**: 王同学

**来源**: https://mp.weixin.qq.com/s/mzDfChgdToDaXdQTKfdcjQ

---

## 摘要

本文以亚马逊ASIN销量监控为例，拆解了基于Sif MCP、Claude Code和飞书CLI搭建的业务监控Agent框架。针对AI落地中数据过时、结果不可控和幻觉三大痛点，该框架提出四要素解法：明确“监控上报”的收窄目标以提升可控性；利用MCP获取实时业务数据解决信息滞后；将稳定提示词打包为Skill固化分析流程以收敛结果波动；通过飞书同步结论并由人工最终决策来规避幻觉风险。

---

## 正文

王同学 王同学

在小说阅读器读本章

去阅读

不知道你是否有过和我一样的疑惑：每过一段时间就会看到某某 AI 新发布了突破性能力，自己也能通过自然语言让 AI 帮忙做不错的分析总结、生成高质量 PPT、甚至写一个自定义小程序玩玩… 但真正想在实际业务场景中落地赋能时，又由于 AI 大模型的生成结果不可控、引用数据过时、自我断言的 AI 幻觉等等局限性，认为 AI 还没到可落地应用的阶段？

这篇内容将以亚马逊电商日常运营中的 ASIN 销量监控为案例，拆解一个跑在实际业务里的监控 Agent——从赋能效果、框架剖析，到完整的实现流程。案例来自电商场景，但真正想分享的是背后那个可迁移的 Agent 框架：换掉数据源和同步端，它可以搬到任何“定期看数据、重复做分析、只需要重要结论”的业务场景。

## 一、先看效果：跑在业务里的监控 Agent

在亚马逊电商的日常运营中，运营人员需要持续跟踪商品的销量波动、关注核心关键词的排名与流量表现，并据此调整广告投放与促销动作。

为了减轻人工定期看数据、做表格分析等重复性工作，我们通过 Sif MCP + Claude Code + 飞书 CLI，设计了满足不同业务需求的 Agent，达到 AI 自动化提效。以 ASIN 销量波动监控为例：过去每月都要固定投入一整块人力时间在拉数据、做表、写结论上，监控的 ASIN 越多，这块投入越接近一个专职工作量——现在，这部分可以直接交给 Agent：

- AI Agent 定期从飞书多维表格读取要监控分析的任务目标；
- 通过 Sif MCP 自动获取 ASIN 销量数据，完成监控、分析、总结；
- 再通过飞书 CLI，把分析结果自动同步给运营人员做决策。

下面这张图展示了不同能力组合能达到的不同效果，比如：

1. 给到 AI Agent 销量数据，由 Claude 模型进行分析总结，Agent 将可视化分析报告上传飞书，并通过飞书消息定时向运营人员同步关键结论。
2. 给到 AI Agent 关键词状态数据，由 Claude 模型进行分析总结，Agent 监控、总结核心关键词的状态后，将紧急重要的结论同步给运营人员。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ciccdkWGpjibQaRIx1abrpSibXIRLibxldrsgfL7uClCRgYT9HecibYvOx6Aiaj4PexiaWrQYiauUkIrJdCjxfNdQNnFNU9TXnicViah2Uxt3CShd1R6c/640?wx_fmt=png&from=appmsg)

## 二、监控 Agent 框架

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ciccdkWGpjibS6sdJAcJLkcDP114SxmuUemG0U2T19HCvxmgZ17eicH9s6GcnZiaRh5OU4KyFO7TZvC4GQnXlOFPcGN1fzNGa0D23ypjrVVrLoE/640?wx_fmt=jpeg)

从上面的效果可以看出：当你明确预期想达到什么目标，能准确为 Agent 提供怎样的可靠数据，设计好如何执行分析流程，最后选对合适高效的同步方式，一个好用的监控 Agent 就成立了。这四个要素，我们拆开说说。

**明确目标：** 这个 Agent 的目标被刻意收窄为“监控 + 上报”，而不是“全自动决策”：AI 负责重复性的看数据、做分析、总结结论，判断和决策仍然留给人。目标定得越清晰、边界越明确，Agent 的产出就越可控——很多“AI 落地失败”的案例，问题出在一开始就想让 AI 包办一切。

**可靠数据：** 分析质量的上限由数据决定。通过 Sif MCP，AI 不再依赖训练语料里的过时信息，而是直接调用 Sif 的实时业务数据——销量、关键词、流量。开头提到的“引用数据过时”，在这一层就被解决了：AI 每次分析用的都是当下的真实数据。

**分析流程：** 同一份数据，AI 每次的分析结果可能不一样，这正是“生成结果不可控”的来源。解法是把流程固化：通过多轮测试打磨提示词，验证稳定后打包成 skill，之后每次执行的都是同一套经过验证的分析过程，把结果的波动收敛在可接受的范围内。Agent 的可靠性是打磨出来的，不是模型自带的。

**同步方式：** 最后一环决定了幻觉的影响半径。在这个框架里，AI 的分析结论只通过飞书同步给运营人员，由人做最终判断——AI 的“自我断言”不会直接变成业务动作。同步载体选消息、卡片还是文档，也决定了人接收关键信息的效率。

把四个要素连起来看，恰好逐一回应了开头的三个疑虑：数据过时靠 MCP 解决，结果不可控靠 skill 固化收敛，幻觉靠人把控最后一关。这也是为什么这个框架不止适用于亚马逊运营——四要素能成立的地方，它就能落地。

## 三、实现：把框架落到业务场景

实现这个 Agent，需要先备齐三个工具，各管一环：Sif MCP 管数据进来，Claude Code 管分析，飞书 CLI 管结果同步。

### 准备三件套

#### 1\. Sif MCP

Sif MCP 是连接 AI 与 Sif 数据的标准协议，让 AI 能直接调用 Sif 的销量、关键词、流量等数据做查询与分析。在 Claude Desktop 中配置：Customize → Connectors → 右上角 Add → Add custom connector，填入 Sif 提供的 URL 即可。配置细节与更多应用案例见官网：https://mcp.sif.com/

#### 2\. 飞书 CLI

飞书官方 CLI 工具，让人和 AI Agent 都能在命令行里操作飞书，覆盖消息、文档、多维表格等功能。命令行对人不算友好，但对 AI Agent 来说恰恰是最灵活的操作方式。Mac 安装： `npx @larksuite/cli@latest install` ，使用说明见官方 GitHub。

#### 3\. Claude Code

Claude Code 是整个流程的中心大脑：调用 Sif MCP 取数、执行分析、再通过飞书 CLI 同步结果。直接下载 Claude Desktop 即可，客户端内置了 Claude Code。

### 四步跑通

下面以亚马逊 Listing 下多个 ASIN 的月销量趋势监控为例，按框架四要素完整走一遍：定义任务 → 理解数据 → 打磨 AI 分析 → 配置定期同步。

#### 1\. 定义任务

由 AI 作为中心大脑，任务流程如下图——源数据对应“可靠数据”，AI 分析对应“分析流程”，同步结果对应“同步方式”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ciccdkWGpjibSSpvgCg4m6lNnMO0EiaEKR5xrye9fuhdustFOmh6mJlV7IQgQ8CPKWDiciaCRtz22FfD7tfefq5xibYI26nQTCcVyNtztnHm6iaF3w/640?wx_fmt=png&from=appmsg)

#### 2\. 理解数据

动手前，先结合 Sif MCP 官网对数据工具的解释，通过 Claude 调用与 ASIN 销量趋势相关的工具（ops\_get\_asin\_sales\_trend），确认返回的数据结构，并保存一份源数据到本地——之后的测试就不用反复调用 Sif，浪费数据额度。

#### 3\. 打磨 AI 分析

任务流程中最关键的是 AI 分析环节：对 Listing 下多个 ASIN 的历史月销量做监控和分析。为了让分析结果更稳定、更有用，我们做了多轮测试、反复优化提示词，最终让 AI 生成带可视化趋势图的 HTML 报告，并把这套分析过程打包为 skill ——之后的定期任务，每次调用的都是这套验证过的流程。

#### 4\. 配置定期任务

最后，就是通过制定定期任务由 Claude Code 将整个流程串起来： `Sif -> AI -> 飞书` ，执行的任务内容如下：

```cs
1. 用 lark-cli base 命令（--as user）读取多维表格数据（--base-token xxx --table-id xxx），列出读取到的所有ASIN2. 加载 asin-sales-trend-monitor skill，对上面的 ASIN 逐个执行销量监控分析3. 通过lark-cli drive 命令 (--as user) 将 skill 生成的 html 文件上传到飞书目录 (—-folder-token: xxx)4. 将 skill 的输出结果合并为一条飞书消息（interactive card格式),   用 lark-cli im 命令（--as bot）发到 chat_id=oc_xxx 的群。5. 完成后仅需简要确认已发送，不需要在会话中额外展开分析过程。
```

在 Claude Desktop 切到 Code 标签页，进入 Routine 配置页面，右上角选择 Local，配置本地定期任务：

![](https://mmbiz.qpic.cn/mmbiz_png/ciccdkWGpjibTiaVPeI7Hibib034ic0GNK8FJiaopbzSMMz73C9By6h3icJE5cHAUu4Cg5qcrE9oROWg5zCgwJq2ibx88okhS4XhdktNicp6FI3VgwqOo/640?wx_fmt=png&from=appmsg)

填写 Name 和 Description，把上面的任务内容粘贴进 Instructions，再按需要设置每天/每周/每月的执行时间。

![](https://mmbiz.qpic.cn/mmbiz_png/ciccdkWGpjibTtuO1k7dqgAVkicPjCqNjdx4lIgylLsBiauUz8ic0FI7xMVK5rx5Xgs303fwf4zS4aEoaibBxKOu0AKY2jN4yWjYAf3e1KepoXpX0/640?wx_fmt=png&from=appmsg)

## 四、写在最后

回到开头的疑惑。AI 从“能聊”走到“能用”，卡点往往不是模型能力，而是缺一个合适的框架：担心数据过时，就用 MCP 让 AI 直接调用实时业务数据；担心结果不可控，就把打磨好的分析流程固化成 skill；担心幻觉，就让 AI 只负责监控和上报，判断与决策留给人。

这个框架不只适用于亚马逊运营。换一个数据源、换一个同步端，有“定期看数据、重复做分析”需求的场景，都可以照这条链路搭一个自己的 Agent。

参考

https://mcp.sif.com/

https://github.com/larksuite/cli/blob/main/README.zh.md

https://code.claude.com/docs/zh-CN/desktop-quickstart

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过