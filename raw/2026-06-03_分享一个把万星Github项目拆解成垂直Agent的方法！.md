# 分享一个把万星Github项目拆解成垂直Agent的方法！

**作者**: AI沃茨

**来源**: https://mp.weixin.qq.com/s/bVl8mnGSK1aYFQ-gGG2jvw

---

## 摘要

针对AI技能数量繁多但实际使用率极低的痛点，本文分享了利用“龙虾教练”将GitHub开源项目拆解并定制成垂直Agent的方法。作者以包含86个产品管理技能的开源项目为例，结合自身项目进度，通过十轮对话生成了专属的产品经理Agent。该Agent能提供独特的问题解决思路，并配合云端执行工具落地代码，有效解决了用户无需刻意记忆技能即可高效调用的难题。

---

## 正文

AI沃茨 AI沃茨

在小说阅读器读本章

去阅读

## 现在Agent太多了，

Skill合集，Agent社区，多Agent，云端和本地Agent结合这四件套都快成标配了。

所以说实话，我刚开始测360安全龙虾云端版的时候很谨慎，模型缓存，安全配置，云电脑，还有OpenClaw同款的EvoMap Evolver自我进化引擎。

每一样我都过了一遍，结果最吸引我的用法是龙虾教练，一个可以把开源项目或者工作流做成垂直Agent的Agent。

听起来有点抽象，我来整点人话，

我们现在其实已经不缺Skill了。

GitHub上有一堆，ClawHub里有一堆，很多人自己的电脑里也攒了一堆。

结果我使用率只有20%左右，真不夸张，如果有安装了superpowers这个项目的朋友可以回顾一下除了Brainstorming（头脑风暴）之外的其他skill你有主动触发过吗？

我基本上是想不起来。

这种我称之为《大佬觉得好用所以放出来的一堆Skill结果我只好好用了一个》的现象还在加剧，我都能一个个数出来，YC总裁Garry Tan的Office Hour，也是用来头脑风暴的一个Skill，其实是来自gstack，是一个Agent团队，说明书里面说到的23位专家我只用了半个。

还有一个经典的lenny-skills，大家可能对这个的名字就没那么熟了，看个图就知道了

![Image](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8Fw4sFEOcZeDD95g4F3JYsVTBLBw3E912ichiaqwrLUxkqarn9wQRLSNqM3mcujyCWzqwSVJ983Ve9cHFEkRN3HNSyhpMA03kb4I4/640?wx_fmt=png&from=appmsg)

这佬把自己从300多集采访里面提炼出来的86个产品管理技能做成了lenny-skills，

我真的每一次看这列表，我就眼馋，但是发现我都只用其中的1到2个。

那为什么不做一个精通这一类Skills的Agent出来，我用多Agent的方式遇到同类型问题的是触发Agent就好了，也不用刻意记忆某个skill的名字。

龙虾教练整体的构建过程跟之前的GPTs其实挺像的，

就一问一答。

我首先是把 lenny skill的GitHub项目丢给龙虾教练，然后跟它提出了我的需求，

我想要做一个可以随时打断我的产品经理来弥补技术空白。

那除了常规的名字，性格，能力边界外，最重要的一个能力区分，龙虾教练会主动问我是完整复制下来86个技能，还是说从这个技能里面提取思路。

然后它还会问，

既然想要做产品经理的话，是不是要先了解我们项目的所有的进度，所以我把我的GitHub项目也发给了它，让它去了解实时的进度。

在经过过大大小小10轮的回答之后，这个专业团队的专业产品经理张伟就出现了，我们来看看它里面的结构长啥样。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/VNz1x8bH8FxtoNtLTy1oj5ibYVCiaaibTiaBNQib8spFevdeBdZX82I1mhnz6awZP34UFq8ztaSc9Pl8dAyBPJfP7UXzrwyX37oiatGxLtrdQK08c/640?wx_fmt=gif&from=appmsg)

这时候切换到对话界面，大家看到这个龙虾后面熟悉的后缀就能猜到是哪个模型了吧，且用且珍惜。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fzwe5GfbQuubP2jeZjV2CuxXms1zrcmiaQOuicGsb642gfFIn31sTKOVb6iaHIearHEmWMAXbckoYgUFs3uKt9PQibgIpMLPmt3Fpk/640?wx_fmt=png&from=appmsg)

为了对比我开发的过程，我把上一版本发给了张伟，让他去判断有什么值得做的。

他先是读了一下我的Roadmap，然后给我给出了v0.6版的北极星目标。

我觉得张伟跟我的思路还是蛮不一样的。

我以前是想用时间轴的形式去表达这个信息，然后通过标题，URL的文本相似度来去合并。

这是我做出来的版本，有打分，信息源和事件合并。

但我没想到可以通过时间窗口来合并重复信息，以及标签化和折叠来降低阅读压力。

通常到这一步之后，我可能会把这个计划分发到一个新的执行Agent去完成。

这次安全龙虾在云电脑里塞进去了满血版的Claude Code和Codex，纯纯执行代码的无情工具人来的。

