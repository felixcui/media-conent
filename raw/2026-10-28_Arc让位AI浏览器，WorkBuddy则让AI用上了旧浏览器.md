# Arc 让位 AI 浏览器，WorkBuddy 则让 AI 用上了旧浏览器

**作者**: 有新

**来源**: https://mp.weixin.qq.com/s/DBaN8wrSG0Lxo6m44uQSxw

---

## 摘要

文章对比了两种AI浏览器路径：Arc宣布关闭桌面端并引导用户迁移至新AI浏览器Dia，而腾讯WorkBuddy则通过扩展让AI直接操控用户已有的QQ浏览器，保留登录状态和数据，由Agent代为完成检索、采集、整理等任务，从而将竞争从“用户打开哪个软件”转向“用户把什么工作交给谁”。

---

## 正文

有新 有新

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39fiaBLf3LFLZWpYF7GHh9VuGEO7jpsazrwsf6egVLGmzFibqljbjpBe9gnLqV83NTIbPG1oJeGrdLfZviapw2UW35QVezA0JYxxkQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39dED5xGzcF3x8iadu9axz7ETQtgPh5OG1H4Vf0dcnFo82I1ARK5do4ibxicfnbKzQkU8D9Hrt1ckh2jx37gtRPMsyOkLA5I0LMxPU/640?wx_fmt=png&from=appmsg)

“未来的人机界面将以委托为基础，而非直接操作。”——尼古拉斯·尼葛洛庞帝《数字化生存》

10 月 22 日，Arc 宣布将于 12 月 22 日关闭桌面端，工程与安全团队转向新浏览器 Dia。用户可以把密码、书签、扩展和历史记录迁过去，继续使用熟悉的功能，也可以选择开启 AI。

![Arc browser is shutting down | The Verge](https://mmbiz.qpic.cn/sz_mmbiz_png/PQ3MNFbl39d4rUISiaLwzg4V7pWEWiaVnbDoJ51MyRYa5CDxwlEWlnooR3BhW7Vflyh3dU0d1sPjeokGX9HDazsnNt6VhjGKiaFWDeicL53Q93Q/640?wx_fmt=png&from=appmsg)

Arc browser is shutting down | The Verge

将 AI 放进一款新浏览器，再邀请用户迁移，是一种产品选择。另一种做法，是让 AI 进入人们已经在用的浏览器。网站照常运行，账号和数据留在原处，打开网页、来回切换、复制和核对的步骤，可以交给 Agent。

后者未必要求用户换掉浏览器，却可能改变他们使用软件的习惯。过去，人要先找到合适的工具，再把任务拆成一连串操作；现在，一部分工作可以先交代给 Agent，由它去使用工具。竞争也因此从“人愿意打开哪个软件”，延伸到了“人愿意把什么工作交给谁”。

浏览器由此牵动了工作入口的竞争。a16z 合伙人 Seema Amble 在 9 月的一篇分析中讨论过一种变化：用户可以在 Agent 中处理工作，原有业务系统继续保存数据、执行规则。当用户先向 Agent 交代需求，再由它调用软件完成，接受任务、组织执行的产品就可能发生变化。原有厂商希望保留与用户的直接联系，AI 公司则希望承接更多原先在其他软件中发起的工作。

## ▍谁来打开下一个网页

了解一款新产品的市场反馈，往往从评论区开始。不同视频下面，有人追问技术，有人讨论价格，也有人只是玩梗。要形成一份有用的判断，先得找到相关内容，筛选、抄录，再把结论与原文对上。分析之前的这些准备，常常比分析本身更琐碎。

在一项围绕特斯拉 Roadster 发布会相关视频的评论整理任务中，用户可以把这串步骤交给了腾讯 WorkBuddy：去 B 站检索视频，收集高赞评论，归纳观众反馈，最后交付简报和评论明细。

任务沿用了 QQ 浏览器里已有的登录状态。安装配套扩展、开启浏览器连接并授权后，WorkBuddy 打开 B 站，按播放量排序筛选视频，进入评论区核对内容，再结合脚本完成采集和整理，最终汇总了 3 个视频下的 600 条高赞评论。这项浏览器操控能力目前仍处于 Beta 公测阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39eZabFKntqVP5vzAVoreY2ibEjtYl5dY8hCk9yzib41LGxUHSRHNFCUQy5yfb14PXwJpaKibBPWnpjremiczmAO74SMQ44TXHeto2Q/640?wx_fmt=png&from=appmsg)

