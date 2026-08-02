# 【手猫研发提效随笔】七句话搞定一年AB实验下线：CodingAgent的魔法时刻

**作者**: 天猫技术团队

**来源**: https://mp.weixin.qq.com/s/WzG_QUCdDtKPWDSRDJtbCw

---

## 摘要

本文分享了利用AI助手CodingAgent高效治理积压AB实验的实战经验。作者通过七句指令将繁琐的手动下线转化为自动化流程，依次创建了查询实验状态和扫描代码生成报告的专用Skill，利用API批量获取数据，并以最小风险策略批量固化代码，最终自动生成提测报告。文章强调工具化关键步骤、明确指令与人工Review的重要性，指出AI作为超级助手能有效提升研发效能，将开发者从重复劳动中解放出来。

---

## 正文

天猫技术团队 天猫技术团队

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/33P2FdAnju9cLcib00YV66gYq2V6Fhm7YTHlzZdFwfnCtxyBCvgiaicG65n8du0mUYunHZIaBKohjsBxA4sgrPSjQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

本文分享了作者利用AI助手高效治理积压AB实验的实战经验，通过七步指令将原本繁琐的手动下线工作转化为自动化流程。核心方法是将复杂任务拆解为创建查询、扫描报告及版本升级等专用Skill工具，利用API批量获取实验状态并生成Markdown报告，随后以最小风险策略（将Key置空）批量固化代码，最终自动生成提测报告。文章强调了“工具化关键步骤”、“明确指令”及“人工Review”的重要性，并总结了API适配、JSON解析及版本冲突等踩坑教训，指出AI并非替代程序员，而是作为超级助手增强研发效能，帮助开发者从重复劳动中解放精力。

## 前言：实验太多也是一种烦恼

话说咱们团队过去一年搞了那么多AB实验，现在回头一看，好家伙，实验列表比我的购物清单还长！这些实验有的已经完成了使命，有的早就该下线了，但就是没人去收拾这个烂摊子。

直到又一次，因为预发环境AB实验过期（线上实验会自动续期，但是预发不会呀~~~）而苦逼的查了半天，这实验治理说什么都要搞了！！！

我看着那长长的实验列表，心里一万只草泥马奔腾而过。手动一个一个下线？那得搞到猴年马月！正当我准备写辞职信的时候，我想起了CodingAgent——那个号称"什么都能干"的AI助手。

## 七句话的魔法时刻

于是，我对CodingAgent说了这七句话：

**第一句：** "CodingAgent，帮我创建一个skill，可以根据AB实验的key查询当前AB实验状态。"

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp0j4icjSBqW1rTYljcMSwTN2Sb2CGd5QlOz6gCCXooPnciaia9NsuXqdzMbCuVTYVBDmr12fyj2wqKSQT8G1iac4IT4SrbpqeB6KFA/640?wx_fmt=png&from=appmsg)

CodingAgent二话不说，直接创建了一个

`ab-experiment-query` skill，通过IDEAs平台的API查询实验状态。我给它提供了我的AK、工号和appCode，它就能像查户口一样把实验的状态查得清清楚楚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp1rCyqefMdTjRVf5X6HBefSM3QlKBQ4tjq4Gibgef2mYicEKTrkZFBUB3b1nXP3CnIzPM7icWqaOevVGuiaEphR5F1uKtQiaG9iankHY/640?wx_fmt=png&from=appmsg)

**第二句：** "扫描代码统计已推全的手猫实验，生成报告。报告内容包括：ab实验key，实验描述，代码路径，实验链接。"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0cxPc2pVBkDLJB8taovPFBt2uomVw0eB0gosfzo9MJ3vMyL4Ewg35a8vpaml8iaoVDkicKlqAQicOrnVZoefEwBxohFXadU5hDdo/640?wx_fmt=png&from=appmsg)

