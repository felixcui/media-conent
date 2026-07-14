# 让 Agent 按工程标准交付：AI Coding 下的质量关卡实践

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/P2FvwzXCrRka4n5kNKm_sA

---

## 摘要

针对AI Coding速度快但交付质量不高的问题，本文提出将质量检查嵌入Agent工作过程的“左移”策略。该策略首先建立Agent操作协议，将项目工程规范转化为必须遵守的执行规则并在关键时机触发验证；其次实现代码写完即审查，通过独立子Agent对照规则即时检查变更代码并输出问题报告，由主Agent修复后继续推进，从而有效提高上游交付质量并减少下游返工。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 无糖可乐

导读

introduction

把验证流程左移，通过前置的审查、运行时验证、视觉验证等系统化的能力建设，让 Agent 在开发过程中就能按项目的工程规范完成自检和修复，提高上游交付的质量减少返工。

*全文 5942 字，预计阅读时间 5 分钟*

**背景**

GEEK TALK

AI Coding 提升了开发速度，但速度快不等于交付质量高。Agent 写得快，也错得快——它不知道项目的工程约定，写完代码不会自己打开浏览器看一眼页面能不能跑。

传统的质量保障依赖提交后的人工 CR 和 QA 测试。但在 Agent 高频产出代码的场景下，所有问题都等后面环节才发现，协作成本只会更高。

所以我们做的事情是： ****把质量检查嵌入 Agent 的工作过程本身**** ，将验证流程左移，提高上游交付质量，减少下游的返工。

整条链路：

```css
Agent Operating Rules    定义操作协议，约束 Agent 在项目里怎么干活        ↓Code Validation          写完代码当场 CR，不等提交        ↓Runtime Verify           改了 UI 就连浏览器验证        ↓Figma To Verify          重点页面对设计稿做视觉走查        ↓Pipeline Code Review     提交后大规模复审        ↓问题结构化 → Agent 辅助修复 → 重新验证        ↓沉淀为 Skill / Rules，持续复用
```

下面按这条链路，逐个讲每个节点都做了哪些事情。

GEEK TALK

01

Agent Operating Rules：把工程规范变成执行协议

Agent 靠通用知识写代码，不知道项目自己的规矩。Prompt 是一次性的，聊完就丢。项目规则是长期的、稳定的、每个任务都要遵守的。

我们在项目根目录的rules下维护索引文件，作为 Agent 在这个项目里的操作协议，包含：

****渐进式加载规则。**** 不同类型的改动需要遵守不同的工程约定，比如状态管理的规范、业务统一的请求类封装、构建配置有多少地方需要同步修改。这些约定分散在各自的 rules 文件里，作为项目的私域知识，让Agent可以在执行了对应类型的任务的时候加载进来补充上下文。

****在关键时机触发验证 Skill。**** 协议里定义了两道门禁：

- 所有代码改动完成后，必须启动独立 subagent 执行 `code-validation` Skill 做即时 CR，不能被跳过，不能用 lint 或 build 替代。
- 如果任务涉及 UI（组件变更、样式修改、交互调整），必须通过 CDP 连接真实浏览器执行 `visual-verify` Skill。CDP 不可用时不能假装验证。

GEEK TALK

02

Code Validation：让Agent写完即 CR

传统 Code Review 环节发生在提交后，问题已经进入协作链路。但 Agent 开发时，很多问题可以在"刚写完"的时候立刻发现，没按约定的方式引入依赖、用了项目已经废弃的写法、新增代码和项目既有的工程约束冲突、改了一处配置但没同步关联的其他配置。而且因为有任务的上下文，这些问题的修复能够变得十分准确，而不需要去猜“当时代码为啥这样，我应该改成啥样”。

这些问题如果等到流水线 CR 才暴露，再经历修复带来的时间和修复成本都是更大了的。

**2.1 具体实现**

`code-validation` 是一个指导模型CR关注哪些内容的 Skill，提高开发阶段产出的代码质量。

```javascript
Agent 完成一批代码改动  ↓启动独立 subagent（不是主 Agent 自己检查）  ↓subagent 加载 rules.md（项目验证规则合约）  ↓只审查 changed lines + 必要上下文  ↓按 CR 风格输出问题报告（Error / Warning / Info）  ↓主 Agent 修复问题  ↓通过后才允许继续
```

