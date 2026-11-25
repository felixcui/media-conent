# Claude Ship 发布：自己审 PR、改 PR、批 PR

**作者**: 尹John

**来源**: https://mp.weixin.qq.com/s/Lxue2bDm0-eHj4Tb0kw8NA

---

## 摘要

Anthropic 推出 Claude Ship beta，面向 Team 和 Enterprise：PR 提出来之后，审查、修复、批准三段都由 Claude 接手，人只需要处理规则没覆盖的部分。三个 Agent 分工清楚：Code Review 并行检查 diff 和周边代码，疑似问题先过一道验证去误报，再去重、按严重程度排序，以行内评论发到 PR；PR Steward 按评审意见改代码；Claude Approvals 按团队事先写好的规则判断能不能批准。边界划得很硬：Code Review 只读代码，不构建不运行，也不批准或拦 PR；PR Steward 不批准、不合并，在 Anthropic 托管环境里直接请求批准会被服务拒绝。三个可分开启用，也能只限某几个仓库。时间线上 Code Review 今年 3 月推出、10 月转正式可用，后两个是这次的新 beta。文章用一个实例说明流程：某 PR 先查出两个问题，改完再审还剩一个，又改一轮才过，之后按规则批准、等待合并。

---

## 正文

尹John 尹John

在小说阅读器读本章

去阅读

刚刚，Anthropic 推出了 Claude Ship（beta）。 **Claude 现在可以审查 PR、修复 PR，并在团队规则允许的范围内，直接批准 PR。**

![Claude Ship](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFkkTQzOia7xkbSLRib7UNmibk8QwHDeAh1zm4qjkiazsaibic3xsdrQ9oAV8wBibUoIoSicwAgicmb87fbzlT9ickBN8WJhib0gYZPaiaGCTGg/640?from=appmsg)

Claude Ship

Claude Code 之父 Boris Cherny 发帖表示：

> <svg height="24" viewBox="0 0 26 24" width="26" xmlns="http://www.w3.org/2000/svg"><text fill="#C4C7C4" font-family="Georgia,'Songti SC',serif" font-size="42" font-weight="700" x="0" y="34"><tspan leaf=""><tspan leaf="">“</tspan></tspan></text></svg>
> 
> 一年前我们发布了 Opus 4.5，它是第一个替我写了 100% 代码的模型。
> 
> 但 PR 的交付一直没有跟上，所以今天我们推出了 Claude Ship 的 beta 版，面向 Team 和 Enterprise。我每天从早用到晚，已经没法想象没有它要怎么发布代码了。

提过 PR 的人大概都熟悉这个过程。你提完 PR 便去做下一件事了，做到一半评审意见回来了，于是只好停下来，翻出刚才的代码改完推上去，再等评审重新跑一轮……最后还要去找个人来点批准。

在代码全靠人写的时候，这套流程并没有什么问题。

而现在 Claude Code 团队（我这里也是）的代码大部分都是 Claude 写的， **卡住的地方也就从写代码，变成了 PR 提交之后的这段路。**

Claude Ship 用了三个 Agent 来走完这段路。

![三个 Agent 的分工](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFlBH88junNnMZI14BibOX3CHPy0NPM7q7lTyP2H0nm8HVgK2yaqzJCeZ78ZL9sibAM15QjkR3r0uzibDQzMt87GvxJYqHoAkvUrVE/640?from=appmsg)

三个 Agent 的分工

Code Review 负责找问题，PR Steward 负责修改，Claude Approvals 则按团队写好的规则来判断能不能批准。

图里的这个 PR 先是被找出了两个问题，改完再审还剩一个，又改了一轮才通过，然后按规则批准，等待合并。

其中 Code Review 在今年 3 月就推出了，10 月转为正式可用，后两个是这次新推出的 beta。三个 Agent 可以分开启用，也可以只在某几个仓库里启用。

## Code Review

01

