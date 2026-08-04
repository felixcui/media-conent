# 给 Codex 和 Claude Code 接入 DeepSeek-V4-Flash，夯爆了！

**作者**: 程序员鱼皮

**来源**: https://mp.weixin.qq.com/s/Nnuwq9giw-jj3fH9WswMrg

---

## 摘要

DeepSeek-V4-Flash正式发布公测，该模型以极低价格和大幅强化的Agent能力著称，在Terminal-Bench测试中反超自家V4-Pro。因其原生支持Responses API，可无需协议转换直接接入Codex和Claude Code，有效解决了国内用户使用这些AI编程工具时面临的账号受限、费用高昂及封号风险等痛点，让开发者能以极低成本、安全便捷地体验主流AI编程工具。

---

## 正文

程序员鱼皮 程序员鱼皮

在小说阅读器读本章

去阅读

大家好，我是程序员鱼皮。

这几天 DeepSeek-V4-Flash 正式发布 API 公测了，这个模型主打一个性价比高，输入 1 元 / 百万 token、输出 2 元 / 百万 token，大概只有 V4-Pro 十分之一的价格。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1E5kgWXS92JZvKAU6dndRWyAQgBRlbdStJFeveicVqFt2IpsZuxibIqseU9iaUeMqBmpq1hTgVXxBCZAcT4OJksMicaibLKP90lBybg/640?wx_fmt=png&from=appmsg)

重点是它这次在 Agent 能力上做了大幅强化，在专门测试 AI 自主执行终端任务的 Terminal-Bench 上拿到了 82.7 分，竟然反超了自家的 V4-Pro 预览版（72.1 分），写代码、调工具、自主执行任务都很能打。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1E3bg41MaugqrtFvf3W6UhInWnCI5TojGibyHpOkbTDaEv7C7cpkpMC5XsDqGtwsTQooerDrmLRAW1oUv2qNmCTia6c2qKneGUug/640?wx_fmt=jpeg&from=appmsg)

再看看这张网传的 DeepSeek V4 斩杀线， **最新版的 DeepSeek-V4-Flash 秒了一大半模型！**

Agent 能力强 + 性价比极高，比它聪明的模型都贵很多倍。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1GhcVTYdXFQeoDKmmaoBuNxOLibkdZIt2tFEw7SP6N0ubzwnElyhmFhricqX2OTfnexC9qpQJI84k1BOaibAgfTkzzflJicSBU4QuY/640?wx_fmt=jpeg&from=appmsg)

**更香的是，它原生支持了 Responses API，可以直接接入 Codex，不需要任何协议转换。**

这下解决了一个让很多人头疼的问题。之前很多人想学 AI 编程，想耍一耍目前最流行的 Codex 和 Claude Code 编程工具，结果一上手就卡在了第一步。

要么没有国外的订阅账号，登录都登录不上；要么好不容易开通了，发现官方额度死贵，对话一会儿额度就耗光了；再加上时不时还有封号的风险，整的提心吊胆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EyNGvgtFbPGaXwmuxrrsM7Pen2oINK4pibe4TMGu22WJK7ZLx1YrrDp38VXmDOZg2mbFl6iaBnGoPR0SAOjkFU3psiaP88icPu3Wk/640?wx_fmt=png&from=appmsg)

**咱们怎么能因为「用不了工具」这种事，就把学 AI 编程的劲头给浇灭了呢！**

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1G4QkRt2AR0uXb8bypwQFfiafGicBkG6lI5vRichuib0Yfypice77pfDYpbPNFqeoXUDRxrXCK4z6uTUm01ZqhODG2ibuTNG0YqcdNMo/640?wx_fmt=png&from=appmsg)

其实 Codex 和 Claude Code 都支持切换模型，咱们直接用 DeepSeek-V4-Flash 来驱动它们就行，量大管饱、不用魔法、也不怕封号。而且现在 DeepSeek 官方已经做了原生适配，接入流程比以前简单多了。

接下来，只要几分钟，我会手把手带你把 DeepSeek-V4-Flash 接到 Codex 和 Claude Code 里，看完你就能跑通整套流程，想换哪家模型都是一样的操作。

点个收藏，咱们开始~

## 准备 DeepSeek 的 API key

不管接哪个 AI 编程工具，都得先有一个 DeepSeek 的 API key。

