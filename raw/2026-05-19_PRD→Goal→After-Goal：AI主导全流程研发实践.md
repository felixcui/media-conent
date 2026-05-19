# PRD → Goal → After-Goal：AI 主导全流程研发实践

**作者**: 欢迎关注的

**来源**: https://mp.weixin.qq.com/s/0dSfok0fLN-OTIIYIYZ5rg

---

## 摘要

本文将/goal斜杠命令 + /prd技能 + /after-goal技能，实现了一个产品特性研发全自动化的流程，探索出一个AI+实践的新案例。该流程成功将原本分散、手动的多环节研发过程固化为高效、自动化的三阶段协作，显著提升了开发效率与规范性，并验证了 CLI 工具优于浏览器操作、Skill 作为流程知识载体等最佳实践，为 AI 辅助研发提供了一个可复用的轻量级全自动解决方案。

---

## 正文

欢迎关注的 欢迎关注的

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5p8giadRibbOib5eKA9DvsnapbBokh883cWMjGKcouP64pz9gW7ayIktXwzlApWmhiawhw9RdHV0cHIv7ubnatc8lQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击蓝字，关注我们

作者 | 鸟窝

导读

introduction

本文通过真实案例展示了如何利用 Claude Code 的 /prd、/goal、/after-goal 三个斜杠命令，实现从需求拆解到代码合入的全自动化开发流程。

该流程成功将原本分散、手动的多环节研发过程固化为高效、自动化的三阶段协作，显著提升了开发效率与规范性，并验证了 CLI 工具优于浏览器操作、Skill 作为流程知识载体等最佳实践，为 AI 辅助研发提供了一个可复用的轻量级全自动解决方案。

*全文 3703 字，预计阅读时间 6 分钟*

前言

GEEK TALK

最近我想给大模型训推任务灵犀诊断平台增加「自我演化」的功能，尝试使用claude code的最新的/goal命令，记录从需求拆解到代码合入的完整流程，供同学参考。

最近两周codex、hermes相继发布/goal斜杠命令，这一周 claude code也不甘示弱，跨速发布了它的 /goal 斜杠命令。本文将/goal斜杠命令 + /prd技能 + /after-goal技能，实现了一个产品特性研发全自动化的流程，探索出一个AI+实践的新案例。

我已经将此流程泛化为一个通用的开发流程，支持github，项目地址：https://github.com/smallnest/goal-workflow, 官网：https://goal.rpcx.io/ 。

GEEK TALK

00

背景

在百度内部研发场景中，一个功能从需求到上线通常经历：写 PRD → 拆卡片 → 写代码 → 提 CR → 合入 → 关卡片。这套流程环节多、工具分散（iCafe、iCode、Gerrit），每一步都要手动操作，容易遗漏步骤。

借助 Claude Code 的 Skill 机制，我们可以将这套流程固化成三个阶段，每个阶段对应一个 Slash Command：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7Rt03kIRdMwWK9YHaEKoIQY7XyYepMXs5arBIPYZkhqp2SIEW0PEDPEIJSkVMfe8K9KTYkgvjUhibHfSDHTibxQm9LRPPTp3a60/640?wx_fmt=png&from=appmsg)

下面用一次真实开发过程，演示这三个阶段如何串起来。

GEEK TALK

01

第一阶段：/prd — 需求拆解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5SbWVzFWEeiaFHicxqOaJyCgqom6ibOd9k1fXEXUTlHeaFcy8ldyjysHZd4ANLSBenhOCibUgKMiaR5Mp4RkibaM6mCH3NPzhibOGNdo/640?wx_fmt=png&from=appmsg)

**1.1 安装PRD skill**

https://console.cloud.baidu-int.com/onetool/skills/4793

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7v7xE58dibG1ogprA5IYO25xrxK5xOWHicicvf3DHfB5LRcVic46t7CKazbrZnzOgXT5EDCb292RNWfnujSxpZUL5tkgDlaWg6IEU/640?wx_fmt=png&from=appmsg)

**1.2 做了什么**

使用 `/prd` 将「诊断案例记录与反馈闭环」这一产品需求，生成结构化 PRD 文档：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5YZ3Ve4KciaINeSoE9DEeE0RRpeaLsvFydztTLnGaYRqe7cRPmWTErgErG3nkvpo1tqvp90OTbOJeaoEQYnJxsUQ1KfoEMbfVY/640?wx_fmt=png&from=appmsg)

