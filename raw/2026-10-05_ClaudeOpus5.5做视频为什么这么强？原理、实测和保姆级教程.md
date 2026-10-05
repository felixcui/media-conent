# Claude Opus 5.5 做视频为什么这么强？原理、实测和保姆级教程

**作者**: AI工具进化论

**来源**: https://mp.weixin.qq.com/s/v58I7Rn5ImgOlzc19WgU8A

---

## 摘要

Claude Opus 5.5 做视频强，是因为它不直接画像素，而是写网页代码描述画面、逐帧截图再用 FFmpeg 合成，从而保证文字清晰、数据准确、可重复渲染，适合信息类视频。其代码能力、视觉理解、长上下文和成本优势共同支撑了这一能力。实测显示，不用 Remotion、HyperFrames 等框架和 skill，反而可能比套用官方 skill 效果更好，作者通过同一首歌和插画制作三个版本进行了对照。

---

## 正文

AI工具进化论 AI工具进化论

在小说阅读器读本章

去阅读

9 月 22 日 Opus 5.5 发布以后，X 上被一类视频刷屏了。

15 秒的动态图形视频，文字飞入，图表生长，转场丝滑。配文都差不多：「一句提示词做的」。

我这段时间也一直在用 Claude 做视频。下面是给开源书「高性价比人生指南」- howtolivebetter 做的宣传片，82 秒，9 个场景。我觉得挺满意，基本不需要修改就能发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ofvKmnZC1iaLAnaIRXV8GyOYK0pHFV5iaIeiaZBSv4HvqvJjPMbBMiaZxgPQSNoX2CLiaatpDejicXkyVrrW3s5N4MS8ARgKI282TUq08tUMIFBdk/640?wx_fmt=jpeg)

这篇讲三件事：它为什么做视频这么强，用不用 skill 差别有多大，以及怎么从零做一条。

## 💡 先搞懂：它不画像素

Sora、SeeDance这类视频模型，是直接「画」出每一帧的像素。

Opus 5.5 写的是代码。它用网页技术描述每一秒画面上有什么、怎么动，再让浏览器一帧一帧截图，最后用 FFmpeg 合成 MP4。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ofvKmnZC1iaL4Tic4NIFZrrTswUYnicrvU9rTYuGNMl6ZMyE7AINeW4Y1wQVSLPxIqdO2cR5pnAjoicaPe47bsKD0qSibEwYY7C1kEVRVnFKCQB4/640?wx_fmt=jpeg)

好处很实在： **文字永远清楚，数据不会错，改一个字重新渲染就行，每次结果都一样** 。

做不了的是真人实拍的质感和电影级光影。所以它最适合做信息类视频：宣传片、知识讲解、数据可视化、片头片尾。

## 🚀 Opus 5.5 为什么做视频这么强？

写代码做视频，水平取决于三样东西：写代码、看图、干长活。Opus 5.5 这三样都涨了一大截。简单理解就是，模型能力足够强，它很多事情都能干好，而不只是写写代码。

**1\. 写代码更强** 。Terminal-Bench 4.0 测的是在终端里完成真实编程任务，Opus 5.5 拿到 66.4%，上一代 Opus 5 是 52.3%。一条 15 秒的动效视频，有人晒出过约 8700 行代码。写得多，还得写对。

**2\. 能看懂自己做的画面** 。它可以先渲染几帧截图，自己看一眼，有问题再改。Roboflow 的视觉评测里，Opus 5.5 在 59 个模型中排第 3，是 Anthropic 视觉最强的模型。

**3\. 能干长活** 。一条视频是个小项目：分镜、旁白、配音、时间轴、动画、渲染、返工。Opus 5.5 的上下文有 100 万 token，单次最多输出 12.8 万 token，中途不容易断。

**4\. 更便宜更快** 。每百万 token 输入 4 美元、输出 20 美元，官方说综合成本比 Opus 5 降了 40%。有人算过，一条片大约 0.66 美元，不到 5 块钱。

