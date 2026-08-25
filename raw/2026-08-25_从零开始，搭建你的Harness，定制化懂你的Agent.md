# 从零开始，搭建你的 Harness，定制化懂你的 Agent

**作者**: 空格丶

**来源**: https://mp.weixin.qq.com/s/J7Cj0k8MMO4Lq955Nqwr3g

---

## 摘要

本文介绍如何从零搭建定制化的 AI Agent Harness，核心是三个 Skill：star-your-harness 通过提问生成职业化目录骨架并整理文件，better-your-harness 从安全、上下文、工具、记忆、学习五方面扫描诊断并生成 HTML 报告，view 用于可视化，帮助用户构建真正懂自己的个人 Agent。

---

## 正文

空格丶 空格丶

在小说阅读器读本章

去阅读

**DeepSeek 把 harness 带火了**

harness 是模型之外、让模型能干活的整套结构。

比如 codex、claude code、workbuddy 已经定义好的工程环境。

**还有一部分是使用 agent 的人来决定的。**

**比如模型能调用哪些文件、工具，那部分任何开源项目都给不了你。**

这块得自己动手搭。

DeepSeek Harness 再强，但它给的只是内核。

我两周前就在弄这件事了，做了几个创建Harness 的 Skill 放在 GitHub 上。

这两天周末又完善了一下。

共有三个 Skill 都是围绕 Harness 展开的。

包括 star（创建）、better（完善）、view（可视化）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFe2b8yvCoyomM4NFxm9KFjA39rO7WdP0ZoveSt5WibHhMWb4ibWibheGUt7r9TLBp3kIDDG2xl36OA7PTEYanJCEsiblFPibCoP55gEiaqibgiakVg/640?wx_fmt=png&from=appmsg)

下面分别介绍下他们怎么帮你搭建一个懂你的个人 Agent。

**01**

**star-your-harness：从零搭你的 harness**

如果你现在开始接触 Agent，刚装完 codex、workbuddy、DSH。

这个时候你面临的第一件事是，选择本地文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCoyic5Q6pK3pfpW2pON59XqqQ3uibPh921pJPfG9dtzyqZicxgYJa9X8uma0aiaRcxVn24B4QVMMkibPibQysVoD9xRXFMXkYKsjV327Q/640?wx_fmt=png&from=appmsg)

这个本地文件夹可以作为项目文件，被 Agent 读取和写入。

它的关键程度好比你给 AI 塞了一个定制化的大脑和双手。

里面你能放各种和你工作相关的文件，还有Skill、插件这类工具。

但是，通常我们电脑文件很乱，很难选择合适的项目文件。

这时候就可以从 star-your-harness 开始。

第一步安装这三个 Skill：

```
帮我安装 Skill https://github.com/SpaceZephyr/build-your-harness.git
```

第二步发送：帮我搭一个 xxx 职位的 harness

它先问你四个问题： **你是干什么的，想让 AI 帮你做什么，现在的资料散在哪，打算放哪儿。**

然后按你的职业生成目录骨架，包含入口 CLAUDE.md、about-me 上下文层、记忆层和索引、协议层、工具层，还有 gitignore 和 hooks。

最后，输出一个搭建方案，让你确认后，开始在本地创建文件，还能搜索文件做分类整理。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCozMo2bfFaQPWItkcrljK8acc7NtvmNVbn9RA9Dew7YZReUR1x9G5phCZOHCH4771gVlrdpsnQ4ibRKKuGqDBtSp4p0use1Sw5X8/640?wx_fmt=png&from=appmsg)

每个目录旁边标着它属于 harness 的哪一层。

不会对本地的文件做删除，破坏性动作一律先出方案等你确认。

**02**

**better-your-harness：给你的 harness 做体检**

如果你已经有一套本地维护好的文件夹。

就可以用 better-your-harness 这个 Skill。

它按五层扫描：安全与隐私、上下文质量、工具装备、记忆、学习。产出一份自包含的 HTML 报告，双击就能看。

我拿它扫了自己的 内容创作目录做了诊断扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCoz2lr9tO2kSbkptxia9FLSLeT5VOLYiacmGo8oHxFTCHew9BRBNGpQ5qTiaVHmmWR6tOXXRSYZRg6nDbLiaEvkfLCF1Zavib33Pju2Q/640?wx_fmt=png&from=appmsg)

总共查 **34 项** ，分五个方面。

**1）检测本地安全与隐私保护**

