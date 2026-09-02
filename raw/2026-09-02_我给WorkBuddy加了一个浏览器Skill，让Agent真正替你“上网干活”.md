# 我给 WorkBuddy 加了一个浏览器 Skill，让 Agent 真正替你“上网干活”

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/NFMi7P5ydebcBpfcGsbOrA

---

## 摘要

文章介绍了作者为WorkBuddy开发的浏览器Skill，让AI Agent能够自动化执行日常办公中高频、流程固定的浏览器任务。通过两个实际案例展示了其能力：一是自动在BOSS直聘上复用登录态、搜索并收集30个AI Agent岗位信息，整理成Excel并生成数据看板，快速完成招聘市场分析；二是从参考网站中学习并提取UI设计token，应用于自己的项目。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyRe1bp0A2m4Wy7kOgDxkbEq6b0M4AYaRgJP1m6vxKrDXShY4430LvUeIfoHu10dCkdI5Aco8dfq5k6uQOCN44Jo9VrjDzlxCSE/640?wx_fmt=png&from=appmsg)

在日常办公中，我们有大量工作都发生在浏览器里，比如查看后台数据、填写表单、下载资料、收集热点……，其中不少操作，每天都在重复。

这些事情并不复杂，但要花不少时间。那么这些杂事是否可以交给Agent来帮我们完成呢？

当然是可以的！

带着这个想法，我最近也梳理了一批高频、且流程相对固定的浏览器任务，然后让workbuddy帮我把这些事情给干了。

这篇文章，就聊聊有哪些场景可以用、如何用、主流方案有哪些，它们的原理又是什么。

## 案例

首先我们先来看几个通过Workbuddy驱动浏览器自动化操作的实际案例。

### 案例一：AI Agent招聘岗位分析

目前市面上对于AI Agent的岗位需要非常多，但是招聘的标准并不统一，这里我们借助Workbuddy + BrowserSkill 自动去招聘网站获取岗位数据，并分析出主要的要求是什么、薪资范围在哪个区间。

提示词如下：

```
/BrowserSkill 打开我已经登录的BOSS直聘，搜索“AI Agent 开发工程师”相关岗位，帮我收集成都最近发布的30个有效岗位。把岗位名称、公司、薪资、经验学历要求、岗位职责和任职要求整理成Excel。最后分析一下，现在企业招聘AI Agent工程师最看重哪些能力、要求会哪些AI工具，以及传统前端、后端开发想转型AI Agent开发最应该补什么。
```

任务发出去之后，它立马打开了招聘网站，登录态复用了之前的，并在搜索框中输入了“AI Agent 开发工程师”，然后开搜索。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyQVjg2hAz1FObuaC4gHoFjMV8Zvd4tD5NSHoNk74PKibt6ov1PqI8waRSBMef4jjkH0mM3nYQXyPibbKaFiaR8GtPvcWIuh6tgicmM/640?wx_fmt=webp&from=appmsg)

最后拿到了30个岗位信息，并生成一个Excel文件，分别记录了所有的岗位信息和关键数据统计分析。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySBA4CkD30NC5b0GtzaWH5SzzeUkR2QCXgwOv0yZ8wmPiavWaTp00fOjmx2nVwkwrkwJVEEoO9Kic9A5sKrbvU49uicgEJSmJK69k/640?wx_fmt=webp&from=appmsg)

如果觉得看起不够直观，我们继续让workbuddy基于这个统计概览表，生成一份数据看板，提示词如下：

> 基于统计概览帮我生成一个数据看板

最终效果如下，我们可以清晰看到关于AI Agent开发岗的数据指标，找这块工作的同学可以重点关注下图中的信息，重点关注薪资范围、高频技能要求、企业要求的工具矩阵、核心洞察。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQehkbHdeKia1pFLhGxofYQ8GZnUGOMPgHDxjI2BxzufFOxwJBlpHCNO8KO1ibdbMClKReibV0eZlJD9Vx3wSf3WbIHyCbcH2Vu40/640?wx_fmt=webp&from=appmsg)

