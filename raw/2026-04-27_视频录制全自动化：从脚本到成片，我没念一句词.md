# 视频录制全自动化：从脚本到成片，我没念一句词

**作者**: 王大懒

**来源**: https://mp.weixin.qq.com/s/4fS0_e3-20S9YioSnQmF7w

---

## 摘要

我提前告诉过它我的写作偏好，比如"先说结论"、“像跟聪明的朋友聊天”、“每句话都要有信息量”。写技术教程类文章，它会引用《黑客与画家》；写评测对比类，会引用《思考，快与慢》。所以就有了接下来的操作 从选题、写稿、做PPT、生成语音、翻页录制到输出成片，全部自动化跑完。我会告诉你每一步怎么做的，用什么工具，踩了什么坑。

---

## 正文

王大懒 王大懒

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4vw6EEXGuR8Yc2nDnic97iaVrczAia8ZRlK3BkZfgibfrPogWCA4qoSJZGDxVRkVE5pRkiaee3BXu23y03wtaw2RzvJYDGBVxd2AK4Q/640?wx_fmt=jpeg&from=appmsg)

  
最近呢，因为生病住院，在病房里不方便录制视频，所以我就想着不张口，用HTML格式+TTS的方式去自动录屏，来完成视频制作。

所以就有了接下来的操作

从选题、写稿、做PPT、生成语音、翻页录制到输出成片，全部自动化跑完。我就在旁边喝了杯水，回来视频已经生成好了。

这篇文章把整个流程拆给你看。我会告诉你每一步怎么做的，用什么工具，踩了什么坑。技术细节不会省略，但也不需要你是程序员才能跟上。

---

## 整条流水线长这样

先给你看全貌。我做一条AI科普视频，完整流程分四步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rte67dtrA4tfxGAEHPTCRld6s5GO2w5CV3uuO33qXqdLicVTDYkvGHbGYeTv5r2pdDicGHuUYhmP9EVzcfD3L24DlibXBxUicLVPA5gCYuZvicQI/640?wx_fmt=jpeg&from=appmsg)

每个环节各有一个 Claude Code Skill 自动完成，最后一步用剪映做音色变换。Skill 你可以理解为一个可复用的自动化脚本，告诉 AI “按这个流程走”，它就会按部就班执行。

我用这套流程录了我的26期视频《Token经济产业链》，从开始到出成片，手动操作加起来不超过5分钟。大家可以先简单看下效果

下面逐步拆解。

---

## 第一步，选题，让 AI 帮你扫一圈热点

做内容最头疼的事之一，就是"今天写什么"。

我用 `topic-generator` 这个 Skill 来解决。它的逻辑很简单，自动扫一圈AI圈的热点源，帮你整理出可写的选题。

它会同时搜这些地方。

- 36氪、极客公园、新榜（国内科技媒体）
- Anthropic、OpenAI 官方博客（海外一手信息）
- B站、小红书、即刻（看普通用户在讨论什么）
- X/Twitter（看大佬们在发什么）
- 知乎、公众号（看深度讨论）

所有信息源只保留最近15天的内容，避免拿着半年前的旧闻当热点。

搜完之后，它会做三件事。

1. **去重** ，跟你的历史选题库比对，完全重复的直接踢掉
2. **分级** ，每个选题标注"信号强度"（多平台同期出现 = 信号强）
3. **出卡片** ，每个选题给一张详情卡，包含标题方案、核心角度、用户痛点、差异化建议
4. 保存，在终端运行后，最后选题会保存在我指定的文件夹中。
![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4tWO74qd8zSZQibCah5bZ7yOGamvFT6icRnm3E9FVulF4zGwSTk0oicicUcPd8vDdUCpz2472qgjzXKAmt73tl5XOrickqNtObMI8JE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rte67dtrA4sM1aN3XictuGb6NTyBdzibODTuAU48nm9fVe9pduFMwmewHpS6CvDMhNxurZWSKibbwE6IbXswXl37rteI8xdJBQhaO0flTHhm48/640?wx_fmt=jpeg&from=appmsg)

我跑一次，拿到6到10个新增选题。从中挑一个信号最强的，进入下一步。

---

## 第二步，写文章，从选题到成稿

选定题目后，我用 `wechat-writing` 这个 Skill 来写公众号文章。

这个 Skill 最关键的一点是，它有自己的写作风格参考文件。

什么意思呢？我提前告诉过它我的写作偏好，比如"先说结论"、“像跟聪明的朋友聊天”、“每句话都要有信息量”。它每次写之前会先读这些参考文件，然后按照我的风格来写，不会写出那种"近年来，随着AI技术的飞速发展"的八股文。

