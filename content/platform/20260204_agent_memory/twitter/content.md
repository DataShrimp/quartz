# Twitter Thread: Agent Memory Systems

---

## English Version

### T1 (Hook)
I spent months studying how AI Agents handle memory.

Here's the brutal truth: 90% of agents fail because they treat memory as an afterthought.

The architecture that works 👇🧵

### T2 (The Formula)
Silicon Intelligence = Memory + Cognition + Planning

Memory is the foundation.

Without it, there's no continuous reasoning.

### T3 (Short-term Memory)
**Short-term memory = Context Window**

It's not just text storage.

It's the agent's perception window:
- Prior knowledge about current environment
- Dynamic attention weighting

This is why Context Engineering matters.

### T4 (Long-term Memory Types)
Long-term memory needs structure.

Three types, like a database:

📅 Episodic → Event logs (what happened)
🧠 Semantic → Knowledge graphs (facts)
⚙️ Procedural → Skills (how to do things)

### T5 (The Skills Insight)
Hot take:

The "Skills" everyone is hyping?

It's just **externalized procedural memory**.

Instead of making LLMs "remember" how to call APIs, give them an executable manual.

### T6 (MemGPT Architecture)
MemGPT got this right:

- Context Window = RAM (fast, limited)
- External DB = Disk (slow, unlimited)
- Agent decides when to read/write

This is the prototype of LLM-as-OS.

### T7 (Forgetting is a Feature)
Counterintuitive but true:

**Forgetting is a feature, not a bug.**

Memory retrieval keys:
- Recency
- Relevance
- Importance

Use TTL policies. Clear the noise. Stay efficient.

### T8 (Summary)
TL;DR:

✅ Short-term = Context Window (perception)
✅ Long-term = Episodic + Semantic + Procedural
✅ Skills = Externalized procedural memory
✅ Forgetting = Necessary for efficiency
✅ MemGPT pattern = LLM as OS

### T9 (CTA)
The future isn't about bigger models.

It's about **lightweight, tool-augmented cognition**.

Travel light.

Follow @datashrimp for more on Agent architecture.

Full breakdown: [blog link]

---

## 中文版本

### T1 (Hook)
我花了几个月研究 AI Agent 的记忆系统。

残酷的事实：90% 的 Agent 失败，是因为把记忆当成了附属品。

真正有效的架构长这样 👇🧵

### T2 (公式)
硅基智能 = 记忆存储 + 认知处理 + 规划能力

记忆是地基。

没有记忆，就没有连续的推理。

### T3 (短期记忆)
**短期记忆 = Context Window**

它不只是文本存储。

它是 Agent 的感知窗口：
- 提供当前环境的先验知识
- 动态调整注意力权重

这就是为什么 Context Engineering 很重要。

### T4 (长期记忆类型)
长期记忆需要结构化设计。

像数据库一样分三类：

📅 情景记忆 → Event Log（发生了什么）
🧠 语义记忆 → Knowledge Graph（事实知识）
⚙️ 程序记忆 → Skills（怎么做）

### T5 (Skills 洞察)
一个观点：

大家都在吹的 "Skills"？

本质是**外挂的程序记忆**。

与其让大模型"记住"怎么调用 API，不如直接给它一本可执行的操作手册。

### T6 (MemGPT 架构)
MemGPT 的设计很精妙：

- Context Window = 内存 RAM（快但有限）
- 外部数据库 = 硬盘 Disk（慢但无限）
- Agent 自主决定何时读写

这就是 LLM-as-OS 的雏形。

### T7 (遗忘是特性)
反直觉但正确：

**遗忘是 Feature，不是 Bug。**

记忆检索的三个关键指标：
- 新近性 (Recency)
- 相关性 (Relevance)
- 重要性 (Importance)

用 TTL 策略清理噪音，保持高效。

### T8 (总结)
划重点：

✅ 短期记忆 = Context Window（感知）
✅ 长期记忆 = 情景 + 语义 + 程序
✅ Skills = 外挂的程序记忆
✅ 遗忘 = 效率的必要条件
✅ MemGPT 模式 = LLM 作为操作系统

### T9 (CTA)
未来不是堆更大的模型。

而是**轻量化的工具增强型认知**。

轻装前行。

关注 @datashrimp 获取更多 Agent 架构干货。

完整解析：[博客链接]



![[封面大图.png]]


![[记忆类型对比图.png]]


![[memgpt_架构图.png]]
