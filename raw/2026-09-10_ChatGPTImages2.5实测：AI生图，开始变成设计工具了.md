# ChatGPT Images 2.5 实测：AI 生图，开始变成设计工具了

**作者**: AI小范儿

**来源**: https://mp.weixin.qq.com/s/ah_zvKyPMZZkKZo7C3vMdQ

---

## 摘要

文章测评了OpenAI最新发布的ChatGPT Images 2.5图像生成模型。该模型在2.0版本基础上重点强化了主体一致性和多轮编辑能力，改善了细节呈现、复杂布局和生成速度，并新增Sketch草图、创作模板、图片评论和提示词分享等工具。作者实测发现，模型在换装、换背景、换发型等多轮修改中能较好保留人物原有形象，甚至会自动补全耐克标志等未指定的细节；用自己照片测试补全马匹下半身并让马奔跑时，人物。

---

## 正文

AI小范儿 AI小范儿

在小说阅读器读本章

去阅读

上周，OpenAI 刚刚发布 GPT-6 Astra。我还没从那股震撼里缓过来，今天早上，ChatGPT 的图片生成又更新了。

这次是 ChatGPT Images 2.5。GPT Image 2 已经那么强了，我很难想象它还能更新什么。越想越兴奋，干脆连夜开始测试。

上一代 ChatGPT Images 2.0 是今年 4 月 21 日发布的。那次升级，加强了对现实世界信息的理解、指令执行，以及密集文字和复杂细节的生成；同时带来了 Thinking 模式，让它能在生图过程中结合推理和工具，搜索信息、规划结果，还能根据一条提示生成多张图片。

当时我的感觉就是：AI 生图这场仗，在我这里已经打完了。强得离谱。从那以后，我的图片就一直交给 GPT Image 2 来生成，公众号的封面、插图，也都用它。

这次的 2.5 在 2.0 的基础上，重点加强了 **主体一致性和多轮编辑** ，同时改善细节、复杂布局和生成速度；工具上新增了 **Sketch 草图、创作模板、图片评论和提示词分享** 。我最关心的，就是照片改完还像不像原来的人，以及这些设计、修图功能到底好不好用。

01模型升级：主体更稳，修改更可控

光照、纹理、复杂布局这些提升，先看官方介绍。这次我没有逐项做新旧模型对照。我最想验证的是：拿一张参考照片来改，最后还像不像原来的人？

换衣服、换背景，再换个发型

先从一个简单的要求开始。我给它一张参考照片，提示词只有一句：

把服装换成运动装。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8TRTn7cvcJKYtiaSzTriaZibtvVhc8VmEFS4UF20iclruRgODjWo1rlSicr7KKboNsxCmnhWPjYzTvoickHv7icYnLqicWDxHxR31hJLxDIJLqibLNqc/640?wx_fmt=jpeg&from=appmsg)

▲ 图：换装前的参考照片

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLPH8kticcqcMte7ict0IyxXaJGA09sgxCXfvGEFHISX2C4kG1B0SBrd3O0HcznJhfkoCj68jHW4Z3PeErMdQoTEfic1EdmcMO6hk/640?wx_fmt=png&from=appmsg)

▲ 图：换成运动装后的结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKE2FibJLZXVueSbkjic4NxWBPtZNsbeoTNejSA3AFfVicAH5iaJWurQmpK66smMJpv8cDcMic2iayicdowbeSenv3aE2L0gDCBvhSnhk/640?wx_fmt=png&from=appmsg)

▲ 图：换装前后对比

卧槽，它把衣服、裤子换了，连鞋子和袜子都一起配好了。运动服和袜子上还出现了耐克的标志。我没有指定品牌，这也是它自己补出来的细节。

我更在意的是脸。就这张结果看，人物给我的感觉还是原来的样子，至少我没有一眼看出明显的失真。

