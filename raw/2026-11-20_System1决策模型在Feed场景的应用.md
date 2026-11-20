# System 1 决策模型在Feed场景的应用

**作者**: 百度Geek说

**来源**: https://mp.weixin.qq.com/s/tf9vVDYYWmO9pyNzujcSzw

---

## 摘要

文章介绍了百度Feed团队将System 1决策模型应用于推荐打分，该模型不生成文本、只输出概率，凭借语言理解和世界知识在低活用户和新内容上优势显著，历史点击最少用户群uAUC比精排高2.95%，并探讨了Encoder、Decoder、双塔三条架构路线及缓存复用、知识蒸馏、FP8量化等降本方法以应对单用户约1800条候选打分的落地挑战。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | Signal

导读

introduction

推荐系统追求既快又准，这正对应《思考，快与慢》里的"快思考"System 1。本文介绍百度 Feed 团队怎样把"只输出概率、不写文本"的决策模型用于推荐打分。这类模型靠语言理解和世界知识判断兴趣，在低活用户和新内容上优势最明显：历史点击最少的一组用户，uAUC 比精排高 2.95%。落地的难点是同一个用户要给约 1800 条候选打分。文章对比了 Encoder、Decoder、双塔三条架构路线，并拆解了缓存复用、知识蒸馏、FP8 量化等降本方法。

*全文 5016 字，预计阅读时间 6 分钟*

System 1 是心理学家丹尼尔·卡尼曼在《思考，快与慢》中提出的双过程理论里的快速直觉思维模式，又称"快思考"。它恰好映射出我们对推荐系统的期待——既快又准。

TypeSafe AI 于 2026 年 9 月 15 日发布了首个 System One 模型 Jev，核心定位是高速结构化决策：放弃自由文本生成，只输出带类型的概率化结果。它真正的意义在于确立了一种新范式：模型不写文本，只输出概率。

****System 1 与 System 2：区别在输出方式****

传统大模型偏"慢思考"（System 2），自回归逐词写出一段文本，速度慢，还得二次解析；System 1 模型更接近人的直觉反应，一次前向就把最后的隐状态交给一个小决策头，直接读出带类型的概率，比如点击概率 0.37。

只给概率，带来三点好处：

- 省掉逐词解码。生成 N 个词要跑 N 次前向，决策模型只跑一次。
- 概率天然可用于校准。它能和线上其他分数一起排序、融合、过阈值，不必再从文字里抠答案。
- 自带世界知识。底座是预训练语言模型，这是传统 ID 类特征模型不具备的。

Laya、Kev 等复刻方案里的 pointer head（指针头）同理：通用语言模型要在几万个词里挑一个，指针头只在输入给定的几个选项（如"会点""不会点"）上打分再归一化，既快，也不会答非所问。

GEEK TALK

01

项目「System 1 决策模型」背景

自Jev发布之后，Feed 团队加大了对 System 1 决策模型在 Feed 场景应用的调研。先用官方版本的 laya-multilingual、Jev-API 在 MIND-small 公开数据集与内部场景数据集上做推荐排序打分，初始 AUC 约 0.539，基本等于随机水平；但经过简单微调后 AUC 迅速提升到 0.6 以上，足以证明决策模型能胜任 Feed 打分这一关键角色。随后在实验阶段尝试了多种用户特征组合，并结合若干内容判别力字段微调，快速筛选出一组高价值的上下文特征。首轮线下评估显示，该方案已超越线上粗排基线，在低活用户上更是优于精排 uAUC。

- 一条样本demo：

```json
{    "state": {        "user": {            "recent_queries": [                "某热门行业的岗位待遇怎么样",                "该行业适合新人的岗位有哪些",                "某岗位最新招聘信息"            ],            "recent_consumption": [                {                    "title": "某热播剧集的剧情讨论……",                    "category": "影视-影视资讯"                },                {                    "title": "某教育话题的热点解读……",                    "category": "教育-教育资讯"                }            ]        },        "candidate": {            "title": "某演员在新剧中的表演评价……",            "summary_full": "内容 Agent 产出的候选文章摘要（此处省略）"        }    },    "questions": {        "click": {            "type": "bool",            "instructions": "结合用户画像、近期阅读兴趣和上下文，该用户会点击这篇候选文章吗？",            "criteria": {                "true": "会点击",                "false": "不会点击"            }        }    }}
```

