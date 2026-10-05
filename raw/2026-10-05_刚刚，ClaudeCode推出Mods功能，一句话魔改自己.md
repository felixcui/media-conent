# 刚刚，Claude Code 推出 Mods 功能，一句话魔改自己

**作者**: 尹John

**来源**: https://mp.weixin.qq.com/s/guoG9O02Ryza01Im2cVTVw

---

## 摘要

Claude Code 推出 Mods 功能，允许用户通过几行 TypeScript 或直接向 Claude 描述需求，修改其行为、界面和内置功能，并实现热重载即时生效。Mods 本质是挂在事件上的中间件函数，可观察、改写或接管工具调用、权限请求等事件，随插件分发，从 2.1.287 版本起默认开启。

---

## 正文

尹John 尹John

在小说阅读器读本章

去阅读

刚刚，Claude Code 推出了 Mods 功能。

用几行 TypeScript，就能 **改掉 Claude Code 的行为、重画它的界面，甚至把它的内置功能换成你自己写的版本** 。

不会写也没关系，直接跟 Claude 说你想要什么， **它会自己写好、装上、热重载，当前会话里马上生效** 。

Mods 随插件（plugin）一起分发，在 CLI 或桌面端里用 `/plugin` 就能安装，从 **Claude Code 2.1.287** 开始默认开启。

![2.1.287 版本](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFknqGrMKmprmGvDvL3M5nZ1cqyVuOZGQuQKR9ibvEsQehxXAAaqF6ib1F76aLg9ibm2nspSyqdxCicU36ibDuVmwCtibupJwYgvKjNEk/640?from=appmsg)

2.1.287 版本

Claude Code 负责人 Boris Cherny 表示：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> Mods 简直疯狂。你现在只需要提示一下，就能把 Claude 定制成你想要的工作方式和样子。每个人的工作方式都不一样，没有理由让所有人都用一模一样的 Claude。

## Mods 是什么

01

Claude Code 每做一件事，都会发出一个事件：调用工具、申请权限、提交 prompt、开始和结束一轮对话，甚至是画屏幕上的某一块。

**一个 Mod，就是挂在某个事件上的一个函数。** 它可以在事件之前跑、之后跑，或者干脆取而代之，也可以把事件包起来前后各跑一段。

Anthropic 工程师 Lydia Hallie 称，Mods 基本上就是 **Claude Code 的中间件** 。

写过 Express 或 Koa 的同学应该会很熟悉，每个 hook 永远是三个参数：

```
●●●on("tool.call", { tool: "Bash" }, async ($, e, next) => {
  // $    Mods API：ui、session、state、store、fs、process、http、tool、command、model……
  // e    这次事件的输入，纯数据
  // next 把 e 交给其他插件，最后交给 Claude Code 自己的行为
  return next(e);
});
└
```

一个 hook 能做的动作只有三种： **观察、改写、接管** 。观察是先调 `next` 再看结果，改写是改了 `e` 再交给 `next` ，接管则是不调 `next` 、自己返回结果。

接管最典型的用法，就是说「不」。

Anthropic 在 GitHub 上公开征求意见时录过一组演示，那会儿它还叫 Function Hooks。其中一个给 `tool.call` 加了 matcher，只匹配命令里带 `curl` 的 Bash 调用，然后不调用 `next` ，直接返回 `deny` 和理由：

![一个说不的 hook](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFkFb1Zl2H15gBcPTtFtgCYZz79o30Pgvzkjic5ZWumOIJLiaCAJbtVrdZhFFUfQZPr8KW3spIice5zExd09zHj2ICXVbXrlEx2J7k/640?from=appmsg)

一个说不的 hook

让 Claude 去 curl 一个网址，模型调用 Bash，被 hook 拒绝， **工具根本没跑** ，拒绝理由作为工具报错回到了模型那里。

整个过程既没有弹权限窗口，也不用去改配置文件。

