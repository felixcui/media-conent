# MCP两周年，Anthropic推出Skills over MCP

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/4oUk4CzVfwMuV6YVTBgOCQ

---

## 摘要

MCP 满两岁，Anthropic 借机放出一批能力：Skills over MCP 进入公开测试，Tasks 与 Elicitation 正式可用，File Uploads 即将推出。官方架构图把服务器侧拆成三层：技能携带领域知识、工具是 Claude 可执行的动作、资源是可拉取的上下文；技能按需加载，并随服务器更新。Tasks 解决长任务阻塞——以前工具调用要等跑完 Claude 才能继续，现在服务器可在后台运行耗时操作甚至整个 Agent 循环，Claude 先做别的、结果好了再取，ZoomInfo 用它做更深的客户研究，之前要好几轮提示。Elicitation 管敏感操作：花钱、删数据前服务器停下来，用表单或链接问用户，Supabase 用它确认建付费项目和执行破坏性 SQL，Railway 删服务前先询问，GitHub 删仓库前要求输入仓库名。File Uploads 则让 Claude 直接给服务器发大文件。另外两个数字：MCP 每月 SDK 下载量超过 7 亿次、Claude 上已有超过 1 万个连接器；工具搜索按需加载定义，多服务器场景上下文占用可减少 85% 以上。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

MCP两岁了。Anthropic趁生日宣布了一批新能力：Skills over MCP进入公开测试，Tasks和Elicitation正式可用，File Uploads也快来了。

MCP两年前是给AI应用连接外部工具和数据的协议。如今，它正在变成Agent之间通信和编排工作的标准。

官方博客给出一个更直接的描述：Claude和服务器协作的方式，正在变得像和另一个Agent协作：向它学习、委派任务、互相交换输入和文件。

**Skills over MCP（公开测试）**

工具名和描述能告诉Claude服务器能做什么，但说不清具体怎么做。Skills就是来补这个缺口的。服务器可以把技能和工具一起发布，技能相当于一份操作手册，指导Claude完成多步工作。技能只在需要时加载，所以上下文占用低；技能随服务器更新，用户不用额外安装。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJibKBzGxmnYJnFjZorIEQpaeYIaPiawf0iaVx7iazYCMMsbdhXD5lSoYTAMAkaU0IkRRsUr91BjahEKzNAQkn66tib713fVGg3qWrcc/640?wx_fmt=jpeg)

官方博客的架构图进一步拆解了这三层：技能携带领域知识，工具是Claude可执行的动作，资源是Claude可拉取的上下文。技能按需加载，并随服务器更新。

实际用例：Shopify的服务器让Claude从零设计并更新店铺；HubSpot的服务器在Claude里引导客户完成配置；Atlassian的服务器利用组织上下文做分析和洞察；Carta即将推出根据上传文件起草股权的技能。

**Tasks（正式可用）**

以前工具调用要等执行完，Claude才能继续。Tasks让服务器在后台运行耗时操作甚至整个Agent循环，Claude先干别的，等结果好了再取。ZoomInfo用Tasks做更深的客户研究，之前需要好几轮提示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ92TTCAV8jUjzA4xBopiapch3WnhZUX2qlelibpBicPiamQLxxOjdemicdvJR1VZhOOMibecuV0R3jmccDKUWia7mZmqCNJMEESmGicJBk/640?wx_fmt=jpeg)

Claude把长任务交给服务器，服务器在后台跑，完成后Claude取回结果。

**Elicitation（正式可用）**

有些操作需要用户确认：花钱、删数据。Elicitation让服务器停下来，用表单或链接向用户提问，然后继续。Supabase用它确认创建付费项目和执行破坏性SQL；Railway删除服务前先询问；GitHub删除仓库前让用户输入仓库名。

**File Uploads（即将推出）**

Claude将能直接把PDF、表格、图片发给服务器，不经过上下文窗口。适合处理大文件或非文本数据。

**MCP生态也在变强**

过去一年，MCP在Claude里变得更省token：工具搜索按需加载定义，多服务器环境下上下文占用可减少85%以上。Enterprise Managed Auth让管理员一次授权，用户自动连接。MCP Apps扩展还能把完整界面嵌入Claude。

MCP两周年，更新不只是加功能。MCP每月SDK下载量超过7亿次，Claude上有超过1万个连接器。它正在从连接协议演变为Agent协作协议。如果你在构建服务器，Skills、Tasks、Elicitation、File Uploads这些扩展现在都值得支持。它们属于开放规范，兼容任何客户端，不只是Claude。

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过