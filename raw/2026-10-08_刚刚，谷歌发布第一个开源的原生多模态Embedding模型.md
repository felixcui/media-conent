# 刚刚，谷歌发布第一个开源的原生多模态 Embedding 模型

**作者**: JJJohn

**来源**: https://mp.weixin.qq.com/s/0iLljlX00Nx-7vqGM-RGnw

---

## 摘要

谷歌正式开源首个原生多模态Embedding模型EmbeddingGemma 2，以Apache 2.0协议发布，权重已上线Hugging Face和Kaggle。该模型总参数量740M，由270M文本主干、170M视觉编码器和300M音频编码器组成，可按需加载实现四种规模，纯文本仅需270M。它支持文本、代码、图片、视频、音频五类任务，输出768维向量，支持100多种语言和8K上下文，并采用Matryoshka表示学习可截断至128维。

---

## 正文

JJJohn JJJohn

在小说阅读器读本章

去阅读

刚刚，谷歌 CEO 劈柴哥 Sundar Pichai 和 Google DeepMind 同时官宣，开源 EmbeddingGemma 2。

![劈柴哥官宣](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkibJDCiaj3q1Y03J0jAnwvFFa9Rgw13jGnS75XEQhMcI5xYaxhnnwMCk6NLibn7AvLicAtWuY8ksDcsgr4GqAPkzQLPpn4Mhr06KE/640?from=appmsg)

劈柴哥官宣

按劈柴哥的说法，这是谷歌 **第一个开源的、原生多模态的 Embedding 模型** 。

文本、代码、图片、视频、音频这五类任务，全都被装进了一个 740M 参数的小模型里，权重也已经放上了 Hugging Face。

DeepMind 也发了条帖子，解释它具体是做什么的：

![同一个向量空间](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFl1Oicf8BZcVXlWv3aPibuRPDW9jKd6SNR8uFXrEKMqvppWsvwqQyjVleqDx74zF6KlMpBD9Q1lFFMUZibRa28XHiak9vADViaD40Fw/640?from=appmsg)

同一个向量空间

一张猫的照片、「cat」这个单词、一段猫叫声，经过 EmbeddingGemma 2 之后会落进同一个向量空间，而且挨得很近，一辆红色的车则被放到了远处。

以前要做这种跨模态的检索，得是文本一个模型、视觉一个模型、音频再来一个模型。现在一个就够了，而且 **是能在手机上跑的那种** 。

DeepMind 还补充说， **协议是 Apache 2.0** ，Hugging Face 和 Kaggle 上都能下载了。

![DeepMind 的帖子](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnrSey5B9eW2cMuJMCiaClzRGxBgqiaOkrMjbYicZPykTHSj8XrSc0jtc7xBY5qudxIURicVYMg2ib6NeaNYNztCc693ic2dWoM0MnYY/640?from=appmsg)

DeepMind 的帖子

## 模型结构

01

740M 是全模态加在一起的数字，它其实是由三块拼起来的。

文本主干有 270M（130M 的 transformer 加 140M 的 embedder），视觉编码器 170M，音频编码器 300M，其中后两块可以不加载，所以实际跑起来有四种大小：

| 加载的模态 | 参数量 |
| --- | --- |
| 纯文本 | 270M |
| 文本 + 图片 | 440M |
| 文本 + 音频 | 570M |
| 全模态 | 740M |

如果只做文本检索， **270M 就够了** 。

它是在 Gemma 4 的架构上做的，和 Gemma 4 共用同一套文本 tokenizer 和音频编码器，两个模型放在一起跑本地 RAG 的时候，总的内存占用还能再省一些。

其他几个参数：

• 输出 768 维向量，支持 100 多种语言

• 上下文 8K token，是上一代的 4 倍，一次能放进 5.5 分钟的音频、29 张图片或者 58 帧视频（默认每秒抽 1 帧），也可以混着放

• 支持 Matryoshka 表示学习，768 维的向量可以截到 512、256、128 维，向量库的存储最多能降到原来的六分之一

• 文本输入可以带一个任务前缀（搜索、问答、代码检索、分类、聚类等），让同一段文字针对不同任务给出不同的向量

