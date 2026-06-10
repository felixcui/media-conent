# 关于 Harness Engineering 你需要知道的一切（2026 版）

**作者**: AI技术立文

**来源**: https://mp.weixin.qq.com/s/lc_iBYAu0kMZNP4cy1P6NA

---

## 摘要

Harness Engineering是2026年AI领域兴起的关键工程方向，核心公式为Agent等于模型加Harness。Harness指代规则、反馈回路、文档和工具等除模型外的一切环境因素，如同操作系统管理CPU般让不可预测的模型变得可靠可控。行业实践表明，决定AI Agent在生产环境中表现的根本不再是模型本身，而是如何设计优化这套环境系统，Harness已成为释放AI生产力的真正关键。

---

## 正文

AI技术立文 AI技术立文

在小说阅读器读本章

去阅读

![图像](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic3yy5vOS8Lzydfe6jS7kSXqsSiaZ8cejza0SdOI1wuCqhQ5tEvKkkCrMpJfmgQpseahGJQczcCzAoAHX1cQZmVzMWzejicsC65aE/640?wx_fmt=jpeg&from=appmsg)

2026 年 2 月，OpenAI 一个小团队交付了 100 万行生产代码。

没有一行是手写的，全部由 AI Agent 完成。

人类做的事情是设计一套系统，让 Agent 变得可靠。这套系统现在有了名字： **Harness Engineering。**

几周之内，Anthropic 发表了 3 篇相关论文，ThoughtWorks 形式化了一套框架，Hugging Face 的 Philipp Schmid 称它为"2026 年最重要的工程学科"。

一个新的工程方向在 90 天内成型，但在 AI 基础设施团队之外，真正理解它的人并不多。

这篇文章尝试把它讲清楚。

## Harness 是什么

### 1\. 定义

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic1v8QjcynlUtia47kQ4hkrPVvmt1BCB1ibCntKBrH3xmicqnc9ohP6ddBEqCP9Z4rhlyQzeaia8Jd41kEInNDBeibvkdM7mv7ZfNbSc/640?wx_fmt=jpeg&from=appmsg)

最简洁的定义来自 ThoughtWorks：

**Agent = Model + Harness**

Harness 是除了模型之外的一切：约束 Agent 不跑偏的规则、捕捉错误的反馈回路、告诉 Agent 当前处境的文档、它被允许使用的工具。

去掉 Harness，模型只能在代码库里摸索前行。加上合适的 Harness，它就成了一个能交付生产代码的系统。

这个名字来自马具。缰绳、鞍和嚼子将一匹强壮但不可预测的动物引导到有用的方向上。核心思路不是让马变聪明，而是通过装备设计让它的力量变得可控。

### 2\. 操作系统类比

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic3yV13bvibJvBMH4M2MKPNHynteLFnVib9hMJnADvTGbd6pnGhL5UjzOqUK2DjWDBuNoO9QAPdgibW0EicbB0ibxB9Dd1q9OyOcv330/640?wx_fmt=jpeg&from=appmsg)

Philipp Schmid 给出了最好的技术类比：

- **模型 = CPU**
	（原始算力）
- **上下文窗口 = 内存**
	（有限的、易失的工作内存）
- **Harness = 操作系统**
	（管理 CPU 看到什么、什么时候看到）
- **Agent = 运行在上面的应用**

模型很强大，但如果没有操作系统来管理内存、调度任务、执行规则，它就只是一块硅片。

大多数人在用 Agent 的时候，实际上缺少这样一个操作系统层。这也是很多 Agent 在生产环境中不稳定的根本原因。

### 3\. 2026 年发生了什么变化

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic1Hjjxj9VcPSnF9o3qWltUG2UibH2yicjU7jaUCEQwyxWE93ewic2TH2tib4BxRDdcOQu9HEobLojUVsFkNaVlVt78dEkasMMr2we8/640?wx_fmt=jpeg&from=appmsg)

LangChain 在 Terminal Bench 2.0 上用同一个模型跑了两次，唯一的区别是 Harness。

- 旧 Harness：52.8 分
- 新 Harness：66.5 分

Vercel 走了相反的方向，他们砍掉了 Agent 80% 的工具，结果性能反而更好了。

