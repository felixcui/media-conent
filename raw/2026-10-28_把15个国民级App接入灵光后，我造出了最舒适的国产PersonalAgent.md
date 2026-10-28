# 把15个国民级App接入灵光后，我造出了最舒适的国产Personal Agent

**作者**: AI沃茨

**来源**: https://mp.weixin.qq.com/s/vavCtYcAEm_SRokI0BHmnA

---

## 摘要

作者通过蚂蚁灵光2.0将米家、滴滴、美团、淘宝、微信读书等15个国民级App接入Personal Agent，验证了国产Agent的核心优势在于贴合本土高频生活场景，并以迪士尼天气提醒为例展示了其主动拆解任务、后台持续跟踪的长期运行能力。

---

## 正文

AI沃茨 AI沃茨

在小说阅读器读本章

去阅读

## 自从拿到蚂蚁灵光2.0这个Personal Agent的内测，它已经成为我的私人管家了。到现在，我已经通过Skill、MCP、GitHub项目或者内置的方式，把15个国民级App都接进去了。

基本上我打开「帮我管」那一栏里，定时任务里会定时刷新值得关注的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8Fy8zHlaC93sTfy7DdP09ibaPeRKw8RbCMwDicnzicCPwOMMEnwkHTXYNXsecEqqc9LQB63ENJwOK9Kyd6Yx76sa0xE1tBMib58qF8Y/640?wx_fmt=png&from=appmsg)

灵光不是我用的第一个Personal Agent，前前后后一共测了12个，测到后面，我越来越觉得，手机上的Personal Agent跟电脑上，根本是两个物种。

电脑上的Agent，我希望它像我们之前测的那样，能用computer use去翻网页点按钮，把信息给我捞回来。手机上的，我的要求反而很朴素，配置方便就行。你给我发link也好，发个马也好，只要接得上，接上之后一直有效，就够了。

那国内做出来的Personal Agent，优势到底在哪？

我觉得答案其实挺直白的，接GitHub、接email就是常规操作。海外那些健身管理，会议记录相关的App，我其实极少用到，哪怕强行用，也很少能找到跟我一起用的人。我每天真正打开的，是米家、滴滴、美团、淘宝、微信读书，一个Personal Agent再聪明，接不上这几个，对我来说就是用起来不够得劲。

就拿瑞幸，还有麦当劳来说，之前我还是在电脑里的Agent上把它接上去，可以直接点咖啡点吃的。所以点子王的我就在想，理论上是不是可以给灵光做一个超级能力扩展包，看看这15个App能不能全部接进去？

先说第一张卡片，这一整天就是从它开始的。

11点31分，我随手丢了一句，在我24号去迪士尼万圣节之前一直帮我留意上海的天气要穿什么？

灵光给的答复是，说24号上海白天小雨，22到25度，要防雨防潮。雨衣比伞划算，排队看巡游撑伞太麻烦，过安检还得翻包。别穿帆布鞋和小白鞋，积水里踩一天很难受。加勒比海盗，创极速光轮这种室内项目，可以当避雨站。

有意思的是卡片最底下那行灰字，

预报取自10/20上午，距24号还有4天仍可能调整，23号给最终穿衣清单，24号早上出门前再提醒一次。

这种主动性，算是Personal Agent蛮标志性的特长了。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FyRVlDba4ianLolw9SWDOWicVlBMKy2eicu8dUrIYvDxfHeIxnlZzGibyjR1xA1AJ0hKo79VPRU9nt722B9ic2bIAF1p5h2n2GwnfaI/640?wx_fmt=png&from=appmsg)

我就问了一次，它能给我拆成了三个时间点。

我可没让它定时啊，它自己定的。

也就是以前问完对话就结束了，现在灵光2.0，哪怕我关掉App，它也会在后台盯着天气变化。

