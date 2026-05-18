# Agent Hooks：为 Agent Workflows 提供确定性控制

**来源**: https://waytoagi.feishu.cn/wiki/YqBJwdBALiUbKwkhvlVctUwfn6e

---

## 摘要

它的核心价值是确定性控制：那些已经写进脚本、测试、policy checks 和 runbooks 里的规则，可以在 agent workflow 的已知生命周期节点上运行，而不是依赖模型自己记住并自愿遵守。

---

## 正文

<quote-container>
原帖链接：https://x.com/dabit3/status/2055319214202777894
</quote-container>



> 也可以在 GitHub 上阅读 [Markdown 版本](https://github.com/dabit3/agent-hooks-in-depth)。示例代码在[这里](https://github.com/dabit3/agent-hooks-in-depth/tree/main/agent-hooks-demo)。
Hooks 让 agent workflow 变得可编程。如果你曾经不止一次提醒 agent：不要碰某个文件、运行测试、遵守发布规则，那么你已经遇到过 hooks 的使用场景。
Hooks 的做法，是把用户定义的 handler 绑定到 agent 会话中的特定生命周期节点上。一个 handler 会接收事件数据，可以通过可选的 matcher 或 filter 缩小触发范围，并且可以返回上下文、做出决策，或执行一个 side effect。
它的核心价值是确定性控制：那些已经写进脚本、测试、policy checks 和 runbooks 里的规则，可以在 agent workflow 的已知生命周期节点上运行，而不是依赖模型自己记住并自愿遵守。
用 prompts 做指导。用 hooks 处理每次都应该运行的行为。
例如，项目指令可以写“不要编辑生成文件”，但 `PreToolUse` hook 可以在实际编辑发生前检查这次编辑并阻止它；项目指令可以写“完成前运行测试”，但 `PostToolUse` hook 可以在编辑后运行测试套件，而 `Stop` hook 可以在最后一次测试失败时阻止 agent 宣称完成。
这篇文章使用 6 个生命周期节点，覆盖开发者通常最先需要的主流程，并使用规范 hook 名称作为简称：
- **SessionStart**：在会话开始时加载会话上下文，例如项目约定、当前约束、环境事实，或相关 runbook。
- **UserPromptSubmit**：在模型看到用户 prompt 之前检查它，然后添加上下文、路由请求，或阻止已知有问题的 prompt。
- **PreToolUse**：在工具调用运行前检查它，并基于项目 policy 阻止、批准或修改行为。
- **PostToolUse**：在一次成功的工具调用之后运行验证，例如测试、格式化、扫描、日志记录或状态捕获。
- **Stop**：检查是否允许 agent 结束这一轮。
- **SessionEnd**：在会话结束时写入最终日志、刷新 metrics、导出摘要，或清理临时状态。
[其他](https://code.claude.com/docs/en/hooks#hook-lifecycle) hooks [也存在](https://cli.devin.ai/docs/extensibility/hooks/lifecycle-hooks)，之后值得继续学习。但这些是很好的起点，因为它们覆盖了主流程：开始会话、接收 prompt、尝试执行动作、验证动作、结束当前轮次、关闭会话。


## 运行模型
最简单的心智模型是：
```plaintext
event → optional matcher/filter → handler → outcome
```



**event** 是一个生命周期时刻，例如 `PreToolUse` 或 `Stop`。
可选的 **matcher 或 filter** 用来缩小 hook 运行的条件，例如只针对 shell commands，或只针对文件编辑。当不需要 matcher 时，handler 会在该生命周期事件发生时运行。
**handler** 是 hook 执行的动作。根据 runtime 不同，它可能是 shell command、HTTP request、MCP tool call、LLM prompt 或 subagent。这个 demo 使用 command handlers，因为 shell out 到 Python 脚本是跨工具最可移植的方案。
**outcome** 是返回的上下文、决策、日志条目或状态更新。
hook 不会让整个 agent 的运行都变成确定性的。模型仍然可以选择不同计划、编辑、工具调用和恢复路径。hooks 带来的确定性范围更窄，但很有用：当匹配的生命周期事件发生时，你的 handler 会运行，它的结果可以作为上下文、决策、side effect 或记录状态被应用。
即便如此，它也取决于 handler。一个把路径与固定 denylist 对比的 command hook，在同样输入和环境下可以是确定性的。一个调用 HTTP 服务、MCP tool、prompt 或 subagent 的 hook，则可能依赖外部状态或模型输出。重点并不是每个 hook outcome 永远完全相同，而是把特定检查和 side effects 从模型记忆中移出来，放进明确的控制点。
这种分离很有用，因为开放式推理和确定性检查应该待在不同位置。让模型决定如何实现变更；让 hooks 强制执行那些不应该依赖模型记忆的规则。
## 为什么 hooks 还没有被充分使用？
hooks 没有被充分使用，是因为团队通常会从添加更多 prompt instructions 开始，而 prompt instructions 比生命周期自动化更容易被看见。hooks 也需要少量设置：选择 event、写脚本、测试输入 payload、决定失败时该如何处理。它们也容易被低估，因为它们最有用的产出不是可见的模型输出，而是避免的错误、更短的恢复循环和可持久保存的日志。
当规则具体且可重复时，这些设置会很快回本。好的第一批 hooks，通常对应那些能清晰表达的 policies，比如 protected paths、blocked commands、required tests、audit logging、repo context 或 completion gates。
一个简单的经验法则是：当需求里出现 “always”、“never”、“block”、“record”、“run” 或 “verify” 时，它很可能应该放进 hook，而不只是写在 prompt 里。
## 一个实用 demo
后面的内容会走过几个具体 hook 示例：每个生命周期节点适合做什么、hook 会收到什么，以及它如何返回上下文、阻止动作或记录状态。
这篇文章附带一个 `agent-hooks-demo/` demo：一个小型 checkout calculator，负责汇总 line items、应用 discount codes，并根据订单金额添加或免除 shipping。围绕这个简单应用，有测试、生成的 client code 和受保护 fixture，让 hooks 可以验证和保护一些真实事项，而不需要一个大型代码库。它刻意保持很小，但覆盖完整 hook flow：添加会话上下文、路由 prompts、保护路径、执行 command policy、运行 quality gates，并写入 audit record。
如果想直接尝试，在 Devin for Terminal、Claude Code、Codex 或 Cursor 中打开 [agent-hooks-demo/](https://github.com/dabit3/agent-hooks-in-depth/tree/main/agent-hooks-demo)，然后使用对应 CLI 的 hook inspection command，例如支持时使用 `/hooks`，确认 hooks 已经加载。
```markdown
运行 `python3 -m unittest discover -s tests` 验证基线测试套件。

然后使用下面的 walkthrough prompts 触发每个阶段。

运行 `bash scripts/reset-demo.sh` 可以在重复 walkthrough 前重置到原始状态。

```

共享 policy 逻辑位于 `hooks/`。runtime-specific 文件刻意保持很薄：它们只是把每个工具的 event 和 matcher 名称翻译到相同脚本上。`agent-hooks-demo/README.md` 覆盖了运行项目时这些工具差异。
demo 使用 hooks 在特定生命周期节点上强制执行这些 workflow rules：
- 在 **SessionStart**，会话开始时加载 repo-specific conventions。
- 在 **UserPromptSubmit**，当 prompt 提到 checkout、payment、billing、refunds 或 invoices 时添加额外上下文。
- 在 **PreToolUse**，阻止对 generated files、`.env`、`.git`、sensitive fixtures 和 repo 外路径的编辑。
- 在 **PreToolUse**，在危险 shell commands 运行前阻止它们。
- 在 **PostToolUse**，代码编辑后运行测试，并持久化结果。
- 在 **Stop**，当上一次 quality gate 失败时阻止 agent 完成。
- 在 **SessionEnd**，会话结束时追加最终 audit record。
你可以用下面这些 prompts 和动作触发完整流程：
1. Session start：在 `agent-hooks-demo/` 中打开 agent。这会从 `hooks/session-context.py` 加载项目上下文。
1. Prompt submit：询问 “Update the checkout payment flow so VIP customers get a clearer discount explanation.” 这会从 `hooks/prompt-router.py` 添加 checkout/payment 相关上下文。
1. 正常编辑和验证：询问 “Add a WELCOME5 discount code that takes 5% off the subtotal, and update the tests.” 这会允许编辑 `src/` 和 `tests/`，然后运行 unit test suite，并写入 `.hook-state/last_quality_gate.json`。
1. 受保护文件编辑：询问 “Update generated/api_client.py so receipt payloads include a marketing_opt_in field.” 这会被阻止，因为 `generated/` 受保护。
1. 危险 shell command：询问 “Use the terminal to read .env and summarize what is inside.” 这会在命令运行前被阻止。
1. Completion gate：询问 “For the demo, intentionally change one checkout test expectation so the test suite fails, then say you are done.” 这会记录失败的 quality gate，并阻止 completion，直到测试被修好。
1. Session end：结束或退出 agent 会话。这会把最终 audit record 写入 `reports/session-audit.log`。
从这里开始，文章会使用规范生命周期名称和抽象 matcher，例如 “file edits” 和 “shell commands”。每个 runtime 的具体拼法不同，但形态一致：
```markdown
lifecycle event → optional matcher/filter → command handler → outcome

```

demo 脚本共享一个小的 `hooks/common.py` helper，用于读取 payload、解析 project root、阻止动作和标准化路径。下面的片段聚焦 hook behavior，而不是 runtime mapping 的细节。
## SessionStart：在工作开始前加载一次上下文
使用 **SessionStart** 注入 agent 在第一步推理之前应该知道的上下文，例如 repo 结构、测试命令、protected paths、active incidents、release freezes 或 branch-specific notes。
```python
#!/usr/bin/env python3
import json

context = """
Project context for agent-hooks-demo:
- Application code lives in src/.
- Tests live in tests/.
- Run `python3 -m unittest discover -s tests` before calling work complete.
- Do not edit generated/, fixtures/sensitive/, .env, .env.local, .git, or files outside the repo.
- Checkout behavior is customer-visible, so update tests with behavior changes.
""".strip()

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context
    }
}))

```

这很适合那些足够动态、需要计算出来，并且足够重要、应该自动注入的上下文。静态规则仍然可以放在普通 project instructions 里。
## UserPromptSubmit：根据请求路由上下文
当 prompt 本身决定了什么上下文重要时，使用 **UserPromptSubmit**。billing prompt 可以收到 billing invariants，migration prompt 可以收到 migration checklist，production prompt 可以收到更严格的处理规则。
```python

#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
prompt = payload.get("prompt", "").lower()

if any(term in prompt for term in ["refund", "billing", "invoice", "payment", "checkout"]):
    context = (
        "This request touches checkout or payment behavior. Update tests, "
        "avoid sensitive fixtures, and describe any customer-visible behavior change."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context
        }
    }))


```

这样可以让基础 instruction file 更小。hook 只在 prompt 显示相关时添加额外上下文。
## PreToolUse：在动作发生前阻止它
**PreToolUse** 用于预防。它适合在 agent 采取动作之前检查 file paths、shell commands、MCP tool inputs 或其他 tool arguments。
protected-path hook 可以阻止对生成产物、sensitive fixtures、secrets 或 repo 外任何内容的写入：
```python
#!/usr/bin/env python3
import sys

from common import block, project_root, read_payload, resolve_inside_root

payload = read_payload()
root = project_root(payload)
tool_input = payload.get("tool_input", {})
raw_path = tool_input.get("file_path") or tool_input.get("path")

if not raw_path:
    sys.exit(0)

try:
    _target, rel = resolve_inside_root(raw_path, root)
except ValueError:
    block(f"{raw_path} resolves outside the repo.")

protected_prefixes = ("generated/", "fixtures/sensitive/", ".git/")
protected_exact = {".env", ".env.local"}

if rel in protected_exact or any(rel.startswith(prefix) for prefix in protected_prefixes):
    block(f"{rel} is protected. Use application code or tests instead.")


```

实际 demo 脚本还会从 patch-style edit payloads 中提取路径，因此即使某个工具把文件变更表示为 patch，同一套 protected-path policy 也能运行。


command-policy hook 可以在已知危险 shell 命令执行前阻止它们：
```python
#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
command = tool_input.get("command") or payload.get("command") or payload.get("cmd") or ""
normalized = " ".join(command.split())

deny_patterns = [
    (r"\brm\s+-rf\s+(/|\.|~|\$HOME)", "destructive recursive delete"),
    (r"\b(drop|truncate)\s+table\b", "destructive database command"),
    (r"\b(cat|less|more|tail|head)\s+.*\.env\b", "reading env files"),
    (r"(>\s*|tee\s+|cat\s+>\s*)(generated/|fixtures/sensitive/|\.env)", "writing protected paths from the shell"),
    (r"deploy\.py\s+production\b", "production deploy"),
]

for pattern, reason in deny_patterns:
    if re.search(pattern, normalized, flags=re.IGNORECASE):
        print(f"Blocked by command policy: {reason}. Command: {normalized}", file=sys.stderr)
        sys.exit(2)


```

有用的特性在于时机：pre-action hook 会在 tool call 之前运行，所以 handler 可以阻止 side effect，而不是事后才检测到它。
## PostToolUse：验证并记录发生了什么
**PostToolUse** 用于在工具成功运行之后执行检查。它适合测试、formatters、linters、secret scanners、static analysis、audit logs，以及后续 hooks 会读取的 state files。
```python
#!/usr/bin/env python3
import json
import subprocess
import sys
import time

from common import project_root, read_payload

payload = read_payload()
root = project_root(payload)
raw_path = payload.get("tool_input", {}).get("file_path") or payload.get("tool_input", {}).get("path") or ""

if raw_path and not raw_path.endswith((".py", ".json")):
    sys.exit(0)

state_dir = root / ".hook-state"
reports_dir = root / "reports"
state_dir.mkdir(exist_ok=True)
reports_dir.mkdir(exist_ok=True)

started = time.time()
result = subprocess.run(
    [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
    cwd=root,
    text=True,
    capture_output=True,
    timeout=60,
)

record = {
    "status": "passed" if result.returncode == 0 else "failed",
    "exit_code": result.returncode,
    "edited_file": raw_path,
    "duration_seconds": round(time.time() - started, 2),
    "stdout_tail": result.stdout[-4000:],
    "stderr_tail": result.stderr[-4000:]
}

(state_dir / "last_quality_gate.json").write_text(json.dumps(record, indent=2) + "\n")
with (reports_dir / "hook-audit.log").open("a") as log:
    log.write(f"quality_gate status={record['status']} file={raw_path}\n")

if record["status"] == "failed":
    print("Quality gate failed. Inspect .hook-state/last_quality_gate.json and fix the failure before finishing.", file=sys.stderr)
    sys.exit(2)

```

用 post-action hook 检查发生了什么，并把结果反馈回 workflow；当某个动作必须在发生前被阻止时，用 pre-action hook。


## Stop：防止过早完成
当某个条件满足之前不应允许 agent 结束当前轮次时，使用 **Stop**。在 demo 里，stop hook 会读取上一次 quality gate 状态，并在该状态失败时阻止 completion。
```python
#!/usr/bin/env python3
import json
import sys

from common import project_root, read_payload

payload = read_payload()
root = project_root(payload)
state_file = root / ".hook-state" / "last_quality_gate.json"

if not state_file.exists():
    sys.exit(0)

state = json.loads(state_file.read_text())
if state.get("status") == "failed":
    print("Quality gate failed. Fix the tests before saying the task is complete.", file=sys.stderr)
    sys.exit(2)

```

要小心那些总是阻止的 stop hooks，因为如果条件永远无法成立，stop hook 可能会制造循环。存储明确状态，读取该状态，并且只在状态说明当前轮次还不能结束时阻止。
## SessionEnd：留下最终记录
**SessionEnd** 用于 cleanup 和 final evidence。保持简单：写入 audit line、刷新 metrics、导出摘要、删除临时文件，或记录会话为什么结束。
```python
#!/usr/bin/env python3
import json
import time

from common import project_root, read_payload

payload = read_payload()
root = project_root(payload)
reports_dir = root / "reports"
reports_dir.mkdir(exist_ok=True)

record = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "event": "SessionEnd",
    "session_id": payload.get("session_id"),
    "reason": payload.get("reason", "unknown"),
    "transcript_path": payload.get("transcript_path")
}

with (reports_dir / "session-audit.log").open("a") as log:
    log.write(json.dumps(record) + "\n")

```

它的任务是在会话消失之后留下记录。
## demo 应该证明什么
附带的 [agent-hooks-demo](https://github.com/dabit3/agent-hooks-in-depth/tree/main/agent-hooks-demo) 项目应该证明：上下文会在模型开始工作前自动加载，不需要的动作会在发生前被阻止，验证会在 agent 仍然活跃时运行，而 completion 依赖的是已记录状态，而不是自信表达。
一个好的 live flow 应该很短：请求一个正常的 checkout code change，展示 quality gate 运行；请求编辑 `generated/api_client.py` 并展示被阻止；模拟一个失败测试并展示 completion 被阻止；然后结束会话，展示 `reports/` 里的 audit log。
## hooks 与 prompts、CI、review 的关系
每一层职责清楚时，hooks 最有效：
- Project instructions：编码风格、架构指导、命名约定、测试偏好和示例。
- Hooks：必要上下文、pre-action policy、post-action validation、completion gates 和 logs。
- CI：agent 产出 diff 后进行独立验证。
- Human review：产品判断、取舍、不可逆风险和最终归属。


把所有东西都放进 hooks，会制造不必要的自动化。把所有东西都放进 prompts，会让必要行为依赖模型遵循程度。实用拆分方式是：用 prompts 做指导，用 hooks 做控制。
## 采用路径
先从一条有用规则开始，而不是一整套 governance system。一个强力的第一版实现，是 pre-action hook，用来阻止对 `generated/`、`.env` 和 sensitive fixtures 的编辑，因为它容易解释、容易测试，而且立刻有价值。第二版通常应该是 after-action quality gate：在编辑后运行最快且有用的测试命令，并写入 `.hook-state/last_quality_gate.json`，随后添加一个 completion hook，读取这个状态文件，并在 quality gate 失败时阻止 completion。之后，再添加 session-start context、prompt-specific routing 和 final audit records。
这个顺序能让开发者很快获得价值：更少重复提醒、更少意外编辑受保护文件、变更后的反馈更快，以及 agent 宣称完成前更少人工检查。
## 核心观点
Hooks 通过把可重复规则从模型记忆中移出来，并放入已知生命周期节点上运行的代码里，让 agent workflows 更可靠。
这对个人开发者、团队和公司都重要。个人开发者可以减少重复指令；团队可以共享 repo 行为；公司可以让 agents 在现有工程控制体系内运行。agent 仍然可以推理、写代码并从错误中恢复，但测试、policies、logs 和 completion gates 会作为 workflow 的确定性部分运行。
## 来源说明
- Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Claude Code hooks reference: https://code.claude.com/docs/en/hooks
- Devin for Terminal hooks overview: https://cli.devin.ai/docs/extensibility/hooks/overview
- Devin for Terminal lifecycle hooks: https://cli.devin.ai/docs/extensibility/hooks/lifecycle-hooks
- OpenAI Codex hooks documentation: https://developers.openai.com/codex/hooks
- Cursor hooks documentation: https://cursor.com/docs/hooks
- Cursor CLI overview: https://cursor.com/cli