收到任务后，WorkBuddy 先确认 QQ 浏览器已连接，随后打开 B 站。执行记录中会显示当前进展，浏览器里也能看到它正在访问的页面。

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39fWlOgYFywPtgWiaDwVFjqia6m4z99xUsKORpKXFt9AfVib2Btn5uuna5NP9FYxDhMTDOqNBE389w8ENDTY5aRSUp7I64myEKpHYM/640?wx_fmt=png&from=appmsg)

WorkBuddy 在 B 站检索相关视频，按“最多播放”排序并筛选，进入评论区核对内容，再结合脚本工具采集和整理，最终汇总了 3 个视频下的 600 条高赞评论。网页操作集中在独立的 WorkBuddy 标签页组中，不抢占用户的鼠标和当前窗口，用户可以同时处理其他工作。此外涉及支付、注册提交或验证码等环节，按产品设定仍需人工确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQ3MNFbl39f4Vh9ddeQ9DXKMC5ReFhXNkmyBJu6EjgYwgAQiauaWmBIjXQkqyk17IDlLXzibYicCdFstR9lHsZreqcj5KCVx3mQW2R10kPMm3M/640?wx_fmt=png&from=appmsg)

任务最终生成一份舆情简报和一份 CSV 评论明细，所收集的评论累计获得约 13.9 万次点赞。WorkBuddy 按情绪和议题分类，并结合互动数据梳理主要讨论。按简报的分类，中立评论约占 54%，正面约 26%，褒贬并存占 12%，负面约 8%。

其中，122 条评论涉及技术惊叹，121 条涉及实用性和使用场景。一些观众关注车辆的姿态控制，另一些追问它在日常驾驶中能解决什么问题，也有人同时表达认可与疑问。不同议题的互动表现也有差异。玩梗类评论占 15.8%，获得约 23% 的点赞；安全、成本与法规相关讨论有 62 条，点赞量较低。简报既呈现了传播热点，也保留了热度较低、值得后续核查和回应的产品疑问。

配套 CSV 保留视频来源、评论原文、点赞和回复数量，以及分类标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/PQ3MNFbl39eBBod2rZUEc0FGDPcIibIcraw3XjcO6mKCCew9AJRxTppwhPfDkgQCicWjAHr0upb737BMZrVd5AYudQ1lBr3WclvBCd3JcQNCM/640?wx_fmt=gif&from=appmsg)

除了上述浏览器操控能力，WorkBuddy 也能通过开源工具 BrowserSkill 操作网页。在“专家·技能·连接器”中搜索并添加 BrowserSkill，再安装配套的 bsk 工具和浏览器扩展，即可完成连接。连接后，它同样能沿用已有登录状态，读取页面、点击、填表和提取数据，支持前文涉及的网页检索与资料收集。

区别在于，WorkBuddy 浏览器操控在独立标签页组中执行任务；BrowserSkill 则提供独立的 Agent 窗口，以及操作录制与回放等进阶功能。作为开源工具，它也能供其他 Agent 调用，并支持进一步定制。

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39flxibxgl62nN4ca4JzIqNI3YhP9rbcXmV1iby6dRpsxe4GevxOwgNuk4pKGI6f86KDeucEPAcajfVFBlNCcbB0oO7CtFmKia3Yiac/640?wx_fmt=png&from=appmsg)

两种接入方式都让使用者可以直接向 WorkBuddy 交代网页任务。工作入口的竞争也发生在这里：下一次需要了解用户反馈、查找和整理信息时，用户是先打开网站自己找，还是先把要求告诉 AI。

