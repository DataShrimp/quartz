---
title: Transformer架构详解：注意力机制原理与最新演进
description: 深入解析Transformer架构核心原理，包括注意力机制QKV、Tokenization序列化、Encoder/Decoder模型分类、Scaling Law，以及稀疏注意力、线性注意力和突破性新架构。
tags:
  - LLM
  - Transformer
  - Attention
  - 深度学习
  - AI
date: 2026-01-05
aliases:
  - Transformer
  - 注意力机制
  - Attention Mechanism
---



> Transformer 本质是注意力机制（*"Attention is All You Need"*）。

本文是 [[IntroduceLLM|LLM技术全景系列]] 的第一篇，聚焦于大语言模型的基础架构——Transformer。

![[transformer_attention_mechanism.png|Transformer注意力机制原理：展示了Query、Key、Value的三维空间映射及多头注意力并行计算结构]]

---

## 注意力机制原理

注意力计算的本质是在训练阶段将 token（词向量或图块等）映射到 Query、Key 和 Value 的三维空间中：

|   维度    | 含义     | 直觉理解                                         |
| :-------: | :------- | :----------------------------------------------- |
| **Query** | 查询维度 | 为了获取相关的上下文，我应该关注什么？           |
|  **Key**  | 特征维度 | 我包含了什么特征，以便更好地与查询词匹配相关性？ |
| **Value** | 信息维度 | 如果相关，我该提供什么信息量？                   |

此外，Transformer 还引入了两个关键设计：

- **多头注意力（Multi-Head Attention）**：并行计算多组 QKV，让模型捕捉不同维度的特征（如语法 vs 语义）。
- **位置编码（Positional Encoding）**：弥补注意力机制本身无法感知序列顺序的缺陷，标记 Token 的位置信息。

正是这种**数据依赖捕获能力**在表达上的通用性，Transformer 架构逐渐替代了 RNN/CNN 并实现更好的泛化能力。但代价是需要"大力出奇迹"——当数据量足够多，通过 **Scaling Law**（模型性能与计算量/参数/数据量呈幂律关系）预训练，其涌现的智能上限远超传统模型。

---

## 序列化与并行计算

注意力的优势是 **"一切信息皆可序列化"**，前提是设计合理的"切块"和"分词"（Tokenization）方法。

将多模态信息（文本、图像、语音、视频、3D 等）序列化后用 Transformer 搭建神经网络模型，计算转为统一的矩阵计算：

$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

通过专用计算设备（如 GPU/TPU）实现 **并行计算** 和 **长距离依赖**。

---

## 模型架构分类

根据任务需求，Transformer 的组装方式一般分为三类：

|      架构类型       | 代表模型 | 擅长任务     | 典型应用                 |
| :-----------------: | :------: | :----------- | :----------------------- |
|  **Decoder-Only**   | GPT 系列 | 生成任务     | 文本生成、对话、代码补全 |
|  **Encoder-Only**   |   BERT   | 理解任务     | 文本分类、情感分析、NER  |
| **Encoder-Decoder** | T5, BART | Seq2Seq 任务 | 机器翻译、摘要生成       |

---

## 注意力的局限

标准注意力机制的主要瓶颈是其计算复杂度随序列长度呈二次方增长（$O(N^2)$），这限制了长文本序列的处理能力。

改进思路主要有三个方向：

### 稀疏注意力机制

**核心思想**：并非所有 token 都需要两两交互，通过掩码（mask）屏蔽不必要的计算，只计算关键位置的注意力分数。

"关键位置"的定义策略：

- **固定间隔**：如 SparseTransformer
- **Top-K 动态选择**：如 MInference
- **自适应扩张**：如 LongNet

### 线性注意力机制

**核心思想**：对标准注意力 $\text{Softmax}(QK^T)V$ 进行线性近似，将 $N \times N$ 矩阵运算近似为 $Q(K^TV)$，使计算复杂度从 $O(N^2)$ 降为 $O(N)$。

近似方法：

