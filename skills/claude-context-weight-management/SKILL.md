---
name: claude-context-weight-management
description: "Use when a long Claude or Claude Code session is burning tokens, to trim carried conversation history instead of just typing less."
---

# Claude Context Weight Management (Clear/Compact/Rewind)

## Overview
Claude's token cost compounds with conversation length because every reply re-reads the
entire thread — message ten costs more than message one purely from accumulated history.
The fix is managing what history gets carried forward, not typing shorter messages.

## Key Techniques
- **Clear** — reset carried context to zero when a topic is genuinely finished.
- **Compact** — shrink history instead of clearing it, when you still need some prior context.
- **Disconnect unused MCP servers** — connected-but-unused MCP servers still cost context
  tokens before you type a word.
- **Rewind** — delete a wrong-turn exchange instead of arguing with the model, since arguing
  only adds more weight on top of the mistake.

## How to Apply
1. Periodically ask: does this session still need everything said so far? If not, Compact.
2. When a topic is fully wrapped up, Clear rather than letting it linger in context.
3. Disconnect MCP servers you aren't actively using in the current session.
4. If the model goes down a wrong path, Rewind past that exchange instead of correcting it
   in-place, which keeps the mistaken turn (and the correction) both in context.

## Examples
The source video frames it as: "Clear it. Compact it. Keep building." — reduce carried
history, not typed input, to control long-session token cost.

## Source
Extracted from: [4 Ways to Stop Wasting Tokens with AI](https://www.youtube.com/watch?v=a4zZuhvMXts)
Channel: Jack Roberts
