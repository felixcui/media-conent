# 我用 WorkBuddy 做了个微信小程序，从开发到上线，全程拆给你看

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/ybllrlUNTGTEeMz4g_Uhag

---

## 摘要

文章介绍了如何用WorkBuddy 5.6.1及以上版本，从零开发并上线一款微信小程序。作者以待办清单为例，演示了工具准备、需求描述、卡片预览等核心流程，强调无需小程序账号、开发者工具或API key，非技术用户也能通过自然语言驱动AI完成开发。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyTECclicXknpvib5ovpuoib10fdhIXfIUVFc5Is5UH7GqS6bvWc64bc9APStskiaH3Xa6Cv89trt31njWlYBgxqyUicv2T1C5lwNmHU/640?wx_fmt=png&from=appmsg)

AI Coding 可以说是AI时代每个人都应该掌握的一种能力。

这是一种原技能，掌握它以后，可以用来创建各种各样的工具，去解决具体的问题。并且AI 在编程这块的能力越来越强大，上手门槛大大降低，非技术同学也能靠自然语言驱动Agent，把应用做出来。

之前我最推荐新手从开发web应用开始，其次才是小程序和APP，因为web最简单，环境和工具依赖最少。

但最近Workbuddy在新版中已经支持在应用内开发、预览并发布微信小程序了，直接把微信小程序开发流程整合了进来，进一步降低了微信小程序的开发门槛。

今天这篇文章，我手把手带大家用Workbuddy开发一款微信小程序。

接下来我会使用"待办事项"这个简单的案例来进行说明，介绍在 WorkBuddy 里面完成微信小程序核心开发流程的具体步骤。

## 工具准备

你需要的工具只有两样：

1. WorkBuddy，版本需要5.6.1及以上。官网workbuddy.cn有Windows和Mac版，装好登录就行；
2. 一个微信账号。

暂时不需要：小程序账号（可以先用试用版）、微信开发者工具、AppID、服务器，以及任何一家大模型型的API key。

## 描述需求

打开Workbuddy，新建任务，切换到代码开发模式，选择小程序，点一下它就会出现在输入框里，上面还有活动报名、社区团购、门店预约、餐饮点单几个现成的例子可以点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQDFvaicZnIYr87zgHJoZ3s25WjTU3dSXibriciacg0AO91dokDz9icTQ3x6icIE7iczChflLMXkztrCdq9hArQC2mrQTI9InYYBiaJDdk/640?wx_fmt=webp&from=appmsg)

你也可以直接在对话框里说「帮我做一个XX微信小程序」，记得把「微信小程序」这几个字写上，不然它可能给你做成网页。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRLQBkQMbhdksSTl1yCfx9GDtkpLiaSEPjCtJWmstgAaFI5EzVEFNQAVBtlwMX8qwriahkSqWI9xHwSMbM6wFzES1CluldicSJics8/640?wx_fmt=webp&from=appmsg)

然后选择一个本地文件夹作为项目目录，注意不要选择C盘，因为生成的代码文件都会放在这个目录里面，可能会持续变大，挤占C盘资源空间。另外把权限设置为允许完全访问，不然你得频繁的点击允许；模型这里选择GLM5.3，用好一点模型，会帮你少走一些弯路，你要相信贵有贵的道理。

完成这些基本设置，下面我们继续看需求应该如何描述。

由于待办清单这个功能非常明确，并且模型接受了大量的训练，我们只需要告诉它做一个待办清单小程序，它完全可以自己去决定做哪些功能。

简单描述：

> 帮我生成一个待办清单微信小程序

如果你想详细描述需求，可以使用计划模式先和 AI 去对齐，然后再让Workbuddy执行。

详细描述：

> 做一个单人使用的待办清单小程序：1）可以新增待办；2）点击待办标记完成，完成后自动移入“已完成”区域，这个区域默认折叠；3）已完成的事项可以恢复成未完成；4）删除是独立操作，需要二次确认，避免误删；5）不需要登录和多人协作。