这样一个函数能做的事，官方列了这几类：在 prompt 发给模型之前改写它；拦下、改写或重试一次工具调用；替你批准或拒绝一次权限请求；在 Claude 读到工具输出之前，把里面的密钥抹掉。

Mod 还能改你看到的东西。Claude Code 给每次工具调用都画一行，另一个演示挂在 `ui.render` 上、匹配 ToolUse 组件，换成自己返回一段黄色文字：

![插件画的黄色那行](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFlYrFlUxbLSKrGfibibia2Z2BibayJO5xRRKKPwUC4iaVTnHQgULcpSUVpZHViaGJHJErUZ8UDDWVAYyibQnIsg1VdBDlL9KeMqdSTXvU/640?from=appmsg)

插件画的黄色那行

黄色那行就是插件画的， **Claude Code 自己的那行没有再画** 。同一个会话切到桌面端，这一行也在。

工具结果、Claude 向你提问的对话框，这些官方界面都能改写或替换。Mod 还能加按钮和输入框，其他 Mod 也能响应这些按钮。目前 Mod 可以画在终端、桌面端，或者两边都画。

多个 Mod 挂在同一个事件上时，按加载顺序执行，先加载的最先看到事件、最后拿到结果。

演示里 hook A 和 B 都在 `next` 前后各打一行日志，A 先注册时是 A 包着 B，把 B 剪切贴到 A 上面再跑一遍，日志就变成了 B before、A before、A after、B after：

![先注册的包住后面的](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFlSmxPYJqgmibTU7mjBtChSXlSfNZN9mC9eFtXTVUXOTKtp6ngJibrZqGkrJ9Ot6yib85cMUYuQ1NJicx4vJmk8fj4yUDGk6zYdbAc/640?from=appmsg)

先注册的包住后面的

像洋葱一样一层套一层，所以管理员想管控就往前插，想设默认值就往后加，不同作者写的 Mod 也能这样叠着用。

注意：上面这几段演示都录于上线前的早期版本，有些 API 和正式版已经不太一样了。

那它和之前的 hooks 有什么区别呢？

hooks 已经能拦截一部分事件，但 **没法改写事件、画新界面、替换功能，这些 Mods 都可以** 。

而且 Settings hook 每个事件都要跑一次 shell 命令，靠 stdin/stdout 传 JSON；Mod 则只加载一次、常驻在会话里，能保存状态，能画随事件实时更新的界面，还能反过来调用 Claude Code 开面板、跑进程、注册斜杠命令，甚至注册一个给模型用的工具。

## 三个官方示例

02

Addy Osmani 写的官方入门指南，用了三个 Mod 来展示它能干什么。

第一个叫 Token Weather，在输入框上方画一行上下文「天气预报」：

![Token Weather](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFnibmprvo04zxkd5h803Vz9N6N7WD9o5YDHWpNAwSLFjGTHL7kxUK3QgwGLDUKrF4Eb0P8ZXy42zhWEzcpOJaDNT2krGO7qyQSE/640?from=appmsg)

Token Weather

上下文用量不到 25% 是晴 ☀，25-49% 多云，50-74% 阵雨，75-89% 雷暴，90% 以上则是「快要 compact 了」↯。

后面跟着百分比、已用 token / 窗口大小、最近 12 轮的迷你柱状图，以及上一轮涨了多少。

在桌面端的真实会话里，每一轮让 Claude 多读几个文件，天气便从晴一路变成了雷暴：

![Token Weather 实际效果](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFnvPFfIkicMcTCNuHeOjgb9PCKeLqBTOIxgKXfyicZdLgKuCicnyNRZpicmInJjzeySs5KS7dm7sT7mydQcib6DiaEINNe1XwUy2wE64/640?from=appmsg)

Token Weather 实际效果

