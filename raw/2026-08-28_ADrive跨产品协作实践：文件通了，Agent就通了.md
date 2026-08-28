# ADrive 跨产品协作实践：文件通了，Agent 就通了

**作者**: 火山引擎存储

**来源**: https://mp.weixin.qq.com/s/OmSFLQude7MpGXOCJjQSjw

---

## 摘要

针对Agent工作流中文件依赖人工搬运的痛点，ADrive通过统一的文件协作空间与ADrive CLI工具，让不同Agent实现文件的无缝流转与接力。文章以48小时新品视频发布实战为例，展示了Codex、豆包工作和DeepSeek Harness三个Agent分别负责策划、制作与发布，围绕同一套文件空间高效协作，将对话成果转化为可交接的正式文件，同时由人类把控关键写入风险。

---

## 正文

火山引擎存储 火山引擎存储

在小说阅读器读本章

去阅读

本文基于 ve-adrive-cli v1.0.2。文中的品牌、项目和文件名均为演示示例。

Agent 已经进入内容策划、素材制作和发布检查的工作流程，但文件仍主要靠人工搬运：资料散落在本地目录、聊天附件在临时链接中，一个 Agent 生成的成果，常常无法直接作为下一个 Agent 的输入。

ADrive 面向人与 Agent 提供统一的文件协作空间；ADrive CLI 则把查找、读取、传输、同步和权限控制带进 Agent 的工作环境。不同 Agent 可以围绕同一批文件接力，关键写入和高风险操作仍由人确认。

下面通过一场 48 小时的新品视频发布实战，看看 Codex、豆包工作和 DeepSeek Harness 如何围绕同一套文件接力。文末再用 3 分钟完成 ADrive CLI 的安装与连接。

**48 小时倒计时：一个目标，三个角色，一套文件空间**

一家消费品牌准备在 48 小时后发布新品，需制作一条新品宣传视频。团队已有产品 Brief、用户调研、采访录音、产品图片和原始视频，但资料由不同成员制作，格式和体积各不相同。

团队在 ADrive 中建立“新品发布项目”，并约定五类目录：Brief 保存产品资料，Research 保存用户洞察，Raw Assets 保存原始素材，Production 保存制作产物，Publish 只放最终发布包。

Agent 正在成为日常办公工具，但不同角色往往选择不同的 Agent：内容策划使用 Codex，内容制作使用豆包工作，发布运营使用 DeepSeek Harness。三者分别负责理解、制作和交付；ADrive 文件协作空间统一存放项目资料和产物，ADrive CLI 负责让文件在三个 Agent 之间流动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee6p3fj5yAl4XA99BXlgicARJPcib9mnXiaH5kcsEAYu5g76qbxfodfSDSYZicxGznjibVVt7icj77OQlQzqycicjlBgOd2t5t6hIYKXQ/640?wx_fmt=png&from=appmsg)

**第一幕** **：内容策划** **× Codex**

**把资料变成创作方案**

1. 发布前 48 小时，内容策划小林把任务交给 Codex：

“我们要制作一条 15 秒新品视频，目标人群是年轻职场人。请查看 Brief 和 Research，找出最近更新的产品说明、用户访谈和品牌规范。先列出准备读取的文件，不要查看原始视频，也不要写入内容。”

Codex 根据自然语言描述 ADrive 空间中的目录、文件名和修改时间，生成读取计划。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecJiaDbXxlpTd2r2TQzs8STUhPMtibLoGRPNM0lmFShUFfsN1ZXTFVng81Eyxswpbx1W4EFZGcbdpcQPnzcU5ecmwo4oenBJ5StQ/640?wx_fmt=png&from=appmsg)

2. 计划确认后，小林继续说：

“基于这些资料给出三个创意方向，推荐其中一个，并生成视频脚本、分镜和素材需求清单。写入 Production 前先告诉我文件名。”

Codex 推荐“把通勤时间还给自己”作为主线，准备写入创意说明、15 秒脚本、分镜和素材需求清单。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedX71ias8F0VvPXS0hvbETPibdV53b1Ov8jXMrYXanfy7reBH7RBHfE6UJBtnYCYRR2IYTQ4IW21CtMDGKObibMeLFkiaic6WAIFk8I/640?wx_fmt=png&from=appmsg)

