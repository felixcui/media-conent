# DeepSeek Harness 首发实测 + 入门教程，夯爆了！对不起梁神我错了。。

**作者**: 程序员鱼皮

**来源**: https://mp.weixin.qq.com/s/Rv3ww-67fZrU2hNQeCp8oQ

---

## 摘要

这篇文章我会从安装开始，手把手带你体验 DeepSeek Harness 的核心玩法。小白可懂，建议收藏~ 一、DeepSeek Harness 是什么。程序员鱼皮 程序员鱼皮 大家好，我是程序员鱼皮。昨天注定是载入史册的魔幻一天，DeepSeek 同时放了两个大招。先是 DeepSeek V4 Pro 正式版上线，紧接着万众瞩目的 DeepSeek Harness 开源。

---

## 正文

程序员鱼皮 程序员鱼皮

在小说阅读器读本章

去阅读

大家好，我是程序员鱼皮。

昨天注定是载入史册的魔幻一天，DeepSeek 同时放了两个大招！

先是 DeepSeek V4 Pro 正式版上线，紧接着万众瞩目的 DeepSeek Harness 开源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GnF7jUvPyKKp5jJzT3icnm9IhG8HQuj0iaaNYzk0VBBWImtkxs5QnKAMb1PrMyOeK87roQkPFMs4ztKaiaZJQnO3Y4edPaMUItlo/640?wx_fmt=png&from=appmsg)

**炸裂！炸裂！炸裂！**

DeepSeek Harness 开源的 GitHub 仓库 上线不到 1 天，就冲到了 7 万多 Star，AI 届的顶流果然名不虚传。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GTd87EL0ACyTVHxHTBpqSAzzgrsG4Mic7q2jEpnjLPt7TfK2OuJOkeibs4FYBsvHKzlicYx9rRbCSrWNevkomBaux2p1ANmregOU/640?wx_fmt=png&from=appmsg)

这下搞不好 Codex、Claude Code、Cursor 都要 **梁乐** 。。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1HkP5KCBvJ2ehibT4nB6s3nQ2K7xCW3eK2OwFSQ1OLUbAuiaowzLicCE5YJGCV2ibuy5gHMNAnFQyZZuVk1luE8XHBeeB2EaicGefLw/640?wx_fmt=jpeg&from=appmsg)

这篇文章我会从安装开始，手把手带你体验 DeepSeek Harness 的核心玩法。

小白可懂，建议收藏~

## 一、DeepSeek Harness 是什么？

Harness 这个词翻译过来就是「驾驭」，如果把 AI 模型比作一匹马，那 Harness 就是你驾驭 AI 模型这匹马所需要的一切工程。

所谓 Harness 工程，就是研究怎么让 AI 模型这匹马跑得更快、更稳，顺利完成任务。

你给 AI 写的项目规则文件、配置的各种工具、安排的任务拆分和执行顺序、设计的测试检查流程，这‌些统统都算 Harness。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EEC1pJfR1XXVTyxeZvklaaEO8BsWWBcOet8piaicEy5duicTtQrd4D4Iu0uNXIUk2xQTJo6RaORhywibmDok3FB22PYKcNiaiaB30FE/640?wx_fmt=png&from=appmsg)

有一个很精妙的公式： **Agent = Model + Harness**

模型负责思考和生成，Harness 负责把这些能力接入文件系统、终端、网页、工具链，让 AI 真正能在现实环境里干活。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1ETNKu6FohQERohWcte1SvZ9k4Kic6gbmZx2NiciarKBiaCIwx8Ib1t61BNjEez8AW3Ox2caxLPLzjHOqpAsC8DGA8A6Nqq5sZibIJ0/640?wx_fmt=png&from=appmsg)

之前 DeepSeek 只开源了模型这一半，Harness 一直没动静，这次终于补齐了。

你可以把 DeepSeek Harness 理解成一个 **可以高度定制的 AI 编程工具** ，对标 Claude Code 和 Codex。

但它的野心比这些工具更大，不只是一个编程 Agent，而是一套可配置、可重组的 Agent 运行环境，官方口号是「一切皆插件」。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FImSB0bZHsrYo7QoZJ5tdlg7y9CcNQ2dSP6SZVzqx2KkbGk6gJq2kY4F5oINj98vJKzFp8FKNRWpib6icu5EdwHGVQRV7qIenAg/640?wx_fmt=png&from=appmsg)

看到这里，你已经超过了 50% 的同学。

接下来只需要 1 分钟，你就能把它装到自己电脑上。

## 二、安装

安装 DeepSeek Harness 真的非常简单，进入到 DeepSeek Harness 官网 。

你会看到一行安装命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FRkNH35RbbjtQxJibZ31WiaicQsXg6Llj3VmCYcA6l8pd1HhFa0YeCNa91icUAeaPBNoHicQoDWOyk18pj9UykG8UNUbkuOtlDIpyM/640?wx_fmt=png&from=appmsg)

在执行这行命令之前，首先要确保你的电脑已经安装了 Node.js 环境，没有的话去 Node 官网 下载安装包，傻瓜式安装就行。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FfOZvKiaoSWVZwOOyyriazN0bLxBdWtYZYh7pnXD1XJwJBGyKVhfnGTu9QrhoJxBllDV5ouM1VTzHdLOoEhuZICrd1IicjlHSYYQ/640?wx_fmt=png&from=appmsg)

