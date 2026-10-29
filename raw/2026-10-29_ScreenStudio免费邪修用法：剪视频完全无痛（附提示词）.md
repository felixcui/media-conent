# Screen Studio 免费邪修用法：剪视频完全无痛（附提示词）

**作者**: AI工具进化论

**来源**: https://mp.weixin.qq.com/s/fHNIanQOSNz7i4ai7SaP4A

---

## 摘要

作者分享了利用Claude Code直接解析Screen Studio工程文件、让AI自动完成视频剪辑的“邪修”方案，无需导出mp4即可读源文件重新拼接素材，并通过两次实战展示了8分钟口播剪成4分钟、自动去口水话、重组章节、抠像换背景等效果，文末附有可直接抄用的提示词。

---

## 正文

AI工具进化论 AI工具进化论

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ofvKmnZC1iaKM5vSDRL3VSXM9DRjTfuThN5ShPYtY3l80THZ4lPn2kqeTfTY8wICmzibkaXMLlq1ynVIZVfOQCvSlslOTor1cxqTiaO5dD6MhA/640?from=appmsg)

做视频，我感觉最难的地方不是拍摄，是剪辑。

作为一个没什么经验的选手，学剪辑对我来说挺有挑战的。之前用 Screen Studio 录演示视频，搞起来也很费劲：录半个小时、一个小时的视频，要花好几个小时才剪得出来。

为了剪掉口水词，我还专门在闲鱼花钱买了剪映的会员。所以我一直不太喜欢搞视频，太麻烦了。

但最近用上 Claude Code 加 Claude Opus 5.5，我觉得效果贼好，现在非常愿意去做视频。

“

我还研究出一个邪修方案：免费用 Screen Studio，剪视频完全无痛。

**录还是用 Screen Studio 录，剪辑交给 AI，让它直接读工程文件来剪。** 我的 Screen Studio 授权只能用旧版本，新版我没买，这套做法也用不到新版。一开始我什么资料都没查，是 AI 自己研究出来的。

下面详细分享一下，文末有提示词，可以直接抄。

本文看点

01

为什么是 Screen Studio

02

两次实战

03

提示词和用法

01

### 为什么是 Screen Studio

做演示和讲解视频，Screen Studio 是我用过最省心的录屏工具。

它录下来的原始画面里没有鼠标，鼠标轨迹和每次点击单独记录，导出时再画回去。开了摄像头的话，人像也单独录一路。

所以后期能做很多事：点到哪里，画面就自动放大到哪里；讲解时还能把人突出出来。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaLicvq5to3bQVvXRaIYyqe1k2pmvl2FyoBfqYFYEMRwYIDSoTPZv9fYsAKUkUooXWsbT6tMqpefSGuglcyDF5Pb4sUNLZZH2xia0/640?from=appmsg)

— Screen Studio 官网宣传图

缺点就是贵：以前买断 **89 美元** ，现在改成了订阅，按月付要 29 美元一个月。

02

### AI 自己把工程文件拆开了

我录了个测试视频，把.screenstudio 文件丢给 Claude Code，只问了一句：

「你能直接通过它的源文件帮我剪辑不，还是需要导出的 mp4？另外也可以去网上找找有没有对应的解析工具。」

不到 3 分钟，它回我：能处理，不用先导出。还顺手从源文件渲染了一段测试视频。

原来.screenstudio 就是一个普通文件夹，素材都没加密：

● 屏幕录像

原始画面，不带光标

● 摄像头

单独一路人像视频

● 麦克风

原声，外加一份降噪版

● 鼠标数据

移动轨迹、点击位置

● project.json

片段、变速、缩放等剪辑设置

素材都在，就不用在 Screen Studio 里拖时间轴了，让 AI 读这些文件重新拼一遍就行。

03

### 实战一：8 分钟口播剪成 4 分钟

我录了一段口播，讲我做的网站《高性价比人生指南》，需求是这么提的：

「内容精简一些，去掉口水话，内容可以重新组织，人物视频去掉背景，背景设为家庭，比较偏科技一点的屋子装饰；动效、数据、内容缩放，你看着办。可以先以人物为主，然后讲解的过程中主要显示桌面。音乐也可以去合成。原声能做一些增强和修复不，如果可以搞也搞搞。」

8:47 → 4:43

原片到成片

约 50 分钟

出第一版成片

成片里，口水话、重复的字和长停顿都剪掉了，内容重新排成了 6 个章节，开头先放结果做钩子。人像抠出来，换成了 AI 生成的书房背景。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaKMcTxZoOBLZS1t9LEfahTCDMew8b7m7xdAyHvPSibsrpliaTrCtpjEtOuNsYhlDsFBVGbKU41W6INQIeNUqJzEUqjLYiaUgmJtwU/640?from=appmsg)

— 说话时人物为主，旁边是数据卡片

