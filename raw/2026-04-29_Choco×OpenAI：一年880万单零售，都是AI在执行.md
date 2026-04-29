# Choco × OpenAI：一年 880 万单零售，都是 AI 在执行

**作者**: 金色传说大聪明

**来源**: https://mp.weixin.qq.com/s/nSQ62QYEYsy17a6Zo-aNMg

---

## 摘要

Choco利用OpenAI API处理每年880万以上订单，调用超过2000亿token，将订单错误率降至1%至5%，减少50%手动录入并提升两倍销售效率，通过OrderAgent和VoiceAgent实现24/7自动收单与隐式上下文消歧，其成功关键在于动态in-context学习与持续评估体系。

---

## 正文

金色传说大聪明 金色传说大聪明

在小说阅读器读本章

去阅读

HOW

OpenAI 分享了一份「Choco」客户案例

Choco 是一家面向餐饮分销商的 AI 平台， 过去一年用 OpenAI API 处理了 `8.8M+` 订单， 调用过 `200B+` token， 把订单错误率压到 `1-5%`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jXSGuwJvpdias0gn5K6HuFbEshP7M0icYBhxnNRczwdbHYZ8DxV8UNAoc2eH8Aial12icMtHLd7HTv1jrrIsXcbI1CWrpK4ZMQkQJYxw0FiaCa4Q/640?wx_fmt=jpeg)

https://openai.com/index/choco

## Choco 是谁

Choco 2018 年柏林创立， 创始人是 Daniel Khachab 和 Julian Hammer. 这是食品分销技术领域第一家独角兽， 累计融资超过 `328M` 美元

平台目前服务 21000 多家分销商， 覆盖 100000 多家餐饮买家， 业务跑在美国、英国、法国、德国、西班牙、UAE

门店给分销商下订单有 6 种方式： 电话、短信、邮件、图片、传真、手写便条。每天傍晚以后， 分销商的订单台员工要花大量时间， 把这些信息手动录入 ERP

订单台员工脑子里， 还装着每家客户的隐式上下文， 常订哪个 SKU、单位用箱还是斤、送货走什么节奏。新人接手要时间， 老人离职就是知识缺口

Choco 的工程 VP Narbeh Mirzaei 在 OpenAI 案例研究里讲： 处理输入只是第一道门槛， 真正难的是隐式上下文。客户特定的 SKU 映射、单位偏好、配送规律。这些知识住在订单台员工脑子里， 要把它们编码进 inference 层去消歧

## 两个产品

OrderAgent 接异步收单， VoiceAgent 接实时电话。Choco 用这两个 agent 把订单两端都连起来

### OrderAgent， 订单 agent

OrderAgent 收下所有非电话的输入。邮件、短信、图片、文档全收， 出口是结构化的 ERP 订单

关键工程在动态 in-context learning. 系统拿每个客户的历史订单和产品目录， 去消歧。Mirzaei 原话翻译过来， 转录和提取能力是底子， 真正的工程挑战是动态 in-context learning. **这是 automation 和 intelligence 的分界**

OrderAgent 用 OpenAI 的 SDK 和 API， 把 speech-to-text、embeddings、function calling 一起接进基础设施。Choco 自己搭了一套 evaluation framework， 包括 ground-truth 数据集、连续监控、A/B 测试， 保证生产环境的准确率和性能

### VoiceAgent， 语音 agent

VoiceAgent 跑在 OpenAI 的 `Realtime API` 上， sub-second 延迟接电话， `24/7` 接得动。会听单， 会查库存， 缺货时推荐替代品， 临期商品做促销， 最后一个干净的结构化订单进分销商的 ERP

多语言， 门店打的还是同一个号码， 开口说话也是同样的方式

VoiceAgent 12 月初由 Choco 和 OpenAI 联合发布， 当时官方说法是「食品行业第一个 AI Voice Agent」. 这次进 OpenAI 案例研究再亮相， **OpenAI 自己挑了 Choco 当 enterprise 标杆**

## 成绩单

OpenAI 案例研究里给了 6 个数据点：

→ `8.8M+` 订单/年， 全部走 AI 一道

→ `200B+` token 在生产环境跑过

→ `50%` 手动录入下降

→ `2x` 销售团队生产力， 团队不加人

→ `1-5%` 错误率， 自动化阈值可配置

→ `24/7` 收单， 夜里和周末没有延迟

Choco 自己博客披露的早期数据： 新接入的分销商 2-3 周内达到 `90-97%` 订单准确率， 每周节省 `15` 工时以上， 每单手动工作量降 `70%`. Autopilot 模式下， 早期采用者 `50%` 订单已经全自动进 ERP

## 工程方法论

Choco 在案例研究里给了三条 lessons: evaluation、observability、概率系统的预期管理

**第一， evaluation 从第一天就跑**. 哪怕只有 10-20 个 ground-truth 例子， 团队也能开始度量进展， 验证改进， 有信心迭代

**第二， 搞 AI-native observability**. 调试 AI 系统超出传统日志能覆盖的范围。要捕获模型输入、输出、reasoning trace， 才能理解和改进性能

**第三， 管理对概率系统的预期**. LLM 输出本身带概率波动。教育团队和用户接受这一点， 是建立信任和减少摩擦的关键

这三条本身不算新， 但作为一家年处理 `8.8M+` 订单的 production AI 公司沉淀出来， 分量在那

## 下一步： agent orchestrator

Choco 接下来要把 agent 推进更多业务流， 包括销售、电商、供应链

Choco 给一类新角色起了名字： agent orchestrator. 他们不写代码， 但设计和管理 agent. 「non-engineers」这个词他们写得很明确

Choco 从 workflow software 在转向 AI execution infrastructure. **操作 agent 的人， 正在替代写脚本的人**

## 参考材料

OpenAI 案例研究

https://openai.com/index/choco

Choco × OpenAI 联合公告

https://choco.com/us/press/choco-and-openai-join-forces-to-launch-the-first-ai-voice-agent-for-the-food-service-industry

Choco VoiceAgent 介绍博客

https://choco.com/us/stories/suppliers/introducing-the-choco-voice-agent-built-by-choco-in-collaboration-with-openai

Choco VoiceAgent 演示视频(YouTube)

https://www.youtube.com/watch?v=nHnCaIPVJgQ

Choco OrderAgent 产品页

https://choco.com/us/orderagent

继续滑动看下一个

赛博禅心

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过