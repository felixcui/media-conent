# 港大实验室111天拿下2万GitHub Star：开源了一款 AI 个性化辅导私教，在 GitHub 上杀疯了！

**作者**: 未知作者

**来源**: https://mp.weixin.qq.com/s/e3npT7ZULHmvVzAOsZK4MQ

---

## 摘要

港大实验室开源的AI学习工作空间DeepTutor上线111天即获GitHub两万Star，它超越了单一问答，集成了对话、研究、解题等多种学习模式。该系统由统一Agent引擎驱动，实现跨模式上下文无缝衔接，其核心亮点在于三层可检查记忆系统，将交互追踪、摘要与综合理解全部可视化且支持编辑溯源。此外，用户还能创建具有持久记忆的AI长期伙伴，打造真正的个性化终身辅导体验。

---

## 正文

在小说阅读器读本章

去阅读

有一个数据值得关注：

GitHub上，一个叫 DeepTutor 的开源项目，111天拿到了2万颗Star。

这是什么概念？按照GitHub的正常增长曲线，大多数优质开源项目要花一两年才能达到这个量级。

而且这不是某个大厂出品——是香港大学数据科学实验室（HKUDS）的研究项目，背后有arXiv论文支撑。

它在做什么？定位是"终身个性化辅导"工具。但深入看下去，它做的事情远不止"辅导"两个字。

