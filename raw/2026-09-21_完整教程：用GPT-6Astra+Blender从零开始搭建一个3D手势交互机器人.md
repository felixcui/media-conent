# 完整教程：用 GPT-6 Astra+Blender 从零开始搭建一个3D 手势交互机器人

**作者**: 阿雅

**来源**: https://mp.weixin.qq.com/s/SbCIASY9jD0145CvR6HoGw

---

## 摘要

作者受他人用GPT-6 Astra操控Blender建模的启发，分享了把IP形象“夕小瑶”做成3D手势互动角色的完整教程：用GPT-6 Astra生图和处理代码，用Meshy生成人物、贴图、绑骨和动作，用Blender修整模型，最终实现摄像头识别比耶、点赞、画圈等手势，让角色做出打招呼、走秀、转身等动作。

---

## 正文

阿雅 阿雅

在小说阅读器读本章

去阅读

家人们，夕小瑶会动了，还能听我的“手势指挥”。

对着摄像头比个耶，她就抬手打招呼；点个赞，她开始自信走秀；食指画个圈，她也跟着转身。

这个网页我也放出来了，大家感兴趣的可以玩一下：

👉传送门 **：夕小瑶 3D 手势互动**

> https://xixiaoyao-gesture-studio.netlify.app/

初次加载3D模型会有点慢，耐心等一小会儿。另外建议用带摄像头的电脑打开，右下角点击开启互动，允许使用摄像头，再把手放进画面里。

以前吧，夕小瑶只出现在我的头像、封面和配图里。这次，我想让她从图片里走出来，变成一个能和大家互动的 3D 玩偶。

起因是最近看到不少人用 GPT-6 Astra 操作 Blender，搭建筑、做游戏，大家也在夸它的建模能力。

比如创作者 Hirokazu Yokohara 分享了一次测试：他把一张图片交给 GPT-6 Astra 后，它就在 Blender 中搭出了城市背景，还自动剪辑了展示制作过程的视频。

比如创作者 Tom Krcha 给它一张蒸汽火车图纸，要求在 Blender 里重建。

演示中，烟囱、锅炉、车轮和驾驶室被搭了出来，一辆火车出现在软件窗口里。

于是，我也试着做了一个： **把夕小瑶做成 Q 版 3D 角色，放进网页，通过摄像头识别手势，让她走路、打招呼、跳舞和转圈。**

想法很简单，实践起来却没有想象中轻松。这个作品前后把我 5X 的周额度耗得差不多了，才勉强做成现在的样子。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0hd8MxUumHPOqR6R87ZymOI2eyEiaNZlricH5TngSVfzDJ9WT9bsNXk8sdvMGdcKjh9V0uialicibw7WPCvTE3X4B0kVQHKuWcR2JFqHTrJzYiauc/640?wx_fmt=jpeg&from=appmsg)

下面就把这次的制作过程分享出来。不会建模也可以跟着做，遇到的坑和每一步需要检查的地方，我也一起写进去了。

我主要在 Codex 里使用 GPT-6 Astra，还用到了 Meshy 和 Blender。

GPT-6 Astra 帮我生图和处理代码；Meshy 生成3D人物、贴图、绑骨和挑选动作； Blender 检查、修整模型。

## ◈第一步：准备人物三视图和 Q 版风格参考图

第一步，先准备人物IP的三视图，也就是同一个角色的正面、侧面和背面。

不会画也没关系。可以把已有的角色图片交给 Codex，让它帮忙补齐视角；如果还没有自己的形象，就先描述发型、服装、配色等，生成一张满意的正面图，再以它为依据补侧面和背面。

提示词可以这样写：

> 以这张人物图为依据，制作同一角色的正面、侧面和背面三视图。保持发型、五官、服装、配色和身体比例一致，不要在不同视角里重新设计。使用简单背景，全身完整可见，三个视角的大小和站姿尽量一致。

夕小瑶原始 IP 三视图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPQ0FsrV0HYNdQx2FzXsuHqQkicCNfiaKnoLhZlTSTTlGWCvTZ5iaunN5ZTL1c9lWFwpefDuEVx0yudSYthWwiadYU8g4Deyw7AFh8/640?wx_fmt=png&from=appmsg)

准备好三视图后，我还另外给了一张 Q 版风格参考图：就是这个穿绿色卫衣、背着书包的角色。我主要喜欢它的大头小身体比例、圆润的脸和宽松卫衣的感觉，希望夕小瑶也往这个方向调整。

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHPSX4O5zb19ibL5oXh363TFZugjYRqbz9mLJWM8ERY2mXjuMnx2xibvzTgT1RvzwdA66DcSefpv4XRbab5slYicuKCVUeCT971iaso/640?wx_fmt=png&from=appmsg)

