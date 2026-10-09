# WorkBuddy这次，把「打开文件」变成了AI的工作入口

**作者**: 花叔

**来源**: https://mp.weixin.qq.com/s/XAIAoq1mQv9xL0f1SwzcwQ

---

## 摘要

腾讯WorkBuddy推出独立文件浏览器，支持Word、Excel、PPT、md和HTML在同一窗口打开，人和AI均可参与编辑。用户右键即可打开文件，无需设为默认程序，文件在左、AI对话在右，可围绕当前文件直接交流。md和HTML可轻松转换修改，例如将skill说明文档转为面向人的HTML说明书。该工具旨在让人、AI、文档形成三角协作关系，打开文件即成为AI的工作入口。

---

## 正文

花叔 花叔

在小说阅读器读本章

去阅读

今年五月，X上有一阵在争论：md和HTML，哪个才是AI时代更好的文档格式？我当时看不下去，做了个能在两种格式之间互转的skill开源了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSWib7vBl8libnAs56wInU1W4LfOaAz1HaEvBoHreFZIOUcfkNOdaPF6GfYlpY0zzK20YojhQubn4fXwYZopiceiaAzewibqsbXiavibUho/640?from=appmsg)

现在我还是觉得， **md和HTML都是AI时代更原生的两种文档语言** 。md可以放规则、计划和初稿，让AI接着读、接着改；HTML则能把内容做成更易读的图表、卡片，甚至是能点、能筛选的小工具。

不过，AI把东西做出来以后，还有挺多事要干。

有时是标题不喜欢，想换几个字；有时是看完图表，才发现自己其实想看另一个维度。想改哪里、怎么改，往往得看到成果以后才说得清楚。

**人、AI、文档，已经成了一个三角关系。** AI能大幅度生成和修改，人也得能方便地阅读它的成果、直接动手改，或者对着具体内容提出下一轮意见。

我想要的其实很具体：打开手头这份文件，就能自己改，也能随时让AI接着改。

这两天，我用 **腾讯WorkBuddy新上的独立文件浏览器** 跑了几份自己正在用的文件。Word、Excel、PPT，以及md、HTML，都能在一个窗口里打开，人和AI也都能参与编辑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSWibC3fWZuiabqqHXvw2LkEZa8lJFEG40kXd5GhiaI4s9XPJG2EAm1BpwyzkAkVWWOXwo5CBCbl5TkSh1HGKerrYoOAuIWEuwF5lAw/640?from=appmsg)

用法很简单：在本地文件上 **右键→打开方式→WorkBuddy** ，文件就在独立窗口里打开了，不需要先把WorkBuddy设为默认打开方式，也不必先进主程序，再把文件拖进对话框。

![](https://mmbiz.qpic.cn/mmbiz_png/aNEfzwzDSWicqF4Z5pTx8zmTKbicLDnic1Kib4F5zbRERHaFNxm4sjdkpbe6nqMmWj6JvMsfptTsIZAPyE90gszx0PQOdxCd9VU5nsvwWCD91G0/640?from=appmsg)

当然，如果你希望以后双击这类文件就用WorkBuddy打开，可以主动选择将它设为该类型文件的默认打开方式；是否设置，由你自己决定。

打开后可以先安静地看，需要AI时再点右上角的「AI对话」。文件在左，AI在右，直接围绕当前文件聊；切到哪个标签，就接着聊哪个文件。

## 一、md和HTML，都能轻松转换和修改

我先拿了一份我现在电脑里最最多的md文档做了个测试。

在WorkBuddy里，md打开就是排好版的，也能直接编辑。我另开一份选题笔记试了下，敲两个井号加空格，那行就变成标题，修改会自动保存：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aNEfzwzDSWibkNZhSlXwgEXHlNEgZA66np9bzXiaz4T68PWPajkTicf2UtHCz7F4SictUtGXpbIPjx7DoWlfCiaQRklzfqviaQZkiaaBb2doZFFkXo/640?wx_fmt=gif)