到 DeepSeek 开放平台 注册登录，进入 API keys 页面，点击创建一个新的 key。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GMdIDicbgcmx7QziaiaKVr7aOqUBSuibBMHOoOhEpzumCficIGIoowOfGfgZBqanWXhntMgS3m0alx3Td6tW5zic99Spg1ubODrXGx8/640?wx_fmt=png&from=appmsg)

注意，API key 只会在创建时完整显示这一次，记得当场复制保存好，后面配置的时候要用到它。

## DeepSeek 接入 Codex

Codex 是 OpenAI 推出的 AI 编程工具，最近的热度堪称炸裂，经常赠送重置额度，使劲蹬都蹬不完。

它有 2 种形态，一种是在终端里跑的命令行版 Codex CLI，一种是带图形界面的桌面 APP。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Hiar3rfDwtzU8OHLODRkoPygMCsc6FgmWkNADSvwebsSRYkQs5rPspDQ6AgRJiahqrJhmlSWt87FFfvic1rUuZT2gLExNqx6WV1o/640?wx_fmt=png&from=appmsg)

命令行版的安装方式很简单，先确保电脑里有 Node.js 环境，没有的话去 Node 官网 下个傻瓜式安装包。

打开终端，输入一行命令就能搞定：

```
npm install -g @openai/codex
```

装好后在终端输入 `codex` 就能进入对话界面，首次使用需要登录 OpenAI 账号。没有账号的话，就要自己折腾一下切换个模型。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GmyTLZDUKrqQEx6H41SwU9m2PD8hIEmRlEHwKue9dbaYOTGrm2n7MciatIWiagwSl7fCv7YePJ7B9fZ8s44eIvokUzUE5HC4e24/640?wx_fmt=png&from=appmsg)

至于 Codex 桌面 APP 的安装和基础玩法，前段时间我出过一套《保姆级 Codex 视频 + 图文教程》，需要的同学直接到我的 鱼皮 AI 导航 自取：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GhWcJrUCQBvRjBRY3nJx4ic9hKeqfKAzuTc7tfQWgX2eqofLqtExgu5RkiasoSD9HiaxziczsF5dp4sQyxL6NsLPDibcmiaxyBQjtIw/640?wx_fmt=png&from=appmsg)

### 方法 1、一键脚本配置（推荐）

DeepSeek 官方提供了一个配置脚本，跑一下就能全部搞定。

在运行之前，确保你已经安装了 Codex CLI 或者 ChatGPT 桌面 APP，并且至少启动过一次。让它生成好 `~/.codex` 配置目录，脚本要往里面写东西。

> 官方文档参考：https://api-docs.deepseek.com/quick\_start/agent\_integrations/codex/

Windows 用户在 PowerShell 执行：

```
irm https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.ps1 | iex
```

Mac 或 Linux 用户在终端执行：

```
bash <(curl -fsSL https://cdn.deepseek.com/api-docs/codex-deepseek-setup.sh)
```

脚本启动后会让你选择要用的模型，目前 DeepSeek-V4-Flash 已经可以直接选了，输入「1」就好：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FNcibmnM8obos2f8dWd5muVOHmv0FAsk2WprcWdy2PsFnQJckneetX91Cskk18kUianPIRyBEhH654ic7YicZg5CWYpSNIQG9PU3M/640?wx_fmt=png&from=appmsg)

首次运行时，它还会让你输入 API Key：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FB7dWNLp8OdKia7XAPgAu4uZyV1tiaMdlOBzR2zW5hrMS8SPmQrpUrJHvODqcfAvt2ickPPGoXpTzKKNicA5OicwI5KDzxzj6adtdA/640?wx_fmt=png&from=appmsg)

然后按回车键执行，唰唰唰，脚本就帮我们把 DeepSeek 接入到 Codex 中了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FMjicX9sOjACiaR530ib2icjx68CTfoafiawd9lhHdeMRXtYC79NSP9wZfPVeSnxly4RrnA1yMQp0vSu1RYLftAsicGyicWFd5ibYhPoI/640?wx_fmt=png&from=appmsg)

为什么这次接入这么简单？

因为以前给 Codex 接国内模型，最大的麻烦是协议不兼容。Codex 用的是 OpenAI 的 Responses API，而国内模型走的是 Chat Completions API，这俩压根儿不是一套东西，你直接改个 Base URL 大概率会报 404 错误，得在本地起一个代理做协议转换才行。

