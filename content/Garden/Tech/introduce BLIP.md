---
title: BLIP 系列：多模态理解与生成的统一之路
description: 深入解析 BLIP、BLIP-2 和 InstructBLIP 的核心原理与技术演进
tags:
  - AI
  - 多模态
  - BLIP
  - VLM
date: 2025-12-12
---

[[Introduce ViT&CLIP|上篇文章]] 详细介绍了如何通过 ViT 将图像模态编码到类似自然语言的 Transformer 架构中，并且基于 CLIP 对比学习对齐两个模态。

这也意味着，不论是图像还是文本，它们在"知识"这个更高维度或许是相通的。这也带来了新问题：

> 除了**理解**多模态内容，能否在**生成**任务中复用这些能力？

---

## BLIP：理解与生成的统一

2022 年，Salesforce Research 提出了 **BLIP**（Bootstrapping Language-Image Pre-training）多模态预训练框架，目标是统一视觉-语言的理解与生成能力。

### 核心架构

BLIP 采用 **MED**（Multimodal Mixture of Encoder-Decoder）架构，包含三个核心组件：

| 组件               | 功能描述                                     |
| ------------------ | -------------------------------------------- |
| **视觉编码器**     | 采用 ViT 作为主干网络，提取图像特征表示      |
| **图像文本编码器** | 基于 BERT 架构，通过交叉注意力层融合图像特征 |
| **图像文本解码器** | 采用因果自注意力机制，实现自回归文本生成     |

### 关键创新点

与 CLIP 的双塔结构不同，BLIP 的文本编码器通过 **交叉注意力层**（Cross-Attention）引入图像特征——在每个 Transformer 块的自注意力层与前馈网络之间插入交叉注意力层，使文本编码器能够"看到"图像内容。

更重要的是，文本解码器将双向自注意力替换为 **因果自注意力**（Causal Self-Attention），类似 GPT 的单向注意力机制，通过掩码保证模型只能看到当前位置之前的词，从而支持自回归文本生成任务。

> 💡 **核心价值**：通过共享参数的编码器-解码器架构，BLIP 实现了多模态理解（如图文匹配）和生成（如图像描述）任务的统一。

---

## BLIP-2：更高效的多模态对齐

上述 BLIP 架构虽然有效，但需要端到端训练整个模型。一个自然的问题是：

> 能否利用已有的冻结模型，以更轻量的方式实现多模态对齐？

2023 年，Salesforce 提出了 **BLIP-2** 框架，通过创新的 **Q-Former** 模块实现高效的多模态对齐。

### Q-Former：可学习的查询桥梁

BLIP-2 的核心是 Q-Former（Querying Transformer），它作为连接冻结预训练模型的桥梁：

| 组件               | 说明                                     |
| ------------------ | ---------------------------------------- |
| **冻结图像编码器** | 复用预训练 ViT（如 ViT-G），参数不更新   |
| **Q-Former**       | 轻量级 Transformer，包含可学习的查询向量 |
| **冻结 LLM**       | 复用预训练大语言模型（如 OPT、Flan-T5）  |

### 工作原理

1. 初始化一组固定数量（例如 32 个）的 **可学习查询向量**（Query Embeddings）
2. 查询向量通过 **交叉注意力层** 扫描图像特征，提取与任务相关的视觉信息
3. Q-Former 输出的查询作为 **软视觉提示**（Soft Visual Prompts），前置嵌入到 LLM 的输入文本中

> 🎯 **核心优势**：Q-Former 仅需约 188M 参数即可对齐视觉与语言模态，充分复用现有 ViT 和 LLM 的能力，大幅降低训练成本。

---

## InstructBLIP：指令跟随的进化

2023 年，Salesforce 进一步提出 **InstructBLIP**，通过在大规模指令数据集上进行微调，使模型能够更好地遵循人类的自然语言指令。

### 指令微调的价值

InstructBLIP 在 26 个公开数据集上转换为指令格式进行训练，覆盖了多种视觉-语言任务：

- 🖼️ **视觉问答**（VQA）
- 📝 **图像描述**（Image Captioning）
- 🔍 **视觉推理**（Visual Reasoning）
- 🎨 **图像编辑指令理解**

这种指令微调范式使模型具备了**零样本泛化能力**，能够处理训练时未见过的任务类型。

> ⚡ **实际应用**：InstructBLIP 的技术思想已被广泛应用于各类 AI 图像编辑工具中，如 Adobe Firefly 的 Generative Fill、各类 AI 修图应用等，它们的核心都是让模型理解用户的自然语言编辑指令。

---

## 参考文献

1. Li, J., et al. (2022). [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086). *ICML 2022*.
2. Li, J., et al. (2023). [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597). *ICML 2023*.
3. Dai, W., et al. (2023). [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://arxiv.org/abs/2305.06500). *NeurIPS 2023*.