那像天气、股票、航班这种公开信息，不用连账号就能查，我就不展开说了，我好奇的是另一半，所以我又问了它一句，你可以连上我哪些账号或者cli，帮我看信息的？

它列了一大串。米家、石头扫地机、小米汽车，钉钉，滴滴，QQ、163、126、新浪、搜狐、Gmail六家邮箱，还有百度网盘等等等等。这数量看着不烧心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fwq0nownqD5N9nrzaXSHDnqgZd0gRaI5ib38XxV28nicqib7OsHRfT5JE23vMr60uTDEa7ibaJhW5OL2zWU3GUxPNyHZ7nfQyKqJ0A/640?wx_fmt=png&from=appmsg)

OK，我又追问了一句，你后面接的是一台一直开着的电脑吗？我给你接的这些服务都是长期保存的吗？顺便列个表给我，毕竟这也算是Personal Agent经典特征了，长期运行的云端电脑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FyvVLChGm7ianwkyPsJuCP8lUll3Shp6I0w5icWTx2mibZmfiaQHmQpabh5pJgsa1KfpFdUjFCibv9y0ux4DZibBYMziaUWmLEGXmzLss/640?wx_fmt=png&from=appmsg)

那会儿表里已经躺了7个，美团跑腿，滴滴打车，高德地图，飞猪旅行和米家智能家居，后面还会有更多的，说是15个就一个都不少。

挨个拆之前，我先把这一天折腾下来的经验，压成了一段总提示语。

你要是也拿到了灵光，整段发给它就行，它会在一个对话里一步一步带你接完。

```swift
## Personal Agent配置提示语
我想把常用的国民级App都接进你这里，做成我自己的Personal Agent。在这个对话里带我一个一个接，每次只处理一个，接完一个再问我要不要继续下一个。
每个服务都按这个顺序来：1. 先检查它现在有没有连上，连上了就跳过2. 没连上的，告诉我最省事的接法，能发授权链接或码的优先，其次是官方MCP、官方Skill或命令行工具3. 需要我去申请Key或授权码的，告诉我去哪个页面申请、要拿回哪几样东西4. 接上后用一次真实查询验证，再把接法存成可复用的技能5. 凡是会花钱的动作，比如下单、叫车、付款，先把费用和细节列给我，我说确认才执行6. 接不上就查清原因告诉我，然后跳到下一个
清单：米家（扫码授权）百度网盘（扫码授权）钉钉（授权链接）QQ邮箱（IMAP/SMTP授权码）滴滴打车（滴滴MCP申请Key）瑞幸咖啡 open. lkcoffee. com麦当劳 open .mcd .cn/mcp/doc高德地图 lbs .amap .com飞猪 flyai .open .fliggy .com/docs/quickstart美团跑腿 github .com/meituan/MT-Paotui-For-Client支付宝（内置授权）微信读书 weread .qq .com/r/weread-skills网易云音乐 github .com/NetEase/skills美图 clawhub .ai/meituskills/designkit-skills
全部跑完，给我一张表，列出服务、接入方式、当前状态、能帮我做什么。
```

一次只处理一个，是因为有的要扫马，有的要申请Key，有的直接丢链接。

下面我按配置难度，从扫码就行到需要自己申请Key，一个个说，gogogo！　

ㅤ

### 一、米家

接法简单到离谱，灵光会直接给我甩个马，用米家App扫一下就完事了。

马上就找到我米家里的18台设备，在线9台，还顺便提醒我，客厅那个温湿度计电量本来就快没了，得先换颗新电池。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwkLsyjHmrsMGiaZwnsExdOibnavKdTqiaDVaL8B6co2PvAFbibtKVqHbnWcA9yjZpslbF3Mcicb35ss1DT3SC4ibOLruYK16qIJibPs4/640?wx_fmt=png&from=appmsg)

然后我上了点难度，早上起床开灯和插座（接mac mini）要自动打开，每天发我温湿度，再给我一份离线设备的重连教程。

