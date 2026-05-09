# 【实践案例】我用Skills实现了个自媒体知识管理神器！

**作者**: 叶小钗

**来源**: https://mp.weixin.qq.com/s/YDnhytrpl26ozXgGvauc1Q

---

## 摘要

作者针对自媒体内容收集整理低效的痛点，利用Claude Skills机制将繁琐流程封装，并开发了一套名为“Krawl”的自动化知识库管理系统，实现了从内容抓取到知识管理的全流程AI处理。文章以该实践为例，详细介绍了Claude Skills作为模块化扩展能力的定义、包含元数据指令与资源的三大要素，以及其按需加载以节省上下文窗口的渐进式披露设计原则。

---

## 正文

叶小钗 叶小钗

在小说阅读器读本章

去阅读

> AI训练营9 **期** ，5 **月7日** 开班，欢迎咨询

这两年，除了投入创业AI项目外，我还有个身份是一名自媒体。作为内容创作者，我经常需要从各种渠道搜集和整理信息，但这个过程始终充斥着低效与痛苦。

例如，当我刷到一条内容扎实的视频时，脑中常会闪过这样的念头：“这段内容如果能转成文字就好了，以后查阅会方便很多。”

然而现实中的操作往往是： **先收藏、再截图** ，最后把链接丢进“稍后处理”的收藏夹。等到真正需要整理时，不仅当时的灵感与上下文早已消失， **手头依然没有一份好用的文字材料** 。

过去，我会把这类任务交给实习生，但看着他吃力的操作过程，我总忍不住摇头：

1. 反复拖拽进度条，寻找关键句子；
2. 紧盯着字幕或费力听写，整理出的格式却依旧混乱；
3. 想做笔记，但信息分散在时间轴上，难以有效重组。

我在想，如果我自己来做，一次两次尚可忍受，但长期这样肯定受不了，于是，我带着实习生将这个繁琐的流程封装成了一个 **Claude Skill：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyQCG3RqrmyGJTtMibkQsto0ia5icP8e3XckVKJnekosGXjzgyTPhRn8DIfVQiba6Piayic5bickYglFnYEhSfZSUuh6q1qrRHictPpPCfU/640?wx_fmt=png&from=appmsg)

严格来说，这个场景其实Workflow已经是最优解了，但谁还没有一个Agent的梦想呢，而且Workflow只是解决了一个单点问题，就这个小问题背后其实有更大的探索空间：

> 能否构建一个完整的系统，让 AI 自动完成从内容抓取、整理到知识管理的全过程？

于是，我开发了 **Krawl 系统** ：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqPm2MSkzwZiboRibErfMj1mUf2yJ6ibatibDjk7gDWOOLJX5Uqib4IWBbTSQ/640?wx_fmt=png&from=appmsg)

一个基于 Claude Skills 机制的知识库管理系统。在深入介绍 Krawl 之前，我们首先需要理解一个核心概念：Claude Skills。

## unsetunset认识 Skillsunsetunset

Anthropic 官方文档给出了 Agent Skills 的定义：

```
Agent Skills are modular capabilities that extend Claude’s functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.
```

由于 OpenClaw 小龙虾的爆火，现阶段大家对 Skills 已经很熟悉了，他是一种模块化的能力，用于扩展 Claude 的功能。

每个skill都封装了相应的指令、元数据和可选资源（例如脚本、模板）。当场景匹配时，Claude 会自动调用这些技能来完成任务。

Agent Skills 的三大组成要素，同时也构成了上下文的三个层级，从抽象到具体：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqEy7c9W3FSRiaJbEpiapPdZw1CkucTvcBrw6S9LSVSuT8uNpdDvqaeWnQ/640?wx_fmt=png&from=appmsg)

1. 元数据：Skill 的名称、描述、标签等信息；
2. 指令：Skill 具体的指令；
3. 资源：Skill 附带的相关资源（比如文件、可执行代码等）；

Claude Skills 设计遵循了一个非常重要的原则，Progressive Disclosure（渐进式批露）： **分阶段、按需加载信息，而不是在任务开始时就将所有内容全部塞入本已宝贵的上下文窗口中。**

整个加载过程分为三个层次，对应上面的三要素：

### 第一层：元数据（始终加载）

Claude 在启动时会扫描所有已安装的 Skills，并加载这些元数据，将其纳入系统提示（System Prompt）中。 作用：

