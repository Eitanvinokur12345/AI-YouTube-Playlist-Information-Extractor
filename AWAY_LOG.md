# Away-week loop log

_What the autonomous 15-minute loop did while Eitan was away — newest first, one line each. This is the quick-glance summary; full detail is in the git commit messages (each carries its own harsh self-criticism) and staged decisions are in `QUESTIONS.md`. The cloud GitHub beat runs the core program 24/7 underneath all of this regardless._

Repo home: **D:\AI-YouTube-Skills** (migrated off the full C: on 2026-07-23). Loop: CronCreate 15-min, session-only.

- **~07:0x (fire 24, unattended, cloud session, live build v131) — Hub default-sort now floats
  ready-to-use elements up.** Standing checks: local HEAD was 1 commit behind `origin/main`
  (`4e6b667d2`) — `git_safe sync` cleared it, no loss; guardrails 15/16 both before and after (only
  `G-C`, stale backup, resolved in-fire with `git_safe backup`). Picked up the item v127 explicitly
  queued as NEXT and v130 didn't reach: `renderHub()`'s list sort only ordered by
  `verified`-status-then-name, so a browsing session with the `▶ ready to use` filter OFF still saw
  the 3,749 unreadable stubs interleaved with the 6,624 actionable elements at random. Reused
  `elReady(e)` as-is (Ponytail — same pure function the filter/count already share) as the PRIMARY
  sort key ahead of the existing verified-rank/name tiebreak, so the filter and the default order now
  agree on what "ready" means with zero duplicated logic. Verified via CLI/data (no browser, per
  away-mode rule): `node --check docs/dashboard.js` and `docs/sw.js` both pass; a Node simulation of
  the new comparator against the real `data/elements_index.json` (10,373 live elements) confirms (a)
  every ready element sorts strictly before every non-ready one — 0 violations — and (b) the existing
  verified/niche/unverified/dead ordering and alphabetical tiebreak are undisturbed within each
  readiness tier — 0 violations (script kept at
  `/tmp/claude-0/.../scratchpad/verify_sort.mjs`, not committed — scratch only). Bumped
  `APP_BUILD`/`SHELL_CACHE` v130→v131 per the standing rule (§4 SESSION_HANDOFF.md). **Harsh
  self-criticism:** did not verify in an actual browser (correctly deferred per away-mode, but a
  layout/CSS surprise from stub cards suddenly clustering at the bottom of a type tab is still
  possible — next attended session should scroll a populated Hub tab and eyeball it). This is
  browse-layer polish again, the same category v130's own self-criticism called "diminishing value"
  after three fires in a row (v125-127) — chose it anyway because it was a small, cheap, already-
  scoped, zero-risk item explicitly left on the table, not because the Hub is still the best lever;
  the bigger levers (stub backlog, brain-gated enrichment) remain genuinely blocked without Eitan's
  return per fire 23/QUESTIONS.md. Did not touch the brains subsystem, did not sweep any of the
  confirmed-safe stray branches (still deferred to Eitan), and per the git-history precedent
  documented at fire 7 (30+ prior fires/beats push straight to `main` via `git_safe ship`, zero PRs)
  used the same convention here rather than opening a fresh per-session-branch PR that would
  reproduce the orphaned-branch liability fire 6/7 already flagged.