起床开灯这个，灵光是按步骤教我我在米家App里建一个起床模式的自动化。隔壁苹果的快捷指令都可以用apple intelligence写了，许个愿后续米家能开放让灵光可以直接录入。

目前来说，用ifelse控制单个电器还是非常简单的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fz7KIFrv8CNqY11LGxN4t96Pia9icxKlkiaeSv64DribUVa00FeuG9US2GyL9xDkwicZeVqgHG4KbUkneQTE9HQDP03cJWwcmXJJgTM/640?wx_fmt=png&from=appmsg)

　ㅤ

### 二、百度网盘

也是扫马，依旧是没啥使用难度。

我的痛点就是我懒得一个个看但是又不想充会员。。。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FzibYLWF8o1UkLTrdgibnSTHoTVO1c3r1H9EibqTJXPNC7ghoMWa7Io7RJrodY3AKkVnqqGx9jiaMdkdb4ZFuDcoohFINMyBtEdd7g/640?wx_fmt=png&from=appmsg)

扫完它把我的网盘翻了一圈，直接就是，你的网盘大头基本都是早年存的课程视频，腾空间完全不用充会员。

回忆感满满啊，居然还有17年我用opencv的猫狗数据集，就离谱。。。

### 三、钉钉

我的需求是，每天帮我总结钉钉的群聊和邮件。

钉钉点个授权就行，推送方式灵光也想好了，总结发在对话里，再给手机推一条通知。我现在最满意的就是可以关掉钉钉晚上的消息通知，真有急事灵光也会给我推送了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FxS0eEIP4icjXIkTGuwvMces6ia4Y7Xsg4JZYwgib1JtlR6gZ61bAaV4lWaDQ4iawKx2Qjib6ibOC71r8cR5chOibYhP6ahZcPyzJr98o/640?wx_fmt=png&from=appmsg)

　ㅤ

下一步我准备也去测测飞书和企业微信。企微本身就有API接口，按理说接起来问题应该不大，飞书如果也能顺利打通，那我日常办公这块基本就能一起交给它盯了。

### 四、QQ邮箱

通常用Personal Agent做每日总结都是公开的API，网页，然后邮件，RSS四件套。

我非常非常非常建议把能连的邮箱都加上，我之前花了一周时间把所有邮箱转发到一个固定邮箱地址，然后就想着以后只看这个就好了，但是还是拉了，不同平台兼容性还是不够，有时间差就算了还会被分类到回收站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwFkNR0oHIz6Mj8hdNVHpNFpHiabPIKv1quawmFzicTXs356IstDZUQuJib5LjaWnprpl9FK2c6XLKddTOcYTetpRibJC0A40No7KQ/640?wx_fmt=png&from=appmsg)

　ㅤ

### 五、美团跑腿

这个开始有点意思了，我只丢了一个GitHub链接，github. com/meituan/MT-Paotui-For-Client。

跑腿里存的地址，其实有大用。后面接一些地图类的App，如果你懒得再写一遍地址，甚至可以让它去美团里把对应的地址读出来记下。比方说我打车想直接打到家，就可以让它去美团里选。

这也是我今天要列这么多App的原因，有些App之间的信息是能互补的，能省掉我很多配置的麻烦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fxv1xfRXMXc4X03b8eLT5I2xMbD9InIB1M8DzDyX8gGxjWBTLc9C6GIPDrlF3ogRdjNY2X6VFWc79gsugyiblNVeLjSmHalVmwM/640?wx_fmt=png&from=appmsg)

我试了个特生活的需求。

杭州有家很好吃的东京烤肉，想让跑腿先帮我去取个号。它说可以搞，帮我把那家店，号单送到哪都弄好了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FyuexqCQOS9UShrR3aLaWOhSiciaTOfXrUdeZ7DOc6g2V67ahAia3BcZK7Z0riadB886YJpYj0xZjv5VUzk6iaWX62CVWu6qcYQ3amM/640?wx_fmt=png&from=appmsg)

