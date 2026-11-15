# DeepSeek Harness成了第一个让我上瘾的Agent

**作者**: 董道力 王兆洋

**来源**: https://mp.weixin.qq.com/s/zFgb_EUXWimu-mjwvBeCqg

---

## 摘要

DSH 和任务型 Agent 的差别在于它是**一张敞开的工作台**：不是帮你把一件事做完，而是**可塑性高到让你随手就想动手改**。作者给了三种玩法：**从零手搓插件**（如 AI 阅读助手）、**基于现有插件二次改造**、**把任意 GitHub 项目一键转成 DSH 插件**；插件之间可以联动，最后沉淀成**个人工具箱**，每折腾一次都是在积累而不是一次性消耗。生态数据（官方披露）：第三方插件已破 **3.5 万个**，约 **60% 的活跃用户**做过或装过至少一款第三方插件。

---

## 正文

董道力 王兆洋 董道力 王兆洋

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatSPSzGA4bUYe186rtqU2UIXe4oV58EjnKpVPLKbT6JA2VuLdj6Z8IcMB51rH1icmnXVnXibcibaHmrhgXJgmGPzVypfYnxz08jgIc/640?wx_fmt=png&from=appmsg)

作者 *｜* 董道力（微信ddl941110）  
编辑 *｜王兆洋（微信Geisterspiele）*

用了 DeepSeek Harness（DSH）一段时间后，最大的感受并不是它的能力有多强，而是它能激发一种让人“随时想 build”的冲动。

通常来说，没有想聊的话题，我不会打开 Claude，没有要写的代码，我也不会点开 Codex。唯独面对 DSH，我几乎无时无刻不想打开它，在上面随手 build 点什么。

原因可能在于，无论是 Codex、Claude Code，还是国内一众 Agent 工具，本质上都是“任务导向”，帮你把手头的活干完。而 DSH 更像是一张敞开的工作台：插件是手边的零件，缺了什么，还能让 Agent 当场手搓一个，看到什么有趣的项目可以直接用起来。

这种“手痒感”源自 DSH 极高的可塑性。任何跑通的功能都能顺手沉淀成插件，再加上原本就丰富的插件生态，让你每次折腾都不是一次性消耗，而是在不断攒厚自己的工具箱。

到底怎么在 DSH 上 build 出属于自己的趁手兵器？结合最近的高频实操，我把自己的玩法拆成了几个部分：从零手搓插件、站在现有生态上做二次改造，以及最爽的，把任意 GitHub 项目一键变成 DSH 插件。

1

**从零手搓：缺什么零件，就让 Agent 现场造一个**

我日常工作中，需要大量的阅读，并且希望将阅读过的文章沉淀下来，作为知识库。

其实市面上的解决方案很多，像 ima 、cubox、notion 等，但它们要么订阅价格不低，或者功能冗余或者缺失。

这时候 就能用 DSH 做一个。

在 DSH 的创造模式下，只需要提出大致需求，“做一个 AI 阅读助手，功能大概是，可以打开任意格式的一篇文章，左侧是文本内容右侧是 AI 解读。”

然后 DSH 会在侧边栏的工具部分生成一个入口，这一步在我体验其实挺重要的，如果这个入口是脱离 DSH 的网页或者应用，大概率用过两次就会躺在浏览器收藏夹里吃灰（经验之谈）。特别是之后如果要和其他工具联动，东一个入口，西一个入口，很麻烦。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatS3uVETNtibsJFxwk5o69PAvQvJOgQeAbzPzxwECR0KUSEhrZFzJGxjicUeiaSHltSgnkMicIYlic37fWcA1XhMjbjQG79GtCLCW1A4/640?wx_fmt=png&from=appmsg)

当然，DSH 插件开发肯定不会一次成功，这部分和 Codex 一样，反复对话就能解决。比如增加翻译、摘要、写作手法分析等功能，都是几轮对话就搞定了。

亮点是 DSH 插件之间的互动。

前文说了，我希望能将我阅读的文章沉淀下来，这就需要一个知识库，我让 DSH 搜索了一下 Karpathy llm wiki，复刻一个下来，并且要求将知识库和AI 阅读助手联动，让看过的文章可以直接保存到知识库中。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatTicBLIyibpxLN1lP50LSZyiaB0lgjib1vTEaB8OpDNjiae562ow0FFmZTgTp0D5OyADtvma4BgLRHB9xD50q4l19h7meSegCHib2vBg/640?wx_fmt=png&from=appmsg)

DSH 作为平台的优势就来了，非常丝滑的在 AI 阅读助手那里增加了一个存入知识库的按钮。不需要考虑跨平台适配，文件保存等等问题。

