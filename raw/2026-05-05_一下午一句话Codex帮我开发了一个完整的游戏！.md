# 一下午一句话 Codex 帮我开发了一个完整的游戏！

**作者**: 歸藏的 AI 工具箱

**来源**: https://mp.weixin.qq.com/s/607NOxMvkny4RlLLe3tzRg

---

## 摘要

作者仅凭想法利用Codex在一下午内开发完成了一款包含完整战斗和卡牌系统的roguelike游戏并开源。Codex展现出超越单纯写代码的全链路规划与执行力，它不仅自带图像生成和浏览器工具，还能在没有人工干预的情况下自动反推需求，自主生成绿幕素材、寻找并调用抠图工具、建立完整的角色资产处理流水线。这种从设定目标到自主补齐实现路径的能力，标志着AI开发工具已进化为能独立解决复杂工程问题的全能型助手。

---

## 正文

歸藏的 AI 工具箱 歸藏的 AI 工具箱

在小说阅读器读本章

去阅读

昨天上午我闲着没事，想做一个类似《杀戮尖塔》的爬塔卡牌游戏玩玩。

我不写游戏代码，也不碰引擎，全程就是把想法丢给 Codex，让它自己折腾。

一个小时后，一个叫《夜巡录：荒庙篇》的志怪题材 roguelike 就能玩了。

标题页进地图，走普通战、精英、事件、商店、休整，一路打到荒庙正殿的 Boss。

七个怪物、二十张左右的卡牌、符印、香火、焚符、请神四条爆发链路都能跑。

剩下几个小时，都在让它变得不像一个 demo。

受击反馈、音效、音乐、卡面、待机动画、结算视频——这些小东西决定玩家会不会相信「这是个游戏」。

**项目已开源** ，桌面安装包 macOS 和 Windows 都打好了

https://github.com/op7418/Night-Patrol/releases

整个下午有几个瞬间是真的把我震到了。

Codex 的模型能力已经不算新鲜事。

让我在意的是它自带浏览器、自带 GPT-Image 2.0，再加上那种不达目的不罢休的执行力。

三样东西摆在一起，能力已经和 Claude Code 完全不一样了。

接下来说一下我是怎么跟它一起开发的，顺便说一些在开发过程中令我震惊的事情：

## 一、我只说了七个字，它就把整条角色流水线建好了

我就跟它聊了一下《杀戮尖塔》，问它能不能帮我做一个类似的游戏。

![游戏截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DVnvGvVLicYEby7uegU292urPnb3HrSB742Y3orqMHotDdughQlXZnURLF1HJHWicXibcGPQ7HARqLoY5kgakZhcttmHMP1AfBQFA/640?wx_fmt=png&from=appmsg)

结果它直接用已有的资源，通过代码生成了一个非常像的 demo。

### 我没要求绿幕，它直接生成了绿幕底的图

之后我让 Codex 用内置的 GPT-Image 2.0 生成里面的图片素材。

我也没说要什么风格的，也没说要哪些妖怪的，也没说要哪些素材。

图生出来我看了一眼，愣了一下。

角色是在一整张纯绿色背景上站着的。标准的影视绿幕底色，均匀、干净，边缘清清楚楚。

没有雾、没有远山、没有任何额外的画面元素。

