# 别再给AI送钱：10款开源工具省80%Claude Code Token，大项目直接砍49倍

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/Z3PT3B5W9stoC-WN8YrUZQ

---

## 摘要

在此之前零散介绍过一些项目节约token： [用Claude Code啃大代码库太费token。winkrun winkrun 在小说阅读器读本章 去阅读 用Claude Code或者其他AI编码工具的人，大多碰过两个问题：要么半个月就用完月度额度，要么API账单超预期。很少有人意识到，你花的钱里80%都浪费在了冗余输出、重复读取全代码库、没用的命令日志和堆叠的对话历史上。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

用Claude Code或者其他AI编码工具的人，大多碰过两个问题：要么半个月就用完月度额度，要么API账单超预期。很少有人意识到，你花的钱里80%都浪费在了冗余输出、重复读取全代码库、没用的命令日志和堆叠的对话历史上。

在此之前零散介绍过一些项目节约token：

[用Claude Code啃大代码库太费token？这个开源工具砍了92%工具调用](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461159740&idx=1&sn=c88b25f893df2b8862679dfb3043a0b5&scene=21#wechat_redirect)

[tokens烧钱太快？试试这个四层模型组合](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461159312&idx=1&sn=c1ff8e15e3bf735d09c0e8e368c7a6bc&scene=21#wechat_redirect)

[像原始人一样和AI对话，费用可直接砍掉40%](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461156573&idx=1&sn=afdb8f293e81b4f9bf70826599366dce&scene=21#wechat_redirect)

近期社区博主Charly一次性整理出10款专门解决这个问题的开源工具，适配几乎所有主流AI编码工具，最高能把大项目的Token消耗砍到原来的1/49。

一、输出压缩类：直接砍AI废话的Token

最容易见效的类别，不需要改工作流，装完直接生效。

#### 1\. Caveman

Slogan是"why use many token when few do trick"，核心是让AI砍掉所有冗余套话，只输出核心内容，实测平均减少65%输出Token，最高到87%，技术准确率100%，同时响应速度快3倍。

举个实际对比：

- 普通Claude回答React重渲染问题：69Token，包含"我来帮你看""这是常见问题"之类的套话
- Caveman模式下：19Token，直接给原因和解决方案"New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

实测基准：

| 任务 | 普通Claude Token | Caveman Token | 节省比例 |
| --- | --- | --- | --- |
| 解释React重渲染Bug | 1180 | 159 | 87% |
| 修复Auth中间件Token过期 | 704 | 121 | 83% |
| Debug PostgreSQL竞态条件 | 1200 | 232 | 81% |
| 实现React错误边界 | 3454 | 456 | 87% |

额外功能：支持一键生成符合规范的短Commit信息、单行PR评论、压缩项目文档，还能统计累计节省的Token和对应美元金额。

支持30+AI工具：Claude Code、Cursor、Windsurf、Copilot、Gemini等，安装一行命令搞定：

```bash
# macOS/Linux/WSL
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

仓库地址：http://github.com/juliusbrussee/caveman

### 二、命令输出过滤类：砍终端冗余日志的Token

AI编码工具执行命令时，会把所有输出全部塞进上下文，大部分是没用的进度条、重复日志、boilerplate，这部分占了日常Token消耗的大头。

#### 2\. RTK (Rust Token Killer)

Rust写的高性能CLI代理，无依赖，启动overhead不到10ms，自动过滤所有命令的冗余输出，实测30分钟的Claude Code会话，总Token从11.8万降到2.39万，省80%。

工作原理：

```
Without rtk:                                    With rtk:

Claude  --git status-->  shell  -->  git         Claude  --git status-->  RTK  -->  git
  ^                                   |            ^                      |          |
  |        ~2,000 tokens (raw)        |            |   ~200 tokens        | filter   |
  +-----------------------------------+            +------- (filtered) ---+----------+
```

30分钟会话实测Token节省：

| 操作 | 标准Token | RTK优化后Token | 节省比例 |
| --- | --- | --- | --- |
| ls/tree | 2000 | 400 | 80% |
| cat/read | 40000 | 12000 | 70% |
| grep/rg | 16000 | 3200 | 80% |
| git status | 3000 | 600 | 80% |
| git diff | 10000 | 2500 | 75% |
| cargo test/npm test | 25000 | 2500 | 90% |
| 合计 | ~118000 | ~23900 | 80% |

核心优化场景还包括构建/Lint输出、云服务/容器命令等，平均省80%。支持13款AI编码工具：Claude Code、Cursor、Copilot、Windsurf、Gemini CLI等，安装后自动挂钩，不需要手动改命令，一行安装：

```bash
brew install rtk
# 或Linux/macOS通用
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

隐私方面：默认关闭遥测，不会收集任何代码、文件路径、命令参数。  
仓库地址：http://github.com/rtk-ai/rtk

### 三、代码库上下文优化类：砍大项目、Monorepo的无效Token

这是浪费最严重的场景：AI处理大项目时，每次任务都会重读整个代码库，99%的内容和当前任务完全无关。

#### 3\. Code Review Graph

核心是用Tree-sitter把整个代码库解析成结构图谱（节点是函数、类、导入，边是调用、继承、测试关联），每次任务只给AI传和当前需求相关的代码，不是全库读取，实测平均减少8.2倍Token，Next.js monorepo 27732个文件，只需要读15个，省49倍Token。

![优化前后Token对比](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJiciaT2Oxl3SvicVcuva5uKasUBTc4vh6ia9Tc3q0cu5yBCQ0lfLgJmGr5VrvX693LTmv02DMFibK2NZPRmmvOTcEtrmDlkibUp3M8PU/640?wx_fmt=png&from=appmsg)

核心功能：

- 爆炸半径分析：改一个函数，自动追踪所有相关的调用方、依赖、测试文件，只给AI传这些内容
- 增量更新：每次文件保存、Git提交，只重解析改动的文件，2900个文件的项目更新不到2秒
- 支持24种语言+Jupyter笔记本：覆盖Python、TypeScript、Go、Rust、Zig等主流语言，还支持Nix配置、Perl XS文件

![Monorepo Token优化漏斗](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJ8Ogkbc7LsmkY6p9hfThmcmCTLwSZRSzJGpFbejz7bO1GiboicI6XEKz86TMiaCooiaGT8ic59FwB0SezPhpbLYSC6Vul1iaicjr91h4c/640?wx_fmt=png&from=appmsg)

实测基准：

| 项目 | 平均全量读取Token | 平均图谱优化后Token | 节省比例 |
| --- | --- | --- | --- |
| Gin | 21972 | 1153 | 16.4x |
| Flask | 44751 | 4252 | 9.1x |
| Next.js | 9882 | 1249 | 8.0x |
| FastAPI | 4944 | 614 | 8.1x |

支持14款AI编码工具，自动检测配置：

![支持的平台列表](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJicmvqHhyS5lmUUBqNTMEmsia1picAKS6JJz8znEOgE0wnO8Z1vo7RyqL6YBVxLyRFWkemhibaicS3oRNBRRVnKZGWaGo8ZbTYg9icDQ/640?wx_fmt=png&from=appmsg)

一行安装自动配置所有支持的平台：

```bash
pip install code-review-graph
code-review-graph install
code-review-graph build
```

仓库地址：http://github.com/tirth8205/code-review-graph

### 其余7款专项优化工具

剩下的工具针对特定场景，按需选用：

#### 4\. Context Mode

把原始输出存在本地SQLite，不占用上下文，日志和GitHub相关内容的上下文消耗减少98%，适合经常处理大量日志、GitHub Issue/PR的场景。  
仓库：http://github.com/mksglu/context-mode

#### 5\. Claude Token Optimizer

优化项目级提示词模板，把项目文档从11k Token压缩到1.3k，省90%，适合固定项目长期使用。  
仓库：http://github.com/nadimtuhin/claude-token-optimizer

#### 6\. Token Optimizer

扫描上下文里的隐形幽灵Token（比如看不见的格式字符、冗余标记），修复后能恢复10-30%的上下文空间，还能保护上下文质量。  
仓库：http://github.com/alexgreensh/token-optimizer

#### 7\. Token Optimizer MCP

给所有MCP工具加aggressive缓存和压缩，平均省95%以上的MCP相关Token，适合重度用MCP工具的用户。  
仓库：http://github.com/ooples/token-optimizer-mcp

#### 8\. Claude Context

Zilliz推出的混合向量搜索MCP，把整个代码库变成可检索的上下文，成本比直接传全库低40%，适合中等规模项目。  
仓库：http://github.com/zilliztech/claude-context

#### 9\. Claude Token Efficient

只需要往仓库根目录丢一个CLAUDE.md文件，就能强制AI输出严格简洁，零代码改动，适合不想装额外工具的用户。  
仓库：http://github.com/drona23/claude-token-efficient

#### 10\. Token Savior

按代码符号（函数、类）导航，不是读取整个文件，代码导航相关的Token消耗减少97%，还有持久内存功能，不用重复传上下文。  
仓库：http://github.com/mibayy/token-savior

### 场景选型指南

不用全装，根据自己的核心痛点选2-3个就行：

- 超大Monorepo/多仓库项目：Code Review Graph + Token Savior
- 日常大量执行终端命令（测试、构建、Git）：RTK
- 重度使用MCP工具、处理大量日志/GitHub内容：Context Mode
- 要快速见效、不想改现有工作流：Caveman + Claude Token Efficient

### 不用工具也能省Token的10个习惯

除了工具，调整使用习惯就能省至少50%的Token，很多人每天都在犯这些错误：

1. **编辑原提示词，不要发追问** ：每加一条新消息，AI都会重读之前所有的历史，第30条消息的成本是第1条的31倍，改原提示词点Regenerate，不要堆对话。
2. **每15-20条消息开新会话** ：有开发者统计，98.5%的Token都花在了重读旧对话历史上，会话太长的时候，让AI总结一下内容，复制到新会话里当第一条消息。
3. **批量提问不要分开发** ：三个问题分开发要三次加载上下文，合并成一条提问，省一半以上的Token，答案质量还更高，因为AI能看到完整的需求。
4. **重复用的文件传到Projects功能** ：不要每次会话都上传同一份需求文档、设计稿、规范，传到Claude的Projects功能里，缓存后不会重复消耗Token。
5. **设置好Memory和用户偏好** ：不要每次都写"我是前端开发，用React，要简洁的带注释的代码"，存到Claude的Memory里，自动应用到所有新会话，省每次的设定Token。
6. **关掉不用的功能** ：Web搜索、连接器、高级思考功能，不用就关，这些功能会给每条响应加额外的Token。
7. **简单任务用低成本模型** ：语法检查、格式调整、brainstorm、翻译这些简单任务，用Claude Haiku就行，成本比Sonnet低75%，比Opus低90%。
8. **分散工作时间** ：Claude的额度是滚动5小时计算的，不是按天重置，不要集中一上午用完，分成上午、下午、晚上三个时段用，额度自动恢复。
9. **高峰时段外跑重任务** ：Anthropic在高峰时段会更快消耗你的额度，跑大的重构、全库扫描这类重任务，选晚上或者周末，非美国用户注意换算时差，避开美国的工作高峰。
10. **开超额使用当安全网** ：Pro、Max用户可以在设置里开超额使用，设好月度上限，不会在关键工作的时候突然断额度，也不会超预算。

这些工具全都是MIT协议开源，本地运行，没有云依赖，不会泄露代码，很多开发者用了之后直接从Claude Max套餐降到Pro，每月省几百刀。

社区里有用户反馈，坚持用这些工具和习惯，几乎再也碰不到额度上限，那么省下来的额度怎么办呢？

再介绍一个项目Local LLM Proxy，可以利用他们贡献出来，存下来下个月使用，我为人人，人人为我，都不再为token使用太多触发限额发愁，也不再为这几天没有使用token额度浪费而可惜。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJib50k5JOKibibrrY3TICg7CXJUxMJAwYl6l4xkDjrHssiakicXhaTLqNtu37MEUicUlrnWppbdvUPxN6SdChRv1X4FdB49icuEe0Bszk/640?wx_fmt=jpeg)

跨时间，跨区域，跨模型复用，做到AI时代的新互助社区。对这个项目感兴趣的也可以进群讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJ9BG9XxIYQXem0JibQ9onF5443HxhpWuaV50DlV2PIwVPuFoR2Ice6YM1DFsq3Cx1WBsuu2hsIbNI1YOZFlxAWfIFPWMKib0xvCc/640?wx_fmt=jpeg)

地址：https://github.com/wink-run/local-llm-proxy

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过