它需要我澄清一些东西，这次我没有做它的选择题，我认为我描述会更清楚，所以我直接告诉它我模糊的想法，它就实现了产品需求文档的编写：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4hR3efBYgEu0MOonpzeP8Cica47WWGia2ibQ6LRBWEEUJuVxGynlkj2oNibs90avt8VhcA8LlAG74LFVk1HvBSUOotd2wwtl4Z0F4/640?wx_fmt=png&from=appmsg)

PRD 文档自动保存到 `tasks/prd-self-evolution.md` ，卡片自动创建到 iCafe 空间，标题、描述、验收标准、优先级一应俱全:

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5BlibibTMR20Poic4nNO99qibdED8ahFgWicGhMuSaRZLiauN8RWHFdIsovpYFHiaF0YFI5Dzqd8hAPACicjjAVtrmFbo89n4devFnFSk/640?wx_fmt=png&from=appmsg)

并拆分为 5 张 iCafe 卡片，然后询问我卡片创建在哪里，我选择icafe,然后它就帮我创建好了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy6hIgibs3PCoL1loC9V3iac17IqDkk8oxSEib6jbzwMlpNf8TiaaUOQb6ObgvjB3dib5tMSE9yPLeDHFS1SJe3uPKv193bDDcvibiaoXI/640?wx_fmt=png&from=appmsg)

我们可以看一个它创建的卡片，主要包括此任务的描述信息、验收标准以及卡片依赖关系：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4cB3XS65UVic1ibmdKOp2UuFzdScJ9WL2LKItSia8Fkv9Wx4bSwrluAxLqX9eOetlL2tDZmcmiarkO7rTGs52tbRVkv1GrQZEqyXA/640?wx_fmt=png&from=appmsg)

**1.3 为什么要先写 PRD**

直接让 AI 写代码，容易出现需求理解偏差、边界条件遗漏。PRD 强制你先想清楚：

- 有哪些用户故事？每个的验收标准是什么？
- 哪些是 Non-Goal（明确不做的事）？
- 卡片之间的依赖关系是什么？实现顺序怎么排？

PRD 写完后再拆卡片，每个卡片的范围足够小、验收标准足够明确，AI 才能高效实现。

而且，卡片如此定义之后，就可以很好的配合使用claude code的 /goal命令或者 codex的 /goal命令了：

- 卡片任务明确可操作：/goal 就可以2按照要求准确的实现
- 卡片有验收标准：/goal 就可以写单元测试，保证它实现的代码符合需求
- 卡片有依赖关系：/goal 可以按照顺序有序的实现功能
- 卡片足够小：/goal 就可以快速实现快速反馈，避免长时间占用资源和死循环

GEEK TALK

02

第二阶段：/goal — 逐卡实现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4WxicePuRUD236Os9VYcdYLiaVEf79gwEpk26kZjwmdfJtU9lAic0Qlse30clNDB82qOgxvU6P7el0dE9j79Wice4DqukbOAViaVcM/640?wx_fmt=png&from=appmsg)

**2.1 卡片 46：Case 数据模型与 Markdown 读写库**

```bash
/goal 实现卡片 baidu-sys-nccl-sys-skills-46
```

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5GQq1wC8FiaJmRPkMFc5emOTWia6Xr0nOgCQfZB3iaFEMeO4vpgBhdzibdVBtZyiaoLFXAp7xfW89w0qQ3VMIF6edqOZbzTGWV3jXw/640?wx_fmt=png&from=appmsg)

Claude Code 自动完成了以下工作：

1. ****查询卡片**** ：用 `icafe-cli card get` 获取卡片描述和验收标准
2. ****理解上下文**** ：阅读 `diag/CLAUDE.md` （项目架构文档）、 `diag/model/types.go` （现有类型定义）
3. ****实现代码**** ：创建 `diag/cases/case.go` ，定义 `Case` struct，实现 YAML frontmatter + Markdown body 的序列化/反序列化，提供 `WriteCase` / `ReadCase` / `ListCases` / `UpdateCase` 四个核心函数
4. ****编写测试**** ：创建 `diag/cases/case_test.go` ，10 个测试覆盖 round-trip 序列化、文件读写、列表过滤、部分更新、空结果、特殊字符、错误场景
5. ****验证**** ： `go vet` 、 `go build` 、 `go test ./diag/...` 全部通过
![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4wONTDr7OufT3qCGML1dzSB43rcichaS95JiaWHT5CDMdFiaYZhRdiaHvLHiaQWvia6JhQ1FVTnQLFYxeSG7DRavlJH7Zl4Bh1z8vT8/640?wx_fmt=png&from=appmsg)