整个 Mod 大约 80 行，而 **你其实可以一行都不写** 。官方给了个捷径，在 Claude Code 里直接粘贴这段描述就行：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 帮我做一个叫 token-weather 的 Claude Code mod：在输入框上方的那一栏里，实时显示我的上下文窗口「天气预报」。
> 
> 一行里要显示：
> 
> • 一个天气图标和词，表示上下文窗口有多满：25% 以下 ☀ Clear（黄色），25–49% ☁ Cloudy（青色），50–74% ☂ Showers（蓝色），75–89% ☇ Storm（品红），90% 及以上 ↯ Compact soon（红色）。
> 
> • 已用百分比，然后是已用 token / 窗口大小，比如「134.4k / 200k」。
> 
> • 最近 12 轮的小图表，用 ▁▂▃▄▅▆▇█ 画。
> 
> • 上一轮增加了多少，比如「▲ +98.3k last turn」。
> 
> 每一轮结束后都要更新。

Claude 会问一次要不要为当前会话开启热重载，同意之后，这一轮结束时那一栏就出现了。

之后你还可以接着提要求（「让 Storm 从 70% 开始」「在最后加上花了多少美元」），一边说一边看它变。

**这段 prompt 从头到尾只描述了想看到什么，一个 API 都没提。**

第二个 Blast Radius，管的是危险命令。

当 Claude 要用 Bash 跑 `rm -rf` 、 `git reset --hard` 、 `git clean` 、强推或者数据库迁移时，Blast Radius 会先把这次调用扣下来， **算出这条命令会影响哪些东西** ，再弹出一个带 Proceed 和 Cancel 的面板：

![Blast Radius](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFkSw8M1ic16qbyYKINicgPa0HRfsxLk2Y77pt4BFX1iaoCgYUm6A8DRCVsWZeOo9Wico3eJQjZlYYlL4eCgYjSFvlPJb8npdGbWaIg/640?from=appmsg)

Blast Radius

演示里它扣下了 `rm -rf build` ，列出会删掉的 9 个文件。按 2 取消，Claude 会收到一条带原因的拒绝，等你说「删吧，我确定」再来一次，按 1 才真正执行。

终端里也是一样：

![Blast Radius 终端版](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmibOY0exKibYLzHWKA0yOXbXheOEvARjSjcEZGIDwUIF0E7BypTX6W70C7NEkK5clxia0GiboUHL2Qt1QM5ZvUFzhibxJMrcuXuON4/640?from=appmsg)

Blast Radius 终端版

窗口不够宽、放不下侧边面板时，它会退回到输入框上方显示：

![Blast Radius 退回输入框上方](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFmMdBlekm84DCQyl5lK7mk10ed6H1bXQcCsBfFs2KoO3gBPOibntd08yYKUZV1ibkN5ticawmCuVC8DFSUqZicjsREgg5f2Vml8chE/640?from=appmsg)

Blast Radius 退回输入框上方

它用的正是「接管」：不调用 `next` ，直接返回 `{ deny: "…" }` 。dry run 的数据则来自 `git status --porcelain` 、 `git clean -n` 这些工具自带的命令。

不过官方也提醒了， **它只是安全网，不是权限系统** 。它看的是命令文本， `$(…)` 、别名、调用了 rm 的脚本都能绕过去，真要硬拦截还得靠权限规则。

Replay Theater 则用来回放 Claude 刚改了什么。

一轮对话进行时，它会记下每一次 Edit 和 Write 改了哪个文件、改前改后是什么。

演示里让 Claude 把 greet 全局改名为 welcome，它在四个文件里改了六处，这一轮结束后输入框上方出现一个回放提示：

![Replay Theater 记录编辑](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFkBh8HbjkuaiaFn4KTWJ2usMbg7fzes9dLYdO0HsBqmzqezGrFia0KUWpHEPwMVtUMtqUXgSDqZNAUSxlhlGf93ff5BygslYCoxQ/640?from=appmsg)

Replay Theater 记录编辑

