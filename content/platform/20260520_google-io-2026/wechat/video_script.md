# 视频号导流脚本 v2（AI 生成版）

> **总时长**：30 秒 = 3 × 10 秒片段拼接
> **数字人**：卡通 Puffin 形象（cartoon_a_puffin_tech.png）
> **语音**：英文发音（AI TTS）
> **字幕**：英文硬字幕（底部）
> **画面文字**：中文（标题卡、关键词弹出、CTA）
> **画幅**：9:16 竖屏
> **BGM**：轻科技电子乐，三段统一同一首，后期铺底

---

## 🎬 视觉一致性规范（三段通用）

确保三段视频拼接后无跳跃感：

| 要素 | 规范 |
| :--- | :--- |
| **角色** | Puffin 始终站在画面中央偏左，身体朝右 3/4 角度 |
| **背景** | 统一深蓝科技风背景，细微粒子缓慢漂浮，底部有浅蓝光晕 |
| **构图** | Puffin 占画面左 40%，右 60% 用于文字和图表弹出 |
| **光源** | 左上方主光，右下方蓝色辅光，保持一致 |
| **字幕位置** | 英文字幕固定在画面底部 10% 区域，白色无衬线字体 + 黑色描边 |
| **中文文字位置** | 画面右侧 60% 区域，作为"信息板"弹出 |
| **转场设计** | 每段结尾最后 0.5 秒画面微微 zoom in，下一段开头 zoom out 回位 |

---

## 📍 Segment 1 / 3（0:00 - 0:10）

### 主题：Hook + 信号一（模型）

**Prompt 描述（用于 AI 视频生成）**：

```
A cute cartoon Puffin character (black-white plumage, orange beak, 
round glasses, navy hoodie with shrimp patch, compass pendant) 
stands in the left side of frame, facing slightly right. 

The Puffin holds a glowing tablet and gestures with its other wing 
as if presenting. 

Dark blue tech background with subtle floating particles. 

On the right side, animated text cards appear one by one:
- First: large white text "Google I/O 2026" with a subtle glow
- Then: "5 Key Signals" in golden text
- Then: a comparison graphic showing a large diamond labeled "Pro" 
  with an arrow flowing into a smaller crystal labeled "Flash"
- Chinese text overlay appears: "从芯片到购物车"

The Puffin looks excited and points upward at the text.
Smooth, professional animation. 9:16 vertical format.
```

**英文配音（21 词 · 约 8.5 秒）**：

> "Google I/O 2026 is here. It’s a new order, not just products. Signal one: Flash 3.5 matches Pro, but costs half."

**英文字幕**（逐句）：

```
[0-2s] Google I/O 2026 is here.
[2-5s] It’s a new order, not just products.
[5-9s] Signal one: Flash 3.5 matches Pro, but costs half.
```

**画面中文元素**：

| 时间 | 中文内容 | 位置 | 动效 |
| :--- | :--- | :--- | :--- |
| 0-2s | **Google I/O 2026** | 右侧顶部 | 光效弹入 |
| 2-5s | **不是产品，是秩序** | 右侧中部 | 渐显 |
| 5-9s | **① Flash 3.5 价格砍半** | 右侧底部，大字 | 滑入 + 金色描边 |
| 5-9s | Pro → Flash 蒸馏示意图 | 右侧中部 | 流体动画 |

**结尾过渡**：最后 0.5 秒画面轻微 zoom in 到 Puffin 脸部

---

## 📍 Segment 2 / 3（0:10 - 0:20）

### 主题：信号二（产品）+ 信号三（硬件）+ 信号四（电商）

**Prompt 描述（用于 AI 视频生成）**：

```
Same cartoon Puffin character (black-white, orange beak, glasses, 
navy hoodie, compass pendant) in the same position (left 40% of 
frame, facing right).

Same dark blue tech background with floating particles.

The Puffin is now typing on its tablet while talking. On the right 
side, a rapid sequence of info cards animates in:

1. A hub-spoke diagram with "Gemini" at center, connected to icons 
   for Search, Gmail, Maps, YouTube
2. A chip icon splitting into two halves (blue and green)
3. A shopping cart icon with protocol labels

Chinese text overlays appear alongside each card.
The Puffin reacts with surprise at the shopping cart reveal.
Smooth, professional animation. 9:16 vertical format.
```

**英文配音（18 词 · 约 8.0 秒）**：

> "Two: all products link via Gemini. Three: TPU splits training and inference. Four: Google rewrites AI shopping rules."

**英文字幕**（逐句）：

```
[0-3s] Two: all products link via Gemini.
[3-6s] Three: TPU splits training and inference.
[6-9s] Four: Google rewrites AI shopping rules.
```

**画面中文元素**：