2026 年一个值得正视的事实： **Agent 从来不是难点，Harness 才是。**

如果说 2025 年是 AI Agent 证明自己能写代码的一年，那 2026 年就是我们认识到环境比模型更重要的一年。

## Harness 的 5 种制品

### 4\. AGENT.md / CLAUDE.md 文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic1vk3kqLG6iblUrZic8ibkTPia4p86rEVze8D6yNEeKRBbibXibcXUTlSs395T0JEkrVFCOHNibicDmIjmHOLeqE5iaXKKEK2BAkgtiabkWM/640?wx_fmt=jpeg&from=appmsg)

最通用的 Harness 制品。分布在代码库各处的 Markdown 文件，Agent 在每次会话开始时读取它们，就像新工程师入职时的引导文档。

内容包括：项目上下文、编码规范、架构决策、"我们这里怎么做事"的指南、当前进行中的工作。

OpenAI 叫它 AGENT.md，Anthropic 叫它 CLAUDE.md，Cursor 用 `.cursorrules` 。名字不同，原理一样：每个主要模块一个文件，随项目演进更新。

没有它，Agent 每次会话都从零开始；有了它，Agent 每次会话都带着背景信息启动。

### 5\. JSON 特性列表（进度追踪器）

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic0hVJWBUbY5Ianpd3ANa6Ywh52fOq9a9gSGwXQwibEATS7d1VJia8sSUAibAWiazpKKHgWkUmtKDFRsQoBZRVIyEwYVhKVianrfwDa8/640?wx_fmt=jpeg&from=appmsg)

当 Agent 跨多个会话构建一个完整应用时，每次会话的上下文窗口都是空白的。它怎么知道哪些已经做完了？

靠一个 JSON 文件。每条记录定义：一个特性、验证方法、通过/失败状态。

Agent 在会话开始时读取这个文件，选择优先级最高的失败项，实现它，标记为通过，提交，重复。

为什么用 JSON 而不是 Markdown？Anthropic 发现 Agent 意外覆盖 JSON 的概率比 Markdown 低得多。看似小细节，但在 6 小时无人值守运行中，这类差异的累积影响相当可观。

### 6\. 会话初始化例程

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic1V78tZibaIVreFmsSPj3IXkmynia9klxndnb30jxIITIhdBB9jA4jKYkOn0qfQ3MTlnvP1qiaNggUaH9qibX8VsQhOjgn6K3OibVUY/640?wx_fmt=jpeg&from=appmsg)

每次会话都用同样的方式启动。每一次都是。

Anthropic 的 7 步启动序列：

1. 确认工作目录
2. 读取 git 日志和进度文件
3. 从特性列表中找到优先级最高的未完成项
4. 启动开发服务器
5. 运行基础端到端验证
6. 实现一个特性
7. 提交（附带描述性消息）并更新进度

没有它，Agent 需要花前 20 分钟搞清楚当前状态，每次会话都在做重复劳动。有了它，Agent 可以立刻进入状态，直接开始工作。

### 7\. Sprint 契约

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic24ef8txsV1sz6ozSlZwSamiaLovmgCUPdZh8gCkxsiakB2RIXAZdVo8MialJNKVQ2lazr8BZMxydU8aQF6KaUFBZgWbC0ATWNPk8/640?wx_fmt=jpeg&from=appmsg)

在 Agent 写任何代码之前，先由两个 Agent 协商。

Generator Agent 提出：要构建什么、如何验证成功。Evaluator Agent 审查：方案是否完整、成功标准是否明确。双方达成一致后才开始实现。

这本质上就是一个设计评审，只不过参与者换成了 AI。

为什么这很重要？如果让 Agent 在同一个 pass 里既做规划又做执行，产出质量往往不稳定。即使规划步骤由 AI 完成，独立的规划环节也能显著提升输出质量。

### 8\. 结构化任务模板

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic2twVuATyXX3b2OYsFn2ZcuhzhNPxl8iacbOQzjZ6ffUicptz37NPEW5ZqVo6EZslIM1Yjyx4TyVrhBfSIFuMaicEF5vrHLEIH8e0/640?wx_fmt=jpeg&from=appmsg)

