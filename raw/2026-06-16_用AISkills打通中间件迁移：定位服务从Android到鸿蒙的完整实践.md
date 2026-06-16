# 用 AI Skills 打通中间件迁移：定位服务从 Android 到鸿蒙的完整实践

**作者**: 用户&amp;内容技术

**来源**: https://mp.weixin.qq.com/s/oMjsImv2x7sJAEPZBWpH5g

---

## 摘要

用户&内容技术 用户&内容技术 本文以Android到鸿蒙的定位服务迁移为实战案例，深入剖析了AI辅助开发中通用智能与领域知识断层的根本矛盾，提出并验证了“AI + Skills”解决方案。实践表明，相比纯AI翻译的低准确率和人工查源码的低效率，AI + Skills模式不仅将单服务迁移时间缩短至30分钟且零编译错误，更在154个服务的规模化迁移中节省25小时，实现了知识的资产化、可复用与持续演进。

---

## 正文

用户&内容技术 用户&内容技术

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/33P2FdAnju9cLcib00YV66gYq2V6Fhm7YTHlzZdFwfnCtxyBCvgiaicG65n8du0mUYunHZIaBKohjsBxA4sgrPSjQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

本文以Android到鸿蒙的定位服务迁移为实战案例，深入剖析了AI辅助开发中通用智能与领域知识断层的根本矛盾，提出并验证了“AI + Skills”解决方案。该方案通过将API映射、枚举细节、回调差异及常见陷阱等隐性知识转化为结构化、AI可读的Skills文档，明确了AI负责通用逻辑生成、Skills提供精准领域知识的分工模型，实现了从“面向人”到“面向AI”的知识传递转变。实践表明，相比纯AI翻译的低准确率和人工查源码的低效率，AI + Skills模式不仅将单服务迁移时间缩短至30分钟且零编译错误，更在154个服务的规模化迁移中节省25小时，实现了知识的资产化、可复用与持续演进，最终展望了从静态文档向知识图谱、主动建议及组织级知识中台发展的未来路径。

引言：AI 辅助开发的根本矛盾

> 又双叒叕经历从0到1翻译一个安卓应用到鸿蒙的需求，并且近期Skill的概念很火，想着能通过Skill真正的解决一些实际业务遇到的一些问题，所以开始着手维护一个鸿蒙依赖分析的Skill，为了协助Curosr更好的理解端侧的二方包，最后我得出了两个暴论：
> 
> 1、目前很多知识库是冗余的，随着模型能力越来越强，需要提供的业务知识库是需要减负的
> 
> 2、未来我们各种二方包的接入方式都会以Skill的形式提供，从面向人转到面向AI

▐现状：AI 很强大，但不够"准确"

**场景还原** ：

```typescript
// 你向 AI 提问："帮我将 Android 定位服务迁移到鸿蒙"// AI 生成的代码（看起来很专业）LocationExpires.ONE_MINUTE    // ❌ 这个枚举值不存在params.onSuccess = (result) => { ... }  // ❌ 回调位置错误// 编译器提示：13 个错误Property 'ONE_MINUTE' does not exist on type 'LocationExpires'
```

**开发者的困惑** ：

- AI 不是能理解代码吗？为什么会犯这种低级错误？
- 文档明明存在，为什么 AI 不看文档？
- 第一次踩坑修好了,第二次还会踩,知识怎么沉淀？

▐本质：AI 的能力边界

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2iaumyzXqxFBMiaas2nEqdLxWYfPdYBUVxicfOBHcEj0YKAgLIUnrvuiatiaIkh9hicbxmibhULMqTWQriaqFrBPUBXbe5hBWGSBB7x34/640?wx_fmt=png&from=appmsg)

**根本矛盾** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp3boXpbygAJCPsTERyz8aIltqETwUoVm4z5X0lgUVJHicctyXr4I3fibuc2EwI8ZEpnEia72iaLXwZhRLDIXZRAWCrhYeqsiboiaD2oM/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/33P2FdAnjuicZrWZ3a7SNVtibcNht0QoXTXKZWKec4l37w6NC4la1sV53zcZqqMO9wnqskOicSVEFvXiboFHlhWDbg/640?wx_fmt=png&from=appmsg)