有了环境后，复制这行命令，然后打开你电脑上的终端，输入这行命令并执行：

```
npx @deepseek-ai/dsh web
```

稍等一会儿，你会看到终端输出了一个网址，打开它就能进入到 DeepSeek Harness 的 Web 界面。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EzIxbSW6q82OvoWMFtgQ4Y3ZNaafODueuqEiaxmnxA6yNZm3NeUbex7gUS0Nyiajicuia6icZEicyDziaHsL7xQj70Y9jica1kbE6ZngI/640?wx_fmt=png&from=appmsg)

第一次使用时，需要填入 DeepSeek 的 API Key：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1F4zgXfuQ4InG8hpUSH1CdrMiaRDKMfvuF511HwwR5jqYv8tY2wkickjsjtTNRdqGVLUksypS5FeQfQQ7eF3VqRvtyx1AXpvmib8M/640?wx_fmt=png&from=appmsg)

到 DeepSeek 开放平台 创建一个 API Key，注意不要泄露，把得到的 Key 复制粘贴过来就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FKrr22B2jwIBrsl7VzlVQ67jSBRQG0gZ6qia5aaEnfiaqhyPviajW1hiaPLFvF7N1X0Q6JBxD5DpOpUeice3ibZz3OxDibSyfqo6ZRMc/640?wx_fmt=png&from=appmsg)

到这里，DeepSeek Harness 就安装成功了，是不是很简单？

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Gia7U5l8ZvKicwNZV7otHpicFAlAWURvHS6vtHc1RZFQ3mNB6VNLkmJ67icZclOibrsDWYHjIazMlDwoVPfbaLW2icphmEE5NuEdEJ4/640?wx_fmt=png&from=appmsg)

看到这里，你已经超过了 60% 的同学，接下来我带大家实战体验一下它的能力。

## 三、Harness 实战

进入 Web 界面后，选择一个你想让 AI 操作的项目文件夹，就可以正式开始干活了。

可以在对话框中选择模型、以及模型的推理等级，还能设置 Agent 对文件系统和终端的操作权限，按需调整就好。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EziblJqTKDQkaiax3WhMhwkeUcjjdUSsfJqNb7ZUicGTHsPYcQ7TqVfYibPNnuBibXic7UjWOY2g9Wibic7SqDH82JEvibQbcG57VqFePI/640?wx_fmt=png&from=appmsg)

默认使用的是「标准模式」，它具备了一个 AI 编程工具应有的全部能力，大多数情况下用这个就够了，后面我会详细介绍各种模式的区别。

你看，是不是跟 Codex 这种 AI 编程工具很像？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1ENbywn3VCVWWRHlVZDnXzotQ76b00H9bds3bFibpRpzncjuxtobfI0HJYSV0YbehIiazgT9ckyda2hvFkYxqrfhiblBS0Gxibh2z4/640?wx_fmt=png&from=appmsg)

没错，你就把它当成国产版的 Codex 来用就好了，AI 编程、自动化办公等任务，都能搞定。

下面我们跑几个任务试试看。

### 任务 1、分析代码仓库，绘制架构图

第一个任务，让 DeepSeek Harness 分析它自己的源码仓库，绘制一张傻子都能看懂的架构图。

DeepSeek Harness 的代码仓库还挺大的，里面模块也多，用来测试 AI 的代码理解能力刚好合适。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1ExlHoqQlVbkXHiabic6fEiafXWR4GecRwkE0N0zyDa8YRHDicMsydfS0NO0c4cOEpXEILfPzxouyqzI7tkcMHCF1LUmyUpVwicBvv0/640?wx_fmt=png&from=appmsg)

给 AI 发送下列提示词：

```
分析当前项目的代码仓库结构，绘制一张清晰的架构图。
要求用 Mermaid 语法输出，让完全不懂代码的人也能一眼看明白各模块的关系。
```

可以看到 AI 开始自动读取文件、分析项目结构，执行速度非常快，而且每一步在做什么都清晰地展示在界面上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1E8Cf24yVgkcoozgG7ph2YdmFkgU522r5DibicSNZlURwOHnH4hWOa9PPhyrBv885r4eWwph3exEMAOUycbAAWGsaO5yDTE2IPdc/640?wx_fmt=png&from=appmsg)

很快任务完成了，能够看到 AI 输出了 Mermaid 文本绘图语法，不过 DeepSeek Harness 默认是不会把这块渲染成图形的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EKTcnDWtLUXLkJZicrX6x7Wq1A5siaztq3c5G3T25vYF0ju1cLkYSXLCAhqfDI9ibEU7QjjdBGGLzZMT7LiaoiabSV37raoJOe0Qcg/640?wx_fmt=png&from=appmsg)

我要把这段代码复制到 Mermaid 渲染工具中，可以看到完整的架构图，虽然效果中规中矩吧，但内容还是比较完整的。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EdtK5nj6mn76I1ovReS0OXeicFyL5o1gywMP879ibzZrValoKaeVrmJAQdQmxd9jDxTHbIvcKZq6SPjPAzDF2g3vcNEV1xe7yTk/640?wx_fmt=png&from=appmsg)