演示视频里是一家卖辣酱的店，Dan 写了个新功能，辣度 8 及以上的订单会免费送一杯牛奶。

![Code Review 找出 bug](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFm6hejJcLPpvmg52kkEPG0XPiagBFy4nrQ7yxYsEnSFjY5w0jV1peV1aT66ZZfelFqj44hIQbT6OgIXrI2eicTialyxGqdc35JBAc/640?from=appmsg)

Code Review 找出 bug

结果他把大于等于写成了小于（这个例子有点儿低估模型的智商），微辣的顾客都有牛奶，最辣的那批反而没有……

Code Review 把这一行标了出来，定为 Important。

它会让多个 Agent 并行检查 diff 和周边的代码，找到的疑似问题再经过一个验证步骤去掉误报，最后去重、按严重程度排序，以行内评论的形式发布到 PR 上。

![评审流程](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFk0vELP4f5Y4Sp9yEBB9CqmpapP6n9e09xjP3fcyibWY4icA20OKbQOCuicLO8iahicwJnv1wYcCLawfgSKhQcTDel1Ocib1c8xSicSpU/640?from=appmsg)

评审流程

严重程度分为三级，Important 是合并前应该修掉的 bug，Nit 是小问题，Pre-existing 则是代码库里本来就有、并非这个 PR 引入的 bug。

评审深度也有 Quick、Standard、Deep 三档，可以按仓库分别设置。它默认主要关注会影响生产环境的 bug，不管格式偏好和测试覆盖率，想调整可以在仓库里放一份 `REVIEW.md` 。

每条评论会写清楚问题、触发条件和修复建议，通常还能展开看它为什么这么判断、又是怎么验证的。

![一条评审评论](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFkToggPb5iah2OJOEfnvZ4THvlplO4p4OtKjGY8IvB4w5bGicLh1T8kPlicDSEwat3JEHmMP0A4aiaNQa1xStuZUGcSXPp1pprBicfw/640?from=appmsg)

一条评审评论

图中的评论指出， `Retry-After` 可能是个日期，也可能根本没有，两种情况都会让等待时间失效，等于对着一台已经在限流的服务器连续重试。

不过要注意的是， **Code Review 只读代码，并不会构建或运行你的代码，它自己也不会批准或拦下一个 PR。**

从 6 月到 9 月， **Claude Code 团队合并的 PR 翻了一倍多，被回滚的比例则下降了 40% 以上** 。

当然，Claude 的评审只是他们整个流程里的一层。

## PR Steward

02

找到问题之后，接手的是 PR Steward。

![PR Steward 修复](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmmO4hSXfrOvzPFESlYALPRlN666msPtamoFXdL51vLpHFBkfQfJpfuacqE8EEtRf47COI3j1Va5pG0S1KTZMNUBWGfbfnVG3o/640?from=appmsg)

PR Steward 修复

它把小于号改回了大于等于，推了一个 commit，失败的测试也随之变绿。同事 Mila 又来留言，问能不能改叫「救命牛奶」（rescue milk），它便也跟着改好了。

PR Steward 运行在云端会话里，会处理失败的 CI、合并冲突，以及来自 Code Review、其他评审工具和同事的意见。

**每次推送之后，它都会留一条评论，写明改了什么、要怎么撤销。**

![PR Steward 留下的评论](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFlL93z1bhRC722l4aDGibcWZCKrswKGtJeFutDUhSiaESgibDhc3HK9wsibLV7QnEHJHPg826ZHyGBstOibpY1yZPHy77s3JHzgN1Tw/640?from=appmsg)

PR Steward 留下的评论

哪些该改、哪些不该改，它也有一套默认的规则。