接着，我让它把背景换成上海城市街头，再换个发型和头发颜色。两次结果放在一起看：

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKdzTUd797gN6BIhHbaiaQke2iblhK6de3htxDgiaLSx9j0ib4f7HRdl8vtVqIFThBib6kgsFFZ6V1SkOgjnicV9fJIw5icvRFudqzV90/640?wx_fmt=png&from=appmsg)

▲ 图：左：换成上海街头背景；右：继续修改发型和发色

这几轮下来，人物整体形象保留得让我挺满意。不过，逐张看也能发现，姿态和背景细节会跟着有些变化，还不能说除了指定的地方，其他部分就完全不动。

其实我还测了很多，受限于篇幅，图片就不一一放进来了。

再拿我自己的头像照测一次

拿自己的照片测，才是我心目中最地狱式的测试。别人像不像，有时看不准；自己被改得不对劲，很容易就能感觉出来。

以前我几乎不敢让 AI 改自己的照片，就是怕失真。这次我拿出了一张骑马的头像照。

原图里，马的腿没有拍全。我希望它把马的下半身补出来，还要让马跑起来，同时尽量保留我的样子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJLI3ZbXzrX8pn2qNL4U20YxSO2crukKCvJmWDbnLTKueMtTvgzTtbjkmU9GkoicqPGORGy4WLiaukn5Kr8DLcLe4GF6lxtUAU82c/640?wx_fmt=png&from=appmsg)

▲ 图：处理后：补全马的身体，并改成奔跑姿态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKocP8QTY1LzYLHiankJKnaxO9STI2ropZ7JqyOGSZic49KA6bhKlAnPtWk1CYwDQhBX9ibtXbpEpdNL2lIQIwotuIdDhRk1IFk48/640?wx_fmt=png&from=appmsg)

▲ 图：骑马照片前后对比：左为原图，右为修改结果

这张出来，我特地把脸放大看了。以我自己的感觉，几乎看不出明显的变化。你们也可以对着原图看看。

但继续改，就碰到边界了。

我又让它把我的动作改成双手握缰绳，再换一头黄毛。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJK1iccCvf5vMvU3abXX58GsfAVnXxRNl6UicdsliaZQKlKuRUnfdB6fw5oicaGn74ZgribmXrKgyN5tGQOIKTTibJsyibSotKfCL0ibYYc/640?wx_fmt=png&from=appmsg)

▲ 图：继续改动作和发色后的结果

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIHMkNawfCgt9TcibX3O5uSggHEvvciad3qhOdbgib6fp4o1TYhiaqzlYqOqzxrMQraobhssq6zsUzayeaqSH1a6e18NJEk9PfHabM/640?wx_fmt=png&from=appmsg)

▲ 图：修改动作和发色前后对比

这一张，我就觉得明显没那么像自己了。原照片里，手和墨镜遮住了一部分脸；把动作改掉以后，它得补出原来没露出来的部分，结果就容易偏。

所以，想改自己的照片，尤其要动到脸和姿态时，我会尽量给一张清楚、遮挡少的参考图。这次能保留到什么程度，成功和没那么成功的结果都放在这里了。

再放一个 OpenAI 官方的例子：把三张人物照片合成一张聚会合照。大家可以对照看看，三个人各自的形象保留得怎么样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKHqQG63exFQr03yW1DjPe0CwjZU1PCIxt8g8tCibLg2T84Gdnu7YqktxYH7ib099yK9pO1nxC4ndDtSC63fqfCdyesELoOcIKic4/640?wx_fmt=png&from=appmsg)

▲ 图：合成前的三张参考照片（来源：OpenAI 官方演示）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJJT6MEYEj6AMqgIic4IAyibFpZS21FkMbmDK1Z52MLpAk2o0FiaEnnJnXzuLl3sur7hiahgGlkB4auzOt7z0sgslebM3DL7S3BVFOI/640?wx_fmt=png&from=appmsg)

