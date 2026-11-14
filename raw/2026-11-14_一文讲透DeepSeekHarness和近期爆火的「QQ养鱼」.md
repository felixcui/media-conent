# 一文讲透 DeepSeek Harness 和近期爆火的「QQ 养鱼」

**作者**: 小灰 & 千与编程

**来源**: https://mp.weixin.qq.com/s/3TEoeqmGIo8BnLpML6RuLw

---

## 摘要

**DeepSeek Harness 是开源的智能体运行底座**，底层是 **Cordis 微内核**、遵循「一切皆插件」：模型适配器、工具、存储、UI、调度逻辑全是可替换的插件，支持读写本地文件、跑代码、管会话记忆、权限隔离、多任务调度，**本地优先**（文件与会话留在本机）。这版新增：**桌面客户端**；**Creator 创造模式**升级，自带**插件自检、权限校验、打包分发**——这是「QQ 养鱼」能玩起来的前提，普通人用自然语言就能做出、打包、分发自己的智能体插件；**内置联网搜索与图片识别**，不用再装第三方插件补。文章重点实测把它接进 **QQ 消息通道**，并说清它和普通 QQ 机器人的本质区别：后者是**固定脚本、关键词触发、回复逻辑写死**，前者是按目标自主拆任务、**子 Agent 分工**。最后盘点插件生态，也讲了风险。

---

## 正文

在小说阅读器读本章

去阅读

大家好，我是程序员小灰。

最近 AI 圈子里「QQ 养鱼」这个玩法热度很高，许多粉丝在后台询问小灰：养鱼到底是什么？和普通 QQ 机器人有啥区别？

这股热度背后的核心载体，就是 DeepSeek Harness。 很多人只听过这个名字，却分不清它和普通网页大模型的差别。

今天这篇教程，我将用最直白、最直接、最不绕弯子的方式帮你搞懂 DeepSeek Harness，同时带着大家实践一下近期热门的 QQ 养鱼、多场景任务，盘点插件生态，客观讲清 DeepSeek Harness 的优势和风险。

文章较长，建议大家先收藏、不迷路。

## 一、DeepSeek Harness 新版核心能力

DeepSeek Harness 是 DeepSeek 推出的开源智能体运行底座，底层基于 Cordis 微内核，遵循一切皆插件的设计理念。 这里有一个很好理解的公式：Agent =大模型+ Harness。

大模型是大脑，负责思考、推理、理解需求；Harness 是承载大脑的身体，负责落地执行。它本身不是大模型，也不是单纯的聊天窗口，而是一套连接模型与真实电脑环境的执行框架：

可以读写本地文件、运行代码、调用工具、管理会话记忆、做权限隔离、调度多任务，所有能力单元（模型适配器、工具、存储、UI、调度逻辑）全部都是插件，随时可以替换、新增、组合，扩展性极强。 它支持本地优先运行，文件、会话记录默认存在本地，同时内置权限管控、沙箱机制，避免智能体无限制操作电脑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K0u5wQo0de2HNaxiaGf22hDG2ibaBj8dia8xju6vroB3erLLFXIxv4HaBYtGCdll32ibqgAuntoVtibt26tiaHmgexUDhYgz7LNOrFYfVrvYg37ibg/640?wx_fmt=png&from=appmsg#imgIndex=0)

## 新增桌面客户端

双击安装、图形化操作，告别黑框命令行，是小白友好度提升最大的更新。不用配置复杂环境，下载装好就能启动智能体。

## Creator 创造模式能力升级

自带插件自检、权限校验、打包分发能力。 这也是现在 “QQ 养鱼” 玩法可以落地的底层支撑，普通人也能用自然语言制作、打包、分发专属智能体插件，不再只能坐等大佬开源。

## 原生支持子 Agent 任务拆分

复杂任务自动拆解、并行调度执行。 解决了单 Agent 串行干活、长任务很容易卡死、中途中断的通病，做大项目稳定性强很多。

## 内置基础能力补齐

原生自带联网搜索、图片识别。 之前这些功能大多依赖第三方插件，现在开箱自带，基础能力不用到处找插件补齐。

## 二、重点实测：全网热门的 DeepSeek Harness QQ 养鱼

很多人混淆两个东西，这里先划清界限：

普通 QQ 机器人：固定脚本、关键词触发，回复逻辑写死，只能做简单应答、定时推送；

Harness QQ 养鱼：把完整 Harness 智能体接入 QQ 消息通道。可以自主思考、链式调用工具、读写本地文件，是一套带完整工具链的 Agent，不是简单的关键词机器人。

## 搭建核心流程梳理