你可以在下方看到任务消耗的 Tokens、当前的上下文占用、以及整个对话的 Tokens 消耗信息。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HutZxSqRWylO81Zrq8vWjiaJKgTLia4I2HVaNNubweKFZGzwDhURAkfexzjxMgYJ7JqXqZ6p2zlQYWZNxdl3gYP2S631dMqmqO4/640?wx_fmt=png&from=appmsg)

你还可以进入上方的「轨迹」面板，清晰地查看到整个对话中每一次的对话和工具调用记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HkGxuQH7xLzibD4mNbjsf6jElVJKVLEmDN2ADyrciaGuMhv4aOoe5ibIkUc4QDxsedDibsVIZqvdQwjxMCXrIp6jpmG3fE6tMRM1s/640?wx_fmt=png&from=appmsg)

这是 DeepSeek Harness 的特色，让每一次运行都有迹可循。

### 任务 2、开发一个知识讲解网站

第二个任务，让它从零开发一个用交互式动画讲解知识的网站。

要讲解的知识点是「注意力残差」，跟我之前测评 Codex + DeepSeek V4 Pro 的时候用的是一模一样的提示词。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EiaFfkHgXeics01kXpwalO6QShHmt8j1jRC1H3ibmbdFvcj2PhjqthUkcdQ18fnhL6as0enzrgsDKwEs6vT0MwQ72UnMQes2NO3Y/640?wx_fmt=png&from=appmsg)

大概过了 20 分钟，AI 完成了任务，这个速度确实不算快，主要的时间花在了 AI 的自检上。

值得关注的是，本次任务的缓存命中率达到了 99%，也就是说绝大多数的费用都按缓存来计算，实际花费极低，这点很厉害啊！

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HrCBeJdibDrudfENsJdfnuiazjTHI27mItxHaajcukogibFFpJtwW4eTcqltWBkf9r72Gib1ibKxLI92xQnLj0YkJ1pTZFehYicEWrk/640?wx_fmt=png&from=appmsg)

看下效果，不错，动画还是很生动的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HxvwibnESOsZibR2m1elic3pe0jgXJuaFLmwWeTqrR5SZseVLkhCSh5JSo7gKGNseR4RiaOLMbaKiayibtvst2TIGZSQJQDOke1Ozxw/640?wx_fmt=png&from=appmsg)

而且点线之间的连接非常准确：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EHgqqOUnmvSdQXyGeq81Tu4xj3nttsPgnE1S8mAoqQNrLttEEmHRCHSUp5x7P8ruJ8nRAeq8mcNict3JCphC7gUhHXwiaURLXUw/640?wx_fmt=png&from=appmsg)

更让我惊喜的是，跟之前 Claude Opus 5 开发的效果一样，这次 DeepSeek 开发的版本也提供了总结和小测验功能，让整个知识讲解更加全面了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HSIqXxnZfjjHHS3daibpMOh8ticOOJvNibnMEshpE0k8rK3xInJeGGj0DUUMSdqKAg9S5RGbFTRIgrHHO8su43CU9yLxnA7xOGEY/640?wx_fmt=png&from=appmsg)

整体来看，相比于我之前用 DeepSeek V4 Pro + Codex 跑的效果要好多了！

之前的版本连线都对不齐，相信你们能明显感受到区别。

![DeepSeek V4 Pro + Codex 的版本](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Eiauhx2v6S3w1tHsgjJtaAia4D2ca70FibSwSPEyxGaW4lAXCeRy2rtOHBfy8NcmuibRsu33oTRYQ9Bw7MXjlZQ8AgEicrW3vqfEpM/640?wx_fmt=png&from=appmsg)

DeepSeek V4 Pro + Codex 的版本

单看这一个例子，我真有种感觉 DeepSeek V4 Pro 可以对标 Claude 了，看来 Harness 真的很重要。

### 任务 3、开发一个 3D 游戏

第三个任务难度升级，让它开发一个 3D 网页小游戏。

这次做的是千万元以内最好的玩具「竹知了」，不过这次比之前测评的 2D 版本复杂多了，还要支持摄像头识别手势来控制竹知了旋转。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GQsukvfxXI4y4xypKzpLx1mgBM2icnELPtFz49ZB08VjluiaSialPtSejTWkWtUFWumOibsBCf78lFrzGqeLRw875xzjq6g51fJgQ/640?wx_fmt=png&from=appmsg)

可以看到 AI 在开发过程中，会自己检查验证程序是否正常：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GOOWUpXCwsibf15zKwMv7OAvofubCAmJv5IubkYiaSldSqfovgsAU74icNzqHbybAaza7xewpHFckkIWM1YWIP87lmF6feq8L2Mg/640?wx_fmt=png&from=appmsg)

这次跑了将近 40 分钟，AI 完成了任务，缓存命中率竟然接近 100%！

我 chovy，真心强啊！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1E3r6nJzazElVGOxVTGEkP9gvbdcbnHw9ZtxEO25nk9V4DwEa5lDfFecmys8yoUWSLVSPuWGWCcbkj1olxy9HQB6pYK48MdjeM/640?wx_fmt=png&from=appmsg)