▲ 图：合成后的聚会合照（来源：OpenAI 官方演示）

02创作工具升级：从草图到修图、分享

这部分的变化，我觉得做公众号配图、海报和产品图的人会特别有感。除了用文字描述，现在还可以直接画、用模板起稿，或者在图片上点出要改的地方。

Sketch：先画个草图，让它接着画

除了直接打字，这次还可以在 ChatGPT 里画草图。

按官方说明，在输入框里输入 @Sketch，就能调用草图功能。我打开后看到的是这样的画布：

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLZfFwJUYotVxOMzgw7o0wKvvlH4z7TMwj5jYMaDrglib0iapXndictYmxqLFM3h1zkZge7TcA0IqHJcQ1d0llLsbLyEefn38vFjw/640?wx_fmt=png&from=appmsg)

▲ 图：Sketch 草图画布

可以调画笔大小、换颜色，也可以添加文字和形状，画错了就用橡皮擦掉。

我画了这么一个小人，然后让它按草图重新画成更精致的插画。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJKVrdh2jSbrPcZhNAhwiagKZzjtlaAWbth53ouEMlJMRHeYfIVTiazsibSX7xpic9wbmtnz7SP7J3X4nv7nqK4ooGLnN3xZVW5Vsa4/640?wx_fmt=png&from=appmsg)

▲ 图：我画的草图

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLW18dJczosTxWsuMGlRkJqXE0bY5pgRwMiar2VUKspLe40ic8pmMXY4oryNyhXYM0KBTbfxzBOeic2nMXAHjEibdicrSJJgUlTibx2M/640?wx_fmt=png&from=appmsg)

▲ 图：草图与首次生成结果对比（左图截取自操作截图）

我这画工，大家也看到了。最后出来的小人，头发、裙子、笑脸都有了，还加上了颜色和纹理。想说一个大致的形状时，现在可以直接画给它看。

模板：先把海报做出来

模板也是这次新增的入口。我选了海报模板，提示词会自动出现在输入框里，可以修改，也可以附上自己的参考图片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJIVelJhWcONz1HjP1PRfq6oB3UOwZz4Klo305PlSAavbibxq5w1u3jsNPJBdBGUJyoezB7R31UHQUzPPviaSCvDINue3BqrFso7Y/640?wx_fmt=png&from=appmsg)

▲ 图：模板选择界面

我上传了一张照片，没改模板里的提示词，直接提交。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJK3XeK8Ma0LlGySsznjHJHPAtgxQ3qiaULz05IcuCuwFwk4BWBXO8IZ4tt9QeCrBXzJV535iadwFnO7icpr40fzWmvHknE6tWwjv0/640?wx_fmt=png&from=appmsg)

▲ 图：上传参考图并使用海报模板

这一次，它没有立刻出图，先问了主题、必须出现的文字、尺寸和风格。我回复：做时尚杂志封面，文字让它帮我写，比例 3:4，采用 Vogue / Editorial 的感觉。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKnUPOeEf9oSpjKzwLcrJicOQSWuAbVRNVich0icv1CDc5kJC6GL0jud7n36hosmpDicosibgelFibySHLeuib1fIZUicwsrbL7oEeez08/640?wx_fmt=png&from=appmsg)

▲ 图：补充海报主题、尺寸和风格

然后得到这张图。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIZxp3S7o13r9DRfn2F5NcEmzpxkfmhfYLS3AkwibJUWtOamyszM6mCic7U6PUKjuJIalIia72EMhMNnSia3Y3pZnT6nxl3gs9DiawE/640?wx_fmt=png&from=appmsg)

▲ 图：根据模板和补充要求生成的海报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJJODCLGw1JcBBKWeJqYNusicDdqrXUhtytrpNDQHfW9D8183HY6w3ztzXESYxia9BibJ31d1f5etY9udtIRj5VEYkWYugLfichNLSQ/640?wx_fmt=png&from=appmsg)

