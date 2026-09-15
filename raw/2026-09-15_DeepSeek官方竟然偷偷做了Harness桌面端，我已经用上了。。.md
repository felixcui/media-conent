# DeepSeek 官方竟然偷偷做了 Harness 桌面端，我已经用上了。。

**作者**: 程序员鱼皮

**来源**: https://mp.weixin.qq.com/s/ieOE4mzyMoa8OVcAOAkhzg

---

## 摘要

DeepSeek 开源其 Harness 工具 DSH（核心理念为“一切皆插件”）后一周即获 20 万 Star，但官方最初仅提供命令行和 Web 两种使用方式，对新手不够友好，社区随之推出了 dsh-desktop 等热门桌面客户端。近期作者发现官方在 deepseek-harness 仓库中悄悄加入了基于 Electron 的桌面端应用目录，已完成打包签名和自动更新流程，却未发布任何公告或安装。

---

## 正文

程序员鱼皮 程序员鱼皮

在小说阅读器读本章

去阅读

大家好，我是程序员鱼皮。

上个月 DeepSeek 开源了自家的 Harness 工具 DSH，被称为 DeepSeek 的角色专武，核心理念是「一切皆插件」。

发布后才过了一周，GitHub 就冲到了 20 万 Star，可见有多火！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GfHbYPXic98U4OPmjMDZxjAiaCYqrVfQYRS4Q4Cyj0Uk5YNCNgZsJBdKLVyvJR86lsuVWrQRQ2mvLVw1cLucehzKJfpuJDScpxI/640?wx_fmt=png&from=appmsg)

不过，官方发布的时候只提供了命令行和 Web 两种使用方式，你得先装好 Node.js 环境，然后在终端里敲命令启动，用浏览器来访问。

对很多小白来说，这个上手门槛就不太友好了。

所以有社区开发者立刻开始做桌面端。Harness 才开源没几天，GitHub 上就冒出了好几个桌面客户端项目。其中最火的当属 dsh-desktop，已经拿了 2 万多个 Star，支持 Windows 和 macOS，双击安装就能用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FGY4smlzJHVOVqGH6c7XrBuic5pdT5g6NmNnmcOibZcE2GwPMOTD7V5E3pdjPRWYFTFEw94lLnOtztMAXaicyxibZqsPotJHnmJpI/640?wx_fmt=png&from=appmsg)

我以为有了社区的支持，DeepSeek 官方不打算出手做桌面端了。结果今天逛 GitHub 的时候，突然发现官方 deepseek-harness 仓库里多了一个 `apps/desktop` 目录。

点进去一看，好家伙，官方自己搞了一个基于 Electron 的桌面端应用，包名叫 `@deepseek-ai/dsh-desktop` ，版本号已经到了 `0.1.5-rc.2` ，连打包签名、自动更新的流程都写好了。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EBHF3gHqjia3nQmTpWmOjkBHuSYq7iap2Xvty8NJSK6pTTDGMgdSVe2KkWQUdXeKZLee7ibrZvEaZ0V2HD93S3TVq38ubl44TYpQ/640?wx_fmt=png&from=appmsg)

最离谱的是，DeepSeek 没有发过任何公告、没有推文、没有博客，就是悄悄地把代码合进了 master 分支。

而且到目前为止，官方也没有放出安装包，想体验只能自己拉代码编译。

很符合 DeepSeek 低调的风格了，闷声干大事啊！

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1EZic1ia8P6t5ucUwL25nE7SRzjpKbKhQFxN7WNG5riaURpD6REs8YIXdMk7AO2ficzGvQ3ib9rGcV54ro05lLlvcJYJoFoRFUVvUvQ/640?wx_fmt=jpeg&from=appmsg)

## 吃波螃蟹

既然官方没放安装包，那我就自己动手编译跑一下，替大家吃一波螃蟹。哦不，是鲸鱼~

整个过程其实不复杂，前提是你的电脑上已经装好了 Node.js（需要 22.19 以上版本）。如果没装过 Node.js，可以去 Node 官网 下载最新的 LTS 稳定版本。

准备好之后，打开终端，依次执行下面 3 步。

> 当然，还有更简单的安装方式，就是你直接让 AI 帮你安装和运行。

**1、安装 pnpm 包管理器**

DeepSeek Harness 用的是 pnpm 来管理依赖，先输入命令全局安装一下：

```
npm install -g pnpm@11.7.0
```

**2、克隆仓库并安装依赖**

