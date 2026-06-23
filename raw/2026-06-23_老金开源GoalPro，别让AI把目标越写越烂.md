# 老金开源GoalPro，别让AI把目标越写越烂

**来源**: https://waytoagi.feishu.cn/wiki/ENbTwmFBiiJJL8kD70DcKEuUngh

---

## 摘要

针对AI编程工具Claude Code和Codex中因目标提示词过于复杂冗长导致AI执行跑偏的问题，老金开源了GoalPro项目。GoalPro是一套帮助AI在执行前精准界定目标的规则技能，能有效防止AI在小任务上过度发散。该项目兼容两款工具的目录结构，用户既可通过一句提示词让AI自动完成全局安装，也能通过简单的脚本手动部署，旨在提升AI长任务执行的准确性与可控性。

---

## 正文

# 老金开源GoalPro，别让AI把目标越写越烂

> 🔗 原文链接： [https://mp.weixin.qq.com/s/AaNJYDBO...](https://mp.weixin.qq.com/s/AaNJYDBOItpf2OUjkdBbNA)

原创 金先森是朝鲜族阿 金先森是朝鲜族阿 老金带你玩AI*2026年6月22日 16:02  北京*

加我进AI讨论学习群，公众号右下角“联系方式”

文末有老金的 **开源知识库地址·全免费**



---

![](https://feishu.cn/file/QJv6bHempoAme7xcj7pcY7Vtnsg)

Goal这个词最近确实火。Claude Code和Codex里都有了，官方文档也把它放在长任务、迁移、重构、实验这类场景里讲。



它的意思很清楚，给AI一个能持续对照的目标，别让它每一步都靠人重新提醒。



但问题也在这。很多人一听goal重要，立刻把它写成一段超级长的提示词。角色、背景、步骤、约束、验收、风险全塞进去。看着专业，复制进去以后，AI也显得很认真。



然后它开始一路认真地跑偏。你本来只想修一个问题，它开始整理全仓库。你本来只想重构一小块，它开始抽象架构。你本来只想让它写个目标，它已经准备继续改文件了。



这就是我开源GoalPro的原因。Github地址：github.com/KimYx0207

![](https://feishu.cn/file/FBgAbrTihovNSUxsZrVc0MxBn5e)

如果你觉得这个项目有用，也麻烦点个Star，顺手转给身边正在用Codex或Claude Code的人。



开源项目能不能持续迭代，很多时候就靠这些真实反馈和传播。



对的，了解我的都知道我所有开源项目，都围绕着我的核心开源项目 **Meta_Kim**  进行制作的。已经有很多小伙伴使用后做完应用来着老金报喜了，甚至有小伙伴在拿这套项目在写成书，已经七八十页了，可见其内容丰富度了。



简单点儿说，其他我开源的仓库，在Meta_Kim面前，根本不够看一点儿，而且 Meta_Kim 是做任何事情都能使用的万能基座，所以中文名，我才起名为 “元”。



## **先装起来，别先背概念**

GoalPro是一个给Codex和Claude Code共用的goalpro Skill。Skill可以先理解成一套能被AI调用的工作方法，它不是普通模板，也不是执行工具，是执行前把目标写清楚的规则。



它同时支持两套目录。Codex看 .agents/skills/goalpro ，Claude Code看 .claude/skills/goalpro 。你可以装到用户全局skills目录，也可以放进某个项目里，只给这个项目用。



最省事的方式，是直接让AI帮你装。复制这一句就够：

```Plaintext
请帮我把GoalPro安装到这台电脑的Codex和Claude Code全局skills里。
项目地址是github.com/KimYx0207/GoalPro。
先确认当前系统和工作目录，如果仓库还没下载就从GitHub获取，然后把.agents/skills/goalpro复制到用户目录下的.agents/skills/goalpro，把.claude/skills/goalpro复制到用户目录下的.claude/skills/goalpro。
最后读取两个SKILL.md开头，确认name是goalpro，并告诉我安装结果。
```



如果你想手动装，Win和Mac分开看，别混着抄。



Windows用PowerShell：

```Plaintext
git clone https://github.com/KimYx0207/GoalPro.git
cd GoalPro

New-Item-ItemType Directory -Force"$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item-Recurse-Force".agents\skills\goalpro""$env:USERPROFILE\.agents\skills\goalpro"

New-Item-ItemType Directory -Force"$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item-Recurse-Force".claude\skills\goalpro" "$env:USERPROFILE\.claude\skills\goalpro"
```



Mac和Linux用Bash：

```Plaintext
git clone https://github.com/KimYx0207/GoalPro.git
cd GoalPro

mkdir -p ~/.agents/skills ~/.claude/skills
cp -R .agents/skills/goalpro ~/.agents/skills/goalpro
cp -R .claude/skills/goalpro ~/.claude/skills/goalpro
```



如果你只是想在某个项目里试，就不用装到全局。把 .agents/skills/goalpro 放进目标项目给Codex用，把 .claude/skills/goalpro 放进目标项目给Claude Code用。



这里不用把命令想复杂。你真正要记住的是，GoalPro装进去以后，它的任务不是替你干活，而是先把活说清楚。



## **技术含量在五个闸门里**

GoalPro不是把提示词写长。它真正做的是给AI动手前加五个闸门。

![](https://feishu.cn/file/TVc3bTX6GoeprKxLEnfca53Bnzb)



第一个是意图。

用户说优化项目，背后可能是不满意可维护性，也可能是不满意交付可信度，还可能是前一个AI已经跑偏。GoalPro不能复述用户原话，它要把真实不满翻出来。



第二个是边界。

哪些做，哪些不做，哪些文件不能碰，哪些风险必须问人。没有边界，AI会把自己的合理扩展当成你的需求。



第三个是证据。

命令通过、结构检查、本地验证、线上验证、人工验收，这几件事不能混在一起。很多假完成，就是把其中一个当成全部。



第四个是暂停。

遇到删除数据、处理密钥、改公共接口、发布上线、路线互斥、无法验证，它必须停。这个停不是软建议，是写进目标里的规则。



第五个是验收。

最后不是汇报我努力了，而是交出能证明目标达成的材料。测试、截图、diff、行为变化、剩余风险，都要和用户最初的目标对上。



我最看重的是第三和第四。因为AI现在最吓人的地方，不是它懒，是它太勤快。方向一旦歪，它会非常认真地把错误做完整。



如果对你有帮助，记得关注一波\~ 



## **用起来，其实是一条很短的路径**

装完以后，你可以这样问：

```Plaintext
用goalpro，帮我把下面这个请求整理成可执行、可验证、可暂停的Goal Contract：

把订单模块重构一下，现在太乱了。
```



GoalPro会输出一份Goal Contract。你确认没问题，再把它交给Codex的/goal、Claude Code或其他Agent执行。



比如类似这样，放个图能让大家感受明确，但这图有点儿长 - -

![](https://feishu.cn/file/K16WbKbqyoGAuXxyuWTcUgQ9n7d)



注意这个顺序。GoalPro默认 **只输出可复制的goal提示词，然后停住** ，这是我的强制规定，人该检查的时候不能偷懒。



它不会因为目标里写了Execution policy、Verification、Checkpoints，就继续替你改文件。用户没有明确说按这个goal执行，它就不能执行。

![](https://feishu.cn/file/NEHqbSaLIoe5NSxoPTrcND06nGw)



我故意设计的prompt-only闸门。Skill mention不等于执行授权。你说goalpro，它就写目标。你说按这个目标执行，它才进入下一轮执行任务。



这个边界看起来有点保守，但真实项目里很有用。



**因为很多失控不是从大错误开始的，而是从一句顺手的我来继续开始的。**



## **为什么我不把它做成自动执行工具**

有人可能会问，既然GoalPro能写得这么清楚，为什么不顺手执行？



我想了很久，最后还是把它卡住了。



因为目标生成和任务执行是两件事。 **目标生成阶段，最怕的是越权。执行阶段，最怕的是没有目标。** 把两件事混在一起，体验上确实省一步，但边界会变糊。



GoalPro的默认交付物是一段可复制的goal提示词。它写完就停。你可以复制到Codex的/goal里，也可以发给Claude Code，也可以交给另一个Agent。只有你明确授权，它才进入新的执行任务。



好的goal要有清楚的完成条件、验证方式和停止规则，适合那些比一条prompt更长、但又不能无限发散的任务。



AI越来越能干以后，人最容易偷懒的地方，不是把步骤交给AI，而是把目标也交给AI。GoalPro干的事，就是把这个目标重新拿回人手里。



## **谁该用，谁没必要用**

小任务别上GoalPro。改一个错别字、查一个文件名、补一句文案，直接让AI做就行。流程太重，会拖慢你。



但只要任务会跨文件、跨模块、影响发布、牵涉外部事实、需要研究判断，或者你自己都觉得这事容易跑偏，就该先写Goal Contract。



它特别适合三类人。



一类是经常用Codex或Claude Code做项目的人。你不缺AI能力，缺的是让AI少乱跑的边界。



一类是做内容、方案、课程、产品文档的人。你不一定每天写代码，但你会把大任务交给AI，这时候更需要先讲清验收。



还有一类，是已经被AI长任务折磨过的人。你看着它很努力，最后却不知道它到底完成了什么。GoalPro就是给这种场景准备的。



## **最后留一句**

这两年我越来越少相信万能提示词。



万能提示词最容易让人产生错觉，以为只要写得够全，AI就会按人的意思走。真实情况更粗糙一点。目标没写对，提示词越全，跑偏越稳。



GoalPro不是让AI少干活。



它是让AI先确认，自己到底在替谁、为了什么、按什么证据干活。



人负责目标、判断、取舍和验收。AI负责搜索、生成、执行和检查。最后要的不是模型自己觉得合理的结果，而是符合人类目标的结果。



这个边界如果守不住，再强的Agent也只是跑得更快。



跑得更快，有时候不是进步。



是更难追回来。



---

**飞书 开源知识库（实时 更新 交流群 ）：**

**https://tffyvtlai4.feishu.cn/wiki/OhQ8wqntFihcI1kWVDlcNdpznFf**



**Claude Code & Openclaw &Codex 仨顶流全中文从零开始的教程：** [**不懂代码照样造网站，老金15万字Claude Code+OpenClaw教程免费开源**](https://mp.weixin.qq.com/s?__biz=MzI0NzU2MDgyNA==&mid=2247491415&idx=1&sn=8f5fef928275df4c595a4245bb2f3691&scene=21#wechat_redirect)



我的小破站（含我开源的项目）： **https://www.aiking.dev/**



---

每次我都想提醒一下，这不是凡尔赛，是希望有想法的人勇敢冲。

我不会代码，我英语也不好，但是我做出来了很多东西。

我真心希望能影响更多的人来尝试新的技巧，迎接新的时代。



谢谢你读我的文章。

如果觉得不错，随手点个赞、在看、转发三连吧🙂

如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。



扫码 **添加下方微信（备注AI）** ，拉你加入 **AI学习交流群** 。

![](https://feishu.cn/file/VZ47bFVqBo8IHdxZ7RacJK4SnJd)