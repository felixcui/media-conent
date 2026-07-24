# WPS 新出的 Agent：专治 Word 填表

**作者**: 金色传说大聪明

**来源**: https://mp.weixin.qq.com/s/XPhTXVBnyyMGbiH8Fe0x5w

---

## 摘要

以往使用Claude等AI工具填写固定格式的Word表格时，常出现中文字体错乱、版式诡异、字符缺失等格式问题，且受限于执行时间。金山办公推出的新产品灵犀专业版解决了这一痛点，它直接采用WPS的文档内核来生成和编辑文件，实现了不到两分钟高标准、无差错地完成填表任务，这表明AI处理文档的难点在于底层内核而非智力。

---

## 正文

金色传说大聪明 金色传说大聪明

在小说阅读器读本章

去阅读

真正的办公 Agent

在过去一年里，我的发票、合同、申请表，全是 claude code 帮我弄的，着实省了不少功夫，但也积累下来了不少抱怨：格式我能自定的还好，直接生成网页版直接打印。最怕对方发来一个固定格式的 Word，只能在指定位置改，直接哭瞎

就以前几天我填的那个 OPC 申请表为例（不得不说，海淀的政策一直很顶），需要对着 仿宋\_GB2312 格式的一堆.doc/.xls 来处理，格式是固定死的，不能懂

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjkQxWGfbRAYPCTRBpWvp199iahems6h6wQszs5bmX9ttn6sk1P4FFK1OJU2xTMnnNt8gs1j1Q6DHaWavD3apEj7aO55siagBSYs/640?wx_fmt=png&from=appmsg)

我自己的各种信息，Claude 它都有，它也确实能干，毕竟它里面有 docx skill

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgYVSdowJGs4eDiaPqWQqjAroJSXBeUkHkKNe0fVnRKuv8ygDoSicZyTP0fV5ZcN74qnrr57YlqVUw9XL6neG641XIL2iasMic8VVQ/640?wx_fmt=png&from=appmsg)

但你要说干得好不好，我只能说...即便是几行字也要用上好久，中文字体和自定义版式经常出问题，需要手调，就比如下图：中文字体经常抽风，且版式非常诡异

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhoS6sYezYFO5KBlyL9jJjIJmyExmkcO3Tia7SglumFvWZ3T6G0VKkdH2VPfyCr1PkggmSwICwQyzhjnmeskPmeeNicM91g90InQ/640?wx_fmt=png&from=appmsg)

同样的，我让他去填写一下 OPC 表格。不出意外的，虽然内容完全 OK，但字体都发生了变化，甚至还有半截的「填写样例」，我甚至用的是 Fable 5，推理 拉满

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjaHJVbRcht7yJrypVicYsWDGia80MO8Ssic2MmZzrib1dCwibX9AUhfC6wOzIl7BYicZSUuibsaqV4KCTTb7zeEKzwFLV76B73d3ZnuA/640?wx_fmt=png&from=appmsg)

这种事情在我工作中还是高频发生的，我也不知道为啥，某个字符突然空白了，某一行内容直接拉到了下一页，某些字段干脆不显示；然后网页版的 Claude 还有个毛病：单个任务最多执行 30 分钟，所以如果表格太大，可能当场寄给你看

AI 能不能处理好文档，和智力无关

前两天我去参加了金山办公的发布会，他们拿出了一款新产品灵犀专业版：用 WPS 的文档内核生成和编辑文件

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdjHZ7HgS4HI1RrpTVaTvIYo0qP4lz0RVDewlU5HjzbibTVnXoqGIEyLvqwceNgQb3KA5qkgonmll6OJqzgJzDGJJfQqUYeUF518/640?wx_fmt=png&from=appmsg)

同样的任务，不到 2 分钟，高标准交付，毫无差错：Agent 填表这事儿，终于有救了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgRp1FZG7Picw6OjNSYickcaY3uPPDqmvXvWt61C1o26kPRz6gQAkqtHQdjvlI4ha78FIibv0PJUI758pnkWVfTqPGz24HGDRXqZ8/640?wx_fmt=png&from=appmsg)

## Agent 填表，问题在哪

所谓自己的毛病自己看，我让 Claude 自己回顾了下他是如何处理表格的，然后...下面是它的坦白，以及我的转述

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdias0ib0pIcht2jicNCOsleNDIM6UOkxw2JACHrZ53kI4ePCjo3EWyZUgV2u1elJmfRQxAKhlYFImO11Zuic4oKOtA4EOhcdVxgK2k/640?wx_fmt=png&from=appmsg)