看下成品效果，还是不错的吧，可以通过鼠标拖拽来旋转角度：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FFiaicwbPef86jiamBSpoX7jFbkpSRnoGLMapWyzex6QcFWfSPoVYczFvG95uurqeMrZ4qSYAeCRqZgRFF9IJRM0dHyxJj4fyIIs/640?wx_fmt=png&from=appmsg)

按住竹签来回移动鼠标就可以控制竹知了旋转，注意看图片中的影子，细节做的非常好！

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GnXEukacJ9pgSicAwMCzFysF7c1HqksX97sggu2gSXriaKolIkKqoxcgNlB06OibM4KHpqBnJsL5qJ2AfxVRicO6ooJ9ZSeuMfKEE/640?wx_fmt=png&from=appmsg)

而且还可以开启摄像头，通过搓手来控制竹知了旋转，这个交互体验非常有趣：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GvARhWR4ZEx9XdKwsOxe0ooNk6bYtZJpHdxpjFvctIgbzezgsfaiaNbPMnpjZgUU6pLBWEjjuVF1SkAm2ITjW3ia13Xh5iaESqsE/640?wx_fmt=png&from=appmsg)

整体来说，功能都是正常的，程序没有明显的问题，细节做的也很到位，我的评价是 **顶级** 。

相比之前用 DeepSeek V4 Pro + Codex 搓的 2D 版本强了太多了：

![之前 DeepSeek V4 Pro + Codex 做的 2D 版本](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GpysQzAqvXBVSbt3VGibyr4S6Ap18hUUQcZDeA6TRcZuFHia4OZ6wqZYoKC48CX6bW57DicuMSzWqCIBUw8r2zibW9tBsW4oiaM5NQ/640?wx_fmt=png&from=appmsg)

之前 DeepSeek V4 Pro + Codex 做的 2D 版本

### 任务 4、开发全栈 AI 应用

最后一个任务，让它开发一个内置 AI 大模型调用能力的全栈应用「AI 网页 PPT 生成器」。

用户粘贴一段长文案进去，后端调用 DeepSeek 大模型把文案拆解成多页 PPT，前端渲染成可以全屏演示的网页 PPT。

这次我特意在提示词里让 AI 自己从我电脑上获取 DeepSeek 的 API Key，看看它能不能自己搞定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EJ6vTRwqsclnLtboud7ZmDmBgfoxB0BSkethtzibmLibforuvK1LAJPIn3mIdGXDs9oib5BmJEpYTIKkjeyZQ7dgHGaphWXt0Pg4/640?wx_fmt=png&from=appmsg)

执行过程中，AI 可能会向你确认权限，比如要不要允许读取某个文件、要不要执行某条命令，安全性这块还是挺到位的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Hy4RHIzUSIrYMgNw0GxGLwQzsSCVy9ReR5glOYVD2jIap3aBcXiarNWCmV3yiciadMbvQz66vDibnEibBibEWXCeA3FmLj4DIGf7wUE/640?wx_fmt=png&from=appmsg)

大概半小时左右，AI 完成了任务，来看下效果。

这个界面风格还可以哈，也是有点儿科技感的，来粘贴一段要制作 PPT 的文章。

哦，这里有惊喜！我们可以自己定义生成 PPT 的风格，还可以选择是否开启推理模式。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HJdr9QK9Ah5amD08gA4FkIhTlno8clTEUwkWsHRtCtuXIvibNl03SGv5UEU6spLVuZUDWpZWP9rP5ZFhd3ibia4Wa1nxExJDqk8c/640?wx_fmt=png&from=appmsg)

然后点击生成 PPT。

生成过程中，是可以实时查看到生成进度和输出信息的，这个交互感比之前的老版本好太多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1E7XRAjJnBypdCQ3JBq3p3Zicn5A4k3dyUD4w0iaQ6BtyIgeJgQzI3ddVbCmmEMl54nWyG55c5Rjz16JPhnTRh4d1FIujnwmzgico/640?wx_fmt=png&from=appmsg)

而且生成速度很快，看起来效果不错，点击全屏查看。

哇，这次生成的 PPT 充满了科技感，而且布局也挺合理的，主次分明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GZURdHvdp8iaMicy9KMRb9mcXNqbbvk7iahEls6ORZ9GZ7SqMYxqqibRhgxs9AwrOT9uiamoZA4hojBcLicW5Fs1NqTSpkFpb5yPwu0/640?wx_fmt=png&from=appmsg)

相比之前用 DeepSeek V4 Pro + Codex 做出来的版本好多了，布局更加合理，配色也更优雅。

![之前 DeepSeek V4 Pro + Codex 做的 PPT](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Hiaoh2k4kG2BaAMbAibjDcIeIdBQpE60oJWZgBh37SH8X8PQFehT39AtwibibLBficOCiaNcoTTPbdcic7670WFPLP5PlIZuxic6iag51Y/640?wx_fmt=png&from=appmsg)

之前 DeepSeek V4 Pro + Codex 做的 PPT

你还可以切换几种主题配色，也都是比较经典的风格了。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EP9bdVHTkkm0L8Cuv3VWMFgoLnIvCrmbv2GVXaPn10kSaTZBic0Fia3JZOIU0DFmx3bjBXeIHeAMR5PG78ibb55562C49Xvpv7To/640?wx_fmt=png&from=appmsg)