把整个 Harness 仓库拉到本地，然后安装依赖。注意这个仓库很大，依赖也很多，安装过程可能会有点儿慢：

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
```

**3、启动桌面端开发模式**

输入一行命令搞定：

```
pnpm run dev:desktop
```

这一步会先编译整个项目，然后自动下载 Electron，也就是一个专门用来开发跨平台桌面应用的开源框架，很多知名应用比如 VS Code、Discord 都是用它做的。

过一会儿，你就能看到一个 Electron 窗口弹出来了，界面和 Web 端几乎没什么区别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1H9pNVEPLHIB2VFJjd8nJ0vicAwocmia7bFEcEFRV3VzrmoBzbRA2odwwStl8ZiclAKD5k7z0aq1eN6ic6cEX1b32EOLljY7fibnsEY/640?wx_fmt=png&from=appmsg)

模型配置和 Web 端一样，在设置里填好 API Key 就能开始用了。我试了一下，跟 AI 对话、文件操作、工具调用、插件管理这些功能都是正常的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1H01C938EXepsKPM3IhFlIousficZl9bbib8ydEFnHLmMxc4PaFEogkGiayYVaHtsWp6mWv6uO6DNhHWrd1xbqKBqRk66DrrxngUY/640?wx_fmt=png&from=appmsg)

不过好像有个明显的 Bug，整个应用内无法粘贴内容，DeepSeek 的 API Key 还是我一个字母一个字母手输进去的……

期待后面改进吧，最好能有一些桌面端特有的功能。

## 官方版会更好么？

可能有人会问，社区已经有那么多桌面端了，官方下场做这个有什么不一样？

我觉得 **最大的区别在于安全性。**

社区做的那些桌面端，不管是用 Electron 还是 Tauri，基本思路都差不多。它们会在你本地起一个 HTTP 服务，然后用桌面窗口去访问 `localhost` 上的这个服务。简单来说，就是给 Web 页面套了一个桌面壳子。

这种方式虽然简单，但有一个潜在的问题：你的电脑上开了一个端口。

如果你在公司内网或者公共 WiFi 环境下用，理论上同一网络下的其他设备是有可能访问到这个端口的。

而官方的桌面端完全没有开任何端口。它用了一套自定义的 `dsh-app://` 协议来传输数据，Electron 主进程和 DSH 后端之间通过进程管道直接通信，请求和响应走的是分帧字节流，生命周期控制则走 Node IPC。也就是说，从网络层面来看，你的 Harness 对外界是完全不可见的。

![安全性对比](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GcBsRnCiaPqBacxptUjia9jOjvAM6O0yJgpibqibq3646yicpT4bYOWHqY3Sb0n7yhjcH54vWoJM0WlwDAgRT7mX0DEpiaeOnXibyc2M/640?wx_fmt=png&from=appmsg)

安全性对比

**另一个区别是版本绑定。**

官方把 Electron 壳、DSH 后端、Node.js 运行时绑成了一个整体，一起签名、一起发布、一起更新。社区版通常是桌面壳和 DSH 后端分开更新的，偶尔会出现版本不匹配导致的奇怪问题。而且官方自己维护更新通道，后续升级肯定会更及时、也更让人放心。

目前官方版本还处于很早期的阶段，没有预编译的安装包，必须自己从源码构建。日常使用的话，社区的 dsh-desktop 之类的项目体验确实更成熟。不过看官方的架构文档和签名流程，后续大概率会通过 `download.deepseek.com` 正式分发安装包，到时候应该就是双击安装、开箱即用了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1HrNE6t20j3uIqDBB2xUvQlVvN13nuE9LwpqNplsY1fgbvD2Uh68S548BGrPQeibWYO8iaMcFeL78orBjGR0oaicVNH3XA5x1OR20/640?wx_fmt=jpeg&from=appmsg)

如果你还不了解 DeepSeek Harness，或者想学习更多 AI 编程工具和经验技巧，可以看看我免费开源的 [《AI 编程零基础入门教程》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=2&sn=91ab9714bff9eb6e26d5c03081ec765f&scene=21#wechat_redirect) ，上千张图、几十万字，带你从 0 开始快速学会 AI 编程，做出自己的产品、跑通变现全流程，一次拿捏。

![鱼皮的 AI 编程教程](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GkOQ6e2ibtgHN39VXm2sGPlFADnarLOJNKSicvf58aicpqtzKurdexA41aE1a0BHaEiaTY5H1VdMJxE9PWUfia9pkAgU6Qf53xF5x8/640?wx_fmt=png&from=appmsg)

鱼皮的 AI 编程教程

评论区聊聊，你更喜欢用网页版还是桌面端的 AI 工具呢？

往期推荐

[耗时 6 年，我终于拿到了 B 站 100 万粉丝奖牌！公布一下明年的秘密计划（](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247591425&idx=1&sn=cdbe3b760d9e61f4906c839d76e911bf&scene=21#wechat_redirect)

[刚刚 DeepSeek V4.1 Flash 正式发布，竟然干掉了自家的 Pro 模型？！梁圣回归](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247591263&idx=1&sn=1b6098c97d733810c92b36575356e571&scene=21#wechat_redirect)

[又一个新项目完结，和 DeepSeek 搞了个 PPT 生成器！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247590743&idx=1&sn=a9d95d34bdd92388e9cf5d286e22b592&scene=21#wechat_redirect)

[又一个新项目完结，用 DeepSeek 搞了个微信小程序！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589708&idx=1&sn=2cb6852d0faba977c076d178a887f5a7&scene=21#wechat_redirect)

[用这个简历，字节当天打电话约面试了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589269&idx=2&sn=75d5668f83eb0428999bb44e72d3405d&scene=21#wechat_redirect)

[完全免费的 AI 资源网站，起飞！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589107&idx=2&sn=0cb64c8664643099430e40b85e8881bd&scene=21#wechat_redirect)

[我的免费 Vibe Coding 教程，大更新！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=2&sn=91ab9714bff9eb6e26d5c03081ec765f&scene=21#wechat_redirect)

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过