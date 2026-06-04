# Review Protocol — 3 agents, Claude first then external

This file is read by the Claude Code GitHub Action in the **review stage**
(`.github/workflows/review.yml`). It is a *quality gate*, separate from analyze
(`CLAUDE.md`) and improve (`IMPROVE.md`). It does **not** change skills, tools,
or the dashboard — it **inspects** the whole system from three independent angles
and writes findings the improve stage and dashboard then act on / surface.

Governed by the `review` block in `config.json`. Read it first; if
`review.enabled` is false, do nothing and exit.

## The three reviewers (different conditions, on purpose)

1. **Usability / UX** (`dimension: "usability"`) — judge the dashboard the way a
   first-time visitor would: how easy is it to *read* information, *find* what you
   want, and *trust* it? **Benchmark against the competitors** in
   `review.usability.competitors` (Future Tools, There's An AI For That, Toolify,
   Product Hunt AI) — what do they do better at discovery, scanning, filtering,
   and visual hierarchy, and what should this dashboard borrow? Inspect
   `docs/index.html` + `docs/dashboard.js` + the live data shapes.
2. **Cut the bullshit** (`dimension: "cut_the_bullshit"`) — hunt vague, padded,
   hype, or filler content: two-sentence "summaries" that say nothing, duplicate
   tips, marketing adjectives with no substance, scores with no evidence, generic
   descriptions ("a powerful AI tool"). Flag the specific record + the leaner
   rewrite. Bias toward *less, sharper* text.
3. **Deep code-bug researcher** (`dimension: "deep_code_bugs"`) — read the actual
   code (`src/*.py`, `docs/dashboard.js`, `docs/sw.js`, the workflow YAML) looking
   for real bugs: crashes, unhandled errors, race conditions in the per-video
   commit/push loop, encoding issues, broken fetch paths, schema drift between
   what analyze writes and what the dashboard reads, dead code, and security
   smells (anything that could leak a secret). The automated arm of this reviewer
   is **CodeQL** (`.github/workflows/codeql.yml`, free for public repos); read its
   latest alerts if available and corroborate. Report concrete file:line issues.

## Claude first, then external (`review.claude_first_then_external: true`)

You (Claude) run **first** and write the full `review_findings.json`. After you
finish, the workflow runs `src/external_review.py`, which asks a **different**
engine (`review.external_engine`, gemini free tier, key in the
`EXTERNAL_REVIEW_API_KEY` secret) for a second opinion — to verify your findings
and add anything you missed. If the secret is absent or the call fails, that step
**skips gracefully** and leaves your findings intact. Never put the key in any
file or log.

## First-week intensive (`review.first_week_intensive: true`)

If `config.cadence.first_week.enabled` is true and we are within the first week
since `config.cadence.first_week.started_at` (or it is still `null` → treat the
first run as the start), set `mode: "first_week_intensive"`, review **more
thoroughly**, and lower the severity bar (surface medium/low issues you might
otherwise defer). Outside the first week, set `mode: "weekly"` and focus on
high-impact findings.

## What to write — `data/review_findings.json`

Read the existing file first (default `{ "findings": [], "history": [] }`) so you
don't lose history or re-raise resolved items. Write:

```json
{
  "generated_at": "<ISO-8601>",
  "mode": "weekly",
  "reviewers": {
    "claude":   { "ran_at": "<ISO-8601>", "ok": true },
    "external": { "provider": "gemini", "status": "pending", "reason": "" },
    "codeql":   { "status": "see GitHub Security tab", "alerts_seen": null }
  },
  "scores": { "usability": 0, "cut_the_bullshit": 0, "deep_code_bugs": 0, "overall": 0 },
  "benchmark": {
    "competitors": ["Future Tools", "There's An AI For That", "Toolify", "Product Hunt AI"],
    "we_do_better": [ "..." ],
    "they_do_better": [ "..." ],
    "borrow_next": [ "1-3 concrete, cheap UX ideas worth copying" ]
  },
  "findings": [
    { "id": "<stable-hash>", "dimension": "usability|cut_the_bullshit|deep_code_bugs",
      "severity": "high|med|low", "area": "dashboard|engine|data|workflow|security",
      "where": "docs/dashboard.js:512  (or a record slug / tab id)",
      "detail": "Exactly what's wrong, concretely.",
      "suggestion": "The specific, minimal fix.",
      "status": "open" }
  ],
  "top_actions": [ "The 3-5 highest-leverage fixes, plain English." ],
  "history": [ { "date": "<date>", "usability": 0, "cut_the_bullshit": 0, "deep_code_bugs": 0, "overall": 0 } ]
}
```

Rules:
- `scores` are honest 0–10 per dimension; `overall` is their average. Append a
  `{date, …scores}` row to `history` (keep ~30).
- `id` is a stable hash of `dimension+where+detail` so the same issue isn't raised
  twice across runs. If a previously-open finding is now fixed, drop it from
  `findings` (history keeps the trend).
- Leave `reviewers.external.status: "pending"` — `external_review.py` overwrites
  it with `ok` / `skipped` / `error` and may append `external_*` findings.
- **Stay read-only on content.** Do not edit skills/tools/dashboard here. For
  actionable findings, *optionally* write a matching `ui_change` (dashboard) or
  `skills_folder_learning` (engine) suggestion to
  `data/improvement_suggestions.json` so the user can approve it and the improve
  stage applies it — never apply it yourself in this stage. Never touch a frozen
  record (`data/stars.json`).
- Respect a token budget similar to improve; if large, finish the dimension
  you're on, write what you have, and stop cleanly.

## Commit

```bash
git config user.name "skills-tracker-bot"
git config user.email "actions@users.noreply.github.com"
git add data docs
git commit -m "review: <mode> — usability/bullshit/bugs findings" || echo "nothing to commit"
git pull --rebase --autostash origin main || true
git push || echo "push skipped"
```

## Checklist
1. Read `config.review` (+ `cadence.first_week`); exit if disabled. Pick `mode`.
2. Usability review + competitor benchmark (`docs/*`).
3. Cut-the-bullshit pass over the data (records, tips, summaries, scores).
4. Deep code-bug pass over `src/*`, `docs/*.js`, workflows; read CodeQL alerts if present.
5. Write `review_findings.json` (scores, benchmark, findings, top_actions, history).
6. Optionally write `ui_change` / `skills_folder_learning` suggestions — never auto-apply.
7. Commit. The workflow then runs the external second opinion.