它还维护了一份参考书籍库。写技术教程类文章，它会引用《黑客与画家》；写评测对比类，会引用《思考，快与慢》。不是瞎引用，是按文章类型匹配的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4sD1bYiahgCBwwlcwX6FHcJiab6ibZdI2h6jScBoa5FrW2UTXuvwiaBa9Kql9ibFlrjjibJicSBOy17O8XD9LQuwtRibNdooCrcia1X1ibJs/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rte67dtrA4sKCniaKsnwMPeCbfFmib00rnETku8TVAJPcEHcTC1rgp1wbib8dB65CbZNh6jJ7lvE2ibC8epWcA8UbETWprKgRa8VL7wdTDCcPVw/640?wx_fmt=jpeg&from=appmsg)

  
给我一篇文章之后，我会在obsidian里快速过一遍，改几个表述，确认没有事实错误。这一步大概花5到10分钟。

---

## 第三步，口播稿 + HTML PPT，一次生成

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4tEDPr2hjJPOAFOhHvfx2SyJF2CXfJnGoCRnhw2ib7rFOL1o6jcGdajuldqmorCjiaTah2jibKmawI5VpO0CBuEOzSqaS2bibSdPOw/640?wx_fmt=jpeg&from=appmsg)

文章定稿后，直接提示用 `koubo` 这个 Skill 同时生成两样东西。

**口播稿** ，把文章转成适合口语表达的脚本。每段编号 P01、P02、P03…一共8到12段。每句话不超过25字，去掉所有书面语，加反问句和语气词，口语化。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4siazib47jgT0QknvbG04tuEQa0lqqFfZ52iaqoicyyxziauOcPw8Mc9vJGWRm0PbO5EYpsmbuZK6fShWQk1MXoFeYsqzQ9eaWBtqdc/640?wx_fmt=jpeg&from=appmsg)

**HTML PPT** ，一个全屏的演示页面，风格自适应，适配1080p录屏。每段口播对应一页PPT，按方向键右键翻页。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4tEYvOl0pyhUBNUhXTWyL5atgjK63d3J6vib3cpoyjIEU98aIFavib8NUgzJLTzhKaf8kn7KxVndFU4pjLibxZgAOV6gdG0XmuFHA/640?wx_fmt=jpeg&from=appmsg)

这里有个细节值得说一下。HTML 上的文字不是一下子全出来的，每页有三批动画，分别间隔0.5秒、2.5秒、4.5秒依次出现。这样录制的时候，画面有动态变化，观众看起来不会觉得死板。

口播稿和PPT是同一个 Skill 同时输出的，页数一一对应，不会出现"讲到第5页了，PPT还在第3页"的情况。

这两个文件会保存在同一个目录下。

---

## 第四步，自动录制，一条命令出成片

这是整个流程里最核心的一步。

以前录制视频，我得打开HTML、打开录屏软件、调整窗口大小、按录制键、念稿、翻页、停止录制。一条5分钟的视频，录制的实际过程可能要20分钟，因为念错一句就要重来。

现在我用 `tts-auto-record` 这个 Skill，整个过程变成了一条命令。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Rte67dtrA4sCJXd7ia6coTwS3NoKnMzibgHzkjWz2IItibHpBKibiaiaaP6lje2jbicSPX8G2ADO5cwwFpIa4Blnic3zdHVvIEUwicTk2NlMZaDACqLg/640?wx_fmt=jpeg&from=appmsg)

  
它的原理是这样的。

```
123456# 简化的核心逻辑
for page in pages:
    按翻页键()        # pyautogui 自动按键
    播放TTS音频(page) # pygame 播放语音
    等待播放结束()
    等待1.5秒()       # 页间隔
```

具体流程是这样的。

**第一步，生成语音。** 用 `edge-tts` （微软免费的TTS服务）把每段口播稿转成单独的 mp3 文件。12页口播稿，生成12个音频文件，大概花30秒。

**第二步，打开HTML。** 自动用浏览器打开HTML，按F11全屏。

**第三步，倒计时。** 给你15秒准备时间。

**第四步，自动播放。** 倒计时结束后，脚本开始循环，播放第1页语音，播完按右键翻页，播放第2页语音…一直到最后一页。

**第五步，录屏。** 整个过程用 `ffmpeg` 自带的屏幕录制功能（Windows上是gdigrab），在开始播放的同时启动录制，播放结束自动停止。

**第六步，合成输出。** 把录屏视频和TTS音频合并成最终的 mp4 文件。

全部跑完，去输出目录拿 `final_video.mp4` 就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rte67dtrA4smLibE6BWQ6dF28alNV9AEdTtHZPkDVLthmhV02uGEfqI7lD91Y1fic26K1cXV67yInJLtEJn35K9bkHFiaE82Rhsg60hSiaufgWA/640?wx_fmt=jpeg&from=appmsg)

整个过程唯一的"手动操作"，就是在倒计时的15秒里，确保浏览器是全屏的、窗口在最前面。其他全自动。

---

## 第五步，剪映换声音，让AI说人话

自动录制输出的视频，声音是 edge-tts 合成的。质量还行，但你一听就知道是AI在说话。语气平，没有情绪起伏，长时间听容易走神。

解决办法很简单，把视频丢进剪映，用它的"音色变换"功能换一个更自然的声音。

操作就两步。

