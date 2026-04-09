---
url: https://mp.weixin.qq.com/s/MtyRSS1Es6XcdcbiTs1frQ
title: "Claude Code/OpenClaw联网工具全攻略，一文梳理15个Agent搜索神器"
description: "Agent联网大全。"
author: "鲁工"
coverImage: "https://mmbiz.qpic.cn/sz_mmbiz_jpg/MHVsz9lwuhVqJJyNvWWMxgicqyBswicjDESryialhN7KZiaow4l9ibn58XEzEnY5jgK2cEB5vWicGqe3OpvL3VObaGutsVAfknibgibH0rA0mR0SaZ4/0?wx_fmt=jpeg"
captured_at: "2026-03-16T07:40:26.699Z"
---

# Claude Code/OpenClaw联网工具全攻略，一文梳理15个Agent搜索神器

大家好，我是鲁工。

在使用Claude Code或者OpenClaw等AI Agent工具时，无障碍联网搜索和抓取是一个基础且必备的关键能力。

但无论是Claude Code，还是OpenClaw，自带的联网搜索工具也才勉强够用，在很多刚需场景下（比如抓取X的帖子），自带的工具经常会失败。

上周，我们发了两篇关于Claude Code联网搜索和数据抓取的文章，一篇是Agent-Reach，一篇是Apify，读者反响不错：

关于Agent联网查询这方面，我前前后后折腾了14个联网相关的工具，踩了不少坑，今天一次性的分层次整理给大家。

## 0 内置工具：WebSearch和WebFetch

Claude Code自带两个联网工具，很多人其实不知道它们的区别。

WebSearch负责搜索，你给它一个关键词，它返回一堆链接和标题。输出很轻量，只有title和url，不会给你正文内容。

WebFetch负责读网页，你给它一个URL和一个问题，它会把网页抓下来转成Markdown，然后用Haiku模型帮你总结出答案。这里有个坑，它内部会把内容截断到100KB，而且返回的是摘要，拿不到原始全文。

这两个工具配合起来，日常搜个文档、查个API用法，覆盖80%的场景没问题。

但是吧，碰到下面这些情况就搞不定：JavaScript渲染的页面（比如X/Twitter）抓不了，需要登录的站点进不去，动态加载的内容看不到，想拿结构化数据（比如表格）拿不到。

所以才有了下面这堆MCP工具的故事。

## 1 搜索层：四大搜索引擎怎么选

搜索类MCP工具我前后试过4个，各有特点。

**Brave Search MCP** 是很多人的第一选择，Anthropic早期也推荐过。它用的是Brave自己的独立索引，搜索质量相当不错，隐私保护也好。不过2026年免费政策变了，新用户每月只有5美元信用额度（大约2000次查询），不像以前那么大方了。

**Brave Search** MCP地址：

https://github.com/brave/brave-search-mcp-server

**Tavily MCP** 是我个人用得最多的搜索工具之一。它是专门给AI Agent设计的搜索引擎，除了搜索还集成了网页提取、站点地图和爬取功能，4合1。免费额度2000次/月，对个人开发者足够了。我觉得它最大的优势是搜出来的结果比较精准，尤其是技术文档类查询，比Brave更对味。无论是Claude Code还是OpenClaw， **Tavily MCP** 都非常实用。

**Tavily MCP地址：**

https://github.com/tavily-ai/tavily-mcp

**Perplexity MCP** 走的是另一条路。它搜完之后会用自己的大模型把结果消化一遍，返回给你的是整理好的答案加引用来源。2026年更新后提供了4个模型：Sonar标准版、Sonar Pro高级推理、Deep Research深度研究、Reasoning Pro复杂分析。而且标准版和Pro版不再对引用token计费了，相当于变相降价。适合需要深度研究的场景，实际上就是给Claude Code配了个专业研究助理。

**Perplexity MCP地址：**

https://github.com/jsonallen/perplexity-mcp

**Open-WebSearch MCP** 是免费党的福音。它聚合了Bing、DuckDuckGo、Brave、百度、Exa、GitHub、掘金、CSDN等多个搜索引擎，完全不需要API Key。缺点也很明显，基于爬取实现，稳定性一般，需要自己维护。

**Open-WebSearch MCP地址：**

https://github.com/Aas-ee/open-webSearch

