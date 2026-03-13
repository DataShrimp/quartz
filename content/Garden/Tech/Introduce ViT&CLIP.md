---
title: 多模态模型入门
description: 介绍 ViT 和 CLIP 两个多模态基础模型的核心原理
tags:
  - AI
  - 多模态
  - ViT
  - CLIP
date: 2025-12-11
---

入门多模态大模型，必须掌握两个基础模型算法原理：**ViT** 和 **CLIP**。

---

## ViT：视觉 Transformer 的开创者

**ViT**（Vision Transformer）是 Google 于 2020 年提出的模型，首次将自然语言处理中的 Transformer 架构成功应用于计算机视觉任务。

### 为什么需要 ViT？

在 ViT 之前，计算机视觉深度学习的主流模型是 **CNN**（卷积神经网络），如 AlexNet、ResNet 等。这些模型通过卷积操作捕获多分辨率图像特征，并借助深度残差网络设计在大规模训练数据上取得了优异效果。

然而，两个关键问题推动了 ViT 的诞生：

1. **可扩展性**：能否进一步提升大规模数据的可扩展性，充分发挥 Scaling Law 效应？
2. **架构统一**：视觉任务能否与 NLP 任务采用统一架构，使跨模态向量相似性计算更加直接？

### ViT 的核心架构

ViT 的核心包括三个关键组件：

![[vit_architecture.png|ViT Architecture]]

| 组件                   | 功能描述                                                                                                                               |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **图像分块**           | 将图像分割成固定大小的 patches（如 16×16），类似 NLP 中的词序列，并展平为一维向量                                                      |
| **位置编码**           | 解决展平后空间结构信息丢失问题，标准 ViT 使用 **1D 可学习位置编码**叠加到 patch embedding 上                                           |
| **Transformer 编码器** | 采用标准 Transformer 块，通过多头注意力机制捕获图像全局关系；借鉴 BERT，在序列**开头**添加一个可学习的 `[CLS]` token，用于汇聚全局信息 |

> ⚠️ **代价与收益**：ViT 相比 CNN 模型需要**更多的训练数据**才能达到最佳效果，但在超大数据集上展现出更优的性能和泛化能力。

---

## CLIP：连接视觉与语言的桥梁

在解决了模态统一编码问题后，一个新问题浮现：

> 我们能否构建**开放式的视觉理解能力**，而不仅仅局限于预设的分类系统？

2021 年 OpenAI 提出的 **CLIP**（Contrastive Language-Image Pre-training）给出了答案——通过对比学习将文本和图像映射到同一嵌入空间。

### CLIP 的架构设计

CLIP 采用经典的**双塔结构**：

![[clip_architecture.png|CLIP Architecture]]

- **图像编码器**：可采用 ViT 或 ResNet 架构
- **文本编码器**：基于 Transformer 的文本编码器
- **投影层**：将两者线性投影到**同一维度**的嵌入空间

### 对比学习的精髓

CLIP 的核心是**对比学习**（Contrastive Learning）：

![[contrastive_matrix.png|Contrastive Matrix]]

1. 每个 batch 包含 **N** 个图像-文本对
2. 计算生成 **N×N** 的相似度矩阵
3. **对角线的 N 对**为正样本（匹配）
4. **其余 N²−N 对**为负样本（不匹配）
5. 使用对称交叉熵损失函数，最大化正样本相似度，最小化负样本相似度

### 大规模训练的威力

CLIP 真正实现了「大力出奇迹」——通过互联网收集的 **4 亿对**图像-文本训练数据（WIT-400M），实现了开放式视觉任务的**零样本迁移能力**。

更重要的是，CLIP 的鲁棒基座能力可广泛应用于：

- 🔍 **图像检索**
- 🎨 **文生图**（Text-to-Image）
- 📊 **零样本分类**
- 🤖 **多模态应用**

---

## 参考文献

1. Dosovitskiy, A., et al. (2020). [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929). *CVPR 2020*.
2. Radford, A., et al. (2021). [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020). *ICML 2021*.