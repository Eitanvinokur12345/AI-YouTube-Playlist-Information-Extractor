# [Lumen's initiative] Ship a real-time contrast checker in the editor that flags issues live but never blocks submissions—designers own the fi

> visualization · task `lumen-s-initiative-ship--13734` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Integrate a lightweight, real-time contrast checker into the editor that highlights WCAG compliance issues without interrupting workflows.

**Steps:**
1. **Add contrast checker module** to the editor’s core (e.g., `src/utils/contrastChecker.js`) using a library like `tinycolor2` for hex/rgb parsing and WCAG score calculation.
2. **Hook into editor events** (e.g., `onInput`, `onSelectionChange`) to trigger checks on text/background color changes; debounce to avoid excessive recalculations.
3. **Render inline flags** via a non-blocking UI layer (e.g., `src/components/ContrastWarning.tsx`) that overlays the editor with subtle indicators (e.g., red underline for low contrast) and a tooltip explaining the issue.
4. **Persist user overrides** in local storage (e.g., `contrastOverrides.json`) to suppress false positives or ignore intentional design choices.
5. **Log metrics** (e.g., `src/logs/contrastIssues.log`) for visualization-lead review without exposing data externally.

**Needs:**
- Access to editor’s color parsing system (e.g., `getComputedStyle` or design token API).
- Permission to modify core editor files (e.g., `src/` directory).
- `tinycolor2` or equivalent npm package installed in the project.
- Local storage write access for user overrides.
```
