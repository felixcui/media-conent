# DeepSeek Bot开源：一句话，让AI自己组队干活

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/P6qlVfBHMNHOZi0pAJeBow

---

## 摘要

社区开发者基于DeepSeek Harness推出开源项目DeepSeek Bot，通过持久化bot实现多AI协作。用户可用自己的API Key创建具有独立上下文和记忆的专属bot，由主Bot Chief负责组队、建群聊和分配任务。群聊中设管理员协调多bot响应以平衡协作与成本，支持独立配置模型和用量统计。项目复用DSH模型配置，提供桌面和Web安装方式，数据存于本地，卸载不删除。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

DeepSeek Bot（ds bot）来了。基于DeepSeek Harness（DSH）打造，注意该项目不是官方，而是由社区开发者创建，该项目可以说是有着grokbot的皮，长着dsh的心。

它的核心能力：把DSH变成一组持久化的bot。用你自己的API Key，创建专属bot，聊天、写代码、干活都行。每个bot都有独立上下文和记忆，可以在一个窗口里持续工作，不用反复交代背景。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJibSWDs3jY1zO6Z0O1ib0S0QFcC5EHHVxRQZUdrVQGckibLLoJyiccUzWrx0NwITTiasgqmV2Yvh7u10woWSYI2I3XTvx5eFaTDp5Ss/640?wx_fmt=jpeg)

## 主Bot负责组队

ds bot预设了一个主Bot，叫Chief。权限很大：管理其他bot，建群聊，分配任务。第一次打开ds bot，直接跟Chief说你想干什么，它会帮你把bot团队搭建好。

实际用起来，Chief会先自我介绍，然后根据你的需求创建群聊，把对应的bot拉进来：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJibrQwNxgbvSxg0fKdblrUEsZ09I9ed9HOsTicwNK2pfnUrHssQlAUZ3xuMuFAGF4rhIj5Kmf0tOyeRU4Nr1dJJPkvIhKm9gOdNA/640?wx_fmt=jpeg)

每个bot可以独立配置模型。想换随时换，但开发者建议一个bot长期固定一个模型，只在确实需要时才切换。Bot详情页可以查看模型、记忆、用量：

![Bot详情页](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ9CM6MbYbic0Ypz1MZTDkctzkeVSbEDlaCgVIe0Thl6sYha6hDrDcQBTuYBemO79Gm4dowA9HRWSY8uroACF6ziaxVNTlhvmjXlg/640?wx_fmt=png&from=appmsg)

## 群聊：让bot互相配合

群聊是多bot协作的主要方式。多个bot同时响应，token消耗不低。ds bot的优化是：每个群聊设一个管理员，默认只由管理员回复你的消息，由它判断该调用哪些bot。也可以直接@指定bot，让它直接回答。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJib8KNngOiblACIv8IXWNYqt8cMCYiczBFictf4eKTDOBxjPibdiczlrto9SYnYB33cUqKLPCajTjyt6otc9ZN9muiakm1WR6420fpQw0/640?wx_fmt=jpeg)

这个机制能在多bot协作和成本之间找到平衡。用量统计在Settings → Usage里，按时间、bot、模型三个维度展示：

![用量统计](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJicQxh0G9U0hOsHCeuribhx5OR5n3yibiaTSViavbSpLQUX51mqma1QzEnzx6iaVopzh5T0vIsheGEtW3EVNmgONt6hQoWEJSh7UFkGo/640?wx_fmt=png&from=appmsg)

## 安装方式

前提是装好DSH并配置至少一个模型。ds bot直接复用DSH里的模型配置。

DSH Desktop（Windows/macOS）：

1. 侧边栏进入Plugins → Add plugin
2. 包名填ds-bot，国内网络建议把Registry切到大陆镜像
3. 安装并启用，按提示重启DSH

DSH Web（Windows/macOS/Linux）需要Node.js 22.19+和pnpm：

```
npx @deepseek-ai/dsh@0.2.1-alpha.1 plugin --profile web add ds-bot
npx @deepseek-ai/dsh@0.2.1-alpha.1 web
```

## 数据都在本地

所有数据保存在DSH目录（默认~/.dsh）下的bot/和sessions/里。卸载插件不会删除数据。

## 兼容性与规划

作者测试了一批DSH插件，包括dsh-web-ui-all、dsh-browser、dsh-ads以及多款记忆插件，大部分表现正常。已知问题：dsh-web-ui-all在macOS上会导致下次启动失败；dsh-ads是占位包。

下一步规划：浏览器操控已经确定在下一版做，电脑操控还在考虑权限设计。开发者表示接下来会开源更多开发中用到的技巧、方法，以及他的思考和取舍。未来还计划支持接入本地agent，直接使用已有的AI订阅。

再次说明此为社区开发者的个人兴趣项目，并非官方推出，结合dsh本身尚处于起步阶段，该项目距离成熟还有很长的距离。

项目地址：https://github.com/FeiZhuLulu/DeepSeek-Bot

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过