## ⚡ 实测：用框架和 skill，还是放开让它写？

Remotion 和 HyperFrames 是两个主流的代码做视频框架，都出了官方的 Claude Code skills。skills 相当于给 Claude 的专业说明书。

按理说用上框架和 skill，效果会更好。但我用下来的感觉正好相反。

我做了一个对照实验。需求只有一句：做一个类似《生活大爆炸》片头的视频，偏动漫风格，欢乐、节奏感强。

同一首 32 秒的歌（Suno 生成），同一批插画，全程让 Opus 5.5 做了三个版本：

① 不用框架、不用 skill：把前两个框架和 skill 都删掉，让它别参考之前的代码，用自己的能力重做

② HyperFrames 版：用 HyperFrames 的 skill，从 Remotion 版移植过来

③ Remotion 版：用 Remotion 和它的 skill

先看全片。每张图是从视频里均匀抽的 12 帧。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaIeUV5S9Q9JLibdofYMia2BVg3KprAaAdCDB3PgoR9uYSCJcSTUqGeZvphrUPR0YSmZL3gtRXRqibFHw9FcHuPmO7FcHibMslzdNjc/640?wx_fmt=jpeg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaI7sha1ChEIv10wQJbpY5xmQeqYJy7mVIACJsW1YFdQwyP0Hx4k3OdnzHic9bbpqQDzreNmickmXiazIHQ4VCa3ibHISsI4w0a8TSY/640?wx_fmt=jpeg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaJtycIySZPEYaIoEPicKiaIgDrytuOUF3swGoFacsxCbibkv9QYFdFd8eqgRibdorKFaE0mLuVX8mL2CCxUOq987vOPCibnuJpMSwOA/640?wx_fmt=jpeg)

把同一时刻的三个版本并排放：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaKTXwqcux8y4qE7rTH6icRsibDyTcyZ8f3GOqLvAEXD8DgV8DDh1RHOyqu1ZJAj2Aia6CicRHqVyldIVvPTR4Gw3gXN5loZt4NuSYY/640?wx_fmt=jpeg)

差别一眼就能看出来。

我只要求了偏动漫风格，具体怎么做都是它自己定的。不用框架的版本做成了漫画分镜，写了 723 行 Python，一帧一帧画出来。每个场景单独写一个函数，用上了分格、对白气泡、拟声字、印章、故障特效。

用框架的两个版本，都是「全屏插画 + 底部字幕」这一套，从头到尾一个版式。HyperFrames 版是从 Remotion 版移植的，所以两版长得很像。

挑同样四个时刻放大看，更明显：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaJwUjKmkU8WKGnQugnic04gsicuB8ibvZPiaMkoQQtvH6AHK2WLZiaMzyiadoGdXmE1Rpy7yHkhLXHkagT6SIPYiclalxUU4sZMvpU8ew/640?wx_fmt=jpeg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaKXSYib1ZW7PiaXzZ7EQcbZvE2750odgoO5LictQyPESMJoZv21bfriciboicAoSglmerOiaWMfPkJFQh9knBA9gwchMQGo9kic5PVCaqU/640?wx_fmt=jpeg)

我的感受是， **用 HyperFrames、Remotion 这些框架和 skill，怎么做都有一点 PPT 和模板的感觉** 。不用它们，整体的设计感和节奏都更自由、更多样。

我的理解是，框架、skill 和现成的项目写法，会把 Claude 拉回「最佳实践的平均值」。四平八稳，但大家做出来都差不多。

当然，放开让它写也有放开的代价。

**一是可控性差一些** 。它想怎么做就怎么做，你很难预判结果，改起来也没有统一的结构。

**二是缺少一些最佳实践** ，部分文字的可读性不太好。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ofvKmnZC1iaIFwKOWuuRaYtXVoRlrReR0rcgRXuXKGGbFLkZrhPe9sTJuamM151EnWnGq1BVtiaiaTewZwZnkjeqOkxS87ZZsgtPEVTCApMIHk/640?wx_fmt=jpeg)

