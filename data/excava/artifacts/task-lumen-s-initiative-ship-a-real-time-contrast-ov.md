# [Lumen's initiative] Ship a real-time contrast overlay that blocks submission only if issues persist after a 5-second delay, but always surfa

> visualization · task `lumen-s-initiative-ship--82413` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a real-time contrast overlay that blocks submissions only after a 5-second delay if issues persist, using a minimal UI that remains legible at a glance.

**Steps:**
1. **Add overlay logic** to `src/ui/contrast-overlay.js`:
   - Use `MutationObserver` to watch DOM changes for contrast issues.
   - Apply a semi-transparent red/green overlay via CSS `::before` pseudo-element.
   - Trigger a 5-second debounce timer on detection; only block submission if issues remain after delay.

2. **Integrate with form submission** in `src/ui/form-handler.js`:
   - Hook into form `submit` event.
   - Check overlay state; prevent default if overlay is active (issues detected).

3. **Add CSS styling** in `src/ui/contrast-overlay.css`:
   - Define `.contrast-overlay` class with `position: fixed`, full viewport coverage, and high-contrast colors.
   - Ensure text remains readable (e.g., `color: white; background: rgba(255,0,0,0.2)`).

4. **Test locally** with:
   ```bash
   npm run dev
   ```
   - Manually verify overlay appears/disappears correctly and submission is blocked only after delay.

5. **Deploy changes** via:
   ```bash
   git add src/ui/contrast-overlay.{js,css}
   git commit -m "Add real-time contrast overlay with 5s delay"
   git push origin main
   ```

**Needs:**
- Access to `src/ui/` directory in the project.
- Node.js/npm for local testing.
- Browser dev tools for contrast validation.