/goal 只负责实现卡片。卡片的代码提交和卡片的更新它不负责，所以我实现了这个卡片后，手工指导claude code使用icode-cli实现代码:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5SHebc7tTdBwPJ51KJ10uiaxX00feHxkw3jT3Klms4uqcDa2jlYbUqC0yp3kLl5Q43AP88KtID8PiaUWtbBvES9Kb0e0X5dpHFo/640?wx_fmt=png&from=appmsg)

并且把实现summary更新到卡片的描述字段中：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6NobwAjsrGEjtibIuuaEIObvXa80DIpMic5ibibXbtMdiaiaJ5hhwcjLU6tTYvoeAGTXCOyyEcP0wicSr2UovZPhfPbju9jlFsnuQahM/640?wx_fmt=png&from=appmsg)

然后我把这个流程作为经验，让claude code帮我实现了一个 `after-goal ` 的skill,负责提交代码、review打分、代码合入、更新卡片和关闭卡片(设置为已完成)。下一个卡片我预期手工调用 `/after-skill` 即可，实际上claude code足够聪明，自己就自动调用这个skill了：

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5NWykUGndrCuaOgZt9k8CfPmpavZDvL9JiattYxChic6qcgbx4ced69usnjDica6pdwaudiaPwtmibkmckHyYorkWPpZ2bQBaYX7Lg/640?wx_fmt=png&from=appmsg)

**2.2 卡片 47：Pipeline 诊断完成后自动写入 Case 文件**

```bash
/goal 实现卡片 baidu-sys-nccl-sys-skills-47
```

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7mr2ib8NwwQq0jOyh2dtsSVVwwygyMjJnFye1A8sg7hq2Vq6DO0iaUY4vOe0sL4MkaZjyc45UiczbzZrjiaY59YA8UeO9tVs6egKo/640?wx_fmt=png&from=appmsg)

这个卡片的实现涉及跨包集成，关键改动：

1. ****导出**** `****claude.BuildPrompt****` ：原来 `buildPrompt` 是小写未导出函数，Pipeline 需要调用它获取 system/user prompt 写入 Case
2. `****PipelineConfig.CasesDir****` ：新增配置字段，为空时不写入 Case 文件，向后兼容
3. `****Pipeline.Run****` ****defer 写入**** ：在 `defer` 块中调用 `writePipelineCase` ，覆盖成功和失败两种路径；写入失败仅 `golog.Warn` ，不阻塞主流程
4. ****修复**** `****extractSections****` ：改为按已知 section 标题（ `System Prompt` 、 `User Prompt` 等）定位内容边界，正确处理内容中含 `## ` 子标题的情况
5. ****3 个新测试**** ：成功路径写入、失败路径写入、CasesDir 为空时不写入

**2.3 /goal 的核心价值**

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7rcPJGPxWVicbr7h4h60R1YXq0aic1mEw8AArqxjYDd2hqUZwrnhflV92dOA4iclNribYPsWCXtY3JqTF4s3fEHEpNybLNBbEfAWM/640?wx_fmt=png&from=appmsg)

GEEK TALK

03

第三阶段：/after-goal — 提交合入关闭卡片

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy6WlPMogoApxC8K5y2hEDKSDTGV2bDTE0ZN6l82MEx6msbWelgXC4hdBRsgKvvYO6fAOibkVamRmIAbGnQicHEbdkAwbfOribRGfQ/640?wx_fmt=png&from=appmsg)

**3.1 安装after-goal skill**

https://console.cloud.baidu-int.com/onetool/skills/4797

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy46FEu4Zf6orbvls1dS4GJibbWPtcT8QthcvPNoibKrIEwrk2aib5Bwj3Puo5KED2kVhzcBXuWv20jyxlLkdrTPmeYSdicWcajkQibQ/640?wx_fmt=png&from=appmsg)

**3.2 从手动操作到 Skill 化**

卡片 46 完成后，我手动执行了提交、推送、打分、合入、更新卡片、关闭卡片的全部步骤。这个过程涉及三个 CLI 工具的配合：

```nginx
git (提交/推送) → icode-cli (打分/合入) → icafe-cli (更新卡片/关闭卡片)
```

问题是：每次都要查命令参数、记 CR 编号、拼 HTML 描述，容易出错。于是我把这套流程固化成了 `after-goal` Skill。

**3.3 卡片 47 使用 /after-goal**

卡片 47 实现完成后，直接调用：

```bash
/after-goal 卡片 baidu-sys-nccl-sys-skills-47
```

Claude Code 按以下步骤自动执行。实际你看下面的截图，我并没有主动调用这个skill,是claude code完成代码后自动调用的，太智能了：

****Step 1: 提交代码****

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7CKXkDWe5dMyRvjPxWKUSkWjxlmib1RXgnlfEBaywcN7k1QP7a8CNGggK3aB4IchltURPWquNCIOOQQtUeHVUEeoMFwDQowWT8/640?wx_fmt=png&from=appmsg)