左边是不用框架的版本，还没唱到的歌词是浅灰色，在白色气泡里看不太清。右边是 Remotion 版本，粉色字压在浅色背景上。可读性最好的是 HyperFrames，它的字幕条有底色，自带检查也会查对比度。

还有个细节。不用框架的版本里，所有随机效果都按时间固定了种子，画面只由时间决定，每次渲染结果都一样。用代码做视频最重要的这条规矩，它也守住了。

**所以我的建议是：不用框架和 skill，或者只给它几条最基本的规矩** 。底线守住了，设计让它自由发挥。

需要稳定交付、批量出片的时候，再上框架和 skill。

## 🔧 Remotion 还是 HyperFrames？

如果要用框架，这两个怎么选？我让 Claude 用它们做了同一段 6 秒的竖版视频，最后一帧几乎一模一样（左 HyperFrames，右 Remotion）：这个 demo 对比其实有点简单，画面看不出差异，主要是工作量和渲染时间的区别。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ofvKmnZC1iaLs8o7cYkEp4AbDYicgMxOy9b2DZZhXjqsxXFARf2J5AaXFbMiaXrOxiaHRvQrbru1s0bKO0mJnK8AC62vm4cjeRtCWwrtJDNnMRI/640?wx_fmt=jpeg)

|  | HyperFrames | Remotion |
| --- | --- | --- |
| 写法 | HTML + CSS | React |
| 同样效果的代码 | 45 行 | 159 行 |
| 渲染 6 秒视频 | 约 6.8 秒 | 约 3.9 秒 |
| 自动检查 | 布局、动效、对比度 | 只有代码检查 |
| 费用 | 完全免费 | 4 人以上公司付费 |

简单说： **做单条视频选 HyperFrames，批量出片或者嵌进网站选 Remotion** 。

## 📝 教程：从零做一条带配音和 BGM 的视频

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ofvKmnZC1iaI2SaNGn5qmcTF61sSbXw9Eicib6t4ibbp6SHSC3W3lgQSVs3t3nt01LC7IfRJSXCfXbicBqZT8DH0bKQPwiafQYTljtwI1stRHgqlQ/640?wx_fmt=jpeg)

### 准备工作

装好三样东西：Node.js 22 以上、FFmpeg、Claude Code。

Claude Code 在 Mac 上一行命令安装：

```
curl -fsSL https://claude.ai/install.sh | bash
```

Windows 在 PowerShell 里运行 `irm https://claude.ai/install.ps1 | iex` 。

### 第一步：接入 Opus 5.5

国内直接用 Claude 官方 API 比较麻烦。我推荐 Hongmacc 这个中转站，国内能直连，Claude Code、Codex、Gemini 都能用。

注册地址：https://hongmacc.com/signup?ref=HONGMACC-4A20839E <sup>[1]</sup>

在控制台复制密钥，然后在终端里设置：

```
export ANTHROPIC_BASE_URL="https://hongma1.com"
export ANTHROPIC_AUTH_TOKEN="你的密钥"
claude --model claude-opus-5-5
```

想让它一直生效，Mac 上把前两行加到 `~/.zshrc` 里。Windows 用 `setx` 设置同名环境变量。

### 第二步：准备配音和 BGM

配音和 BGM 我都用 kie.ai，一个 key 就能调 Suno、TTS，还有各种图像、视频模型。

注册地址：https://kie.ai?ref=46d0a6cc6361af6da00f9433dc92e890 <sup>[2]</sup>

拿到 API Key 后在终端设置：

```
export KIE_API_KEY="你的 kie key"
```

这两个模型我都实测过：

- 配音：Gemini 3.8 Flash TTS。中文没问题，70 个音色，能用一句话描述语气，比如「活泼的科技博主口播」。
- BGM：Suno V6。选纯音乐模式，30 秒的轻快电子乐，24 秒就生成好了，一次给两首。