## ▍交付要经得起实际使用

产品开发中，写完功能并不等于页面已经能正常使用。几个单独运行正常的功能接在一起，可能出现计算错误、信息不同步，或不符合要求的输入被放行。开发者和测试人员需要沿着用户的使用路径检查，找到问题后修改代码，再回到页面确认结果。

AI 生成的代码同样需要经过这些检查。浏览器操作让 Agent 能够参与拟人交互走查，在运行中的页面上点击、填写和提交，检查操作带来的变化，并将发现的问题带回开发过程。

本次用于测试的是一个本地模拟的活动报名页面，不涉及真实支付，包含门票数量、报名信息、同行人及订单确认等功能。任务通过一段自然语言指令交给 WorkBuddy：使用本地浏览器打开页面，将门票改为两张，填写本人和同行人的测试信息，核对总价是否等于“单价 × 数量”，并输出异常报告。

WorkBuddy 随后操作页面，完成填写与提交。在这个过程中，它发现门票数量已经变为两张，总价却仍显示 88 元。按单价计算，两张门票应为 176 元；提交后的确认弹窗也显示“两张门票 88 元”，错误一直延续到了确认环节。

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39fwqx4y9TUkUZnKfQCRUHBKWhZSfXiak6nEIJqLCia3wCYd0fQ7E6D7lOUIW588ic6vGWRnEB7YJvjJKmdTUEo8c1iaNiaYiaSoI98Uk/640?wx_fmt=png&from=appmsg)

首份 HTML 走查报告记录了操作结果、异常截图和修复建议，共列出7项问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PQ3MNFbl39dquJIF70brHzDWKjSFyshicHpCYNy6Qta5kRs97WTGiajh10q3WXxEYDMibZl0t8vd0dq1qTVqibArG8zaqhxpMQbbWRqkjU4corY/640?wx_fmt=jpeg)

针对金额异常，WorkBuddy 进一步检查了页面代码，指出总价和弹窗金额都只取了单价，没有乘以数量，并建议统一计算逻辑，避免两处显示各自计算而发生遗漏。检查还覆盖了人数与票数的匹配、输入有效性及提交后的页面状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/PQ3MNFbl39et8pOLEUN1icdAxIx4beXSdzd99Yywb2HUInrrXc1qYqXMX3hYaAnNSG6fiaO6sYd01fmqACzciaTPlmuYLj77kIQHUGecMaib02E/640?wx_fmt=gif&from=appmsg)

使用者确认并采纳建议，修改金额计算，同时补充提交时的人数校验。随后，WorkBuddy 按相同的任务要求再次走查，核对修改后的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQ3MNFbl39dibS79JoglGGhjbr1ic6DRib9FBxgJaGbcj0SxbdooPIK8A0JicJHzqZAVxAnQGADHLiaJgkqLjqLkkTRJj5Gq3gInjkpsQq72qFVE/640?wx_fmt=png&from=appmsg)

第二份 HTML 报告显示，两张门票的页面总价和确认金额均为 176 元；补充检查覆盖 1 至 99 张门票，各档金额均与“单价×数量”一致。报名人数与票数不符时，提交也被拦截。报告对照首轮清单，确认 3 项问题已修复，保留 4 项未解决的问题，并补充记录了同行人可超量添加、直到提交时才提示的交互问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/PQ3MNFbl39fEE5JK7aq9t9apCO09DB6hOeS7r738IIxJUZyAZiaZLCSwl8B7iaKvB1Jn8McutMW0YDmcOibgp0WeemKA3EcjicvIibAArWdHUsC4/640?wx_fmt=gif&from=appmsg)

代码由使用者修改，WorkBuddy 负责提出建议并复查运行结果。两轮走查记录了已修复和仍待处理的问题，也为判断页面能否交付提供了依据。浏览器操作将这部分验证工作纳入 Agent 的能力范围，交付质量也因此成为产品之间可以具体比较的一项能力。

## ▍更多工作如何变成生意