看到这次做出来的版本，我觉得真的可以和 Claude Opus 5 媲美了，给到顶级。

![Claude Opus 5 做的 PPT 工具](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HxFJI1Pua0BAusI6mspfJiadibPcKEtcMk5OnAWJVh5EKyE7nQaTkxbjuiaOq4bVsM8lHFTXwtP1MicdvsoCHbwzibCSgNOickqicrWE/640?wx_fmt=png&from=appmsg)

Claude Opus 5 做的 PPT 工具

### 实测感受

几个任务跑下来，DeepSeek Harness 给我的感受是速度还行。优点是缓存命中率很高，而且执行过程非常清晰透明。你能看到 AI 每一步在做什么、调用了哪些工具、读了哪些文件，不像有些工具暗箱操作，辜负用户的信任。

单从我这几次测试来看，DeepSeek V4 Pro 配合自家 Harness 的 AI 编程能力确实可以和 Claude Opus 5 对标了，官方那个只差 0.1 的跑分诚不欺我。

**看来用 DeepSeek 模型，还是得用自家的 Harness 工具啊。**

![deepseek v4 pro 跑分图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1Gj0qStWgt1oSeOhpib35Xgz8q2eoWUEBIG9zQQI55evmkELvUy0GfyEwjAxle430DmYZJaA3EkC260iaEiaia6G8e3VWKqJKetdX0/640?wx_fmt=jpeg&from=appmsg)

deepseek v4 pro 跑分图

再说下费用，大家猜猜这几个任务跑下来花了多少钱？

**答案是不到 5 块钱！**

因为缓存命中率基本都在 99% 以上，实际花费极低。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HZBX0lZ4YHTrdhBm0W060ms9MLrpRNKzibtNb3awPI3PpGbMeoia4UvvVYJnC4oDEicLlBRnfJoX7CicibicictVAFNwrUISU4dSFO4Y/640?wx_fmt=png&from=appmsg)

不过要提醒大家的是，DeepSeek 已经宣布 8 月 17 日起涨价，而且涨了好几倍。

![DeepSeek 涨价](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1FKyAJiax86HGtziaVrceibGfhX0vBljz9UTIlsRR7r3vfoPoM5fNRDvMiaQk0MT9pzI6GAYE2ttVsH4VeaVZrhhM28UU0Lrdicbnvk/640?wx_fmt=jpeg&from=appmsg)

DeepSeek 涨价

但即便是涨价之后，跟 Claude 比起来还是便宜很多的，而且缓存命中的价格依然非常低。

总的来说，自己的模型配自己的 Harness 工具，真的强。

我收回之前对梁子的失望，梁神受我一拜！

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GaCMogTYHGysevD8PFX3k82hBHIn9K3mt1DOqbucdiaI5ZP4JQsY1hRibKfjBP3hoPktPiaBLXdVxvTibthPES6WnKTWsDTtRQ040/640?wx_fmt=png&from=appmsg)

看到这里，你已经超过了 70% 的同学。

接下来我们了解一下 DeepSeek Harness 的几种运行模式，看看它还有什么用法。

## 四、4 种运行模式

DeepSeek Harness 提供了四种运行模式，适配不同的使用场景。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H6arfjCymia9m0Xx3vboVoW8sibDAfkrwT6Aia2kZe18ulq2b8ABZL7Ha5EJFbGDQm6LvC6hfDkic4LRdo820FL4u0jddwZVzWZoo/640?wx_fmt=png&from=appmsg)

**标准模式** 就是我们前面实战一直在用的那个。它加载了完整的工具组合，包括文件编辑、Shell 命令、网页搜索、子 Agent、Skills 技能等等，覆盖了日常开发的所有需求。绝大多数情况下用它就好了。

**极简模式** 只保留了 Bash 和文件编辑这两件最基础的工具，其他能力全部关掉。这个模式主要是官方拿来跑模型基准测试用的，在最小环境下考验模型的纯编程能力，普通用户基本用不到。

**PTC 模式** 全称是「程序化工具调用」。普通模式下 AI 是一步一步调用工具的，每步执行完才能决定下一步做什么。但在 PTC 模式下，模型可以直接生成一段 TypeScript 代码，把多步工具调用串联起来一次性执行完。适合那种步骤很多但逻辑清晰的任务，比如批量重命名文件、跑一整套自动化流程，效率比一步步确认要高得多。

**创造模式** 适合想要开发插件、创造新工具或者定制模式预设的同学。它继承了标准模式的全部能力，在此基础上还让 AI 可以检查当前运行时有哪些插件在跑、在内存里试验新的插件组合、甚至自己创作出一个全新的模式预设。后面我们会用这个模式来开发自己的插件。

总结一下，这四种模式的本质区别就是「当前会话加载了哪些工具插件」。极简模式只留两件工具，标准模式叠满全套能力，创造模式还能让 AI 自己查看和改装当前的插件配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HFBnS1wJF24Xia7g4OD1Nia73g1QTldOdC65bHmvtxYC9mXhIU2KX3wickYFtfHOFyaSFbQSglhsKl4wfl0Wzv6YMiadctWyb2hFU/640?wx_fmt=png&from=appmsg)

看到这里，你已经超过了 80% 的同学，但 DeepSeek Harness 真正让我兴奋的地方才刚刚开始。

