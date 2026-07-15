# [Access's initiative] Implement a hidden skip link that appears only after keyboard focus, tested for contrast and reduced motion

> accessibility · task `access-s-initiative-impl-71652` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a skip link that becomes visible only when keyboard-focused, ensuring WCAG 2.2 AA contrast (4.5:1) and respecting `prefers-reduced-motion`.

**Steps:**
1. **Add HTML/CSS:**
   - Insert `<a href="#main" class="skip-link">Skip to content</a>` before `<main>` in the layout file (e.g., `src/layouts/base.html`).
   - Style `.skip-link` with:
     ```css
     .skip-link {
       position: absolute;
       left: -9999px;
       top: 0;
       background: #005fcc;
       color: white;
       padding: 0.5rem 1rem;
       z-index: 999;
       transition: left 0.2s ease;
     }
     .skip-link:focus {
       left: 0;
     }
     ```
   - Verify contrast ratio (e.g., `#005fcc` on white = 4.6:1) using [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).
   - Add `@media (prefers-reduced-motion: reduce) { .skip-link { transition: none; } }`.

2. **Test Keyboard Navigation:**
   - Navigate via `Tab` key in Chrome/Firefox with screen reader (NVDA/JAWS) to confirm visibility and focus order.

3. **Automated Checks:**
   - Run `axe-core` via Playwright:
     ```bash
     npx playwright test --project=chromium --grep "skip-link"
     ```
