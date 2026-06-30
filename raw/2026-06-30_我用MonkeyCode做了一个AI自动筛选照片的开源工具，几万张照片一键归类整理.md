# 我用Monkey Code做了一个 AI 自动筛选照片的开源工具，几万张照片一键归类整理

**作者**: 网黑哥

**来源**: https://mp.weixin.qq.com/s/aSa8SHbeUxlZInSS2mCi8g

---

## 摘要

前两天周末，媳妇甩过来一句话：什么时候把硬盘上的照片整理一下。我一听头都大了，俩小孩十几岁了，你想想这得存了多少张照片。明明知道有些照片该删了： 拍糊的、曝光炸了的、连拍十几张只选了一张的。因为整理照片这件事，实在太反人类了。你得先双击打开，再右键删除或者拖到别的文件夹。

---

## 正文

网黑哥 网黑哥

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/ncicWtGoBHtKIia2Uq8JzQjic4ytsSRaChaaWeNqcDCf78xF5XtSibuVmQuRHHicAbmS14Boxajc1bHqSabNibjTiazOg/640?wx_fmt=jpeg)

事情是这样的。

前两天周末，媳妇甩过来一句话：什么时候把硬盘上的照片整理一下？照片太多了。

我一听头都大了，俩小孩十几岁了，你想想这得存了多少张照片。

这种情况我相信每家都有。

明明知道有些照片该删了： 拍糊的、曝光炸了的、连拍十几张只选了一张的。但就是懒得整理。因为整理照片这件事，实在太反人类了。

你得先双击打开，再右键删除或者拖到别的文件夹。几十 GB 的照片，搞到猴年马月去。所以拍的照片从来没整理过，结果越攒越多。

所以还是交给 AI 吧。

正好那几天，在抖音上我刷到了 MonkeyCode。

一个浏览器里就能用的 AI 开发工具，主打免费、不用装任何东西，打开网页就能开始干活。内置了云端开发环境，自带各种大模型，你可以直接用自然语言让它帮你写项目。

我第一反应是：又一个 AI 编程工具？ 这玩意儿能有什么不一样？

但我注意到一个点：它不需要本地环境。

不用装 Node.js，不用配 npm，不用折腾半天就因为 Python 版本不对报一堆红字。浏览器打开，说人话，它帮你把代码跑起来。

市面上新出的工具，我基本上刷到没见过的，如果觉得有亮点，都会下载下来，至少给它一个机会，跑一个案例来试试。

一开始不知道这个的背景，后来我搜了一下才知道，原来这是钉钉新上任的 CEO 陈宇森以前创办的公司长亭科技出品的，MuleRun 也是他们家的，这个你可能听过。

我寻思，正好拿这个照片筛选器的需求试试它的成色。手头就是这件事，需求足够真实，又不复杂，最适合测一个 AI 开发工具到底能不能落地。

最初的想法是做一个简单的筛图工具：看一眼，按个键，归好类，继续下一张。

就这么简单。

**开搞**

用 MonkeyCode 开始做项目的方式很简单：在输入框里打字就行。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N8yfxKBjfTCsZEhKIXJUnpYOEUF2IqjPNEkNrqI7RgEbaicUhOpZszRYIWxU4fNEhp5THKoI23BKkx5owbFR61icJ6Cfjs9Uw2lQ/640?wx_fmt=png&from=appmsg)

我直接写了一段需求：

创建一个本地照片快速筛选工具，用户选择电脑中的照片文件夹后，可以通过方向键快速分类照片。上键待删除、下键保留、左键暂存、右键精选。不要做宣传页，打开直接进入筛选工具。

然后点执行。

它就开始自己干活了。

先出了项目规划： React + TypeScript + Vite，用浏览器的 File System Access API 读本地文件，不需要后端，严格 TypeScript。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4NibUhjGD7QroZ2OhgR4l15Dw6Rg24PuCuU8b2pdeiaI9CWEJXVg7rYgW7rE4HITkW4MaVLHd1CySTeucnngUeJpbLX2U559FRWkQ/640?wx_fmt=png&from=appmsg)

说实话，看到这个技术方案的时候我还挺满意的。

File System Access API 这个选型很聪明，因为是浏览器里运行的应用，直接用 Chrome 的原生 API 读写本地文件，不需要上传到服务器，照片全程留在你电脑上。

这点其实挺关键的。谁也不想把自己的照片库传到某个服务器上去让 AI 分析，对吧？隐私这件事，心里都有数。

说回项目本身。规划完之后，MonkeyCode 没让我等太久。

**第一版**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NibwkVpSxVcuctJJvmX62IEWf7YhE9k1xJTJvmQ8HRfggtHstcQm9VFgHehG4XMwKV1ySfCLge8kVWh940ZIUFXH7jyLjkSsicuU/640?wx_fmt=png&from=appmsg)

大概几分钟，第一版就跑起来了。

系统还提供了云空间给你在线进行预览，直接点击就可以打开。

