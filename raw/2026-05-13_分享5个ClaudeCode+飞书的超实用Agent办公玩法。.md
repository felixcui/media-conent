# 分享5个Claude Code + 飞书的超实用Agent办公玩法。

**作者**: 数字生命卡兹克

**来源**: https://mp.weixin.qq.com/s/6vqkEvFYNEtUu3rTQAllzw

---

## 摘要

本文分享了利用Claude Code结合飞书CLI进行高效办公的Agent玩法。随着飞书CLI开放近120项能力，Agent已能深度处理云端协作数据。文章重点展示了“为周期性会议建立跨场次知识库”的场景：通过Claude Code直接提取飞书历史会议记录，自动分析并生成包含议题转化、决策机制和建议的飞书文档。此举有效解决了会议记录缺乏长期沉淀与追踪的痛点，实现了数据的高效整理与知识管理。

---

## 正文

数字生命卡兹克 数字生命卡兹克

在小说阅读器读本章

去阅读

最近很多人也在问我，我用Agent，是怎么跟很多数据进行交互的。

我说我其实分的比较开，一部分是本地数据，一部分是在飞书上的云端数据，我们公司现在将近30号人，我对大家的要求是，需要跟同事协同的，都一律上云。

所以其实很多的交互，都是我让Claude Code直接跟飞书进行交互的，包括我们公司小伙伴也是，大家用图形化界面的时间占比，反而变得越来越少了。

之前飞书CLI第一次开源出来的时候，我写过一篇， [刚刚，飞书CLI开源，Claude Code也可以丝滑操控飞书了。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647681090&idx=1&sn=70ff1397460421defa4dcbdf85d77012&scene=21#wechat_redirect) 数据非常好。

但是现在其实已经过去一个月了，从之前的那一些能力，飞书一直在背后默默的加，加到昨天我统计了一下，将近120项。

有点过于离谱了，CLI开放的能力，都已经快追上API了，这个其实是有点离谱的。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWGCR2wtuY5S8fiaK6xSicqAmuA99cZ8eaedd7fdSFHfBzAWHRz10J2Knt6WhCwWhuAxHCX3Gsg24QeMicEjFv3N2zR3opgiadB6eg/640?wx_fmt=png&from=appmsg)

现在，你用比如Claude Code之类的操控飞书，如果要求没有那么高那么极客的话，几乎所有的事情，你都可以做了。

他们把能力大全现在也已经上到飞书开放平台了。

网址在此：

https://open.feishu.cn/changelog?abilityType=Tool

而GitHub上，飞书CLI甚至star数都已经快过万了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVS1yeWWkrJE3R9xibDqdWKbLtvNK5vS0RuFSIFibpEAtVNux3x1HR7yiaE4LAR81zIib2uXzp9sJD3fczhnm5jzx91V5FK19PsoRM/640?wx_fmt=png&from=appmsg)

所以，我也想给大家分享一下，我们自己用Agent跟飞书CLI交互的案例，我觉得还是蛮有意思的。

过程中是真的有好几个让我非常惊艳的瞬间。

话不多说，直接开始。

**1\. 给每个会议系列养一个跨场次的知识库**

第一个想分享的，是我们已经开始用、并且发现真的很有价值的场景，给每个会议系列养一个跨场次的知识库。

我们公司内部，每周都有培训会、周会、复盘会，反正这种重复发生的会一抓一大把。

但这种会都有个共同的毛病，开完之后，妙记都躺在飞书里，最多会后当时翻一翻，长期上是没人做追踪的。

时间一长，问题其实就出来了。

比如，我们有一次在选题会上讨论过的一个长线选题，事件本身是假期之后才会发生的，当时所有人都觉得这个不错，结果假一过回来上班，就没人再提过这事了。。。

又比如，每次招新伙伴进来，我其实是希望他能比较快地知道我们选题会的流程，了解我们对选题的要求和偏好，而这些长期堆下来的真实选题会数据，恰好就是新伙伴最好的入门材料。

