# MCP Events：OpenAI 又给 MCP 添加了新能力

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/Fow44pT301_0DLhKzcLsXA

---

## 摘要

OpenAI 为 MCP 协议新增 Events 能力，改变 Agent 被动等待指令或轮询的工作方式，使其能主动感知环境变化。MCP 服务器声明支持的事件并实现 list、subscribe、unsubscribe 三个方法，用户通过 ChatGPT 订阅事件并提供回调 URL 和签名密钥，事件发生时服务器将匹配数据 POST 到回调地址，ChatGPT 按用户指令处理。订阅前服务器需验证权限、校验事件参数并验证回调 URL。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

OpenAI 最近给 MCP 协议加了一个新能力：Events。

现在 Agent 怎么工作的？你打开聊天框，敲一段 Prompt，等它响应。或者设个 Cron Job，每隔几分钟去轮询一次。两种方式都很被动。Agent 不会自己感知环境变化，它只是在等你的下一个指令。MCP Events 要改的恰恰是这套唤醒机制。

它的逻辑不复杂：MCP 服务器声明自己支持哪些事件，用户告诉 ChatGPT 要监控什么以及怎么处理，ChatGPT 订阅后提供一个回调 URL 和签名密钥。事件一发生，服务器把匹配的事件 POST 到那个地址，ChatGPT 收到事件后按用户的指令干活。

![OpenAI 文档中的插件页，事件与 MCP 工具并列显示。](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ9G58ywOhTNoA9rJ3gGpmquHb1NicmktlznJmH1MKF4X1qcicnzf6bdesQ1vAriceeeH6cYYbLRXQ0XOR9zL6ibwD4FAkvUIUACOYM/640?wx_fmt=other&from=appmsg)

## 协议怎么走

服务器要在 `server/discover` 的 capabilities 里声明 `events` ，然后实现三个方法： `events/list` 、 `events/subscribe` 、 `events/unsubscribe` 。

事件的 schema 分两部分： `inputSchema` 描述订阅时的过滤参数， `payloadSchema` 描述每次投递的数据形状。比如一个文档评论事件长这样：

```json
{
  "name": "comment.created",
  "description": "A new review comment was added to the specified document.",
  "delivery": ["webhook"],
  "inputSchema": {
    "type": "object",
    "properties": {
      "document_id": {
        "type": "string",
        "description": "ID of the document to monitor for new review comments."
      }
    },
    "required": ["document_id"],
    "additionalProperties": false
  },
  "payloadSchema": {
    "type": "object",
    "properties": {
      "document_id": { "type": "string" },
      "comment_id": { "type": "string" },
      "text": { "type": "string" },
      "url": { "type": "string" }
    },
    "required": ["document_id", "comment_id", "text", "url"],
    "additionalProperties": false
  }
}
```

用户说"帮我盯着这个文档的评论，有新的就通知我"，ChatGPT 调 `events/subscribe` ：

```json
{
  "method": "events/subscribe",
  "params": {
    "name": "comment.created",
    "arguments": { "document_id": "doc_123" },
    "delivery": {
      "mode": "webhook",
      "url": "https://receiver.example.com/mcp-events/callback_123",
      "secret": "whsec_<base64-encoded-signing-key>"
    },
    "cursor": null
  }
}
```

服务器在确认订阅前要做三件事：验证用户权限、校验 event name 和参数、验证回调 URL。验证回调的方式是发一个带 challenge 的签名请求过去，确认对方能正确 echo 回来。

这里面签名用的是 Standard Webhooks 规范。发事件时，服务器用 Node.js 大概是这么写的：