Anthropic 在10月16日发布的内部研究中，记录了 Agent 在不同岗位中的应用：销售人员用它起草邮件、连接客户管理系统，法务人员用它初步审核文案，财务人员则搭建采购申请审核工具。研究还追踪了各岗位的人均产出。以2025年12月为基准，到图中统计期末，工程师人均代码提交量达到原来的5.1倍，法务人员人均合同处理量为3.1倍，销售人员人均成交量为1.7倍。不同岗位的增幅并不一致，图中呈现的是具体业务产出的变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQ3MNFbl39cHPSq7jU1xER686k45G59AgDXVKWADib2reUNYNJBNotpxKqCyblPibM0MEzxHdgnicyaVnKXDXEjo3RmDKnXrUlKeZFxFr15Kug/640?wx_fmt=png&from=appmsg)

来源：Anthropic内部研究。同期业务扩张等因素也会影响产出，图中增长不能全部归因于Agent。

Agent 参与的业务环节增加，也让厂商有了按工作产物或业务成果收费的可能。a16z 普通合伙人 David Haber 在 10 月 14 日的分析中提出，长期运行的 Agent 可以围绕一项业务持续跟进，在多个步骤之间保留信息、推进事项。他看重的收益包括减少遗漏、加快跟进，以及帮助客户获得新增收入，Agent公司的收费空间也可能随之扩大。

腾讯近期对 WorkBuddy 的升级，也在增加它能够持续处理的工作。行业 Buddy 将专家、技能和连接器按场景组织起来；定时任务汇总、历次运行记录和产物通知，支持使用者跟踪重复执行的任务。这些功能与浏览器操作、文件处理和开发能力结合，使 WorkBuddy 可以处理一次性任务，也能按设定重复执行、留下运行记录。

专业 Agent 可以围绕特定业务积累优势。客户此前谈过什么、业务卡在哪个条件、哪些情况需要人工确认，都要结合历史记录和业务规则判断。团队的行业经验，需要落实到这些判断，以及相应的界面、审核方式和交付要求中。

这些积累也能支持产品承接相邻的工作。研究工具掌握了客户持续关注的对象和判断标准，就有条件继续跟踪变化、筛出需要重新评估的信息；原先交付一份报告的产品，便有机会承接客户后续的监测需求。新增的服务建立在已有业务知识上，而不只是多接入几项工具。

**✦** **精选内容** **✦**

**[当 Personal Agent 有了记忆，Today AI 尝试主动跟进](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247502711&idx=1&sn=141917c6c97952ff3f43ad46d626dc01&scene=21#wechat_redirect)**

**[当 AI 健康应用开始赚钱，「豆包工作」让我们重新思考垂直 App 的价值](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247502648&idx=1&sn=b267adb49e7dd4b05b97574948037dbc&scene=21#wechat_redirect)**

**[YC 华裔团队造了一台本地 AI 电脑，1799 美元三天售罄](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247502622&idx=1&sn=c75e9683f6c750e5d98ce65fe635a30d&scene=21#wechat_redirect)**

**[「深创超导」获数千万元天使轮融资，布局 AI 用电需求背后的聚变材料](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247502610&idx=1&sn=461cc27d9c5afe2f39f299dddfe38a5e&scene=21#wechat_redirect)**

**[成立半年，源策未来想让一份数据服务更多机器人](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247502568&idx=1&sn=c8793a972e7f0d112fabf2a39dcf0113&scene=21#wechat_redirect)**

![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39cWjXFaSNHSSTejrdUeN3GRfDic9HcFgTgrEV9xEExS7B7XDrMMBMETR4ibqIBXbLuNLj5P4lFWQ1vYUBVpL8HBoQkeWkOhcwM0k/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/PQ3MNFbl39d45nB0UrXRrcQic6uEW8ia5SsKAyicRafceHnYnx7aaGrDGJLiaZXX969HMg00BL5xxYj2EkCAWICCXGYlX4nC8riaIT4up2JibXwyc/640?wx_fmt=png&from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过