重新定义问题

▐这不只是"代码翻译"问题

**表面问题** ：Android 代码如何迁移到鸿蒙？

**深层问题** ：

1. **知识获取：开发者如何快速掌握新平台的 API？**
2. **知识传递：团队如何避免重复踩坑？**
3. **知识演进：API 更新后如何快速同步？**
4. **AI 协同：如何让 AI 使用最新的领域知识？**

**对比传统方式** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp0Jv32py9lqicLklORCYvKCSKaLs19xdjFzMNgaZ9Zmm8JiaD7tibS6bhK03CRdnGGZZE2veA6ULZwticpUSiaKpUQctsZOWJrUmHuc/640?wx_fmt=png&from=appmsg)

▐这是一个"知识工程"问题

**软件工程的两大知识库** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1j0VYxTuJfNiaOee3iaWfxVWNeibicrUhE6JeUh2BicW5icvuX1q6v3hoNB6AfzUR3icuE6GibDGSzWqvR6BgaKguSEHH68RKv7whouT8/640?wx_fmt=png&from=appmsg)

**知识的三个状态** ：

1. **隐性知识：在老员工脑子里（"这里要用 ONE\_MIN，别用 ONE\_MINUTE"）**
2. **显性知识：在文档里（但分散、滞后、难搜索）**
3. **可执行知识：在 Skills 里（结构化、可索引、AI 可读）**

**AI + Skills 的价值** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2tdcOQ1UWPicjtCJ0xvlke1mG3Pj2lZZN0Vg7ZicvVZL6teI9icG7CNIU101j8VibsTaibVIzDX9ibm3XYdpn6XBBmtv0rc5iabSyyxc/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/33P2FdAnjuicZrWZ3a7SNVtibcNht0QoXTPXlMC7M5h83yzCia08ia5SksCneXXPkicCvWGTgaIStFe0XPAOzaOvLlg/640?wx_fmt=png&from=appmsg)

AI + Skills 方法论

▐核心概念

**定义** ：

AI + Skills = AI 的通用能力 + 可执行的领域知识包

**类** **比理解** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1eTULu6V4ygxEySKCyleh794PDXM8FNLP7BaehyydxQd87oSbs4y6e9FQrY3JperKtx9RZFJZ475kfxyWvyZLKcuhUFzoCwbY/640?wx_fmt=png&from=appmsg)

▐分工模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0UAIibvHuQ8kMcjYQibQH0cFxpzKJmEJDFictZ6UPuCBI6CjFkQiaYfJ1wibE8yVtt4HbliagjUQ1fdB1POosicqjm2ia3ahaaCTEMRR4/640?wx_fmt=png&from=appmsg)

▐工作流程

**完整闭环** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1SYibcdHFl7Iia8rIrdBCAZODUGXDeWoxtXcE9SdSbbCefdydwLM1jib5ITcuOEhg1tr3GvkHnvXxnyfTE60ARrdbPIm6OrEna6M/640?wx_fmt=png&from=appmsg)

**关键环节** ：

1. **输入阶段：AI 加载 Skills 获取领域知识**
2. **生成阶段：AI 使用 Skills 中的映射表**
3. **验证阶段：编译/测试验证准确性**
4. **反馈阶段：问题 → 提炼 → 更新 Skills**
5. **沉淀阶段：成功经验 → 记录到 Skills**
![](https://mmbiz.qpic.cn/mmbiz_png/33P2FdAnjuicZrWZ3a7SNVtibcNht0QoXTEckyrs2AEMfbYLRp4wWezyVM5XiaEeDC8UW37DXUNVNazPXhxt8LB0w/640?wx_fmt=png&from=appmsg)

实战案例 安卓定位服务 - 鸿蒙代码迁移

#### ▐ 问题背景

**业务场景** ：穿搭业务需要从0到1迁移到鸿蒙

**技术挑战** ：

- 154 个 Android 服务需要迁移
- 每个服务涉及不同的 API 映射
- 团队中大部分人不熟悉鸿蒙 API

**传统方式的成本** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp3hJronxXJP07BFOnCLOvz3iaXDAvUZhnKMWl8kiaVxP4gBuJoC1RTdicIJfYjh670F555NhOEbSbiaXI5WfiaAEtGSwBqheENzVAt4/640?wx_fmt=png&from=appmsg)

