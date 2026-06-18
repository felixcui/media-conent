# harness-pilot 给代码库加一套"规则说明书"和"自动检查器"

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/oy8xzG363P73jTM57yzJTQ

---

## 摘要

Harness Pilot针对AI Agent在代码库协作中无法感知隐性规则导致反复违规的问题，提出了从依赖“自觉”的事后检查转向编码前强制预验证的范式转变。它通过将项目规范显式化、版本化并集成到Git工作流中，依靠自动化脚本在编码前进行强制验证，有效解决了规则更新滞后和约束力弱的痛点，确保AI Agent在既定架构下可靠协作，并将项目知识沉淀为可复用资产。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 杨桐

导读

introduction

Harness Pilot通过将项目规范显式化、版本化并集成到Git工作流，从根本上解决了AI Agent因无法感知隐性规则而导致的协作不可靠问题。其核心在于从依赖AI“自觉”的事后检查，转变为依靠自动化脚本在编码前进行强制预验证的范式，从而确保AI Agent在既定的架构和质量约束内可靠、高效地协作，并将项目知识沉淀为可复用的资产。

*全文 6343 字，预计阅读时间 6 分钟*

GEEK TALK

01

核心问题：AI Agent 在代码库中的协作挑战

AI Agent 在代码库协作中面临的核心问题是 ****可见性**** ——项目中的分层约束、命名规范及架构约定对 Agent 而言往往是 ****隐性**** 的。

如果这些规则未在 Git 仓库中以显式化形式存在，Agent 将无法感知，进而导致反复违规、陷入修复循环，且上下文容易被错误日志填满。

****隐性规则示例**** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy6yX8icckL96XebVsTljY1aHsR7LRyYSkqDtyRbZxFiaibW2lodUn4bVNUoJYzwFOky5OxWKWJMYvRFxgSC6ARiaFAUl19JdibjQzX4/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5KucLlUKOjcxV4munRs0pqg6vWy8090S8bV3cUQC6iaytwogRGfb4libI9vfic7Ml9m3HARwV3eKMOjwF7Mpe6bbVPxKYrXJYrqU/640?wx_fmt=png&from=appmsg)

GEEK TALK

02

解决思路：从"教"到"验"的范式转变

现有方案（如 System Prompt、RAG、CI/CD Lint 等）的根本局限在于：规则更新往往滞后于代码演进，检查时机过于靠后，且约束力过度依赖“自觉”。

Harness Pilot 的核心优势在于： ****实现规则在 Git 仓库中的版本化、在编写代码前进行预验证，并依靠自动化脚本强制执行**** 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy7siaAJeo92IunTLFvtjccORiaHy5A4ey7mltu3FUEI4Ng5icM3tBMBKLblfsghibAL5ia99BuSDqUQicvlqEHkicQBUUYNxKyEmTWFy0/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4Wbkfw7m4CoQgpInNxbk71fr75UrYWLfSYkGBprkQNpicGSMSPLVFQzkpAy8icBptPNktqLZGv6zVb7rZQonFMywfsG936Dt1R8/640?wx_fmt=png&from=appmsg)

GEEK TALK

03

项目愿景与设计原则

### 目标

确保 AI Agent 在代码库中 ****可靠协作**** ，并构建可复用的项目知识资产。

### 解决的问题矩阵

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy569tvgex2JGgWq47UHqxILuv3I2zKk4sbdEBy6PiaYHQlJBA92yzjrFxlWbsXFbJtOBGjmWuWD8WLO7YKOPcsrhUH45I4O9Gug/640?wx_fmt=png&from=appmsg)

### 四条设计原则

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy6azExJc8Kst4qCNT0pibtk08XkmtI2kH5xmQ6B12r2lGu7ibbLGIxroibe6f4iagUhvIVI7Q2ibs8eehIJ010ewsyDTQ2gvWm6ywKw/640?wx_fmt=jpeg&from=appmsg)

****1\. Git 仓库作为唯一事实来源（SSOT）****

- 规则必须沉淀在代码库中，而非仅存在于 Wiki 或口头约定中
- 通过 Git 实现版本化，与代码同步演进
- 确保 Agent 接入项目即可获取完整上下文

****2.**** `.harness/` ****具备自包含性****