量化之后放到 Pixel 11 Pro 上跑，官方给的数据是 **纯文本只占约 191MB 内存，全模态约 567MB** 。

模型卡里还写了两个容易踩的坑。

一个是截维度。截到 256 维基本不掉分，但到了 128 维，多模态的分数会掉得很厉害（MMEB v2 从 59.01 掉到 45.65），官方建议 128 维只用在纯文本上。

另一个是精度， **不要用 float16 来跑** 。

它的激活值超出了 float16 能表示的范围，结果会变成 NaN 或者悄悄变差，而且还不报错……官方让用 bfloat16 或者 float32。

## 跑分

02

模型卡中的成绩单（768 维，全精度）：

| 模态 | 评测 | EmbeddingGemma 2 | 上一代 |
| --- | --- | --- | --- |
| 文本 | MTEB 多语言 v2 | 61.36 | 61.15 |
| 文本 | MTEB 代码 v1 | 78.68 | 68.76 |
| 图片 | MIEB lite | 64.64 | \- |
| 图片 | MMEB v2 Image | 57.28 | \- |
| 文档 | MMEB v2 VisDoc | 67.84 | \- |
| 视频 | MMEB v2 Video | 50.67 | \- |
| 音频 | MSEB 检索 | 69.54 | \- |
| 音频 | MAEB | 49.39 | \- |

多语言文本的成绩和上一代基本持平， **涨得最多的是代码检索，从 68.76 到了 78.68** ，将近 10 分。

给本地代码库建索引、给 coding agent 做检索，也是谷歌这次专门点了名的用法。

图片、视频、音频这几行上一代是空的，因为上一代只支持文本。

劈柴哥帖子里说的「超过一些比自己大两倍多的专用模型」，对应的是官方博客里的三张散点图，横轴是模型大小，纵轴是分数。

![代码检索](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlgfcVBY6Qx6UIr6vibpntzWn23IINyjzf4g2iakNqMgDPhBsavgOq5XVCtDM2E0icRDGuvaGVqOZ2E3GVLneXibrYXYgNcNaxwowg/640?from=appmsg)

代码检索

代码检索只用得上那 270M 的文本部分，按这个大小算，它压过了体积是自己两倍多的 Qwen3-Embedding-0.6B，和 4B 的 pplx-embed-v1 差不多在一个水平，最高的还是 Qwen3-Embedding-8B。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlSCINIGEyIISaCrR4cicUbxbFDqUp5uYsCjq7EHJaticQzv4a7xqLKd63SfkRv1ibRXxAiaqpeqzVNurX2GWO9l64eEljicGe72tWo/640?from=appmsg)

图片

图片方面，它和 3B 的 LCO-Embedding-Omni 只差 1 分左右，jina-embeddings-v5-omni-small、SigLIP 这些都排在它的下面。

![音频](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnE3X5tfbl5S5PVS8zKEiarXjtb3EiaSibxaemRiaXiabEUIPCIYnwZX3XCQxWR35tXrzMbVGNy9pgsmouLHtMr1n9LPuibWllYWgPRc/640?from=appmsg)

音频

音频上它比 jina-embeddings-v5-omni-nano 略低一点，而 7B 的 Qwen2-Audio 和 3B 的 Qwen2.5-Omni 则被它落下了一大截（这两个本来也不是专门做 Embedding 的）。

官方自己的定位是： **1B 以下最强的多模态 Embedding 模型之一** 。

## 对比友商千问、OpenAI

03

那它和千问、和 OpenAI 的 Embedding 等友商相比如何呢？

千问现在有两条 Embedding 线，也都是 Apache 2.0。一条是去年 6 月的 Qwen3-Embedding，纯文本，有 0.6B、4B、8B 三个尺寸。

另一条是今年 1 月的 Qwen3-VL-Embedding，支持文本、图片和视频，有 2B 和 8B 两个尺寸。

OpenAI （对外）在用的还是 2024 年 1 月发的 text-embedding-3 系列，纯文本，只有 API。

把大家放在一起来看：

