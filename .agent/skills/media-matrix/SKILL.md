---
name: media-matrix
description: A comprehensive content matrix generator for "Data Shrimp" IP. Converts core content into platform-optimized posts (RedBook, Twitter, WeChat, Zhihu) following 2025 algorithm rules and "One Person Company" branding. Use this skill when you need to repurpose distinct content for different social media platforms.
---

# Media Matrix (Data Shrimp IP)

This skill helps you repurpose core technical/thought leadership content into platform-native formats for the "Discovery -> Trust -> Sales" funnel.

## 1. Core Principles (The "Data Shrimp" Way)

Before generating any content, review the IP Strategy:
[Data Shrimp Identity](references/ip_strategy.md)

**Key Takeaway**: 
*   **One Journey, Two Outputs**: Always produce both "Builder Focus" (Tech/Logic) and "Creator Focus" (Story/Emotion).
*   **HKR Rule**: Happiness, Knowledge, Resonance.

## 2. Platforms & Strategies

Choose the target platform(s) and follow their specific algorithm rules.

### 🔴 RedBook (小红书) - Discovery / Traffic
**Goal**: Viral reach, visually striking, "useful" feeling.
*   **Strategy**: [RedBook Algo & Rules](references/algo_redbook.md)
*   **Focus**: Hook titles, Emoji layout, "Collection" value.

### 🔵 Twitter (X) - Trust / Networking
**Goal**: Thought leadership, networking, global reach.
*   **Strategy**: [Twitter Algo & Rules](references/algo_twitter.md)
*   **Focus**: Thread structure, No-link hooks, Growth hacking.

### 🟢 WeChat (公众号) - Retention / Depth
**Goal**: Deep connection, private domain traffic, long-term asset.
*   **Strategy**: [WeChat Algo & Rules](references/algo_wechat.md)
*   **Focus**: Narrative flow, "Logbook" style, Aesthetics.

### 🔵 Zhihu (知乎) - Authority / SEO
**Goal**: Professional authority, long-tail search traffic.
*   **Strategy**: [Zhihu Algo & Rules](references/algo_zhihu.md)
*   **Focus**: Clear stance, logic, evidence-based.

## 3. Workflow

### Step 1: Content Analysis
Analyze the input content (blog, notes, code) to extract:
1.  **The Core Insight** (What is the one thing?)
2.  **The Emotion/Story** (For RedBook/WeChat)
3.  **The Logic/Data** (For Twitter/Zhihu)

### Step 2: Workspace Setup
Use the script to create the standard folder structure under `content/platform/`:
```bash
python3 .agent/skills/media-matrix/scripts/setup_content.py <topic_name>
```

### Step 3: Generation (Iterative)
For each selected platform:
1.  **Draft**: Generate text following the specific `references/algo_*.md` guide.
2.  **Review**: Check against `anti_patterns` in the guide.
3.  **Visual Prompts**: Create a `images/prompts.md` file in each platform directory.
    - **Format**:
      ```markdown
      ## 1. DescriptionWithNoSpaces (Filename_Hint)
      **Prompt**: "Your detailed prompt here..."
      ```
    - **Constraint**: Ensure prompts specify "text in Chinese" unless English is strictly required for technical correctness.

### Step 4: Visuals Generation (Agent Execution)

After creating the content and `images/prompts.md` files, **you (the AI Agent) must use your built-in `generate_image` tool** to create the visuals.

1. Read the `prompts.md` from each platform folder.
2. For each prompt, use your `generate_image` tool to generate the image. 
3. Move the generated image artifact to the platform's `images/` directory under the designated filename.
4. Insert `![[image.png]]` references into the main content file (Obsidian style).

## 4. Example Usage

**User**: "I just finished a project on 'Building an AI Agent with Claude'. Help me distribute it."

**Claude**:
1.  Ask for the project details/draft.
2.  Run `setup_content.py building_agent`.
3.  **RedBook**: "7 Tools to Build AI Agents (No Code Needed)" aimed at beginners.
4.  **Twitter**: "I spent 48 hours building an Agent. Here is the architecture 👇" (Thread).
5.  **WeChat**: "The Anxiety of the AI Era: Why I decided to build my own Agent." (Deep Dive).
6.  **Zhihu**: "How to implement Agentic Workflow? Evaluating LangChain vs manual coding." (Professional).
