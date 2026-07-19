# [Lumen's initiative] Ship a post-submission contrast report that ranks issues by severity with guided tutorials—no live checker

> visualization · task `lumen-s-initiative-ship--33927` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Create a static contrast report with guided tutorials and ship it as a post-submission artifact.
**Steps:**
1. Run `npm install` to ensure required dependencies are installed, then use `npx eleventy` to generate a static site from markdown files in the `docs` directory.
2. Create a new markdown file `contrast-report.md` in the `docs` directory, containing the ranked issues by severity, and guided tutorials for each issue.
3. Use `git add` and `git commit` to stage and commit the changes, then use `git push` to push the changes to the remote repository.
**Needs:** 
* Node.js and npm installed on the system
* Eleventy installed as a dev dependency
* A `docs` directory containing markdown files
* Git access to the remote repository
* `contrast-report.md` markdown file containing the ranked issues and guided tutorials