1. 导入视频，选中音频轨道，点击"音频""换音色“
2. 从音色库里选一个喜欢的，点应用
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rte67dtrA4tmiaXLWLcI8wqvjkmKibruxGsiaEnvnw1BXQeMicTaPKUNrN1uKicIzg0LSPAsPicyXKIwZOvEpRJBUYYus4wrIBKsgrMGFNzErDEj0/640?wx_fmt=jpeg&from=appmsg)

剪映内置了不少音色，男声女声都有，大部分比 edge-tts 自然。如果你愿意多花两分钟，可以先克隆自己的声音——录制几段自己的语音，上传训练，之后每次都选自己的音色。观众听到的就是你本人在讲，但录制的时候你根本没张嘴。

这一步是目前流程里唯一需要手动操作的环节，但操作量很小。导入视频、点几下、导出，加起来不超过3分钟。

---

## 踩过的坑

讲几个实际使用中遇到的问题和解决办法。

**翻页节奏不对。** 刚开始TTS播完立刻翻页，感觉太急了。后来加了一个1.5秒的页间隔，每页语音播完后等一下再翻，节奏自然多了。这个值可以根据自己视频的风格调，脚本里改一个数字就行。

**浏览器焦点丢失。** 有时候倒计时结束，脚本按翻页键，结果焦点跑到别的窗口去了，PPT没翻页，录屏全废。解决办法是在倒计时阶段点一下浏览器窗口，确保它拿到焦点。

**单页口播稿太长。** edge-tts 对单次文本长度有限制。如果某一页口播稿特别长（超过1000字），建议拆成两页。我的口播稿每页控制在150到300字，没遇到过这个问题。

**语音选择。** edge-tts 自带几十个中文语音。我试了一圈，最后选了"云希"（zh-CN-YunxiNeural），男声，自然风格。女声推荐"晓晓"（zh-CN-XiaoxiaoNeural），也不错。可以在脚本里改一行配置切换。

---

## 你需要准备什么

如果你也想搭这套流程，需要这些东西。

**AI 工具**

- Claude Code（Anthropic 的 CLI 工具）
- obsidian+claudian
- Skill 脚本（文章后面会说怎么获取）

**可选升级**

- 如果觉得 edge-tts 的语音太机械，可以换成其他的，例如 GLM-TTS（智谱的TTS API），语音自然度提升明显，按字符计费，一条视频几分钱
- 有 NVIDIA 显卡（8GB+ 显存）的话，可以跑 CosyVoice 本地推理，完全免费，音质顶级

---

## 这套方案的局限

实话说几个不够好的地方。

**TTS 的语气偏平，但也能解决。** edge-tts 免费归免费，但情感表达有限。它只能调语速，不能控制语气、重音、停顿。讲技术科普问题不大，但情感类、故事类的内容，语音感染力不够。好在剪映的音色变换能一定程度上弥补这个问题，换一个更自然的音色后效果明显改善。如果追求极致，可以换 GLM-TTS 或本地跑 CosyVoice。

**HTML 的表现力有上限。** 它本质上是网页，做不了PPT那样花哨的动画。文字、图标、简单动画够用，但复杂的数据可视化还是得用专业工具。

**录屏质量取决于显示器。** ffmpeg 的 gdigrab 直接抓屏幕像素，你显示器是1080p就录1080p。想要4K画质，得换 OBS 之类的专业录屏软件。

**不能实时改稿。** 录制过程是全自动的，中间不能暂停改某句话。如果某一页的口播效果不满意，只能删掉那一页的音频重新生成，然后从那一页开始续录。脚本支持 `--start 5` 这种参数，指定从第几页开始。

---

## Skill 怎么获取

文章里提到的四个 Skill（topic-generator、koubo、wechat-writing、tts-auto-record），都是基于 Claude Code 的自定义技能。它们本质上是 Markdown 格式的指令文件，告诉 AI 按什么流程、用什么工具、输出什么格式。

你可以理解为，每个 Skill 是一份详细的 SOP（标准操作流程），Claude 读到这份 SOP 就知道该怎么干活。

如果你已经在用 Claude Code，可以直接把 Skill 文件放到 `~/.claude/skills/` 目录下。每个 Skill 是一个文件夹，里面有一个 `SKILL.md` 文件描述功能和流程。

具体的 Skill 文件，我在公众号后台放了获取方式，关注「AI淇橦学」回复"SKILL"就行。

---

## 回到最开始

做内容最难的不是写，是重复。

选题要想、稿子要改、录制要重来、剪辑要等。每一步都不难，但每一步都要你亲自上手。做一条视频，从早忙到晚。

这套流程做的事情很简单，把重复的部分自动化，把人的时间留给真正需要判断力的环节。

选题还是你来选，文章还是你来改，最终效果还是你来定。但录制这个过程，交给机器就行。

保罗·格雷厄姆说过一句话，“做一个创造者，而不是消费者。” 这套自动化流程让我从"反复录制的消费者"变成了"设计流程的创造者"。

如果你也在做内容，试试把重复的部分交给 AI。省下来的时间，用来想更好的选题。

---

关注「AI淇橦学」，回复"SKILL"获取本文提到的 Skill 文件包。

继续滑动看下一个

AI淇橦学

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过