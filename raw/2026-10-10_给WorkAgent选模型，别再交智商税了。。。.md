# 给 Work Agent 选模型，别再交智商税了。。。

**作者**: 刘聪NLP

**来源**: https://mp.weixin.qq.com/s/HXdCAt62x6OIv99sU4_YyA

---

## 摘要

给Work Agent选模型不必无脑拉满配置，简单任务用Lite或Flash级模型即可，复杂任务再用Pro级模型。实测豆包2.1 Lite在数据清洗等日常办公任务中表现稳定、速度快、消耗仅为Pro的零头，而复杂多文件协同、3D渲染和游戏开发等硬仗仍需上Pro，但排版好看不代表答案全对，关键数据仍需人工核验。

---

## 正文

刘聪NLP 刘聪NLP

在小说阅读器读本章

去阅读

大家好，我是刘聪NLP。

之前用 Work Agent 的时候，很多人习惯把配置无脑拉满，上来就调最贵最大的模型，

不仅额度消耗大，等结果也更消耗时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRMHNQI3eCO0EMYKTDic6VicG7yJnibibLzdTBR0JVScOAfmLEJ6aZTq4QETEGRkMBu8j6AicwQTzFclNDvfAnmuLHXO77ialE5ThiafUQ/640?wx_fmt=png&from=appmsg)

在我们 AgentWork 社区群里，也有群友一直在问各种Agent如何选择又便宜又能干活的模型，

其实最简单的就是思路就是， **简单任务使用lite或者flash级别模型，复杂任务使用pro级别或者积分消耗大的模型**

这也是为什么前段时间Jev模型会这么火的原因，

现在很多模型通过增加reasoning来提升模型智能，

但确实很多真实任务，不需要让模型无限发挥，也许把任务变成选择题，模型只负责从预设选项里挑，可以又快又便宜。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRPhTyaXfXtpQlvDyiayEMzPzgDGmLtUX01TsOdIBHka7wDK4sHcLhdsicbicVicry2Qp9PIxQVAxsmib0aoUpT9feHIEluj9BSlLV54/640?wx_fmt=png&from=appmsg)

仔细想想，我们平时丢给 Agent 的活儿，很多基础判断和轻量整理，压根用不着动用旗舰大模型。

那任务边界如何定义呢？

正好最近豆包工作接入了豆包 2.1 Lite，直接有 **Lite、Turbo 和 Pro 三档，**

下面找了9个真实任务来进行测试，到底哪些活 Lite 就能搞定，什么时候才真需要上 Pro？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeROuHn6JXUibvDyicfUB7NQaKOhGWoovTkFyTtFQzAN7vDz14XyRgd2owdo2vNaiaCR4mCmAcoArufCILMfoOQHG8gCfYiafKSHK2Lk/640?wx_fmt=png&from=appmsg)

整体任务，从简单到复杂，有常规的会议纪要、两万多行的真实交易数据清洗，还有十几份文件的复杂采购案、3D 渲染和一句话做游戏。

每道题都是开独立会话，高推理全开。

先说一下整体感受：

- Lite 很适合做日常办公的常用档位，日常问答、文档撰写、表格处理和 PPT 制作，都可以先用 Lite
- 高频任务用 Lite，速度快、额度也省，消耗只有 Pro 的零头，适合每天都要反复处理的办公活，
- 复杂多文件协同和 3D、游戏这种硬仗，必须上 Pro，交付质感确实不在一个段位
- 最后，办公任务，排版好看不代表答案全对，关键数据还是得自己核一遍

**具体实测如下：**

先看一个高频的日常办公场景，Excel 数据清洗，

我找了一份 2011 年英国零售商的真实交易数据，25525 行，让去除重复记录、处理缺失和异常，最后生成一个带汇总公式的表格。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRM15RygPs6BQeBhnlFjKncdNK6TygiaMsMvg010TqByhicV1QhPMxOibQe5Sh2qQIKgUeWXXpWdy9X3HJlB4dFPEazxRHXCXibmJicI/640?wx_fmt=jpeg&from=appmsg)

