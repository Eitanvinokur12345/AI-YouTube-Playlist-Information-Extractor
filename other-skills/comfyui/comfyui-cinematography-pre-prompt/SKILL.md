---
name: comfyui-cinematography-pre-prompt
description: "Use when ComfyUI image generations look generic and you want a consistent, personal cinematographic style applied automatically."
---

# Personal Cinematography Pre-Prompt for ComfyUI

## Overview
A reusable block of prompt text that encodes your own cinematography taste (lighting setup, lens choice, color grade) so every ComfyUI generation starts from your visual style instead of a generic default look.

## Key Techniques
- Write a standing pre-prompt describing lighting, lens/focal length, and color-grade preferences.
- Prepend that block to the subject-specific part of every prompt.
- A/B compare the same subject with and without the pre-prompt to tune it.

## How to Apply
1. Draft a short paragraph capturing your preferred lighting, lens, and grade (e.g. "golden-hour rim light, 35mm anamorphic, teal-and-orange grade").
2. Save it as a reusable snippet/template in your ComfyUI workflow.
3. Prepend it ahead of the subject prompt on every generation.
4. Iterate the wording whenever the output drifts from the intended look.

## Examples
Source video demonstrates generating two images of an elephant — one plain prompt, one with the cinematography pre-prompt enabled — showing a clear visual upgrade from the same base subject.

## Source
Extracted from: [Stop making "basic" AI images. Do this instead.](https://www.youtube.com/watch?v=SpO5qVQxxP0)
Channel: Mike Staniforth