|  | EmbeddingGemma 2 | Qwen3-Embedding-0.6B | Qwen3-VL-Embedding-2B | text-embedding-3-large |
| --- | --- | --- | --- | --- |
| 参数量 | 740M（纯文本 270M） | 0.6B | 2B | 未公开 |
| 模态 | 文本（含代码）、图片、视频、音频 | 文本 | 文本、图片、视频 | 文本 |
| 向量维度 | 768 | 1024 | 2048 | 3072 |
| 上下文 | 8K | 32K | 32K | 8K |
| MTEB 多语言 | 61.36 | 64.33 | 63.87 | 58.93 |
| MMEB-V2 总分 | 59.01 | \- | 73.2 | \- |
| 权重 | Apache 2.0 | Apache 2.0 | Apache 2.0 | 闭源 |

（千问和 OpenAI 的分数取自千问的模型卡，EmbeddingGemma 2 的取自谷歌的模型卡，两边的评测口径可能会有细微出入）

和千问相比， **单论分数的话，EmbeddingGemma 2 是打不过的。**

纯文本上它比 Qwen3-Embedding-0.6B 低了 3 分，多模态的 MMEB-V2 比 Qwen3-VL-Embedding-2B 低了 14 分，而 8B 的版本更是到了 77.8。

但两边关注的地方不一样。

Qwen3-VL-Embedding 最小也有 2B，而且不支持音频。EmbeddingGemma 2 全模态加起来才 740M，奔着的是手机和笔记本。

而 OpenAI 的 text-embedding-3-large 的 MTEB 多语言是 58.93， **被 EmbeddingGemma 2 那个 270M 的文本部分超了 2 分多** 。

模态上它肯定是更全的，OpenAI 的 Embedding 到现在还只能支持文本。

而很关键的一点是，它是开源的。

谷歌自己也有闭源的 Gemini Embedding 系列，需要走 API，官方说 EmbeddingGemma 2 和它用的是同一套技术。

## 四个 demo

04

官方这次配了四个 demo，你可以带着问题往下看：我可能用来做些什么？

第一个是 Google AI Edge Gallery 里的 Instant Media Search，在手机相册里打字搜图，或者举起相机，拿眼前的东西去搜相似的照片：

![相册搜索](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmTk0lNHNBYVujc7GlmRwphQibrIHW80gtn3MjdBpbibPq4bbIyuibKv6JXia2NibMj09xBLBQjiavsUYT82Bu1HG68bWDIa4td9PCp8/640?from=appmsg)

相册搜索

输入「cat sleeping on keyboard」，搜出来的便是趴在键盘上睡觉的猫。

第二个是 Video Moments Finder，在一段视频里搜「Turtle eating」，海龟吃东西的那几段就在进度条上被标了出来：

![视频片段定位](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFnfcAaqEaJJd5Gy9VHM0tx6YRasgA2U2YFbmfv6bepOADicrHx4OlNJHhu8rqxjDvpWD3mwkc7zSh2fBRl9R0eGCKibdMZ10MG6A/640?from=appmsg)

视频片段定位

查询也可以换成一段音频，DeepMind 帖子里说的「用一段语音备忘去找视频里的某个瞬间」，就是它。

第三个是 Google AI Edge Foresight，由 EmbeddingGemma 2 负责在本地文件里检索，Gemma 4 负责回答。

开会时有人问了个问题，答案和出处就自己出现在侧边栏里了：

![Foresight](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFlrlMaIvp4Llp7MpOyupammZr7S25lScF0oEna8FpXicMpzqAQmmnfEV91GwhicAez15Sh5zxAzM5twtic52G8BtibC4V1PCb42iaro/640?from=appmsg)

Foresight

第四个是拿它来做实时决策的 MediaPipe Decision Task API，演示是一个仿 Chrome 小恐龙的跑酷游戏（这是要 PK 一下 Jev 啊）。

上面一条跑道，由 270M 的 EmbeddingGemma 2 在浏览器里判断该跳、该蹲还是该冲刺，下面一条跑道则交给了普通的 LLM：