建议排序：日常开发用Tavily，深度调研用Perplexity，预算敏感用Open-WebSearch，Brave Search作为备选。

## 2 阅读层：让Agent读懂全网内容

搜到链接只是第一步，怎么让Agent把内容完整读进来，这是第二个要解决的问题。

**Jina AI Reader** 是最老牌的方案。URL前面加个 `https://r.jina.ai/` 前缀就能把网页转成干净的Markdown，简单粗暴。它也有MCP Server版本，提供read\_url和search\_web两个工具。不过要注意，Claude Code对MCP响应有25K token的限制，超长页面会被截断。

![Image](https://mmbiz.qpic.cn/mmbiz_png/MHVsz9lwuhVSqVZ1mEzXUCeYgQvG9YcnwbDj6B0YFZpDicUdtJFbiaggVRv7KUib3UdoicOu4cfodyfFo0icHop1yzjztYicWWWmm9MFudd9QXV10/640?wx_fmt=png&from=appmsg#imgIndex=0)

**Jina AI Reader地址：**

https://github.com/jina-ai/reader

**x-reader** 是我最近发现的一个宝藏工具。它支持7个以上平台的内容获取：微信公众号、Telegram、X/Twitter、YouTube、B站、小红书、RSS，全都能读。底层集成了Jina Reader、Playwright、yt-dlp、feedparser这些工具，还有个很实用的功能，通过Whisper把视频和播客转成全文文字稿。

**x-reader地址：**

https://github.com/runesleo/x-reader

**Agent-Reach** 是OpenClaw生态里很火的一个skill，GitHub 6900+星。它的核心卖点就一个字：免费。不需要任何API Key就能访问X/Twitter、Reddit、YouTube、GitHub、B站、小红书等平台。安装之后先跑一下 `agent-reach doctor` 看看哪些渠道可用，很贴心的设计。这个我们上周专门写过，这里不详细展开了。

```javascript
channels/├── web.py          → Jina Reader     ← 可以换成 Firecrawl、Crawl4AI……├── twitter.py      → xreach            ← 可以换成 Nitter、官方 API……├── youtube.py      → yt-dlp          ← 可以换成 YouTube API、Whisper……├── github.py       → gh CLI          ← 可以换成 REST API、PyGithub……├── bilibili.py     → yt-dlp          ← 可以换成 bilibili-api……├── reddit.py       → JSON API + Exa  ← 可以换成 PRAW、Pushshift……├── xiaohongshu.py  → mcporter MCP    ← 可以换成其他 XHS 工具……├── douyin.py       → mcporter MCP    ← 可以换成其他抖音工具……├── linkedin.py     → linkedin-mcp    ← 可以换成 LinkedIn API……├── wechat.py       → camoufox+miku   ← 搜索+阅读微信公众号文章├── rss.py          → feedparser      ← 可以换成 atoma……├── exa_search.py   → mcporter MCP    ← 可以换成 Tavily、SerpAPI……└── __init__.py     → 渠道注册（doctor 检测用）
```

这三个工具定位不同：Jina Reader做单页面转换最稳，x-reader做全平台覆盖最广，Agent-Reach免费且零配置。建议x-reader和Agent-Reach两个都安装上， **Jina AI Reader功能其实在Agent-Reach已经包含了，所以可以不装。**

## 3 浏览器层：前端开发必备

搜索和阅读工具都搞不定的场景，就得上浏览器了。这一层工具最多，也最卷。

**Playwright MCP** 是Microsoft官方出品，28.7K stars，当之无愧的人气王。它最大的特点是用accessibility tree（无障碍树）代替截图来理解页面，只需要2-5KB的结构化数据，比截图方案快10到100倍。跨浏览器支持Chrome、Firefox、Safari，25+个工具覆盖导航、交互、截图、JS执行等。安装一行命令：

```nginx
claude mcp add playwright npx @playwright/mcp@latest
```

我个人觉得它最适合自动化测试和表单操作这类场景。而且它支持可见浏览器窗口，遇到需要登录的页面，你可以手动登进去，cookie会保持在整个session里。

**Playwright MCP** 地址：

https://github.com/microsoft/playwright-mcp

**Chrome DevTools MCP** 是Google官方出品，28.6K stars，和Playwright并驾齐驱，这个我们号创号第二篇文章就写了。它提供29个工具，分6大类：输入自动化、导航、设备模拟、性能追踪、网络分析、调试。和Playwright不同的是，它更偏向开发调试，能做性能trace分析、Lighthouse审计、网络请求检查、控制台监控（带source-mapped堆栈）。做前端开发的同学个人推荐这个。

**Chrome DevTools MCP地址：**

https://github.com/ChromeDevTools/chrome-devtools-mcp

**Chrome in Claude** 是Anthropic自己的官方方案，目前Beta阶段。通过Chrome浏览器扩展，Claude Code可以直接操控你的浏览器，共享你的登录状态。关键是它能读取浏览器控制台输出、录制交互GIF，甚至支持定时任务。不过有个限制，需要付费的Anthropic计划（Pro、Max、Teams或Enterprise）才能用。在Claude Code启动时添加--chrome命令即可：

```css
claude --chrome
```

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/MHVsz9lwuhVYWq3svDmyNAFrM9NxuQeUSh4C42iaibnevNtSzhcL9sics7cIib8NGfuRNQDiaMBKIT0OEx4jqqdFJPA7Mahlz3xpL1F0GRBNYQ5A/640?wx_fmt=png&from=appmsg#imgIndex=1)

**Agent-Browser** 来自Vercel Labs，19.6K stars，Rust实现的无头浏览器。它用reference-based targeting（@e1、@e2这种标记）代替CSS选择器来定位元素，稳定性比传统方案好不少。这个我们号之前也写过：

**BrowserWing** 走的是差异化路线，1.1K stars。它的亮点是可视化脚本录制，你在浏览器里操作一遍，它自动生成MCP命令或Skills文件。26个HTTP端点，支持MCP Server、Skills文件、内置AI Agent三种集成方式。对于重复性的浏览器操作，这个工具方便很多。

**BrowserWing地址：**

https://github.com/browserwing/browserwing

这五个浏览器工具按场景来分：自动化测试选Playwright，前端调试选Chrome DevTools，日常浏览选Chrome in Claude，追求性能选Agent-Browser，重复任务选BrowserWing。不过这几个工具功能多少有些重叠，看个人喜好选择就好。

## 4 采集层：结构化数据的大杀器

前面的工具都是拿文本内容的，如果你需要结构化数据（比如从某个平台批量抓取产品信息、用户评论），就需要Apify了。

**Apify Agent Skills** 提供12个预制技能，从万能爬虫ultimate-scraper到垂直场景的品牌监测、竞品分析、KOL发现都有。返回的是结构化的表格数据，支持CSV和JSON导出。

**Apify Agent Skills** 地址：

https://github.com/apify/agent-skills

**Apify MCP Server** 则是另一条路径，通过MCP协议接入Apify平台上15000多个现成的爬虫和自动化工具。配置也简单，托管远程服务器一行JSON搞定。不过要注意SSE传输会在2026年4月1号移除，届时需要切换到Streamable HTTP。

Apify按结果付费，适合有明确数据采集需求的场景。

## 5 建议按需配置

建议按需进行配置，推荐基本组合如下：

搜索用Tavily（精准） + Open-WebSearch（免费备选），阅读用Agent-Reach（免费多平台） + x-reader（组合优势），浏览器用 **Chrome DevTools MCP** （chrome官方出品）加Chrome in Claude（claude原生支持），采集按需开Apify。

这套组合基本上能够覆盖日常写文章调研、代码开发查文档、数据采集分析的所有场景。免费工具为主，付费工具按需。

14个工具看着多，但是按照"搜索、阅读、浏览器、采集"四层来理解就很清晰了。每层选1到2个趁手的，比全装一遍但都用不熟要强得多。

感谢您阅读我的文章。我是鲁工，九年AI算法老兵，AI全栈开发者，深耕AI编程赛道。感兴趣的朋友也可以加我微信（louwill26\_）交个朋友。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MHVsz9lwuhVHoC2oaSxvHo0abDZFiarFSK2ACKCtbEiaM7To6TEIqADmCtcvYneA30JicMhgMib75UIqVAPxWCg79hzkZ8PkZbJXK1rJ4ZibX8lA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

\>/ 作者：鲁工

作者提示: 个人观点，仅供参考

继续滑动看下一个

AI编程实验室

向上滑动看下一个