得到这样一份基于真实岗位数据的分析报告，如果靠人工去招聘网站找这些信息再总结，估计得花不少时间，但是通过Agent + BrowserSkill也就10多分钟的事情，并且我可以不定期去分析，看看市场要求是否在发生变化。

### 案例二：提取参考网站的UI设计风格

在用Vibe coding开发自己的工具时，都希望界面更加美观，但是又没有设计经验，审美能力又不行。即使安装了一些UI设计美化的Skill，效果还是不尽人意。

这里更好的方案是：找到一个你喜欢的网站风格，然后让Agent去这个网站学习它的UI风格，并提取网站的设计 token，包括颜色、字体、 间距 、 圆角 、 阴影 、动效等，再把这套设计语言应用到自己的项目中。

比如我们使用workbuddy执行下面这段提示词：

```
/BrowserSkill 打开这个页面https://huaban.com/materials，学习它的UI设计风格，提取站点的设计 token，包括颜色、字体、间距、圆角、阴影和动效，并输出一份设计规范文档
```

workbuddy就会利用浏览器自动化工具打开目标网站，分析页面的视觉样式，并将提取到的信息整理输出一份规范的设计文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRmXnEZUtVdaopTAmvXb28RgFSADS96Z2ZXAIrvSggvXCRmUe8RwbQiaOZth5sBIYndSENcjMrB7sNicVzXGICghsmxpJDIUnXt4/640?wx_fmt=webp&from=appmsg)

然后我拿着这份设计规范文档，继续让workbuddy按照设计规范生成一个静态的素材网站，提示词如下：

```
根据这份设计规范帮我生成一个静态的素材网站，使用html+tailwindcss实现
```

生成出来的效果如下图，相比直接让 Agent 自由发挥，基于成熟网站的设计语言进行创作，整体视觉效果会更加统一、精致，也更具专业感。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyS43lWibfItEWS3E4bygAniaQf3drkaiaUt30wpiabvmuFNGy3JOt4WMMAo0UgUCjTY5VBMFZaX6b2roGuGibROwJktpgbe5V96LSG4/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyRHREtRBpn11P1yuJv3YbjDic9SDkJf5F7Fq6Ebh40eLHic8siaCPuM76ssiauqic5vbmfDjPkhKjTtqItGDValQakclJr9GHhLQm3Y/640?wx_fmt=webp&from=appmsg)

### 案例三：小红薯爆款作品分析

这里我们让workbuddy去小红书上面获取关于 AIGC 这个关键词的高赞作品。提示词很简单：

> 帮我获取小红书上关于AIGC点赞最高前5条笔记

从界面上可以看到，Agent正在控制，它先是打开了小红书页面，然后搜索AIGC，并设置筛选条件为点赞最多，然后分别获取点赞最高的五条笔记的信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTNpsG6dmnyaZAFOGdX3MF01909lOu1OvYgRoWIkgLXHqe6Jib8ibm9a02drAQxiatnooSQUGeWL21jNOmrgDVWXKsjZ6MUv3aIQ8/640?wx_fmt=webp&from=appmsg)

最终，它把拿到的5条笔记进行汇总并输出，在此基础上，我们可以进一步进行作品分析，甚至去获取作品下的评论数据，提取用户的真实需求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyQW44grMewg7ibaBUH1hdpyM7wSO7kdbpvfmmJKjnrsKBNgamK6iapng41Gc7tRcWNEd5ic65riana1f0eBPX476HPzJSic471x7ckw/640?wx_fmt=webp&from=appmsg)

### 案例四：让 Workbuddy 按验收标准自动测试

使用 Vibe Coding 开发功能时，Agent经常会不做验证就认为任务已经完成了。但是代码能运行不等于功能可用，页面中可能仍然存在按钮无法点击、表单校验失效、流程无法闭环等问题。

