# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-978` (dept) · 2026-08-16T05:03:13.747635+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 2px #fff outer stroke at 100% opacity for keyboard navigation.

**Plan:**
1. Implement the 2px solid #005fcc focus ring with a 2px #fff outer stroke at 100% opacity.
2. Test WCAG 2.2 AA contrast on all backgrounds (light, dark, and very light).
3. Ensure the focus ring remains visible and distinct in all modes (contrast, mobile/touch, reduced-motion, keyboard nav).
4. Update EXCAVA’s design system documentation to include the new focus ring specifications.
5. Validate changes across all supported browsers and devices.
6. Deploy the updated focus ring styles to production.

**What changed:**
Focus ring updated to 2px #005fcc with 2px #fff outer stroke at 100% opacity for guaranteed WCAG 2.2 AA contrast.
