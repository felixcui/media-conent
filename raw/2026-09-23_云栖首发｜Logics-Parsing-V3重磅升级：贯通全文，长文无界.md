# 云栖首发｜Logics-Parsing-V3 重磅升级：贯通全文，长文无界

**作者**: 阿里数据

**来源**: https://mp.weixin.qq.com/s/8lHpeTAQgD4qayy-RWcvFA

---

## 摘要

阿里巴巴在云栖大会开源Logics-Parsing-V3模型，针对长文档解析中“局部正确、全局失联”的痛点，采用循环滑动窗口与结构状态传递机制，使模型翻页时延续前文结构状态，有效解决跨页表格截断、段落割裂、标题层级错位等问题，最终将各页面统一重建为完整文档树。

---

## 正文

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVOUkHsd1C95tE7lU0NtQ0sgkPMgMzic25yEhDHNvnPyCg2Un6s7rHQ1FdAoa4mV9lkqe2NftKfUZNO9MnRJEbOYibWj1VIWv7Jp0/640?wx_fmt=png&from=appmsg#imgIndex=0)

01

为什么“全局解析”如此重要

举个例子：装修一套房子，各支队伍依次进场，每位师傅都能把手头的活做好，但如果交接时没说清“哪里要留线、哪里不能封、哪里需要避让”，麻烦就会在最后冒出来：预埋的线路没用上，柜子装上挡住了插座、开关与灯对不上号。每支队伍都完成了自己的任务，合在一起却不是原本想要的家。问题就在“局部正确、全局失联”。长文档解析也面临同样的困境。

模型可以识别每一页的文字、表格和图片，但如果翻页就“重新开工”，段落可能断开、表格拆成两截、标题层级发生错位——每一页都识别正确，整份文档却没有真正读通。

在今年的云栖大会上，阿里巴巴推出了 Logics-Parsing-V3 开源模型。把这场“交接”放进了解析过程：让模型带着前文的结构状态继续翻页，在跨页过程中保持内容连续、关系完整，最终还原一份结构清晰的完整文档。

在延续Logics-Parsing-V2复杂版面解析与精准元素识别能力的基础上，Logics-Parsing-V3通过循环滑动窗口与结构状态传递，让页面之间拥有了“统一施工图”：模型在翻页时延续前文的结构状态，再将解析结果重建为完整文档树。文档不再是一组彼此割裂的页面，而成为一个能够被连续理解和结构化还原的整体，为下游的检索、问答和深度分析提供更精准的识别结果和层级结构。

Github: https://github.com/alibaba/Logics-Parsing

HuggingFace: https://huggingface.co/Logics-MLLM/Logics-Parsing-V3

Demo: https://www.modelscope.cn/studios/Alibaba-DT/Logics-Parsing

02

模型优势

跨页不断，长文无界：同时支持单页与多页解析，通过长文档滑窗方案灵活处理超长内容，有效解决跨页表格截断、文本割裂等问题，让全文语义衔接更连贯。

不止识别，更懂结构：能够抽取全文层级结构、定位图表所属层级并建立图文关联，让模型真正“读得懂、理得清”每一份文档。

复杂内容，精准还原：面对密集文字、复杂表格、科学公式、化学符号等复杂排版，依然能够精准识别，并支持乐谱、思维导图、代码及伪代码等内容还原。

SOTA 表现，性能领先：模型仅0.8B，在MPDocBench多页榜单取得SOTA表现，层级结构识别（Heading TEDS）大幅领先。

03

技术拆解：从识别单页，到理解全文

Logics-Parsing-V3 如何做到翻页之后，依然记得前文？

核心在于一套循环滑动窗口推理框架（Structure-Aware Recurrent Parsing）。它将长文档按顺序划分为一组连续的页面窗口。模型每读完一个窗口，都会提炼并更新一份结构状态，其中记录着尚未结束的标题路径、近期已闭合的标题以及跨页延续的内容。就像装修中每支队伍进场前，都要接过一份持续更新的交接清单：前一道工序做到了哪里，哪些部分已经完成，哪些接口还要保留，接下来该从哪里继续。

