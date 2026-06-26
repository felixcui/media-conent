---
title: "使用Coze与飞书打造你的专属网页收藏助手"
source: "https://mp.weixin.qq.com/s/pPTPW-griYu6GUSMD6du_A"
author:
published:
created: 2026-06-22
description: "平时浏览AI资讯，发现有收藏资讯的需求，以便后续深入阅读或后续整理归纳。"
tags:
  - "clippings"
---
AICoding基地 *2025年9月16日 23:23*

## 背景

平时浏览资讯，发现有收藏资讯的需求，以便后续深入阅读或后续整理归纳。希望能构建一个AI智能体，发给他URL链接，便能把该网页的信息存入到飞书多维表中，经过摸索，实现了一个相对比较简单且完善的方案，包括以下四步。

1. 创建多维表格。
2. 创建飞书机器人应用，创建流程通过webhook写入多维表格。
3. 创建coze智能体，获取网页的标题，内容摘要，并调用飞书机器人将网页信息收藏到多维表。
4. 发布coze智能体到coze或飞书，就可以通过对话收藏网页了。

## 创建多维表格

创建多维表格，主要包括三列，可以根据情况调整

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7m35GicdmxJPKQ1xWQfeGq1xpIUT55TQCUSzdicAJlf4OZICMWztTyI5Q/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 创建飞书机器人应用

https://botbuilder.feishu.cn/home/my-app

1. 建立机器人应用
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7ibzdxibLECNf4hrIyzn2C8TXnKm2w7zsfL7I2J3y57YibJOZGpsNmmDgg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)
2. 创建流程，我这里创建了两个流程，1个专门收集AI Coding的资讯，1个收集其他AI资讯。 流程是通过webhook写入多维表格。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7cDpWLcDcInmGiaE6mFfcZB0emiaYWib3yvB00IjhBY03I96RxAqUA7KeA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

webhook触发：定义传入的参数，将来在coze工作流中要传对应的参数进来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7G8D075picGo503vRwuWYlNicjrfWjicpAibC3O4cMkRiaVDib5LTeiahtvHyw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

写入多维表：选择正确的表，前一个阶段传入的参数写入对应的多维表格列。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7eFJwBmGdwCG7OTlQl3yOj8gl5xgJpibprmQPerpBhCDsCBE3hAXSq8Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

## 在coze中创建智能体

https://www.coze.cn/

1 创建智能体

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh752OrCJfPhBMqsAlA0nk6wniaicz2NShdrXHHTFHicicvTQGDHVibHmUjgSg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

2 设置提示词，创建并添加工作流

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7iaYg1fKBK4d9JYicOrh0eyagsYf5KzqlXTEGYa8asKqcD75XwevzQhXQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

3 创建工作流

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7f9rQRRPWOQs3ibqpWj2cIvbLLPmEdbPbnyQzichntHoqmhtjvPZ5ceNA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

使用LinkReaderPlugin获取链接的url，标题，及内容等信息。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7UREanf63JZq741sgYElSeLUXvPRbbqy45QaRN11HLtrgFNksSnntJA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

使用大模型进行内容总结

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7f6D1r0eSJ3ibGK7ctsYsoTcvRib7bkpLRgjC64SqmricJyPCYfdmuAw5g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

意图识别，我这边将AI资讯分成了AI编程相关和其他AI资讯两大类，分别写到不同的表里（大家可以根据情况定制）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7ftwXM91suDXfaW3pnOSia3adrnWhZQia5I7zvP1IcCib5Xr8IFuUnSOOw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

使用HTTP请求组件，将URL，摘要，标题通过之前的webhook地址写入多维表，这里的HTTP链接就是第二步飞书机器人应用中的webhook地址。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7iaK6QVtdH18HvOmcTictYXcVq5ZreZ5cF2GhIGzWvDK7KRIpeic2ia3D1w/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

4 最后发布到豆包或飞书

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh72dichXM9QlibpBgtBklkAkycic7LbLJnsibXW5yOxicENeAV1FY79eUbuKA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13)

## 使用智能体

发布成功后，在豆包就可以看到发布的智能体了，可以将需要收藏的URL发给智能体

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7pXbvC61dmmMd9R7kUrWsS8Jz8iaTWNo7PQUNFCDgyribqunHkjmKkrRg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

或者在飞书中找到智能体机器人，进行对话

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh78Wr6V4pDA4KAbn07Ct8NvYwj1IoCjy0IqUk2T5JIgAK0vryUia6cbtg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

查看多维表格，已经成功写入

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6nvxptpA29yVxKGHgiclZRy3WlvHgcgh7qia00dhWoggHIzw12w1hwWDpKuYpBoXzpqx9tGyCEmAcehhVsT34sdA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

## 参考资料

1. https://x.com/vista8/status/1890017517688725970
2. https://juejin.cn/post/7405476511186927667
