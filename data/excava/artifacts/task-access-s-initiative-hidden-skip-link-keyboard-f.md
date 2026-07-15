# [Access's initiative] Hidden skip link (keyboard-focus only) wins

> accessibility · task `access-s-initiative-hidd-14006` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a hidden skip link visible only on keyboard focus to bypass navigation blocks, meeting WCAG 2.2 Level A.

**Steps:**
1. **Add HTML skip link** in `src/layouts/base.html` (or equivalent root template):
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
2. **Style skip link** in `src/styles/main.css`:
   ```css
   .skip-link {
     position: absolute;
     left: -9999px;
     top: 0;
     background: #000;
     color: #fff;
     padding: 8px;
     z-index: 999;
   }
   .skip-link:focus {
     left: 0;
   }
   ```
3. **Add target ID** to main content container in `src/layouts/base.html`:
   ```html
   <main id="main-content" tabindex="-1">
   ```
4. **Test keyboard navigation** via:
   - Chrome DevTools → Device Toolbar → Keyboard (⌘+F12 → More Tools → Rendering → Emulate vision deficiencies → Keyboard)
   - Manual tabbing with screen reader (NVDA/JAWS) to verify focus visibility.
5. **Verify contrast** with `axe DevTools` or `WebAIM Contrast Checker` on the skip link text.

**Needs:**
- Access to project’s root template (`base.html` or equivalent).
- Write access to `src/styles/main.css`.
- Browser with keyboard/screen reader testing capability (NVDA/JAWS/VoiceOver).
- `axe DevTools