- 所有生成文件均集中于 `.harness/` 目录，避免污染项目根目录
- 文档统一存放于 `.harness/docs/` ，支持按需加载
- 通过 `manifest.json` 追踪状态，支持增量更新机制

****3\. 关注边界，解耦实现****

- 明确层级依赖规则
- 不强制规定设计模式或编码风格（质量规则除外）
- 边界内的具体实现方式保持高度自由

****4\. 预验证优于事后检查****

- 在执行结构性操作前，优先验证其合法性
- 在编写代码前确认可行性，而非事后修补
- 大幅降低代码修复成本

GEEK TALK

04

HarmonyOS开发简介

Harness Pilot 作为一款 Claude Code 插件，集成了两大核心 Skill、五类内置 Agent 以及一套分层模板系统。

**4.1 两个 Skill**

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5v105cyOtGib325gmuICibCGOzyX8pOEstW2u7UjDvWQBuxKX2pfAyhyhLPfIc9GqIT9dh4BuUJibibYoR6AtWugQqujVYbO331l4/640?wx_fmt=png&from=appmsg)

#### harness-analyze

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy5Qbb46MZkUaLWHPiasibqSAwNcsT7WXTRvnvbtTSCchjoHw89y1OELasZdmaby1sAgeic5glKj0s94oxKwcUbeHFkPg87AQT9dt4/640?wx_fmt=jpeg&from=appmsg)

分析流程包含以下四个步骤：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6GhIPeerqXGypmUfvMt0fMFnTPlPYavXEB4UrYfRgWuMVsXAZTHicquOm8ENhWkBeNdIyU6uJXluA9zKNEGf1qwxMQKUibtZtico/640?wx_fmt=png&from=appmsg)

评分权重分配为：文档覆盖率 35%、架构合规度 35%、测试覆盖率 30%，并支持历史趋势追踪。

#### harness-apply

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy5seAQgBz3wr4befOkbszlCPZCniaX4QosR6JqySdv1L81BGXicib49usTpvsJqXZZQe8PzzxPUJIAWzGGuhqpkPH2E3SVTRYlzBw/640?wx_fmt=jpeg&from=appmsg)

支持三种模式：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4lGXEyL3p6JcqBkAsDyGZETwoCia6TSjia1hJYF1Brlt9kRzvRcRHgpUya4c8AetlhM5ibou67cTG7gHYHYwg2SXnZrWUVQ0zZD4/640?wx_fmt=png&from=appmsg)

****开发模式选择（Development Mode）****

`harness-apply` 在初始化和代码生成模式中， ****首先**** 进行开发模式选择（Step 0），再执行生成。默认使用 ****SPEC（SDD）模式**** ，由复杂度分数强制执行。

****复杂度 → 模式 映射表**** （SPEC 是所有任务的默认模式）：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4ribotS89pIf4bbYj3d0Uav6dYFCObE0ibYicsMzAniayxO1fPtNAqWLCCJQhFD5HzgSyl1cOFNpLk0cNic9YLprBmhN1KHdyN0gco/640?wx_fmt=png&from=appmsg)

****openspec 插件集成**** ：选择 SPEC 模式后，自动检测 openspec 插件是否已安装：

- ****已安装**** ：将完整 SDD 工作流（doc.md → tasks.md → 实现 → summary.md）委托给 openspec 插件
- ****未安装**** ：使用内置 fallback（展示预填充 spec 大纲，用户确认后生成 `.comate/specs/{taskId}/` 产物）+ 推荐安装 openspec

****专家团自动路由**** ：分数 ≥ 11 时自动组建专家团（Architect、Implementer、Reviewer），展示团队构成后等待用户确认，再进入生成阶段。 `--no-panel` 可跳过（critical 级别不可跳过）。

****覆盖标志**** ：

- `--auto` — 跳过所有提示，接受默认值
- `--no-panel` — 跳过专家团（仅在 `expertPanelCanSkip: true` 时有效）

**4.2 Agent 体系**

Harness Pilot 内置五个专职 Agent，在特定场景下由 Skill 自动调度：

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy7UEWmxiaLwRvCqunD1RV812zbsrC9AHXnV1GzFwIEbIuBY9jb53lKHIZesS2m9cbeZlMDrT1bicCzGOAHNYs6Z3pIIgwcP4wibQM/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4gibiage6VIicHUBSsc28Cia28047GCibavMunQRoPzuAyf27jDcpMu4LYeUCOlqWjevJ2JMp3VAkJSIodA5v9hxwQLvDxIugZ36cQ/640?wx_fmt=png&from=appmsg)

