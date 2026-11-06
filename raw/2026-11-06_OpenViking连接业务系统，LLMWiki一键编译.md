# OpenViking连接业务系统，LLM Wiki一键编译

**作者**: OpenViking

**来源**: https://mp.weixin.qq.com/s/BIxTsyFOjhB0JdOv8qTCjQ

---

## 摘要

火山引擎 OpenViking（Agent 上下文数据库，支持文档/图片/音视频/3D）上线**数据连接器 + 知识编译**：可接飞书文档、项目、Git 仓库并**定时同步**；再用 Compile 指令一键产出 **LLM Wiki（项目知识）、Code Wiki（代码图谱，函数调用与逻辑关系）、阶段性汇报材料**。典型用法是让装好 ov 的 Agent 直接读库：说“整理某项目这周进展”就出周报；说“基于产品文档写技术方案”就自动取飞书需求 + 仓库代码生成方案，多人协作时库与 Code Wiki 持续更新、不用管版本。后续将接钉钉、Confluence。

---

## 正文

OpenViking OpenViking

在小说阅读器读本章

去阅读

🔥 **OpenViking上线数据连接器、知识编译功能** ，支持飞书文档、项目和代码仓库的数据接入与同步，一键编译出业务需要的知识 Wiki、代码图谱、阶段性汇报产物，让 AI 帮你搞定项目交接、进展同步。

**OpenViking ✖️ 3D 内容理解模型**

OpenViking 是火山引擎推出的 Agent 上下文数据库，支持文档、图片、音视频、3D 等多模态数据的导入与理解。

现在，OpenViking 已上线多种数据连接器，支持飞书文档、项目、代码仓库的连接与定时同步。

使用可参考 https://docs.volcengine.com/docs/vector\_database\_vikingdb/Overalldescription?lang=zh

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FectfGhkofrZumOc7gQMOChnwHE9Or9Enf3AcFHQ9icpIP80xxpUaS3icx0z4iarjJicJmOeadE3ibxMRdyzM76q8d6UEcPEIEOyNeZA/640?wx_fmt=png&from=appmsg)

连接入口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefTMWc98xYgDyW0GqxUmWkY8N7Rtt1M48hKl6aPguNld2bnA8PKwwRvLzXthRbWu37AQAzz4opUreOoQcmzhibFiaLEtNC5UBMBk/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeNFTCicWabc2t3ypBsQwR0RoCTlYpt3cWQKGUWic2V8iaD137ibXf126R76uDYKqIuRzBtW9ibVF9IfATiaHVA0ib2ibGeNMN6jf6CQEk/640?wx_fmt=png&from=appmsg)

数据导入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecJnMS9DQ1sMMibmyZvsy525szHSMaxQhTIm51QIorvsEV8s2HFub5GHD4rLK7cArlTdPcMxVZ20G0ic7xu6L5MJnZia7tDQGzEko/640?wx_fmt=png&from=appmsg)

定时同步

左右滑动查看更多精彩内容

基于导入的项目知识，通过知识编译(Compile)指令，就可以一键产出知识 Wiki、代码图谱、汇报材料等业务需要的加工产物，打通从数据连接到业务可用的高速通路。

支持自定义加工，使用可参考：https://docs.volcengine.com/docs/vector\_database\_vikingdb/Compile-Compileresources?lang=zh#knowledge-graph

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecXYQucibj4Q4OKMDlp2cqnRXoHRlXTNPDzJvvM90sUZlagtjvu9QjpgaAUp6qwyG2dm7R6cdynKNBzn5IUMmyoVZoKdtTLSpiak/640?wx_fmt=png&from=appmsg)

预置编译模版

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeePrffp4yFT9zGwUKvcaVicTrLc6TGObkhdcQFkC9n9Yjjvy8wK7qicEv00Dr6zHHUg49fL3QZOUGhEVAdU5JbotxRho4k6o2RKU/640?wx_fmt=png&from=appmsg)

原始项目文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeftMTcPRPNCsZ9P7bOW8D5lUq0puvYjicUdvcl5ZRAhB1849faAjaLd8HcKULxsJv3iaVm8Dnm13Fpc5rD5NEuaiaQMjMibPqmjDhI/640?wx_fmt=png&from=appmsg)