这两类图的作用不同：夕小瑶的三视图用来保留角色形象，Q 版参考图用来说明我想要怎样的比例和画风。

所以我特别强调，粉色头发、蓝色眼睛、猫耳、发饰和尾巴都要保留，不要把参考角色的绿色衣服和白色头发一起搬过来。可以提供的提示词如下：

> 图 1 是夕小瑶的三视图，图 2 是 Q 版风格参考。请保留图 1 的粉色头发、蓝色眼睛、猫耳、发饰和尾巴，参考图 2 的大头小身体比例、圆润画风和宽松卫衣感觉，制作属于夕小瑶的 Q 版形象。不要照搬图 2 的角色和配色。先给我一张完整正面图，等我确认造型后，再制作一致的侧面和背面图。

确认后的 Q 版夕小瑶：

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHOI3Dvak28oEdtJ0JcibHnAUiaCeDK1OHibOzsVfCJTOZQ406JmBBN7QIbiaLaXTmGnTFxj4q7DkDOMR5FfBzyTzeJOCPyMeqVaLEI/640?wx_fmt=png&from=appmsg)

Q 版造型确认后，再按这个版本补齐正面、侧面和背面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPYDnGAeIVNep5jawicY9ju7VBA40IEKkGoia9JOe60UgEuOAO0QKKq0UPuk0iaegUiajpIetEdkhJiaPiaXJEWvxkOSjT52YD9P2aqg/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHO524mq9713G4V3ibzAnFl1dnWIVXgic9VDBOMGlvwKibticBuFeKiajibjqVdHGr93ehT6UKwWnZktiaeiagmTXk7HGc0oGBicALsylkWw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPVNLxR0B5G7iaVtGrDMKFAovbMyyWEKEVrySjicPlBhl2dvP261NnOMs1SuoKl4FP4gYJmaefvha2waxFqSYVogp1Z4oNtQ8nXk/640?wx_fmt=png&from=appmsg)

这里需要留意一下，AI生图模型推出来的侧面和背面可能和正面不完全一致，生成后我们记得要对照一下尾巴、发夹、发束和衣服。

背景也尽量简单，别让道具或复杂光影干扰人物轮廓。

## ◈第二步：在 Meshy 生成基础白模

这里先说一下，我为什么没有直接让 Codex 在 Blender 里把人物做完。

最初我确实这样试过，但做出来的人物和我想要的夕小瑶差得有点远。

OMG，它有点吓到我了。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHMH2BVbDJt3SxZVIb4gTtfzLnDa8ovKMJnibib6ic60ZBtFS5b7UrE48FRn9cAOZzMnIM8AHDpm6iaicD4zrekgywtuxbZYuVuL1icds/640?wx_fmt=png&from=appmsg)

后来我去网上搜集案例才发现，它在建筑类场景相对还行，到了建模人物就没那么容易满意。所以我换了个办法：先根据图片生成3D形象，然后进入Blender再修局部。

这里我选的是 Meshy。它是一个网页端 AI 3D 建模工具，可以把文字或图片转成可导出的 3D 模型。

当然市面上也有很多其他工具，比如Tripo，腾讯旗下的混元 Hyper3D，

最开始我还想偷个懒，想着直接让Codex 操作这个网站，后来发现这个过程速度很慢，还很耗费额度。。。

干脆我直接上手操作，发现需要自己操作的地方其实不复杂。打开网站进入工作区，

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNrLn3Xic5icM3jAZzNUZVljbLhNrAuk6n5W0V9U9sQKHibtnghaYBORJHLUyxBibnEag2WWX9IcrTvATLKfoGzAVic71ibCS0YLgMPs/640?wx_fmt=png&from=appmsg)

上传第一步生成的三视图，然后这里记得勾选 **多视图** 和 **拆分** 两个选项。

“拆分”指的是把生成后的身体、衣服、配饰等尽量分成独立网格，方便后续在 Blender 里单独处理身体各个部件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPJqGvNZvEfVChewQWHxz2eic3ia5tJFaGQRZlKEHPUkicTJDfXwPgP6Hl865iaPbp58rPItHNKqYWqJeVfEk7wJ2zAO5I2icicFJxLU/640?wx_fmt=png&from=appmsg)

通常这一步出来的基础模型通常叫白模，可以理解成还没上色的立体坯子。先看形状，颜色放到后面处理。