#### ▐ 三种方式对比

## 方式 1：纯 AI 翻译（❌ 快但不准）

**操作** ：

提问："帮我将 Android 的 LBSService 翻译到鸿蒙"

**AI 生成的代码** ：

```javascript
// AI 基于"常识"猜测的枚举值LocationExpires.ONE_MINUTE    // ❌ 实际是 ONE_MINLocationExpires.FIVE_MINUTE   // ❌ 实际是 FIR_MINLocationAccuracy.MID_MODE     // ❌ 这个枚举不存在// AI 推测的回调方式const params = new LocationRequestLocationParams();params.onSuccess = (result) => { ... };  // ❌ 回调不在这里
```

**结果** ：

- 编译错误： **13 个**
- 调试时间：无法估计
- 根本原因：AI 没有准确的 API 文档

## 方式 2：查源码 + 人工修正（✅ 准但慢）

**操作流程** ：

1. 打开 Mega Location 源码
2. 查看实际的枚举定义
3. 逐个修正 AI 生成的错误
4. 测试验证

**发现的真相** ：

```typescript
// ✅ 实际的枚举定义（非常反直觉）export enum LocationExpires {  ONE_MIN = "ONE_MIN",     // 不是 ONE_MINUTE  SEC_MIN = "SEC_MIN",     // 不是 TWO_MINUTE (SEC = SECOND)  THR_MIN = "THR_MIN",     // 不是 THREE_MINUTE (THR = THREE)  FOR_MIN = "FOR_MIN",     // 不是 FOUR_MINUTE (FOR = FOUR)  FIR_MIN = "FIR_MIN"      // 不是 FIVE_MINUTE (FIR = FIVE)}// ✅ 实际的回调方式const options: Location.LocationRequestOptions = {  onSuccess: (result: LocationData) => { ... }  // 回调在 options 内};
```

**结果** ：

- 编译错误： **0 个**
- 耗时： **40 分钟**
- 问题：知识留在开发者脑子里，下次还要重新查

## 方式 3：AI + Skills（✅ 又快又准）

**Step 1：构建 Skills**

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1ueSKCuOhYHzmNm1aRHibcZibgIqDYHW3uk5GaCxcrwDDcGPlP8stXqpRgRYtjvkIpMduNoomQuf3pYyUJKfL6fdmIDWGzGds40/640?wx_fmt=png&from=appmsg)

```perl
## 4. API 对比### 4.1 LocationExpires 枚举值映射| Android 常量 | 鸿蒙枚举 | 说明 ||-------------|---------|------|| "1m" | LocationExpires.ONE_MIN | ⚠️ 不是 ONE_MINUTE || "2m" | LocationExpires.SEC_MIN | SEC = SECOND，不是 TWO_MIN || "3m" | LocationExpires.THR_MIN | THR = THREE，不是 THREE_MIN || "4m" | LocationExpires.FOR_MIN | FOR = FOUR，不是 FOUR_MIN || "5m" | LocationExpires.FIR_MIN | FIR = FIVE，不是 FIVE_MIN |⚠️ **不存在的枚举值**（AI 经常错误生成）：- ❌ \`ONE_MINUTE\`, \`TWO_MINUTE\`, \`FIVE_MINUTE\`- ❌ \`TEN_MINUTE\`, \`MID_MODE\`### 4.2 定位请求方法对比| Android | 鸿蒙 | 差异说明 ||---------|------|---------|| \`LocationServiceBridge.requestLocation()\` | \`Location.requestLocation()\` | 回调方式不同 |#### 关键差异：回调设置方式**Android**（回调作为独立参数）：\`\`\`kotlinLocationServiceBridge.requestLocation(    params,    { result -> ... },  // 成功回调    { error -> ... }    // 失败回调)
```

**鸿蒙** （回调在 options 对象内）：

```typescript
const options: Location.LocationRequestOptions = {  bizName: 'TB_SHOPPING_PROCESS',  onSuccess: (result: LocationData) => { ... },  // ✅ 在 options 内  onFail: (error: string) => { ... }};Location.requestLocation(params, options);
```