| 时间 | 中文内容 | 位置 | 动效 |
| :--- | :--- | :--- | :--- |
| 0-3s | **② 产品：底层全打通** | 右上 | 卡片弹入 |
| 0-3s | Gemini 生态图（简版） | 右中 | 辐射动画 |
| 3-6s | **③ 芯片：训练推理分家** | 右上 | 替换上一卡 |
| 3-6s | TPU 8t ⚡ TPU 8i 对比图 | 右中 | 分裂动画 |
| 6-9s | **④ 电商：暗渡陈仓** | 右上 | 替换上一卡 |
| 6-9s | 🛒 UCP + AP2 + Universal Cart | 右中 | 购物车滑入 |

**结尾过渡**：最后 0.5 秒画面轻微 zoom in

---

## 📍 Segment 3 / 3（0:20 - 0:30）

### 主题：信号五（科研）+ 核心观点 + CTA

**Prompt 描述（用于 AI 视频生成）**：

```
Same cartoon Puffin character (black-white, orange beak, glasses, 
navy hoodie, compass pendant) in the same position.

Same dark blue tech background with floating particles.

The Puffin first shows a science-themed card (DNA helix, weather 
icon, shield icon). Then the Puffin puts down the tablet, looks 
directly at the camera with a serious but warm expression, and 
makes a "come here" gesture with its wing.

A large golden quote card appears on the right:
Chinese text: "发布的不是产品，而是一套秩序"

Then the quote card transitions to a CTA card showing:
- A WeChat public account QR code placeholder
- Chinese text: "完整拆解 → 公众号「数据小虾米」"
- The Puffin points downward toward the QR code area.

Smooth, professional animation. 9:16 vertical format.
```

**英文配音（19 词 · 约 8.5 秒）**：

> "Five: AI accelerates science. Google is establishing a new order. Read the full breakdown in the comments below."

**英文字幕**（逐句）：

```
[0-3s] Five: AI accelerates science.
[3-6s] Google is establishing a new order.
[6-9s] Read the full breakdown in the comments below.
```

**画面中文元素**：

| 时间 | 中文内容 | 位置 | 动效 |
| :--- | :--- | :--- | :--- |
| 0-3s | **⑤ 科研：AI 终极杠杆** | 右上 | 卡片弹入 |
| 0-3s | DNA 🧬 + 天气 🌪️ + 药瓶 💊 | 右中 | 图标逐个弹出 |
| 3-6s | **「发布的不是产品，而是一套秩序」** | 画面中央，大字金色 | 渐显 + 光效 |
| 6-9s | **完整拆解 → 公众号「数据小虾米」** | 右中 | 滑入 |
| 6-9s | **评论区见 👇** | 底部 | 箭头动画 |
| 7-10s | Puffin Logo + 「数据小虾米」 | 左下角 | 品牌水印常驻 |

**结尾**：BGM 渐弱，Puffin 挥手告别

---

## 🛠️ AI 视频生成工作流

### 推荐工具链

| 步骤 | 工具 | 说明 |
| :--- | :--- | :--- |
| 角色一致性 | 参考图 `cartoon_a_puffin_tech.png` | 每段 prompt 均引用同一参考图 |
| 视频生成 | Kling 2.0 / Runway Gen-4 / Pika 2.0 | 选支持角色参考图的工具 |
| 英文配音 | ElevenLabs / Fish Audio | 选一个温暖、自信的男声 |
| 字幕烧录 | 剪映 / CapCut | 英文字幕 + 中文画面文字 |
| 拼接 & BGM | 剪映 | 三段拼接 + 统一 BGM |

### 生成顺序

```
1. 先生成 Segment 1，确认角色外观和背景调性
2. 用 Segment 1 最后一帧作为 Segment 2 的起始参考
3. 用 Segment 2 最后一帧作为 Segment 3 的起始参考
4. 三段拼接后，统一铺 BGM 和英文配音
5. 最后在剪映中添加中文文字层和英文字幕
```

### 一致性检查清单

```
□ Puffin 外观三段一致（衣服、眼镜、罗盘、虾米胸章）
□ 背景颜色和粒子效果一致
□ 光源方向一致（左上主光）
□ Puffin 在画面中的位置和大小一致
□ 转场处无明显跳跃（zoom in/out 衔接）
□ BGM 节奏跨段连贯
□ 英文字幕字体和位置三段统一
```

---

## 📝 评论区置顶（中文）

```
📖 完整版 5000 字深度拆解：
👉 公众号搜「数据小虾米」

从芯片到购物车，Google 的全栈 AI 野心远比你想的大。
模型｜产品｜硬件｜电商｜科研——5 个维度全拆了。

你觉得哪个信号最让你意外？评论区聊聊 👇
```
