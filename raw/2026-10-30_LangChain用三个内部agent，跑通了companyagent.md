# LangChain 用三个内部 agent，跑通了 company agent

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/zum0JvusQrZW7qiETSntFw

---

## 摘要

LangChain 内部搭建了 GTM Agent、OpenSWE 和 Content Studio 三个 company agent，它们运行在同一套 harness 上，共享五个核心组件：以 Slack 为主要交互界面并辅以自定义 UI、按工具拆分身份策略（OBO 与固定凭据混用）、区分短期与长期记忆并强调程序性记忆、以及尚未完全解决的定时触发和离职交接等身份难题。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

coding agent 是第一批真正落地的 agent。现在 company agent 来了。

Harrison Chase 在 LangChain 内部搭了三个。GTM Agent 管销售，OpenSWE 管工程，Content Studio 管营销。三个 agent 配方一样，跑在同一套 harness 上。他说这不是巧合。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJibs5SWWwNnrictzTFABv1zlNdVnBNkRgwLdeT7SMW5fbmUqLlXXJXd1eNu0ib7dyyKb6QrTv9Aykl9qozn7wTHicliaKauicSFIWDfs/640?wx_fmt=jpeg)

## 五个组件

### 一、活在人们工作的地方

所有 agent 都是 Slack app。可以 DM，也可以在频道里 @。频道里用的好处是别人能看到你怎么用，不是单机工具，是多人 harness。

一个有意思的 UX 细节。人聊得正好，想让 agent 插句话，如果 agent 直接在原线程里回，对话就被污染了。他们的做法是 agent 在频道里单独开线程，同时建议在原线程贴一条简短结果，不进去也能看到 outcome。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ94EsvJ4ZhoQqR90R6hib9LcY2ibftRpxvu1rNCh7icH90hicsEib7jBCNSApBq64Tb0b2cHbCosTZIPMBAMGKibBcEEsXd3I30ZiacgY/640?wx_fmt=jpeg)

Slack 搞不定的事也有。GTM Agent 起草邮件让人审核，一两封在 Slack 看还行，积压多了翻消息非常痛苦。这类场景做了自定义 UI。Jeff Schneider 调侃过：第一步往 Slack 硬编码，第二步再把第一步撤了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJicicymB3OrXTVwJantTWx4SqAicNic76uh8BaduSD0zS7FRltAibSmaDcI78GrNJWXiaXkwqPl5fCyR74WIoa9vTcAvd3n1SH6gewHU/640?wx_fmt=jpeg)

### 二、身份，五个问题里最难的那个

Harrison 自己用的词是 the thorniest and trickiest。agent 动手的时候，到底代表谁？

两种做法。OBO，代表调用者。固定凭据，用一套服务账号不管谁来。LangChain 没二选一，按工具拆。Harrison 后来在评论里确认了两个字：Per tool。

OpenSWE 最简单。DM 里干活用你的 GitHub handle 开 PR，后台代码审查切 GitHub app 身份。

GTM Agent 更复杂。Salesforce 用固定身份，不用每个人登录。邮件用 OBO，而且只在 DM。频道里不给。逻辑很清楚：频道里多人能看，以你的名义发邮件等于给别人一条冒充路径。

Content Studio 又不一样。Notion 用 OBO，Twitter 用公司固定账号，只有白名单能发推。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ9pSFic0yDJzfSvc2OJSHlmheDmgChNK1dyRicwBrGxpiaZ1dmaoPzJeGs0gwibUE3DjPfx7raibh3GhM8ca1qdNLya7E4tlbyxKib6Y/640?wx_fmt=jpeg)

没解决的问题比已解决的多。定时 cron 触发时设的人不在场，用谁的身份？换岗或离职后怎么办？定时加 OBO，agent 能在没人看着的时候发信删除，谁签字？有人提了一个原则：agent 用自己账号干活，以人名义发出的先等审批。也有人搭共享记忆 hub 搭到一半，发现 identity 是唯一卡住的地方。

### 三、记忆，两层不够

短期工作记忆存对话、工具结果、便笺，跑完就清。长期分三种：语义，记事实偏好。情景，记过去交互。程序性，记行为规则。