这里用独立 subagent的原因，Agent会倾向给自己的代码打高分，独立 subagent 相当于切换视角，用新的上下文、站在 reviewer 的位置审查，减少"自己写的看着都对"的盲区。

**2.2 项目验证规则合约**

在skill中定义了这个项目里什么是对的、什么是错的，分两层：

****通用检查：**** 包括但不限于类型安全、生命周期、组件边界、错误处理等通用内容，同时让模型积极的探索其他可能存在的问题并报告。

****项目专属的阻塞规则：**** 这层规则对应的是团队自己的工程约定，比如用哪个 UI 库、样式写法是否符合规范要求、数据请求走哪个封装、多套构建配置之间怎么保持同步。针对每个特殊规则都附带了具体的判断标准和正确写法的示例告诉模型什么是对的。

**2.3 复用**

同一个 `code-validation` Skill 在两个场景下使用：开发期作为 Agent 的即时 CR，流水线上作为 Pipeline 项目特定的 Code Review 的规则注入，两边维护一套规则即可。

GEEK TALK

03

Browser Use：让 Agent 在真实浏览器里工作

代码没报错不等于页面没问题。页面打不开、弹窗被裁切、控制台报错、接口失败、布局在某些条件下塌陷了，只靠看代码是发现不了的。

所以我们做了 `visual-verify` ，让 Agent 通过 CDP 连接真实浏览器，在里面做 DOM 断言、截图、检查 console、给元素画标注框。

下面用三个真实案例讲这套能力怎么工作。

**3.1 能力基础：visual-verify skill**

visual-verify 使用 ****Contract 模式**** 工作：

1. Agent 用 JSON 描述期望的页面状态（哪些元素存在、可见、在什么位置、点击后发生什么）。
2. 先跑 `contract-lint` 做静态校验，避免格式问题浪费浏览器执行。
3. 再跑 `dom-assert` 在真实浏览器里执行断言。
4. 所有结果写入 `contract.md` 作为验收记录。

除了断言，还有几个关键能力：

- ****标注截图**** （annotate-screenshot）：在页面元素上画标注框并编号，用于空间问题的可视化诊断。标注框直接画在真实元素上，如果元素被裁切或遮挡，标注框也会被裁切，真实反映页面状态。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6mXhh7c7JTf29snCdrcRZ4T8NNJt9lYgLzKjVM7wq9kmdvLxMCN5rhbyP3Lrs7yPcjQIicukQnytUkZr851gpibxAfgKVMSr9qs/640?wx_fmt=png&from=appmsg)

## △ 截断的红框表明了元素无法完全展现

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5QnbQyju7xt2lY6xJEX4Cv7wzZ6ECHjUZP1dkqEpjopYz3dbENpMTvoJDFicoy6vCXcILeasmOBbz3ZNVhIvfKtz3Fvpyedbg4/640?wx_fmt=png&from=appmsg)

## △ 修复后红框完整，问题被解决

- **console 检查** （console-check）：监听 CDP 的 console 事件，捕获运行时错误。
- **Memory 机制** ：跨任务积累页面知识，稳定的选择器、已知的时序问题、可复用的检查脚本。新任务启动时先读 memory，避免重复探索。

### 3.2 案例一：快捷回复功能，Agent完成交互需求闭环

**背景：** 让 Agent 实现一个快捷回复功能，评论管理页面的回复框旁边加一个按钮，点击弹出面板，面板里有分类标签、搜索、短语卡片，点击短语回填到输入框。

Agent 写完代码后，按 Agent Operating Rules 的要求进入 visual-verify。接下来发生了三轮"发现问题 → 修复 → 再验证"的循环。

#### 3.2.1 第一轮：页面直接崩了

Agent 打开页面，看到的不是评论列表，而是 Error Boundary——"服务器开了小差，请稍后重试！"。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5NuUVL3BymsdYPZ3uA5daSuFWVCNz7xB4gMPjYDIb2TITvtTySuAFw0KByZ0PGadpAat1CKLDA8KwThKSGHKmdwRtGuXra8JE/640?wx_fmt=png&from=appmsg)

代码有运行时错误导致 React 组件树崩溃。Agent 通过 `console-check` 获取控制台错误信息，发现 `card/index.tsx` 里访问一个全局状态为 `undefined` ，Agent 迅速定位问题是访问与请求数据顺序错乱，快速完成了修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5hrVbictibibtQjRmut3BCOe8LVPVBgSJ5memsEpXTgyk4wiaib2xDMIeiaxXzt2CiaNM3BoaTZVK8UIyZVeWsTe7k7HcrKsYz3gWhdA/640?wx_fmt=png&from=appmsg)

