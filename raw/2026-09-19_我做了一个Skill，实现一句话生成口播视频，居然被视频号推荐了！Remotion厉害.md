# 我做了一个Skill，实现一句话生成口播视频，居然被视频号推荐了！Remotion厉害

**作者**: Jenny木妈

**来源**: https://mp.weixin.qq.com/s/HImGXBtPLN_jx1OOS64Lfg

---

## 摘要

作者利用Claude Code、Remotion和Listenhub制作了一个Skill，只需一句话就能将微信文章自动转化为带本人克隆声音的口播视频：由Claude Code统筹全局，根据文章生成脚本和口播文案，调用Listenhub克隆声音，再指挥Remotion以写代码的方式渲染图文视频并保存到本地。整个视频5分钟完成、成本不到1元，播放量超过2000并首次获得视频号推荐，效果胜过真人出镜。

---

## 正文

Jenny木妈 Jenny木妈

在小说阅读器读本章

去阅读

周一啦，你周末创造了么～

哈哈，我周末“创造”了一个skill，终于实现了一键把我的微信文章转化为视频，而且是有我声音的视频。

我的视频号几乎是0起步，目前两个视频的播放量2000+，还首次获得了视频号的推荐，这不是多好的数据。

但一句话5分钟就做出的视频，成本不到1块钱，居然比我真人出镜的数据好😂，所以赶紧来分享一下是怎么做的。

这里面用到了Claude code，Remotion，Listenhub。一句话总结就是，Claude code负责编码统筹全局，它的工作如下：

- 根据文章产出脚本
- 根据脚本生成口播文案
- 根据文案指挥Listenhub克隆我的声音
- 再指挥Remotion生成图文视频。
- 最后渲染下载保存到本地

于是，我只要对着Claude code说一句话：帮我把这个文章转化为视频。

剩下的我就该干嘛干嘛去了，等着收视频即可。

我一晚上产出了3个视频，下面是我今天才放到视频号的视频，来听听是不是我的声音。

接下来，我分享完整的实现过程。

我觉得你未必会有我这个需求，也未必会用到我的skill。但我想分享的是整个和AI协作的过程，因为AI工具和方法真的已经很多了，关键是你是否能找到适合你和AI协作的方式。

而且我的确发现很多人，用不好AI不是因为没用到最牛的模型，是没找到和AI协作的方法。

所以，相比分享一个简单的视频制作，我更想分享的是，如何与AI更好的协作，我相信会对你有所启发，不信你看完试试～

1

先让Claude code学习如何用Remotion做视频

我没一开始就干，因为我自己完全不懂Remotion，我都是周六才知道有这个开源项目的。一句话总结Remotion，就是用写代码的方式来做视频。这非常适合我，而且意味着足够个性化和掌控感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GPgaTC9HFHhnatibrt3YWJKXNMibg1kibQpZFhSRdceicdUGibGCe4gBoSEBr1fkpYoL0AC7ne2lZSL4vQ/640?wx_fmt=png&from=appmsg)

所以，我需要先和AI一起学习官方文档，看看到底怎么实现，以及可能出现的坑是哪些。

第一步：让AI先学习

我把官方文档，包括remotion和Listenhub，复制给Claude code，让它先学习。

> https://www.remotion.dev/docs/
> 
> https://blog.listenhub.ai/openapi-docs

这个过程就像你不会让一个新人没培训就上岗一样，为了验证AI真的学会了，我让AI学完后总结出来具体的步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GPgaTC9HFHhnatibrt3YWJKXkKooRb4e3mp6ETVUiaEx2w6qlN6uB3EjUqEvsYvLZ6pthhRaNeu75YA/640?wx_fmt=png&from=appmsg)

第二步：用真实任务驱动学习

我截图给它一个图说：请生成一个动态的GDP效果图。结果Claude code学会了，立马就打开了remotion的预览，确实是动态的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GO1nckRn4cRtibxlRKMWy5yenicNH0BPnCHOoib78HxXzdvLgrfibgHg7QgNxd6yfES2w8skHXZib7icjXQ/640?wx_fmt=png&from=appmsg)

同时，也让它测试通过Listenhub API获取我的声音，也输出了一个声音。说明测试成功了～

第三步：根据学习结果，输出可执行的方案

和Claude说，现在你已经学会了如何用Remotion做视频，接下来，我们要实现之前的功能，把我的公众号转化为视频，请给出你的方案。

结果这一步让我失望了，给的方案还是用nano banana生图。

于是我说它：刚才你是如何实现了GDP的？那我们未来的视频就如何实现。

Claude马上修改了自己的方案，完全用代码生成视频效果。真的很有意思，和带一个智商300的新人差不多，哈哈～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GO1nckRn4cRtibxlRKMWy5yek1uwsXKIHkibU5IxDUqYT38RE1cIHricTyL7vpXpMORpbexOqlu1FyiaA/640?wx_fmt=png&from=appmsg)

不知道你有没有发现，不管是人，还是AI，最快的学习方式就是动手干，边干边学。

**仔细回想，这个过程很有意思，** 我好像在充当AI的外部奖励系统，通过真实任务、即时验证和纠偏，让Claude在上下文中形成"类似强化学习的效果"。

写到这里，我贼开心，心想这是真正的AI协作啊～

2

Claude code真正动手开始干活儿

AI学会后，要开始干活儿了。