但是没人整理、没人沉淀，过去这些就纯纯是浪费。

就拿我们的选题会的例子，隐私起见，我用的是3月份的数据。

当你有了飞书CLI之后，你就可以直接在claude code里，调用飞书的CLI来进行交互。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUttCicB7mdibU2snpLABUJDNG0iaQnCjuHib0RGGQTOWonIX9DSjk0eu8f56255lkban2sEx8nIdNQrKTibskuDkyrccV1NKiaoRq3k/640?wx_fmt=png&from=appmsg)

很快他就给我生成了一份飞书文档。

会议清单、选题转化分析、会议节奏、决策机制、现象、建议，全都有。

真的，Agent直接接入飞书拿数据，然后整理一个这样的内容，真的就是究极舒适区，以前真的导出下来手动用Agent整理，非常非常的麻烦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWdTVFrBB6Kz7yXjKkrxUeJYJO6tJIqY4ic7ad7jUb8cbicNJXzjbaicGy2NcN2NY7MzIQoibF4uQsG6ia4nTkUB2X2SHrALmgrRRP4/640?wx_fmt=png&from=appmsg)

反正就是究极全面详细，每一场选题会，讨论的选题，最后的决议以及对应的理由全都有。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUdKicBPE6BiaolFlFESOicAQHCUTIBxcd29at4VpvKK4RD4uMvfMjfISPea53IhVgRYlZWVaDIYhHIN1jq4nIgnuS1icrj0R2EDM4/640?wx_fmt=png&from=appmsg)

它这里面很多信息都是可以沉淀到知识库里面的经验素材。

那这样重复的会议的经验留存，可以复用到各个方面，并且直接存成一个固定的知识库，方便我们以后进行各种各样的知识存档。

公司内部的培训会也是一样，直接让他先把过去的培训会抓出来，沉淀成知识库。

后续隔一段时间让他自动去抓相关的会议信息，自动更新维护，不过就是打开Claude code一句话的事。

而这些知识库积累下来，我相信对每一个公司都是很珍贵的经验。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqW6bG3Z9m5e3skRznlel5T3qib60ZPIEK43dPuZemiavxPs8j3696q3ySj2pWh4EicicK6jx0xyCZ5v1tMyfsPtNHUuibuVlamv5pFs/640?wx_fmt=png&from=appmsg)

**2\. Agent+飞书做工作整体复盘**

第二个用法是我们同事非常喜欢的，就是给自己做一下全面的工作复盘。

就像我老是说，我们公司是完全长在飞书上面的，所有同事每天都在飞书里面工作。

留下的各种数据其实非常珍贵，但分散在私信、群聊、会议、妙记、日程、任务、邮件、文档、OKR这一堆地方，我们自己根本没办法对自己做横切面分析。

所以，这种事，就非常适合扔给Agent去干。

比如，我们有小伙伴，让它把过去7天、30天或者90天里这些数据一口气全拉一遍，有了这些数据，可以做的事情就很多了。

这个我们小伙伴甚至直接做成了一个skill，放到公司内部的Skill Hub上给所有小伙伴用。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVsBDndskSoYnO9zoeqAnRP8Q6mrqJPSFYiabicsltYNQDN0QO0yOND7gEk2peyib2sicDzfIEmxZ7OD8ZCqLJT5h4xa7bRjjlIhicM/640?wx_fmt=png&from=appmsg)

我拿一个小伙伴的账号来演示了一下，给他做一份季度报告。

直接一句话启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUIyXP8xXrGsLaiaDFAUp3wWuuTLAo0n1WZhPUTasxAQoHeoZSUOn9qxgXSHZBbhibAMmodkLr4QDqvRs8TDrqNHXQwA71nBHmGs/640?wx_fmt=png&from=appmsg)

