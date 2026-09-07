# GPT-6最佳拍档＝字节Seedance

**作者**: 关注前沿科技

**来源**: https://mp.weixin.qq.com/s/QYn2OeBXhsO2O7XLwE0lfA

---

## 摘要

GPT-6的Agent（Astra）展示了与字节Seedance 2.5协作的AI全流程影视制作能力：人类仅给出一段总要求，GPT-6便自主编写故事、在Blender中搭建3D场景完成影视预演、布置机位并生成参考帧，再调用Seedance 2.5将预演转成带人物动作与镜头运动的正式视频，最后自行剪辑导出成片。

---

## 正文

关注前沿科技 关注前沿科技

在小说阅读器读本章

去阅读

##### 闻乐 发自 凹非寺量子位 | 公众号 QbitAI

GPT-6咋跑去给字节Seedance打工了？？？

而且这一打，还是身兼数职的那种——

写故事、搭场景、摆演员、定机位、做分镜、生成视频、剪辑成片……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A6fTew8FFGFYOZozLiaib3544IsUcHoUjyT8ovsD84HhFyIr6jmbiayQTa8cDD4JKF9wLfq3z9zCmtUk7gZIkPLcIgFwOclYdiaD99rEoYxQSmA/640?wx_fmt=png&from=appmsg)

好好好，这波是GPT-6负责当导演，Seedance2.5负责出片。

表面上看，是两名动漫角色在日式街巷里拔刀对砍。

镜头一会儿从屋檐掠过，一会儿贴着人物快速推进，角色从对峙、冲刺到近身交锋，前后几个镜头还能保持在同一片场景里。

放在现在的AI视频圈，单看成片可能还不至于让人当场瘫坐(doge)。

但你再看看Higgsfield交给Astra的任务：

> 想一个剑斗故事，在Blender里完成预演，使用Seedance 2.5生成镜头，再把这些素材剪成最终版本，同时保持角色与场景一致。

也就是说，人类只给了一段总要求，剩下从Brief到最终导出，GPT-6 Astra自己在桌面上全包了。

不er，GPT-6发布会上还在KiCad里画电路板、在Blender里盖房子——

这才过去两天，网友已经顺手给它安排进影视基地了。。。

## GPT-6当导演，Seedance负责把戏演出来

整条实现路径，看起来多少有点像一个AI版动画剧组。

GPT-6 Astra拿到任务之后，首先要做的是从头编出一个能拍的故事。

谁和谁打、为什么打、在哪里打、动作怎么推进、需要几个镜头，这些东西得先捋明白。

故事有了，它再打开Blender。

根据剧情把街道、房屋、人物和道具先搭成一个相对简化的3D场景，然后把两个角色放进去，安排他们在不同镜头里的位置和移动路线。

这一阶段做的就是 **Previs影视预演** 。

这么折腾一圈之后，整场打戏其实已经在Blender里用3D模型排练过一遍了。

GPT-6 Astra随后根据预演画面，继续生成不同镜头对应的参考帧，再把角色形象、场景画面和动作参考交给Seedance 2.5。

到这一步，字节Seedance才正式进组。

它负责把静态的参考帧和粗糙预演，转成真正带有人物动作、镜头运动和动漫质感的视频。

当然了，生成完成之后，Astra还没下班。

它再把Seedance生成的各段素材拖进剪辑工具，挑选镜头、排时间线、拼出完整版本，最后导出成片。

更准确地说，是GPT-6把多个工具和模型攒成了一间临时片场：

**GPT-6 Astra写故事、操作Blender完成预演，再调用Seedance 2.5生成正式镜头，最后回到桌面完成剪辑和导出。**

人类搁外面等着收片。。。

什么AGI先放一边， **Seedance 2.5这波接得确实挺稳** 。

紧接着，网友又把这套玩法搬去了 **木叶村** 。

Astra先把场景做成3D Blockout，也就是只保留建筑结构、人物位置和大致空间关系的简模。

然后在Blender里提前架好6台摄影机，分别决定6个镜头怎么拍。

镜头确定之后，每个切点都会导出一张画面。

这些画面再交给 **GPT Image 2** 进行细化，把原本粗糙的3D灰模变成带有火影风格的关键帧。

最后，Seedance 2.5登场，一条30秒、包含6个镜头的木叶村同人短片，就这么给攒出来了。

动画还没拍够，GPT-6和Seedance又对中国短剧下手了。

