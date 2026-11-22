# 3万star！huashu-design 3.4 发布！让你的Agent做出顶级App设计

**作者**: 花叔

**来源**: https://mp.weixin.qq.com/s/c0yz12AGZQf5MhqUIJhL9w

---

## 摘要

huashu-design开源项目star数突破3万，作者用Fable5.2模型大幅优化并发布3.4版本，新增小红书头图设计、DeepSeek Harness支持，并通过拆解90个苹果年度入围App的1572张截图提炼出八条设计口诀，重点提升了Agent设计App的能力与丰富度。

---

## 正文

花叔 花叔

在小说阅读器读本章

去阅读

先说个好消息！！！huashu-design在GitHub的star数过3万啦，这是继女娲skill之后，我的第二个3万star的开源项目。

![](https://mmbiz.qpic.cn/mmbiz_gif/aNEfzwzDSWic1SxCTgic8GR6IQB1SGxiaIhahKGN16zbqYJqqdk7of8q8gfUEMfEibMiaKPjZTInHVpzR3RbCxAvmGDcqTwwK8JomeyZy9dnIQzw/640?wx_fmt=gif)

于是呢，最近一周我也花了很大力气，用现在最强的Fable5.2模型对huashu-design做了大大大幅度的优化和迭代。

上面这支片子里的每一个界面都是huashu-design自己做出来的。相比10月份发布的3.0版本，这一期的更新包括：1）除了网站、app原型、PPT之外，huashu-design也可以帮你做出出色的小红书头图设计了；2）我给huashu-design增加了对Deepseek Harness的支持（当然，Workbuddy、豆包工作、千问办公等国产agent也都是可以使用最新huashu-design的）；3） **最最最重要的！！我还把huashu-design设计app的能力，提升了一大截！！** 并且设计的丰富度也大大提升了。具体怎么做到的，后面会细说。

## 它是什么

这个之前介绍过很多次了，就不细说了，简单来说呢，这就是在借鉴了4月Anthropic发布的Claude Design之后，结合我的设计探索，做出来的一份能让你的agent在做各种类型的设计都能变得更出色的skill，目前已经开源发布半年多了。

装上之后，在agent里说一句「做个XX的网站」「做份PPT」「做个App原型」，它会先摆三个方向的真实设计让你挑，挑完再往下做，交给你的是网页、能点的原型、能导出可编辑PPTX的幻灯片、动画或者信息图。

发布9个小时1600多star，6月发2.0的时候16k+ stars，10月23日写3.0那篇的时候是25k+🌟，今天过了3万啦！

![](https://mmbiz.qpic.cn/mmbiz_png/aNEfzwzDSW9z73sLYemNYOrzPU6W5npGnY9noxILRqULmGKTibq9unQgxBa4jNX7g95aP1VEYibcuB4d7vbAN2iasuyb7VYhNSzgbQuIQAeLvE/640?from=appmsg)

MIT协议，商用也免费，能装skill的agent基本都能用。

## 3.0之后的三个小版本

**3.1（10月31日）加了小红书图文。** 一组3:4竖图的八种范式（标本志、贴纸本、索引、长卷、日报、集换卡、留白、信息图），每张样张同时是能直接改的模板，一条命令切成成图，顺手查字号、出界和长卷跨缝。

**3.2（11月4日）装进了DeepSeek Harness。** 一行命令就能装成插件，导出PPTX和PDF要用的依赖会一起带上。

**3.3（11月10日）加了打磨环。** 页面写完之后它会先按原尺寸逐屏截图，自己看着截图改一轮再交给你。另外给轻量模型留了一条稳妥轨道，能力强的模型放手做，轻量一点的模型从样张改起。这一版还合了两位社区朋友的修复（PPTX导出截错图、配音混音报错），感谢。

## 3.4：我去拆了90个苹果年度入围App

说起来这次更新的起因挺简单的，我想把App原型这一块再往上提一大截，agent做App，主屏做来做去大概还是「导航栏＋卡片列表＋底部五个tab」那一套。

所以我让agent把2025和2026两届App Store Awards的入围名单全拉了一遍，一共90个作品，89个取到了商店截图，1572张，一个一个看过去。

看下来有个挺明显的规律：这里面做得清楚的那些App（入围不等于界面都好看，有的是靠社区入围的），主屏很少是一张列表。它们大概都先回答了一个问题， **这个App管的那件事，在现实里长什么样？** 界面是从那个形状里长出来的（有些拟物，让用户的直觉更容易在app界面上应用的意思）。

最后提炼成八条口诀： **界面即世界、签名物件、时间有形状、一套语义色、内容当主角、AI落在物上、角色承载状态、可达性定形式。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSWicfs1tibJZoibDxBgQxkicSq0gN2VdXuWb3sBo9LCDHPRm5fYplfGJXjA60MNuQlfYNtM9E4k7eibrOZzHJ0Zhh3qsJrhQe6UEDjMM/640?from=appmsg)

反过来，这两届里几乎没看到的东西也挺有意思：紫蓝渐变的AI感、占掉主屏的聊天框、每张卡片一个彩色图标、五个tab平均用力（没有，这些boring的设计一个都没有！）

## 特点一：借鉴，但别特么抄袭

然后呢，其实第一次实测就出了问题。

新版会真的去取入围App的商店截图当参照，结果参照得有点过了，有一个方向直接贴了上去，底色、强调色、进度条的形状都跟它的参照App对上了。

这其实是个老问题的两头。把一个好设计概括成一句「大留白、克制的强调色」，信息已经丢了大半，再让模型把这句话变回页面，补上去的是它自己的平均印象。可你要是让它把原图看得特别清楚，它又容易做成翻版。

我最后定的办法叫「借一层，不借一身」：一个参考拆成三层，它在解决什么问题、用什么结构解决、长成什么样。中间那层可以借，配色、字体、形状这些长相一律从你自己的题材里重新长。看的时候看原图、量数字，做完再把自己的图和参照并排摆回去，问一句：熟悉原作的人会不会说这是它的新版本？会，就把长相换掉重做。

加上这条之后，我出了一道家常菜谱App原型的题。它找的参照是一个入围的日程App，这是那个App的商店图，我把它借走的那一处圈出来了：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSW8PSBh6J3X4SWwp6kP1mYg5e5Mvz8zicm9W2IPbUpzCyAkbOkwwdO0OnVdgks5NzyeWfmUrjh8qgkKYiao8CATnSw2Q8sFX8hRM4/640?from=appmsg)