## ▐ 三种方式的本质差异

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp3EUicpulicDatx7D4YNiauPerWiblDoLaJ80JcJAHNcXTibelS7ERw2sNGmbia3GzhfS7ziafetDvuSZQxJM3PKVWCTT6lSKUaMP849g/640?wx_fmt=png&from=appmsg)

**关键洞察** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp3UgChSo81n1Gc12gSt2yuBR6f36qiaJCAB4cdDNgiaYYHEqO2dXDzFeK36DOzkQZ0umjP9dMdDF7nUGJRMnjUgkCE3jwKZ4NibVI/640?wx_fmt=png&from=appmsg)

## ▐ 规模化效果

**单个服务的迁移效率** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp3qK7x3OY2HDibQZrWEgDdZc0BAkya9Zvo602gCzO5Pib2lFcSH7f3VSzuYutOnCcYY2gaNvO67t9diaGuv9xfqic32Odz4dKEh2gE/640?wx_fmt=png&from=appmsg)

**154 个服务的总成本** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp1mhlTLuRF3vG8znIOfOQL6yYns3qDdHW2MP0tibhXSq0jAHBCKV3tc4v1iceloqUkdL29Floib0t506iaQSoD3oWwg8cgia6CPjIzE/640?wx_fmt=png&from=appmsg)

**节省时间** ： `102 - 77 = 25 小时`

**关键价值** ：

- ⏰ **效率提升** ：节省 25 小时
- 📚 **知识资产** ：154 个服务的迁移经验永久沉淀
- 🚀 **团队加速** ：新人 0 学习成本
- 🔄 **持续演进** ：API 更新后，只需更新 Skills

## 方法论推广

#### ▐ 适用场景

AI + Skills 模式不只适用于代码迁移，而是适用于所有 **需要领域知识的 AI 辅助开发场景** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp2pD0Lw3sMKO1b1CeEgoZtU97OSm4OOuX2hQmj27BuA6iaW1DdRiceCicXCkzjkesfMw9DkQ5NX7fDXY0zHCb0YXH6JNhUZRMQ63c/640?wx_fmt=png&from=appmsg)

**通用模式** ：

有明确知识的场景 → 知识结构化为 Skills → AI 索引使用 → 提升质量和效率

#### ▐ 构建 Skills 的原则

## 原则 1：AI 友好的结构化

**❌ 不友好的文档** （人类可读，AI 难索引）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0ibXMkVianyaLwMXIbQW6gowicofyP0lGGicIaE3ZpRwPpyEUXNVTDOmoxsLzAHjqKY1c6sClxQCWJh8VGekBeYxMyD4RFUP0BGGI/640?wx_fmt=png&from=appmsg)

**✅ AI 友好的文档** （表格化、结构化）：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp3GMqHQIktnLbzXjKaygiaqUGWvCPUFR7Pay7ibGSRw5vkKNQOibkxia0frAfoeZrZ7JqOf3v32JneWV224JErtZu2GZe5Z60X9Mgo/640?wx_fmt=png&from=appmsg)

## 原则 2：持续演进

**Skills 更新流程** ：

遇到问题 → 查看源码 → 提炼规律 → 更新 Skills → 发布版本 → 团队同步

## 原则 3：分层组织

**Skill 文档结构** ：

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1BvglYTLpibRgoVNOiaj5vsyJYeJqSYtHJGRmpoWGvicZFicc7UqXT4iboDKCMHycFwpJU7oia1v5zhJ9PlvRnYzvJlkoZdEyqL3QBY/640?wx_fmt=png&from=appmsg)

## 未来展望

#### ▐ 从 Skills 到知识图谱

**当前：文档化的 Skills**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0UKWZGaKnSyvEYXGpRHg90Fk1ScQWjQSU1PkboMfuzgQm8PIcXp1zlcfeu0Dhr3QhCYEsPeUkYXicKlxzgWXk1ONVJcXJ06FLI/640?wx_fmt=png&from=appmsg)

****未来：知识图谱****

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp0Z9J03lnJiazcCc9hib7jVg0YhE5u7ST4LtwmEUkReQDYCJXwhdbTUQhHYEkibwiczEEJq5exp43F9SJgwqBlyc3joZzgsIHoBugQ/640?wx_fmt=png&from=appmsg)

