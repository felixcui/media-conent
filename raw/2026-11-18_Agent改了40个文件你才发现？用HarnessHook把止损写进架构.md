# Agent改了40个文件你才发现？用Harness Hook把止损写进架构

**作者**: 李隆熹

**来源**: https://mp.weixin.qq.com/s/0nO92ufveC_cXjkMiontNg

---

## 摘要

长任务 Agent 最麻烦的不是做错一步，而是错了还接着干：同一个补丁换着写法打四遍，原本 3 个文件的改动蔓延到 40 个，rm -rf 不问一声就执行。作者为此写了 stop-line：一个 Skill 加一个 Hook 插件，让 Agent 在继续之前先回答这件事还值不值得做。关键思路是不指望模型自觉，把计数和拦截从模型推理的数据面挪到 harness 生命周期钩子的控制面——Hook 层做确定性计数与拦截，Skill 层做判断与交接，挂在 6 个生命周期事件上组成状态机。被拦下时输出一张 HANDOFF 交接单，写明因何停止（loop、stuck、budget、boundary）和已用额度，例如 3/3 次尝试、6/15 个文件。三条原则：fail-open、never-trap、human-only-reset。

---

## 正文

李隆熹 李隆熹

在小说阅读器读本章

去阅读

关注腾讯云开发者，一手技术干货提前解锁👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr5cVljsZaTerseHo0b30q5ACI8PKQZDgtq7iaRpXwCrV8UnWMvP2gXatJwwmsic6wcF404wPNYIBa0PmibGC70MSZISib2VJoD3JRk/640?wx_fmt=png&from=appmsg)

**写在前面**

用 Agent 跑长任务，做错一步其实不算什么，麻烦的是它错了还接着干：同一个补丁换着写法打四遍，原本 3 个文件的改动蔓延到 40 个，rm -rf 不问一声就执行了。

stop-line 是我为这个问题写的 Skill + Hook 插件。它让 Agent 在继续之前先回答一个问题：这件事还值得做下去吗？我的思路是不指望模型自觉，把计数和拦截从模型推理（数据面）挪到 harness 的生命周期钩子（控制面）上。

文章会讲这几件事：

- 纯 Prompt 方案为什么管不住止损：它要防的那几种情况，正好也会让它自己失效
- 双层架构：Hook 层做确定性的计数和拦截，Skill 层做判断和交接
- 挂在 6 个生命周期事件上的状态机，以及 fail-open、never-trap、human-only-reset 三条原则
- 照着通用文档实现时会踩的 4 个协议坑（CodeBuddy 和 Claude Code 的差异）
- 一天的线上运行记录：拦截和交接按预期生效，也暴露了 2 个 bug，已修复并补了回归测试
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr7kic2GBsZicOf0j8oZwCC0pQEDxLrRnB6Rgic2HBibshmaysxianjU8mjTlFiaFRrcKuxuNdU1pUvQ8L85AHtp105mcuDP8GW8Wy908/640?wx_fmt=png&from=appmsg)

## 01

背景：三种最费钱的失败

**1.1 三个现场**

长任务 Agent 跑久了，下面三种情况会反复出现。

**现场 A：换汤不换药的重试**

```bash
$ pytest tests/api/v2/test_orders.py -xFAILED tests/api/v2/test_orders.py::test_create - assert 401 == 201$ sed -i 's/return 401/return 200/g' src/api/v2/orders.py$ pytest tests/api/v2/test_orders.py -xFAILED tests/api/v2/test_orders.py::test_create - assert 401 == 201$ sed -i 's/status_code=401/status_code=200/g' src/api/v2/orders.py$ pytest tests/api/v2/test_orders.py -xFAILED tests/api/v2/test_orders.py::test_create - assert 401 == 201
```

每次改完，Agent 都觉得"这回该好了"，可失败原因一直没变。它改的是返回值，根因碰都没碰。

**现场 B：错误指纹漂移**

```apache
E: connection refused 127.0.0.1:5432E: connection refused 127.0.0.1:5433E: connection refused 10.0.0.12:5432
```

行号、端口、ID 每次都不一样，Agent 就当成新问题去查。其实是同一个问题。

**现场 C：范围失控和不可逆操作**

"顺手修一下"，3 个文件的任务改到了 40 个；或者为了"清理环境"，没确认就跑了 `git push --force` 、 `DROP TABLE` 。