![DeepTutor 首页 —— 聊天工作台：侧栏汇集 Home、Partners、My Agents、Co-Writer、Book、Learning Space，底部固定 Memory、Knowledge Center、Settings；主区域是问候语与输入框。](https://mmbiz.qpic.cn/mmbiz_png/lRCYHuYWAuIu8I96hwDm49JaY7hYk5WGsOQdXNOTDg3WsMCRdeK2RyzDJNJdibv6jrdna0FgTmsGw6fcE9vGczIYa4ZQ3eDdJOicZ3JYG9Fko/640?wx_fmt=png&from=appmsg)

DeepTutor 首页 —— 聊天工作台：侧栏汇集 Home、Partners、My Agents、Co-Writer、Book、Learning Space，底部固定 Memory、Knowledge Center、Settings；主区域是问候语与输入框。

它到底是一个什么产品

DeepTutor 的产品形态是一个AI学习工作空间。

不是单一功能，不是问答机器人，是一个把学习、研究、练习、记忆、创作全部串起来的系统。

核心思路是：用一个Agent引擎跑所有模式，而不是每个功能单独搭一个AI助手。

所以你在DeepTutor里可以：

- Chat —— 跟知识库对话、做研究
- Quiz —— 自动生成练习题，检验学习效果
- Research —— 做深度研究，输出报告
- Visualize —— 数据可视化、图表生成
- Solve —— 解题，带步骤拆解
- Mastery Path —— 掌握路径，按掌握程度规划学习顺序

所有这些模式，共用同一套Agent内核，共用同一个记忆系统，共用同一套知识库。

你在Solve里解题做到一半，切到Research继续研究同一个主题——上下文无缝衔接，不需要复制粘贴。

![我的智能体页面：上方是 Connected agents，下方是 Imported conversations](https://mmbiz.qpic.cn/sz_mmbiz_png/lRCYHuYWAuIhwRXDXPJYnCKI65VtcSdG9v9ibZmPgOQcJHMx6wIUuwQytYVTIE63IekQChnESPWjmMnibfmQ7libp8Pfd6fHv1EjvXusf89eX0/640?wx_fmt=png&from=appmsg)

我的智能体页面：上方是 Connected agents，下方是 Imported conversations

核心技术：三层次记忆系统

这是DeepTutor最有差异化的部分。

大多数AI学习工具是"用完就忘"——每次会话独立，历史积累依赖外部知识库。

DeepTutor做了一套三层可检查记忆系统：

- L1 追踪层 —— 记录每一次交互的原始痕迹，包括来源证据
- L2 摘要层 —— 把追踪记录提炼成表面摘要
- L3 综合层 —— 把跨会话的摘要整合成系统性理解

更关键的是：这三层全部可视化、可编辑。你能看到AI记住了什么、记住了哪来的，还可以手动修正。

它还内置了"记忆图谱"——每个结论都能追溯到原始证据来源。

![记忆总览：L1、L2、L3 层卡片与计数，以及记忆图谱入口](https://mmbiz.qpic.cn/sz_mmbiz_png/lRCYHuYWAuKY0aaSefJmic6dFMMDr201uuFzVSSKeMSxxr2rs3p6kYVnibwyMwWgLicbV59YEVeQNAMU9nBpkKV8w4DIbTYS13tia812tLLzc40/640?wx_fmt=png&from=appmsg)

记忆总览：L1、L2、L3 层卡片与计数，以及记忆图谱入口

Partners：把你的AI搭档变成长期伙伴

DeepTutor引入了一个"Partner"概念——

你可以创造一个AI角色，给它设定人格、知识背景、工具权限、记忆。

这个Partner不是一次性的会话，而是持久化的、有记忆的、能跨会话积累经验的AI搭档。

你可以：

- 给Partner上传专属知识库
- 安装社区Skills扩展Partner的能力
- 在任意对话里随时调取Partner参与讨论
- 每个Partner有自己独立的私人记忆

Community Skills可以从社区安装，也可以用一键装入。

```nginx
deeptutor skill install
```

此外，DeepTutor v1.4.7之后，还支持直接接入本地 Claude Code / Codex——把本地跑的大模型当作Partner，在DeepTutor里调用。

![伙伴页面——带已连接渠道的伙伴卡片](https://mmbiz.qpic.cn/mmbiz_png/lRCYHuYWAuKEBmDVeg7x35CWib9H9BH04nsgVNcqicEQMwn4VO6vzjsHfcVbAAEWSRTRB63NFw857KhQOoNDuhicicEAMHVYrjq9POJichPve5r0/640?wx_fmt=png&from=appmsg)

伙伴页面——带已连接渠道的伙伴卡片

技术细节

- 技术栈：Python 3.11+（后端）+ Next.js 16（前端）
- 协议：Apache 2.0，完全开源
- 模型支持：OpenAI / Anthropic / Gemini / 本地模型（Ollama / llama.cpp / LM Studio / vLLM），只要是OpenAI兼容接口就能接
- 部署方式：Docker 一键部署 / pip本地安装 / CLI命令启动 / 云端使用
- 多语言：内置11种语言界面，包括简体中文

安装和使用

一行命令启动（需要Python 3.11+）：

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init # 提示输入端口 + LLM 提供商 + 可选 embedding
deeptutor start # 同时启动后端 + 前端；保持终端开着
```

Docker方式：

```apache
docker run -p 18789:18789 ghcr.io/hkuds/deeptutor:latest
```

浏览器打开 http://localhost:18789，配置好API Key就能用。

完整的文档站：

```js
deeptutor.info
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lRCYHuYWAuLoJiaAb2eVmQKpd8PaG0zFMVz6jxXib4g33VAibq52UBRBRUMCott87kDg345Hwicz2klc2Do1X32frJibDHo7U89pJacIeibt5Vc9I/640?wx_fmt=png&from=appmsg)

适合谁用

- 学生 —— 不会的知识直接问，系统记住你学了什么、哪里卡住了，下次继续推进。
- 老师/培训师 —— 上传课件，自动生成练习题和掌握路径，观察每个学生的薄弱点。
- 研究者 —— 用Deep Research做文献调研，知识库连接多个RAG引擎，检索全面不遗漏。
- 知识工作者 —— 打造个人知识管理系统，所有笔记、文档、AI记忆、工作区连成一体。
- AI爱好者 —— Agent-native架构、多层记忆、Partners系统，是目前开源学习工具里架构最完整的一个。

最后

2万Star不是偶然。

DeepTutor解决了一个真实问题：AI工具越来越多，但它们互相孤立、记忆不连续、上下文不共享。

DeepTutor的思路是把所有能力收敛到一个Agent内核里，加上可检查的三层记忆，让AI真正成为"了解你学习历程"的长期伙伴。

不是替代你学习，而是陪你学习。

GitHub：https://github.com/HKUDS/DeepTutor

一个能记住你学了什么、卡在哪里、下一步怎么走的学习系统，这才是AI辅助学习该有的样子。

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过