code-reviewer 检查维度：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5LmicB76tjBOhMiaqeTZCG3dora5a2sp1u70lrvd0wC01qoWUtkuuu79WIQNqJ9iaKddbvr3aQ3as7xLI1fBSSj1HjsecHTgwXWI/640?wx_fmt=png&from=appmsg)

**4.3 模板系统**

`harness-apply` 使用分层覆盖机制生成文件，越靠后的层优先级越高：

****AGENTS.md：AI Agent 的导航地图****

`AGENTS.md` 是 `harness-apply` 生成的核心文件之一，位于 ****项目根目录**** （与 `.harness/` 同级）。它是 AI Agent 进入项目时的第一站，提供快速导航。

****生成的 AGENTS.md 结构**** ：

```shell
# {PROJECT_NAME} - Agent Navigation Map
## First Principles# 四条核心原则（从需求出发，而非模板）
## Project Overview# 语言、框架信息
## Key Files# 关键文件索引# ├─ AGENTS.md（本文件）# ├─ .harness/docs/ARCHITECTURE.md（架构规则）# ├─ .harness/docs/DEVELOPMENT.md（开发命令）# ├─ .harness/docs/PRODUCT_SENSE.md（业务上下文）# ├─ .harness/manifest.json（配置快照）# └─ .harness/capabilities.json（已启用能力）
## AI Rules Location# 规则文件索引
## Available Harness Skills# /harness-analyze、/harness-apply 命令说明
## Workflow# 标准工作流：analyze → apply → develop → validate → ship
```

****设计目的**** ：

- 新会话的 Agent 打开项目首先读取 `AGENTS.md` ，快速定位关键文件
- 避免在目录中盲目搜索，降低上下文消耗
- 包含 First Principles，确保 Agent 从核心需求出发而非模板化操作