Word 文件本质是个压缩包，后缀改成 `.zip` 就能解压。那份 OPC 申请表解压出来十几个 XML 文件，我们在 Word 里看到的那张表格，只是这些文件渲染出来的结果。

对于上面的那个文件，看上去是一个大的表格，其实在每个格子里都藏着很多排版规则，比如字体、行距、对其、折行等等...

在 Claude 处理 Word 文件的过程中，使用了一个叫做 python-docx 的开源工具，而这个库的抽象层里没有「在保留格式的前提下编辑内容」这个操作——它能做的是「替换」：把格子里原来的内容整个换掉

这意味着：Claude 每往格子里写一行字，这些规则就会全部清零

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjicdVbnTWZPWw5cGMgGJak7eh8Tp3aNA1LQJFRlQ6z5serFcGSUJASU0m6CxCgicTlZSPA2xCX8GBwICXG9knuaFGODBmXKOZyY/640?wx_fmt=png&from=appmsg)

这份表用的字体是 `仿宋_GB2312` ，公文标配。但在格式声明没了之后，系统不知道这行字该用什么字体，就从机器上找一个凑合

行距也一样。原表设的是「固定行距」，格子紧贴着文字，上下几乎没有空隙。格式没了之后走默认行距，默认比固定值高一截。一个格子多出几毫米看不出来，十几行叠在一起，整张表就被撑高了，内容挤到了下一页...

而对于那半截文字，是本看到标题上方有一个空的占位段落，行距设成了固定 8 磅，但塞了 16 磅的字；在这里，Claude 用来预检的是 LibreOffice 的响应方式不同，不同于 Word 本身：LibreOffice 对这个规则更宽容，会把超高内容画全，但 Word 则更严格，导致了半截文字

....

这么一连串下来，Fable5 即便再聪明，但由于渲染和处理的内核不对，该错的还是错，不可避免...完全是渲染引擎的问题

## 亲生的内核

这里有个冷知识：WPS 和 Word 是文档互认的，能对信息进行完美渲染

而灵犀专业版，调用的便是 WPS 自己的文档内核，在往格子里写字的时候，文字和会连同各种排版规则一起写入，这极大的保证了速度与准确性

这里有个值得说的事。市面上不少 AI PPT 产品能给到「可编辑的表格」，看上去挺厉害。点一下才发现，那些表格是一堆自由文本框拼的，加一行都加不了。图表呢，也是图片，拖位置可以，改数据不行

灵犀生成的图表就是原生 Excel 控件，点进去能改数据维度。生成的表格就是原生表格，加一行就是加一行。他们内部管这个叫 **「图是图，表是表，图表是图表」**

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiazNwPfyl1ggwow1Xb5ic5Ugx4NhtB5FKHdlRj7w8yUiaRwefrDbeyZmcKsqnxDcN7wDqpTCiaNPt6o2URDwBCTu9sw5icice2llmXQ/640?wx_fmt=png&from=appmsg)

数据联动也跟着解决了，灵犀生成的表格由数据驱动，改了原始数据结论跟着走，追到对应的原始指标

排版这边还有一道渲染检查，专门扫跑版、遮挡、文字压图这类事故

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaZR2oW1snB3xM9V971XxmBMOxfhfOhayFd0PMWlyxXn1zic7xnKbwMtApN10TFmQhuWoeENDFoH5QdQK90qSwwyI6pI5S2YHB4/640?wx_fmt=png&from=appmsg)

而对于大难题排版，灵犀更是还有一道渲染检查，专门扫跑版、遮挡、文字压图这类排版事故

也是考虑到交互的便捷性，灵犀把所有界面做成了一个闭环。文档打开之后，右边有个对话框可以跟灵犀交互，中间的正文区可以用审阅模式逐条改，改到某个地方觉得不对了可以直接上手用键盘编辑。生成、交互、批注、编辑、交付，都在一起

并且，它既有独立客户端，在 WPS 和微软 Office 里也有对应的插件，也还有网页端，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjdWic8H8tibQWibbWh6KnamXyf5ia0NGEDFibQfLdzaOLsBCXwERJta74vvqA22Pibfdd8fiaLOdJ5tl63rwFSicVtkYfb8FkpfUx0psI/640?from=appmsg)

「参谋可以出主意，但助理要把事情做掉」「市面上会聊天的 AI 很多，能把结果直接交付出来的还不多」

田然，金山办公助理总裁

金山做文档格式做了二十多年，这些能力在 Agent 时代反而更值钱了

## 不只是 Word

灵犀的能力，其实也远不止我上面提到的那些，这里也整理如下

**Excel 公式和图表**

