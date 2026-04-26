# AI 编程工作流选型指南：Spec-Kit、OpenSpec、Superpowers、Spec-First 全面对比（附实操落地路径）

**作者**: 智能体AI

**来源**: https://mp.weixin.qq.com/s/FlmWZGWom1TZNsYJFTejZg

---

## 摘要

文章指出，AI 编程的核心瓶颈不是 prompt，而是缺少规范驱动工作流；应先明确做什么、为什么做、怎么做，再让 AI 写代码。spec-first 是理念，Spec-Kit 和 OpenSpec 管规范，Superpowers 管执行，适合不同复杂度与团队场景。

---

## 正文

我有个朋友，做了十年后端开发。去年他跟我说，用上 Cursor 之后效率翻了三倍，代码写得飞快。
上个月再聊，他有点沮丧：AI 写的代码越来越难维护，改一个地方出三个问题，有时候同一个逻辑前后不一致，跑起来也没问题，但下次接手的人（包括他自己）完全不知道这段代码为什么这么写。
他问我："是不是我的 prompt 写得不够好？"
不是。
问题不在 prompt，在于根本没有工作流。
一、大家都没聊的问题：AI 编程的瓶颈
过去两年，AI 编程工具的进化路径大概是这样的：
第一阶段
，你学会用 Copilot 补全代码，感叹"哇，真方便"。
第二阶段
，你开始用 Cursor 或 Claude Code 做稍微复杂的功能，AI 能写、能改、能调 bug。
第三阶段
，你开始做超过三个文件的项目，然后你发现——AI 越跑越偏，第 100 行代码和第 10 行的逻辑开始矛盾，上下文一长就开始"失忆"，你花在修正 AI 输出上的时间，比直接写代码还多。
这就是所谓的 
Vibe Coding 瓶颈
。不是模型不够聪明，而是你在让一个"能力极强但极度字面意思"的家伙在没有图纸的情况下盖房子。
解法其实早有人想清楚了：
在写第一行代码之前，先把"做什么、为什么做、怎么做"说清楚
。这套方法论叫做规范驱动开发（Spec-Driven Development，SDD）。
2025 年下半年到 2026 年，围绕 SDD 理念，社区涌现出一批非常优秀的工具。今天要聊的四个，是目前讨论度最高、实际可落地的选项：Spec-Kit、OpenSpec、Superpowers，以及作为底层理念的 spec-first。
二、先建立认知地图：这四个东西不是同一类
很多人第一次看到这几个名字，会以为它们是"功能类似、选一个就行"的竞品关系。
实际上差远了。
打个比方：你要建一栋楼。
Spec-Kit
 是建筑规范手册，规定了"什么材料、什么标准、什么流程，必须照做"
OpenSpec
 是施工变更单，记录了"这次改动了什么、为什么改、改到哪里"
Superpowers
 是施工队的操作手册，规定了"工人怎么干活、先干什么后干什么、验收标准是什么"
spec-first
 是一种建筑哲学："先画图纸，再动砖头"
它们解决的问题不一样，所在的层次也不一样：
spec-
first
（理念层）
       ↓
Spec-Kit / OpenSpec（规范管理层）
       ↓
Superpowers（执行纪律层）
理解了这个分层，你才能知道自己到底缺哪一块。
三、Spec-Kit：GitHub 官方出品，"宪法派"的代表
如果只能记住一句话，就把这句记住：
 这里的开发，有法可依。
Spec-Kit 是 GitHub 官方在 2025 年推出的开源工具包，专为 AI 辅助编程设计，核心思想是"规范先行"——先精确定义做什么和为什么，再由 AI 基于清晰的规范生成代码。
它的工作流分五个阶段，严格按顺序推进：
Constitution（宪法）
    → Specify（功能规范）
    → Plan（技术方案）
    → Tasks（任务拆解）
    → Implement（代码实现）
其中最有意思的是第一步 
Constitution
。
这份"宪法"文件定义了项目的最高原则，比如测试覆盖率要求、代码风格、技术栈限制、安全策略等。一旦写进去，后续所有 AI 的行为都要以此为约束，不可逾越。
一个实际的例子，宪法里可以写：
#
 项目宪法
#
# 技术标准
- 前端：React + TypeScript
- 后端：Node.js，禁止引入 ORM 以外的数据库抽象层
#
# 质量要求
- 单元测试覆盖率 ≥ 85%
- 所有 API 必须有错误处理
#
# 简化原则
- 初始实现特性数 ≤ 3，多一个要写说明理由
AI 在整个开发过程中都要遵守这些原则，不会因为你一时的 prompt 就跑偏。
适合谁？
复杂的新建项目、对合规性有要求的企业场景，或者团队协作中需要统一标准的情况。项目越复杂，前期投入的回报越高——经验来看，超过 3-5 个模块的项目，用 Spec-Kit 的系统化规划能在后续执行阶段节省大量返工时间。
不适合谁？
快速迭代的小需求、已有代码库的局部改动，以及不想搭 Python 环境的朋友（Spec-Kit 依赖 uv 包管理器）。
有人用完 Spec-Kit 的感受是"一片 Markdown 的海洋"——确实，它很重，前期要写大量文档。如果你的项目本身就不复杂，这个成本可能超过收益。
上手命令：
pip install uv
git 
clone
 https:
//github.com/github/spec-kit.git
# 在 Claude Code 中依次执行：
/speckit.constitution
/speckit.specify 
"用户登录功能，邮箱密码验证，返回JWT"
/speckit.plan
/speckit.tasks
/speckit.implement
四、OpenSpec：轻量敏捷，专门为存量项目设计
如果只能记住一句话，就把这句记住
：
 这里的变更，有据可查。
OpenSpec 来自 Fission-AI 团队，定位很明确：为
已有项目
提供低侵入性的规范层，在改需求之前先把"要改什么、为什么改"讲清楚。
它最核心的设计是 
Delta Specs（增量规范）
：把"当前项目的事实"和"这次的变更提案"明确分开存放。
目录结构大概是这样：
openspec/
├── specs/          
# 当前项目的真相（已建立的能力）
└── changes/        
# 变更提案（准备改的东西）
    └── 
add
-dark-mode/
        ├── proposal.md   
# 为什么改、改什么
        ├── specs/        
# 这次涉及的规范变更
        ├── design.md     
# 技术方案
        └── tasks.md      
# 任务清单
每次改需求，都是一个独立的"变更单"。改完之后执行 archive，变更合并回主规范库，历史可查。
这个设计解决了一个很实际的问题：
规范不会随着项目演进而失真
。很多团队的文档最大问题就是，写完就扔，代码改了文档没改，两边越来越对不上。OpenSpec 通过强制的"归档"步骤，让规范始终跟着代码走。
它还有一个亮点：支持 25+ 种 AI 工具，零 API 密钥，完全用你本地已有的工具。
适合谁？
存量项目维护、需求频繁迭代的中小团队、个人开发者。特别是那种"已经有一堆代码，但没有任何规范文档，想补上又不知道从哪里下手"的场景，用 OpenSpec 可以从下一个需求开始，渐进式地把规范建立起来。
上手命令：
npm 
install
 -g openspec-cn  # 推荐中文版
cd your-
project
openspec init
# 在 
Cursor
 或 Claude Code 中：
/opsx:
new
 
add
-dark-
mode
        # 创建新变更
/opsx:ff                       # 快进，自动生成所有文档
/opsx:
apply
                    # 执行实现
/opsx:
archive
                  # 归档，更新主规范库
五、Superpowers：不管规范，只管行为纪律
如果只能记住一句话，就把这句记住
：
 这里的代码质量，有保证。
Superpowers 跟前两个都不一样。它不关心你写没写规范文档，它关心的是：
AI 在执行的时候有没有按照工程最佳实践来干活。
这是 Jesse Vincent（GitHub ID：obra）在 2025 年 10 月开源的项目，进入 Anthropic 官方插件市场后迅速爆发，目前 Star 数已经突破 15 万，是同期增长最快的开发工具之一。
它的核心理念是 
Process over Prompt（流程大于提示词）
：与其给 AI 写更精准的 prompt，不如给 AI 套上一套工程纪律，让它像有经验的工程师一样工作。
安装之后，AI 在处理任何超过 50 行代码的任务时，都会强制走这套流程：
brainstorming（需求澄清）
    → git worktrees（创建隔离分支）
    → writing-plans（拆成 
2
-
5
 分钟粒度的任务）
    → TDD（先写测试，再写实现）
    → subagent execution（子代理并行执行）
    → code review（双阶段审查）
    → 
finish
 branch（验收，处理分支）
最有意思的是 
TDD 强制
这一步。AI 必须先写出"会失败的测试"，再写实现代码让测试通过，最后重构。任何试图跳过这一步的 prompt，Superpowers 都会拒绝执行，并解释为什么。
关于 Token 消耗的问题：完整跑下来确实比直接写代码多消耗 10-20% 的 Token，但返工减少了 60-70%。算总账是划算的。
适合谁？
Claude Code 重度用户、对代码质量有硬性要求的正式项目、想让 AI 产出"能上线"而不只是"能运行"的代码的开发者。
注意：
 Superpowers 本身不负责管理规范文档，它只管执行时的行为约束。所以它最好跟 OpenSpec 或 Spec-Kit 配合使用：前者负责"做什么"，后者负责"怎么做好"。
上手命令：
# 在 Claude Code 中执行：
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
# 重启 Claude Code 后，使用：
/superpowers:brainstorm     
# 从需求澄清开始
/superpowers:write-plan     
# 生成执行计划
/superpowers:execute-plan   
# 开始执行
中文用户也可以用增强版，支持更多国内工具：
npm 
install
 -g superpowers-zh
