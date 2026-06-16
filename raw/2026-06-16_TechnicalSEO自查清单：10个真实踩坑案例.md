# Technical SEO 自查清单：10 个真实踩坑案例

**作者**: 子木

**来源**: https://mp.weixin.qq.com/s/BnvJ_ecIP5e569R-MWpyUA?scene=1

---

## 摘要

Technical SEO的本质是确保网站具备被Google抓取、理解、收录和正常访问的基础能力，核心目标是实现网站基建的SEO Friendly。文章通过真实踩坑案例剖析了常见技术错误，例如测试子域名与正式官网内容一致导致被判定为重复页面而分摊权重，需通过密码或robots.txt屏蔽；以及多语言页面URL结构混乱导致权重内耗，需统一规范默认语言路径并补齐hreflang和canonical标签。

---

## 正文

子木 子木

在小说阅读器读本章

去阅读

▲ 是新朋友吗？可以点上方 “蓝字“ 关注下 ~

---

「AI 工具站 SEO 小册子：图解入门」

https://usdunlunl.feishu.cn/docx/JasgdjA7yoy1KTxpwuIcEkJ1noo

大家都知道我喜欢打比方，今天继续聊 Technical SEO 的本质。

一句话说清它要解决什么： **让网站先具备被 Google 抓取、理解、收录和正常访问的基础能力。**

Google 本质上就是一只爬虫加一套页面理解系统。它先派爬虫上门翻你的网站，再尝试读懂每一页讲了什么，最后决定要不要收录、给什么排名。 **所以如果你的网页打不开、加载慢、结构混乱、移动端体验差、服务还不稳定，就像一本书破到翻不开，连摆上书架都难，更别提被人翻到。**

也正因为这样，Technical SEO 的重点不是直接冲排名，而是先把这些地基问题解决掉：

页面性能、前后端加载、CDN、稳定性、URL 结构、目录层级、内链、多语言、响应式、lang / hreflang、结构化数据、robots.txt、sitemap、404 和重定向。

**我们的目标只有一个：让网站基建达到 SEO Friendly。**

下面是我认为最值得拎出来讲的 10 个 Technical SEO 错误案例，以及对应的解决思路 ～

## 1、test.xx.ai 测试子域名，跟 www 一模一样

很多团队为了测试方便，会照着 www 搭一套一模一样的环境，部署在一个测试子域名上。最神奇的是，用 `site: test.xx.ai` 一搜，发现谷歌居然把它也收录了，而且内容跟正式官网几乎没区别。

问题就出在这里。对 Google 来说，test.xx.ai 和 www.xx.ai 是两个长得完全相同的页面，它分不清谁是正主， **于是判定为「重复页面」** ，权重被两边分摊，正式官网的排名反而被自己的测试环境拖累。

**怎么处理：**

• 给 test.xx.ai 加访问密码，让爬虫根本进不去；

• 在 test.xx.ai 的 robots.txt 里明确禁止所有搜索引擎爬虫抓取和收录。