- 让 Claude 知道“自己拥有哪些技能”
- 用于后续的意图匹配和技能触发判断
- 不包含具体执行逻辑，占用上下文极小
![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyTt1blib5ptAV2xStfYnkB9cNGGqfrVCnFicNCJ4n9YoNZZo1wAgSXguDwZuc7YFVEoMiaLGJP1PyYFvrGicmyO6heGgpDVRjH3vWI/640?wx_fmt=png&from=appmsg)

### 第二层：核心指令（触发时加载）

当用户的请求与某个 Skill 的描述相匹配时，Claude 会通过 bash 从文件系统中读取对应的 SKILL.md 文件，并将其完整内容加载进当前对话上下文：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyQTPMRaWaP2Ns6djZcnjU1tvdU88UuRxyMS5fxicbr5ng6ib97rsicZLcZ20cJFBNUDkiaEY9fGkgvjNF0fzYwOhwYXQsEEEY7R1oc/640?wx_fmt=png&from=appmsg)

### 第三层：代码与资源（按需加载）

一个复杂的 Skill 可能包含多个文件，形成一个完整的知识库。 Skill 可以将这些资源与指令一起打包，实现完整的任务闭环。

通过 元数据 → 指令 → 代码与资源 这三层结构，一个 Skill 不仅能被 Claude 正确识别和触发，还能真正完成从“理解需求”到“执行任务”的完整闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqISKVRAgv5dvnkKG57eGFvLqOqeq0XRoLLfYFA32OmcibEVvpNdhLMuw/640?wx_fmt=png&from=appmsg)

### Skills 的价值

通过实际案例，大家可以再次体会到Skills模式带来的价值，也就是我们常说的工作流的迁移一块：

1. **知识的沉淀与复用** ：反复使用的流程被固化为技能，避免重复造轮子；
2. **模块化架构** ：每个技能都是独立的，易于测试、维护和扩展；
3. **无限的可能性** ：通过组合不同技能，可以构建复杂的工作流；
4. `最后也是最关键的，他可以大大提升Tools调用的准确性；`

## unsetunsetClaude Skills安装与使用unsetunset

在Claude Code中，你可以通过以下两种方式使用Skills：

**方法一：使用官方技能市场（推荐）**

```
# 添加官方技能库
/plugin marketplace add anthropics/skills
# 浏览可用技能
/plugin list
# 安装文档处理技能
/plugin install document-skills@anthropic-agent-skills
```

安装完成后，你可以直接询问Claude有哪些技能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqpU7MLjvgMWChcyU3icdXhssyCJ1B65Iun2sRmF6UlG5ayu1GnuFvdWQ/640?wx_fmt=jpeg&from=appmsg)

**方法二：手动创建自定义技能**

如果你想让自己定义一个skills，比如“自动总结抖音视频”，你可以自己编写一个 Skill。原理非常简单：

1. 在用户根目录下的 ~/.claude/skills/ 中创建一个新文件夹，比如 douyin-summary。
2. 编写指令：在文件夹内创建一个 SKILL.md，告诉 Claude 这个技能是干嘛的、怎么用。
3. 准备工具：(可选) 放入 Python 脚本或其他辅助文件。

目录结构看起来是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgq1I86nC3BnB61jPSBia78FvCtwgzfiaku4Kms6r0s720J8ayvSib7mtPibg/640?wx_fmt=png&from=appmsg)

1. **创建技能目录** ：
```
mkdir -p ~/.claude/skills/douyin-summary
```
2. **编写SKILL.md** ：
```
---
name: douyin-summary
description: 抖音视频总结助手。当用户提供抖音视频链接时，自动调用此技能获取文案并总结。
---
# 抖音视频总结助手
## 工作流程
1. 识别用户输入中的douyin.com链接
2. 调用scripts/fetch_douyin.py获取视频文案
3. 提取核心观点并结构化输出
```
3. **实际使用** ：

配置好后，可以查看技能是否安装成功。老版本的Claude code 需要重启才能看到新安装的技能，新版本已经不需要重启了

![](https://mmbiz.qpic.cn/mmbiz_jpg/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqsr6Sqq3X5UTD1AmdgEvaEhzjLxQicmVeXJsRPNAzpwOLY2rseCe7T9g/640?wx_fmt=jpeg&from=appmsg)

使用Claude Skills提取抖音视频内容的效果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgq9qCibacVuibjibvbmy3ovouLYeLibe0HE4jT4wuyrlK8ibHNV8pGWfy6Oyw/640?wx_fmt=png&from=appmsg)