产物1：LLM-Wik

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeKSHpqiaHUpTmXdbGDLEneAsQicPTVALyUfrREc4VMYmlrA3Qgicbo0SOAglPzEnZPDU8Yibe2yynZLu1EVKiaz8yuX4ibRsVPcyzyM/640?wx_fmt=png&from=appmsg)

产物2：知识图谱

左右滑动查看更多精彩内容

将数据导入 OpenViking，连接上你的 Agent，无论是豆包工作，Workbuddy，还是 Codex，Claude 都可以在以下场景感受到价值。

**场景一｜新人入职，快速了解项目全貌**

新员工入职、项目交接，动辄需要整理几万字的交接文档，新人理解多少还要另说。

现在，把项目资料上传到ov，一键形成 LLM Wiki，捕捉每一份上下文。新人安装好 ov，只需要跟自己的 Agent 说：“我是一个新来的研发，接下来主要负责xxx项目。根据 ov 公共库的内容，帮我梳理一份 onboarding 阅读材料”。

然后，Agent 就会自动通过 ov 查询，找到关联信息，最终推给用户一个含项目背景、目标、需求列表（来自飞书文档）、代码架构设计、模块设计（来自仓库）、项目进展、当前迭代情况（来自飞书项目）的完整阅读文档，同时通过 LLM-Wiki 清晰阐明各模块间的关系。

新人通过阅读了解很快就可以完成 onboarding。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefJh18njK4kq201XcZaviaHnWGa8svpzDD953icDlicMbXff5xe4TsqBKRo9pT8LH8Km0VQr4bqsHDiazHYFBEZS3ibAgPylkAMgk0U/640?wx_fmt=png&from=appmsg)

项目上传OV

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fee1AG5RoeOAAgeTJ8guWgdekiaTIa4naPlDqBtnzT7CWPD1NtDnMdMc2cYnUjiakvceKtqQ1BRKx1JJjHDw7E7MOXoeJ3ibBTv6L0/640?wx_fmt=png&from=appmsg)

编译出LLM Wiki

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedpGjicgPSHfyM7PHnrCKs6mpzliakNbTibOrVUNV059jTseNInbOjRUoGnxWE1Zn68DLSfPXczRYjtKFfKKJUv88vSSEd9HnQAGc/640?wx_fmt=png&from=appmsg)

OpenViking + Codex检索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecGbfseLDHlxv8qxzPTZAxRPx4ZticLpSg7mhcxDhS5BGah4Rk3jj7O3rMG71K2B8ibh9BmP1ukRBTXRrGs9HzjCnPmmovrTTQGg/640?wx_fmt=png&from=appmsg)

Onboarding阅读材料

左右滑动查看更多精彩内容

**场景二｜周期汇报，业务进展一键追踪**

每次项目周会、季度总结，都需要成员一起复盘、梳理进展、互相关联，再集中呈现。

现在，项目在ov持续编译，LLM Wiki 实时更新。项目负责人只需要安装好 ov，跟自己的 Agent 说：“帮我整理xx项目这周的进展”。

然后，Agent 就会通过 ov 和最新的图谱，找到项目关联的所有产品需求、技术文档、市场反馈（来自飞书文档）、项目代码（来自仓库）以及当前版本正在开发的需求进展和 bug 处理进度（来自飞书项目）。最终整理出一份完整的市场、产品、技术进展以及版本迭代详情。

汇报再也不需要团队成员花时间去整理复盘，项目负责人也能随时获得最新反馈。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fee3c9lO1OHY1nfI5zcQ7ZTz5mc4mPxFic0VvXU0xkO5Y8qIga0HsleQvxnUsibSgVElwgILZVz1oz3doLU7SoVD2Kxa9PickOSrvs/640?wx_fmt=png&from=appmsg)

项目上传OV

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecBb2Lud9OYSSdF5znuUQGxEzVbhqdmsOXxFu2axQG1ZqJHKhujfrUicGQQjaee1pFWPh10LUzW7MZLUhlpiaKEzicfT1Sop2cQ0Q/640?wx_fmt=png&from=appmsg)

