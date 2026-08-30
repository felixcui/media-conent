# 【WorkBuddy开学季特辑】如何用WorkBuddy学好高数？！

**作者**: DracoVibeCoding

**来源**: https://mp.weixin.qq.com/s/nrnsia0mn7BR9vaVGesUOg

---

## 摘要

文章以开学季为契机，结合作者大学学高数的经历，介绍用WorkBuddy学习高数的方法：先让它学习Manim、Hyperframes和EdgeTTS三个开源项目，再借助AI生成数学动画与语音讲解，把抽象概念直观化，帮助理解和掌握高等数学。

---

## 正文

DracoVibeCoding DracoVibeCoding

在小说阅读器读本章

去阅读

今天看到腾讯搞了个WorkBuddy开学季的活动：

> 「大学四年，Buddy 陪你一路闯关升级」
> 
> https://www.workbuddy.link/p/uHz0Lf52Bq12QKPlsKOKSz

挺有意思，就想着也为即将开学的大学生们写点东西～

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiaQeDWzRjKdBag6O4w7Q3rTHZVUCbfdYzEibcrC13f5Z9e7ZYxBQbXr7r1LlDFcx825Y7Wr9W9ibu4YVKQP207qycX9GibYP2DKIw/640?from=appmsg)

> 有兴趣的同学可以点击文末“阅读原文”自己去看看

## 如何用WorkBuddy学好高等数学

我还记得当年数学学的不错，高考考了140多分，进了大学觉得也没太把高数当回事，结果大一上半学期的期中考试就让高数给我来个下马威，记不清具体多少分了，但似乎没上70分😂

然后才开始认真对待高数，后来基本都上90了，不过我依然能回忆起当初学高数时的种种痛苦...

要是当时有AI就好了，学习可能会方便很多。

所以，今天给大家展示一下如何使用AI来学习数学/物理这种抽象的学科。

## 准备阶段

首先，你需要让WorkBuddy学习两个用代码制作视频的开源项目：

1\. Manim

2\. Hyperframes

3\. EdgeTTS

### Manim

> Manim是大神‘3b1b’为了讲解深奥的数学概念而开发的使用代码来制作数学动效的开源项目/框架

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiaPD85mf80JKw6sYyAg5AsZYacPHn1bad2J3BWjxGGVP9Hq4UU9V3rEtETiak63DvDUy0w5ttldLl63vwgvvtfOCAd6wFeNmSk0/640?from=appmsg)

你可以把这个仓库喂给WorkBuddy：https://github.com/3b1b/manim 让它熟悉一下这个项目（其实WorkBuddy里的大模型应该的训练数据里应该基本都包含了Manim相关知识，不过，温故知新没啥毛病）：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgdWlrPrZ5NqS8PjNx6VU7XMWPIcoqKQ4eicugFBrL3Wy770AKwBayOnpx5VT8TFCSFLqrzwNT5mFYaqjPgZ4LhJHB9Vxq3QWL4/640?from=appmsg)

> 这个阶段我用的是GLM-5.3

经过和WorkBuddy的沟通和讨论之后，WorkBuddy建议使用Manim Community社区版：https://github.com/ManimCommunity/manim

### Hyperframes

Hyperframes是HeyGen团队开发的用前端代码来制作优雅美观视频效果的开源项目/框架。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhicNnnGmZ5QzjsGXPu6ngqpWsBx9fTrFJVFSgO4ZmMKrWCOVYVS4hsHMzYg0oZjBUc7yRLXMiax9zkHU62rnVXyxY06fliawewSA/640?from=appmsg)

接下来可以把Hyperframes仓库喂给WorkBuddy：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjXyHCHZBJtHQPC2WF1IEyA8zAS3BHL7FWVGNJCmoReRQYXQQ1YGx0QCOIszSOsLhudRXyTaibekRQnjFpn3RGKgslAHxRc2hPI/640?from=appmsg)

### EdgeTTS

EdgeTTS 是微软开源的 Python 库，调用 Edge 浏览器的神经网络语音服务（Online Neural TTS），免费、无需 API Key、无调用量限制，中文音质接近商用方案。它把文本送云端合成后返回音频流，支持多音色、语速/语调调节与字幕时间轴导出（SubMaker）。

```
# 安装EdgeTTS
pip install edge-tts
```

```
# 已装：pip install edge-tts
# 命令行直接生成
python -m edge_tts --voice zh-CN-XiaoxiaoNeural \
  --text "你好，高等数学" --write-media out.mp3

# 中文音色（节选）
# XiaoxiaoNeural 女声温暖 / YunxiNeural 男声阳光 / YunyangNeural 男声专业
```

有了EdgeTTS，你就可以免费给视频配上语音讲解了！

> 如果你看不懂这段，没关系，把这篇文章喂给WorkBuddy，它能读懂就能替你搞定。

