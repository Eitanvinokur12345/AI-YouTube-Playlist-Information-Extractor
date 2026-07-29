---
name: claude-video-flipbook-analysis
description: "Use when you need Claude to analyze the actual visual content of a video (cuts, on-screen text, pacing, hook) since Claude has no native video input and would otherwise only see the transcript."
---

# Claude Video Flipbook Analysis (yt-dlp + FFmpeg frame extraction)

## Overview
Claude has no native video/animation input — Anthropic's own docs list only image formats — so
handed a video task directly, Claude only ever sees the transcript and misses the cuts, the
on-screen text, the b-roll, and the pacing that usually explains why a video actually worked.
This skill converts the video into a still-frame image sequence so Claude can "watch" it.

## Key Techniques
- Download the source video locally and losslessly with `yt-dlp` (no re-encoding needed).
- Slice it into one still frame per second with `FFmpeg` so Claude receives a manageable image
  sequence instead of raw video.
- Prompt Claude to treat the frame folder like a flipbook: count cuts, decode the hook (first
  ~3 seconds), and extract every on-screen text line with its timestamp.
- Everything runs locally — no per-frame API cost, and nothing is uploaded to a third party.

## How to Apply
1. `yt-dlp <video_url>` to download the source file.
2. `ffmpeg -i input.mp4 -vf fps=1 frames/frame_%04d.png` to extract one frame per second into a
   folder.
3. Point Claude at the `frames/` folder and ask it to: count the cuts, describe what happens in
   the first 3 seconds specifically, transcribe every on-screen text line with its timestamp,
   and summarize the pacing.
4. Turn the output into a shot list you can hand directly to a video editor.

## Examples
- Reverse-engineering a competitor's viral Short: extract frames, ask Claude "how many cuts in
  this 30-second video, and what's on screen in the first 3 seconds?" to find the hook pattern.
- Building an edit brief: ask Claude to timestamp every on-screen caption so an editor can
  recreate the pacing without rewatching the source video manually.

## Source
Extracted from: [Claude Can't Actually Watch Your Videos Until You Do This](https://www.youtube.com/watch?v=ABAuLH5sKvo)
Channel: Sebastian Hardy | AI Marketing
(Note: the video's linked Google Doc with the exact install commands and all six analysis
prompts returned HTTP 403 — inaccessible without authentication — so this package is built from
the video's own transcript/description only.)