在写代码之前，Harness 先分析真实的代码库，产出一份基于实际情况的影响图：真实的文件路径（不是臆造的）、真实存在的符号名、可以遵循的现有模式、具体的验收标准。然后才开始实现。

这听起来理所当然，但大多数团队跳过了这一步。结果 Agent 只能猜测文件结构，编造不存在的 API 端点，产出的代码与现有代码库风格脱节。

先给 Agent 提供基于真实代码库的上下文，产出质量会好得多。

## 三大阵营

三个团队撞上了同一堵墙，然后各自造了不同的梯子。

### 9\. OpenAI：环境优先

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic1fv01s5dn4mzCr5znv6Zch6Mplj2ZJCOVZCUgQ1qKhKD9NvtTGFusMMB4z49TtKiabHArCQO3LYBcoYZgmgSppzgAaeD3xGjnM/640?wx_fmt=jpeg&from=appmsg)

OpenAI 的 Codex 团队面对一个现实问题：100 万行生产代码，没有一行手写，在这个规模下逐行 Code Review 已经不可行。

所以他们换了思路：把环境设计得足够严密，让 Agent 产出的代码从一开始就具备可审查性。

具体做法包括：严格的依赖流（Types → Config → Repo → Service → Runtime → UI）、代码库各处的 AGENT.md 文件，以及 Agent 直接接入 CI/CD 流水线。

核心理念： **设计好环境，然后放手让 Agent 去做。**

实际成果：Sora Android 应用由 4 名工程师在 28 天内完成，Play Store 排名第一，崩溃率低于 0.1%。Codex 每周处理 70% 的内部 Pull Request。

### 10\. Anthropic：把执行者和评审者分开

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic3Em0a2bN4OxwIPKjMK78qoDliaVIXbjU2unRJlbfnzndepdzo37egZm0r6MsCqltN5MeHlsj7vxdhufPyPvia7HJu0UbQiaHb3jg/640?wx_fmt=jpeg&from=appmsg)

Anthropic 遇到了另一个问题：让 Agent 评估自己的产出时，它倾向于给自己打高分，即使人类一看就知道质量有待提升。

自我评估行不通。Agent 同时充当学生和老师，缺乏对自身产出的客观判断。

他们的解法：三个专业化的 Agent。

- **Planner：** 把两句话的提示词展开成完整的产品规格
- **Generator：** 每个 sprint 实现一个特性
- **Evaluator：** 用浏览器自动化测试运行中的应用，像真实用户一样

核心洞察： **让一个独立的评估者变得严格，远比让生成者对自己的工作保持批判要容易得多。**