生成后不要只看正面。拖动模型转一圈，看看侧面的手臂有没有粘住衣服，背面的头发、尾巴有没有变形，再放大检查脸和手。

看我第一次生成的模型，尾巴就出了问题。。。

不过不用担心，我们在页面点击绿色箭头，把导出文件交给Codex，让它直接去操作Blender修复。

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHO3A9ZrE3jOsjfs2n1RdibpwBP3aiaeHfh6wib8kxn4EKlfoZ7GNENV77iaCPZyoEOWQ0YGJZ2al7BtOjL9bSeHEaImibnwPRgvgVbo/640?wx_fmt=png&from=appmsg)

## ◈第三步： 让 Codex 在 Blender 里修尾巴

有了基础模型，Blender 的任务就明确多了：直接把明显的瑕疵修好，已经满意的造型可以保留下来。

让 Codex 操作 Blender，有两种常见方式。一种是直接操作软件界面，像我们自己点菜单、选物体那样完成任务；另一种是通过 MCP 连接，让 Codex 调用 Blender 的工具能力、执行脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNpicHjZwnIBGeMIg3JzicSWBWQ2CSxOOWT9meX7tgHxsgWEiaNTgZtTLBklGolgNTcibWVF581ehakUgNSXsjLjoTXtePYg8ZRNWg/640?wx_fmt=png&from=appmsg)

MCP 可以理解成两者之间的接口。处理重复或批量任务时，程序化操作能减少一些截图、找按钮的往返，通常更适合这类工作。 这里我建议大家使用Blender MCP，速度快还省额度。

首先我们在 Codex 安装 Blender MCP 页面 ，

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNaGt3YzLuWZTRVYOAYfOgMSDqDuDwYRayl4e4NKo6UkEpejND7e8ORPjFXdqKbyn7iaYM7prCnccgicUWtsp3MPaicGkdeQZEtrE/640?wx_fmt=png&from=appmsg)

然后把刚才 Mershy 的导出文件地址发给它，让它根据要求修改。

比如这次的尾巴，可以这样提：

> 导入我下载的模型，先另存一个修复版本。检查尾巴的尖刺、连接处和形状，只修尾巴，保留脸、头发、衣服及人物比例。完成后给我正面、侧面和背面的截图，并说明修改了哪里。

修整后的白模正面和侧面如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHPOUiauBRl5tiat6jSIXxTNFkcLHgI2gxnUuZdpcIsZjkRAjeVVyELh5DtbGibgQZZBMHJtUKuNDaHPEY3rCu03CgiaoJ7Hv5mXgbE/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHPxuqXOI5DJlbeven99CfHhicx1mo1wnNJib6JibtFS8vHPZDeCtWpdlzDEY5U3CSVDTOLHnMmaS3SotbeETibDoYBp9uRE6CrLWSs/640?wx_fmt=png&from=appmsg)

哈哈哈，效果看起来不错吧，但是整体这一步耗时也太长了吧，用了一个多小时。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNibeLp6XhBls0EUk4t2q7icibTfmrMZSVTpfq1scibUBh9Ycy17YVa9HkecEYqQBe4mdYbG4NJSY5pmo2Kcd3zUQDExNqR1lVia4ia4/640?wx_fmt=png&from=appmsg)

修复完基础的白模，接下来还有重要的一步，就是减面，减面之前先了解一个知识点： **面数** 。

“面数”是什么意思。

它指的是我们生成的白模表面由很多小面组成，三角面就是其中的一种。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPwqpY0BTMgU9rib8aHLjxEUwDCVcgPcrrtNW0YDbMQotXgvViaU8Pl9JCOqYpAfoswtvWFE4F9TG2w7b65andNdd0ZbZm6q9edU/640?wx_fmt=png&from=appmsg)

像我最初在 Meshy 生成的白模显示有 3,074,822 个三角面。面越多，描述的形状越细，但处理和显示的负担也会增加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOVibiawSJFa7hZU5h21YJV5pswbiaZZG0nVmtvsyrmiaUoIzVtnQn3PjHcD97xIxiawYVeROgaOiaTnenP44MGEcJ98Tia61D08vdp4c/640?wx_fmt=png&from=appmsg)

由于我的网页还要开摄像头、识别手势、播放动作，所以没必要把所有细节都用几何结构硬撑出来。

这里我们只需要告诉Codex 完成修正后，进行减面，把白模的面数降到适合在网站交互的数量就可以。

> 保留原始高面数模型，另外制作适合网页使用的减面版本。优先保护脸、手指、猫耳和尾巴的轮廓。完成后给出面数和对比图，检查破洞、尖角、手指粘连，以及轮廓是否明显变形。