▲ 图：参考照片与首张海报对比（左图截取自操作截图）

这个质量确实让我惊喜。头发、衣服的纹理，连同中英文排版，放在这张封面里看起来很协调。

局部编辑：圈出来改，点一下加评论

打开生成的图片，就能看到编辑工具：标注、评论、移除背景、擦除、调整尺寸。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKhbQXAgSTbkv8uGgPGggVhKbUEnHpZJO8qtgURgnc8vwzUfgrbvLxajj1MXB9QKjx3dKoZJjj93YopfUxD7CPzFoSj6S7TSWU/640?wx_fmt=png&from=appmsg)

▲ 图：图片编辑工具栏

我先试了标注。把上面的标题圈出来，再输入想替换的文字。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIG0bbYly7tjMP7NmqmCvf4XzQfVmK4gR5T3uQubK0wNcGLAUQ5fSRqHKeYHSyvJevKVicgfHy3ld2vB1SKYCJeY0tFKicDKic7F8/640?wx_fmt=png&from=appmsg)

▲ 图：圈选标题，并输入替换文字

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKTsS7N4icQHXcJg9u9mGHrqxYDGR4ic6MUP9j9YDL1EKSHAs3Bym69NnVhDXvwtkmSKZf02BI5s0p64BT3Z6LlJia34k8IpX362o/640?wx_fmt=png&from=appmsg)

▲ 图：替换标题后的海报

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLkPWenLI5k5ftXC5qPsKE06mpFt3JRk4ICz5HrkSDakgiaTGSnm1mfgVOdBJunvWOJc6veP8XESzjMTEPhUXPu1m4NSDE7x31Y/640?wx_fmt=png&from=appmsg)

▲ 图：标题修改前后对比：左为初版，右为替换标题后

这里有意使用了变体拼写“VOUGE”，图片也按提示词保留了这个写法。图中是测试用的杂志风格设计，非杂志官方封面。

再试评论。在眼睛附近点一下，写上“加一副墨镜”，提交。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKrFK4zWYArForzkHItW9YOJ6s20uT36b05VbqGhOtZ40W758NzBVOFBF3aUVxuQ9Bkqk2ibnd33a7FuMSVIns3g9sAYPSWyDps/640?wx_fmt=png&from=appmsg)

▲ 图：在眼睛附近添加评论：加一副墨镜

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJJQPrqgdiasSibWiceB9ShrZrGgbVPFDdeWceNdDh7awypB4s0thJwpyHuvThuOoia7cRqsUYscHN8tIPmOdjz7YfIc4dMnD3MiauKk/640?wx_fmt=png&from=appmsg)

▲ 图：加上墨镜后的海报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJI0NNX3S7IgMhPoqcJJibgwfVGWWTJqibB3oCpiarlr5Z8PVGC3eURMVm6AxR1cc7oibmsa9cyRWA0dkbj3Qj9dTm8shw2UIfguo34/640?wx_fmt=png&from=appmsg)

▲ 图：添加墨镜前后对比

墨镜加上了，前一轮改过的标题也保留着。把这张和初版放在一起看，人物、衣服和版面的整体感觉仍然接得上。这是我今天觉得多轮编辑好用的地方：可以继续改下去，不用每次重新做一张。

这种一致性，真的是强得离谱。它解决了我一直以来的一个痛点：以前改图，总是改着改着就跟前面不像了，好不容易做出来的效果又丢了，真的让人恼火。

调整画幅：从竖版到横版，重新排一遍

工具栏里还有移除背景。这次我更想讲的是调整尺寸，因为我经常要把图片用到不同平台，3:4、9:16、16:9，各有各的要求。

以前改画幅是件很麻烦的事。简单裁一下，人物可能被切掉，文字也可能放不下。要让它在新的比例里看着舒服，往往得重新排版。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJJqEUzQT74LtToiakG9SkOUayX0yGvlJL4Ciarj0AvbOvZqmoU5ZlEITL0CK5hlIPc7uOVPYNKmAkbiaDYAcxjFrJJzIH46CmzuhU/640?wx_fmt=png&from=appmsg)

