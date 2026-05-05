# Anthropic 公布 Claude Code 黑客松六强作品，来自医生、老师、木匠的儿子……

**作者**: J0hn

**来源**: https://mp.weixin.qq.com/s/RJOgFEajlC4hhyamHBO-hw

---

## 摘要

Anthropic公布的Claude Code黑客松六强作品显示，AI应用已告别通用聊天机器人模式，全面转向与垂直行业深度结合的实战工具。参赛者利用Claude的长文本与视觉能力解决专业痛点，例如土耳其医生开发AI虚拟诊室供医学生仿真练手并依据指南打分，法国开发者打造工具自动解析长篇原理图并在主板上画出电路诊断路径。

---

## 正文

J0hn J0hn

在小说阅读器读本章

去阅读

刚刚，Anthropic 公布了 Claude Code 比赛的六组获奖作品。

![](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnluhYyPvBjyWTydGQx1vib6kWeA5aCPs0udicYR0DSEmd0oVRxz1ScB9DXJHFoEtPDAOm5bkwW3WAatBzzw5lAhic3mBWVNnIWZk/640?wx_fmt=png&from=appmsg)

这是 Claude 和 Cerebral Valley 联合办的一场黑客松，规则是：用 Opus 4.7 + Claude Code，一周时间，做个东西出来。

看完这六个项目，我发现： **没有一个是「再做一个聊天机器人」。**

一个土耳其医生做了虚拟诊室，让医学生在 AI 病人身上练手；一个法国人做了电路板维修工具，读完 80 页原理图后直接在主板上画诊断路径；一个智利大学老师做了编程教学平台，学生不先写清楚自己要做什么，编辑器就锁着不让你碰。

还有一个智利小伙子，拿他木匠老爸三十年的手艺，训了个修墙的 AI。

下面，我们就一个一个地来看，或许会给你一些启发。

01

## AI 病人

金奖给了 MedKit，来自土耳其的 Bedirhan Keskin。