编译出LLM Wiki

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefaQj3mUYreuySFgNaF9mYCpb2FWsOlnr662re0SNByicW9YicEVQGTLoUHWJR9cyhZbNBTBpkkxMrKmiciap0tgvgleowpzR3rZxg/640?wx_fmt=png&from=appmsg)

OpenViking + Codex检索

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedETKtGDD95TgLFHTItTYNEibicEMU3w07G3gPEq9gD3H4KMwD0OCa2VhAmN0C1eU0l5nWH0Gl8L8SiccbCMaVL428jgZDAKlBZcM/640?wx_fmt=png&from=appmsg)

项目周报

左右滑动查看更多精彩内容

**场景三｜协同开发，代码逻辑清晰可见**

项目的 Git 仓库调用逻辑复杂、频繁更新，每次熟悉代码，都像剥了层皮一样痛苦。

现在，所有Git仓库都可以通过连接器上传到 OpenViking，并一键编译为 Code Wiki，清晰呈现函数间的调用和项目逻辑关系。每次开发时，你只需要跟安装好 ov 的 Agent 说：“基于xxx产品文档，帮我写一份技术方案”。

然后，Agent 就会通过ov自动查看库里同步的产品需求文档（来自飞书文档），找到当前项目的代码（来自于仓库），结合需求和现状，完成技术方案。如果是多人开发同一个项目也没关系，库里的仓库会保持定期同步，Code Wiki 也会动态更新，Agent 看到的永远是最新的，不用担心代码的版本问题。

进入测试，你也可以直接通过 Agent 看到所有的缺陷（来自飞书项目），指导它一步步完成修复，直到顺利上线。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeIGP0pg9sHr6ib3dkxDZfbtArgviaK4vdvlZvNAtiaY3OVOc4WuTMQ5sq2aqLasKXeYq1TDBgpiak08GF07A2ASGE6fuTNy6u1B6g/640?wx_fmt=png&from=appmsg)

项目上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeUA2hvdC1ZjUM1CmkvYahCybsXbJ5BN945WcRlNZbQzxArmpyYicy9MgGnbeS0fhdkMf0k0kicYCwDXqjiats2yK1lfLM0Fmhkq0/640?wx_fmt=png&from=appmsg)

编译出LLM-Wiki

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FectN6mkIUgh7JCAm2rpZiaiasWiavgpAkkOmNHOzhaI7OVysQx8SrxRtxia0ic2b3ZMIVP4Zeo8JnDC2ibicCAXc8L7t6gTbUq8tVHXlI/640?wx_fmt=png&from=appmsg)

OpenViking + Codex检索

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedM47RogrGJGQ2uPAa6JYBicsuLTI4XHniboEwkeIiaLrhZstNZ6sVbzpZoX3HSNiaqd6csg6bx3Px2DGyWcqwFfSReIsZwtIrab1k/640?wx_fmt=png&from=appmsg)

技术方案

左右滑动查看更多精彩内容

**最后**

OpenViking 将陆续覆盖钉钉、Confluence 等更多数据源，推出更强大且个性化的知识编译能力。

打通从数据连接到业务应用的高速通路。

现在接入，后续上线无需额外操作，即刻使用。

🚀 **上手试用，前 50 文档免费** **：**

https://s.c1ns.cn/WEuSd

🌟 **开源 OpenViking** **：** 访问 GitHub 仓库

（https://github.com/volcengine/OpenViking），为我们点亮一颗 Star！

❓ **三分钟测出你是哪种 Agent 饲养员选择属于你的 OpenViking**

https://blog.openviking.ai/post/should-you-use-openviking/

💬 加入飞书交流群&微信群！

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Feft7DUbpx1PgABHWtkB5piaoQLqUpOjmcEcDOHLhbBtjEb4zXTNpqOjgGHdPK07G7u2LSRdnTFuwsULpic2R4M7WSyUt10IWGFQo/640?wx_fmt=png&from=appmsg)

点击阅读原文立即体验👇

阅读原文 不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过