```javascript
import { Webhook } from "standardwebhooks";

export async function sendEvent(subscription, event, webhookFetch) {
  const body = JSON.stringify(event);
  if (Buffer.byteLength(body, "utf8") > 256 * 1024) {
    throw new Error("Event payload exceeds 256 KiB");
  }

  const signedAt = new Date();
  const signer = new Webhook(subscription.secret);
  const response = await webhookFetch(subscription.url, {
    method: "POST",
    redirect: "error",
    signal: AbortSignal.timeout(10_000),
    headers: {
      "Content-Type": "application/json",
      "webhook-id": event.eventId,
      "webhook-timestamp": String(Math.floor(signedAt.getTime() / 1000)),
      "webhook-signature": signer.sign(event.eventId, signedAt, body),
      "X-MCP-Subscription-Id": subscription.id,
    },
    body,
  });

  return { accepted: response.ok, status: response.status };
}
```

payload 上限 256 KiB，超了这个数文档建议只发摘要，让 Agent 通过 read tool 去拿完整记录。重试用指数退避，410 和 413 不重试。事件的 `cursor` 字段支持断点续传。

订阅有生命周期。 `refreshBefore` 是服务器给的过期时间，ChatGPT 会在这之前调 `events/subscribe` 续期。用户不再需要监控时调 `events/unsubscribe` ：

```json
{
  "method": "events/unsubscribe",
  "params": {
    "name": "comment.created",
    "arguments": { "document_id": "doc_123" },
    "delivery": {
      "mode": "webhook",
      "url": "https://receiver.example.com/mcp-events/callback_123"
    }
  }
}
```

有人会说这不就是 Webhook 吗。原理上确实类似，但关键区别在于协议和大模型上下文的标准化打通。以前你很难让外部业务事件直接、原生、低门槛地唤醒 ChatGPT。MCP 2.0 协议（版本 `2026-07-28` ）把这层打通了。

## 几个具体的场景

事件一旦能被标准化订阅，几个场景就不再是概念了。

第一个是工作流里的原生协作者。在 Notion、Figma 或 Linear 里 @Agent，它能立刻捕捉上下文执行编辑或任务，不像现在的机器人脚本那么死板。

第二个是智能分流与前置执行。Agent 监听 Slack 消息或 GitHub PR，不只是通知你，还能在打扰你之前完成优先级研判、草拟回复或跑完检查。

第三个是多 Agent 异步协作。主 Agent 做中枢，法律合规、数据校验等专业 Agent 作为事件驱动的模块按需介入。

文档里给的例子很具体：监控 #product -feedback 频道里的 bug 报告，自动开 draft PR 附带修复和测试（事件类型 `message.created` ，按 `channel_id` 过滤）；或监听文档的 review 评论，自动实现修改（事件类型 `comment.created` ，按 `document_id` 过滤）。

## 没那么乐观

但这不全是好消息。事件驱动会让 Agent 变得危险——没有人在环里，坏的工具调用或中毒的上下文没人拦，安全检查几乎没有时间。

Agent 在没有人类把关的情况下自主执行写操作，出问题的概率比有人盯着大得多。文档里也提醒了这点：确保写工具是幂等的，避免重复调用造成问题；如果订阅的行为会改变源应用的数据，要验证不会形成反馈循环。

另一个网友提到了一个更实际的顾虑：不用定时刷了，但愿别有点动静就来喊我。

这就回到一个老问题了：事件驱动的 Agent，它的判断力到底够不够。事件过滤只能做粗筛（按 channel\_id、document\_id 之类），真正决定"这个事值不值得打断我"的判断，还是得靠模型本身的能力。过滤条件设得太宽，就变成了另一个形式的噪音；设得太窄，可能漏掉该处理的事。

## 现状

目前 MCP Events 只在 Work 聊天（ChatGPT web 和桌面端 Cloud 模式）和 dots 中可用。ChatGPT 的集成不支持 Polling、Streaming，也不支持草案里的 `gap` 和 `terminated` 控制通知。可以说还是一个比较初期的实现。

但方向是对的。Agent 从"问答式工具"变成"自主数字员工"，中间缺的那一环恰恰是感知和响应环境变化的能力。事件驱动不是新概念，但把它标准化到 MCP 协议层、和大模型上下文打通，这件事值得关注。

OpenAI 官方文档：https://developers.openai.com/plugins/build/mcp-events

关注公众号回复“进群”入群讨论

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过