# 万字深读 DeepSeek Harness：没有特权核心，万物皆插件？Agent 架构新范式揭秘

**作者**: 技术方舟

**来源**: https://mp.weixin.qq.com/s/tFS0DiC1oX7HPjJyY2HEUA

---

## 摘要

模型适配器硬编码在核心循环里，工具函数散落在各个角落，状态管理靠全局变量维持。当你想要换一个 LLM 提供商（比如从 OpenAI 切换到 DeepSeek），或者把本地执行改成远程沙箱时，你会发现牵一发而动全身——你需要修改核心逻辑，甚至重构整个项目。

---

## 正文

技术方舟 技术方舟

在小说阅读器读本章

去阅读

## 引言：Agent 开发的“混乱时代”，我们需要什么样的基础设施？

如果你最近尝试过构建一个稍微复杂一点的 AI Agent（智能体），你大概率经历过这样的痛苦循环：

起初，它只是一个简单的 Python 脚本，调用 LLM API，打印结果。一切都很美好，代码只有几十行。接着，你需要它读取文件、执行代码、搜索网页。于是，你在脚本里塞进了 `os` 、 `subprocess` 、 `requests` 。代码变成了几百行。然后，为了安全，你加了沙箱；为了记忆，你接了向量数据库；为了多步推理，你写了复杂的循环逻辑和状态机。很快，你的代码变成了一团“意大利面条”。模型适配器硬编码在核心循环里，工具函数散落在各个角落，状态管理靠全局变量维持。

当你想要换一个 LLM 提供商（比如从 OpenAI 切换到 DeepSeek），或者把本地执行改成远程沙箱时，你会发现牵一发而动全身——你需要修改核心逻辑，甚至重构整个项目。更糟糕的是，当 Agent 出现幻觉或错误行为时，你很难追溯它到底是在哪一步、基于什么上下文做出的决策。

这就是当前 Agent 开发领域的普遍现状： **缺乏统一的基础设施，过度依赖临时脚本，架构脆弱且难以扩展。** 我们拥有了强大的模型，却还在用石器时代的工具来驾驭它们。

然而，就在最近，DeepSeek AI 开源了一个名为 **DeepSeek Harness (`dsh`)** 的项目。与市面上大多数“玩具级”的 Agent 框架不同， `dsh` 展现出了惊人的工程成熟度。截至分析时，它已经积累了超过 **12,404 次提交** ，拥有完整的 Monorepo 结构、严格的 CI/CD 门禁、以及一套名为 Cordis 的底层运行时框架。

更令人震撼的是它的核心理念： **“没有特权核心，万物皆插件” (No Privileged Core, Everything is a Plugin)。**

这意味着什么？

- 意味着在 `dsh` 中，连 Agent 的核心循环本身都是一个可替换的插件；
- 意味着你可以通过配置而非代码修改，将 Agent 从本地环境无缝迁移到隔离沙箱；
- 意味着它试图用软件工程的严谨性（类型安全、事件驱动、依赖注入），来驯服 AI 的不确定性。

本文将基于对 `deepseek-harness` 仓库的深度分析，为你揭开这套架构的神秘面纱。我们将深入探讨它的“能力接缝”设计、Turn/Step 生命周期管理、Host/Client 分离架构，以及它对未来的 Agent 开发意味着什么。无论你是架构师、后端工程师，还是 AI 应用开发者，这篇万字长文都将为你提供全新的视角和实战启示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IIn51j6BmCZ5sZmwRCJ4xSWU6d0gnlXb3mcfoeY5eeKskMmaSa1Cx7oK7wIYXToJ8aylDCIqGATFo2jVux9TDLaXicQYtrUhl1vxhK19iawIo/640?wx_fmt=png&from=appmsg)

---

## 一、 哲学重构：“万物皆插件”与 Cordis 范式

要真正理解 DeepSeek Harness (`dsh`)，不能只看它的代码结构，必须首先理解它的灵魂—— **Cordis** 。

在传统的软件架构中，我们习惯于“核心 + 扩展”的模式：有一个稳定的内核（Core），负责调度、路由和生命周期管理；有一堆插件（Plugins），负责具体业务逻辑。内核拥有最高权限，插件只能被动响应。这种模式在单体应用或简单的微服务中很有效，但在 Agent 领域却显得僵化且危险。

Agent 的行为是动态的、不可预测的，它需要一种更灵活、更具组合性的架构。如果核心代码写死了“必须先调用搜索工具再总结”，那么当我们需要一个“先规划再执行”的 Agent 时，就必须修改核心代码。这在大型系统中是不可接受的。

`dsh` 选择了另一条路： **去中心化** 。