以及，很多适合，为了不同的需要，你很可能需要对文件格式做转化，以我的Huashu-Design的skill.md文档为例，我打开以后，在右边让AI把它做成HTML说明书。提示词如下👇

> 这是我开源的huashu-design skill的说明文件，原本是写给AI看的。  
>   
> 帮我把它做成一页给人看的HTML说明书：开头一屏讲清它是干什么的；把工作流程画成一条看得懂的流程；触发词做成标签；核心原则做成卡片，点开能看细节。  
>   
> 内容以这份文件为准，不要编造文件里没有的功能。做成单文件，存到同目录，命名「huashu-design说明书.html」。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWibvqzL99H8G1vwnkxoASIibV4pcVo5K1Vibv3xmnr8aWDL9nCrVvcTcG7glrWHFxLVpibrZkMoTP5SdWaayRJo1otiaL64zLcotYWs/640?from=appmsg)

同一个文件夹里多了一个HTML，打开是这样：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSW8VY5B2fTfd8IPuKj8P8sFf48ib8w6pZOboJ2ibgrhj7v0YicfiaR89L2EouBcEwAbBVFbic9HszmvicYoEsfULMWDVQOZl8C8daDEgU/640?from=appmsg)

原来的工作流程、触发词和原则，都放到了对应的位置，原则卡片点开能看细节。我把页面文字跟原文对了一遍，没有发现它给skill编新功能。

但它起的那个标题，我不太喜欢。

这次就很省事了。 **HTML也可以像Word一样，直接点进去改字。** 点右上角的编辑按钮，再双击标题，我就能把它换掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWiczPHtwuZrsW6ficzqp7ichpOUk0XjYPskxBSLrrEeibLVEjBwK2FUl4fLibQgCT0PHqL5yxf1GBTR9xZWkefbDwEKxQA9BZs66WlU/640?from=appmsg)

然后我让AI接着干：在最下面补一节「这页说明书是怎么来的」，写清来源文件、原文行数、生成日期，再加一个能展开SKILL.md开头那段原文的按钮。

我特意交代了一句： **标题我刚手动改过，别动。**

它加完了，新一节沿用前面的样式，按钮也能点开，手改的标题原样留着。然后我看到它把原文行数写成了583。

我数过，是582。差这一个数字，直接选中改掉就好了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW8QqFvZSibLjcSjar2Yso4nb8dszPfmT4rb6umFBBhdcwEhU70iam36iadXw1GTFR4sPlORTwMZK2l7BQ0e177ibFibgdpwAxDf2J1w/640?from=appmsg)

改完先点一下别的正文，再退出编辑，HTML就存好了。关掉重新打开，标题、AI加的那一节、改过的582都在，我也核过文件，除了这几处，正文没被动过。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aNEfzwzDSW9VdNlyeZhwRCPlju7STvt73gwMQIwJBB3xsmFgj5SKJ12QlZA5spcRqrGUH2yusS0BL6Oe7eMQtbmRogiaGsDIK8YN4exT6ABU/640?wx_fmt=gif)

**一整块的活交给AI，几个字的事自己动手。** WorkBuddy把这叫「人机双写」，在这份说明书里，我和AI来回改了几轮：