![图 01：test 子域名和正式官网长得一模一样，Google 分不清谁是正主](https://mmbiz.qpic.cn/mmbiz_jpg/3ezicJ4SpLiaKEkdg97QN2pIjuIyfYjw57rxbWtCTsOtvwicwicgLxfMR5jJVEY1W5UGD8MCoW9m6yXXgSwqJ7x3kqYjcMTicYuWus0Huj0AF5KM/640?wx_fmt=jpeg&from=appmsg)

*两本一模一样的破书都摆不上架，Google 干脆判成重复页面，权重两边分摊。*

## 2、产品上了多语言，SEO 却没跟上

有时候 `/en` 和不带语言前缀的地址都能打开，内容还一模一样。对 Google 来说，这就是两个独立页面，等于自己跟自己抢同一份首页权重。

**建议的做法：**

• 把英文设为默认语言，统一收口到不带 `/en` 的规范 URL，比如直接用 `https://soloent.ai` 。权重集中在一个首页上，也避免了默认语言的重复页面问题。

• 其他语言走清晰、可被索引的独立路径，比如 `/zh/` 、 `/ja/` 、 `/ko/` ，而不是只靠前端的语言切换按钮换文案，那种方式 Google 根本看不到其他语言版本。

• 全站补齐 `hreflang` 和 `canonical` ，让 Google 明确知道「默认英文页」和「各语言版本」之间的对应关系， **减少误判、重复内容和地区流量错配** 。注意 canonical 要和实际 URL 路径保持一致。

像 xx.ai 现在已经有多语言切换了，但 URL 结构和 SEO 信号还不完整，搜索引擎既不知道这些语言版本的存在，也不知道该怎么收录它们。所以核心页面要优先处理：首页、feature 页、Blog 博客页。

两个一致原则记住就行：

• **hreflang 要一致**

• **lang 要一致**

![图 02：同一份内容挂在 /en 和根路径两个 URL，等于自己跟自己抢权重](https://mmbiz.qpic.cn/mmbiz_jpg/3ezicJ4SpLiaLia44uMwiaxZg9Gj1VnOUaQWk2k6Koyex0wExv91sSTs90gXSUKa1alJus4vYfIqYDzzSk5cAPeW2Ru5wt11HcAQc2riaF9jygwM/640?wx_fmt=jpeg&from=appmsg)

*一份首页权重被天平劈成两半，收口到规范 URL 才能把它合回来。*

## 3、全站 E-E-A-T 信任信号

有些站连 privacy（隐私政策）和 terms（服务条款）页面都没有，最好再补一个 about 页面，pricing 也单独成页。

这些页面看着不起眼，作用却很实在：让 Google 和用户都更容易确认，网站背后是一个真实、可信、可联系的团队或公司，从而提升整站的信任感和权威信号。这正是 E-E-A-T 想衡量的东西。

## 4、URL 唯一

同一个页面不该有好几个能访问的地址。逐项检查：

• http 全部跳转到 https；

• 统一带 www 或统一不带 www，二选一；

• 结尾斜杠也要统一，要么都带 `/` ，要么都不带。

## 5、谷歌抓取状态异常

在 GSC 的抓取统计里，重点看请求中的错误占比。像图里这种错误比例就明显偏高了。什么时候会出现尖刺波动？通常是 CF 或 AWS 这类底层服务宕机的时候。

这里有个关键概念， **抓取预算** ：Google 每天分给一个站的抓取次数是有限的。如果 4xx/404、5xx 占比偏高，说明 Googlebot 把宝贵的预算大量浪费在了打不开的死链和报错资源上，真正该被抓的好页面反而轮不到。

![图 03：抓取预算有限，大量漏给了 404 和 5xx 死链](https://mmbiz.qpic.cn/mmbiz_jpg/3ezicJ4SpLiaIXcbNYXp486NCXARwckxAOq8Az2n1U8ceBMhYibcxXxRAgxP2U0ia0rRpKInnl5aelCGcqahZQwjghqzgicJtH4XSZCBjndzfdBs/640?wx_fmt=jpeg&from=appmsg)

*预算从 404/5xx 的裂缝漏光，真正该抓的好页面只剩一线细流。*

## 6、PageSpeed Insights 性能分

性能不只是体验问题，也是排名信号。可以在 GSC 后台看「核心网页指标」报告，或者直接用官方测试地址：https://pagespeed.web.dev/。

我这边的要求是：

> • 首页 PC 端：【性能】最好 90 分以上，其他几项尽量做到 100；
> 
> • 首页移动端：【性能】最好 80 分以上，其他几项尽量做到 100。

## 7、sitemap.xml 不完整

sitemap 是给 Google 的「目录索引」，常见两个坑：

• 漏掉了多语言的 URL，等于没告诉 Google 还有别的语言版本；

• 页面量很大时没做分片处理，一个超大文件容易抓取不全。

## 8、结构化数据（Schema）

结构化数据是用一套标准格式，把「这是一篇文章」「这是个产品」「这是 FAQ」这类信息直接喂给 Google，让它更准确地理解页面，还可能拿到富媒体搜索结果。常见两个问题：

• **schema 属性配置错误** ，字段写错或缺失，Google 直接忽略；

• Schema 没有做多语言，各语言版本应该有各自对应的结构化数据。

## 9、URL 不规范

估计是 AI 自动生成的，没人给定规范，导致 URL 又长又乱，最常见的是 Blog 文章的 slug 一长串。

理想的 slug 应该短、英文小写、用连字符分隔关键词，比如 `/blog/technical-seo-checklist` ，而不是把整句标题或一串随机字符塞进去。

## 10、Technical SEO 的检查修复思路

最后说下我自己整套的检查修复打法：

• **首页单独处理** ，它通常最特殊、权重也最高；

• **其余页面按模板归类** ，比如 `/blog` 、 `/blog/xxx` 一套， `/tools` 、 `/tools/xxx` 一套；

• **能靠改模板一次性修复全站的，就在模板层一次解决** ，不要逐页手动改；

• **剩下少数页面才有的个性化问题，用 plugins 这类插件化方式单独叠加** ，避免污染通用模板。

![图 04：三层修复法，首页单独、模板层一次修、插件单独叠加](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ezicJ4SpLiaKfyoVZaMdX1tHjJye1VKlNLwBcpEjKaTQ2vXFcib7F04vLbuicBZ4dC3eWgfYjtB1DfxMCLzJlV0TfFCcCZ1XibSUHukvicg2tDQM/640?wx_fmt=jpeg&from=appmsg)

*别逐页手改，按首页 / 模板 / 插件三层来，一次修一层。*

一句话总结： **地基稳了，排名才有的谈。Technical SEO 不性感，但它是后面一切内容和外链能不能生效的前提** 。

更多阅读下面复制链接

「AI 工具站 SEO 小册子：图解入门」

https://usdunlunl.feishu.cn/docx/JasgdjA7yoy1KTxpwuIcEkJ1noo

谢谢阅读！更多推荐阅读：

- [AARRR：AI 增长是每个人的基本能力](https://mp.weixin.qq.com/s?__biz=MzkwMTM5OTcxMQ==&mid=2247484782&idx=1&sn=4dc300c2c213550b7548674849f13c47&scene=21#wechat_redirect)
- [靠 11 个 SEO 大神 + Grok 任务，每天 5 分钟追完一手 SEO 情报](https://mp.weixin.qq.com/s?__biz=MzkwMTM5OTcxMQ==&mid=2247484774&idx=1&sn=b5acd716079bc63c8847b18bfadb4fb7&scene=21#wechat_redirect)

幸会幸会，我是子木。一直在 SaaS 软件行业，近几年 AI 软件出海中，略懂谷歌 SEO。

日常喜欢扒拉内容、扒拉代码，期待多交流，相互学习。也欢迎点击下面卡片，关注我公号杂文：

**扫码加我微信** **，有缘** **一起聊聊出海吧**

**👇👇👇**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ywAmIUMia5YgLhlEicQ4a69qdgibWMBaeqOnnzXKtar80ADxsuLVfLUicX7x35BibHMGU0SQr8hQJQXpjQ7Oar3iaMcg/640?wx_fmt=jpeg)

（你扫我？还是我扫你？）

继续滑动看下一个

写增长的子木

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过