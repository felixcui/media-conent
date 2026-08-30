# llm-d：别再用 Round-Robin 给 LLM 推理做负载均衡了

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/6rSmObuWO1PxB_Rr_Z0h3g

---

## 摘要

Round-robin 负载均衡会破坏 LLM 推理的 KV 缓存复用，导致前缀缓存失效、吞吐下降。llm-d 通过缓存感知调度、热副本粘性直至饱和、缓存分层卸载以及 prefill/decode 拆分，解决了这些问题，在相同硬件上可将输出吞吐提升约 3 倍，首 token 延迟降低一半。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

LLM 推理并不能像普通 Web 服务那样扩展。单个 vLLM 或 SGLang 实例上，KV 缓存的效果立竿见影。只要在多个副本前面放一个标准 Kubernetes Service，用 round-robin 转发请求，缓存带来的加速就大部分蒸发。每个 pod 都没见过之前请求的前缀，于是把整个上下文从头算了一遍。

Round-robin 假设每个副本对每个请求的服务质量相同。这对无状态 Web 流量成立，一旦请求之间共享缓存，这个假设就崩了。副本之间的差别在于它们各自记住了什么，而默认路由层完全无视这一点。

## 先补背景：KV 缓存从哪来，为什么值钱

LLM 生成回复分两个阶段。Prefill 处理用户输入的全部 token，并行度高，瓶颈是算力，衡量指标是首 token 延迟（TTFT）。Decode 逐个生成新 token，每次只算一个 token 的 query，但要把权重和缓存的 K/V 矩阵从内存里搬一遍，瓶颈是内存带宽，衡量指标是 token 间延迟（ITL）。

KV 缓存是 Attention 计算中产生的 Key 和 Value 矩阵。已经处理过的 token，其 K/V 在后续生成中不再变化，因此被留存复用。13B 模型大约每 token 产生 1MB 缓存，一个 4K context 的请求，光 KV 缓存一项就占 4GB 显存。

缓存这么贵，自然希望它能被复用。两个请求共享同一段前缀（比如相同的 system prompt）时，第二个请求可以跳过这段 prefill，直接开始生成。这就是 prefix caching。前提是请求必须落在同一个副本上。

## Kubernetes 要学的四个问题

**第一，哪台副本持有什么前缀。** 每个推理服务器在创建或驱逐缓存块时都会发出事件，路由层据此维护一份实时索引。llm-d 的智能路由器用这份索引做前缀缓存感知的调度。

**第二，什么时候该无视索引。** 缓存亲和性会把流量引向热的副本，超过负载阈值后，热副本自己就成了瓶颈。路由器在亲和性和纯负载均衡之间切换：低负载时粘住热副本，高负载时放弃亲和性。llm-d 管这个叫 sticky until saturated。

**第三，缓存还能往哪放。** 显存很快被塞满。llm-d 把缓存块分层卸载到 CPU 内存，再落到磁盘。4 张 H100、250 个并发用户下，这套分层机制带来 13.9 倍于全部缓存留在 GPU 的吞吐。

**第四，prefill 和 decode 要不要分开。** Prefill 吃算力，decode 吃带宽，放同一个副本上互相拖累。拆成独立池后，AWS 在 GPT-OSS 上测到最高 70% 的 tokens/sec 提升。代价是 KV 缓存要过一遍网络，首 token 出现前多一跳。

这些全部解决后，同样的硬件、同样的模型，输出吞吐大约提升 3 倍，首 token 延迟降低一半。

## llm-d 是什么

![llm-d 项目 logo](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJibroeCKPrMVFP6rpowe5nuyHH3uiavttpQIdVQSp0aiccVRjKHAWVbdahJZDsJ3nCGalmDHzVXGD3VOGzb5gozibyxGdN7FkTuFA4/640?wx_fmt=png&from=appmsg)

llm-d 项目 logo

llm-d 就是把这四个问题一起解决的项目。它运行在 vLLM 或 SGLang 之上，不替换它们，接管的是路由、缓存索引、分层卸载和 prefill/decode 拆分。Apache 2.0，云原生计算基金会（CNCF）sandbox 项目，由 Red Hat、Google Cloud、IBM Research、CoreWeave 和 NVIDIA 联合创立，AMD、Cisco、Hugging Face、Intel、Lambda、Mistral AI 等也在支持名单里。生产用户包括 Tesla、Snowflake、Cohere、DigitalOcean。

架构上，llm-d 位于 Kubernetes 与模型服务器之间，通过 Gateway API Inference Extension 感知每个副本的缓存和负载状态，把请求送到最合适的地方。

![llm-d 架构](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM75f9aIeicz5icSJ9rIPbiaE1H1uiaPa3aER1hf2icur6NXUxoTiaD38rjGKbHTc2pDwRsoSLtatDTEcwsf8l9UpqhLbcY9v7icVoXn93FicFcB79AG2A/640?wx_fmt=svg&from=appmsg)

## 实战复盘：特斯拉 × 红帽

今年 4 月，特斯拉和红帽的工程团队发了一篇复盘，讲如何把 KServe、llm-d 和 vLLM 组合成生产级推理栈。

特斯拉早期用 vLLM + Kubernetes StatefulSet，遇到三个问题：模型文件动辄几百 GB，NFS 网络存储拖垮加载；换成本地 LVM 后，pod 和节点绑定，硬件故障必须人工删除 PVC 再调度；NGINX Ingress 和 round-robin 对 LLM 负载完全无效，GPU 上的 KV 缓存被白白浪费。

切换到 KServe + llm-d 后，路由层通过 Envoy AI Gateway 做前缀缓存感知转发。Llama 3.1 70B 跑在 4× MI300X 上，tensor-parallel=4，gpu-memory-utilization=0.90，max-model-len=65536，输出 tokens/s 提升 3 倍，TTFT 降低一半。下图是切换路由后的效果。

![切换路由后的性能曲线](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ8ttzvibGEq1UIwrn5UFibvduvQhWdewRrQpMATzxdlsJicjuwguqWABoicfr6bo7ibckaYofrrxey1CiaF43EGRacdz61ZhibCGgM7XE/640?wx_fmt=png&from=appmsg)

切换路由后的性能曲线

过程中发现的问题也修回了上游 KServe：让 storageInitializer 可选（PR #4970 ），跟进最新 Gateway API Inference Extension（PR #4886 ）。

关注公众号回复“进群”入群讨论

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过