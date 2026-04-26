# 子智能体 vs 智能体团队：颠覆全局的架构抉择

**来源**: https://waytoagi.feishu.cn/wiki/TAx1wE2XbiQ0dpkbZxFc0SOOn3e

---

## 摘要

文章指出复杂任务不应本能选择多智能体，而要先判断所需协作机制；子智能体适合隔离、并行、压缩明确任务结果，信息流可控，团队智能体适合需要持续上下文、成员通信、任务依赖和动态调整的真实协作场景，二者决定截然不同的系统架构。

---

## 正文

<quote-container>
原帖链接：https://x.com/Suryanshti777/status/2047694444787577236
</quote-container>



大多数 AI 系统，一开始就搭错了。
很多人一旦觉得任务复杂，就会立刻伸手去做 multi-agent systems。
但这通常是错误的直觉。
真正的问题不是“我是否应该使用多个 agent？”
而是“这个任务到底需要什么样的协作机制？”
这个答案，会决定你整个架构的走向。
类似 Claude 的系统里，通常会给你两种截然不同的方案：sub-agents 和 agent teams。它们表面上看起来很像，但实际上解决的是完全不同的问题。


## 子Agent：带隔离的并行化
sub-agent 是一个在独立隔离上下文中运行的专门化实例。
你可以把它理解为“委派”。
你把一块聚焦明确的工作交给它，它返回一份干净的结果。
每个 sub-agent 都会拿到：
- 一个定义其角色的 system prompt
- 一组受限的工具集合
- 一个完全隔离的上下文
- 一个边界清晰的单一任务


当它执行结束时，它只会返回最终输出，而不会把推理过程或中间步骤一并带回来。
这一点很关键，因为 sub-agent 的价值不只是“更快”，更在于“压缩”。
它会把混乱的探索过程，压缩成一个干净的信号。
同时，这套机制也有严格限制：
- sub-agents 之间不能互相交流
- sub-agents 不能再继续生成新的 agents
- 所有信息流都必须经过父级 agent
这能让整个系统保持可预测、也更干净。
实际用起来大概是这样：
```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def main():
    async for message in query(
        prompt="Review the authentication module for issues",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            agents={
                "security-reviewer": AgentDefinition(
                    description="Find vulnerabilities and security risks",
                    prompt="You are a security expert.",
                    tools=["Read", "Grep", "Glob"],
                    model="sonnet",
                ),
                "performance-optimizer": AgentDefinition(
                    description="Identify performance bottlenecks",
                    prompt="You are a performance engineer.",
                    tools=["Read", "Grep", "Glob"],
                    model="sonnet",
                ),
            },
        ),
    ):
        print(message)

```

这里最关键的细节，是 `description` 字段。
它本质上承担的是 routing signal 的作用。
## 智能体团队：通过通信实现协作
agent teams 是为“协作”而设计的。
这里不再是彼此隔离的执行单元，而是一组能够持续持有上下文、彼此沟通、并且实时调整的 agents。
它通常包括：
- 一个负责分配任务与做综合的 lead agent
- 一组负责执行具体任务的 teammates
- 一个用于跟踪进度和依赖关系的共享任务层


这让真正的协作成为可能。
例如，一个 frontend agent 可以把 backend 变更即时同步出去，相关内容会立刻更新。
## 核心差异
sub-agents 和 agent teams 在本质上完全不同。
sub-agents 的关注点是执行：
- 隔离的
- 无状态的
- 一次性的
- 由父级控制的
agent teams 的关注点是协作：
- 持续存在的
- 可交互的
- 共享上下文的
- 点对点协作的
如果任务彼此独立，就用 sub-agents。
如果任务之间彼此依赖，就用 teams。
## 大多数人到底错在哪里
很多系统喜欢按角色拆分，比如 planner、developer、tester。
这种拆法会在每一次交接中都制造上下文丢失。
- implementer 不知道 planner 当时掌握了什么
- tester 不知道 implementer 做了哪些关键决策
- 质量会在每一道边界上持续下滑
更好的方式，是按“上下文”来拆，而不是按“角色”来拆。


你应该问的是：
这个任务到底真正需要哪些信息？
如果两个任务共享了大量深度上下文，那就让它们留在同一个 agent 里。
只有当上下文能够被干净切开时，才去拆分。
## 真正重要的 5 种模式
### 1. Prompt chaining：顺序步骤


### 2. Routing：把任务送到正确的 agent
### 3. Parallelization：把彼此独立的工作并行执行
### 4. Orchestrator–worker：一个 agent 负责委派
### 5. Evaluator–optimizer：先生成，再迭代优化
## 什么时候不该用多智能体系统
有时候，一个单 agent 就已经足够了。
适合使用 multi-agent systems 的场景：
- 你需要上下文隔离
- 你有可以并行执行的任务
- 你确实需要专门化分工
不适合使用的场景：
- agents 之间高度互相依赖
- 协调成本过高
- 任务本身其实很简单
## 最后的原则
围绕上下文边界来设计，而不是围绕角色来设计。
先从简单系统开始，只有在真正需要时，再把复杂度加上去。