3. 小林确认后，四个文件才进入 Production。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefMWv9so49ts0PkPe94pVBQJE5sqiaHS0cSiaQ3L3UAaurcgKhP1WtWUs2TO0WOy5PS8KfrnwYibGhWyia04bG75PDd3FNqKl7GNkk/640?wx_fmt=png&from=appmsg)

这一步把策划成果从一次性对话变成了可交接的正式文件。制作人无需重新询问背景，也不用接收一堆聊天附件，直接从 Production 接手即可。

**第二幕** **：内容制作** **× 豆包工作**

**让大素材和中间产物流动**

1. 发布前，首先明确 ADrive 项目空间。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefO6YmhB9SLcPk4IlciaFvD8YzjpWtjUXASq08OZ5Y0mibchoCD5TtWnMZCx0I3w1C0QByuAqXNbUAqZaCCsUibESeUDEhy65fOfk/640?wx_fmt=png&from=appmsg)

2. 发布前 24 小时，内容制作小周对豆包工作说：

“读取 Production 中的最终脚本、分镜和素材需求清单，再检查 Raw Assets。告诉我已有素材、缺失素材和传输计划，不要一次下载全部内容，也不要修改原始文件。”

豆包工作根据需求与现有素材，发现主要画面和采访录音已经齐全，但缺少一些特写素材。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefJPensFdUUG8JV3tbyyOkP075jp990NHqxy2oDX0xyicSnGbMiahg1wrWTtuXeRAs2ZCvaOLF9pjZO18Q7IRkadWhdSwJnZU2Go/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeHIoxudgasrrehoayCgL3HJPnQiaAkzBwHiaiczhLVqZYcsAYBvzDShdw7AfHFC7icUMMGCuTIAnEO6wGgabrhbPKpdOaEK83s10E/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeedWIpSHF5UBJ21ic60Wao2axBh9qz5oZL8v0Bwq7ibBLgshKZKR0VnRxrZnv3pmeZcz0u1KV0hibOmT44ydjAf8mwxJOlmxeXeK0/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM59tX23msrEP4xpXeEUq6tQcPM2LhyWXm7h0jqib7RadsGGf5Kj5sBefxQeTrniaa2fCdIGib838j7Rf1xRXAmFS96XHYzenamtttxw1SzpbEJ5w/640?wx_fmt=svg&from=appmsg)

左右滑动查看更多

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5JRHWiawQVGajeZdxY8qYxMnv9L0ML4jMYWhia3dciajbImicPVPXCH5rGbubvW4zfCOIMyAgTkQiciaib2Tw8oAKmUmxZY3uffsKFsfRpNdSzx2bRQ/640?wx_fmt=svg&from=appmsg)

小周补齐素材后确认传输。在大体积视频素材的传输过程中，Agent 会使用可恢复的传输检查点，网络中断后无需从头开始。

3. 豆包工作将选定素材同步到本地制作目录，再调用已经配置好的字幕、封面和视频制作工具。第一轮完成后，它向小周汇报：

“粗剪视频、第一版字幕、两张封面和制作说明已经生成。我准备把这些文件写回 Production；临时缓存不会上传，原始素材不会修改。是否写入？”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fec06fuBZ2GrgrAC17YGibkjzBDQnoa4W7ZgGD4y3arM9OcqwJ4pKMV7bibNbHRGY2kEvXIZyv0vViblzKr80APcwIU3pARY4NuC5k/640?wx_fmt=png&from=appmsg)

4. 小周确认后，豆包工作只同步新增和修改过的正式产物。经过两轮调整，Production 中留下脚本、粗剪、字幕、封面和制作说明。下一位接手者既能看到当前版本，也能知道还有哪些问题需要处理。

**第三幕** **：发布运营** **× DeepSeek Harness**

**自主检查，但不擅自执行**

发布前 2 小时，运营小陈在 DeepSeek Harness 中使用 ADrive CLI 连接到同一个 Space，开始确认发布细节：

“检查 Production，确认最终视频、封面、字幕和发布文案是否齐全。”

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeekpfdQl2PZnAYWDTN7CqmL8xWia4XMlEwZsXvashfFgK1UibrC7xr2WX6uLtQrLHNo8DfVsj07p33xXzJVANTr7HKxUhLJDQMoc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeCibxgicaicxMIggSe1FS1BFMJBpPrAWbBsU1b4nP7UA3a7ZdOeDQyYHDibLGp0qic1KPP5dnicCtg2SICuIX7BByw5Puf9CiaxIm7Uw/640?wx_fmt=png&from=appmsg)

