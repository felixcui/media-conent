# 新项目完结！AI 智能 PPT 生成 Agent

**作者**: 程序员鱼皮

**来源**: https://mp.weixin.qq.com/s/g9U5hpv3fnMXeeoM4VAjsw

---

## 摘要

程序员鱼皮宣布编程导航新项目教程《AI 智能 PPT 生成器》完结。该项目以 AI 工程化、工作流和异步任务编排为核心，基于 FastAPI、LangChain、LangGraph 与 React 开发。用户输入主题、粘贴长文本或上传文档后，由 DeepSeek 等 AI 先生成可修改的大纲，确认后异步并发生成各页内容，经 Redis 与 SSE 实时推送进度，支持单页重试与取消，最终导出原生可编。

---

## 正文

程序员鱼皮 程序员鱼皮

在小说阅读器读本章

去阅读

大家好，我是程序员鱼皮。

又经过了一段时间的爆肝，我在编程导航的保姆级新项目教程《AI 智能 PPT 生成器》，完结啦！

这是一套以 **AI 工程化 + 工作流 + 异步任务编排** 为核心的全栈项目教程，基于 Python FastAPI + LangChain + LangGraph + React 开发。用户只需要输入一句主题、粘贴一段长文本，或者上传一份文档，就能通过 DeepSeek 等 AI 生成一份可修改的 PPT 大纲，然后并发生成完整页面，最终导出原生可编辑的 PPTX 文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Gia39k6B4VYILFSIaAd4sHLOlRwXYvSqpebtoVdeXZC0rXYG0iapkbVmUE2aJaD8hcDwFq8wq2MSPloSvibPEt2hsqlDHfUiaB0qs/640?wx_fmt=png&from=appmsg)

每一期文字教程都详细讲解了设计决策和实现细节，让你不只会做，还知道为什么这么做。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FxTffGOVlTxr35mKKaMOxh6icEHbRYA39mlyeDHeVIv5qksmSWuEiaK74IMraEaZnAx4XqlRozqGPMbB55QoDVfpkJMFMIwNbP8/640?wx_fmt=png&from=appmsg)

这还不够，每个项目我都写了详细的简历写法和面试题解，做完项目直接写到简历上、突击面试，一条龙服务！

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1F1nvNgic1O9c64ODWIaiaGal8A69VrXcVJMToKSicKsyxvalb5TvxUQ2VrlJ2MF0Ribv2moSB9eic5B2OST5iaH0IOibeeeeT3A1ibfFc/640?wx_fmt=png&from=appmsg)

真心换真心，我做项目教程的付出也得到了大家的认可，也帮很多同学拿到了大厂 offer~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Gic45w63thL1jwgjlrP7Egn9T1LjBgzW2v4rbyzeuiaZ02oTBkZ9OibjSWpg4pWGFUd5yRuMF0rE8K4YE6g4tMROjibicbDouZGxVc/640?wx_fmt=png&from=appmsg)

接下来鱼皮给大家快速介绍这个项目，希望让更多需要它的同学看到，把它变成自己的项目。

秋招正处于黄金时段，简历上写满前沿技术，不仅求职有底气，做项目的能力也会大幅提升！

**🧧 后文有加入学习的方式，千万不要错过！**

## 项目介绍

项目有 4 大核心能力。

1）多种输入方式，自动生成大纲

项目支持从主题、长文本和文档三种入口创建 PPT，用户可以自由控制页数、排版模式、文字量、语气和目标受众。系统不会跳过用户直接生成最终页面，而是先生成一份结构化的大纲，包括每页的标题、页面目标和核心要点，你可以随意修改内容、增删页面、调整顺序，确认满意后再开始生成。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GJPtKTxWnqybQHu3ZBrTJcee0icnMITkaO2EkQkHeibMW63YDQEgZWKPWiaiaicqwgWhH80JibAJChcHMUCSN4ibPjAbLu3U747PPT5c/640?wx_fmt=png&from=appmsg)

2）异步并发生成，实时推送进度

一份 10 页的 PPT 如果串行调用模型，很容易让用户等上一分钟以上。项目把每一页拆成独立的任务，通过 ARQ Worker 并发执行，用 Redis 保存任务状态并传递事件，前端通过 SSE 实时接收生成进度。