## △ 修复后重新截图发现变成正常

不打开浏览器根本不知道页面已经崩了。在 Agent 开发场景下，如果没有浏览器验证这一步就会被直接跳过。

#### 3.2.2 第二轮：面板被 overflow:hidden 裁切

页面恢复后，Agent 点击快捷回复按钮，面板出现了，但上半部分被截断，搜索框和分类标签看不见，只露出短语卡片的下半截。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6ib7d2wKF8khfzlsU6TYOH53D24nexcv9XqH09Q3EHUPvBqykfD7x8ouJUicnWxLZK6hdYfM9BSRonb6DmfsZWnZRtpZGia03LibI/640?wx_fmt=png&from=appmsg)

Agent 用 `annotate-screenshot` 给面板区域画红色标注框，给回复框画蓝色标注框。截图上可以清楚地看到：面板的红框上半部分被父容器截断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7spHNtdiaFX7ywAsjzicmqJ1ibib2ShSGse1WGOAhpW32VByG8dFcI3FdM4APbRW5PicA8S9diaFAbeZePRxuHxL3yDPE2TYWMzIjjA/640?wx_fmt=png&from=appmsg)

面板定位在回复框上方，但是这个面板超出它上层元素的部分被裁掉。Agent 根据标注截图定位到具体的 DOM 层级和样式，修复后面板完整展示。

DOM 断言会告诉你"元素存在"，但不会告诉你"元素被裁切了一半"。标注截图的价值就在这里：把"看起来不太对"变成可定位的视觉证据。

3.2.3 第三轮：功能逻辑验证

布局问题修完后，Agent 继续验证全部功能点：

- 切换分类标签（"感谢类"→ 过滤出 2 条短语）✅
- 搜索关键词过滤 ✅
- 点击短语回填输入框（字数计数器 17/500，回复按钮变蓝）✅
- 最近使用区出现 ✅
- 添加短语弹窗 ✅
- 删除前二次确认弹窗 ✅
- localStorage 持久化 ✅
![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5uKGFjlqUoj0z1SflZX945hfvfKnaRscRgico8f0GNnPPiaoVHa3nqMcjD1nJr86AhE6HL3DKnvWI0ATeDz9NiaPs5dqfAYEcia0s/640?wx_fmt=png&from=appmsg)

最终输出 `contract.md` 验收记录，约定的checkpoint 全部通过。

3.2.4 小结

三轮验证分别抓到了三类问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6JP83HkEIZRYbmLibvnMpA2QIM3ibYVhV6zAzWIf2icA01tdEMIxaS9bbNrTTdIs6ugx1BpML2tS7dlP10Rl2aznQSP3yJV0aunk/640?wx_fmt=png&from=appmsg)

把验证前移到 Agent 写完代码的当下，问题在几分钟内闭环，不用等到后面的环节才暴露。

**3.3 案例二：RSpack HMR 调试，让Agent 独立完成工程诊断**

****背景：**** 项目用 RSpack + Module Federation 构建。开发中发现两个问题：修改文件后页面不更新；即便 HMR 生效了，每次增量构建也要 2 秒以上。

我只告诉 Agent 这两句话。它连接浏览器后，独立完成了全部定位和修复。

****HMR 不生效。**** Agent 在控制台看到 HMR 消息到达了但 UI 没变化。检查 React Refresh runtime 挂载情况后，发现 `ReactRefreshPlugin` 的 `library` 参数和 `output.uniqueName` 不一致，Refresh runtime 挂载到了错误的命名空间，组件静默跳过重渲染。对齐配置后修复。

****构建时间虚高。**** 控制台报 2400ms，但 Agent 查看计时插件源码后发现其中 1000ms 是人为加的防抖延迟。去掉防抖后真实数据是 480ms。

****真实耗时仍偏慢。**** 去掉防抖后继续排查，发现两个原因：SWC 的 polyfill 分析在 dev 环境下无意义但每次 HMR 都在执行；Module Federation 的 manifest 插件在每次增量构建时重新做资产分析。关掉这两项后，增量构建降到合理范围。

