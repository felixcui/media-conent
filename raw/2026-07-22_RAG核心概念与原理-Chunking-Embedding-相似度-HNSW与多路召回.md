---
title: "RAG 核心概念与原理：Chunking、Embedding、相似度、HNSW 与多路召回｜得物技术"
source: "得物技术"
link: "https://mp.weixin.qq.com/s/gfFlUUNbKZ23G7NgWHU3YQ"
description: "得物技术团队发布的RAG系统性入门教程，涵盖从原理到工程落地的完整链路。文章首先解释了RAG解决的LLM三大先天缺陷（知识时效性、幻觉、私有知识盲区），然后依次讲解Embedding（语义向量化与对比学习训练原理）、Chunking（切块策略与重叠设计）、相似度计算（余弦相似度vs欧氏/内积）、HNSW向量索引（分层可导航小世界图的建图与搜索原理）、以及完整检索链路（Query Rewrite→Metadata Filter→ANN+BM25双路召回→RRF融合→Rerank精排）。文章强调RAG效果关键在「搜得准」而非LLM本身，并区分了静态共享知识与企业动态个人记忆两种检索场景。"
updatetime: "2026-07-22"
---

# RAG 核心概念与原理：Chunking、Embedding、相似度、HNSW 与多路召回｜得物技术

> 作者：羊羽 ｜ 来源：得物技术 ｜ 2026-07-22
