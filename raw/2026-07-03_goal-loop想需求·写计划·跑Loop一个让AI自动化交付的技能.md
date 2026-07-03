# goal-loop 想需求 · 写计划 · 跑 Loop: 一个让AI自动化交付的技能

**作者**: 江枫AGI

**来源**: https://mp.weixin.qq.com/s/n-nAJRDLOFKsqntJCgbgVw

---

## 摘要

goal-loop是一个实现AI自动化代码交付的技能，它将需求澄清、计划拆解与循环执行结合为标准化工作流。用户提出想法后，该技能会通过苏格拉底式提问对齐目标并产出需求规格文档，随后将其拆解为细粒度任务计划，最后启动无人值守循环自动构建并交付代码。这套“想需求、写计划、跑循环”的流程能帮助独立开发者或产品经理等人群高效落地MVP想法，且无需编程经验。

---

## 正文

江枫AGI 江枫AGI

在小说阅读器读本章

去阅读

![](https://mmbiz.qpic.cn/mmbiz_png/BbYXKJeDichgjMnlRn3h7PcBRYB10rLticPYPkiaDv2EMygibVoQpTjEpp4qQddlDbMABt6GvcrHyrYk7A4jEsg2rdDLXjEUmT6mgSr4kQCuo2U/640?wx_fmt=png&from=appmsg)

前几天在社群里看到一个"AI 自动化工作流"单次咨询收费5000，仅有标签包装又不能看到实质性的内容。再结合最近一段时间研究，这事本身没那么玄学。拆解开就是需求澄清 + 计划拆解 + 循环执行 + 背压测试全流程设计而已。这次作者将此直接做成 Skill 开放出来。这就是 goal-loop 目标循环的由来。它不会替代你思考，只是把"想（需求）、写（需求规格与计划文档）、跑（Loop 自动化循环构建）"做成完整的工作流。你与AI讨论清晰需求后，把需求、规划任务交给循环构建。让它把协助你把代码构建出来。无需编程经验的朋友也可以试试。

**一句话说清楚 goal-loop** ：你说"我想做个 X"，goal-loop 会先把 X 问清楚、再拆成可执行计划、最后挂一条无人值守循环把 X 跑成代码。

---

> 适合人群：
> 
> 独立开发者、产品经理、技术负责人、学习者/研究者、AI Coding 用户、MVP想法落地应用的验证者
> 
> 不太适合：
> 
> 1、一两行就能改完的小补丁（用普通 AI 对话更快）
> 
> 2、需要大量人类美学判断的 UI / 视觉设计任务（循环擅长结构性代码，不擅长品味）
> 
> 3、对生产分支直接构建的场景

---

goal-loop 技能为目标循环，主要协助使用者，从"需求想法或头脑风暴→编写任务规划→自动化循环构建实现代码"全流程交付的技能。

---

核心：假设你有一个需求或想法，启动 goal-loop技能，AI 会通过苏格拉底式反向提问，向需求设计者询问与需求相关的问题，从而收敛需求-对齐人与AI目标，并产出需求规格文档 specs/\*。你可以修改审核产出的需求规格文档，接着将需求规格文档 specs/\* 拆解成可执行的细粒度任务清单。最后启动无人值守模式

`./loop.sh build 10` ，从而自动构建并交付出代码。

> 温馨提示：从想需求 → 写规格/计划 → 跑自动化循环 Loop 「Think → Spec → Loop」 —— 标准化工作流设计，无论是在 Claude / Codex / OpenCode 智能终端代理工具， 还是在Trae / Kiro / Cursor 界面化代理工具中同样适用。

## 一、goal-loop 是什么？

## goal-loop 为目标循环，作者通过该技能将头脑风暴（brainstorming）、计划编写（writing-plans）与 Ralph Loop 构建循环与 Geoff Huntley 的 Ralph 自主执行循环相组合, 从而形成一条从"需求想法→任务规划→自动实现代码构建"完整的工作流。

- ## 需求想法与规划层：采用“结合头脑风暴、计划编写”的方法论（brainstorming + writing-plans），通过苏格拉底式提问把模糊需求拆成清晰的 specs/\*，再对比现有代码产出可执行的细粒度计划IMPLEMENTATION\_PLAN.md
- **执行层** ：采用 Geoff Huntley 的 **Ralph Loop** 自主循环，执行 `./loop.sh build 10` 构建交付代码, 每轮启动全新 `claude -p` 进程，清空上下文，按 plan 选任务、实现、跑测试、提交、推送，周而复始。

这里，我们可以看到需求想法与规划层就是在自动化构建实现代码之前，彻底与AI讨论搞清楚要做什么 specs/\*及怎么实现IMPLEMENTATION\_PLAN.md的问题。构建实现交付代码交给循环即可。简单说就是在交给自动化实现之前，先与AI对齐，并想清楚

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BbYXKJeDichgtCzz8GicSCjKUcOibj9z6BJGhQ0eicgSJAicpK6KZdvRPMvsHiapUNs4n4nibwic74iagQgdE7BNCU6AficRDbOSISxD2AdpvVdia3vZV8/640?wx_fmt=png&from=appmsg)