了解了上述基础知识后，我们再看简单知识库如何实现：

## unsetunset基于Skills构建系统unsetunset

Krawl 是我们小伙伴自己取的名字了，很难记的名字，我也不知道他为撒要这么取，单子就是一个知识管理和智能体，它通过 **技能扩展机制** 实现了 AI 与工具的深度集成。其主要目的就是展示如何使用 Skills 技术。

![](https://mmbiz.qpic.cn/mmbiz_png/6Uzn2S5AAyScbxAOqkYtCqjlTgUmyXTKn7g4RHTzIvFYgjbmSr5gHehODfRwPsFfQJIcno2LsbHOaQhywrYFIic11icof09YRrANRv5HiamUqY/640?wx_fmt=png&from=appmsg)

**系统效果展示**

点击右上角"从链接添加"按钮输入需要解析的链接地址，就会自动提取内容：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqTONSc2Qbiad6k6nojWCB8CP8NrV78yAtkIrkWA3g1j6Xr0dAaibzgA3A/640?wx_fmt=png&from=appmsg)

添加完成后，系统会自动提取内容并生成智能总结：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqPm2MSkzwZiboRibErfMj1mUf2yJ6ibatibDjk7gDWOOLJX5Uqib4IWBbTSQ/640?wx_fmt=png&from=appmsg)

### Skills 设计思想

Skills 模式使用很简单：将多媒体内容提取与入库这一复杂流程封装为独立的 `link_ingest` 技能，将知识库检索封装为 `knowledge_query` 技能。

这种模块化的设计的好处是：skill与系统解耦，可移植性就上来了，如果其他项目需要类似能力，只需复制对应的技能文件夹，即可实现能力的即插即用。

### Skills 工作原理

一个完整的skill由三个层级组成，这里和Claude Skills是一样的设计：

1. **元数据（始终加载）** ：告诉AI"有什么技能可用"
2. **指令（触发时加载）** ：告诉AI"如何执行这个技能"
3. **资源与代码（按需加载）** ：实际执行具体任务

在 Krawl 的 skill 系统实现中，我们采用了一种 **"Dynamic Router"（动态路由）** 与 **"Lazy Loading"（按需加载）** 相结合的架构。

这种设计是为了解决随着技能数量增长带来的启动延迟和上下文污染问题，核心原则包括：

1. **懒加载**: 系统启动时只扫描技能的元数据（Markdown Frontmatter），不加载具体的 Python 代码。
2. **元控制**: 系统提供一个核心的 Meta-Tool `load_skill` 。LLM 根据任务需求，自主决定加载哪个技能。
3. **资源隔离** ：技能的代码和工具定义在需要时动态注册到当前会话中。

整体技术架构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqrhoK2K2nKKiaP2woIj2icKOCOfZOAZmR28E2ADyOIljguWnhu8YiaHg6g/640?wx_fmt=png&from=appmsg)

### 核心实现

要实现这样一个动态路由系统，需要几个核心组件的配合。下面我将展示 Krawl 后端的关键代码实现。

**1、技能元数据结构 (Metadata)**

首先，我们需要定义一个轻量级的结构来持有技能信息。它的核心目的是 **占位** ，而不是直接加载代码对象。

```
@dataclass
class SkillInfo:
    """Skill 信息容器 - 核心是 lazy load"""
    name: str
    description: str  # 从 skill.md 的 frontmatter 读取的简短描述
    is_loaded: bool = False  # 标记是否已加载实际代码
    content: str = ""  # skill.md 的完整内容 (Prompt)
    tools: List[Dict[str, Any]] = field(default_factory=list)  # 具体工具定义
    handlers: Dict[str, ToolHandler] = field(default_factory=dict)  # 执行函数
    module_path: str = ""
```

**2、管理器与轻量扫描 (The Manager)**

`SkillManager` 是整个系统的调度中心。它在启动时只做"轻量级扫描"：仅遍历目录并读取 Markdown 的头部描述，不加载任何 Python 代码：

```
class SkillManager:
def scan_skills(self) -> None:
  """轻量级扫描：只读取目录结构和 frontmatter，不加载具体代码"""
  for item in self._skills_dir.iterdir():
    if not item.is_dir() or item.name.startswith("_"):
      continue
    # 仅读取 Frontmatter 描述，不读取全文，保证启动速度
    description = self._read_frontmatter_description(item / "skill.md")
    self._skills[item.name] = SkillInfo(
      name=item.name,
      description=description
    )
```

