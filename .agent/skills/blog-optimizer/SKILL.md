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

Instead of injecting special HTML comments or running an external script, **you (the AI Agent) must use your built-in `generate_image` tool** during your optimization pass.

**Placement & Generation Guide**:
*   **Cover**: Top of file, after frontmatter.
*   **Concepts**: After H2 headers introducing complex topics.
*   **Flows**: Where steps or processes are described.

When an image is needed:
1. Determine the appropriate prompt and filename (`slug-name`).
2. Use the `generate_image` tool to create the image based on your prompt.
3. Move the generated artifact image to the `attachments/` folder relative to the markdown file. Make sure the filename matches your intended `filename`.
4. Insert standard Markdown image syntax into the file: `![Descriptive alt text](attachments/filename.png)`.

**Example**:
```markdown
# The Architecture of Transformers

![Transformer Architecture Diagram](attachments/transformer-arch.png)

The transformer model consists of...
```

### Step 3: Execution (Agent Workflow)

You are responsible for executing the image generation and file placement.
1. Draft or edit the markdown file.
2. Generate all necessary images using `generate_image` and specify "text in Simplified Chinese if any".
3. Copy/move the images to their correct `attachments/` relative paths.
4. Ensure the markdown directly references those generated images.

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
