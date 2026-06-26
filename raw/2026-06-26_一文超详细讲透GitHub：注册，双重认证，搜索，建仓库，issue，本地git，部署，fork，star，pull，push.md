# 一文超详细讲透GitHub：注册，双重认证，搜索，建仓库，issue，本地git，部署，fork，star，pull，push

**来源**: https://waytoagi.feishu.cn/wiki/FaiswBIzaiYkOHk0AEJctvHRnOb

---

## 摘要

本文是一篇面向AI编程爱好者的GitHub保姆级教程，强调了掌握GitHub的重要性。文章首先解释了开源的本质及常见许可证，并清晰区分了本地版本控制工具Git与云端代码托管平台GitHub。随后详细演示了如何使用Gmail注册GitHub账号、设置规范用户名与强密码，以及如何开启强制要求的2FA双重认证，为新手后续学习建库及代码协作打下基础。

---

## 正文

> 🔗 原文链接： [https://x.com/laowangbabababa/statu...](https://x.com/laowangbabababa/status/2061384966227849698)

![](https://feishu.cn/file/BAgcbVF6JoIbAxx8Bi7c5MwjnQf)

这是一篇 GitHub 的奶爸级别教学。如果你是 AI 编程爱好者，本文对你帮助是极大的。

GitHub 有多牛？它有 1.8 亿开发者，至少 6 亿以上的仓库数量。你知道的腾讯，阿里，字节的开源项目全部都会放到 GitHub 上。

上面内容五花八门，全部开源免费，比如有最近爆火的 OpenClaw，有数字人，有 Skill 仓库，甚至还有阿波罗登月的代码等等。

GitHub 可不是程序员专属，因为 AI 编程能力变强了，现在几乎要人手一个 GitHub 仓库里。

接下来老王带你学习它的核心功能，包括：

- 怎么注册，搜索，使用 GitHub
- 了解 GitHub 详细功能点
- 如何提交和备份 GitHub 项目



# 先说说开源是什么

说 GitHub 之前，先讲清楚一个更基础的问题。别人说把自己的代码开源了，到底是什么意思。

代码本质上是文字，你写了一段程序，它就是一个文本文件。不开源的意思是这段文字只在你电脑里，别人看不到。开源的意思是你把这个文本文件放到 GitHub 上，设成公开仓库，任何人都能看、能复制、能拿去改。

但开源不等于放弃所有权。你仍然可以在代码里放一份许可证，规定别人能用它做什么、不能做什么。MIT 协议最宽松，几乎不限制。GPL 协议最严格，别人用了你的代码，他自己的代码也得开源。什么都不放，法律上默认保留所有权利，但实际没人管得住。

搞清楚这个前提，接下来所有操作都围绕它展开。

![](https://feishu.cn/file/RE6DbMeS0oU16bxXpDBcIe0Qnme)

# 再说说 Git 和 GitHub 的区别

两个名字长得像，但不是一回事。

Git 是一个版本控制工具，装在你电脑上。它帮你记录代码的每一次改动，谁在什么时候改了什么，随时能退回到任意一个历史版本。Git 不用联网，单机就能用。

GitHub 是一个网站，跑在云端。它把 Git 仓库托管到服务器上，让你能和别人共享代码、协作开发。你把本地 Git 仓库推到 GitHub，别人就能看到和下载。

就是，Git 是你电脑上的版本记录本，GitHub 是这本记录本的云端备份加共享平台。

![](https://feishu.cn/file/AGLZbQHejormedx4CnlcvLpXnKe)

# GitHub 账号

打开浏览器，地址栏输入[github.com](https://github.com/)，回车。页面正中间点绿色的 Sign up 按钮。 

![](https://feishu.cn/file/WgQ3bBj4joZFb3xZU9jcbEtbnZg)

要填四项：邮箱、密码、用户名、国家。

邮箱直接用 Gmail。没有的话，提前注册一个，网址：

不只是 GitHub，后面做开发还会用到 Supabase 数据库、Vercel 部署、Cloudflare 域名，这些全部支持 Google 账号一键登录。一个 Gmail 在 Chrome 浏览器里就包圆了，省掉反复注册的麻烦。

QQ 邮箱和 163 邮箱经常把验证邮件扔进垃圾箱，不推荐用。

![](https://feishu.cn/file/QpFxbqyu1o1PTYxhZX0czgWinHc)

用户名是你在 GitHub 上的身份标识，以后会出现在所有代码链接里，别起 test001 这种临时名字，用真实姓名拼音或长期用的英文 ID。

密码建议让浏览器自动生成强密码，存进密码管理器。自己想出来的密码大概率跟别处重复，一处泄露全网遭殃。

填完解谜验证，GitHub 会往你邮箱发一封验证邮件，里面有一个 8 位数字的验证码。复制粘贴回来验证，注册就完成了。



# 开双重认证

注册完第一件事，开 2FA 双重认证。

GitHub 从 2023 年起强制要求所有做过代码贡献的账号开 2FA。只要你上传过文件、提过 Issue、发过 PR，90 天内必须开，不然账号会被限制。

路径是，点右上角头像，选 Settings，左侧菜单点 Password and authentication，找到 Two-factor authentication，点 Enable。

![](https://feishu.cn/file/D6JmbSshtoI63Wxpx0ScuWRonQh)

三种方式里推荐 Authenticator app。手机上下载 Google Authenticator，扫码绑定后每次登录除了密码还要输入 App 里 6 位动态码。

![](https://feishu.cn/file/D2hlb4A1do3jhixjmrGcgnRanGd)

绑定完成后 GitHub 会给你 16 个恢复码。

恢复码必须存好。手机丢了、App 删了，这 16 个码是唯一的救命钥匙。

复制进密码管理器或打印出来锁抽屉里。

![](https://feishu.cn/file/T5atbDhuToweA1xCx6Tclex7ngb)

# 创建仓库

有了账号，第一件事是建一个自己的仓库。仓库是 GitHub 上装代码的最小单位，一个项目一个仓库。

右上角点加号图标，选 New repository。进入新建页面，填几项： 

![](https://feishu.cn/file/Tehdbc6Boo2BlDx0HZVc3mDan8g)

仓库名，全小写英文，单词之间用连字符。比如 my-first-project，别用中文。

Description 描述，一句话说清楚这个仓库是干什么的。可填可不填，建议填上，以后自己回来看一眼就懂。

Public 还是 Private。公开仓库任何人都能看到你的代码，私有仓库只有你和你邀请的人能看到。免费账号两种都能无限建，放心选。

下面三个初始化选项。 Add a README file 勾上，这是仓库的脸面，打开仓库第一眼看到的就是它。Add .gitignore 选 None，后面再说。Choose a license 如果不打算开源给别人用，可以不选。

点绿色的 Create repository 按钮，仓库就建好了。现在里面只有一个 README.md 文件，后面把本地代码推上来就会慢慢充实。老王建新仓库时 README 一定勾上，没 README 的仓库别人点进来就走，根本不会细看。

![](https://feishu.cn/file/LNUAbK4HcoAhkuxCnpvcVrTwn1c)

# 搜索项目

GitHub 上有几亿个仓库，搜到你要的东西是第一个实际技能。

顶部搜索栏直接打字就能搜。比如输入 OpenClaw，回车。搜索结果页左边有一列类型筛选，切到 Repositories 看仓库，切到 Code 看代码内容。 

![](https://feishu.cn/file/BGSIbp3gGoPVNOxteYhcdbyznLg)

几个最常用的限定符，组合起来能精确到离谱的程度：

- language:python，只搜 Python 项目
- stars:>1000，只要 Star 数超过一千的热门项目
- pushed:>2026-01-01，今年还在更新的活跃项目
- in:name，关键词出现在仓库名里

组合起来用。想找 Python 写的、Star 过五千、今年还活跃的机器学习项目，搜索框里打：machine learning language:python stars:>5000 pushed:>2026-01-01。

老王日常找开源方案、对比竞品、翻参考实现，全靠这套搜索语法。比在搜索引擎里搜某某项目推荐快一个数量级，出来的结果也干净，没有 SEO 灌水文章夹在中间。

![](https://feishu.cn/file/P58SbMSLaoB7RHxE2HdcPkkWnMd)

# 读懂一个仓库

GitHub 上一个项目就是一个仓库，英文 Repository。打开任意一个仓库页面，从上到下，每个区域和按钮都讲清楚。

![](https://feishu.cn/file/WS2Hb3h7loXPwfx55Vtcd10XnKb)

仓库名，格式是 用户名 / 仓库名，点用户名能跳到那个人主页。

旁边有一个小标签标注 Public 还是 Private，公开还是私有。

![](https://feishu.cn/file/FHAQbYqfCoyjiuxqCYVczQsHn9e)

再往右三个按钮： 

![](https://feishu.cn/file/R8pMbuGFcoXveixqrm3ca7j1nle)

Star，收藏加点赞。点了之后仓库进你的收藏夹，头像菜单的 Your stars 里能找到。Star 数越高说明项目越受欢迎，找开源项目时先看这个数字。

Fork，把整个仓库复制一份到你自己的账号下。复制完是你的独立副本，随便改不影响原项目。

Watch，订阅更新通知。点了之后这个仓库有新的 Issue、PR、版本发布，你都会收到通知。不需要通知就别点，默认就好。

横栏下面一排标签页。日常只用前三个。

再者，

Code，默认页，看代码和文件的地方。所有操作都在这。 

![](https://feishu.cn/file/QYOob31r3opgRyxc0omcQYs3nFe)

Issues，工单区。提 bug、提需求、问怎么用，都在这发帖。对开源项目有问题，先来这搜一下有没有人问过。

Pull requests，合并请求区。别人想给这个项目贡献代码，就在这里提交改动等审批。用 Fork 和 PR 给开源项目贡献代码时才会用到。

后面 Actions、Projects、Wiki、Security、Insights、Settings 六个标签，上手第一周用不到，不用管。

Code 标签页是整个仓库最核心的地方，分左中右三栏。

![](https://feishu.cn/file/GLokbkFKOoB860xbO9PccK20nhe)

左上角有一个分支下拉框，默认显示 main。main 就是主分支，第一版代码在这。有些项目会有 dev、develop 等分支，不用管，只看 main 就行。

中间文件列表，跟电脑上的文件夹一模一样。点文件夹进去，点文件名看代码。每个文件名旁边有一行小字显示最后修改时间和说明，点进去看那次具体改了哪些代码，红色行是删掉的，绿色行是新增的。

文件列表上方绿色 Code 按钮，这就是下载代码的入口。

文件列表下方是 README.md，打开仓库自动渲染在最显眼的位置。README 是作者写的项目说明书，一般包括四块：项目是什么、怎么安装、怎么用、几个示例。 看一个陌生项目，先看 README，就知道这个仓库值不值得细看了。

右侧 About 信息栏，显示项目简介、主要编程语言、Star 数、Fork 数。往下拉有 Releases 版本发布区，如果作者发过正式版本，这里会有版本号和下载包。想下载稳定版本不用克隆整个仓库，来 Releases 找对应的压缩包就行。

如果 README 里没写怎么装，这个项目大概率没打算给别人用，或者维护者没顾上写文档。换个同类型有 README 的项目会更省时间。



# Issues 工单系统

仓库顶部的 Issues 标签，可以理解为这个项目的留言板加任务系统加 bug 报告中心。 

![](https://feishu.cn/file/OvtibfkkOo955lxFnmYcXTEknEb)

任何人都能在这里提 Issue，用来报告 bug、提议新功能、问怎么用。点 New issue 按钮，写标题和正文，提交就行。

给开源项目提 Issue 之前做两件事：先在 Issues 页面搜一下有没有人提过同样的问题，重复的 Issue 维护者直接关掉。再看仓库根目录有没有 CONTRIBUTING.md 或 ISSUE\\\_TEMPLATE，按对方要求的格式填。



# 本地 Git 操作

不需要装 Git，不需要背命令。打开你的 AI 编程工具（Cursor、Copilot、Claude Code、Trae 都行），直接跟它说话就行。下面是要对它说的几句话。

把项目变成 Git 仓库时，对 Agent 说：帮我初始化 Git 仓库。

![](https://feishu.cn/file/SpFTb5UVOoETAIxbJVqch6pIncc)

下载别人的仓库，把仓库地址复制下来，对 Agent 说：帮我把这个仓库克隆到本地 [github.com/xxx/xxx](https://github.com/xxx/xxx)。

改完代码提交，对 Agent 说：提交所有改动，说明是：修复了登录页白屏。

推到 GitHub，对 Agent 说：推送到 GitHub。

拉取远端更新，对 Agent 说：拉一下最新代码。

本地已有代码想关联 GitHub 上刚建的空仓库，对 Agent 说：帮我把这个项目关联到 GitHub 上的 xxx 仓库，然后推送上去。

就这六句话。Agent 在后台自动执行一切，包括第一次推送时自动配好 SSH Key，你不用管它具体做了什么。 

![](https://feishu.cn/file/MFyPbCRA6og5FVxu59gcY4BAngd)

# 部署上线

代码推到 GitHub 之后，怎么让别人在浏览器里看到你的作品。跟 Agent 说就行。

静态 HTML 页面走 GitHub Pages，对 Agent 说：帮我把这个仓库部署到 GitHub Pages。三十秒后 Agent 给你一个 你的用户名.[github.io/](https://github.io/)仓库名 的公开地址，任何人打开就能看。

React、Vue、Next.js 这类前端框架项目走 Vercel，对 Agent 说：帮我把这个项目部署到 Vercel。Agent 会自动关联 GitHub 仓库、自动 build、自动分配一个

域名。以后每次 git push，Vercel 自动重新部署。免费套餐个人项目够用。

老王自己的博客就是 GitHub Pages 托管的，1 年没花过一分钱，加载速度比国内很多付费虚拟主机还快。

适合放的：个人作品集、博客、开源项目文档站。不适合的：需要后端数据库的应用、需要登录注册的系统。

![](https://feishu.cn/file/DsI5bEBfhoorzxxN0MrcH5Mqnmg)

# Fork 复制仓库

GitHub 最核心的协作机制就这两个动作。单独讲，因为这是开源协作的基础。

进任何一个公开仓库，右上角有一个 Fork 按钮。点了之后，GitHub 会把整个仓库完整复制一份到你自己的账号下，你拥有这个副本的完全控制权。

Fork 出来的仓库可以随便改，不影响原项目。原作者更新了新代码，你这边不会自动同步，想同步的话点一下 Sync fork。

什么时候 Fork？想给别人的项目贡献代码，先 Fork 到自己的账号下，在自己副本里改，改完发起 Pull Request 申请合并回原项目。或者想基于别人的代码改一个自己的版本。



# Pull Request 合并请求

PR 是开源协作的关键一步。流程是：

先 Fork 目标项目到自己的账号下。用 git clone 把自己的 Fork 仓库拉到本地。在本地改代码，add、commit、push 推上去。

打开自己 Fork 仓库的 GitHub 页面，顶部会出现黄色提示条，问你要不要发起 Compare and pull request。点了之后填写标题和描述，说清楚自己改了什么、为什么这么改，然后点 Create pull request。

提交之后，原项目的维护者会收到通知。他来看你的代码改动，可能会留言让你改几处，也可能直接点 Merge 合并。如果他点了合并，你的代码就正式进入原项目了。

![](https://feishu.cn/file/DlpgbMu7Oob5IXx7kXNc9YSCnld)

# 再说一些开源项目

GitHub 上托管着全球几乎所有重要的开源项目。下面列几个国内大厂和社区的代表项目。这些项目本身就是最好的学习资源，打开看它们的代码结构、README 写法、Issue 管理方式，比一篇一篇翻教程快得多。

阿里巴巴通义千问 Qwen，阿里开源的大语言模型系列，从 7B 到 72B 参数全量开放，GitHub 上模型权重和训练代码全部可下载。地址：[github.com/QwenLM/Qwen](https://github.com/QwenLM/Qwen)

![](https://feishu.cn/file/TzRybe6n3o2JsfxEAQsc09Q1nKc)

飞书 ，飞书官方开源的命令行工具，覆盖消息、日历、文档、邮箱、会议等 11 个业务域，还带了 19 项 AI Agent Skills。发布不到两个月 GitHub Star 破万。

 

![](https://feishu.cn/file/HYgzb90ZUoYWEhxcUB4coHsankh)

说两个有意思的。

Apollo 11 登月源代码，1969 年阿波罗 11 号制导计算机的原始代码，14.5 万行，GitHub 上 3 万多 Star。打开那个仓库，看到的是五十多年前送人类上月球的第一手工程资料，代码注释里甚至能看到那个年代工程师的英文俚语。

地址：[github.com/chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11)

![](https://feishu.cn/file/UEJnb9VPBoWM2Gx0mJDcgksdnAJ)

HowToCook，程序员做饭指南，80K Star。微软工程师居家隔离时写的，把菜谱按程序员思维结构化：每道菜标难度等级、材料精确到克、步骤拆成条件分支。不含一行代码，但可能是 GitHub 上最实用的非代码仓库。

地址：[github.com/Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook)

![](https://feishu.cn/file/BYwGbnAl7oj6npx4kAQcK3JanLv)

English-level-up-tips，46K Star。作者大四一学期过了 26 门考试，高考江苏卷英语加语文双科省第一。7 层结构从基础认知到 AI 工具，每层独立，挑着抄都行。 地址：[github.com/byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips)

看这些项目不需要完全看懂代码。打开每个仓库先看 README，了解项目是干什么的。再看文件结构，看它是怎么组织的。点几个核心文件的代码看一看，感受一下真实项目的代码长什么样。这种浏览本身就是最好的学习。

到这一步，你已经能注册账号、搜索项目、读懂仓库、用 Git 在本地和远端之间同步代码、把网站部署上线、给开源项目发 PR。GitHub 开发够用的全套操作都在这里。

剩下的就一件事了，打开 GitHub，搜一个你感兴趣的项目，点进去看它的 README 和文件结构。再用 git clone 拉到本地，改点东西，push 上去。踩过一次完整流程，这些知识才是你的。