- Laya具备更强的世界知识和推理能力、可有效使用用户和内容理解的产出特征，在新内容/长尾内容/低活用户的预估、 用户和内容的兴趣匹配上存在优势
![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5TGiaNUgh8Hks00NzgIJ2Om6LpuvhuvApRVy572EmF4BF4STNkhgiafAwbrNkhQHOBnHUqicqJMsssOiarCQ9P7U8Pdaxzw4YHujo/640?wx_fmt=png&from=appmsg)
- ****Case：****
- 一位历史点击较少的低活用户，此前点击过某篇民生政策类内容；系统为其推荐了一篇相关的政策解读后用户点击，决策模型将该内容排进前 5%，而当前系统排序靠后。可见决策模型能基于用户基础属性与少量点击行为，更好地满足个性化需求。
- 一位对历史与国内时政感兴趣的低活用户，面对一条突发时政内容，决策模型将其排进前 5%，当前系统排序靠后。决策模型具备一定世界知识，在新发布/突发内容上更容易找到目标受众。

****越"冷"的用户，收益越大****

传统精排依赖大量 ID 类特征和历史统计，用户点击少、内容又新时，就没多少数据可用。决策模型靠语言理解和世界知识，凭少量行为也能推断兴趣，因此在低活用户、新内容和长尾内容上优势最明显。反过来，重度用户点击行为已经很充分，精排本就足够准，决策模型能带来的提升也趋近于零。

GEEK TALK

02

项目目标

为此，我们计划在 Feed 推荐链路层面对 Decision-Model 进行重构，并成立联合优化项目「System 1」，核心目标包括：用更大规模的用户样本探明离线评估的效能极限，同时对在线决策模型进行性能调优，以满足低成本推全的工程要求。

****1\. 将样本规模扩大至亿级，验证 System 1 决策模型在推荐场景下的 Scaling Law 表现****

圈定千万级乃至亿级用户，通过天级任务产出数十亿训练样本，协同多机分布式训练资源，验证"模型/数据/算力越大、效果越好"的缩放规律在推荐场景下是否同样成立，并探明离线评估的效能极限。

****2\. 通过将决策模型升级为双塔结构，降低在线推理成本，支持高效的线上 A/B 测试与效果验证****

提取决策模型的 Last Hidden State 作为向量输出，并将 Item 向量预先缓存至内部存储介质。结合 User 侧的实时预估能力，以低成本完成线上实验的快速验证。

****3\. 构建标准的 LLM Scoring 架构，通过推理成本优化实现合理成本范围内的全量上线****

利用 Decoder 架构完全共享 User 侧 Prefill Cache，将推理成本压至最低，以支持全量部署所需的目标算力规模。

GEEK TALK

03

项目方案

****核心难点：user 部分能不能只算一次****

Feed 的难点不在模型准不准，而在于同一个用户要对约 1800 条候选打分时，user 部分能不能只算一次。三条架构路线的根本差别，就在于 user 部分能不能缓存、又能缓存到什么程度。

这又取决于注意力能"看"到哪里：

- ****Encoder（双向注意力）**** ：每个 token 的表示都依赖左右两侧，后面新增一个 token，前面全部要重算，user 部分几乎无法提前缓存。
- ****Decoder（因果注意力）**** ：前面的 token 看不到后面，它们的 Key / Value 一旦算出就不再变，可以存下来复用，也就是 KV Cache / Prefill Cache。user 在前、候选在后时，user 的 prefill 只算一次，就能被约 1800 条候选共享。

**① 以Laya为代表的纯encoder架构**

