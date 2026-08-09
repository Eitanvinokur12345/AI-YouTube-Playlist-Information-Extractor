# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-537` (dept) · 2026-08-03T02:37:48.986251+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a threshold-based pulse system for EXCAVA’s interface.

**Plan:**
1. Implement a threshold-based pulse: nodes glow once (bright and fast) only when data crosses a predefined meaningful change (e.g., % delta or absolute threshold).
2. Test against a static baseline (no pulses) and a scaled pulse system in a controlled A/B experiment with 3 user groups (n=50 each).
3. Measure user attention via:
   - Time-to-notice for new data (via eye-tracking or click logs).
   - False alarm rate (ignored pulses).
   - Subjective feedback (post-task surveys on distraction/usefulness).
4. Set initial threshold at 5% change for numeric data; adjust dynamically based on pilot data.
5. Add a user-configurable toggle to disable pulses or adjust threshold sensitivity.
6. Deploy with analytics tracking for 2 weeks, then refine thresholds based on false positives/negatives.

**What changed:**
Replaced volume-based scaling with a threshold-based pulse to avoid signal desensitization.
