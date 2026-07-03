# 用 Codex 读 DeepSeek 最新论文 DSpark，AI 改变了读书方式

**作者**: 成峰

**来源**: https://mp.weixin.qq.com/s/tOHFr6g0N1GimPOzBbIoPQ

---

## 摘要

作者分享了使用 Codex 结合其开源的“论文 Skill”阅读 DeepSeek DSpark 论文的高效体验。该 Skill 能根据个人阅读习惯重组论文，将卡顿处的解释直接写回正文，生成可入知识库的中文解读材料。这种方式依托模型能力、Codex 同屏交互及浏览器操控，将多软件切换阅读转变为人机同屏“共读”，用户负责提问，AI 负责查资料并重写内容，极大提升了阅读效率。

---

## 正文

成峰 成峰

在小说阅读器读本章

去阅读

我用 Codex 加“论文 Skill”读 DeepSeek 的最新论文，省了一半时间。

还留下了一份图文并茂的中文解读材料。

![中文解读材料](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2ZjkupykUIjPCictJ8GK6Qnibd2z8j0SMpCc48glJILgT0iasuOxeYkyM5ficxO0dhVyzHboYejeTrRSEfHJ7oExEqc1vlbMX5m0BStA3zE/640?wx_fmt=jpeg&from=appmsg)

这个论文 Skill，我已经打磨了一个月。现在开源出来。

它能根据我的阅读习惯，重新组织论文。读到哪里卡住，就在哪里标记，Codex 会把解释重新写回正文，最后变成一份能继续写、能进知识库的论文解读。

## 怎么用

打开 Codex App，直接跟它说：

> 帮我安装 paper-reading 这个读论文 Skill。安装命令是 `npx -y github:Agentchengfeng/paper-reading-skills install` 。执行前先给我确认一下。

![安装 Skill](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2ZjkupxicVT6arUiats2oNYERbBfssqiageOv0diaJ1jqcfMKFVI6fxfficAfek1fw2XY2FNuM70gW3n9a3TdHLNldZBQv910uoZKUd118dk/640?wx_fmt=png&from=appmsg)

整个过程不用打开终端。

装好以后，把 DeepSeek DSpark 的论文链接或者 PDF 丢给 Codex。