## 2026-07-27
- **~06:0x (fire 23, unattended, cloud session) — found and fixed a real, live false-positive in
  the supervisor (the project's central "is work real" honesty tool), plus surfaced a 3+-week-old
  self-inconsistent department charter that had been silently hiding.** Standing checks first:
  local `origin/main` cache was 1 commit stale (`629da018`, fast-forward, nothing lost — the same
  recurring pattern fires 8/9/16/17/19/20/21 already documented) — `git_safe sync` cleared it;
  guardrails 15/16 pre-fire, 0 critical (only `G-C`, stale backup, self-heals). `systemcheck`
  reported a clean 11/11 with the only blocked department ("watch") already confirmed genuinely
  blocked on Gemini quota by fire 20 — no obviously-broken thing was sitting there, so I looked
  harder at `python -m src.excava_supervisor`'s own output instead of reaching for a sixth
  guardrail-flap fix: 6 of the last 40 tracked completions were flagged `noop` ("theatre"), ALL
  from the "news" department, ALL the exact same text —
  `Ran the trend watch. trend_watch: N proposals (top score X); queued 0 into self-improvement.`
  Traced it: `src/excava_agents.py`'s `REAL_TOOL["news"]` runs `src.trend_watch` (a self-improvement
  trend-proposal tool per its own docstring, nothing to do with news content) for every task the
  "news" department gets, including ones literally named `news-room-action-fetch-*`. `trend_watch`
  DEDUPES queued proposals by key — checked `data/improvement_tasks.json` and found the 5 proposals
  it queued back on 2026-06-29 are STILL open, so "queued 0" has been the objectively correct report
  on every run since (nothing new to add, not nothing done) — the supervisor's blanket `"queued 0"`
  no-op pattern was misjudging a genuinely healthy, deterministic result as a facade. Fixed with a
  targeted carve-out in `judge()` keyed to trend_watch's own report signature (mirrors the existing
  security-dept "0 leaks = good" carve-out already in the same function) — `src/excava_supervisor.py`.
  Along the way found the ROOT cause was one level deeper: `data/excava/intent.json`'s "news" charter
  has said `should_do: "refresh the AI-news digest..."` since it was first authored, but `right_tool`
  was always `src.trend_watch` — self-inconsistent from day one. Because `right_tool` happened to
  already match the actual code (`REAL_TOOL["news"]`), the supervisor's own intent-drift detector
  (the exact mechanism that already caught mining/visual/memory drift in earlier fires) had nothing
  to flag and stayed silent for 3+ weeks. `data/excava/agents.json`'s independent "news" dept
  description ("refresh official-site AI news") confirms headline-refresh really was the true
  original intent. Restored `intent.json`'s `right_tool` to `src.news` (the tool that actually
  matches `should_do`) with a full explanatory `note` — this makes the drift VISIBLE going forward
  (`systemcheck`'s "intent aligned" line now honestly reads 10/11, 1 tool-drift, not 11/11) without
  changing any executed code. **Deliberately did NOT rewire `REAL_TOOL["news"]` to actually call
  `src.news`** — flagged as a real decision for Eitan in QUESTIONS.md instead of forcing it through
  unattended: `src/news.py` already runs independently every 6h via `.github/workflows/news.yml` and
  writes files CLAUDE.md governs as the separate YouTube-playlist-analyzer pipeline's own territory
  (out of this fire's scope per the hard constraints), and it sequentially fetches ~95 RSS sources at
  up to 15s each — comfortably past `_run_real_tool`'s hardcoded 90s subprocess timeout, which would
  trade today's honest no-op for a noisier "failed (timed out)." **Verified:** 8-case unit check
  against `judge()` (real trend_watch strings incl. a 0-proposals case, a genuine visual no-op, an
  empty/planned result, a blocked result, and the pre-existing security 0-leaks carve-out) — all 8
  correct, zero regressions; live re-run of `python -m src.excava_supervisor` against the real,
  unmodified `data/excava/bus.json` shows `real_pct` jump 82%→100% the moment the fix lands (0 noop,
  was 6); `python3 -c "json.load(...)"` on `intent.json` after editing. `python -m src.guardrails` →
  15/16 both before and after (only `G-C` flaps, self-heals on ship). **Harsh self-criticism:** the
  100% real_pct is now itself worth being suspicious of — I fixed a real false-positive, but a
  supervisor that reads 100% could just as easily be hiding the NEXT genuine no-op behind a
  carve-out that's slightly too broad; my carve-out is keyed narrowly to trend_watch's own exact
  two-substring signature (verified only that phrase appears anywhere else in the codebase, via
  grep, before trusting it), but "narrow enough today" is not a permanent guarantee if trend_watch's
  own output format ever changes. I chose to surface the intent-drift via the SAME existing detector
  other fires already used for mining/visual/memory rather than writing new prose, which keeps the
  fix consistent with established practice — but flipping `right_tool` does drop `systemcheck` from
  a clean 11/11 to 10/11, and I already worry a future fire skimming that number fast will read it as
  a regression to "fix" by reverting my change rather than reading the note; said so as plainly as I
  could in both this note and the intent.json note itself. I did NOT resolve the actual underlying
  question (should the news department really run `src.news`) — correctly left as Eitan's call per
  the hard constraints, but it means the department stays doing work unrelated to its own name and
  charter until he decides, same as it has for 3+ weeks already. Did not touch the ~20 confirmed-safe
  stray branches (still his call, fire 19) or anything brain-side.

- **~05:0x (fire 22, unattended, cloud session) — landed QUESTIONS.md #10, a real (non-duplicative)
  M3/Hub increment.** Standing checks first: local `origin/main` cache stale (re-fetched, nothing
  lost), upstream tracking already set; guardrails 15/16 pre-fire (only `G-C`, stale backup — fixed
  with `python -m src.git_safe backup`). `python -m src.excava_systemcheck`: 11/11, all critical OK
  — no broken system to chase this fire (unlike 16/17/19/21). Checked recent Actions run history via
  the GitHub API for the excava-beat workflow: mostly `cancelled` conclusions, but confirmed via the
  concurrency-group + 5.3h-job + 10-min-cron math (`cancel-in-progress: false`, one queue slot) that
  this is the DESIGNED supersession pattern fires 16/17/19/20/21 already understood, not a new
  regression — the current run (started right after fire 21's fix) is alive and landing heartbeats
  normally. Rather than re-diagnose an already-closed area or hand-grind `backlog.json`'s
  `queued_now` (fire 20 already flagged that as duplicating what the CI beat drives continuously),
  picked the one item in QUESTIONS.md §D marked "will do unless you object, default: yes" that was
  still open: **#10, fold `formats.json` into the Designs tab as a content-type filter.** Shipped:
  `docs/dashboard.js` — the Designs tab now merges `data/formats.json`'s 95 layout/diagram records
  into the same gallery as the 978 website/app designs, behind a new subnav (All / Websites·apps /
  📐 Formats (95)) alongside the existing style-tag filter; format cards render distinctly (kind pill
  + description + `rebuild_hint`, no screenshot — there isn't one) and are excluded from the ⚔ Arena
  pool (no live URL to compare two of). Bumped `APP_BUILD`/`SHELL_CACHE` v129→v130 and added the
  matching SESSION_HANDOFF.md §0d entry (G-E/G-I both require this in lockstep — learned from the
  fires that built those guardrails). **Verified via CLI/data, not the browser** (away-mode rule):
  `node --check docs/dashboard.js` passes; a Python simulation of the exact merge/slugify logic
  against the real `data/formats.json` + `data/designs.json` confirms all 95 formats map to a
  non-empty slug/name and the 978 existing designs are untouched. Guardrails 16/16 after (0 critical)
  once synced. **Harsh self-criticism:** could not verify the actual rendered card/CSS in a real
  browser from this unattended session — the away-mode rule is correct to forbid it here (flaky
  headless, can prompt), but it is a real residual risk; next attended session should open the
  Designs tab and glance at a Formats card before trusting this is pixel-clean. Also did not touch
  the ~20 confirmed-safe stray branches (still Eitan's call, per fire 19) or the brains subsystem
  (out of scope per `away_mode.json`). Scope stayed to the one queued item — did not try to also
  knock out backlog.json entries or re-open the excava-beat cancellation investigation just because
  I'd already gathered the Actions data for it.

- **~04:0x (fire 21, unattended, cloud session) — chased a false alarm to ground, then landed the
  real fix: guardrails.py now self-fetches instead of trusting a caller to have done it.**
  Standing checks first, per the ritual — but this fire ran `python -m src.guardrails` directly
  before that, and got a scary reading: `G-G` "NOT in sync (behind/ahead: 50 50)", `G-P` "last
  excava-beat commit 38.0h ago." Before treating either as real, cross-checked against the GitHub
  API (not just local git, per fires 8/9/10/16/17/19/20's own precedent for exactly this trap):
  `main` was current (`skills-tracker-bot` had just landed `connectors-verify: 2026-07-27T03:58Z`,
  and the container's own fire-20 commits were already ancestors of it) — the "50/50" and "38h"
  were both artifacts of this session's *own* local `origin/main` cache never having been
  fetched yet this fire. Also checked the one thing that WAS only visible via the authoritative
  GitHub Actions API and not local git: `excava_beat.yml` run `30228872527` had been `in_progress`
  since `01:06Z` (~3h, well inside its 5.3h budget) but had stopped landing "excava-beat #N" commits
  after `#6` (`02:00Z`) and `movement.json`'s done-counter had been flat at 4657 across real,
  spaced-out samples from `02:04` to `04:04` — the same "room-advance loop wedged inside an
  otherwise-alive job" pattern fires 16/17 already diagnosed. Cancelled that run (its own
  concurrency group queues, `cancel-in-progress: false`, so nothing else could start while it sat
  wedged) so a fresh beat can pick up immediately instead of waiting out the remaining ~2.5h.
  **The actual fix, not just a diagnosis:** `guardrails.run()` now does one quiet
  `git fetch origin main` before any check runs, so `g_remote_sync`/`g_beat_heartbeat` can never
  again read a stale cache regardless of whether `standing_checks.py` ran first — closes the exact
  gap that produced this fire's own false alarm and four earlier ones. Verified: re-running
  `python -m src.guardrails` standalone (no prior fetch) now correctly shows `G-G` "HEAD ==
  origin/main" and `G-P` "2.1h ago" instead of the phantom 50/50 and 38h. `git_safe sync` pulled
  the 2 real commits `main` had gained during this investigation; guardrails 15/16 after (only
  `G-M` still flags the same flat done-counter — expected, since the wedged run I just cancelled
  is exactly why it hadn't moved; should self-clear once the next beat lands real completions).
  **Harsh self-criticism:** the false-alarm chase ate most of this fire's budget — proportionate
  given it could have been real and four prior fires already paid this exact cost without fixing
  it at the source, but the actual product surface (M1/M2/M3 milestones) got zero attention this
  cycle. The cancelled run is a judgment call made unilaterally (workflow cancellation is a
  shared-state action) — defensible since the evidence (dead heartbeat + flat done-counter for
  2h inside a job whose own design commits every ~10 min) was concrete and the alternative was
  ~2.5 more idle hours, but worth Eitan's awareness, not silent.

## 2026-07-27
- **~03:0x (fire 20, unattended, cloud session) — 10-fire checkpoint (every-10th-heartbeat review)
  + two real guardrail fixes, no new code gap found this cycle.** Standing checks first: local
  `origin/main` cache was stale again (`1f9ed759`→`3b6df8ff`, same recurring sandbox-checkout
  artifact fires 16/17/19 already documented — re-fetched, nothing lost). Guardrails pre-fire
  13/16 (0 critical): `G-C` (no recent history bundle) and `G-G`/`G-P` (stale local `origin/main`
  making remote-sync + beat-heartbeat look wrong) all failing. Fixed for real: ran
  `python -m src.git_safe backup` (fresh bundle → `G-C` now passing) and the `origin/main` re-fetch
  (→ `G-G` "HEAD == origin/main", `G-P` "last beat 1.1h ago", both passing — confirmed via the
  GitHub API directly, not just the local check, that `origin/main`'s real tip already carried
  fire 19's commits and 6 more `excava-beat` cycles). Guardrails now 16/16 (`G-M` alone reads
  "STALLED" — same known-flappy artifact of an infra-only fire producing no new video-analysis
  completions in its own window, not a regression; prior fires document this exact pattern).
  Ran `src.excava_systemcheck`: 11/11 systems working, 0 critical broken; the one real structural
  gap is unchanged from fire 17/19 — "watch" is the last department without a working executor,
  genuinely blocked (checked `src/gemini_video_analyze.py` line-by-line before touching anything:
  it already round-robins all 7 possible Gemini keys with 429/503 backoff — the "needs a non-Gemini
  path or owner capacity" note in `intent.json` is accurate, all keys are actually exhausted, this
  is NOT a coding bug I almost "fixed" with a duplicate of existing logic). **10th-heartbeat review**
  (owner's away-mode asked for a check-in every 10 fires): storage 30.4GB free on the repo drive
  (`G-N`, healthy, no cleanup needed); fire 19 completed cleanly (its commits are on `origin/main`,
  verified via API, not just local git); no operational limits exceeded (0 critical guardrail
  failures across this window); across fires 11-19 the loop landed 2 genuine department-executor
  builds (visualization, then this fire confirmed watch is legitimately blocked not neglected),
  2 real stranded-branch rescues (fire 19), 3 guardrail additions/fixes (`G-M` recount, `G-P` new,
  this fire's `G-C`/`G-G`/`G-P` refresh), and flagged the branch-deletion decision for you
  (`QUESTIONS.md`, fire 19) — nothing is silently broken. **Harsh self-criticism:** this fire is
  AGAIN mostly verification + two small guardrail fixes rather than new product surface — I looked
  hard for a real M1/M2 increment (read `EXCAVA_V2_STEPS.md`'s M1 checklist, confirmed
  `deep_retrieve`/`discovery_agent`/`element_model`/`verify_elements`/`prewarm`/`relate`/
  `source_trust.json` all exist AND are wired into `docs/dashboard.js`, not just present as dead
  files; M1's tutorial/podcast ship-artifacts already exist too, `data/tutorials.json` +
  `docs/tutorials/m1-podcast.wav`) — M1 genuinely looks complete or very close to it, which is good
  news, but means I did not manufacture a change just to have shipped one; I verified before
  claiming, including nearly writing a false "fix" for `gemini_video_analyze.py`'s key rotation
  before reading it closely enough to see it was already correct. The honest backlog for a future
  fire is `data/excava/backlog.json`'s own `queued_now` (verify-the-next-200-unverified-elements;
  raise G8 personal-fit) — those are department-executor work the CI beat already drives
  continuously, not something this session-based fire should duplicate by hand.

- **~02:0x (fire 19, unattended, cloud session) — finally ran the branch sweep fires 6/7/9
  kept flagging as unstarted, and it paid off: found and landed two genuinely stranded pieces
  of real work instead of a symptom-free audit.** Standing checks first: local `origin/main`
  cache stale (`1f9ed759`→`fef8223f`, re-fetched, nothing lost), upstream tracking missing on
  this session's branch (auto-fixed); guardrails 14/15 pre-fire. Then, rather than re-diagnosing
  the ~20 `claude/kind-shannon-*` branches by hand again, checked systematically: for every
  branch, diffed file lists against `origin/main` restricted to `src/*.py` (zero hits — no
  source-code file is stranded anywhere) and then to docs/skills/json (a handful of shared
  SKILL.md paths absent from `main`, traced to fires 12/13/15's own deliberate anti-boilerplate/
  dedup removals — confirmed via their AWAY_LOG entries, not assumed innocent). Two branches did
  carry real, never-landed content: (1) `kind-shannon-hcwmum` (3 commits, fire 18) had a fully
  written, correct `G-P` "beat heartbeat commit freshness" guardrail in `src/guardrails.py` that
  never reached `main` — ported verbatim, guardrails now defines 16 checks. (2) `kind-shannon-
  yj1a6g` (a day-old branch, pre-dates a history rewrite) had already fully analyzed two videos
  — `SpO5qVQxxP0`, `D6cBsAWwCd0` — that were STILL sitting untouched in `main`'s own
  `data/_pending/`, with real non-boilerplate skills (a ComfyUI cinematography pre-prompt
  technique; an LLM-fingerprinting-via-random-number technique), a ComfyUI tool endorsement, and
  filled news summaries. Rather than let the normal pipeline redo that work from scratch, ported
  all of it: `skills.json` + `index.json` + both `SKILL.md` packages (`other-skills/comfyui/`,
  `other-skills/other/`), the `tools.json` ComfyUI endorsement, `daily_news.json` summaries,
  moved both files `_pending`→`processed`, and updated `run_report`/cumulative counters
  (`total_videos_analyzed` 1520→1522; `total_tools` corrected 844→2847, which was already stale
  before this fire — nobody had recomputed it against the real file count in a while). **Verified:**
  `python -m src.guardrails` → G-P now reports "last 'excava-beat #N' commit 0.2h ago" (passing);
  all 9 touched JSON files re-parse clean; `git_safe ship` confirmed `origin == HEAD` after push.
  **Harsh self-criticism:** did NOT delete any of the ~20 stray branches even though most are now
  confirmed safe to remove (superseded or deliberately-obsoleted content) — branch deletion is a
  destructive, harder-to-reverse action than anything else this fire did, and no prior fire has
  taken it unilaterally either; leaving it as an explicit, cheap decision for Eitan
  (`git push origin --delete <branch>` for the confirmed-stale ones) rather than doing it myself
  in an unattended run. Also did not re-verify EVERY one of the 20 branches commit-by-commit
  (only the ones whose file-diff showed something main didn't already have) — the file-diff
  heuristic can't catch a case where a branch modified an EXISTING file's *content* differently
  from main without adding/removing files; considered this an acceptable bound given the sweep's
  goal (find stranded new capability, not audit every historical line) but flagging the gap
  honestly. G-M still reads "STALLED" — same known-flappy artifact prior fires already documented
  for infra/audit-heavy fires, not a new regression.

- **~00:0x (fire 17, unattended, cloud session) — confirmed fire 16's wall-clock fix actually
  recovered the stall, then gave "visualization" (the last talk_only department) a real
  executor.** Standing checks first (`python -m src.standing_checks`): local `origin/main` cache
  was stale (`1f9ed759`→`3cf7b311`), upstream tracking missing on this session's branch — both
  auto-healed, nothing lost. Re-ran `python -m src.guardrails` + `python -m src.pulse`: G-M read
  "Work is moving" — 4616 done (▲+46 over 13.6h), NOT stalled — confirming fire 16's
  `ROOM_ADVANCE_BUDGET_S` wall-clock bound in `excava.py` did fix the real hang (the long-running
  `excava_beat` cycle it described has since produced completions again). Then picked the next
  concrete, well-scoped gap from `excava_systemcheck`'s own "departments executable" line:
  "visualization" was the one remaining `talk_only` department (`right_tool: null` in
  `intent.json`) — staffed but unable to do real work, same class of gap `accessibility` had
  before fire ~ (2026-07-25) got `src.accessibility_scan`. Built `src/liveliness_scan.py`: a
  read-only, deterministic (no LLM/network) scan matching the department's own charter
  ("visibility, liveliness, clarity... OUR screens") — (1) broken local asset refs in
  `docs/*.html` (`src=`/`href=` pointing at a same-repo file that doesn't exist), (2) shipped
  placeholder text (`Lorem ipsum`, bare `TODO`/`FIXME`, leaked JS artifacts `undefined`/`NaN`/
  `[object Object]` in static markup, template-literal-aware so `${x}` code isn't misread as
  content), (3) data liveliness — every `data/*.json` file `dashboard.js` actually fetches must
  exist, parse, and carry a non-empty payload (an empty top-level list/dict is a screen that
  would render blank). First real run against the live dashboard came back clean (0 issues) —
  a genuinely clean shell, not a bug: a synthetic sanity check (fake broken `<img src>`, fake
  `Lorem ipsum` text, a `${x || "undefined"}` template expression) proved the detectors actually
  fire and don't false-positive on template code. One real false positive DID surface on the
  first live run and was fixed before shipping: "Coming Soon" is EXCAVA's own real, intentional
  tab name (the upcoming-tools view), not unfinished-content boilerplate — dropped that pattern
  rather than ship a checker that nags about a legitimate feature. Wired it in exactly like
  `accessibility_scan`: `REAL_TOOL["visualization"] = "src.liveliness_scan"` +
  `TOOL_DOMAIN` keywords in `excava_agents.py`, `intent.json`'s `right_tool` set from `null`.
  **Verified:** `python -m src.excava_systemcheck` → "departments executable" now
  **13/14 have a real executor, `talk_only: []`** (was 12/14, `talk_only: ["visualization"]`);
  direct call to `_run_real_tool("visualization")` returns `{"ok": true, "tool":
  "src.liveliness_scan", "tail": "liveliness_scan: 0 issue(s) — clean"}` and `_task_tool_fit`
  correctly routes a visualization-worded task to it; `python -m py_compile` clean on both
  touched files; `python -m src.guardrails` → 14/15, 0 critical (only G-C, self-heals on ship;
  G-L flagged the new file pre-commit, resolves on this commit; G-M's own live window shows
  STALLED again simply because this fire did infra work, not analyze/bulk-analyze work — the
  done-counter genuinely didn't move in that narrow window, not a regression, same known-flappy
  behavior past fires already noted). **Harsh self-criticism:** a first-run "clean, 0 issues"
  result is honest but unproven against a REAL break — I have not yet seen this scanner catch a
  genuine problem in this repo's own shell (only the synthetic unit check proves the logic
  fires), so its true value is unconfirmed until either a future regression trips it or someone
  seeds a deliberate break to watch it catch. The data-liveliness check only covers the 7
  `data/*.json` paths `dashboard.js` references by literal string match — a dynamically
  constructed fetch path (template-built, not a literal `data/...json` substring) would be
  invisible to it, same brittleness class `accessibility_scan` already accepts for JS-templated
  HTML. Scope stayed to one department, one new module — did not touch the 187 empty-body
  records, the ~13 stray `kind-shannon-*` branches, or the `watch`/`transcripts` BLOCKED
  departments (both still genuinely blocked on owner resources: Gemini quota / a residential
  IP — not something a fire should route around).

## 2026-07-26
- **~23:0x (fire 16, unattended, cloud session) — chased down G-M's "STALLED (no new
  completions in the last 4 beats)" instead of assuming it was another metric artifact like
  the fire-5/6 one, and it was real: the `excava_beat.yml` job that has been `in_progress`
  since 21:46:40 (run 30220502266) had produced ZERO `excava-beat #N` commits across 70+
  minutes, against a historical cadence of ~6 min/cycle (verified via `git log --grep`).**
  Confirmed via `mcp__github__actions_get`/`actions_list` this is the run that finally started
  after queuing behind the previous 5.3h-budget run (which itself completed successfully at
  21:46:30 — not a crash, just the normal durable-loop handoff). Could not pull live logs for
  the in-progress job (GitHub's log-download API 404s until a job completes), so root-caused
  by reading the code path instead: `excava.py`'s room-advance loop
  (`for r in open_rooms[:18]: for line in chat.advance(r["id"], turns=2)`) had NO wall-clock
  bound, only a room-count bound — and `excava_engines.complete()` already tries up to 3
  engines at up to ~60s each per call, so 18 rooms x 2 turns can chain past an hour of pure
  timeouts on a day where the shared free-engine pool is quota-exhausted (exactly what the
  workflow's own header comment already names as the reason `excava_beat` was split out of
  `bulk_analyze` in the first place). Not a hang/bug — a genuinely unbounded worst case. Fix:
  added `ROOM_ADVANCE_BUDGET_S = 240` and a wall-clock deadline check inside the loop
  (`src/excava.py`) — once 4 minutes of room-advancing elapses, remaining rooms are skipped
  for THIS beat (logged as "N deferred to next beat") instead of silently eating the rest of
  the cycle; the next beat already resumes untouched rooms by design, so nothing is lost, only
  deferred. **Verified:** `python -m src.py_compile` clean; a standalone monkeypatched-clock
  simulation of the exact loop logic (4 rooms fit an assumed 60s/room worst case inside a 240s
  budget, 14 correctly deferred) — could NOT live-verify against the real degraded engine pool
  from this sandboxed session (same network-scope wall fire 10 hit); `python -m src.guardrails`
  13/15, 0 critical, G-M still shows STALLED (expected — it reads history that predates this
  fix; watch PULSE.md over the next few beats to confirm it recovers once this ships and the
  currently-running long cycle eventually exits). **Harsh self-criticism:** I did not (could
  not, from here) prove this is THE actual cause versus a contributing one — there could be a
  genuine hang elsewhere in that 70-minute window I couldn't see without live logs; the fix is
  real and safe regardless (a beat should never be allowed to starve the outer commit loop for
  70+ min on principle), but if PULSE.md's done-counter is STILL flat after this ships and the
  stuck run cycles again, the next fire needs the completed run's actual logs (available once
  it finishes or times out) rather than my code-reading inference. Scope stayed to the one
  confirmed mechanism; did not touch the ~13 stray `kind-shannon-*` branches (still someone
  else's problem) or the 187 empty-body records (still a dedicated-pass item, not a fire-sized
  one).

- **~22:1x (fire 15, unattended, cloud session) — closed the OTHER half of item #11: the 10
  real title-collision DATA records fire 14 deliberately left untouched are now resolved,
  4 merged + 1 correctly NOT merged.** Non-brain front, same chain as fires 10-14. Read
  `maintenance_check.py`'s 5-title sample (of its 10-count) and pulled the FULL description of
  every colliding record before touching anything — refused to blind-merge on name match
  alone. 4 were genuine same-product duplicates the automated slug-dedup missed: skills.json's
  two identical "Codebase Knowledge Graph for Claude Code Token Savings" records (same source
  video, same technique, just two different slugs); tools.json's "Higgsfield AI" / "Higgsfield"
  (same platform, two videos covering different features); "Claude Opus 4.8" / "Claude Opus
  4.8" (same model, one mis-categorized as "productivity" instead of "code"); "Llama" / "Llama"
  (same Meta model). Merged each per CLAUDE.md Step 3 (skills) / Step 3b (tools) compare-and-
  keep-best: kept the higher-`quality_score` record, unioned tips/endorsement_video_ids/
  compatibility, backed the loser up to `deleted_skills.json` (skills) with reason+timestamp
  matching the file's existing convention, logged every merge to `merge_log.json` (matching the
  2026-06-03 gemini-N merges already on record there), pruned `index.json`, deleted the
  redundant `skills/code-knowledge-graph-for-claude-code/SKILL.md` folder (Step 5). The 5th
  pair, "Hermes" (hermes-coding-harness) / "Hermes" (hermes-skill-runner), was NOT merged —
  their descriptions are genuinely different products (an agentic coding harness vs a self-
  hosted skill runner that pairs with "SkillSmith") that just happen to share a brand name;
  merging would have destroyed real, distinct information. Disambiguated the display names
  instead ("Hermes (Coding Harness)" / "Hermes (Skill Runner)"), exactly the fix
  `maintenance_check.py`'s own issue text already suggests ("de-duplicate OR suffix"). Checked
  `data/stars.json` (doesn't exist — no frozen records exist yet) and every record's own
  `starred`/`locked` flags (all `None`) first, per Golden rule #8. **Verified:** zero duplicate
  slugs left in either `skills.json` or `tools.json` (`Counter` check); re-ran
  `maintenance_check` — the "Title collisions" issue type is now completely ABSENT from the
  report (was 10, health score 40→48); rebuilt `brain_graph.json`/`brain.graphml` with fire
  14's fixed generators so the merges propagate cleanly — 0 duplicate node ids in both, same
  Counter check as fire 14. `python -m src.guardrails` → 15/15, 0 critical (G-C/G-G — backup-
  freshness/remote-sync — both self-heal inside `git_safe`'s own push sequence). Shipped via
  `git_safe ship` (commit `3cf78daf`). **Harsh self-criticism:** the 187 empty-body records
  (the OTHER number in item #11) are still untouched — that's real content backfill across 187
  distinct records, and writing 187 rushed one-line descriptions unattended in one fire's time
  budget would trade a honestly-flagged stub for a plausibly-wrong one, which is a worse
  outcome; it needs a dedicated enrichment pass (deep_retrieve, or a deterministic filler like
  fire 10's GitHub-metadata one), not another maintenance fire, and I said so explicitly in
  QUESTIONS.md rather than leaving a vague "later." Only investigated the 5 pairs
  `maintenance_check`'s own (5-capped) sample surfaced for its 10-count — trusted its Counter
  logic rather than independently re-deriving whether other collisions exist beyond what it
  reported, which is reasonable (fire 14 read that logic closely enough to trust it) but not
  independently re-verified from scratch. The merge script itself lived in `/tmp` scratch, not
  a new `src/` module — a deliberate scope call: this was 5 specific, individually-investigated
  pairs, not a general "auto-merge same-named records" tool, and building that generically
  would risk exactly the blind-merge mistake the Hermes case shows is unsafe for a problem this
  small. Fifth-plus fire in a row on the non-brain-front data/graph-quality chain (10→11→12→
  13→14→15) — the loop's own recurring self-criticism (fires 8, 12, 14) about M1-M5 brain/agent-
  orchestra work going untouched applies here too, doubly so now that it's two fires in the
  same run; a future fire with a real time budget and/or the brain-front unblocked should
  prioritize that.

- **~22:0x (fire 14, unattended, cloud session) — QUESTIONS.md item #11 (owner default: yes):
  ported build_brain.py's proven empty-body-skip + unique-id fix into the two OTHER
  brain-graph generators that still had it, `build_graph.py` (dashboard in-page graph) and
  `export_graphml.py` (Graphify/Gephi export).** Non-brain front, deterministic, no LLM.
  Read `build_brain.py` first — it already carries a "MAINTENANCE FIX" comment block from an
  earlier fire: items with no real body were plotted as blank "white" graph nodes, and items
  with no slug/name collided onto the SAME note title, silently overwriting each other.
  `build_graph.py` had the identical root cause via a different mechanism: its fallback id used
  the per-category loop `rank` (0, 1, 2…) when slug/name were missing, so "skill:0" in one
  category collided with "skill:0" in another. `export_graphml.py` was actually worse: when
  BOTH slug and name/skill_name were missing, `str(None)` produced the literal id `"skill:None"`
  — every such record across the whole library collapsed onto one shared node. Ported the same
  two guards (`has_body()`: skip if no description/use_case/tips for a skill, no description for
  a tool, no what_it_does/description for a connector; `ident()`: require a real non-empty
  slug/name, never fall back to an index or `None`) into both files, matching build_brain.py's
  already-proven definitions field-for-field. **Verified:** re-ran both generators —
  `build_graph.py` → 1872 nodes, 0 duplicate ids, 3 empty/unidentified items skipped (out of the
  curated top-55-per-category pool, so few were affected there); `export_graphml.py` → 8569
  nodes, 0 duplicate ids, 218 empty/unidentified records skipped (it walks the FULL library, not
  a curated top-N, so it had far more junk to catch) — confirmed via `grep` for any literal
  `"skill:None"`/`"tool:None"`/etc. id or `>None<` label (zero matches) and a Python `Counter`
  over every `<node id>` in `brain.graphml` (zero duplicates). `python -m src.guardrails` → 14/15,
  0 critical (only G-O info-level, unrelated). `python -m src.standing_checks` first: local
  `origin/main` cache was stale by one commit and this session's branch had no upstream tracking
  — both self-healed automatically (the `ensure_upstream()`/re-fetch fixes fires 6–8 built),
  nothing lost. Shipped via `git_safe ship` straight to `main` (commit `de3a16ab`), same
  convention as 30+ prior fires. **Harsh self-criticism:** this fixes the GRAPH-RENDERING half of
  item #11 (what the dashboard and Graphify actually display), but NOT `maintenance_check.py`'s
  187-empty/10-collision COUNT — that metric reads `skills.json`/`tools.json`/`connectors.json`
  directly, i.e. real records with genuinely empty descriptions or two distinct records sharing
  one title, which is a data-enrichment problem (the same stalled "0 stubs/day" blocker already
  tracked elsewhere in QUESTIONS.md), not something a graph-code fix can move. I did not
  re-run `maintenance_check` expecting the score to change, and it won't — flagging that
  explicitly so a future fire (or Eitan) doesn't mistake this commit for having closed #11's
  underlying data debt, only its visible rendering symptom. I also did not touch the 10 actual
  title-colliding records or the 187 actual empty-body records themselves — that's real content
  work (backfill a description, or merge/rename a duplicate), squarely in "advance a milestone"
  territory rather than a one-fire fix, and a reasonable next non-brain-front task if nothing
  higher-priority is queued. Fourth-plus fire in a row on the non-brain-front data/graph-quality
  chain (10→13→14) rather than the actual M1–M5 brain/agent-orchestra work — repeating the same
  self-criticism fires 8 and 12 already made; a future fire with a bigger time budget and/or the
  brain-front unblocked should prioritize that over a fifth piece of this same chain.

- **~21:2x (fire 13, unattended, cloud session) — the 2 real boilerplate offenders fire 12 found
  but deliberately left alone are now cleaned up, via a NEW second net in `cross_tab_check.py`
  that closes the gap fire 12's own self-criticism named.** Non-brain cleanup front, same
  module fire 11 already owns. Fire 12's `is_boilerplate_skill()` gate only fires at creation
  time on a NEW candidate; `cross_tab_check.run()`'s existing collision logic only catches a
  boilerplate skill that shares a slug/name with an EXISTING tool — neither one would ever touch
  "Client Onboarding" (whose description is scraped Zoho-CRM landing-page copy) or "Social media
  post generation" (same pattern), because no tool named either of those things exists to
  collide with. Added `sweep_orphan_boilerplate()`: reuses fire 12's exact
  `bulk_analyze.is_boilerplate_skill()` gate but scans EVERY skill (not just tool-colliding
  ones), reroutes a match into `tools.json` as a real tool record (never silently dropped — the
  CLAUDE.md line this whole chain traces back to: "record the tool ... and emit no skill"),
  deletes any orphaned `SKILL.md` package, and logs to the same `data/_removed_cross_tab.json`
  audit trail `run()` already uses (added a `reason` field so the two nets are distinguishable
  in the log). Wired into `main()` right after `run()`, so it runs automatically every
  `bulk_analyze.yml` cycle (`python -m src.cross_tab_check` is already a step there) — a real
  standing second line of defense, not a one-off script. Verified: `--dry-run` first, found
  exactly the same 2 records fire 12 had already identified read-only (no drift, no surprises);
  applied for real — `skills.json` 3119→3117, `tools.json` 2848→2850 (both records rerouted, not
  merged into anything pre-existing, since neither "Client Onboarding" nor "Social media post
  generation" had a same-named tool), 1 orphaned `SKILL.md` folder deleted
  (`other-skills/higgsfield-ai/social-media-post-generation` — quality_score 5 had earned it a
  package; the other record's quality_score was 1, below the package threshold, so it never had
  one to clean up), `index.json` pruned for both dropped slugs (the same staleness class fire 11
  fixed a crash for). `python3 -c "json.load(...)"` on all 4 touched data files; `python -m
  src.guardrails` → 14/15, 0 critical (same known-flappy G-M, unrelated). Zero frozen/starred
  records touched (checked `stars.json` + per-record flags before removal, same as `run()`).
  **Harsh self-criticism:** the new tool records are honest but low-quality — I named them
  after the SKILL's (often generic) name ("Client Onboarding", "Social media post generation")
  rather than the actual product the description is really about ("Zoho CRM"), because
  extracting the real product name out of scraped landing-page copy reliably would need another
  LLM call or a much fussier regex, and I chose not to build that unattended for 2 records. The
  result: `tools.json` now has 2 more entries that are technically correct (a real product with
  a real description) but oddly named and easy for a human skimming the Tools tab to find
  confusing ("Client Onboarding" reads like a technique, not a CRM product) — a small data-
  quality debt trade against not losing the record or over-scoping this fire. `quality_score: 1`
  on the Zoho-CRM one also just carries over from the original (mediocre-source) skill record
  unchanged; I did not re-score it as a tool, which is a fair reason it might be a weak one to
  even keep — a human pass on these 2 specific records would be cheap and is a reasonable ask
  for Eitan's return rather than mine to force through unattended. I did not go looking for MORE
  orphan-boilerplate cases beyond what fire 12's read-only sweep already found — `sweep_orphan_
  boilerplate()` will only prove its ongoing value the next time `bulk_analyze.yml` runs and
  either finds 0 (nothing new slipped through — good) or something (the second net earning its
  keep) — that's for a future PULSE.md/heartbeat check to notice, not this fire.

- **~21:1x (fire 12, unattended, cloud session) — anti-boilerplate gate moved to the point of
  creation: bare-product-name "skills" are now blocked BEFORE they're written, in the same
  free-lane extractors fire 11 suspected (`bulk_analyze.py`, and `mine_feeds.py`'s shared
  `merge()` which `gemini_video_analyze.py` also imports).** First: fire 10's GitHub-metadata
  enricher is CONFIRMED working with hard evidence — the real (un-proxied) GitHub Actions runner
  ran it in workflow run `30218575686` / job `89836888193` / commit `c16ed596` (2026-07-26T20:15Z)
  and logged `github-meta-enrich: batch of 22 (fresh pool 22) from 22 github-linked stubs; 22
  processed (9 descriptions upgraded); stubs now 2044` — closes fire 10's open item for real, not
  just via guardrails. Non-brain front: this fire's own increment. Investigated fire 11's own
  named follow-up ("root cause... a bigger, riskier change I did not have the review budget to
  make safely unattended") — read `src/mine_feeds.py`, `src/gemini_video_analyze.py`,
  `src/bulk_analyze.py`, and `src/analyze_batch.py` end to end. Found the actual mechanism:
  `bulk_analyze.py`'s `merge_skills()` and `mine_feeds.py`'s shared `merge()` (imported by
  `gemini_video_analyze.py` too — the exact "gemini-video" stub source fire 11 named) each carry
  their own anti-boilerplate denylist, but it's a ~7-word EXACT-match set (`{"claude","chatgpt",
  "gemini","openai","anthropic","make","mcp"}` / similar in mine_feeds) — it blocks a bare
  "Claude" but not "Claude Code", "Claude Projects", "Frontend Design", "AI Code Generation" —
  precisely the 5 slugs fire 11 found stuck in `cross_tab_check`'s tie queue. `src/analyze_batch.py`
  turned out to be a RED HERRING: confirmed via `.github/workflows/analyze.yml` that the real
  Claude-driven analyze stage runs `anthropics/claude-code-action` reading CLAUDE.md directly —
  `analyze_batch.py` is dead code, never invoked by any workflow (hardcoded `TODAY = datetime(2026,
  6, 3, ...)` and its own legacy `AI_TOOLS` knowledge base are giveaways); did not touch it, and
  said so plainly rather than silently fixing something inert. Fix: added `is_boilerplate_skill()`
  to `bulk_analyze.py` (imported by `mine_feeds.py`, which `gemini_video_analyze.py` already
  imports from) — fires ONLY when a skill candidate has ZERO captured technique evidence (no
  tips/slash_commands/general_tips, mirroring `cross_tab_check._has_concrete_technique` exactly)
  AND EITHER its description/use_case matches the literal forbidden template CLAUDE.md quotes
  ("is an AI tool ... enhances productivity" / "is an AI-powered X that streamlines/helps/...")
  OR the same name was also returned as a tool in the same batch. Reordered all three call sites
  (`bulk_analyze.main()`, `mine_feeds.main()`, `gemini_video_analyze.main()`) to merge tools
  BEFORE skills so the name-collision signal is live, not stale. **Verification, two layers, no
  live LLM key needed:** (1) 5 synthetic unit tests reproduce the exact fire-11 pattern (a video
  naming "Claude Code" as both skill+tool with empty tips) — tool kept, skill correctly blocked
  (0 added); a real technique WITH tips sharing a product name is never touched; a boilerplate
  description alone (no tool-name collision) is still caught; a genuine no-tips niche technique
  ("GitHub Repository Monitoring and Iteration" — real text sampled from today's actual
  `skills.json`) is correctly NOT flagged. (2) Ran the new `is_boilerplate_skill()` **read-only**
  against all 3,119 real skills in the live `skills.json` — flagged exactly 2, both genuine
  pre-existing junk records found in the process ("Client Onboarding" whose description is
  scraped Zoho-CRM landing-page copy; "Social media post generation" ditto for a generic
  generator tool) — 0 false positives against the other 3,117, including 2,406 skills with no
  tips at all (spot-checked 15 at random: things like "No-Code App Development", "Agent Swarm
  Execution", "Direct Preference Optimization (DPO)" — real techniques that just lack tips, not
  boilerplate; the gate correctly leaves every one of them alone). `python3 -c "ast.parse(...)"`
  on all 3 touched files; `python -m src.guardrails` → 14/15, 0 critical (only the known-flappy
  G-M "stalled" noise, unrelated). One stray artifact from my own test run cleaned up before
  shipping: `merge_skills()` calls `write_skill_md()`, so running it against a >=5-quality
  synthetic test record wrote a real (fake) `skills/github-repo-monitor/SKILL.md` to disk —
  caught by G-L before commit, deleted, re-ran guardrails clean. Left the 2 real offenders
  in `skills.json` untouched — this fire is the point-of-creation fix only, not a retroactive
  sweep; flagged as a good, small, low-risk next task in QUESTIONS.md. **Harsh self-criticism:**
  the "same name in both arrays this batch" signal only catches a collision within ONE response —
  it does nothing for a skill named in video A that collides with a tool named only in video B
  (that gap is still `cross_tab_check`'s job, running after the fact, same as before this fire;
  I did not change that division of labor, just made the point-of-creation half stronger). The
  boilerplate-description regex is necessarily a guess at CLAUDE.md's prose template and could
  miss a differently-worded stub a future LLM emits (a smarter model might phrase the same
  vendor-echo without ever using "AI tool" or "AI-powered" — this is pattern-matching, not
  semantic understanding, and will need retuning as stub phrasing drifts) — I biased hard toward
  ZERO false positives (proven against all 3,119 real records) over maximum recall, which is the
  right call for something unattended and irreversible-if-wrong, but it means some future stubs
  will still slip through to `cross_tab_check` rather than being caught here. I also did NOT
  build the retroactive sweep for the 2 confirmed real offenders sitting in `skills.json` right
  now — could have reused the exact same gate to fix them today; left them for a cheap next fire
  instead of stretching this one's scope, but that is a deliberate scope call, not an oversight,
  and it means the dashboard shows 2 known-bad records one fire longer than strictly necessary.

- **~20:0x (fire 11, unattended, cloud session) — cross-tab check now resolves boilerplate ties
  instead of flagging them forever, and one live crash-bug was found and closed along the way.**
  Non-brain cleanup front (`src/cross_tab_check.py`, the Step-5 skill/tool single-tab guarantee).
  It had 5 skill/tool slug collisions permanently stuck at "kept-both (tie — needs review)" —
  `claude-code`, `claude-projects`, `find-skills`, `frontend-design`, `ai-code-generation`. Read
  all 10 records (5 skill + 5 tool pairs): every one of the 5 "skills" was a bare-product-name
  stub with `tips: []`, no `slash_commands`, no `general_tips` — the exact anti-boilerplate
  pattern CLAUDE.md's Step 3 forbids ("Claude Code is an AI tool by Anthropic. It assists with
  software development...", verbatim from `skills/claude-code/SKILL.md`), while the paired TOOL
  record for the same name was always the richer, factual one. Added `_has_concrete_technique()`
  as the tie-break: a tie where the skill side has zero captured technique evidence now resolves
  to the tool, deletes the skill's now-orphaned `SKILL.md` package folder (mirrors Step 5's merge
  cleanup), and logs to `data/_removed_cross_tab.json` as before — a genuine tie (either side has
  real evidence) still just gets flagged, unchanged. Along the way found `data/index.json` (the
  compact skill dedup cache `analyze_batch.py`'s Step-3 "index-first dedup" trusts) is
  incrementally maintained and NEVER pruned when a skill is deleted elsewhere — a stale
  `index.json["claude-code"]` entry pointing at nothing would make the next video that mentions
  "Claude Code" hit `existing=None` in `analyze_batch.py`'s merge branch and crash on
  `existing['tips'] = ...` (NoneType). Fixed by having `cross_tab_check.py` prune the index entry
  whenever it drops a skill, and manually cleared the one stale entry my own run left before that
  fix landed. Verified end-to-end via CLI/data only: dry-run showed the correct verdict change
  first; applied run actually removed the 5 stubs from `skills.json` (3124→3119), left
  `tools.json` untouched (2848), deleted `skills/claude-code/` from disk, logged all 5 to
  `_removed_cross_tab.json`, pruned `index.json`; re-ran `cross_tab_check` → 0 collisions;
  `python3 -c "json.load(...)"` on every touched file confirmed valid JSON; `python -m
  src.guardrails` → 14/15 (only G-C, cleared by `python -m src.git_safe backup` this same fire →
  15/14 momentarily, G-M flaps STALLED/OK on beat timing noise unrelated to this change, 0
  critical either way). **Harsh self-criticism:** the fix is narrow by design (only fires on a
  genuine 0-evidence tie, so it can't touch any of the thousands of non-colliding or
  non-boilerplate skills), but that narrowness means it only resolved the 5 collisions that
  existed *today* — nothing stops five more identical `mine_feeds (gemini-video)` stubs from
  piling up tomorrow and sitting as new ties until the next cross-tab run catches them (it does
  run every bulk-analyze cycle per the module's own docstring, so the lag is bounded, not
  unbounded, but it's still lag). I did not go fix `mine_feeds`/`gemini_video_analyze.py` itself
  to stop emitting bare-product-name "skills" at the source — that's the actual root cause and a
  bigger, riskier change I did not have the review budget to make safely unattended this fire.
  The `existing=None` crash I fixed was one I created the precondition for (by deleting skills
  without pruning the index) rather than a pre-existing bug I went hunting for — worth being
  honest that "found and fixed a crash" here means "fixed a crash my own change would have
  caused," not an independent audit win.
- **~19:1x (heartbeat check, fires 1–10) — storage OK, no limits exceeded, all 10 fires landed.**
  Disk: 30 GB free on the repo drive (guardrail G-N), no cleanup needed. `origin/main` ==
  local HEAD, verified by `git_safe push()`'s own post-push check on both of this fire's
  commits (`196c9647` / `854a6cbc`) — nothing stranded. Guardrails 15/15, 0 critical after this
  fire's ship (was 12–14/15 transiently mid-fire on expected pre-commit/stale-backup flags,
  self-healed by `ship`, matching the pattern of every prior fire this week). Reviewed fires
  1–10: 1 staged an audit-decision batch, 2 created this log, 3 fixed memory-recall recency,
  4 added a decisions-CLI, 5 flagged the enrichment blocker + staged 4 more audit decisions, 6
  fixed the done-counter regression + ported a stranded `links`-routing fix, 7 landed that fix
  for real + diagnosed the recurring missing-upstream symptom, 8 built `ensure_upstream()`
  auto-heal, 9 built the `standing_checks` one-command entrypoint, 10 (this fire) built and
  wired the deterministic GitHub-metadata enricher — the actual blocker fire 5 named. No fire
  in this window hit an operational limit, a rate limit, or a push failure. Two open items carry
  forward unresolved, both already flagged and neither urgent: ~13 stray `kind-shannon-*`
  branches of unknown content on origin (still nobody's had a time budget to sweep them), and
  the branch-vs-main shipping convention (used again this fire, still unconfirmed by Eitan — see
  QUESTIONS.md). Per the outer routine's "every 10th heartbeat" instruction: reporting this
  summary to the repo now; no blocker serious enough to interrupt Eitan for.

- **~19:0x (fire 10, unattended, cloud session)** — Attacked the actual blocker fire 5/9 flagged
  instead of a sixth piece of plumbing: built `src/github_meta_enrich.py`, a fully deterministic
  (no LLM, no Ollama) enricher that fills github-linked stub descriptions straight from the
  GitHub REST API's own `description`/`topics` fields, falling back to `deep_retrieve`'s
  README-first-sentences extractor only when the API gives nothing. Wired it into
  `core_spoton.yml` to run HOURLY (vs. deep-retrieve's every-2h + local-drain's PC-dependent
  cadence), so stub-filling no longer depends on EITAN-PC being on. Verified: dry-run correctly
  found the 22 github-linked stub elements currently unfusable by deep-retrieve's LLM path; a
  mocked-metadata unit check (no real network, no file writes) proved `describe()` builds a
  factual sentence + topics from repo metadata and routes to the right per-type field via
  `DESC_FIELD`/`element_model.set_field`. Could NOT live-verify against the real GitHub API from
  this cloud session — its proxy scopes GitHub access to this one repo and returned 403 on
  `api.github.com/repos/Instagram/LibCST` (not a code bug: `deep_retrieve.py`'s own raw-network
  calls would hit the identical wall here) — the real un-proxied GitHub Actions runner is what
  actually exercises this end to end starting the next hourly `core_spoton` run; watch stub
  count in PULSE.md to confirm. `python -m src.guardrails`: 13/15, 0 critical (G-C stale-backup
  self-heals on ship; G-L flagged this new file pre-commit, resolves on this commit).
  **Harsh self-criticism:** I did not (and could not, from this sandbox) prove the happy path
  end-to-end before shipping — that's a real gap, mitigated only by the mocked unit check and by
  the fact the code path is structurally identical to `deep_retrieve.py`'s already-proven
  network calls; if it fails silently in CI it will show up as `github-meta-enrich` making 0
  progress in the next PULSE.md refresh and needs a follow-up fire to check the Action's own
  logs, not just guardrails. Also a repo-convention judgment call, now the THIRD cloud fire to
  make it (fires 8 and 9 both flagged this unconfirmed): pushed via `python -m src.git_safe
  ship`, which hardcodes `origin HEAD:main` per `away_mode.json`'s explicit instruction and the
  tool's own documented 2026-07-26 fix — not this session's default per-branch/PR harness
  convention. Continuing the established, self-documented pattern rather than re-litigating it
  a third time, but it is still genuinely unconfirmed by Eitan and stays flagged in QUESTIONS.md.
  Scope stayed narrow (one enricher, one workflow wire) — did not touch the ~13 stray
  `kind-shannon-*` branches, still someone else's problem.

- **~16:5x (fire 9, unattended, cloud session)** — Built the standing-checks entrypoint fire 8
  queued (twice now, per QUESTIONS.md) instead of re-diagnosing the same symptoms by hand a
  third time: new `src/standing_checks.py` — `python -m src.standing_checks` in one call (a)
  snapshots `origin/main` before/after a real fetch to answer "is a stale local ref hiding lost
  work?" deterministically instead of by eyeball, (b) calls `git_safe.ensure_upstream()` and
  reports whether it had to act, (c) runs `guardrails.run()` and folds the pass/critical count
  in. Writes `data/standing_checks.json` for the cockpit. Verified live on this fire's own run:
  cached `origin/main` (`1f9ed759`) WAS stale vs the real fetch (`5719279b`) — exactly the fire-8
  scenario — but HEAD matched the fresh ref, so nothing was actually at risk; upstream tracking
  was indeed missing on this session's branch (auto-fixed); guardrails 12/15, 0 critical (G-L
  flagged this new file itself pre-commit — resolves on this commit; G-M flagged no new task
  completions this fire, expected — this fire built tooling, not analyze/bulk_analyze work, so
  the done-counter genuinely didn't move; not a regression to chase). **Harsh self-criticism:**
  this is STILL meta/plumbing, the fifth fire in a row (v125–v128 hub polish/observability, fire
  8's git-hygiene fix, now this) rather than the actual program — Hub content, enrichment,
  departments, M1–M5 milestones are all untouched again. In fire 8's defense of its own
  direct-to-main call: I followed the same convention here (`git_safe ship` straight to `main`,
  no per-session branch/PR) for consistency with 30+ prior fires and zero prior PRs — still
  flagged, still unconfirmed by Eitan, still worth him overriding explicitly if he wants
  cloud-hosted fires to open PRs instead. Did not touch the still-unswept ~13 stray
  `kind-shannon-*` branches (unknown liability, someone else's problem again this fire) nor the
  real blocker QUESTIONS.md already names (enrichment stalled at 0 stubs/day, deterministic
  GitHub-metadata enricher still unbuilt) — next fire with a real time budget should attack that
  instead of finding a sixth piece of plumbing to polish.

- **~16:0x (fire 8, unattended, cloud session)** — This fire ran from the cloud GitHub-hosted
  scheduled session, not the local PC loop (repo path was this environment's own clone, not
  `D:\AI-YouTube-Skills`). Standing checks: local `origin/main` ref was stale (cached at
  2026-07-25T15:56, a full day behind); `git ls-remote origin main` + a real fetch showed the
  true remote HEAD was only 1 commit ahead of local (`cc95c509`), so nothing was actually at
  risk — but it cost time to rule out data loss, which is exactly the kind of check a dedicated
  standing-checks entrypoint should do in one command instead of by hand each fire (still
  unbuilt — queuing again). Landed fire 7's queued task: `src/git_safe.sync()` now calls a new
  `ensure_upstream()` first, which detects a branch with no `@{u}` tracking ref and sets it to
  `origin/main` automatically — closes the "SECOND session in two fires" recurring gap for good
  instead of a third manual one-off. Verified: unset upstream locally, called `ensure_upstream()`
  directly → returned `True` and re-tracked; `python -m src.guardrails` 14/15 (only G-C, stale
  local bundle in this fresh container, which `git_safe push`'s own backup step fixes). Commit
  `bce03ae6`. **Harsh self-criticism:** this is the FOURTH fire in a row that is meta/plumbing
  work about the loop's own git hygiene rather than the actual program (Hub content, enrichment,
  departments, M1-M5 milestones) — the standing-checks-as-one-command idea has now been queued
  twice without being built; next fire should build it instead of re-diagnosing by hand a third
  time. Also a judgment call worth flagging explicitly: this cloud session's harness defaults to
  developing on a fresh per-session branch and opening a PR, but that directly reproduces the
  "14 stray `claude/kind-shannon-*` branches" liability fire 7 already flagged as unresolved debt
  — so I pushed straight to `main` via `git_safe ship` instead, matching the repo's own
  established convention (30+ prior fires/beats, confirmed by git history, zero PRs) and the
  explicit "ship ONLY via `python -m src.git_safe ship`" instruction in the plan text itself.
  That is the right call given the pattern already in place, but it overrides a generic
  platform default and Eitan should confirm on return that direct-to-main is still what he
  wants from cloud-hosted fires, not just the local-PC ones. Confirmed real remote state was
  fine (not a phantom day of lost work) before touching anything, and did not attempt any of
  the 13 OTHER stray branches — still unswept, still an unknown liability, still someone else's
  problem for a fire with a bigger time budget.

- **~09:5x (fire 7, unattended)** — Standing checks: `git fetch --prune` found 14 stray
  `claude/kind-shannon-*` session branches on origin, one of them (`ae4swi`) still carrying real,
  never-landed work flagged in QUESTIONS.md — commit `1205385a` "wire the links department into
  the agent registry". Its branch shares no merge-base with `main` (history has been rebased/
  rewritten since), so a git merge/cherry-pick wasn't viable; ported the fix by hand instead:
  registered a `links` department (capability `resolve-links`, keywords matching
  `excava_agents.py`'s `TOOL_DOMAIN` links-lane entry) plus two tier-1 agents (Anchor: doer,
  Tether: checker) scoped to `src.resolve_links` in `data/excava/agents.json`. Verified:
  `pick_department()` now routes a link-coverage task to `links` (4 keyword hits, scoped worker
  found — previously "no scoped worker (G-7)"); `guardrail_test` still 10/10; `guardrails` 14/15
  (only G-C, history-bundle freshness, which `git_safe push` itself fixes by taking a bundle
  before pushing). Also fixed this session's own branch: it had no upstream tracking configured,
  which would have made `git_safe`'s `pull --rebase` fail — set
  `--set-upstream-to=origin/main` (same one-time fix fire 6 needed on its branch; this is now the
  SECOND session in two fires to hit this, so it is a real recurring setup gap, not a fluke —
  flagged in QUESTIONS.md). **Harsh self-criticism:** this closes exactly the "land it or discard
  it" ask QUESTIONS.md raised for `1205385a`, but I did not sweep the other 13 stray branches this
  fire (no time budget for 13 unknown diffs against a rebased history) — they're still an unknown
  liability and the underlying cause (every scheduled session gets a fresh throwaway branch name,
  and `git_safe push()` only saves work if that session remembers to run it) is unfixed. A cleaner
  fix would be a standing-checks step that force-sets upstream tracking automatically at session
  start, rather than relying on each fire noticing the symptom after the fact — queuing that as
  the concrete next-fire task.

- **~03:10 (fire 6, unattended)** — Standing checks found `sync` broken (this session's local branch had no
  upstream — a one-time `--set-upstream-to=origin/main` fixed it, no data lost, HEAD==origin/main after).
  Diagnosed the guardrails 15/15→13/15 drop from PULSE.md/pulse.json: the real 2 failures were G-C (CI's beat
  bypasses `git_safe`, so `_ATTIC/backups` is permanently empty on its ephemeral runner — now recognizes
  `GITHUB_ACTIONS=true` and reports info/pass there) and G-I (SESSION_HANDOFF.md hadn't mentioned build v129
  since v128 shipped — added the missing §0d entry). Also ported an already-correct, tested fix for the
  done-counter decline (G-M was recounting live `bus.json`, which `prune()` empties after 7 days; switched to
  the monotonic `state.json['usage'][dept]['done']` tally — now 4520, correctly only-rises) from an orphaned,
  never-merged branch (`origin/claude/kind-shannon-ae4swi`) I found while investigating — flagged that
  orphan-branch problem in QUESTIONS.md since it means at least one prior fire's real work never reached
  `main`. Verified via CLI: `python -m src.guardrails` now reports 15/15, 0 critical; re-ran `python -m
  src.pulse` to refresh PULSE.md/pulse.json. **Harsh self-criticism:** this is diagnostic/plumbing work, not
  a user-visible product win — three fires in a row now (v125-127 hub polish, v128 exposing the regression,
  this one fixing it) have been meta-work about the observability system itself rather than the actual
  program (Hub content, enrichment, departments). The G-C "fix" is also a judgment call I made unilaterally
  (loosening what counts as "passing" in CI) rather than deferring — defensible since it's deterministic and
  reversible, but Eitan didn't ask for guardrail semantics to change and should sanity-check it on return. And
  I still haven't touched the `links`-department routing fix sitting on that same orphaned branch — left for
  next time. Also had to fix `src/git_safe.py` itself mid-fire: `push()` used a bare `git push`, which fails
  whenever the branch name doesn't literally match "main" (this sandbox's branch tracks origin/main under a
  different name) — one more sign the contract's tooling was written for a specific local machine, not this
  environment. Commit `3d1d889a` (git_safe fix itself: `ebb224ca`).

## 2026-07-24
- **~18:00 (fire 5, unattended)** — Shipped `src/pulse.py` → **PULSE.md** + `pulse.json`: one-glance "is it actually working?" status that federates guardrails, movement, drain, open questions, the away-log and recent commits into a single file at the repo root (open it, no server). It refuses to cheerlead — the first run surfaced a HIDDEN regression the green dashboard hid: the done-counter has fallen 1566→1256 over three days while "depts moving" sat flat at 12. Commit `24f0a3bb5`.

## 2026-07-23
- **~16:59 (fire 4, 2nd unattended)** — Added `python -m src.audit_decisions next [--stage]`: prints the next open §7 decision batch with proposed verdicts, and `--stage` appends it to QUESTIONS.md — so staging the 118 open decisions is one deterministic command instead of hand-writing each batch. Verified via CLI: prints items 5–8.
- **~16:44 (fire 3, first true unattended fire — always-allow confirmed)** — Improved `memory_brain.recall`: it ranked only by keyword overlap, so ties fell back to store-iteration order and stale context could outrank fresh. Now the tiebreaker is RECENCY (newest `at` first), so agents reading the one-brain get the freshest relevant memory. Verified via CLI: equal-score hits now order Jul 23 → Jul 22 → Jul 11.
- **~15:59 (fire 2)** — Created this AWAY_LOG so you have a one-glance record of the loop's work without scrolling every commit. Also verified honestly: deterministic keyless enrichment is currently DRY (fresh-fusable pool = 0 — the drain/beat already reached everything with recoverable sources; the remaining ~2007 stubs need discovery or transcripts, not another fetch loop), and the One-Brain memory census is current (~9,016 records across 4 stores).
- **~15:44 (fire 1)** — Staged the next overhaul-audit decision batch (items 5–8: buy-Gemini-Pro / in-app-write / offline-keys / naming) into `QUESTIONS.md` with proposed verdicts for you to confirm on return. Per §7 the decisions are yours — the file was left OPEN, not auto-applied. Commit `e00b3f183`.
