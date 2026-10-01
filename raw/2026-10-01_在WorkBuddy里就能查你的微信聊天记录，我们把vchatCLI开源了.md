# 在 WorkBuddy 里就能查你的微信聊天记录，我们把 vchat CLI 开源了

**作者**: 万涂幻象

**来源**: https://mp.weixin.qq.com/s/b3Vu8oODiuA52U5hqOtiHg

---

## 摘要

万涂幻象团队将其群日报工具的底层能力开源为 vchat CLI，这是一个能解密并查询本地微信聊天记录的命令行工具，支持拉取全量记录、成员列表、头像导出和语音转写，已收录在 vantasma-toolkit 仓库的 cli/vchat 路径下。

---

## 正文

万涂幻象 万涂幻象

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEF2S8kksqTb906ef2QfWCw3T18X2D3Bpj9FS5jumAlDgicGWPRN5qPEI7jaTFqwERGQAIdUEXeq0LQ0oROcwDurZE0d0SoQxtS4/640?wx_fmt=png)

万涂幻象 · 让 AI 真的进业务

2026.09.19

熟悉我们的朋友都知道群日报，也有不少人想用一下这个工具。经过很多考虑，我们决定把群日报底层的那个 CLI开源了。

先说群日报。“祥瑞和 Ta 的朋友们”这个群，每天都会把聊出来的好问题、管用的方法和踩过的坑整理成一篇日报。不是逐字聊天记录，也不是冷冰冰的会议纪要，就是当天群聊的一篇短篇报道。5 月我花两天把整理流程做成了 skill，一天的群聊记录变成一份杂志风长图，八段时间故事线、真实头像、Q&A 沉淀，能从头读到尾。公众号发过一篇 [我做了一个微信群聊总结 skill，把聊天记录玩出了点新花样](https://mp.weixin.qq.com/s?__biz=MzYzNjk5MTU2OA==&mid=2247501286&idx=1&sn=2daa49173d4b4d9b5481d4c8184d54b2&scene=21#wechat_redirect) 。公开归档从 4 月下旬起放在 GitHub 上，到 8 月下旬攒了 115 篇。

看过的人里，不少人来问过同一句话，这个工具能不能给自己也用一下。

真正的障碍不在长图那一步。群日报每天要干的是底下那层活，拉群聊全量记录、列成员、导头像、转语音。这些数据都在每个人的电脑里，锁着，一般工具读不了。

这个底层能力，我们后来把它做成了一个命令行工具，叫 vchat。今天开源，放在万涂幻象的工具箱 vantasma-toolkit 里，路径 cli/vchat。macOS 上一条 sudo vchat setup，你电脑里那份微信数据就全打开了。

01

怎么装

最省事的装法，是把这段话直接贴给你的 AI Agent，Claude Code、Codex 都行。

帮我安装 https://github.com/xiangruiai/xiangrui-toolkit 里的 vchat CLI（微信本地数据查询 / 解密工具），路径是 cli/vchat。按它 README 走：clone 仓库 → cd cli/vchat → bash install.sh → pip3 install cryptography zstandard → sudo vchat setup。过程中需要我输一次 sudo 密码，解密时保持微信桌面版开着并已登录。装完跑 vchat doctor 和 vchat ls 20 给我看结果，再用三五句话告诉我最常用的命令。

习惯自己动手的话，手动就四行。

...bash

git clone https://github.com/xiangruiai/xiangrui-toolkit.git

cd vantasma-toolkit/cli/vchat

bash install.sh

sudo vchat setup

系统要求不高，macOS 就行，Apple Silicon 和 Intel 都支持，另外微信桌面版要保持登录。Windows 也能用，查询没问题，解密那一步要看 setup 里的提示。语音转写要额外装 openai-whisper 和 silk-python，不用语音可以不装。

装好 vchat 之后，群日报的 skill 你也拿得到，仓库 skills/ 目录里，group-daily、group-daily-newspaper、group-activity-base 都是开着的。数据层和流程层在一个仓库里，想跑同款流程的，从这两样开始搭就行。

02

在 WorkBuddy 里安装使用

打开 WorkBuddy，把 README 里那段安装话术原样贴进输入框，直接发送。

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEGNvrnhwJGvyuh52OTqCEWqlYKUaibH4KmuAIZSIr9DabqHnTAeEFrBKrFDyy2zdx74WZX1Sx0X4F4ORosjeHUyAWBaHWlIOnUE/640?wx_fmt=png)