然后，它就会分8路并行去抓消息、会议、妙记、日程、任务、邮件、文档、OKR数据进行分析。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqXw6dQdibSyd4hwMCw1147oa1Szy64KibvU1lqTRkWyVDv849WjPHuqnBBPuScaY4MsfEEdJ4Z4jKibBeTAvYu4dPCiawqWyBjgwlQ/640?wx_fmt=jpeg&from=appmsg)

最后，它会生成一份非常全面的文档，里面有一句话总结、时间投入分布、协作情况、主要项目、产出，还有它对这些数据的一些洞察和建议。

比如它会发现某个项目的排期漏了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUevbD7vGjO2uVvfIoIpRV5l8o3Pl4QGAYNTGABAU7IrMmWPyawgbWko6SEvZe5zmB80050HKicYcBguG2pombEd4hjfLFvwHU8/640?wx_fmt=jpeg&from=appmsg)

建议把飞书"文件传输助手"里的东西每个月沉淀成结构化文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWiagiayqMPmZsSYCZY1W1ib4X9phMVWE4GSycLhNtxmUyxzPsosXiaw3Px8QJUyL5snXdVZuE0wvsZW73MxvHLiagsVIQSh7ugIYnA/640?wx_fmt=jpeg&from=appmsg)

末尾还附上了一份完整的季度汇报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqXQekMvlsCgWUDrq5pMSKnEe8MTv6qjTYaJPUXgHkD0fkoPlA0xuicIQpMRfMicO31DAvkWUdLHTe3h5QcwpicMx63gziabU3Vbtr8/640?wx_fmt=jpeg&from=appmsg)

因为飞书上有大量真实的context，所以它生成的文档是真的能拿出去用的，不是那种凑字数的水货报告。

而且这只是起点。

后续你可以根据自己的需求，把这个画像做成网页、PPT、多维表格看板，都很丝滑。

思考有了，产出有了，但是其实有没有占用太多时间去做一些无意义的执行，我觉得就很棒。

**3\. 重复性对接流程自动化**

第三个是我最有成就感的一个。

我们因为有很大一部分收入，其实是我们的AI领域的媒介和MCN的业务，然后我们有自己的经纪团队，因为我们每个月都要给博主来打款，所以经纪部门每个月固定时间要跟合作博主对账，确认金额、确认项目、确认有没有漏单。

之前的玩法是，Agent能帮我们去多维表格里把项目和金额查出来，但最后一公里还是人去聊，我们每个月要对接几百个博主，我们的经纪人其实只有3个，所以他们要把对账明细贴到群里，等博主回，根据博主反馈再分流到不同同事手里，重复的沟通其实非常多。

那现在，飞书开放了这个CLI的能力以后，这个流程其实就可以用Agent开发一个小东西，全面的放在飞书机器人上，交给机器人来跑。

所以我们也开始做了内部迭代，这次跑的流程是这样，先把博主和机器人拉进同一个群，群里@机器人对一下账，机器人去多维表格里把这个博主相关的项目数据查出来，在群里@博主，把这个月所有合作的项目、金额、备注列清楚，让博主确认。

博主反馈之后@机器人，机器人按反馈内容自动分流。金额不对就通知商务那边核对刊例，漏单就通知财务那边补单，没问题就@我表示对账完成。

我也是简单粗暴地直接语音转文字，口喷我的需求，说了一大堆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqX3RnJtdaBsd8suySd0icruNh1XRiavtXupomV7aNUqicUsr4iaR6libfKWV8OnibgibvGy5avKJlyw4M9sy19ZRMTnVYAOeESibFT2GFc/640?wx_fmt=png&from=appmsg)

因为有了飞书CLI，所以开放机器人的成本，也变的无限低了，你根本不需要知道什么是API，什么是事件回调啥的，直接就干完了。

然后我把建的机器人和博主拉进一个群聊。

这里为了保护博主隐私，就用的假数据，并且用同事的账号进行测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWOtGcLvKhmme7T6ggTzjCU02PeFLol1Gw3rowHJFib71aQib2AOTuElqznmIyn6OGRrCo1F5h4MlCJuajhfIbE9FvtS7dKFYRqs/640?wx_fmt=jpeg&from=appmsg)

