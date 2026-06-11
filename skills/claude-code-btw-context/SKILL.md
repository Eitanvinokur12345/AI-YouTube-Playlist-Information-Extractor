---
name: claude-code-btw-context
description: "Use when you need to ask Claude Code a side question without consuming main context window tokens, keeping the primary task context clean."
---

# Claude Code Context Isolation with /btw

## Overview
The /btw command in Claude Code opens an overlay for side questions that never enter the main context window. Unlike regular messages, /btw exchanges don't consume tokens in the primary conversation, so you can ask clarifying questions, check documentation, or explore tangents without degrading the main task context.

## Key Techniques
- Type `/btw <your question>` to open the side-question overlay
- Use for quick factual questions that don't need to be part of the task history
- Reserve main context for task-relevant exchanges only

## How to Apply
1. During a Claude Code session, identify a question that's tangential to the main task
2. Type `/btw` followed by your question
3. Read the answer in the overlay
4. The overlay closes without adding anything to the main conversation
5. Continue the main task with context budget intact

## Examples
- `/btw what's the syntax for Python list comprehension with conditional?`
- `/btw how many tokens does a typical system prompt use?`
- `/btw is async/await supported in this Node version?`

## Source
Extracted from: [You're burning tokens and don't even know it](https://www.youtube.com/watch?v=2Cw0gaxe-fk)
Channel: Amine Hn | AI Automation