这三种情况难防的地方在于：单看每一步都说得过去，代码能编译，碰巧存在的测试也过了，看起来一直在推进。等回过头看，事故已经出了。

**1.2 Skill 生态里没人管的一块**

到 2026 年 11 月，Agent Skill 生态里热门的方向，基本都是让 Agent 多做一点、做好一点：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr7Wm1bmpibbso9IP9MzGt0noIMWfeb12QQDkIwojnlCu2Szo6aXlkvcsHytymERdLhJibDMPadmHVXE2h1jBBoubUbL8JPpPLKvc/640?wx_fmt=png&from=appmsg)

我调研时看到，"计划和交付对账"（valerie、gsd-verifier）、"事实核验"（blog-fact-checking、verify-citations）都已经有好几个实现。但执行到一半该不该收手，这个问题没有哪个 skill 在管。

stop-line 只做这一件事，对 Agent 也只有一条要求：

> 继续做是一个决定，不是默认行为。 每次准备重复上一步、扩大改动范围、或者执行不可逆操作之前，先讲清楚这次比上次多知道了什么。讲不出来，就停下，把控制权交还给人。

## 02

为什么光靠 Prompt 不够

**2.1 Skill 是怎么加载的**

在 CodeBuddy / Claude Code 里，Skill 说白了就是按需注入的提示词：

```objectivec
┌──────────────────────────────────────────────────────────────┐│ ① description（约 100 词）   常驻系统提示，模型据此决定是否加载   ││              │                                               ││              ▼  模型调用 Skill 工具                           ││ ② SKILL.md 正文              作为一条消息注入上下文             ││              │                                               ││              ▼  模型自行判断                                  ││ ③ references/*.md            需要时才 Read                    ││              │                                               ││              ▼                                               ││ ④ 模型按文字自我约束          ← 执行与否，完全取决于模型          │└──────────────────────────────────────────────────────────────┘                     图 1  纯 Skill 方案的执行链路
```

设计品味、写作风格这类 Skill 走这条链路没什么问题。模型照着做就行，偶尔没照做，也就是输出差一点。

**2.2 止损场景下的四个失效点**

可 stop-line 要防的那几种情况，偏偏会让这条链路断掉：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr713HuymRVWG9QfFlibibs4Apf2olhd4O37VibmiavBbUhjBp3iaibK6kWj2b5k6icibibM4ImtJtSPtXlOxw7x2Gp9iayMCzicTmrh4Oiby1E/640?wx_fmt=png&from=appmsg)

说直白点：越是需要它的时候，它越可能不管用。

**2.3 把止损挪到控制面**

借基础设施里的说法：模型推理是数据面，跑业务逻辑，会出错也会过载；harness 的生命周期钩子是控制面，在数据面之外独立执行，数据面绕不过去。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6FJuEXU4qLTibOnYeeaVwmQAgHGclibe2KkTOwf7eAS2O9I0MJibN6r7q23ViaibwsmdlWmz9dYCfpRuSUDicCqpTzmX3fARRa9ze4k/640?wx_fmt=png&from=appmsg)

这样分工就清楚了：计数和拦截交给代码，判断和交接交给模型。

## 03

方案设计

**3.1 总体架构**

```css
┌─────────────────────── Harness（CodeBuddy / WorkBuddy / Claude Code）──────────────────────┐                │                                                                                          │  用户消息 ────▶│ UserPromptSubmit ──┐                                                                      │                │                    │                                                                      │                │  模型 ── 工具调用 ──▶ PreToolUse ──▶ [ 执行工具 ] ──▶ PostToolUse / PostToolUseFailure     │                │   ▲                │      │                              │                              │                │   │                │      │ exit 2 / ask                 │ additionalContext            │                │   │                ▼      ▼                              ▼                              │                │   │          ┌──────────────────────────────────────────────────────┐                  │                │   │          │                hook_guard.py（控制面）                │                  │                │   │          │  签名归一化 · 错误指纹 · 预算计数 · 高危规则 · 状态机     │                    │                │   │          └──────────────────────┬───────────────────────────────┘                  │                │   │                                 │ 原子写                                            │                │   │                                 ▼                                                  │                │   │                     state/<session_id>.json                                        │                │   │                                                                                    │                │   └──── SKILL.md（数据面）：收到 [stop-line] 消息后选择 ASK / STOP / ROLLBACK，写 HANDOFF.md │                │                                                                                          │  会话开始 ────▶│ SessionStart：发现 HANDOFF.md 则注入；上下文压缩后重新注入预算状态                             │  结束一轮 ────▶│ Stop：已停止但未写交接 → 拦截一次                                                           │                └──────────────────────────────────────────────────────────────────────────────────────────┘                                           图 2  stop-line 双层架构
```

