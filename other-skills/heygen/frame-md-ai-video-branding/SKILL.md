---
name: frame-md-ai-video-branding
description: "Use when configuring AI agents to generate correctly branded videos by specifying frame-level pacing, scale, and motion rules in a frame.md file."
---

# Frame.md AI Video Branding Workflow

## Overview
AI agents default to treating 16:9 video frames like web pages, breaking brand consistency. This skill uses HeyGen's Hyperframes system and a frame.md specification file to encode brand-specific pacing, scale, and motion rules that AI agents follow during video generation.

## Key Techniques
- Convert your design.md into a frame.md with video-specific rules
- Define pacing intervals, element scale ranges, and allowed motion types per frame region
- Use Hyperframes as the execution engine that reads frame.md during generation

## How to Apply
1. Start with your existing design.md (brand colors, fonts, layout rules).
2. Add video-specific sections: pacing (cuts/second), scale rules, and motion constraints.
3. Save as frame.md in your project root.
4. Point HeyGen or Claude Code to frame.md as the brand spec when generating video.
5. Iterate on frame.md rules based on output review.

## Examples
- Teaching Claude Code to generate branded short-form videos that match a company's motion design language
- Preventing AI from scaling text incorrectly or cutting too fast for a cinematic brand

## Source
Extracted from: [HeyGen Frame.md: Teach AI to Code Branded Videos in Seconds](https://www.youtube.com/watch?v=q8e_hZXq70s)
Channel: geekslab
