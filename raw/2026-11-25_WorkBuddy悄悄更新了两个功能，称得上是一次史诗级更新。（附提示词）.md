# WorkBuddy 悄悄更新了两个功能，称得上是一次史诗级更新。（附提示词）

**作者**: 大刘

**来源**: https://mp.weixin.qq.com/s/bntKq-pa3pWF4Yww5UpRsg

---

## 摘要

腾讯财报披露 WorkBuddy 千万日活前后，产品悄悄上线了两个用户催了很久的功能。一是跨设备数据迁移：同一个账号在多台设备间迁移任务、对话、分组和定时任务，换电脑不用从头攒；但作者点出关键限制——MCP、全局 Skill、专家和全局记忆都不在迁移范围，偏偏这几样最要紧；另外定时任务导过去默认是关闭的，要用得手动打开。作者的绕法很实用：在旧电脑新开一个任务，让 WorkBuddy 把带不走的东西打包成任务产物跟着任务走——自建 Skill 整个文件夹拷进来、技能市场装的只记名字、MCP 配置导出但 API Key 和 Token 一律替换成「【待填写】」、专家列清单、全局记忆整理成 memory.md、各分组关联的本地文件夹只列路径清单，最后写一份恢复说明，读不到的直接说不要猜。二是任务管理与分组：统一管理文件夹工作区和普通对话，按工作事项整合目录、重组资料，实现文件互通共享。

---

## 正文

大刘 大刘

在小说阅读器读本章

去阅读