结果在一些明确的计算和数据清洗上，Lite 的表现很稳，

Lite 汇总出来的数字很扎实， **819 张订单、313612 件商品、637790.33 英镑** ，重新输入数值，单元格也都能通过公式正常重算，整个 case 只花了 6 分 24 秒，消耗才 5.69。

Pro 也全做对了，甚至把商品销售和运费等费用单独拆开统计，口径分得更细，

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRMGEILUWEWfgSMiaqiaQNKamict15IKUM70DHVd4sNQBQrrK62EqCaeCQMcoHFX842Hu4ThmGsevQ0hI8WyrfTYYHnJDnKvJpB6bM/640?wx_fmt=jpeg&from=appmsg)

不过，足足跑了 29 分钟，消耗 422.86，是 Lite 的 70 多倍。

**面对这种明确的清洗、汇总计算，完全不用纠结，选 Lite 就行，又快又省。**

再来试试解题这方面，这里许需要视觉能力，

我找了 2024 年高考新课标理综第 24 题双绳吊重物，题里给了一张图，让算两根绳子的拉力和做的功。

![](https://mmbiz.qpic.cn/mmbiz_png/oUDMrTdAeRPq3kx1Vs1oW0SUYv4Kq1201JXOdIgfLyT7mKsSymrqV79A4q4Wa1GgSmHm2YBRicWicmovdBAZeoh0YTGHJMdllT3EmZBrkJozk/640?wx_fmt=png&from=appmsg)

结果，全解对了（ **P 绳 1200 牛、Q 绳 900 牛、两绳总功 -4200 焦** ），公式和数值完全一致。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oUDMrTdAeRMqbc9Fibzg4Tq6GcibVpA8A1P6f2T7re8I5ib8ibicbVSOXE1jQXjC8jTP8pa98k4pdMxYiahZkwGqLDsicHQIkAhb4JWNcB1JNxDy7Y/640?wx_fmt=jpeg&from=appmsg)

结果一致，比较的就是耗时和消耗，Lite 只要 3 分多钟，消耗 5.67；Pro 跑了 17 分钟，消耗干到了 294。算出来的结论一模一样，但 Pro 多烧了 50 多倍额度，

**这说明这种明确的推导题，Lite 就足够好了，真没必要上顶配。**

**那什么时候才必须动用 Pro？**

下面我们来看看一些进阶的 case，先看一个复杂的多文件协同任务。

我找了一个真实的政府宣传采购项目，直接丢了 17 份附件进去，里面有采购公告、7 个合同包各家供应商的报价明细、声明函，还有背景研报。

让它把这些零散材料对齐，出三份能直接拿去汇报的材料：一份 Word 执行方案、一份带公式的 Excel 预算表，外加一份 10-12 页的汇报 PPT。

**只有 Pro 交出了一套真正成熟可用的成果。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRO1NlZmSAetrePFoXAibO5NiadRltfs1waR5jA0fqAibcApaFYPljWh800Gwz1ibwSfe8394eOR1vxf1dKoSDQwFHqiaSr9CIw80Xbk/640?wx_fmt=jpeg&from=appmsg)

生成的 Excel 有 **6 张工作表** ，并且做到了 **跨表公式联动** 。我特地在副本里改了一家供应商的报价和代理费，汇总金额马上跟着变动。

不仅如此，Pro 还准确挑出了几份声明函里的文字瑕疵，我往回看了看原件，确实存在这样的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeROTCH7vCtmVsAuTNAtabX6dxMHp9GoT0vjOgsvqd0oWibZl9ZjdpPGE7zctUmEdibWMMK1ibI2HEVTVJmm0Imrv4AKnNa3ZqpsicNE/640?wx_fmt=png&from=appmsg)

而 Lite 虽然也交齐了三份文件，但把原文明确写的 33 分钟误读成了 3 分钟；

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRMkQd2GFXzdbbia90jbPibwpfvbjgURO4u5R1UJZyB7v5HhGqLYx3z2AQD9NY4vUHnx2ZUMBwdmvn3BsHhz1D2kjiaD05xJ5wv7O0/640?wx_fmt=jpeg&from=appmsg)