前置环境准备 → 插件安装加载 → 消息通道绑定 → 白名单 + 消息限速配置 → 人设编写 → 工具权限精细化授权

## 前置准备

下载 DeepSeek Harness 桌面客户端，安装并登录账号。

账户充值，拿到可用模型额度，优先测试对话，确认基础对话、联网、识图功能正常。

准备：QQ 号（官方机器人无需单独 QQ；第三方方案准备小号）

## QQ 养鱼实操

打开 Harness 左侧边栏【插件】，点击右上角【添加插件】，输入插件地址：@tencent-connect/dsh-qqbot@latest，点击安装、立即启用。

![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de1tJxbgwga8ic2YxF6kv8zyciaSiaLiaZN8KmLbWaxuhicPTJnGwfphJtKGxUl3JWibeTBPNs0D8icKWpPPebLHQia9IAiaNlqq0bQNTicZM/640?wx_fmt=png&from=appmsg#imgIndex=1)

重启 Harness，左下角头像进入设置，找到【QQ 机器人】，调出绑定二维码，使用 QQ 扫码，填写机器人名称、简介，创建机器人并连接，配置白名单、消息限速：设置允许响应的群 / 好友，限制单分钟调用次数，防止并发爆账单。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/K0u5wQo0de2hp9HGNDJY7Q4jAthO9jTHLibTH00icUptukpylt8DY3ROSUCABuM1ias9Zg5fGqjiaIM1BHdm0M5pjvNNR45jwMM0S32R8tmm2ys/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

测试：私聊或在授权群内 @机器人，验证是否调用 Harness Agent、工具调用是否正常。

![](https://mmbiz.qpic.cn/mmbiz_jpg/K0u5wQo0de3bVraD04z1kqiacf2zeab3j5Z92RzHFfiaCtgRGgbVm667vnG4jFp5y0bZChaz1uUhKibqdkH25f9DOxnX8YoicrxvXLAkRhObOeA/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)

实测私聊、群聊响应速度、工具调用成功率，对比网页端 Harness，两者底层能力池保持一致。

## 三、DeepSeek Harness 实战任务测试

我们用 3个典型任务，直观感受新版 Harness 的落地能力：

## 任务 1：HTML 幻灯片 PPT（标准模式） 新增预览自查能力，智能体可以提前检查版式问题，排版错乱、页面翻车的情况明显变少。

标准模式主打轻量化、高稳定的静态演示内容生成，本次新增前置预览自查链路：智能体在输出最终 HTML 之前自动扫描页面布局边界、文字容器溢出、元素错位、字体截断、配色对比度、分页内容过载等版式风险，提前修正排版错乱、内容撑出画布、页面比例失调等问题，有效减少交付后 “页面翻车”。

需求产出：一套独立 HTML 幻灯片，无需额外依赖，浏览器直接打开播放；结构完整包含封面页、目录页、3 张主题内容页、结尾致谢页，支持键盘方向键、按钮翻页，自带演示控制栏，适合方案宣讲、内部技术分享。

![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de1znR0grnwgkK9vy9TZkEACDUVeah7m4KTm8micyRiaZC0rNlgcrJnzUqmrSRz9Q2fBUPLC7dJzRIFsdO7tYD0FtlzFTic2JchQSc/640?wx_fmt=png&from=appmsg#imgIndex=4) ![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de0iawOkWibGqdR5AWOSOZ0PxiaszgcnLKe3obkxqSGIdJstjicI8ftfKEtibichKib4fTico21Bwzu04HnHxzHDlNWM8h1BknBktdjpmiaE/640?wx_fmt=png&from=appmsg#imgIndex=5)

## 任务 2：AI 工具导航网站（PTC 模式） 依托子 Agent 并行开发，项目模块化拆分，多模块协同构建，复杂项目不容易半路中断。

PTC（Parallel Task Composition，并行任务编排）模式面向中大型 Web 项目，核心能力是需求模块化拆解 + 多子 Agent 并行协同开发。

主智能体对项目做边界拆分，把首页布局、分类管理、搜索检索、卡片渲染、详情弹窗、数据源维护拆成独立子任务，交由不同子 Agent 并行实现；模块之间约定数据接口，解耦互不干扰。

即使某个模块调试卡住，其余模块不受影响，解决长流程复杂项目容易中途中断、一次生成全量代码出错难以定位的痛点。

需求产出：一个可独立运行的 AI 工具导航站点，包含首页工具卡片流、分类筛选栏、关键词搜索、点击唤起详情弹窗；配套一份结构化 JSON 工具数据源，数据和视图分离，后续新增、修改 AI 工具只需要更新 JSON，不用改动页面渲染逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de3Qg9b80b5C5s00icMND8CnVAXUSjcCe7D848FaqHgrPThUOuZuuhyNO2WZJxcHX0fS8boyJWU1IVeBz7OOkHViaSiarXibbfWFia1Y/640?wx_fmt=png&from=appmsg#imgIndex=6) ![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de22d9Sbg18qc0EOTyzkfNpKLks0TiaNRfAqAyZT1EiaplyicK3QOichXEDjarpwkfDX7g6MpspX4ZX9z6Ek1biajFXW1Mgbz1iaTBfsA/640?wx_fmt=png&from=appmsg#imgIndex=7)

任务 3：3D 地标展厅插件（Creator 模式）

Creator 模式面向插件类、可嵌入型交互应用，专注自动生成标准化插件面板、资源调度、渲染主逻辑、自检与权限骨架，产出物遵循插件规范，调试通过后支持一键打包、跨环境分发嵌入。

需求产出：DeepSeek Harness 生态插件，自带左侧固定侧边栏作为功能入口；基于 Three.js 实现 3D 渲染，内置巴黎埃菲尔铁塔、中国长城、紫禁城、比萨斜塔四个地标模型；内置完整交互能力：

鼠标拖拽旋转模型、滚轮缩放视角、侧边栏点击切换地标，切换时同步展示对应建筑图文简介；框架层面内置插件权限校验入口、代码静态自检逻辑，自动检查渲染依赖加载、画布尺寸、模型资源、交互事件绑定异常；整体结构隔离，和宿主环境解耦，调试完毕即可打包成插件包，在 Harness 平台直接加载运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K0u5wQo0de27XZV1ATWHEDvsdJRZK7P5aVhUhTux9BxVBg5dCbJtsSsWzNlruSRnr81ib8oSFsOKHkqqZLf73AibI0WIq1JQvruEOw6Aryyvg/640?wx_fmt=png&from=appmsg#imgIndex=8) ![](https://mmbiz.qpic.cn/mmbiz_png/K0u5wQo0de34G59JCGtfB7yAo9I2qffaorIrBbXEARyoydtQshIiaKiac1SZQRnIctFMvWva3pNiaicaEsdL9KiagWlbk9dNxlA7qQTTHXYz8nJU/640?wx_fmt=png&from=appmsg#imgIndex=9)

## 四、DeepSeek Harness 插件生态：从 “拿来用” 到 “自己造”

Harness 生态最有意思的变化，是社区风向的转变： 早期的插件以 UI 美化、轻量化辅助工具为主，比如 XP 复古皮肤、看图插件、文件读取插件等。

如今社区重心已经转向工程化能力插件：子 Agent 调度器、长期记忆存储、定时看板、多模型路由切换、QQBot 消息通道插件……

一个非常明显的趋势是：大家不再只是下载别人开发好的插件直接使用。

越来越多人选择直接用 Creator 模式，按照自己的需求生成自定义插件，使用者也慢慢变成了创作者。

## 五、写在最后

## 好了，关于DeepSeek Harness 与 QQ养鱼，我们就介绍到这里。

## 最后我们来总结一下 DeepSeek Harness 的亮点：

1\. 上手门槛大幅下放：桌面客户端降低了入门成本，零基础爱好者也能体验可执行智能体；

2\. 架构灵活可扩展：QQ 仅仅是一个可插拔的消息通道，这套智能体的能力可以迁移到其他聊天载体，不绑定单一平台；

3\. Flash 缓存保留成本优势：合理配置后，可以节省不少调用开销，性价比可观。

但是DeepSeek Harness 也存在需要留意的问题：

1\. 群聊场景一定要做好限速、白名单、调用次数限制；一旦并发失控，调用成本会快速飙升；

2\. NapCat+OneBot 桥接方案存在明确风控风险，仅适合小号娱乐测试，不要使用主账号；

3\. 智能体依然存在幻觉问题，日志回溯仅能辅助排查问题，重要结论务必二次核验。

正在读这篇文章的朋友，你最想用 DeepSeek Harness 实现什么？是搭建 QQ 智能助手，还是写代码、分析文档？欢迎在评论区交流。

< END >

最近小灰创建了一个AI副业交流群，对AI和副业变现感兴趣的朋友，都欢迎进群交流。扫码添加小灰微信，备注“ai“即可进群：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/9ojSnBX2WWaursxyQ3btbQia7SFOnPlRfX9omFDfVcV2gUDJQsgdRt4Fyqfib6yEgvGz7XJyvZH8hACLmOhicJGAHibCrMjVkHyJrEZdReBPO38/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过