▲ 图：调整尺寸菜单

我把刚才那张 3:4 的竖版海报，改成了 16:9 的横版。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJKiba1NVYQfZT75dDlwgefHY61XAJeWmkddA7jvyskZDjFyRHQiceX1nJiaSL9eyXkM7JGVM7wN6vYRXKcVkicL2vpQD5kM2UrpuZ0/640?wx_fmt=png&from=appmsg)

▲ 图：转换为 16:9 后的横版海报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJI8eicShILj0hO9BPDVleqUriclvE8tcek5BSW6A10ug8XYdd1ictc0W6BqHrF5VnsOutvJhtOtL2hKtuMan7Opxq7ict7Frgmj4Yc/640?wx_fmt=png&from=appmsg)

▲ 图：调整画幅前后对比

这一步超出我的预期。人物缩小了，画面向两边展开，标题和左右的文字也重新安排了位置。前面加的墨镜还在。

对我这种经常做封面、配图的人来说，这个功能太实用了。一张已经做好的图，换个画幅还能继续用，省掉的是重新摆人物、重新放文字的工夫。

分享：把提示词也带上

原来生成好的图片就能分享，这次多了“分享提示模板”。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJK9IFxpCPPbhLRiaWoUFn1z16WwDzGibzFQzOiccOKrGtZOjrMHJbFxGgRTiaVd5onTeyVI43wBdZ1Qbt9kYBEaQT3I795KAlLzIUk/640?wx_fmt=png&from=appmsg)

▲ 图：分享菜单里的“分享提示模板”

我点进去，复制链接，打开后能看到图片、提示词，以及“添加图像试试”的按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJJrX80sePHxIJesAuoySV11XhiaQt8qDaxb3tT3NjibxFfzXXKZEwCo5Vz9yVDyEoMucTI0DT0arlJgR6NI0z7bpQRHCwfxqAibWw/640?wx_fmt=png&from=appmsg)

▲ 图：打开分享链接后的页面

我这里做的是改图，所以分享出去的也是改图提示词，页面上显示的是“将宽高比设为 16:9”。别人可以添加自己的图片，试试同样的修改。

我看到这里，还是会想到那些围绕提示词模板做生意的产品。这样的入口直接放进 ChatGPT，它们得重新想想，自己还能提供什么。

03速度更快，在哪里能用？

最后说速度。官方的说法是，相比 Images 2.0，生成延迟最多降低 50%。

我自己的体感也确实非常快。以前尤其做测试的时候，总要等前一张图出来，才能进入下一步，一轮轮等下来挺磨人。这次等待明显短了很多，有些图感觉几乎一转眼就出来了。连续改图的时候，这种差别特别明显。

按发布公告，Images 2.5 正在向 ChatGPT、ChatGPT Work 和 Codex 的各档用户推出，覆盖桌面、移动端和网页。我今天早上打开 ChatGPT，已经看到了更新提示。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJIYs2V8ef6jrib3oLmxYibzgVnH6IAicBDIWt41A1gLqawXQczcUzCQgib8nGia2d7crOPsUWE7d2jEiaZgYKkvF1PbiauGUpy5mbUts4/640?wx_fmt=png&from=appmsg)

▲ 图：今天早上看到的图像创作更新提示

开发者还可以通过 API 使用两款模型：GPT-Image-2.5 Flare 侧重质量、编辑和速度的平衡；GPT-Image-2.5 Sunburst 追求更精细的控制，但生成时间更长。下面放上官方价格表，供需要接入 API 的朋友参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8TRTn7cvcJI6icH87hHlygjT3hicckyckWtMjvGj0GHYmLbNel7iaLWYfVlAf3eXh8u7AJDjsH0q8xiaqxSwLZPADnnxNAPzwLYy6LZxcia5NPyU/640?wx_fmt=png&from=appmsg)

