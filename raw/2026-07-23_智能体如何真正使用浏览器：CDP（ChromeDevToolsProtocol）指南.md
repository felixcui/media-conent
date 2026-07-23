# 智能体如何真正使用浏览器：CDP（Chrome DevTools Protocol）指南

**来源**: https://waytoagi.feishu.cn/wiki/Ac6nwuLyJi3IDNk2Sc0cdAQXnAf

---

## 摘要

本文介绍了Chrome DevTools Protocol（CDP），它是外部程序与Chromium浏览器通信的底层控制接口，我们常用的开发者工具面板正是通过该协议与浏览器交互。CDP最初源于WebKit远程调试协议，后随Chrome Blink引擎的拆分而独立演进，如今已被Puppeteer、Playwright以及各类浏览器智能体广泛作为实现浏览器自动化的核心通信标准。

---

## 正文

作者：Kyle Jeong（[@kylejeong](https://x.com/kylejeong)）

> [原帖链接](https://x.com/kylejeong/status/2078196340216185127)

**CDP 是让外部程序能够访问 Chromium 的页面、网络栈、JavaScript 运行时、输入系统、调试器和性能分析工具的控制接口。本文面向初学者介绍 CDP。**

当你打开 Chrome 并按下 F12 或 `Option + Command + I`，会出现一个面板：它能检查页面、观察每一条网络请求、执行 JavaScript、模拟手机，以及录制性能跟踪。

![图片展示了Chrome DevTools（开发者工具）界面，左侧是Browserbase网站，宣传其为开发者提供访问整个Web的代理，支持10,000+公司。右侧是DevTools面板，包含Elements、Console、Sources、Network等标签，显示了网页代码、网络请求等信息。该图与上下文紧密相关，直观呈现了上下文提到的“打开Chrome并按下F12或`Option+Command+I`，会出现一个面板”的场景，帮助读者更好地理解Chrome DevTools的功能。](https://feishu.cn/file/QCgPbFHF3oCO4Wxzv8lcodBEnQe)

这个面板是一个与浏览器通信的独立进程。两者之间使用的语言，就是 **Chrome DevTools Protocol**，简称 CDP。

在 Browserbase，我们花了多年工程时间试图驯服这个协议的不完美之处，也从中学到很多。这正是我们当初希望能读到的 CDP 说明文。

# DevTools 背后的协议

CDP 随 Chromium 系浏览器一起提供，包括 Chrome、Edge、Brave、Arc 和 Opera。DevTools、Lighthouse、Puppeteer、Playwright 以及许多[浏览器智能体](https://www.browserbase.com/agents)都通过它与浏览器通信。

只要你的代码控制着 Chromium，底层某处就存在 CDP。

## 一点历史

CDP 最初是 [Chrome DevTools](https://blog.chromium.org/2018/09/10-years-of-chrome-devtools.html) 背后的基础设施，并不是通用自动化 API。

Chrome 在 2008 年发布时，它的检查器来自 WebKit，也就是当时 Chrome 与 Safari 共享的渲染引擎。DevTools 前端需要与被检查的页面分开运行，因此团队定义了一套位于前端与浏览器之间的线协议。

```text
┌─────────────────────┐       CDP 消息        ┌─────────────────────┐
│ DevTools 前端       │  ← 命令 / 事件 →     │ Chromium 浏览器     │
│ HTML、CSS、JS       │                       │ 渲染器、网络、运行时、输入 │
└─────────────────────┘                       └─────────────────────┘
```

这套 [WebKit 远程调试协议](https://code.google.com/archive/p/chromedevtools/wikis/ChromeDevToolsProtocol.wiki)成了 CDP 的前身。

随后，Google 在 2013 年将 Blink 从 WebKit 中拆分出来。Chrome 的协议也随之独立，成为有文档、有版本的 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)。Safari 则继续使用 WebKit Inspector Protocol。

[Headless Chrome](https://www.browserbase.com/blog/what-is-a-headless-browser) 和 Puppeteer 在 2017 年出现，之后 Playwright 将浏览器自动化泛化到 Chromium、Firefox 和 WebKit。

## 亲自与 Chrome 通信

![图片为时间轴图，展示了从2008年到今天的浏览器相关协议演变。2008年Chrome随WebKit发布，2010 - 2012年DevTools前端协议拆分，2013年Blink分叉，Chrome协议分叉为CDP，2013年Node包装器，2017年无头+Puppeteer，2020年Playwright，2020年代理使用CDP，2021年Lighthouse、扩展和代理共享CDP。其中2013年Blink分叉处有虚线箭头指向“WebKit Inspector Protocol”，标注为“Safari track；limited cross - tool reuse”。](https://feishu.cn/file/CzkSbHKBTo65G0x7kBAcSeLtnpf)

启动 Chrome 时启用远程调试。请使用临时配置目录，因为现代 Chrome 限制在默认配置目录上启用远程调试。

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/cdp-demo \
  about:blank
```

现在 Chrome 会暴露本地发现端点：

```bash
# 在另一个终端中运行
curl -s http://localhost:9222/json/version | jq .
curl -s http://localhost:9222/json/list | jq .
```

第一个端点描述浏览器，第二个端点列出可附加的目标对象。页面目标对象中会包含 `webSocketDebuggerUrl`，即其 CDP 连接端点。

通过 WebSocket，你可以创建一个最简 DevTools 客户端：

```typescript
import WebSocket from "ws";

const targets = await fetch("http://localhost:9222/json/list")
  .then(response => response.json());

const page = targets.find(target => target.type === "page");
const socket = new WebSocket(page.webSocketDebuggerUrl);

let id = 0;
const send = (method, params = {}) => socket.send(JSON.stringify({
  id: ++id,
  method,
  params,
}));

socket.on("open", () => {
  send("Page.enable");
  send("Page.navigate", { url: "https://example.com" });
});

socket.on("message", data => {
  const message = JSON.parse(data);

  if (message.method === "Page.loadEventFired") {
    console.log("页面已加载");
    socket.close();
  }
});
```

这段代码连接到一个页面、启用生命周期事件、进行导航，并等待 Chrome 宣告页面加载完成。

CDP 的其他部分与此类似，只是规模要大得多。

## CDP 的语义

CDP 使用 JSON 消息，通常通过 WebSocket 或管道传输。协议被划分为 Page、Network、Runtime、Input、Target、Accessibility 和 Tracing 等域。

每个域负责浏览器的一部分：

- Page 负责导航。
- Network 观察请求与响应。
- Runtime 执行 JavaScript。
- Target 发现页面、框架与 worker。
- Tracing 记录性能数据。

![图片展示了Chrome DevTools Protocol中Network domain的结构。左侧是不同领域，如Page、Network、Runtime等，其中Network被红色框突出显示。右侧详细说明Network domain，包含Commands和Events两类消息，Commands有enable、getResponseBody、setExtraHTTPHeaders等，Events有requestWillBeSent、responseReceived、loadingFinished等。该图与上下文紧密相关，直观呈现了Network domain在DevTools Protocol中的位置及消息类型，帮助理解DevTools与Chrome通信时Network领域的操作。](https://feishu.cn/file/UrZTbSPQkoJC6KxHn1oc24jSnGg)

命令是要求 Chrome 执行某件事：

```json
{"id": 1, "method": "Page.navigate", "params": {"url": "https://example.com"}}
```

Chrome 会返回带有相同 ID 及结果的响应：

```json
{"id": 1, "result": {"frameId": "...", "loaderId": "..."}}
```

ID 让客户端可以同时发送许多尚未完成的命令，并将每个响应与其请求对应起来。

事件则反向传递。浏览器状态变化时，Chrome 会发出事件：

```json
{"method": "Network.requestWillBeSent", "params": {}}
{"method": "Page.frameNavigated", "params": {}}
{"method": "Runtime.executionContextCreated", "params": {}}
```

事件没有请求 ID。要读取它们，需要先启用某个域，再消费该域的事件流。

**CDP 命令是问题或指令，事件则是浏览器的回应。**

![图片展示了CDP（Chrome DevTools Protocol）中CDP客户端与Chrome之间的通信流程。左侧为CDP client，右侧为Chrome，中间通过一个WebSocket连接。CDP client发送带有id的“Page.navigate”命令，Chrome返回带有相同id及结果的响应。随后Chrome发出“Page.frameNavigated”和“Page.loadEventFired”事件，事件没有请求ID，需先启用域并消费事件流才能读取。该图直观呈现了CDP命令与事件的交互过程，与上下文对CDP通信机制的介绍相契合。](https://feishu.cn/file/WOowbnBgZovNLhxTy1kcHh2Lnyd)

## 会话与目标对象

可以把 CDP 连接想成一棵树。

![图片展示了Chrome DevTools Protocol（CDP）中目标对象的树状结构。根为浏览器，从浏览器开始，可发现并附加到页面、进程外iframe、service worker、shared worker或扩展页面等目标对象。每个目标对象对应一个会话，会话通过一个socket与客户端通信。页面目标对象的会话id为“page_A01”，其导航、DOM、输入和网络命令等路由在此。右侧还呈现了单个目标对应一个socket的逻辑，以及页面目标的示例帧内容。](https://feishu.cn/file/AXDUbqPHToXFHyxaEM4cxpmwnAc)

这棵树的根是浏览器；从那里开始，你会发现并附加到各种目标对象。

目标对象是 Chrome 可以检查或控制的东西：页面、[进程外 iframe](https://www.chromium.org/developers/design-documents/oop-iframes/)、service worker、shared worker 或扩展页面。

附加到一个目标对象会创建会话。通过该会话发出的命令会影响这个目标对象，其事件也会通过同一个会话返回。

Chrome 使用 [Site Isolation](https://www.chromium.org/Home/chromium-security/site-isolation/) 将不同站点的页面隔离在不同渲染器进程中。当一个页面嵌入跨站 iframe 时，Chrome 可能将该框架提升为进程外 iframe。它看起来仍嵌套在页面内，但 CDP 可能会将它暴露为另一个拥有独立会话的目标对象。

**Worker** 会增加更多分支。专用 worker 在页面主线程之外运行 JavaScript；shared worker 和 service worker 则可以比单个页面存活更久。CDP 将这些环境表示为目标对象或执行上下文，客户端因此能在执行代码或监听事件时准确定位到正确位置。

**导航**会再次改变这棵树。加载新文档会销毁框架旧的 JavaScript 执行上下文，并创建新的上下文。即使标签页和框架 ID 看起来没有变化，之前上下文中的对象 ID 或引用也会失效。

CDP 客户端必须跟踪结构和生命周期：存在哪些目标对象、附加了哪些会话、每个框架属于哪些执行上下文，以及它们何时消失。

现代页面表面上可能只是一个标签页，底层却是不断变化的一组进程和 JavaScript 环境。这正是为什么在其上层构建系统如此困难。

你可以为每个目标对象打开独立的 CDP 连接，但很快就会难以管理。扁平模式会将这些连接多路复用到单个连接上，并用 `sessionId` 标识每个会话。要正常工作，客户端必须发现目标对象、在恰当时机附加、将消息路由到正确会话，并在目标对象消失时恢复处理。

# CDP 暴露了浏览器的哪些部分？

CDP 从页面外部与浏览器通信。这个位置使它能够观察到更多东西，例如渲染器、网络栈、输入系统、worker、存储和调试器。

![图片展示了CDP（Chrome DevTools Protocol）与浏览器各部分的交互关系。CDP作为核心，连接着Network、Runtime、Input、Targets、Tracing、Storage等模块。Network模块可观察文档请求等；Runtime模块可执行脚本；Input模块可触发鼠标事件；Targets模块可连接目标；Tracing模块可开始跟踪；Storage模块可获取Cookies。这些模块通过CDP与浏览器各部分交互，共同实现对浏览器的控制和调试功能。](https://feishu.cn/file/PbDcbgKLBozq4QxMd9ycQTr6nae)

## 网络流量

Network 域可以观察文档请求、脚本、图片、API 调用、重定向、缓存命中和 service worker 活动。

一项请求通常会依次经过 `Network.requestWillBeSent`、`Network.responseReceived` 和 `Network.loadingFinished`。这些事件共享 ID，因此客户端可以重建完整生命周期，然后调用 `Network.getResponseBody`。

一次可见的页面加载可能涉及多个框架、重定向、预检请求以及数百个资源。

## JavaScript 执行

Runtime 域执行代码，并报告控制台调用、异常和执行上下文。执行上下文很重要，因为代码并非在单个永久环境中运行。框架和 worker 各自拥有上下文，但导航会销毁它们。

## 浏览器输入

Input 域通过浏览器的输入系统发送鼠标、键盘、触控和拖拽事件。

这比在元素上调用 JavaScript 方法更底层。但它仍不会决定该点击什么、不会等待布局稳定，也不会检查覆盖层是否挡住目标。

浏览器级输入也无法让自动化与真人操作无法区分。它只是让客户端控制 Chrome 的输入路径，仅此而已。

## 跟踪与诊断

`Performance.getMetrics`、`Tracing.start`、控制台事件、异常事件、截图和录屏，暴露的能力与 DevTools 中可用的能力相同。

一次失败的浏览器运行本身就携带解释：可能是停滞的请求、发生导航的框架、触发的异常，或显示时间消耗位置的跟踪记录。

CDP 将浏览器变成一个可被完全观测的系统。

# 为什么直接执行原始 CDP 令人头疼

线格式很简单，难的是状态管理。

原始 CDP 客户端必须在有用事件到达前启用各个域；在导航创建和销毁目标对象与执行上下文时持续跟踪它们；还要协调跨多个域并发竞速的响应和事件。

参考文档解释了消息形状，却跳过了真实客户端所需的生命周期细节：一个会话能存活多久？什么会杀死它？导航会保留它吗？另一个 WebSocket 能复用它的 `sessionId` 吗？

一个优秀客户端必须在目标对象、会话和上下文出现、消失时持续跟踪它们，通常此时仍有命令在执行中。我们不得不通过强制导航与崩溃、记录每个事件、观察哪些部分存活下来，亲自发现这些规则。

![图片展示了CDP中对象生命周期的示意图。导航操作后，Connection、Target、Session、Domains对象存活，JS Context和DOM Nodes对象被导航销毁。图中用不同颜色区分存活和被销毁的对象，绿色代表存活，红色代表被销毁。该图与上下文紧密相关，直观呈现了导航操作对CDP中各对象生命周期的影响，帮助理解在目标对象、会话和上下文出现、消失时，对象的存活与销毁情况。](https://feishu.cn/file/WymrbKsEiohgetxCE8pcb3C4ndf)

Chrome 自身也在不断变化。稳定、实验性和已废弃的方法会同时存在于协议中。

此外还有策略问题：CDP 可以向某个坐标发送鼠标事件，却无法决定哪个元素值得点击，也无法判断结果是否算成功。

这就是 Playwright 和 Puppeteer 等库存在的原因。它们处理等待、目标定位、生命周期状态与交互策略，并在你需要更底层能力时暴露 CDP 会话。

## 协议的边界

CDP 属于 Chromium，也只属于 Chromium。Firefox 和 WebKit 都提供不同的调试接口（[Firefox 已在 2024 年废弃 CDP](https://fxdx.dev/deprecating-cdp-support-in-firefox-embracing-the-future-with-webdriver-bidi/)）。[WebDriver](https://www.w3.org/TR/webdriver/) 提供跨浏览器自动化标准；[WebDriver BiDi](https://w3c.github.io/webdriver-bidi/) 为该模型增加双向事件。CDP 能够更深入地进入 Chromium，是因为 Chromium 同时控制协议两端。

调试连接的能力也强大到足以带来风险：它可以检查页面、执行任意 JavaScript、读取网络流量，并控制已经认证的会话。

[主干最新版协议](https://chromedevtools.github.io/devtools-protocol/tot/)会随 Chromium 变化。生产客户端需要选择支持哪些版本，并处理方法缺失的情况。

## 浏览器的控制接口

人类使用语言彼此沟通，程序使用协议彼此沟通，智能体则使用 CDP 与浏览器沟通。

通过一套协议，你可以导航页面、观察请求、执行 JavaScript、检查 worker、发送输入、收集跟踪记录，并追踪每个目标对象。建议使用能让这些能力更易用的高层[工具](https://github.com/browserbase/stagehand)。

你大概不应该基于原始 CDP 构建每一次交互。但理解它的工作方式及合适的抽象，能帮助你决定如何让智能体访问网络。

→ Kyle

---

想阅读带交互组件的版本，请查看[原文](https://www.browserbase.com/blog/what-is-cdp)。