一件事占多长时间，那个胶囊就有多长，它主要借的就是这一样。然后这是它交的方向，叫「饭点」：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWicaQh6TqZQfDZEkaYibndOHUz3vYhc2osoZWOWgENrKxdZIvvicpYjVZ47aSnSdaZD2gzFYSyJBsmyeU1BjFvO8qVYgib5yCTmEEA/640?from=appmsg)

这个结构被搬去了做饭，你告诉它几点开饭，红烧肉要55分钟所以那根柱子最长、最早动手，蒜蓉菜心只要6分钟，排在最后。粉色、圆润的字、那套图标，一样都没带过来。（左边做法那一屏里，时间做成了能点的计时钮，这个是它从另一个做菜App那借的。）

## 特点二：该是图的地方，放真的图

去年年初我写过一篇「一句话生成高保真app原型图」，那段提示词里就有一句「使用真实的UI图片，而非占位符图片」，当时的办法是让它去Unsplash上找。

快两年过去了，agent做原型的时候常常还是特别爱拿emoji、手画的SVG和灰色方块顶替图片，这个对观感的影响其实非常大。我把仓库里一张样张上代码画的阳台花架换成了一张生成的照片，其他一行没改，观感差得非常多。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWicMBzlnBXDAOo3CnZbqVYsicqPBbqkcq8mF4lSoJKpuMAwfBUoeicnLKicQRKj3r8BqzXZRV6A7EC8RfOzTlic01DWrT5hshTD2iaibY/640?from=appmsg)

所以3.4会先看自己在哪个环境里：Codex、豆包、WorkBuddy这类自带生图的，界面里要用的图直接生成，出几张挑一张（WorkBuddy生成的图右下角带水印，关不掉，3.4.1起遇到这种会自动换下一个来源）；Claude Code、DeepSeek Harness这类不带生图的，去借本机的Codex，或者用你给的生图API（我最推荐GPT-Image 2.6和Seedream 5.5）；实在都没有，就去取开放许可的真图。

还是上面那道菜谱题，除了「饭点」它还交了另外两个方向，里面的菜全是它在Claude Code里借Codex生成的。

一个叫「灶台」，深色的硬件面板风格，火力是一个能拧的旋钮，计时用的是橙色的数码管字：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW8lkk6wbCz1iayyYyAbZF0ybxbicMIYsl19hZDaJiaMOAmTSdI7V7iaM5rzfsBgf4VnA933aeXdtbHhTZmUjb1TpdOFygu9TRvAiaMQ/640?from=appmsg)

另一个叫「食单」，做成了一本摊在灶台边的小书，米色纸、宋体字，配料、做法各占一页，翻着看：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWicBWZ6XnPrQOvAg8hEp1pb5SEwVzLhGzaiafCIvq3HIuEJRyqeIFcXRWfzHgAvKEROwoDicgr3ia6K1j0icp4dM2pJ4qibAkp7aibAMM/640?from=appmsg)

「做一个旅行手账App原型」这道题我觉得有两版不错。第一版让照片当主屏，一打开就是今天拍的那张，文字压在照片上：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW8JrjxY5wBSPJP0cvCQIMmS53n7gxST3hS7RGgqJyPib4khYAQCkjib9AAibGcmibiasAxibEwYictJhrak0SVoaicj61PkUicib8JicthjbI/640?from=appmsg)