六、spec-first：一种理念，不是工具
前三个都是具体工具，spec-first 是它们共同的底层哲学，值得单独说一下。
它的核心很简单：
在写第一行代码之前，先把以下四件事写清楚。
#
# 做什么（What）
用户可以用邮箱+密码登录，登录成功返回 JWT token
#
# 为什么做（Why）
现在没有认证机制，所有接口都是裸露的
#
# 约束（Constraints）
- 密码必须 bcrypt 加密
- 连续 5 次失败锁定 15 分钟
- token 有效期 7 天
#
# 非目标（Non-Goals）—— 这条最重要
- v1 不做 OAuth 第三方登录
- v1 不做手机号登录
- 不做"记住我"功能
"非目标"这一栏是整个 spec-first 里最有价值的部分。
 它明确告诉 AI"不要做什么"，这比告诉它"要做什么"更重要。很多时候 AI 跑偏，是因为它太"积极"了，总想帮你把没说到的边角案例也一起实现。
不想装任何额外工具？用 spec-first 理念也完全可以上手：
在项目根目录维护一个 
AGENTS.md
 文件，写上你的项目约束和 AI 行为规范。每次开新会话，先粘贴你的需求模板，把"做什么/为什么/约束/非目标"填完，再开始跟 AI 对话。
成本极低，效果立竿见影。
七、横向对比：帮你快速做决定
选型决策，直接用这棵树：
你的情况是什么？
│
├─ 全新项目 + 团队 ≥ 
3
 人 + 流程要正规
│       └─→  Spec-Kit
│
├─ 已有代码库 + 要加新功能或局部重构
│       └─→  OpenSpec
│
├─ 主要用 Claude Code + 想提升代码工程质量
│       └─→  Superpowers
│
├─ 先感受一下 SDD 是什么，不想装工具
│       └─→  spec-
first
（AGENTS.md 即可）
│
└─ 想要最强组合？
        └─→  OpenSpec（规划对齐）+ Superpowers（执行纪律）
             这是目前社区最推荐的黄金搭档
八、实操：用黄金搭档开发一个登录功能
下面是 OpenSpec + Superpowers 组合的完整实战流程，一步步跟着来。
第一步：安装
npm 
install
 -g openspec-cn
# 在 Claude Code 中：
/
plugin
 marketplace 
add
 obra/superpowers-marketplace
/
plugin
 
install
 superpowers@superpowers-marketplace
# 重启 Claude Code
第二步：用 OpenSpec 锁定需求
cd
 your-project
openspec init
然后在 Claude Code 里：
/opsx:
new
 
add
-user-login
/opsx:ff
/opsx:ff
 是"快进"命令，会自动生成 proposal.md、design.md 和 tasks.md。
生成之后先别急着执行——
打开 proposal.md，手动补上"非目标"那一栏
：
## 非目标（v1 不做）
- 
OAuth 第三方登录
- 
手机号登录
- 
记住我功能
这步很多人会跳过，跳过之后 AI 就会开始"好心办坏事"。
第三步：用 Superpowers 执行开发
/superpower
s:brainstorm
AI 会先问你几个关键问题，比如密码策略、token 过期时间等。回答完之后：
/superpower
s:write
-plan
它会读取 OpenSpec 的 tasks.md，生成极细粒度的执行计划——每个任务精确到文件名和函数名，2-5 分钟粒度。
/superpowers:
execute
-plan
接下来就是 AI 自动干活：创建 Git 分支、写失败测试、写实现代码、让测试通过、双阶段代码审查。
第四步：归档闭环
/opsx:verify    
# 检查代码是否符合规范
/opsx:archive   
# 合并回主规范库
跑完这一套之后，你的项目里会有一份完整的、可追溯的开发记录。下次新成员接手，或者半年后你自己接手，打开 openspec/specs/ 就能知道这套登录是怎么设计的、为什么这么设计。
九、避坑：三条经验，少走弯路
第一条：
 工具越重，门槛越高，但项目得匹配。
有人用了三个月 Spec-Kit 最后放弃了，原因是企业的真实需求是多线并行、随时变更，Spec-Kit 的严格阶段门控在这种场景下变成了阻碍。工具没有错，只是不适合那个场景。选型之前先想清楚你的项目特点。
第二条：
 规范写完不是终点，上下文管理才是真正的成本。
AI 会失忆。长对话必然导致前面的约束被后面的 prompt 覆盖。建议把"规划会话"和"执行会话"分开，通过文件传递上下文，而不是在一个超长对话里做所有事情。
第三条：
 工具是手段，抽象能力才是核心。
用 SDD 用得好的人，真正提升的不是"配置工具的能力"，而是需求抽象能力、约束定义能力、任务拆解能力。工具帮你把这三种能力固化成流程，但能力本身还是要靠你自己练。
十、最后说一点
有一个判断我觉得是对的：
未来的编程竞争，不是谁写代码写得快，而是谁能把问题定义得更清楚。
Spec-Kit、OpenSpec、Superpowers，这些工具本质上都是在做同一件事——
把"先想清楚再动手"这个工程习惯，强制执行化
。让 AI 帮你把流程跑起来，而不是靠你个人的自律。
你现在的 AI 编程，有没有工作流？
如果没有，从这周开始加一个。不一定要装复杂的工具，先从 AGENTS.md + 需求模板开始。感受一下"先签字，后动手"和"边做边改"的差别。
工作流不是读出来的，是用出来的。