# [Access's initiative] Implement a high-contrast, always-visible skip button that's styled to look like a functional element, allowing discover

> accessibility · task `access-s-initiative-impl-77909` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a persistent, high-contrast skip link styled as a functional UI element, positioned to remain visible and accessible during all interactions.

**Steps:**
1. **Add HTML Skip Button**
   Insert `<a href="#main-content" class="skip-link">Skip to content</a>` as the first element in `<body>`.
   *File:* `src/index.html` (or equivalent root template).

2. **Add CSS for High Contrast & Visibility**
   Style `.skip-link` with:
   ```css
   .skip-link {
     position: absolute;
     top: 0;
     left: 0;
     background: #000;
     color: #fff;
     padding: 0.5rem 1rem;
     z-index: 9999;
     transform: translateY(-100%);
     transition: transform 0.3s;
   }
   .skip-link:focus {
     transform: translateY(0);
   }
   ```
   *File:* `src/styles/main.css` (or project CSS entry).

3. **Add JavaScript for Persistence**
   Ensure skip link remains visible if JS is enabled (fallback to static high-contrast button if JS disabled).
   *File:* `src/scripts/skip-link.js` (or existing JS bundle).

4. **Test with Screen Reader & Keyboard**
   Verify:
   - Tab order includes skip link.
   - Screen reader announces it.
   - Focus styles meet WCAG 2.1 AA contrast (4.5:1 for text).

**Needs:**
- **Tooling:** Git, text editor (VS Code/Vim), browser dev tools.
- **Access:** Screen reader (