**goal-loop 核心机制** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BbYXKJeDichiaxk1jZxB3mInkE6NbWFzMxicBHbGlWpPSXQZIPOsathABSy44fts3o4RibDrU5J6yiajATFL9VoCaZUfRJFUeLMm9fS8hvC7tFuY/640?wx_fmt=png&from=appmsg)

---

## 二、使用场景

goal-loop 技能最适合以下使用场景：

1. **需求还不清晰，需要先探索再动手**  
	例如：“我想做一个支持多主题切换的黑客帝国精灵符文终端数字雨特效”——先用 Phase 1 把待完成的工作、范围、验收标准聊清楚。
2. **功能有一定复杂度，需要拆解成多个小任务**  
	适合 2–5 分钟一个任务的中等粒度，便于循环逐项实现与验证。
3. **需要在长周期内自动持续构建**  
	如：睡前挂一个 `./loop.sh build 20` ，让循环自动推进、测试、提交。
4. **希望把需求、计划、实现过程沉淀为可审查的文档**  
	产出的需求规格文档 `specs/*.md` 和 `IMPLEMENTATION_PLAN.md` 任务清单文档，即项目决策记录。
5. **已有代码库，需要新增复杂模块或重构**  
	Phase 2 会对比 `specs/` 与现有代码，识别差距并生成具体改造路径。

---

## 三、解决的问题