我们在群里直接@机器人让他对账。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWwo5nxLQ5wLBu6TkHI3CeH9MhqBlUGpiaRTqyJEEDY447NIBQgI5I8C97HTdwxicSOBomX7HvLIahbhNm2n41OMmlLwbExzgvk0/640?wx_fmt=png&from=appmsg)

他会自己去表格里拉取数据，生成对账明细，发到群里，@博主进行确认。

等博主反馈没问题后，他就会通知我们对账无误。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqU3ZJ3IWIKrhicqQzGBl54uv76iaa4hXctUfLFhgtEjhIzdHiatH3HQib88DNjtjmLAQRd6fcPSicTC3N967RhC7wlhZNBq8AeqweR8/640?wx_fmt=png&from=appmsg)

那如果博主反馈有问题，机器人会把博主反馈的问题转发给对应的同事。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXxMF3JYBEMhPoU7DliaZfIbnmgu1cSywdbNjgoaPpSk2JgM6b8rAOOP8BBdVPCWktCV3lCF3voY1ePiaOjPlHrMEibY80ia91ZNoY/640?wx_fmt=png&from=appmsg)

这时候，对接的负责人就会收到机器人的私信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU0QyuNluEyVIl3aLr992s26vGfjxkx9ianbvdaj9JBeRIosCicneIPN2JeaK5504eFAzB1vkz4bdhoU3wOSq3JTiaHyszOs0ic4rs/640?wx_fmt=png&from=appmsg)

我对天发誓，整个过程都是机器人自动做的，我们只需要在群里@机器人对账，然后博主给出相应的反馈，整个过程都是自动的。

当然，如果你想提高私信的重要程度，你甚至可以，让Agent以你账号的名义直接发私聊消息，现在飞书CLI也支持以你 **本人名义** 发消息了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqXVkZZMxEZuZnfPlnSHia10gjvs7YlMNEiatjelGZkIibClqkZjicvtibnofJ7uLlaC42viafBv8M9jQjWzVKOd0hANjzSyBicwxK3UVw/640?wx_fmt=jpeg)

就像这样。。。

这个玩法也能很简单套到很多业务上，只要替换机器人查什么数据、反馈分几类、分流给谁，就能直接复用。

比如客户回款核对、订单异常处理、合同到期提醒、甚至年终发奖金前的数据核对等等。

**4\. 生成可协同的画板**

第四个是飞书最近新放出来的一个能力，画板。

一句话，让它生成一张能全员协作编辑的结构图，这个我觉得还是挺有意思的。

用Agent生成HTML来画一些信息图啥的其实也不是啥新鲜事了，网上应该能见到很多很多这样的案例。

但区别在于，当你把Claude Code跟飞书的画板结合的时候，这里吐出来的不是一个HTML网页或者是图片，出来的是飞书原生的画板，你可以分享给团队里任何人，他们打开都可以拖动、改文字、加节点、改连线。

可复用的协同能力，这个其实是我非常非常看重的，以前做出来的HTML的内容啥的，我想跟同事一起协同，其实很费劲。

我自己试下来比较顺手的一个场景是，开会的时候把口头讨论的架构或者流程，让Agent当场出一张丢到群里，然后大家一起在上面边改边讨论。

比如我跟AI讨论我的AIHOT架构图，我想跟同事协同，让他们看看这个架构是怎么做的，我就可以直接让Claude Code配合飞书，直接给我生成一个画板。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWFsgAmhib16ju7gcdeYgCwFj4bgUr1BydrPibAQfhFHngCHcrsfJ6xjoiaxHaAWS7APPhciaiaeTEnWC1QwIEVFHpaK4KoSasqBIJM/640?wx_fmt=png&from=appmsg)

