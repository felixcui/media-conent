# 分享靠1个Agent控制所有Agent和应用新技巧

**作者**: 未知作者

**来源**: https://mp.weixin.qq.com/s/okMPP3Cn50lcao9ud8tE0w

---

## 摘要

用「1 个 Agent 指挥所有 Agent 和应用」的两条技术路线对比。①**LCU**（走 macOS accessibility API）：能“看懂”按钮和输入框，但 UI 不暴露到 accessibility tree 就抓瞎——剪映是 Electron 自绘 UI，时间线拖拽目标对 AX 几乎不可见，指令根本收不到，且全程要模型做视觉理解、烧 token；②**agent-desktop（vercel 开源）**：走 **CGEvent 注入**，在系统层模拟真实鼠标键盘事件，本身只是 CLI、不做推理、单独运行零额度，重复操作写成脚本回放即可。实测剪映 AI 剪辑：首次 13 分钟、第二次仅 **37 秒**，LCU 平均 4–5 分钟。代价是模拟真实输入必须占用窗口（不能后台跑），最佳搭配 Mac mini。

---

## 正文

# 分享靠1个Agent控制所有Agent和应用新技巧

两周前我吐槽Grok Bot控制终端codex绕开沙箱用上gpt独一档的computer use能力失败率奇怪的难题终于被我解决了，不只是浏览器自动化，是能操控本机里其他Agent，能操作剪映做AI剪辑，在第二次操作的过程中还可以完全不消耗额度，非常Amazing。

先说一下结论，目前最佳搭配是，
Grok Bot➕vercel开源的agent-desktop

因为openai没有开口子所以现在想要用codex同款computer use有两条技术路线。

1️⃣ amontlabs的LCU（Local Computer Use）跟codex用的同一条路，通过macOS的accessibility API读取界面，用accessibility动作去点击输入拖放。

好处是能「看懂」界面，知道哪个是按钮、哪个是输入框。坏处是，如果app的UI不暴露给 accessibility tree，就抓瞎了。它们都需要一个模型在后面做视觉理解和决策，所以截图，识别，规划动作都烧tokens。LCU作为MCP工具我在grok bot调用的时候也是走Codex的token。

2️⃣agent-desktop走的是另一条路CGEvent 注入。它不通过 accessibility API，是直接在操作系统层面模拟鼠标和键盘事件。按下，移动，释放，跟我手指在触控板上划一样。app 收到的就是真实的输入事件。它本身只是一个 CLI工具，不做任何推理，所以单独跑agent-desktop的命令是零额度消耗。

但agent-desktop不会自己思考。要告诉它点哪里，拖到哪里，等多久。这个「告诉它」的工作可以交给1个agent来做，写成脚本后回放时，消耗的额度是零。

重复的操作步骤遇到可变项，比方说ai剪辑就是素材不同导出分辨率不同，才需要模型介入，这样换来就是操作速度会快很多。同样是剪辑视频，第一次用了13分钟但是第二次用37秒就搞定了，LCU平均是4到5分钟。

但也不是完全没有缺点。agent-desktop模仿是真实输入所以需要占窗口，不像LCU可以在后台慢慢跑，最佳搭配还是mac mini。

还有一个技术点区分来这两套方案，

1️⃣ 我仔细对比了ai剪辑每步的操作时间，LCU在素材拖拽里浪费大部分时间，后面发现剪映是Electron套壳的自绘 UI，时间线区域的drop target对accessibility API几乎不可见，用人话说就是发的拖拽指令剪映根本收不到

2️⃣agent-desktop就没这麻烦，duration给了800ms的慢速拖动。对剪映来说这就是一个真实鼠标操作，跟人手拖一样。

果然这种在不断尝试慢慢找到正解，
在啥都可以问agent的现在还是很爽的，
现在我们都可以用1个Agent控制各种应用了！
这把效率又原地起飞了！