生成过程中，已经完成的页面可以立即预览，失败的页面可以单独重试，用户也可以随时软取消剩余任务，不需要整份重来。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EkLKiaFhzyIB0cWXoib5l5Kh32ibvFc4dTHSv5wtVCOb1opAhwZBcotg4hAYmjpnXYDpMcdQ5VbBGYSIaApBicIp4bVXe3QypZogk/640?wx_fmt=png&from=appmsg)

3）功能完善的在线编辑器

生成完成后进入在线编辑器，左侧是页面缩略图，中间是 16:9 的画布区域，右侧提供 AI 修改、主题切换、版式选择和图片管理四个面板。

文字内容支持直接编辑，灵活排版的页面可以拖动分隔线调整内容块尺寸，也支持跨容器移动和更换排布方式。切换主题后，Web 预览和 PPTX 导出会读取同一份主题数据，保证效果完全一致。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H2D9qZYbRhIrzIh6qj831tbrXUrRFmLbYmSRZTZKmYicRJ6E6n7KAXiaicYA002qMAWmyxeRSVvycUlp3beGerQJic8LlIEicTDANk/640?wx_fmt=png&from=appmsg)

4）原生可编辑的 PPTX 导出

AI 输出的文字长度不可预测，直接导出很容易出现文字溢出、缺页或整页被渲染成图片的问题。项目在导出前会自动检查结构、文字占用、数字来源和页面边界，将问题分成 error 和 warning 两个级别，error 会阻断导出，warning 则提醒用户核对但允许继续。

通过检查后，后端用 python-pptx 逐块构造文本框、表格、图表和图片，再回读生成的文件进行验证。最终得到的 PPTX 不是一张铺满全页的截图，而是每个元素都能继续修改的原生对象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EPWsIXs8tcw5Zgr2WItiaSTGqa2b2bOujahCIGbpEtK8AiaIyuJkibrDicYygYQ8ibDZu3fLTEeoHZmemwibYMw7KjHCZ0v5NtGj80Y/640?wx_fmt=png&from=appmsg)

学会这个项目后，你不仅能做出一个 AI 智能 PPT 工具，还能完整解释它为什么这样设计、哪里容易失败，以及怎样把一个模型 Demo 做成可持续运行的工程项目。这些经验可以复用到任何 AI 全栈项目中，绝对让你收获满满！

而且为了让更多同学参与学习，我直接把所有代码 **完整开源** ！能力强的同学可以自学，点个 star 就算对鱼皮的支持啦~

> 开源仓库：https://github.com/yuyuanweb/ai-ppt-generator

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HSIDShnFzoxEy5TYtesyCVDrRYAHmvhDDcHWJibiaibGpe209iaYqxMskCaUzdSQ1fFP2KWb1bUAf95jia9YfFuyNhyLGxEjcu7RnI/640?wx_fmt=png&from=appmsg)

## 项目收获

本项目选题新颖，紧跟 AI 工程化时代，以 **实用工具 + 完整工程** 为导向。区别于增删改查的烂大街项目，这套教程讲解的是一个经过市场验证的完整项目，重点不是带你照着代码从零敲一遍，而是把每个关键决策背后的动机、替代方案和踩坑讲清楚，快速给你的简历和求职大幅增加竞争力！

项目内容精炼， **不到一周就能学完** ，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力！

Python 后端 + LangChain + LangGraph + React + 企业级 AI 应用开发，技术丰富，学完后在 AI 工程化、异步编排、文档渲染、前端编辑器、工程质量 5 个方向都能获得完整实践。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GRpAWgLmycDkKm66P0q8O0iaq4zs49neJECPKfhzFI8L5XIhb4LvaRo06j6ziaAbR8svRp85OQDlQhIEYvzsgXsaicn7MjFnojkg/640?wx_fmt=png&from=appmsg)

鱼皮给大家讲的是 **完整的 AI 工程化实践和从模型调用到产品交付的全流程** ，从这个项目中你可以学到：