---

在WorkBuddy熟悉完Manim和Hyperframes这两个框架并安装好EdgeTTS之后，我们就可以让WorkBuddy把大学阶段的高数知识点按照结构进行梳理：

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhUbGkaem7h8hKYrSzBndRjAx0Y6g9ZEicxN2oXKFPVjkEbkSu0utu560PYLVvBhCHjJUNic3cLluASlZUvoH4aM707ZDmAsBuoU/640?from=appmsg)

> 这里不需要coding，就用免费的Hy3就行

片刻之后，WorkBuddy梳理出了高数的知识模块

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgicYJcIFyUtkmUbwwLh7Wic02dg2YKc3fZn5ANy9Ed0bNu4KJqmkZ94ptevRqz4bawne9aFNhTJtRmxBRe3VUicLiakxicicIicCXV1k/640?from=appmsg)

梳理清楚之后，我们可以告诉WorkBuddy，让刚才它学习的Manim和Hyperframes以及安装好的EdgeTTS来制作一个POC/Demo视频来看看效果：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhiciaylbI5ia7waRJusvU6bevmQI8decKibwzaAJeL7J2aA1SBXwWvmeyt460L35YGaH2Op9HRs2rH0Hd1aSqxA2naWOWJ6HMm6yQ/640?from=appmsg)

> 这里，可以使用今天刚刚发布的腾讯混元4-Hy4 preview模型来制作～

通常情况下不会在第一个版本就得到很理想的视频，你可以和WorkBuddy一起微调若干次，直到你认为满意为止。

下面是高数第一讲“极限”的视频版，大家可以感受下效果：

当然，如果你对于EdgeTTS的语音效果不满意，市面上还有很多其他商业化TTS不是免费的，效果的确会更好，质量与成本，这个大家自己权衡就好。

接下来，如果视频就躺在自己硬盘上觉得不过瘾，其实还可以让WorkBuddy通过EdgeOne上线到公网。

> EdgeOne也和WorkBuddy一样，是腾讯家的，你只需要告诉WorkBuddy上线EdgeOne公网可见，它自然知道怎么办。
> 
> 如果你想了解更多使用EdgeOne的细节，可以参见我过往的教程：
> 
> 【Workbuddy基础教程】如何开发部署网站到公网可见的自有域名 - 腾讯EdgeOne Pages版

我快速搞了一个：https://gaoshu-notes-orpjzawv.edgeone.cool/

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0m9F5vC1OGjRZ02QUC4TvibKdQZMeRZibZvpSAatJfklEhzgXTJq7EDtd7piakDqhCQ7Lh21ET3yoZ0QejbCNJLlIZVr6IlDOtJiak8t9aFFQDg/640?wx_fmt=jpeg)

![image](https://mmbiz.qpic.cn/mmbiz_jpg/0m9F5vC1OGianWQEMnChib7Jo9SiaTOQQ7dJZGFTsWCj6wMPicDY2gPEsm9ajXGCah8pzDe8VlibaiaUFdRJg6fiarq6TheTju4CjCm17ZP9As0ug4/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0m9F5vC1OGiaowSryYYgz6yTk0N2T2eRiadPrWhZFcIHicPOaCtw5Z18pWqACFWOy4lYKuvekfBicrsOM7GUWMfibDb1luVI9kNOH3lQAbQ8sdjw/640?wx_fmt=jpeg)

目前16集已经全部上线：

> • 数列的极限：ε–N 到底在说什么
> 
> • 函数的极限：x 靠近时，f(x) 去哪
> 
> • 无穷小与极限运算法则
> 
> • 两个重要极限
> 
> • 函数的连续与间断
> 
> • 导数的定义：从割线到切线
> 
> • 求导法则：四则运算与链式法则
> 
> • More to come...

哦对了，之前还用Manim搞过一些关于傅里叶展开、AI Transformer架构的的视频，大家有兴趣也可以看下：

总之，这篇文章是想告诉大家：

> 在AI Agent时代，要学什么、以什么形式学，主动权完全掌握在你自己手里。
> 
> 只要你想学，AI Agent可以帮你实现一切～
> 
> 当然，这里面需要点钻研和打磨的精神，因为AI Agent通常不会在第一次就给你最好的结果。
> 
> 这本身也是一种“泰勒展开”嘛～

WorkBuddy官方这个H5小游戏也蛮有意思，有兴趣的同学可以点击“阅读原文”去看看：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjtzjL4mJV9H1MvdXCo1PG7g0asNZ7PhMCvibBnDJHKydBibcg3iblCt9fWLXcN9IzwIjqOruGibfzZfvlVCrChXRPMyzibnQwiaiav2I/640?from=appmsg)

#WorkBuddy开学季

#我的开学搭子WorkBuddy

阅读原文

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过