![导入论文](https://mmbiz.qpic.cn/mmbiz_png/7e6H2ZjkupyjtcpRZsxMhzGSQ46J5BGF7T6wxFWMlfUIajKmzsWiakD2VTiaLMtXiajrFPToE8JaVG4UhChCk1KI4OCIFCF7ZI2zQNtxXuECic0/640?wx_fmt=png&from=appmsg)

接下来就可以让 Codex 生成阅读页面，再按自己的疑问一路读下去。

## 为什么用 Codex 读论文

这里其实叠了三层东西。

第一层是模型能力。它要能读懂论文里的技术关系，否则只能停在逐句翻译。

第二层是 Codex 的交互。Codex 内置浏览器，论文页面、聊天窗口和生成的 HTML 可以放在同一个工作区。

第三层是工具能力。Computer Use 和浏览器操控让 Agent 能看到页面里的文字、按钮和标记，也能把解释、图和重写后的段落放回正文。

这三层叠起来，我不用在 PDF、翻译软件和聊天框之间来回切。

![Codex 论文阅读器三层组件](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupzUbeIsM3EpIp7bibW5eNEoPp8x8nZCjicJZ6vsQ1o9HbJNmy47gw67aj0fBNice9QAJtA7bib1zGMEqtjSibNT1icx3hFu5shO6b1WM/640?wx_fmt=jpeg&from=appmsg)

**读论文开始变成一件共读的事。**

我负责提出问题，Agent 负责读上下文、查资料、补解释，再把有用内容写回正文。

## 读论文变成一个页面

把论文发给 Codex 以后，它会生成一个 HTML 页面。

![阅读页面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupzESdtZEQzdREj4ZbV92L2t40E6nvgNFJm63ojDFBsKSVo0DobicVrE9Nic5Q2fMVdCtZzyqdSCRTQpfWkyaGlW1r0KRicZBRwEG0/640?wx_fmt=jpeg&from=appmsg)

这个页面先把英文论文变成中文材料。

再按我的问题，把论文重新组织成一篇能读下去的解读。

左边是 Codex 的聊天窗口，右边是 Codex 新编写的 HTML 文章。

![同屏阅读](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2Zjkupyuw4d3FJDKu22lkP6FYxJdoECf3Hskqd1tQ0ojljlLDLGH6EDWHPDvw0uJUTSW4OKMtsUKLfCUxNqEha0lNJqqiaSgdO3AVyQc/640?wx_fmt=jpeg&from=appmsg)

一个屏幕就能放下。

我看到哪里不懂，就在左边问；Codex 读右边的页面，再把解释写回右边的正文里。

## 词不懂，先划线解释

读论文最先卡住的，通常是一个词。

有些技术名词我没见过，就把它们批量划线，再补一句具体问题。

![批量划线](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2ZjkupwkMibyPw8hyCmJvkF6G3QYek5g2pciciblnlicicErEb0T6pr9cugFFRKzIjDx2BQsPqmfqQqZ3I3kYPecHO5SPIQJ7ufuPFZJib9L8/640?wx_fmt=jpeg&from=appmsg)

划线成功后，页面会保留这些标记。

![划线标记](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2Zjkupz0hZFjiaic50hff5sZBnS019IktUKibflXFxcmN5QB2RciaecAHibRIDcBngRV5corXeNvLOYQF6gI5jo7OPFmuGo5iajgBRmKby9kw/640?wx_fmt=jpeg&from=appmsg)

我再让 Codex 解读这些划线。

![解读划线](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2Zjkupyx87CyACybp8M4eG3Fo7AXN6bEkn6XHlIhCm4g6goCEpyzqPibOLfy7jheOFuVPdlE3rSoEibV3qJMuK6CrGibZUPianRicwhSqwBw/640?wx_fmt=jpeg&from=appmsg)

解释会直接出现在词语下方。

![词语解释](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2Zjkupy9PnMWH6FKuV6BzLFtaZjibR8p8KsdAiboK67tic2iaibGfHxYsTwHQx2zokDia6uQG9koG8uzia1rgWcwcuFWw307O3AUcpDASh4GIA/640?wx_fmt=jpeg&from=appmsg)

## 一段读不懂，就重构这一段

很多时候，我卡在一整段逻辑上。

这时候我会把这一段标出来，直接告诉 Agent：这一段我没看懂，帮我重新解读。

![重构段落](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2ZjkupwPlb7Nb97bg6FB1G96L7T4ye9ytbqs8jt1BlXbr7xicgcxh4XBlGYicAhIU2k7REjPtk33SaaV9pAs4DQ593wPojRwqGc9MiauoY/640?wx_fmt=jpeg&from=appmsg)

如果只是术语问题，它补一句解释。

如果是推导断了，它会把这一段重新写一遍。

这一步把聊天里的回答，变成了正文里的材料。

解释会回到原句下面。

## 读完整篇，还能重组成新正文

词和段落都处理完以后，整篇文章还能再往上整理一层。

![整合正文](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2Zjkupx5zaFBUfxBg5icnufyRM7IsgibLxMto0gicQqicdMvq6Ym0WHNRxLbx5rbMIiaEO6ib2VdFbh5BkuFS3CCiaswS6mWGdYbrlMIiaaxiazw/640?wx_fmt=jpeg&from=appmsg)

我可以直接跟 Codex 说：

> 整合一下这一段/篇。

这一步会直接产出一段新正文。

它把原文、解释、我的问题和保留下来的图，合成一版新的中文解读。

旧的疑问卡删掉，有用的图留下。

页面从“哪里看不懂”，变成“这一段已经写清楚”。

![论文理解的三层重构](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2Zjkupytq0FMibZWEJX8syaJ7NLia421juAwAzTdYibJibnjdkeQoR9GIxlXXOm5NMnREmibmw9ia9SCdic3XgIVlgia4XGPEbcEKV9AE0xHibm0/640?wx_fmt=jpeg&from=appmsg)

## 读书从翻译，变成重构

英文翻成中文，只解决第一层问题。

后面还有三件事：

这个词是什么意思  
这段在推什么  
整篇文章能不能变成自己的材料

Codex 和论文 Skill 把这三件事放到同一个页面里。

一个词能被解释，一段逻辑能被重写，整篇论文能被整理成自己的知识材料。

我不用再一个人对着译文硬啃。

我和 Agent 在同一个页面里，把论文拆开、理解，再重新写成我能用的东西。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过