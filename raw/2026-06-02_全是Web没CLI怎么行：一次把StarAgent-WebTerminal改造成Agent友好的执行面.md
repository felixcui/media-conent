---
title: "全是 Web 没 CLI 怎么行：一次把 StarAgent WebTerminal 改造成 Agent 友好的执行面"
source: "阿里云开发者"
url: "https://mp.weixin.qq.com/s/5qwjuSZmENMovuEStczQEg"
author: "风夏"
date: "2026-06-01"
---

# 全是 Web 没 CLI 怎么行：一次把 StarAgent WebTerminal 改造成 Agent 友好的执行面

## 阿里妹导读

全是 Web，没有 CLI，怎么行？Agent 都会写代码了，远程排障还要人肉点网页、复制命令、盯滚动条，这画面多少有点"地铁老人看手机.jpg"。本文记录一次围绕 StarAgent/Drogo WebTerminal 的工具化实践：我们没有把 GPU hang、core dump 调试等场景固化成一个个"祖传脚本套件"，而是把 WebTerminal 抽象成稳定的 CLI 执行面，再用 Skill 描述操作方法。Agent 在任务中动态生成命令、读取结果、继续决策，最终完成远程 GPU hang 分析、文件上传下载、以及 Emacs + eshell + gdb 的交互式 coredump 调试验收。

插播：我对 Skill 的态度很朴素：Skill 不是法器，不是咒语，也不是"复制进去 Agent 就突然开悟"的玄学符纸。Skill 本质上就是说明书，是贴在工具箱盖子上的那张"先拧这个、再接那个、别把手伸进风扇里"的操作指南。真正能把活干成的，必须是 CLI：参数清楚、行为稳定、输出可解析、错误可复现、证据能落盘。所以这套东西的核心不是"写一个很长的 Skill 让 Agent 背下来"，而是把能制度化的都制度化，把能流程化的都流程化，把以前靠老师傅手感、群里口口相传、网页上点点点的部分，全部压进 wt 这种可执行接口里。Skill 只负责告诉 Agent：什么时候该登录、什么时候该 run、什么时候该 interact、什么时候该停手问人。至于真正挥锤子的活，必须交给 CLI。

## WebTerminal 黑屏模式补充说明

号外号外，重大更新：WebTerminal 终于可以像 SSH/SCP 一样用了

这轮最核心的新能力很直接：新增wsh/wcp，把 WebTerminal 从"打开浏览器点来点去"推进到"直接黑屏操作"。用户可以手动上去敲 shell，程序也可以直接调用命令；传文件也不再靠页面弹窗，而是走 wcp ，用法尽量贴近 ssh / scp 的肌肉记忆。

感谢@先濠提供的多屏多容器支持，这让 session -> container -> role -> host 这条链路终于能落到比较完整的模型里，而不是只盯着一个默认页面硬猜。

也感谢和@思潜的交流。聊完之后思路突然变得很明确：既然目标是让 WebTerminal 更像原生终端，那就别老想着再包一层 CLI 了，干脆往native terminal 化继续推，连 CLI 味儿都尽量去掉。

### 核心用法

先通过浏览器完成一次官方登录，把 cookie 缓存下来：

```
$ ./bin/wt auth login --target-ip x.y.z.w
wt: waiting for browser login cookies; finish login in the opened browser
authenticated: True
user: default
source: browser
```

之后就可以直接黑屏进 shell，或者把它当成可编程的远程命令执行入口：

```
$ ./bin/wsh x.y.z.w
attached direct: x.y.z.w
$ ./bin/wsh x.y.z.w -- 'hostname; pwd'
hippo-033126067104.na175
/home/admin/hippo/worker/slave/drogo-share_worker-h20-na175.worker-h20-na175_11_33/main
```

文件传输也直接走wcp：

```
$ ./bin/wcp /tmp/wcp-demo.txt x.y.z.w:/tmp/wcp-demo.txt --force
uploaded: /tmp/wcp-demo.txt -> /tmp/wcp-demo.txt
$ ./bin/wcp x.y.z.w:/tmp/wcp-demo.txt /tmp/wcp-demo.down.txt --force
downloaded: /tmp/wcp-demo.txt -> /tmp/wcp-demo.down.txt
```

