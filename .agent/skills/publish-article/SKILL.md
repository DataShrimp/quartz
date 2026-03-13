---
name: publish-article
description: 文章发布/流转技能。用于将 platform/ 目录下的草稿文章（通常为博客版 content.md）正式发布到数字花园（如 Garden/Tech）中。该技能可自动执行格式转换（去除H1、转换图片链接）、草稿状态变更以及相关图片物理迁移等流水线操作。
---

# Publish Article（文章发布流水线）

将打磨好的内容草稿从工作区（`content/platform/`）正式推送到展示区（`content/Garden/` 或 `content/Projects/`）的自动化脚本套件。

## 1. 核心流程

该技能规范化了内容发布的标准流程：

1. **确定源与目标**：
   - 源文件：通常是 `content/platform/<topic>/blog/content.md` 或类似经过最终润色的文章文件。
   - 目标路径：根据文章类型归档，如 `content/Garden/Tech/<ArticleName>.md`。
2. **状态更新**：
   - 将文章头部 `frontmatter` 中的 `draft: true` 变更为 `draft: false` 以表示可公开访问。
3. **视觉冗余清理**：
   - 自动移除正文开头的第一个 `H1` 标题（`# Title`），因为 Quartz 等系统会自动从 frontmatter 渲染标题，保留 H1 会导致页面出现双标题。
4. **图片依赖剥离与迁移**：
   - 将源目录的 `images/` 中，被当前博客内嵌引用的相关图片拷贝至全局资产库 `content/attachments/` 中。
5. **语法转换适配**：
   - 将标准 Markdown 的相对资源引用语法（如 `![](../images/cover.png)`）重写为 Obsidian/Quartz 支持的双中括号 Wiki Link 语法（如 `![[cover.png]]`）。

## 2. 工作流范式 (Agent 执行步骤)

当用户说：`将 platform/openclaw 下的博客文章发布到 Garden/Tech 目录下，名字叫 OpenClaw_Digital_Employee.md`，执行以下检查清单：

### Step 1：确定文件
- 使用 `view_file` 或 `grep_search` 确认源文件内容。
- 确认目标文件名未与已有文件重名。

### Step 2：资产迁移 (Asset Migration)
- 在源 Markdown 文件中，使用正则识别所有 `![](...)` 引用的图片文件名。
- 使用 `run_command` (cp) 将这些图片文件从 `content/platform/<topic>/images/` 复制到 `content/attachments/` 中。

### Step 3：内容转换与保存 (Content Transformation)
读取源文件内容，在内存中进行以下几项替换操作：

1. **Frontmatter 状态**：
   查找 `draft:` 或新加一行，将 `draft: true` 替换为 `draft: false`。
2. **正文去头**：
   移除第一个以 `# ` 开头的行（并且紧跟其后若是空行则同时去掉，保持版面整洁）。
3. **资源引用转换**：
   利用寻找替换能力，将诸如 `![](../images/xxx.png)` 或 `![](images/xxx.png)` 的文本替换成 `![[xxx.png]]` 格式。

使用 `write_to_file` 直接在目标路径（例：`content/Garden/Tech/<New_Name>.md`）创建最终版本的 Markdown。

### Step 4：善后核对 (Post-flight check)
- 检视最终目标文件的头部 `draft` 是否为 `false`。
- 抽样阅读生成的新文件中，图片引用格式是否确为双括弧 `![[]]`。
- 确认原文中的 H1 大标题是否已经剥除。

## 3. 防呆指南（注意事项）

- **保留源代码**：技能的原则是**"Copy and Transform"**，永远只进行复制和衍生转换，不要直接删除 `platform/` 目录里的原始手稿（以备不时之需或多平台需再次生成）。
- **附件覆盖**：拷贝图片时遇到同名附件，默认选择覆盖模式（`cp -f`），以便能及时反映修改了的图像。
- **关联平台图片特例**：只处理在给定文章文件中实际引用的图片，未被引用的平台专享图（比如 `cover_wechat.png`）不需要带过去导致全局库污染。