对于这种情况，我们可以提前写清楚验收标准，并要求 Agent 完成开发后，使用 浏览器自动化工具 模拟真实用户进行自动化测试。只有所有验收项全部通过，任务才算真正完成。

比如，开发一个登录功能时，可以这样描述：

```
帮我完成用户登录功能，并按照以下标准进行验收：

1. 输入正确的账号和密码后，可以成功登录并进入首页；
2. 密码错误时，页面需要显示明确的错误提示；
3. 账号或密码为空时，不能提交表单；
4. 连续点击登录按钮，不应重复发送请求；
5. 登录成功后刷新页面，仍然保持登录状态。

功能开发完成后，使用 BrowserSkill 在浏览器中逐项测试。记录每一项的测试结果；如果发现问题，继续修改代码并重新测试。只有全部验收标准通过后，才能结束任务。
```

这样，Agent会形成一个完整的工作闭环：

> 编写代码 → 启动项目 → 操作浏览器测试 → 对照验收标准检查 → 修复问题 → 重新测试

Workbuddy最终交付的质量就会更高。

## 如何让Workbuddy支持自动化操作浏览器？

上面我们介绍了一系列的应用场景案例，大家可以结合自己的工作情况，看看哪些场景是很适合用这种方式来做的。

那么接下来，我们看一下如何让Workbuddy支持这种能力？

方案有很多，主要形态包括Skill、MCP、CLI，这里我们以BrowserSkill为例子，上面案例都是基于这个完成的。

这里简单说下BrowserSkill ，它是腾讯开源的一个智能浏览器自动化工具，让 WorkBuddy 能够像人一样操作网页，自动填表、点击、翻页、截图，完成任何需要浏览器的复杂任务。

安装步骤很简单，在Workbuddy工作台选择技能，搜索BrowserSkill，点击安装，这里只完成了第一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAyTtfP0cS4JXfthpNR0eLvDjCo7wChWPkUn0OpChasnp9gicsp2nLmWAYhia6cyPbQu575abt447icDJdM0eiavm6n9YeqsJf26xpeg/640?wx_fmt=webp&from=appmsg)

然后我们新建一个任务，输入 `/` 就可以调用BrowserSkill了，并输入我的指令：

> 帮我打开京东，定位到我的订单页面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySrDSN5bhEbFcZyx3PZZ1kGMflt4Xhgc7XjgGibwRic6ibRqVucwgDwkWIPLYjibnE1AYWBRynx1DyKm7hYyCblq0pHcVnvy2k74icw/640?wx_fmt=webp&from=appmsg)

根据Workbuddy的回复，它自动帮我安装了bsk CLI，但还需要我们手动安装一个浏览器扩展插件，然后打开提供的链接地址，来到如下页面：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRbQKrJqziavp0gIQZNnI6UicHQMpfMRPjMUs8Mh4nDiaOPFCbcfJUXy3fzFKnpIdCiaZU4qWyiaWYNtO2w7llYeY3icAKh8ib4bxCZQI/640?wx_fmt=webp&from=appmsg)

点击添加至Chrome按钮，在弹出的弹窗内点击添加扩展程序，这样就插件就安装成功了，接着再把扩展固定到浏览器右上角。

操作也很简单，直接点击右上角的扩展图标，再点击BrowserSkill的图钉按钮。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTy9IavGg76vfqCRkMXLiaeqn5DtNPTxUrMksMbr6nld8icecrBTqvAZR3nq3OcnNwicFWxMw3pE8e7nQZJHvJq7usT73uhYSz5fs/640?wx_fmt=webp&from=appmsg)

这样浏览器的扩展栏就能看到这个扩展图标了，点开可以看到一个开关，确保显示已连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Uzn2S5AAySQhIxBzjkLiaancX3rK4fHPyicYAiaXkKDPRCnMK0DSKmqYVuficRwSIy9OlfQ5vFzKHibKiboFznxW3ibtAOH9gkOVv1alibJhU08XBQ/640?wx_fmt=webp&from=appmsg)