## ◈第四步： 贴图，让白模变回熟悉的夕小瑶

结构修好后，可以直接告诉Codex 把刚才修正减面后的模型直接导入放回 Meshy，完成贴图。

贴图是映射在白模表面的图片，眼睛的颜色、衣服的图案等细节都可以通过它表现。材质还会影响表面怎么反光，比如看起来是哑光的，还是像塑料一样亮。

操作时选中修整后的模型，进入贴图功能，用刚才第一步确认过的角色图作为参考，再生成并检查结果。

我在 Meshy 手动贴图后的效果：

![](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHPSafXQ0lcN95T00XP6NicfTGchYH8usby7wH6Ytxm0zNxeTic9Fe46TDDa0GZop38W5WG2gOIJ52d3U79j0mWySQFthwH5fd904/640?wx_fmt=png&from=appmsg)

这一轮我主要看眼睛、眉毛和嘴巴的位置，再转到侧面、背面，检查头发与衣服之间有没有串色。有些正面看不出来的色块，转过去会很明显。

## ◈第五步：绑骨，再挑几个适合她的动作

上好色的模型还不会自己动。接下来要做的是绑骨，也就是给角色装上能够活动的骨架。

Meshy 有自动绑骨和预设动画。选中人物，进入绑骨或动画入口，按界面要求确认骨架或定位点，完成后先预览几个动作，再决定是否保留。

这是我给设定的基础跑步动画预览：

除了基础的跑步，我又加入了自信走秀、大方打招呼、跳舞和摆臂舞步等各种动作。

## ◈第六步： 导出 GLB，做成网页

模型和动作准备好后，我把它们下载到本地，交给 Codex 接入网页。这里用的是 GLB 格式。

GLB 可以把模型、材质、贴图和动画等内容装进同一个文件，网页加载起来方便。

在 Meshy 下载时选择 GLB，并确认所需动画包含在导出内容里。如果动作分成多个文件，就放进同一个文件夹，保留原始文件名，方便 Codex 对照整理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOcibvuIZsTNBvHLqKlN7GOcgNHjsEWm55uqmExqnP4cmfKdv9seBwnk5CCqhiap9b9djib92E1JMUf39NyiblubpIxTU6Kc7zsIkM/640?wx_fmt=png&from=appmsg)

开发网站项目的时候，我们需要简单的了解一下：Three.js 负责显示 3D 人物，MediaPipe 负责提供手部识别信息，代码决定播放哪段动作、缩放多少、旋转多少。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHN7CfH4HTDgFSrzgBCXRHPEo19prO9lLE6o69972J6KQmTXwsTYM5Q8mNavQ74QEibkpXKJoT5qmOT8icYBxERtovYAGibatScNmw/640?wx_fmt=png&from=appmsg)

> 使用我提供的 GLB 和动画，制作摄像头手势互动网页，按上面的表格设置控制。同一个手势只对应一个动作，手势短暂稳定后再切换，避免频繁误触发。默认播放自信走秀；画圈控制旋转，停止后平滑回正。提供开启、关闭互动的入口，并说明本地怎么打开测试。

网页背景方面我这次做了虚化的霓虹城市背景、倾斜的透明代码卡片，开启摄像头后，在角色后面加了连接线，切换动作时，卡片里的代码跟着变化。

确认本地版本没问题后，再让 Codex 部署到支持 HTTPS 的托管平台，我这里使用的一个免费的部署平台 Netlify，在Codex可以直接搜索这个插件安装，部署完成后就可以把链接分享给朋友了。

## ◈最后

做到这里，夕小瑶终于从一张图片，变成了能在网页里走路、跳舞，还会跟着我的手势转圈的 3D 玩偶。

虽然中间修尾巴、调动作花了不少时间，额度也消耗得有点心疼，但看到自己的 IP 真正在屏幕里动起来，还是挺开心的。

而且，这个人物后面还可以做成 **3D 打印的小摆件** 。以后说不定大家就有机会把屏幕里的夕小瑶摆到桌上了。想想还挺期待的。

如果你也有自己的 IP，可以照着前面的步骤试试。工具和提示词都放在文中了，动手时可以随时翻回来对照。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qEyDKnkjcT4bd38ljNdEGscMzUYibunoJ8KWC3aUv6EUpdes1rbU2Kp7TQXqFwMicLuciaz9q7tiaI3UQ/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qFTxv9NHS6qfAMNc8vX6mCflXssEayu9ZeR87weY35R6n50juv6Pme03oV49a3l3YM9VKJvNKWgjQ/640?wx_fmt=png&from=appmsg)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过