### 1.1 什么是“没有特权核心”？

在 `dsh` 中，没有任何代码片段拥有“上帝视角”。

- **模型适配器** 是插件：你可以随时替换底层的 LLM 实现。
- **工具注册表** 是插件：工具的发现、加载和执行策略都是可插拔的。
- **会话日志系统** 是插件：存储后端可以是 JSONL，也可以是 SQLite，甚至远程数据库。
- 甚至 **Agent Loop（智能体循环）** 本身，也是一个插件。

这种设计带来的最大好处是： **极致的可替换性** 。如果你想改变 Agent 的行为模式（例如从“单步执行”改为“并行规划”，或者引入一个全新的反思机制），你不需要去修改框架的核心代码，只需要加载一个不同的 `agent-loop` 插件即可。核心框架只负责提供运行环境（Context Bus），而不干涉业务逻辑。

### 1.2 Cordis：时空组合性的编程范式

支撑这一理念的是 **Cordis** 框架。根据官方文档，Cordis 的设计灵感源自论文《A Programming Paradigm for Spatiotemporal Composability》（一种用于时空组合性的编程范式）。虽然名字听起来很学术，但其核心思想非常直观且强大：

1. **Context Bus (上下文总线)** ：所有插件通过一个共享的 `ctx` 对象进行通信。这个 Context 不是简单的全局变量，而是一个类型化的服务注册表。
2. **Effect (效果/副作用)** ：插件通过 `ctx.effect()` 注册副作用（如启动 HTTP 服务器、监听文件系统变化）。当插件卸载时，这些副作用会自动回退（Cleanup），确保环境干净。这解决了传统插件系统中常见的“资源泄漏”问题。
3. **Event (事件)** ：插件通过 `ctx.on()` 监听类型化事件。事件是解耦的关键，发布者不需要知道订阅者是谁。
4. **Waterfall (瀑布流)** ：插件可以通过 `ctx.waterfall()` 注册拦截器，形成处理链。这对于实现审批流程、安全检查和日志记录至关重要。

这种机制使得插件之间 **解耦但协同** 。它们不需要知道彼此的存在，只需要约定好 Context 中的 Key（键）和事件的 Schema（模式）。

### 1.3 Profile & Bundle：组合的艺术

既然一切皆插件，那么如何组装一个可用的 Agent？ `dsh` 引入了 **Profile** 和 **Bundle** 的概念，这类似于操作系统的“发行版”或 Docker 的“镜像层”。

- **Bundle (捆绑包)** ：是 Cordis 配置行的分发格式，包含一组相关的插件及其依赖。例如 `dsh-base` （基础能力）、 `dsh-web-app` （Web UI）。
- **Profile (配置文件)** ：是一个命名的组合，定义了加载哪些 Bundle，以及它们的顺序。

这种设计允许用户通过简单的 YAML 配置（ `cordis.patch.yml` ）来定制 Agent。你可以创建一个“开发模式 Profile”，加载本地调试工具和详细日志；也可以创建一个“生产模式 Profile”，加载远程沙箱、监控插件和精简日志。 **代码不变，行为万变。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IIn51j6BmCbFDjz896nWFvup8XY677wx6h9SA9Bxl6EYHicISz5hib07MgwN7nEvEcfj2ZBqG3od4TzjI0lOeSDVPa9bjpe5HHSCd2kNzhWAo/640?wx_fmt=png&from=appmsg)

---

## 二、 架构核心：能力接缝 (Capability Seams) 的设计智慧

如果说 Cordis 是 `dsh` 的骨架，那么 **能力接缝 (Capability Seams)** 就是它的灵魂。这是整个架构中最具创新性的设计模式之一，也是解决 Agent “扩展性难题”的关键钥匙。

### 2.1 什么是“能力接缝”？

在 `dsh` 中，“接缝”不是一个物理接口，而是一个 **逻辑插槽** 。它定义了一种可替换的能力，包含三个角色：

1. **Service Definition (服务定义)** ：声明接口。例如：“我需要读取文件”。
2. **Service Provider (服务提供者)** ：实现接口。例如：“我用 Node.js `fs` 模块读取”或“我通过 SSH 远程读取”。
3. **Consumer (消费者)** ：使用接口。通常是暴露给 LLM 的工具（Tools）。

**关键点在于：** Consumer 只依赖 Service Definition，完全不关心 Provider 是谁。Provider 通过 Cordis Context (`ctx`) 动态注入。这种模式类似于依赖注入（DI），但更加灵活和运行时化。

### 2.2 案例解析：从本地执行到远程沙箱的无缝切换

