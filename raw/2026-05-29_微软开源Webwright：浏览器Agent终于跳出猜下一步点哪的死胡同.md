# 微软开源Webwright：浏览器Agent终于跳出"猜下一步点哪"的死胡同

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/LNbIX4v9zy2wQZlngyNiFg

---

## 摘要

微软开源了原生Web Agent框架Webwright。该框架跳出传统单步点击预测模式，直接让大模型编写可复用的Playwright自动化脚本。其架构极简，核心代码仅约1500行。Webwright在主流基准测试中达到了开源SOTA水平，且支持小模型低成本部署。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJicicKZmjrcgvp2SibYvo3wICpjiaQjvwdasuHaSTMdICPQnqWfDxVibhAZwt8kjytuVMPjic7er3ibCvRLbmXv4DOX8KTibo0LdCTricFw/640?wx_fmt=jpeg)

2026年5月，微软正式开源终端原生Web Agent框架Webwright，项目刚发布就引发了Agent开发社区的广泛讨论。

核心设计：完全跳出单步操作的旧模式

过去绝大多数浏览器Agent都走同一条路径：观察当前页面状态→预测下一步点击/输入动作→执行，每一步都要调用LLM做判断。这套设计在LLM能力较弱的时候确实有效，但随着模型写代码能力的提升，反而成了瓶颈。

Webwright的思路完全不同，更接近真实工程师做自动化的逻辑：

1. 让LLM直接编写可运行的Playwright脚本，把网页操作转化成可复用的Python程序
2. 所有状态（脚本、截图、日志）都存在本地工作区，浏览器会话是可以随时启动、检查、丢弃的运行环境，而非状态载体
3. 架构极简，核心只有三个模块共约1500行代码：Runner（150行）、Model Endpoint（550行）、Environment（300行），没有多智能体系统、没有图引擎、没有多余的插件层，仅依赖httpx、pydantic、playwright、typer四个库。

这种模式的直接好处是，Agent运行完任务留下的并非一次性操作痕迹，而是可直接修改、复用、分享的自动化脚本。

### 性能达到SOTA级别

Webwright在两个主流浏览器Agent基准测试上都拿到了当前开源框架的最好成绩，100步预算下的测试结果：

- Online-Mind2Web（300个真实网页任务）：用GPT-5.4达到86.7%的准确率，是同类开源 harness的最高水平；用Claude Opus 4.7也能达到84.7%，在难例拆分上甚至超过GPT-5.4（80.5% vs 76.6%）
- Odysseys（200个长程任务，平均需要76.1步）：用GPT-5.4达到60.1%的完成率，比之前的SOTA高出15.6个百分点，比用坐标预测的基线GPT-5.4高出26.6个百分点。

另外测试显示，哪怕是Qwen-3.5-9B这类小模型，配合预置的工具脚本，也能在Online-Mind2Web的难例上达到66.2%的完成率，适合低成本部署场景。