检查通过后，DeepSeek Harness 给出执行计划：把已批准的成片、封面、字幕和三份渠道文案复制到 Publish，同时保留 Production 中的全部历史版本。

“以上操作只会向 Publish 新增和更新已确认文件，不会删除 Production 中的内容。是否执行？”

小陈确认后，DeepSeek Harness 才执行文件操作。ADrive CLI 会先生成操作计划，收到明确执行指令后再运行；删除、移动或同步删除等高风险操作，还会触发更严格的确认。

最终，Publish 中形成一套可以直接交付的发布包：成片、封面、字幕、渠道文案和发布检查清单。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefJlO7cDd0EMEkibSicJMx4V38GiaTILSicK7Ea4ickCubqBtcQI63f2HRp2paUsJFCVhnC1DibG4iaT3jL8sn8gfPo8IvOU3lvd1aWzA/640?wx_fmt=png&from=appmsg)

**交付结果：Publish 中的最终发布包**

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeclicLasTXicxPW1VXXlBRkJEAR970tzQHWdTVQeWKhHhVu90mq9lcONzFia6nbX4LB7pZwfHzw9KGeHicDQHKn5AD0z5xKKmfGrds/640?wx_fmt=png&from=appmsg)

**接力的关键：共享文件，而不是共享对话**

这条工作流中，上一个 Agent 写回的文件就是下一个 Agent 的输入：Codex 把资料变成脚本和分镜，豆包工作把脚本与素材变成视频、字幕和封面，DeepSeek Harness 检查成果，并在人工确认后组装发布包。

三个角色可以使用不同的 Agent，却不需要建设三套文件集成，也不用反复上传同一批附件。ADrive CLI 提供统一的查找、读取、传输和写回能力，大文件检查点与增量同步则保证素材稳定流动。

模型决定内容生成得有多快，文件基础设施决定这些内容能否成为可交付、可复用、可管理的工作成果。

落地时，不必先设计复杂的多 Agent 工作流。选择一个正在进行的内容项目，先跑通 **读取资料—生成产物—写回 ADrive** 的最小闭环，再让第二个 Agent 直接接手。一次可靠的文件交接，就是 Agent 协作真正开始的地方。

**看完案例，用 3 分钟把 ADrive CLI 交给 Agent**

无需先学习命令。把 **ADrive CLI 的 GitHub Release** （https://github.com/volcengine/ve-storage-uni-cli/releases/tag/v1.0.2）发给 Agent，让它完成安装和连接；你只负责确认来源、选择空间，并在浏览器中授权。

**第一步：安装**

对 Agent 说：

“请从这个官方 Release 安装 ADrive CLI。识别我的操作系统和芯片架构，只安装 ve-adrive-cli，校验官方 SHA-256，并告诉我最终版本。”

Agent 会选择对应的安装包并完成校验。本文验证时得到的版本是 ve-adrive-cli 1.0.2。

**第二步：授权**

告诉 Agent 要连接的 ADrive Instance，并优先使用 OAuth：

“请用 OAuth 连接这个 ADrive Instance，发起设备授权。不要在对话中输出任何访问令牌。”

示例：OAuth Auth Endpoint

https://614fc48\*\*\*\*.idsapi.volces.com

其中 614fc48\*\*\*\* 为网盘 ID。

Agent 会提供浏览器验证地址。你登录 ADrive、检查权限范围并确认授权，凭证随后保存在本地。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FeexjaE2IAtN3e79uLZwskwL1bbtShfib4EERTW65D4XmS75XyxjCSs0GKtsIibib90wBOBBPzkE942qh3fjQ5YAsicibjXGIBoDDCicc/640?wx_fmt=jpeg&from=appmsg)

**第三步：只读验证**

授权后继续说：

“检查当前登录状态，只列出我有权限访问的空间，不要上传、移动或删除文件。”

选择本次协作使用的 Space 后，再告诉 Agent：

“把这个 Space 作为工作空间。写入前先给我计划，涉及移动、覆盖或删除时必须再次确认。”

至此，Agent 获得的是一个边界明确的文件工具，而不是无限权限的网盘账号。接下来的任务都可以用自然语言完成。

**立即开始：** 下载 ADrive CLI（https://github.com/volcengine/ve-storage-uni-cli），选择一个正在进行的内容项目，跑通第一个文件协作闭环。

**申请试用：** 如需开通 ADrive，请联系 ADrive 团队。

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过