**3.2 四个核心抽象**

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6iabjnvE8JGsymNkt1amEwFTVlBhibYoJXYjE5DEPeK0u89Z4JISCibf0c72DGD8JGrZrpzNOmiaUlFPC1WpDkn0NRKib0fPcRna0E/640?wx_fmt=png&from=appmsg)

交接文档的结构如下：

```apache
# HANDOFF — <一句话任务>Stopped by : loop | stuck | budget | boundaryBudget used: 3/3 attempts, 6/15 files, 1 distinct error
## What is true        已验证的事实，每条附验证方式## What is done        已完成的改动，path:line + 验证方式## What is ruled out   已排除的假设及证据   ← 最有价值的一节## Where it broke      错误指纹、出现次数、最后的命令与输出## Next move           具体的下一步动作，不能是"继续排查"## Do not              刚刚浪费掉预算的那件事
```

这 6 节里我最看重 "What is ruled out"。交接之所以比从头再来省钱，靠的就是这一节：下一个会话不用再花预算去验证已经失败过的方向。

**3.3 停止状态机**

```sql
失败计数 < 阈值                    ┌──────────┐                    ▼          │              ┌───────────┐────┘   ─────────▶ │  RUNNING  │              └─────┬─────┘                    │  同一错误第 2 次                    │  或 同一签名第 3 次失败                    │  或 超出预算                    ▼              ┌───────────┐  变更类工具 → 阻断              │  STOPPED  │  只读命令 / 写 HANDOFF*.md → 放行              └─────┬─────┘  想结束本轮但没写交接 → 拦截一次                    │                    │  人发来任何消息（UserPromptSubmit）                    ▼RUNNING
    图 3  停止状态机
```

**3.4 四条设计原则**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr7b2jjAzib81IRvPiayicAdJiaWCOdDmicSwYFj96z2Xvd3Eetg5q2783ic7euicFcGGF39Bl6EHPUZREx2Thtj6JMDBtAGeU2CSWxay4/640?wx_fmt=png&from=appmsg)

## 04

关键实现

**4.1 Hook 协议速览**

Hook 是 harness 在生命周期节点上拉起的外部进程：从 stdin 读事件 JSON，用退出码和 stdout 返回决策。

输入（PreToolUse 示例）：

```json
{  "session_id": "abc123",  "transcript_path": "/.../00893aaf.jsonl",  "cwd": "/path/to/project",  "permission_mode": "default",  "hook_event_name": "PreToolUse",  "tool_name": "Bash",  "tool_input": { "command": "rm -rf build/" }}
```

输出有三种通道：

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr7CyTqZicMP3wevnlHnUZK6sEWxbzIxHWjBcNG1zrom5YKAics1X6e6R3Oe8zkASBpibGaOpsqWic6HD7gDbc6Gshic4M7g2wt3Aaj8/640?wx_fmt=png&from=appmsg)

stop-line 挂了 6 个事件：

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4ia7A5zibogapcnhWPPYBysfNZ3Al4ZZb2Lzqkdqx9dR7k099zybEAYH8GvZ3gicsC8hU0OicDBMUCKVk70nicicsymlxpRcpPdFW9o/640?wx_fmt=png&from=appmsg)

**4.2 签名归一化：把换汤不换药的重试认出来**

循环检测和卡死检测都依赖一个前提：表面不同、本质相同的东西，要能认成同一个。

```python
MASK_HEX  = re.compile(r"\b[0-9a-fA-F]{8,}\b")MASK_HOST = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}(?::\d+)?\b")MASK_STR  = re.compile(r"'[^']*'|\"[^\"]*\"")MASK_PATH = re.compile(r"(?<![\w])[.~]?[\w.-]*(?:/[\w.-]+)+/?|(?:[\w-]+\.[A-Za-z0-9]{1,5})\b")MASK_NUM  = re.compile(r"\b\d+(?:\.\d+)?\b")
def mask(text: str) -> str:    # 顺序敏感：先剥离引号字符串再匹配路径，    # 否则 sed 的 's/a/b/g' 会被拆成三段路径，预算统计虚高    text = MASK_HEX.sub("<id>", text)    text = MASK_HOST.sub("<host>", text)    text = MASK_STR.sub("<s>", text)    text = MASK_PATH.sub("<path>", text)    text = MASK_NUM.sub("<n>", text)    return re.sub(r"\s+", " ", text).strip()
```