![Odysseys长程任务评测结果对比](https://mmbiz.qpic.cn/sz_mmbiz_png/rY5icXvTTrJic2Mukp2eVPNaQReIYnBPBnYADaed9qYwt8Ypq3vbialm1LNDic4MSVMoiajnaPCqJoFuoyYxRjMiaqEJHaqOB7oM1EyRoGacjoTJ4/640?wx_fmt=png&from=appmsg)

![Online-Mind2Web任务评测结果对比](https://mmbiz.qpic.cn/mmbiz_png/rY5icXvTTrJibibKs01gn4LhPU5uwLhnaTsmNKOgPP7CXInZaTfib9vV1wFQcE1fD2HIpQrKwPwjvNq0x2Rx23RJj1ULibmZOBYVWaO6Q5F1WLOM/640?wx_fmt=png&from=appmsg)

### 生态集成与附加功能

Webwright已经完成了主流Agent生态的适配，不用改现有工作流就能接入：

- Claude Code：直接通过插件市场安装，支持 `/webwright:run` （一次性任务）和 `/webwright:craft` （生成可复用的参数化脚本）两个命令
- OpenAI Codex：通过插件市场安装后，用 `@webwright` 就能直接调用
- OpenClaw、Hermes Agent：共用同一套skill目录，直接加载即可使用。

另外还有两个实用功能：

1. Task2UI模式：任务完成后自动把结果渲染成可交互的HTML应用，不用自己再做可视化
2. 全程可审计：每次运行的轨迹、截图、日志都会存在本地，方便调试和回溯。

### 和同类项目的核心区别

社区也有人提到Webwright和browser-use、agent-browser等项目的差异，官方给出的架构对比如下：

| 维度 | Stagehand (Browserbase) | agent-browser (Vercel) | browser-use | Webwright |
| --- | --- | --- | --- | --- |
| 范式 | 混合：代码+自然语言原语 | 供其他Agent调用的CLI工具 | 基于DOM快照的自主LLM循环 | 带终端的编码Agent，浏览器只是启动的运行环境 |
| 动作空间 | Playwright代码，或自然语言转译的Playwright | 离散子命令（打开、点击、截图等） | LLM选择的索引式点击/输入 | 自由格式Python，自己写完整Playwright脚本 |
| 状态载体 | 浏览器会话 | 浏览器会话 | 浏览器会话 | 本地工作区（代码、截图、日志），浏览器可丢弃 |
| 循环形态 | 命令式，需要时做多步操作 | 每个微操作调用一次CLI | 观察→预测动作→执行循环 | 写代码→执行→检查截图→修复代码 |

### 行业共识：Agent要跳出单步操作的局限

Webwright的设计思路在社区得到了广泛认同，不少从业者表示这才是浏览器Agent的正确发展方向：

- 有开发者指出，绝大多数自动化的瓶颈不在动作层，而在决策循环。Playwright点的已经足够快，真正的问题是该点什么。如果新工具能压缩这个决策 gap，就是完全不同的品类，如果只是重新包装一层CDP调用，最多是横向移动。
- FSB（Full Self Browsing）的作者Lakshman Turlapati表示，Webwright说明方向是对的：Agent不该只猜下一步点击，还要能把真实浏览器会话、DOM、截图、日志和恢复机制放进同一个控制层。FSB做的就是Chrome端的MCP层，让Codex、Claude、Cursor这类Agent能直接控制用户的真实Chrome，保留原有的cookie、扩展、登录态，同时做到敏感信息不泄露、多Agent tab隔离，适合处理收件箱分类、客服回复、数据拉取等需要登录态的重复工作。
- 还有开发者表示，Webwright本质就是面向浏览场景的编码Agent，自己之前手动用Copilot CLI+Playwright MCP搭过类似的工作流，现在终于有了更 streamlined 的官方方案，已经给OpenClaw和Hermes Agent装好了，用来收集AI编码的模式数据，提升Agent的编程能力。

### 快速上手

#### 基础运行

环境要求：Python 3.10+，Playwright安装的Chromium，对应后端的API密钥（OpenAI/Anthropic/OpenRouter）

```bash
# 安装
pip install -e .
playwright install chromium

# 运行示例任务
python -m webwright.run.cli \
    -c base.yaml -c model_openai.yaml \
    -t "Search for flights from SEA to JFK on 2026-08-15 to 2026-08-20" \
    --start-url https://www.google.com/flights \
    --task-id demo_openai \
    -o outputs/default
```

#### 作为Claude Code插件安装

```bash
# 添加插件市场
/plugin marketplace add microsoft/Webwright
# 安装插件
/plugin install webwright@webwright
```

### 相关链接

- Webwright GitHub仓库：https://github.com/microsoft/webwright
- Webwright官方博客：https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/
- FSB官方网站：https://full-selfbrowsing.com/agents
- FSB GitHub仓库：https://github.com/lakshmanturlapati/FSB

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过