```swift
git add diag/cases/case.go diag/llm/claude/claude.go ...git commit -m "baidu-sys-nccl-sys-skills-47 Pipeline 诊断完成后自动写入 Case 文件..."
```

关键：commit message 以卡片 ID 开头，iCode 要求绑卡。

Step 2: 推送 Gerrit

```ruby
git push origin HEAD:refs/for/master
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy4d0Iv7NE5DGpW1MibtjShv1j3iafJ9SUspOHLsVrZtiattZvCNk50cXJAORicsKFRWPachicGGlg8Wib4vhGPAxA1F6hAcIDFMcAD7Y/640?wx_fmt=png&from=appmsg)

iCode 禁止直接 push master，必须走 `refs/for/` 。输出中包含 CR 编号。

Step 3: 打分 + 合入

```bash
icode-cli api get_review_info -n 120869646 -o table  # 确认可合入icode-cli api set_review_score -r baidu/sys-nccl/sys-skills -n 120869646 -s 2  # 打分icode-cli api submit_review -r baidu/sys-nccl/sys-skills -n 120869646  # 合入
```

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy7zXYOrO4o1eBib5RQxusQEMic64Z6QFGbMkZSFMEicUd3foy1qH7IaOJpRxdKNjYic4tbnVb50GXniaSetHuNaJo5vwnEgd2EcF0OY/640?wx_fmt=png&from=appmsg)

这里有个经验：之前卡片 46 时我尝试用 playwright-cli 打开 iCafe 网页操作，非常笨重（弹窗多、元素难定位、登录态问题）。换成 icode-cli 后一条命令搞定打分和合入，效率提升巨大。

****Step 4: 更新卡片描述****

```css
icafe-cli card update --space baidu-sys-nccl-sys-skills --sequence 47 \  --detail "<原有描述><h3>实现总结</h3><ul>...</ul>"
```

注意 `--detail` 会覆盖整个描述，必须保留原有内容再追加。实现总结包含：核心改动、测试覆盖、验证结果、Commit 和 CR 链接。

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5V5Rr1r8vVumfdZlOrAlnicHPfx2ARCW36Sicp9YIeThuS1VTI0uIc69aEfbvv69se1j6weDyfTSGrINspEkV3L8oYLf3RCc17M/640?wx_fmt=png&from=appmsg)

****Step 5: 关闭卡片****

```css
icafe-cli card next-statuses --space ... --sequence 47  # 查可用状态icafe-cli card update --space ... --sequence 47 --status 已完成  # 关闭
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5ib1rUJ1jQyQuGbhyZ8PF02sxBkhmaNpgdhuAhqic8kBqPvqRBkQdgp46thnDiaOXnWNFQuTTskkwFOj4FShrGkicFzkc4gqVePNA/640?wx_fmt=png&from=appmsg)

状态名不是随便写的，不同空间可能不同（"已完成" vs "Done"），必须先查 `next-statuses` 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5Pd786rEIZic4WLTlKWkqDm90APnX7PIQKspbID7maBicAfe1uiad1apqoLTFLszLdWhBYfQcN0Fw2z1SXD3enbz8RYkGxAibyyFc/640?wx_fmt=png&from=appmsg)

**3.4 /after-goal 的核心价值**

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy4df1MryVaDQ2EpZmEOenvnUXS377dwiakMQGTcynAuYBxyo7hUWoicYjNQSSnnbc7VhicZUVf7s62TibVndRiaAqSuo4fRiasPTrH6w/640?wx_fmt=png&from=appmsg)

GEEK TALK

04

经验总结

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy5Lk9pKYjW45WN6DK2I8KX2Q2eE4IIp0Cbv5pVE29hen8BYLO1icuN8s54C04tzldVicFY5uHxytR2tFYBTeiasatyC8jicsNiaKh8w/640?wx_fmt=png&from=appmsg)

1\. PRD 先行，避免返工

AI 直接写代码容易偏离需求。先用 `/prd` 生成结构化 PRD，确认范围和验收标准后再拆卡片实现，能大幅减少返工。

2\. 卡片粒度要适中

本次拆出的卡片 46（纯数据模型 + 读写库）和卡片 47（Pipeline 集成）各自独立、验收标准清晰，AI 能一次实现到位。如果卡片太大（比如把 46 + 47 合成一个），实现过程中容易丢失焦点。

3\. 依赖关系决定实现顺序

卡片 47 依赖卡片 46 的 `cases` 包。按依赖顺序实现，每个卡片完成后再做下一个，避免同时改多个包产生冲突。