### 这次补上的关键体验

- 认证只需要浏览器进一次门，后续操作复用 auth cache。默认 cache 在 `~/.drogo-webterminal-helper/direct/default.auth.json`，wsh/wcp会直接复用；如果换机器，也可以把这个 cache 拷过去继续用。
- shell 终于像个正常终端。exit不再卡死，远端 EOF / closed / reset 会正确退出；本地 terminal 的 rows / cols 会同步给 WebTerminal，窗口 resize 后也会继续同步，不再是一个小得离谱的假 shell。
- 浏览器模式还保留，但不再是主路径。wtsh/wtcp --transport browser仍然可以作为兜底；默认使用 direct HTTP/WebSocket 做黑屏操作。

### 一点遗憾

纯黑屏登录暂时没有硬上。阿里 SSO 的 HTTP 登录链路会进入 RSA、风控、账号安全检查，继续硬怼收益不高，还容易把账号搞进风险提示。所以当前最稳的路线是：浏览器负责合规授权，真正干活走黑屏 shell。不算 100 分的"全黑屏"，但已经把最高频、最烦、最容易误操作的部分从网页里拽出来了。

## 前言：先把仓库拍你脸上

代码仓库在这里：`foundation_models/webterminal-cli`。

先说结论：如果你也受够了"打开网页、点登录、复制命令、盯输出、再复制下一条"的人工智障流水线，那这个仓库就是给你准备的。它不负责让 WebTerminal 变得更漂亮，它负责让 WebTerminal 终于长出 CLI。是的，2026 年了，我们还在为"能不能别用手点网页"而奋斗，听起来很离谱，但工位现实就是这么朴素又残酷。

这玩意儿的目标也很直接：让 Codex / Cursor / Claude Code 这类 Agent 不再隔着 DOM 猜命，而是通过wt像普通 shell 一样控制远端。能跑命令，能传文件，能开 gdb，能一条条交互，能把证据落盘。少一点"我好像看到了"，多一点"日志在这，别装死"。仓库欢迎试用、拍砖、提 MR，尤其欢迎那些一边骂"tmd 怎么全是 Web"，一边还能把工具补上的同学。

## 背景：Agent 要的不是另一个网页按钮，它要手脚

最近很多 AI Coding / Agent 实践都会落到同一个问题：模型会想、会写代码，甚至能一本正经地给你写 800 行设计文档；但真正接入企业内部系统时，经常卡在"可执行接口"上。它脑子很大，手却被绑在网页按钮上。

远程机器排障就是典型场景。人可以打开 WebTerminal，点击登录，输入命令，看输出，再决定下一步；但 Agent 如果只能操作浏览器 DOM，它看到的是按钮、输入框、滚动区域，而不是一个稳定、可组合、可回放的执行协议。然后场面就变成：Agent 在旁边吟诗，人类在网页里点点点。这不就是"AI 时代的纯手工流水线"吗？

这次实践的起点很朴素：希望 Agent 能在目标机器上完成 GPU hang 分析。结果做着做着发现，坑不是 GPU hang 一个坑，而是"WebTerminal 没有 Agent 友好执行面"这个大坑。于是需求开始膨胀：

- 目标 IP、操作步骤都必须参数化，框架和具体案例隔离
- 不做固定 suite，Agent 应该像工程师一样动态发送命令
- WebTerminal 浏览器会话要持续存在，不能每次操作都重新登录
- 上传下载要走 WebTerminal 后端 API 或协议，不能靠 DOM 自动化点弹窗
- 调试要是真交互：Agent 可以一条条给 gdb / emacs / eshell 发命令，拿到 response 后继续判断

最后沉淀出来的不是一个"GPU hang 工具"，而是一个面向 Agent 的 WebTerminal CLI：wt。不是再造一个网页，不是写一个固定脚本，也不是在 DOM 上跳舞，而是给 Agent 一双能干活的手。