是简单描述还是详细描述，可以根据我们自己的需求清晰度、复杂度进行选择。

**重点是，把核心功能说清楚、界面长啥样、怎么交互、数据存哪里、约束条件是什么、以及验收标准定义清楚** 。

## 卡片预览

任务执行完成后，底部会出现一个小程序卡片，点击卡片就可以在右侧看到手机样子的预览效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRrrx79XpAicS8cPp6tAvibU5AibDjgGC0Wia57NrTaPtItSoiaBF2UW7vzBg3VsG6mxywwBx85awqGE7MCb3yBiaBYlyXnUMO6VwqV0/640?wx_fmt=webp&from=appmsg)

如果没有出现这个小程序卡片，并让你用微信开发者工具打开，这说明它没有按照Workbuddy托管的方式进行开发，这时候可以直接在对话框里告诉它：

> 使用Workbuddy托管链路进行小程序开发

通过预览，我们可以在应用内即时看到小程序页面长什么样，验证交互逻辑是否正确。这里重点验收几个功能是否正确：

- 新增待办
- 标记该待办事项完成
- 进行中、已完成正常切换
- 已完成的待办可以恢复到进行中
- 删除需要二次确认

如果有功能修改，完成后，点击「刷新预览」就能看到最新的效果。

不过需要注意的是，这个预览是H5的效果，不是真实手机打开小程序的效果。 **底下也写着「预览仅做参考，可发布后扫码查看真实效果」。** 这里有对应的解决办法，在后文会进一步介绍。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRpEbVpPYyIAoUsOFtxvQc23DibotdG4bxrOTvdCDWTHk1FLsoSn6ndHib4AOXEwJNu0qkiaKIaLSXic0NuwFjicNoiaqMxG2azlYNYw/640?wx_fmt=webp&from=appmsg)

## 预览发布

小程序功能开发完成后，点击右侧边栏分享按钮，就进入发布流程。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySqAfnX4N5gB1X0xnXubDX4E6lHtIcW1zdC2iam2NzzTJhK4yF1LDrL1KC4SMuiaI1wAibTkb7JpP3BYPAwhW0w7G28lSmiaRR2zz0/640?wx_fmt=webp&from=appmsg)

这时候，它会弹出如下弹窗，让你选择是绑定已有小程序账号还是用试用版小程序。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQ8x8hic0PulX1HUicgo6qUFjk2Um4We5CZhm9UpWI3uGpPsGbicrj6GynlLGUgqoLnN5xrlPQ4KM8ibtpKFIADOqfaibz0hyvAeWXg/640?wx_fmt=webp&from=appmsg)

如果你已经在微信公众平台创建了微信小程序账号，可以直接选择方式一，扫码完成绑定后，就可以发布体验版本做真机测试了。

如果暂时没有小程序账号，就没办法绑定，但可以选择方式二，先创建14天试用版，快速验证功能。不过一旦创建了试用版，它就再也没办法绑定小程序账号了，目前不支持试用版直接转换为正式版。

因此，如果打算长期运营的话，一定要先去微信公众平台注册一个自己的小程序账号并绑定。

注册也很简单：打开微信公众平台，在账号分类这里选择小程序，然后按照流程填写相关信息就能完成注册。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySibLsl5MQ7iaN6mQNHftVTqHnQ8uIYS5GwuL6uYtKj5SRcclBqLOFpB0G36rlxThHABa95ecyEaNaicsgvfds8hhQEMzq530akibU/640?wx_fmt=webp&from=appmsg)

注册完成后，用微信扫码完成绑定。这里扫码绑定相当于把小程序账号授权给Workbuddy进行托管，它有权限上传代码进行发布。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRe9eibPzEmegDaKXJRwyic6T4k04Wibf8lecUvwMfEgPIpUtSSNfibVH553djGYqLXsm7QibzEobDVibianzcrV1B0mnVcsHlYnV5sGQ/640?wx_fmt=webp&from=appmsg)

