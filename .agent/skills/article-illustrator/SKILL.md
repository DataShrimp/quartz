---
name: article-illustrator
description: 文章配图生成技能。为公众号、知乎等平台文章生成"知识可视化"风格的配图，融入数据小虾米品牌元素。当用户要求为文章生成配图、插图、封面图时使用此技能。
---

# Article Illustrator（文章知识配图）

为文章生成两类配图：**封面图**（吸引点击）和**内文知识图**（传递知识）。

- **封面图**：视觉冲击力优先，抽象 + 高级感 + 热点关键词，目标是让读者点进来
- **内文知识图**：信息密度优先，白板手绘 + 框架可视化，目标是让读者觉得「这张图值得保存」

## 1. 核心理念：知识图 vs 装饰图

### ❌ 装饰图（绝对避免）

| 特征 | 表现 |
|------|------|
| 信息密度为零 | 抽象光球、3D 渲染、剪影人物 |
| 无品牌识别 | 换任何文章都能用 |
| 素材网风格 | "vector style, dark background" 套路 |
| 与内容脱节 | 图和段落可以互换位置 |

### ✅ 知识图（追求目标）

| 特征 | 表现 |
|------|------|
| 信息有增量 | 读者看图能学到一个模型/框架 |
| 品牌一致性 | 品牌色 + 虾米水印 + 统一风格 |
| 与内容绑定 | 图是文章核心论点的视觉压缩 |
| 激发获得感 | "这张图值得保存" |

## 2. 品牌视觉规范

### 色彩

| 用途 | 色值 | 说明 |
|------|------|------|
| 主色（重点/核心） | `#FF6B35` (Orange) | 标注核心概念、高亮关键元素 |
| 辅色（结构/框架） | `#004E89` (Navy Blue) | 结构线、边框、次要元素 |
| 内文背景 | Light cream / Off-white | 白板/笔记本感，不用深色背景 |
| 封面背景 | Deep navy / Dark gradient | 电影质感，衬托主体元素 |
| 弱化元素 | Light gray | 用于对比中的"反面"部分 |

### 水印

- 右下角放置小虾米（shrimp）剪影图标作为签名水印
- 保持简约，不影响主体阅读

### 统一风格关键词

**内文知识图**（类型 A-E）在 prompt 末尾附加：

```
Small cute shrimp silhouette icon as watermark in bottom-right.
Style: clean whiteboard/notebook sketch on light cream background. Hand-drawn lines, 
circles, arrows, and dotted annotations. Orange (#FF6B35) highlights on key concepts, 
navy blue (#004E89) for structural elements. NO photorealism, NO 3D rendering. 
16:9 landscape format.
```

**封面图**（类型 F）在 prompt 末尾附加：

```
Small shrimp icon watermark bottom-right.
Style: Cinematic, abstract, moody lighting. Deep shadows and warm highlights from 
orange (#FF6B35) focal point against deep navy (#004E89) background. Bold Chinese 
title text in clean modern font. Premium editorial cover feel. NOT cartoon, NOT sketch.
Ultra-wide 2.35:1 panoramic aspect ratio (WeChat cover standard).
```

## 3. 图片类型与 Prompt 模板

### 类型 A：框架/模型图（最常用）

**适用场景**：文章提出一个模型、框架、公式

**Prompt 结构**：
```
A clean editorial whiteboard-style infographic diagram showing [你的模型名称].
The diagram has clear hand-drawn sketch aesthetics with annotations:

- [核心元素1]: [视觉表现], labeled "[中文标注]"
- [核心元素2]: [视觉表现], labeled "[中文标注]"
- [关系/箭头]: [元素间的连接方式]
- Below/beside: annotation text showing "[核心逻辑链: A → B → C]"

[附加品牌风格关键词]
```

**示例**（杠杆模型）：
```
A clean editorial whiteboard-style infographic diagram showing a lever mechanism model.
- A solid triangular fulcrum in the center, glowing with orange (#FF6B35), labeled "支点 = 你的想法"
- A long lever beam in navy blue (#004E89), labeled "OpenClaw = 杠杆工具"
- Left side: a small hand pushing down with dotted arrow showing minimal input
- Right side: heavy blocks being lifted upward, labeled "效率 × 价值"
- Below: annotation "Skills 积累 → 支点变强 → 杠杆效果放大"
- Small cute shrimp silhouette icon in bottom-right as watermark
Style: clean whiteboard sketch on light cream background...
```

### 类型 B：同心圆/洋葱图

**适用场景**：层级关系、核心-外围结构

