# 如何构建 Claude Research Agent：自动抓取全网资讯生成日报

**来源**: https://waytoagi.feishu.cn/wiki/T1wuwpfRZiC0vhkgPfMc2v45nxb

---

## 摘要

本文介绍了如何构建Claude Research Agent以解决每天浏览无效信息浪费时间的问题。该Agent每天早晨自动执行来源监控、信号过滤、综合分析和投递四项功能，将45分钟的信息搜集缩短为5分钟阅读。其技术架构由Claude、Filesystem MCP、Brave Search MCP、n8n和CLAUDE.md五个组件构成，协同实现在Obsidian库中自动生成结构化且贴合个人需求的每。

---

## 正文

<quote-container>
原帖链接：https://x.com/cyrilXBT/status/2058749052712276332
</quote-container>



大多数人每天开始工作的方式都一样。
他们打开 Twitter，用 20 分钟刷过一堆噪声，只为了找到真正重要的三件事。他们打开邮箱，还没做任何原计划中的事，就已经被拖进被动响应模式。他们查看 RSS 阅读器，看见 200 条永远读不完的未读内容，只觉得不知从何开始。他们打开新闻聚合器，读了三篇与自己工作或生活毫无关系的文章。
45 分钟后，他们落后于计划，压力更大，掌握的信息却并不比多睡 15 分钟更有价值。
Claude research agent 可以长期解决这个问题。
每天早晨，在你打开任何信息源之前，一个 Claude agent 已经读完与你工作相关的重要来源，过滤掉无关内容，综合真正值得了解的新动态，并将一份结构化、5 分钟可读完的 brief 放进你的 Obsidian库。
你醒来，读完 brief。五分钟内，你已经知道今天需要知道的内容，然后直接开始工作。
本文会从零开始，完整搭建一个能在每天早晨自动为你生成简报的 agent。
## Research Agent 实际会做什么
进入技术搭建前，先弄清楚你要构建的是什么，以及每个组件为什么重要。
Research agent 每天早晨会自动执行四项功能。
**来源监控。** 它读取你配置的每一个信息源：行业新闻、竞争对手网站、所在领域的学术论文、指定 newsletter、发布研究内容的 YouTube 频道、播客文字稿、你关注的 GitHub 仓库、所在细分领域的 Reddit 社区，以及任何可能出现在工作中的关键信息来源。
**信号过滤。** 它不会把读到的一切都压缩一遍。它会按照你定义的标准，识别什么内容真的重要。竞争对手推出新产品属于重要信号；一篇复述上周同样信息的 博客文章则不重要。过滤层决定了这份 brief 是否真正有用，而不是所有信息的缩短版。
**综合分析。** 它不会把重要事项只是列成项目符号，而是组织成结构化叙述，告诉你发生了什么、为什么重要、它如何连接到你已经知道的事情，以及你可能应当怎样应对。
**投递。** 它会在每天设定时间，把 brief 放到 Obsidian库的指定位置，在你打开电脑时它已经等在那里，而不是要求你手动触发。
这四项功能会把每天 45 分钟的信息搜集，替换成 5 分钟的阅读。

## 技术架构
Research agent 由五个组件组成。每个组件都有特定职责；去掉任意一个，系统产出的结果都会变差。
**Claude** 是智能层。它读取来源中的原始信息，用你的标准过滤重要内容，再把过滤后的信息综合成结构化 brief。
**Filesystem MCP** 将 Claude 连接到你的 Obsidian 库。它为 Claude 提供对库的直接读写权限，使其能够读取 `CLAUDE.md` 获取内容，并自动将 brief 写入正确的文件夹。
**Brave Search MCP** 让 Claude 能访问实时网络搜索。没有它，Claude 只能基于训练截止时间前的信息进行推理；有了它，Claude 就能搜索实时网页，获取你指定主题的最新信息。
**n8n** 负责调度整个工作流。它在每天你配置的时间触发 research agent，将正确的内容传给 Claude，接收输出，并把内容保存到库。
**CLAUDE.md** 是 背景层，它让 brief 与你的具体处境相关，而不只是泛泛地提供信息。它告诉 Claude 你在做什么、你关心什么、你已经了解什么，以及哪些信息对你确实可行动。
## 搭建基础环境
构建 工作流 前，需要先准备三样东西。
**带 MCP 连接的 Claude Desktop。**
从 [<text underline="true">claude.ai/download</text>](https%3A%2F%2Fclaude.ai%2Fdownload)安装桌面端 Claude 。
在 `claude_desktop_config.json` 中配置 Filesystem 与 Brave Search MCP servers：
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/your/obsidian/vault"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-brave-api-key"
      }
    }
  }
}