抛开这些麻烦，我就有精力向外扩展了不同的信息来源，制作了一些插件，像专门搜索 AI 公司新闻的 AI 情报台，转录采访/发布会的AI 访谈档案、AI 对话收藏等。这些插件最终会汇聚到知识库中，随时可以调用。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatTEPia3BrAHW5xVqvx23At9HCMYWZUnwWdiaCNBe2Iwmflia3kEdjlBFk2Dh3NJSwctbH6LxkQQN5Te5LKDAhaa0V0gwwWTGpU1uA/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatS5XfE9icGMWGCxgQS7yr4dVq9KtX0EgcqIDJTnv6etT2q2KzefwnaC0eWicCTSo9NWf17sEUFUXGsZH8wGibGIYoKwF5lqNfY6tk/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatSdbrlhfhjb0ibRGNia1bTElzYoTzsjNRNOv6sVzIJg2pVbNjeHvg83gpicQmtbibicE6FrTRkvngWIGibVicL7DiaarpLX27l37YdL3OE/640?wx_fmt=png&from=appmsg)

其实上述的插件/功能，有很多现成的方案，或者用 Codex 也能轻松做一个出来，但将他们关联起来本身就是一个麻烦事情。 DSH 依靠插件形式解决了关联问题，让开发变得更加丝滑，只需要关注功能。

1

**站在生态肩上：DSH 的强大生态**

接下来不得不提的，是 DSH 庞大的插件生态。根据官方披露的数据，DSH 的第三方插件数量已突破 3.5 万个，约 60% 的活跃用户都制作或安装过至少一款第三方插件。

这个生态让我受益良多。毫不夸张地说，市面上绝大多数以“纯功能”为导向的 AI 应用，只要不像腾讯那样握有社交关系链、或像字节那样手握内容池护城河，你几乎都能在 DSH 的插件生态里找到平替。

比如前阵子很火的 Grok Bot，很快就有团队在社区里做出了同款的 DSH Bot。

但光有还不够，要让这些功能更适合自己，这时候就可以魔改第三方插件。

比如最近“Agent 记忆 ”很火，在 Codex 或者 Claude 里记忆通常就是一个.md，想一笔笔改还挺困难，从 0 开发个记忆功能也没那么简单。

DSH 插件生态里就有很多关于记忆的插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatTmd86cbubW8qY3Fvq5XLsZ7X8HSUDDD2k7TjUiaeNiaPW6ufOrV9z7onueHXu0jweA0jiclqYkeC0xdQYzbZDuDia0zFAVKdhdARc/640?wx_fmt=png&from=appmsg)

我就下载了个排名比较靠前的“MemOS #memos -local-plugin”，随后让 DSH 在这个插件基础上制作了一个名字叫“关于我”的记忆插件，读取了我所有 Codex 的记忆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatQiaePDSz2hia8lqIRBBV8ShGpPdibyUXwpK4Bu1GrqiaEmmo69mTElaQdQgYeLuwicYicJDnheDf6nMqaqEyoZ1LzUkLgPg3bJ4eJFE/640?wx_fmt=png&from=appmsg)

但 Agent 记忆技术变化很快，比如前两天 Anthropic 就发布了篇大模型做梦的技术博客。

这时候只需要用最简单的提示词，告诉 DSH “anthropic 最近发布了一个 大模型做梦功能？可以增加优化记忆，帮我添加在“关于我”的插件中。”

可以看到， DHS 非常丝滑的将做梦功能增加到插件里。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatSrwYtjrTIviaiaSc2Sy5zSVE5PqEu2ibz9RC0S624UxJibFMW3OtAWBCLP7wHewJz4qP7fKLibicwMhl7UriaRibQEBpXX8ZoUOtNcnl8/640?wx_fmt=png&from=appmsg)

没有人比自己更懂自己要什么，大佬提供的插件作为优质的底座，在此基础上开发一些更适合自己的功能哪怕是 UI，如果有能力还能反哺社区。

这也是 DeepSeek 的知名度带来的优势。像 OpenCode 也有插件功能，但其生态是一点点长出来的。而 DSH 靠着 DeepSeek 这块招牌，发布当晚就冒出近三百个插件仓库，想动手的人一下子全涌了进来。

1

**DSH 另一个生态其实是社交媒体**

不知道大家有没有过这样的经历：刷短视频、翻公众号时，冷不丁撞见一两个特别惊艳的开源项目，偏偏人不在电脑旁。放在以前，最多截张图，在手机上随口问问 AI 这项目是干嘛的，之后多半就躺在相册里不了了之，时间一久，连项目名叫什么都想不起来。

但自从装上 DSH Go（一个能用手机遥控桌面端 DSH、也能控制手机的第三方插件），这件事就彻底变了：现在我在手机上刷到什么好项目，家里电脑的 DSH 侧边栏里，很快就会自动多出一个复刻了该功能的插件，安安静静等我回去用。