到这一步就说明浏览器扩展已经连接到了本地服务。接着回到WorkBuddy，回复已安装扩展。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyRcCaES8FdyCRBVCOC5c7546scnVvZDH8gdzkaNyLibyUk81HyAoBrkzibc5961WFHCe7TLHickoCMWg4IjzPu7AQgvCFNIuTRkfg/640?wx_fmt=webp&from=appmsg)

Workbuddy就能顺利的操作浏览器去完成我们的任务了。

## Agent操作浏览器的原理是什么？

我们在更进一步来看。

从上面的安装过程可以看出，通过BrowserSkill让Agent控制浏览器自动化操作，需要准备三个组件，分别是：BrowserSkill、bsd CLI、浏览器扩展插件。

它们分别负责什么？为什么装了Skill，还需要安装命令行工具和浏览器扩展？

带着这些疑问，我又看了其他方案，发现选择还真不少：Agent-browser、Browser Use、Playwright、Puppeteer、Kimi WebBridge、Midscene等一大推。有的提供 MCP 接入，有的通过CLI并搭配 Skill 使用，还有需要依赖浏览器扩展插件，配置视觉模型、或者使用Computer use 等

各种方案名词一大推，越看越懵，于是我先把这些工具、名词放到一边，从一次具体的任务入手，系统性梳理了背后的工作链路。

Agent控制浏览器本质上像是在模仿人的行为，看一眼页面，点击一下，然后继续观察。

实际上，这里可以拆成是一个循环：

> 接收任务 → 读取页面 → 判断下一步 → 执行动作 → 检查结果 → 继续或结束

整个过程我们可以拆分为三个问题来看：

1. 谁决定下一步做什么？
2. 怎么执行操作？
3. 怎么理解页面？

对于第一问题很好理解，所有的决策都是由大模型来控制的。

### 怎么执行操作？

关于如何控制浏览器执行操作，这里有三种方式：

**第一种是通过浏览器调试协议，从外部控制浏览器。**

CDP，全称是 Chrome DevTools Protocol **，** 就是其中一种代表性协议 **。** 浏览器开一个给程序连接的调试端口，外部程序连上它就能指挥浏览器干活了，比如控制导航、刷新、点击、获取页面信息、截图等。我们看到的Playwright、Puppeteer 这些框架走的都是这条路，它们是基于CDP的上层封装，但并不是另一条路径。CDP这种方式能力是最全的，但目标网站能察觉到你在用程序控制，容易拦截。

**第二种是通过浏览器内扩展程序**

控制代码作为扩展跑在浏览器内部，直接操作页面，再通过一个本地服务把能力开放给外面的 Agent。它最大的优势是登录状态和你本人操作时一模一样，因为它就在你日常用的那个浏览器里。

我们前面的安装例子就是使用的这种方式，它的整个调用流程如下：

1. Agent 发起任务：通过 `bsk CLI` 下发浏览器操作指令，CLI 将指令交由本机 daemon 处理
2. Daemon 本地转发：Daemon 将请求安全地传递给浏览器扩展
3. Agent Window 隔离执行：扩展在独立的 Agent Window 中完成自动化操作，不触碰用户日常窗口；必要时向用户发起借用（Borrow）请求，使用已有的标签页
![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAyTTZbgUl8WQkJZh9pmH4rltHKRUbXBd8RHUz1hVN0Whic1vkbgp9yHaCHlfM126CowF1RU5sicibEGmt1lVwERsCzcDJuNpPiaKnicc/640?wx_fmt=webp&from=appmsg)

理解了这里的原理，我们应该很容易理解前面安装BrowserSkill的时候，为啥要安装bsk CLI和浏览器扩展了。