```

在 [<text underline="true">brave.com/search/api</text>](https%3A%2F%2Fbrave.com%2Fsearch%2Fapi)<text underline="true"> </text>获取 Brave Search API key。免费层每月允许 2,000 次查询，对每天运行一次的 research agent 来说已经足够。
保存配置后，重启 Claude。让 Claude 搜索某项内容，确认它能返回实时结果，以此验证连接已生效。
**你的 Obsidian 库结构。**
如果库中还没有 `BRIEFINGS` 文件夹，请创建一个。每天早晨的 brief 都会投递到这里。
```plaintext
vault/
  BRIEFINGS/
    [YYYY-MM-DD]-morning-brief.md  ← 每日自动生成
  CLAUDE.md
  [vault 中的其他内容]

```

**自托管 n8n。**
在每月 5 美元的 DigitalOcean droplet 上自托管 n8n，可以获得无限工作流运行，不按单次执行收费。
如果你还没有设置 n8n，请按以下顺序进行：创建 DigitalOcean 账号，启动最小配置的 Ubuntu droplet，通过 SSH 登录，用 npm 安装 n8n，并将其配置为 service 运行。
第一次完整设置 n8n 大约需要 30 分钟。之后构建的每一个 工作流 都可以复用同一套基础设施。
## 编写 CLAUDE.md 中的research context
`CLAUDE.md` 决定 brief 是否真正针对你本人。
通用 research agent 只会生成通用 brief。加入你个人具体背景的 research agent，会让每个条目都直接关联你的工作和决策。
在现有 `CLAUDE.md` 里加入 `Research Context` 章节，或在 vault 中创建一份专用的研究 `CLAUDE.md`：
```markdown
# Research Agent Context

## 我是谁
[你的名字、角色、所做的工作]

## 我的主要关注领域
[列出你需要保持了解的具体主题、行业或领域]

## 对我来说什么算重要新闻
[要具体。不要只写 “AI news”，而要写 “Claude Code updates、
新的 MCP servers、multi-agent frameworks、
AI agent security developments”]

## 我的竞争格局
[你监控的具体公司、人物和产品]

## 我已经非常熟悉的内容
[你有深厚经验的主题，因此只需要真正重要的新动态，
不需要入门级覆盖]

## 我目前正在做什么
[相关新闻可以直接转化为行动的活跃项目 - 每周更新]

## 我信任的来源
[值得优先处理的具体 publications、newsletters、researchers、
YouTube channels、subreddits]

## 我明确不想看到的内容
[在你的领域里经常出现，但会浪费时间的主题，
例如泛泛的 AI 炒作文章、重复内容、
你并不关心的公司公告]

## Brief 格式偏好
[你希望输出怎样组织 - 参见下方模板]

```

`我明确不想看到的内容` 是大多数人都会跳过、但最重要的章节。
没有它，Claude 会纳入所有与主题稍微相关的内容。有了它，Claude 就能更积极地过滤，brief 中只保留你真正可能采取行动的信号。
## Research Agent Prompt
这是每天早晨运行的核心 prompt。把它作为发给 Claude API 的 message，放进 n8n 工作流 中。
```plaintext
你是我的个人 research agent。你的任务是生成我的晨间情报简报。

读取我 vault 中 CLAUDE.md 里的 research context。

然后执行以下研究流程：

步骤 1：主要主题搜索
针对 research context 中的每个关注领域，搜索过去 24 小时内的重要动态。

以下 search queries 可作为起点，但请根据你发现的内容动态调整：
[Claude 将依据 CLAUDE.md 中的关注领域生成合适查询]

步骤 2：信号过滤
对你找到的所有内容，应用以下过滤规则：

纳入：
- 我关注的公司或工具发布的新产品或重大更新
- 会改变我们对某个关注主题理解方式的研究发现
- 我监控的竞争对手采取的战略行动
- 会影响我所在领域的监管或政策变化
- 值得了解的新工具、framework 或技术
- 我关注领域中的重大市场变动

排除：
- 我在 “我明确不想看到的内容” 章节中注明的任何内容
- 复述 48 小时以前发布信息的二次内容
- 没有新增信息的观点文章
- 我不关注的公司发布的公告
- 缺乏具体可行动细节的泛化 AI 炒作

