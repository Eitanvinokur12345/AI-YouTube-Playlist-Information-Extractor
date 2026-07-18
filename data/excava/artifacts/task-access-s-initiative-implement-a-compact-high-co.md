# [Access's initiative] Implement a compact, high-contrast skip link always visible above primary nav—tested with Playwright MCP for keyboard na

> accessibility · task `access-s-initiative-impl-39185` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
## Approach:
Implement a compact, high-contrast skip link above primary navigation, ensuring keyboard operability and screen reader compatibility, validated via Playwright tests.

### Steps:
1. **Create skip link markup**
   - Add `<a href="#main-content" class="skip-link">Skip to main content</a>` as the first focusable element in `<body>`.
   - Style with high-contrast colors (e.g., `background: #000; color: #fff; padding: 0.5rem 1rem;`), fixed positioning (`top: 0; left: 0;`), and `transform: translateY(-100%)` (reveal on `:focus-within` or `:focus-visible`).

2. **Add CSS for visibility**
   - Ensure `.skip-link` is visible when focused (e.g., `transform: translateY(0);` on `:focus`).
   - Test contrast ratio ≥ 4.5:1 (use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)).

3. **Implement Playwright test**
   - Create `tests/skip-link.spec.ts` with:
     ```ts
     import { test, expect } from '@playwright/test';
     test('skip link is keyboard accessible', async ({ page }) => {
       await page.goto('/');
       await page.keyboard.press('Tab'); // Focus skip link
       await expect(page.locator('.skip-link')).toBeFocused();
       await page.keyboard.press('Enter'); // Activate
       await expect(page.locator('#main-content')).toBeFocused();
     });
     ```
   - Run via `npx