它自己 clone 仓库、装依赖、跑 setup，中间停下来等两次确认，一次是管理员密码，一次是微信登录状态，在卡片上点一下“已登录，开始解密”就继续。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bicKL8EichaEEvNapGRZCicVs6OgtD3QezGxwlib2xLfcGZDswNUXKVw4Q0w8Rq4srwaln5nOkHKTT8qiayemiaH0sYC2GgfaRcgaWibLKaribBSU8A/640?wx_fmt=jpeg)

18 分钟后就报了“安装完成”。vchat doctor 检查必需库全部齐全，拉出来的会话数据很新，最新一条就是前一天晚上的。有一件小事要留意，codesign 那一步在 WorkBuddy 里会被 macOS 权限挡住，不影响使用，以后想增量解密新消息，回自己的终端跑一句 sudo vchat decrypt 就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEHpNTLic5U8rG2SzcdUREibKHbqXMhGkGBkLHnLl45bsHRRFV1mzV3wknM0M4rlqsF8RNZMzrzKJhv0rhzJaBQwpD5xs6N60XRwo/640?wx_fmt=png)

03

60 多个子命令，群日报只用其中一角 ![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEEE5mtn8OxTnkxXO7VxicdvrIwD4jI1UQg1NzWSS9ApTWuT7roGuLF8ASicZ4qKgNUStuJN9R9vI9YUmCGWibUkoOn8VRuNwLC6hE/640?wx_fmt=png)

装好先跑三条。vchat doctor 检查数据齐不齐，vchat ls 20 看最近会话确认读到了自己的数据，vchat --help 看全量命令。群日报每天真正用到的是几条，history 拉群聊记录，group-members --avatars 列成员加导头像，voice-transcribe 转语音。剩下的，你拿到手自己挖。

看和搜。 拉一个群五千条历史是 vchat history “群名” -n 5000；全库关键词搜走 FTS 索引，vchat search “关键词” --fast；找一个人的 wxid 用 vchat contacts “昵称”，联系人多还有走拼音索引的 contacts-fast。

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEEMYiaiaY76Cuvup8mxVj0aOOnj1g5WMPIuKhk35iaOXupaPIjBjmniaHnzgyrnsfWgEicWQVk8AOCYeGmh3zduafwHRhoE55XR5Quw/640?wx_fmt=png)

群和联系人。group-info 给你群主、公告、成员数；group-members “群名” --avatars -o dir/ 列出全部成员，顺手把头像批量导出；联系人标签用 tags-ls 和 tags-members 查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEELxHM0ffA4O3oJqqXcuZbPn2s7ltnJt0Gvm1pdXFjTtxFkHxc1xnUVsYVFr13Qicq9XCeqqvia5CqOYaTzPW3jwDtnAcUNrs7gk/640?wx_fmt=png)

导出。 单个聊天可以 vchat export “某某” -o x.json 导成 JSON 或 Markdown。要整库就走 vchat corpus。corpus stats 看全库统计和时间跨度，corpus export --limit 1000 分页导出、游标断点续传，corpus export --stream 用 NDJSON 流式往外倒，多大库都能读完。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEG5hkap4YV9Etyibx46lxxIufrUNVhmsnQUH3fzOXGGoMhfWQaoTfg3eBTZD4Jic7HxdQx4xf4jibZdSibnomx1hr3GfovdZJiaw7OA/640?wx_fmt=png)

语音和图片。 语音消息存的是 SILK 格式，vchat 接了本地 Whisper 转写，模型就跑在你自己电脑上。图片是另一套加密，聊天附件和朋友圈图片的 V1、V2、XOR 几种格式，它都能自动识别解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEFFwAVdUiaKrL2RDvJeQdzMFLynXHkeJw0ic2NuVZ0kHJakxxm6PZvEsWbPIATMGYm8jNUYewTR1cEFG5o5JJicGVniak3QQYGaKsg/640?wx_fmt=png)

