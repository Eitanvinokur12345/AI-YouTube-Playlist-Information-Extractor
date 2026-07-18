# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-714` (dept) · 2026-07-18T15:31:01.985590+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a subtle, persistent skip link that expands smoothly on keyboard focus.

**Plan:**
1. Create a skip link element (1px × 1px, transparent) at the top of every page.
2. Style it to expand to a large, high-contrast target (e.g., 44px × 44px) when focused.
3. Ensure the expansion uses CSS transitions (no layout shift).
4. Test with Playwright MCP for no unintended shifts or flashes.
5. Add `tabindex="-1"` to the target section for reliable focus trapping.
6. Document the skip link’s behavior in the accessibility statement.

**What changed:** Skip link now appears only on keyboard focus, expanding smoothly without layout shift.
