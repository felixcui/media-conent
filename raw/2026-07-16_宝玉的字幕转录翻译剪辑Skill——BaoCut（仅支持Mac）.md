# 宝玉的 字幕转录翻译剪辑 Skill —— BaoCut（仅支持 Mac）

**来源**: https://waytoagi.feishu.cn/wiki/Fqgjw2i3tijO7ckpQp3cY6Punug

---

## 摘要

BaoCut是一款仅支持Mac的字幕转录翻译剪辑Agent Skill及配套App，它通过命令行配合Claude Code等Agent实现视频转录、说话人识别、文本润色翻译及基于文本的简单视频剪辑，有效解决了AI处理后缺乏友好二次编辑界面的问题，支持进度同步至图形界面供人工预览与编辑。该工具翻译质量好但速度略慢，可通过官网或GitHub下载使用。

---

## 正文

# 宝玉的 字幕转录翻译剪辑 Skill —— BaoCut（仅支持 Mac）

> 🔗 原文链接： [https://x.com/dotey/status/20770749...](https://x.com/dotey/status/2077074912435433901)



字幕转录翻译剪辑 Skill —— BaoCut（仅支持 Mac） 

借助 Agent Skill，可以转录视频、对转录结果识别 Speaker、润色（纠正错别字口癖等）、也可以根据转录结果对视频进行简单的剪辑，比如删除口癖、重复等。

这次尝试解决一个问题就是 Agent 对字幕转录翻译后，无法通过一个友好的操作界面二次编辑的问题。 

现在的做法是为 Agent 提供一个 cli，配合 Skill 的说明，Agent 可以借助 cli 去转录，获取转录结果润色、翻译，并实时同步进度到 GUI。后续可以在 GUI 进行预览和人工编辑。 

安装了 Skill 和 App 后，后续只要从 Codex 或者 Claude Code 这种 Agent，触发 Skill 即可执行，比如： > /baocut 转录并翻译视频：<视频 url 或路径> 

已知问题： 

\- 仅支持 Mac 

\- 翻译速度略慢，但质量会不错 

下载地址： [baocut.app ](https://t.co/89Wi1b3hZT)

Skill 从 App 内可以安装，或者 Skill 地址： [github.com/jimliu/baocut](https://t.co/aON4AditbU)

![](https://feishu.cn/file/RSLlbTOX4oia4zxnMsKcNrAfnwf)