# Pi Agent深入浅出：OpenClaw底下那层，极简四工具是怎么跑起来的

**作者**: 全金属外壳AI

**来源**: https://mp.weixin.qq.com/s/EYsByaiFm21Rs7B-kfrAUA

---

## 摘要

关键细节： • 文本和常见图片都能读；图会进附件（可自动缩小） • 默认会截断：大约 2000 行或 50KB 量级——防止一次 read 撑爆窗口 • 大文件靠 offset/limit 分页读，而不是假装「全文件永远塞得下」 模型侧的正确用法是：先缩小范围，再精读。全金属外壳AI 全金属外壳AI 你跟终端里的 Agent 说一句：「登录页点提交没反应，帮我查。

---

## 正文

全金属外壳AI 全金属外壳AI

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I0RpvpvRJ8O0er6ibFA6sdXHsn1QEnejZTPTFH5kIIMFEYqvgjaibqjHIoHPibibryIx8icPXxmvkXBDAVoGfU5Cwib2Us9nfXYpNiacJiamXlUsnm8/640?wx_fmt=png&from=appmsg)

你跟终端里的 Agent 说一句：「登录页点提交没反应，帮我查。」

屏幕上开始刷文件路径、diff、命令输出。很多人以为中间是魔法。其实没有魔法。

模型在想。本地在干活。结果再塞回模型。想不动了就停。

Pi 把这件事做得特别干脆：默认只交给模型四样工具——read、write、edit、bash。OpenClaw 火的时候，很多人追小龙虾外壳；底下转工具、调模型、撑会话的那层，常常就是这套循环。

这篇不写产品简介。写清楚一件事：这四个工具，在一轮任务里到底怎么跑起来。

---

一

先把「跑起来」画成一张图

忘掉「Agent 很聪明」这种空话。Pi 里真正转的是这个环：

```
你输入一句话
    ↓
系统提示 + 历史消息 + 四个工具的说明书  →  发给模型
    ↓
模型回一条助手消息，里面可能是：
  · 纯文字（讲完了）
  · 一个或多个 toolCall（要干活）
    ↓
本地运行时按名字找到工具 → 校验参数 → 真正执行
    ↓
把结果写成 toolResult，追加进上下文
    ↓
再发给模型……直到 stopReason 不是「还要调工具」
```

三层分工，记这张就够：

| **层** | **包（现名）** | **干啥** |
| --- | --- | --- |
| 说话 | pi-ai | 统一多家模型的流式接口；文本 / 思考 / toolCall 事件归一 |
| 转圈 | pi-agent-core | Agent Loop：调模型 → 执行工具 → 回写结果 → 再调 |
| 干活 | pi-coding-agent | 默认挂上 read/write/edit/bash，会话、压缩、扩展、TUI |

OpenClaw 之类产品，多半是在最外层再包聊天频道、权限、记忆。心脏仍是：模型提调用，本地执行，结果回灌。

模型从不直接摸你的磁盘。它只是在消息里写：我要 read，path 是某某。真正 fs.readFile / spawn 的是你机器上的 Node 进程。

这就是「四工具怎么跑」的第一句话：跑的是循环，不是某一个按钮。

---

二

用一个假任务，把四工具串一遍

假设你说：

> 登录按钮点了没反应。先定位，再修，再跑相关测试。

下面是机制上常见的一串调用（真实顺序会因模型而异，但形状差不多）：

第 1 轮：摸清战场

2\. read：打开可疑组件，必要时带 offset / limit 只读一段

3\. 模型看到 toolResult：哦，提交函数里少了 await，或者校验提前 return 了

第 2 轮：动刀

4\. edit：用精确字符串替换改那一小段（不是整文件重写）

5\. 若文件不存在或要新建：write 一把写完

6\. bash：npm test -- login 或项目里真实的测试命令

第 3 轮：收口

7\. 测试挂了 → 再 read 失败输出 → 再 edit

8\. 测过了 → 模型输出一段人话总结，stopReason 变成正常结束

你会发现：没有「调试工具」「测试工具」「搜索工具」这些专名，也能走完。因为：

• 搜 ≈ bash（rg/grep）或扩展里的 grep/find（只读工具集里有，默认四件套之外可开）

• 看 ≈ read

• 改 ≈ edit（小改）或 write（大改/新建）

• 验 ≈ bash

Pi 的极简，不是能力残缺，是：把专名压成组合。 组合靠模型编排，执行靠本地四个（加可选只读）原语。

---

三

四个工具分别在干什么（深入，但不玄乎）

1read：把文件「喂」进上下文

参数大致是：path，可选 offset（从第几行）、limit（读多少行）。

关键细节：

• 文本和常见图片都能读；图会进附件（可自动缩小）

• 默认会截断：大约 2000 行或 50KB 量级——防止一次 read 撑爆窗口

