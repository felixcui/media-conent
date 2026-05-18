# Agentic Memory：详细拆解

**来源**: https://waytoagi.feishu.cn/wiki/NP8QwegILi0vU6kwTClcRdiEncc

---

## 摘要

第一天，她表现惊艳，能抓出每一个 bug，文档写得干净利落，甚至还提出了你没想到的改进建议。核心想法很简单：记忆不是只做一件事；它同时承担三类非常不同的任务。第二天，你走进去说：“嘿，还记得我们昨天讨论的那个问题吗。

---

## 正文

<quote-container>
原帖链接：https://x.com/techwith_ram/status/2037499938574110770
</quote-container>



想象有一天，你雇了一位非常厉害的自由职业者。第一天，她表现惊艳，能抓出每一个 bug，文档写得干净利落，甚至还提出了你没想到的改进建议。你很满意。
第二天，你走进去说：“嘿，还记得我们昨天讨论的那个问题吗？”
她停了一下，看着你，微微一笑。
“抱歉……哪个问题？”
没有记忆。没有上下文。彻底消失了。写到这里时，我和你一样会被这件事震住。
这正是大多数 LLM 的行为方式。每一段新对话都是一次全新的开始。模型不知道你是谁，不知道你们一起构建过什么，也不知道你们几分钟前在另一个聊天窗口里讨论了什么。
对于一个简单的聊天机器人来说，这没问题。但对于一个 agent，也就是能够执行任务、做决策并随时间改进的系统来说，这种失忆是致命缺陷。
因为真正的智能不只是回答得好。它还意味着记得、学习，并在过去的基础上继续推进。
记忆把一个无状态系统变成了真正能够演化的系统。
# Agentic Memory 到底是什么？
Agentic Memory 不是单一组件。它更像是一套在幕后运行的系统，由不同类型的存储、信息检索方式，以及管理它们的策略组成，让 agent 真正能够在时间维度上延续上下文。
核心想法很简单：记忆不是只做一件事；它同时承担三类非常不同的任务。
➜ **连续性**关乎身份。它让 agent 知道你是谁、你偏好什么、你们已经一起构建过什么。没有它，每次交互都会像从零开始。
➜ **上下文**关乎当前任务。刚刚发生了什么、调用了哪个工具、返回了什么结果、下一步应该做什么。它让多步骤 workflow 不至于中途散架。
➜ **学习**关乎变得更好。理解什么有效、什么无效，并随着时间逐步改进决策，而不是一遍遍犯同样的错误。
这三者结合在一起，会让 agent 在每次交互中都显得更一致、更可靠，也更聪明一点。


设计良好的 agent 记忆系统会同时处理这三件事，并针对每类需求使用不同的存储后端。
# 4 类记忆
这个领域已经逐渐收敛到四类不同的记忆。你可以把它们看成大脑里的四个区域，每个区域都为特定任务演化而来。


## 1. 上下文内记忆
上下文窗口就是 agent 的工作台。放在上面的所有东西都能被即时访问。模型可以在一次 forward pass 里对它进行推理，不需要额外的检索步骤。
但这张工作台有尺寸限制。每个 token 都会带来成本和延迟。而一旦 session 结束，工作台就会被清空。
上下文里通常放什么？
- **System prompt：** agent persona、规则、能力、当前日期/用户信息
- **对话历史：** 当前 session 到目前为止的来回交互
- **工具调用结果：** agent 刚刚调用工具得到的输出
- **检索到的记忆：** 从外部存储拉回来的内容片段
- **Scratchpad：** 中间推理内容，例如 think-step-by-step 输出



**滑动窗口问题**
在长对话中，历史会不断累积，最终溢出上下文限制。最朴素的方案是截断最早的消息，但这会丢掉重要的早期上下文。更好的策略包括：
- **压缩概括**：定期把旧轮次压缩成一段简短概述，并用这段概述替换原始内容
- **选择性保留**：保留包含关键事实、决策或工具结果的轮次；丢弃闲聊
- **卸载到外部记忆**：把重要事实抽取到向量存储中，需要时再检索回来
## 2. 外部记忆
外部记忆是指任何持久化在模型之外的东西，比如数据库、向量存储、键值存储和文件。它能跨越 session 边界。只要存得好，你的 agent 可以记住六个月前的事情。
外部存储有两种主要形式：
**结构化存储（精确查找）：** PostgreSQL、Redis、SQLite。你通过 key、ID 或 SQL 查询。它快速、可预测，很适合用户 profile、偏好和结构化数据。
**向量存储（语义搜索）：** Pinecone、Chroma、pgvector。你按语义查询，比如“找到和这个概念相似的记忆”。它对非结构化笔记和情景回忆非常关键。