　ㅤ

### 六&七、瑞幸咖啡 & 麦当劳

瑞幸也有个MCP，我把MCP配置整段粘进对话框就行。

接上之后，灵光马上就知道离我最近的瑞幸在300多米外，正在营业，最新的单品啥的也都能正常点。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8Fy45lJzOrFh8UjL2rJSMOZoMBAIuUvrNNq5JC8bbMFL3rdGcrte3dicjt24RicbJyic5mTMKicP2j8apibXwu5yS64dVE76gOq1ZK8o/640?wx_fmt=png&from=appmsg)

隔壁麦当劳也有自己的MCP开放平台，这次我连配置都没有复制了，只丢了个教程链接，让灵光它自己去读文档，接好之后帮我选最近最优惠的两人套餐，有没有新东西上线。大家知道麦当劳最近新出了全明星双人分享餐八件套吗？星期三我也是可以当做疯狂星期四来吃的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FyzeCHEb5HZhstK9cD4f8vBicFJjtwTSJ5o8jJOcwTL48YyrzyTN3IYZwib1atCsYsUKoqiaTGy0ZhN2kEE4ntia8YIGO6nohPHQNc/640?wx_fmt=png&from=appmsg)

　ㅤ

### 八、滴滴打车

还有一个盲点，如果你在高德打车的话，是没有办法选油车和空气清新的，但是在Agent上可以。

我的需求就是要油车➕空气清新，再把家、工作室、杭州机场记成触发词，以后一句话就能打车。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwuyvSA30lyC2ItMAv2ZqhU7rMjykbmeFdvFbxriaRx9uUKmuttlxH7KcDEPSlCug7koqU6Yc60RGzdO6ibbWzGB0Cmd5UlrVS0s/640?wx_fmt=png&from=appmsg)

这个时候就是我刚刚说的，能够把刚刚美团里的地址全部复制过来直接用的场景了

### 九、高德地图

还是丢一个文档，再加上在开放平台申请的Web Key，就好了。

灵光拿这把Key试了两条路。先直接调Web服务接口，查萧山机场坐标，通了。再连高德官方托管的MCP，路径规划，POI搜索，天气全拉下来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FwbGXKtJl99UbLNKmzPibb10TibmMba6vQEQH1fyzbJk6TibmeXylqkH2ZhaeyDibPkLzZS1GN0VCqibO8nic2hSzDz057s9msBJmhys/640?wx_fmt=png&from=appmsg)

### 十、飞猪

还是老样子，Personal Agent只要你知道某个服务有MCP有Skill，或者是有GitHub项目之后，其实配置起来都已经比电脑上的Agent要方便了。飞猪也是有开放平台的，我们照样也是有能接上的全接上去。

中间还有个小插曲，自动安装连GitHub一直超时，灵光自己换成了手动安装，把Key写进配置，再拿「杭州西湖 酒店」实测了一次，返回了真实的酒店套餐和预订链接。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FztYZDDZf1qdwyCtpWe3anJ2wE6feVees2Xho0zL0lCLBZ6yM7AaoH7jfaFt634JOKpkBtAANXE7T2dIqkcNIAhTjXicn79x6dU/640?wx_fmt=png&from=appmsg)

然后我问，我经常北京深圳杭州飞，有没有合适的随心飞？

它推荐了长龙航空的全年不限次畅飞卡，长龙的大本营就在杭州。后面还提醒了我，这类卡每趟一般要另付机建燃油费，等明年我再跟大家说说能省多少。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FxJ1Cib7aSty864K6S7cPWzKribtAakyyoOfYo7ia5MhOw5dUwdekDn0ibkA8c7DoDGCcdNOIic20eKWmtzBCeDWc3K6IwxfUtCIbUI/640?wx_fmt=png&from=appmsg)

　ㅤ