• 大文件靠 offset/limit 分页读，而不是假装「全文件永远塞得下」

模型侧的正确用法是：先缩小范围，再精读。乱读全仓库，循环还没修好，上下文先死。

2write：新建或整文件覆盖

参数：path + content。

• 父目录不存在会先建

• 覆盖已有文件——所以它是「重写/落盘」，不是外科手术

适合：新文件、模板生成、内容几乎全换。 不适合：只改三行却 write 整文件——又贵又容易无声丢改动。

3edit：精确替换（这是手感的核心）

参数：path、oldString、newString，可选 replaceAll。

硬规则（官方工具行为）：

• 精确字符串匹配，不是正则

• 找不到 oldString → 失败

• 找到多处且没开 replaceAll → 失败

• 成功时往往带 unified diff，方便人眼核对

为什么故意这么「笨」？因为笨才可控。模糊匹配一错，半个文件被改歪，循环后几轮全在擦屁股。

edit 逼模型先 read 出真实片段，再原样抄进 oldString。这是 Agent 改代码里最朴素、也最稳的纪律。

4bash：把终端变成万能接口

参数：command，可选描述。

关键细节：

• 在工作目录的持久 shell 里跑（环境变量能延续）

• 输出可流式回传

• 同样截断：大约末 2000 行或 50KB；太长时完整输出可能落临时文件，上下文里只留尾巴

所以：测试、安装、git、rg、curl，全是 bash。Pi 默认不内置「后台 bash」——长任务官方态度更偏向 tmux 这类你看得见的会话，而不是黑盒挂起。

---

四

循环里还有三件「看不见但要命」的事

1工具结果必须回写给模型

执行成功或失败，都应该变成 toolResult 消息进上下文。 文件找不到、参数校验挂、被 hook 拦住——更好的做法是 isError: true 写回去，让模型改计划，而不是进程直接炸。

UI 上你看到的「红字」，和模型下一轮看到的「错误结果」，最好是同一件事。只展示给人不回写模型，循环就瞎了。

2并行可以，副作用要串

一条助手消息里可以有多个 toolCall。只读的 read / 搜索类，常可并行；带写盘、带依赖的，要串行。

Pi 的实现味道是：能并行就并行，但 toolResult 回写仍按原始调用顺序，避免模型看到乱序上下文。

3截断是特性，不是 bug

read 和 bash 都截断。因为 Agent 死法第一名永远是：工具输出把窗口灌满，后面几轮开始遗忘目标。

极简四工具能撑住 OpenClaw 级用法，有一半功劳在这：结果管道自带节流。

---

五

会话树和压缩：循环跑久了怎么不塌

只讲四工具不够。循环一长，还有两样配套：

会话是树，不是一条直线。你可以 /tree 回到之前节点再分叉：旁支去修坏掉的工具或试另一条路，修好再回主线。旁支用摘要接回来，主上下文少掺垃圾。

上下文会压缩（compaction）。接近窗口上限时，旧消息可自动摘要。扩展还能自定义「按主题压」「换模型摘要」。这是薄 harness 能跑长任务的另一半。

再加一句交互：Agent 跑着时，Enter 是转向（steer，当前工具结束后插入，后面排队工具可跳过）；Alt+Enter 是跟进（follow-up，等这轮自然结束再问）。你不是只能干等到结束。

---

六

装上，只为验证你看懂了循环

```
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
# 或：curl -fsSL https://pi.dev/install.sh | sh

cd /path/to/repo
pi
```

```
Summarize this repository and tell me how to run its checks.
```

盯屏幕：有没有 bash/read，有没有截断后的长输出，最后有没有人话收束。 那就是循环在跑。项目约定放 AGENTS.md（也认 CLAUDE.md）。

安全： 默认权限≈启动它的用户，没有细粒度弹窗。真要边界，上 Docker / 文档里的沙箱方案。

---

七

和 Cursor / Claude Code：比的是「谁在转圈」

|  | **Cursor** | **Claude Code** | **Pi** |
| --- | --- | --- | --- |
| 你主要看见 | 编辑器里改代码 | 厚 CLI/产品能力 | 薄循环 + 四工具 |
| 工具哲学 | IDE 工作流 | 内置很多能力 | 原语组合 + 扩展 |
| 模型 | 多，但产品意见强 | Claude 为主 | 15+ 厂商，会话中可换 |
| 适合 | 日更业务 | 开箱强、少拧螺丝 | 看懂循环、控成本、嵌 SDK |

选型人话：

• 要 GUI 手感 → Cursor

• 要 Claude 成品车 → Claude Code

• 要看清「模型怎么调工具」、要自建外壳（OpenClaw 那类）→ Pi

多数人该并存，不该宗教站队。

---

八

我的判断

第一，懂 Pi，是懂所有 Coding Agent 的捷径。换皮不换骨：都是「模型发 toolCall，本地执行，结果回灌」。Pi 把皮剥到只剩四根骨头，适合当教具，也适合当底盘。