然后，就直接出了一个这样的画板，非常详细，且每个节点，都是你的同事们，可以随意编辑随意修改随意拖动的。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW4uUsZMnwic4sc6mG4HatDc6TOOjt1QxQsy5sIUL0z3LBshxgs1XG5CMRvFLh4oSJicGaAv6BAibUSHfENs7HszGicfaeibRB6bYeE/640?wx_fmt=png&from=appmsg)

还有像之前我们的AIFUT大会，讨论出来的观众入场流程是一大段文字，看起来真的挺费劲的，我就试了试丢给他。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWp067E9UFlkibUfoByffNXfXMTjsqNTASXzHqfNwYpWlAnDv6GQ4xicZ9eiagLTiaBibibtnibQ2lHWWDGGmTV3Up74APNOssUHa8X30/640?wx_fmt=jpeg&from=appmsg)

提示词也很简单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVKOIliauLC5TbLIo4TcZnmZoZ9BC3fgK8DXgv4PXwFFCzsibKNbfyeaXa2T56k8ZTWMo2ZsMOYPBaWJA6jjHuQEdhp0fNibgmMOs/640?wx_fmt=png&from=appmsg)

没几分钟，一个流程图的画板就出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVUSXO7ORL99aguKNsUK8ickU3yA1IvMYMg9tYkVyoia7Kx5cu5rvPlicgZEORfae9h6OlibgtStgIialDiaDy1kzIToI1ibP9njDBibPw/640?wx_fmt=png&from=appmsg)

所有人都可以在上面接着协同修改，这个香爆了。

而且，因为这是画板，所以，你完全不止可以做架构图和流程图，你甚至还可以做，PPT。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV0fmPsicmqK6eugMsH72mmGlJtiaD1upia3aaibmDXWvJ2lkK4g2lzD1OMAp0ialjYbdmDVQd58htP01ARwOQicZUGmib6wWbLvNrzW0/640?wx_fmt=png&from=appmsg)

而且可以随意修改，随意分享，随意编辑。

协同，协同，还是协同。

**5\. 自动报销和审批**

第五个是我们一个小伙伴今天刚跑通的，把整个报销申请和审批，都让Claude code来做。

报销这个事有多麻烦，我就不多说了，工作过的都懂。

然后我们这个小伙伴，直接跟claude code说收发票的邮箱（她把收发票的邮箱直接填成了公司的飞书邮箱），然后让他去知识库里找报销SOP，照着SOP填写报销申请。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqW0NLMTicExnZIOS2CS92shNsRQm13rfAx4fukR5SAhtI0zniapejqkUjFOPBv1jVVzvibnXylDVibrAbaY9C4VCjAg7UoI4Qr4ibDg/640?wx_fmt=jpeg)

然后他就会先去指定的邮箱搜索。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqVI56R2ibkx3knibhLUWuqzq0af99JCbjc3XZoLWE384ewwhDOHm3fKWKnQia7WlTyl7NF1E4YJKia6R3KIIaQX2XOyrSbY4yKxuB4/640?wx_fmt=jpeg)

整理好发票。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqVhicSuGf5knnbjwLzccS5glGtfgEXal0fKFHibuFC2XVpuGiaexOkBC8AFcu4MsUjqG6jhGvIeMOyXN4dkozEITnUfOe1o1vL3iaw/640?wx_fmt=jpeg)

然后他能自己在飞书上发起报销申请，但是在发起前会先跟我们进行确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXxBk2Nz5eLFNIFGDnXWQicbDHakURYj6r6GqxNxqiaQkTvrgQ5OPYJGFrc67FXicpxW6FAAPnPEzQ80icmicWuHMc6Y2BXrneSBUPg/640?wx_fmt=jpeg)

我们确认后就完成了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqX9bicafwicOdgK1Yy6zDic0tEIiaVCddHWaVtOAIYYYiaQZw8ibCJrRch9ZZ96NdOaSz6BhNrMkfHrR5kzgXsCRYFehaU58ZTrNpqBc/640?wx_fmt=jpeg)