效果：

```swift
sed -i 's/return 401/return 200/g' src/api/v2/orders.py   ─┐sed -i 's/status_code=401/status_code=200/g' src/api/...   ─┼─▶  sed -i <s> <path>sed -i 's/HTTP_401/HTTP_200/g' src/api/v2/orders.py        ─┘E: connection refused 127.0.0.1:5432                       ─┐E: connection refused 10.0.0.12:5433                       ─┴─▶  E | connection refused <host>
```

**踩坑记录** ：第一版是先匹配路径、再剥引号字符串，结果 `sed 's/a/b/g'` 里的 `/a/b/g` 被当成了路径，一个只涉及 3 个文件的样例会话统计出 11 个"路径"。把顺序调过来以后，降到了 2 个。

**4.3 只读判定：逐段检查，防止夹带**

停止状态下得放行只读命令，不然 Agent 连 `git status` 都跑不了，交接也就写不准。但又不能让 `ls && rm -rf x` 这种复合命令混过去：

```python
SEGMENT_SPLIT = re.compile(r"\|\||&&|;|\||\n")HANDOFF_HEREDOC = re.compile(    r"^\s*cat\s+>{1,2}\s*['\"]?[^\s'\"]*HANDOFF[\w.-]*\.md['\"]?\s+<<", re.IGNORECASE)
def is_readonly(command: str) -> bool:    """复合命令的每一段都只读，才算只读。"""    if HANDOFF_HEREDOC.match(command):   # heredoc 正文里可以自由出现 | ; &&        return True    for seg in SEGMENT_SPLIT.split(command):        # 1. 输出重定向只允许写到 HANDOFF*.md 或 /dev/null        # 2. find 带 -delete / -exec 不算只读        # 3. 命令头在白名单（ls/cat/grep/git status/pytest...）才放行        # 4. tee 的所有目标都是 HANDOFF*.md 才放行        ...    return True
```

有两处容易漏：

- heredoc 要单独处理。Agent 常用 `cat > HANDOFF.md <<'EOF'` 写交接，正文里的 `|` 、`;` 会被误拆成多段命令，所以要在拆分之前先整体识别。
- tee 不能整体放行。tee 能写任意文件，只有所有目标都是 HANDOFF\*.md 时才放。

**4.4 失败识别：跨 harness 的 outcome()**

各家 harness 表达"命令失败"的方式不一样（第五节细说），outcome() 按下面的优先级判断：

```python
def outcome(data: dict) -> tuple[bool, str]:      # 节选，完整实现见 hook_guard.py    resp = data.get("tool_response")    text = resp if isinstance(resp, str) else json.dumps(resp, ensure_ascii=False)    # 1. 结构化退出码：在嵌套结构里查找 exitCode / exit_code / returncode / returnCode    code = _find_key(resp, ("exitCode", "exit_code", "returncode", "returnCode"))    # 2. 回退：文本中的 "Exit Code: N"    if not isinstance(code, int):        m = re.search(r"Exit Code:\s*(-?\d+)", text)        code = int(m.group(1)) if m else None    # 3. 失败判定：PostToolUseFailure 事件、is_error 标记、或退出码非 0    failed = (data.get("hook_event_name") == "PostToolUseFailure"              or _find_key(resp, ("is_error", "isError")) is True              or (code is not None and code != 0))    # 4. 取最有代表性的一行错误（优先 stderr），过滤掉 "Stderr: (empty)" 之类的框架行    ...
```

**4.5 状态持久化**

- 按 session\_id 隔离：每个会话一个 JSON 文件
- 原子写：先写 `.tmp` ，再 `os.replace` ，避免并行的 hook 写出半个文件
- 存储位置： `$STOPLINE_STATE_DIR` → `$CODEBUDDY_PLUGIN_DATA` （插件升级不丢）→ `~/.cache/stop-line/`
- `不污染项目：项目目录里只会出现模型自己写的 HANDOFF.md`

上下文一压缩，模型就"忘了"自己失败过几次，状态文件不会忘。 `SessionStart(source=compact)` 会把计数器重新注入上下文：