检索步骤是一个**瓶颈**。如果没有检索到正确的记忆，agent 的行为就会像那些记忆不存在一样。好的记忆架构，20% 在存储，80% 在检索设计。
## 3. 情景记忆
情景记忆是最容易被低估的一类记忆。外部记忆存储事实，而情景记忆存储事件，具体来说，是过去行动的结果。
最简单的形式是一份结构化日志：每当 agent 完成一个任务，就记录发生了什么。随着时间推移，这份日志会变成 agent 的自我知识来源，让它在做决策之前可以先查阅过去经验。
一个 episode 大概长这样：
```json
{
  "episode_id": "ep_20240315_003",
  "timestamp": "2024-03-15T14:23:11Z",
  "task": "Summarize 50-page PDF into 3 bullet points",
  "approach": "Sequential chunking, 2000 tokens per chunk",
  "outcome": "success",
  "duration_ms": 4820,
  "token_cost": 12400,
  "quality_score": 0.91,
  "notes": "Worked well. Hierarchical chunking would be faster.",
  "embedding": [0.023, -0.441, 0.182, /* ... 1536 dims */]
}

```

当一个新任务进来时，agent 会检索语义上最相似的过去 episodes，并用它们来选择策略。这本质上是**基于个人历史的 few-shot learning**，而不是基于手工构造的数据集。
**反思循环**👇


## 4. 语义/参数记忆
这是模型“天生”拥有的记忆。所有内容都在训练过程中编码进权重里：关于世界的事实、语言模式、推理策略、编码约定，以及文化知识。
它始终存在。agent 永远不需要检索它。但它有很硬的限制：
- **冻结在训练时刻：** 模型不知道 cutoff date 之后发生了什么
- **无法在运行时更新：** 不经过重新训练或 fine-tuning，你无法注入新的永久事实
- **不透明：** 你无法准确检查模型到底“知道”什么或不知道什么
- **容易幻觉：** 模型会用看起来合理但实际错误的补全来填补空白
对于任何时效性强、领域特定或私有的信息，**不要依赖参数记忆**。使用外部检索。参数记忆适合作为通用世界知识的 fallback，前提是没有更好的来源。
正确的心智模型是：参数记忆是 agent 的通识教育。外部记忆、情景记忆和上下文内记忆是 agent 的**在岗经验**。最好的 agent 会把两者结合起来。
# 记忆如何流经 agent loop？
现在把它们放到一起看。每当 agent 处理一个请求时，下面这些事情都会发生，每套记忆系统都会参与其中。


注意，记忆操作位于 LLM 调用的前后两端：调用前检索，调用后写入。模型本身是无状态的；真正制造出“有状态、能感知”的 agent 体验的，是记忆系统。
# 构建记忆层
我们来构建它。这里使用 **Python**，用 **OpenAI** 做 embeddings，用 **ChromaDB** 作为本地向量存储。相同概念适用于任何其他技术栈，只需要替换库即可。
我们来构建它。这里使用 **Python**，用 **OpenAI** 做 embeddings，用 **ChromaDB** 作为本地向量存储。相同概念适用于任何其他技术栈，只需要替换库即可。
```bash
pip install chromadb openai anthropic python-dotenv
```

## MemoryStore class
它负责写入记忆（包含 embeddings）和语义检索，是其他所有东西的基础。
```python
import chromadb
from openai import OpenAI
from datetime import datetime
import json, uuid

class MemoryStore:
    """Persistent vector memory for an AI agent."""

    def __init__(self, agent_id: str, persist_dir: str = "./memory_db"):
        self.agent_id = agent_id
        self.openai = OpenAI()

        # ChromaDB stores vectors on disk, persists across restarts
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(
            name=f"agent_{agent_id}_memories",
            metadata={"hnsw:space": "cosine"}  # cosine similarity
        )

    def _embed(self, text: str) -> list[float]:
        """Convert text to embedding vector using OpenAI."""
        response = self.openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    def remember(
        self,
        content: str,
        memory_type: str = "general",
        metadata: dict = None
    ) -> str:
        """Store a memory. Returns the memory ID."""
        memory_id = str(uuid.uuid4())
        embedding = self._embed(content)

        meta = {
            "type": memory_type,
            "timestamp": datetime.utcnow().isoformat(),
            "agent_id": self.agent_id,
            **(metadata or {})
        }

        self.collection.add(
            ids=[memory_id],
            embeddings=[embedding],
            documents=[content],
            metadatas=[meta]
        )
        return memory_id

    def recall(
        self,
        query: str,
        k: int = 5,
        memory_type: str = None,
        min_relevance: float = 0.6
    ) -> list[dict]:
        """Retrieve the k most relevant memories for a query."""
        query_embedding = self._embed(query)

        where = {"type": memory_type} if memory_type else None

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=where,
            include=["documents", "metadatas", "distances"]
        )

        memories = []
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            relevance = 1 - dist  # cosine distance → similarity
            if relevance >= min_relevance:
                memories.append({
                    "content": doc,
                    "metadata": meta,
                    "relevance": round(relevance, 3)
                })

        return sorted(memories, key=lambda x: x["relevance"], reverse=True)

    def forget(self, memory_id: str):
        """Delete a specific memory (GDPR compliance, stale data, etc.)"""
        self.collection.delete(ids=[memory_id])

```

