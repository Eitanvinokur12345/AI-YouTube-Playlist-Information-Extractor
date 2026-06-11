---
name: ai-writing-detection-signals
description: "Use when reviewing content for AI authorship or improving AI-generated text to remove telltale patterns and sound more human."
---

# AI Writing Detection Signals

## Overview
A checklist of 10+ specific linguistic, formatting, and metadata patterns that identify AI-generated text, sourced from Wikipedia's moderator guide. Covers language, formatting quirks, and technical metadata tells.

## Key Techniques
- **Language tells**: Promotional adjectives without evidence (breathtaking, profound, unique), negative parallelisms, editorializing without support
- **Formatting tells**: Em-dash overuse, curly/straight quotation mark mixing, emoji in subheadings, broken markdown
- **Metadata tells**: UTM URLs ending in `?utm_source=chatgpt.com` or `claude.ai`, leftover AI setup phrases ("as an AI language model")
- **Style tells**: Sudden grammar quality shifts, American/British English mixing, superficial analysis tacked onto facts

## How to Apply
1. Read through the text checking for each signal category
2. Look for URL parameters in any links — a `utm_source=chatgpt.com` is a dead giveaway
3. Search for negative parallelism structures: "Not only is it X, but Y"
4. Check quotation mark consistency (straight vs curly in the same document)
5. Look for opinions or analysis that lack any supporting evidence or citation

## Examples
- A Wikipedia article flagged for AI: uses "breathtaking cultural heritage" with no source, contains negative parallelisms, has a curly/straight quote mismatch
- A submitted blog post where all links have `?utm_source=chatgpt.com` appended
- Marketing copy that editorializes ("this is a unique approach") without defining what makes it unique

## Source
Extracted from: [Wikipedia's Secret Signs of AI Writing Exposed!](https://www.youtube.com/watch?v=34BmRpsDTh0)
Channel: Will Francis
