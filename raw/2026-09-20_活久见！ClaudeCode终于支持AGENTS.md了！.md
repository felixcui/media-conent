# 活久见！Claude Code 终于支持 AGENTS.md 了！

**作者**: AI小范儿

**来源**: https://mp.weixin.qq.com/s/7rcwEIuQWT-L4IBcSRcHEg

---

## 摘要

Claude Code 工程师 Thariq 宣布，最新版本起若项目中没有 CLAUDE.md，Claude 将自动查找 AGENTS.md，也可在 /config 中切换。AGENTS.md 是写给 AI 智能体的项目说明书，已成为行业事实标准，而 Claude 此前坚持自有格式，令同时使用多个智能体的开发者不得不维护多份内容相近且易失同步的规则文件。

---

## 正文

AI小范儿 AI小范儿

在小说阅读器读本章

去阅读

活久见，Claude 也开始支持 `AGENTS.md` 了。

今天，Claude Code 工程师 Thariq 在 X 上宣布：从最新版本开始，如果文件夹里没有 `CLAUDE.md` ，Claude 就会去找 `AGENTS.md` 。这个行为也可以在 `/config` 里切换。

消息公布后，评论区却一片欢呼。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLGJMuibNHXclG6ARyuqGNQBJQXWrJRdYr5MGmvEU6QZ2HIDnP7ibYy6K4nuoxvSHia3XmACv1AAASibWkJZJcN6ZIHkCTKRGXJZZU/640?wx_fmt=png&from=appmsg)

▲ 图：Thariq 原帖

评论区的呼声很高：有人喊“和平奖”，有人说“这是个很好的决定”，还有人感叹“难以置信，终于等到了”。最有意思的是，最高赞的回复来自隔壁对手 OpenAI 的 Tibo，大家都叫他“义父”：

> 太好了，这才是正确方向。欢迎来到光明的一边。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLpl2KD7ySsXVFMm9aUJxuwxmnM8rd1HnjaRHSibek0j8o6WVuaqzQYl8j9T6vyHiaMaUUBbXnAIQDFrAdJu9BAzggdmbTJf3ev0/640?wx_fmt=png&from=appmsg)

▲ 图：Tibo 回复

只是增加了一个文件支持，大家怎么都这么嗨呢？

以前大家在网页上使用 AI，换一个产品，最多重新开一个页面。现在不一样了：智能体会进入项目、读文件、改代码、跑测试，项目里的规则会直接影响它怎么干活。

`AGENTS.md` 可以理解成一份写给 AI 智能体的项目说明书。

它会告诉智能体：项目怎么运行、代码怎么写、测试怎么执行，以及哪些地方不能随便修改。这样，开发者不用每次打开新对话，都重新解释一遍。

除了 Claude，越来越多产品都在使用同一个名字： `AGENTS.md` 。它已经成了事实上的行业规范。

偏偏作为这个领域的早期代表，Claude Code 一直有点“傲娇”，坚持使用自己的 `CLAUDE.md` 。

这点独特性，对产品品牌可能有好处，对同时使用多个智能体的人却是额外麻烦。一个团队如果同时使用多种编程智能体，就可能需要维护多份内容相近的规则文件。

问题不在于多一个文件，而在于它们很容易变得不一样。

今天修改了项目规范，只更新了 `AGENTS.md` ，却忘了 `CLAUDE.md` 。过一段时间，两个智能体面对同一个项目，执行的却是两套规则。

国内不少产品也已经把 `AGENTS.md` 当作通用入口。即使保留自己的配置文件，也基本都在往兼容这个格式的方向走。

大家逐渐发现，项目规则最好有一份通用版本，而不是每个产品都单独维护一套。

所以，这次更新虽然只是补了一个文件入口，大家在意的却是更大的事情：不同智能体能不能共用同一套规则。

开发者 Matt Pocock 已经开始催下一步，希望 Claude Code 接下来也能支持`.agents/skills` 。大家期待的，已经不只是一个文件名，而是项目规则、技能和工作方式都能真正共享。

曾经高高在上，现在终于低头了。

你在用哪种编程智能体？欢迎留言聊聊。

资料来源

01｜原帖  
https://x.com/trq212/status/2101009392611278961

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过