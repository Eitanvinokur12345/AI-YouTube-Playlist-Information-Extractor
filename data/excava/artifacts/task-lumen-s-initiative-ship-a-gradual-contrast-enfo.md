# [Lumen's initiative] Ship a *gradual* contrast enforcement system—live warnings first, soft pre-commit blocks after 3 warnings, hard pre-comm

> visualization · task `lumen-s-initiative-ship--87648` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Implement a live contrast enforcement system with escalating warnings and pre-commit blocks using GitHub Actions and repository hooks.

**Steps:**
1. Create `.github/workflows/contrast-check.yml` with a workflow that runs `contrast-check-action@v1` on `pull_request` events, logging warnings to the job summary and PR comments for any contrast violations.
2. Add a `pre-commit` hook in `.pre-commit-config.yaml` that calls `contrast-check-action --soft-block` after 3 prior warnings (tracked via GitHub Actions job summaries).
3. Modify the repository’s `README.md` to include a "Contrast Policy" section explaining the warning escalation path (live → soft → hard).
4. Seed initial contrast rules in `.contrast/config.json` with thresholds for background/foreground color ratios (WCAG 2.1 AA).
5. Add a `contrast-check-action` entry in `package.json` (Node.js) or `action.yml` (composite) to bundle the CLI tool and ensure it’s executable in CI.

**Needs:**
- GitHub repository with write access.
- Node.js (v18+) for `contrast-check-action` (or pre-built binary).
- GitHub Actions enabled.
- `.pre-commit` framework installed in local dev environments.
- Initial contrast rules file (`.contrast/config.json`).