按 r（或输入 `/replay` ），就会打开一个面板，一步一个 diff 地回放，带编号步骤条和 Prev、Next、Close 按钮：

![Replay Theater 逐步回放](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmxKYQSmGJZgMib4coHeDsnXWdrFNPy30BhXbg9Wfoic3uHswKnLQJnxF75iaicwkZQJRIicgfFpZYh2ACF5ApUrSl7nwRrPlicqIibicM/640?from=appmsg)

Replay Theater 逐步回放

它全程只观察，不拦也不改任何一次编辑。全屏时面板停靠在右边，80 列宽时则直接内嵌在输入框上方，Mod 画的是同一棵树，摆在哪由界面决定：

![Replay Theater 内嵌](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnM8nicnYniaoG3rPpKpRYmvvicH7bSnkgDwiauuAWpc4WvkjY6zMVGwzEiaefkHDQRicCrACY55ubt9iaUJuvgCh9owC1wbbicuiaQf3Q4/640?from=appmsg)

Replay Theater 内嵌

## 让 Claude 帮你写

03

最省事的，还是在交互式会话里直接跟 Claude 描述你想要的 Mod，比如「做一个 mod，在输入框上方显示当前 git 分支」。

Claude 靠的是一个内置的 `plugin-authoring` skill，里面写清楚了 Mod 该写在哪、当前版本有哪些事件和方法、怎么加载。你也可以手动输入 `/plugin-authoring` 加载它。

设计帖里有一个完整演示， **人只打了一句话** ：「把工具输出里的高熵密钥抹掉，并告诉模型抹了几个」。

Claude 先加载写插件的 skill，写好两个清单文件，再写一个挂在 `tool.call` 上的函数，扫描像密钥的长串、按熵打分、把分高的换成标记，最后自己跑完校验。

带上插件重新启动后让它读 `.env` ， **两个 key 都变成了 `[REDACTED_SECRET]`** ，普通的那行原样保留，模型还被告知了具体发生了什么：

![一句话做出的抹密钥插件](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFlgnxUE8LJeQzX6OnQfqSjkfdK5NmON53Aubvs2002DNRpzuqM4GsODlu5gI7lFghzP1PPC4ibFNHQOYcMxz66ceF4iaVWKUXEiaE/640?from=appmsg)

一句话做出的抹密钥插件

另一个演示在桌面端，需求同样只有一句：做个插件，把屏幕上的数字和邮箱都藏起来，鼠标悬停时再显示。Claude 写好、两条命令装上，不用重启，当前会话就生效了。

它写的 hook 挂在 `ui.render` 上，所以 **Claude 读到的仍然是真实文本，变的只是显示** ：

![共享屏幕时藏住数字和邮箱](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFnssvKOfv4ECtlLibl3WrOqPcFZS3rtkoxiaibpO3S2CDYuyGgzx0lMYPictuyicgqzb9ibPRoPJVlHSGGRKIibWdDhMMyR5sJx0vdhIw/640?from=appmsg)

共享屏幕时藏住数字和邮箱

让它出本季度报表，表格里所有数字和邮箱都被藏了起来，指到哪个才显示哪个，问 EMEA 的增长率，它照样能按真实数据答出来。

正式版里，让 Claude 写 Mod 的流程是这样的：

1\. Claude 把 Mod 写进当前会话专属的目录 `~/.claude/dev-mods/<会话 ID>/` 。因为 `~/.claude` 是受保护路径，default 和 acceptEdits 模式下每个文件都要你批准一次

2\. 保存第一个文件时，Claude Code 会问是否为本会话开启热重载。选 Enable for this session，Mod 会在这一轮结束时加载，之后每次修改都在轮次结束时重载；选 Not now 则暂不加载，下次启动这个会话时再加载

3\. 运行 `/plugin` ，按 Tab 切到 Installed 标签页，就能看到这个 Mod，也可以在这里关掉它

