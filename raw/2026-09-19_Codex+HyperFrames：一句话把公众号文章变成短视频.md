# Codex + HyperFrames：一句话把公众号文章变成短视频

**作者**: 大瑜

**来源**: https://mp.weixin.qq.com/s/vCoKBDUnuFb0Zn5AscJz_A

---

## 摘要

文章介绍了借助Codex和HyperFrames将公众号文章一键转为短视频的工作流：先在Codex中安装HyperFrames插件，订阅用户可直接安装，第三方API用户发送提示词即可；再利用skill下载公众号文章并提炼核心观点；然后通过提示词让HyperFrames自动生成适配视频号、抖音等平台的9:16竖版、15-30秒短视频，包含脚本、分镜和预览；最后用MiniMax替代其自带功能生成更优质。

---

## 正文

大瑜 大瑜

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3z0Fj216Du4lcZxgCy49PpMCPGtzOmskhEhicHYMwlgpat2QleArJyv3IxQWbEvSGYw0SD2z24Q3fnib5UXCk8ibaapNkmGTH1Azg/640?wx_fmt=png&from=appmsg)

不会剪视频，能不能讲公众号文章转为短视频？

说实在话，要是以前，确实比较麻烦。不懂：脚本、分镜、剪辑等，大多人都劝退了。

但是今时不同往日，现在就不用那么那么折腾了。

今天大瑜就演示一个简单的工作流：codex+HyperFrames ，它可以快速把网页、文字、图片、声音做成视频。

## 第一步：安装hyperframe

如果你是codex的订阅用户，直接去“插件”哪里找到hyperframe安装即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3zZ2QRSgRktx7FqfzBibTRCNfvjiaJcfrNPW6XfJo1h39WaSff1R9bbEN9wFD5YMe3I2Z2MmibU7eARzAIicJZnVNJpTy7RZ8iaukGQ/640?wx_fmt=png&from=appmsg)

但是譬如你用的第三方api，如deepseek之类的，直接讲下面的提示词发给codex就行。

Mac 复制下面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3x84DI2H9mbhfKD9jWbrMBc6hF7t3xibURSXpqwrTGh2ZaeBh5YmIs0LtDWvbFlYjJ9GVQHWhLnhxW6Y4JctV6SlEPWwBkNVnnk/640?wx_fmt=png&from=appmsg)

win复制下面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3wLUVTtT63DGmybCh3WClUydObom2BibrQqj6Df4GVltBoXUg3ys8GHh7l58Q0xwTCI8277v3ybNibcnRsjdj6NwL6dLYx4M9ZdU/640?wx_fmt=png&from=appmsg)

## 第二步：提炼公众号文章

很多人无法将公众号的内容下载下来，这里我们用到一个下载公众号md的skill，当然也是大瑜写的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3xefkJ93uFgxmvIKe17Yia04CiaXBQ5mSt52c42ZBiaKFPKx5aeRqQrPKqqeWnicLLiaEHJoia51hBvBAGtEK0OY7qiciclJ2EXFcBHhWk/640?wx_fmt=png&from=appmsg)

只需要将下面的提示词发给codex就行。

```
读取公众号文章：XXXXXX，
用https://clawhub.ai/harven-droid/skills/wechat-article-archive这个skill 
来下载公众号文章。
要求：
1. 判断这篇文章适合做成什么类型的短视频
2. 提炼出这篇文章核心观点
3. 找出适合放进视频的 3-5 个重点
4. 不要编造文章里没有的信息
5. 保存到文章提炼.md
```

不一会儿，这个提炼内容就出现了。

![](https://mmbiz.qpic.cn/mmbiz_png/aVawKBqlw3wbeibLMns7W9k7CEaRmaQttSK8b1fh0IW2fp0GRn7BzgYMLqny8cCiaBt1Gdb2d7JzJ4KZuFibXPCJ6tibneaiamyg2B7JtApbAR4Q/640?wx_fmt=png&from=appmsg)

## 第三步：一键生成文章视频

```
请使用 HyperFrames，根据公众号提取的内容以及文章提炼，生成视频。

要求：
1. 9:16 竖版
2. 15-30 秒
3. 适合视频号、抖音、小红书
4. 文字短
5. 画面清楚
6. 不要编造文章里没有的信息
7. 自动生成脚本和分镜
8. 先生成 preview，不要直接导出最终版
9. 生成配音

请把过程文件保存到script文件夹下。
```

## 第四步：生成配音文件

其实hyperframe自带生成配音的功能，但是这个玩意配音太垃圾，我们怎么处理呢？

大瑜交给你们一招，用minmax的生成语音的能力。

先给codex说：

```
将逐字稿发给我。
```

我一般选择这个语音，还不错。中文识别也很高。地址如下：

https://www.minimaxi.com/audio/text-to-speech

每月，用户有免费的额度可以下载，下载后将语音发给codex，重新生成即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3wdMjUyagGWMBGyaxLRc9ibJAxEibZ93n6ScUekFmXJh10osreiap693EqETUicemJ1VUhVvH7EPHBOu29tnh2V9wXZfryqRWz4VMo/640?wx_fmt=png&from=appmsg)

## 第五步：哪里不完整该哪里

这个时候，你的界面会出现一个预览的视频，供你预览发现问题。

![](https://mmbiz.qpic.cn/mmbiz_png/aVawKBqlw3wXlKbLvrib65ZFjA2C5HxPIjrusPf1sb71ru5TUKKYcqtWHPY82Zl62WvhibNolfo1ABvd09CCn29D7LBRBoiahGyLTibu91ex5Ng/640?wx_fmt=png&from=appmsg)

你可以让它添加封面，添加动画，配音和文字匹配等问题，只需要发给codex不断调整即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aVawKBqlw3y9IbBLXaTcFIFWolFpgZutcPw1DVM6z61Fb6F2Iib0oOkZCf1SlVRSzuVykzBCv0HBzkcmH6WyYgUn4ibw1flkziawOBqRicTDcOw/640?wx_fmt=png&from=appmsg)

当然，你可能担心语音和文字画面不匹配的问题，放心hyperframe也会帮你调整。

## 写在后面的话

简单五个步骤，就将之前复杂的内容给搞完了，如果你也想讲你的文章转化为视频，那么可以试一试啦。

历史文章：

[最近几周用 Codex，我踩到了这 6 个坑](https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247491923&idx=1&sn=f576edfcb094277081d4b7ad5bdb1251&scene=21#wechat_redirect)

[Codex + Obsidian 火了：公众号文章怎么一键保存到知识库？](https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247491913&idx=1&sn=51846c8e78f15bd2c4e959821f4cb96d&scene=21#wechat_redirect)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过