### 十一、美图

这次我先问了一句，生成超清图，给图片打码，去掉路人，灵光是需要借助美图CLI，还是原生就会。

OK，文生图和简单打码，灵光本身就能做，海报生成，人物消除和超清放大，可以通过美图来补充。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FxUicXjmyvlzVAKMt90phickWXs8nQERUziaCW7vGPfymyQZ94sicUUpZRksNVNbUsOciaDqMm3RibO22nxYbllXic5n1wYYqb3YladhU/640?wx_fmt=png&from=appmsg)

留意看上面右图灵光的回复，密钥已存进沙箱里单独保管，就是前面提到的蚂蚁APASS智能体可信基建在起作用。

给大家看看我做的猫猫海报。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FxfZC0X9cXx0KtsU2TibkJ7YV1YrEdwzNT9PpQsbKicDKxFJcvGwQC2R5ia056jXsreaiaaHj0ziasYKZFvm0iacRHiaBJPBbzELicIl8s/640?wx_fmt=png&from=appmsg)

　ㅤ

### 十二、支付宝

支付宝我也是带着疑问去的，年底了，我是真希望支付宝可以整个Agent帮我开发票，跟统计我今年花了啥。

不过支付宝之前公开的这个Skill，个人日常的转账付款、看账单，支付宝并没有开放通用接口，它更多是给收款用的，其中还有一个是专门支持个人场景的。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FxlDsjt9P3poZlOkCXbmYOXUTJibXacjmqhrialvIdKDlZpQScz0RzolibO5mLJbE4UGrVC59wl4Th3DJBUOgQCkiakvw7ibcuMIqyA/640?wx_fmt=png&from=appmsg)

在我测试的过程中，灵光2.0迭代速度还是很快的，后面直接原生打通了支付宝全生态。

我试了最实在的管钱场景，让它帮我梳理最近三个月的支付宝账单，看看钱都花哪了，重点放在那些自动续费刺客。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwOqVzPCgaFaxtibGFjw5QxoxzeZgnTiaxNjUSa4XYRAXhiavL1NBEAcYx5tpqq1eE75jJwAb2ot3ABfIscKQA1mQVRI7AXe6DNsg/640?wx_fmt=png&from=appmsg)

而且因为是设置成定时任务的，所以我可以直接给灵光2.0发一个预算，然后它来定时统计，这比一般的记账软件要好用很多。就是一旦它发现我有超预算的风险就会通知我。

### 十三、微信读书

微信读书这个我已经用很久了，之前还用它来统计我每周读过的书然后做成行动卡。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwuPYibclLeEJpVgEYWXVYEmlqworTWpLe8tv7gCFl7ZdPXibiaYibsNgibaWzadx9fuTpAGOia2Bd3SC2wRIKVgKl3t1ae45Py8d8YY/640?wx_fmt=png&from=appmsg)

原生的weread-skills是可以读取书架，阅读时长，每本书读到哪的，

不过我最近没空看书，所以接进来的第一条数据，卡片底部就写着本周阅读时长为0，属于是公开处刑了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FyxTwNicHIQMPUKjdc7cd1dZkdhP6UGHvsnDyBiaDGjW5FSl7AUSwS7cIPY3423FKuDcXxEAvHbuKW69TCVthNQo31b23sQh9qAQ/640?wx_fmt=png&from=appmsg)

　ㅤ

### 十四、网易云音乐

想不到吧，网易云也有。。。

github. com/NetEase/skills，顺手带了一个我最近一直想不通的问题，最近觉得听的歌越来越无聊，网易云为什么同时给我推三种语言的歌。不过这个配置要麻烦一点，要设置一个自建应用才能配置完成。