第二，四工具够不够，取决于你会不会组合。不会组合的人觉得残缺；会组合的人觉得清爽。缺的能力，用扩展 / Skill / pi install 补，或让 Pi 当场给自己写扩展再 /reload——这是它和「功能清单越来越长」的产品最大的差别。

第三，别被「极简」骗去生产机裸奔。薄 harness = 你承担更多边界责任。先侧项目、先便宜模型、先看截断和错误回写，再谈主力迁移。

---

参考链接

• Pi 官网：https://pi.dev/

• Quickstart：https://pi.dev/docs/latest/quickstart

• 仓库 earendil-works/pi：https://github.com/earendil-works/pi

• 内置工具 API（read/write/edit/bash）：https://badlogic-pi-mono.mintlify.app/api/coding-agent/tools

• Armin Ronacher — Pi 与 OpenClaw：https://lucumr.pocoo.org/2026/1/31/pi/

• 原理拆解教程（Agent Loop / 工具）：https://how-pi-agent-works.vercel.app/

• Nader — 用 PI 包分层搭 Agent：https://nader.substack.com/p/how-to-build-a-custom-agent-framework

**\-END-**

更多 **Cursor、Codex、Claude Code、Skills、MCP** 相关的教程、配置和踩坑记录，持续更新中。

关注公众号 **未来的回响** ，看深度解读与版本追踪。  
加入知识星球 **AI工具实战派** ，获取精校版文章 + 完整命令、配置文件与扩展案例。

**【限时开放】** 欢迎加入 **AI工具实战派** 交流群一起学习进步～

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I0RpvpvRJ8MxkvLQibgVdEbQorD2ThRvFiag308m7jIrqKOMq4a1AHDNVV66FVts2tm7rJPA7ScR8WenGkvAmXnibgEmVgAkxxOKeuuu7qc2lc/640?wx_fmt=jpeg)

**AI编程、AI运营、工具资料分享** 请加入知识星球

![](https://mmbiz.qpic.cn/mmbiz_jpg/xFbsATlObBKKtKmzU94ezBKA7kn1W8XCs1r6oRibDNG4rVV516OrHNZY8oNFKAbRP3rsicfe2VU0SpCwBznic4sww/640?wx_fmt=jpeg)

**\-推荐阅读-**

**【AI编程】**

- [Cursor+Gitlens再也不用担心频繁重建项目了](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483693&idx=1&sn=cffa5e0542c912297387ee2637b98cee&scene=21#wechat_redirect)
- [使用Cursor时如何规避AI改坏代码——终极指南](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483699&idx=1&sn=7fbd243a6357d8f15e526b2a3126af5a&scene=21#wechat_redirect)
- [Cursor编程bug反复改不好⁉️让AI用思维链整理思路](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483705&idx=1&sn=7a3658d619cf882f4f2ccd1919d69f71&scene=21#wechat_redirect)
- [怎么从Cursor转到Claude Code？配合GLM-4.5的性价比AI编程指南](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247484341&idx=1&sn=d3d70b3522d175c9448a66f2fc0daef6&scene=21#wechat_redirect)

**【AI设计】**

- [AI设计对话指南（第一期）：一文掌握20个主流UI组件库，让AI秒懂你的设计意图！](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483978&idx=1&sn=28e4853177c30b4bbadf1acb8ac276dc&scene=21#wechat_redirect)
- [AI设计对话指南（第二期）：19种UI设计风格速查手册](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247484010&idx=1&sn=5f4773a2ffb1df2b62adb01b167f84d8&scene=21#wechat_redirect)
- [AI设计对话指南（第三期）：UI设计提示词指南，减少与AI掰扯](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247484219&idx=1&sn=e4841d0987003f0d722fd3ff3a495a2b&scene=21#wechat_redirect)
- [如何使用Magic MCP生成好看的UI](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483898&idx=1&sn=325483d6c635e779b6cc0f105daaf69e&scene=21#wechat_redirect)
- [如何使用Magic MCP生成好看的UI（第二期）](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483920&idx=1&sn=29ae0739dff846d72c9792291aedc23d&scene=21#wechat_redirect)
- [如何在Cursor中使用Figma MCP自动进行产品原型设计](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247484042&idx=1&sn=769e7881f49ae4529025bdb434d55c1e&scene=21#wechat_redirect)

**【AI工具】**

- [【2025最全】12个顶级MCP服务器资源汇总，Cursor/Claude/AI开发者必备](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483865&idx=1&sn=9998131d2ac940084fefbfb8224206fa&scene=21#wechat_redirect)
- [简单介绍一些常用的MCP服务器，快用来提高Cursor干活效率吧](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483825&idx=1&sn=a6138244d10a05c96520a1dffaff9528&scene=21#wechat_redirect)

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过