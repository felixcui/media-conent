# 刚刚，Hermes上线/learn 模式！从任何地方提炼任何Skill！

**作者**: DracoVibeCoding

**来源**: https://mp.weixin.qq.com/s/yUN3B7KVHOnXVXE5tsOSVA

---

## 摘要

Hermes上线了全新的/learn模式，支持用户输入GitHub仓库、PDF等任意资料，系统会自动学习、提炼并封装成对应的Skill。文章以爬取微信公众号文章专辑为例，演示了升级Hermes后，通过/learn指令学习指定代码仓库生成skill，并配合安装OpenCli插件完成实际爬取任务的完整操作流程。

---

## 正文

DracoVibeCoding DracoVibeCoding

在小说阅读器读本章

去阅读

刚刚，Hermes上线了 /learn 能力，你可以喂给他任何资料（Github仓库/代码、PDF、API文档、配置文件、等等），它可以自行学习、提炼、封装出合适的Skill来~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjjBWPTaaAuWPIgLjv9nbRKOYVQAWeazhIPo0gWWrMC4RbVT924ON9CcOO5UYlAkR04XwtuBsVxa2nHex4Uwx1JLCnXBtpibyU8/640?from=appmsg)

今天带大家一起看Hermes如何通过/learn模式封装skill并爬取指定公众号专辑里的全部文章的~

•

首先，需要将Hermes升级到最新版本

> 在hermes agent终端输入 hermes update 指令以完成升级

```
hermes update
```
•

选择一个爬取微信公众号文章专辑的Github仓库

> 我用的是这个仓库（opencli-weixin-album）：https://github.com/SlowGrowth1314/opencli-weixin-album
> 
> ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGia2tQ1IYBciciaWdwfFUKypib3I479rXHNqxxrWN4bPMicxutx3EJdRcEoCEpzibCxMGADiaqTrYu7bxtYuG0LT8eQbnpdZJXbwgm5dM/640?from=appmsg)

•

将这个Github仓库喂给hermes agent，记得要采用 /learn 模式：

```
/learn https://github.com/SlowGrowth1314/opencli-weixin-album
```
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhptR1VHicAlicxNZVId40zQKibjibhM16NKzrS82aBg56M8d0JepeQb9qq6K5ric4SpqhLVyK8Qylzmq7fB6dEdz4fnFysygDFpVsc/640?from=appmsg)

•

大概3分钟后，hermes agent完成Github仓库代码的学习、提炼、封装过程：

> 封装出的skill就是仓库名：opencli-weixin-album

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhTEWmG4muAWOeejrvQaAR38AbpwoePicxWpUuj60rOS0FBHm89EFjdGdzgORNZAicicWsxNCbq9g8lLY7wBVVE4Q9YfaHMxVworM/640?from=appmsg)

•

你可以询问hermes agent该如何使用该skill

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGiamglBbVq2BficPmbRuOFqOD1OOrwGlaIwUOKiaQ6Hujs5ZYxWw3iaLXABych5OnMicULktmKPpG9tRGGPbmibH69yDYDIe1qZEfgqE/640?from=appmsg)

•

由于opencli相关插件并没有安装，所以，补装一下opencli

> OpenCli是一个将所有浏览器操作都CLI化的项目：https://github.com/jackwener/OpenCLI

```
npm install -g @jackwener/opencli
```
•

安装opencli插件，让hermes agent把OpenCli插件下载到Downloads文件夹

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjFXrQn9ceicnRNVeyO1aLEvQKFnw0L2YaSAodXe5cIJfdORsz3vO3rh0bnSicsic0eDDPuKWsakNFGMjYdp7Z2f4QLxuulibvGyibA/640?from=appmsg)

•

然后，在Chrome浏览器的 &#x27;chrome://extensions/&#x27; 中【加载未打包的扩展程序】把OpenCli的插件加载进来

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgPyNQLgd7NhTPONJ94rpTSooOdncQuGoRQJzuk8Q7zNhLmmZVYTpV8LtR06GbndlAwJvwWP9zsVL3WaYbR5Fic026HhjWSvWms/640?from=appmsg)

---

•

接下来，让我们选个大V的公众号文章专辑，比如卡神公众号里‘那些思想’专辑

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhzNSdz8ygg9IcwPy6EITfqfVQWcyBw4a9DzKEfrEfnptfmoKNtmJfJiaGux7icKcYCJ24EggCAlam28wnXA4qO9VIwcUBW09ibUY/640?from=appmsg)

•

进入专辑文章列表后，点击右上角‘···’ --> 【复制链接】，把专辑链接复制出来

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgnmUXWtS8dbswDATJ8Ea6Hno0fJWkricjRkTVxIp4vyIibY96xb5Sw5aeQKiaCLH9MYv67pgybJXzrLLk6cCUDDU6jhXgcIyrhR4/640?from=appmsg)

•

然后，将这个链接发给hermes，让它使用刚才/learn 模式封装出来的skill爬取这个专辑链接里的所有文章

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhlNZLib0ZlAiaQ5707GqvK6664dOEZGfqJCxwczQmpOxEertyFnYM0BVLjlppmQicGibADVrEXYdHeo9hlRltsSO2PWnQgHdyK5ico/640?from=appmsg)

•

之后，hermes agent会采用OpenCli插件，控制浏览器逐条打开每个文章的链接，并完成爬取；

> 本质上是Chrome浏览器的CDP的二次封装和OpenCli打通

•

大概10分钟之后，所有文章都以markdown形式爬取下来，并放到了【weixin-albums】目录下；

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjAoXXLmPJAzy2BI1zzjuvaBHk7ZHdmBNia1ZXcicDLw5iafibaghZ6r9HvUibJbVtyicicoTd6xQpuzpkoIpRPiaLdOTJwR64hibK9aw4s/640?from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGiaNcw5l3kM2waibiaWbl83wpIkDtPly4vEOKKRYia3qgLvzQxyicq94eibmJSdicLEFPUo4BICicibGjibgibAXGic2Jf9KD9RB2tgVr8PR4M/640?from=appmsg)

•

随便打开一篇看一下，OK，所有文字和图片都被很好的保留下来了：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGh2pX29765AYzD8ysRVgPm0GaH1OPm7RicPtojrlTCMF2kLNCN9f4WCYfzHLE31YUamQZOsAUfk9V4JWS9quT7lTaCHgapJRxWk/640?from=appmsg)

恭喜，你现在拥有了爬取任何公众号专辑文章的能力！

---

从现在开始，请把Github当成你的应用市场~ 任性的把各种能力逆天的仓库Repo丢给你的hermes agent吧！

•

https://github.com/yt-dlp/yt-dlp

•

https://github.com/Panniantong/Agent-Reach

•

https://github.com/3b1b/manim

•

https://github.com/remotion-dev/remotion

•

https://github.com/heygen-com/hyperframes

•

https://github.com/firecrawl/firecrawl

•

https://github.com/jgm/pandoc

•

https://github.com/rclone/rclone

•

https://github.com/aria2/aria2

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过