**3、动态加载机制 (Dynamic Activation)**

这是系统的核心魔法所在。当且仅当 LLM 决定使用某个技能时，我们才通过 `activate_skill` 方法动态加载对应的代码文件：

```
def activate_skill(self, skill_name: str) -> Tuple[bool, str, List[Dict[str, Any]]]:
  """按需激活一个 Skill"""
  skill = self._skills.get(skill_name)
# 1. 命中缓存直接返回
if skill.is_loaded:
      returnTrue, skill.content, skill.tools
# 2. 动态读取 Prompt (skill.md)
  md_path = self._skills_dir / skill_name / "skill.md"
  skill.content = md_path.read_text(encoding="utf-8")
# 3. 动态 Import 代码模块 (execute.py)
# 只有这一步才会真正消耗内存和解释器资源
  module_name = f"app.skills.{skill_name}.execute"
  module = importlib.import_module(module_name)
# 4. 提取并注册工具
  skill.tools = getattr(module, "TOOLS", [])
  skill.handlers = getattr(module, "HANDLERS", {})
  skill.is_loaded = True
# 将新工具注册到活跃列表
for name, handler in skill.handlers.items():
      self._active_handlers[name] = handler

returnTrue, skill.content, skill.tools
```

**4、Meta-Tool 实现 (Meta-Control)**

为了让 AI 能自主控制这个过程，我们需要把 `load_skill` 暴露给 LLM。这是它唯一自带的"初始技能"（Meta-Tool），用于发现和加载其他技能：

```
async def _handle_load_skill(self, args: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
"""Meta-Tool: 允许 LLM 自行加载新能力"""
  skill_name = args.get("skill_name")
  success, content, tools = self.activate_skill(skill_name)
if success:
    tool_names = [t["name"] for t in tools]
    return {
        "ok": True,
        # 关键：告诉 LLM 加载成功，并把 Manual (skill.md) 返回给它学习
        "message": f"Skill '{skill_name}' loaded.",
        "manual": content, 
        "new_tools": tool_names
    }
return {"ok": False, "error": content}
```

## unsetunset流程梳理unsetunset

为了让大家更清楚地理解这套系统是如何运转的，我们以“用户想要保存一个抖音视频”为例，拆解整个交互流程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Uzn2S5AAyQ2SR54gFZswsGbibgJCXDKibp1ES1BNS8EXOLj97ql6yjIia8fc9vj0icXT2ibMnlibIJCXwRrHPoutan9nVwcicgpT1pbWtBKvWrVwE/640?wx_fmt=png&from=appmsg)

**场景** ：用户发送消息 "帮我保存这个视频 https://v.douyin.com/xxxxx"

### 1、系统初始化

系统启动时， **SkillManager** 扫描 **skills** 目录。

- 它只读取 **skill.md** 的头部信息（名称和描述）。
- **结果** ：系统知道有 **link\_ingest** 这个技能，但还没有加载它的代码，内存占用极低。

### 2、意图识别与路由

用户的消息发送给 LLM。此时 System Prompt 中包含了一份"技能菜单"：

```
Available Skills:
- link_ingest: 链接内容提取技能...
- knowledge_query: 知识库查询...
```

LLM 分析用户意图："用户想保存视频，这匹配 **link\_ingest** 的描述"。 **决策** ：LLM 决定调用 Meta-Tool: **load\_skill(skill\_name="link\_ingest")**

### 3、动态加载与注册

系统接收到 **load\_skill** 请求：

1. 读取 **link\_ingest/skill.md** 的完整内容（作为操作手册）。
2. 动态 import **link\_ingest/execute.py** 。
3. 将 **execute.py** 中定义的工具 **save\_link\_knowledge** 注册到当前会话的工具列表中。

**返回给 LLM** ：

```
Skill 'link_ingest' loaded.
Manual: (skill.md 的内容...)
```

#### 4、执行具体任务

LLM 收到了加载成功的消息，并阅读了刚才返回的 Manual。 Manual 告诉它："要保存链接，请调用 **save\_link\_knowledge(url=...)** "。

**决策** ：LLM 再次发起工具调用 \*\*save\_link\_knowledge(url="https://v.douyin.com/xxxxx")\*\*。

系统执行对应的 Python 函数，下载视频、提取字幕、存入数据库，并返回结果：

```
{"ok": true, "title": "抖音视频...", "id": 101}
```

### 5、最终响应

