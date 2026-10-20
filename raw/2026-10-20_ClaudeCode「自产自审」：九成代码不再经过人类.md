# Claude Code「自产自审」：九成代码不再经过人类

**作者**: ASI启示录

**来源**: https://mp.weixin.qq.com/s/hGaPhUBuJbA_E0wSQ6Fl4Q

---

## 摘要

Anthropic披露Claude Code约九成代码由AI编写、大部分审查也由AI完成，6月至9月合并PR翻倍且回滚率下降超四成。团队认为“人是否看过”只是不准的替代指标，关键是根据改动风险匹配测试、AI或人工检查，并以回滚率和事故率衡量成效。

---

## 正文

ASI启示录 ASI启示录

在小说阅读器读本章

去阅读

### 新智元报道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWGxcbmnyYvqrSqhntcbPdelKBG0JLug4pEX8icjBSe5eib6PekswOSvrq8ybatQJRDr9Vib5WOKaUuibKfLb5qH3J4kEIYmC4NQJU/640?wx_fmt=png&from=appmsg)

你可能不信，Claude Code 现在差不多 90% 的代码，是 Claude 自己敲的。

你要是写代码的，第一反应估计跟很多人一样，那谁审？

答案是，大部分也是 AI。

而且你猜怎么着，6 月到 9 月，Claude Code 合进去的 PR 翻了一倍多，要回滚的反倒少了四成多。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXAfGPhN3gESfZibIOyrGYwZORQYKYTmmTMkfEf0UZ1bf55NWRt0ITIaPzOicxicnsHlJSyFZruGk9SbjTjxe1dV0icSX2eJiaicOXEo/640?from=appmsg)

中间还闹过一出，俩 AI 互相 Review，一个挑刺一个改，一宿干了 50 多轮，谁也不服谁。

你肯定想说，AI 写完 AI 审，人看都不看，这不就是学生自己批自己卷子嘛。

这么想一点毛病没有，好多线上事故回头一查，就是瞄一眼就能看出来的傻得冒泡的低级错误。

Anthropic 最近这篇博客，就是来回应这个疑问的，讲清楚 Claude Code 到底是如何自动审代码的。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXeKlrmsunWgX5Nt0BDHBg7WT7qHcceFbPSQ4KaY0koHXhVic3HsASuVaBuiaayjguOpJHzrvuJicFl50G7Fdib9ZO5Aib9jyVXBCQg/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**问题从一开始就问错了**

5 月的时候，Anthropic 大仓库一天合进去 2500 个左右的改动，而到 9 月，一天 3 万多个。

Claude Code 不在那个大仓库里，但也是差不多的势头。

这么多东西靠人一行行看，看到明年也看不完，所以他们干脆不纠结人到底看没看了。

Anthropic 开发团队在博客中说，人看没看过，只是个不太准的替代指标。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYViawocmEegwvcfPhCjHic6vRKC5KjWcsUI4ibwibVg2MlA6YYXyxp4VoO6ddBAwVAje3ZvKgGB5vbLuhLA1EA1LgZlwWe9f0KfeyU/640?from=appmsg)

真正该琢磨的，是这次改动万一出事会怎么出，然后让最合适的那道检查去拦它，至于那道检查是测试是 AI 还是人，看情况。

时间点也跟着变了。

以前的流程大家都熟，写完、提 PR、干等同事有空。

现在 Claude 是边写边查，有点像打字时候自动标红的拼写检查，很多改动等到有人来看的时候，Claude 早就自己查过改过一遍了。

那省下来的人力怎么算？

他们的账是这么算的，看代码费时间，烂代码上线以后去救火也费时间，前一头省了，后一头又冒出来，那就是白折腾。

最后他们就看两个数，回滚率跟事故率，只要这俩指标没往上走，就算没白干。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**七层检查，挑三层说**

原文一共列了七层，全讲太长，挑三层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWicFAf0NhN4uWGUZLVTcqoZJjrVRt7Z3lIR0emOa68Ql46GgVEwlicsSciaKdT8jO0t9JI9yTdAC9g9OPnGMPk3SgqbYGA9kmcn0/640?from=appmsg)

**PR 提之前，Claude 得先拿出证据。**

光一句搞定了不算数，测试跑出来什么结果、Build 有没有过，改界面的还得拿截图跟设计稿对一对。

Claude Code 之父 Boris Cherny 讲过，给 Claude 一个能自己检验结果的办法，大概是让它把活干好最要紧的一件事，他估计效果能好上两三倍。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYUE5UBXCtJDibCjXYSJ9TKAg1YuGzVFwicEuFQF2b4z0iaiaXbibHuTc4ibIOMtktQRaARembQsDTfWF0lxoaCtlfuc2mOU5rv5DM79c/640?from=appmsg)