## EpisodicLogger class
现在在上面加一层 episode logging。
```python
from .store import MemoryStore
from dataclasses import dataclass, asdict
from typing import Optional
import time

@dataclass
class Episode:
    task: str
    approach: str
    outcome: str           # "success" | "partial" | "failure"
    duration_ms: int
    token_cost: int
    quality_score: float   # 0.0 – 1.0, set by evaluator or user
    notes: str = ""
    error: Optional[str] = None

class EpisodicLogger:
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store

    def log(self, episode: Episode):
        """Save an episode to memory as a searchable document."""
        # Build a rich text representation for semantic search
        doc = (
            f"Task: {episode.task}\n"
            f"Approach: {episode.approach}\n"
            f"Outcome: {episode.outcome}\n"
            f"Notes: {episode.notes}"
        )
        self.store.remember(
            content=doc,
            memory_type="episode",
            metadata={
                "outcome": episode.outcome,
                "quality_score": episode.quality_score,
                "duration_ms": episode.duration_ms,
                "token_cost": episode.token_cost,
            }
        )

    def recall_similar(self, task: str, k: int = 3) -> list[dict]:
        """Find past episodes similar to the current task."""
        return self.store.recall(
            query=task,
            k=k,
            memory_type="episode",
            min_relevance=0.65
        )

```

## 放到一起：一个带记忆增强的 agent
```python
import anthropic
from memory.store import MemoryStore
from memory.episodic import EpisodicLogger, Episode
import time

class MemoryAugmentedAgent:
    def __init__(self, agent_id: str):
        self.client = anthropic.Anthropic()
        self.memory = MemoryStore(agent_id)
        self.episodes = EpisodicLogger(self.memory)

    def _build_memory_context(self, user_message: str) -> str:
        """Retrieve relevant memories and format them for injection."""
        # Semantic search for related facts
        memories = self.memory.recall(user_message, k=4)
        # Similar past task approaches
        episodes = self.episodes.recall_similar(user_message, k=2)

        context_parts = []

        if memories:
            context_parts.append("## Relevant memories\n" +
                "\n".join([
                    f"- [{m['metadata']['type']}] {m['content']}"
                    f" (relevance: {m['relevance']})"
                    for m in memories
                ])
            )

        if episodes:
            context_parts.append("## Past similar tasks\n" +
                "\n".join([
                    f"- {e['content'][:200]}..."
                    for e in episodes
                ])
            )

        return "\n\n".join(context_parts) if context_parts else ""

    def run(self, user_message: str) -> str:
        start = time.time()

        # 1. Retrieve relevant memory
        memory_context = self._build_memory_context(user_message)

        # 2. Build system prompt with injected memory
        system = """You are a helpful agent with memory.
You have access to relevant context from past interactions.
Use this context to give better, more personalized responses.
"""
        if memory_context:
            system += f"\n\n{memory_context}"

        # 3. Call the model
        response = self.client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": user_message}]
        )
        answer = response.content[0].text
        duration = int((time.time() - start) * 1000)

        # 4. Save useful info to memory for next time
        self.memory.remember(
            content=f"User asked: {user_message[:200]}",
            memory_type="interaction"
        )

        # 5. Log the episode
        self.episodes.log(Episode(
            task=user_message[:200],
            approach="single-turn with memory retrieval",
            outcome="success",
            duration_ms=duration,
            token_cost=response.usage.input_tokens + response.usage.output_tokens,
            quality_score=1.0,  # would come from evaluation in prod
        ))

        return answer

```

# 向量数据库
它是任何严肃记忆系统的核心。不同于 SQL 那样按精确匹配查询，向量数据库会在高维空间里寻找一个向量的**最近邻**。这让语义搜索成为可能：即使记忆之间没有共享词汇，也能找到概念相关的内容。
## 相似度搜索如何工作
每条记忆都会被转换成一个**向量**，也就是由 OpenAI embedding model 生成的 1,536 个浮点数组成的数组。概念相近的文本会产生相近的向量。查询时，你先对 query 做 embedding，然后用**余弦相似度**找到最接近的向量。
```python
import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    1.0  = identical meaning
    0.0  = unrelated
    -1.0 = opposite meaning
    """
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Example: these two sentences will have high similarity
embedding_a = embed("The user prefers dark mode")
embedding_b = embed("They like their interface theme to be dark")
score = cosine_similarity(embedding_a, embedding_b)
# → ~0.91 (very similar)

```