LLM 根据工具返回的结果，组织自然语言回复用户：

"视频已保存！标题是《...》，已归档到视频分类中。"

理解流程后，就进入关键skill实现了：

## unsetunset关键skill实现unsetunset

首先是 **link\_ingest** ，链接内容提取技能：

这是Krawl最核心的skill，也是我在前言中提到的痛点的直接解决方案：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqpFvp3eOZ3zia1qnOxnmBZeAOqrotWLCEFzqzS46aNdaOqjZcl8mDqibg/640?wx_fmt=png&from=appmsg)

为了配合这个系统，每个 Skill 的脚本 (**execute.py**) 必须遵循标准协议。以 **link\_ingest** 为例：

```
# app/skills/link_ingest/execute.py
# 1. 工具定义 - 告诉 LLM 这个技能能做什么
TOOLS = [
{
"name": "save_link_knowledge",
"description": "将链接内容保存到知识库...",
"parameters": {
    "type": "object",
    "properties": {
      "url": {"type": "string"},
      "category": {"type": "string"}
    },
    "required": ["url"]
  }
}
]
# 2. 工具实现 - 实际的处理逻辑
asyncdef save_link_knowledge(args: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
  url = args.get("url")
# ... 业务逻辑 ...
# 调用 Service 层处理
return {"ok": True, "id": 123}

# 3. 处理器映射 - (系统自动注册到路由表)
HANDLERS = {
"save_link_knowledge": save_link_knowledge
}
```

然后是 **knowledge\_query** ，知识库查询skill,当用户提问时，这个技能会被自动调用：

![](https://mmbiz.qpic.cn/mmbiz_png/JdfjlwvwuTCFD1QL46wbKfVnGoZibrpgqeZgc6gLGm7NZ6S9NZLt0CDZvmBuuzGzKxplFrMpZVZn4IytYSTZkCQ/640?wx_fmt=png&from=appmsg)

```
# 工具定义（供 loader 读取，传给大模型）
TOOLS = [
{
"name": "search_knowledge",
"description": "搜索用户的个人知识库，查找与用户问题相关的已保存内容。支持单个查询或多个查询。当用户询问已保存的知识、提问关于之前保存的内容时使用。",
"parameters": {
    "type": "object",
    "properties": {
      "query": {
          "type": "string",
          "description": "搜索关键词或问题（单个查询，与 queries 二选一）"
      },
      "queries": {
          "type": "array",
          "items": {"type": "string"},
          "description": "多个搜索关键词或问题（多个查询，与 query 二选一）"
      },
      "top_k": {
          "type": "integer",
          "description": "每个查询返回最相关的结果数量，默认3个，最多10个",
          "default": 3,
      },
    },
    "required": [],
  },
},
]
async def search_knowledge(args: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
"""搜索知识库内容，支持单个或多个查询。"""
    return {"ok": true,"content":"content"}
# 工具名称到处理函数的映射
HANDLERS = {
"search_knowledge": search_knowledge,
}
```

至此，一个简单的skill就实现了，最后聊聊Skills的“最佳实践”吧：

## unsetunset结语unsetunset

通过Krawl项目的实践，我总结了Skills模式的几个典型适用场景：

1. **重复性工作流** ：将重复的AI交互流程固化为skill；
2. **工具集成** ：需要AI调用外部工具或API的场景；
3. **复杂任务分解** ：将复杂任务分解为多个可复用的子skill；
4. **多用户共享能力** ：在团队或社区中共享AI能力；

在具体实施过程要注意： `从简单开始` 。不要一开始就构建复杂的系统，先做一个能解决具体问题的小skill，验证思路。

其次就是skill的 `粒度把握` 了：

1. skill不宜过大：一个skill应该只做一件事；
2. skill不宜过小：避免skill爆炸，难以管理；
3. 建议：按业务领域划分技能，每个skill对应一个完整的用户故事；

最后，是错误处理与监控

1. 为每个skill设计明确的错误处理机制；
2. 记录skill使用日志，便于调试和优化；
3. 考虑skill版本管理，支持回滚；

在 Krawl 项目中，Skills 让 AI 成为了一个可以主动调用工具、完成实际任务的智能助手。这种"技能化"的思想，值得在更多的项目中应用和实践。

相信通过这个案例，大家对Skills更为了解了，如果有帮助的话，可以给我点个赞哦！

**点击上方卡片关注叶小钗公众号**

继续滑动看下一个

叶小钗

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过