```css
[stop-line] Budget state survived compaction. Files edited: 9/15.Distinct failures: 2/3. Failed signatures: {"pytest <path> -x": 2}. No stop in force.
```

**4.6 双写阻断消息**

```python
def block(message: str) -> None:    """退出码 2。CodeBuddy 优先读 stdout，Claude Code 读 stderr，两边都写。"""    msg = f"{TAG} {message}"    print(msg)    print(msg, file=sys.stderr)    sys.exit(2)
```

## 05

协议踩坑

下面这几个坑，照着通用文档或者 Claude Code 的经验去写都会踩到。我对照 CodeBuddy 官方文档和本机的真实会话记录，逐个核实过。

### 坑 1：退出码 2 时，两边读阻断原因的地方不一样

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr5tWhLeriaibDZWOP6YoXibb7ibrGguCAm67jicYrRVgqK7db24VrwwiaLTbPt0zQb69E4FVe4oMUvVDBibRxicCTQZfCicmjRnjDAD31AQ/640?wx_fmt=png&from=appmsg)

**后果** ：如果按 Claude Code 的习惯只往 stderr 打，在 CodeBuddy 上只要 stdout 有任何输出，阻断原因就丢了。模型只知道自己被拒，不知道为什么。

**处理** ：两边都写（见 4.6）。

### 坑 2：Bash 退出码非 0，不等于工具调用失败

我从 WorkBuddy 会话记录里取了一次失败的 Bash 调用（只保留字段骨架）：

```swift
{  "type": "function_call_result",  "name": "Bash",  "status": "completed",  "providerData": {    "toolResult": {      "rawResponse": { "exitCode": 1, "interrupted": false, "sandboxDenied": false }    }  },  "output": { "type": "text", "text": "Stdout: ...\nStderr: (empty)\nExit Code: 1\nSignal: (none)" }}
```

注意 `status` 是 `completed` ：命令执行失败了，但"工具调用"这件事本身算成功。

**后果** ：如果只监听 PostToolUseFailure，失败的命令一条都抓不到，stuck 和 loop 两个哨兵等于没装。

**处理** ：在 PostToolUse 里自己解析退出码（见 4.4），同时保留对 Claude Code `PostToolUseFailure + error` 形态的支持。

### 坑 3：写在 SKILL.md 头部的 Hook 用不上

CodeBuddy 支持在 SKILL.md 的 frontmatter 里直接声明 `hooks:`，看上去这是让 Skill 自带 Hook 最顺手的办法，但它有三重限制：

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr65kpLVLfd4KnHv4M2Pduf5QCyYFb51wXDR3spIqaTZP7Xg7RV1j0XdruvOz1SM5IVIeiaiaaGzVZX5KbriaSL5xbv1LeHHJCQ6pw/640?wx_fmt=png&from=appmsg)

stop-line 要守的是主会话，所以只能做成插件，用 `hooks/hooks.json` 分发。插件 hook 对整个会话生效，也不受上面的门禁限制。

### 坑 4：Hook 进程里的 Python 不是你以为的那个

激活时我才发现，hook 进程跑在一个干净的 login shell 里， `python3` 解析出来是系统自带的 3.8.2，不是我开发时用的 3.13：

```shell
$ env -i HOME="$HOME" PATH=/usr/bin:/bin /bin/zsh -lc 'python3 --version'Python 3.8.2
```

3.8 不支持 `dict | dict` 、 `match` 这些 3.9 以后的语法。我是这么处理的：

- hook 命令写死 `/usr/bin/python3` ，不依赖 PATH
- 测试脚本支持用 `STOPLINE_TEST_PY` 指定解释器，在 3.8 下跑全量测试

### 其他需要注意的协议细节

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr5NrGgicbhLesmMbJghSEniaibBxrfcr8Eek1VAudykTuVoupuM94icu1tkh18mSUsy23UpJ69Hu69lD19mUCS9h2rmy3ET4eWLLCA/640?wx_fmt=png&from=appmsg)

## 06

线上跑了一天：记录和两个 Bug

2026-11-05，stop-line 以用户级安装的方式，在我本机的 WorkBuddy 上跑了大约一天，覆盖 3 个真实会话。其中一个会话完整走了一遍停止、交接、解除，拿到的信息比模拟测试多得多。

以下记录取自 guard 状态文件和会话记录，做了脱敏，具体业务内容和路径都略去了。

**6.1 事件时间线**