绑定完成后，我们就可以直接在Workbuddy中完成小程序体验版、正式版的发布了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTW913AS3ic6RWic9GcRvMwlgKicebb9eUQiccjFmCaIic4j55gWxztZ0SFoBqba96uhOod0icJgheY2Z4D4kT0hfeic2IamdBWmfspNU/640?wx_fmt=webp&from=appmsg)

这里我先发布体验版本，会得到一个体验版的二维码，手机扫码就可以真机预览小程序了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyS9YOMBCKdJZicbDPbEoYvURX2v7z8Kc2X0QGFpbK3M0icss3xedexa9KXLl13JusnlkzLXTbRVxjVtASRuxIiaKE7nicJaF7EfImA/640?wx_fmt=webp&from=appmsg)

体验版本测试没有问题后，就可以发布正式版本，提交之后，需要等待微信公众平台官方审核，一般情况下，快的话1-2小时即可通过，慢的话一天内会有结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTLHMGJYbAIQFaNUvQvx6058iauDVSTAOkriaSrPex1PrC4tNIaeF8gKqHrChqtibrehLAqexNCL8xrYYk1A4v1HlO6H6SkjNcQGQ/640?wx_fmt=webp&from=appmsg)

官方审核完成后，手机微信会收到公众平台审核结果通知。

如果通过，小程序就自动发布上线了，其它人就能使用我们的小程序了。在这里我们可以看到状态变成了已发布，并生成了一个正式版本的访问二维码。

这里要注意的是，在Workbuddy中发布正式版本有次数限制，每周最多三次。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRtmpBTMicVej3YNgkqXfvp1ibs3rezyraXTe16jwZLtfNObFV5sI1BVH0ziaRrvjVvfHxKTE0iaica7ER8a1ichJP8H3IWqBIqNF3VM/640?wx_fmt=webp&from=appmsg)

## 需求迭代

前面初版实现的功能非常简单，数据是保存在本地的，这就有一个弊端，如果我换了设备使用，之前记录的数据都不见了。

现在我希望能在多端同步使用，这就需要把数据存到云端，存在云端还需要做身份识别，得知道这条数据是哪一个用户的，所以我们还要增加登录功能。

需求提示词如下：

> 现在数据是保存在本地的，一旦换了设备数据就不见了，我希望能在多端使用，把数据存在云端，并支持登录功能

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyR4GJHJoBicibozcRMar3sFSOcHKa01E4TaKNUdcTgPFG0MXZNEAI7cbouufXKVicnXEqNgdMZib9pPRfaDL2mhzs1uwUiaN8icicc5x0/640?wx_fmt=webp&from=appmsg)

这时候会让我们选择是否开启云服务，选择开启。

这里的云服务是Workbuddy提供好的，它支持按需接入云数据库、登录认证、文件存储、AI调用等云服务，对于新手而言是很省事的，不需要我们自己去搞服务器环境或者开通任何服务。

接入云服务后，数据就可以长期保存在云端，用户可以登录自己的账号，图片和附件也能在线上传；有AI需求时，还可以直接调用大模型。

大约10分钟后Workbuddy完成了开发任务，在右侧面板点击一键登录，会出现无法操作的提示。因为这里是H5预览环境，微信登录需要在真机上操作。因此我们需要把最新的功能发布为体验版本，然后用真机测试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTVmMggky1roIjqWzLFHQicrE7ibiaLFgkicwEcOC6dt0DsoPn2xB9zAQo9ibtfibzPY386MG6iaaOSul3IibnzRoT2KERS7SwLubeXIicI/640?wx_fmt=webp&from=appmsg)

体验版本的发布流程跟前面介绍的一致，点击右上角分享按钮，勾选体验版本，点击更新即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRs2bibbibbzMciaA9AuHDJMdns2g7SgOv76ZhpiagFLAkSFQibxuYOyzYhzkpzaXT5IBaDeUeACqHDTQjdPjISCmsXJFo72BKC4meo/640?wx_fmt=webp&from=appmsg)