灵犀生成的表格，数字背后有公式。改了原始数据，结论跟着联动。表格自动美化之后，图表用的是原生 Excel 控件，点进去能改数据维度和图表类型

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhydzf6QgibojRpClb5OgWgeibpN5uvXGuegCXMU9smo1aoaQVrtZyyryj4ItCY4tQtBjsSAw4myZVlsStKHBEQnhGQv2FnGNZjo/640?from=appmsg)

**读文档生成 PPT**

灵犀能直接读文档生成 PPT，排版样式不少，图表用原生控件。发布会演示了一份市场复盘 PPT，十几页，图表数据都能二次编辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjn8ODZw67QbvP5icpFqY49E5ib7PH8oTVERficpd7w7iaMHkWIo72O0kuuCXGplT6vicb8BWpyAjU09lEq4ibEzvcV6b6fJldOgVHt8/640?from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhck2lUia2Mnjm1ILh20ywkxZGuq8d2sVibH9u6iaWmiaZuF3oPCpKZt1xDn5xQzibvjYB5HNl87bCDmuonsLjNlCpxFVso0WNSL70k/640?from=appmsg)

**浏览器自动化**

灵犀能调用用户的浏览器，登录公司内部系统，按流程填表提交。发布会演示的是报销单：打开报销系统、选费用类型、填金额、上传附件、提交，全程用用户自己的登录身份

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaRxm3ga1f0kN4vva5iahQE6d1XQia6gLyWn6IHxermwWlgn2jcYDzKPkWGRZFdibu2utqSI4gMXdvFMHcXu9ic9RvRpJv1YfjT93g/640?from=appmsg)

**论文和公文排版**

论文排版，页眉页脚、摘要区、数学公式用的都是标准组件，分栏也是原生分栏。公文格式同理

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaePA3Mo3mQ5GdnYiaPXkyMz2uIgOZxUTqpxePKrKd4FPqM4vrHjicQCnTw0zEGh7CEQXdgyQibrjdS1aQnEr1nmCaeo9xMM5pY3c/640?from=appmsg)

**项目记忆**

灵犀按「项目」组织上下文，历史任务、文档、对话、改过的意见都跟着项目走。第二次说「按上次的来」它知道上次是什么。授权过的文档它能调取，记了什么你能看到，能校准，能关，能删

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdjtyeuFtgoJKTROmsSEswJXB6dCn3yiaZm0XAWiaPVPLxSkBvXxyboAeScQEoBvqibAia5rJmELeds9vHEicwVyYd2FbkwsEdD7IvXk/640?from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhF5kc9powFvjRjLpKfI9JOCicX1Kocaksk1TpJic2L7IYyciaxuxClsJA1YVy8icW2bruHxrT1OfAU1snB3ib32G0tBMbnNrhreqs8/640?from=appmsg)

## 最后

参加完发布会我追着他们技术和生态的朋友问了老半天，产品之外，我贼想要这东西的 API 或者云部署方案...希望能出吧

然后，我还要来了发布会的 PPT，如果感兴趣，可以一看

