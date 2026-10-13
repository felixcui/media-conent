# Codex 都没解决的事，Workbuddy 帮我搞定了

**作者**: 网黑哥

**来源**: https://mp.weixin.qq.com/s/nksek-xkdw113hyd7XvgFA

---

## 摘要

作者因公众号大量旧文被平台倒查删除，试图用AI自查近2000篇文章，但Codex因浏览器访问限制无法进入公众号后台，最终借助腾讯开源的Workbuddy BrowserSkill连接本机已登录浏览器，成功让AI读取后台文章列表并辅助排查违规内容。

---

## 正文

网黑哥 网黑哥

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N8QkbJT3a4BCOJ1QBBPE0vhM29LPnhsEQ9rpH6JiaVmXAzS6WibMXf6lFic2QNc3Fca8EZQ2RqqzubLv0UWH88Mu0QLxm4bCtC0C0/640?from=appmsg)

最近，公众号里总有陈年老文章被和谐掉。

![图1](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N8cibmxWwLKWGdXBkujEc416vJYxeWFniavOliaiacDUXZB5HReWhiaEtnjTczATj5GMwQh7K6OYwktDib6pg9kGGD4uJM7Z0mX8mC5s/640?from=appmsg)

公众号平台就是这样的，当时可能发出来没啥问题，现在倒查，可能你就有问题。

就最近这段时间就十几篇被和谐，所以还不如自查一下，但是一打开后台，将近 2000 篇。

![图2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4QK9bGpA4N8wTCKVTef4F2X6b7lHibu6oMUcL2d6cZFNPcvJFLs9ENnT12GJ3Cxetkia2u3zmAKqO7TB4Tu6vgIFicgECtoic9icngwF5WvHJDe0/640?wx_fmt=jpeg)

好家伙，写的时候一篇一篇不觉得，轮到自己检查，才发现这些年没少给自己攒活。

我寻思，这种重复劳动，总该轮到 AI 出场了吧。

要求也不高：先把值得检查的文章找出来，列个清单。有没有问题、要不要改，我自己看过原文再决定。

结果，第一步就没走通。

先找了 Codex，让它进入我已经登录的公众号后台，查找历史文章，结果呢，它却没完成任务。

按照它给出的提示，这次使用的浏览器工具受到访问限制，无法进入微信公众号后台。

