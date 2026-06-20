# Artifacts 来了：Claude Code 把 AI 会话变成了共享文档

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/ZAZQoeI7vWCpd2kPvjdLVw

---

## 摘要

Claude Code新增Artifacts功能，可将包含全量上下文的AI会话自动生成可交互的独立页面，实现链接一键共享与内容自动同步刷新，大幅简化团队协作中的进度同步流程。该功能目前仅限企业版，已有开发者推出开源落地工具及替代品tdoc。这不仅解决了整理文档的痛点，更标志着Agent时代团队协作的核心交付物正从代码向可审核的Artifact转变。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

刚刚，Claude官方宣布为Claude Code新增Artifacts功能，目前处于Beta阶段，仅对Team和Enterprise计划开放。

核心特性非常明确：

1. 完全基于Claude Code会话的全量上下文生成，包括关联的代码库、插件、连接的第三方工具数据，不用手动上传整理
2. 输出是可交互的独立页面，覆盖PR走查、项目仪表盘、故障分析报告、发布清单等常见协作场景
3. 默认私有，仅组织内成员可见，分享只要发链接就行，不用额外设置权限
4. 会话内容更新时，Artifacts会自动同步刷新，所有共享链接的人看到的永远是最新版本

直观感觉这不就是加强版的飞书文档嘛？之前用AI做团队协作，最麻烦的就是同步进度：你用Claude改了一下午bug，要给团队说清楚前因后果，得截好几张聊天截图、复制代码片段、拼错误日志，只要后面又调整了内容，所有材料都得重发一遍。Artifacts相当于把整个AI会话的工作成果打包成了一个自动更新的页面，一个链接搞定所有同步。

功能发布不到1小时，已经有开发者做出了上层落地工具。开发者Austin Wallace把自己之前做的PR Walkthrough技能适配了Artifacts，已经开源。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ9C7lVViawSmA5W0nVkYAfibhUG1gvcHjVich3kDWFxtUibaiaEghZZNfDIHtxrzJVkyFGZnfxDnMucEw0190H1Q4INI6rmRm7pMV1g/640?wx_fmt=jpeg)

这个工具能把Codex、Claude Code、OpenCode的会话历史，自动转成结构化的代码讲解页面：包括整个系统的架构图、每一步的决策逻辑、被否决的方案、踩过的坑、对应的代码链接，所有内容都打包成一个单文件HTML，不用依赖任何服务，打开就能看。

演示页面：https://austeane.github.io/walkthrough/out/meta-descent/walkthrough.html

开源地址：https://github.com/austeane/walkthrough

**开源替代：tdoc**

由于Artifacts目前仅限Team和Enterprise计划。这里有一个开源替代项目tdoc，可以部署在Cloudflare Worker，同时支持Claude Code和Codex。

核心能力：用 `/tdoc new "描述"` 让Agent生成文档， `/tdoc publish` 发布为公开链接。协作者可以像Google Docs一样选中任意内容评论，Agent读取评论后自动生成新版本，并在每条评论上标注 ✅ 已处理 / 🟡 部分处理 / ❓ 需要澄清。每次编辑都是完整快照，可随时回退。

安装就一行命令，跟着引导走完Cloudflare配置，3分钟上线。

开源地址：https://github.com/serenakeyitan/tdoc

在线演示：https://tdoc.serenatan.workers.dev/d/conway-life/v/2

tdoc的灵感来自Coinbase开发者Jesse Pollak提出的bdocs概念。如果官方一直不开放给个人用户，这大概是最接近的替代品了。

Artifacts的影响其实远不止“省了整理文档的时间”，它刚好踩中了现在AI时代团队协作的核心变化。  
早在一个月前，产品经理Paweł Huryn就写过一篇文章，说Agent时代PM的工作已经从审核代码，变成了审核Artifact。他自己两周内靠Agent发了三个项目、更新了一个SaaS产品，全程没读过一行代码，只审核Agent生成的Artifact：包括项目计划、决策记录、测试报告、变更说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ8pPgnVbrFicyBckTAzR04jOzichmp050Sf9WqHuS8icdzCSiaAOk39hPic9ejAOaauoMJTZu9cQUI6iakUFLSxg54icdH6aBWicqukyQ8/640?wx_fmt=jpeg)

这种模式已经在大公司跑通了：Google的产品团队已经从“先写PRD再开发”变成了“先做原型再对齐”，Meta的PM现在直接用Agent做原型给扎克伯格演示，LinkedIn甚至把PM岗的招聘考核改成了用AI做可运行的原型。

当Agent生成代码的速度比人对齐需求的速度还快的时候，团队的核心交付物就已经不是代码了，是承载决策逻辑的Artifact，包括演示视频、核心指标、决策记录，而不是底层的代码或者原始聊天记录，新的协作模式正在起变化。

官方详细说明：https://claude.com/blog/artifacts-in-claude-code

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过