4\. CLI 工具优于浏览器操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7A1EictTRRcp4Y2Wtzg1fQGItkchfqv6BuDUN9bCCj7d59maoKC4xjn3PtwY6h2peBrlkzUaSfLXEDF0ryC91FhfN8pSKCsQlA/640?wx_fmt=png&from=appmsg)

****结论**** ：凡是能用 CLI 完成的操作，不要用浏览器。

5\. Skill 是流程知识的载体

`after-goal` Skill 把「提交代码 → 推送 Gerrit → 打分合入 → 更新卡片 → 关闭卡片」这套需要记住的操作流程固化成了可复用的 Skill。核心要素：

- ****触发条件**** ： `/after-goal` 或说"提交代码"、"打分合入"、"关闭卡片"
- ****步骤定义**** ：5 步串行流程，每步有具体命令和参数
- ****错误处理**** ：常见问题的处理方式（push 被拒、状态名不对等）
- ****关键规则**** ：commit message 绑卡、 `--detail` 覆盖问题、先查 `next-statuses`

写 Skill 的过程本身就是梳理流程、沉淀知识的过程。

6\. 踩坑即修正，不要留到后面

卡片 46 中 `extractSections` 按 `\n## ` 分割的方案在简单场景下工作，但卡片 47 的 UserPrompt 包含 `## ` 子标题时解析失败。发现后立即修复（改为按已知标题定位），而不是"先这样后面再说"。早期修正成本最低。

GEEK TALK

05

三阶段协作模式

![](https://mmbiz.qpic.cn/mmbiz_png/D0qMsFCrMy5z8fVUXI2oqNX0sj28hiaofmTqzVIxaL1mV64E6b8iahBzss2MAPP0cZWz55dAeGl9tKDyJAzkjHdyBaZ2E2ibBejzqv7t4nlSF4/640?wx_fmt=png&from=appmsg)

```bash
┌─────────────┐     ┌──────────────┐     ┌───────────────┐│   /prd      │     │   /goal      │     │  /after-goal  ││             │     │              │     │               ││ 需求 → PRD  │────▶│ 卡片 → 代码  │────▶│ 代码 → 合入   ││ PRD → 卡片  │     │ 代码 → 测试  │     │ 合入 → 关卡   │└─────────────┘     └──────────────┘     └───────────────┘      ↑                    ↑                     ↑      │                    │                     │  人类定方向           AI 执行实现          AI 执行收尾  AI 辅助拆解         人类验收结果          流程自动闭环
```

三个阶段各有侧重：

- ****/prd**** ：人类主导方向，AI 辅助结构化输出
- ****/goal**** ：AI 主导实现，人类验收结果
- ****/after-goal**** ：AI 全自动执行，流程自动闭环

这套模式不仅适用于本次「诊断案例记录」功能，任何需要从需求到上线的开发任务都可以复用。只需三个命令，就能走完从需求拆解到代码合入的全流程。

GEEK TALK

06

Autoresearch vs /goal

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D0qMsFCrMy7JJupCOtHC22phFxgyFn4xibTrD6T4WBWZPSZnia5l64nP61vWogqpZEPr9PguZo35ib36mLib9QtIKFYxGZkibpSiayx5IJMlMicuWo/640?wx_fmt=png&from=appmsg)

先前我也介绍了 `autoresearch ` 全自动开发的方式和流程，整个流程和这个类似，不过 `autoresearch ` 在开发过程中采用了多智能体review和开发的方式，通过5个维度对代码进行打分，给予开发者更灵活的配置方法，但是开发速度也远远大于/goal的方式，token的费用也远远大于/goal的方式。

所以如果想实现一个轻量级的全自动开发流程，本文介绍的 `/PRD → /Goal → /After-Goal` 是一个不错的选择。

END

**推荐阅读**

[AI Agent 如何重构 App 稳定性治理流程](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247606823&idx=1&sn=edbf58352657c27caac32c0688dab187&scene=21#wechat_redirect)

[AI Coding 入门指南 - 如何更好地让AI真正帮你干活](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247606815&idx=1&sn=669d7f811d09b128c451630f9a170d24&scene=21#wechat_redirect)

[2 小时，0 行手写代码，我用 Claude 做了一个生产级 VSCode 插件](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247606775&idx=1&sn=087dc53d2592426863211b8ef4570ce4&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5p8giadRibbO9x9T3iaxknhz6B4v4PPxvGEAlXibefUzgTftSnnT6QficHvz0w4T1CtHpDD8ZDU7NiaAjkHFssZN9IYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

一键三连，好运连连，bug不见👇

继续滑动看下一个

百度Geek说

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过