4\. 不满意就继续跟 Claude 说要改什么

这个 Mod 只在写它的那个会话里生效，会话目录超过 `cleanupPeriodDays` 后还会被清理。

想留着用，就把目录拷到比如 `~/mods/git-branch` ，之后用 `claude --plugin-dir ~/mods/git-branch` 启动，或者放进 marketplace 分享给别人。

另外，在 `claude -p` 、dontAsk 模式这类没人能点批准的会话里，或者在没信任过的目录、开了 `--safe-mode` / `--bare` / `disableAllHooks` 的情况下，Claude 写的 Mod 都不会加载。

## 自己写一个

04

想看懂 Mod 的代码长什么样，官方文档给了一个 first-mod 教程：统计 Claude 调用了多少次工具，把次数显示在 spinner 旁边，再加一个 `/tally` 命令。

![spinner 旁的工具调用计数](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFlBZBL9fFuibsWfH2kESkbdv480xIickRNOCG68FJRY1ic3icf6l89gApKDDXUGXxDjYckb1Due2ZFQnoLEaOPI7sVNxib0By5ibwaZ8/640?from=appmsg)

spinner 旁的工具调用计数

前提是 Claude Code 版本在 2.1.287 及以上（ `claude --version` 查看）。 **不需要 Node.js，也不需要打包和构建** ，`.js` 和 `.ts` 文件 Claude Code 直接就能加载。

目录结构只有三个文件：

```
●●●first-mod/
├── .claude-plugin/
│   └── plugin.json
└── hooks/
    ├── hooks.json
    └── register.js
└
```

`plugin.json` 是普通的插件清单：

```
●●●{
  "name": "first-mod",
  "version": "0.1.0",
  "description": "Counts Claude's tool calls, shows the count beside the spinner, and adds a /tally command",
  "author": { "name": "Your Name" }
}
└
```

`hooks/hooks.json` 里的 `modules` 指向你的代码，有了它，这个插件才算一个 Mod：

```
●●●{
  "description": "The first-mod hooks module",
  "modules": ["./register.js"]
}
└
```

`register.js` 是 Mod 的本体，官方叫它 hooks module：

```
●●●// 计数，下面几个 hook 共用
let calls = 0

// Mod 加载时，Claude Code 调用一次
export function register(on) {
  // 会话开始时（第一条 prompt 之前）运行
  on('session.start', async ($, e, next) => {
    // 注册 /tally 命令
    await $.command.register({
      name: 'tally',
      description: 'Show how many tool calls Claude has made',
    })
    return next(e)
  })

  // Claude 每次要用工具时运行
  on('tool.call', async ($, e, next) => {
    calls += 1
    // 让界面重画，显示新的计数
    $.ui.invalidate('ui.render')
    // 工具照常运行
    return next(e)
  })

  // 只在输入 /tally 时运行（matcher 过滤）
  on('command.run', { command: 'tally' }, async () => {
    return { text: 'Claude has made ' + calls + ' tool calls since this mod loaded' }
  })

  // 每次画 spinner 时运行
  on('ui.render', { component: 'Spinner' }, async ($, e, next) => {
    // 保留原来的 spinner，在后面加上计数
    return next({ ...e, props: { ...e.props, suffix: ' · tool calls: ' + calls + '…' } })
  })
}
└
```

四个 hook 正好把三种动作都用上了： `session.start` 和 `tool.call` 是观察， `command.run` 是接管， `ui.render` 是改写。

然后用 `--plugin-dir` 加载，这个参数只在本次会话里加载插件，不会安装：

```
●●●claude --plugin-dir ./first-mod
└
```

让 Claude 做点需要好几次工具调用的事，spinner 后面就会出现不断上涨的计数，比如 `Thinking · tool calls: 2…` ；结束后输入 `/tally` ，会打印出总次数。

