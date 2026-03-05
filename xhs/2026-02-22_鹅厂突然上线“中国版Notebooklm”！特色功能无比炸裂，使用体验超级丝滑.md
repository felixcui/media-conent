---
title: "鹅厂突然上线“中国版Notebooklm”！特色功能无比炸裂，使用体验超级丝滑"
author: "无名的帕斯卡尔"
date: "2026-02-22"
source: "https://mp.weixin.qq.com/s/Lrh0MKLkxfXqyZf3O2ISFg"
---

# 鹅厂突然上线“中国版Notebooklm”！特色功能无比炸裂，使用体验超级丝滑

> 来源: [无名的帕斯卡尔](https://mp.weixin.qq.com/s/Lrh0MKLkxfXqyZf3O2ISFg)
> 时间: 2026-02-22

---

喜欢研究AI产品的都知道，国内有希望对标**谷歌Notebooklm**的产品，一直默认都是**腾讯ima**。

毕竟二者在技术原理上是一样的，都是**RAG（检索增强生成）产品**，无非接入的模型不一样。

而ima似乎也在紧追Notebooklm的脚步，最近推出了**【任务模式】**，支持生成报告、播客和演示文档。

**腾讯文档空间：翻译翻译什么叫惊喜**

但是，我今天偶然点进**腾讯文档空间**，差点不敢相信自己的眼睛：

这这这……**这不是Notebooklm吗？**

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLtgDpI8UZibooWwfcyvmW9TYgmfsxkYdrObTr4kEbwZFjaZJv5H09H4Q/640?wx_fmt=png&from=appmsg#imgIndex=0)熟悉的左中右三列布局，

左边**【资料】**，中间**【问问空间】**，右边**【应用】**。

![07e10710bd7d10857cbbcf935aacb4c4.gif](https://mmbiz.qpic.cn/mmbiz_gif/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLJhrMnhiav460ENZLusQ6AgEXAUhNicpb782QYzFLaqhiavR2ibSWZQt4KA/640?wx_fmt=gif&from=appmsg#imgIndex=1)

好家伙，鹅厂内部赛马，把ima的老家给抄了？

激动的心，颤抖的手，我立刻开始试用！

使用感受非常炸裂，使用体验非常优雅，且听我细细道来：

## 

## **第一炸：支持导入微信文件
生态闭环了！**

正好最近我想要研究Skills，建一个主题空间。

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLayhJGkoVPpia91sec95ZGETITCmjLrsibViaicofqlib9xxrzeJLnfzuv6w/640?wx_fmt=png&from=appmsg#imgIndex=2)看了一眼能添加的文档类型……

卧槽，有点炸裂！

支持导入**腾讯文档、微信公众号文章**自不必说了，

它居然**支持从微信导入聊天文件**！

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLn0NMGwDkYulG2hKX8kibyWNrtV13wUSibNvj5Lrkd62j8XosbjuNICcg/640?wx_fmt=png&from=appmsg#imgIndex=3)也就是说，以后微信上的收到的文件不用保存到本地了？

缓存后直接导入到【资料】，用AI进行提问！

另外，腾讯文档空间接入的云盘产品是**腾讯微云**……

说实话，我已经百八十年没用过这玩意儿了。

如果这个腾讯文档空间能火，搞不好可以把微云也给盘活了！

## **第二炸：已保存的答案随时修改
****知识变“活”了！**

光说不练假把式，接下来测试一下腾讯文档空间的生成能力。

先导入几篇跟Skills有关的微信推文，提问试试。

就用它默认的问题：“Skills与Prompt有何区别？”

看看它的回答：

#[#1](javascript:;).**本质形态不同**

-**Prompt**：只是一个**Markdown文本**，是一次性、临场的自然语言指令。

-**Skills**：是一个**文件夹**，其中可整合Prompt、参考文档、脚本等资源，是流程性知识的**能力包**。

#[#2](javascript:;).**作用方式与时效性**

-**Prompt**：

-类似“站在实习生旁边口头交代任务”，只适用于**一次性、临时、随时变化**的指令。

-一旦关闭对话，其指令就失效，仅在当前会话轮次有效。

-**Skills**：

-类似“给实习生一本SOP手册”，Agent可在需要时自行查阅、加载其中的规范、脚本、模板、参考资料等。

-可**跨会话、重复使用**，形成稳定的可复用能力。

#[#3](javascript:;).**知识组织与调用机制**

-**Prompt**：单段文字，无内部结构，无法分层加载。

-**Skills**：采用**渐进式披露（ProgressiveDisclosure）**机制：

1.先加载元信息（目录/适用范围）；

2.判断任务需要后再加载完整SKILL.md；

3.仍不足时按需读取文件夹内的其他文件。

这样可显著降低Token消耗，保证长对话中模型性能稳定。

#[#4](javascript:;).**适用场景**

-**Prompt**：适合快速、临时的单次交互任务。

-**Skills**：适合**流程化、可复用、需多次调用的领域经验或工作流**，如自动化选题、整合包生成、数据分析等。

#[#5](javascript:;).**价值定位**

-**Prompt**：侧重即时指令传递。

-**Skills**：强调**经验沉淀与复用**，让Agent在不依赖人工反复交代的情况下稳定执行复杂任务，是Agent的扩展模块。

---

**总结**：

Prompt是一次性的“口头交代”，Skills是可长期复用、结构化的“SOP手册”。Skills通过文件夹形式整合多种资源，并配合渐进式披露机制，在Token效率和任务稳定性上明显优于传统Prompt，尤其适合需要流程化、多次调用的智能代理应用场景。

点击**【保存为笔记】**，回答就变成了一个**在线文档**，进入了右边的**【应用】**模块，且可以转换为左侧的**【资料】**：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfL4om8rQL9wicUyZI5iaHiaIzRuSIDicWmVEOfKcArC2ibbXYSLB3iaAEjm0zw/640?wx_fmt=png&from=appmsg#imgIndex=4)虽然表面上看和Notebooklm一样，但是保存到【应用】里的，并不是一个“死”的文本，而是一个**随****时可以修改的在线文档**：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLibkxbSDE16tYMoyV7cWPmbEbqiaAicUADYfia9nP7icatOHHRURdrFtR7bw/640?wx_fmt=png&from=appmsg#imgIndex=5)横向比较一下，**Notebooklm不支持修改已保存的答案**；

就算用户把答案导入到GoogleDoc里，再怎么修改，Notebooklm里的那个已经保存的答案也是不变的。

而**腾讯文档空间不仅支持直接修改文档，而且文档自动同步到腾讯文档首页**，也就是说……

用户不再需要点进特定的空间里寻找已经保存的答案，**在腾讯文档首页就可以搜索到****它**：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLHQ6jpzv1T8zsCg31XHOK6ZFbsdq7iall1IJNtYFRicibZRfdric7XvU7Cg/640?wx_fmt=png&from=appmsg#imgIndex=6)优雅，实在是优雅！

## **第三炸：从【应用】进入【资料】的文档
可以同步更改**

然后，更炸裂的来了……

当我修改右边的【应用】里的文档，已经加入【资料】的文档也随之修改了。

这个功能一下子就“弯道超车”了呀！！！

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLBQoXtOSUc4ic3tGmGAyGlCzrl5jPavz7mwIWhIoSXNkL1neiaIb6lDLA/640?wx_fmt=png&from=appmsg#imgIndex=7)用过Notebooklm的都知道，**Notebooklm“来源”里的文档也是“死”的**。

而腾讯文档这个**同步更新**的设计，一下子就把所有文件全都盘“活”了！！！

换句话说，和Notebooklm需要用户使用新文档替换【资料】里的旧文档不一样，**腾讯文档空间里的【资料】都是“活”的**：

假如【资料】里的文档是从腾讯文档导入的，那么它支持实时修改；

假如【资料】里的文档是从生成的答案转换来的，那么它也支持实时修改！

## **第四炸：导入到【资料】的网页
****支持修改！**

然后！更更更炸裂的来了……

我突然发现，**已经导入到【资料】的网页，也变成了“活”的在线文档！**

是的，你没听错，网页变成了在线文档，可以任意修改：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLSQiccEBuLdDNZCsDNhmfocDibicGSWBloBdQD12ias2JPYCFI1GIUWvRHg/640?wx_fmt=png&from=appmsg#imgIndex=8)也就是说，我们在将互联网内容接入到【资料】库的时候，可以手动干预信息源，取出冗余信息，避免信息污染。

妈呀，**Notebooklm突然就不香了**。

## **第五炸：生成PPT支持二次编辑**

目前为止，腾讯文档空间的唯一弱点，似乎就是【应用】里那六个功能：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLs4Vs94Fx2N5xCucmzO2ib8ib8nIsyyrto4oKQlygOvuD5jcTUtrF2Gzg/640?wx_fmt=png&from=appmsg#imgIndex=9)

**学习大纲、重点提炼、思维导图、汇报（PPT）、测验、记忆卡片。**

貌似除了汇报（PPT），其他都只是生成文字。

于是我试了试生成汇报（PPT），结果发现：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLHzjSkCt9wpia4UJAqK17xib4fEcnn1SJg8O5TwS5AibabHsricTJ6e4Vkg/640?wx_fmt=png&from=appmsg#imgIndex=10)

坏消息——

说是生成PPT，其实还是纯文字

好消息——

**这PPT也是个在线文档，支持二次修改！！！**

**![8f80c917972f051a379540ed257443a0.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfL7GrxJXW58kSOCsia6bN6DVll2fotzYcYAVOvgPD6j5ZbIumOqicA0YXw/640?wx_fmt=jpeg&from=appmsg#imgIndex=11)**

用过Notebooklm的都知道，Notebooklm背靠地表最强生图模型Nano Banana，生成的PPT虽然美观，但是不支持修改。

而腾讯文档空间背后的Hunyuan模型……

![1ec556ce32ac966678bb90fada31ca6e.jpeg](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLTRuLalZdWiadX65wsZD6MfZcK4jiawEtTtpC8O2So6yXr5mytvjWDMWQ/640?wx_fmt=png&from=appmsg#imgIndex=12)

开个玩笑，没有批评的意思。

在我看来，这其实是个**功能取舍**的问题：

想要**画面美观**，就要走模型生图的路线，必然要牺牲可编辑性；

想要**可编辑性**，那就要走结构化文字生成+PPT模板的路线，牺牲的是美观。

## **第六炸：【资料】库终于有文件夹了**

就在我以为自己体验得差不多的时候，我突然注意到【资料】栏的上方有一个小小的按钮……

那颜色淡得，诶唷，生怕用户看不到。

此事必有蹊跷，好奇心驱使我轻轻点了一下那个按钮，赫然出现五个金光闪闪的大字：

**新建文件夹**

妈呀，顿时感觉天亮了！

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLyv1kDwfHLsdWDe4J6fw0viaJPEUCEc1Dic6ve9E9UzDOoWCkhKOye3Ww/640?wx_fmt=png&from=appmsg#imgIndex=13)Notebooklm用户都知道，想要用好Notebooklm，就要同时管理几十个文件，提问前一个个勾选，真的折磨人。

而Notebooklm迟迟不上线的文件夹分级功能，腾讯文档空间一步到位了。

点击文件夹旁边的➕，就可以**上传资料到指定文件夹**，

对于已经上传的资料，只要拖动鼠标，就可以放入指定文件夹，

然后，提问之前**勾选文件夹**就可以了，不需要一个个文件地勾选。

**开发这个功能的鹅厂员工配享太庙！**

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLqUmQdoNd6h7dpV3yeNvCUMZtL8c5xVbTaFx6GHLgBzewdQMdY7MoFQ/640?wx_fmt=png&from=appmsg#imgIndex=14)## **第七炸：这个产品的上限不可斗量**

然后，我突然意识到了一件事……

这玩意儿……不会还支持多人协作更新吧？？？

然后我就看到了右上角那个熟悉的蓝色“分享”按钮。

是的，它支持多人协作：

![图片](https://mmbiz.qpic.cn/mmbiz_png/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLOZWttLicdrKkyb8qzzFdJUkH1EjPbGevnc3PCSLs6NxOgE9AyDm7Ywg/640?wx_fmt=png&from=appmsg#imgIndex=15)到这里，我突然有点头皮发麻

因为我意识到这个产品

虽然目前还不支持多模态生成

但是它的上限其实非常非常非常高

![知识库.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/06vRoic7ibgEq4PM7KgZkcjPLIAF0gIgfLHeQXYzvviaTlicwqBb07JrjNpXemgTrghzFfUtVa4iahFAWVpfDQ3TBoQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=16)

想象一下：

假设有100个领域专家，每人都用专业知识写一个在线文档，上传形成一个知识库。

那么，使用者就可以通过不停提问，将这些知识和经验彼此交叉，不断涌现新的知识，新的知识还可以再加入到知识库里。

而每一位领域专家只需要定期更新自己的在线文档，就可以保持这个知识库的“新鲜”。

不仅如此，他们还可以把经过审校、删改的优质信源添加到这个知识库。

这样一个基于腾讯文档的知识库，可以打败市面上99%的同领域知识类产品了……

以上就是我初步试用腾讯文档空间的一些感受。

虽然它多模态生成的能力还有待加强，但是它的产品设计思路实在是强悍。

**【开放+活动】的知识库，有很大概率击败【封闭+呆板】的知识库**——即使后者有Gemini和Nano Banana的加持。

欢迎在评论区交流使用感受。

往期文章

[AI赋能出版1：仅需3步，生成定制表格，工作效率提升300%](https://mp.weixin.qq.com/s?__biz=MzA4Mzk5OTMzMw==&mid=2650562173&idx=1&sn=8c2516f94e41fa75d3cfb249deafaf06&scene=21#wechat_redirect)

[AI赋能出版2：仅需3步，让AI生成高质量文字、图片、播客、视频或PPT](https://mp.weixin.qq.com/s?__biz=MzA4Mzk5OTMzMw==&mid=2650562209&idx=1&sn=54fb8eb38bc291beafca109196d522d2&scene=21#wechat_redirect)

[AI赋能出版3：“新书选题分析智能体”上线，一秒捕捉漏洞，扫清选题盲区](https://mp.weixin.qq.com/s?__biz=MzA4Mzk5OTMzMw==&mid=2650562219&idx=1&sn=1fef749172120c59907e7b17a04a0aaa&scene=21#wechat_redirect)

[#AI](javascript:;) [#Notebooklm](javascript:;) [#谷歌](javascript:;) [#腾讯](javascript:;) [#人工智能](javascript:;) [#生产力工具](javascript:;) [#知识管理](javascript:;) [#ima](javascript:;) [#鹅厂](javascript:;) [#腾讯文档](javascript:;)

---

*原文链接: [https://mp.weixin.qq.com/s/Lrh0MKLkxfXqyZf3O2ISFg](https://mp.weixin.qq.com/s/Lrh0MKLkxfXqyZf3O2ISFg)*