![大刘品牌动图](https://mmbiz.qpic.cn/sz_mmbiz_gif/J1Cdba5GUc3icSbdAQv9EqA9F0W4LaWojc2dyibSCa50WWDic7HjXkzyZCiatrH8c5hn0KJWMltvRfrF4HF2ZlgtGVpg4QTP01uqYa1sdNGpRL4/640?wx_fmt=gif&from=appmsg) ![DALIU · AI 品牌字标](https://mmbiz.qpic.cn/mmbiz_png/J1Cdba5GUc1U8aKX66XeD8e48eOSj7NSmfwf4vzranh57ouUR2ic3ACUhmEcTjhic9Fia2y8ibDSnyaickdJSIbrrQmY7ponQRXV87A7lyrnHQlQ/640?wx_fmt=png&from=appmsg)

这两个功能的更新，我觉得是必须写一篇文章来说的程度。

就在上周，腾讯财报里面，WorkBuddy，千万日活，着实有点太吓人了。

从 3 月发布的时候我就开始用了，那时候还有很多Bug，到现在的千万日活用户，不到一年的时间。我是真的看着 WorkBuddy 一点点优化到现在，真的有点「国民级」产品的感觉了。

也就是在发布财报的前后脚，我发现 WorkBuddy 悄悄更新了两个功能，对我们来说，很小但是非常有价值。

1\. 跨设备数据迁移，终于可以在几个设备终端，丝滑迁移所有数据了。换电脑也可以继续工作。我也准备了完善的提示词帮大家做到一键迁移。

2\. 任务管理和分组功能，WorkBuddy 现在可以统一管理文件夹工作区和普通对话内容，解决聊天越聊越多杂乱无章的问题，现在可以按工作事项整合好工作目录，甚至，可以让分区重组工作资料来实现文件互通和共享。当然，我也整理了一套方法帮大家用好这个功能。

实际上，这两个功能在几个月前，很多用户包括我在内就一直在吐槽必须得有，甚至好多人还为了这个功能，去做了各种Skill。

![技能市场里的 WorkBuddy 跨设备迁移工具](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc3ufnIoqDzeQcdgm8XhQHuhxfLCZBCEicZAQwLZFX4GgTCcB3BMiakftYFInhpbeNSibfo90L4Fa4ugqrndO6LNIaaE7hMNDQXWzM/640?wx_fmt=jpeg&from=appmsg)

现在是终于，端上来了这个史诗级更新。

先把 WorkBuddy 更新一下到最新版，我的是 5.11.3，是都支持的。

![WorkBuddy 界面显示当前版本 5.11.3](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2euGyok4ZDCY6n0cnKJ2MrADj4N9hRFp0uVxby3VfPbsNxicvviaFo1LE4qs4v6fr6nGmHZfRrvX0hobJsOkXibmexicyYlfYMFPk/640?wx_fmt=jpeg&from=appmsg)

我们一个一个来说。

1.

跨设备数据迁移。

先说迁移。

大半年用下来，我 WorkBuddy 里攒的东西，已经多到有点离谱了，几百个任务，按项目建好的分组，每天早上准点跑的定时任务，还有一堆调了好久的 Skill。

而这些内容大多都在公司电脑里面。家里的电脑就像是刚出厂的WorkBuddy一样，啥也没有。

当然，还有个更适用的场景就是，换了新电脑，啥都得从头再来一遍，想想就头大。

而现在，终于能一起带走了。

先来说 **迁移怎么做。**

流程其实不复杂，不过开始之前，得先满足三个条件。

1\. 两台电脑都更新到最新版，登录同一个账号。

2\. 旧电脑开着机，WorkBuddy 也开着，数据是从它那头直接拉过来的。

3\. 点开左下角铃铛旁边的小图标，打开「允许移动设备远程连接」。

![左下角铃铛旁的图标点开后的弹层，「允许移动设备远程连接」开关处于打开](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc01TqeWuokP3hjOve8KUg9t58uxaPO07ae8F3LcciaibFgBXNsW5ulX6icJR7mfVVsZHRdia2rv5oW5wyDNJyfobAP8hfo6gsnUR70/640?wx_fmt=jpeg&from=appmsg)

然后到新电脑上，打开WorkBuddy的 设置 → 数据与安全 → 数据导入。

右边会列出你这个账号下的其他电脑，带小绿点的，就是在线的。

![设置-数据导入页，右侧列出同账号的其他电脑，在线的带绿点](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2SOh8Fib2SzoJLibv3ib4Xhn5NXHYJclxHheepnkO5FOGGLWXXpicAibFBWUia8Hh5rMypAgr1pDVRs3Brsyb50nfiaJ3Y26YAiabul5c/640?wx_fmt=jpeg&from=appmsg)

点开你的数据源的电脑，直接「全部导入」就好。

我这边几十项，几十秒钟就导完了。

![弹出「数据导入完成」，下方出现导入历史](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc0SXbw7gTxJINtFibdYiaaamJxZQ8NTOq5HR7tEMY0TtiaWkf0HEpWb98omjjQYy79asWx6r9LEIU4XymvYNn0OTkGvZiafL7wq0JY/640?wx_fmt=jpeg&from=appmsg)

导完我随手点开一个几个月前的任务，对话一条没少，接着往下问，它也接得上，这一下是真的爽，跟没换过电脑一样。

不过有个地方要留意，定时任务导过来，默认是关着的，如果说还需要的话，得手动开一下。

![定时任务列表里，导入的任务处于关闭状态](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1TjYovlReuicZQr89q2RAutCW2YpvLCRs6CdSvXo9PHb8nT2FibwNdNW9KyvPWlRScXAqImrFicOAqLibfXClm6TzQAqxFsXic8utQ/640?wx_fmt=jpeg&from=appmsg)

这个其实是好事，不然两台电脑到点一起跑，你就会收到两份一模一样的推送。。。

实际上这里面有个小坑，能迁移的只有任务、对话、分组和定时任务。

但是 MCP、全局的 Skill、专家，还有全局记忆，这几样都不在迁移范围里。

而最要紧的这几样，偏偏不在迁移范围内啊。

所以，这里我也准备了一套方法，让那些 **带不走的，让它自己打包带走。**

逻辑很简单。

**让旧电脑上的 WorkBuddy，先把带不走的东西打成一个包，放进任务里，跟着任务一起过去。**

第一步，导入之前，在旧电脑上新开一个任务，发这段：

●●●

我要把这台电脑上的 WorkBuddy 迁移到新电脑，官方迁移带不走 MCP、全局 Skill、专家和全局记忆。请你做一个迁移包，放在这个任务的产物里，单个文件不超过 100M：  
  
1\. 我自己做的 Skill 整个文件夹复制进来，技能市场装的只记名字。  
2\. MCP 配置导出，API Key、Token、密码一律换成「【待填写】」。  
3\. 专家列个清单，你记得的关于我的全局记忆整理成 memory.md。  
4\. 每个分组关联的本地文件夹，只列路径清单，不打包文件。  
5\. 写一份「恢复说明.md」，写清到新电脑上按什么顺序恢复。  
  
读不到的直接告诉我，不要猜。

其中关于密码的部分，一定写成待填写站位，平时还是需要多注意下信息安全的。

打包完会产出这些内容。

![旧电脑上跑完提示词，任务产物里能看到迁移包、memory.md 和恢复说明](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1ADE1oONH0I3pp1T4aMtDAID8X9dtuCSflibxM6ZEAbRUJUUVHBquJgOZ17rsIefvVqYTmv9CSkfT496CtLF6GqU7mM8LcNp6Y/640?wx_fmt=jpeg&from=appmsg)

打包完，再去新电脑导一次，我们整理的包也会跟着迁移。

第二步，在新电脑上打开这个任务，接着发：

●●●

旧电脑的数据已经导进来了，这个任务的产物里有迁移包和「恢复说明.md」。请照着恢复说明把这台电脑恢复好：  
  
1\. 自己做的 Skill 装上，技能市场的列个清单给我。  
2\. MCP 重新添加，遇到「【待填写】」就停下来问我。  
3\. memory.md 先给我过一遍，我确认了再写进长期记忆。  
4\. 找到分组对应的本地文件夹，告诉我每个分组该重新关联哪几个。  
5\. 定时任务先别开，运行目录要是还指着旧电脑，告诉我该改成什么。  
  
做完给我一张清单：哪些已恢复，哪些要我手动处理。

然后它就开始一项一项往回装了，碰到密钥就停下来问我，我填一个，它接着装一个。

![新电脑上跑完恢复提示词，它给出的恢复清单，标了已完成和需手动处理](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2OFb0oicPiaUT00XQwnG7RTicAyffvWptsK1K0BsGiaBCt4nY2MPYnQ6uTIO8WzYUvImnzvUZkB32vm2vqR8cVXRAX6Wuc4O0Qv4Q/640?wx_fmt=jpeg&from=appmsg)

至此。

可以说是 WorkBuddy 完完全全的迁移了。比起传统的那种用Skill迁移的方法，丝滑太多太多了。那更传统的手动迁移，就更别说了。

所以这个功能，一定值得我写篇文章。

2.

任务管理和分组。

再说分组，说实话，这个是我盼了最久的功能。

其实解决的问题很简单，以前WorkBuddy的侧边栏，管理是很混乱的，全是一个个对话无序排列，主打就是乱和找不到。

那现在就可以通过这个功能，统一整理起来。

先来说说基础的 **分组怎么用。**

这个其实很简单。如果你已经更新到最新版的WorkBuddy，那之前侧边栏的「任务」「空间」已经变成了「最近」和「分组」。

![更新后的左侧栏，「最近」和「分组」两个分区](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2BZOKTxiaeWH9CKazQCysxC3uiaFqvvUlktkJdOJguzdFevPWGiaCnlhRm4icAibVXzEu2ia6wDxoKu7tGcsoka0MibzeprGq8TicekYg/640?wx_fmt=jpeg&from=appmsg)

在左边「分组」标题右侧点一下，起个名字，一个分组就建好了。

![左侧栏「分组」标题右侧的新建入口，正在输入分组名](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1P6Y1JyNK5ObV2xBfpQj8Kb63z6Rzhx97B7HuenSDBiaiaLgIxyXxlUHdSWzHia1hnGjpxBhMmjBdOvg8dsCw3DokHWLIsCtlYDA/640?wx_fmt=jpeg&from=appmsg)

然后按住任务，往分组上一拖，就归进去了。不习惯拖的，点任务右边的「···」，选个分组也一样。

![按住任务拖到分组上，目标分组整行高亮（动图）](https://mmbiz.qpic.cn/sz_mmbiz_gif/J1Cdba5GUc3NNiaEibswMvtFiciaOyia4HmNTEr2B8ln1vGHggMPtfRiatVLcXOOlibuUsVvsqnHv5kQRBewibaQMZKWnaYeyLLmFbxSfGIgesO0k7w/640?wx_fmt=gif&from=appmsg)

不过拖完你会发现，「最近」里这些任务还在，看着跟没整理一样。

这时候在「最近」右边点「···」，选「隐藏其他分区的任务」，「最近」里就只剩还没归类的了。

我现在就拿它当待整理的清单用。

![「最近」右侧「···」里选「隐藏其他分区的任务」，已分组的任务从「最近」里消失（动图）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2omewXhzNb9HtXGiafqM00vUetztOrWh8qedY4bPQZnFONdSO4wjQqX3jLotX3YWp4Tm9QTBZhDqrLsXNt7niantjLy2Z9DqKe0/640?wx_fmt=jpeg&from=appmsg)

剩下的就比较随意了，分组能手动排序，常用的任务和分组也能置顶，按自己习惯来就好。

![左侧栏最上方的「置顶」区，置顶了两个分组](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1EwYiaeORegPp8DvXefuwib9tOwtBqFDq5xoA8Bcop4CbLq4SwyQzrSRWHHBZ2xvr7RJsCRe9IXPHlcSr1YOkbiaYiaq7CH4gsnMQ/640?wx_fmt=jpeg&from=appmsg)

当然，手动分类还是太麻烦了一些，所以我的方案是 **让 WorkBuddy 自己给我分。**

新开一个任务，直接把这段发给它：

●●●

我想把 WorkBuddy 里侧边栏的历史任务按工作事项分组。请你出一份分组方案，只出方案，不要修改、移动或删除任何东西。  
  
1\. 先找到这台电脑上 WorkBuddy 保存任务和对话记录的地方，只读。  
2\. 把每个任务过一遍：标题、在做什么（一句话）、最后更新时间、用到了哪些文件夹。  
3\. 按"我在做哪件事"分组，比如某个客户、某类内容，不要按 PPT、文档、图片这种文件类型分。分组控制在十个以内，每组写清组名、包含哪些任务、建议关联哪些文件夹（不超过 16 个）、哪个设为「主要」。  
4\. 分不进去的放进「待定」；很久没动的一次性问答单独列出来，建议归档，最后由我决定。  
5\. 最后给我一份操作清单，我照着一条一条拖就行。

我最后分出来，就会是这样的一个方案。

![](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc13ianVpT22jTpDdDtYwvWjib9vq3CPK8zVStSofkseYABlxAqK5HZhc07T7VQPVpicY7PK5R2B6883JCicrFlicYCnuBDzFsUuhMFA/640?wx_fmt=gif&from=appmsg)

分组定好了，唯一实在没法省掉的，还是得手动拖动来管理。

然后我就照着它给的清单，一条一条拖，二十来分钟，左边终于干净了，强迫症都治好了。

![整理完的左侧栏：置顶区两个分组，分组区七个分组，「最近」里只剩几条未归类的任务](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc3Ouf9mam1l9Bs7gEPoTbUKiap2pGpy7HYEOeZdcor9XOpOibDZwBeuJhUm0BqSHgiaD33ISv9tGWlTxAYrtPFuOlJuxLkeib7GFRI/640?wx_fmt=jpeg&from=appmsg)

当然，就是简单整理下历史的对话和任务，谈不上史诗级升级。那分组这个功能的优化，最最最最有价值的地方，是 **分组还能让资料互通。**

现在一个分组，最多能关联 16 个本地文件夹。

新建或者编辑分组的时候，点「关联电脑上的文件夹」，可以一次多选，再把其中一个设成「主要」，它就会优先参考这里面的资料。

![](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc2j3ibuB7gxHVM718yibcdJcicXqFN8EfgIgDQI1vV8WtHrpR4gWRs4D2lk2kYJcnqwrQicUfh0hI6icEeMriboyDLfdtwwTiabzX7MTk/640?wx_fmt=gif&from=appmsg)

拿我自己的「宏光项目」分组举个例子。

客户材料一个文件夹，产品文档一个文件夹，会议纪要又是一个文件夹，以前我得先把它们拷到一起，现在呢，全挂到这个分组上就 Ok 了。

所有在同一个分组内的资料是共通的。

而且同一个文件夹，项目分组能挂，培训分组也能挂，一份资料两边一起用，再也不用复制来复制去了。

**所以现在咱们用WorkBuddy的逻辑又得变一下。**

**之前是创建一个文件夹，新建一个工作空间。现在我开始一件新的任务，第一步就是先建个分组，把要用到的文件夹全挂上去。**

**而分组里面的多个子文件夹，就可以尽可能的让我们一个大项目里面的不同资料更成体系。**

这个功能真的很棒。

**最后。**

说实话，WorkBuddy 最近这段时间，更新是真的勤。

这么大体量的产品，千万人每天在用，细节上能吐槽的地方肯定少不了。

但好事是，他们一直在用户体验和这些痛点上，高频地下功夫。

我自己也经历过在腾讯做产品的时光。

刨开商业上那些事，每一个产品人都是真真切切想把产品做到最好给用户的。

期待能有更多好用的功能。

以上，希望对你有所帮助。

以上，既然看到这里了，  
如果觉得不错，随手点个赞、在看、转发三连吧，  
如果想第一时间收到推送，也可以给我个星标⭐～  
谢谢你看我的文章  
你的关注是我持续更新的动力～

我是谁

我是 AI大刘，北大毕业，大模型研究方向，腾讯犀牛鸟，先后在腾讯、百度的大模型研发部门。现在斜杠青年：给多家国企做AI顾问 \\ OPC \\ 研究员 \\ 产品独立开发者 \\ Vibe Coder

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过