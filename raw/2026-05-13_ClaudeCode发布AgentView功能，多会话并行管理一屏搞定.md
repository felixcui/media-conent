# Claude Code发布Agent View功能，多会话并行管理一屏搞定

**作者**: 鲁工

**来源**: https://mp.weixin.qq.com/s/mRbTHpCYeFoiny4vm_1Puw

---

## 摘要

Claude Code最新推出Agent View功能，旨在解决多会话并行开发时终端散乱、状态难以追踪的痛点。用户只需输入`claude agents`命令，即可在单屏内以表格形式集中管理所有后台任务。该功能通过直观的状态图标和智能分组，实时展示各会话的运行情况与耗时，并支持按空格键快速预览详情及直接回复。这打破了多终端间的信息孤岛，让开发者无需频繁切换窗口，即可一屏高效掌控所有并行任务。

---

## 正文

鲁工 鲁工

在小说阅读器读本章

去阅读

大家好，我是鲁工。

今早刷X，看到Claude官方账号推出了Agent View功能。

![](https://mmbiz.qpic.cn/mmbiz_png/MHVsz9lwuhXBJ8PHq3NKQofn1ibEaBOu9BIgypB1kTo0jWe58hRtEuqQSibqSzEzEF3pNAytXbGCCM1danI77Picq8b8Wrh407icjrgsib8ibE5qg/640?wx_fmt=png&from=appmsg)

一屏幕里好几个Claude Code会话同时在跑，状态图标实时变化，光标停在哪一行按个空格就能直接看那个会话需要什么、敲一句话就能回复。

然后我去Claude Code官方页面看了Agent View的文档，觉得这个功能值得专门写一篇文章。下面先把官方文档的核心点串一下，简单说一下用法。

Claude Code的并行能力不是今天才有。

Subagents给的是一个独立context的子代理，Agent Teams让多个Claude队友彼此通信，Git Worktrees让多个分支文件层隔离同时开干。这三块我之前都写过实操文章，感兴趣的朋友可以回看：

[Claude Code + Agent Teams，并行任务的最佳实践](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247485577&idx=1&sn=5f48937e411001465056a1c9278ed306&scene=21#wechat_redirect)

[Claude Code + Git Worktrees，并行开发最正确的打开方式](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484869&idx=1&sn=1d723494a0cef93f4a21d1d1e5913f8f&scene=21#wechat_redirect)

[用Subagents打造Claude Code专业开发团队](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247483687&idx=1&sn=7e14d5bd5dafc9e8db0181687d3da5bc&scene=21#wechat_redirect)

这些工具本身非常好用，但就像我昨天说的一样，并行项目时的多会话管理功能几乎没有，高强度Vibe Coding下，人的注意力被拉扯到四分五裂。

会话散在不同终端里，每个tmux窗口、每个标签页都是一座孤岛。某个会话在等你做权限决策你不切过去就不知道，某个PR已经准备好让你review状态也得手动ls各个worktree才能拼出来。任务一多，注意力全花在切换上，真正干活的时间反而被切碎。

Agent View要解决的就是这个痛点。

玩法很简单，入口就一行命令：

```nginx
claude agents
```

打开后整个终端就是一张表，列出当前用户下所有的后台会话，按状态分组。pinned的和需要你输入的排在最上面，往下依次是有PR待review的、正在跑的、已完成的。每一行三个核心信息：会话名、当前正在做什么、距上次状态变化多久。注意，在claude agents启动前到已有会话，需要/bg转为后台运行，才能让Agent View看到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MHVsz9lwuhUalt9h2wrHDRzRYDwvPvZNWgWvCeTiag2KWIYzsck565JOQtibvRoBmxKUgmeKWicG7FCKcXl2lY9FHmKTOWYCfQWlM9AayTpicibM/640?wx_fmt=png&from=appmsg)

状态图标设计得挺克制。动画的✽是正在干活，黄色是等你输入，绿色是搞定了，红色是挂了。除了颜色还看形状：✻表示进程还活着可以直接回复，∙表示进程已经退掉但状态保留在磁盘上，下次你attach自动从断点拉起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MHVsz9lwuhXbMaSZAfnp3MyJCqPOicwNEFia9AmJrlLw9jCDpzwAxAXicwX5QT0Zzt6ZYxOOEicMGGFKJkBQvgsG1jzg6OLhumW7368rh46aaX4/640?wx_fmt=png&from=appmsg)

最高频的三个操作：

- 按Space打开peek面板，不用attach就能看到这个会话当前在干什么、需要你回什么。多选题直接按数字键选，普通问题在面板里输入回复直接发送。
- 按Enter或→完整attach到一个会话，跟你直接 `claude` 启动的体验一样，所有命令和快捷键照常用。
- attach之后想回控制台，空prompt上按←就detach回去。

新建会话也有三个口子：agent view输入框敲prompt回车、已有session里跑 `/bg` 、shell里直接 `claude --bg "<prompt>"` 。这三个口子启动的会话最终都汇到同一个agent view列表里。

## 然后Agent View有几个值得说道的设计点。

第一个是文件隔离。

每个后台会话默认禁止写工作目录文件。一旦它要edit，Claude自动把会话挪到`.claude/worktrees/` 下的一个独立git worktree，并发会话各写各的，互不踩脚。删会话时worktree一起清理，重要改动记得先merge或push。

这个做法等于把之前Git Worktrees文章里讲的手动玩法做成了内置默认。对不太熟worktree操作的朋友来说，门槛一下降下来。

第二个是supervisor进程。

后台会话不依赖你的终端存在。Claude Code在你机器上跑一个per-user的supervisor进程，所有background session挂在它下面。即使是关闭agent view、关终端、甚至升级Claude Code，会话都还在跑。会话完成后闲置约一小时supervisor会把进程停掉省资源，状态依然在磁盘上，下次peek或attach时再fork一个新进程从断点继续（attach时会有一小段启动延迟，文档里专门列出来说过这点）。

睡眠和关机会让会话停掉，重新启动后 `claude respawn --all` 一键全部拉起。

第三个是行摘要交给Haiku模型。

Agent View面板每一行的行摘要Edit src/physics/CollisionSystem.ts、needs input: double jump or wall climb?，由配置的Haiku模型实时生成，每15秒最多刷新一次。一个本职是调度的功能里嵌一层小模型做语义压缩，这个设计还是蛮好的。稍微费点token，好在Haiku单价低，这点消耗可以忽略不计。

需要明确一点：Subagents、Agent Teams、Worktrees这几个并行能力Claude Code里都已经有了，Agent View真正新增的是supervisor后台托管机制，再加上一个把所有session装到一起的监控面板。

| 功能 | 解决什么问题 |
| --- | --- |
| Subagents | 给子任务一个独立context window |
| Agent Teams | 多个Claude之间互相通信协作 |
| Worktrees | 文件层隔离多个分支并行 |
| Agent View | supervisor托管 + 把所有后台会话装进一块屏幕统一管理 |

supervisor让session彻底脱离终端独立运行，agent view这块面板把调度员这个角色从人手里交回给工具。之前我们可能要里要记10个tmux窗口的状态，现在一张表全摆出来。

更进一步，agent view输入框里还能直接dispatch一个特定subagent（ `@code-reviewer "..."` ）或skill（ `/<skill-name>` ）。从控制台触发已有的agent和skill抽象，整个Claude Code的复用闭环就跑通了。

整体看下来，Agent View是Claude Code从单会话工具向多会话工作站过渡的关键一步。Subagents、Agent Teams、Worktrees各自补的是垂直能力，Agent View是把这些垂直能力组织起来的横向UI层。

如果你日常已经在跑两三个并行的Claude任务，可以马上试下Agent View功能。

如果觉得有用，点个赞或者在看，也方便更多朋友看到。

感谢您阅读我的文章。我是鲁工，九年AI算法老兵，AI全栈开发者，深耕AI编程赛道。

继续滑动看下一个

AI编程实验室

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过