![](https://mmbiz.qpic.cn/mmbiz_png/BbYXKJeDichjRA1MfQtoYicJXV44iayxcTjK7HicrYBAw5tQz6uUDj0zMwK5Ldf6ToVo82OxORUFbVicbBdEaWZD6QmpPeebjl1Mcveicaibnx2J9Y/640?wx_fmt=png&from=appmsg)

---

## 四、三阶段流程

```bash
┌────────────────────────────────────────────────────────────┐│ Phase 1 — 思考（交互式）                                    ││ 模糊想法 → JTBD(待完成工作) → topics(主题拆分)              ││         → specs/<topic>.md (需求规格)                       │└─────────────────────────┬──────────────────────────────────┘                          │ specs/ 是事实来源                          ▼┌────────────────────────────────────────────────────────────┐│ Phase 2 — 规划（二选一）                                    ││ 默认：交互式产出任务清单 IMPLEMENTATION_PLAN.md                     ││ 备选：./loop.sh plan  无头循环迭代收敛 plan                 │└─────────────────────────┬──────────────────────────────────┘                          │ IMPLEMENTATION_PLAN.md                          ▼┌────────────────────────────────────────────────────────────┐│ Phase 3 — 执行（自主循环）                                  ││ ./loop.sh build → 读 plan → 选任务 → 实现 → 测试 →         ││ 更新 plan → git commit + push → 退出 → 重启                 │└────────────────────────────────────────────────────────────┘
```

### Phase 1：思考（头脑风暴）

- 触发词： `探索需求` 、 `探索设计` 、 `用户意图` 、 `先探索再实现` 、 `需求澄清`
- 一次一问、苏格拉底风格，把模糊想法拆成多个 **topic** （一句话、不带“且”）
- 每个 topic 写成 `specs/<topic>.md` ，包含待完成工作、范围、验收标准、约束
- **硬性门禁** ：未经用户批准，不写任何实现代码

### Phase 2：规划-产出拆解的任务清单

### IMPLEMENTATION\_PLAN.md

- 触发词： `写实现计划` 、 `写计划` 、 `做计划` 、 `实现计划` 、
- 默认路径：在当前会话交互式调用 `phases/writing-plans.md` ，一次性产出计划
- 备选路径：运行 `./loop.sh plan [N]` ，让 Ralph 循环反复读取 specs 与代码，迭代产出计划
- 每个任务必须细到 **2–5 分钟可完成** ，包含确切路径、完整代码、验证方式

### Phase 3：执行（无人值守模式）

- 触发词： `goal loop` 、 `自主构建` 、 `构建循环` 、 `自动构建` 、 `loop build`
- 命令：`./loop.sh build [最大轮数]`
- 每轮：
1. 读取 `IMPLEMENTATION_PLAN.md`
	2. 选择当前最重要任务
	3. 实现并运行 `AGENTS.md` 中的测试命令（反压）
	4. 更新计划状态
	5. `git commit` + `git push`
	6. 退出进程、清空上下文、重启下一轮
- 停止条件：plan 清空或达到最大轮数或 `Ctrl+C`

---

## 五、快速上手指南

### 1\. 安装 goal-loop Skill 技能

创建一个项目 project-app,到项目根目录下，执行 npx goal-loop，该Skill 会自动安装在当前项目下

![](https://mmbiz.qpic.cn/mmbiz_png/BbYXKJeDichgHcCfpOS5iatsGC0wKGzLYXegzuFTNrEXibckzg1I9icUVnpUySHNsZiaeia5amNf5TAVyOrCgIA5xmKgN0rTEF9SIB7icE2D3pgosE/640?wx_fmt=png&from=appmsg)

goal-loop 技能安装包地址

```bash
# goal-loop 从想需求 → 写规格/计划文档 → 跑自动化循环 Loop # 工作流技能 https://www.npmjs.com/package/goal-loop
# github 仓库地址https://github.com/AragornZJF/goal-loop
```

### 2\. 启动 goal-loop

用触发词激活 skill，例如：

> “帮我 **探索需求** ：实现一个终端黑客帝国精灵符文数字雨特效。”

系统会根据项目状态自动路由：

![](https://mmbiz.qpic.cn/mmbiz_png/BbYXKJeDichiaa4Vum2t7XcYeRU7feUYUn84RXd8dbYKndKkIg9Yn9vAUF7aemwibo7W7Agd7wda2F4SV4xSW2h3dsmBNbPmMiaLEGll3icUlMB4/640?wx_fmt=png&from=appmsg)

### 3\. Phase 1：澄清需求

跟随 skill 的苏格拉底式提问，回答关于用户、场景、价值、约束的问题。  
最终你会得到一组 `specs/*.md` 文件。  
**确认无误后再进入下一步。**

### 4\. Phase 1→2 过渡：首次运行设置

skill 会自动执行首次设置：

```shell
mkdir -p buildspecs# 生成 loop.sh / clean-state.sh（wrapper，自动回退到用户级 skill）# 复制 templates/AGENTS.md 到项目根# 如检测到 build/package.json，自动从 scripts.{build,dev,test,typecheck,lint} 填入命令
```

检查生成的 `AGENTS.md` ，确认命令与项目实际一致（未检测到的占位符需手动补齐），例如：

```markdown
## Commands- Build 构建: \`npm run build\`- Test 测试: \`npm test\`- Lint 检测: \`npm run lint\`
```

### 5\. Phase 2：生成实施计划

默认选择 **交互式路径** （选项 `1` ），在当前会话产出 `IMPLEMENTATION_PLAN.md` 。  
如果你希望循环自动迭代计划，可选择 `./loop.sh plan [N]` 。

审查计划：确保每个任务 2–5 分钟、路径明确、可验证。

### 6\. Phase 3：启动自动构建

**默认（推荐）** ：以无头循环交付代码。

```bash
./loop.sh build        # 无限轮次，直到 plan 清空./loop.sh build 15     # 最多 15 轮./loop.sh 15
```

一键启动Loop循环，自动化从拆解任务清单文件 IMPLEMENTATION\_PLAN.md，然后从中选择任务，直到所有任务全部完成，实现，通过测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BbYXKJeDichjmG1PkvH4t0rUeSeLdkXRSeU5ykjrLDx2HHtg6pfYKH3wsvOCG1cIoraWn93d9ChVpibn0lhMKDibMOz69cyTaibqzdAS5qkqibsg/640?wx_fmt=png&from=appmsg)

循环会自行实现、测试、提交、推送。你可以随时：

- `Ctrl+C` 停止循环
- `git reset --hard` 回滚未提交改动
- 删除 `IMPLEMENTATION_PLAN.md` 重新跑 Phase 2

**备选（在当前窗口手工实现）** ：如果你不想跑无头循环，可以 **明确告知 skill** ：「在当前会话按 plan 逐项实现」。skill 会在本窗口按 `IMPLEMENTATION_PLAN.md` 一项项实现，每完成一项更新计划状态、运行 `AGENTS.md` 中的测试命令，按需 `git commit` 。默认路径仍是无头循环——除非你开口，不会在当前会话直接动手写实现代码。

---

## 六、安全提示（运行循环前必读）

`./loop.sh` 以 `claude --dangerously-skip-permissions` 运行，会绕过所有权限提示：

- 每轮自动 `git push` ，请确保当前分支是隔离分支， **不要在生产分支上运行** 。
- 推荐在 Docker、E2B、Fly 等隔离环境中使用，并配置最小权限 API 密钥。

## 七、实战演示

*往期关联文推荐*

## 我把Markdown转知识图谱，做成了Skill

*[Ralph 实践手册一、让AI自主循环编码指南](https://mp.weixin.qq.com/s?__biz=MzIxMTgyOTQyNQ==&mid=2247485867&idx=1&sn=64f851d81b9d43a5b9c682114f737c93&scene=21#wechat_redirect)*

*[Ralph Loop：让Claude Code自主运行数小时，交付任何代码](https://mp.weixin.qq.com/s?__biz=MzIxMTgyOTQyNQ==&mid=2247485618&idx=1&sn=486b784b1e396ac7edd3828e00e973f4&scene=21#wechat_redirect)*

*[微信ClawBot + Claude Code：构建你的24小时数字员工](https://mp.weixin.qq.com/s?__biz=MzIxMTgyOTQyNQ==&mid=2247485656&idx=1&sn=44f0ba7c67636b2852a9c2f627c3a86f&scene=21#wechat_redirect)*

*[使用Claude Code四个高阶技能，让生产力翻倍](https://mp.weixin.qq.com/s?__biz=MzIxMTgyOTQyNQ==&mid=2247485656&idx=1&sn=44f0ba7c67636b2852a9c2f627c3a86f&scene=21#wechat_redirect)*

参考资料

1.https://www.npmjs.com/package/goal-loop 从想需求、写规格与计划文档、跑自动化循环 Loop 仓库地址

2.https://github.com/AragornZJF/goal-loop github goal-loop 地址

3.https://github.com/obra/superpowers

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过