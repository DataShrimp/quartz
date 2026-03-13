# 配图案例库

记录每次成功的配图 prompt，供后续参考和迭代。

---

## 案例 1: OpenClaw 杠杆文章（2026-03-13）

**文章主题**：OpenClaw 不是答案，它更像一根杠杆  
**生成图片数**：5 张（1 封面 + 4 内文）  
**适用平台**：公众号 + 知乎

### 封面: 电影质感杠杆（类型 F: 封面图）

**文件名**：`cover.png`  
**位置**：文章最顶部（标题之前）

**Prompt**:
```
A powerful, abstract cover image for a tech thought-leadership article about AI being a lever.

Visual concept: Top-down view of a dramatically lit lever mechanism on a dark surface. 
The lever is a long navy blue (#004E89) metallic bar stretching diagonally across the frame. 
At the pivot point, an intensely glowing orange (#FF6B35) geometric crystal/gem serves as 
the fulcrum, casting warm light and long shadows across the dark surface. The fulcrum 
crystal has facets that catch light beautifully.

On the lifted end of the lever, small luminous objects float upward - representing amplified output. 
On the pressing end, a single small hand silhouette pushes down - minimal effort.

Chinese text overlay: "OpenClaw 不是答案" in large white bold font on the upper portion, 
"它更像一根杠杆" in orange below, slightly smaller.

The overall mood is dramatic, thoughtful, premium. Like a high-end magazine cover or 
conference keynote slide.

Small shrimp icon watermark bottom-right.

Style: Cinematic, abstract, moody lighting. Deep shadows and warm highlights. 
NOT cartoon, NOT sketch, NOT 3D render. More like editorial photography mixed with 
graphic design. Ultra-wide 2.35:1 panoramic aspect ratio.
```

**效果评价**：✅ 电影质感强烈，发光水晶支点是视觉焦点，热点词"OpenClaw"醒目，高级感突出

**选型过程**：生成了 3 个方向，最终选择 V3（电影质感），因为：
- V1（动感爆发式）：冲击力有余但略显杂乱
- V2（生成失败）
- V3（电影质感）：✅ 质感 + 高级感 + 热点词突出 + 光影戏剧性

---

### 图 1: 杠杆模型（类型 A: 框架图）

**文件名**：`lever_fulcrum_hero.png`  
**位置**：文章开头（封面之后）

**Prompt**:
```
A clean editorial whiteboard-style infographic diagram showing a lever mechanism model. 
The diagram has clear hand-drawn sketch aesthetics with annotations:

- A solid triangular fulcrum/pivot point in the center, glowing with orange (#FF6B35), 
  labeled area representing "支点 = 你的想法" (fulcrum = your ideas)
- A long lever beam in navy blue (#004E89) resting on the fulcrum, labeled "OpenClaw = 杠杆工具"
- On the left side (effort side): a small hand pushing down, with dotted arrow showing minimal input
- On the right side (load side): heavy blocks being lifted upward with upward arrows, 
  labeled area showing "效率 × 价值" being amplified
- Below the fulcrum: small text annotation area showing "Skills 积累 → 支点变强 → 杠杆效果放大"
- Small cute shrimp silhouette icon in bottom-right corner as a watermark/signature
- Style: clean whiteboard sketch on light cream/off-white background, with hand-drawn lines, 
  circles, arrows, and dotted annotations. Orange highlights on key concepts, navy blue for 
  structural elements. NO photorealism, NO 3D rendering. 16:9 landscape format.
```

**效果评价**：✅ 核心模型清晰传达，品牌色和水印到位

---

### 图 2: 元技能洋葱图（类型 B: 同心圆图）

**文件名**：`meta_skills_network.png`  
**位置**：第 2 节 Skills 章节末尾

**Prompt**:
```
A clean editorial infographic showing a concentric circle / onion diagram with 3 layers, 
whiteboard sketch style:

- Innermost circle (smallest, glowing orange #FF6B35): labeled area "元技能 Meta-Skills" 
  with three small icons inside representing: a gear+wrench (skill creator), a robot head 
  (agent builder), a circular arrow (self improving)
- Middle ring (medium, lighter orange): labeled "普通 Skills" with small task icons scattered 
  around (search, write, translate, analyze)
- Outermost ring (largest, navy blue #004E89 outline): labeled "具体任务 Tasks" with many 
  small dots representing individual tasks
- Arrows pointing inward from outer ring to inner ring, with annotation: 
  "元技能 → 快速生成新技能 → 指数增长"
- A small upward trending graph/sparkline in the corner showing exponential growth curve
- Small cute shrimp silhouette icon as watermark in bottom-right
- Style: clean whiteboard/notebook sketch on light cream background. Hand-drawn circles, 
  arrows, dotted lines. Orange (#FF6B35) for core/important elements, navy (#004E89) for 
  structure. NO photorealism, NO 3D. 16:9 landscape format.
```