CodingAgent立马开始干活，先是用grep从代码里扒出了20个AB实验的key，然后批量调用API查询状态。20个实验，18个已推全，2个还在运行中。它还贴心地生成了一个markdown报告，表格排得整整齐齐，比我做的PPT还好看。

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2CjoKWmqj5cvaqV04azoEbp8WwZsIFRe9eTqdJQFW7c7dJX8CBPsQMWPPrhUtZ4ud2BgWOXaApjc6cYF4w9VoPdKRMfxvpYnM/640?wx_fmt=png&from=appmsg)

**第三句：** "将这个扫描能力也创建成skill。"

于是 `scan-ab-experiments` skill诞生了。以后只要输入 `/scan-ab-experiments` ，它就能自动扫描代码、查询状态、生成报告，全程自动化，我只需要喝茶看结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp1Q4WUALngv3Zo7L7zib6HbC7aM8AFcWC7NicvoROOBwy8vkch5eEhAv9AD5NxW6CgrZHfXZBSXIzKqTGPfibKBC49hHic5JSzzpjU/640?wx_fmt=png&from=appmsg)

**第四句：** "帮我将当前二方库版本升级并设置为SNAPSHOT版本。"

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1Emf8A6LyDBlUiaPoRZ5AOeamvaenA2ia1jIGT3BiadxSBGgZXjLzT4BhxnZZGmaeTVgh7xMMINEMfghGtcWZ6xDQh9KPibMOw4Gw/640?wx_fmt=png&from=appmsg)

CodingAgent看了看pom.xml，发现当前版本是2.10.51-RELEASE-2026012902，二话不说就升级成了2.10.52-SNAPSHOT。我还让它加了分支标识，避免和其他开发者的版本冲突。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp3DsAZ8pv1wKostoXC9czSLLJIcHOaqdgRDB7B2JsTahJQpqpYOU6adDYSmLianVIGxaqbv8cBETGPuYUicCH8WCyHVhqh4tXQrU/640?wx_fmt=png&from=appmsg)

**第五句：** "将上述操作创建一个skill给我，方便下次快速执行。"

`upgrade-snapshot` skill闪亮登场！以后每次开发新功能，只要输入 `/upgrade-snapshot` ，它就能自动升级版本号、提取分支标识、生成新版本号，全程不用我操心。

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp0QibOpmASOIDiaaPomNqhicjbJJIGic5N5osH0KdK1DaFGia00H5icm0P7UZSx30icLBiaaGcPXmrVicuYCTasIRbC56Zxa1pOuK5a3Haw/640?wx_fmt=png&from=appmsg)

**第六句：** "把报告文件中已推全的实验逻辑，固化到代码中。并将固化逻辑生成md报告给我。"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp3ezPIR4xJ7dOibtxbmjqpCib0iaia3zKT6eef23V89wZPVcmBGYUfAgByccZURN6l9n9JqCxAs8SgqbNCG1jY3icVYFxsYf7QzlLicY/640?wx_fmt=png&from=appmsg)

CodingAgent进入计划模式，分析了18个已推全实验的代码结构，然后问我："大哥队长，这些实验怎么固化？设置为空值还是删除判断逻辑？"我选择了设置为空值，这样代码改动最小，风险最低。CodingAgent就开始批量修改代码，每个实验key都改成空字符串，还加了注释说明原值。

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2917YMuUmUaz2PXbTJj9VX6oTW8L2gycDWjjYZ3cK7fWfPo3xtvaZzBNRQ6GFmvGA5uqjDuiaNvsmFc0f5V6OcwN9EFDekgNtw/640?wx_fmt=png&from=appmsg)

**第七句：** "生成最终的提测报告，准备上线。"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp3WZRjcmfsrdElLhDINbiadoamsZXqqctAtZEb6ADicfibrboVjj85FH2XmQmmqHL2ozrtkhfbShMguv29E1gC5v4MbpSEu7KOyIk/640?wx_fmt=png&from=appmsg)