体验版发完成后，扫码体验版二维码就能看到最新的版本了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyR6Ym5GZjonMfUjrDZkFSmTHW51sKl7B7IttZDauq9IuxfZ4LibuQKl1QLdeZH4iaBsdDXz1rlSXW4I9a7PpfTUZuz5icY3sDMLjY/640?wx_fmt=webp&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySXt6SDNLJibf1VV2KbrQlibUuItp8kZBibUTXibfQ1SPomFjMtoGBEicGM6ibgdHKI4t0SyNJpWKSdYbB5AfY8N9FE4mibibWiawWrWOkA/640?wx_fmt=webp&from=appmsg)

<<< 左右滑动见更多 >>>

现在的版本就支持微信一键登录，并且所有的待办数据是保存在云端的，支持多人多设备使用。

为了验证我们的数据是否真正保存到了云端，可以去云服务后台查看数据是否存进来了，点击下图按钮即可进入云服务后台。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRQcRicXobLJ9xk6I5eJzAO2qp2eic1EawXiaUUrvqn7xGc25bIIDmKMJxlh4u7t1qQlzTOzF1nNFssedwWpDCdDm7c0KqYGu7iau4/640?wx_fmt=webp&from=appmsg)

通过下图可以看到，云端数据库存储的数据与界面显示的一致。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRsiaG39qEFKK9G4DiamHBXXmX9QkeMqqHIrwVpBW3cibKR2ZhzPNYqoRY7Mxvtoa3w9vnSsJTRunXK2fonnLvbaTqrEpHaJBZq1g/640?wx_fmt=webp&from=appmsg)

## 发布之后，小程序管理

从账号左下角进入「设置>数据管理>应用」 **，** 在这里可以管理已发布的小程序和网页应用、快速查看对应的云服务、需要调整的话，也能直接跳转到对应的任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRq4wo57uWib77h5H9glaSNAb4SBXXm6xCYdzmeYrkFP6qeoRxMhnuRjicfeIhRxicEbxcbsybiciatRZ7gTLQo31mwF2LDmm9sAb0s/640?wx_fmt=webp&from=appmsg)

小程序上线后的用户访问情况、文件存储等云服务也可以继续在WorkBuddy里查看。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRCWPHfQI31QBJIY5FlqMd9DpnkZCvvp0qr6mAqZVN5zI9j5LLcibrHib2U9rRmxxkFWjgQ4ASJNDqibfzXk4JDcmQavic73TodmzM/640?wx_fmt=webp&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTrtcAf1Vuuw0Ih2L8yVy3F8DYMI9mXUpDxiavA8DUqKNuaabSgzibYq61xy68aP2dN8MYgYfuRs18WquZ1KWibAee9sOrq1Eln98/640?wx_fmt=webp&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySQC1x7AXM45Rg0LibicpxadF6vsjo3S1Koyp3q72yanapZ9QVnyenWqImic17NySMExaAO1hX8Cu6htHtkwoOUKDibiaqEJiaB3aicOA/640?wx_fmt=webp&from=appmsg)

<<< 左右滑动见更多 >>>

**到这里，我们就走完了从需求到上线的完整路径，整个过程除了小程序账号注册、备案需要在微信公众平台操作，其它所有事项，从开发、调试、预览、到发布、云服务都可以在Workbuddy应用内搞定，我们只需要描述我们的需求即可。**

整个开发体验还是很友好的，足够简单、闭环，不需要在多个应用程序之间切来切去。

**但是对于复杂需求这个流程可能就不满足了，核心在于侧边栏预览的是H5环境，而不是真机运行环境，这两套环境是存在很大差异的** 。可能在H5上面可能一切正常，但是运行在真机上就出问题了，比如常见的键盘问题、页面布局问题，还有一些微信相关的功能H5是没法操作的。

那这样开发调试起来就会很麻烦，像前面这个案例的登录功能，我们只支持了微信一键登录，而这个操作在侧边栏是没法执行的，那我们就无法登录进入功能界面。要登录就得发布体验版本，然后用手机打开。