如果某个分类中没有发生重要事情：
请直接说明没有重要动态，而不要为了填充篇幅加入内容。

步骤 3：竞争情报
专门搜索我在竞争格局中列出的公司和人物相关新闻。

突出显示代表战略转变、新产品或重大公告的内容。

步骤 4：综合输出
严格按照以下格式生成 brief：

---
# 晨间简报 - [DATE]
生成时间：[TIME]

## 今天最重要的一件事
[今天最重要的单项动态。用一个段落说明。
解释为什么它对我的具体情况重要。]

## 发生了什么
[3-7 个重要事项，每项包含：]
- **[来源/公司/主题]**：发生了什么，以及为什么与我的工作有关。
  最多一到三句话。

## 竞争动态观察
[竞争格局中出现的任何重要行动。
如果没有值得注意的内容，写 “今天没有重要动态。”]

## 可采取的行动
[根据今天的动态，列出 1-3 个值得考虑的具体行动。
只有真正可行动时才包含。没有必要行动时跳过本节。]

## 深入阅读
[与今天首要事项相关的 2-3 篇重要完整文章链接]
---

重要格式规则：
- 整份 brief 应该在 5 分钟内读完，而不是 15 分钟。
- 每一项必须直接对应 research context 中的某个内容。
- 不要填充句，不要闪烁其词。某件事重要，就明确说明它为何具体重要。
- 如果当天新闻平淡，请直接说明，不要把稀薄内容写得很膨胀。

将 brief 保存至：BRIEFINGS/[YYYY-MM-DD]-morning-brief.md

```

## 构建 n8n 工作流
n8n 工作流包含五个节点。每个节点在整个流程中执行一项特定职责。
**Node 1：Schedule Trigger**
将 trigger 设置为你偏好的晨间时间。对大多数人而言，早上 6 点很合适，因为 brief 会在你打开笔记本电脑前准备完成。
根据你的 时区 配置 cron expression：
```plaintext
0 6 * * 1-5    # 周一至周五早上 6 点
0 6 * * *      # 每天早上 6 点，包括周末

```

**Node 2：读取 CLAUDE.md**
这个 node 使用 Read File operation，从 vault 中正确路径读取你的研究 `CLAUDE.md`。
输出：`CLAUDE.md` research context的完整文本。
**Node 3：准备 API Request**
这个 node 构造发送给 Claude 的 API call，将 research 提示词模版 与 Node 2 读出的 `CLAUDE.md` 内容组合起来。
```javascript
const claudeMd = $node["Read CLAUDE.md"].json.content;
const today = new Date().toISOString().split('T')[0];
const time = new Date().toLocaleTimeString();

const systemPrompt = `你是一个个人 research agent。
今天日期为 ${today}，当前时间为 ${time}。
你可以通过 Brave Search MCP 访问实时 web search，请充分使用。

用户 CLAUDE.md 中的 research context：
${claudeMd}`;

return {
  model: "claude-opus-4-5",
  max_tokens: 4096,
  system: systemPrompt,
  messages: [{
    role: "user",
    content: "请按照 research context 中规定的格式与指令，生成我的晨间研究简报。"
  }]
};

```

**Node 4：Claude API 调用**
使用 HTTP Request node 调用 Anthropic API：
```plaintext
URL: https://api.anthropic.com/v1/messages
Method: POST
Headers:
  x-api-key: [YOUR ANTHROPIC API KEY]
  anthropic-version: 2023-06-01
  content-type: application/json
Body: [Node 3 的输出]

```

**Node 5：保存到 库**
使用 Write File node，把 Claude 输出保存到 `BRIEFINGS` 文件夹：
```plaintext
File path: /path/to/vault/BRIEFINGS/[date]-morning-brief.md
Content: [从 Claude API response 中提取的文本]

```

从 Claude API response 中提取文本内容：
```javascript
const response = $node["Claude API Call"].json;
const content = response.content[0].text;
const date = new Date().toISOString().split('T')[0];

return {
  filename: `${date}-morning-brief.md`,
  content: content
};

```

**可选 Node 6：Telegram 通知**
加入一个 Telegram bot 通知，在 brief 准备完成后触发：
```plaintext
Message: "晨间简报已准备完成：BRIEFINGS/[DATE]-morning-brief.md"