CodingAgent汇总了所有操作，生成了一份完整的提测报告，包括修改的文件、固化的实验列表、风险评估、测试建议。我看了看报告，嗯，挺专业的，可以直接发给测试同学了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp05zfEpROP0xPiclrtRDnbZnFIoTAicNgWKx1wWjFEK6Q3Jgq3ZriapzLibKYiabFTZQ2c2gwWV2FKxJpjicb53YmlS5f5j7azuW28Jw/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0fp4G1UqrIAZHEwM2B3PWgpFsiaicxUbAqdCpkHLFGrslp5Wciawk6icgNoBhWicNmfb2iaG3uJDwRPXiaLqAgDNwW66BVBub2EccOBg/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp1HTWRhHlqpKc6AM8f1mFf68V2h7tf0ExK5tXpQ28mdUO0T6QPNVHecsLHkj3Fwfs6jzwmd5jF0z3G1BESaFU9L3dkH9KfTXMs/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp3aU3cb77xMQNOgG0EKkx97OERcAPFiaicia8cPy2DByFaceogrlBYM2SrdFD89iaPuRuWpv9d6qUa5Vtw4RbKBNo1jwfJndicZUr40/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp0RJFgR91cyick95bo9xwU6wGseak9fdibmVsT4AibUxDQibyUIhSrm20kAk87oicL3bXWCaqj2pjYAmicchGyiaZnWdWhl7dY3oL2cIo/640?wx_fmt=png&from=appmsg)

就这样，七句话，一年积压的AB实验下线工作，搞定！

## 核心思路：把复杂问题拆解成简单步骤

## ▐ 先把工具准备好，不要急着动手

很多人一看到任务就急着开始写代码，结果写到一半发现方向错了，还得推倒重来。我的做法是先花时间把工具准备好：

- **ab-experiment-query：查询单个实验状态的工具**
- **scan-ab-experiments：批量扫描和生成报告的工具**
- **upgrade-snapshot：版本升级的工具**

有了这些工具，后面的工作就像搭积木一样简单。

## ▐ 工具化关键步骤，让机器干活

人工操作最大的问题就是容易出错，而且效率低。我把关键步骤都工具化了：

- **实验检索：用grep从代码中提取AB实验key**
- **状态查询：通过IDEAs平台API批量查询实验状态**
- **报告生成：自动生成markdown格式的报告，表格清晰易读**
- **代码固化：批量修改代码，添加注释说明**

这样，我只需要告诉CodingAgent"做什么"，而不是"怎么做"。

## ▐ 创建skill，让工具协同工作

单个工具虽然好用，但如果能组合起来就更强大了。我创建了三个skill，每个skill都是一个完整的工作流：

```markdown
# ab-experiment-query skillname: ab-experiment-querydescription: 根据 AB 实验 key 查询实验状态workflow:- 获取用户输入的实验key- 调用IDEAs API查询状态- 解析并展示结果# scan-ab-experiments skillname: scan-ab-experimentsdescription: 扫描代码中的 AB 实验，查询状态并生成报告workflow:- 扫描代码提取实验key- 批量查询实验状态- 筛选已推全实验- 生成markdown报告# upgrade-snapshot skillname: upgrade-snapshotdescription: 升级二方库版本为 SNAPSHOTworkflow:- 读取pom.xml获取当前版本- 版本号+1- 提取分支标识- 生成新版本号- 更新pom.xml
```

这样，CodingAgent就知道什么时候该用什么工具，整个流程就像流水线一样顺畅。

## ▐ 生成报告，把控过程

很多人觉得写报告是浪费时间，但我觉得报告是控制过程的最好方式。每完成一个步骤，就生成一份报告：

- **实验状态报告：告诉我哪些实验已推全，哪些还在运行**
- **代码固化报告：告诉我修改了哪些文件，改了哪些实验**
- **提测报告：汇总所有操作，方便测试**

有了这些报告，我就能随时掌握进度，及时发现问题。

## ▐ 明确的编码指令，批量完成改造

CodingAgent最强大的地方就是能理解自然语言指令。我给它的指令非常明确：

"把报告文件中已推全的实验逻辑，固化到代码中。固化方式：将AB实验key设置为空值，添加注释说明原值。"

CodingAgent就会按照这个指令，自动完成所有操作：

```java
// 修改前public static final String AB_202407291048_1537 ="AB_202407291048_1537";
// 修改后// [AB已推全-2026.02.02] 原值: AB_202407291048_1537public static final String AB_202407291048_1537 ="";
```