这次的玩法更抽象，一句话，把一部30集中国短剧改成美国版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A6fTew8FFGFibTrTA2vZFB4ianCGGiaXSlq78R4OEE2NH66n0wrtoE7ZZrZPYkxXFvj4gH990HQviabRwSVV1DkXyRbNian8u7ic0nHw72md5ib9yw/640?wx_fmt=png&from=appmsg)

在对比视频里，故事主线和镜头节奏基本照搬，但人物、场景、语言以及文化背景全部换了一套。

中国AI演员脸换成美国AI演员脸，原来的房间、街道和服装被重新生成，画面构图和人物动作则尽量跟着原片走。

## GPT-6、Fable5.1、Gemini 3.8全来找Seedance拍片了

而且吧，跑来找Seedance搭班子的还不只GPT-6。

这两天，GPT-6 Astra、Fable 5.1、Gemini 3.8 Flash轮流写Prompt，然后统一交给Seedance 2.5拍成视频。

好好好，Seedance直接：开机！！！

同一份Brief到了不同模型手里，还真拍出了三股味儿。

有的版本把重点放在人物动作上，镜头跟着事件快速推进；有的更强调构图、光线和氛围，整体看起来更像经过分镜设计；还有的严格沿着任务往下执行，信息给得完整，但导演感相对没那么强。

GPT-6 Astra和Fable 5.1还被抓去连考好几轮，依旧是Seedance 2.5。

比如，手绘日式怪谈：

或者，水墨动画：

先别管GPT-6和Fable谁赢，Seedance这水墨效果确实有点东西。

一圈对比下来，三家大模型的胜负还没吵明白，字节Seedance倒先稳坐片场C位了。。。

## Seedance下班之后，GPT-6又去DaVinci当调色师了

从片场下班之后，GPT-6紧接着又去兼职调色师了。

这次GPT-6打开的是DaVinci Resolve。

网友给了GPT-6 Astra一张参考图片，让它像专业调色师一样，把原视频的颜色调成相近风格。

它需要观察参考图里的色温、对比度、阴影、高光和整体色彩倾向，再操作DaVinci里的调色工具，一点点修改视频。

最后用时4分钟的效果be like：

从前后对比来看，原视频整体偏平、偏灰，处理之后色调明显更浓，阴影被压低，画面的冷暖关系也更接近参考图。

当然，网友对于这位AI调色师的评价，就没有动画短片那么一致了。

有人觉得4分钟完成参考图风格匹配确实方便；

也有人毫不留情地表示，调完之后反而更难看了。。。调色应该服务于故事，颜色本身也可以是叙事母题，AI显然还无法真正理解这些创作意图……

![](https://mmbiz.qpic.cn/mmbiz_png/A6fTew8FFGE5s64q8MMcsbWfDSjNawuo2vZLmRKicwz0N1WHDvvYHQhAWbC5qgDfhiahkZdib79rU0Zs8gyOHaXgdYibD8v3PYG8gk2G6C6nlr4/640?wx_fmt=png&from=appmsg)

只能说，很有影视行业传统艺能，工具刚刚进组，审美之争已经先打起来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A6fTew8FFGHIffwIGUwzs9rjRAxWmPAR3SCbicgVmmGAlI7WdQY0KtTCDeJg00o89n2fDgMbT0vUVMgMwtypXqiacJicNGMREJ34mvEuM9kka0/640?wx_fmt=png&from=appmsg)

发布会上，OpenAI还在努力证明Astra可以操作各种专业软件，到了网友手里，使用说明已经被玩出花了。

至于Seedance——

人在字节坐，GPT-6莫名其妙就成了自己的最佳拍档。

Sora：那我呢？？？

*参考链接：*  
*\[1\]https://x.com/higgsfield\_ai/status/2096352124754104618?s=20*  
*\[2\]https://x.com/groovestreetgen/status/2096354475879600432?s=20*  
*\[3\]https://x.com/Pinkuo\_/status/2095754189548986426*  
*\[4\]https://x.com/eachlabs/status/2095911062499381467*  
*\[5\]https://x.com/eachlabs/status/2095911062499381467*  
*\[6\]https://x.com/higgsfield\_ai/status/2095609438946394380*  
*\[7\]https://x.com/AngryTomtweets/status/2095654817154908253*  
*\[8\]https://x.com/higgsfield\_ai/status/2096334648016253339*

**一键三连** **「点赞」「转发」「小心心」**

**欢迎在评论区留下你的想法！**

— **完** —

**🌟 点亮星标 🌟**

**科技前沿进展每日见**

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过