| 情况 | 默认做法 |
| --- | --- |
| 检查失败 | 原因出在这个 PR 涉及的代码里才修 |
| 不稳定的检查 | 测试还没开始就失败，或同一个 commit 之前通过过，则重跑一次 |
| 改名、补测试这类小意见 | 直接改完，关掉讨论 |
| 大改动或设计层面的意见 | 只回复，不改代码，除非评审者说明了要怎么改 |
| 合并冲突 | 把目标分支合并进来解决 |

草稿、来自 fork 的 PR、机器人提的 PR，以及没有写权限的作者提的 PR，它默认都会跳过。

在自己的 PR 里发一条以 `@claude` 开头的评论，就可以给它下指令，比如让它只修 lint。想让它停下来，则评论 `@claude stop` ，或者摘掉 PR 上的 `claude-pr-steward-watching` 标签。

每个人还可以在设置里逐项关掉不想让它处理的事情。

![个人设置](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFlrG0FwbCzhiaicbW1ianuoKPhXxAEPJWiaa2zD0eudjKCXdw5KMQXdeEbgMPpvVUpmySrnrmEgFPBJLhgCy6pm91SoTCT4gMD7qzM/640?from=appmsg)

个人设置

**PR Steward 在设计上不会批准，也不会合并 PR。** 其中批准请求，在 Anthropic 托管的环境里会被服务直接拒绝。

但合并就不一样了，先拦它的是一套匹配命令文本的规则，再加上模型的判断，文档里也承认，换一种写法的命令有可能两道都能通过……

所以在启用之前，还是要先把 GitHub 的分支保护设好。

## Claude Approvals

03

到了批准这一步，就要看团队自己写的规则了。

![Claude 批准常规改动](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFmJ3JQbO0Edm9w3Via9CGzz0S9sKP4D5PVfIFFBD16x84F0YAe6YFY2gAGWFpveDYTt6L8MWA1OKMgxMjFCnFHUljd9FwAsjGsU/640?from=appmsg)

Claude 批准常规改动

Dan 改的是 `shop` 目录，规则允许 Claude 批准，于是他只需要回来点一下合并。辣度 10 的顾客，终于喝上了免费的救命牛奶。

而另一个同事 Theo 改的是 `billing` 目录里的税费计算，测试同样全部通过，但规则要求必须有人来看，Claude 便停在那里等着，直到 Mila 点了批准。

![高风险改动交给人](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFlnupAugk1f1f40rtWVmkvwEibjNQKRUtsqURibrcvvWzrNibXlQq7FIZZtJJ0Pyk7Egiaia3BXV5VZ8MVA7e94ytIibtSLLJZQAKCTc/640?from=appmsg)

高风险改动交给人

规则写在仓库的 `.claude/approvals.yml` 里，官方把它比作更聪明的 CODEOWNERS。

![规则文件示例](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFm1G6EQNXzzSBsw7Hlv0ZqibLSaulTZkz04OYsjokNSDeehNZhRjh71YB45iaKPx8PTCx6FCnDB0l4yKNeSV7ET5nnwQICmXsAD0/640?from=appmsg)

规则文件示例

这份示例对应的审批要求如下：

| 路径 | 默认 | Claude 评审通过后 |
| --- | --- | --- |
| 大部分代码 | 2 个人 | 1 个人，Claude 批准 |
| `docs` | 2 个人 | 0 个人，Claude 批准 |
| `services/billing` | 2 个非作者的人，其中至少 1 个来自支付团队 | 不变，Claude 只评论 |

如果一个 PR 同时命中了多条规则，则按最严的来，每条规则要求的人数也都得满足。

除了路径，规则还可以看改了多少行、谁提的、要合到哪个分支。

**更灵活的是自定义分类器，你可以用一段自然语言来提问** ，比如「这个改动上线的风险有多大」，让模型从低、中、高里选一个，再按答案决定要几个人来批。

判断的结果，会以一条评论和一个检查项的形式出现在 PR 上，可以展开看规则是怎么得出这个结论的。