- 如何基于 LangChain 实现 AI 结构化输出，保证模型输出始终可用？
- 如何基于 LangGraph 构建自纠环工作流，系统性提升单页生成质量？
- 如何设计 AI 工具调用机制，让模型快速修改页面？
- 如何使用 ARQ 实现页级并发生成，控制模型调用频率？
- 如何通过 Redis + SSE 实现实时进度推送和断线重连恢复？
- 如何设计内容、布局、主题三分离的数据模型，让 Web 和 PPTX 同源渲染？
- 如何构造原生可编辑的 PPTX，处理中文字体和 emoji？
- 如何实现结构化编辑器，保证光标稳定？
- 如何通过乐观锁 + 按页串行保存队列处理编辑冲突？
- 如何实现字形级文字溢出检测和分级门禁？
- 如何快速生成前端 TypeScript 类型，消灭前后端接口不一致？
- 如何实现 PPT 灵活排版，并保证前后端求解器双端一致？

此外，还能学会很多 AI 工程化、系统架构设计、技术方案对比的方法，提升排查问题、自主解决 Bug 的能力。每一期还附带了项目的扩展方向，有能力的同学可以进一步拉开和别人的区分度，无限进步！

满满的项目正反馈：

![编程导航 26 年报喜](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GGeYvVKKeAS2qS8MuSykeBUdoMtA6fGJ76L05PsEl48IHcAn9wmDClf22TyicKWqAicZATY9P9w9xkHLFSgs8fr04WHG3Bj7icHo/640?wx_fmt=png&from=appmsg)

编程导航 26 年报喜

除视频教程外，鱼皮编程导航的项目还提供：

| 教程资料 | 求职助力 |
| --- | --- |
| 详细的文字教程 / 直播笔记 | ⭐️ 现成的简历写法，直接写满简历 |
| 完整的项目源码 | ⭐️ 项目相关面试题解和真实面经 |
| 1 对 1 答疑解惑 + 专属交流群 | ⭐️ 项目扩展思路，拉开区分度 |
| 前端 + Java 后端万用项目模板 | ⭐️ 从学项目到拿 Offer 一条龙 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1EkDnmPuQYLmTVSMXBGfrlwWpI52ib4HABmoMAib52ZYMicvN50biaqu45n24x1J2XERApoFq4zwuLq6STDmzIUdfT9xib7kTqEgfia4/640?wx_fmt=jpeg&from=appmsg)

## 加入学习

比起看网上的教程学习，鱼皮项目系列的优势：从学知识 => 实践项目 => 复习笔记 => 项目答疑 => 简历写法 => 面试题解的一条龙服务

编程导航 已有 **近 30 套项目教程！** 每个项目的学习重点不同，从 0 到 1 带做，涵盖企业级 Java 后端 + 前端全栈项目、最新 AI 应用开发 + AI 编程项目、大厂架构进阶项目。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H6GNAiaxWV5Y8WpDD1QHMwQQYyHMb0b4UKjJoRwEztF45mDaLsK7SNtCCPiawSvWxPibPzUZDTQjmOtbMDGyfHzic2IDBvhMiaxzYk/640?wx_fmt=png&from=appmsg)

欢迎加入编程导航，不仅能学习往期 **所有** 原创项目，还能享受更多原创资料、1 对 1 学习和求职指导、几百场面试视频，开启你的编程起飞之旅~

🧧 新项目刚刚完结，给大家临时发放一波限时特惠， **仅限 1 天** ，扫码即可领券加入。

仅限前 50 位，速来学习，三天内不满意全额退款！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EpAWNzBxDfI86qX6dtcWdicqe7FwV6vlfh5lgPZTtU9ocAuorVSu5yLAYcvX0hia69oYJh9q2WQDibKR69ibE4B4CD8HXx4SE6XsI/640?wx_fmt=png&from=appmsg)

1 天不到 1 块钱，绝对是对自己最值的投资！成为编程导航会员 后，可以解锁近 30 套项目教程和海量资料，如图：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EIJeeeaBMxbhZsjWZOY9ibaUiaDRQkJLcZQFRiaTN33tCia3jZpIRF1DyvWl6iaHqHEVHMwlWK4iauVAdXxzkibDxWNtFqVtazsicoJTU/640?wx_fmt=png&from=appmsg)

