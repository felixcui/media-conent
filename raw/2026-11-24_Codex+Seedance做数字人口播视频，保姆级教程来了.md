# Codex+Seedance做数字人口播视频，保姆级教程来了

**作者**: 过客AI

**来源**: https://mp.weixin.qq.com/s/tH47PkOvR_nGXKuNGBLkVw

---

## 摘要

一篇五步实操教程，用 Codex 加 Seedance 做数字人口播视频。第一步让 Codex 写 15 秒口播稿，限定只讲一个问题、开口先说问题、句子要短、用聊天语气，写完再朗读着改。第二步把稿子放进 MiniMax 或豆包配音，选适合教程的音色，也可以克隆自己的声音，先生成一小段留着驱动口型。第三步用 Seedance 2.0 fast 出人物出镜：人物参考图和配音文件放进同一个任务，参考图锁住人物、服装和构图，配音驱动口型；真人素材要先确认使用权限。第四步用 HyperFrames 做动态演示、字幕和合成，先出 15 秒预览，确认字幕在手机上看得清、口播和画面对得上，再做完整段落。第五步合成交付。作者提示配音试听、检查清单这类段落可用旁白配演示，省掉重复生成人物的时间。

---

## 正文

点这里关注→ 点这里关注→

在小说阅读器读本章

去阅读

大家好，我是AI实战博主过客，用系统专栏拆AI工具与实战玩法；独立运营200人付费AI陪伴群，全年直播课陪跑；关注后加微19350634199，免费领10万字的《AI实战知识库》

不好意思了，拖稿一周的数字人口播视频教程终于来了，最近因为校园行的演讲确实时间比较紧，这周又有好几场，不过我后面会做好时间管理的，大家放心。

这次做了两个版本，一个是视频版，一个是文字版。想看视频教程的，直接戳下方就可以。

下面是文字版的教程。我们开始。

如果你也想做一条，手边准备好一个主题、一张有权使用的人物参考图就可以了，一共5步，不难的。下面是我把 YOYO 这条视频做出来的五个步骤。

GUOKEAI

01 第一步｜先写一段你自己想表达的口播稿

比如我做这条视频，主题是数字人，讲给第一次上手的人听。

我是把下面这段话直接发给 Codex。当然你给其他的agent，比如豆包工作，workbuddy也是OK的。

●●●  
帮我写一段 15 秒的中文口播，讲给第一次做数字人视频的人听。只讲一个问题。为什么数字人的文案要先读出声？开头直接说问题，每句话短一点，用平时聊天的语气。

初稿出来， ==自己读一遍。== 遇到一句话读到一半想换气，就拆成两句。遇到「提升自然度」「优化表达」这种说出来有点空的词，就改成听得见的动作。比如把「优化文案表达」改成「读一遍，哪里拗口就改哪里」。这样改完，稿子就能送去配音了。

GUOKEAI

02 第二步｜把稿子变成配音

把改好的稿子放进 MiniMax 或豆包的配音工具，选一个适合教程的中文音色。你可以用自己的声音，也可以从平台提供的音色里选一个。先生成这一小段，保留音频文件，后面做口型要用。关于配音这块我之前写过详细的文章，可以戳这篇查看。 [语音及声音克隆的方法](https://mp.weixin.qq.com/s?__biz=Mzk2OTA4OTM5OQ==&mid=2247490373&idx=1&sn=af44a0cd8dbe038f6527dc41f0cc8d73&scene=21#wechat_redirect)

![配音试听与音频波形](https://mmbiz.qpic.cn/mmbiz_jpg/bh9XUZB5jhpaWSb3iaVMaggz9FaedjYRYgmXtwo6ibWAWwViaj48IYkmHJnLJ55u307JaMbKYfmFr1U2xCP0FyhI2CMCOwNMqicb26oMAtPuAg0/640?from=appmsg) GUOKEAI

03 第三步｜用形象和配音生成口播母片

我是用的Seedance 2.0 fast生成的人物出镜视频。把 **人物参考图和配音文件** 放进同一个生成任务里，分别说明两份素材怎么用。参考图锁住人物、服装和构图，配音用来驱动口型。人物形象可以用照片或视频，采用真人素材时，先确认你有使用权限，按所用工具的要求提交。

第一次做母片，可以先用下面这段提示词。

●●●  
用附件中的人物参考图保持同一个形象、服装和背景。以附件配音驱动口型，做一段 9:16 的竖屏口播。固定中景，看向镜头，双手自然放在桌上，做轻微的头肩动作。请输出干净的母片，字幕和画面演示留到剪辑时加。

因为我的豆包工作seedance有额度，所以我是在豆包里面用的，你们也可以直接在codex里面调用API，我在豆包工作里面是这样来沟通的：我把图片跟音频直接发过去，然后说明我的要求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bh9XUZB5jhpbKsBsHloiaXXlXjRmUgO2hLHqacesTPpYD89FibPYB2RibM2Efu9TFvpibVpN4w3FOcHUxJKicj9SNcIcTIIuHSlByWlfT5fjXEog/640?from=appmsg) GUOKEAI

04 第四步｜把需要看懂的内容用hyperframes做成画面

我会先把母片和稿子一起交给 Codex，让它按句指出哪里适合让 YOYO 继续出镜，哪里换成画面更清楚。讲操作就上录屏，讲效果就放前后对比，讲流程就把动作拆成几步。这样整个视频A B role都比较丰富。

![HyperFrames 时间线演示](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bh9XUZB5jhrCLiaIibYhkXz5XRT4t3wOb9ecicGqoSCdbGJATzeaxcJ1HRqxdv5WyjMH3kXcwiatotAt9jtcgbG0ZCY5uiau0Y3IBDzfUXA71OAc/640?from=appmsg)

我是用 HyperFrames 做的动态演示、字幕和最后合成。我的做法是先出 **15 秒预览** ， ==确认字幕在手机上看得清楚、口播和画面接得上== ，再做后面的段落。像配音试听、检查清单这些部分，可以直接用旁白配演示，省下重复生成人物的时间。

GUOKEAI

05 第五步｜把流程做成skill

第一条跑通后，把 **写稿提示词、人物参考、声音设置、剪辑工程** 放在一起。经常要做同一类视频，就把这些整理成一个 Skill。下次给 Codex 一个新主题，先复用跑通的流程，再根据这次的内容换文案和画面。

![](https://mmbiz.qpic.cn/mmbiz_png/bh9XUZB5jhozjQHwgacqESpWonViaAljDiaiaWgGiaVVXPL4M4GWInU5FYdEBIwr4CpY8TaSSkoKyk8U0wun9iblk69ianvP1fd0n7ibe9EwATxsjY/640?from=appmsg)

这个skill我共享到实战群了，群友可以直接用。有skill方便一些，没有skill的走一遍5个流程，然后自己做一个skill也可以。

大家好，我是AI实战博主过客，用系统专栏拆AI工具与实战玩法；独立运营200人付费AI陪伴群，全年直播课陪跑；关注后加微19350634199，免费领10万字的《AI实战知识库》

![关注过客AI并加入交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/bh9XUZB5jhohIqeXfpZAjjPBvowPuaFJicqibo070p8lkX9AiauW6BNUdhYJicBXqIfYje0OGcy2UnvnMOJ6icGHM84w6dIBe9ibuhBEMjyKFsSqE/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过