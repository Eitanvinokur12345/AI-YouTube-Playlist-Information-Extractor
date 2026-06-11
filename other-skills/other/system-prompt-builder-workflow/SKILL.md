---
name: system-prompt-builder-workflow
description: "Use when you need to create a reusable AI assistant for a specific recurring task — have AI build the system prompt through questions, then deploy it."
---

# System Prompt Builder Workflow

## Overview
Use pull prompting to co-create a reusable system prompt with AI: have it ask you questions about the desired behavior, iterate until perfect, then deploy into a Custom GPT, Claude Project, or Gemini Gem so it runs automatically on every session.

## Key Techniques
- Prompt AI as an expert AI engineer to create the system prompt, using pull prompting
- Iterate on the draft by testing responses and asking for refinements
- Deploy the final prompt into a persistent AI surface for zero-setup reuse

## How to Apply
1. Say: "You're an expert AI engineer. I want you to create a system prompt that [does X]. Ask me all the questions you need."
2. Answer the questions using voice-to-text
3. Test the system prompt: send a sample input and evaluate the response
4. Refine: "Update the prompt to [fix Y]" until it's dialed in
5. Copy the final system prompt into a Custom GPT, Claude Project, or Gemini Gem
6. Share the link with teammates or use it yourself without repeating instructions

## Examples
- A system prompt for a content strategist that generates social posts from any URL — deployed as a Claude Project
- A research assistant system prompt that always returns structured competitor analysis — shared via Custom GPT link
- A code reviewer that follows your team's style guide — deployed in a Gemini Gem

## Source
Extracted from: [You're not behind (yet): How to learn AI in 18 minutes](https://www.youtube.com/watch?v=0Tch0N5nsRU)
Channel: Dan Martell