**面对这种十几份材料跨格式、跨逻辑的深度联动，Pro 的优势就非常明显了～**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRNUpTsIGvvum63zmdIibHpgwvmDw1uraRGicWmicpia2ZHyABbDic71ggQ0NdN59uWorMsiaJEibCicgOslnIIs0OoJuCJ46svPovZPvac/640?wx_fmt=png&from=appmsg)

再进阶一点的，把物理题做成可以玩的交互网页，

我拿了 2016 年国际物理奥林匹克（IPhO）旋转空间站落体的原题丢给它。同一个球扔下去，站外看走直线、站内因为科里奥利力看它拐弯。让它做个同屏对比网页，还能自己拖动高塔高度，看球能不能正好掉回脚下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRO7pYOibGmdra9bDG8GYS8c8eoiaqQM0H0Z6bKykTgzrPKy6mdcWhX4R2EYh82GiaGaZiag8icX9NwIx1bnzI8ib3ibP0yjEabiaweblicg/640?wx_fmt=jpeg&from=appmsg)

这题跑出来的结果特别有代表性，Pro 做的页面最漂亮，各种滑块轨迹都齐了，不过高塔回底算粗了；

Lite 也做了双视角和滑块，高塔预设同样能算到约 87.16%；但把塔高调到 1 米，页面自己算出偏移 0.095 米。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRMmvXR6MVJEccgClM7AqMfaCugxOKhpkUBVVEMNQN41HMgxzgvAQp3NicJ0efrXUYxCdjRrbGOo1aD6bDjSVw1ACbC96QK6ibN8s/640?wx_fmt=jpeg&from=appmsg)

然后，测2个高难度的视觉交互，

先做一个 3D 镜头实验室，参考了之前推特上很火的 Ryan Sael 案例。让不懂摄影的人转动对焦环，就能直观理解光圈、虚化和景深的概念。

这个任务里，Pro 出来的质感最好，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRONjDC4QGOnWia8e3O84BNbXpXTrQhd0hK77ia21W3d8DX6hR9icwrbicgYAJkVcBpiaBU9rNVDxeNyCbrPgwiabRskYnQulp55iam5SM/640?wx_fmt=png&from=appmsg)

拖动对焦环，对焦距离从 **110cm 变到 63.8cm** ，镜筒内部的镜片在物理位移，场景里的焦平面在扫过物体，右下角的取景画面也在同步虚化和清晰。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRPgfdq3aicSNUkV8j41JxzTEvja9flGRTcEWia8eQHBCOBLyCphTf86dfP6V7ekzgcyicUDm1Cf4LwkWB3dclNPSBRw7xTv1qDlx8/640?wx_fmt=png&from=appmsg)

切到爆炸视图，光圈叶片、齿轮组、前后镜片逐层炸开，机械质感非常到位，而且重新装配回来之后，刚才设置的参数也都没丢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oUDMrTdAeRNZLOpxN3NhDibafhK0uOqbKEbZj7icpmcVQTmeg8ESXsvkfNwJMZDhVssfBSbjTstwGZ4Ipsiajx5wZVx9s2JibjgFBjDJvMic4J4k/640?wx_fmt=png&from=appmsg)

对比来看，Lite 虽然也做了控件，但取景是简化的 2D 贴图，

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRPOFa3FHicBNo1TcSuS8nGquDI4sibPrIxytwgyicFBrZs2NScMlhQ1GzEQeL9ic7zpUM8ick8Y5icFhibyZCibMRehWljc7ljW63WNJRY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oUDMrTdAeRNWWibnmBmKOdFG4RMibYVO2IBCQKkxgaP1h0RM5kXT8JLK6haoicThWn9NyEzicqKVcVrAICyEYfHNvrgAhsN45Hb0JBzMm5gzvia0/640?wx_fmt=png&from=appmsg)

