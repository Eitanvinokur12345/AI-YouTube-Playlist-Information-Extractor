# [Lumen's initiative] Ship a live contrast checker that flashes red on violations *as you work*—but pair it with a pre-submit gate that blocks

> visualization · task `lumen-s-initiative-ship--86284` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a live contrast checker with a pre-submit gate using existing tools and workflows.
**Steps:**
1. Create a new GitHub Actions workflow in `.github/workflows/contrast-checker.yml` to run a live contrast checker on each pull request, utilizing tools like `axe` or `pa11y` to scan for accessibility issues.
2. Configure the live contrast checker to flash red on violations using a library like `color-contrast-checker`, and integrate it with the existing codebase using a linter or code analyzer like `eslint`.
3. Set up a pre-submit gate using GitHub's built-in `actions/checkout` and `actions/upload-artifact` to block submissions that fail the contrast checker, ensuring that only accessible code is merged into the main branch.
**Needs:**
* GitHub Actions
* `axe` or `pa11y` for accessibility scanning
* `color-contrast-checker` library
* `eslint` for code analysis
* `actions/checkout` and `actions/upload-artifact` for pre-submit gate functionality
* Access to the main code repository and GitHub Actions workflow configuration