![Claude 批准的 PR](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFn2CJSiaMqYLAwLnIIXC5GgfibNJtNXM0ic1E9UW6qP4PPTBgsVoQzJP0PWiafKKIpsDR4Y8ezmVVGPLOyJuicQibFcvOU62q9h9sK30/640?from=appmsg)

Claude 批准的 PR

## 作者默认占一个名额

04

规则里的 `seats` ，意思是需要几个人批准。而文档里有个很容易忽略的设定， **只要对仓库有写权限，PR 的作者自己默认就能占一个名额，而且不用点批准。**

![作者先占了一个座位](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKqVLiaIpzFmIm51Ro1B31OBjhjSX4adlnDUa15fqnH48dQ27VQ7Hc19U8R3dxYicRC5Nb2jCjk8RwqTssia46chXmWX1fmnTx5HJelk8Oj9uw/640?from=appmsg)

作者先占了一个座位

也就是说， `seats: 2` 可以是作者再加一个人， `seats: 1` 则只要作者自己就够了（来自 fork 的 PR 除外）。

回头看上面那份示例，大部分代码在 Claude 评审通过之后「一个人」就行，这个人可以是作者。那除了作者和 Claude，可能就没有第二个人看过这段代码了。

不过这个名额会随着推送变化，通常要由同一个人写出并推送最新的 commit 才能占住。比如 PR Steward 推送了修改，检查就可能会重新要求批准。

想要作者以外的人来看，得像 `billing` 那条规则一样，写上 `"!pr/authors"` 把作者排除掉。

另外，如果仓库在 GitHub 上的分支规则要求 1 个 approval， **Claude 的批准就可以算作那一个。**

10 月 Anthropic 公开自己的内部评审流程时，有一条规定是 Agent 的批准永远不能顶替人的名额。

Claude Approvals 的 `seats` 默认也只数人，但 GitHub 那一层可不管这个……

如果规则没有要求任何人批准，又开了自动合并，一个 PR 就真的可以从头到尾没有人看过：Claude 写，Claude 审，Claude 改，Claude 批。

官方文档专门为此写了「无人评审的合并」一节，里面还列出了几种情况：

• `seats: 0` 时，机器人提的 PR 可以在没有任何人看过的情况下合并

• 只写 `claude: approves` 而不带评审条件，并不会触发 Code Review，Claude 可能会批准一个谁都没审过的改动

• 由脚本或 Agent 操作的普通 GitHub 账号，也会被当作「人」来计数

• 分类器的答案会受 PR 里的文字影响，作者写的话有可能把风险等级带偏

**想要稳妥，可以加一条排除作者的规则并让它正式生效，再把 Claude Approvals 设为 GitHub 的必过检查。**

## /ship

05

上面这些只面向 Team 和 Enterprise 的组织。如果你是个人用户，可以用 Claude Code 里的 `/ship` ，Boris 表示任何人都能用。

![输入 /ship](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFm8aiam5RL3q4O9wmTP1j55B3TH4MVECxVWgeSt9AS1sswBCIHEZyhmTSD31pyMrVW5U1OZzxI7vIficB7feiaUJOJRX0CGJfian2g/640?from=appmsg)

输入 /ship

改完代码后输入 `/ship` ，Claude 会帮你提交、推送、开 PR，然后用 `/code-review` 审一遍，再进入一个叫 watch 的状态，持续跟进这个 PR，处理失败的检查、冲突和评论。

![/ship 的流程](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFnBpGSoOyL583ccxf6siaOr9kVHqh0iaSg9aFx8U0jKwMsLpiczPW1yh1URibC0hm8mdiarH0wxpj598oeWAKLQTWT3JsTUbaCZmA90/640?from=appmsg)

/ship 的流程

等检查都通过、评论都回完了，它会告诉你一声， **最后的合并还是由你自己来点** （除非你提前开了自动合并）。