![MedKit 首页](https://mmbiz.qpic.cn/mmbiz_jpg/ZKqVLiaIpzFnXHqOR0wCOoUfrpLktxEAibOt2fZ7CiboCYeBMqayqSibpUbROWzDiclO74HbdOY3POOQlVclLYjXZJjk6lXfItYKLqy23Nd3AUuU/640?from=appmsg)

MedKit 首页

他本身是个执业医生，但过去四年一直在做软件工程。他做这个项目的出发点，来自于自己的亲身经历：

> “ 刚从医学院毕业的时候，最缺的就是实战经验。真实的病人不会按教科书来。我和很多同学刚到急诊科的时候，都挺手忙脚乱的。

MedKit 是一个语音驱动的虚拟诊室。系统会生成 AI 病人，医学生通过语音对话来问诊、开检查、看影像、做诊断、开处方。

每次问诊结束后，系统会根据最新的临床指南，给你的沟通能力、病史采集和临床推理逐项打分，每个扣分点都附带文献引用。

一些 AI 病人的例子：

一个 AI 病人说自己春天咳嗽加重、夜里喘息，医学生开始追问过敏史；另一个病人血压计显示 188/120，伴头痛，降压药停了一周；还有个肩膀疼的、一个拉肚子的……

不同的病例、不同的症状分支、不同的诊断陷阱。

技术实现上，Bedirhan 用了 Claude Managed Agents。

一个 Opus 4.7 驱动的「主治医师」Agent，同时管着病人角色扮演、观察者评估和问诊复盘三个子 Agent。

他提到 Opus 4.7 在长时间会话中不跑偏，所以他直接让 Agent 自动生成了整个病例库：病史分支、金标准诊断、评分标准，每一条都能追溯到真实存在的临床指南。

> “ 在 AI 身上犯所有的错，然后再去面对真正的病人。

02

## 80 页原理图

银奖是来自法国的 Alexis Chapellier 做的 Wrench Board。

Alexis 是个自学成才的开发者，一直在为维修行业做工具。

![Wrench Board 界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFkBGPC99yqsSs1kzLhXVkrSVHu8jzTiaKib8sHuv5NsXdlBXvMFduia6K57J9TF3wYFYyy6oHStuLIve8ydgeJ6KHNt5EQ7JRbgnk/640?from=appmsg)

Wrench Board 界面

先来介绍一个背景和数字：全球每年大约有 5000 万吨电子产品变成垃圾。

但其中很多并非修不了，而是板级维修的知识掌握在极少数人手里。

Wrench Board 想做的事，用 Alexis 自己的话来说就是：

> “ 我为「剩下的我们」做了这个工具。

你导入一块主板的照片和原理图 PDF，而原理图有时候 80 多页，密密麻麻的电路图、元件参数、连接关系。Wrench Board 用 Opus 4.7 的视觉能力分批并行读取，两分钟内，就编译成了一个可查询的电气知识图谱。

25 个元件按功能分类，33 种可观测症状映射到故障机制，10 条诊断规则，每条都有可验证来源。

然后就到了最关键的部分：你可以直接跟 Agent 对话， **它会在主板照片上一步一步画出诊断路径。**

该量哪里、该测什么值，直接标在板子上。

而且，这个 Agent 还……认识你。

它会记录你的工具清单和维修经验，如果你没有热风台，它不会让你去做 BGA 返焊，每次成功维修，你的技能档案自动升级。

而且它对每块板子也都有记忆。之前修过哪里、试过什么方案、踩过什么坑，下次打开新对话的时候全都还在。

为了防止 AI 乱说，Wrench Board 做了一层硬约束：Agent 说出的每个元件编号都必须来自工具查询，没查到的编号会被服务端过滤掉，到不了你的屏幕。

Alexis 在视频结尾说：

> “ 当一个拿着万用表的普通技术员，能做到昨天只有 OEM 售后中心才能做的事，「维修权」才算真正落地了。

项目已经在 GitHub 开源。

03

## 先想后写

铜奖是来自智利的 Paula Vasquez-Henriquez 做的 Maieutic。

Paula 是智利发展大学（Universidad del Desarrollo）计算机科学系的副主任，也是 AI 方向的博士生。

她在大学教了六年入门编程课，带过 200 多个学生学 Python。她在视频里讲了三个反复出现的场景：

一个学生从 LLM 上复制了一段代码，不知道这代码干嘛的。另一个随便扫了眼题目要求，直到测试报错才发现自己漏了什么。

而第三个，还没想清楚要解决什么问题，手就开始敲了。

三个学生都交了作业，倒是都能及格。

**但没有一个人学到了真正重要的那个东西。**

Maieutic 的做法是：写代码之前，先把编辑器上把锁。

学生得先用自己的话描述「这个程序应该干什么」，AI 读完之后会追问那些没说清楚的地方。只有当 spec 足够清晰了，编辑器才解锁。

![先想，再写](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFk1QOsibYef6ED1qxKvHalCNlPDribPuAOazjgJvYs8PvZ8ukMGHbKlicEat9n3X7rjYgByEqR3wbTL6x6hF9XvV4cfZBrjkd6GOY/640?from=appmsg)

先想，再写

编辑器打开后，自动补全是关的。学生可以问 AI 某个函数的语法，AI 会回答。但如果学生问「我该怎么做」，AI 会引导你思考，不会直接给答案。

提交代码后，AI 会把学生最初写的 spec 和实际代码对齐，让学生自己解释中间的差距：你说你要做 A，但你实际做了 B，这个 gap 在哪？

> “ 在大学禁 AI 并非正确的做法。未来的程序员，大部分时间都在写 prompt。但好的 prompt 来自于理解你要构建什么、什么可能出错、以及结果对不对。

![Maieutic 教师面板](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFmia6p4OYMcdRA1G1vjn7G4hZ8D64whQhf6qQ3F1tQc7Jg7SswE4Fggrib1rupPAUjX6cXZSrQaFSzpIiclPNFlSsCywpGKEzY1Aw/640?from=appmsg)

Maieutic 教师面板

而

对教师来说，Maieutic 还提供了一个以前不曾有过的视角：一个能看到学生「思考过程」的实时面板。

不是看分数，是看每个学生此刻卡在哪里、在怎么推理、哪些错误反复出现。

> “ 第一次，老师有了一份记录，记下的是学生到底怎么想的，而不只是答案对不对。

Paula 指出，一个好老师需要好几年才能积累出对学生常见思维误区的直觉。Maieutic 第一次布置作业的时候就能给你这个。

**因为 Opus 4.7 能分辨出学生是在「推理」还是在「猜」。**

04

## 木偶剧场

最佳创意奖，则给了来自丹麦的 Rene Hangstrup Moller 做的 Virtual Puppet Theater。

这是六个项目里，画风最为不一样的一个。

你用手对着摄像头比划，屏幕上的木偶就跟着动；你说话，木偶也说话；你说「给 Bob 戴个王冠」，王冠就出现了；你说「我们去海滩吧」，背景就换成了沙滩。

你说「给我一顶冰淇淋帽子」……嗯，它也真给你戴上了。

（你的第一反应可能是：这也太适合哄小孩了吧。）

技术栈方面拆解如下：

手部追踪用的 MediaPipe，检测手指关节的 3D 位置来驱动木偶；语音识别用了浏览器原生的 Web Speech API，免费、够用；语音合成用的 11 Labs Flash，比浏览器自带的要有表现力得多。

引擎底下跑着两个模型，共享一个缓存。

日常对话用 Haiku 保证响应速度，道具生成用 Opus 保证创意质量。有些道具是预设的 Three.js 模型，但像冰淇淋帽子这种，是 Opus 实时用基础图形组合拼出来的，你第一次说出来的时候它才去生成。

Bob（那个木偶）在视频结尾自己作的总结：

> “ 一个用于玩耍的交互界面，一年前还不存在。

05

## 木匠之子

「Keep Thinking」特别奖给了来自智利的 Benjamin Torralbo 做的 MaestrIA。

这个项目的背景故事，可能是六个里面，最让人能够记住的。

Benjamin 的父亲 Juan Rodrigo Torralbo，做了三十年木匠，其中八年在修复智利奇洛埃岛上被列为联合国世界遗产的木教堂。

但在智利的体制里，没有大学文凭，你修过再多世界遗产，你也是全隐形人。

> “ 智利有超过 28 万名非正式建筑工人，没有任何途径能展示自己的手艺。我爸修复了联合国世界遗产教堂，可没有大学文凭的他，在系统里根本不存在。

Benjamin 做 MaestrIA，就是要把他父亲这样的手艺人的知识数字化。

> “ 工具是我做的。知识是他的。

![MaestrIA 首页](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFkUHlv3tYVDmQZYMPHf8AZprlzqx9yQkic22JHPM8SRd1lGsC77ibldGia68lnjqVJuCgKINes44mSBkduqeYAKLU9LmyB0JGHdUE/640?from=appmsg)

MaestrIA 首页

使用方式是：拍一张受损墙面的照片，输入你的位置。

Opus 4.7 开始分析，而且推理过程是实时展示的，不是在转圈等。先观察，再诊断，就像一个老师傅到了现场，得先看一圈再开口。

分析完后，AI 会给你四个答案：修什么、你所在地区大概花多少钱、需要多长时间、不修会怎样。

接下来才，系统会推荐你附近的手艺人。

选一个之后，第三个 Agent 自动帮你写一条 WhatsApp 消息，用智利本地西班牙语，附上完整诊断报告。

> “ 你不再是一脸懵地跟工人说「我墙湿了」。你手上拿着诊断报告。客户不会被乱开价，有手艺但不会推销自己的工人也能接到活。

分析过程中还有个有点意思的环节：系统会模拟不同工种的专家辩论。

木匠 vs 泥瓦匠，用智利西班牙语各自论证自己的修复方案。另一个 Agent 则跑去当地建材超市 Sodimac 和 Easy 实时查价，验证预算是否靠谱。

![木匠 vs 泥瓦匠](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlKvJkMxVnOSGmoAzqa8avSXwFHFLgj854g1nMiaJASyicI4ibFyTSiag9MsAAb6BibBSx4pibya1uoBXZHa96cZnAiatdicduOUEbTSBY/640?from=appmsg)

木匠 vs 泥瓦匠

一个报价没有实际价格支撑，说了也等于没说。这一步想得挺周到的。

Benjamin 还把 MaestrIA 拿给他爸进行了测试，一共 12 张照片，12 个诊断。

结果是： **与三十年老师傅判断的吻合率：81%。**

06

## 工厂老师傅

最佳 Managed Agents 使用奖，则给了法国的 Idriss Benguezzou 和 Adam Hnaien 做的 ARIA。

ARIA

ARIA 解决的是工业维护领域一个老问题：

> “ 在每个工厂、每个车间、每个水站里，总有那么一个人。他能听出机器声音哪里不对劲，他能在机器坏之前两天就知道它要坏了。他就是知道。然后他退休了，这些知识就永远消失了。

传统的工业维修管理系统部署成本 50 万美元起，需要半年的专业咨询。结果就是，超过一半的工厂压根不装，等机器坏了再说。

![知识消失 vs 知识留存](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlbwpuuTYOYObyVj0GTNvs4Uk6t5Qf8wD82sgmODxdwZrowtqZicWt37J2Uaw9Lku2T4ng7d9dpjtVHo8icquiaZR8xdsXFUY2G64/640?from=appmsg)

知识消失 vs 知识留存

ARIA 用了五个 Agent 各司其职，像一支维修团队一样层层传递工单。

演示场景是一个矿泉水灌装厂：一条线，五台设备。把设备手册丢给 ARIA，Opus 4.7 的视觉能力读完手册，问了三个问题，系统就上线了。

其中一个场景是：瓶盖机报了一个振动异常警报，但 ARIA 没有立刻发工单。它查了上下文，发现振动值其实在下降，并非异常。

并给出结论： **无需处理** 。

大多数系统到「发了警报」就结束了，而ARIA 多走了一步：它在判断这个警报值不值得理。

但如果真的出故障了，处理链路就有所不同了。

检测 Agent 发现异常后，调查 Agent 接手，启动 Opus 4.7 的 extended thinking。它会写一段 Python 代码，在 Anthropic 的云端沙箱里跑了一次回归分析，从原始信号中算出设备的退化速率。

精确的数据会直接进入工单。技术人员拿到手的已经不再是一句「振动异常」了，是一张详细的维修表： **根因分析，加上一步步的修复建议** 。

并且，它还拥有记忆。

灌装机又出了一次类似的振动异常，ARIA 翻出三个月前 Tom Anderson 处理过的那个 case，找到当时的修复方案和零件编号，直接告诉操作员：上次就是换了这个零件好的。

5 个 Agent 共享 17 个工具，通过 MCP 协作。日志、操作员的班次笔记、信号趋势、KPI、历史故障……全部汇入每台设备背后的知识库。

这个知识库是从设备手册和操作员的实际经验中一起构建的。

用 ARIA 团队的话说：那个「什么都知道的人」，再也不会因为退休而消失了。

07

## 手艺的数字化

六个获奖项目来自五个国家，覆盖医疗、维修、教育、工业、创意五个不同领域。

这些项目有一个共同的内核： **它们都在把原本锁在少数人脑子里的专业知识，变成更多人能触及的工具。**

板级维修经验锁在少数硬件工程师手里；临床直觉锁在资深医生的脑子里；工厂维护知识锁在那个「什么都知道」的老师傅心里；木工手艺锁在一个没有大学文凭的匠人手上。

![从锁在脑子里，到人人可用](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnZsm3WAibYZsQWz4iamicibNdpnlKO4u5UuMlgP9t9IgF3PHAVvzcKCpLeg5LcOJ7DxV2fLIAoISSdRhweQbyufQriafhdnM6HQkUg/640?from=appmsg)

从锁在脑子里，到人人可用

人类文明里有大量这样的知识。

它们不在论文里，不在教科书里，不在任何数据库里。

它们只存在于某一个人的手感里、直觉里、几十年累积出来的判断力里。

这些知识，一直在消失。

老师傅退休了，手艺传不下去了，临床直觉随一代人老去而失传。没有人宣布它的死亡，也很少有人意识到自己失去了什么。

这六个项目背后的指向是：AI 可以接住这些正在断裂的经验，让它变成一种工具，一种传承。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlj0mib5NAws1QsQmGTiccSeocLiabzKyf2gOKXeHYiavncIJ68hunt6SDpT3xaswKzTyfhULd6iapDoXaOZXZAPicpA74DJMvnqJicnE/640?wx_fmt=png&from=appmsg)

