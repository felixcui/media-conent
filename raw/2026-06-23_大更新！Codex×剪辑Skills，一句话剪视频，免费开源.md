# 大更新！Codex × 剪辑Skills，一句话剪视频，免费开源

**作者**: 成峰

**来源**: https://mp.weixin.qq.com/s/elM9M7UbspSt9RhQUIUPog

---

## 摘要

本文介绍了一款免费开源的剪辑Skills（chengfeng-videocut-skills）的大版本更新，该工具接入了Codex并增加了复杂动画效果，已成功产出多条千赞视频。用户只需在Claude Code或Codex中安装该Skills，然后将口播视频和文字稿交给Agent，即可通过简单指令自动完成视频剪辑与字幕生成，实现一句话剪视频，大幅简化了视频制作流程。

---

## 正文

成峰 成峰

在小说阅读器读本章

去阅读

我之前做过一个 2000+ Star 的剪辑 Skills。

![开源背书](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2ZjkupxzYFTM12DqCDnPhuWC50td3Sp7bmJDVXTAPbjsIVM14S3mibcLI6d7ML4OgWrNUB95hrsfwQkFsIx2UbXIiazFxqY8jPlnYFutQ/640?wx_fmt=png&from=appmsg)

这次接上 Codex，大升级！加上了复杂的动画效果。  
已经帮我跑出好几条千赞视频。

![千赞视频](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupyhZvMlEI5nB9l4xpcYibjeWq900IjCqXRP2w7tEgGVnOwrlibZpBjGJPaicPAwAWSxzgpLSKKJuJnu7SR6ibEObEib5tE9HwaPUAKM/640?wx_fmt=jpeg&from=appmsg)

先看结果：

我近期的视频，都是用这个流程去跑的。

以前做视频，要先打开剪映。

现在装好 Skills，把视频和文字稿丢给 Agent，它就能把整条片子往下跑。

## 我是怎么做的呢？

## 1.让 Agent 安装剪辑 Skills

打开 Claude Code 或 Codex，发给他这个提示词：

> 帮我安装或更新 `chengfeng-videocut-skills` 这个剪辑 Skills。
> 
> 安装命令是 `npx chengfeng-videocut-skills install` 。

Agent 会先跟你确认，然后自己去跑安装。装好以后，本地就能调用这套剪辑 Skills。

这套skills，我把所有的经验，都放到里面了。

安装好了以后，效果如下图：

![安装完成](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2ZjkupyJQq6piciabmWcEjLKL1c0pZibCia5z74ibnq9lTH8VftVNibVwtVWU1EjfCDWRd8BJpmx5kmWyKoUX5USa9nAN5jgAzYzCoPib0H5ia0/640?wx_fmt=png&from=appmsg)

## 2.生成剪后视频和字幕

第二步，先把原始口播整理成基础素材包。

![基础素材包生成](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2ZjkupyOCr21bsMzeJ2WbdAF6xiaQhGZ7x53MUibicXkoZRZrMUZNqupXKPnMlepqUpNdkE9CWgariaib0cU3XPGA16Zbxz3LjI4AkGbYO10/640?wx_fmt=jpeg&from=appmsg)

我们把口播视频和文字稿交给 `剪口播` Skills，就能拿到剪后视频和字幕文件。

下面具体看怎么做。

口播视频不用复杂录。我一般直接对着文字稿念一遍。

![录口播](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupyPMTvzibviasg2bseNJTFibpFKlYfGD2UH1jL5eaIeZLXzR86s28SvGGWxYeF4Te6P9DxlDFjJ2lC2otM1FtY7taibBHSXfclZfmE/640?wx_fmt=jpeg&from=appmsg)

如果中间涉及到具体操作，就切换画面，把操作过程录进去。

