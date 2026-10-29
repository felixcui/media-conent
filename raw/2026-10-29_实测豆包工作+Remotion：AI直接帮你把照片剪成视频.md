# 实测豆包工作 + Remotion：AI 直接帮你把照片剪成视频

**作者**: 王平安

**来源**: https://mp.weixin.qq.com/s/ptwczQjWZ3y_7Tmrf26ACw

---

## 摘要

本文介绍了通过给豆包工作安装Remotion Skill，实现用对话方式让AI自动完成视频剪辑的方法。Remotion是代码渲染视频的开源框架，天然适合AI操作；安装过程无需配置环境或敲命令，对非程序员友好。安装后用户只需选择素材文件夹并用自然语言描述需求，豆包工作便会自动拆解任务、设计分镜脚本、整理素材、剪辑视频并添加转场、配乐、文案、旁白和字幕，整个过程透明可见、可随时打断调整，成片可在Remotion编辑器中查看和导出。

---

## 正文

王平安 王平安

在小说阅读器读本章

去阅读

大家好，我是 Chris。

假期出去玩了一趟，手机里多了很多照片和视频。回来想剪个 VLOG 视频，就挺头疼，打开剪辑软件 → 新建项目 → 导入素材 → 一张张拖进时间轴 → 排顺序 → 加转场 → 配音乐 → 对字幕。

头疼，还很消耗体力。麻烦。

最近 Chris 发现了一个办法： **给豆包工作装上 Remotion Skill** ，前面的那些事情，就可以给豆包工作去做：导入素材、安排播放顺序、加转场、配背景音乐，甚至写文案、配旁白、上字幕，我只要说下想要什么样的视频。

## 一、Remotion 是什么

Remotion 本身是一个用代码做视频的开源框架，视频里的 **每一帧都是代码渲染出来的** ，所以 **天然适合交给 AI 来操作** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L3QFuGxENjeJEYcicRIk1PVLhXCea0NjrH0JlWiaMVblpgl9XHMicibFYJavewjsvk3FsPVqGJkCs80D3iaU3EpZK3drjulrUr9Lpzqa7DMgBibibA/640?wx_fmt=png&from=appmsg)

而 Remotion Skill 相当于给豆包工作配了一套“视频剪辑技能包”。装好之后，豆包工作就懂得“帮我把这个文件夹剪成一条旅游 VLOG”这种需求了， **会自动拆任务、调技能、剪视频** 。

这是 Chris 觉得最有价值的地方，它让大家不用学习新软件， **直接对话就可以剪辑视频了** 。

## 二、安装 Remotion

首先打开豆包工作，输入提示词：

> 帮我安装 github 上 remotion-dev 的 remotion 和 remotion-dev 的 skills

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L3QFuGxENjcfcuLFzmnrXeP83wcs0H6u0BPTcPVSaDUibdhWj3LBZQPibicVlqRzYdUhicVHBrKbolDcYGbDJcGgmVbbOzy7NEHt2SIJQnXHmcY/640?wx_fmt=png&from=appmsg)

看到豆包提示 Studio 已经在后台运行 http://localhost:3000 就表示已经安装并启动好了，我们可以直接打开这个链接，在浏览器看到一个视频编辑器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L3QFuGxENjekNgbl17c0vUyKljPmIVGkLP2XibB1qX9KN0mbSpuXhUvibEJx6VyOKOTKOfyKU0FpatWHoaXeQK1AZE4ibS8aO4eu4E8QnZu4Aw/640?wx_fmt=png&from=appmsg)

整个过程不用配环境、不用敲命令，对不懂代码的朋友非常友好。

## 三、自动剪辑视频

安装完成后，用起来就很简单了，在豆包工作中，选择你的素材文件夹，直接告诉豆包工作你想要什么样的视频。

比如输入：

> 使用 Remotion Create 把我添加的这个文件夹里的素材，剪出一个旅游 VLOG，需要有合适动画特效，还有文案、旁白和字幕。

![](https://mmbiz.qpic.cn/mmbiz_png/L3QFuGxENjcmzFQNfZTAhhap5sL1iaY7rYCZTjeegr1z6n38sj7HDaXLgH9kuLrm287WHFLHqnziaqdB2ATYZn6qc2SdOc9fLIe8rIqAm7EYU/640?wx_fmt=png&from=appmsg)

发送之后， **豆包工作会开始拆解任务、调用对应技能执行** 。右侧能看到实时任务进度和产物，我注意到 **它连分镜脚本都已经设计好了** ，再往下才是整理素材、剪辑视频。

这里有个细节真不错，就是 **整个剪辑过程是透明的** 。它不是黑盒只给你成片，而是先出脚本、再执行，每一步都能看到，不满意随时可以打断它进行调整。

## 四、查看效果和导出

剪辑完成后，打开 Remotion 启动的网页，就能 **看到完整的编辑器和成片** 。

素材会按照要求排列在时间轴上，转场、背景音乐这些也可以看到。如果想继续调整，可以直接在 Remotion 里手动改，也可以接着用对话让豆包改：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L3QFuGxENjeO7xtxcM1umURqVfKJbic7XZveRCwJXkloSDVrhHwicF2Nzuu1s6K4JPuoYZaFjqUGEuYC2t9mJ9HAXBQia95NVfx4iac7LlGlTHc/640?wx_fmt=png&from=appmsg)

最后导出视频，两种方式都行：

1. 直接在编辑器界面导出；
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L3QFuGxENjdZMK92ZoGBv1icGRRdM1pU85qNibuUkiaUqHJnnn53DDicMnzIMUJdM6jSkm4GynUibiaedgdwZiaLjgE0ednofY4CjAoxiczlIeuxHMY/640?wx_fmt=png&from=appmsg)

2. 让豆包执行命令导出：

这里我让豆包执行“帮我执行 npx remotion render XiamenVlog out.mp4” 导出视频，就像下面这样：

![](https://mmbiz.qpic.cn/mmbiz_png/L3QFuGxENjdMHIRwicxNQRRsGEyVqcjpL235JcdXXpoklMzCzcXeKBhWXVI1NyAArm3YPBw3wQXFR4KFlFVFaiadJy7IiauSzaLwz8AX3usE6M/640?wx_fmt=png&from=appmsg)

这样既能让 AI 完成基础剪辑，也方便自己进一步完善，直接让 AI 来干这些体力活，我们负责去做审核就可以了。

下面是 Chris 做好的效果：

## 五、总结

Chris 整体用下来，豆包工作 + Remotion Skill 一起用，安装简单、操作方便， **视频剪辑的门槛降低了非常多** 。

我们只要准备好素材，再 **用文字描述剪辑要求** ，豆包工作就能完成基础剪辑，比较适合旅行相册、生活记录、产品展示这类“素材多、要求不苛刻”的场景。

如果平时经常需要把照片整理成视频，可以试试这个方法。

**现在网页搜索『豆包工作』下载电脑端，新用户免费领 30 天会员权益体验。老用户每日签到领额度可以攒着，等做任务的时候用，签到 30 天得到的福利额度很高。**

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过