# 分享 6 个最新我自用的 Skills，WorkBuddy/Codex/Claude一键安装。（附提示词）

**作者**: 大刘

**来源**: https://mp.weixin.qq.com/s/ZFIgLVoj0-hHnpThoGM2YA

---

## 摘要

文章推荐了作者近半年最常用的6个AI Agent Skills，覆盖计划、设计、审核、执行、汇报等场景，适用于WorkBuddy、Codex、Claude Code等工具，并附有一键安装提示词。文中重点介绍了grill-with-docs（通过多角度提问帮助细化需求并整理成文档）和show-me（将文字方案转为HTML页面以便高效审阅计划）两个Skill的用途与安装方法。

---

## 正文

大刘 大刘

在小说阅读器读本章

去阅读

![大刘品牌动图](https://mmbiz.qpic.cn/mmbiz_gif/J1Cdba5GUc2kCewBCAdiauRZaMVKUOmpse0sia4azINh8DVrRVTUia7sMBiciamqVma6W45aX89iabdRmficxS0Awa95FiaX5EaXs9TVVK0sh3t5MU0/640?wx_fmt=gif&from=appmsg) ![DALIU · AI 品牌字标](https://mmbiz.qpic.cn/sz_mmbiz_png/J1Cdba5GUc3VbpfNNVz2UicRQhe27KcAQNB2cfedXQgty8d5iapvc4Y2KLtkzZXpv8PV5LRux7F0VnQYO6yE8RNk9rRa3nx4k6whWgSFEjIhI/640?wx_fmt=png&from=appmsg)

想推荐最新最优质的 Skill 很久了。

今天，就推荐给你这半年，我用的最多的 6 个 Skills。

老的那些 Skill 我们就不说了，相信大家也都看腻了。

覆盖计划、设计、审核、执行、汇报几个场景，即使其中有比较小众的，但是我保证，绝对精致且有品。

如果你用 WorkBuddy、Code或者Claude Code，或者任何 Agent 工具，建议你都装一下。

一键安装的提示词，我也放在文末了。

好了，我们直接开始。

1.

grill-me / grill-with-docs。

第一个，来自 Matt Pocock 的 skills 仓库。估计大家经常刷到光头哥的 Skill。

这个仓库在 GitHub 上大概 30 万 star，grill-me 在 skills.sh 上的安装量，140 万。

本质上这两个 Skills 他们是同一个，用途是帮我们把一个没有成型或者没有考虑完善的想法，拆分成多个问题，提供很多角度让我们细化想法或者需求。

![mattpocock/skills 仓库首页，能看到 star 数和仓库简介的那一屏](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc326COm9zrJvjOd3QicgwDdhmNBcCs8FUBeUWLgjltKHBnl9qoWMyCYBsW0A1JfOicD0ic8tysEuboWkeDicCVExzZRHgbqDWW9bFo/640?wx_fmt=jpeg&from=appmsg)

看过我之前文章的朋友应该都知道，我不厌其烦的强调，在每个任务开始之前一定要把需求整理清楚。就是这个Skill做的事。

简单区分以下两个skill，grill-me 就是直接问你，grill-with-docs 内核也是grill-me，只不过他会持续把确认的问题整理到一个文档里面。

我推荐，无脑用 grill-with-docs 就好。

作者自己在 README 里也说了，这俩是他最受欢迎的 Skill，每次要改东西之前都该用一下。

装法，在你的Agent里说：

●●●

帮我安装skill：  
npx skills@latest add mattpocock/skills --skill=grill-with-docs  
npx skills@latest add mattpocock/skills --skill=grill-me

2.

show-me。

这个就相对比较小众了。

但是是我非常喜欢，非常有 Taest 的Skill。

解决的问题很痛很痛，相比大部分人都遇到了。

就是，我们经常用Agent做计划，经常就会产出一个几百上千行的计划，不知道你看不看审不审，反正一般我是下定决心看，但是看个十行，就看不下去了。

但是这样的后果就是，做到后面发现计划有问题，就只能重头来过。

所以 show-me，顾名思义，就是把文字的方案以 html 的方式展示出来，让我们以更舒服的方式审计划。

比如说我有个这样上万字的 plan。

用这个skill之后就会出来一个html，把所有重点需要我关注的内容展示出来。

它的 README 第一句话，我很喜欢。

你没看到的渲染，就等于不存在。

特别是前端设计，简洁现代风、活泼年轻风、高贵鎏金风，让他 show 出来，我们才知道好不好。

装法，在你的Agent里说：

●●●

帮我安装skill：npx skills add https://github.com/charlie947/show-me --skill show-me

这个项目还挺小众的，star 刚过一百，好东西是真没多少人知道。不过其实这种思路的skill很多，我比较偏爱这种比较克制高效的skill罢了，所以，也推荐给你。

另外 HumanLayer 家也有一个同名的 show-me，更偏讲代码，调用树、文件树、流程图那种，写代码的朋友可以两个都看看。

3.

frontend-design。

其实 frontend-design 这个，已经大名鼎鼎了，Anthropic 官方出品，skills.sh 上 100 万安装。

不过有个信息差，我觉得很多人不知道。

网上流传最广的那个版本，什么禁用 Inter、Roboto、Arial 字体，禁用白底紫色渐变，那是去年 12 月的旧版。今年 6 月和 9 月，Anthropic 把它重写了两遍。

新版的思路换了。

它让 Agent 把自己当成一家设计工作室的设计负责人，这家工作室出名的地方，就是给每个客户一套独一无二的视觉。

先搞清楚这个产品是干嘛的、给谁用的，搞不清楚就先问你。然后它不直接写代码，先出一份计划，定四到六个有名字的颜色，挑一两种字体，对布局先拿字符画个线框，着需求自己审一遍，再动手。

其中比较核心的其实就是线框设计这一块，很多广告公司或者海报设计公司，都有一个线框设计的阶段。也基本是所有高级感的基础。

比如这些设计都是遵循这样的规则。

之前安装的朋友，更新一下。

没安装过的朋友，这里安装：

●●●

npx skills add https://github.com/anthropics/skills --skill frontend-design

4.

mono-color。

这是我最近在设计上比较喜欢的 Skill。

AI 生的图，你一看就能认出来，饱和度拉满，光影油腻，每张都像在拍广告，看多了是真的腻。

mono-color 采用的是完全相反的逻辑。

它做的是那种单色、双色印刷感的编辑风图片，就是你在独立杂志、孔版印刷海报上看到的那种，暖白的纸底，网点照片，大块留白，字排得很克制。

效果会是这样。

特别适合做广告、海报、杂志等等场景。

除此之外呢，我也推荐大家可以看看这个Skill的设计模式，从设计系统到 Skill 构建逻辑，都是比较精致的。

以及其中的设计系统。

装法，在你的Agent里说：

●●●

帮我安装skill：npx skills add https://github.com/yanliudesign/mono-color-skill --skill mono-color

5.

ip-as-logo-skill。

顾名思义，为 IP 生成 logo。

绝大多数情况下，高级好看的logo都是遵循的纯色、单一设计、IP加持的逻辑。

那么这个skill，我觉得是在这方向做的比较克制高级的存在。

看看case。

推荐给大家。

装法，在你的Agent里说：

●●●

帮我安装skill：npx skills@latest add s1dashu/ip-as-logo-skill

6.

dashi-ppt。

最后一个，PPT。

其实PPT这个行列里面有非常多优秀的skill，比如说大家比较熟悉的 guizang-ppt-skill、ppt-master 等等。

我觉得这个skill可以作为一个补充。

他的优势就是，生成的ppt，是直接可以改的，可以导出为 pptx 格式文件的。

风格上也比较多主题可选。

装法，在你的Agent里说：

●●●

帮我安装skill：npx dashi-ppt-skill@latest

最后。

不管你是WorkBuddy、Codex还是Claude Code，都可以用这个命令，一次性全部安装。

●●●

为我安装以下Skills。  
npx skills@latest add mattpocock/skills --skill=grill-with-docs  
npx skills@latest add mattpocock/skills --skill=grill-me  
npx skills add github.com/charlie947/show-me --skill show-me  
npx skills add github.com/anthropics/skills --skill frontend-design  
npx skills add github.com/yanliudesign/mono-color-skill --skill mono-color  
npx skills@latest add s1dashu/ip-as-logo-skill  
npx dashi-ppt-skill@latest

其实大家也看出来了，我推荐的这些Skills，基本都是沿着痛点解决问题的。

实际上好的skill，都这样。

那遇到我们很多 skill 解决不了的场景，那么从痛点出发，造一个 skill，就是最正确的路径。

如果你也有用得顺手的Skill分享给大家，欢迎评论。

实际上，除了Skill外，我还有巨多让我自己都觉得精彩至极的 Prompts，如果大家有需要的话，后续也整理分享给大家。

祝大家食用愉快~

以上，既然看到这里了，  
如果觉得不错，随手点个赞、在看、转发三连吧，  
如果想第一时间收到推送，也可以给我个星标⭐～  
谢谢你看我的文章  
你的关注是我持续更新的动力～

我是谁

我是 AI大刘，北大毕业，大模型研究方向，腾讯犀牛鸟，先后在腾讯、百度的大模型研发部门。现在斜杠青年：给多家国企做AI顾问 \\ OPC \\ 研究员 \\ 产品独立开发者 \\ Vibe Coder

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过