不过 Pro 这题足足跑了 **1 小时 25 分钟，消耗了 1208** 。

**这儿插一句，也是豆包工作的一个亮点，我点完生成之后直接把客户端关了，该干嘛干嘛去，云电脑在后台自己跑完了整个任务，重新打开客户端直接下载源码，完全不占本地资源。**

最后，来一个一句话手搓游戏，

参考了 Brotato（土豆兄弟）原作者的实机预告，让它做一款 2D 俯视生存游戏《修理站守夜》。

Pro 搓出来的版本，完成度相当高，

![](https://mmbiz.qpic.cn/mmbiz_jpg/oUDMrTdAeRNrN3mIic3sicYNtQJmHiapSkfDNFlZbwuMia72iadzEp9H0ibcecueoI0zy2hArVmyEQFEtwia85xees6qbSqia2WDibOtQ3bNJ75SFqBs/640?wx_fmt=jpeg&from=appmsg)

车间地面的灯光层次、小维修员的攻击动作、扳手和射钉枪的弹道，非常有独立游戏那味儿。

局间商店的逻辑也是真跑通了，第二波打完剩 **79 金币，买了 35 的合金扳手头，金币正确扣减剩 44** ，买过的卡直接置灰禁用；如果金币不够，卡片也按不了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oUDMrTdAeRNMNHsaiae10rH7BH3IwpwiastqYfc2kVC8B6P20C02JXaSoF8ia901e1Z7ertAxl7BITTVrTkwFxVuasD9dribvzkRK8bz7Rkf3n8/640?wx_fmt=jpeg&from=appmsg)

唯一可惜的点是我太菜了。。。全死在半路上没见到 Boss，胜利画面到底长啥样也没测出来。

但代码完成度和手感，Pro 确实比另外两档成熟，Lite整体可玩，但细节处理没有那么好

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oUDMrTdAeROAibKuwYvZegianFXLibB1oWkjf7icUBdyhiaA69bco5JaickIj5DT7eM45AQvGTawCqLtIQJ55CsORebKNYmAM9kSNicUvnMVkLmXQo/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oUDMrTdAeRP6CDVYNxu8Lk2nAzOGOj50iaEBKDs95V09F7MAfD5MMZRZG22ibCCMicHUFbDoVwiaT1hACLURMT92ECHqmg52LIUVtW5ibiciaszFnY/640?wx_fmt=jpeg&from=appmsg)

最后，

来算一算总账，这 9 道题跑完，

Lite 一共 157.63，单次生成用时中位数 6 分 24 秒；Pro 一共 6273.24，单次用时中位数 29 分 02 秒。

Pro 的消耗差不多是 **Lite 的 40 倍，时间也长了将近 5 倍** 。

日常的高频任务，会议纪要、常规数据清洗、解一道高考物理题，真没必要无脑拉满顶配，

Lite 又快又稳，不仅省下 40 倍的额度，还不用在屏幕前干等半小时；

但如果是跨十多份材料的综合汇报、复杂的前端 3D 联动、或者全栈小游戏开发，

也千万别心疼额度，直接砸 Pro。

**根据不同难度任务，切分好工作流，才是真正用好 Work Agent 的姿势～**

最最最最最后，

实在不行，就直接选择自动（Auto）模型，各家会帮你做好模型路由，根据你的任务难度来自动分配模型，但就是有点黑盒，你也不知道具体用的是什么。

![](https://mmbiz.qpic.cn/mmbiz_png/oUDMrTdAeRMlaRMtn4JcamqhbJib0dvq0cxGA2gUQUCVBFgJoOZ8et3GRoaRfGJVjshvs4VkHa9y2jkfkILupEO8BmDJl95bZOKmyp71JQuw/640?wx_fmt=png&from=appmsg)

都看到这里，来个点赞、在看、关注吧。

您的支持是我坚持的最大动力！

当然想第一时间收到推送，也可以给我个星标⭐~

也欢迎评论区多多讨论，说出你的想法。

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过