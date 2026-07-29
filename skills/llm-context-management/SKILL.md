---
name: llm-context-management
description: "Optimizing LLM interactions, reducing costs, improving accuracy, preventing context rot."
---

# LLM Context Management

## Overview
Understanding how the context window of a Large Language Model (LLM) works, including its capacity (tokens), how conversation turns and file reads consume context, and the impact of a full context on cost, accuracy, and performance (context rot). Knowing when and how to clear context to maintain optimal performance.

**Use case:** Optimizing LLM interactions, reducing costs, improving accuracy, preventing context rot.

## Key steps
1. Use /context to monitor token usage.
2. Clear context with /clear when switching tasks.
3. Be aware that every prompt re-reads the entire context.
4. File reads consume significant context and persist until cleared.

## Details
- **Category:** agents
- **Tool:** claude  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=B02zy3adeb0