## 五、插件

接下来要聊 DeepSeek Harness 跟 Codex、Claude Code 这些工具最大的区别了，就是它的插件系统。

### 一切皆插件

DeepSeek Harness 中的一切皆插件。

模型、工具、技能、会话、沙箱、UI，甚至 Agent 的运行循环本身，都是插件，都可以拔掉换成别的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1EHXZxyhuIho2bJQSic8HNfjmAibZVvoGnSiavYLic61Zibsric5RBnQ1ULZfjwwnY96Ys3cAdZLaWpsjFVwQLzZib4iaSbNK91Sv8cONo/640?wx_fmt=png&from=appmsg)

也就是说，如果你对这个工具哪个地方不满意，随时可以自己替换或者安装插件来扩展，不需要改框架源码。

Codex 和 Claude Code 虽然也有一定的扩展能力，但远没有做到这种级别的开放，DeepSeek Harness 的定制化能力要强得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HH0uHSneSaw77RC3hibp4caVNQ9G4qVWLtqfY3oQ6TXwqeIWAjonEge7Kbw6iaErOnwz4mlic94A2QAspdUyCO47sCkts0JKicIGo/640?wx_fmt=png&from=appmsg)

接下来我先带大家使用社区插件，再带大家开发属于自己的插件。

### 使用社区插件

在 DeepSeek Harness 官网中，点击「社区插件」，就可以看到所有 社区开发的插件 了。

其实就是 GitHub 上打了 `dsh-plugin` 这个主题标签的项目：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EU0YibrgDoZm3ZmUynQ21mb3LbPZzAF1U54alicmtiavBMAsuOLsD0CowxG8wwL6XpTwxBPb8wTLXkm1BswvV0RDwcGHpMXMU724/640?wx_fmt=png&from=appmsg)

不过这个页面的插件又多又杂，我更建议直接去看 GitHub 上的 Awesome 仓库，里面有分类整理好的精选插件列表，每个插件都经过了验证，目前已经收录了 300 多个可安装插件，上线一天就这么多，生态起飞的速度确实夸张。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H7Ql8THkiasbBft5ibEibyLgYJevgrbIoUic6xVFrnFySPSPpoVycyGm4MrAdG6I5eXxapan0s7FdGiae2ObcLCicnb5iaO7zNZ2BOCg/640?wx_fmt=png&from=appmsg)

安装一个社区插件也非常简单，比如我看上了这个鲸鱼娘皮肤美化插件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1H5eVIdMn21p26urTobFecuDaFfCkD020XibMeQaryCGD5cxJKX0CSnQzYDEQcNQiaiaLO83tQfZtJpAjk2Y1bkoASLEB1YaJRwJA/640?wx_fmt=png&from=appmsg)

我只需要进入 DeepSeek Harness 网页中，随便选一个工作目录，然后把插件开源地址提供给 AI，让它帮我装就好了。

想省事的话，可以先把 Agent 的操作权限改为全放开，这样 AI 执行命令的时候就不用你一个个确认了。

```
帮我安装插件 https://github.com/Small-tailqwq/dsh-deep-whale
```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GRL3GsJPuMvjapRV3u5YlQyYEAIyFyKqDeNVlEtGePzQ9d4icSEbOVuVqUwj7ia5Sj55TvsofQjSggjlH2TS6FYUsx3I7hP42Ic/640?wx_fmt=png&from=appmsg)

很快，AI 完成了安装。我们按它说的，打开终端输入命令，重新启动一下 DeepSeek Harness 网页：

```
npx @deepseek-ai/dsh web
```

刷新，怎么样？！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Hgrv3lR5KU66POJrlcMJW3iaPOLwnDZH0KcxmVUGficduiaEvicZ6tP2DOXEbNu2r8enjiaXiaJowafEd50uXGsrghyRaLkaOy0WXoY/640?wx_fmt=png&from=appmsg)

效果不错吧，是不是使用 AI 的念头更强了呢？

如果你不想要这个皮肤了，直接再跟 AI 说一句话，把插件卸载掉就好了：

```
帮我取消掉这个插件，回到最开始的设置
```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GqG43UsgxetjRcYzdhSGOBEhbOoMibf8MR3aib2ibWTrcGJfTCGDbP77h37If3uEzibXZa7YNclFUDclqXqnkebYbVMeQvicia9MEibo/640?wx_fmt=png&from=appmsg)

还有一些比较有意思的皮肤类插件，比如 dsh-deepcel 把界面做成了 Excel 表格的样子，摸鱼神器啊这不是？

![Excel 风格的 deepseek harness](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1H8icxa5IdnZ0eg3ug4U2mb3aDJlbM2FsZBV7W7KgIB9A4ib7yhST0DZSMLibFqGPNN9swyAS9srBdoUsZ5pM98u3FM5TY8hfgiaMY/640?wx_fmt=jpeg&from=appmsg)

Excel 风格的 deepseek harness

还有 dsh-tianshu-tui 直接把 Web 界面换成了 TUI 终端风格：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1FhicuYkXO7YtF7xFOFtqy0HZ6D9ibgQ2iaHWdicOKQIKysOZMP4whMJM6gibykgiaumA8ibUtf3hWrPrV2lQlRic8ruKnxib2y9W0OInfs/640?wx_fmt=jpeg&from=appmsg)

