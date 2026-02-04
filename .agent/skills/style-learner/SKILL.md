---
name: style-learner
description: Learns, adapts, and applies the user's personal writing style. Monitors user content to evolve a persistent style profile and applies it to generate or rewrite content that feels authentically like the user.
---

# Style Learner

This skill empowers the agent to act as a **digital ghostwriter**, analyzing the user's past work to build a robust, evolving model of their writing persona.

## 🧠 The Brain: `style_profile.json`

The core of this skill is the persistent JSON file located at:
`assets/style_profile.json`

This file is the "Single Source of Truth" for the user's voice. It must be updated whenever new content is analyzed.

### Schema Overview
- **voice_and_tone**: The emotional temperature and personality (e.g., "Cynical but hopeful," "Professional yet approachable").
- **sentence_patterns**: Structural habits (e.g., "Starts paragraphs with questions," "Uses short, fragmented sentences for impact").
- **vocabulary_preferences**: diction choices (e.g., "Prefers Anglo-Saxon words over Latinate," "Uses specific tech slang").
- **formatting_habits**: Visual rhythm (e.g., "Heavy use of bullet points," "Bold text for emphasis everywhere").
- **rhetorical_devices**: Persuasion tools (e.g., "Metaphors involving cooking," "Direct address to the reader").
- **signature_phrases**: Specific idioms or catchphrases the user loves.
- **anti_patterns**: Things the user HATES or never does (e.g., "Never use the word 'delve'," "No passive voice").
- **analyzed_sources**: A registry of files that have been 'learned' to prevent redundant processing.

---

## 🛠 Workflows

### 1. Training Mode (Learning Style)

**Trigger**: User provides text/files and asks to "learn my style," "analyze this," or "update my profile."

**Procedure**:

1.  **Ingest**: Read the content of the provided files.
2.  **Load State**: Read the current `assets/style_profile.json`.
3.  **Deconstruct**: Analyze the new content against the existing profile. Ask:
    *   *Consistency*: Does this match what we know?
    *   *Novelty*: What's new here? (New phrase? New tone?)
    *   *Context*: Is this style specific to this format (e.g., a tweet vs. a whitepaper)?
4.  **Synthesize**: Generate a merged profile.
    *   *Do not explain the analysis to the user yet.* Focus on updating the data structure.
    *   Be specific. avoiding vague terms like "professional." Use "Professional with a tendency to use engineering metaphors."
5.  **Commit**: Overwrite `assets/style_profile.json` with the updated JSON.
6.  **Report**: Tell the user what was learned.
    *   "I've updated your profile. I noticed you're starting to use more direct questions in your intros, and I've added 'Let's dive in' to your signature phrases."

### 2. Ghostwriter Mode (Applying Style)

**Trigger**: User asks to "write this in my style" or "rewrite this like I would."

**Procedure**:

1.  **Load State**: ALWAYS read `assets/style_profile.json` first. Do not rely on context memory alone.
2.  **Drafting**: Generate the content.
    *   *Check against Anti-Patterns*: specific check for banned words/structures.
    *   *Inject Signature Phrases*: where natural.
    *   *Mimic Rhythm*: Copy the sentence length distribution found in the profile.
3.  **Review**: (Self-Correction)
    *   "Does this sound like [User]? Or does it sound like an AI trying to sound like [User]?"
    *   *Tweak*: Remove "AI-slop" words (e.g., "Ensure," "Maximize," "landscape").
4.  **Deliver**: Present the result.

---

## 💡 Best Practices for Analysis

When updating the profile, look for these specific signals:

*   **The "Hook"**: How does the user start articles? (Story? Data? Question?)
*   **The "Turn"**: How do they transition between ideas?
*   **The "Outro"**: Do they end with a Call to Answer? A summary? A joke?
*   **Punctuation**: Do they use em-dashes? Semicolons? Lots of exclamation marks?
*   **Self-Reference**: Do they say "I" often? Or "We"? Or passive voice?

## 📂 File Management

*   **Path resolution**: Always use absolute paths when reading/writing the asset file.
*   **Corruption prevention**: Ensure the JSON is valid before writing.