让我们通过一个具体的例子来理解 Seam 的威力。假设你的 Agent 需要执行 Bash 命令和读写文件。

**传统架构的做法：**

- `bash_tool.py` 直接调用 `subprocess.run()` 。
- `file_tool.py` 直接调用 `open()` 。
- 如果你想把执行环境从本地改为 Docker 容器，你需要修改这两个工具的所有代码，让它们连接 Docker API。 **牵一发而动全身，且容易引入 Bug。**

**dsh (Seam) 的做法：**

1. **定义接缝** ：核心包定义了 `ctx.fs` （文件系统）和 `ctx.subprocess` （子进程）接口。
2. **默认 Provider** ：在本地模式下，加载 `LocalFsProvider` 和 `LocalSubprocessProvider` 。Bash 工具和文件工具从 `ctx` 中获取这些服务并调用。
3. **切换环境** ：当你想要沙箱化时，你只需要加载一个 `RemoteSandboxProvider` 插件。这个插件接管了 `ctx.fs` 和 `ctx.subprocess` ，将其指向容器内部。
4. **结果** ： **Bash 工具和文件工具无需修改任何代码** ，它们自动开始通过远程接口操作沙箱内的文件系统。 **这就是“能力接缝”的魔力：替换 Provider，即可改变整个产品的行为边界。**

### 2.3 关键能力接缝清单

`dsh` 定义了约 15 个主要的能力接缝，覆盖了 Agent 的核心需求。以下是其中几个关键的：

| 接缝名称 | Context Key | 说明 |
| --- | --- | --- |
| **Shell/Bash** | `ctx.shell` | Bash 命令执行器。支持本地、远程、沙箱等多种 Provider。 |
| **Terminal/PTY** | `ctx.terminals` | 持久化终端会话，用于交互式程序（如 vim, top）。 |
| **Sandbox** | `ctx.sandbox` | 进程隔离策略，集成 Landlock (Linux)、Seatbelt (macOS) 等安全机制。 |
| **Filesystem** | `ctx.fs` | 文件读写操作，支持本地、远程、只读等多种模式。 |
| **LSP** | `ctx.lsp` | 代码导航与智能提示，通过 stdio provider 连接语言服务器。 |
| **Web** | `ctx.web` | 网页搜索与抓取能力。 |

这种设计使得 `dsh` 具有极强的适应性。无论是用于本地开发辅助，还是云端自动化运维，只需调整接缝的 Provider 即可。

### 2.4 架构图解：Seam 的工作流

为了更直观地展示 Seam 的工作原理，我们绘制了以下 PlantUML 组件图：

