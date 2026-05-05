# Cursor SDK正式发布，“cursor” inside！

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/Ufn8eGaUG-z_VraA_uOSEA

---

## 摘要

Cursor正式发布TypeScript SDK，将智能代理运行时打包成可编程组件，使开发者无需打开IDE即可驱动Cursor工作，成功跳出纯编程工具的局限。该SDK提供生产级智能体开发套件，支持本地与云端双模部署，具备沙箱环境与断网不中断等特性，企业已将其应用于构建定制代理、工单自动转合并请求及维护自愈代码库。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

四月的最后一天，Cursor终于正式放出了他们的TypeScript SDK。这不是简单的API封装，而是把整个智能代理运行时（Agent Runtime）打包成了可编程组件。这样不必打开Cursor IDE就能驱动Cursor干活，也就是说他终于跳出了编程工具的定义。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJib3ibeIAicUnsYVJ7BXEeaVAFWOYKCd21DQKicvYeO32SzspzJO9ECN5icOWE8zicUIiahhfmz7lLl5ibvHia89548k7ic2OsDdu4DguNQs/640?wx_fmt=jpeg)

Cursor SDK提供一整套完整的生产级智能体开发套件，模型无关，支持双模部署，本地运行时直接操作工作区代码，云端模式则自带沙箱环境、仓库克隆和开发环境配置，断网也不中断任务。

运行时即服务

Rippling和Notion等公司已经在用这个SDK做三件事：

1. 构建定制化后台代理
2. 让工单自动变成可合并的PR
3. 维护具有自愈能力的代码库

开发者Hemachandiran说，这相当于把IDE里的推理模型直接植入产品。"当代理能看见完整的CI/CD日志和部署状态时，它们才真正开始理解系统。"

有开发者吐槽说，现在最难的不是搭建代理，而是决定哪些任务值得自动化。"这已经变成决策问题，不是技术问题。"

### 开箱即用的代理栈

SDK包含三个关键部分：

- **托管云** ：带沙箱的专用VM
- **本地工作站** ：完整开发环境
- **模型层** ：支持Composer、Claude、GPT等
```typescript
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  model: { id: "composer-2" },
  cloud: { autoCreatePR: true }
});

const run = await agent.send("修复鉴权令牌过期问题");
```

目前SDK仅支持TypeScript，Python版本还在路上。但更值得关注的是Composer模型首次开放给外部使用——这个专为代码优化的模型，可能比SDK本身更具战略价值。

Cursor在GitHub放了Cookbook，里面有四个现成模板：

1. 极简CLI工具
2. 原型设计web应用
3. 看板任务自动化
4. 编码代理命令行

地址：http://github.com/cursor/cookbook

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过