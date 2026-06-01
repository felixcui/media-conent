# Anthropic 偷偷给 Claude Code 上了个官方插件，专治不会配的人

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/YOTKNUD_nlZnM2cvvyFCHQ

---

## 摘要

Anthropic悄悄发布了Claude Code官方插件claude-code-setup，能以只读方式扫描代码库，智能推荐适合该项目的MCP Servers、Skills、Hooks、Subagents和Slash Commands五类自动化配置，用户通过自然语言即可获取建议并自主决定是否安装，有效降低了Claude Code复杂的配置门槛，但大项目可能产生噪音且未解决CLI会话丢失等底层痛点。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

Anthropic 没怎么吆喝，悄悄给 Claude Code 放出了一个官方插件，叫 `claude-code-setup` 。

功能很直接：扫一遍你的代码库，然后告诉你这个项目适合配哪些自动化。覆盖五类东西：

- **MCP Servers** ：外部集成，比如查文档的 context7、跑前端的 Playwright
- **Skills** ：打包好的能力模块，比如 Plan agent、frontend-design
- **Hooks** ：自动化动作，比如自动格式化、自动 lint、拦截敏感文件
- **Subagents** ：专项审查代理，安全、性能、可访问性各管一摊
- **Slash Commands** ：常用工作流的快捷指令， `/test` 、 `/pr-review` 、 `/explain`

用法也朴素，直接说人话就行：

```
"recommend automations for this project"
"help me set up Claude Code"
"what hooks should I use?"
```

这个插件是 **只读** 的，只分析不改文件，看完推荐再自己决定要不要装。

![Automation recommender analyzing a codebase and providing tailored recommendations](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ8mnSX9ohC6ZibeouibKe5xLptkknjyIlmbOBrHazo1HrhS0DOrhbvlfA0kUj25053eYjia6pEFHmFSGia5bD2Ux0CTGrr8rt8pMtE/640?wx_fmt=png&from=appmsg)

说句实话，Claude Code 这套配置体系，hooks、skills、MCP、subagents 摞在一起，新手第一次看基本是懵的。大多数人装完就用个对话框，剩下一半功能压根没碰过。这个插件至少把入门门槛压低了。

不过，有人担心大项目自动扫会吐出一堆噪音，建议先手动收窄范围再跑；也有人指出配置层解决不了 CLI 本身的问题，比如重启会话就丢、长会话自动压缩会悄悄丢掉早期的决定。这些是另外的话题了，但确实是 Claude Code 现在的实际痛点。

仓库地址：https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过