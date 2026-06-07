---
name: ai-video-editing-claude-remotion-whisper
description: "Use when you want to edit and produce polished YouTube videos or Shorts entirely with AI tools — no Premiere Pro, no Final Cut, no manual editing."
---

# AI Video Editing Pipeline (Claude + Remotion + Whisper)

## Overview
A no-traditional-editor video production workflow: Claude orchestrates the pipeline, Remotion handles clip merging and code-driven transitions, and Whisper transcribes speech and auto-places text overlays at correct timestamps. Produces channel-quality content from raw phone footage.

## Key Techniques
- Use Whisper for accurate speech-to-text with timestamps for synchronized captions
- Use Remotion (React-based) to programmatically merge clips and build transitions via code
- Use Claude to normalize audio, orchestrate the pipeline, and handle edge cases

## How to Apply
1. Shoot clips on your phone.
2. Run Whisper on your audio to get timestamped transcription.
3. Ask Claude to: normalize audio to YouTube standards, strip background noise, and write Remotion code to merge clips with transitions.
4. Have Claude auto-place text overlays at Whisper-provided timestamps in the Remotion script.
5. Render the final video via `npx remotion render`.
6. Upload directly — no editing software opened.

## Examples
- A solo creator produces and publishes weekly videos entirely via this pipeline with no editing software.
- A team generates localized versions of the same video by swapping Whisper transcription language and re-rendering.

## Source
Extracted from: [I Edited This Entire Video With AI (No Premiere, No Final Cut)](https://www.youtube.com/watch?v=qck6zHy2WPs)
Channel: Neo-Pioneer
