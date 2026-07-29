---
name: claude-code-wrap-it-up-protocol
description: "Use when ending a Claude Code session to automatically update CLAUDE.md, sync touched projects, and log billable time before running /clear."
---

# Claude Code Wrap-It-Up Protocol

## Overview
A two-word trigger phrase ("wrap it up") that tells Claude Code to close out a working session
in a repeatable way instead of just running `/clear` and losing context. It turns session-end
into a scripted checklist rather than an afterthought.

## Key Techniques
- Say "wrap it up" at the end of a session instead of clearing immediately.
- Have Claude update `CLAUDE.md` with what changed/was learned this session before it ends.
- Have Claude sync/commit every project touched during the session.
- Have Claude log billable/session time automatically for tracking.

## How to Apply
1. Define a short-form command/alias in your project instructions (or a slash command) that,
   when invoked, runs through: update `CLAUDE.md` → sync all touched repos → log time spent.
2. Say the trigger phrase before every `/clear` so the habit is consistent across sessions.
3. Review the updated `CLAUDE.md` occasionally to prune stale notes it accumulates.

## Examples
The video demonstrates saying "wrap it up" before clearing a Claude Code session, which then
updates the project's `CLAUDE.md`, syncs every touched project, and logs billable time — all
before the context is discarded.

## Source
Extracted from: [My WRAP IT UP Protocol for Claude Code (3 Steps)](https://www.youtube.com/watch?v=uop2iPerLsQ)
Channel: Giuseppe Builds
