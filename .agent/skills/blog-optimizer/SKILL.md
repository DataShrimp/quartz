---
name: blog-optimizer
description: An optimization suite for blog articles (Quartz/Obsidian). Handles typography, SEO, structure, and automated image generation.
---

# Blog Optimizer Skill

This skill transforms raw markdown drafts into high-quality, SEO-optimized blog posts with professional visuals.

## 1. Capabilities

1.  **Structural Optimization**: Fixes heading levels, paragraph length, and formatting logic.
2.  **SEO Enhancement**: Generates YAML frontmatter, keywords, and description.
3.  **Visual Automation**: Automatically generates cover art and diagrams based on injected prompts.

## 2. Workflow

### Step 1: Analysis & Content Edits (Agent)

As the AI agent, your first job is to refactor the user's markdown file directly.

1.  **Read** the target file.
2.  **Critique** structure based on `gen-blog.md` rules:
    - Only one `# H1` title.
    - No heading level jumps (e.g., H2 -> H4).
    - Paragraphs < 5 sentences.
3.  **Edit** the file directly to:
    - Add/Update YAML Frontmatter.
    - Break up long text.
    - Add internal links `[[wikilink]]`.
    - **Insert Image Placeholders** (See below).

### Step 2: Image Placeholders (The Protocol)

Instead of asking the user to run prompts, inject **special HTML comments** into the markdown file where images should go.

**Syntax**:
```html
<!-- IMAGE_GEN: {"prompt": "Detailed prompt here...", "filename": "slug-name.png", "alt": "Descriptive alt text"} -->
```

**Placement Guide**:
*   **Cover**: Top of file, after frontmatter.
*   **Concepts**: After H2 headers introducing complex topics.
*   **Flows**: Where steps or processes are described.

**Example**:
```markdown
# The Architecture of Transformers

<!-- IMAGE_GEN: {"prompt": "A technical diagram showing the Transformer architecture with Encoder and Decoder blocks, minimal style, cyan and dark blue colors", "filename": "transformer-arch.png", "alt": "Transformer Architecture Diagram"} -->

The transformer model consists of...
```

### Step 3: Execution (Automatic)

After inserting image placeholders, **automatically run** the processor script using Bash:

```bash
python3 .claude/skills/blog-optimizer/scripts/process_blog_images.py <path_to_markdown_file>
```

Do NOT ask the user to run this command - execute it directly.

**What the script does**:
1.  Scans for `<!-- IMAGE_GEN: ... -->` comments.
2.  Generates images using the local IDM-VTON/Gemini API (same as media-matrix).
3.  Saves images to `attachments/` relative to the file.
4.  Replaces the comment with standard Markdown image syntax: `![alt](attachments/filename.png)`.

## 3. SEO Checklist (Reference)

Ensure the final file meets these criteria:
- [ ] Title < 60 chars.
- [ ] Description 150-160 chars.
- [ ] URL-friendly filename (kebab-case).
- [ ] Images have `alt` text.
- [ ] 2-3 Internal Links (`[[Link]]`).

## 4. Troubleshooting

*   **Image Failures**: If the script fails, verify the local API is running on port 8045.
*   **Bad Images**: You can manually update the prompt in the component or regenerated file and run the script again (it skips existing files unless forced, or you can delete the image to regenerate).