这一步基本就是Claude自己规划，自己干，可以看看它的输出节奏，真的很稳，一共8步，几乎人是不用参与的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GO1nckRn4cRtibxlRKMWy5yeMPPPYibNZN7OExK4mcjvvicHmlByibV2cZUxl3Ziahia3vIvWq7hSRM8JwA/640?wx_fmt=png&from=appmsg)

接着就是，不断的调试bug

第一次做，一次成功的几率是很小的，不过问题都出现在了声音和图像的对齐，改了7个版本，才改成功。

但还是那句话，遇到问题不要担心，AI来解决，在经过7次打磨后，完成了。

![飞书文档 - 图片](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GO1nckRn4cRtibxlRKMWy5yeDa9RvIT2DviakZ5OP305KvmFiaWBamjEN9oL5rTn64QPP1nu9EHJTUVA/640?wx_fmt=png&from=appmsg)

3

让Claude总结最佳实践，形成可复用的Skill

经过两个视频的打磨，已经可以实现一键生成完整的作品了，但我想下一次再用这个功能的时候，实现一遍过，而不是来来回回截图，来回的改。

于是，我让AI先总结输出声音对齐的最佳的方案。

这一步，很重要，因为刚才修改的地方是因为什么原因，如果不固化下来，下次还得调整。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GO1nckRn4cRtibxlRKMWy5yepfriboBOs3ApZLBYJuSnZGeHPibTibibvzw5nwsRXiaxaMYuPKhicQSxibk6w/640?wx_fmt=png&from=appmsg)

AI自己分析完毕后，我选择了稳妥的方案，最后让AI参考如何创建Skill的文档 ：

> How+to+create+Skills+for+Claude+steps+and+examples++Claude.md

生成了remotion-Listenhub-auto-video的skill。

接着，我用这个skill来做了一个更长的视频《苏格拉底提问法》；这个视频一共235秒，45个场景，一次成功了，视频已经上传视频号：木妈AIdea。

如果你也有类似的需求，欢迎找我获取skill。

4

总结：和AI协作的技巧

所以，你发现了么？我在用AI的时候，我真的把AI当成了最牛的搭子，我们一起学，我给它提供反馈，给他一个方向，它来自己规划自己执行。

我觉得和AI协作很像是带了一个智商180的新人，既然是带新人，就需要我们：

- 给它学习的机会：先让它读官方文档，理解底层逻辑
- 给它试错的空间：第一次做不好很正常，关键是能快速迭代
- 给它即时的反馈：不管是对还是错，立马给AI反馈
- 让它总结最佳实践：把经验固化成可复用的知识

这个AI协作范式，可以用在任何领域。

不管你是做视频、写代码、做设计，还是做数据分析，都可以用这个方法。

在我看来，AI时代，真正的竞争力就是如何更好地和AI协作，是你 **能不能把 AI带进你的工作方式里** 。

是把你的经验、判断和审美，和AI的执行与快速学习能力结合起来，形成 1+1＞2，甚至大于2的N次方的价值。

当然，这套方法只是我的实践经验，未必是最优解，但至少目前，它是 **最适合我的** 。

希望你也能从这个过程中，找到属于你自己的AI协作范式。我觉得，这才是AI时代最大的机会，用AI放大你的独特性，而不是被AI同质化。

因为我一直觉得，每个人的经验、遇到的问题和工作风格都是独一无二的，别人的Skill或者方法只能参考，真正该自动化的，一定是你自己的需求。

昨天一个做AI的朋友说我：感觉你没听过\*\*大佬的课，因为你创建Skill的方法和他们不一样。

这也反映了我学习的习惯，我一般都是要解决一个问题的时候才开干，在干的过程中学习和总结，分享的也仅限于自己的实践。

所以，我还是很有必要去学习一下别人是怎么创建的，本周会分享创建Skill的完整方法～如果你对Skill感兴趣，记得回来看哦。

回头一看，我从完全不懂代码和Remotion，到一键做出3个视频，再形成可复用的Skill，整个过程不到5小时。

感叹AI时代的学习曲线真的很陡峭啊，但也真的快啊～

对了，马上寒假了，你会让孩子接触AI么？受读者家长邀请，我准备寒假开一期线上和一期线下（成都）的AI创造营，是真的让孩子用AI创造哦～

感兴趣的联系我锁定名额。

👀如果你也在探索 AI +个人成长 +家庭教育 ，关注后加入木妈2026年AI家庭教育学习社群～

---

我是木妈，一名AI+家庭教育实践者，得到AI学习圈讲师，已经上线2门给家长的AI实战课。私信我可获得讲师亲友价。

木妈未来社区是一个浸泡式学习「AI家庭教育」的社区。如果你也想找个组织浸泡学习，欢迎后台留言。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wHWuIvyr8GP6vAiarqCH54c4NibakwHU0jfJMgtbVZwicupwa2afHmUBBZUHXgyNqEDYaxqxwuL1GrlR7THenLAjQ/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25)

点击👇查看往期实践案例

[AI+家庭教育案例合集](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5Njg5NDE3MA==&action=getalbum&album_id=3800737980130541580&uin=&key=&devicetype=iMac+Mac15%2C12+OSX+OSX+15.5+build\(24F74\)&version=13080810&lang=zh_CN&nettype=WIFI&ascene=15&session_us=gh_e5a9a48f9bf4&fontScale=100)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过