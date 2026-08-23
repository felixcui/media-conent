# 全网都在推 DeepSeek Harness 插件！skill 还有必要装吗？

**作者**: AI早高峰

**来源**: https://mp.weixin.qq.com/s/-lYVYxeSozbZKbQ3fu0ZqQ

---

## 摘要

DeepSeek Harness（dsh）作为开源Agent框架，以“一切皆插件”为理念，开箱即用性较弱，需自行组装能力。插件提供可执行能力，而skill本质是纯指令，告诉模型“怎么做”，由插件系统承载和加载，二者互补而非冲突。旧skill可迁移至dsh，但需适配其格式。

---

## 正文

AI早高峰 AI早高峰

在小说阅读器读本章

去阅读

AI TOOL · 科普2026.08

必装 skill 文章满天飞？

插件火了， 旧装备

别急着扔

DeepSeek Harness · 插件生态 · 技能迁移

DeepSeek Harness

dshSKILL

📦 3 Parts + Conclusion

👉 滑动

PART 01

能力缺口

毛坯房之谜

PART 02

skill × 插件

车间与工艺

PART 03

迁移旧技能

无脑 copy

PART ///

写在最后

弹药库

前言

最近 dsh 非常火，开源不到 48 小时就破了 10 万 Star，创下 GitHub 史上最快涨星纪录💹

DeepSeek Harness（简称 dsh）是 DeepSeek 于 2026 年 8 月 13 日开源的 Agent 框架，口号是「 **一切皆插件** 」

截至目前，全网都是 dsh 相关教程的文章，火了大半年的「必装 skill」文章，被「dsh 必装插件」取而代之。

好像 skill 被「插件」这个词吞掉了。那么：

dsh 中 skill 还存在吗？

现在以什么形式存在？

以前给别的 agent 装的 skill，dsh 还能用吗？

如果你也有同样的疑问，见下文分享～

01

PART

先聊聊 dsh 的能力缺口在哪？

WHY GAP

「 **一切皆插件** 」的意思是：开箱状态下，这是个毛坯房，没有冰箱彩电（丰富的插件），还不能让你「拎包入住」（直接上手用）。所有插件和能力靠你自己组装，比如需要看图片、换皮肤、有记忆、连浏览器。一装一个不吱声。

Agent 框架前辈们（WorkBuddy、Codex、Claude Code 等），都是集成好的产品，模型、工具、执行循环、UI 耦合在一起，你拿到手的是厂商配好的那一套。

然而，DeepSeek Harness 把这件事推到尽头，它的插件能替换的，包括核心模型、工具箱、规则、甚至整个 UI。别的产品是「在核心外面加东西」，它是「连核心本身都能换」。