第二版换了个思路，主屏是一张等高线地图，今天走过的路线直接画在上面，下面是公里数和步数：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW9DSxQVyul0ScyomU65P9uPiaVawUvIw2oNvY9q6rfKs5cYQAdn8ibUJj8aEvz9fqqVymcQPFn242pCfh9NzEKxwclvanHXvOoo4/640?from=appmsg)

## and，顺手加了App Store宣传图

拆那90个App的时候，它们的商店宣传图我也一起看了，连幅、破框、一句话拆两张、一张一色，这些手法挺成体系的，于是顺手做成了一个新模块。

说一句「给XX做一套App Store宣传图」，它按1320×2868出图，还会出一张搜索结果里的缩略预览。奖项、评分、用户评价这些它不会替你编，没有就不放。

我拿上面那个「饭点」的原型接着跑了一次，让它给饭点做一套App Store宣传图。这一版是连幅的做法，三张连成一幅，底下那条「开饭」的线从第一张一直拉到第三张：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSW9OBLxMsEPuRPKky2QMR0reTB47UWoGAeBGeibATvbtBr15PRn9KCEPeO7a19ADrOeyREUdFFtibBia2CSLNj92KGic4MdUfFboicrs/640?from=appmsg)

这一版每张是一个问句，背景直接铺满那道菜的照片：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSW862Kx8CuXSHI5zQ6RJKMcYj5Txz9mAoGHb601DKhV1N2xa63fqYEpvD5rWhbJhG5xsOcBzH4nIMibnuxQdVib5Xg1kKfBRlMkdU/640?from=appmsg)

## 做网站也跟着变了

App这套想法对做网站其实也一样有用，题材在现实里长什么样，页面就从那里长出来。我出了一道题：「做一个马尔代夫旅行观光局的概念网站」，就这一句。

第一个方向叫「一条线」。马尔代夫南北很长、东西很窄，还跨着赤道，所以它把页面的滚动轴直接当成了纬度，左边那根深蓝的竖条就是这个国家，你往下滚，就是从北往南走：

![](https://mmbiz.qpic.cn/mmbiz_gif/aNEfzwzDSWicHAmZsx0eWr8s9zVWTr2jKCj38PHmicDHO5F57bYmQdqMfI16D0mLDpgZVDUszVJCRNyeMJkBibjicXsnco1WtnVMWTrlibLdnreU/640?wx_fmt=gif)

第二个方向换了个完全不同的思路，叫「风向轮」。那里一年只有两种季风，它就做了一个能拨的十二个月的轮子，拨到哪个月，风从哪边来、哪一面海平静、适合去干嘛，跟着一起换：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aNEfzwzDSWicibD3A8C52gj40utDy8x7I7icLPLuE9HvbUCTwmmwX8a6YiaH8M4FvjHGAhwVwRN6QKtsnmQc7LGnkp4wJPtdUkuG0AgNTWg8Ezw/640?wx_fmt=gif)

它还做了第三个方向，「天空占九成」。岛只比海面高一米多，所以整页都是天，从黎明滚到夜里，右上角的钟跟着走，地面永远只有最底下那一条线：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aNEfzwzDSWic5DcZzJzwJvAtmkLHJXDGibzlrLTcBiaY2RuR3uMnwBc0icmx4LXPhwFub4iaUrLiaEY4DXmr8df4oEJmCnW5tQcqlWpCO7ubJibwa4/640?wx_fmt=gif)

机构名是概念稿，图是它生成的示意图。

## 最后，怎么装呢？

没装过的，可以复制下面两句话给你的agent：

```
帮我去GitHub：https://github.com/alchaincyf/huashu-design 安装这个skill的最新版本 如果访问有问题的话，也可以执行以下命令安装：npx skills add alchaincyf/huashu-design
```
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWibxtPLuH3jelV9ibDgISHVOpvXwVfZX3f6PlO8LN1bEa6JMkV8BUuBVBOg0BaK9ylSAiaicSViaibcltZ550IK8rQw6UkT8Aanh38KU/640?from=appmsg)

如果你想了解更多这个skill信息，尤其是它的更新迭代历史的话，也可以直接去访问GitHub仓库页面，顺手右上角点一下Star，新版本出来GitHub会提醒你。

用了觉得哪里不对，欢迎在评论区或者GitHub issue里告诉我，我接着改。

哦对，顺便说一下，我的第三本纸质书《图解Agent Skills》刚刚出版上架啦！

如果你或者你的朋友对于如何使用skills去更好的提升工作效率有需求，或者你想知道更多我在设计女娲skill、huashu-design等skill时的想法。又或者，你想学习一步步如何搭建自己的skill，可以考虑看看👇

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过