****顺带发现端口冲突。**** 排查过程中还发现 MF 的 `dts: { generateTypes: false }` 和 `dts: false` 语义不同——前者只是不写出类型文件，DTS 插件本身和它的内部 WebSocket server 仍然启动并占用端口。

最终优化效果：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7q65mDTkicsYGsD7P0m4xoLiaiaoBdESL8icm644CrMEX20vNicx5rrjPJJLL5SKVUyhuLevXYRbLpMaERicUs17t0r591kte5Bb0L4/640?wx_fmt=png&from=appmsg)

**3.4 案例三：Figma To Verify，把"感觉不像"变成量化问题**

3.4.1 问题

视觉走查是 QA 和前端协作中的老难题。设计稿和开发页面不是天然可比的——设计稿是局部，开发页是完整页面；图片、文案、数据都可能不同；直接截图做像素 diff 会产生大量无意义的红区。人眼走查能发现明显问题，但容易漏掉间距差 2px、字号差 1px 这种微妙差异。

我们想做的是： ****把视觉差异变成可确认、可量化、可标注的问题。****

3.4.2 整体流程

```css
Figma 设计稿  ↓  figma-to-html（将指定 Node 导出为高还原 HTML）设计稿 HTML 基准页  ↓  chrome-cdp（两个独立 Tab 打开设计页和开发页）  ↓  element-screenshot（只截取目标元素，排除无关内容）双页元素截图  ↓  vet-generator（生成 VET 并对齐颜色）6 张分析图（2 原始 + 2 VET + 2 Diff）  ↓  vet-investigation（识别候选问题）N 个候选问题  ↓  visual-issue-clarification（每个问题单独 subagent 复核、量化、标注）最终视觉走查报告
```

这条流程由 7 个 Skill 组合完成（chrome-cdp、element-screenshot、figma-to-html、vet-generator、vet-investigation、visual-issue-clarification、visual-diff 作为顶层路由）。下面讲其中三个关键技术点。

3.4.3 技术点一：VET，把动态内容抹掉，只留结构

VET（Visual Expression Tree）将页面中有语义的元素标记为纯色色块，文字、图片、图标等动态内容全部替换，只保留元素的位置、大小和层级信息。

为什么需要它？设计稿和开发页面之间存在大量内容差异：图片不同、文案不同、数据不同、DOM 结构也不同。直接对两张截图做 diff，红区几乎覆盖整个页面，没有任何可用信息。VET 把这些动态差异消除，让对比聚焦在布局和结构上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5QiaWic4EL41hjViaqia2hTtCLj11ceCjVUmGIvsBUs0JcQr6UPRTuDZkSAiadViaE69uEPpECRFG4ApI5S6gAagiasq88nyTopcoyh4/640?wx_fmt=png&from=appmsg)

## △ 原始截图DIFF，非常杂乱

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6swMibB8dXke2vQ3Ov3JFP71nxMSN7nvZxV9CDyd8mzIVb35PmzVIBXnib0rR9nhvVnRgEp4OrbWmuBULnwNnzAjvULUKx9x39s/640?wx_fmt=png&from=appmsg)

## △ VET的DIFF，更清晰的表达结构差异

#### 3.4.4 技术点二：VET 对齐，解决 DOM 深度不一致的问题

VET 的自动着色基于 DOM 深度：深度 7 是紫色，深度 14 是青色。但设计稿导出的 HTML 和实际开发页面的 DOM 结构完全不同。同一个视觉元素（比如一个卡片），在设计页 DOM 深度 7，在开发页因为多了 Provider、Layout 等包装组件变成了 14。直接用自动着色，同一个语义元素在两边颜色不同，diff 就会标为差异，这不是布局差异导致的，是 DOM 结构差异带来的噪声，应该被消除。

`vet-generator` 的解法：先只在设计页上跑自动 VET 建立颜色方案，然后由 Agent 分析两边 DOM、识别语义对应的元素，在开发页上手动注入相同颜色。这个过程是程序能力 + 浏览器操作 + Agent 语义理解的组合，不是纯算法能搞定的。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5rbb0ePicP6sm7uKMic1OYb493MTzwgg6n6aQRa3NwVoZE4BfwGKAIYF1otcJBiaFFJvH6WQbXL38EHZiblAdyK3cR5htEbtjH4tc/640?wx_fmt=png&from=appmsg)

## △ 不同环境VET

#### 3.4.5 技术点三：问题复核，看 CSS 看 computed style

