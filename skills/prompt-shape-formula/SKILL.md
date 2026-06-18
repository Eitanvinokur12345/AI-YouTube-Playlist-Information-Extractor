---
name: prompt-shape-formula
description: "Use when structuring any Claude prompt for reliability and precision — apply the three-part shape: name a role in line one, lock the output format explicitly, and end with a hard stop line to prevent rambling."
---

# Prompt Shape Formula: Role + Locked Format + Hard Stop

## Overview
A three-part Claude prompt structure that consistently produces tight, on-target outputs. Line one assigns a specific role, the middle section locks the output format precisely (sections, word counts, bullet limits), and the final line is a hard stop instruction that prevents Claude from filling the session with increasingly sloppy content.

## Key Techniques
- Line one: assign a specific role (e.g. "You are a chief of staff who writes executive morning briefs")
- Middle: lock output format explicitly — name each section, set word or bullet limits, specify what to include and exclude
- Final line: hard stop instruction (e.g. "Stop." or "Do not continue past this point.")
- The prompt shape carries the reliability — not model intelligence

## How to Apply
1. Open your prompt with a role statement: "You are a [specific role] who [specific function]."
2. Write the task instructions in the middle, naming the exact output structure you expect.
3. Include a constraint if needed: "Do NOT invent or estimate — only use data provided."
4. End the prompt with a single hard stop line: "Stop."
5. Test once with a sample, adjust the format lock if needed, then reuse as a template.

## Examples
- "You are a project manager who writes precise weekly status reports. Do NOT invent or estimate metrics — only report what is explicitly in the data below. [Sections: Completed, In Progress, Blocked, Key Metrics]. Stop."
- "You are an executive assistant who drafts email replies. Study these 5 sent emails to match my voice: [EMAILS]. Draft replies to each unread email below. Match tone exactly. Stop."
- "You are a content strategist who repurposes content across channels. Rewrite as: 1) 5-tweet thread, 2) LinkedIn post under 200 words, 3) Newsletter section, 4) Promotional email. Stop."

## Source
Extracted from: [5 CLAUDE PROMPTS THAT RUN MY 8-HOUR WORKDAY IN 47 MINUTES](https://www.youtube.com/watch?v=5RsMqAzHeUw)
Channel: Dubibubi