任务背景：一个跨平台 trace 数据采集与分析任务。主 Agent 派出两个并行子 Agent 批量拉取明细，每条明细暂存为 /tmp 下的一个中间文件，预计要写约 79 个文件。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr42icuukmVsKGdnnrE6OEJREibdAX2cThu8A9IeI43Cu9p7BEFYWfkiaoAC5TTsYmLXtAIicT5A0F1gnxfWoHdibM3bLzz0Ydph8NI4/640?wx_fmt=png&from=appmsg)

**6.2 哪些地方按预期工作了**

- 停得及时，交接也完整。子 Agent 停下时，已经采集的数据写进了交接文档，没有丢。主 Agent 汇报的是已有结论加几个可选方案，用户拿到就能决定下一步。
- 强制交接生效了。Stop hook 刚好拦了一次，Agent 补完交接就正常结束，没有陷进循环。
- 自我保护生效了。Agent 先后用 Edit 和 Python 脚本改配置，两次都被拦下。（不过这次拦截本身有问题，见 6.6。）
- 退出码识别是对的。另一个会话里有一次失败的 `python3 -c` ，被正确记成了 ModuleNotFoundError 指纹，说明坑 2 的处理在真实的 tool\_response 上管用。
- 零内部错误。运行期间 errors.log 一条记录都没有。

**6.3 Bug 1：预算停止被人解除后，马上又触发了**

**现象** ：11:54 用户回复后停止被解除，两分钟后 Agent 编辑一个新文件，立刻又触发了同样的 budget 停止。用户那次回复等于白回了。

**根因** ：UserPromptSubmit 清掉了失败签名和错误指纹，却漏了已编辑文件列表。文件数还停在 15/15，下一个新文件必然越界。

```python
def on_prompt(data, st, sid):    ...    st["tripped"] = None    st["failed_sigs"] = {}    st["fps"] = {}    # 缺失：st["files"] 未处理
```

**修复** ：用户看到预算停止后还回复了，我把这当作对范围的重新授权。所以只在 budget 类停止被解除时清空文件列表；stuck 和 loop 类停止跟范围无关，不清。

```bash
st["failed_sigs"] = {}     st["fps"] = {}+    if t["cls"] == "budget":+        # 人已经看到范围并回复，视为重新授权。+        # 否则下一个新文件会立即重新触发同一个停止，人的回复毫无作用。+        st["files"] = []     save(sid, st)
```

**6.4 Bug 2：临时文件被算进了文件预算**

**现象** ：数据采集任务的 79 个暂存文件都放在 /tmp 下，却被当成了"改动范围失控"。

**根因** ：文件预算本来是用来限制对项目的改动范围的，实现时却把所有 Edit / Write 的目标路径都算了进去。中间产物不该算在范围里。

**修复** ：

```python
SCRATCH_PREFIXES = tuple(p for p in {    "/tmp/", "/private/tmp/", "/var/tmp/", "/var/folders/", "/private/var/folders/",    (os.environ.get("TMPDIR") or "/tmp/").rstrip("/") + "/",} if p)
def counts_toward_budget(path: str) -> bool:    """临时文件是工作材料，不是改动范围。"""    if not path or HANDOFF_RE.search(path):        return False    return (not os.path.abspath(path).startswith(SCRATCH_PREFIXES)            and not path.startswith(SCRATCH_PREFIXES))
```

**6.5 回归测试**

两个 bug 都按线上场景补了回归用例。流程是先在旧版本上确认能复现，再在新版本上确认通过：

```cs
=== 旧版本 v1.1（线上运行版本）===FAIL  16 budget stop -> human reply -> next new file is allowed (no immediate re-trip)FAIL  17 10 scratch files under /tmp do not consume the 2-file budget25/27 passed
=== 新版本 v1.2（Python 3.8 / 3.13）===27
```

先在旧代码上跑一遍这一步省不得：如果新用例在旧代码上也能过，它就证明不了修复有效。

**6.6 两个值得讨论的问题**

**问题 1：守卫拦住了用户授权的操作**

11:56 那次拦截，表面上看是自我保护生效了，可当时 Agent 执行的是用户明确授权的卸载。它被拦是 Bug 1 导致的，按设计本不该拦。

这里有个绕不开的矛盾：Agent 为了绕过限制自己去改配置，这种应该拦；用户明确要求卸载，这种不该拦。可单看一次工具调用，guard 分不出这两种情况。