其实这里有更好的方案，那就是用微信开发者工具。

## 开发者工具

这个微信开发者工具是微信官方提供的，专门用于开发调试微信公众号网页、小程序的专业工具，需要大家单独下载安装。它内部模拟了一套微信小程序真实的运行环境，支持大部分微信接口。

安装完成后，打开微信开发者工具，并用自己的微信账号完成登录，并选择小程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySQmlGF0M3C71NIEX9LTEDF4q2TL97K1XMUgYlxC3icOwQBjVkzOstFVib6bphskB7OScn5U5kwOcnaV56XVMHOFbhAtJwPSfhSs/640?wx_fmt=webp&from=appmsg)

这里我们点击右上角的导入按钮，然后选择Workbuddy中小程序项目空间目录，此时需要填入AppID。

这个AppID需要在你注册的公众平台获取，路径：管理-> 开发管理 -> 开发设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyS6QEXgwH2tM81xClOCq34Tb47tedh116ibnEu9iamAu0iavknKcBGN3FoZJyYuRzIy09zcbdx53Obco11PNHfUy08MzVNz7HniaMs/640?wx_fmt=webp&from=appmsg)

填入AppID后，点击创建。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTiaccZY5YN6k219nnF4Z4nqibdhZM6ibtlprTZicfPoGVFdvKrVkTicibkFxS6Z5FE7aSpLjt5qC0lIrSfSUYfx0QT6zXiajPAQODPmY/640?wx_fmt=webp&from=appmsg)

然后在开发者工具中我们就能看到小程序运行起来的效果了，并且在这里可以直接点击微信登录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS9umZLFRzWDZ1PDWx7DYro4iboBgNz2YtrBA1NoKU9icj875dqGcOFk8LnvrDACKiaE9icCWWKrHvZvvdbBva2IaxnewepD9hvicXU/640?wx_fmt=webp&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRiaKeVr7beHCbzqKZpZiaPt3r1GtdXibEzkngTSe459kVyKtBeP1jX2n2zJUPOLlaT4K4kXzKMQMwic39d6e6JXyJGS7Y35XYOyew/640?wx_fmt=webp&from=appmsg)

<<< 左右滑动见更多 >>>

Workbuddy做了任何功能改动，这边也会即时更新为最新的效果，如果没有更新，可以手动点击上方的编译按钮。

更重要的是，在调试小程序过程中，如果遇到功能报错，我们可以在调试面板直接拿到错误日志信息，然后把这个错误信息给Workbuddy，让它进行修复。有了明确的错误信息，比盲目猜测分析能更快的定位到问题的根因。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySU2nreicO8sTibZCNKf2tLFDvFkicn1n1sVUZlL3Y47icnNd9TwHLBt2mv2xer1VNoGPxsKgmMubdmnqszqGiaj9HAc6UA1MsPFQak/640?wx_fmt=webp&from=appmsg)

除了Console面板之外，我们还可以查看网络请求(Network)信息、本地存储(Storage)信息、以及性能分析等，这里就不逐一展开了。

其实，在Workbuddy没有集成微信小程序开发流程之前，如果我们想做一个小程序，就类似上面的流程一样，需要先下载安装微信开发者工具、创建项目，再用 AI 编程工具打开项目写代码，写完在回到微信开发者工具里去预览、测试、上传代码到微信公众平台，要在多个客户端来回切。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySmh7C23RaiaStVqo61DXniax7mTor4dPCpRCleOv5UxiaZDXxNgazmsqF8hFemYyOy3vHbWgyyibv0fg0zbibAGXgCAUias3MnBWPJo/640?wx_fmt=webp&from=appmsg)

## 版本管理

如果我们的小程序打算持续迭代，一定是离不开代码版本管理的， **当然做版本管理我觉得最核心的点是，防止AI把之前做好的功能改坏了还不了原，因此随时做好版本记录，以便可以回退** 。