**效果评价**：✅ 层级关系清楚，指数增长曲线增加了信息密度

---

### 图 3: 有想法 vs 没想法（类型 C: 左右对比图）

**文件名**：`idea_vs_no_idea.png`  
**位置**：第 3 节想法章节末尾

**Prompt**:
```
A clean editorial whiteboard-style comparison diagram split into left and right panels 
with a vertical dashed line divider:

LEFT PANEL (muted, gray tones with a big X mark):
- A lever lying flat on the ground with NO fulcrum underneath
- Small icons floating aimlessly: gears spinning, tokens burning, arrows going in circles
- Annotation with downward arrow: "没有想法 = 空转" (No ideas = spinning wheels)
- Everything drawn in light gray pencil sketch style

RIGHT PANEL (vibrant, orange #FF6B35 highlights):
- Same lever now properly balanced on a bright orange fulcrum/triangle
- The lever is actively lifting blocks upward with momentum arrows
- A lightbulb icon above the fulcrum glowing
- Annotation with upward arrow: "有支点 = 杠杆生效" (Has fulcrum = leverage works)
- Below: a small checklist with 4 items with checkmarks: 
  "能自动化? 能被agent接住? 值得沉淀? 能形成闭环?"
- Small cute shrimp silhouette icon as watermark in bottom-right

Style: clean whiteboard/notebook sketch on light cream background. Hand-drawn lines, 
circles, annotations. Orange highlights on right panel key elements, gray for left panel. 
Navy blue (#004E89) for structural lines. NO photorealism. 16:9 landscape format.
```

**效果评价**：✅ 对比鲜明，检查清单提供了可操作的行动项

---

### 图 4: 多智能体流水线（类型 D: 流程图）

**文件名**：`multi_agent_orchestration.png`  
**位置**：第 4 节多agent编排章节末尾

**Prompt**:
```
A clean editorial whiteboard-style flow diagram showing a multi-agent pipeline:

TOP ROW - A horizontal pipeline with 5 connected nodes/stations, each drawn as a 
rounded rectangle with an icon inside:
1. Magnifying glass icon → "研究" (Research)
2. Pen/pencil icon → "生成" (Generate) 
3. Checkmark icon → "审校" (Review)
4. Palette/brush icon → "风格" (Style)
5. Shield/lock icon → "收口" (Brand)

Arrows flow left to right between nodes. Each node has a small agent avatar above it.

MIDDLE - A conductor/orchestrator node in orange (#FF6B35) in the center with dotted lines 
connecting to all 5 nodes above, labeled "编排中心"

BOTTOM ROW - A horizontal cost bar/meter in navy blue (#004E89), like a progress bar or 
fuel gauge, showing "Token 成本" with small coin icons. An annotation arrow pointing to it: 
"链路越长 → 成本越高 → 需要权衡价值"

- A small voice/microphone icon on the far left with "语音输入" label and a speed-up arrow
- Small cute shrimp silhouette icon as watermark in bottom-right

Style: clean whiteboard/notebook sketch on light cream background. Hand-drawn rounded 
rectangles, arrows, dotted connections. Orange (#FF6B35) for orchestrator and highlights, 
navy (#004E89) for structure and cost bar. NO photorealism, NO 3D. 16:9 landscape format.
```

**效果评价**：✅ 流程清晰，Token 成本条是亮点，体现了文章的关键洞察

---

## 迭代笔记

### 第一版失败经验（2026-03-13）

第一版使用了以下反模式导致效果差：

1. **"dark gradient background with subtle tech grid lines"** → 像素材网壁纸
2. **"futuristic feel with soft ambient lighting"** → 科技感过重，无信息
3. **"NO text"** → 丢失了信息密度
4. **"vector-style art"** → 太通用，无品牌感
5. **没有指定中文标注** → 图与中文文章脱节

### 第二版改进要点

1. 换成 **浅色背景 + 白板手绘风** → 知识感提升
2. 加入 **中文标注和逻辑链** → 信息密度大幅提升
3. 加入 **品牌色功能化使用** → 不是铺色而是标注重点
4. 加入 **虾米水印** → 品牌识别
5. 指定 **具体的文字内容** → 图与文章紧密绑定

### 封面图设计经验（2026-03-13）

封面图和内文图是两套完全不同的设计语言：

| 维度 | 封面图（类型 F） | 内文图（类型 A-E） |
|------|-----------------|-------------------|
| 目标 | 吸引点击 | 传递知识 |
| 背景 | 深色 + 光影 | 浅色 + 白板 |
| 信息密度 | 低（一个意象） | 高（一个框架） |
| 文字 | 大标题 + 热点词 | 标注 + 逻辑链 |
| 风格 | 电影/杂志封面 | 手绘笔记 |

**核心发现**：封面标题中包含热点关键词（如 "OpenClaw"）能显著提升信息流点击率，因为读者在刷内容时，先看到的是封面图 + 标题。

