# Anthropic 发布 Claude Opus 5

**来源**: https://waytoagi.feishu.cn/wiki/AKbLw6rziinuS6kzJQecEjjdnlg

---

## 摘要

Anthropic正式发布Claude Opus 5，该模型以一半的价格逼近Claude Fable 5的前沿智能水平。它在编程与知识工作评测中达到业界最佳，但网络安全任务仍落后于Mythos 5。Opus 5专为日常使用设计，运行效率高，已成为Claude Max的默认模型及Claude Pro中能力最强的模型。在相同价格下，其性能较前代Opus 4.8实现显著提升，具备极高的成本效益。

---

## 正文

# Anthropic 发布 Claude Opus 5

Anthropic 产品发布 · 2026 年 7 月 24 日

> [原文](https://www.anthropic.com/news/claude-opus-5)

<callout emoji="📌"><p>大聪明：<cite doc-id="A7aKwQMCIip5nZkFmPrcxYCMnYg" file-type="wiki" title="Opus5 官方 Prompt 指南" type="doc"></cite></p><p>卡尔：<cite doc-id="H0ycwpveiiwfc4kqiOyc9MXqnac" file-type="wiki" title="实测Claude Opus5，系统提示语删了80%，半价还能逼近Fable5。" type="doc"></cite></p></callout>

![图片展示的是Anthropic发布Claude Opus 5的相关内容。画面中，多块形状不一、大小各异的鹅卵石排列成数字“5”的形状，这些鹅卵石表面有斑点、条纹等纹理，颜色以灰、棕、绿为主，背景为浅棕色。图片位于文档中介绍Claude Opus 5发布信息的上下文之间，起到视觉过渡和强调发布主题的作用。](https://feishu.cn/file/EqpzbsGRqobuymxbOZUc4I4VnFh)

Claude Opus 5 现已发布。它审慎且主动，以一半的价格接近 Claude Fable 5 的前沿级智能。

在 [Frontier-Bench](https://www.frontierbench.ai/) 和 [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa) 等编程与知识工作评测中，Opus 5 达到新的业界最佳水平；不过在网络安全任务上，它仍落后于 Mythos 5。

Opus 5 为日常使用而设计，运行效率高于其他模型。它已成为 Claude Max 的默认模型，也是 Claude Pro 中能力最强的模型。

![图片展示了Anthropic公司Claude系列模型在不同任务上的表现。表格中对比了Opus 5、Fable 5、Opus 4.8、GPT - 5.6 Sol等模型在Agentic terminal coding、Knowledge work、Novel problem-solving等15个任务上的得分。如Opus 5在Agentic terminal coding任务中得分为43.3%，在Knowledge work任务中得分为1861分。该图与文档中对Claude Opus 5在编程与知识工作评测中达到新业界最佳水平等内容相呼应，直观呈现了其在各任务上的表现情况。](https://feishu.cn/file/JanUbA1g3obEUwxZHIpcAI35nIf)

## 性能与成本效益

Claude Opus 5 以与前代 Opus 4.8 相同的价格，提供了显著更强的性能。本节图表展示了性能如何随模型的推理强度档位变化，用户可借此在更高智能与更快、更低成本的结果之间取舍。

Opus 5 在高价值的软件工程任务上表现突出。例如，在 **Frontier-Bench v0.1** 上，Opus 5 超越所有其他模型，并以更低的单任务成本将 Opus 4.8 的性能提升至两倍以上。在 **CursorBench 3.2** 上，最高推理强度下的得分距离 Fable 5 的峰值仅差 0.5%，但单任务成本只有一半；在 high、xhigh 和 max 档位下，它也在同等成本下取得了比其他模型更高的性能。

![图片为Frontier-Bench v0.1上Agentic coding任务的得分与成本关系图。横轴为每次尝试成本（USD，对数尺度），纵轴为得分（%）。图中展示了Opus 5、Fable 5、Opus 4.8、GPT-5.6 Sol四个模型在不同努力梯度下的得分情况。其中，Opus 5在不同成本下得分均最高，且在高成本区间有明显优势。该图与上下文紧密相关，直观呈现了文档中提到的Opus 5在Frontier-Bench v0.1上超越其他模型、以更低成本提升性能等信息。](https://feishu.cn/file/WTxCbznTYoJ1EmxanhTc6nkCnjb)

![图片为CursorBench上的Agentic coding by effort level图表，展示了不同模型在不同成本下的得分情况。横轴为每任务成本（USD，对数尺度），纵轴为得分（%）。图中分别用不同颜色的点线表示Opus 5、Fable 5、Opus 4.8、GPT-5.6 Sol四个模型在不同努力等级（low、medium、high、signh、max）下的得分变化。该图与上下文紧密相关，直观呈现了在知识工作与问题求解任务上，Opus 5等模型在不同成本下的性能表现。](https://feishu.cn/file/YWB9b7t5Vox9Y2xYSlWcW1vZnXe)

![](https://feishu.cn/file/SsAobhRAJo6P29xQoiOcRZZInYe)

在知识工作与问题求解任务上，我们也观察到类似结果。例如：

- 在 **ARC-AGI 3** 上，这项评测要求模型解决新颖问题，Opus 5 的得分是第二名模型的三倍。
- 在 **Zapier AutomationBench** 上，这项评测衡量模型能否端到端完成业务任务。Opus 5 的通过率约为同等单任务成本下第二名模型的 1.5 倍；即使在最低推理强度下，它通过的任务数量也多于其他任何模型。
- 在计算机使用基准 **OSWorld 2.0** 上，Opus 5 在任意给定成本下都优于其他模型，只需略高于 Fable 5 最佳成绩三分之一的成本便可超过它。

它也是下列多项相关评测中能力最强、成本效益最高的模型。

![图片为ARC - AGI - 3在成本下的新问题解决能力图表，横轴为总评估成本（USD，对数尺度），纵轴为得分（%）。图表显示Opus 4.8（high）在成本约$10,000时得分约1%，Opus 5（high）在成本约$20,000时得分约30%，GPT - 5.6 Sol在成本约$20,000时得分约7%。该图与文档中提到的Opus 5在多项评测中能力最强、成本效益最高的内容相关，直观呈现了其在成本下的新问题解决能力表现。](https://feishu.cn/file/K3ejbpHnroEBsuxJmRLcqSGMnOg)

![图片为“Real - world knowledge tasks by effort level”图表，展示了在不同努力程度下，GDPval - AA v2模型在真实世界知识任务上的Elo得分情况。横轴为运行完整基准测试的成本（USD，对数尺度），纵轴为Elo得分。图表中用不同颜色的线条分别表示Opus 5、Fable 5、Opus 4.8、GPT - 5.6 Sol四个模型的表现，直观呈现了各模型在不同成本下的Elo得分变化趋势。](https://feishu.cn/file/MJ8abWh3lodxXVxF4wlcOGPsn2e)

![图片为“OSWorld 2.0 - 任务执行能力随成本变化的图表”，展示了不同模型在不同成本下的任务执行能力。横轴为每任务成本（USD，对数尺度），纵轴为得分（%）。图表中，Opus 5（红色）在任意成本下均优于Fable 5（黄色）、Opus 4.8（蓝色）和GPT-5.6 Sol（浅灰色）。在最低成本2美元时，Opus 5得分约20%，而Fable 5、Opus 4.8和GPT-5.6 Sol分别约10%、5%和20%。该图与文档中在OSWorld 2.0基准上评测模型能力的内容相关，直观呈现了模型成本效益。](https://feishu.cn/file/C992b13vkoi5pwx7dt2cDi2vnJh)

![图片为“多学科推理随努力程度变化图”，展示了在“人类最后考试（含工具）”中，Opus 5、Fable 5和Opus 4.8三个模型的通过率随任务成本变化的情况。横轴为任务成本（USD，对数尺度），纵轴为通过率（%）。图中以不同颜色的折线分别表示三个模型，其中Opus 5通过率最高，Fable 5次之，Opus 4.8最低。该图与文档中介绍Opus 5在多项评测中能力最强、成本效益最高的内容相关，直观呈现了其在成本与通过率方面的表现。](https://feishu.cn/file/FpN7bKkEPoT8UExpBtucmQuNnof)

![图片为“Agentic business workflows by effort”图表，展示在AutomationBench上不同模型在不同成本下的通过率。横轴为每任务成本（USD，对数尺度），纵轴为通过率（%）。图表中Opus 5（红色）、Fable 5（黄色）、Opus 4.8（蓝色）和GPT-5.6 Sol（灰色）模型通过率随成本变化。Opus 5在不同成本下通过率均高于其他模型，且在最低成本下通过率最高。该图与文档中对Opus 5在Zapier AutomationBench评测中表现的描述相呼应。](https://feishu.cn/file/WXPib7ChMoUI4IxdkK6crDv8n9d)

![图片为“Agentic search by effort level”图表，展示了不同模型在不同任务成本下的通过率。横轴为任务成本（USD，对数尺度），纵轴为通过率（%）。图中用不同颜色的折线分别表示Opus 5、Fable 5和Opus 4.8三个模型，每个模型在不同成本下有对应的通过率点。该图与文档中对Opus 5在Zapier AutomationBench评测中表现的描述相关，直观呈现了其在成本效益方面的优势。](https://feishu.cn/file/X68KbB8kPo3iW1xYycwcAgeInPe)

相较于 Opus 4.8，Opus 5 在科学研究方面也有实质进步。在我们所有生命科学评测中，它的表现都更好，覆盖结构生物学、有机化学和生物信息学等主题。其中，有机化学任务的提升尤为明显，例如根据光谱数据推断分子结构，在我们的内部基准上比 Opus 4.8 高 10.2 个百分点；在与蛋白质相关的任务中，例如预测蛋白质序列的变异会如何影响其功能，得分也高出 7.7 个百分点。

最后，Opus 5 还能生成明显更强的视觉输出：

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="LP8AbIgQZoE7l4xzOBBcgYVansb"/></figure>

《Opus 5》直观呈现了空气在符合空气动力学（及不符合空气动力学）的物体表面流动的过程。



<figure view-type="Preview"><source mime="video/mp4" origin-height="1078.000000" origin-width="1920.000000" token="SREVbsVnCoaJ2LxXbXoczrvUnbf"/></figure>

Opus 5 制作了一个简化版的交互式细胞示意图。



## 与 Claude Opus 5 协作

Claude Opus 5 在验证自身工作、谨慎迭代直至成功方面强得多。在评测和早期试用中，我们与用户发现了许多体现 Opus 5 自主性和周密性的例子：

- 在一项 Frontier-Bench 任务中，Opus 5 获得一张机械零件图，并被要求编写代码将其重建为 3D FreeCAD 模型。但该任务刻意没有给模型任何直接查看图纸的方式。Opus 5 自己编写了计算机视觉管线，从原始像素中提取几何信息，再重建出完整零件；它多次重复完成了这一任务，同样设置下的其他模型在五次尝试后仍无法解决。
- 面对一个流行开源包管理器中的真实缺陷，Opus 5 找到根因，并修复了社区补丁遗漏的一个边界情况。某个竞争模型只修复了表面症状而没有处理根因，随后便报告缺陷已解决。
- 一家交易公司的工程师在一次会话中，借助 Opus 5 为一家新交易所构建了市场数据源。即使工程师提供了详尽计划，以往模型也无法完成这项任务。由于没有可供验证的实时数据源，Opus 5 还自行搭建了测试支架，以检查代码能否正确解析交易所数据。

## 对齐与安全

*对齐。* 在部署前测试中，我们的自动化行为审计发现，Opus 5 是迄今对齐程度最高的模型，如下图所示。它比 Opus 4.8、Sonnet 5 或 Fable 5 更好地遵守 [Claude 宪法](https://www.anthropic.com/constitution)，欺骗性行为的比例最低，也最不容易被诱导用于不当用途。在避免可能造成难以逆转副作用的鲁莽行动方面，它也是目前最安全的模型。

![图片为Anthropic发布的Claude Opus 5在自动化行为审计中的失配行为得分柱状图。图中显示Opus 4.8得分为2.85，Mythos 5为2.81，Sonnet 5为3.35，Opus 5最低为2.30。该图与文档中对齐与安全部分上下文相关，用以说明在部署前测试中，Opus 5是迄今对齐程度最高的模型，其失配行为得分是近期模型中最低的，且比其他模型更不易被诱导用于不当用途。](https://feishu.cn/file/W8N2biGmxoineoxpzR9cFX7Vnln)

*图注：在自动化行为审计中，Opus 5 的整体失配行为得分为 2.3，是我们近期模型中最低的。*

*安全。* Opus 5 并未推进高风险双重用途能力的前沿。我们与私营部门和政府合作伙伴进行严格评测后发现，它在生物学研究和进攻性网络安全两方面仍落后于 Mythos 5。更多评测信息见其 [System Card](https://www.anthropic.com/claude-opus-5-system-card)。

与前代 Opus 4.8 一样，我们有意避免用网络安全任务训练 Opus 5。尽管如此，随着通用能力提升，它在这些任务上仍有显著进步；在发现网络安全漏洞方面，它已接近 Mythos 5。不过，在利用这些漏洞方面，它仍显著落后于 Mythos 5。这里的“利用”是指将漏洞转化为实质性网络威胁。

这可从 Opus 5 在 **OSS-Fuzz** 上的表现看出。我们开发了这项评测，用于衡量模型在缺少大量人工指导的情况下发现并利用漏洞的能力。Mythos 5 和 Opus 5 在发现漏洞上的成功率相近，但 Opus 5 在开发利用程序方面的得分远低于 Mythos 5。

![图片展示了Anthropic的Claude Opus 5在OSS-Fuzz评测中的表现。左侧图表为漏洞识别成功率，Opus 4.8、Mythos 5、Opus 5分别识别出61.5%、80.0%、79.4%的漏洞。右侧图表为漏洞开发利用成功率，Mythos 5成功开发13个漏洞，Opus 5仅4个。该图与上下文紧密相关，直观呈现了Opus 5在识别漏洞方面接近Mythos 5，但在开发利用程序方面成功率明显更低的情况。](https://feishu.cn/file/TkyobaaExorMIkxfo2IcMsvyncd)

*图注：在网络安全评测 OSS-Fuzz 上，Opus 5 在识别软件漏洞方面接近 Mythos 5（左），但在为漏洞开发利用程序方面的成功率明显更低（右）。*

## Opus 5 的安全防护

Claude Opus 5 的安全防护旨在支持模型在网络安全和生物学中的有益使用。它们与 Opus 4.8 的防护措施相似，只是在少数网络安全任务上增加了更强的护栏。

*网络安全。* Opus 5 的网络安全分类器比 Fable 5 上的相应分类器限制更少。它们允许 Opus 5 在源代码中寻找漏洞，但会拦截“基于二进制的”漏洞扫描，这种方式更可能与恶意行为者相关；也会拦截渗透测试和利用程序生成。

根据我们的测试，预计分类器的介入次数将比 Fable 5 少约 85%。在 [Claude.ai](http://claude.ai/redirect/website.v1.584385cd-13d1-4d35-80d2-19ac3968526f)、Claude Code 和 Claude Cowork 中，任何被标记的请求默认都会回退到 Opus 4.8。API 也可启用回退到 Opus 4.8 的机制。

我们的 [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)（CVP）可支持那些原本会被模型防护措施阻碍的网络安全工作。已加入 CVP 的企业和研究人员，可立即访问一个安全限制更少的 Opus 5 版本。

*生物学。* 由于 Opus 5 采用与 Opus 4.8 类似的一套防护措施，它现已成为我们面向科学研究公开提供的能力最强通用模型。不过，它在长周期、自主式研究任务上仍存在重要局限，而这正是我们预计 AI 模型会带来最大生物相关风险的场景。Mythos 5 在这类生物工作中仍是能力更强的模型。本次发布后，原先会在 Fable 5 上被拦截的生物学相关请求，将转而路由至 Opus 5，而非 Opus 4.8。

## 开始使用

Claude Opus 5 现已在所有平台上线，价格为每百万输入 token 5 美元、每百万输出 token 25 美元，与 Opus 4.8 相同。开发者可通过 Claude API 中的 `claude-opus-5` 开始使用。

它还提供 Fast 模式，运行速度约为默认速度的 2.5 倍。与 Opus 4.8 一样，Fast 模式在 Claude Platform 上的价格是 Opus 5 基础价格的两倍，也可通过 Claude Code 的用量额度使用。

我们还与 Opus 5 一同推出两项 Beta 更新：

- Claude Platform 的[对话中途工具变更](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)：开发者现在可以在一次对话中变更 Claude 可使用的工具，而不会使提示词缓存失效。
- API 的[自动回退](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback)：用户现在可以选择让被 Opus 5 或 Fable 5 安全分类器标记的请求自动路由至另一模型。启用自动回退后，API 请求默认会始终路由到当前可用的最佳模型，而不是被拦截。

与此前的 Opus 模型一致，Opus 5 的通用访问不要求保留数据。

如需更多关于如何充分发挥 Opus 5 能力的指导，请参阅 [提示词指南](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)。