## 先看效果：别先讲架构，先看能不能干活

在实现完成后，我们用目标机器 x.y.z.w 做了三类验收。先把 PPT 收一收，工具这种东西，能不能跑比"愿景很大"重要。

第一类是普通命令执行。Agent 通过 `wt run` 发送命令，命令输出会被捕获成本地证据文件，包括 raw ANSI、去 ANSI 的 plain text，以及 xterm snapshot。不再是"我刚刚屏幕上好像看见了"，而是"证据在这，别耍赖"。

第二类是文件传输。上传下载不再点击页面弹窗，不再祈祷浏览器下载目录没抽风，而是复用已登录浏览器上下文，直接调用 WebTerminal 文件 API。

第三类是交互式调试。`wt interact` 会启动一个本地 HTTP 控制面，远端交互程序保持运行；Agent 每次只发送下一条命令，拿到结果后再决定下一步。这才叫调试，不叫"把 gdb 命令写进遗书"。

## 1. 目标：把 WebTerminal 变成 Agent 友好的执行面

这类工具最容易走偏的地方，是一上来就写一个场景套件。这种方式短期有效，但它和 Agent 的能力是冲突的：场景逻辑被写死后，Agent 只能"调用工具"，不能"分析现场"，智商被强行锁死。

所以这个实现刻意把职责拆开：

| 层次 | 职责 | 不做什么 |
|------|------|---------|
| WebTerminal 页面 | 登录、角色选择、审计、心跳、官方连接链路 | 不承载任务逻辑 |
| wt CLI | 会话复用、命令发送、输出捕获、文件 API、交互控制面 | 不内置具体排障 suite |
| Skill | 描述操作方法、风险边界、推荐命令模板 | 不绑定某个 IP 或某个案例 |
| Agent | 动态规划、执行、观察、复盘 | 不绕过授权链路 |

一句话总结：CLI 提供稳定手脚，Skill 提供行动章法，Agent 负责临场判断。别把 Agent 当高级 crontab 用，它会委屈，我们也亏。

## 2. 会话设计：授权留在浏览器，执行交给 CLI

企业内部 WebTerminal 通常不是一个裸 SSH。它背后有 SSO、角色、审批、审计、心跳、跳板、容器选择等一串逻辑。

因此 `wt session start` 的设计是：启动或复用一个持久 Chromium，会话仍由官方 WebTerminal 页面建立；用户完成登录后，CLI 只复用页面里已经存在的终端实例。会话 ready 后，后续所有命令复用同一个浏览器上下文。

这个设计带来几个直接收益：
- 授权、审计、心跳仍走官方页面链路
- CLI 不保存 SSO token，也不绕过登录流程
- 目标 IP 是参数，不会写死在实现里
- 多轮排障可以共享同一个远端 shell 状态

## 3. 命令执行：不做 suite，做动态闭环

`wt run` 是最基础的能力：发送一条 shell 命令，等待结束标记，返回远端 exit code，并把输出落盘。

输出捕获分三份：
- `*.raw.log`：原始 ANSI 输出，适合保留完整现场
- `*.plain`：去 ANSI 后的文本，适合 Agent 解析
- `*.snapshot.json`：xterm buffer 快照，适合排查全屏程序或显示问题

以 GPU hang 为例，Skill 只给出建议命令，不把诊断固化进 CLI。Agent 读完结果后再决定是否继续查 wait channel、是否需要 gdb attach、是否需要用户批准侵入式操作。这里的关键不是"命令多"，而是"下一步有脑子"。

## 4. 文件传输：从 DOM 自动化改成 API 调用

我们把文件传输实现成了直接 API 调用。CLI 复用已登录浏览器上下文里的 cookie 和终端状态，调用 WebTerminal 文件接口。下载路径先拿文件 head，获取 fileUuid、分块数、总大小和 md5；再按 block 下载；最后校验 size/md5，并可选通过远端 sha256sum/stat 二次校验。上传路径同样分块发送并校验。

能协议化就协议化，少点玄学，多点 checksum。

## 5. 交互式调试：默认接口应该像普通 shell