## ▐ 人工review，确保质量

虽然CodingAgent很厉害，但我觉得还是需要人工介入。我会仔细review报告，检查：

- 实验是否真的可以下线
- 代码修改是否正确
- 是否有遗漏的实验
- 注释是否完整

发现问题就及时修正，确保万无一失。

## ▐ 生成提测报告，准备上线

最后一步是生成提测报告，这份报告包括：

- 修改的文件列表
- 固化的实验清单
- 每个实验的改造摘要
- 风险评估
- 测试建议

有了这份报告，测试同学就知道该怎么测试了。

## 实战经验：踩过的坑和学到的教训

## ▐ 坑1：API调用失败

刚开始查询实验状态的时候，我用的是钉钉个人助理接口，结果返回的是success，但实际结果要通过钉钉消息异步返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DthwRd8vvp05fkGkZKydmdPylajllGoeANQ03LtTiaJKY7tjVxibWtNJBkjvaYUEZKJQia5yicfz4e2jfTRyptVXuN2DjVTTBXEY7qLFjpsFicXs/640?wx_fmt=png&from=appmsg)

后来我改用了IDEAs平台的API，把API文档生成md文档交给CodingAgent学习适配，问题就解决了。

![](https://mmbiz.qpic.cn/mmbiz_png/DthwRd8vvp2ia78XWC9RFuZ1gu1nNDlc08EwLrrGWkmcRbXv43F1SkMaDLrTGgWj8xOmfjTmJ7iauicHI6kbHTbSxTFLm7cpicF6cvsXqfK2QvU/640?wx_fmt=png&from=appmsg)

所以，遇到问题不要着急，不要轻易放弃。不要预设困难，找到文档让AI学习，他的能力可能比你想象中要强！

## ▐ 坑2：JSON解析错误

批量查询实验状态的时候，有些API返回的JSON包含控制字符，导致解析失败。

教训：不要相信API返回的数据永远是干净的，但AI可以处理这种问题，只需要你给出明确的引导。

## ▐ 坑3：版本号冲突

升级版本号的时候，如果多个开发者同时开发，可能会出现版本号冲突。我让CodingAgent从分支名提取功能标识，加到版本号里，这样就避免了冲突。

教训：版本号管理要考虑团队协作场景。

## ▐ 坑4：代码固化策略选择

一开始我想直接删除AB判断逻辑，但这样改动太大，风险太高。后来选择了将key设置为空值，这样改动最小，而且保留了原有变量定义，后续可以逐步清理。

教训：重构要循序渐进，不要一步到位。

## 总结：AI不是替代，而是增强

有人说AI会取代程序员，我觉得不会。AI更像是一个超级助繁琐的工作，让我们把精力花在更有价值的事情上。手，它能帮我们完成那些重复、就像这次AB实验下线，如果手动做，可能需要一周时间。但有了CodingAgent的帮助，我只需要花一天时间思考和review，剩下的工作都交给CodingAgent完成。当然，前提是你得会"指挥"CodingAgent。你得知道什么时候该让它做什么，怎么给它明确的指令，怎么review它的结果。这其实也是一种能力。所以，不要害怕AI，要学会利用AI。毕竟，我们的目标是解决问题，而不是展示自己有多能干。

> 写在最后
> 
> 七句话只是调侃，其实黎明前有很多人在黑夜里默默流汗。

## 团队介绍

本文作者依凡，来自淘天集团—天猫APP技术团队。作为淘天集团的核心技术引擎，我们负责天猫APP的全栈开发与体验升级，支撑导购、搜推、商详、购物车、下单等核心交易链路。我们以极致的端侧性能与创新的Agent架构，打造「AI导购」「AI助手」等面向C端的智能应用，并探索端外场景合作，为千万级用户构建沉浸式、个性化的购物体验，持续引领电商APP的技术演进。

## ¤ 拓展阅读 ¤3DXR技术 | 终端技术 | 音视频技术服务端技术 | 技术质量 | 数据算法

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过