然后审批人就能看到刚刚提交的报销。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUD32YzsZlg0nEObwKMoQBEKAzgLAULhsTxuPFqrdCuAFezFWytw613SYXStPCmQgnMchia4WXQIkFbzHMK7hLvh6GUJ0c1XGhA/640?wx_fmt=jpeg&from=appmsg)

我们财务下午看到都惊了。

那其实除了帮我们提报销，在审批这一端，也可以直接让他来做。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWNEjnXHNyF0mtJ4JDKlKlIQqNMpET351nfcg2zRLROrEjGuic6ZIUFPR1YM2HicicWXu3NictOhe0tjmZjHkkybe2CLgIuD4MJKl0/640?wx_fmt=jpeg)

他会去核对各种信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqVqkIBCCzNp5yEClUdN5EI6Y9Lt8qCZDnuKLjdEfibC5PMtUEZDaOdEUU1N6NgIZYZvgUMIJQ9BGxSCABh9tfPFeRe6KgZB0arw/640?wx_fmt=jpeg)

然后汇总到一起和我确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXTwU8OUSmr3EK1OOnU2Mpbt1iaEvjjao6PHcGWiacEicqRU0ZdHMMMH372px9AcAUZALGiceGZ9Fwc0rt7zU01504IrtJkFO39BmE/640?wx_fmt=jpeg)

我确认后就审批通过了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqVPMVm3yZia9eUT48T0H3EiccehZiaddNibuic3BCctsKUk9MntIdq4qZqRg49oXUiaicrEgeqoM3jrURI6CiciaF9xAS1mDOZ4icgTEQOz0/640?wx_fmt=jpeg)

并且还根据具体情况给了审批意见。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqX5Cb0TSMlcczsRho2kmxbrLbUTuhw4JZXuP93kwJEyfDicIYUIWou9T9TnicvSEFZgicJGUBYWyMvQSbKsxXuo9huic1yicmCLdcS0/640?wx_fmt=jpeg&from=appmsg)

这一套跑下来，整个报销从发票整理到审批完成，都是直接跟Claude code对话，完全不需要打开飞书。

而且这种用法只要换个壳，套到出差申请、采购申请等等流程上都适用，骨架完全一样，无非就是信息收集、匹配模板、提交、追踪反馈。

**写在最后**

上面的场景，都是我们自己公司在用的，但是肯定没法展示Agent+飞书的全部能力，也仅做一个抛砖引玉。

最后简单总结一下。

现在飞书CLI已经是开源的，可以直接在GitHub上拿，覆盖15个业务域、114个能力。

也可以把这段Prompt，直接发给你的Agent，让它给你装：

```objectivec
帮我安装飞书 CLI：https://open.feishu.cn/document/no_class/mcp-archive/feishu-cli-installation-guide.md
```

现在因为能力实在是太多了，我直接帮大家，做了一个能力的全面总结，可能会有点长，因为实在是太多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWsRjsibicia3IYx4cibDkS9zJq3MRscqYMMGibSb45c6QtzbYDrQ9GdVnXO8jWZ9DZQXIGANOZ0qchFBIFJibDCUZAcg7qZgWgUjXBU/640?wx_fmt=png&from=appmsg)

现在我觉得，Agent几乎已经趋于两种协同形式了。

一种是本地自己玩，另一种是在公司里，跟同事强协同的。

甚至都可以机器人@机器人，AI之间自己协同了。

这块我觉得除了飞书之外，真的没有任何一个替代品。

用Agent来操控飞书，形成多方位的提效和协同，可能就是现在很多组织进化的一个很有用的要素。

等啥时候，飞书把所有的能力全都开放，整个飞书几乎全面CLI化的那一天。

那我觉得，我们的办公与协同方式，可能就会迈向了一个全新的时代了。

希望上面这些场景，能对大家有一点启发。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、tashi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

继续滑动看下一个

数字生命卡兹克

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过