下面是更多关于本项目的介绍。

## 更多介绍

该项目功能完整，涵盖用户项目管理、输入解析、大纲生成、页面生成、在线编辑、主题布局、图片管线、导出质量检查 8 大模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EIU7cXich2SGTtht4OC8OjtQpOLqW93XYgZZIBDRlyfyEeBIhapmOkGlt9LL1XQXsw6yVfkLp9rZz5ZCBmW5FzSbHlweX87P94/640?wx_fmt=png&from=appmsg)

本项目采用前后端分离 + 异步 Worker 架构。前端是 React + TypeScript SPA，后端是 FastAPI + ARQ Worker 服务，通过 REST API + SSE 通信。

后端内部按照 API 层、领域层、工作流层、渲染层分层，耗时的 AI 任务通过 ARQ 异步队列和 Redis pub/sub 来管理。内容、布局、主题三种数据通过 `shared/` 目录下的 JSON 文件前后端物理共享。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EpPcXPJZykwl8iafibuKDjmf0KIbTPlWYkVoxovlHyAJ1qnoib1fd8NJVeDC01ib1D7K4jlnK49z73mumWbHx3nH6rUMJouWdljQo/640?wx_fmt=png&from=appmsg)

项目的核心业务流程非常清晰，能够帮你理清 AI 工程化项目的开发思路。整个流程从注册登录开始，经过创建项目、输入主题或材料、生成并确认大纲、并发生成页面、在线编辑、质量检查，最终导出 PPTX 文件。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Gic9khab0zLKvRiaSzAAHjTehgwl33qjxm9l3iavFf91bbuZVKtOGSwy6iaj3Os30gO5qxWPOcCJdunEFsqlsAhLmRpob8EmTTJ08/640?wx_fmt=png&from=appmsg)

## 加入学习

欢迎加入编程导航，不仅能学习往期 **所有** 原创项目（近 30 套），还能享受更多原创资料、学习和求职指导、几百场面试视频，开启你的编程起飞之旅~

🧧 新项目刚刚完结，给大家临时发放一波限时特惠， **仅限 1 天** ，扫码即可领券加入。

仅限前 50 位，速来学习，三天内不满意全额退款！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HuAlVkfkWcfIe15LOZaXjgicVw8FxYTAGC05SdgDw2weXWV36LZUu7l5e46SMddVAI0k15knqheia8CbXTHEM6yseShxBpVJK88/640?wx_fmt=png&from=appmsg)

已经有 **几万名** 小伙伴学起来了，还有很多大家自发整理的笔记。

不得不说，做项目真的给了很多同学坚持学习的目标、也有了更多拿 Offer 的机会，大家的动力也更足了！冲冲冲！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FOmvqQCiaLYiacnllwwhm8MicUTicI3WDmDNOP3F4WWVUuy2CKKYEkrua1Ju1ydjic11bCpA709DHhAqUbtGjWUtWEhBOiagAiacSFv4/640?wx_fmt=png&from=appmsg)

往期推荐

[字节搞了一种全新的面试玩法，看完我崩不住了。。](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247590662&idx=1&sn=a8da98ba7bd212dd4f17c0371b26c597&scene=21#wechat_redirect)

[27 届秋招龙王群，限时开放！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247590063&idx=2&sn=39c89a63cd92698361b5348813e20352&scene=21#wechat_redirect)

[27 届秋招面试，90% 的原题在这里。。](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589780&idx=2&sn=c296549f9ed8e7fa1f8daf2914f619fb&scene=21#wechat_redirect)

[又一个新项目完结，用 DeepSeek 搞了个微信小程序！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589708&idx=1&sn=2cb6852d0faba977c076d178a887f5a7&scene=21#wechat_redirect)

[完全免费的 AI 资源网站，起飞！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589107&idx=2&sn=0cb64c8664643099430e40b85e8881bd&scene=21#wechat_redirect)

[我们招人了！急急急急急急急急](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=1&sn=b86c18e05defc803a644e2b6dc3dae12&scene=21#wechat_redirect)

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过