![绿幕角色图](https://mmbiz.qpic.cn/mmbiz_png/ofWbZTuv4DUSNM70b1cfOb1pzxxEia9Mdf7SreXvgWXHw1k4f9JEBRk3Dh6gt0rYkFSrvD8yjBQKN34vowZia4JLWa6nhaaoTomDQeDty2rEk/640?wx_fmt=png&from=appmsg)

恐怖的是它上来就知道要生成方便后续处理的绿幕图。

我压根没告诉它「游戏里用到的立绘需要是透明背景的 PNG」，也没告诉它「请你生成一张绿幕底色的图方便我后期抠掉」。它自己在规划这条管线。

从想要生成什么样的角色，到角色要怎么放进战斗舞台，再到放进去之前需要经过哪道处理——它在调用 GPT-Image 的那一刻已经全想好了，然后反推回去写了提示词。

### 抠图工具也是它自己找的

我没给它装任何图像处理工具，没给它 rembg，没给它 Python 环境里的任何特殊依赖。

它自己查、自己装、自己调，抠完规规矩矩丢到 tmp/imagegen/ 下面。

生图用绿幕、工具自己找、抠完按文件名归类，三个动作连起来，其实已经是一条完整的角色资产流水线。

我从头到尾只说了「调用GPT-Image 2.0 生成素材」这几个字。

![工作流程截图](https://mmbiz.qpic.cn/mmbiz_png/ofWbZTuv4DWpBjpqODlUyMvlavyznnlISdg7ZQ4cvsIEso7VXviaLnoQjicNbDgLtqndJm7VUoDb7EMQrhVYmibEDBplCJFeztnnTgGk3vZWYo/640?wx_fmt=png&from=appmsg)

以前的体感是「模型会写代码，工具和上下文得我配」。

现在更像是你报个目标，它自己把路径补齐。

我只负责审美，它负责把供应链跑通。

## 二、为了下几个图标，它差点黑掉一个素材站

### 买会员不够，它开始分析网站结构

立绘这种核心视觉用图像模型生成没问题。

但游戏里还有一大堆小东西——卡牌边框、费用宝石、牌堆底图、血瓶、八卦按钮、符箓面板——这些要是全用图像模型一张张生，又贵又慢，质感还不统一。

我跟它说，要不你自己去网上找现成素材吧。

它就认认真真开始找。看中一个素材站，我顺手买了会员，账号扔给它。

![素材站截图](https://mmbiz.qpic.cn/mmbiz_png/ofWbZTuv4DVVEBr8s4jiaMCXaSRcpVm5Fjia0kH44OLpGAc8LUdPoTvHoaRwwSSiaia7v8vAJiahxIDPEIZibZANicVdGgviaRAvjgB6sRk1NFHc8Zw/640?wx_fmt=png&from=appmsg)

接下来的十几分钟属于灵异事件。

它登进去，找到想要的素材，准备点击下载。但下载按钮前面有人机验证，一次、两次、三次，过不去。

换一般的模型，这时候就会回来跟你说「我没法处理验证码，你能帮我下载一下吗」。

Codex 开始分析网站结构，试图绕过前端的点击限制，直接构造请求去拿静态资源。

然后 Codex 自己的安全护栏介入了。

GPT 现在这代模型，一旦涉及可能的网络安全越界行为，系统会直接把这段任务掐掉，弹出提示要你做企业认证，证明你是合法使用者。

![安全提示截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DWjRfOZkedcjOLyWH16mPrgLEzgWJicM2ic02JVSiapej7eXibXK9DjMnuiac0ZNHgpsQnWaPEgRGCDicc1HyW7jIkI68zU0r59Xze6o/640?wx_fmt=png&from=appmsg)

我盯着屏幕愣了几秒。

一个要你帮它办会员卡、结果自己下手写爬虫的 AI，说实话挺有病的。

它也谈不上「坏」，只是把「拿到这批素材」当成了一个必须完成的闭环任务。

遇到阻力就自动升级手段，一路升到了安全红线那边去。

最后的解决办法很朴实：它把自己觉得合适的素材链接发给我，我点下载、拖给它。那一刻我有种自己在给 AI 当实习生的错觉。

![工作截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DXOnYbSfS4GE59K142aKl1e6dGkibHvnQg4KCvfnZoibnvicAqFQwia4duYDZkOC8oJzKzrCpS0k9HLicuxtic1Y7Zy5xgicdEcgz30C4/640?wx_fmt=png&from=appmsg)

## 三、它把几百张素材拼成一张大图，这是整件事最精彩的动作

### 一个文件夹一百张图，模型怎么挑？

抠图和爬虫那两件，更多还是能力展示。

下面这件，我觉得是真正意义上的「解题思路」，是那种让你合上电脑默默拍一下桌子的动作。

我找到一个巨大的游戏素材压缩包发给它。

里面大概几千张图，按「UI 界面」「法宝奇遇图标」「角色」「徽章」这种方式粗略分过类。

问题是：

•

一个分类文件夹动辄几十到上百张 PNG

•

文件名多是 ui\_001.png、icon\_047.png 这种没信息量的命名

•

多模态模型的上下文根本扛不住一张张喂

![文件夹截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DWoGicpd81dmicXIuNicaG2F2myLqEuNUicAZO0rfH3OS2fZlOiaNyyiax2L7iaTlLfOdDdQ2Z5qj7zHrobeQCoMWJ8nO7l8lVFJCeHOo/640?wx_fmt=png&from=appmsg)

老路子基本两条：

•

逐张读：一张一张送进模型，几十张上百张 context 就炸了

•

按名猜：文件名没标内容，猜了也没用

### Codex 走了第三条路

它写了一个小脚本，把文件夹里所有小图自动排版、拼成一张巨大的网格图。

每张小图下面标上原始文件名，像一本目录图册。

然后它只读这一张大图。

多模态模型扫一眼，就能同时看到一百张素材的样子。

看中哪张，直接读出下面的文件名，去原文件夹里按名字引用就行。

![拼图截图](https://mmbiz.qpic.cn/mmbiz_png/ofWbZTuv4DXgH8lIXM4S0sXrib9pRhqvDM3UFr9Cm8J10YqYV53bgsnjibosfkuXM5QJdZGm5vmePFHcKwibqWicsbKaMsWCyWmSjUgAmBOawAY/640?wx_fmt=png&from=appmsg)

一次视觉消费，顶一百次检索。

### 它自己意识到了自己的瓶颈

那张巨大的 contact sheet 生成出来的时候，我盯着看了好久。

这个动作本身不复杂。

老摄影师做的印样，老电影素材库做的 thumbnail wall，都是一样的思路。

关键是模型自己意识到「我的视觉带宽有限，我得把问题压成一张图」——这一步是它独立完成的。

能意识到自己工具的限制，然后主动为自己造一个更好用的输入，这一下已经非常接近一个会写工具的工程师了。

我作为使用者什么都没参与，只是看到桌子上多了一张拼图。

最后游戏里很多 UI 素材，费用宝石、牌堆、血瓶、按钮、符箓边框，都是从这个流程里挑出来的。

后面我再看 assets/vendor/aigei/ 下面那一堆干净的切图，会觉得那张 contact sheet 才是整个项目最值钱的一步。

## 四、Seedance 2.0 给七个 Boss 拍了处决动画

视觉打磨到一定程度以后，我想给战斗结尾加一点仪式感。

最后方案是：每打死一个怪物，进入一段过场，播放一个几秒的处决动画。

这活现在用 Seedance 2.0 做最合适。

![Seedance 截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DU64PfHcEuo6zqk7umMy5S74ibTtffCBLibaUgygM9F4ywawpdLuTz6TavHa1l5DRg07psgPdyf5bjxUNTIpTbT79iajNmgcavRNQ/640?wx_fmt=png&from=appmsg)

### 流程

1.

GPT-Image 给七个怪物分别生成一张结算定帧画面

2.

把这些 poster 分别丢给 Seedance 2.0，生成对应的短视频

3.

视频放进 assets/generated/cinematics/，战斗胜利后自动播放

![工作流程截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DV2Byr0ThkxoyArEzjrJv6kw3ImVWovh36CKNEOI6yvic5gjYz5SE7JkwlIWYcK8fSicYDgKWSZtGJt4Jx0FtLWVq6GDO3gicslhs/640?wx_fmt=png&from=appmsg)

## 五、一版能玩之后，真正的工作才开始

### 第一版其实已经够"能玩"

三个小时跑完原型的时候，这个游戏该有的东西其实都有了。

标题页、地图、战斗、奖励、事件、商店、休整、Boss、结算——完整循环在那里，玩法爽点也在那里。

按以前的标准，这一版已经可以发出来骗人玩了。

![游戏截图](https://mmbiz.qpic.cn/mmbiz_png/ofWbZTuv4DUib4Us6TXsfEwb6ElCp1S6zTlo5JfnCMAsa30Dib8RrpAMMPCDMYTEYOXRHGs1YDicia1OPKOvCiaLqpLcyAka908DLo17PvZ1ILjI/640?wx_fmt=png&from=appmsg)

但这个版本玩起来还是个流程图，而不是游戏。每一步都通，但每一步都干巴巴。

剩下的几个小时，全都花在那些单独拎出来说不上来、但合起来决定"这东西像不像真游戏"的细节上。

### 音乐来自 Suno v5.5

背景音乐全是 Suno v5.5 生成的，没用任何现成素材。

我给它一段方向描述——"志怪夜路、木鱼、铃、低频 drone、五声音阶、克制不煽情"

跑出来几版，挑一版进游戏。标题页的调子更沉一点，战斗背景轻一点不抢人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DV7yCqKcIgGz920qDsgdnVcf3eTGNw4o5iapvrJUa2SX5Kc06tlbeJcibaJMwFIAZCHibVkoC21wLcNVkGQX3ur9a5DPh3ib4SZyAc/640?wx_fmt=png&from=appmsg)

这里我还做了一些细节处理：在等待页面时，音乐音量较大；

等到点击"开始游戏"，音量就会变小，转为背景音。

### 受击动画和打击音

早期的战斗，卡牌打出去怪物就是掉数字。没有反馈，没有分量。

Codex 做了一整套打磨：

•

角色受击左右摇晃、镜头轻微震动、屏幕短暂泛红

•

每种攻击类型配不同的打击音——剑、符、雷、拳，质感不一样

•

格挡和符印结算也有自己的声音，不会糊成一团

•

敌人死的那一帧有一个短暂的定格，再进入处决视频

这些东西单独看都很小。合在一起，整个战斗的"手感"就从网页表单变成了卡牌游戏。

![战斗截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DX7zwiaYPfw0iaVG0bVQu0ddCthU5R9kuBHsk4y53fJBgx9oAYzQEtlacFDkvpo5rsP5iclykJbibkH7fpe7ablhIIWaLxiaICLqQVk/640?wx_fmt=png&from=appmsg)

### Seedance 2.0 还拍了待机动画

这一步是整个打磨阶段我最喜欢的一个用法。

除了 Boss 结算的处决动画，我还让它做了标题页的背景——环境里火在烧、灯笼在飘、远处有云雾流动。

Seedance 2.0 默认出的是一段有头有尾的视频，循环播会在接缝处跳一下。

首帧和尾帧传同一张图。

视频从这张图开始、又回到这张图结束，接起来就是无缝的无限循环。

![Seedance 截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DWyicOZea2bBjyDKFJofrfZkvicaHv4ftWMmjTHNuNVicyQHqAWj1aribiavs47hE4OxTrBePLS07U86A47HF3IOibzqqgX26JDKl6AE/640?wx_fmt=png&from=appmsg)

标题页那段背景动画就是这么来的。火一直烧、灯笼一直飘、云雾永远在流——你盯着看三分钟也看不出接缝。

这种用法其实在视频生成出来前就存在，老动画里循环场景都是这个做法。

![标题页截图](https://mmbiz.qpic.cn/sz_mmbiz_png/ofWbZTuv4DWiaXMTagHO5nrfIHHSWX4aZrtKs95TyuibYk73Da67qzKjMLMvCaO3sU8CibZ9icLyCAjZUEf6clSVZg4BAM6oiah6LV59Y4epbrJQ/640?wx_fmt=png&from=appmsg)

## 最后：这个下午把我震到了好几次

这个项目全部在一个 Codex 会话里完成，没开过第二个窗口。

玩法原型、状态机、React + Phaser 架构、素材管线、抠图、爬素材、拼 contact sheet、调 GPT-Image、跑 Seedance 2.0、接 Suno v5.5、Electron 打包、GitHub Actions 构建 Release、README、图标、宣传物料——全在里面。

我自己做的事很少：

•

选方向：中国志怪题材、爽点放在符印和香火

•

给审美意见：这里糙、那里像网页表单、亮度打架

•

做看门人：什么素材合规、什么爬虫不能碰、什么权限不给

剩下全是 Codex 在跑。而且每一步都有让我合上电脑愣一下的瞬间。

它上来生成的就是绿幕图，因为它知道角色要进游戏之前得先抠掉背景。

它自己下手写爬虫去绕验证码，被自己的安全策略拦住。

它把几千张素材拼成一张巨大的索引图，让自己用一次视觉消费顶一百次检索。

这些事单拎出来都不是什么天大的发明，但每一件都指向同一个变化：

以前你得把工具给它摆好，它负责写代码；

现在你只管说目标，工具和模型已经内置了、还会自己造。

这种感觉已经脱离了「写代码助手」的范畴。

更像有一个相当接近 AGI 雏形的软件在干活了。

## 要不要把这套流程打包成 Skill？

这个项目跑下来，我心里其实已经有了一套相对稳定的流程：

我在想，要不要把这套流程封成一个 Codex 里专门做独立游戏 demo 的 Skill。

你只要丢一个玩法想法进去，它就能在几个小时里给你跑出一个能玩、能打包、能分发的版本。

如果大家有兴趣，我就抽时间把这套 Skill 做出来开源。反正我自己也要继续用。

## 游戏试玩

代码都开源，安装包也都打好：

https://github.com/op7418/Night-Patrol/releases

✦

继续滑动看下一个

歸藏的AI工具箱

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过