![小恐龙](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmN1uK9ryqJhcDciamHlXFBosy2xwL5uiaRibk0AmdvxoicQ7RIjibARakoEeE0Vf5y6ro8ia3RcrCmjF4WWp87SNBUNrbrcgFp4SFPs/640?from=appmsg)

小恐龙

**前者一次决策 43 毫秒，后者要 640 毫秒。**

等 LLM 把那段 JSON 吐完，恐龙已经撞上去了……

工具链方面，transformers、sentence-transformers、MLX、vLLM、llama.cpp、SGLang、Ollama、LM Studio 都已经支持。

浏览器里可以用 transformers.js 或 WebGPU，Unsloth 也给出了微调的教程。

用 sentence-transformers 的话，可以参考下面的代码：

```
●●●from sentence_transformers import SentenceTransformer

model = SentenceTransformer("google/embeddinggemma-2")

query_emb = model.encode("What causes the northern lights?", prompt_name="SearchQuery")
doc_emb = model.encode("The northern lights are caused by charged particles from the sun.", prompt_name="Document")
print(model.similarity(query_emb, doc_emb))
└
```

## 相隔一年

05

谷歌今年在开源上其实一直有些动作。

4 月的 Gemma 4 第一次把协议换成了 Apache 2.0，6 月又补了一个 Gemma 4 12B，夏天还陆续放出了 TimesFM 3.0、TabFM 等模型。

但 Embedding 模型的上一次更新还是去年 9 月的初代 EmbeddingGemma，308M、纯文本，用的也还是谷歌自家的 Gemma 协议。

到这次的第二代，中间 **隔了 13 个月** ，协议也跟着换成了 Apache 2.0。

官方博客里说，初代的下载量已经超过了 2000 万次。

## OpenAI 的乌龙

06

说到 Embedding 和开源，还有个小插曲。

今年 4 月 22 日，OpenAI 给开发者群发了一封模型下线通知，官方的 deprecations 文档也同步更新了。

名单里就有 **text-embedding-3-small** ，按当时开发者们转述的说法，它排在 10 月 23 日下线的那一批。

Embedding 模型下线，和聊天模型下线不是一回事。聊天模型换个型号接着用就行，Embedding 模型一换，库里存着的所有历史向量都得重新算一遍。

很快就有开发者在官方社区发帖，问 OpenAI 能不能在下线之后把它开源出来：

![开发者社区的帖子](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFl1PJxNJ94J2nBBJnYVapXrVQYeXKmMWn3ibIBytb4xL8vWEYKGSDOShLw50MFmI5z3b33JlP77iaIbyPxQqgRL7C2aW5L6iaibtyE/640?from=appmsg)

开发者社区的帖子

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 如果不行，这就开了一个危险的先例。开发者只会更愿意把系统建在开源的 Embedding 上，免得哪天 OpenAI 决定下线某个模型，自己的系统也跟着垮掉。

这封乌龙邮件，我也有收到。

我当时还慌了，我好多数据都在用 OpenAI 的 Embedding，那我是不是得考虑迁移了？

几个小时之后，文档里的那一行先不见了。随后 OpenAI 又发了一封更正邮件，说上一封写错了，text-embedding-3-small 并不会下线。

总算是虚惊一场，我目前就也没动。

不过要是当初没有这封更正，按那个日期算， **再过两个多星期，它就该停掉了** 。

而 EmbeddingGemma 2 的权重下到自己硬盘上之后，就没有谁能给你发这种邮件了。

◇ ◆ ◇

官方博客：https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/

Hugging Face：https://huggingface.co/google/embeddinggemma-2

Sundar Pichai 的帖子：https://x.com/sundarpichai/status/2107501975671890211

Google DeepMind 的帖子：https://x.com/GoogleDeepMind/status/2107502286758895878

OpenAI 开发者社区的帖子：https://community.openai.com/t/open-sourcing-text-embedding-3-small-after-deprecation/1379551

![](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFkTVMiaBJThORibtsevicWQCJkKFeuKhPaKF4KSVWLu0195WIgmjVia9MicE3J2IMiaWBEOEZAn7p80ibdic4ibhcjI9wKw8MfLe1qbnOes/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过