![](https://mmbiz.qpic.cn/mmbiz_png/IIn51j6BmCZdqTBMia7dRPQYmoTJRcJwjsfyXup131Brz55ogUOpI2griaFn3nshH2iaG4sBxJroj6qFPibKKesVL2pzkSdDRkKEmhicibDUyOyxE/640?wx_fmt=png&from=appmsg)

---

## 三、 生命周期引擎：Turn/Step 流转与状态一致性

Agent 的运行不是线性的，而是循环的、交互式的。如何管理这种复杂的流程？ `dsh` 定义了一套严谨的 **Turn (轮次)** 和 **Step (步骤)** 生命周期模型。这不仅是业务逻辑的实现，更是保证 Agent 行为可预测、可恢复的基础。

### 3.1 Turn vs Step：核心概念辨析

在深入流程之前，必须明确这两个基本单位的关系：

- **Step (步骤)** ： **原子操作单元** 。
- 包含一次模型请求（LLM Request）及其调用的所有工具执行。
	- 它是 Agent “思考并行动”的最小闭环。
	- *例如* ：Agent 收到问题 -> 调用搜索工具 -> 返回结果，这是一个 Step。
- **Turn (轮次)** ： **交互会话单元** 。
- 由零个或多个 Step 组成。
	- **起点** ：从第一个输入被认领（Claimed）开始。
	- **终点** ：当系统“不再欠债”时关闭（即没有待处理的工具结果，也没有新的用户输入）。
	- *例如* ：用户提问 -> Agent 搜索 (Step 1) -> Agent 总结回答 (Step 2)。这整个过程属于同一个 Turn。

> **关键理解** ：一个 Turn 可以包含多个 Step。这种分离使得系统可以精细地控制成本（按 Step 计费）和交互粒度（按 Turn 管理会话）。

### 3.2 完整流转逻辑图解

根据 `dsh` 的架构文档，一个标准的 Turn/Step 生命周期如下所示。请注意其中的 **拦截点 (Waterfall)** ，这是插件扩展的关键位置。

![](https://mmbiz.qpic.cn/mmbiz_png/IIn51j6BmCbRa1Kma0TfJ4pOwOWASkXIALmcToEfqPklPNicayGxfjQcWQf9vKFb6678gfsl1WO4jcTYo0GayLPxL9ickHWgSicRNeWUBOlsbk/640?wx_fmt=png&from=appmsg)

### 3.3 核心设计原则：“模型可见即日志”

`dsh` 有一个极其重要的不变量（Invariant）： **“Model-visible means logged”** 。

这意味着：任何到达模型请求的内容，必须可以从 Session Log（会话日志）中重建。运行时系统会断言这一点。

- **为什么这么做？**
- **崩溃恢复** ：如果 Agent 运行中途崩溃，重启后可以从日志完美重建上下文，继续之前的任务。
	- **一致性** ：Fork、Resume、遥测都基于同一份日志源，避免状态漂移。
	- **可观测性** ：你可以精确地知道模型在每一步看到了什么，便于调试和审计。

### 3.4 deriveMessages()：从日志推导历史

Agent 不维护内存中的对话状态（如一个巨大的数组）。每次 Step 开始时，系统调用 `deriveMessages()` ，从 Session Log（JSONL）中重新投影出模型历史。

- **好处** ：消除了“内存状态”与“持久化状态”不一致的风险。
- **代价** ：需要高效的日志查询机制（ `dsh` 使用 SQLite FTS 进行语义过滤和全文搜索）。

---

## 四、 Host/Client 双面架构与 Typert RPC

为了支持 Web UI 和命令行两种模式，同时保证类型安全， `dsh` 采用了 **Host/Client 分离** 的架构。

### 4.1 为什么分离？

- **Host (服务端)** ：运行在 Node.js 环境，负责 API Gateway、HTTP 路由、核心 Agent 逻辑、工具执行。
- **Client (浏览器端)** ：运行在 React 中，负责 UI 渲染、用户交互。

两者通过 **Typert RPC** 桥接。这种分离带来了两个好处：

1. **安全性** ：敏感的工具执行（如文件读写）只在 Host 侧进行，Client 无法直接访问文件系统。
2. **类型安全** ：Host 构建时生成类型声明，Client 自动获取这些类型，确保前后端接口一致。

### 4.2 TypeScript Solution Graph (双聚合)

`dsh` 维护两个独立的 TypeScript 聚合程序（Aggregates）：

- `tsconfig.host.json` ：针对 Node.js 服务端。
- `tsconfig.client.json` ：针对浏览器端。

**设计纪律** ：这两个聚合在 Cordis Context 接口上进行声明合并，但键不同。如果一个程序同时看到两个合并，会报告冲突。这种“故意制造冲突”的设计，确保了 Host 和 Client 的代码不会意外混用，强制开发者遵循边界。

### 4.3 Typert RPC 机制

Typert 是 `dsh` 自研的 RPC 类型生成系统：

1. Host 定义服务接口（如 `getSessions()` ）。
2. 构建时，Typert 生成 Host-for-Client 的类型声明和运行时贡献。
3. Client 通过 `api-remotes` 加载这些贡献到 `ctx.remote` 命名空间下。

这使得前端调用后端 API 就像调用本地函数一样自然，且拥有完整的 IDE 自动补全支持。

![](https://mmbiz.qpic.cn/mmbiz_png/IIn51j6BmCbkzbRmgq4bZXammM6reFNaBpRrVZq6K2c6g5rHCcIlzZIPgO6MhjxMZbrANpOun7icHVESG9oM0YlMIVzportMg6ibicj16AMNH0/640?wx_fmt=png&from=appmsg)

---

## 五、 工程卓越：12,404 次提交背后的质量门禁

在 AI 开源项目中，代码质量参差不齐是常态。很多项目只有几个脚本文件，缺乏测试和文档。但 `dsh` 不同，它展现出了 **企业级软件** 的工程素养。

### 5.1 技术栈选型：前沿且严格

- **TypeScript 6.x + Node.js 22+ / 24+** ：
- 使用最新的语言特性，确保类型安全和性能。
	- `engines` 字段严格限制版本范围，避免环境差异导致的 Bug。
- **pnpm workspace (Monorepo)** ：
- 管理 100+ 个工作区包，跨 38 个能力组。
	- 利用 pnpm 的硬链接机制，节省磁盘空间并加速安装。

### 5.2 测试矩阵：7 套 Vitest 配置

`dsh` 没有依赖单一的测试脚本，而是建立了分层测试体系：

1. **Unit Tests** ：单元测试，覆盖核心逻辑。
2. **E2E Tests** ：端到端测试，模拟真实用户交互。
3. **Snapshot Tests** ：快照测试，确保输出格式稳定。
4. **Web Tests** ：针对 Web UI 的测试。
5. **Stress/Perf Tests** ：压力与性能测试，评估高负载下的表现。
6. **GUI Tests** ：图形界面自动化测试。

这种覆盖度在 AI 框架中极为罕见，表明团队对稳定性的极高要求。

### 5.3 Lint & Quality：Oxlint-only 工作流

- **Oxlint** ：唯一的 Lint 工具，基于 Rust 编写，速度极快。
- **Knip** ：死代码检测，确保没有无用的依赖和文件。
- **Jscpd** ：重复代码检测，保持代码库的整洁。
- **Git Hooks (lefthook)** ：在 `pre-commit` 、 `pre-push` 阶段自动运行检查，阻止低质量代码入库。

### 5.4 自动化脚本体系

仓库 `scripts/` 目录包含 **50+** 自动化脚本，覆盖：

- **构建** ： `run-gates.ts`, `clean.ts`
- **发布** ： `release/bump.ts`, `publish.ts` （支持 npm 和 PyPI 双轨发布）
- **验证** ：20+ `verify-*.ts` 脚本（包路径、不变量、doc 链接、Mermaid/PlantUML 语法等）

这种高度的自动化，使得维护这样一个庞大的 Monorepo 成为可能。

---

## 六、 落地评估：风险清单与企业级应用建议

尽管 `dsh` 展现了极高的技术水准，但在企业级落地时，仍需保持理性。基于分析报告，我们梳理了以下风险与建议。

### 6.1 主要风险 (Risks)

1. **Developer Preview 不稳定性** ：
- 当前版本为 `0.1.0-rc.7` ，官方明确声明会有破坏性变更（Breaking Changes）。
	- **影响** ：直接用于生产环境存在 API 破裂风险。
3. **外部贡献暂不可行** ：
- `CONTRIBUTING.md` 指出目前不接受外部 PR。
	- **影响** ：社区修复 Bug 的速度受限，生态增长可能放缓。
5. **Bus Factor (关键人员依赖)** ：
- 核心知识可能集中于少数维护者（如 imccyu）。
	- **影响** ：若核心团队变动，项目维护可能受阻。
7. **技术栈前沿性** ：
- 依赖 TypeScript 6.x 和 Node.js 22+。
	- **影响** ：部分企业的旧版基础设施可能需要升级才能支持。

### 6.2 企业级落地建议 (Mitigation Strategies)

针对上述风险，我们提出以下缓解措施：

1. **建立内部适配层 (Adapter Pattern)** ：
- 不要直接在业务代码中深度耦合 dsh 的内部 API。开发一个内部的“Agent SDK”或中间件层，封装对 `dsh` 的调用。当 dsh 升级时，只需修改适配层。
3. **利用插件机制进行外围扩展** ：
- 既然不能改核心代码，就通过编写高质量的 **外部插件（Plugins）** 来实现企业定制需求（如私有知识库、内部审批流）。这符合“万物皆插件”的理念。
5. **严格的版本锁定与灰度发布** ：
- 在 `package.json` 中严格锁定版本号。建立自动化测试流水线，每次 dsh 发布新版本时，先在非核心业务线进行回归测试。
7. **沙箱环境隔离运行** ：
- 利用 dsh 自身的 `sandbox` 能力（Landlock/bwrap），将 Agent 进程严格限制在容器或沙箱中运行，防止框架的不稳定行为影响宿主机。
9. **等待 v1.0 正式版** ：
- 对于核心业务流，建议等待官方发布 `v1.0` 并开放外部贡献后，再大规模引入。

---

## 结语：Agent 基础设施的“成人礼”？

DeepSeek Harness (`dsh`) 的出现，或许标志着 Agent 开发正在从“脚本时代”迈向“工程时代”。

它不仅仅是一个工具库，更是一套 **方法论** 。它告诉我们：

- Agent 架构应该是 **去中心化** 的，没有特权核心。
- 扩展性应该通过 **标准化的接缝 (Seams)** 来实现，而非硬编码。
- 可靠性应该建立在 **严格的日志不变量** 和 **类型安全** 之上。

虽然目前它还处于 Developer Preview 阶段，存在诸多不确定性，但其展现出的工程深度和设计哲学，已经足以让每一位 AI 开发者深思。

未来，随着 v1.0 的发布和社区生态的完善， `dsh` 有望成为构建企业级 Agent 应用的首选底座之一。而对于我们而言，现在正是深入研究、提前布局的最佳时机。

**你准备好拥抱“万物皆插件”的 Agent 新范式了吗？**

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过