这也许是 AI 能给世界留下的，一份不那么显眼、但足够持久的东西：让那些本会被时间抹去的人类经验，留下来。

因为在 AI 到来之前，这些知识和声音，因为太过于不起眼和长尾，而被鉴定为没有价值，从而忽略。

而借助 AI 来做出这些项目的人，也不是什么硅谷连续创业者。

他们是，一个土耳其医生，一个智利大学老师，一个木匠的儿子。

他们可能，就是你。

◇ ◆ ◇

相关链接：

• 获奖公告：https://x.com/claudeai/status/2049523899918934384

• 黑客松活动页：https://cerebralvalley.ai/e/built-with-4-7-hackathon

• MedKit 演示 / GitHub：https://www.youtube.com/watch?v=6bN6hnx-A2A / https://github.com/bedriyan/medkit-app

• Wrench Board 演示 / GitHub：https://www.youtube.com/watch?v=OZ2D\_p82z6w / https://github.com/Junkz3/wrench-board

• Maieutic 演示 / GitHub：https://www.youtube.com/watch?v=IJ9FyX2xwWA / https://github.com/bcanata/maieutic

• Virtual Puppet Theater 演示 / GitHub：https://www.youtube.com/watch?v=qLuGU4PQNss / https://github.com/rhmoller/virtual-puppet-theater

• MaestrIA 演示：https://www.youtube.com/watch?v=rkH4AjoTL5Q

• ARIA 演示 / GitHub：https://www.youtube.com/watch?v=Hen24w2Jyz4 / https://github.com/zestones/Aria

• Claude 开发者通讯：https://claude.com/newsletter/developers

继续滑动看下一个

AGI Hunt

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过