**第三种是操作系统层，在电脑桌面上模拟鼠标键盘，或者截屏给模型看。** 网站察觉不到程序控制的痕迹，因为确实没有走任何协议通道。代价是每走一步都要截屏加识别，比前两条慢得多；窗口大小、缩放比例、页面遮挡，任何一样变了，原来记好的点击位置就失效。

### 怎么理解页面？

要让 Agent 操作浏览器，首先得让它知道： **当前页面上有什么，哪些地方可以操作。**

拿到页面信息，有三种方式，分别是 **获取页面DOM树、获取无障碍树、页面截图。**

其中DOM树就是整个页面结构、内容的表达，它包含的信息是最全面的，但是它也包含了大量的html嵌套标签、css样式，以及其它无关的内容，对于大模型来说，上下文可能会很快被占满。

而无障碍树，它原本是帮助屏幕阅读器理解网页的，重点描述元素的角色、名称、能不能操作和具体的值。比如：

> 这是一个输入框，标签是订单编号，当前的值是空的，可以输入。

它拿到的信息相比DOM树会更加精简，但是非常依赖于页面是否写得规范，如果一个图标按钮没有提供名称，或者输入框没有提供相应的语义信息，仅靠无障碍树，Agent 也无法理解。

截图则提供的是页面渲染后的视觉结果，直接让 大模型 看页面长什么样子，比如查询按钮在哪里、订单号输入框在哪里，这些信息通过图片很直观。但是看是看得准不准取决于视觉模型的能力了，不能保证每次都能准确识别元素的位置坐标。

实际实现时，这几种方式可以配合使用，一起帮助 Agent 判断下一步该做什么。

## Agent操作浏览器的方案有哪些？

理解了前面的原理，再来看这些工具方案，就不会被各种名字绕晕了。

不过还有一个地方需要先分清楚：Skill、MCP、CLI，和前面说的 CDP、浏览器扩展，并不是同一个层面的东西。

Skill 主要告诉 Agent 这个工具该怎么用，MCP 把工具能力开放给 Agent 调用，CLI 则让 Agent 通过命令行来执行操作。

至于指令发出去之后，底层通过什么方式连接浏览器、拿什么信息理解页面，是另一回事。

所以，同一个工具可以同时提供 MCP 和 CLI，也可以搭配 Skill 使用。我们需要关注的，还是它具体怎么干活，以及这种方式适不适合自己的任务。

下面我看看几个主流的选择方案：

### 一、Playwright

Playwright 是微软开源的浏览器自动化与测试框架，它在这一波 Agent 热潮之前就已经存在了，主要解决的是通过代码操作网页、检查功能是否正常的问题，支持 Chromium、Firefox、WebKit 三种浏览器内核。

比如打开订单页面、填写查询条件、点击查询，再检查结果有没有出现，这些操作都可以写成一段 Playwright 脚本。

接入 Agent 之后，变化主要发生在上面这一层：原来由开发者编写操作步骤，现在是让 Agent 根据任务和页面情况来生成、执行这些步骤。

它的调用过程可以简单理解为：

> Agent → Playwright MCP 或 CLI → Playwright → CDP → 浏览器

这里需要补充一下， **Playwright 不能简单理解为只对 CDP 做了一层封装。** 它需要适配不同浏览器，连接方式也有所不同；通过 CDP 连接现有浏览器，是它针对 Chromium 提供的一种能力。

官方提供了两种供Agent调用的方式：Playwright MCP 和 Playwright CLI。它们最大的区别在于上下文信息的维护不一样。

Playwright MCP完整的维护了页面结构、可访问树等信息到大模型上下文中，因此上下文占用和Token消耗非常多。

而Playwright CLI 是按需读取页面信息，不会把大量的工具定义和页面内容反复放进上下文中，因此上下文和Token消耗更少。

对于Vibe Coding的UI自动化测试场景而言，更加推荐使用Playwright CLI 。

### 二、Chrome DevTools for agents

这个工具是 Chrome 团队提供的，安装包的名字是 `chrome-devtools-mcp` 。

