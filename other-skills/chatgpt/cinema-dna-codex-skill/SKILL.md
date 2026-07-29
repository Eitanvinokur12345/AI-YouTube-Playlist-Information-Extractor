---
name: cinema-dna-codex-skill
description: "Use when directing an AI image/video agent (e.g. Codex) to produce cinematic, director-style shots instead of generic AI-art compositions."
---

# Cinema DNA (Codex Skill)

## Overview
A packaged skill for Codex that reframes image generation as cinematography rather than
"pretty picture" prompting: it teaches the agent to reason about camera position, who is
looking at whom, and where the light source is, so output reads as a movie frame instead of a
CG wallpaper/billboard render.

## Key Techniques
- Specify camera position/angle explicitly instead of leaving composition to the model.
- Establish eyeline/who-looks-at-who between subjects to create narrative geography.
- Define a single, consistent light source direction across a shot sequence.
- Generate connected multi-shot sequences (not one isolated image) in a wide cinematic aspect ratio.

## How to Apply
1. Install/invoke the "cinema dna" skill in Codex before an image-generation request.
2. Describe the scene's blocking (camera position, subject eyelines, light source) alongside the
   subject matter, the way a director's shot list would.
3. Ask for a connected sequence (e.g. 3 shots) in a 21:9 cinematic aspect ratio rather than a
   single frame, so the shots read as one continuous scene.

## Examples
The video contrasts a default "beautiful AI image" (flat, loading-screen/billboard look) against
a Cinema DNA output: three connected 21:9 shots with deliberate camera placement, eyelines, and
lighting consistent across the sequence.

## Source
Extracted from: [This Codex Skill Makes Your AI Images Look Like Real Cinema](https://www.youtube.com/watch?v=mKazoZ0CA0M)
Channel: Evgenii Arsentev
