---
name: claude-code-hyperframes-video-editing
description: "Use when editing video files through a chat interface instead of a timeline editor — Claude Code drives the open-source HyperFrames framework to apply edits and show a live preview."
---

# Chat-Driven Video Editing with Claude Code + HyperFrames

## Overview
HyperFrames (open source, by HeyGen) lets an AI agent render and edit video by generating
HTML/CSS/JS. Paired with Claude Code, you describe the edit you want in plain chat and see
a live preview update, skipping a traditional non-linear editor entirely.

## Key Techniques
- Drive HyperFrames from **Claude Code** (not plain Claude chat) so editing uses local/system
  memory instead of being bounded by the chat context window — this is what lets it handle
  large, GB-sized video files.
- Apply edits incrementally through chat instructions, checking the **live preview** after
  each change before requesting the next one.
- Treat the setup as a repo you install once (HyperFrames + Claude Code config), then reuse
  for every subsequent editing session.

## How to Apply
1. Install and configure HyperFrames alongside Claude Code per the project's setup guide.
2. Open the target video project with Claude Code.
3. Describe the desired edit in chat (e.g. "cut the first 5 seconds", "add a lower-third
   overlay at 0:32").
4. Review the live preview HyperFrames renders; refine with another chat instruction if needed.
5. Repeat until the video matches your intent, then export.

## Examples
- Trimming and adding a title card to a raw screen recording purely through chat prompts,
  watching each change render live.
- Iterating on b-roll placement by asking for adjustments instead of dragging clips on a
  timeline.

## Source
Extracted from: [Claude Can Edit Videos With this Skill](https://www.youtube.com/watch?v=bw6YZFhzRfU)
Channel: Gundeep Ai
Related project: HyperFrames — https://github.com/heygen-com/hyperframes
