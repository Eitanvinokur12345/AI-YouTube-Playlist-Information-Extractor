# [Access's initiative] Enforce a logical tab order and add skip links for critical actions to eliminate keyboard traps and enhance navigation f

> accessibility · task `access-s-initiative-enfo-97886` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Audit and enforce logical keyboard navigation with skip links for critical actions in Access.

**Steps:**
1. **Audit current tab order** using browser dev tools (Chrome/Firefox) with `Tab` key and screen reader (NVDA/JAWS). Identify keyboard traps and illogical focus jumps.
2. **Add skip links** (e.g., `<a href="#main-content" class="skip-link">Skip to content</a>`) before primary navigation/headers. Style with `position: absolute; left: -9999px;` and focus styles.
3. **Enforce tab order** via `tabindex` attributes (use `0` for natural order, avoid `tabindex > 0`). Test with `document.activeElement` in console.
4. **Validate fixes** using axe-core CLI (`npm install -g @axe-core/cli && axe http://localhost:3000`) and manual keyboard-only testing.
5. **Document changes** in `CHANGELOG.md` with before/after snapshots of focus order.

**Needs:**
- Access to Access codebase (repo: `access-web`)
- Browser dev tools (Chrome/Firefox)
- Screen reader (NVDA/JAWS)
- axe-core CLI (`npm install -g @axe-core/cli`)
- Test URLs (staging/prod)
```