![watch 期间可以去做别的](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZKqVLiaIpzFm2hZJqwlLqHlSHRibF6XkaAcFZpAbV6mpLXLvVric4kWWDHeSTwqd60Tr762HgJ70TddhBku3FWEibulduHojHnBwCiakWBHHKuo0/640?from=appmsg)

watch 期间可以去做别的

想让它无人值守，需要先切到 auto mode，在其他大多数权限模式下，它会停下来等你逐个确认。

PR 已经开好、不需要评审的，可以用 `/steward` 直接进入 watch。

它和云端的 PR Steward 不是一回事， `/ship` 和 `/steward` 都运行在你自己的会话里，用你的 GitHub 和 git 登录身份，也算你的用量。

**所以会话要一直开着并留在前台，电脑不能休眠，分支也不能切走** ，最长 7 天，期间按一下 `Esc` 就可能结束。

![/ship 启动后的提示](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFkIgubVAoubo91MLgDtvpibGCbGWJzq85iaQPNdAUn6eUzkNBYGqtOI9sZoMaPdlLAkKclITt3ib8ZxMfuaypzdm8ibPPC6VzbWje0/640?from=appmsg)

/ship 启动后的提示

想继续做下一个改动，可以另外 clone 一份仓库，再开一个会话。

用之前有几件事要留意：

• `/ship` 没有确认弹窗， **回车之后不管它，它就会继续往下执行** ，只在提交前和推送前各显示一行以 `Esc to cancel` 结尾的提示，留给你几秒钟

• 在非公开仓库里，还没开 PR 的话，它可能会把所有未提交的改动一起提交，包括新文件，运行之前先 `git status` 看一眼

• 它只按文件名来识别密钥，比如 `.env` ，写在文件内容里的得自己检查

• commit message 是根据会话内容写的，能看到 PR 的人都能看到（所以别在会话里骂同事……）

• watch 期间，能往目标分支合并、或能往你分支推送的人，他们的代码都可能在你的电脑上运行，用的还是你的凭证

`/ship` 需要 Claude Code 2.1.330 及以上版本、GitHub CLI 2.63 及以上版本，目前正在 CLI 和桌面端逐步推送。

云端会话里没有 Claude Ship，设置了 `DISABLE_TELEMETRY` 或接了第三方模型服务的会话里也没有。而在 Windows 原生环境和 `bypassPermissions` 模式下，则不会启动 watch。

## 怎么启用

06

团队的设置入口在 Organization settings 的 Claude Ship 页面，需要 Owner 权限。

Code Review 和 PR Steward 由 Owner 逐个仓库开启， **Claude Approvals 则只要有人把规则文件合并进已接入仓库的默认分支，就会启动** ，Owner 可以为整个组织关掉它。

![仓库列表](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFnBIOmjzZ2N6icEmUNXdVs9lG1deRMTnhSTsjdCaUeUYWp8rLXiavpFlWbhCZicr0CACnkmS1tGJAibzk7UMU4JOoZYczcz9bNnRrk/640?from=appmsg)

仓库列表

官方建议是 **从一个仓库开始，一次只开一个 Agent** ：

1\. 先开 Code Review，设好每月的花费上限，跑几轮看看平均一次要花多少钱

2\. 再开 PR Steward，先用手动模式，有人评论 `@claude steward` 时才启动

3\. 最后加规则文件，用 observe 模式跑一段时间

![PR Steward 启动方式](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZKqVLiaIpzFmLMFOUic8FnTzNZe1HaOSWIu9D1WJwYfk2a9PvB6drh9nbzPQ33RMcvicJRdeWgvMNbowY2ict4WvvVOicdnFOR1GtHsPgWEDlcCI/640?from=appmsg)

PR Steward 启动方式

在 observe 模式下，Claude Approvals 只会写出它会怎么判断，并不会真的批准。

等它的判断和团队里的评审基本一致了，再删掉 `mode: observe` 这一行。 **注意规则文件里要是没写 mode，默认会直接生效。**