最离谱的是 dsh-ads 这个插件，它给你的 Web 界面加上了 2005 年中文网站风格的侧栏广告、对话内信息流和角落弹窗，纯粹的抽象艺术。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LlSQOKIxJ1GEOp7O4rIEq563CWUib0DQGiaYtLdNCAUPFeibWTh5Bp5T60DuPXzeMDIVwdiaPW5XD5gTI1SLicrUxVVgZJiciceE3Aw163V2gDXzSk/640?wx_fmt=other&from=appmsg)

因为 DeepSeek Harness 本质上就是个跑在浏览器里的 Web 应用嘛，所以定制皮肤这件事非常简单。

不过皮肤插件只是 DeepSeek Harness 生态的冰山一角，翻一翻插件精选列表你会发现，很多真正实用的插件其实都在往成熟的 AI 编程工具产品方向靠拢。

比如 DSH-better-sidebar 优化了侧边栏的交互体验，dsh-at-file 让你可以用 @ 符号快速引用文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GMY6ibDkssQTqP3Ecicbpv9b8S5uiaib4ElXgIriaSqg7zfaFVHbHjY6CTxHr2LibrbDw1fBjmMzHdQE8pibmm9zJI1rLWlEOwrI5OZQ/640?wx_fmt=png&from=appmsg)

我个人最看好的是 modlens 这个插件，它是 DeepSeek Harness 的第一个视觉插件，你把图片粘贴进去，它会帮模型把图片解析成结构化的 JSON 文字信息，包括 OCR 文本、页面布局、语义内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LlSQOKIxJ1GpnjVb41ZfC07GTCDL8qtwUSM8Tx6swCgxu8icDgKDMaPt1SPBPq3VMYxrFjaYKV80YHQ0uibAKKC2iaUPWkzvfC1dNctplmT7Po/640?wx_fmt=jpeg&from=appmsg)

这个插件解决的正是我之前测评时吐槽最多的那个痛点。DeepSeek V4 Pro 是纯文本模型，看不了图，写完页面没办法自己截图检查效果对不对，前端布局有没有错位它全都判断不了，我上次还专门搭了一套 Playwright 脚本来替它做验证。现在社区直接用一个插件把这个短板给补上了。

这些插件补齐了 DeepSeek Harness 在交互细节和能力上的不足，也侧面说明了「一切皆插件」这个架构有多灵活，靠社区自己就能把产品体验补上来，用户也有了更多选择。

### 自己创造插件

光装别人的插件不过瘾，其实自己开发一个插件也很容易，因为可以直接让 AI 帮你写。

切换到「创造模式」，在这个模式下 AI 可以帮你检查当前插件树、试验新插件、最终打包发布。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1FVDozcK65s6ibGVbVapWke6Bn22M5DQCDKV8p3IicIAedkGkarRLvTj2FR0roIsZZU9diajZNcTHVjOlUg3nLnAw3qqKCLq66zB8/640?wx_fmt=png&from=appmsg)

比如我之前给 Codex 装了一个桌宠插件，现在想搬到 DeepSeek Harness 上来。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1HOY8avRvWZUicfCHKn6q4ictm96wicrxx3RiaDvicGKakZAGSAjUvAgliaNPqnOcHaUSVR8LJ8SD6yXOujr9SYTAMEyzvCuZ8BfWSzw/640?wx_fmt=png&from=appmsg)

直接在创造模式下跟 AI 提需求：

```
帮我开发一个 DSH 桌宠插件，在 Web 界面右下角显示一个小宠物。
你需要直接把我本地的 Codex 目录下的 Kun Like 桌宠素材移植过来，不用自己重新设计形象。
它会根据当前 Agent 的工作状态做出不同动作。
当任务完成后，还会发出「你干嘛~」的声音
音频文件路径在：/Users/yupi/Downloads/你干嘛哎呦.mp3
```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1E1eZQ0hG9RZGdlLOMiaJMGzWfLBvO5emAO5uy7zSJpO7vsl5xnaoYdVxHLQbWLh5ibseticaTQ6s1cCye0CVfV6w7Yyq55pHyicJA/640?wx_fmt=png&from=appmsg)

AI 开发好插件之后，会先找你人工审批，确认没问题之后才会正式安装，安全性很有保障。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1EiaJ6epASRuV4RMjmYVib80R0hYUPsNzrdiaCZeAicziaXeGLkRB75BicpIgrwkMXXKWeU2oI2WEtWGlSwYRzJtrSVGbiadSuEnscXBI/640?wx_fmt=png&from=appmsg)

很快开发完成，打篮球的小鸡就出现在屏幕上啦！

随便跟 AI 对话一次，就能听到「你干嘛~哎哟」的声音，可谓提神醒脑、如听仙乐耳暂明~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1GXeuw7BibIUfyfjBSrVic0Gbxrd76zvnW0KIAbXrwlTkrQmAuibg6srQsdekJNRoOOdBTLa5nTsx9cvGCCnAuhRvF9bCgSz0hnoc/640?wx_fmt=png&from=appmsg)

除了桌宠之外，你还可以发挥想象力做各种有意思的插件，比如提醒你定时喝水的健康助手、实时展示模型账户余额的悬浮窗、定制你自己的主题皮肤等等。