![](https://mmbiz.qpic.cn/mmbiz_jpg/9UpB4iayXMVPuyfWqiaRwS97PNOchOOg3Cibnr0RXWzPAJpxXnYapKgqYAZGnZN1kibOiatYjTJRgtzv9tf7upxnwD1FiasEGS94gEuPIHnZ9hd0Q/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

Logics-Parsing-V3 循环滑动窗口推理框架

具体来看，每个页面窗口不仅接收当前几页的内容，还会接收上一窗口传来的结构状态。经过模型解析后，它会输出带有页面定位、标题层级、内容延续标记和图文引用关系的结构化结果；这些结果一边汇入持续累积的文档记忆，一边更新结构状态，继续传递给下一个窗口。

当全部窗口处理完成，系统再依据页面来源、层级关系和阅读顺序，对各窗口的解析结果进行统一重建，最终形成一棵完整的文档树。至此，模型面对的不再只是一页页彼此孤立的内容，而是一份结构连续、关系清晰的完整文档。这套机制要解决的，本质上是长文档翻页之后的三类“失联”：让段落与跨页表格更不易被截断，让标题层级与阅读顺序得到延续，也让图片、表格、图注及正文引用保持关联。

即使面对论文、报告、书籍等超长文档，模型也能沿着全文结构持续阅读，让跨页内容更连贯、文档层级更清晰、图文关系更准确。

04

模型表现优异

在 MPDocBench-Parse 综合评测中，Logics-Parsing-V3 以 85.26排名第一，领先端到端方法第二名 PaddleOCR-VL-1.5达4.46分。

面对 PaddleOCR-VL、MinerU、OvisOCR 等主流文档解析模型，Logics-Parsing-V3 拉开了清晰的综合得分优势，此次升级在整体文档解析能力上提升明显。

![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVPngic3sB4EKYcQZsBppFRCUmCt6gh3gicDQnBOG1xVThqVMvicls9R1cLrmd6cCysyIAwhghO7SCwYH3PuibqN1ibjcNKv9LzGfDZY/640?wx_fmt=png&from=appmsg#imgIndex=6)

在跨页文本衔接和全文层级重建方面Logics-Parsing-V3 的优势突出，公式识别、表格结构与跨页表格等指标也保持在第一梯队。![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVO939Llib19kWPyVBLbXzSlXvwrL3Imrm8snNaBKpID2wFcWicFBCiapWPTeVUR9uiaB5icMZHuzYJQdHZZlC6ReicTuUPHicePAt8zfM/640?wx_fmt=png&from=appmsg#imgIndex=7)

![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVMWhM5icv9a0F9DeoTF9WXYY4wpHmiahmiaBjicMbxBXP0WCicrywn5YvpfncEvZFLbvsqTaQiagzcmlicFkFa5EzibVZ4f9u4RzDJicITw/640?wx_fmt=png&from=appmsg#imgIndex=8)

Logics-Parsing-V3 长文解析能力优势还体现在在 MPDocBench-Parse 明细评测中, 其中，截断文本编辑距离降至 0.07，在参评模型中表现最佳；Heading TEDS 达到 62.33，领先第二名8.97分。

同时，公式识别、表格结构与跨页表格等指标保持前列。另外面对多页复杂文档，Logics-Parsing 3.0 不仅支持跨页文本与跨页表格合并，还能建立图文关联并恢复标题层级，是表中两个覆盖全部四项关键能力的模型之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/9UpB4iayXMVOISvUpcwwDRfVtBD5wkmRicUMu07lPmiaDfjdkHVrb6pywSM4AECphes1OxzNm5GNg22conn8B5O01tCCBiaTELwmU3aQRW4JNRk/640?wx_fmt=webp&from=appmsg#imgIndex=9)

05

案例效果展示

#### 跨页文档

1）多层级结构提取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVPP81UViac2tFoH9gPUXfGoPjqot06LYSic8WDuEIqHmib1mxGkD2r0mnyDajpV8O8jCufvgicwYbxPLrzxGd6VUycJ6Vyknf4fzK0/640?wx_fmt=png&from=appmsg#imgIndex=11)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVPKKhhnOrA2zibZibaDaVBtia7ZVxHwQbZ3XXbT46s3Idx1zSSzJQqwtPrtab1QYxo0NahMicrdN5iaQgHr0v2WXZcAOlBSpxmtskjc/640?wx_fmt=png&from=appmsg#imgIndex=12)

2）截断表格合并

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVNmkiaEca9HXjianVjSA86y0e4D8ibPp4m4RT0XCFIKmdV3VaicLyzrcBSM5ewBqUicCjQXicSfibhC0cqhjT356GicjxvuqP5zDphubVI/640?wx_fmt=png&from=appmsg#imgIndex=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVOhK6rYWdsRYgfibCicDdoHTgn0LDdgIX9so5mhzgINrKSZWLFA7bibaT8qNUjibbZ6qp6NRCVBxDv4K6kIO75STa8Spyh5bJwLN1Q/640?wx_fmt=png&from=appmsg#imgIndex=14)

3）跨页文本合并

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVOmRDL8r0PxibqBE0yCibjicw6E3iciavFSsyiaCyLZyLtsRIK8Krz81DoiajrneY1VqvwPlr19cl35OJ7UeQEibytxZ4vnECaMWoC9doE/640?wx_fmt=png&from=appmsg#imgIndex=15)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVMxmQFl4P2bmVSDUialrwmvxSSKR1fJT1bojZ4YOzcnoSpnOtwQqhxal54A0LhqFkQzGQ4sjMUUXYmVvQhJa5TptJcx7NZtNLH8/640?wx_fmt=png&from=appmsg#imgIndex=16)

#### 单页文档

1）学术海报

![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVN10jNPoN72L3WpT1nmsykdaPicGVJssSK0ibSP58nCQiaqfoRibzYOicSB4ulzyEL2bWHKibscqIb2T3frSTDPyIVMReDTUdiaPHDd2M/640?wx_fmt=png&from=appmsg#imgIndex=17)

注：箭头表示阅读顺序，绿色正确，红色错误

2）复杂表格

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVMibAerCLZGRSNGkYfDp3qSouXb5NNkZGB1A6saiaoOXyDCH25iag4GqsI2ibEONCMVOvlp8Q3hOz8D6JrvdPZhaDicqzuSooXDTcI4/640?wx_fmt=png&from=appmsg#imgIndex=18)

3）代码块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVOxPQ9PhkKAJslbPPcXXoyaR3YkBZxfnky5hLP1Z5RWxa42KLXE5DF4FPG6KDUHic5DHkwE5VtOVUmzWqQT7jZXBIiagclLf3NDI/640?wx_fmt=png&from=appmsg#imgIndex=19)

4）化学试卷

![](https://mmbiz.qpic.cn/mmbiz_png/9UpB4iayXMVMPvxsicwgibEWGn6GaA44EKXeL9wO2Loqic2PHz7GVUz0CkWkQepffWx5YmyUsLYhUPyZoTqY3JzEd9IlJ8vI6V41Pib3mNx1AwkA/640?wx_fmt=png&from=appmsg#imgIndex=20)

5）手写笔记

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UpB4iayXMVMXXrpb6wMibM3qXWTb9GCg7xmpuzWxyDCuy6TPiaXLdVibLF2QTsxEKIXiaeAicEBfgpNsiad6ia49AcWJug1AGqoc2HzjK23Yy2VDCg/640?wx_fmt=png&from=appmsg#imgIndex=21)

Github: https://github.com/alibaba/Logics-Parsing

点击“阅读原文”访问项目Github

![图片](https://mmbiz.qpic.cn/mmbiz_gif/OmCbZ5JK30GbpbpADRYqgC6MMvNfRPY8cGySPF2f9miavJibvCOiaUelcS2LX6uSMGEic1ztD9ECCvN2rcupEseySg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

欢迎留言一起参与讨论~

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过