如果你的团队已经在用 Code Review，规则文件合并之后（observe 模式也算），没有规则提到 `claude/code_review` 的话，自动评审一般就会停掉。

Claude Ship 并不要求你用 Claude Code，代码是人写的还是别的编程 Agent 写的都可以。

## 费用

07

Claude Ship 按 token 计费，从组织的 usage credits 里扣除，不含在套餐的用量里。

PR Steward 在你设置之前，是没有单独的花费上限的。Claude Approvals 的分类器默认也没有总额上限，其中自定义分类器只有单次运行 10 美元的默认上限。

Claude Approvals 没有基础费用，但规则触发的评审和分类器都要收费， **observe 模式也照样收费** 。

新加的仓库默认是每次 push 都审一遍，push 得勤的话花费也就成倍地涨。

而且， **在后台关掉 usage credits，并不会让已经开着的 Agent 停下来，它们会继续运行、继续计费。**

![开关关了，计费还在走](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFngZiaiaELe3bynybepMsRE3LcYbfdO5g38Y24icVXWAnueXAhYUlbycMQWOjR0BNYEXSLvgAH7dPp0x5UWmF6nYmgUazy5XUooJY/640?from=appmsg)

开关关了，计费还在走

想让它们停下来，需要到 Claude Ship 的设置里逐个关掉，顺序也有讲究，要先关 Claude Approvals 再关 Code Review，因为规则文件可以在 Code Review 已经关掉的情况下触发收费的评审……

而 PR Steward 关掉之后，已经打上标签的 PR 它还会继续处理一段时间，要先把标签摘掉。

符合条件的 Enterprise 组织可以领一笔 1 万到 5 万美元的抵用额度，按 Claude Code 的活跃席位数来定，2027 年 1 月 15 日前领取，领取后 30 天内用完。

这笔额度不能用在 `/ship` 上，它的用量算在你自己的 Claude Code 里。

目前 Claude Ship 只支持 GitHub，启用了零数据留存（ZDR）、HIPAA 配置，或客户自管加密密钥的组织都用不了。

## 在用团队

08

Claude Code 团队自己的很多 PR 已经在用 Claude Ship 了， **最大的变化之一，是能动手处理用户反馈的人变多了。**

前阵子有位客户被 Analytics API 的文档弄糊涂了，以为 Admin key 可以拉取 Pro 和 Team 的用量。团队里的产品经理便去问 Claude Tag 有没有人在修，Claude Tag 直接开了个 PR。

Code Review 没发现阻塞问题，一位文档评审看过，Claude Approvals 通过，当天晚上就合并了。

外部用户里，加拿大电信公司 TELUS 在用，美国二手车平台 Carvana 也有团队在试点 PR Steward。

TELUS 的工程总监 Vatsal Bhatt 表示，Code Review 已经多次赶在人工评审之前发现了真正的问题，他们仍然保留了人工环节，只是人的时间会花在更需要的改动上。

![Claude 开船了](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFmJg1KHBCFT4t99AIQwwdsBCNXtMP0Lh9JzlwufdricnticO0ZbMc8d4BoceWSPfw2ibKWiaDD7QbvwUXJ7bmlicpXDkkTxlNoQDAZE/640?from=appmsg)

Claude 开船了

想试试的话，可以先更新 Claude Code，在下一个改动收尾时输入 `/ship` （记得先 `git status` ）。

◇ ◆ ◇

![](https://mmbiz.qpic.cn/mmbiz_gif/ZKqVLiaIpzFnkQCQpCXbuO62OrjoP7a52Ayoyr1yKW4Z5AN7l0ibUEoh0YXSDkQMpR2tfwyiboumyAGaaA5M9mQ0uic0RxsuznnW9YXjUQy1LUE/640?from=appmsg)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 推荐 ，轻点两下取消推荐 分享 留言 收藏 听过