![](https://mmbiz.qpic.cn/mmbiz_png/zgfUuwO1OHxbJxgz54MpWsrxx88l5nenmsNYMTFMhiatwBRRibjVEWPDbx55tXkXwhiaP2WooxKphFvLWHDfPpKKIo8ia0soHSWQCIyM21ESY6I/640?wx_fmt=png&from=appmsg)

CC vs dsh：别的产品在外围加东西，dsh 连核心都能换

初次使用的人免不了直接吐槽：「太毛坯房了」「HTML 预览窗口都没有」「还不如 WorkBuddy 舒服」。

这个机制，对开发者来说，确实很灵活；

对非技术人员而言，就是有缺口、有使用门槛。

好消息是，目前市场上已有 8k+ 插件，正在填补这部分缺口。

02

PART

skill 和插件是什么关系？

SKILL × PLUGIN

那么，skill 在该生态中处于什么位置？是插件的一部分吗？

官方说： **「skill 是纯指令，不提供可执行能力」**

这句话其实点出了 skill 和插件的核心区别：

一句话理解 skill 的本质

skill 本身不是一个可执行的能力组件，而是一段告诉模型「应该怎么做」的指令

在 DSH 的生态中，skill 是由插件系统承载、发现和加载的内容。我们可以用一个简单的比喻来理解：

一个最直观的比喻

插件是一个车间，skill 是一道工艺流程

「车间」提供连接工具和运行环境，「工艺流程」则告诉模型具体应该按照什么流程去完成任务。

因此，DSH 中的 skill 依然存在，但它不是插件，也不是与插件并列的另一套执行机制。

它更接近于插件生态中的指令层：由插件系统负责发现、注册、加载，并在需要时提供给模型。

所以，插件和 skill 并不冲突，而是互补关系：

插件：解决「能做什么」

提供能力和运行时。

skill：解决「怎么做」

提供流程、指令和使用规范。

![](https://mmbiz.qpic.cn/mmbiz_png/zgfUuwO1OHx98e9CWeyuSHoTCWRSnfiahkDGdK8ftVE5JDuIiaDJezMuw4XyHOPIEZu5KI9ia2Ciaznh0R7tAFliaIR9TziaBZXEDn7J6h6U5LrhQ/640?wx_fmt=png&from=appmsg)

一图理解：skill 与插件的关系（车间/工艺流程）

03

PART

dsh 的 skill 格式有什么不同？

FORMAT

dsh 的 skill 也是一个带 YAML 格式 的 Markdown 文件，和 Anthropic 给 Claude Code 定义的是同一套契约。

两种合法的 skill 形态：

...text

skills/

　kimi-webbridge/

　　SKILL.md　　← 目录包，主文件加 references/、scripts/

　quick-note.md　← 扁平文件，单文件技能

格式细节不赘述，dddd。

注意事项：按官方 skills 子系统文档的说明，确定不支持递归发现。dsh 只认根目录下的子目录和扁平文件，把技能藏进二级子目录就找不到了，这是一个容易被忽略的细节。

04

PART

skill 安装在哪？

INSTALL

| 优先级 | 路径 | 什么时候用它 |
| --- | --- | --- |
| **200** | 项目/.agents/skills | 技能只属于这一个仓库，需要随仓库一起走 |
| **500** | ~/.agents/skills | 技能是你个人使用的，其他 Agent 框架也要用，就放这 |

第 1 个优先级最高，最快的落地方式是第 2 个：把技能目录放进 ~/.agents/skills/，dsh 启动时自动扫到，不需要任何配置。

而且安装一份 skill，两个 agent 都能看见，这就是 skill 比插件灵活的地方～

05

PART

以前用过的 skill，dsh 能用吗？

MIGRATION

放心， **无脑迁移～** 可以直接 copy：比如我装了个 kimi-webbridge skill，就在 ~/.claude/skills/kimi-webbridge。想让 dsh 也用上，直接复制到 dsh 的 skill 根目录 ~/.agents/skills/ 就行。

...bash

mkdir -p ~/.agents/skills

cp -r ~/.claude/skills/kimi-webbridge ~/.agents/skills/

拷贝完成，重启 dsh。输入 /，kimi-webbridge 就出现在命令面板的 Skills 分组里，就可以使用啦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zgfUuwO1OHxibg60WUwbjjZsbBLzDKuO2TK6mG5Bl9skErQFGvonVicqG833EFCsH5BZ0Nu4b1sLTJ4xeDH5KGGoQgoBOGHbbjBJl1hNBbiceI/640?wx_fmt=png&from=appmsg)

kimi-webbridge skill 出现在dsh命令面板

**实用规则：** 在 cc / CodeX 写过的 skill，原样丢给 dsh 试一遍，大概率不用修改。

06

PART

彩蛋 · 亲测好用的 9 个 dsh 插件

BONUS · TOP 9

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zgfUuwO1OHzEGLZAvpibhvWxbGV7ahYta0vBo9BQTwktibBHCpML9gKGicB2nwmiaqYoLPmMbl3W2QJbEAuWJORtj1EibZGdQeWx2PPib64TYruWo/640?wx_fmt=png&from=appmsg)

dsh 插件 TOP 9（按 Star 从高到低排列，快照 2026-08-20）

1

**先装 dsh-plugin-store** ，它是装插件的插件，也是这 9 个里唯一要敲命令的。

...bash

dsh plugin --profile web add github:0xKcyzz/dsh-plugin-store

装好后设置里就有插件商店，剩下 8 个全在商店搜名字一键装。

2

**优先级分三档** 。最该先装的是插件商店、better-sidebar（日常工作的台子）、modlens（给纯文本模型配眼睛）。用到再装的是 dsh-office、dsh-turn-rewind 这类。最后才是皮肤、宠物这些花活。

3

**装完记得重启** 。如果没生效，重启 dsh 或强刷新页面。

∞

LAST

写在最后

SUMMARY

所以，「一切皆插件」并没有吞掉 skill，它只是换了个地方继续发光。插件解决能力，skill 沉淀流程，插件生态再热闹，也替代不了你验证过的那套打法。

skill 不是过时资产，是现成的弹药库

全网都在装插件，但你的技能库是独一无二的

全网都在装插件的时候，把你吃灰的 skill 搬进 dsh，可能是性价比最高的一步。

---

你的 dsh 装了什么插件和 skill？评论区聊聊～

既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。

点赞 在看 转发

THANKS FOR READING

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过