▲ 图：OpenAI 官方 API 价格表（中文翻译），标准档；单位：美元／百万 tokens

04实测中遇到的几个问题

前面说了不少好用的地方，但这一轮测下来，也碰到了几个让人卡住的问题。

换件衣服，也可能被拦下来

测试第一个模特的时候，我输入了一句“换成晚礼服”，结果没等来图片，反而收到一条提示：生成的图片可能违反了针对潜在欺诈或诈骗活动的防范措施。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJJwun8erCMJpBWMXaTZHBDOZtRxLLP2bWd2kFibDAtKicPPUXEDFCWLMJibevPD7FNZKc41wfq2YFnT9ZbQD7m37MHKsueuDpjsKU/640?wx_fmt=png&from=appmsg)

▲ 图：输入“换成晚礼服”后，出现安全拦截提示

这让我有点摸不着头脑。只是想换件衣服，怎么就跟欺诈、诈骗扯上关系了？以前用的时候，我印象里很少碰到这种情况。这次是不是风控更严格了？目前还不好下结论，也可能是这一次触发了误判，但它确实打断了正常的改图过程。

想回头改前面的图，它却改了后面的图

另一个问题出在多轮对话里。顺着上一张图继续改，整体还挺顺；但中间换过别的图，再想回头修改前面那张，就容易混乱。

比如下面这次，我引用的是前面那张模特图，要求“戴上墨镜”。结果它却给后面那张骑马照里的人加上了墨镜。

![](https://mmbiz.qpic.cn/mmbiz_png/8TRTn7cvcJLYUpIF7ruQmbSCXAhItxqcHsZNyhDbvYjamCicFtmn88eOVOQHNibTc2nBI83Ubd6fljia2aaQd1hV1FicTUZcfELsIvicbYOgxicico/640?wx_fmt=png&from=appmsg)

▲ 图：引用的是模特图，实际加上墨镜的却是骑马照

也就是说，在我这次的测试里，它似乎更容易沿着最近一张图往下改。即使我已经指定了前面的图片，它还是可能找错对象。一个对话里交替处理几张图的时候，这个问题就挺烦人的。

生成快了，但还是得一张张等

还有一点：这次在 ChatGPT 里测试，我没法同时发起多张图的生成，得等前一张完成，才能开始下一张。

前面说它快，是指单次生成的等待明显缩短了。但如果要连续测试很多提示词，或者手头有几张图都想改，还是得排着来。速度提升缓解了等待，并发这件事，在我这次使用的界面里还没能实现。

05最后说几句

用完这一轮，我越来越觉得，AI 生图已经成熟到了一个很高的程度。至少对我每天做的公众号封面、插图和海报来说，它已经是一个可以长期放进工作里的工具了。

2.0 的出图能力让我愿意一直用它，2.5 则把后续那些琐碎的修改接了起来：人物要保留，标题要换，画幅要适配，改了几次之后，前面的效果还得在。能把这些事做顺，才会让人放心把日常工作交给它。

当然，它还会出错，我那张改了动作的骑马照就没那么像自己。但整体上，我现在考虑得更多的是这张图该怎么设计、哪里还可以改，而不是担心一动手，前面做好的东西就全变了。

这也是我觉得这次升级有分量的地方。一张好看的图，已经越来越容易得到；而当它能顺着你的想法，一步步改到能用，AI 生图才算真正走进了日常创作。对我来说，这个变化已经发生了。

参考资料

https://openai.com/index/introducing-chatgpt-images-2-5/

https://openai.com/index/introducing-chatgpt-images-2-0/

https://openai.com/index/gpt-6-astra/

https://deploymentsafety.openai.com/chatgpt-images-2-0/new-safety-challenges

https://developers.openai.com/api/docs/pricing

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过