最终把 `wt interact` 改成默认启动一个本地 HTTP server：

| Endpoint | 用途 |
|----------|------|
| GET /health | 查看交互会话是否存活 |
| GET /summary | 查看完整步骤摘要 |
| GET /snapshot | 获取 xterm 屏幕快照 |
| POST /command | 发送一行命令，按 prompt regex 等待结果 |
| POST /send | 发送 raw keys，适合 emacs/vim/TUI |
| POST /drain | 读取当前缓冲输出 |
| POST /close | 退出远端交互程序并关闭本地 server |

关键点是：远端程序只启动一次，状态在多次 HTTP 请求之间保持。gdb 的 $x、当前 frame、breakpoint、Emacs buffer，都不能每请求一次就失忆。

## 6. 验收案例：在 Emacs 里写 crash.c，再用 eshell + gdb 定位 core

在远端打开 `emacs -nw -Q`，通过 raw key 创建 C 文件，进入 eshell 编译运行，再在 eshell 里启动 gdb 调试 coredump。这个流程像什么？像让 Agent 穿着拖鞋跑了个铁人三项。

GDB 输出证明调试链路有效：

```
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x0000000000401168 in crash (n=7) at /tmp/wt-emacs-crash.c:12
12          return *ptr + item.id + n;
```

`bt` 看到调用栈，`info locals` 和 `print` 给出关键变量：`ptr = 0x0`，第 12 行对空指针解引用导致 coredump。凶手就是它，证据链闭合。

## 7. GPU hang 分析：场景逻辑留给 Agent

基于 Skill 推荐的命令做 GPU hang 分析，没有 `wt gpu-hang --please-save-me` 这种神棍命令，只有 Agent 根据现场一步步查。机器没有 active GPU hang，但 kernel log 里有历史信号。如果当时存在 GPU 进程，Agent 可以继续查看，必要时请求用户批准后再执行侵入式操作。排障不是法术，不要没病也上猛药。

## 8. Skill 的角色：把经验写成操作方法，而不是写死代码

Skill 不是"更长的 README"，而是 Agent 执行远程任务时的操作规约。它写清楚了如何启动 session、什么时候用 run/attach/interact、侵入式命令需要用户批准等。新增场景更可能是改 Skill，而不是改 CLI。

## 9. 几个设计取舍

- **为什么不直接连 SSH**：WebTerminal 承载授权、审计、角色、心跳和访问入口，直接 SSH 可能绕过治理链路
- **为什么不把 GPU hang 做成内置命令**：固定 suite 会限制 Agent 成"报告生成器"
- **为什么交互控制面用 HTTP**：简单、可调试、Agent 容易调用，接近 ReAct loop
- **为什么保留 interact-script**：固定 expect 脚本对 smoke test、固定初始化流程仍有价值

## 10. 可以复用的工程模式

1. 先抽象执行面，再沉淀场景
2. 授权和执行要解耦
3. 输出必须可保存、可解析、可复盘
4. Skill 应该写边界和方法，而不是把所有业务逻辑变成代码
5. 交互式程序要按状态机设计
6. 文件传输要协议化

## 结语

让 Agent 从"会聊天"进化到"能上手干活"。这中间差的不是一句 prompt，差的是一整套可执行、可观测、可复盘的工程接口。

## 附录：当前 CLI 能力速览

- `wt session` — 管理持久 WebTerminal 浏览器会话
- `wt status` — 查看当前终端状态
- `wt run` — 执行一条 shell 命令并捕获输出
- `wt attach` — 本地 raw TTY 直接接入 WebTerminal
- `wt interact` — 启动 live HTTP 交互控制面
- `wt interact-script` — 执行固定 expect 风格交互脚本
- `wt snapshot` — 获取 xterm buffer 快照
- `wt ls-files` — 通过 WebTerminal 文件 API 列目录
- `wt download` — 通过 WebTerminal 文件 API 下载文件
- `wt upload` — 通过 WebTerminal 文件 API 上传文件
- `wt direct-info` — 输出脱敏后的直连协议材料