- laya的单次预估延迟极低（tilelang & fp8 & 1k-token单条预估能跑进个位数毫秒内），但是laya-multiligual(mmbert-base模型)天生的双向encoder注意力结构导致在工程上无法提前预计算，而且Feed场景对对链路延迟要求极高
- user 编码无法预计算：上下文 state 是 user-nid 信息对，而 mmBERT 是双向编码器，每个 token 的表示都同时依赖左右两侧上下文；一旦后面新增候选 token，前面 user 部分的表示就会随之变化，导致提前计算并缓存 user-state 的收益非常有限。
	- 双向注意力推理算力消耗巨大：受双向注意力结构影响，单卡吞吐有限，在严格的延迟约束（p80速度在数十毫秒）下，处理单个用户一次约 1800 条候选的预估，需要占用相当可观的 GPU 资源。
![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5CvFNUXPG2XgFh0zjKxL6ltOPf1WPyKegw9FDtBbSp6iaNKMv6zZ7CDAibiayicaicGQCeOPlWQzjncmichn1Vhib8sBkU4wZ1XrvWkc/640?wx_fmt=png&from=appmsg)

如上图，线上要对同一个 user 预估约 1800 条候选时，当前架构只能硬算 user-state（约 1k token 上下文中 user 部分占比约 75%），而 mmBERT-base 的 22 层 Transformer 结构让单卡算力相当吃紧。下面是精排预估与 Laya 预估的算力对比。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7fDWDW7AYPicLhPkzkma1U2xU3AADnYicgQt7yR7Ku6jfBvNRiaFjuzcVrBFHCleVgomgEv04BOx4DfoOsY71rSibCgKG47uFpvpo/640?wx_fmt=png&from=appmsg)

双向编码器虽有潜力，但这套架构后续的策略迭代空间比较有限。

主要有两点原因：

1、token 数越多，延迟越高。目前对 laya 架构做 32k 上下文 token（约 100KB 的 UTF-8 文本）的测试，单条延迟已接近 ****1.5s**** 。而策略迭代的方向恰恰是往上加上下文，这块延迟又已经压不动，继续扩展的余地就很小了。

2、蒸馏方面，我们借鉴 tiny-BERT 的多阶段蒸馏：在 teacher 指导下，参数减半的 student 效果损失很小，但小流量仍需不少算力，推全成本会成倍放大。

结合近一周的优化，联合团队综合运用了多项降本手段—— ****FP8 量化**** （把权重/激活从 16 位压到 8 位，显存减半、张量核心更快）、 ****libtorch**** （PyTorch 的 C++ 运行时，去掉 Python 调度开销）、 ****tilelang**** （为特定形状定制高效 GPU 算子）与 ****知识蒸馏**** ——并在线上申请少量 GPU 做真实压测，验证了合适的 batch 与扇出配置可将 P90 耗时控制在 数十ms 以下。最终在满足线上小流量实验标准的前提下，Encoder 路线的小流量成本相比初始版本下降到约三成。

但这依然是一笔巨大的成本开销（评估推全成本约数万张GPU显卡）。

**② 以Qwen为代表的纯decoder架构**

既然双向 encoder 的 cache 复用有限，而且同一用户多次 nid 预估的 user-state 基本不变，那么不妨转向 decoder 架构尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5xVl559y777gZgZ8iaI7l6yemNUuWjZjbEEFkiakKHTZKFDc2b6AG2MM5SWzqHoAJEYH442BBN7ah1MVXnI4ZGfj1llADicBm0hA/640?wx_fmt=png&from=appmsg)

如上图，

- 请求入口一收到用户请求，就向 Decoder 预估集群发送 user 信号，提前触发 user-state 的 prefill 计算。这段计算在全链路上可与「入口开始处理」→「预筛结束」完全并行，可用时间窗口约 数百 ****ms**** ，且 user 只算一次（user-id hash 到同一张卡，保证缓存命中）。
- 等到预筛结束，再发起约 1800 条候选的预估，此时直接复用已算好的 user-state，只并行计算各候选的增量部分。
- 粗略统计，encoder 架构换成 decoder 后，在不考虑参数量与网络结构差异的前提下，单个用户批量预估的 1000\*1800 tokens 计算量可降低至 750\*1+250\*1800 tokens（ ****降低至原来的25%**** ）。

****更大的空间还是在 decoder。****