讲到网站时，屏幕放大到左边，人缩到右下角，用的就是 Screen Studio 记下的点击放大。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaKdh3zxCaic0nndYlntB9967iaalLv4TXf9oUMkhjicR6nYLIwWX9xqUgOHRDGBHKsTmuTPqArzqh7EEOwTEK1p5KVaWUIhROjfBI/640?from=appmsg)

— 讲解时屏幕为主，人物缩到右下角

原声做了降噪和增强，背景音乐用 Suno 生成。我又让它出了一个美颜版，轻度磨皮加提亮，看着不假。

剪完它还会自己检查：把成片音频重新转录，逐句对照字幕。开头那句「大家好，我是 Ben」一度被剪没了，就是这么查出来的。

04

### 实战二：近两小时的录屏交给 Codex

今天我又用 Codex 处理了一场将近两小时的分享录屏。要求是保留完整内容，配上字幕，压到 1 GB 左右。

Codex 先研究了 GitHub 上的几个开源解析库，用其中一个读懂了我的工程，再导出、转写、加字幕。

第一版字幕一大段压在幻灯片上，我让它拆成单行短句，底部单独留一条放字幕：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaKL0oib7uwRCWFA4ZclNYHicUd12BKud0MAD0hNkq5mDib30BnEOajYiasxU7Vwdma6gFvzic1lpL5DW0rXcPKaX9WOmfDdqyCM9UvU/640?from=appmsg)

— 字幕单独占底部一条，不挡演示内容

最后 1 小时 49 分钟的完整内容，压到了 **971 MB** ，一共 1609 条短字幕。从提需求到交付大约 50 分钟，顺带还生成了飞书上的图文总结和逐字稿。

05

### 和以前比

|  | 以前 | 现在 |
| --- | --- | --- |
| 剪辑方式 | 剪映手动剪 | AI 读工程文件自动剪 |
| 花的时间 | 一小时的视频，剪好几个小时 | 8 分钟口播，约 50 分钟出片，我不用盯着 |
| 成片 | 剪得磕磕巴巴 | 基本不用大改 |
| 额外处理 | 很少做 | 降噪、换背景、美颜、字幕都能加 |
| 成本 | 剪映会员 | 每次约 2700 万 token |

剪视频其实不怎么费 token。我翻了最近的会话记录对比了一下：

• 剪一个视频：约 2700 万

• 写一篇公众号文章（含配图、排版）：1100 万到 7600 万

• 编程任务：一次网站 UI 改版约 2 亿，全面检查一个网站的代码约 5.4 亿

剪视频用的 token 里，98% 以上是缓存读取，按最贵的官方 API 价折算一次只要 4 到 9 美元。用订阅套餐的话，更加是四舍五入不要钱一样。

流程跑通、沉淀成 skill 之后，再处理类似的视频就很稳定，基本不出错。

以前剪辑是我的活，现在我只提需求、看成片。

06

### 怎么抄作业

工作流就三步：

1

用 Screen Studio 录屏幕和人像

2

把.screenstudio 工程路径交给 AI Agent

3

让 Agent 重新组织、剪辑、导出

Claude Code 和 Codex 都可以。提示词参考，路径换成你自己的：

...text

先研究这三个仓库的 README、SKILL.md 和关键解析脚本：

https://github.com/vignesh-sabhahit/screenstudio-export

https://github.com/salatech/screenstudio-to-mp4

https://github.com/shaominngqing/screenstudio-export

再检查这个本地工程：/你的路径/Demo.screenstudio

先列出画面和声音通道、时长、剪辑范围。

然后按我的要求剪辑：去掉口水话，讲解时切到屏幕，

字幕每次一行短句。先出短样片给我看，再导出全片。

不要修改原工程，结果放在单独的输出目录。

想加配音和背景音乐，我推荐语音用 **MiniMax** ，音乐用 **Suno** ，配好 API 让 Agent 直接调用。

想一条命令调用，可以把第一个库装成 Skill：

...bash

git clone https://github.com/vignesh-sabhahit/screenstudio-export.git ~/.claude/skills/screenstudio-export

Codex 装到 ~/.agents/skills/ 下面，用 $screenstudio-export 调用。

一定先让它出一段短样片，画面、声音、字幕都对了再跑全片，长视频渲染一次要十几分钟。

07

### 最后

这样我就解锁了一种「免费」使用 Screen Studio 的方式：录还是用它录，剪辑交给 AI。

市面上也有很多开源录屏软件，我还没怎么深入研究。这套工作流已经跑通了，就先分享出来，欢迎大家试试。有更好的方案，也欢迎留言交流。

END

如果这篇文章对你有帮助，欢迎点赞、在看、转发，让更多人看到。

关于作者

Ben，前古典互联网产品经理，在 AI 时代探索 AI 工具产品，以及更多可能性。

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过