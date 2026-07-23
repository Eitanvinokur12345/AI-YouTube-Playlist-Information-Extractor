# [Access's initiative] Implement a high-contrast, always-visible skip button that's styled like a small button, to ensure all users, including 

> accessibility · task `access-s-initiative-impl-78971` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Add a fixed-position, high-contrast skip button to the top-left of every page, visible at all times, that skips to main content.

**Steps:**
1. **Create skip button HTML/CSS**
   - Add `<a href="#main-content" class="skip-button">Skip to main content</a>` to the `<body>` start in `src/layouts/base.html`.
   - Add CSS in `src/styles/skip-button.css`:
     ```css
     .skip-button {
       position: fixed;
       top: 0;
       left: 0;
       z-index: 9999;
       padding: 8px 12px;
       background: #000;
       color: #fff;
       font-size: 14px;
       text-decoration: none;
       border: 2px solid #fff;
       border-radius: 4px;
       margin: 8px;
     }
     .skip-button:focus {
       outline: 2px solid #ff0;
       outline-offset: 2px;
     }
     ```
   - Import `skip-button.css` in `src/styles/main.css`.

2. **Add target for skip button**
   - Add `<main id="main-content" tabindex="-1"></main>` after `<header>` in `src/layouts/base.html`.

3. **Test high contrast & keyboard**
   - Run `npx eslint --rule 'color-contrast: error'` to enforce WCAG 2.1 AA contrast.
   - Manually test with screen reader (NVDA/JAWS) and keyboard tab navigation.

**Needs:**
- `src/layouts/base.html` (must edit)
-