效果对比：没有 Harness 的单 Agent 方案花费 <svg style="vertical-align: -0.452ex;display:inline-block;max-width:100%;height:auto;" xmlns="http://www.w3.org/2000/svg" width="70.977ex" height="2.149ex" role="img" focusable="false" viewBox="0 -750 31372 950"><g stroke="#222222" fill="#222222" stroke-width="0" transform="scale(1,-1)"><g data-mml-node="math"><g data-mml-node="mn"><path data-c="39" d="M352 287Q304 211 232 211Q154 211 104 270T44 396Q42 412 42 436V444Q42 537 111 606Q171 666 243 666Q245 666 249 666T257 665H261Q273 665 286 663T323 651T370 619T413 560Q456 472 456 334Q456 194 396 97Q361 41 312 10T208 -22Q147 -22 108 7T68 93T121 149Q143 149 158 135T173 96Q173 78 164 65T148 49T135 44L131 43Q131 41 138 37T164 27T206 22H212Q272 22 313 86Q352 142 352 280V287ZM244 248Q292 248 321 297T351 430Q351 508 343 542Q341 552 337 562T323 588T293 615T246 625Q208 625 181 598Q160 576 154 546T147 441Q147 358 152 329T172 282Q197 248 244 248Z"></path></g><g data-mml-node="TeXAtom" data-mjx-texclass="ORD" transform="translate(500,0)"><g data-mml-node="mo"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">、</tspan></text></g></g> <g data-mml-node="mi" transform="translate(1500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">耗</tspan></text></g> <g data-mml-node="mi" transform="translate(2500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">时</tspan></text></g> <g data-mml-node="mn" transform="translate(3500,0)"><path data-c="32" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path><path data-c="30" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" transform="translate(500,0)"></path></g><g data-mml-node="mi" transform="translate(4500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">分</tspan></text></g> <g data-mml-node="mi" transform="translate(5500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">钟</tspan></text></g> <g data-mml-node="mi" transform="translate(6500,0)"><text data-variant="italic" transform="scale(1,-1)" font-size="884px" font-family="serif" font-style="italic"><tspan leaf="">，</tspan></text></g> <g data-mml-node="mi" transform="translate(7500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">产</tspan></text></g> <g data-mml-node="mi" transform="translate(8500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">出</tspan></text></g> <g data-mml-node="mi" transform="translate(9500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">的</tspan></text></g> <g data-mml-node="mi" transform="translate(10500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">应</tspan></text></g> <g data-mml-node="mi" transform="translate(11500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">用</tspan></text></g> <g data-mml-node="mi" transform="translate(12500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">核</tspan></text></g> <g data-mml-node="mi" transform="translate(13500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">心</tspan></text></g> <g data-mml-node="mi" transform="translate(14500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">功</tspan></text></g> <g data-mml-node="mi" transform="translate(15500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">能</tspan></text></g> <g data-mml-node="mi" transform="translate(16500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">存</tspan></text></g> <g data-mml-node="mi" transform="translate(17500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">在</tspan></text></g> <g data-mml-node="mi" transform="translate(18500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">缺</tspan></text></g> <g data-mml-node="mi" transform="translate(19500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">陷</tspan></text></g> <g data-mml-node="TeXAtom" data-mjx-texclass="ORD" transform="translate(20500,0)"><g data-mml-node="mo"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">。</tspan></text></g></g> <g data-mml-node="mi" transform="translate(21500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">完</tspan></text></g> <g data-mml-node="mi" transform="translate(22500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">整</tspan></text></g> <g data-mml-node="mi" transform="translate(23500,0)"><path data-c="1D43B" d="M228 637Q194 637 192 641Q191 643 191 649Q191 673 202 682Q204 683 219 683Q260 681 355 681Q389 681 418 681T463 682T483 682Q499 682 499 672Q499 670 497 658Q492 641 487 638H485Q483 638 480 638T473 638T464 637T455 637Q416 636 405 634T387 623Q384 619 355 500Q348 474 340 442T328 395L324 380Q324 378 469 378H614L615 381Q615 384 646 504Q674 619 674 627T617 637Q594 637 587 639T580 648Q580 650 582 660Q586 677 588 679T604 682Q609 682 646 681T740 680Q802 680 835 681T871 682Q888 682 888 672Q888 645 876 638H874Q872 638 869 638T862 638T853 637T844 637Q805 636 794 634T776 623Q773 618 704 340T634 58Q634 51 638 51Q646 48 692 46H723Q729 38 729 37T726 19Q722 6 716 0H701Q664 2 567 2Q533 2 504 2T458 2T437 1Q420 1 420 10Q420 15 423 24Q428 43 433 45Q437 46 448 46H454Q481 46 514 49Q520 50 522 50T528 55T534 64T540 82T547 110T558 153Q565 181 569 198Q602 330 602 331T457 332H312L279 197Q245 63 245 58Q245 51 253 49T303 46H334Q340 38 340 37T337 19Q333 6 327 0H312Q275 2 178 2Q144 2 115 2T69 2T48 1Q31 1 31 10Q31 12 34 24Q39 43 44 45Q48 46 59 46H65Q92 46 125 49Q139 52 144 61Q147 65 216 339T285 628Q285 635 228 637Z"></path></g><g data-mml-node="mi" transform="translate(24388,0)"><path data-c="1D44E" d="M33 157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z"></path></g><g data-mml-node="mi" transform="translate(24917,0)"><path data-c="1D45F" d="M21 287Q22 290 23 295T28 317T38 348T53 381T73 411T99 433T132 442Q161 442 183 430T214 408T225 388Q227 382 228 382T236 389Q284 441 347 441H350Q398 441 422 400Q430 381 430 363Q430 333 417 315T391 292T366 288Q346 288 334 299T322 328Q322 376 378 392Q356 405 342 405Q286 405 239 331Q229 315 224 298T190 165Q156 25 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 114 189T154 366Q154 405 128 405Q107 405 92 377T68 316T57 280Q55 278 41 278H27Q21 284 21 287Z"></path></g><g data-mml-node="mi" transform="translate(25368,0)"><path data-c="1D45B" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path></g><g data-mml-node="mi" transform="translate(25968,0)"><path data-c="1D452" d="M39 168Q39 225 58 272T107 350T174 402T244 433T307 442H310Q355 442 388 420T421 355Q421 265 310 237Q261 224 176 223Q139 223 138 221Q138 219 132 186T125 128Q125 81 146 54T209 26T302 45T394 111Q403 121 406 121Q410 121 419 112T429 98T420 82T390 55T344 24T281 -1T205 -11Q126 -11 83 42T39 168ZM373 353Q367 405 305 405Q272 405 244 391T199 357T170 316T154 280T149 261Q149 260 169 260Q282 260 327 284T373 353Z"></path></g><g data-mml-node="mi" transform="translate(26434,0)"><path data-c="1D460" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path></g><g data-mml-node="mi" transform="translate(26903,0)"><path data-c="1D460" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path></g><g data-mml-node="mi" transform="translate(27372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">方</tspan></text></g> <g data-mml-node="mi" transform="translate(28372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">案</tspan></text></g> <g data-mml-node="mi" transform="translate(29372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">花</tspan></text></g> <g data-mml-node="mi" transform="translate(30372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">费</tspan></text></g></g></g></svg> 200、耗时 6 小时，产出的是功能完备的软件，UI 也相当精致。

### 11\. ThoughtWorks：2×2 框架

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic3daV98icdiaGS3hLrciaOCsZgfMrG550s2nFfiaTblRKAY8VKaictgiaB2rDGNcvWhwnkicaPAmwkiayQpg4qUpGSpG4KVozblSQ3TjHw/640?wx_fmt=jpeg&from=appmsg)

ThoughtWorks 的出发点不同。他们不是在做产品，而是在观察 50 多个工程团队反复遇到相同的问题。

他们的洞察是将所有 Harness 控制沿两个维度分类：

**维度一：什么时候运行？**

- 前馈（Feedforward）= Agent 行动之前（引导）
- 反馈（Feedback）= Agent 行动之后（感知）

**维度二：怎么运行？**

- 计算型 = 确定性的，毫秒级（lint、类型检查、测试套件）
- 推理型 = 用 LLM，秒级（代码审查 Agent、语义分析）

形成的 2×2 矩阵：

|  | 前馈（行动前） | 反馈（行动后） |
| --- | --- | --- |
| **计算型** | 类型系统、linter、架构规则 | 测试套件、覆盖率分析、变异测试 |
| **推理型** | 规格文档、约束描述 | LLM 代码审查器、行为验证器 |

只有前馈或只有反馈都不够，两者都需要。

## 5 条共识原则

三个团队从未协调过，但独立得出了相同的结论。

### 12\. 原则一：上下文胜过指令

**让 Agent 看到世界的当前状态，效果始终优于抽象地告诉它该做什么。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic3LItzxFbDz7fNvDKZIzdCHggJjwjvVpS9mdryOYxXJ96WPvMovYticURY18MgZpCb8WSSOCe8KSIvmv73S3SibuXrguAMYoQEzw/640?wx_fmt=jpeg&from=appmsg)

OpenAI：「给一张地图，别给一本千页手册。」Anthropic：用 JSON 特性列表和进度文件让 Agent 始终知道自己在哪。Red Hat：在生成任何任务之前先分析真实代码库。ThoughtWorks：「前馈。」

基于真实文件路径工作，产出的代码自然能融入代码库。基于模糊描述工作，结果往往是臆造的文件路径和编造的 API。

经验很明确：在 Agent 写下任何代码之前，先确保它知道自己在哪。

### 13\. 原则二：规划和执行必须分开

**让 Agent 在同一个 pass 里既规划又执行，产出不可靠。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic0JAGowkjRom9Ct4d8NEeyRjNpwrcco75DPmyyQHea5rFxB3qwvNKSQicDnpE3Ig3h2sbnvicR8SNy0ZELZQqezOO5M5j9uyYmLY/640?wx_fmt=jpeg&from=appmsg)

OpenAI 的做法是人设计环境，Agent 负责执行。Anthropic 让专门的 Planner Agent 在 Generator 接触代码之前运行。ThoughtWorks 在规划和实现之间设置了强制的人工审查检查点。Red Hat 在影响图阶段和实现阶段之间设置了硬性门禁。

规划步骤不一定要人来完成，但它必须是一个独立的环节，产出物在实现开始前需要经过审查。

### 14\. 原则三：反馈回路不可商量

**没有反馈的 Harness 只是一个带了额外步骤的 prompt。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic2mkn1nA96tJTqDnSUqQibnicdLAziavSZg9mla1SzZ6YgK6fsXzdia30VvuzCen1UicJ7n5GJmhQdEH7NvNT4x06SDBLSv7wFDibAjg/640?wx_fmt=jpeg&from=appmsg)

OpenAI 让 Agent 接入 CI/CD 和可观测性系统。Anthropic 使用专门的 Evaluator Agent 通过浏览器自动化进行测试。ThoughtWorks 将其形式化为"传感器"，并指出纯前馈方案永远无法确认引导是否真正生效。

三种方案，同一条原则。各方对谁来提供反馈有不同看法，但对是否需要反馈没有分歧。

### 15\. 原则四：一次只做一件事

**试图一次做太多的 Agent 会耗尽上下文，失去连贯性，无声地丢弃需求。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic3BLnGkXYibV9iahrLUfs3PaLTiayxenPyveD946AnqTbLJOpKBPIT6cJbQkkg6qDTsxXrIFDeGnzj34ME7nRXQBKKcXDrf06t8HU/640?wx_fmt=jpeg&from=appmsg)

OpenAI 的做法是把目标拆成更小的构建块，深度优先推进。Anthropic 强制每个 sprint 只实现一个特性，完成后立即提交。ThoughtWorks 采用分阶段生命周期（预集成 → 后集成 → 持续监控）。

Anthropic 的标准流程很简洁：读取进度 → 选一个特性 → 实现 → 提交 → 重复。

强制渐进式推进，是每个成功 Harness 的共性。

### 16\. 原则五：代码库本身就是文档

**如果一条规范、约束或架构决策没有写在代码库里，Agent 就不会知道。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic3HXeS87icUn0we1ib4CUSic5Av877eykTNloD4OWVg3sK8rvZ38IEY9hiaibqoicM1l3Pibx8eVDovy2CzcF2WqYHZa5Is44F4fAmflE/640?wx_fmt=jpeg&from=appmsg)

OpenAI 在仓库里嵌入 AGENT.md 文件。Anthropic 用特性列表、进度文件和 git 历史作为 Agent 的连续性机制。ThoughtWorks 衡量"可 harness 化程度"，即代码库对 Agent 的可读性。

没有人为 Agent 单独维护一个知识库，仓库本身就是唯一的事实来源。

实际意义很清楚：在代码组织上投入的团队，Agent 性能会随之提升。反过来，结构混乱的仓库加上 AI Agent，只会把混乱放大。

## 悖论：为了删除而构建

### 17\. Harness 衰减是真实的

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic1amman0MkRtCdoicVS185nE2UNRZYYO8YmXJnPxoFgYHUb7rcuN13A2maqUSicIjxk0POUyricjIaqClSoia9yyxXMJJQIvGeuUUw/640?wx_fmt=jpeg&from=appmsg)

Anthropic 从 Opus 4.5 升级到 Opus 4.6 时，Sprint 分解这个原本不可或缺的环节变得多余了。模型规划能力的提升使它不再必要。

一个 3 月份还在承担关键功能的 Harness 组件，到 4 月份就变成了额外开销。

随后 Opus 4.7 发布，模型开始自行验证产出，Evaluator Agent 的职责进一步缩小。

这就是 Harness 衰减。Harness 中的每个组件都编码了一个关于"模型做不到什么"的假设。随着模型能力提升，这些假设逐渐过期，对应的组件也就变成了负担。

- Opus 4.5：Sprint 分解 + 逐 Sprint 评估
- Opus 4.6：去掉 Sprint 分解 + 单次评估（节省 38% 成本）
- Opus 4.7：模型开始自验证 → Evaluator 角色进一步缩小

### 18\. 为了删除而构建

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic3GL5Iexvj3ILiaPl80ibibPk7WATIxFuFyv1gib1ZfIHn0cicwZsIWPZcnE80IDePiaWPxf4m8p8FXAoZ5RyYkibEjja54K7mE3fQ8jk/640?wx_fmt=jpeg&from=appmsg)