会话别关，直接改代码保存， **Claude Code 会热重载这个模块** ，下一个 spinner 就用上了新文字。官方说，这个快速反馈的循环，正是写 Mod 好玩的大部分原因。

只是热重载会重新跑 `register` ，模块里的变量会清零，想跨重载保存数据，要放进 `$.state` 。

写完之后，有两个命令可以检查：

```
●●●claude plugin validate ./first-mod
claude plugin test
└
```

`validate` 会用和 Claude Code 加载时相同的静态分析，列出这个 Mod 挂了哪些事件、调用了哪些 API，事件名拼错它会直接报出来，比如 `"tool.calls" is not an event` 。

`test` 则跑 `tests/` 下的测试，不需要会话、登录和网络。

静态分析也带来了几条写法上的规矩： `$` 的调用要写全（ `$.store.get(...)` ，不能把 `$.ui` 赋给变量或解构）， `on` 的事件名必须是字符串字面量，只能用 ES module 的 import，也只能引用插件目录里的文件……

每次加载 Mod 时，Claude Code 还会把当前版本的类型声明写进 `.claude-plugin/types/` ，编辑器能直接补全和类型检查。

官方特别说明，事件和方法在版本之间可能会变， **两者冲突时以这些类型文件为准，文档也不例外** 。

完整的 API，可以看 GitHub 设计帖里 9 月 9 日放出的这张官方速查表，只是它对应的还是上线前的版本：

![Claude Mods 速查表](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkJtLTkict0QC0xnjTaqfM3apkQkOWmFYTgxpuEqiauriam3iaqoVjG7cXzlQoZ7wlp38RnknlV5GaC52LAs3UwFRja7xaBQ1uP6ic4/640?from=appmsg)

Claude Mods 速查表

## 安装与分享

05

**Mod 就是插件** ，所以分享方式跟插件完全一样：把它放进一个带 `.claude-plugin/marketplace.json` 的 GitHub 仓库，这个仓库便成了你的 marketplace。

```
●●●{
  "name": "my-mods",
  "owner": { "name": "You" },
  "plugins": [{ "name": "token-weather", "source": "./token-weather" }]
}
└
```

别人安装只需三条命令：

```
●●●/plugin marketplace add your-org/my-mods
/plugin install token-weather@my-mods
/reload-plugins
└
```

也可以在 shell 里用 `claude plugin install <名字>@<marketplace>` 。想让更多人找到，可以提交到 Claude 目录 claude.ai/directory/manage。

发布前还要注意，插件名不能像 Anthropic 官方的（比如以 `claude-` 开头）， `validate` 会直接拦下；而事件和方法又会随版本变化，最好在 README 里写明你测试时用的 Claude Code 版本。

官方还会在 Claude Code Playground 仓库里陆续放入预置的示例 Mod，可以直接拿来改。

Anthropic 的 Thariq 推荐了一个他自己用得很多的 Mod，叫 next-steps，每轮结束后会给出下一步建议，包括该用哪个 skill 或命令：

![next-steps](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFnjziacMJ69j3THnEqficcsLamyXfnvJ6hDfChibpnDxwY5jLRDTTYicPV82L6VKQq8JcJrNSUo1DqTRSJKwLtrGVibyqSzgID1FNV0/640?from=appmsg)

next-steps

安装方式：

```
●●●claude plugin marketplace add anthropics/claude-plugins-community
claude plugin install next-steps@claude-community
└
```

## 内置 Mods

06

**Claude Code 已经把自己的一部分功能改成了 Mod。**

比如 `/diff` 现在就是一个 Mod，你可以在 `/plugin` 里关掉它，或者换成自己写的版本，AGENTS.md 支持也是。

而官方的计划是把更多内置功能陆续迁成 Mod，最后让你可以 **把 Claude Code 削减到一个很小的核心，只把自己想要的加回来** 。

目前内置的 Mods 有这些：

