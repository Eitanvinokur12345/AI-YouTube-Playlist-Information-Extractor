---
name: brand-voice-file-claude-code
description: "Use when Claude keeps writing generic marketing copy that doesn't sound like a specific brand — create a single brand context file that every skill and chat reads before writing."
---

# Brand Voice File for Claude Code

## Overview
A single markdown file (e.g. `brand-voice.md`) that captures a business's tone, vocabulary, and
style guidelines. Claude reads it before writing, so output consistently matches the brand instead
of defaulting to generic AI copy.

## Key Techniques
- Keep one canonical brand context file in the project root (terminal use) or upload it into a Claude
  Project's knowledge (no-terminal use) so it's available to every session automatically.
- Point every marketing-related skill or chat at this file instead of re-explaining brand voice in
  each prompt.
- Pair it with Anthropic's official Marketing plugin for ready-made brand-aware skills instead of
  writing marketing prompts from scratch.

## How to Apply
1. Write `brand-voice.md` with concrete tone/vocabulary/style guidelines (not vague adjectives —
   include example phrases and words to avoid).
2. Terminal users: drop it in the project root; Claude Code picks it up each session.
3. Non-terminal users: upload the same file into a Claude Project's knowledge base.
4. Install Anthropic's official Marketing plugin from the Claude Code plugin marketplace (a few
   commands) to layer in ready-made marketing skills that also read the brand file.
5. Before installing any community (non-official) skill, check what it actually does first.

## Examples
Source video ties the technique to a "Claude writes generic marketing copy because it doesn't know
your business" problem — the fix demonstrated is exactly this: one file, read by every skill/chat,
loaded either via the filesystem or Claude Projects' knowledge for non-technical users.

## Source
Extracted from: [I Gave Claude One File And It Became My Brand Team](https://www.youtube.com/watch?v=ACwHpJZOZB4)
Channel: Sebastian Hardy | AI Marketing

Also seen in: [The Brand Voice File That Makes Claude Code Sound Like You](https://www.youtube.com/watch?v=QG63UIN0hdA)