但这次 DeepSeek-V4-Flash 官方原生支持了 Responses API 格式，不再需要任何中间层，配置完就能直接跑通。

多说几句，这个脚本会自动完成下面几件事：

1. 把你现有的 Codex 配置备份到 `~/.codex/backup-deepseek/` 目录，随时可以恢复
2. 生成一个 `~/.codex/models.json` 文件，告诉 Codex 关于 DeepSeek 模型的元数据（上下文窗口大小、支持的推理等级等等）
3. 修改 `~/.codex/config.toml` ，写入 DeepSeek 的接口配置，你之前设置的 MCP 服务器和项目配置都会保留
4. 自动校验配置语法，如果有错就中止，不会损坏你的文件
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1G2nnLAbibxzuibBVAibn1kNAFJs30EFj46ZMVwfQIMlIoOuicSyQoQbicicBaQLHZS1VcGKx0R4IKL9ueWU18yV5mDpnkKWJtDQIF6A/640?wx_fmt=png&from=appmsg)

配置完成后，重新打开 Codex，启动横幅如果显示 `deepseek-v4-flash` ，就说明配好了：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FrDhEGqoswDSia50xRVadiabTucJuZvTwWibaic7OXfAKRHCxWAll5FxK7LC1wLwkyE8A8VUH6KoibOlffHKq469qjeyzOQlibtvJdg/640?wx_fmt=png&from=appmsg)

如果你用的是 ChatGPT 桌面 APP 或者 Codex 的 VS Code 插件，不用单独配置，直接打开就能用 DeepSeek 模型了，因为它们和 CLI 版共用同一套配置文件。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Ft6jW61xcAjYdUjNTZpseZARvoMfpLZVvicpmDzL7NPK4arsensYQoqIl6K5h4VI9IruD7hmhP9QKy8VXCVbzn8RpjIZB8iarOQ/640?wx_fmt=png&from=appmsg)

想切换回官方模型的话，重新跑一遍脚本，在菜单里选恢复选项就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HM9B0JZib9U7O5yOX3pMatt64JxmphgTFWAXsZRJic51ZGPwf4BoJ1nexN6md8qSRYnuX9Djel4UEzqkcib1mI3yeiceleFJQrlco/640?wx_fmt=png&from=appmsg)

怎么样，是不是比想象中简单多了？

### 方法 2、手动编辑配置文件

如果你不想跑脚本，也可以自己手动修改配置文件，两步就能搞定。

第一步，在电脑的用户目录下找到 `.codex` 文件夹（Mac/Linux 路径是 `~/.codex/` ，Windows 是 `%USERPROFILE%\.codex\` ），创建一个 `models.json` 文件。

文件中的内容可以到 DeepSeek 官方文档 复制。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Egvwj7SPOdzDPaZpjiaXE0bBfe7haiaDnsqQZWxceH3wEJdacd7CA10W53UmeqiaZXt6w6vFib9NPhJhjAHUodL7ibicUYYwiauvH8as/640?wx_fmt=png&from=appmsg)

这个文件的作用是告诉 Codex 关于 DeepSeek 模型的各种参数信息，比如支持 100 万 token 的上下文窗口、支持 low / high / max 三档推理深度等。

第二步，在同一个目录下编辑 `config.toml` 文件，添加下面这段配置：

```
model = "deepseek-v4-flash"
model_provider = "deepseek"
preferred_auth_method = "apikey"
forced_login_method = "api"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/models.json"