```cs
base/ → languages/ → frameworks/ → rules/ → capabilities/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6MdB3cMhvrAibiaMkly2rfTIkXZkWSTGUFYltgfQb7PiaACYDPJrL9iclqZUjALqKSY8ic8NpGvjSICH0XiceiawS50FrBAB4NngC69k/640?wx_fmt=png&from=appmsg)

模板使用轻量级 Mustache-like 引擎（ `scripts/template-engine.js` ）渲染，支持变量替换、条件块、循环，并内置 LRU 缓存提升性能。

GEEK TALK

05

关键机制

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy7sHF196zEI6uNIcKE0mJOq4Rib49y8PFwHicsUv2U5hHr9QVnCz74KUbeg7TJqgAibYvNAqBSnxEZEHSxpW6sc9lWzfichD0nOTPc/640?wx_fmt=jpeg&from=appmsg)

**5.1 Ralph Wiggum Loop**

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy6h1xOxkcibDxcpUAtk3lxKlO0pNTwyibSnc4sAbQXgRR3BjtVIskXUsFu6Uk1077M3muhRFwNNZLianOWRv8BZAh5u0HibPIGyl6g/640?wx_fmt=jpeg&from=appmsg)

自动化审查-测试-修复质量循环， `harness-apply` 执行后自动运行，最多 3 轮：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6f1r2zXzrGkTeItibQNbt29PN8z5K95q0iaffvuPwUaucCyfVY3J1sZZFml6HVnibbBQQI0RKZQfF4D5ib22Ppvic4rQDyH0RMFibV4/640?wx_fmt=png&from=appmsg)

失败轨迹记录在 `.harness/trace/failures/` ，供后续会话复盘。

**5.2 Handoff 跨会话机制**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy79sniaoDGXibdPJnBrrYPl7CaRRTJ5yiacaABDJCYaTf35RH1gjKKl2CsQYgzT6cwsnWd48rFOSEaHSm5SArCzl7oUiaD3ETMkkrA/640?wx_fmt=jpeg&from=appmsg)

鉴于 LLM 上下文窗口的限制，随着 tool call 次数的增加（约 40 次后），早期关键信息易遭压缩或丢弃。Handoff 机制通过 ****结构化 artifacts**** 实现状态持久化，从而摆脱对 AI 内部“记忆”的依赖。

****触发条件**** ：

1. 上下文窗口接近限制（tokens > 100k）
2. Loop 迭代耗尽且问题未解决
3. 用户显式请求 handoff

****传递结构**** ：

****Session A → 写到文件 → Session B****

- `agent-state.json` ：上一个 agent 的执行状态
- `context.json` ：上下文摘要（目标、进度、关键文件）
- `resume.json` ：下一个 session 的恢复指令

基于文件系统的持久化方案——确保数据准确无误、不会遗失，且不受上下文压缩的影响。

**5.3 Reentrant Apply**

`manifest.json` 追踪状态，支持增量更新：

- 记录上次 apply 时间与版本
- 追踪层级映射和自定义规则
- 增量更新时保留用户自定义内容，仅覆盖标准生成部分

**5.4 Hooks**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4SlWRDxpiauuukSJIt13LwaQv3icjnAuFnKgLiauJmibVEHPtbedFM7rMvibvy61icYBfMlZFaoygqfVcaH9j80dYQUOShmXr4tAbjQ/640?wx_fmt=png&from=appmsg)

GEEK TALK

06

架构设计

![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy5zf8mne6eXWwPGczsVygPunH7ctiaoibZef9R7q0XgvyOvmic7zTr3uTVoiaxwuXb7z4tLbdNodsDncK7phhuOibmich0icicN68w2QQQ/640?wx_fmt=jpeg&from=appmsg)

**6.1 插件内部结构**

```objectivec
plugins/harness-pilot/├── .claude-plugin/         ← 插件元数据（plugin.json）├── skills/│   ├── harness-analyze/    ← 分析 Skill（SKILL.md + 4 个工具）│   └── harness-apply/      ← 生成 Skill（SKILL.md + 4 个工具 + config/）├── agents/                 ← 5 个 Agent 定义（.md 文件）├── templates/              ← 分层模板系统│   ├── base/│   ├── languages/│   ├── frameworks/│   ├── rules/│   └── capabilities/├── lib/                    ← 共享工具模块│   ├── config.js│   ├── constants.js│   ├── detect-language.js│   ├── fs-utils.js│   └── path-utils.js├── scripts/│   ├── template-engine.js  ← 模板渲染引擎│   └── generate-test.sh    ← JIT 测试生成脚本├── hooks/                  ← session-start hook└── tests/                  ← 单元测试
```

**6.2.harness/ 目录结构（生成产物）**

应用 `harness-apply` 后，在目标项目中生成：

```python
my-project/└── .harness/    ├── manifest.json          ← 状态追踪（reentrant apply 用）    ├── capabilities.json      ← 已启用能力快照    ├── docs/    │   ├── ARCHITECTURE.md    ← 项目架构、层级规则    │   ├── DEVELOPMENT.md     ← 开发命令、测试方法    │   └── PRODUCT_SENSE.md   ← 业务上下文    ├── scripts/    │   ├── lint-deps.*        ← 依赖方向检查    │   ├── lint-quality.*     ← 代码质量检查    │   ├── lint-imports.*     ← 导入限制与循环依赖检测    │   ├── lint-semantic.*    ← 语义业务逻辑验证    │   └── validate.*         ← 统一验证入口    ├── rules/    │   ├── common/    │   │   ├── safety.md          ← AI 安全约束    │   │   └── git-workflow.md    ← Git 工作流规则    │   └── {language}/    │       └── development.md     ← 语言特定开发规范    ├── memory/                ← 三种记忆（情景/程序/失败）    ├── trace/                 ← 失败轨迹    ├── hooks/                 ← Git hooks（post-commit）    ├── tasks/                 ← 任务状态与检查点    │   ├── {task-id}/    │   │   ├── task.json    │   │   ├── checkpoint.json    │   │   └── next-steps.json    │   └── .current    └── handoffs/              ← 跨会话 handoff artifacts        ├── {session-id}/        │   ├── agent-state.json        │   ├── context.json        │   └── resume.json        └── .latest
```

**6.3 共享工具库（lib/）**

`lib/` 是插件内部的共享工具层，消除 Skill 和 Agent 之间的代码重复：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4vUMdIFAJOicGab7IA6E6RPpQ7w9FYjVEy8w1JqRZdskMBsU4UFS9JgHlWwSResWbv7dAiaZNr7Tx6JYHOicEKCmufStHlwBzWias/640?wx_fmt=png&from=appmsg)

GEEK TALK

07

业界在做什么？

**7.1 核心共识**

- ****OpenAI**** ：Harness Engineering 让 Codex 在复杂任务中保持可靠
- ****Anthropic**** ："手"与"脑"的分离——Managed Agents 实现规模化
- ****Google DeepMind**** ：小模型 + 好 Harness > 大模型（Gemini Flash + AutoHarness > Gemini Pro）
- ****LangChain**** ：五大 Harness 中间件让 Terminal Bench 得分从 52.8% 提升至 66.5%

**7.2 Harness 架构演进与分类**

业界执行循环经历了四代演进： ****ReAct**** (思考-行动) → ****Reflexion**** (行动-反思) → ****Planner-Executor**** (规划-执行，当前主流) → ****Meta-Harness**** (自动进化)。目前主流架构分为以下四类：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6AxBDAfOwxozuibW3BknRLcSJM9eibIM9GZ1ga9EguqQ8iaDBIBg4fVHH38MeXkUXCuYr30aBAu7rtG6GLdhLibXhdccm5uibZbGjg/640?wx_fmt=png&from=appmsg)

**7.3 测试验证机制**

涵盖静态 Lint、单元/集成测试、端到端及真机测试。 ****关键数据**** ：Meta 研究发现，在 PR 阶段自动生成测试（JiT），能将 AI 代码缺陷检出率提升 ****4倍**** （测试覆盖率从 60-70% 提升至 85-95%）。

**7.4 参考链接汇总**

- OpenAI: Harness Engineering
	https://openai.com/zh-Hans-CN/index/harness-engineering/
- Anthropic: Claude Managed Agents
	https://claude.com/blog/claude-managed-agents
- DeepMind: AutoHarness
	https://deepmind.google/discover/blog/autoharness/
- LangChain: Agent Harness Anatomy
	https://blog.langchain.com/the-anatomy-of-an-agent-harness/
- Meta: Harnessing Llama
	https://ai.meta.com/blog/harnessing-llama-building-reliable-agents/
- Cursor: Better Bugbot
	https://cursor.sh/blog/better-bugbot
- Stanford: Meta Harness
	https://arxiv.org/abs/2603.18952

GEEK TALK

08

总结

**8.1 核心理念**

与其试图“教导” AI Agent 如何正确执行任务，不如赋予其 ****自动验证**** 执行结果正确性的能力。

依靠代码、linter 及自动化测试来保障正确性，而非依赖 LLM 的“直觉”。

**8.2 行动建议**

1. 运行 `/harness-pilot:harness-analyze` 分析项目健康状况
2. 运行 `/harness-pilot:harness-apply` 生成基础 `.harness/` 结构
3. 调整 `lint-deps` 脚本，确定层级规则
4. 搭建完整验证管道（build → lint → test → validate）
5. 让 Ralph Wiggum Loop 和 Handoff 机制自动运行
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy4SO8ibmlbnLvwc5zAFsCdKiagky3jZZO5Wb5RVayRRj4036qs8ynW2micwncslkxnPojHpB3DSb5OQyUYTzG2m2icrbuY8QJ4w8v8/640?wx_fmt=jpeg&from=appmsg)

GEEK TALK

09

附录

### 支持的语言

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5LLl6v5sn9aCJbScDHOS5EO66sAjSeDMthZjqHjnoR4XEkx9sDtCoEzd8zQFnxPMEDvrpMsUMvJjuYQqGm9SXuySHCNfhpCcA/640?wx_fmt=png&from=appmsg)

### 支持的框架

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4EYkPk6surTMVxQVjiadPrLZA43aR3pmcM3tRCsAsGlKHRiavwEY3e7iaSAWFqKXBBp7lGbToFPMC2afMoj96c2Jv2iaUb6gzJS3Q/640?wx_fmt=png&from=appmsg)

GEEK TALK

10

使用效果

## 执行harness-analyze

```swift
/harness-pilot:harness-analyze⏺ I'm using harness-analyze to perform a dryrun analysis of this project.  Let me gather the project information and run the analysis checks.⏺ Searched for 8 patterns, read 2 files (ctrl+o to expand)⏺ Bash(go test -cover ./... 2>&1 | grep -E "ok|coverage" | head -20)  ⎿     github.com/atom-yt/claude-code-go/cmd/claude            coverage: 0.0% of statements     ok         github.com/atom-yt/claude-code-go/internal/agent        0.529s  coverage: 68.0% of statements     ok         github.com/atom-yt/claude-code-go/internal/api  0.431s  coverage: 28.5% of statements     … +17 lines (ctrl+o to expand)⏺ Searched for 1 pattern (ctrl+o to expand)⏺ Bash(command -v claude >/dev/null 2>&1 && claude plugin list 2>/dev/null | grep -q "superpowers" && echo "INSTALLED" || echo "NOT_INSTALLED")  ⎿  INSTALLED⏺ ╔══════════════════════════════════════════════════╗  ║          Harness Health Report                   ║  ║          Project: claude-code-go                 ║  ║          Score: 10/100 (D)                       ║  ╠══════════════════════════════════════════════════╣  ║                                                  ║  ║  Category          Score   Status                ║  ║  ─────────────────────────────────────────────── ║  ║  Documentation      0/100  ░░░░░░░░░░  Poor      ║  ║  Architecture       0/100  ░░░░░░░░░░  Poor      ║  ║  Quality Rules      0/100  ░░░░░░░░░░  Poor      ║  ║  Test Coverage     50/100  █████░░░░░  Fair      ║  ║  Validation         0/100  ░░░░░░░░░░  Poor      ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Details                                         ║  ║  ─────────────────────────────────────────────── ║  ║  [x] .harness/docs/ARCHITECTURE.md              ║  ║  [x] .harness/docs/DEVELOPMENT.md               ║  ║  [x] .harness/docs/PRODUCT_SENSE.md             ║  ║  [x] .harness/scripts/lint-deps.go               ║  ║  [x] .harness/scripts/lint-quality.go            ║  ║  [x] .harness/scripts/validate.go                ║  ║                                                  ║  ║  Project Information:                            ║  ║  Language: Go 1.22.10                           ║  ║  Framework: cobra, bubbletea, lipgloss, glamour ║  ║  Total code: ~19,912 lines                       ║  ║  Test files: 41 test packages                    ║  ║                                                  ║  ║  Import Analysis:                                ║  ║  Total imports: 100+ blocks across codebase      ║  ║  Packages: 23 internal packages                 ║  ║  Potential violations: None detected            ║  ║  Circular dependencies: No                      ║  ║                                                  ║  ║  Test Coverage (selected):                      ║  ║  sandbox: 95.1% | pathutil: 88.4% | compact: 81.6%║  ║  cmdutil: 82.6% | permissions: 79.7%            ║  ║  agent: 68.0% | hooks: 66.0%                    ║  ║  api: 28.5% | memory: 22.8% | prompt: 21.1%    ║  ║  mcp: 5.6% | Several at 0%                       ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Recommendations                                 ║  ║  1. Run harness-apply to generate infrastructure ║  ║  2. Create ARCHITECTURE.md defining layer rules   ║  ║  3. Add lint-deps.go to enforce import boundaries ║  ║  4. Increase test coverage for api/mcp packages   ║  ║  5. Migrate .claude/rules/ to .harness/docs/      ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Toolchain                                       ║  ║                                                  ║  ║  [Installed] Superpowers — planning + review    ║  ║    Already installed, ready for integration      ║  ║                                                  ║  ║  [Recommended] harness-apply — generate harness  ║  ║    Why: Automated review-test-fix cycle for      ║  ║         continuous quality enforcement           ║  ║                                                  ║  ║  Recommended workflow:                           ║  ║  analyze → apply → develop → apply (loop) → ship ║  ║                                                  ║  ╚══════════════════════════════════════════════════╝  ---  Would you like to:  1. Run harness-apply to generate/update harness infrastructure  2. Review specific recommendations in detail  Choose an option or describe what you'd like to do next.
```

## 执行harness-apply

```swift
❯ /harness-pilot:harness-analyze                                                                                                               ⏺ I'm using harness-analyze to perform a dryrun analysis of this project.⏺ Bash(pwd)  ⎿  /Users/yangtong07/Desktop/code/llm-agent/claude-code-go⏺ Bash(git rev-parse --git-dir)  ⎿  .git⏺ Searched for 4 patterns, read 1 file (ctrl+o to expand)⏺ Bash(go test -cover ./... 2>&1 | grep -E "(^ok|^FAIL|coverage:)" | head -30)  ⎿     github.com/atom-yt/claude-code-go/cmd/claude            coverage: 0.0% of statements     ok         github.com/atom-yt/claude-code-go/internal/agent        (cached)        coverage: 68.0% of statements     ok         github.com/atom-yt/claude-code-go/internal/api  (cached)        coverage: 28.5% of statements     … +18 lines (ctrl+o to expand)⏺ Read 1 file (ctrl+o to expand)⏺ Bash(find . -name "*.go" -type f | xargs stat -f "%m" 2>/dev/null | sort -rn | head -1)  ⎿  1776924231⏺ Searched for 1 pattern (ctrl+o to expand)⏺ Bash(go run .harness/scripts/lint-deps.go 2>&1 | tail -20)  ⎿  ✓ No layer architecture violations found⏺ Bash(go run .harness/scripts/lint-quality.go 2>&1 | tail -20)  ⎿  ✓ No quality issues found⏺ Searched for 1 pattern (ctrl+o to expand)⏺ ╔══════════════════════════════════════════════════╗  ║          Harness Health Report                   ║  ║          Project: claude-code-go                 ║  ║          Score: 91/100 (A - Excellent)           ║  ╠══════════════════════════════════════════════════╣  ║                                                  ║  ║  Category          Score   Status                ║  ║  ─────────────────────────────────────────────── ║  ║  Documentation     100   ███████████  Excellent  ║  ║  Architecture      100   ███████████  Excellent  ║  ║  Quality Rules     100   ███████████  Excellent  ║  ║  Test Coverage      54   ██████░░░░░   Fair      ║  ║  Validation        100   ███████████  Excellent  ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Details                                         ║  ║  ─────────────────────────────────────────────── ║  ║  [✓] .harness/docs/ARCHITECTURE.md             ║  ║  [✓] .harness/docs/DEVELOPMENT.md              ║  ║  [✓] .harness/docs/PRODUCT_SENSE.md            ║  ║  [✓] .harness/scripts/lint-deps.go             ║  ║  [✓] .harness/scripts/lint-quality.go          ║  ║  [✓] .harness/scripts/validate.go              ║  ║                                                  ║  ║  Audit:                                          ║  ║  Documentation freshness: ⚠️  STALE (older than source)║  ║  Lint coverage: ✓ All directories in layer mapping║  ║  Layer violations: 0 found                      ║  ║  Quality issues: 0 found                         ║  ║                                                  ║  ║  Import Analysis:                                ║  ║  Total imports: 83+                              ║  ║  Test files: 37                                  ║  ║  Layer violations: 0                             ║  ║  Circular dependencies: None detected           ║  ║                                                  ║  ║  Test Coverage (Highlights):                     ║  ║  sandbox: 95.1%  | taskstore: 91.6%             ║  ║  pathutil: 88.4% | cmdutil: 82.6%               ║  ║  subagent: 90.2% | permissions: 79.7%           ║  ║  agent: 68.0%     | hooks: 66.0%                 ║  ║  ─────────────────────────────────────────────── ║  ║  ⚠️  Packages with 0% coverage:                    ║  ║  cmd/claude, internal/commands, internal/config, ║  ║  internal/mcpresource, internal/runtime,         ║  ║  internal/tools (parent package)                  ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Recommendations                                 ║  ║  1. Update ARCHITECTURE.md to reflect recent     ║  ║     source changes (websearch, planmode, etc.)  ║  ║  2. Add tests for 0% coverage packages:          ║  ║     - internal/config (settings logic)          ║  ║     - internal/commands (slash command handlers) ║  ║     - cmd/claude (CLI entry point)               ║  ║  3. Commit pending harness changes (capabilities, ║  ║     websearch_test.go, .harness/)                ║  ║                                                  ║  ╠══════════════════════════════════════════════════╣  ║  Toolchain                                       ║  ║  [Recommended] harness-apply — update harness +   ║  ║                quality loop (Ralph Wiggum Loop)  ║  ║    Why: Automated review-test-fix cycle for       ║  ║         continuous quality enforcement           ║  ║                                                  ║  ║  Recommended workflow:                           ║  ║  analyze → apply → develop → apply (loop) → ship ║  ╚══════════════════════════════════════════════════╝  Key Findings:  - Harness infrastructure is comprehensive and fully functional  - Layer architecture is clean (0 violations across 100+ files)  - Quality rules are enforced and passing  - Main gap: Test coverage is uneven — 6 packages at 0%  - Documentation needs refresh to capture recent features (websearch, subagent, planmode, taskstore, runtime)  ---  Would you like to:  1. Run harness-apply to update harness infrastructure (refresh stale docs)  2. Review specific recommendations in detailProceed
  Choose an option or describe what you'd like to do next.✻ Cogitated for 3m 27s❯ /harness-pilot:harness-analyze                                                                                                               ⏺ I've already completed the harness-analyze dryrun analysis for this project (see the health report above).                                                                                                                                    Summary:  - Score: 91/100 (A - Excellent)                                                                                                                - Documentation: ✓ Complete (ARCHITECTURE.md, DEVELOPMENT.md, PRODUCT_SENSE.md)  - Architecture: ✓ Clean (0 layer violations)                                                                                                   - Quality Rules: ✓ Passing                                        - Validation: ✓ All 5/5 checks passing  - Test Coverage: ⚠️  Mixed (54% average, 6 packages at 0%)  Audit Findings:  - Documentation is stale — ARCHITECTURE.md older than latest source changes  - Layer violations: 0  - Quality issues: 0  ---  Would you like to:  1. Run harness-apply to refresh the stale documentation and update harness  2. Review specific recommendations in detailProceed
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy5LE9nkTIzFCNATNPFrvRdMM4xviaVL0MKRmlNXyRmAgTib3rc3ric3ibicSnYqYXFiaLpxW3p0w1JCHlhxCricsU4MN9YIvQ9mCqUjSk/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy74fhicx56ZdjNIV9IOVGibC9ciceWWAm6MtkmrZlRyMpMLibjpsECrxM3v2Ro5ZoKe34rKMPZvLe8Oz8SkicUroTMdg6XMDibMicSD2s/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy7XbrBVGjcI2VM42Ht5PlPcQh9S3G9iaTXnEEIjTN3BRkrABMPAQ2emc16ATSnkXhBwe7iaTJfHibChic8GqpavVJ4BbzKqQYm2RiaU/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D0qMsFCrMy70ocfiaATv2aibIsKIEe8vmatPWHmt0Qd7v0PiaTV7CCcpsvHkI4ZGY2jhXoVNvdxEzUzZue6ImoLuxWlNCEWUsCVQKRS7NFRH9g/640?wx_fmt=jpeg&from=appmsg) ![](https://mmbiz.qpic.cn/mmbiz_jpg/D0qMsFCrMy7gicyjnBf6cUdRudcLdxVX17DSxrQNLQ5A7BlNdgmqksgNrAP6j5cren1BqxhOOjm0Q91jyjhx7AnEO5SwSHHwfFFv2WAx2f8M/640?wx_fmt=jpeg&from=appmsg)

END

**推荐阅读**

[Superpowers：给 Claude Code 装上“工程大脑”](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607138&idx=1&sn=747cfb219a8dbda0249991af5b6eb7f1&scene=21#wechat_redirect)

[如何利用 Harness “一句话交付产品功能”？](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607090&idx=1&sn=7ffb7af71f8cc537005dcb4e987cb060&scene=21#wechat_redirect)

[CodingAgent 的原始森林困境：一张地图能解决什么？](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607050&idx=1&sn=f75138b649a0a568aa8c60c574d32c5f&scene=21#wechat_redirect)

[电商搜索H1提升AI-Coding质量实践 RD & QA](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247607023&idx=1&sn=abb96ea9a094246d2156cf5054719ac7&scene=21#wechat_redirect)

[用数据说话：贴吧 AI CR（小码哥）落地 10 周，bug密度下降 66.87%](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247606943&idx=1&sn=805a8afb96422f9aafbf909919df8faf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

继续滑动看下一个

百度Geek说

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过