目前的取舍是：状态目录和 reset 命令始终阻断；hooks 配置文件不做特殊保护，靠"停止期阻断所有变更"兜底。更好的做法可能是对 hooks 配置的修改一律走 ask，让人在确认框里拍板（见第九节）。

**问题 2：守卫类插件该装在哪一级**

这次全局安装本身就超出了预期。stop-line 是参赛作品，不该影响日常用的 Agent。守卫类插件一旦全局生效，会作用到所有项目和定时任务上；定时任务是无人值守的，弹出来的确认框没人点，任务就卡在那儿了。

我的结论是： **守卫类插件默认应该项目级启用，全局启用要用户显式选择。** 这次实测结束后，全局配置已经按用户要求卸掉了。

## 07

效果评估与局限

**7.1 Hook 层：确定性测试**

`evals/test_hooks.py` 共 27 项。每一项都把模拟的 hook 事件通过 stdin 喂给 guard 子进程，再断言退出码和输出跟 harness 里实际观察到的一致：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRhjO8xAWr4BHdvhgXWicuxjI1WPbWpzyCZ3HQpOic4DMBQTjoiaEsaOkobc6FV7EvFialPdkUQHSOGFqk1LYqNibdgPa4lLJApXmxrZzmjnsdYs/640?wx_fmt=png&from=appmsg)

测试里我还多加了一道检查。guard 是 fail-open 的，内部异常被吞掉后照样返回 0，这时"期望放行"的用例也会显示通过。所以除了故意构造坏输入的用例，任何一次运行只要产生了 errors.log 就判失败。开发过程中这道检查报过一次，查下来是测试本身写错了。

**7.2 Skill 层：触发测试**

**方法** ：17 条用例，每条交给一个独立的子 Agent。子 Agent 只能看到 16 个 skill 的清单和用户原话。清单里放了 systematic-debugging、database-migrations 这些真实的竞争者，每条用例单独打乱顺序，文件名不带提示，答案表放在子 Agent 读不到的目录里。

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr6Gcvgcic6icPEXtwziapomYQjSdYKsJDkeTH80xOPrrs61taFr9icPO6LogjBAibgfx4aQ1rFtia0icq441sx53Cx7bRK0bmNiaWcr1Go/640?wx_fmt=png&from=appmsg)

用户已经把问题说出口的场景（卡住了、反复失败、太费 token、要交接、要强推或删除）全部命中。漏掉的 3 条都是任务刚开始、还没出问题的场景（重构、迁移、部署）。打个比方，Skill 层现在能当刹车，还当不了安全带。

这也是 Hook 层必须存在的另一个原因：高危拦截和失败计数，不依赖 skill 有没有被加载。

还有个意外发现：在"修了三次""反复失败""跑到全绿"这三条用例里，stop-line 都和 systematic-debugging 一起被加载了，理由各管一摊，一个查根因，一个防死循环。这两个 skill 可以搭配着用。

**7.3 局限**

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr5vtVfxFZmibfqM1WzEC6IRXbb3YPJnjcmoJqJh4UbtQbloia01oHwAicBSjztzzJIaB5SOXaq3icTuUf8LbdwNeSicGSt19tdB8og4/640?wx_fmt=png&from=appmsg)

## 08

使用与配置

**8.1 目录结构**

```css
stop-line/                               插件根目录├── .codebuddy-plugin/plugin.json        CodeBuddy / WorkBuddy 插件清单├── .claude-plugin/plugin.json           Claude Code 插件清单├── hooks/│   ├── hooks.json                       插件 hook 配置（6 个事件）│   └── settings.example.json            手动写入 settings.json 用的片段└── skills/stop-line/    ├── SKILL.md                         预算、三哨兵、三级升级、交接、hook 消息应对    ├── references/                      归一化规则 / 交接规范 / 恢复流程 / hook 说明    ├── scripts/    │   ├── stopline.py                  离线日志扫描 + 共享检测规则    │   └── hook_guard.py                hook 入口    └── evals/                           hook 测试 27 项、触发用例与结果
```

**8.2 安装**

```bash
# 推荐：项目内临时试用，仅当前会话生效codebuddy --plugin-dir /path/to/stop-line
# 验证/hooks                                         # 6 个事件下各有一条 hook_guard.pycd stop-line/skills/stop-line && python3 evals/test_hooks.py   # 期望 27/27 passed
```

手动写入 settings.json 时注意三点：