本地开发可以从 **ChromaDB** 开始。准备部署时，如果你已经在使用 Postgres，可以评估 **pgvector**，几乎不需要额外基础设施。需要更大规模时，再考虑 Pinecone 或 Qdrant。
# 记忆管理
真实的记忆系统不能只是一味累积。它们需要被整理和筛选。一个不断增长、缺乏焦点的存储会随着时间退化：检索噪声变多，延迟上升，互相矛盾的记忆也会让 agent 困惑。
你需要一套遗忘策略。下面是三种主要方法：
## 1. 基于时间的衰减
越旧的记忆，相关性通常越低。可以用新近程度和语义相关性共同给记忆打分。研究中常用的公式如下：
```python
import math
from datetime import datetime

def memory_score(
    relevance: float,      # cosine similarity 0–1
    importance: float,     # stored at write time 0–1
    created_at: datetime,  # when memory was formed
    recency_weight: float = 0.3,
    decay_factor: float = 0.995
) -> float:
    """
    Inspired by the Generative Agents paper (Park et al., 2023).
    Balances: how relevant, how important, how recent.
    """
    hours_old = (datetime.utcnow() - created_at).total_seconds() / 3600
    recency = math.pow(decay_factor, hours_old)

    return (
        relevance * 0.4 +
        importance * 0.3 +
        recency * recency_weight
    )

```

## 2. 写入时的重要性评分
存储一条记忆时，让模型自己判断这条信息是否重要。只保存高分内容。这样可以在源头过滤噪声。
```python
import re

async def score_importance(client, content: str) -> float:
    """Ask the LLM if information is worth saving (0.0 to 1.0)."""
    
    prompt = f"""Rate the importance of saving this for future interactions. 
    0.0 = trivial (greeting)
    0.5 = moderately useful
    1.0 = critical (preferences, errors, decisions)
    
    Information: {content}
    Reply with ONLY the number."""

    try:
        response = await client.messages.create(
            model="claude-3-haiku-20240307", # Use the current available Haiku model
            max_tokens=10,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract the first string that looks like a float/int
        text = response.content[0].text.strip()
        match = re.search(r"[-+]?\d*\.\d+|\d+", text)
        
        if match:
            score = float(match.group())
            return max(0.0, min(1.0, score))
            
    except Exception:
        pass 
        
    return 0.5  # Default fallback

```

## 3. 定期整合
运行一个 nightly job，把重复或高度相似的记忆合并成一条规范化概述。这类似于人类睡眠时对记忆的整合。
```python
async def consolidate_memories(store: MemoryStore, similarity_threshold: float = 0.92):
    """Efficiently merge near-duplicate memories using vector search."""
    
    all_mems = store.collection.get(include=["documents", "embeddings", "ids"])
    if not all_mems["ids"]:
        return

    visited = set()
    consolidated_docs = []

    for i, (mem_id, doc, emb) in enumerate(zip(
        all_mems["ids"], all_mems["documents"], all_mems["embeddings"]
    )):
        if mem_id in visited:
            continue
            
        # Use the vector store's built-in search to find neighbors
        # this is much faster than a manual nested loop
        results = store.collection.query(
            query_embeddings=[emb],
            n_results=10, # Adjust based on expected density
            include=["documents", "distances"]
        )

        # Identify group members (1.0 - distance = cosine similarity)
        group = [doc]
        visited.add(mem_id)

        for res_id, res_doc, dist in zip(results["ids"][0], results["documents"][0], results["distances"][0]):
            sim = 1.0 - dist
            if res_id != mem_id and res_id not in visited and sim >= similarity_threshold:
                group.append(res_doc)
                visited.add(res_id)

        # Process the group
        if len(group) > 1:
            summary = await summarize_group(group) # Likely needs to be async
            consolidated_docs.append(summary)
        else:
            consolidated_docs.append(doc)

    # Atomic-ish replacement: Clear and Re-populate
    store.collection.delete(where={})
    for doc in consolidated_docs:
        await store.remember(doc)

```

# 最后的思考
说到底，记忆会让 AI 不再只是一个工具，而更像一个协作伙伴。没有记忆，每次交互都从零开始。有了记忆，agent 就能理解、适应，并随着时间改进。
真正的力量不只在模型里，也在于你如何设计：模型应该记住什么、遗忘什么，以及如何使用这些信息。
把记忆层设计好，其他一切都会变得更聪明。
**代码由 AI 生成。**
**关注** @techwith_ram，获取更多类似内容。