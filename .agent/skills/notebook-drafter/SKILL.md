---
name: notebook-drafter
description: Interactive tool to draft articles using Google NotebookLM. It prompts for a notebook ID and personal opinions, then generates a structured article draft based on the notebook's sources and your viewpoint.
---

# Notebook Drafter

This skill provides an interactive workflow to generate high-quality article drafts using Google NotebookLM.

It is designed to "pair program" the writing process: you provide the core viewpoint (the "Soul"), and NotebookLM provides the supporting evidence and structure (the "Body") from your research materials.

## Usage

Run the interactive script:

```bash
python3 .agent/skills/notebook-drafter/scripts/draft_article.py
```

You can also provide arguments directly to skip the interactive prompts:

```bash
python3 .agent/skills/notebook-drafter/scripts/draft_article.py --notebook <notebook_id> --opinion "My personal opinion is..."
```

## How it Works

1.  **Select Notebook**: You choose which notebook (containing your research/sources) to use.
2.  **Input Viewpoint**: You input your unique personal perspective or thesis statement.
3.  **Generate Draft**: The skill constructs a specialized prompt that instructs NotebookLM to:
    *   Center the article around *your* viewpoint.
    *   Use the notebook's sources to support (or challenge) this viewpoint.
    *   Follow a professional structure (2000-3000 words, rigorous logic).
4.  **Download**: The generated draft is automatically downloaded as a Markdown file.

## Dependencies

*   `notebooklm` CLI tool (installed via `pip install notebooklm-py`)
*   Authenticated NotebookLM session (`notebooklm login`)

## Prompt Structure

The skill uses a proven prompt template optimized for thought leadership articles:

*   **Role**: Professional Engineer/Writer
*   **Goal**: 2000-3000 word draft
*   **Key Elements**:
    *   Structure: Title, Intro, 3-4 Argument Paragraphs, Conclusion.
    *   Fusion: Personal Viewpoint + Notebook Evidence.
    *   Critical Thinking: Dialectical analysis of conflicting data.
    *   Style: Professional, rigorous, clear.
    *   Citations: Standard academic format.