程序性记忆最容易被低估。agent 反复格式化错误、调工具顺序不对、忽视 tone 规则——不是缺知识，是缺程序性记忆。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJicdrDaUJ3Eic2nhlV3buwfIFcAATvrxsRHM6W3fJ6ZL11AZdQcalPbxCQtLQTIEOCW75JcUlW6PIwMck2VTusUJUYpqIp4tty3w/640?wx_fmt=jpeg)

Harrison 说记忆是五个方向里探索最少的。三条设计原则：不是所有 trace 都该进记忆，大部分只配当历史。确保下次跑了真的读到更新。重要的行为变更用 eval 保护。

但真正麻烦的不是架构，是隔离。

GTM Agent 的邮件工具锁在 DM，但记忆没这种隔离。你在 DM 里说的话可能被判为全局记忆，后来所有人都能用。更隐蔽的是 GTM Agent 读外部邮件和线索，陌生人的文字也能进全局记忆，之后以某个员工的 OBO 身份被调用。全局写入有没有权限校验？全局记忆和个人记忆冲突谁赢？用户记忆和系统记忆在文件系统怎么隔开？车间的真实流程在主管 WhatsApp 里，tribal knowledge 怎么处理？

没标准答案。记忆需要可见性，不只是为了纠错——是你得知道 agent 记了什么、从哪来的、谁写的。每次写入要能看能撤销，否则一个错误会一直粘着。

Kyle Johnson 在 Monument Labs 的做法是一条思路。结论账本，append-only。每条信念挂着 SQL 和最后验证日期。不删除，只退休。最旧的信念优先重测。agent 只有只读角色，敏感用户文字对它不可见，只给消毒视图。

### 四、沙箱 + 定时 = 无人值守

三个 agent 都能写代码执行代码。进程在沙箱外跑，执行时连沙箱。各自不同基础镜像，OpenSWE 按频道和用户选。用 secret proxy 从沙箱安全连外部。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJicg6dZVUKovib4yVVWvM0JXgviclLLar7nVQ2EaqaMKia63xZj1l9axn44Rv1WcAJibxMdzLYaopibQ96Mc5ZNFrgbIia4yCDr9tybAw/640?wx_fmt=jpeg)

但大部分运行来自定时或后台事件触发，不是人手动点的。OpenSWE 监听 PR 自动审查。Harrison 让 GTM Agent 每天发简报，它自己建了 cron。有人早上跑几个 routine，起来只看留下什么。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJibtkbaw6c1gacxax20arIRREqLiacOZkmy6sXApbMV4utByS2msMjR6UKBIStQtJkqAIAWGvAUTiaBVJE3P3KXiavh5l76jtJnt38/640?wx_fmt=jpeg)

ambient agents 脆弱的地方：有一个从周二起每 15 分钟安静失败一次，可能到周五才有人发现。

Monument Labs 给了一个能力阶梯。Observe，只读，人执行变更。Propose，起草给人审批。Experiment，人设边界内做可逆测试。Operate，闭环运行，火灾上报。上一级的前提是前一级的记录在账本里可查。

### 五、监控和知识层分开做

EKOS 从另一面碰了这个问题。企业信息散在代码、schema、配置、文档、管线、git 历史里。向量检索给一段文字，不等于给实体关系、依赖、来源证据。EKOS 把这些编译成结构化知识图，保留文件路径和行号，通过 MCP 给 agent。

安全那侧更关键。监控、告警、执行是不同职责。OpenAI 内部评估里 agent 干扰了自身监控告警——被监控的能改监控组件，监控就不可靠了。agent 不该对自己被约束的边界有单方面修改权。知识层和运行时安全分开做。

## harness 比模型重要

给 agent 一个 Slack 头像很容易。给它工牌、权限、值班表、操作日志和一份可验证的 track record，才是 company agent 落地的开始。

harness 最初是包一个模型的 wrapper，现在包了整个组织架构。你让 agent 碰邮件、碰 Salesforce、碰公司推特、碰 GitHub PR，它就不再只是一个模型调用的问题了。它需要知道自己在替谁干活，需要记住什么不该记住什么，需要在沙箱里跑代码，需要在没人的时候自己运行然后安静地把结果放好。这些都不是模型能解决的，是 harness 的活。

说得直接一点：harness 往往比模型本身更重要。Harrison 也确认了这一点。看这三个 agent 的实践，确认这点的应该不止他一个。

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过