![](https://mmbiz.qpic.cn/mmbiz_gif/aNEfzwzDSW8OHibvjc4l9lPFFGGq8Fkx8gtYdIQpeSgicgTmv50Jt9q2EEr8aaS7PPwLuvXsIl12Z6S7TQiaKqXgVUf2QibUoWa6Gib6M4gB8nqg/640?wx_fmt=gif)

我觉得这个分工还挺顺畅的。能自己改好的地方，直接改给它看，复杂的部分就在右侧口头描述需求就行。

## 二、从HTML到Excel

我还拿了一张Excel表试，里面是电脑上md和HTML文件的统计。9月20日数的时候，一共有32,797个，近30天平均每天新建200个，最多的一天新建了649个。

选题方案、调研笔记、审校记录、skill说明……说起来有点好笑，AI写这些东西的速度早就超过我看它们的速度了。

![](https://mmbiz.qpic.cn/mmbiz_gif/aNEfzwzDSW9nPMN7e3T3OaACpicWKYpPJYMzg7icx4JpuB2S5KAbw4bA1S2PUQ78H0iaPvl53aqiaibAru1ONbCswJjEp81tv7wJxU7RwJnSOZ0E/640?wx_fmt=gif)

表格有明细，但想看看每天的变化、哪类工作产生文件最多，我更愿意看图。于是我在WorkBuddy里打开这张表，让AI按数据做一个网页版汇报：顶部放几个大数字，每日新增画成柱状图，按工作类型做能切换的条形图，所有数字以表格为准。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWibrOib9VDvVxqyfMLfxkErO5OxmkYMp1PvjdgiaBJGgGJacszCSqH1YvmFpdHugWUKqKCyJHWN0qCA1T6hB3OC8R4IGCN9UmKreg/640?from=appmsg)

汇报做好后就在同目录，我把图上的数字和表格核过，都对得上。没有记录的那天，它在图下面标了「无新增记录，未列入」。

看着这张图，我又想加个开关：只关注超过200个的日子，其余柱子变灰，旁边显示这样的日子有几天。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aNEfzwzDSWicCb2FHNDS3ibUHAn9eJnb0zozoo4IGJmzhyXUAialvvkoUnRQW15qKLoF2Pb7Cj41VLEOrXnd1WJtjiaJLoIJ6HeXTHwonOzEibw4/640?wx_fmt=gif)

其实这个需求，在一开始让它做汇报的时候我也没想好。看到整张图以后，才想知道超过日均值的日子有哪些，再往下改，要求就具体了。

对着已经有的东西提意见，比凭空描述清楚一份完整的需求容易很多。这个只给自己用的看板，可以在使用的时候慢慢改出来。

## 三、手头的Office文件，都能这样一起改

md和HTML再好用，出版社要的书稿还是Word，手头的统计表和课件也还是Excel、PPT。这些原本就在用的文件，我也想打开以后就能和AI一起改。

### Word：AI补一句，我改一处

我打开了《图解Agent Skills》的Word审校稿，190页、4.7万字、69张配图，封面排版、字体、配图都在（Office这部分用的是腾讯文档自研的编辑引擎）。

第1章里有女娲.skill的star数，我让AI在那段末尾补一句「截至2026年10月6日，这个数字是33,641。」只加这一句，别的不动。新增的文字在界面上是黄色高亮，很容易找到：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW8JiaeLyiaKf2WcMEOIEibDtjpLtU0aAdC55URyRSaRqiawOrFv7LoicEMibdpfTTUKxPrIXE0lVTGrqLssthlZC6u53D3XXtgc8LyXQ/640?from=appmsg)

接着我关掉文件再重新打开，把封面的「第3稿」手动改成「第4稿」。Office改完需要点保存，标题旁边的「未保存」会变成「已保存」：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWibn80OTP3cEkSN4FpKr8PiaePjS3osq0a8Hq1ZEypeRdoSI32H3QF5iaMSlrrEiaOT9mgkOnM0Y751ap37FLOpJ4ia7opVSAX8XGzc/640?from=appmsg)

最后核了一遍，两千多个段落只差这两处。 **我和AI的修改都存回了原文件，69张配图也都还在。**

### PPT：选中哪里，就让AI改哪里

PPT我换了一份12页的Skills培训课件，里面的文字和图片是独立的元素。这里有个挺实用的入口： **选中具体的文字或图片，浮动工具栏里就会出现「AI编辑」。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW9sm0icGKKGQNtwgNicTVe34cyGdnOzMfWhlAbEdJreLayia2fLabS2kZJiaR1nbXHpriauBvm5oPemQLYQiad500Dw3wiczWn8aIFSXg/640?from=appmsg)