**Prompt 结构**：
```
A clean editorial infographic showing a concentric circle / onion diagram with N layers:

- Innermost circle (orange #FF6B35): labeled "[核心概念]" with icons [具体图标]
- Middle ring (lighter orange): labeled "[中间层]" with [元素描述]
- Outermost ring (navy #004E89 outline): labeled "[外层]" with [元素描述]
- Arrows showing [关系方向], with annotation: "[逻辑链]"
- Corner: [辅助信息，如增长曲线]

[附加品牌风格关键词]
```

### 类型 C：左右对比图

**适用场景**：好 vs 坏、有 vs 无、旧 vs 新

**Prompt 结构**：
```
A clean editorial whiteboard-style comparison diagram split into left and right panels 
with a vertical dashed line divider:

LEFT PANEL (muted, gray tones with a big X mark):
- [反面元素的视觉表现]
- Annotation: "[反面结论]"

RIGHT PANEL (vibrant, orange #FF6B35 highlights):
- [正面元素的视觉表现]
- Annotation: "[正面结论]"
- Below: [补充的检查清单或行动项]

[附加品牌风格关键词]
```

### 类型 D：流程/流水线图

**适用场景**：步骤、工作流、pipeline

**Prompt 结构**：
```
A clean editorial whiteboard-style flow diagram showing [流程名称]:

TOP ROW - A horizontal pipeline with N connected nodes:
1. [图标] → "[步骤1名称]"
2. [图标] → "[步骤2名称]"
...

MIDDLE - [编排/控制节点] in orange (#FF6B35), connected to all nodes

BOTTOM - [补充信息，如成本条、时间线、注意事项]

[附加品牌风格关键词]
```

### 类型 E：矩阵/四象限图

**适用场景**：分类决策、优先级排序

**Prompt 结构**：
```
A clean editorial whiteboard-style 2x2 matrix diagram:

- X-axis labeled "[维度1]" (low to high)
- Y-axis labeled "[维度2]" (low to high)
- Top-right quadrant (orange #FF6B35 highlight): "[最佳象限]" with [元素]
- Other quadrants in lighter tones with respective labels
- Arrows or annotations showing recommended direction

[附加品牌风格关键词]
```

### 类型 F：封面图（Cover）— 吸引点击

**适用场景**：文章封面/首图，目标是吸引点击

**设计原则**（与内文知识图完全不同）：
- **视觉冲击力 > 信息密度**：封面不需要传递知识，只需抓住眼球
- **深色背景 + 品牌色高光**：电影质感，而非白板手绘
- **必须包含文章标题关键词**：中文大标题 + 副标题，直接传达主题
- **紧扣热点关键词**：标题中包含热点词（如产品名、技术名）提升点击率
- **核心视觉隐喻要抽象化**：不需要完整的框架图，一个强烈的视觉意象即可
- **高级感和质感**：像 keynote 封面或高端杂志封面

**Prompt 结构**：
```
A powerful, abstract cover image for a tech thought-leadership article about [核心主题].

Visual concept: [核心视觉隐喻的抽象化表达]. 
[主体元素] in navy blue (#004E89). 
At the focal point, [关键元素] in intensely glowing orange (#FF6B35), 
casting warm light and dramatic shadows.

[动态元素描述 - 如飘浮、发射、粒子化等]

Chinese text overlay: "[主标题]" in large white bold font on the upper portion, 
"[副标题]" in orange below, slightly smaller.

Small shrimp icon watermark bottom-right.

Style: Cinematic, abstract, moody lighting. Deep shadows and warm highlights. 
Premium editorial cover feel, like a keynote slide or magazine cover. 
NOT cartoon, NOT sketch. Ultra-wide 2.35:1 panoramic aspect ratio.
```

**成功案例**（OpenClaw 杠杆文章封面）：
```
A powerful, abstract cover image for a tech thought-leadership article about AI being a lever.

Visual concept: Top-down view of a dramatically lit lever mechanism on a dark surface. 
The lever is a long navy blue (#004E89) metallic bar stretching diagonally across the frame. 
At the pivot point, an intensely glowing orange (#FF6B35) geometric crystal/gem serves as 
the fulcrum, casting warm light and long shadows across the dark surface.

On the lifted end, small luminous objects float upward - representing amplified output. 
On the pressing end, a single small hand silhouette pushes down - minimal effort.

Chinese text overlay: "OpenClaw 不是答案" in large white bold font on the upper portion, 
"它更像一根杠杆" in orange below, slightly smaller.

Small shrimp icon watermark bottom-right.

Style: Cinematic, abstract, moody lighting. Deep shadows and warm highlights. 
Premium editorial cover feel. NOT cartoon, NOT sketch. Ultra-wide 2.35:1 panoramic aspect ratio.
```

