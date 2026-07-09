# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-151` (dept) · 2026-07-09T15:19:58.346768+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Export only the *current* 3 variants (light/dark/system) of Eitan’s 5 "high-impact" files at 2x—no more.

**Plan:**
1. Create the folder `mine-ai-designs/2024-06-21-eitan-picks/`.
2. Copy the 5 "high-impact" Figma files into the folder: `mine-ai-core`, `mine-ai-hero`, `mine-ai-card`, `mine-ai-modal`, `mine-ai-footer`.
3. Run `figma-export` on the selected files with `--ids=123abc,456def,789ghi,jkl012,mno345 --format=png --scale=2 --suffix=_eitan` to generate PNGs of the current variants.
4. Include only light, dark, and system variants in the export.
5. Create a `README.md` in the folder mapping each design to Mine AI’s stage gaps.
6. Review and validate the exported designs against the current product requirements.

**What changed:** The export was scoped down to only essential designs and variants to align with Mine AI's current product stage.