我选中第2页的标题，点「AI编辑」，让它改成一句更适合第一次接触Skills的人看的提问，18字以内，其他内容不动。

要求先写在选中位置旁边的小输入框里，确认后，右侧对话自动带上了「幻灯片2」和这行原文，再点发送就开始改。不用再跟它描述是哪一页、哪个位置：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSW8DI42onRpicdt0sJlDoVRq0QdJeZkzwu30q3oPdopiaJVn5qrxG0wlCX5HFTa4n3IIlHqebHUjNTo3L8YkOArxuzhYLyw9h5ncA/640?from=appmsg)

图片也可以这么选。我点中右边那张插图，让它等比缩小20%，右边界保持不变，底边对齐左侧第三条说明的文字框：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSW8ArSiaFxbNUPb0u6cdyKmUTQ33Dj8bEsibXicIdfvqibWWC8h0pjWT0mpIVmX5IPlMStWMyuRwKWeQXxsqRpgK1qZxRJNZKwn9hY0/640?from=appmsg)

它调整了这张图的大小和位置，图片内容没有换。我再自己把页脚的「是不是很熟悉？」改成「哪件重复工作，你最想交给AI？」，点保存。

关掉重新打开，标题、图片布局和我改的页脚都在，改动存回了打开的这份pptx。12页课件，实际变化只在第2页的这三个对象上：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aNEfzwzDSWicABBQHk767UibYtyVjQhZjL1HFo9uLfAzYfAME1p6E2jQ9iazJicEicMpyZFBNmIbujSEmelz8icJtMH4kEVheHlngCbmNsWicaiaPk4/640?from=appmsg)

### PDF：打开后接着问

PDF的话，WorkBuddy上倒是还不能直接编辑，但是你完全可以打开浏览，然后随时打开右上角的AI窗口去对话，把WorkBuddy当作阅读助手的角色。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aNEfzwzDSWibwiaRzCAfFmefliamBvRBiawZqlXhHlwAOAztXqiaagPjD6C2jp2ChdicDyBt2NxncJS2SCTze8pf2ic1pCHxtvOjJ3NXlH1o6a8KjU/640?from=appmsg)

这些都是我平时要处理的文件，现在可以在一个窗口里打开，需要的时候再让AI参与处理：

![](https://mmbiz.qpic.cn/mmbiz_gif/aNEfzwzDSWic4JkmecTw5yPYqCseBHPjunbgY8EET73ibib4MfbL9UjKgTz54rSq2NuSkaZPuibXr90lLvj7vn3EMOJia2kpZrxcJ89fETPYsJGA/640?wx_fmt=gif)

## 四、文件打开以后，人和AI怎么一起干活

前几天Karpathy也聊到了一个变化：模型做的基础工作越来越多，人会把更多精力花在监督和理解输出上。他提到，可以让模型用清楚的文字、图表、交互式HTML等形式帮助人理解。

我觉得理解之后，人还得能很方便地参与修改。

这也是我喜欢这次WorkBuddy更新的原因。它把Office三件套和md、HTML放在一起，阅读、自己动手、让AI加工、保存回本地，这些动作都连起来了。 **就这套协作方式来说，WorkBuddy是我目前看到系统集成最成熟的一个实践。**

如果想试，可以直接拿一份自己正在处理的文件打开。Markdown自动保存；HTML手动改完，先点一下别的正文再退出编辑；Office手动点保存。查看和自己编辑本地文件不消耗积分，让AI总结、改写、生成内容会消耗积分。

微信里收到的md和HTML，也可以选择用其他应用打开，通过WorkBuddy小程序预览。

你也不用一开始就想清楚这份文件最终要变成什么样。打开看看，先改一处，想到了再让AI接着做。

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过