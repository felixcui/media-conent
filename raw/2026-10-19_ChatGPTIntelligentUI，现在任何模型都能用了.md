# ChatGPT Intelligent UI，现在任何模型都能用了

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/fkzgh_aEf2APAPZ_6W3FAQ

---

## 摘要

Machina 用开源框架 OpenUI 在任意模型上复现了 ChatGPT Intelligent UI 的生成式交互，让 Claude Opus 5.5 和 Kimi K3 等模型能直接输出可点击地图与行程界面而非文字墙。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

ChatGPT 最新的 Intelligent UI 让人眼前一亮：让它规划一次旧金山之旅，它直接给你一张地图、几张照片、一个可以点选的路线。不用读大段文字，看就行了。

现在，Machina 用开源框架 OpenUI 在任意模型上复现了同样的交互。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ8CahvvDmtpPQV2picCFNgq4MmiaBkZaicHiasMJIEHXN9Jf4VfzgF0T8tLhk4agF9ZL3AxXpFwJ6Eq52N0Qu8R0FW1uW1ia8lHMuZA/640?wx_fmt=jpeg)

他让 Claude Opus 5.5 和 Kimi K3 分别规划「旧金山一日游」，两个模型都没有输出大段文字，而是返回了一张可点击的地图和行程。下面视频是两者的对比：

## 问题出在哪

有一小撮重度 AI 用户在拼命消灭界面。黑屏终端，白色文字，没有按钮。他们觉得CLi才是最好的交互方式，但这群人很小。

绝大多数用 AI 的人并不想要一个黑屏终端。他们想看到东西，点击东西，快速做决定。你让 AI 帮你找酒店，它做了所有调研、比价、读评论，然后丢给你一堵文字墙，把决策工作原封不动还给了你。ChatGPT 的 Intelligent UI 解决了这个问题，却只在自己的聊天产品里提供。

如果你在构建自己的应用或帮客户做 agent，你还是在用文字回复。

## Generative UI 是什么

AI 决定答案应该长什么样，屏幕自己围绕答案构建。

原理上，模型不写网页代码，而是从你预先定义好的组件里做选择：卡片、图表、地图、按钮。模型决定用哪些组件、怎么排列，OpenUI 负责把它们画到屏幕上。就像从自己打包的乐高盒子里搭东西，界面风格始终是你产品的风格，模型也不会跑到盒子外面搞破坏。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJicH1QibRvUlpFryrUS4XOPuUxIGSLJgVMlBj9sDVozX1ra8GKyPN9x5cbzc1nsIKonuYMdpxECyXGCxvGC1EFWG0ACsME8bJzvs/640?wx_fmt=jpeg)

具体流程五步：

1. 定义或复用一套组件库
2. 从组件库生成系统 prompt
3. 把 prompt 发给模型
4. 模型流式返回 OpenUI Lang
5. Renderer 渐进式渲染成界面

## OpenUI Lang 好在哪

模型输出的不是 JSON，而是一种叫 OpenUI Lang 的紧凑格式。它专门为流式生成 UI 设计，核心优势就三个：

**省 token。** 在七个 UI 场景的基准测试中，OpenUI Lang 比 Vercel 的 JSON-Render 少用了 52.8% 的 token，比 Thesys C1 JSON 少用了 51.7%。具体到场景：contact-form 场景下差距最大，分别少了 67.1% 和 65.4%；dashboard 场景差距最小，也少了 45% 以上。完整数据：

| 场景 | Vercel JSON-Render | Thesys C1 JSON | OpenUI Lang | vs Vercel | vs C1 |
| --- | --- | --- | --- | --- | --- |
| simple-table | 340 | 357 | 148 | \-56.5% | \-58.5% |
| chart-with-data | 520 | 516 | 231 | \-55.6% | \-55.2% |
| contact-form | 893 | 849 | 294 | \-67.1% | \-65.4% |
| dashboard | 2,247 | 2,261 | 1,226 | \-45.4% | \-45.8% |
| pricing-page | 2,487 | 2,379 | 1,195 | \-52.0% | \-49.8% |
| settings-panel | 1,244 | 1,205 | 540 | \-56.6% | \-55.2% |
| e-commerce-product | 2,449 | 2,381 | 1,166 | \-52.4% | \-51.0% |
| **合计** | **10,180** | **9,948** | **4,800** | **\-52.8%** | **\-51.7%** |

**真流式。** token 到了就渲染，不用等完整 JSON 闭合。

**可控。** 输出被限制在你注册的组件范围内，带 Zod schema 校验，模型没法越界。

## 上手只要一条命令

需要 Node.js 24、pnpm，以及一个 OpenRouter 的 key。OpenRouter 用一个 key 就能调用几乎所有主流模型，这也是换模型像换配置一样简单的原因。

```bash
pnpx @openuidev/cli@latest create --example open-intelligent-ui
```

这条命令自动创建项目、装好依赖并启动。然后编辑.env 文件，填入 OpenRouter 地址、key 和模型 ID，比如 `anthropic/claude-opus-5.5` 。再 `npm run dev` ，打开 localhost:3000，问它一个需要可视化回答的问题。地图出现了，就跑通了。

## 一个关键点

有网友指出，这个功能能在任何模型上跑，是因为渲染层接管了大部分工作。模型输出一个组件 schema，应用负责绘制。只要模型能返回 JSON，就能用。ChatGPT 的智能界面并没有用上什么独家模型能力，只是先做了一层渲染。

这也解释了为什么 OpenUI 能在多框架、多平台上跑。它目前支持 React、Vue、Svelte、Angular，还有 A2UI 协议（Google 的 Agent-to-User Interface）和 LangChain/LangGraph 集成。以下是和其他方案的对比：

| 特性 | OpenUI | json-render (Vercel) | A2UI (Google) | CopilotKit OpenGenUI |
| --- | --- | --- | --- | --- |
| Token 消耗 | 1x | 3x | 3x | 4x |
| 延迟 (60 tok/s) | 4.9s | 14.2s | 14.2s | ~20s |
| 流式输出 | 是 | 是 | 是 | 部分 |
| 输出一致性 | 是 | 是 | 是 | 否 |
| 组件 | 内置库 + 自定义 | 内置库 + 自定义 | 仅自定义 | 无 |
| 多平台 | Web, mobile, email | Web, mobile, PDF, email, video | Web, iOS, Android | Web |
| 内置数据获取 | 是 | 否 | 否 | 否 |
| 内置 Chat UI | 是 | 否 | 否 | 是 |

## 想直接试？

不想安装的话，打开 https://openui.com/compare 在浏览器里可以直接试。

GitHub：https://github.com/thesysdev/openui

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过