```

这样，当 brief 已投递后，你的手机就会收到通知。你甚至可以在起床前先在手机上读完它。
## 配置来源列表
Brave Search MCP 会自动处理开放网页搜索。但某些最有价值的信息源，并不能被标准 search 良好索引。
对于需要定点监控的来源，请将它们加入 `CLAUDE.md` research context，并写明具体指令：
```markdown
## 需要监控的具体来源

### 每日检查
- news.ycombinator.com - 检查首页中的 AI 与 developer tools 内容
- reddit.com/r/MachineLearning - 仅关注重要论文发布
- reddit.com/r/ClaudeAI - Claude 新功能与社区构建成果

### 每周检查
- arxiv.org/list/cs.AI - 本周发表的重要论文
- github.com/trending - 我的 tech stack 中的 trending repositories

### 警报级监控
[出现任何相关新闻都很重要的公司或人物]
- Anthropic blog: anthropic.com/news
- [Competitor 1] blog: [URL]
- [Competitor 2] press releases: [URL]

### 明确忽略的来源
[在你的领域中持续产生低信号内容的 publications 或 websites]

```

## 让 Brief 随时间越来越准的 反馈回路
如果你每次读完 brief 后用两分钟给 Claude 写下反馈，它会每周变得更好。
在每份 brief 底部加入你的 notes 章节：
```markdown
## 我对这份 Brief 的笔记
[你的标注 - 哪些有用、哪些是噪声、缺了什么]

```

每周日，在 Claude 中运行以下 prompt：
```plaintext
读取过去一周我 BRIEFINGS 文件夹里的所有晨间 brief，
并读取 “我对这份 Brief 的笔记” 章节中我的全部标注。

根据这些标注，更新我的研究 CLAUDE.md：
1. 持续产出有用信号的来源 → 加入 priority list
2. 持续产生噪声的主题 → 加入 Do Not Want 章节
3. 能够发现我指出的缺失信息的新 search queries
4. 我觉得有用的内容是否存在某些模式，应当被记录为明确偏好

在实际修改 CLAUDE.md 前，先向我展示拟议变更。

```

有了这个 反馈回路，到第三个月时，brief 对你的具体信息需求会比第一周校准得准确得多。
Agent 会从你的标注中学习你真正关心的内容，你无需手动持续微调配置。
## 进阶配置
基本晨间 brief 稳定运行后，你可以沿几个方向扩展系统。
**主题深挖**
当晨间 brief 出现重要动态时，把它加入 deeper research 队列：
```plaintext
DEEP-DIVE: [今天 brief 中的主题]

```

队列处理器会拾取它，并运行一次更全面的 research session，生成详细 analysis 笔记，而不是简短信息条目。
**竞争情报提醒**
配置一条独立的轻量 工作流，每四小时检查一次竞争对手新闻，而不是每天只运行一次。如果发现重要内容，它会立刻发送 Telegram 通知，而不是等到次日晨间 brief。
**每周综合分析**
每周日早晨，不生成标准日报，而是让 Claude 读取这一周的七份日报，生成周报：
- 本周最大的主题，以及它对你所在领域长期意味着什么。
- 最重要的单项动态，以及你应该怎样应对。
- 你原本预期发生、但实际没有发生的事，以及这意味着什么。
周报往往能揭示单份日报中无法看见的模式。
**按需研究**
将任意主题放进 `QUEUE` 文件夹，并加上 `RESEARCH` 前缀：
```plaintext
RESEARCH-quantum-computing-applications-in-finance.md

```

队列处理器 会对该主题运行一次深入 research session，将全面研究 brief 写入 `GENERATED`，无需等待晨间周期。
## 运行 30 天后会发生什么
Morning brief 从第一天起就会提供直接价值。
到了第二个月，复利效应会开始显现。
运行 30 天后，brief 已经依据你的具体标注完成校准。持续产生噪声的主题已经被移除，持续产出信号的来源获得优先级。五分钟阅读时间里包含的真正可行动信息，会明显多于第一周。
运行 60 天后，周报会开始揭示任何单份 brief 中都看不见的模式。在八周数据中，日常快照里隐藏的趋势开始浮现。
运行 90 天后，你拥有的是一套研究运作系统：它对你所在领域的理解，接近一位已经连续三个月为你提供 briefing 的专职分析师。
这种信息优势会每周累积。
你的竞争对手仍然每天早晨花 45 分钟在噪声中滚动浏览。
你只花 5 分钟读取信号。
差异不只是省下来的时间。
而是随着时间持续积累、基于更好信息做出的更高质量决策。
这个周末把工作流建起来。
第一份 brief 会在周一早晨运行。