- user-nid state 现在各占 75%:25%， ****未来的迭代只会让 user 部分明显变大**** ；而在 Feed-decoder 架构下，前面架构图中多出来的 数百ms 正好能把 user-state 提前算好。
- 效果方面仍有优化空间，decoder 模型选择众多，实际上找到一个（甚至多个）decoder ****超越当前 laya 的效果并不难**** 。

所以，我们整个 10 月份的训练工作基本集中在 decoder 架构上；若重点看 uAUC，已经很接近精排了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5dUUIia69n5FCiaPdTX04OWBFK3O6GFfP0VGSafnw8KuQKxibOibNQIqrvcGeH6OJDORNMLq92doUEicD5XNWOufXFSBN0iaeG9szvw/640?wx_fmt=png&from=appmsg)

目前这套 Decoder 方案已能把小流量的成本控制得相当低，按比例推算推全成本在1万张GPU显卡内。

**③ 以startlux为代表的双塔架构**

****双塔与交叉编码器的取舍****

交叉编码器把 user 与候选拼成一个序列整体编码，两边的每个词都能相互关注，交互充分，但每个 user×item 组合都要整体算一遍。双塔把它拆成独立的 user 塔和 item 塔：item 向量离线算好、小时级更新，线上每个请求只编码一次用户，最后做一步向量匹配。代价是 user 与 item 的细粒度交互会丢失，精度通常不及交叉编码器。它更适合用来低成本验证，再决定是否推全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7nPSC2iaq80ufzIob7xicsxa0RiaKQtDJTgBT7sdLxHddp93vjHbF0fv1leE1sjWBXQMictw1po2XZwubvw1ic0EuO6DDp98E0oDAA/640?wx_fmt=png&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4vjiadtDsRaqnZevUlSEl0Y5j0julOVSQtLAPaj1x1mCQsYRO92IZW4xBwZYlHkdP3NntljYHz2ibevRuXVQ2pJ6wtPaCcxcElY/640?wx_fmt=png&from=appmsg)

借鉴传统的双塔做法，把 startlux-gemma、startlux-decision 0.8B/2B/4B 的交叉编码器（cross-encoder：将 user 与候选拼成一个 prompt，读取 A/B 选项概率）拆成 user 塔和 item 塔，item 向量可以离线算好、小时级更新，线上每个请求只需编码一次用户。这样评估下来，小流量的单次上线成本可降到极低水平。

此外，在线上应用环节，user 预估不一定要实时完成，可视情况调整为次刷更新、小时级更新或天级更新；更新频率越低，成本越低。

### 三条路线一览

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4CZPRRVtVZNM0rw1Fm1lts983IibWtEAkjKEDtRbAzO5eyOu8ich1EAL76Uo8XoCdRYDf9qJlj7moXT87nD0s9GicDjgWGcc0Wkw/640?wx_fmt=png&from=appmsg)

GEEK TALK

04

降本技术全景

推理和训练的成本，大体取决于两件事：算多少，以及每次算多贵。项目的降本手段也围绕这两点展开，可分为四类：复用缓存以减少重复计算、蒸馏裁剪以缩小模型、低精度与算子优化以压低单次开销、LoRA 与前缀打包以节省训练资源。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5qmDIGEzP8QialecjkDqL74TWOoiafpicYbb7zPiaohHYLJIEKrdTEiblicKmmwu2PNpljicjaLJu5jELPd9xqgTGqsIftsKzwsSOd1o/640?wx_fmt=png&from=appmsg)

**① 知识蒸馏：让小模型学会大模型的"判断"**

蒸馏的思路是用大模型（teacher）的输出分数来指导小模型（student），让层数更少的 student 也能逼近 teacher 的判断。我们借鉴 tiny-BERT 的多阶段蒸馏，把 mmBERT 的 22 层 encoder 压缩到 11 层。四组对比如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7SxM0E8LVqBvJwqlthFibYqux6luIRsD06KbibNEvnjcVciavLPx7fAdYcbAq81c4eTUVuRjxKvafkAeiawPKLVkibics9tvjXK15zU/640?wx_fmt=png&from=appmsg)

具体来看：