![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaia3kPbSLjZpLgeeMBdIvoudkLQsh1DiaHqHNSLwedZpNZcUPXosXv11xuTicNjQc28QQBAy5t8d5sr7RApwRdbgq3mcX8jdzy78/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdjUHtUicCl9LkbF5Puia1rK1S8ib4CBOxF2gAUvwH5H1TrUFwV5AcQ9rpnduXIpol58wvK5N9uDesLxmaA81ebgeR4m6xZU0ibfnMw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjf2Q4Banuxy59xbhV1yscjBiaBy77v0tfibHvgicdxviaO8uUmIdg52HIbhhqJfoI0XjKnqNWHrYdqvUW8hSBZtQ5N7B0LFF0niaIE/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgY5NVIaGYIreBiaj2ibicwTDqyppbcibnmGCWp55a8Eibmv9RpjlAzFQbyxdW6tNPQLIDeBIJp1mwdkrGV04JFwjtKVJJWT0X92218/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdia69aDeMPmWCpRDW833wxJ7UEBmUxLgG2JlBnIWvdia5rv0o9oQaKKr7oH99XsLDsLv5LTv3JprfPiaYhkqArpTge0OnXln7syXI/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhtpqO0H4gYct2HFcU74FwO0nkK8akGyp4nuXlU3Jibm3YRicic3loxIIW9xia1icqicLvosoPm5xesxVXPZzQhFeuE1O5kkC9yQcrEw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaBStyEdnhjwlRD1ZB2pfPeqfUux3rvtWVADt5bzUnGCTicwg8h2NOvjm0RKMS1NsrbpDr8DkDaSvwBoKpFEZBrk0qFiaV2BzRzY/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdiayPANtqQ06uB3EqQibz8nMicYNKGdKv6XXWoXYRsEwk3xDsXtkrT0DNff2M3enx6tfgiaiaOoBLdKRlADibTwYxSVcF9n5uI4icoysc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjlDdWPS0uJ9d1UZEztfcSicfmHKuGVN3LRiaBZelyLicZDibvZtYDOlcfTwA7p6X6jFvcZ468oiajicK2ia6iaicMw6dDn2Mia3ISeyA8Kc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhxKCXGoM5TJrSibo9zVIzXzaqpoiamMblib9C4gE9vRQkx2yQSbnMAZnFibGgoTo778M5JlicsQpsBCs7rT9bxObAExMU26kAQZnicc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhaD2mG8lDGqEtKiaicMswYGOuaRyhDVFtfbyib7euHaBmvAthJeibVrkAjzicQOZic7iaX2C9ibSwEfia3mUSXYYmAl4piaFhndHx3wljLg/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgich5Ckice4Nxu8KbS2KYuvojarHIevxK7QBTpphSNfljESoormVN5gsCWDqXrJZfgzNUYS8030VXk5MumNDduibRwj785q5zoicM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhRFCMXxcJ8ichD9J5Jpa0w5iaJYL1I5dbFhXaGyZcCMpoeDeeiaHho1jurDiaKEfpVabAYg0QfIMBMmicMrYh70xF3458qOH6nKPKM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjfQKGaOGJGkX2qD2Xb6yddJKAwd5zNicztOMB9kv0GlibUYBRoBOYsPslia7SNAu8hsbyKlaVWcYAibyJZtvHKOibw69jP9axW2Z58/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdjzOhZezUDM2eic8PupmsnjCia9GVN1yIibMq4PIj6lSnruQD2fxOpJ0uxdTFKJFXyYS9L8OmfHPib7X0e1DTn7hib5WuzWTupynV9E/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdj43ibUZ6oGKCRnLyFjl9oVibibJ8EwHFI53VDjHjaZ3HSib2zu88eAnDIFGLuUCEaKHrgrZwmMicYDfRVxySfk25kSdBRgxUuzn488/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjblNic8ARRWlktg5WrO8z8a0Tfsee2CymDJMBRGdicBokchCEBuoj61JlDgG4hiceYIQrRyBIhbKbwibfqtRBpkWt1ichcxb9WuibBE/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhhb9NicHH2bqhfoia5Z0CtWyTuTgrq3ahfdxx8ictG9WkAyianoCOXd7Vjj9pXgcUMic2V7fsVtjAibK4kGottlozGRFLQ43iaR6P5yM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgX8uqkD4MB8HIQIcKFLViclV9E4eqc91NhXNxtbEDctrhggoKfABuYibfZE88pRpNEqGVmAOS1YbOytDCNNqC7MVBvuSdzX66zA/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdia8u2MsibTFsUX7QsFGzQt3H4SrZbiaYbP5eSajremCLSnDFSKXSWicGd2VAfOm8LBkFDF7HKgpOugevpsFtzicQRiaeRHKuT4aDsaQ/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgp2zaIzErMxEuTupzAMiaMib7vqFmIVtic0Olhgtj3OOrjGNYW1nsbiaMiakeTgbEqxn59HrVFianZmpaAcTnAqxwGNp8RhZVtNWxp8/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdiafJOQYV0opX8WzYiaLl3s1vMiaicWvibTQXib8RVjibsWkibjuv74ic6icSqMEo3QYUTnMvuVwKH6VMCRLia98YQicRkbtBMBjKLoH0qKiaZs/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjn5qZg4FP4bKrtNwu6GibiaO7ko7gLP7PtVfUV4vvFFaagficBOjAV51TeUhEkyNv6g998XLc6VuH5pPu1AzVlvKQvMs8684w2VU/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaI1uUUbQmrXTIgbGOgPPGY4xz1pjX9ftDja11TsYCgb9owZEoQu43lVvHZbV3VkbHAvqdibuZPVlL7dRDwGUqpN8pf837BpNAM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgh8bZ2WAicvSBibJ6OoicjbCeFkDIE6zic2LYsUpAtVUSD9yJKl13lOcucX6yqCk2icZJjnEu98UImCiar4vmmjD0qxjk5J3Ls9VPzk/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhF620Cm02xF9uZKvEENLIYofbzXia2icas0iam6g6dDWVMeYr5oAgicFKSzaOUv9EZ6uPnxDqiapbr9qGXJKXgb5mEGLk4Rv0IQLMg/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhx7xF8ZjJWwWpMgkDnmdwIDIbJtqIDEwvossULOaZPjrmwIR9pcQFsjZjibGcuxD1FnzwMvRrtu7Xx5Moc1RicEwHiaiaRotjJQH4/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgArLo9REeqjwSuZNHTHBL8KlmKIeVY4Qxibz0dUtFXf2zX9vibPx2vhgwm2iaQ0qPIMMLX8JRvg0Micax96J3d29MMfrXYwDPhug0/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdglW47YQrZZmAp0ficQbfxVyicFVf3jOH13NTB3YGCuoGPEDWFJXXiauGyLyiacmeFQ1JSVfaWoJby9Txf1rL2ldFZg0ufvQKGrBvc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjiaHHibggic6cMTr1DCMhbmsiaicpTrbRy23U13Mf7xAs86xmW0IGLyLibpmEo2r5QoHH2m7MlkUMRjaAmOiaIphcl6TOUVBwxIcNJy0/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdjyBPZD4zBSmfJ09pC7viaaJrTv2LmgOzNFehdBeN7Qlctlg7Ygg0sLZiam2WD5Kvf6ZRibVGq2gHh93Oj2eYhicibXZzHhickBU9NCs/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdiaoRorVdtwaEDS1wSNrCMwlRycFDib545rld8RV5HdW5j0SWkUpfe88IzckWdicaZMseOQYbeIp7ic8LaPPIVbU4pv2z0UGvnjgfw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhDMurb3wKazEGGgCBvWAY4g49iaia59jtY8u2iahj2xnO99AU0w94vbcOL8n6x9xibbHCcyeoGicOqdEDUibMib2zfAU4ScQBnrmQSibs/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdgFNLYoWFskB5icFXSVBqqxUYV45nNPnksk3ZFenVMSvp0DdjaoSbVlRwU5axf7VBDJicMDtPmH6afzuEq1d0dZyyeyeicbAibHibjc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdjHZ7HgS4HI1RrpTVaTvIYo0qP4lz0RVDewlU5HjzbibTVnXoqGIEyLvqwceNgQb3KA5qkgonmll6OJqzgJzDGJJfQqUYeUF518/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdiaSjLaoBXiahe9KBrwPnrDV8NG5IoK9Y5uexpfPtWnic600G3fWBJicXTg39wTvzMPlnxm9c2LO6GI95iaialOqvgBricQXFVJwhQArU/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhsr7GCickUQibg77ewLPe441ouFbtMmwjUPgibZTQuMoMmR4vB8zhu3IZGhnBlY8gdw41ON9vibSImFicWnz2J5JnxSkonBsiat08E0/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgCmLysQje6wYS8Oc8F0cuYBHvibKEgvEMuW5Dds9hg3322qCp8icRCFXntTk9sPwPiacsAR82amR4Sy5loeN5sR4ZEqjnruYdNIk/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhzpvuR4DiaWIfvXahfByiaj9ianEEOm59tRQHhpmV8NPNtwk9uwooalMJxCrb0OyBB0qyUFldEOOWkIzl4PCsibFQJibcx9DOYD0a4/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgeBkKGYkjCRQaI0ZmibBVqk0rj1UkRMSSlSicFdpFXUzeAIK6IJficgM3VL0OhCM6TAXZfy0iaFy6xratcWUXLJCz1qs2SBxrKLAk/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhJfub3Z7GdIrWWdTnLe9KvFIJK6hundIQStGl5ejKC8wEens1KLajY7ibWFTWINe7lFKIBsnZP2KrDgvHFLBoG0n4sYuhSQfUg/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdgnXyJkNqhtDqO82pSOrrBw45R5ISrcGwIBpLePFdBa9dbjPldkrp2toCg8GvibY18Tg5I7Ax3jUcul8wkGeMyLcptFD7WD6NKU/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdguibqecibTdLSofRPOuG0X7RicfA6bxbu9ib6IBfiageMh1nLxmERrDxibvg86d1ZibUhiaCic1jXWBslGmoGe1xDv98Ajtf9oGhQzGasE/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/jXSGuwJvpdhibjqia9zZ39x8avNsq42vwblZOoy6oQK2ibjdYmFT18CnkiaZn5f1e29xRtv3XYh6vnrLDCvW217aqiacBmYPoP8Y9WANq9gz3ro0/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/jXSGuwJvpdhHwmw568nhFxxz3gasrib9B4IYAia5WdBicxuZLbmXLh3KLMTefMzQIxZOicLaQLjyd4CW3GFa3JMM07NEcIy0wCgnQ6aiawnznAt4/640?wx_fmt=png&from=appmsg)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过