![录操作](https://mmbiz.qpic.cn/mmbiz_png/7e6H2ZjkupzuibuASR2jgJF4oDOH6tS3JJvQn28rPd1AZ814AcjqCLWT7Fmqyxy8iaK4gYz5JibZbp1jXUpw5mt9ibxGicF0iahbKWyicrnf3icstFE/640?wx_fmt=png&from=appmsg)

这些都准备好以后，就可以交给 `剪口播` Skill。

直接在项目里输入斜杠命令：

```
/剪口播  + 视频地址 + 口播稿地址
```

它会开始处理你给它的视频和文字稿。

![唤醒剪口播](https://mmbiz.qpic.cn/mmbiz_png/7e6H2Zjkupzgj2VVCYshDFkOHuHjjHL9uRibfpOUYtQja9Io5d2ktY38oSqsvZLPDCm259InDJFTIg4ftg9I2FXuNxaOBoSSE0n5NC4icF74Q/640?wx_fmt=png&from=appmsg)

接到命令后，Agent 会先生成审核页。

![审核页](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupxC0U0NP6vQZXYEWowicaXjpBDSeNDfiaXrv9s5urEzm8k9p0AvhBpnKicdqIsF0ibKZ4KXXGoNUV5FaV8yWBbFEUpibGb2fkmjH0sk/640?wx_fmt=jpeg&from=appmsg)

Agent 会把停顿、口误、重说先整理出来。我要做的，就是确认这些删除项是否对。

确认没问题后，我点“执行剪辑”。

这一步跑完后，Agent 直接输出“剪后视频”和“字幕文件”。

![剪辑输出](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2ZjkupztsiaXCvYSbsE6BNPibCaibHcGdZhoAru3p204CyV50zOj3jiceLBPDrQfISvtDt5OtIEZaeaTZD5rvA2nuPLCGicoAbB5cIjM53Mk/640?wx_fmt=png&from=appmsg)

得到的字幕，和剪后视频，在时间上是对齐的。

到这里，基础素材包就准备好了：

```
剪后口播视频
对齐字幕文件
```

## 3.按字幕生成分镜页面

素材包准备好以后，在项目里输入斜杠命令，唤醒这个 Skill：

```
/口播成片
```
![唤醒口播成片](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2ZjkupxBaXoR5K8QamosZuDVq5EjliaeIFNEH18oYoSQGpwic0qLTtISicPt7YYictnJWic6lgbeP4Bmib8tibp1w1IDq2rRpT5w28rUMY0Nfs/640?wx_fmt=png&from=appmsg)

Agent 生成一个 HTML 分镜核对页。

如下图：

![分镜核对页](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2Zjkupxw9COfDG5Jeks0Vs1VdzibwfSzzxsh3WM5LvoonjUO2wZRYzH2sZoD8XOgoMlIE1pVvlombf8JVBAfKjVapobibOibtbGza3pZDo/640?wx_fmt=jpeg&from=appmsg)

左边是 Agent 生成的画面，右边是字幕、画面任务、素材来源和镜头动作。

这个 Skill 在分镜页里实际做三件事：

![分镜页面生成逻辑](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2Zjkupxt8JA43mu5ic7mRmfHdlNdcOcgxVWv82Sgia3W4356mAyn33VwshN4FYoDxohGkISEDicLQdWPLhPLFf7CgG7uficicVpwKErkHluw/640?wx_fmt=jpeg&from=appmsg)

它会先按字幕时间轴拆段，再根据每一段内容选择画面来源。

每一句话，到底保留原视频，还是换成截图、产品页面、结果页，或者做一个 HTML 动画，Agent 都会在这里一步处理掉。

如果这一段讲的是录屏操作，Agent 就会保留原视频片段。下面这个画面，就是保留原视频里的页面效果。

![保留原视频](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupyVGJW9QE8Ia1Qs4lvyZRfbg7tsqdSkQmZ1x1xM5J4M3UvTAicLXNFI6jMRDydwpIjUiaXtB8HLdpmIBice85skHpibbAxEDFCvIkY/640?wx_fmt=jpeg&from=appmsg)

如果这一段更适合用截图、产品页面或结果页来解释，Agent 就会切到对应素材。比如下面这个页面，直接展示了 Agent 的回答。

![展示素材](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2Zjkupy4DYxILXaNBfoULMCkCIJK1vXGpVvFQU78lreac3B8mR8VLHudZZWacS7iaQuicswJzWYmFnvEca4J14Ma3ovl6sNVdsDxzic1yI/640?wx_fmt=png&from=appmsg)

在前面的两个素材基础之上，它还可以做非常丰富的动画。比如下面的这一个动画，就是背后有一张素材图，我又让他在这个素材图上，去画了一些动画。

![手绘动画](https://mmbiz.qpic.cn/sz_mmbiz_gif/7e6H2Zjkupwibb0oLz4wT984HvUcS7eurWsxNq1KYyOvXQTOCofu6sJD2Hkyt2TXXUBpicCumLv1T6gKKmRKOnBFOUpaL6OicqmV5fXZqOycvs/640?wx_fmt=gif&from=appmsg)

我试了几个动画方案，现在用下来 rough.js 效果最好。

它画逻辑图和标注比较顺手，圈重点、画箭头的效果也更接近手绘批注。

如果某一段不满意，直接告诉 Codex 第几段哪里不对。改起来也非常快。

比如直接说：

```
05 这一段动画改一下。
箭头指向标题，圈出右侧结果。
```

Codex 的 Computer Use 可以打开这个页面，看左边画面和右边口播，再回去改 HTML 画面或标注。这个更自动化。

我的动作从“自己排分镜”，变成“看分镜，提修改一键”。

## 4.检查时间线预览

分镜页面确认后，就可以进入预览。

继续说：

![进入预览](https://mmbiz.qpic.cn/mmbiz_png/7e6H2ZjkupyZia8blmdbIgcJ90UVuOahdo67CXM21bBeJTkUIeIgv0aCNfReSWA6zRWTMQ8nxIFA2y6490Smtib1r4Ig0cf3bpomiafibbQeDWs/640?wx_fmt=png&from=appmsg)

然后 Agent 就会给出来一个预览页面。

左边是视频预览；底部是进度条，附带文字说明；右边展示口播内容。

![时间线预览](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupzicZXNxNAeEzhxFrwcNaqTw9ibgDibCjLAsHSanGTqwR9dlmGdrYJCtAKCOQshq5ZZM5eUmfZXMPozuCJDgqBTia9ET49oqVWvO00/640?wx_fmt=jpeg&from=appmsg)

时间线预览会按字幕时间点排动画。字幕说到哪里，动画就出现在哪里，这比自己在剪辑软件里对时间线省很多事。

![动画对齐](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7e6H2ZjkupxPFfqPqvZibxFQKEBAEHeb80BlWLib8bWOI2GSsAU2UCIhxQ2KOGLFmb7SDKzuxv3uSC50iaicbX3OjLbM1J1W6BwMeOpEMwQ8sAE/640?wx_fmt=jpeg&from=appmsg)

这里看的是“这些画面放回整条视频以后，出现得对不对”。

如果视频出错，比如：

```
画面没有提前出现
原视频被误换成 HTML
截图用错
文字挡住画面
节奏不是跟着口播走
```

反馈不用写长文，直接按片段说：

> 01保留原视频。
> 
> 02图出现太早
> 
> 03画面太满，删掉下面两行字。

这一步确认以后，才进入最终合成。

## 5.合成 MP4

前面的这个视频预览确认了以后，我们就可以让它合成了。

![开始合成](https://mmbiz.qpic.cn/sz_mmbiz_png/7e6H2Zjkupx4QGsTFonr7VwTORzGnP9F456NB48F2AMiboZuJ9qtrnUlM5kJRHLTKIhkLbmibqHZAQibeKmZfDWju9IVgcOzIaGoBcmhzWjuVE/640?wx_fmt=png&from=appmsg)

Agent 会用 HyperFrames 负责把它变成可以渲染的视频动画工程。

![HyperFrames工程](https://mmbiz.qpic.cn/mmbiz_png/7e6H2ZjkupwUQ1yEfU7h6u2Rnr4BSOUGjlRkR7ZBhxTBBPEOhukKiaXMtmjfUvLs3s8tOkbLibyj48Ft05773NWZmy4rlw2FCpfE9BdBia5e74/640?wx_fmt=png&from=appmsg)

HyperFrames 对 Agent 很友好，因为它可以把 HTML 动画变成视频。只要画面能用 HTML 做出来，就能进入这条合成流程。

过几分钟我们就可以看到最后的动画了。

导入字幕和视频到剪辑工具里面，检查一下有没有一些细节有错。

![最终检查](https://mmbiz.qpic.cn/mmbiz_jpg/7e6H2ZjkupyuFxz2kyPD0ZCmKkwmWCIhg64n8jWUxBzibDdJdPopibKqEOJ2ic0ldH7x9neFu9WoRnZ2AicK1wVnicmPpx5ysE8vzZuziaolC8plg/640?wx_fmt=jpeg&from=appmsg)

## 剪辑Agent，正在逐步替代传统剪辑

以前，视频生产围绕时间线展开。

现在，视频生产开始围绕工作流展开。

剪辑 Agent 正在替代传统剪辑里的操作层，把视频生产变成一条可以持续复用的自动化流程。

继续滑动看下一个

AI产品自由

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过