![图3](https://mmbiz.qpic.cn/mmbiz_jpg/4QK9bGpA4N8FSEuOW5A023c8h3oLqGw1ibXCTVPRErFicFiaXXXK7CJnxA7YGEVFY7VxchZNGzEFXTEdrib1Sqsk7Biawsk7DxibYAs0lTDRMYFXE/640?from=appmsg)

试了很多次，就是没办法。Codex 调用浏览器，就是上不去微信公众号后台。

后来我就想，腾讯自己家的东西，要不试试 Workbuddy？刚好试试最近腾讯新开源的一个 Skill，名字叫 BrowserSkill。

看项目介绍，它干的就是这件事，把日常使用的浏览器接给 AI 助手，让它能在里面读取页面、点击操作。

结果没想到还真跑通了， 这个 BrowserSkill 还真挺好用，我就干脆把这个过程攒了一篇文章。

## BrowserSkill

简单点说，这个 Skill 就是对 Workbuddy 使用浏览器功能的补强。

github.com/Tencent/BrowserSkill

![图4](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NibGB7go7opNULFzLEUT49VqcD97hT2CENUXhdeGbcHOPSIjwfZLZUggiclriamTxpjcqY7kSfEWbnuc3BASJWXGbWyme0ia3RrzgQ/640?from=appmsg)

就是把你平时用的、已经登录好账号的浏览器，接给 AI 助手。

WorkBuddy 理解你要干什么、分析拿到的内容。BrowserSkill 则负责连接浏览器，让它能读取页面、点击按钮、填写内容。

你可能也遇到过这种尴尬：资料明明就在眼前的网页里，自己看得见，AI 却拿不到。

公众号后台就是这种情况。文章记录放在那里，但得登录自己的账号才能查看，光给 AI 一个网址不够。

配置好 BrowserSkill，WorkBuddy 就可以通过它使用本机 Chrome 或 Edge 已有的登录状态，进入页面继续操作。

开始前，我先问了 WorkBuddy，公众号文章被删除或限制展示，一般可能涉及哪些问题。

它列了一份分类说明。

![图5](https://mmbiz.qpic.cn/mmbiz_jpg/4QK9bGpA4N8Gs2bbUS6x9RuvsDZtxSPOoaSnapXeSKvMNrw2SEJaAXtTk5mjDwMNOwDbxUnzN6RibKIzUTwwcrcVic7HjhpK0SYyujxXdD3qU/640?from=appmsg)

不出所料，都是一些大路货建议，我还是直接给它案例吧。

我把之前被和谐过的文章记录发给他，让它也总结一下规律。

![图6](https://mmbiz.qpic.cn/mmbiz_jpg/4QK9bGpA4Nic9G7oIG63icJjc2oqwxDSVIAsGXSLtXibKwpbclm6iaWzibdianMePRuU7luOJdgEFFQjHzteE0icl3wRebm6Q1ic0WAib9VRfTPj94Xw/640?from=appmsg)

晕，原来我以前尺度这么大的吗？

它总结好之后，我把任务发了过去：

根据前面整理的排查方向，使用 BrowserSkill 进入我已登录的公众号后台，筛选历史文章，把可能有风险、需要人工复核的文章整理成列表，包含文章标题和发表时间，不修改后台内容。

指令发出后，WorkBuddy 通过 BrowserSkill 进入发表记录，根据总结出的风险关键词，进行搜索搜索、查看，再整理找到的文章。

操作时，它还有一个独立的任务窗口，打开了什么页面、走到哪一步，都能看见，也不用把任务页面和自己的日常标签页搅在一起。

更妙的是，它也不抢你鼠标，这个就很舒服。

![图7](https://mmbiz.qpic.cn/mmbiz_jpg/4QK9bGpA4N9UVh9PQSjG7pLEmS4gPLibd72cCeDC43r003Ax1gicjzQekmu66hksmqsKVRQcjc8J7L4cKOmvpq7BEGEpicAxBj2EUjjGpZgPJw/640?from=appmsg)

WorkBuddy 最后交回来两份文件。

![图8](https://mmbiz.qpic.cn/mmbiz_jpg/4QK9bGpA4N8HqoABznZqbnZpVThVvJKAOBkr8Smtv0m48D3zLn2USF9F77UmZa7EjsFSU2hA9bD1yyK99dXXvE2DdTOQQnl28IiaOFOaxeuQ/640?from=appmsg)

一份是 CSV，用表格软件就能打开。另一份是排查方法和结果说明。

标题、发表时间、命中关键词、风险类别，还有把这篇文章挑出来的理由，都列在表里。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4NibnHc0E2QwpDbskqiaSbhwibZTGXH8hmMmqAzRWArnGN2D4UBM8Zicf3F8hmltx7nsBibcRObDk2e5ZL3lTibonC45ODZiaQ2CgYPtNc/640?wx_fmt=png&from=appmsg)

总之呢，拿到了一份能够接着往下检查的清单。

我最后根据这份风险文章列表再慢慢核实，确实有风险的直接删除，风险不大继续保留。

不过基本上能删的我都删掉了，都是一些陈年老文章，有些已经失效了。

我这次想用它，是因为文章多，导出得分批，搜索条件也不少。光把材料凑齐，就够忙一阵。

这种时候，能让助手自己进页面查找，才有实际意义。

BrowserSkill 这次的表现值得让我高看一眼。

## 怎么装？

安装过程，倒不用想得太复杂。

在 WorkBuddy 对话框里发一句：

PROMPT

安装这个 https://github.com/Tencent/BrowserSkill

轻按自动全选复制

最后需要你手动打开它提供的链接，安装浏览器扩展。

![图10](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NicxxibMJcl4UJ232mTsYcrPI8DuicZmz5WticVqwhGHia0ibKXJagYUDERQpgYDOjpiaOucHd3pyd1TJl48tebWgoS8ycyxmVV4jqVKg/640?from=appmsg)

然后再根据提示重启 WorkBuddy，就可以开始用了。

## 结语

我觉得，Browser Use 对 WorkBuddy 最大的意义，就是让 AI 直接去浏览器帮你干活，而且还不抢你鼠标。

以前让 WorkBuddy 干活，遇到没有 API 的网站，很多事情就卡住了。比如登录后台、查数据、填表单、点按钮，往往还得自己动手。

现在 AI 可以像人一样操作浏览器，进入网站、点击、输入、读取信息，甚至把多个网站上的工作串起来。

这意味着，很多原本需要人工配合的任务，现在有机会让 WorkBuddy 独立完成。

当然，验证码、复杂登录这些问题还没完全解决，但方向已经很明确了。

如果你也经常用 WorkBuddy 的话，建议你装上试试，很舒服。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NibMP4Aur1VUEiaI1g2NpreKcLJLJYNskX1T8TxY0HFaF9naf039MicuvPUSUkj68QWfAic5YFI10YOIk9MK7ICOjlvvdTlFfxaGQY/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过