界面是暗色主题，很简洁。打开就是一个按钮，点了之后 Chrome 弹出一个文件夹选择对话框，选完它自动扫描里面的所有图片。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4Nib5TCfia5kHrNibxZFc894oFjBibibNqtr77MvibeOAqchr7sVALNxWPGgOI8EMKaDRvngvxvp5OBCp1bAHJGA604HZa8ddnSiclkJzk/640?wx_fmt=png&from=appmsg)

支持 JPG、PNG、WebP、GIF、BMP、HEIC/HEIF，基本上覆盖了主流格式。

选完文件夹，直接进入筛选主界面：

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N9Rh2S2nO3CD5dxEKC2CDyhpNpnIRoOJIDgnoHhmnPo8vR4TpbChzmgvRLvk4F48qGkpb5l4SYg1ibXb2S7ic642GQoCS9nSnXC8/640?wx_fmt=png&from=appmsg)

中央是大图预览，右边是四个方向键对应的分类按钮：红色的待删除 ↑、黄色的暂存←、紫色的精选→、绿色的保留↓。

操作逻辑很直觉：看照片， 按方向键，照片被移动到对应文件夹，自动跳到下一张。

顶部有计数器，告诉你还剩多少张没处理，已经分类了多少。底部有一个最近操作的记录，每一步都能看到刚才做了什么。

还有一个细节我很喜欢：待删除的照片不是真删，只是移动到待删除 文件夹。万一你手滑了，还可以捞回来。

有一说一，第一版到这一步，作为基础工具已经能用了。

但就算筛选方式快捷了许多，但还是太费人了，这活儿还是得让 AI 多干点。

**AI 加码**

这时候 MonkeyCode 的一个优势就体现出来了：它把模型、环境、项目文件、运行调试都放在一个工作流里。

你可以一边描述需求，一边让它改应用、补文档、解释问题。整个过程更像是在浏览器里带着一个 AI 工程助手干活。

于是我跟它说：加一个 AI 预筛选功能。让大模型先帮我看一遍照片，给出预筛选建议：哪些模糊、曝光差、重复感强的进入待删除，哪些构图好、人物表情好的进入精选。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N8HPzz4UcAN08qOkI1ThibD5iaf5rqluGdct3OqjOJJY1qbRQX9HPX8hicMq8LdqEIs0U0x10aKsmibkxGBDVdf3zaBic7ZICWBcK3Y/640?wx_fmt=png&from=appmsg)

根据我的需求，它开始改代码，没过多久，第二版就做好了。

并且自己知道提供了三种预设提示词：

• 通用分类：综合质量和内容判断

• 质量筛选：重点识别低质量照片标记待删除

• 内容优先：按内容价值判断

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NibcbJh950F2vBItWLA8gR6eq6u6WWbZ0ePGCpz4XLYiajmnqMtibSHNFpp95KibZkLqI1N1c13DPaZcHI14Htr29ngQvxkSMBHcEI/640?wx_fmt=png&from=appmsg)

这个我可没教它，这一点很适合新手上手。

当然，也可以完全自定义提示词，按照你的个性要求进一步筛选。

最后，我给它加上了接入 API 的接口配置：

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N836icnuDQ1CzfaTU5eGu9BSPlhYNnZcquiaxlsLXSTdjXAibmjEemC796bjEcUf9TfaLJepdFCxfZXajQ9PpMOQicT08xZrFp0gHk/640?wx_fmt=png&from=appmsg)

可以选 AI 服务商，我就预设了几个，阿里千问、OpenAI、DeepSeek、SiliconFlow、Google Gemini 都支持。填上 API Key，，我当时用了阿里的 qwen-vl-plus，这是去阿里百炼白嫖来的。

配置好之后，点击 AI 预筛选，它就开始逐张分析照片了。

**AI 的表现**

说实话，跑起来之后的效果，比我想象的好。

比如这张：对焦不清楚，明显是废片：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4N9V8OmrbWK0HHkwZwXUfX8kSoftcoaSX23FxU7SicorL2YDWJEBrBibIAb0MrKuibTxPu7iaicnj4WlWG4UYiaXpR87U9buOWFK49CO8/640?wx_fmt=png&from=appmsg)

AI 直接给了待删除建议，理由是：严重的运动模糊，导致主体无法辨认。

再看这张：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4NicS7lRW0DibGjWDU218r8ibEIxrcowDA8u5slg65QygzhJQbRfyia02sR4iaQq8kQkHlGo2YU0ghFBCmNFXSIicyvJzFsQ5Qfr45teE/640?wx_fmt=png&from=appmsg)

AI 给了暂存，理由写的是：照片质量尚可，构图有自然美感，但整体色调偏暗，建议暂存后再判断。

这个判断我觉得靠谱。这张照片确实不算差，但也不够好到进精选。