![](https://mmbiz.qpic.cn/mmbiz_png/VNz1x8bH8FwUvROPQ2IvtfibJicHmELPYicXBHGGbU8ibFAI1RTcLWWbVP5jSZkruGC8JibucZQVW08xnjVddCib9u6c7XuwhlOvPSl9zKTia9qnx0/640?wx_fmt=png&from=appmsg)

　ㅤ

### 十五、淘宝

最后一个，淘宝。

15个里只有它连账号都不用绑，直接上手干活，也是这一天里最有Personal感的一段。

我用语音甩了一大段很啰嗦的话，大意就是听说iPhone 18 Pro因为什么券降价了，帮我看看，但我只认苹果官方旗舰店或者百亿补贴这种靠谱的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8Fwiasm3BruwcXYkmVAQazibmMFjVAcEYC1iateTicJvtNR85BEnMFTaU78ud6z05YJeBHl4xYJaiaExg2RSpLywgiauK8FVMgIcMmGEQ/640?wx_fmt=png&from=appmsg)

最后一段灵光是这么写的，盯价我已经给你安排上了，整个双十一到11月13日，每12小时看一轮。

我顺嘴又问了一句iPhone Duo，确实是有店无货，预购一分钟清空，排期到2027年1月才能拿，还把我刷到的那几条新闻逐条核了一遍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VNz1x8bH8FyhC1LZ2MyTzLZs67ickAzelGJBN5sQLImuL2xe59LFkRib6AxyLCa8M317Sur56V9lz09ibIX0KPlNQsqYUNTs07YvdWCcuVSpFM/640?wx_fmt=png&from=appmsg)

15个，到这儿全部接完。

回头看这一天，最开始我其实也有个偏见。

Personal Agent是不是就是把原来的Agent换个壳，几个working Agent配一配，也能配出差不多的效果。

接完这15个，我改主意了，

手机上的形态，比我想的要丰富得多。

扫马的，MCP的，Skill的，CLI的，全都能往上装，像搭积木。更舒服的是装上之后，它会自己主动来找我。很多定时任务都是我说了一句，时间点它就自己kuku排上了。

以前我们每天刷十几家信息源，认知压力很大。

现在换成Agent按理来说应该减少才对。

但一点也没有。

我有个项目，让Agent连着跑了两三天，它是干完了，我是要花好长一段时间，让它给我复述做到哪了，计划文件到底更新没有。

Personal Agent正好反过来，我不用追着它问，到点了，它自己就恨不得把所有的都推到我面前。

所以我干了一个更大胆的设计。

数据焦虑，信息焦虑，我干脆一起交给它。我用Apple Watch的全天录音设备录了一整天，传进灵光，让它按时长给我划了10个闹钟，从凌晨2点看有没有AI新闻更新开始，一直排到一天里的每一个节点。

把其他一个放出来看看，真的是大道至简，日历，提醒事项，邮件通知通通不好使，唯有烦人的闹钟。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VNz1x8bH8Fw7HBRMI5cib3ibHuGQgcmXmHMSkziaQrXwZuCErtPM9TGAJcePSPhI2ZZBMGlPIBmsYvOgYgBz3mqicVy9WfZ8QI2LLHbb6TJdtCU/640?wx_fmt=jpeg&from=appmsg)

我要做的，就剩一件事。

相信它，相信我自己的设计。

定时收回来的数据再喂回给它，

Personal Agent会自己长成最合适我的样子。

@ 作者 / 卡尔

---

最后，感谢你看到这里👏

如果喜欢这篇文章，不妨顺手给我们

*点赞｜在看｜转发｜评论 📣*

如果想第一时间收到推送，不妨给个星标🌟

如果你有更有趣的玩法，欢迎聊聊🤝

更多的内容正在不断填坑中……

![](https://mmbiz.qpic.cn/mmbiz_jpg/YEhakvKZjXmCDLEEW1wClZOVGFURjmibJmciaYLNhp0N55Y6mPiaCj01eV8yzACqDvWDhicbPm07Wu7bboATuKgAbA/640?wx_fmt=jpeg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过