**封面 Prompt 要点**：
- 标题文案中包含产品/技术热点词 → 提升搜索页和信息流中的点击率
- 视觉焦点用橙色 (#FF6B35) 发光 → 自然吸引视线
- 主体用深蓝 (#004E89) 金属质感 → 高级感
- 光影对比要强烈 → 在缩略图中也有辨识度

## 4. 工作流程

### Step 1: 阅读文章，提取知识结构

1. **读完全文**，识别文章的核心论点和框架
2. 为每个主要章节判断：
   - 这一节的核心知识点是什么？
   - 能不能用一张图压缩表达？
   - 适合哪种图片类型（A-E）？
3. 确定需要生成的图片数量和位置

**经验法则**：
- 文章 < 1500 字：封面 + 1-2 张内文图
- 文章 1500-3000 字：封面 + 2-3 张内文图
- 文章 > 3000 字：封面 + 3-4 张内文图
- **封面必须有**，是点击率的关键
- **内文图不要每节都配**，选择信息密度最高的章节

### Step 2: 撰写 Prompt

1. 根据知识结构选择图片类型模板
2. 将文章的**具体概念和术语**填入模板
3. 确保 prompt 中包含：
   - 具体的中文标注文字
   - 品牌色值
   - 虾米水印
   - 风格关键词

### Step 3: 生成图片

1. 使用 `generate_image` 工具生成每张图
2. 将图片从 artifact 目录复制到文章的 `images/` 子目录
3. 使用描述性文件名（kebab-case）

### Step 4: 插入到文章

1. 在对应章节位置插入 `![](../images/filename.png)` 或 `![](images/filename.png)`
2. 确保图片位置与知识点内容对应
3. 注意不同平台文章路径的相对引用关系

## 5. Prompt 写作反模式（必须避免）

| ❌ 反模式 | ✅ 正确做法 |
|-----------|------------|
| `"dark background, futuristic, glowing"` | `"light cream background, whiteboard sketch"` |
| `"abstract conceptual illustration"` | `"infographic diagram showing [具体模型]"` |
| `"vector style, clean, minimal"` | `"hand-drawn sketch with annotations and labels"` |
| 不指定中文标注 | 在 prompt 中写明每个标注的中文文字 |
| `"no text"` | 主动要求带中文标注，增加信息密度 |
| 用英文标注 | 标注使用中文（目标读者是中文用户） |
| 一次生成过多图片 | 精选 3-4 张最有价值的 |

## 6. 目录结构与命名约定（多平台适配）

在应对多平台分发时，内文图往往可以**复用**，但封面图或特定场景图需要**定制**（例如由于尺寸要求或立意差异）。

**命名规范**：
- **通用/共享图片**：直接命名，描述内容大意。如 `lever_fulcrum_hero.png`
- **平台专属图片**：在名称中加入平台标识。如 `cover_wechat.png` (2.35:1 比例), `cover_blog.png` (16:9 比例), `chat_vs_system_blog.png`

**目录结构示例**：
```
content/platform/<topic>/
├── images/                    # 统一图片资源池
│   ├── cover_wechat.png      # 平台专属：微信封面 (微信立意：杠杆)
│   ├── cover_blog.png        # 平台专属：博客封面 (博客立意：数字员工)
│   ├── chat_vs_system.png    # 平台专属/按需定制的配图
│   ├── model-name.png        # 通用图片：所有平台共用的知识图解
│   └── comparison.png        # 通用图片：所有平台共用的知识图解
├── wechat/
│   └── content.md            # 引用 ../images/cover_wechat.png 和通用图
├── blog/
│   └── content.md            # 引用 ../images/cover_blog.png 和通用图
└── zhihu/
    └── content.md            # 按需引用对应的图片
```

**原则**：同一套基础知识图片被多平台文章共享，避免重复存储；但因平台要求（尺寸、受众语境）不同的图片，必须在文件名中明确区分。

## 7. 质量检查清单

生成配图后，逐项检查：

- [ ] 每张图是否传达了一个独立的知识点？
- [ ] 图中是否有中文标注/标签？
- [ ] 是否使用了品牌色（Orange + Navy Blue）？
- [ ] 是否有虾米水印？
- [ ] 背景是否为浅色（非深色科技感）？
- [ ] 图片位置是否与文章对应章节匹配？
- [ ] 是否避免了素材网风格？
- [ ] 图片数量是否合理（不过多也不过少）？