调用代码不用自己写。告诉 Claude「用 kie.ai 的 API 生成配音和 BGM，key 在环境变量 KIE\_API\_KEY 里」，它会自己查文档、写脚本。

### 第三步：写需求，先要分镜

新建一个文件夹，在里面启动 Claude Code，发这样一段提示词：

```
帮我做一条 30 秒的竖版视频，主题是「AI 做视频的原理」。

- 风格：深色背景，橙色强调色，设计和节奏自由发挥
- 配音：用 kie.ai 的 Gemini 3.8 Flash TTS，音色 Kore，活泼的科技博主语气
- BGM：用 kie.ai 的 Suno V6 生成 30 秒纯音乐，音量压低
- 字幕跟着配音走，场景时长按配音长度自动算

守住这几条底线：
1. 画面只由时间决定，不依赖真实时钟和随机数
2. 中文字号不小于 40px，文字和背景对比度要够
3. 渲染前先截几帧关键画面自己检查
4. 重要文字留在安全区内
5. 渲染后用 ffprobe 确认分辨率、时长和帧率

先别写代码。先给我旁白和分镜表，再挑 4 个关键画面描述一下，我确认后再做。
```

注意，这里没指定框架，也没让它用 skill。设计交给它，底线写清楚。

分镜不满意就直接说，改到满意为止。这一步改的只是文字，几乎没成本。

### 第四步：自检、返工、渲染

分镜确认后，回一句「开始做」。

它会自己生成配音和 BGM，写动画，截图检查，渲染成片。

看片时发现问题，直接用大白话说：

- 「第 3 个场景的字太小了，放大一倍」
- 「转场太快了，慢一点」
- 「BGM 有点吵，再小声一点」

它改完重新渲染就行。

## 🕳 几个踩坑经验

**1\. 中文字体要写清楚** 。告诉它用系统里的苹方或微软雅黑，不然可能渲染成方块或默认字体。

**2\. 视频素材要重新编码** 。网上下载的素材关键帧间隔大，渲染时会卡帧。用 FFmpeg 转一遍，加上 `-g 30 -keyint_min 30` 。

**3\. 时间轴跟着配音走** 。别手写时间，不然改一句文案，后面全乱。

**4\. 浅色字是重灾区** 。不管用不用 skill，都让它截图检查一下文字对比度。

## 最后

以前做一条 80 秒的动效宣传片，得会写脚本、配音、剪辑、做动效，基本要找专业的人。

现在我要做的，主要是想清楚要讲什么，再跟 Claude 来回改几轮。

**做视频的门槛还在，只是从「会不会用工具」，挪到了「能不能说清楚你想要什么」** 。

可以先从一条 15 秒的小视频开始，试试那条刷屏的提示词：

```
做一条 15 秒的动态图形视频，展示你作为动效设计师有多厉害，就像简历里的作品集。
```

记得别加 skill。做出来了，欢迎在评论区晒一晒。

ps. 文中 Hongmacc 和 kie.ai 的链接带了我的邀请码。

---

**相关数据来源** ：

- Anthropic 官方发布 Introducing Claude Opus 5.5（2026-09-22）：anthropic.com/claude-opus-5-5
- Roboflow 视觉评测：playground.roboflow.com/models/anthropic/claude-opus-5-5
- 单条视频成本估算：Hugging Face Blog《How to Make Videos with Claude Opus 5.5》
- HyperFrames：github.com/heygen-com/hyperframes
- Remotion：remotion.dev

---

如果这篇文章对你有帮助，请随手点赞、在看、转发三连，可以让更多小伙伴看到；如果你想第一时间收到推送，也可以给我一个星标⭐️，感谢你的支持。

---

**关于作者**

Ben，ALL in AI 出海

- 前字节 PM
- WaytoAGI 从 1-10 策划人，AI 编程区主理人
- AI 编程实践者，上线了 30+ 产品

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过