这里检测的范围包括`.gitignore` 有没有、覆不覆盖常见噪音、有没有明文凭证、凭证有没有被跟踪、仓库是 public 还是 private、Agent 权限开到多大。

**2）检测上下文质量**

这层是我觉得最重要的， **模型读你本地的文件到底要消耗多少tokens。**

如果你本地的文件太多，规则又很乱，每次你的Skill或者Aagent.md 都要让其去读取本地的文件夹，就会出现消耗太大的问题。

我的文件首次加载要消耗 **12878 token** 。

这是一个 Agent 从零理解这个项目、光读入口文件和各层 README 就要吃掉的量。

信噪比、目录深度、超大文件、索引里的死链，也都在这一层。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCowOqJZfwQ2FCvtaP8wSxLMb2fY4jB5TCUiaKomMSeVlGJD843jr83vg9lgNw0Nia83XXqptibVfqqm0W3ibepSib8ERCxpclXIru7GA/640?wx_fmt=png&from=appmsg)

**3）检测工具装备的数量**

Skill 装了多少、MCP 接了几个、有没有子 Agent 和自定义命令。

以及Skill 的真实调用情况分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFe2b8yvCozKaibrE1a8k7DA1xwsCViak2a589NEzjjhLgTu4rzsArXOhe0qHyTYuBM40J3Pdgam5VaA1uSbFWaTLPbO6UwXag2B6VOyOur2s/640?wx_fmt=png&from=appmsg)

**4）检测 Agent 的记忆学习**

主要检测记忆目录在不在、有没有索引、索引里有没有指向不存在文件的死链、有没有文件游离在索引之外。

有没有迭代记录和复盘、距上次提交多少天、工作区堆了多少未提交改动、Skill 还在不在更新。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCowqiaTWfkNYxNVA7GgCVnia1wwcjg8AfgRspgP1xTT0ccDMGCbIMHnx9uIFtp6TLnm4ics158qHyhAo2rKuq3wzxCgWG9DAPurkhw/640?wx_fmt=png&from=appmsg)

**5）最后给几个可以直接复制的修复提示词**

这些修复提示词，按严重度排序，每条一个按钮。点一下复制，粘给 Claude Code 或 Codex 就能修。

口令里有绝对路径、具体文件清单、验证命令，以及一句「先给我看，不要直接改」。

扫描器只报路径和变量名，任何密钥的值都不会出现在报告里。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCox75tOeCeulFBGt0X9bHqNIgO2qIhNQQRNzowibCyE3t3wChYD0qDEYwMhJwbw8A4qn126mtryv3LTIjHtoUHRlbWtyHia1IEH3w/640?wx_fmt=png&from=appmsg)

**03**

**view-your-harness：搭建你的个人工作台**

前两个回答的是我的 Harness 哪里有问题，这个回答的是我的 Harness 该怎么用

**它起一个本地服务，把你的文件夹和 Skill 变成一面卡片墙。**

这里会统计你本地项目文件共有多少个，按文档、代码、数据、图片做分类。

对于 markdown 文件可以直接预览和修改。

能够交给 AI 让其分类整理。

![](https://mmbiz.qpic.cn/mmbiz_png/CFe2b8yvCoweO1Zic7rpPq05yQN92HsquN7AocbKEpyFlA0zkzevujJEB5pllvIRcsooNGjiaER0AM4bO3HnHmkAdKyErcgBhYy2V6SNlVoHk/640?wx_fmt=png&from=appmsg)

还有一个 Skill 页，本这个项目下的 Skill 全部列出来。

统计这些 Skill 的调用次数，没用的可以直接删掉。

也可以选择调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFe2b8yvCoxEBVR4pG08P1yFibYib2B5rJicKNjLpWV24gcuae25vibmgHOvM2fzCD2IgItXHJ1UicyIUukOD7bjyj0fnng6ZnF49zmT83MoUoPw/640?wx_fmt=png&from=appmsg)

这就是你的项目文件夹的可视化展示。

也是一个简单的个人工作台。

他可以用在任意 Agent 里。

**04**

**最后**

如果你下载了 Agent，不知道怎么开始。

如果你用了 Agent 的过程中觉得它不懂你。

如果你对于操作 Agent 觉得不够便捷。

就可以使用这 3 个 skill 完善你的Harness，搭建你自己的 Agent。

有了一个属于自己的 Harness，不管换了什么 Agent，都可以让自己的工作无缝衔接。

地址：/SpaceZephyr/build-your-harness

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过