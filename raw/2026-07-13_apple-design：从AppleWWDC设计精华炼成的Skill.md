# apple-design：从Apple WWDC 设计精华炼成的 Skill

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/dDLz8cxx3mwVzsIjQJAflA

---

## 摘要

前Vercel设计师Emil Kowalski开发了包含apple-design在内的五个AI skills，旨在解决AI生成界面缺乏设计品味的问题。他将苹果WWDC演讲中的精华提炼为17条设计原则，转化为AI可直接执行的规则。该工具能指导AI生成符合苹果级品位的界面与动效，或对现有代码进行审查优化。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

把好的设计判断力，写成 AI 能执行的规则。

Emil Kowalski（前 Vercel、Linear 设计师，现 animations.dev 创始人）把苹果级设计品位做成了一个 skills。

安装很简单：

```bash
npx skills@latest add emilkowalski/skills
```

装完之后，AI 就能按照这些规则来生成界面或审查代码。

仓库里目前有五个 skill，最值得看的是 `/apple-design` 。Kowalski 翻了他最喜欢的 WWDC 视频，提炼出 17 条设计和动效原则，翻译成了 Web 开发能用的规则。

为什么需要这个东西？Kowalski 的原话是：

**"Agents don't have great taste."**

AI 生成的界面经常差那么一点。入场动画用了 `ease-in` ，但应该是 `ease-out` 。边框用了实线，但应该是半透明阴影。单独看都是小事，堆在一起就变成「说不出来哪里不对，但就是不好看」。

这套 skills 就是把这些「说不出来」的问题一条条列出来，告诉 AI 怎么改。

五个 skill 分别是：

- **emil-design-eng** — 主 skill，覆盖动效和设计建议
- **review-animations** — 严格审查动画，按他的个人规则
- **improve-animations** — 扫描整个代码库的动画，输出优先级排序的修改计划
- **animation-vocabulary** — 教 AI 用正确的术语描述动效
- **apple-design** — 从 WWDC 提炼的 Apple 设计原则，适配 Web

有人问他为什么选 2018 年的 Designing Fluid Interfaces 而不是更新的 Liquid Glass。他说那场演讲是他心中 Apple 最好的设计演讲之一，里面的原则是 timeless 的。

笔者试用了一下，确实让人眼前一亮，它可以帮你分析当前设计差距并给出改进计划，几句话便能对齐顶级苹果设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJibH6RUTvlx7U51kOiakZ8Pr4Jxq13GowlZ0VvwFf0wUkul71haglI6wWtNIEyIAVdDibGBNic7CUTYcXxzrakvyEpvNvkxbEIPDXE/640?wx_fmt=jpeg) ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rY5icXvTTrJictqhtarZMcYBur2WJqS4ePTMcC7lpdCIhHibUGrpNsweu9oJusHLntVBvWWvxI3od2O09ic9U6WGR3IQiamB93OmCcksvqj9DjSE/640?wx_fmt=jpeg)

这是改后的效果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rY5icXvTTrJ9LaQ9PD1ClNOYicPZzv7ibUXek1KJP3tkgPlmQhhbKZG7vFl98uVOOCyaIhtb9w5caXuJzu8Z33Jr8ZvINoElTVF43rFB4bj81c/640?wx_fmt=jpeg)

就像把一些工具书炼化成 skill 直接交给 AI 执行,与这个思路异曲同工，不用经过人的理解和转述,而是让内容直接对接 AI,效率更高,信息损失也更少。把领域经验直接编码成 AI 可消费的形式,或许会成为未来的主流模式。

Kowalski 自己也说，他最近变得极度「AI-pilled」，但不是因为觉得 AI 能替代专家。恰恰相反，AI 不替代专业能力，它放大专业能力。

GitHub:https://github.com/emilkowalski/skills

关注公众号回复“进群”入群讨论

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过