- **核近似**：如 Performer
- **遗忘机制**：如 RetNet、Mamba

### 无限注意力机制

**核心思想**：结合局部 Masked Attention 和长期压缩记忆的混合机制。

这是 Google Gemini 系列大模型实现 **100 万 Token 上下文窗口** 和高细节召回率的关键技术，也是工业界主流方案。其实现原理为：

- 局部使用标准注意力
- 将旧的 KV 状态写入压缩记忆矩阵
- 复用注意力机制的 Q、K、V 进行写入和检索

---

## 未来：突破 Transformer

上述改进都是微观层面对注意力机制的优化，而最新研究已在探索如何 **突破 Transformer 架构本身**。典型工作包括：

### Monarch Mixer (M2) — Stanford

除了序列长度的二次方复杂度，模型维度同样面临复杂度瓶颈。M2 架构通过 **Monarch 矩阵**（可看作快速傅里叶变换推广的结构化矩阵）替代 Attention+MLP 的稠密矩阵，在更少参数、更快速度的情况下匹配 Transformer 性能。

### Titans — Google

提出 **神经长期记忆模块**：将长期记忆看作一个深层神经网络，当模型处理新数据时，若梯度足够大（意味着有意料之外的信息），则更新记忆模块。同时引入动量机制累计短期记忆，以及遗忘机制擦除旧记忆。记忆块可作为上下文、门控分支或独立层与神经网络结合。

### mHC — DeepSeek

解决深层神经骨干网络中 ResNet 通道宽度受限于隐藏层维度、从而限制模型潜力的问题。提出将残差连接矩阵投影到 **Birkhoff 多胞形**（双拟随机矩阵流形），通过 Sinkhorn-Knopp 算法使信息传播变成特征的"凸组合"，保证信号范数稳定性，解决梯度爆炸问题。

目前，Titans 和 mHC 架构已在工业实践中得到初步验证，大模型的演进仍在继续。

---

## 相关阅读

- [[Introduce Diffusion|扩散模型入门]] — 图像生成的核心技术

---

## 参考文献

1. Vaswani, A., et al. (2017). *Attention Is All You Need*. NeurIPS. [[arXiv:1706.03762](https://arxiv.org/abs/1706.03762)]
2. Devlin, J., et al. (2019). *BERT: Pre-training of Deep Bidirectional Transformers*. NAACL. [[arXiv:1810.04805](https://arxiv.org/abs/1810.04805)]
3. Brown, T., et al. (2020). *Language Models are Few-Shot Learners* (GPT-3). NeurIPS. [[arXiv:2005.14165](https://arxiv.org/abs/2005.14165)]
4. Kaplan, J., et al. (2020). *Scaling Laws for Neural Language Models*. [[arXiv:2001.08361](https://arxiv.org/abs/2001.08361)]
5. Child, R., et al. (2019). *Generating Long Sequences with Sparse Transformers*. [[arXiv:1904.10509](https://arxiv.org/abs/1904.10509)]
6. Choromanski, K., et al. (2021). *Rethinking Attention with Performers*. ICLR. [[arXiv:2009.14794](https://arxiv.org/abs/2009.14794)]
7. Gu, A., & Dao, T. (2023). *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*. [[arXiv:2312.00752](https://arxiv.org/abs/2312.00752)]
8. Munkhdalai, T., et al. (2024). *Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention*. [[arXiv:2404.07143](https://arxiv.org/abs/2404.07143)]
9. Fu, D., et al. (2023). *Monarch Mixer: A Simple Sub-Quadratic GEMM-Based Architecture*. NeurIPS. [[arXiv:2310.12109](https://arxiv.org/abs/2310.12109)]
10. Behrouz, A., et al. (2025). *Titans: Learning to Memorize at Test Time*. [[arXiv:2501.00663](https://arxiv.org/abs/2501.00663)]
11. Xie Z, et al. (2025). *mHC: Multilevel Hadamard Convolution for Deep Neural Networks*. [[arXiv:2512.24880](https://arxiv.org/abs/2512.24880)]