**PR 提上去以后，先过 AI 这一关。**

这里不是一个 Claude 自己说了算，几个 Agent 分头找 Bug，找出来的东西再交给另一拨 Agent 投票，票不够就不发，纯属修改代码风格灌水的也不发。

这功能刚推出预览版那会儿，内部有实质性审查意见的 PR，占比从 16% 一下子涨到了 54%。

还有个挺贴心的小设计，每条意见会打标签，其中一种叫 Pre-existing，意思是这毛病早就在了，不是这次 PR 搞出来的，作者不用背这个锅。

**最后才是人。**

这一层有条死规矩，Agent 点的 Approve，不算数。

哪怕 AI 审得再好，需要人签字的那一栏，它也填不进去。

另外，是谁让 Agent 写的这段代码，谁就得算进审批人里头，跟自己亲手写的没两样。

人要不要上、上几个，也看风险。

改个文档跟改自动更新器，显然不是一回事。

风险低的，自动检查和安全检查都绿了就能合并，普通改动得一个人点头，最要命的那几块要两个人。

风险等级是分类器看改动本身判定的，跟谁提交的没关系。

这么一层一层摞起来，有点像航空和医疗安全里常提及的瑞士奶酪模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYW8licNRibfQuu3FBFjHWD39EscKJKZUMhxGc7sO2SMZFLjJqJyuia704nSGxUDrFPZuTUv7WcDVA0CNv1I8NGAh8uQQz1sTZ2p44/640?from=appmsg)

每片奶酪都有洞，可洞的位置各不一样，摞够了，很少有问题能从第一片一路漏到最后一片。

就算真漏下去了，底下还有 Feature Flag 和一键回滚兜着。

纯人工手搓放慢速度确实能少犯错，不过主要是因为你啥都干得少了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**两个 AI 吵了一整晚**

前面提了一嘴，两个 Agent 吵了 50 多轮。

其实是个 CLI 的 PR，写代码的是 Agent，审代码的也是 Agent。

一个提意见，一个改，改完再审，审完又提，一个晚上就这么来回拉扯了 50 多轮。

最后还是 PR 的主人发现了，手动给停了。

为什么会这样？

原文的解释是，人看到一条可改可不改的 Nit（小毛病），扫一眼也就算了，Agent 偏偏较真，真去改，一改就多一个 Commit，新 Commit 又把 Review 叫起来，Review 又挑出点新东西。

他们后来拿 Git Blame 回头查，Reviewer 一轮一轮揪出来的问题，差不多 59% 在第一轮审的时候就已经存在了。

等于它不是在找新 Bug，是每轮多翻出几个老的 Bug。

原文还挺坦诚，说这里面也有他们团队自己的锅，之前习惯了默认多审几轮，觉得每多一轮总能多抓点东西。

现在改成最多三轮，三轮过不去，就让作者别改了，退一步想想方案本身是不是有问题。

这么一改，一个 PR 平均要审的轮数从 2.08 降到 1.32，要审五轮以上的，原来差不多每 11 个里有 1 个，现在不到 2%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYU7gkGY0aQntDIdIpXtic9Mk7TbaK4pdA2TetmjM0CpwyxSOaH94mMXicuDxopOFJGwPPo5Vmt4yYdRqwZnFnXPl3fhRTnFJgJVc/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg)

**人现在干点啥**

代码大部分交给机器看了，人也没闲下来，只是活变了。

最典型的，是判断这东西到底该不该做。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYWnC9Qekz2MGVjMc7DySW1ww9O4dOnP7QYDFeGW7FSUfEOrK1ndfXFD7nONwSFs4GjCLm03N3K3RicXa1u2vgxplZ1T87Cu7tOU/640?from=appmsg)

原文提到，有个团队都已经宣布审查瓶颈解决了，团队外面的人提的改动，还是留着人工审，就是为了有人能问一句，这事真有必要做吗？

计费、自动更新器、CI 这些出了事会造成重大事故的代码，照样要人盯着；会被别人当模板抄的架构也是一样。

现阶段，人还是被 AI 大人所需要的。

参考资料：

https://claude.dev/blog/solving-code-review-at-anthropic/

编辑：马可

**秒追ASI**

**⭐** **点赞、转发、在看一键三连** **⭐**

**点亮星标，锁定新智元极速推送！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UicQ7HgWiaUb1y6B5OM79TFzpkceWtUkI6LEwv0uYicSoM5Q3I3kDNJhxWdL3tQvbOpU3Ty7icBqnDDNd4CCu4ibiaHw/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVMuHfFGD1mFMfc5284R22LkqUkpItsc62vpgD4gUNm74S0DFlRWMg0ANo2ia5h3KXHoDYubJUcrJYBHXqYEFlibCHQxVDddZe3s/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过