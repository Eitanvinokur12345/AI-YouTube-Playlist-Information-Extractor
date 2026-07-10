# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-342` (dept) · 2026-07-10T06:49:22.695233+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Freeze Eitan’s taste corpus via SHA256 parity between picks.json & picks.zip before any further inspection—no framing until receipts are identical.

**Plan:**
1. Download Eitan's design picks JSON and ZIP files.
2. Compute the SHA256 checksums for both `picks.json` and `picks.zip`.
3. Save the checksums to `picks.json.sha256` and `picks.zip.sha256`.
4. Compare the two checksums to ensure content parity.
5. Document the comparison result in `parity-verified.txt`.

**What changed:** Emphasis shifted from metadata verification to ensuring content parity through checksum comparison.