如果想把插件分享给其他人，只需要让 AI 通过 GitHub MCP 插件，把代码推送到 GitHub：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1GCoQI3E5Rvpod7icD43xtXKBWYks8VPhePaliclFjwT0nytgibjmyOicNIzZQGT9HmLWaqZmjIlMCDibtA79PSnP4lVMKicLgQWdr5Q/640?wx_fmt=png&from=appmsg)

很快就开源完成了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1FOEj6licTp7G6jibY8bCDqr3JmSy6qlzmUOoKicE3beVViaWeOiatmKicpAXhGv5zR13U55ayaibanxwhvTgGibI39RPcapGTXZTQAGvc/640?wx_fmt=png&from=appmsg)

然后给仓库打上 `dsh-plugin` 的 topic 标签就行了：

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1H4MGYFlSUdycxfeJrxK1vwSGP6OFmxDibZCPIyBKTztJicZSAMFH2VyL4BC74NcmpuibVb5CM8z8b5mAD0PJ3Bib44AzlgeuwicJhs/640?wx_fmt=png&from=appmsg)

AI 甚至帮我给 README 项目介绍文档中添加了效果截图，太贴心了吧！这下大家都可以一起来做小黑子了~

> 开源指路：https://github.com/liyupi/dsh-kun-like-pet

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1Hia7qTUjGtzNYkBTqAj5AIpjKyySBUhiaNMP7dAyhDsFQ849DPyib7Q2ofq5g6icZJhbvOe29g8gAZqwDuFyswPauwqNrwDlCGq5o/640?wx_fmt=png&from=appmsg)

## 最后哔哔

恭喜你，DeepSeek Harness 才发布了一天，你就已经掌握了 DeepSeek Harness 的基础用法，至少超过了 90% 的同学！

时间原因，还有很多 DeepSeek Harness 的进阶玩法我没有展开，比如用命令行模式批量跑任务、接入和切换其他大模型、自定义 Agent 预设来适配不同的工作场景、甚至把它部署到服务器上让整个团队共享等等。

我也正在探索，这些内容我会在下一篇进阶教程里详细讲解，感兴趣的朋友们可以先关注一下。

![](https://mmbiz.qpic.cn/mmbiz_png/LlSQOKIxJ1Gbibr6ficrH99AhlnuYqn0WBO0qWicnBBfKOcQKUnZMhSctEX3zib1vq1REpvWmNTicrtD5HD5XuT0b99BX80hcNjmPJicdtVoAT6X0/640?wx_fmt=png&from=appmsg)

我非常看好这个项目，因为「开源 + 一切皆插件」，让 DeepSeek Harness 做到了极致的开放，它的可能性是无限的。

**也许用不了多久，我们每个人手里的 AI 编程工具都长得不一样，因为每个人都可以根据自己的需求自由组装，我觉得这是一件很酷的事情~**

OK 就分享到这里，本文会收录到我免费开源的 [《AI 编程零基础入门教程》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588403&idx=2&sn=91ab9714bff9eb6e26d5c03081ec765f&scene=21#wechat_redirect) ，上千张图、几十万字，带你从 0 开始快速学会 AI 编程，做出自己的产品、跑通变现全流程，一次拿捏。

> 开源指路：https://github.com/liyupi/ai-guide

![鱼皮的 AI 编程教程](https://mmbiz.qpic.cn/sz_mmbiz_png/LlSQOKIxJ1HHRtDiawNbniaLXkhicrmPXDoR4Rt6uw4zAGU5ymmycl5VvyJ7Xria9RrR7jxUsTSYxvl7KicxcxqqGCeaEHqyTx4cFWI76FE9p1wQ/640?wx_fmt=png&from=appmsg)

鱼皮的 AI 编程教程

我是鱼皮，持续分享 AI 编程干货。觉得有用的话记得点赞收藏和关注~

欢迎在评论区聊聊你使用 DeepSeek Harness 的感受，有哪些不错的玩法？

往期推荐

[刚刚 DeepSeek V4 Pro 正式发布，夯还是拉？首发实战测评](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589394&idx=1&sn=189efe8d78f24d17a2f4171762cc8aa3&scene=21#wechat_redirect)

[B 站排行第 1 的 AI 编程教程，大升级！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589202&idx=2&sn=237459930b3e9402fb51fa461e72f2eb&scene=21#wechat_redirect)

[鱼皮软件外包团队，启动！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589148&idx=2&sn=9d0a6c17ff81747216e27c78cc05bd37&scene=21#wechat_redirect)

[完全免费的 AI 资源网站，起飞！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589107&idx=2&sn=0cb64c8664643099430e40b85e8881bd&scene=21#wechat_redirect)

[给 Codex 和 Claude Code 接入 DeepSeek-V4-Flash，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247589086&idx=1&sn=2bee88ff5ca40edc485a973001ac995e&scene=21#wechat_redirect)

[27 届秋招，巨能打的 AI 智能体项目来了！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588930&idx=2&sn=f5d157d911f02f17b2131307e6afe953&scene=21#wechat_redirect)

[27 届秋招早鸟群，限时开放！](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588776&idx=2&sn=dd20847f4d28a3167537c95ac18058b1&scene=21#wechat_redirect)

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过