它既能操作网页，也能把 Chrome 开发者工具里的信息开放给 Agent，包括网络请求、控制台报错、性能分析等。

它的主要调用过程是：

> Agent → Chrome DevTools MCP → Puppeteer／DevTools 能力 → Chrome

它比较适合的一类任务是获取浏览器控制台的信息。

比如点击页面查询按钮后，页面一直没有结果，这时候，我可以让 Agent 检查：请求有没有发出去？接口返回了什么？控制台有没有报错？

因此，对页面调试、接口排查、性能分析这类开发任务，可以优先考虑它。

### 三、Browser Use

前面两款分别是微软和谷歌开发的，大家用的都比较多。 **而Browser Use 是这几个工具中，Github Star是最多的** ，目前有110k+，排第二的是 Playwright，95.3k，第三是 Chrome DevTools MCP，50k+，并且它是为AI Agent原生打造的浏览器自动化框架。

在接入方式上，需要区分两种情况：本地使用、云端浏览器。我们使用 WorkBuddy 这样的 Agent，就重点看本地使用 CLI 这条路径。

调用过程可以理解为：

> Agent 生成 Python 代码 → Browser Use CLI → CDP → 浏览器

这里有两个核心变化：

第一个是Browser Use 抛弃掉了Playwright的使用，直接调用CDP操作浏览器，速度更快。

第二个是操作浏览器的方式从过去的单个 CLI 命令，变成了直接编写脚本的方式来操作浏览器了。

直接编写脚本来执行工具可以解决多次调用工具导致上下文过载的问题，比如要从多个页面整理数据，Agent 可以把翻页、提取、去重写进一段程序，最后只返回整理后的结果。这样就有可以减少“做一步、返回一大段内容、再让模型判断”的往返过程。

Browser-use对token的消耗很低，但是执行效果比较挑剔模型能力。

### 四、Midscene.js

Midscene.js 出自字节跳动，它的整体思路又不太一样， **核心是以视觉理解驱动的** ，并且Midscene内部还有一层Agent。

我们可以用自然语言描述操作目标，它会通过页面截图识别界面、定位元素，再执行操作。对于图标按钮、自定义控件、Canvas 画布这类不容易从页面结构里读懂的内容，这个方案非常值得考虑。

比如一个按钮没有文字标签，但从界面上看，它就是右上角那个齿轮图标。我们可以直接描述“点击右上角的设置图标”，让视觉模型来定位。对于这种情况，如果依赖DOM树和无障碍树就很难发现。

另外，Midscene还支持录制功能，并且除了支持浏览器端，它还是支持操作安卓、IOS 端的APP应用。

对于视觉理解要求较高、跨端的场景可以优先考虑。

然后还有其它很多的方案，比如出自于Vercel Labs 团队开源的Agent Browser也是很好用的，专门为AI Agent打造的自动化工具。

下面我们直接看一张大表，方便对比选择：

![](https://mmbiz.qpic.cn/mmbiz_jpg/6Uzn2S5AAySlJ4b3D5e9FRWUPicq5KXDyf7SnfNddMevgibfx2PYMbCibXsJ7EBxSoiaVxxibdtq28KSAmZbmXYDYrITx6BITV8Mkh4GH0icPXaeE/640?wx_fmt=webp&from=appmsg)

## 总结

对于不同场景，没有绝对好的方案。

不管用哪种工具，核心工作链路都没变：读取页面、判断下一步、执行操作、检查结果。

关键是从高频、重复、流程明确的任务开始，并设置清晰的验收标准，把这些琐碎操作交给 Agent去做。

然后对 AI 深度学习感兴趣的可以点击：

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyTCQhJHOsXm47dGViaYFsFuuDwa5fdWE9C6gPtic8amSwGhm3aIhNyK1sCWOOiaicicwG7WpKibf6wgXcjve3eeT5n8EyE5thonzBFyk/640?wx_fmt=png&from=appmsg)**

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过