朋友圈。sns-ls 看最近动态，sns-search 全朋友圈搜关键词，sns-user 看某人的时间线，sns-export 导成 Markdown，sns-likes 和 sns-ads 能翻出你的互动记录和刷到过的广告。

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEFdtJjPQBZkk5lldNLiavLP5oJFr4fydbcaAuP0CmNjw4zvpnB0vVwrexxPnab4mNW8GY5bgibKejtOPEkrFv3jCOkq0rCqvmLYM/640?wx_fmt=png)

公众号、视频号、企业微信。biz-ls 列你看过的公众号文章，biz-articles 翻某个号的全部文章，finder 和 finder-lives 管视频号和直播状态，bizchat-contacts、bizchat-groups 读企业微信联系人和群。

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEHpc3PxqV3joPcpmUBeJrnBysXnqgAFNoGaPicIGcCzSt3WPztG5F2uicR8WEy0UOibeImfje1Qf6GTjaqIzgHPjITZjFlOGJE7wo/640?wx_fmt=png)

冷门但真用得上。revoked 列被撤回的消息，deleted-sessions 找被删掉的会话，search-history 能看到你在微信里搜过什么，money 导转账和红包历史（只记往来，不含金额），收藏夹有一整套 fav-ls、fav-search、fav-tags、fav-export。

![](https://mmbiz.qpic.cn/mmbiz_png/bicKL8EichaEFlzw5F3DLoiaXCn8PpQnc9Tde87mrmLEMVTicHJGaibEKSUtC2X9mVMVTlEoZujegflq2aTKz27MDqQfEmCOdQxNPWpiacSkYqKh4/640?wx_fmt=png)

统计和实时。stats-overview 报消息总量和时间跨度，stats-top-groups 排群发言量，stats-monthly、stats-hourly 画活跃直方图；vchat watch --chat “群名” 像 tail -f 一样盯着新消息往下滚，做自动化时当触发器用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEE5mnf0dCFVVq13bYGyuWMHC8jSfb6ibCOHUOmkdialKUv4RQcQqgvqHD9cWv1uiasmosrWY65Gb2g46R0ahK85LWd4iaSlk9v4x8k/640?wx_fmt=png)

数据目录不想用默认位置，export 一个环境变量随时改。对数据完整性特别在意的话，可以开隔离快照模式，每次解密都写一份独立副本，校验全部通过才切换使用，文件要是被人动过，它会拒绝读取，让你重新解密（这个模式目前支持 macOS 和 Linux）。

每个子命令都支持 --json，输出结构化数据，管道、脚本、AI Agent 拿来直接用。vchat\_core 还能当独立的 Python 包 import，get\_chat\_history、search\_messages 这些函数直接写进你自己的代码。工具箱里的群日报 skill 干活时，走的就是这层数据接口。

命令看到这儿，你可能会想，这么多谁记得住。其实一条都不用记。上面这些只是 Agent 的工具箱，你用自然语言跟它聊就行，想看什么直接说，最近哪个群聊得最热闹、把我和某某的聊天记录整理一下、上个月我发了多少条朋友圈，它自己去挑命令、跑查询，跑完把结果讲给你听。对话聊着聊着，数据就到手了。

仓库地址再放在下面的阅读原文里了。点击阅读原文就可以打开，vchat 在 cli/vchat。装完跑一下 vchat doctor，能看到自己的数据，就算跑通了。

装好之后能干的事，比群日报多。让 Agent 每天定时拉一遍群聊记录做个总结，把某几年的聊天记录导出来看看自己都聊了些什么，语音批量转成文字，或者用 watch 盯着新消息接你自己的自动化，都是几条命令的事。

最后啰嗦一句，这个工具只能用于个人学习，能处理的只有你自己有合法访问权的数据，别拿它去碰别人的账号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bicKL8EichaEF1AEoJVhX8puONRU96scOlsd08icX6Ssmibk4ATXdkTyFzibdKYeCLn9CNEU8bfdzP1NDbWy51qH3syuyXwYdcKUpQap2lnGxInw/640?wx_fmt=png)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过