VET diff 阶段会识别出一批候选问题（间距异常、对齐偏差、元素缺失、尺寸不一致等），但候选问题不一定都是真的。每个问题会启动一个独立 Subagent 做四件事：

1. **复核** ：回到 DOM 和运行时样式里确认问题是否真实存在。
1. **量化** ：用 `getComputedStyle()` 测量具体数值，包括间距、字号、颜色值、对齐偏差，精确到 px。只看运行时最终生效的样式，不看静态 CSS 声明。
1. **标注** ：通过注入 SVG 在页面上画框、标数值、写说明，然后截图。让人一眼看懂问题出在哪。
1. **排查线索** ：记录是哪个 DOM 元素、哪个 class、哪个嵌套层级导致的，为修复提供起点。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4hbrOHk4GNXb5WywTwVnA8aP3xynM449b143yK83wMR8WHuKgeEBvtqbYo3VCZbAuPf7e6rwKPGlwt9mn3kGESyDLbXWfkWfU/640?wx_fmt=png&from=appmsg)

## △ 正确设计标注

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7nJxkTribxx6qJHqafiaRsWiaZArkBG1jXObwO4YH16NN889uibzhBHkAK739A6vHzYdPufOGnypbdgyb9znoGia0bjhV4af7EJqAI/640?wx_fmt=png&from=appmsg)

## △ 对应开发也标注

#### 3.4.6 Figma To Verify 的价值

把"感觉不像"变成可确认的（排除误报）、可量化的（精确到 px 和色值）、可标注的（在页面上可视化）、可修复的（提供排查线索）问题。

GEEK TALK

04

Pipeline Code Review：提交后的大规模复审

开发期的 code-validation 关注当前任务的增量改动，Pipeline Code Review关注一次提交的完整变更。两道不同的关卡，分别覆盖不同的审查范围和时机。

人的阅读量非常有限，大量 diff 人很难一次看过来；单 Agent 审大 diff 容易遗漏；分文件 CR 缺少上下文关联；历史遗留代码和多时代规范混杂会干扰模型判断；Review 结果不可追踪，和修复链路断开。

**4.1 核心思路**

****把大 diff 拆成小块，并发派发给多个 AI 子进程独立审查，最后合并结果。****

整个流程分 5 个 Phase：

****Phase 0 — 拆 Diff。**** 逐行解析 unified diff，按目录前 3 级分组（同模块的文件优先放在一起，保留上下文关联），再在模块内按行数做 bin-packing，每个 chunk 控制在 500 行以内。

****Phase 1 — 状态检查。**** 用纯文本的 `task.log` 管理任务状态，支持中断恢复——跑到一半挂了，重启后只处理 pending 的任务。

****Phase 2 — 并发派发。**** 这里用 CLI 子进程而非 subagent。CLI 的 prompt 由脚本程序化生成，避免模型理解偏差和上下文抄写开销，并发数可以开到 10 个以上。每个 chunk 审查完写一个 result JSON，用文件系统追踪进度（File as Progress）。进程收到终止信号时做优雅关闭，已完成的标 completed，未完成的标 failed，保证状态一致。

****Phase 3-4 — 合并汇总。**** 收集所有 result，按文件维度聚合成最终 `review.json` 。

**4.2 Prompt 设计**

几个要点：severity 分三档（error / warn / style），每档用 few-shots 约束分类边界；输出强制 6 个结构化字段，便于后续程序化处理；子进程写完 result 后必须 `JSON.parse()` 回读验证，格式问题在单次 CR 内闭环修复，不透传到调度层。

**4.3 后续链路**

CR 产出的结构化数据可以驱动后续修复流程：

- ****可视化报告页面**** ：展示 issue，支持按 severity 过滤、批量选择。
- ****唤起 IDE 修复**** ：页面上拼接修复 prompt，直接调起 Comate IDE。
- ****自动批量修复**** ：按文件分组，每个文件一个独立 git worktree + 一个子进程，互不干扰。按变更行数从小到大依次 merge（小改动冲突概率低，优先合入），每次 merge 后跑构建验证，失败则 revert。全部完成后 `git reset --soft` 消除中间 commit 历史。
- ****闭环标记**** ：收集修复结果，批量标记已修复的 issue，完成 CR → 修复 → 标记的全链路闭环。
- ****现场集成：**** 厂内开发者的CR是在iCode进行的，让他们直接在这个现场就能看到问题、快速修复无疑是最好的。我们已经基于OpenClaw + BrowserUse初步打通了iCode集成，经实验发现集成到iCode能极大的增加开发者接收问题解决问题的积极性。
![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5L2Dg5Kc7WsHW6TCic4GEGUzmQqoH6qJ8UNLmjwib0Y40xhNwz6YSY48viaXtgtuBwF4iaQJy4sjbPpLefadgtoezkgjVGtagNwW8/640?wx_fmt=png&from=appmsg)