AI 理解构图有美感但色调暗这件事，本身就说明视觉模型的语义理解已经到了一定水平。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QK9bGpA4N9G33iazPnAUSaRy16UJCGTCdrlnSsyOtrN34X9RmAJpxl0ZpBz4JsaVxFfytianeI44OM0yDe9h9BrX571GyGnKtwATOhTz62js/640?wx_fmt=png&from=appmsg)

再看这张，我只能说 AI 是懂看图的。

**批量结果**

等 AI 初筛把照片都扫完，出来的批量结果页长这样：

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N8OWSuRMGJ1gnUmibgSksy8d04GvOkjzNbGbu6JglBlIdgBvn1KcWUDaIsDktgdmiaWyYlbeibnGcFATZK4L9PeZGwrgbf1p4LZXw/640?wx_fmt=png&from=appmsg)

省了你大量去筛选低质量照片的时间。

然后，你再去每个分类文件夹下面，再去人工手动筛选，当然，就是前边提到的方向键快速筛选图片。

到这里，我心里已经给这个项目打了个 70 分。从一个几万张照片不想动的痛点，到 AI 先筛一轮、我只需要审核重点，这个效率提升是实打实的。

最后，考虑到用起来大家会问 token 用量，就又加入了一个 token统计功能，跑一次任务花了多少，心里有数。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N9hTSoa5ONqicEWdvTWJrYJ7m3EuSfYjpPgwpEIBCBQZRqkHjsIfwic4TiaZWhMdOYkEJkMHTXhBznqmNgiadMXMiatXAO46HDAO2r0/640?wx_fmt=png&from=appmsg)

这个最小版本的功能已经跑通了，基础功能确实都可以用。后续有时间的话，我还会再加上一些细化的功能。

这次的项目我已经发布到 GitHub 上，目前还有些简陋，但基本功能是可以用的，重点是如何去把握筛选的标准，这个需要慢慢调试，感兴趣的同学可以去试试看。

github.com/aiolosking/photo-quick-filter

**聊聊MonkeyCode**

接下来说说这次的干活小能手 MonkeyCode，值得单独拿出来说一下。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4NictYsbbRibsbrvLoEJlC2AS1N2LC292mhLHGeF1icqfXAw5qyYukmbfo0rlf7icaAO5zHV0cksWukf0EcfAVNRGDeJdgnPcKacjX0/640?wx_fmt=png&from=appmsg)

它支持的基础模型每天有 3000 万免费额度。 3000 万 tokens 什么概念？大概够你一天不停地跟 AI 对话，做几个中等规模的项目绰绰有余。

想用更强的模型？可以用积分换。国产的热门模型 都支持，看里面提到的这个不知名的极致模型，看版本号是 5.4 和 5.5，我感觉有点熟悉，你懂吧。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4Nica44xNQTWp2AwiciaxzJuyOxT78b2EELd4rTicFBRrsqKYgcET2vtibw4UC494W0qHSPAalsX4qicGwPcVhLF6y6rHmzkhcMptZ1T8/640?wx_fmt=png&from=appmsg)

同时支持绑定个人配置模型，可在对应配置模块填写模型 API Token 完成绑定，支持主流大模型的接入适配。

![](https://mmbiz.qpic.cn/mmbiz_png/4QK9bGpA4N96HHvj4zezRgpVI8lXYnsOW3TXBH6Flkiboh13pU6OWYtXzib8HWD5F2O2vicbjUMwKwEhqRdG78SVhWPrtH2cgM8a8gn7Q8HhOA/640?wx_fmt=png&from=appmsg)

说实话，目前市面上 AI 编程工具很多，但把免费用顶级模型和云端开发环境一起打包的，确实不算多。大多数要么月费不低，要么免费版模型能力阉割得厉害。

MonkeyCode 这个基础模型每天 3000 万免费额度的打法，对个人开发者和小项目来说，是真的香。

这是在线环境地址，大家都可以去体验一下。

monkeycode-ai.com/?ic=019ecab5-3250-7cf9-927d-15a761c1270c

另外还有开源地址：

github.com/chaitin/MonkeyCode

开源这件事，比单纯用一个在线工具的信任感高了一个维度。你能看它怎么实现的，能自己部署，能 fork 一份魔改。

新版本还支持离线部署，适合对本地环境、数据安全、私有化更敏感的用户。在单位内网或者自己服务器上跑一套，数据不出门，放心。

**结语**

整个项目做下来，我的感受其实不是 AI 帮我写了几行代码。

而是：一个生活里的小需求，从算了太麻烦了，变成了打开浏览器、半小时搞定。

这种体验上的变化，比技术参数更重要。

以前遇到类似的需求， 比如整理照片、处理表格、写个内部小工具、做调研文档。

大部分人的反应是忍一忍，或者找个现成的工具凑合。因为从零开始做太折腾：装环境、配依赖、查文档、写代码、调试……这一套下来，小需求早就不值得了。

但 MonkeyCode 把这件事的成本压到了极低：打开浏览器，说人话，它帮你把项目跑成。

如果你也有类似的小工具需求，可以试试。反正免费的，又不亏。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过