- 合并，别覆盖：已有的 hooks 配置（比如团队的上报 hook）要保留
- 解释器写绝对路径：比如 /usr/bin/python3，避开 PATH 差异
- 优先项目级（<项目>/.codebuddy/settings.json），别默认装到全局

**8.3 参数**

通过环境变量配置，直接写在 hook 命令前面：

```powershell
"command": "STOPLINE_MAX_FILES=40 STOPLINE_BOUNDARY=deny python3 \"${CLAUDE_PLUGIN_ROOT}/skills/stop-line/scripts/hook_guard.py\""
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr7Vwo6mcPvqAu91eUynaB0pkfibec0ImWE0LDib26jDhUDeS3ObkNIYOc7FogozuSlYRgD7HjPict5V8LAHLoCDEOc3hYA0Za3oHY/640?wx_fmt=png&from=appmsg)

高危命令规则（23 条，其中 13 条必须确认）和只读白名单，都可以按团队的实际情况扩展，例如：

```python
# scripts/stopline.py · BOUNDARY_PATTERNS(r"\bhelm\s+(upgrade|uninstall|rollback)\b", "block",   "cluster mutation"),(r"\bmy-deploy-cli\s+release\b",             "confirm", "internal release"),
```

**8.4 运维**

```bash
python3 scripts/hook_guard.py status        # 查看最近会话的计数器（仅限人工执行）python3 scripts/hook_guard.py reset         # 重置最近会话（仅限人工执行）
```

Agent 停下后想让它继续，直接回一条消息就行。

## 09

总结与后续

**9.1 几点体会**

1. 止损不能只靠 Prompt。 上下文腐化、自我监督失效、长上下文里计数不准，这些正是止损要防的，也恰好会让 Prompt 失效。
2. 计数和拦截放控制面，判断和交接留在数据面。Hook 不经过模型推理，模型绕不过去；但 Hook 不懂语义，该问还是该停、下一步做什么，还得模型来判断。
3. 停下来一定要配交接。 光停不交接，等于把问题原样丢给下一个人。交接里最有用的是"已排除的假设"那一节。
4. 守卫本身必须 fail-open、never-trap。 守卫出了 bug，不能把整个会话也拖垮。
5. 不同 harness 的协议差异比我预想的大。 消息从哪读、失败怎么表达、frontmatter hook 的作用域，都得实测过才敢下结论。

**9.2 后续计划**

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr64AVkJK1RXmKWiariaiageXUAoyWekZEGntFn68enJojk70lSgBAdFrOQPue7dJ4Aibwgl7l5tGibuuop9P2PTIibNhTnNTYQy3NBTs/640?wx_fmt=png&from=appmsg)

## 10

附录

### A. 参考资料

- ### CodeBuddy Code Hooks Reference：https://www.codebuddy.ai/docs/cli/hooks
- ### CodeBuddy Code Plugins Reference：https://www.codebuddy.ai/docs/cli/plugins-reference
- ### Agent Skills 开放规范：https://agentskills.io
- ### Skill 安装量与热度数据：skills.sh、Skillselion（2026-11-01 快照）、GitHub Trending 周榜（2026-10-30 快照）

### B. Hook 事件输出速查

![](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr7cwS5DoL3GQPE3bOlOYuQXKHb0t3SCg0ibRxSOafnkibaB1xK7mIRQklsRqXzwZwzZnFjq4KTngobwtCtIbFFAbUCBwDoEDKQm0/640?wx_fmt=png&from=appmsg)

\-End-

原创作者｜李隆熹

感谢你读到这里，不如关注一下？👇

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95UnhD9f7ia4T3ufXM1liaxxffiaEy41n0icohEC2qDS05icapaN4iaTVfsClibPRmqOjNW6q33PZicAVoSOg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

扫码领取腾讯云开发者专属服务器代金券！

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZRhjO8xAWr4nU3obq4B4URKhzJMmibw1uR1ZehOtyeel5hYevARgDqdKxqXvtzclLhu7g28g6PBib8M2uaQegic6MrCdBic0SdHh4XUQODQkmKk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe979Bb4KNoEWxibDp8V9LPhyjmg15G7AJUBPjic4zgPw1IDPaOHDQqDNbBsWOSBqtgpeC2dvoO9EdZBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7) ![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95pIHzoPYoZUNPtqXgYG2leyAEPyBgtFj1bicKH2q8vBHl26kibm7XraVgicePtlYEiat23Y5uV7lcAIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过