## △ 超大量的CR例子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7K70hAaD6xbEhxic3owZ4y6d0232Gvb3ibefVn3CUmnT9Z77Bql9dhYibslV9YnWWTlYiaaWXHSLQGgm8ctvXORJ7e3WkoA0fTc94/640?wx_fmt=png&from=appmsg)

## △ 修复问题

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5Qzljw1fmLzeYm6CHRNYLNcvkQha0ial0hdicib6qT7Rb4cPS3wkOkcRWicSw4Upib8icxEX9cFNlXT1nrTk3GibK4nDVbS0k0PuP0S4/640?wx_fmt=png&from=appmsg)

## △ 集成openclaw review

GEEK TALK

05

从工具到工程资产

回到开头的全链路：

```css
Agent Operating Rules    → 约束 Agent 怎么干活Code Validation          → 写完即 CRRuntime Verify           → 改了 UI 就看浏览器Figma To Verify          → 对设计稿做视觉走查Pipeline Code Review     → 提交后大规模复审问题结构化 → 修复 → 验证 → 沉淀
```

这些关卡能持续复用和迭代：

- 项目工程规范沉淀为 Agent Operating Rules，每个任务自动生效。
- 代码审查经验沉淀为 code-validation 的 rules.md，开发期和流水线共用。
- 页面验证经验沉淀为 visual-verify 的 memory，跨任务积累。
- 视觉走查能力沉淀为 Figma To Verify 的 Skill 组合，可复用于任意页面。
- QA 发现的高频问题可以反向写入 Rules 和 Skill，下次 Agent 直接避免。

****一次检查只是工具，能持续复用和沉淀的检查机制，才是团队工程化资产。****

对 RD 和 QA 协作的意义

过去：RD 写完代码 → QA 测出问题 → RD 修 → QA 回归。低级问题和高价值测试混在一起。

现在：RD + Agent 完成实现，QA将测试经验和能力赋能到开发环节，通过左移讲质量控制前置，code-validation 做开发期 CR，visual-verify 做运行时验证，Figma To Verify 做视觉走查，RD 带着验证结果交付，QA 进一步在复杂业务风险和用户场景上配合Agent自动化，全面保障项目质量。

GEEK TALK

06

附录

OpenClaw配备review的SKill：https://bjh-fe-assets.cdn.bcebos.com/assets/icode-review.tar.gz

browser相关的skill：https://github.com/hixuanxuan/browser-automation

安装方式：

1\. 只安装 `visual-verify` ，用于日常开发的验证工作。

```sql
npx skills add hixuanxuan/browser-automation --skill visual-verify
```

2\. 安装figma走查相关的skill。

```ruby
npx skills add https://github.com/hixuanxuan/browser-automation/tree/main/figma-to-verify
```

3\. 我只想用CDP，做基础的截图、获取DOM、获取HTML等工作，或者在此基础上封装其他的browser Skill。

```sql
npx skills add hixuanxuan/browser-automation --skill chrome-cdp
```

END

**推荐阅读**

[AI 写代码越来越快，质量谁来守？网盘主端 FE 的 AICR 准入实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607296&idx=1&sn=6391624f21e7b937993f76d71ed31c13&scene=21#wechat_redirect)

[协作的逆向演进：从 Agent 逻辑重构团队管理](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607278&idx=1&sn=cb5a7864388354184e4abd5d9867709b&scene=21#wechat_redirect)

[AI Coding 的底层框架：一切优化都是在对抗熵增](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607253&idx=1&sn=e89c9492c24a9f710d802034525bf27a&scene=21#wechat_redirect)

[全链路研发智能体 ——从"体感能用"到"实际可用"的工程实践](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607224&idx=1&sn=0aadef3dcfe99403781d226431539874&scene=21#wechat_redirect)

[当代码越来越便宜，什么在变贵？](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607179&idx=1&sn=e6c3e57e110325c5ef070d0cec7d20f9&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过