- ****Accuracy 区分度不够**** ：四组都在 0.91 上下。点击样本占比低时，一律判"不点"也容易判对，所以真正拉开差距的是衡量排序能力的 AUC 和 uAUC。
- ****只裁剪**** ：AUC 0.51、uAUC 0.514，几乎等于随机。层数砍掉又没重新训练，判断力也就丢了。
- ****通用蒸馏**** ：让 student 模仿 teacher 的通用表示，能找回一部分（uAUC 0.569），但对"点不点击"这件具体任务学得不够。
- ****任务蒸馏**** ：直接用 teacher 在本任务上的打分来训练，uAUC 0.652 反超原模型的 0.649，单条耗时也从 20+ms 降到 10+ms。

**② 低精度与工程优化：让每次计算更便宜**

- ****FP8 量化**** ：把权重和激活从 16 位浮点压到 8 位浮点，显存占用约减半，GPU 的张量核心处理 8 位数据也更快。
- ****libtorch**** ：PyTorch 的 C++ 运行时，去掉 Python 层的调度开销，适合延迟敏感的在线服务。
- ****tilelang**** ：用来写 GPU 算子的编程语言，能为特定形状定制高效算子。Laya 靠它 + fp8，把 1k token 的单条预估压进个位数毫秒。
- ****batch 与扇出调优**** ：在线申请少量 GPU 做真实压测，验证 `batch=20` 、单次扇出约 90 次时 P90 耗时可控制在 数十ms 以下；在小流量实验标准下，Encoder 路线成本相比初始版本下降到约三成。

**③ LoRA 与冻结层：让训练装得下、跑得起**

全量微调要更新所有参数，显存和耗时都很大。 ****LoRA**** 的做法是冻结原权重 W，只训练一对小矩阵 A、B，让更新量 ΔW = B·A，其中 `r` 是"秩"（这里取 16），r 越小，要训练的参数越少。再叠加 ****冻结底部若干层**** ，只训练上层，进一步省显存。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5iaSo47pYd1jGdwXnWkpUYLTiaial8xiaWfQVhicbshiaZhKBPOETBm2ML9o87GzV6YY5AI8IjLYO48oQrzftaJbjre8dS4qTHCGWPw/640?wx_fmt=png&from=appmsg)

可以看出： ****冻结一半层更省资源，代价是 uAUC 下降约 0.0064**** 。

**④ 共享前缀打包：训练时也复用 user 部分**

同一个用户会对应很多候选，样本里 user 前缀完全相同。 ****共享前缀打包**** 可以理解为：把共享同一 user 前缀的多条样本放进同一个序列里，前缀只算一次，每条候选只补自己那一段。这和线上"user prefill 只算一次"是同一个思想——训练端是打包，推理端是缓存。

GEEK TALK

05

项目成果

****Encoder 模型（laya）优化****

- 联合团队采用 libtorch、FP8、蒸馏等多种手段， ****小流量**** 成本相比初始版本下降到约三成。

****Decoder 模型（qwen 系）优化****

- 联合团队通过复用 user-cache 等多种手段，进一步大幅降低小流量成本，相比Encoder模型下降到约三成。

****双塔模型（startlux）进展****

- 决策-双塔模型架构充分利用提前缓存的优势，继续降低实验成本。

END

**推荐阅读**

[从代码生成到需求交付：DarkFactory 的工程实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607833&idx=1&sn=46122dcf464df97a601d62e805c5e617&scene=21#wechat_redirect)

[研发Loop的上下文优化与多Agent协作实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607822&idx=1&sn=aff3817a60d009e1427b8ea14823c07a&scene=21#wechat_redirect)

[AI 内容核查怎么做：智能内容 AI 核查系统实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607774&idx=1&sn=fe90aff1e78ff6f023dabeb9dcf2ad63&scene=21#wechat_redirect)

[QCon上海2026：百度 SRE Agent 规模化落地实践解读](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607755&idx=1&sn=936783445cb9453c62b22c7aeb92014b&scene=21#wechat_redirect)

[好看视频鸿蒙端AI研发交付流程的建设思考与实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607730&idx=1&sn=f7ae4efd3270278f46340fc01e4abab9&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过