| `/plugin`  中的名字 | 作用 |
| --- | --- |
| cc-plugin-agents-md | 把 AGENTS.md 作为项目指令加载 |
| cc-plugin-diff | 接管 `/diff` 并画出它的面板 |
| cc-plugin-plugin-authoring | 给 Claude 提供写 Mod 用的 skill |
| cc-plugin-sec-default | 企业安全兜底，用户关不掉 |
| cc-plugin-telemetry | 发送 Claude Code 及内置 Mod 的分析数据 |
| cc-plugin-you-should-know | 一个旁路 Agent 盯着长任务，发现你和 Claude 可能漏掉的问题时在输入框上方提醒 |

其中 You should know 默认关闭，用 `/plugin enable cc-plugin-you-should-know@builtin` 开启（限直连 Anthropic 的会话，且要开着遥测）。

这些内置 Mod 的源码和测试都公开在 anthropics/claude-code 仓库的 `mods/` 目录下，官方团队怎么写的，可以直接翻。

同一个 2.1.287 版本里，追踪账号 ClaudeCodeLog 统计到提示词文件少了 13 个， **提示词 token 少了 8328 个（-26.6%）** 。我大胆猜测一下……这或许跟一部分功能被挪进了 Mod 有关？

## 能在哪跑

07

| 运行方式 | hooks 是否运行 | Mod 画的界面是否显示 |
| --- | --- | --- |
| 终端里的 `claude` （含编辑器内置终端、JetBrains 插件） | 是 | 是 |
| 桌面端 Code 标签页（WSL 会话除外） | 是 | 是，标为仅终端的元素除外 |
| 桌面端的 WSL 会话 | 否 | 否 |
| VS Code 扩展的聊天面板 | 是 | 否 |
| `claude -p`  和 Agent SDK | 是 | 否 |
| Remote Control（claude.ai 或手机端） | 是，在你本机的会话里 | 在你本机的终端里 |
| 云端会话 | 插件能到达云端会话时是 | 否 |

## 安全

08

Mod 的权限和 Claude Code 本身一样大， **没有沙箱** 。

按官方文档的说法，一个 Mod 可以以你的身份读写你账号能碰到的任何文件、启动程序、发网络请求；读到环境变量和配置文件里的 API key；看到你发的每条 prompt 和 Claude 的每次工具调用，并改写它们，甚至冒充你提交一条 prompt；不问你就批准一次工具调用；还能用你的套餐或 API key 调模型花钱。

所以官方反复强调， **只装你信得过的来源** ，就像在电脑上装任何代码一样，装之前先看看仓库。

安装前，可以先用 `claude plugin validate ./some-mod` 列出这个 Mod 会做什么。

想关掉 Mod，有三种粒度：

• 关掉单个 Mod：在 `/plugin` 的 Installed 标签页禁用或卸载

• 本次会话关掉所有已安装的 Mod：用 `--safe-mode` 启动（其他自定义也会一起关掉）

• 所有会话都关掉自己装的 Mod：在 `~/.claude/settings.json` 里设置 `"disableAllHooks": true` （settings hooks 和自定义状态栏也会停，组织管理的照常运行）

## 企业管控

09

对于团队和企业，Mod 沿用插件的那一套管控，管理员可以允许或屏蔽 plugin marketplace。

Team 和 Enterprise 套餐由 owner 在管理后台设置，Claude API 和第三方 API 套餐则由管理员把 managed settings 推到用户机器上。

在 Team / Enterprise 套餐，以及任何有 managed settings 的机器上，会有一个叫 **sec-default** （security default）的内置 Mod 最先加载，用户关不掉。

它保护的是组织管理的那部分，用户装的 Mod 不能改托管 hooks 的输入和决定、系统提示词、托管的 CLAUDE.md 和指令、托管 MCP server 的工具，也不能批准被 deny 规则拒绝的调用。