**价值** ：

- AI 可以理解模块间的依赖关系
- 自动推荐相关的 Skills
- 提供跨模块的最佳实践

#### ▐ 从被动查询到主动建议

******当前：开发者主动询问 AI******

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp2hu2pb0qCmaTnYDydtTicmYT38DTJ9I29eiaokWiafpLBBibamW1HAyUNXC2TwJ4sCODSsNX1QpPjwxm03zjRFddWxLsX4kc29Kz8/640?wx_fmt=png&from=appmsg)

**未来：AI 主动发现问题**

![](https://mmbiz.qpic.cn/mmbiz_jpg/DthwRd8vvp1gnobnxZt7Mf1YrLjtX8hoL39UvKxSJbcyLds1SMUyneFGzqicBR4mOwqRW1Y3J8Lib55nAcYfibHEL4jFp9zYCJ3fRmRWXZpbAk/640?wx_fmt=jpeg)

**技术方案** ：

- IDE 插件实时分析代码
- 匹配 Skills 中的常见陷阱
- 编译前预警

#### ▐ 从静态文档到动态生成

****当前：人工编写 Skills****

**工程师踩坑 → 查源码 → 编写文档 → 更新 Skills**

****未来：AI 自动生成 Skills****

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp0JVoYk46tH4EvodxqzJJNlyKnKrSiaaaHapY037P2brXlaW85nreWPuINm2QFjwh9bvVOmx8kkZxppZJvHEwSlK1cJe1bHiaHcU/640?wx_fmt=png&from=appmsg)

**价值** ：

- Skills 永远是最新的
- 0 人工维护成本
- 覆盖所有场景

#### ▐ 从个人工具到组织能力

******当前：个人/团队使用******

******开发者 → AI + Skills → 提升个人效率******

******未来：组织级知识平台******

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0MTXrEY4dwFkc5P0vQFryZQb6AbTuS7Vv3K0XNukodevkqRWYVnJ7IevtauCN311TiaRAPtDN2KFibZAWNXNZhqKKbZxIC856BY/640?wx_fmt=png&from=appmsg)

**终极愿景** ：

- 新人入职第一天就能高效工作（AI 教学）
- 老人离职后知识不流失（Skills 沉淀）
- 组织智慧持续积累（每次踩坑都是资产）

## 结语：重新定义软件工程的知识传递

#### ▐ 传统模式的困境

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp2giaoxaoqLQBicUNv3SkFcQaOKtsEPVFktHHl6P7McUBkFpdJqRzF0ic5w7VNzcQQgeBzJuIpBgI3icmBydOna0ibV8NfpjAs71XdA/640?wx_fmt=png&from=appmsg)

#### ▐ AI + Skills 的突破

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2IeiaxTNZveCiboUPiczicM0micHSWRkK2pMc0XPBvXcMiaRbE8o7Dzc0iaXHUKCqSMP6KrBxrI3Z1vk1LnwkHww16WywwicxtWs43PTw/640?wx_fmt=png&from=appmsg)

#### ▐ 核心价值主张

1. **效率提升：AI 的速度 + 领域专家的准确度**
2. **知识沉淀：从"人脑记忆"到"组织资产"**
3. **持续演进：每次踩坑都让 Skills 更完善**
4. **团队赋能：新人 0 学习成本，老人不再重复劳动**

## 团队介绍

本文作者开益，来自淘天集团-用户终端技术团队。我们服务于淘宝基础用户产品，是淘宝最重要的业务线之一。首页、信息流推荐、消息聊天、搜索、我淘、用增、互动、内容等亿级用户规模产品，为我们带来大量业务/技术挑战及机会。

团队在保证业务的同时，以先进的跨端框架和研发模式不断完善自己，打造最极致的体验和工程技术，保障多端设备的适配和稳定运行，并探索端智能等创新机会，通过技术高效驱动业务的良性发展。持续探索以AI为底座构建从需求到上线的端到端自动化与产品化能力，使亿级规模的交付更快、更稳、更可控。

## ¤ 拓展阅读 ¤3DXR技术 | 终端技术 | 音视频技术服务端技术 | 技术质量 | 数据算法

继续滑动看下一个

大淘宝技术

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过