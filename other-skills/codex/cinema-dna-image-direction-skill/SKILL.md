---
name: cinema-dna-image-direction-skill
description: "Use when an agent's AI-generated images look flat or generic (like loading screens or billboard ads) and you want cinematic, story-connected shots instead."
---

# Cinema DNA Image-Direction Skill

## Overview
A packaged skill for Codex that teaches it to think like a cinematographer when
directing AI image generation, instead of just describing a subject and style.

## Key Techniques
- Specify camera position explicitly (angle, distance, framing)
- Specify who is looking at whom (eyeline/gaze direction) to create implied narrative
- Specify where light comes from (direction, hardness, color) to build mood
- Request multiple connected shots (e.g. 3, in 21:9) instead of one isolated image

## How to Apply
1. When prompting an image-generation agent, add camera-position, gaze-direction, and
   light-source details on top of subject/style description.
2. Ask for a small set of connected shots (the source video uses 3, at 21:9) that read
   as consecutive frames of one scene rather than unrelated single images.
3. Use this as a reusable skill/preset so every generation applies the same direction
   rules instead of re-explaining them per prompt.

## Examples
Source video contrasts a flat, "loading screen"/billboard-ad-looking AI image against
a cinematic 3-shot, 21:9 sequence produced once camera position, gaze, and light source
are specified.

## Source
Extracted from: [This Codex Skill Makes Your AI Images Look Like Real Cinema](https://www.youtube.com/watch?v=mKazoZ0CA0M)
Channel: Evgenii Arsentev