Dang，Dang，Dang，Dang，

所以现在ai news rader的v0.6版本加上了每一个源的AI占比和信任打分，

每一条信息都会有具体的时间线和来源标签，

按事件去重的逻辑也搞定了，虽然标题有点翻译味但胜在不花API啊。

Claude Code还给我加上了滑动高亮浮动的特效，优化了加载的速度，每日摘要第一个，会全量列表前30条轻量错峰入场，刷选源这种需要展开的界面会留到最后。

而且全程没有把自己思考过程加进去（GPT5.5你知道我是吐槽你的对吧）

![](https://mmbiz.qpic.cn/mmbiz_gif/VNz1x8bH8FwKrXg8s5ic8gkswcadXkXAhBnmHLA4M3q8Vib2ibwXUTvRvms3rLbFvcFbLtZMVxIFsiaTJxu2yLDpOyYeMRxzc4dUNZmdHsk8T7k/640?wx_fmt=gif&from=appmsg)

张伟在执行的过程中还可以动态加载能用上的Skill，

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwANrjmB9l2zgt4W4TlW1ut95u1b4qXpkXmPKuXr0CWdY0ERze4b1UvEicj0uiaE91mRRfa76u96uOKm3FwQvibkTsLcUTXFjNkaw/640?wx_fmt=png&from=appmsg)

而且对话缓存也做出来了，同一对话耗的积分会更少。实现的原理大概是在请求的时候会把不变的部分(通常是系统提示语和TOOLS)设置为缓存，接下来 5 分钟内，只要继续请求同一家模型，并且固定内容没变，就不用重新完整处理这部分内容了，模型可以直接复用缓存。

一开始我给安全龙虾打的定位是一个还不错的云端Agent，但后面在安全设置里发现它更像是本地和云端Agent的结合体。

直接把文件，网络，系统操作和技能的权限都划分了不同等级，每一个权限都可以单独设置能不能访问本地，是可以细化到限制每个技能能不能访问本地的文件的。

我可以把它配置成为一个本地的高权限Agent，也可以把它当作一个高性能的有独立工作间的云Agent来用。

当然如果一开始没有之前囤到的Github项目的话，也可以试试看这些熟人的专家虾们。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FxdgvGYO8dBXC2X3Ecubyc6YIKqqUpDt0tNibad4t7uUZX7nMUJ8DFgqYDMC2bPHHrAriaO3NgL0xRvXzU2bPHHLf8EygrhnRiahY/640?wx_fmt=png&from=appmsg)

以前很多Agent产品，

普通人一上手，第一反应经常是懵的。

让我写Prompt，我不知道怎么写。

让我配工作流，我不知道从哪一步开始。

比方我想训一只专门帮我做PPT的龙虾，除了一大堆Skills，它还应该懂什么？

审美要知道吧，

排版，追问，字体大小也要知道吧。

这些问题，如果一开始全让用户自己想明白，基本就会卡死。

所以龙虾教练这个东西，我觉得是有发挥到云端Agent即用即开发的特点，

以前我看到一个好用的Skills工作流，

我就直接把它发给Agent，让它根据我们的对话来告诉我什么时候用这个skill，或者把使用步骤什么时候触发写到Rules里面被动触发。

但现在可以直接告诉龙虾教练你想做什么，

它会反过来问你，拆解需求，补充背景，补充技能，再把这只专家虾训练出来。

当然，它不是魔法大师。

你不能指望点点按钮，就多出一个完美员工。

Agent这东西，越强就越需要会给明确任务，会验收，会调整能力边界。

但至少龙虾教练把第一步变简单了。

不用一上来就记住每个Skill的使用步骤，

让自己强行兼容大佬们的工作流，

我到现在都还记得同样是obsidian做知识管理，

llm-wiki，GBrain和Obsidian-Wiki这个三个项目直接让我停摆了一周，

因为都在我单个Agent上生效，

我甚至能看到同一个文件重复存到三地方。

同时我又觉得这些Skill都是好用的，也希望能保留这四个Skill融于我工作流的可能性。

那怎么办啊，

当时只能慢慢磨然后淘汰掉一些子skill，

现在我可以把同类型skill都放到一个agent里，

自然用上一段时间后，

这个Agent里每个skill的使用频率，

会给我一个真正的版本答案。

@ 作者 / 卡尔

---

最后，感谢你看到这里👏

如果喜欢这篇文章，不妨顺手给我们

*点赞｜在看｜转发｜评论 📣*

如果想要第一时间收到推送，不妨给我个星标🌟

如果你有更有趣的玩法，欢迎在评论区聊聊🤝

更多的内容正在不断填坑中……

![](https://mmbiz.qpic.cn/mmbiz_jpg/YEhakvKZjXmCDLEEW1wClZOVGFURjmibJmciaYLNhp0N55Y6mPiaCj01eV8yzACqDvWDhicbPm07Wu7bboATuKgAbA/640?wx_fmt=jpeg)

继续滑动看下一个

卡尔的AI沃茨

向上滑动看下一个

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过