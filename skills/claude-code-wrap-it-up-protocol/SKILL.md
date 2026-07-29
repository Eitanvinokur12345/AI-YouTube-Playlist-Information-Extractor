---
name: claude-code-wrap-it-up-protocol
description: "Use when closing out a Claude Code session, right before running /clear, to make sure project memory, sync, and time tracking aren't lost."
---

# Claude Code "Wrap It Up" Session Close-Out Protocol

## Overview
A short trigger phrase said to Claude Code before /clear that bundles end-of-session
housekeeping into one step: updating CLAUDE.md, syncing every project touched, and
logging billable time.

## Key Techniques
- A fixed spoken/typed trigger phrase instead of a multi-step manual checklist
- Updating CLAUDE.md with what changed during the session
- Syncing every project touched in the session before clearing context
- Logging billable time automatically as part of the same step

## How to Apply
1. Before running /clear at the end of a work session, say or type your close-out phrase
   (e.g. "wrap it up").
2. Have Claude Code update CLAUDE.md with the session's changes.
3. Have it sync every project that was touched during the session.
4. Have it log the session's billable time.
5. Only then run /clear, so nothing from the session is lost to the reset.

## Examples
Demonstrated in the source video as a 3-step outcome triggered by two words ("wrap it
up"): CLAUDE.md update, project sync, and billable-time logging, all before /clear.

## Source
Extracted from: [My WRAP IT UP Protocol for Claude Code (3 Steps)](https://www.youtube.com/watch?v=uop2iPerLsQ)
Channel: Giuseppe Builds