[model_providers.deepseek]
name = "deepseek"
base_url = "https://api.deepseek.com/"
wire_api = "responses"
experimental_bearer_token = "<你的 DeepSeek API Key>"
```

把其中的 `experimental_bearer_token` 换成你自己的 API Key 就行。

这里的关键是 `wire_api = "responses"` ，它告诉 Codex 用 Responses API 协议跟 DeepSeek 通信，而 DeepSeek-V4-Flash 原生就支持这个协议，所以能直接跑通。

保存文件后重新打开 Codex，就能用 DeepSeek-V4-Flash 了。

## DeepSeek 接入 Claude Code

搞定了 Codex，再来看看 Claude Code。

虽然 Claude Code 之前因为封号问题闹得臭名昭著，我之前也写过 [相关文章](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588292&idx=1&sn=00a748cb79f2cb762927cb3597c32ce2&scene=21#wechat_redirect) 对其进行了一番《赞美》。但不得不承认，它在 AI 终端编程工具里的能力确实很强，如果改为对接国内的模型，就不用担心被封号了。

DeepSeek 官方目前只提供了 Codex 的原生集成方案，Claude Code 这边接第三方模型最省心的方式还是用 **CC Switch** 这个开源工具。

### CC Switch 是什么

像 Claude Code、Codex 这些 AI 命令行工具，每一个的配置格式都不一样。如果你想给它们换个模型供应商，得自己去翻文档，手动编辑 JSON、TOML 或者 `.env` 文件，填一堆 Base URL、API Key、模型名之类的参数。说不定改错一个字符就跑不起来，想在几个模型之间来回切换就更麻烦了。。。

CC Switch 就是来解决这个痛点的。它是一个免费开源的跨平台桌面工具，用一个可视化界面统一管理 Claude Code、Codex、Gemini CLI、OpenCode 等多个 AI 编程工具的配置。

> 开源指路：https://github.com/farion1231/cc-switch

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1F0xvxwicSrILKgnYgEVYIASXCn81fu9lg9TNHJYBOUfwle6Y0iczP2uz07ZHveew4c5a7ibkCtquHXD5aqP6944Cna1KIXpEeVpQ/640?wx_fmt=png&from=appmsg)

CC Switch 内置了 50 多个供应商预设，DeepSeek、Qwen、Kimi、智谱 GLM、MiniMax 这些都有，你不用自己手动改配置文件，点几下就能一键切换模型，还能从系统托盘里快速切换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HRjPKJpDOibichB4tTBibZVOjsYQj8hryRgksxqyw2JuHM1u8W6jvfjwRkm64zoaicJDyQZX1xPicCYLo8EXNumyEUX4QYt2yH68nY/640?wx_fmt=png&from=appmsg)

下面我就用它来带大家实操一遍。

### 安装 CC Switch

打开 CC Switch 官网，根据你的操作系统选择对应的安装方式。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HvzdPtApt3fph5kcn4tvjcPibsy63gZgv3F1TVJKL4kSsicsCRpl7ZEWvDMscKNe5mW0hs46HxAsIXYDdh96KEHaWpBDaicZVMws/640?wx_fmt=png&from=appmsg)

Mac 用户推荐直接用 Homebrew 这个软件包管理器，输入一行命令安装，直接就能用：

```
brew install --cask cc-switch
```
![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1G9ZXLlFZRgxpziaZgWrMso0fjyyUgTe5lh4VR15eybT1agr6v4icf626wOFbfxTxWYf4V4NPcEiaw6gs8wDtXHXkicmVC3zn1L73A/640?wx_fmt=png&from=appmsg)

Windows 用户下载 `.msi` 安装包，双击运行即可；Linux 用户根据发行版选择 AppImage，或者 deb / rpm 软件包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GFWfCPNgxNicutWtAGTU81HAUxKtQSicQ52AcsMIzve7gVZ84AU6nq0RjgG7Jf3aE2pNVPa69Oz7of0ml3xrBSkrSsWIzRVtHhI/640?wx_fmt=png&from=appmsg)

安装完成后启动 CC Switch，主界面会出现在桌面或者系统托盘里。

### 安装 Claude Code 并切换模型

先简单介绍一下，Claude Code 是 Anthropic 推出的 AI 编程工具，直接在终端里运行，你跟它聊天描述需求，它就能自主分析项目、写代码、跑命令、修 Bug，全程自主执行。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HtCDSnpZVbX2niaaRFHyFWbQY10jMFaHz3YPFyMiaRA6SiaXaexicxAtWFNzZ3LxRRnCsMbia95SZtZRplibNko8LbtlIdSMibCXO5lk/640?wx_fmt=png&from=appmsg)

安装 Claude Code 很简单，打开终端，输入一行命令搞定：

```
npm install -g @anthropic-ai/claude-code
```

装好后在终端输入 `claude` 就能进入对话界面，首次使用需要登录。但很多同学没有 Anthropic 的官方账号，登录这步就卡住了，根本没法直接用。

别急，下面就用 CC Switch 把它切换成 DeepSeek V4 模型。

打开 CC Switch，在顶部应用栏选择 **Claude** ，然后点击「添加供应商」：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GmsWBA7sPIwDmQB5MBoVvUywBgf8t0oLicia04CyATVMk4MdCtKGrGyKkymbnVWaDTiaJA8BYVicwtkpCYyrA9wibl6U6pjVwq28kQ/640?wx_fmt=png&from=appmsg)

在预设的模型供应商列表里选择 **DeepSeek** ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1G4XjU4dbCba8M9tCaJ5xwTaufdGdia84AVVczfUCk2BFcjysJsicndm1DPLuRARsYJP3KXI6KKficmKOIhDP4HLyamzzflSeV5xM/640?wx_fmt=png&from=appmsg)

接下来填写刚才在 DeepSeek 开放平台创建好的 API Key：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GkfslQPVXKMkMmIER1CNs8klz0og2s8xRwSPvnQd76L7mW9CvVl3suibunlfFZNh06RfafuB8S4SicY82gypLVakicRkGgyeyfHQ/640?wx_fmt=png&from=appmsg)

其余字段基本不用动，CC Switch 的 DeepSeek 预设已经帮你把模型都配好了，内置了 DeepSeek-V4-Pro 和 DeepSeek-V4-Flash 两个版本。主模型默认是 Pro（对应 Claude Code 里的 Opus 位），小模型是 Flash（对应 Haiku 位）。

如果你想省钱又够用，直接全部用 V4-Flash 也完全没问题，它的 Agent 能力已经很强了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GjZgOiapTJ9IMfpv3YgHibg1TmqwDyGZ2LAib9COicNQpySuXanaQCK80mDRK4uBzH2KGB8j4bNPhrtJKq4SpRIIDf9Kh1dx31ibog/640?wx_fmt=png&from=appmsg)

填完点右下角的「保存」按钮。这里能看到 Claude Code 的 JSON 配置文件，CC Switch 干的活儿就是帮你可视化地修改它，省去手动编辑的麻烦。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FWF0qZqFKkczzRowiayiagmxYj9gLdicuaACYzT5wt2ias6VoqUH1BUoDia4c6dJaW8bUWGJdj4LibAicfxGPk2PVY4f7n7UH08HtX7k/640?wx_fmt=png&from=appmsg)

最后点击启用 DeepSeek 模型：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HPHTvGoicjyOsOmpFHibuzTwbyYuNRPjhMncw3JRrCDEibsTCdkicI6WLXO0Whiaicm07L595ESTRRp7Qic98K6Cq9YG2TcbYZZ3BrKY/640?wx_fmt=png&from=appmsg)

重新进入 Claude Code，让它自报家门，输入一句：你是什么模型？

AI 能正常给出回复，就说明切换成功了：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FncbMY6CgubxkKW03xpoXf4FLHR6efia3xFGyot8vFFSlTe0rQBSobPHxPFdwRp8ky4oCkscEmDGKHsa5DicUvDuYy14MeZ0fYo/640?wx_fmt=png&from=appmsg)

你会发现，用 CC Switch 给 Claude Code 接 DeepSeek，整套流程格外简单。

这是因为 DeepSeek 提供了兼容 Anthropic 协议的接口，而 Claude Code 本身就是按这个协议来通信的，CC Switch 直接把配置写进 `settings.json` 就能用了。

## 给 DeepSeek 加上看图能力

虽然 DeepSeek-V4-Flash 的 Agent 能力很强，但它是纯文本模型，不能理解图片。如果你在 Codex 或 Claude Code 中让它分析一张截图、看一下 UI 界面长什么样，它是做不到的。

不过这个问题也有现成的解决方案，就是给你的 AI 编程工具装一个 **Vision Skill** ，用另一个多模态视觉模型来帮它「看图」。

比如这个通用的 多模态视觉识别 Skill，专门就是为 DeepSeek 这类没有视觉能力的模型设计的。而且由于 Skill 是通用的，Codex 和 Claude Code 等各种 AI 编程工具都能安装使用。

你需要先准备一个支持图片理解的视觉模型，比如通义千问最新的 Qwen3.8-Max，并且到对应的大模型平台获取到模型的 API Key。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1G4I7oI2SibHrdC0Ij0uw8pOqmQEIFgyFvI51Voto9TCe7aavXUQazYYY7psP6UEVCLiaCaNzmCxSZwMLRZLkfyibVdCqySOazFFc/640?wx_fmt=png&from=appmsg)

然后直接在 AI 编程工具中发一段提示词，让 AI 帮你完成 Skill 的安装和配置：

```
全局安装 Vision Skill（https://github.com/asuojun/claude-vision-skill），按照 README 的说明进行配置。
- 视觉模型用通义千问的 qwen3.8-max
- API Key 为 <改为你自己的 API Key>
```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HzXM1ia3mtJOfvSOSAGqXUT8ELXNNIqUUUCmAibWhFhkk5F5xtZefxFQmfhRqqlibgtBCn8ia7pnNrEa59MjwpdssHEpKuPwgJNmA/640?wx_fmt=png&from=appmsg)

安装好之后，当 AI 遇到需要看图的任务时，Vision Skill 就会自动把图片发给视觉模型，让它把图片内容转成文字描述，再交给 DeepSeek 继续推理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HFa7awpQfqgsgibchOL1rBmFwJhqzRK5zDxOk2vhtaEBzoUcM8e5J0X4IZJKybqMZPbXzNL7mib6klApuSRiaRHDvwXK7GUBFXOk/640?wx_fmt=png&from=appmsg)

如果你平时写代码不怎么需要 AI 看图，这一步可以先跳过，等用到的时候再装也来得及。

## 最后

好了，现在你的 Codex 和 Claude Code 都跑上 DeepSeek-V4-Flash 了，百万 token 上下文、Agent 能力拉满、价格还便宜到离谱，爽了爽了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1F3B1dKl7Q0Xpj3w1XYrYPaOWV6mxpgqyibN7FZSd0V7hX8tXDy91juh4tAeaSl7ibhx6RWknLLf1ISC8FcBDJbKCnbtblH5licNg/640?wx_fmt=png&from=appmsg)

你会发现，学习 AI 编程的门槛真的低到不能再低了。

**工具和模型，都不该成为你学习路上的拦路虎。**

所以别再用「我没账号、用不起」当借口了，配好环境，赶紧上手把工具用起来才是。

OK 就分享到这里，本文会收录到我免费开源的 《AI 编程零基础入门教程》，上千张图、几十万字，带你从 0 开始快速学会 AI 编程，做出自己的产品、跑通变现全流程，一次拿捏。

> 开源指路：https://github.com/liyupi/ai-guide

![鱼皮的 AI 编程教程](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Hm2YtyXzic20G7mRyB7KkiaO8QRje5e8v6a0EG8MGcV0vGrErlW5pxOBSeiaiaJlQLDVEl6MgPSw9hZDuN6F0s0X9xTtsQKiaqI71E/640?wx_fmt=png&from=appmsg)

鱼皮的 AI 编程教程

我是鱼皮，持续分享 AI 编程干货，觉得有用的话记得点赞收藏和关注。

也欢迎在评论区聊聊：你用 DeepSeek-V4-Flash 的体验怎么样？

往期推荐

[Codex 又叕重置额度了！送你一份零基础实战教程，狠狠蹬](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589030&idx=2&sn=094158b7116522c9c3683c9103cb0ed6&scene=21#wechat_redirect)

[27 届秋招，巨能打的 AI 智能体项目来了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588930&idx=2&sn=f5d157d911f02f17b2131307e6afe953&scene=21#wechat_redirect)

[我们招人了！急急急急急急急急](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=1&sn=b86c18e05defc803a644e2b6dc3dae12&scene=21#wechat_redirect)

[我的免费 Vibe Coding 教程，大更新！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=2&sn=91ab9714bff9eb6e26d5c03081ec765f&scene=21#wechat_redirect)

[还学不会 AI 编程？我出手了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588292&idx=2&sn=75d57645c0f7d910574677f9d0e14d18&scene=21#wechat_redirect)

[Cursor 保姆级项目实战教程，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247587914&idx=2&sn=2ca469305d3c6c24900deb0bc815d09d&scene=21#wechat_redirect)

[全体码农做好涨薪的准备吧！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588976&idx=1&sn=df3bea7d357480751a77b77b6c7194f5&scene=21#wechat_redirect)

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过