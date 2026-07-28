---
name: claude-mem
description: "Use when Claude needs to remember what happened in past sessions — Claude Mem captures, compresses, and re-injects session history as searchable persistent memory."
---

# Claude Mem

## Overview
A persistent memory system for Claude that captures everything an agent does during a
session, compresses it with AI, and injects relevant context back into future sessions, with
natural-language memory search and a web viewer for real-time memory streams.

## Key Techniques
- Automatic context preservation across sessions via 5 lifecycle hooks.
- Natural-language memory search through the mem-search skill.
- Hybrid semantic/keyword search backed by a local SQLite + Chroma vector database.
- Privacy controls via `<private>` tags to exclude sensitive content from stored memory.

## How to Apply
1. Install with `npx claude-mem install` or `/plugin install claude-mem` inside Claude Code.
2. Work normally — the lifecycle hooks capture and compress session activity automatically.
3. Search past sessions in natural language when you need prior context.
4. Wrap anything sensitive in `<private>` tags so it's excluded from persistent storage.

## Examples
Recommended as one of "5 Claude skills you need," fixing the common complaint that Claude
"forgets everything" between sessions by giving it a real, searchable memory store.

## Source
Extracted from: [5 Claude skills you need](https://www.youtube.com/watch?v=W1_hQoDYVXU)
Channel: TheCyborgGirl
Repo: thedotmack/claude-mem (88.8k stars)