这里就需要用到Git，这个去可以让Workbuddy帮我们安装。你可以这样跟它说：

> 帮我在本机安装Git，并引导我完成初始化设置

我们只需要提供用户名称和邮箱地址，配置完成后，就可以让他把当前项目初始化为一个git仓库。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRd2RibPr2uX8ebj1XBvQFxbJqao41N9Uplsv4s2DvHgulroowPL9F40icHcgNnUyIY5xcYO505cDoA2bE3Ptk7AIIM91A2k6jXw/640?wx_fmt=webp&from=appmsg)

初始化完成后，它自动帮我们进行了版本提交。

那么后续有任何文件的修改，我希望Workbuddy能自动帮我记录版本，而不是每次都口头交代一次。这里可以利用Workbuddy的记忆规则来完成自动化提交，在当前项目路径下创建`.workbuddy/memory/MEMORY.md` 文件，然后设置如下内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRwewicEq2Rhh3sMHjWsSNauQRVk5ibrM2DdJ2stJFfzaBYdkFCvtJh0MNbvpakpwgoz485RyicShpuPFfibibzuiaO9E6Uz3CZvHO0I/640?wx_fmt=webp&from=appmsg)

如果不想手动创建，也可以直接跟Workbuddy说，让它帮你创建并设置，提示词如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRCtCvuO9c8Trg68n57ic025HwV82O9d4ZnrI2ZNzTbpY1jUI2sM1vAUQib9ouQKgPFaWmlWjQrtBg6C5EsOibJIoj8PustzhG6Eo/640?wx_fmt=webp&from=appmsg)

设置完成后，会话完成后一旦有代码变动，就会自动生成版本记录了。

那怎么查看已经提交了哪些记录呢？最简单的方式就是直接问Workbuddy：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQ7Px8whfiasONbwl473YK3WNGuBG9kk3SRV4dOibhlm9L1y8xqlvqaF0xpNJXXTyWkFUibGnvKrN200eHWI5icL1MBXBO8BsSyp7c/640?wx_fmt=webp&from=appmsg)

这里我们可以看到有两个版本记录，如果我想回到第一次提交的版本，直接跟Workbuddy说：

掌握这些基本操作，基本就够用了，确保能在你电脑本地做好版本记录，以便随时可以回退。只有当你需要多人协作或者多台设备同时编码，才需要把代码提交到远端仓库，比如github、gitee等平台上去。

## 总结

以上就是使用Workbuddy开发微信小程序的完整流程，通过自然语言，就能把自己的想法变成真正可以使用的产品。

当然， **能把小程序做出来，和能把小程序做好，还是两回事** 。

如果只是开发一些功能简单的小工具，WorkBuddy 提供的这一套流程基本就够用了。但如果需求比较复杂，涉及大量交互、业务逻辑和长期迭代，还是需要掌握一些基本的开发知识，知道怎么测试功能、查看错误日志、管理代码版本，以及如何判断 AI 生成的结果是否符合预期。

毕竟 AI Coding 并不是把需求扔给 AI，然后什么都不用管了。 **AI 可以帮我们完成大量具体的开发工作，但做什么、怎么做、做到什么程度，以及最终能不能满足需求，仍然需要我们自己来判断。**

所以，对于非技术同学来说，我的建议是，不要一开始就想着开发多么复杂的产品。

先从自己工作和生活中的一个小需求开始，做一个真正能用的工具，完整经历需求、开发、测试、上线和迭代的过程。

当你亲手把第一个应用做出来，并且真正用起来以后，对 AI Coding 的理解会比看多少教程都更加深刻。

我们训练营 13 期，11 月 3 日发车，有意者看这里： [如何进入 AI 行业？这是我目前最确定的一条学习路线](https://mp.weixin.qq.com/s?__biz=Mzg2MzcyODQ5MQ==&mid=2247500859&idx=1&sn=759cd2dd218a369059793872b016eff2&scene=21#wechat_redirect)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过