Philipp Schmid 的建议： **Build to delete。**

设计每个 Harness 组件时就考虑它是可移除的。定期关掉某个组件，看输出质量是否有变化。如果没变化就删掉它。

Manus 在 6 个月里重构了 5 次 Harness。LangChain 一年调整了 3 次。Vercel 砍掉 80% 的工具后性能反而更好。

这些频繁的重构不是工程能力不足的表现，而是在快速进步的模型之上构建系统的必然结果。

保留无用的 Harness 组件，每次运行都会消耗额外的 token，却没有任何质量收益。

### 19\. 成本现实

![](https://mmbiz.qpic.cn/mmbiz_jpg/IUJGIjicknic2apjnOKCq5RwXI9WcicvSkHMskzzBDDDNOwB8ADP3aYic5p9J9Fibf7ZIibdc73guIV2thqktKTpWSp2ibiatoQWzuMcFLCEXbYHvlE/640?wx_fmt=jpeg&from=appmsg)

Anthropic A/B 测试的真实数据：

- 无 Harness 的 Agent：$9、20 分钟，UI 可用但核心功能存在缺陷
- 完整 Harness（Opus 4.5）：$200、6 小时，功能完备的软件，精致的 UI，正确的业务逻辑

22 倍的成本差距，换来的是一个真正可交付的产品，而不是只在截图里好看的 demo。

是否值得，取决于一次失败发布对团队的实际代价。

另一个容易被忽视的事实是：Harness 与模型的组合在持续进化。 <svg style="vertical-align: -0.452ex;display:inline-block;max-width:100%;height:auto;" xmlns="http://www.w3.org/2000/svg" width="39.303ex" height="2.149ex" role="img" focusable="false" viewBox="0 -750 17372 950"><g stroke="#222222" fill="#222222" stroke-width="0" transform="scale(1,-1)"><g data-mml-node="math"><g data-mml-node="mn"><path data-c="32" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path><path data-c="30" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" transform="translate(500,0)"></path><path data-c="30" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" transform="translate(1000,0)"></path></g><g data-mml-node="mi" transform="translate(1500,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">的</tspan></text></g> <g data-mml-node="mi" transform="translate(2500,0)"><path data-c="1D43B" d="M228 637Q194 637 192 641Q191 643 191 649Q191 673 202 682Q204 683 219 683Q260 681 355 681Q389 681 418 681T463 682T483 682Q499 682 499 672Q499 670 497 658Q492 641 487 638H485Q483 638 480 638T473 638T464 637T455 637Q416 636 405 634T387 623Q384 619 355 500Q348 474 340 442T328 395L324 380Q324 378 469 378H614L615 381Q615 384 646 504Q674 619 674 627T617 637Q594 637 587 639T580 648Q580 650 582 660Q586 677 588 679T604 682Q609 682 646 681T740 680Q802 680 835 681T871 682Q888 682 888 672Q888 645 876 638H874Q872 638 869 638T862 638T853 637T844 637Q805 636 794 634T776 623Q773 618 704 340T634 58Q634 51 638 51Q646 48 692 46H723Q729 38 729 37T726 19Q722 6 716 0H701Q664 2 567 2Q533 2 504 2T458 2T437 1Q420 1 420 10Q420 15 423 24Q428 43 433 45Q437 46 448 46H454Q481 46 514 49Q520 50 522 50T528 55T534 64T540 82T547 110T558 153Q565 181 569 198Q602 330 602 331T457 332H312L279 197Q245 63 245 58Q245 51 253 49T303 46H334Q340 38 340 37T337 19Q333 6 327 0H312Q275 2 178 2Q144 2 115 2T69 2T48 1Q31 1 31 10Q31 12 34 24Q39 43 44 45Q48 46 59 46H65Q92 46 125 49Q139 52 144 61Q147 65 216 339T285 628Q285 635 228 637Z"></path></g><g data-mml-node="mi" transform="translate(3388,0)"><path data-c="1D44E" d="M33 157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z"></path></g><g data-mml-node="mi" transform="translate(3917,0)"><path data-c="1D45F" d="M21 287Q22 290 23 295T28 317T38 348T53 381T73 411T99 433T132 442Q161 442 183 430T214 408T225 388Q227 382 228 382T236 389Q284 441 347 441H350Q398 441 422 400Q430 381 430 363Q430 333 417 315T391 292T366 288Q346 288 334 299T322 328Q322 376 378 392Q356 405 342 405Q286 405 239 331Q229 315 224 298T190 165Q156 25 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 114 189T154 366Q154 405 128 405Q107 405 92 377T68 316T57 280Q55 278 41 278H27Q21 284 21 287Z"></path></g><g data-mml-node="mi" transform="translate(4368,0)"><path data-c="1D45B" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path></g><g data-mml-node="mi" transform="translate(4968,0)"><path data-c="1D452" d="M39 168Q39 225 58 272T107 350T174 402T244 433T307 442H310Q355 442 388 420T421 355Q421 265 310 237Q261 224 176 223Q139 223 138 221Q138 219 132 186T125 128Q125 81 146 54T209 26T302 45T394 111Q403 121 406 121Q410 121 419 112T429 98T420 82T390 55T344 24T281 -1T205 -11Q126 -11 83 42T39 168ZM373 353Q367 405 305 405Q272 405 244 391T199 357T170 316T154 280T149 261Q149 260 169 260Q282 260 327 284T373 353Z"></path></g><g data-mml-node="mi" transform="translate(5434,0)"><path data-c="1D460" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path></g><g data-mml-node="mi" transform="translate(5903,0)"><path data-c="1D460" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path></g><g data-mml-node="mi" transform="translate(6372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">在</tspan></text></g> <g data-mml-node="mi" transform="translate(7372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">一</tspan></text></g> <g data-mml-node="mi" transform="translate(8372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">次</tspan></text></g> <g data-mml-node="mi" transform="translate(9372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">模</tspan></text></g> <g data-mml-node="mi" transform="translate(10372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">型</tspan></text></g> <g data-mml-node="mi" transform="translate(11372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">升</tspan></text></g> <g data-mml-node="mi" transform="translate(12372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">级</tspan></text></g> <g data-mml-node="mi" transform="translate(13372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">后</tspan></text></g> <g data-mml-node="mi" transform="translate(14372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">降</tspan></text></g> <g data-mml-node="mi" transform="translate(15372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">到</tspan></text></g> <g data-mml-node="mi" transform="translate(16372,0)"><text data-variant="normal" transform="scale(1,-1)" font-size="884px" font-family="serif"><tspan leaf="">了</tspan></text></g></g></g></svg> 124。

趋势线： **更好的模型 = 更简单的 Harness = 更便宜的运行 = 更快的产出。**

## 总结

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IUJGIjicknic2lWE1CrxkibnlaBt8lAKPgWaw2NzW2KQZRvOEXcjr8EVQ3HSbRkgLn6zdzFlaX1QKLxy7wpg6ialq7duLXRtZURWuJEmez2f1PI/640?wx_fmt=jpeg&from=appmsg)

**概念：** Agent = Model + Harness。模型是 CPU，Harness 是操作系统。同一个模型换个更好的 Harness 就能提升 13% 的性能。

**5 种制品：** AGENT.md/CLAUDE.md 引导文件、JSON 特性列表、会话初始化例程、Sprint 契约、结构化任务模板。

**三大阵营：** OpenAI 的环境优先、Anthropic 的执行评审分离、ThoughtWorks 的 2×2 前馈/反馈框架。

**5 条共识原则：** 上下文胜过指令、规划与执行必须分开、反馈回路不可商量、一次只做一件事、代码库本身就是文档。

**核心悖论：** Harness 衰减是真实的，要为了删除而构建，更好的模型意味着更简单的 Harness。

2026 年走在前面的工程师，不是写最好代码的人，而是设计最好约束的人，并且愿意在约束失效的时候果断移除它们。

继续滑动看下一个

AI技术立文

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过