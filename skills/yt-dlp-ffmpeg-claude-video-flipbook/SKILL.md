---
name: yt-dlp-ffmpeg-claude-video-flipbook
description: "Use when you need Claude to understand what happens VISUALLY in a video (cuts, on-screen text, pacing, b-roll) rather than just its transcript, since Claude has no native video input."
---

# yt-dlp + FFmpeg Video Flipbook Analysis for Claude

## Overview
Claude's documented inputs are image formats only — it cannot watch a video, and animations
are unsupported. A transcript alone misses most of why a video actually worked: the cuts, the
on-screen text, the b-roll, the pacing. This skill gives Claude an image-based read of a video's
edit structure by turning it into a folder of still frames it can page through like a flipbook.

## Key Techniques
- Download the source video locally with `yt-dlp` (free, open source, works on YouTube and
  thousands of other sites).
- Slice it into one still frame per second with `FFmpeg` — dense enough to catch cuts and
  on-screen text without producing an unmanageable number of images.
- Hand Claude the resulting frame folder and let it read the sequence in order, like a flipbook.
- Both tools run entirely locally: no API costs, nothing uploaded anywhere.

## How to Apply
1. Install the two free CLI tools: `pip install yt-dlp` and FFmpeg (`brew install ffmpeg` /
   `apt install ffmpeg` / the Windows build).
2. Download the target video: `yt-dlp <video-url>`.
3. Extract 1 frame/sec: `ffmpeg -i input.mp4 -vf fps=1 frames/frame_%04d.png`.
4. Point Claude at the `frames/` folder and ask it to analyze the sequence in order.
5. Useful prompts to run against the frame sequence:
   - Count the total number of cuts.
   - Decode exactly what happens in the first 3 seconds (the hook).
   - Extract every on-screen line of text with its approximate timestamp.
   - Produce a shot list an editor could work from directly.

## Examples
The source video demos this exact pipeline to reverse-engineer why a viral short worked —
extracting the hook, the on-screen captions, and the cut rhythm — then handing the resulting
shot list to an editor to replicate the pacing in a new edit.

## Source
Extracted from: [Claude Can't Actually Watch Your Videos Until You Do This](https://www.youtube.com/watch?v=ABAuLH5sKvo)
Channel: Sebastian Hardy | AI Marketing