举个例子，前几天刷短视频，我刷到好几个效果很炫的 Code2Video 项目，像 Remotion、HyperFrames、DrawAI。我人在外面，只是随手截了张图扔进手机端的 DSH Go，让模型自己去识别图里的项目信息，并直接在桌面端把它的核心功能封装成一个新插件。等我回到电脑前，工具已经就位了。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatQHtVI90UqnCA1tO4WekqKz9g8IBzLxs4pw5feAxmzGKA1qz2nB0raVYzOyrmtVSHPLLZDicmpXOgDh54v7Bax5O9lic1wPPgvxM/640?wx_fmt=png&from=appmsg)

放在以前，想跑通一个 GitHub 上的开源项目，光是拉代码、配本地 Python/Node 环境、解决依赖冲突就能劝退一票人。现在 DSH 直接把这套脏活累活吞在了后台，交到我手里的直接是一个带 UI、随时可调的成品插件。如果试完觉得顺手，就再聊两句优化留下；要是个噱头，随手删掉也不心疼成本。

1

**DSH 本身是个插件，那就可以用其他 Agent 来“训练”**

造工具越爽，越容易犯“松鼠症”，那就连 DSH 一起改了

当然，折腾了这么久，DSH 这张工作台也并非毫无槽点。

最直观的副作用就是“插件膨胀”。因为造轮子和复刻开源项目的门槛被压得太低，用久了之后，侧边栏很容易从趁手的工作台变成堆满半成品的杂物间，很多一时兴起搓出来的小工具，新鲜感一过就沦为僵尸插件，反过来增加了日常寻找的视觉负担。再加上 3.5 万个社区插件良莠不齐，挑挑拣拣、串联调用下来，不仅得花时间帮原作者“排雷”，底层上下文的膨胀和 Token 消耗也常常让人肉疼。

但妙就妙在，DSH 连它自己的界面本身也是插件做的。这就引出了另一个好玩的解法：直接叫来别的 Agent，把 DSH 这张工作台本身给改了。

比如我的 DSH 侧边栏就是经过 Codex 优化后的样子。

那么，既然能改 DSH，那能不能“教” DSH 呢？

Codex 的computer use 能力有目共睹，基本上模型 Ultra 思考一开，啥软件都能拿来用用。我就尝试让 Codex “教会” DSH computer use 能力。

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatS71nE6S8BvLzmbmZfRHPP1X2suEPznAznlcqedY1qHeDuoQ4UoSADDGtmc8MicJbks0lY5Oq6qyxYCPjVzLZma5l1SgbicjZaJM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatTm7g6VnReMtzvVd7akZ1SticbqHkqAo3szcauLvJkzduydicDxiaYg5DG5vq8YX1zIS21CMH5zKqBNsIFkGaYh3n2oHnY3L9Fnq4/640?wx_fmt=png&from=appmsg)

从测试结果来看，打开飞书、新建个文档、排个版这些基础功能 DSH 在 Codex “调教”下一件能顺利完成。那我们也许可以畅想，让 Codex、Claude 教会 DSH 一些其他能力？

1

**写在最后**

回头看 DSH和这些插件，没一个是正儿八经“立项”做出来的，全来自平时一闪而过的瞬间：读完一篇文章想顺手存下来，刷到个炫酷的项目想上手试试，或者觉得别人的记忆插件还差点意思。放在以前，这些念头大多没有下文，截图躺在相册里，链接躺在收藏夹里，时间一久，连当时为什么心动都想不起来。

是 DSH 给这些念头接上了下文。以前从一个想法到一个能用的工具，中间隔着一整套开发流程，现在只隔着几轮对话。

这也是我管它叫“人生 Agent”的原因：工作里的活，派给 Codex 们总有干完的时候，但日子里冒出来的念头没完没了，还总挑你不在电脑前的时候钻出来。

更妙的是，这些念头最后还会攒到一起。阅读助手里留着我读过的文章，知识库里攒着我盯紧的 AI 公司，“关于我”里存着我的记忆。

现在翻开 DSH 的侧边栏，基本就能看到我最近这段时间在琢磨什么、对什么上心。

我对它越来越依赖，而无论什么Personal Agent产品，在争夺我这样的用户时，这种“上瘾”都已经让它领先了半步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gdEn3pxzatSRMlPJan8yg8eFZagVwZDEZko9eYtDUH9X46ib7upd1FqfHzEjZbZGS6cofell4jKSDRWUBCoChQ9yVaeyyN2ricmhy1VLUjZFU/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/gdEn3pxzatT7tUPtTEzRP8ywicKtv1Xp0PMtbB3rurzCUOic4Zf6nnPpevgsicHibMDIkmsUDEdC5Vfibibnkfvwe0aA7XR2WqldNnEn9b3Ud0Kt4/640?wx_fmt=jpeg&from=appmsg)

阅读原文 不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过