除此之外它不加其他限制，用户的 Mod 依然能以用户权限读写文件、跑进程、联网、改写 prompt 和工具调用。管理员想更严，可以开 `allowManagedModsOnly` ， **只让组织自己的 Mod 加载** ：

```
●●●{
  "pluginConfigs": {
    "cc-plugin-sec-default@builtin": {
      "options": {
        "allowManagedModsOnly": true
      }
    }
  }
}
└
```

团队也可以用 Mod 做自己的管控和功能，官方举了三个例子：在对话旁边放一个面板显示 CI/CD 流水线状态；任何命令碰到生产配置前都要求确认；写一个最先加载的 Mod，记录其他所有 Mod 的每一次调用，当作审计日志。

## 和 hooks、skills、MCP 怎么选

10

|  | Mod | Settings hook | Skill | MCP server |
| --- | --- | --- | --- | --- |
| 是什么 | 插件里的函数，在 Claude Code 进程内被调用 | 生命周期事件上跑的 shell 命令、HTTP 请求或 prompt | 一个 Claude 会读的 SKILL.md 指令文件 | 给 Claude 提供工具的外部进程或服务 |
| 能改什么 | 工具调用、prompt、命令、轮次、界面 | 是否放行、工具参数和结果、给 Claude 补充上下文 | Claude 知道什么、做什么 | Claude 有哪些工具 |
| 能画界面吗 | 能 | 不能 | 不能 | 不能 |
| 用什么写 | JavaScript 或 TypeScript | 脚本 + settings.json | Markdown | 任意语言 |
| 什么时候选 | 想要面板、输入框上方的栏、自定义命令，或改写事件 | 用现成脚本拦截、放行或记录事件 | 老是在对话里粘同一段指令 | Claude 需要连外部系统 |

**原来的 hooks 也没有被废弃** ，settings 里和插件 `hooks/hooks.json` 里的 hooks 都照常运行，和 Mod 并存。

## 从一个 issue 开始

11

Mods 的设计，最早是 **9 月 3 日在 GitHub 上公开征求意见** 的，issue 标题叫「Mods - make Claude 10x more extensible」。

提案作者把它描述成 Express / Koa 那样的函数式 hook，按注册顺序用 `next` 串起来，副作用都走一个参数化的 `$` 对象。他还专门留了一句：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> `$` 这个符号没得商量，我信奉的是一位更古老的神。

后面链接的，正是 jQuery 官网……

这个帖子下面有两百多条讨论。

9 月 9 日官方宣布几周内上线，正式改名叫 Claude Mods，function hook 则保留为底层的技术名词，想尝鲜的可以用 `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude` 提前开启（2.1.287 起这个变量已被忽略）。

到 **10 月 1 日** ，它就上线了。

Thariq 表示：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf="">“</tspan></text></svg>
> 
> 所有软件都在变得可塑，所以把它作为 Claude Code 的一等公民来支持很重要，我希望越来越多的软件能像这样可扩展！

他还提到，Mod 可以分叉出子 Agent 去做额外的活，比如自己做一套记忆系统：每轮跑一个自定义分类器，命中了就写入记忆。 **他自己正在把 plan mode 也改成一个 Mod。**

TestingCatalog 则认为，这其实意味着大部分客户端软件，只要花点功夫和 token 都能被「mod」，算是迈向个性化 UI 的第一步。

入门指南的结尾，官方也给了一些可以动手的点子：用 `$.session.usage()` 做一个花费或限额的状态栏，用 `prompt.submit` 给每条 prompt 自动加上团队规范，做一个面板列出这次会话 Claude 读过的所有文件，长任务结束时用 `$.ui.toast` 弹个提醒，或者针对自己的技术栈加一道 `tool.call` 守卫，比如生产环境的 kubectl 和 terraform apply。

建议先从 Token Weather 那段 prompt 开始，改改「一行里要显示」下面那几条，就是你自己的 Mod 了。

◇ ◆ ◇

官方博客：https://claude.com/blog/claude-code-mods

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过