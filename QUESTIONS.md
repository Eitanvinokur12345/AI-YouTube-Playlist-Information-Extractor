# Open questions for Eitan (non-blocking — answer whenever; work continues meanwhile)

_Per your rule: questions live here + in memory so they never block work or waste tokens. Answer any subset, in any order, whenever you want. Each has my default so you can also just say "defaults"._

---

## ⏸ AWAY WEEK — batched while you're out (since 2026-07-21)
You're away ~1 week; the offline loop is running (non-brain fronts, hourly) and collecting questions HERE instead of asking. Every question I hit this period is appended below with the default I proceeded on. I'll present this whole list the moment you're back. Contract: `data/excava/away_mode.json`.

### Away-week questions

**2026-07-29 (fire 61) — possible name collision on the `openclaw` tools.json record.**
Several existing endorsing videos describe OpenClaw as a B2B lead-gen agent (satellite-imagery
property scraping, direct-mail automation) — that's the description currently on file. A newly
hand-drained video (`46fI3TSx3hE`, "Install OpenClaw on a VPS with one command") describes a
self-hosted AI-agent gateway with a one-line VPS installer and Discord bot integration, which
matches the OSS `openclaw` project this repo's own EXCAVA architecture docs already reference as
a channels/shell tool (§2 of `EXCAVA_END_PLAN.md`). These read like two different products
sharing a name, not one product two ways. _Default: left the existing description untouched,
added a `data_quality_note` on the record instead of overwriting — insufficient evidence from a
43s/131-char source to safely rewrite a record with 8 mentions._ Proposed resolution once you're
back: split into `openclaw` (real OSS agent gateway) and `openclaw-leadgen` (the B2B sales tool),
re-sorting each endorsing video's id to the record it actually matches.

**2026-07-28 (fire 52) — new guardrail G-T found a real, previously-unknown commit-loss gap:
the `data_guard.json`-only auto-resolve fallback (fires 25/28-41) doesn't cover other shared
mechanical files, and `bulk_analyze.yml`'s 17:56-18:00 UTC run today lost its entire commit to
exactly that gap (full evidence chain in AWAY_LOG.md's fire-52 entry).** → **Proposed default:**
widen the known-stateless auto-resolve list in all 19 workflow files from just `data_guard.json`
to also include `data/health.json`, `data/effectiveness.json`, `data/hub.json`,
`data/self_check.json`, `data/safety.json`, `data/guardrails_status.json` — all fully
regenerated from scratch every run, safe to take "ours" on conflict. Explicitly proposing to
**NOT** touch `data/excava/*` the same way — those accumulate real memory/conversation content
across lanes, and "ours" there would silently discard another lane's genuine work, the exact
failure this fix exists to prevent. Did not implement this myself this fire (touches the same
19 files as the original rollout and deserves the same bare-repo-repro verification those fires
used before landing) — parking here for confirmation or for a future fire with the budget to do
the repro properly.

**2026-07-28 (fire 47) — the "away ~1 week" mark from `away_mode.json` (`since: 2026-07-21`) is
reached today, and the exit condition ("Eitan posts any message indicating he's back") hasn't
fired.** Flagging rather than assuming: away mode has no built-in expiry, only an explicit
back-signal, so the loop is continuing on the same non-brain-fronts/hourly cadence unless told
otherwise. _Default: keep running away mode until you actually say you're back — a calendar
week alone isn't a stop signal, don't want a fire to silently go quiet on real work assuming
you'll show up on schedule._

**Overhaul audit — next decision batch (§7; items 5–8 of 122).** These are YOURS to decide; I did NOT auto-apply them — `data/excava/overhaul_decisions.json` stays OPEN. My proposed verdict on each (confirm or change with `python -m src.audit_decisions set <id> <verdict>`):
- **#5 "Should I just buy Gemini Pro?"** → proposed **REMOVE the worry.** The free path (VPS + Ollama + the free model pool) is real and proven this week — 11/11 engines answered, four brain families live. Paying is unnecessary.
- **#6 Direct in-app write to EXCAVA (no GitHub step)** → proposed **REBUILD.** Async-via-GitHub works now; true real-time in-app write needs the VPS (ties to A1, which you already KEEP'd).
- **#7 API keys work offline / without your PC** → proposed **KEEP the answer (yes).** Proven this week: the cloud beat ran the keys 24/7 with your machine off; the VPS will too.
- **#8 EXCAVATORTRON = HUB, EXCAVA = agents (naming)** → proposed **KEEP + lock everywhere.** This is the canonical naming and it's used consistently across the code and docs.

**2026-07-27 (fire 26) — should `core_spoton.yml` gain `actions: read` so a guardrail can see real job-level failures, not just commit gaps?** Fire 25 fixed the octal-arithmetic bug that (before that fire) let a failed step silently discard a whole run's real work when the Commit step defaulted to skipped, and flagged that nothing watches for that class of failure. This fire added guardrail G-Q (git-log-only: flags `core_spoton.yml` stale if no "core-spoton:" commit lands within 4h) — real value for a total stall (cron off, a crash before any step runs), but it CANNOT see a partial failure that still ends in a normal-looking commit, which is what fire 25 actually hit. A precise version needs the GitHub Actions REST API (list runs + jobs for `core_spoton.yml`, check step-level conclusions) cross-referenced against git history — that needs `permissions: actions: read` added to `core_spoton.yml` (currently `contents: write` only). → **Proposed default: yes, add it** — `actions: read` is a narrow, read-only grant (no ability to trigger/cancel/modify runs) scoped to this one workflow's own token, and GitHub's own docs describe it as safe to add alongside `contents: write`. Did NOT add it myself this fire (a permissions-block change to a scheduled, unattended workflow is exactly the kind of thing to flag rather than silently do, per the away-mode ask-questions-never-block rule) — parking here for your call; the git-log-only G-Q stands either way.

**2026-07-27 (fire 28) — the same "job succeeds, real work silently lost" bug fire 25 found in `core_spoton.yml` also exists in `mine.yml` (fixed) and the identical fragile pattern is shared by 19 workflow files (not fixed).** Live GH Actions logs confirmed `mine.yml`'s 2026-07-26 run reported "success" on every step while a full day's real mining (+5 skills, +31 tools, +3 connectors) was silently discarded: `git pull --rebase --autostash origin main` conflicted on the fully-regenerated `data/data_guard.json`, left HEAD detached, and `git push || echo "push skipped"` swallowed the failure. Fixed `mine.yml` only (verified against a real bare git remote — see AWAY_LOG fire 28 entry for the full repro/fix detail) since that's the one place I have PROVEN live evidence. `grep -rl "git pull --rebase --autostash" .github/workflows/*.yml` shows the exact same fragile pattern in 19 of ~22 workflow files total (`analyze.yml`, `bulk_analyze.yml`, `connectors_verify.yml`, `core_spoton.yml`, `creators.yml`, `discover.yml`, `excava_beat.yml`, `excava_inbox.yml`, `fetch.yml`, `gemini_video.yml`, `improve.yml`, `links.yml`, `mine_social.yml`, `news.yml`, `review.yml`, `sources.yml`, `transcribe.yml`, `visual.yml`, plus `mine.yml` now fixed) — any of them could hit the identical silent-loss bug the next time two lanes happen to commit within the same few minutes. → **Proposed default: yes, roll the same fix out to the rest, one or a few files per fire, prioritizing the highest-cadence/highest-value lanes first** (the busier a lane, the more likely a same-window collision) — did NOT do all 18 in this fire on purpose (small-scoped-increment rule); parking here so it doesn't only live buried in AWAY_LOG. A generic guardrail that detects "job succeeded but no matching commit landed" across ALL lanes (extending `pipeline_status.json`'s staleness view or cross-referencing the GH Actions API) would catch this bug class the moment it recurs, instead of waiting ~2 days for a staleness threshold to trip — flagged as a second, independent follow-up candidate.

**UPDATE (fire 29):** rolled the fix out to the 3 highest-cadence remaining lanes —
`excava_beat.yml` (every ~10 min), `core_spoton.yml` and `links.yml` (both hourly) — re-verified
against the same throwaway-bare-remote repro fire 28 used. **4 of 19 files now fixed** (`mine.yml` +
these 3); **15 still exposed**: `analyze.yml`, `bulk_analyze.yml`, `discover.yml`,
`connectors_verify.yml`, `news.yml`, `creators.yml`, `fetch.yml`, `gemini_video.yml`, `improve.yml`,
`review.yml`, `sources.yml`, `transcribe.yml`, `visual.yml`, `mine_social.yml`, `excava_inbox.yml`.
Next-highest cadence among those: `bulk_analyze.yml` (every 2h) and `analyze.yml` (every 3h, plus a
30-min catch-up cron that's normally a no-op) — good candidates for the next fire that picks this up.
The generic cross-lane "success but nothing landed" guardrail is still unbuilt, still the deeper fix.

**UPDATE (fire 30):** rolled the fix out to the next 3 highest-cadence remaining lanes —
`bulk_analyze.yml` (every 2h), `analyze.yml` (every 3h), and `connectors_verify.yml` (every 6h) —
re-verified with a fresh, cleaner throwaway-bare-remote repro (explicit `main` branch on both
sides, a genuine `data/data_guard.json` conflict between two clones): rebase fails → aborts →
merge retry also conflicts → auto-resolve-ours on `data_guard.json` only → merge commits → push
succeeds → HEAD stays on a real branch (never detached) → the other clone's real content
(`A-content`) survives all the way to a fresh clone of the remote. **7 of 19 files now fixed**
(`mine.yml`, `excava_beat.yml`, `core_spoton.yml`, `links.yml`, `bulk_analyze.yml`, `analyze.yml`,
`connectors_verify.yml`); **12 still exposed**: `discover.yml`, `news.yml`, `creators.yml`,
`fetch.yml`, `gemini_video.yml`, `improve.yml`, `review.yml`, `sources.yml`, `transcribe.yml`,
`visual.yml`, `mine_social.yml`, `excava_inbox.yml`. All remaining ones are daily-or-less cadence
(the sub-6h lanes are now all covered), so the marginal risk per remaining file is lower — still
worth finishing for completeness, no longer the highest-leverage next fire task. The generic
cross-lane "success but nothing landed" guardrail is still unbuilt, still the deeper fix.

**UPDATE (fire 35):** rolled the fix out to the 3 highest-remaining-cadence lanes — `news.yml`
(every 6h), `gemini_video.yml` (2×/day), `visual.yml` (2×/day) — re-verified with a fresh
throwaway-bare-remote repro. **10 of 19 files now fixed** (adds `news.yml`, `gemini_video.yml`,
`visual.yml` to the fire-30 list); **9 still exposed**, all daily-or-less: `creators.yml`,
`discover.yml`, `excava_inbox.yml`, `fetch.yml`, `improve.yml`, `mine_social.yml`, `review.yml`,
`sources.yml`, `transcribe.yml`. Fire 35 flagged that the remaining files are a textually
identical mechanical edit and asked whether a future fire should just do all 9 in one pass
instead of another 3-file increment — no strong reason not to, just following the smaller-scope
precedent fires 28-30 set. The generic cross-lane guardrail is still unbuilt.

**2026-07-26 (fire 10) — deterministic GitHub-metadata enricher BUILT, per the proposed default below.**
`src/github_meta_enrich.py` now fills github-linked stub descriptions from the GitHub REST API's
own `description`/`topics` (no LLM, no Ollama, no local-drain dependency) and is wired hourly into
`core_spoton.yml`. Could not live-verify against the real API from this cloud session (its proxy
scopes GitHub access to just this repo — 403 on other repos) — logic verified via dry-run +
mocked-metadata unit check instead; real end-to-end proof needs the next `core_spoton` Action run
and a PULSE.md stub-count check (see AWAY_LOG fire 10). This does NOT replace the LLM-fused path
for non-GitHub stubs (video-only elements, sites without API metadata) — deep-retrieve + the local
drain are still the only path for those. Original blocker note preserved below for context.

**The real hub blocker: enrichment is stalled at 0, and away-mode can't fix it (decision for your return).**
Three loop fires this week shipped read-side hub wins (v125 type-aware Activate · v126 "ready to use" filter
· v127 inline payload in the detail view). All real, but all BROWSE-layer — because the actual problem is
CONTENT: 3,628 of 10,133 elements are bare stubs and the local drain has enriched **0** for days (guardrail
G-O). deep_retrieve rides the brains/Ollama subsystem, which away-mode tells me not to touch, so I keep
polishing how you browse the library instead of filling it. → **Proposed default (on your return):** stand up
a DETERMINISTIC enricher (no LLM) that fills stubs from real sources — GitHub API repo description / topics /
homepage / README first line for the ~1,600 repo elements — network-bounded with a hard timeout (the 793-min
hang lesson). Free, non-brain, attacks completeness directly. Until you approve a network front or lift the
brain freeze, these fires keep producing browse-layer polish of diminishing value.

**2026-07-26 (fire 6) — orphaned branch found: away-fire work landed on a branch that never reached `main`.**
While diagnosing why guardrails dropped 15/15→13/15 (real cause: fixed in this fire — see AWAY_LOG/
SESSION_HANDOFF §0d v129), I found `origin/claude/kind-shannon-ae4swi`, a branch that diverged from `main`
after beat #17 (2026-07-26T01:58Z) and already contains a correct, tested fix for the exact same done-counter
metric bug (G-M) plus an unrelated `links`-department routing fix — fully written, verified, committed with
a proper message — but never merged/shipped to `main`. It sat idle 11+ beats while `main` kept the bug. This
means at least one earlier away-fire (or a parallel session) did real, good work that got silently stranded
because it ran on its own branch instead of `main` and nothing forced a merge. I ported the G-M fix myself
into `main` this fire (small enough to redo by hand safely), but the `links`-routing fix on that branch is
still stranded and unreviewed. → **Proposed default:** (a) every away-fire session should verify, before
shipping, that its working branch either IS `main` or gets merged into `main` before the session ends — a
fix stuck on an abandoned branch is equivalent to no fix; (b) someone (next fire, or you) should look at
`origin/claude/kind-shannon-ae4swi`'s `1205385a` commit ("wire the links department into the agent
registry") and land it or discard it explicitly, rather than leaving it to rot. _No further branches checked
this fire — there are ~9 other `kind-shannon-*` branches on origin whose contents are unknown; worth a sweep._

**2026-07-26 (fire 7) — `1205385a` landed; the branch problem is confirmed recurring, not a fluke.**
Ported the stranded `links`-department fix by hand (no merge-base with `main` after the history rewrite, so
a real merge/cherry-pick wasn't possible) — see AWAY_LOG fire 7. This session's own branch ALSO had no
upstream tracking configured (same symptom fire 6 hit and one-time-fixed on its own branch) — the second
occurrence in two fires confirms proposal (a) above isn't optional, it's necessary: every fresh session
branch starts detached from `origin/main` and silently loses work if the session doesn't notice and doesn't
run `git_safe push`. → **New proposed default:** add a standing-checks step (start of every fire, before any
other work) that unconditionally runs `git branch --set-upstream-to=origin/main` on the current branch — 
cheap, idempotent, and removes the whole failure class instead of relying on each fire to notice the symptom.
There are still ~13 other `kind-shannon-*` branches on origin of unknown content (grew from ~9); a full sweep
(diff each against `main`, land or explicitly discard) remains unstarted and should be the next fire's focus
if nothing higher-priority is queued.

**2026-07-26 (fires 12→13) — anti-boilerplate gate moved to point-of-creation; the 2 real
offenders found are now cleaned up too — DONE, both halves landed this run.** Fire 12 root-caused
fire 11's open item: `src/bulk_analyze.py` and `src/mine_feeds.py` (shared by
`gemini_video_analyze.py`) now block a bare-product-name "skill" (CLAUDE.md's own forbidden
template, e.g. "X is an AI tool by Y. It enhances productivity...") BEFORE it's written. Fire 13
(same run, right after) added `src/cross_tab_check.sweep_orphan_boilerplate()` — a permanent
second net wired into `main()` (so it runs every `bulk_analyze.yml` cycle) that reuses the same
gate retroactively and catches a boilerplate skill even with NO matching tool name to collide
with. Applied for real: `skills.json` 3119→3117, `tools.json` 2848→2850 (both records rerouted
as tools, not dropped). See AWAY_LOG fires 12 & 13 for full verification. **One loose end fire 13
flagged, worth a human glance whenever convenient (not urgent):** the 2 rerouted tool records
are named after the original SKILL's (generic) name — "Client Onboarding" and "Social media post
generation" — rather than the actual product the description is about ("Zoho CRM" in the first
case), because extracting the real product name from scraped landing-page copy wasn't worth an
extra LLM call for 2 records. Both are factually correct, just oddly titled; fine to rename
by hand or leave as-is. _Default: leave as-is; low priority._

**2026-07-26 (fire 11) — commit-signature / "Unverified" badge on GitHub, declined to rewrite history.**
This session's local hook flagged fire 11's two commits (`e849f557`, `83d2685f`) as showing "Unverified"
on GitHub (no GPG/SSH signature — the committer email was already `noreply@anthropic.com`, so email wasn't
the actual gap) and suggested `commit --amend --reset-author` + a rebase against `origin/...` to fix it. I did
**not** do this: (a) amending author metadata doesn't add a cryptographic signature, so the suggested fix
wouldn't actually produce a "Verified" badge — there's no signing key configured anywhere in this repo's
tooling; (b) the fix as given implies a rebase + force-push on a branch the `skills-tracker-bot` CI identity
is *also* actively committing/pushing to every 20–90 min (see `18c3ac3f` interleaved right between fire 11's
two commits) — rewriting history there risks a race against a concurrent CI push, and force-push isn't
something to do unattended without your sign-off regardless. **Default: leave commits as-is** (they're
correctly on `origin/main` — `git_safe.push()` already verifies `origin == HEAD` after every ship — just
cosmetically "Unverified"); if you want real "Verified" badges going forward, that needs either a GPG/SSH
signing key added to this environment's git config, or switching these commits to go through the GitHub API
(which auto-signs as "GitHub verified") instead of local `git push`. Neither is a fire-sized decision to make
unilaterally.

**2026-07-27 (fire 34) — same "Unverified" badge issue as fire 11 recurred; same decision stands, no new action taken.**
This fire's stop hook flagged commit `b75ae37d` (the designs.json conflict-marker fix) as
"Unverified" for the identical reason fire 11 already investigated and decided: the SSH
signature is present but unverifiable locally (empty `commit_signing_key.pub`), and by the time
the hook fired, `origin/main` had already moved 2 commits past mine (`excava-beat #7` + a merge)
via the independent CI beat — so the suggested amend+force-push would rewrite shared history a
concurrent process is actively building on, not just a cosmetic fix. Declined again, same
reasoning as fire 11's entry above; not re-litigating it a second time unless you want to add a
real signing key to this environment (the actual fix, still unbuilt, still your call).

**2026-07-27 (fire 19) — the branch sweep finally ran; two real gaps found and landed, ~20 branches now safe to delete.**
Checked every `claude/kind-shannon-*` branch for content `main` lacks (file-diff, not full history reread — see
AWAY_LOG fire 19 for the method and its one acknowledged blind spot). Found zero stranded source code, and landed
the two real gaps that did exist: a `G-P` guardrail from `kind-shannon-hcwmum` (fire 18) and two already-analyzed
videos' worth of skills/tools/news from `kind-shannon-yj1a6g`. Everything else on every other branch is either
already independently on `main` or was deliberately removed by later cleanup fires (12/13/15) — confirmed via
`deleted_skills.json`/`merge_log.json`, not assumed. → **Decision for you:** all ~20 stray branches are now
confirmed safe to delete (`git push origin --delete <branch>` for each) — I did not delete them myself since
branch deletion is harder to reverse than anything else this fire touched and no prior fire has done it
unilaterally either. _Default: delete them next time you're at a terminal; low priority, no urgency._

**2026-07-27 (fire 23) — the "news" department's charter was self-inconsistent since it was
authored; found and partly fixed, one real wiring decision left for you.** `data/excava/intent.json`'s
"news" charter has always said `should_do: "refresh the AI-news digest..."` but `right_tool` was
always `src.trend_watch` — a self-improvement trend-proposal tool (see its own docstring) with
nothing to do with news content. `data/excava/agents.json`'s own "news" dept purpose ("refresh
official-site AI news") independently confirms headline-refresh was the true original intent.
Because `right_tool` happened to already match the actual code wiring in `src/excava_agents.py`'s
`REAL_TOOL`, the supervisor's own intent-drift detector (the one that already caught mining/visual/
memory drift) saw no mismatch and stayed silent on this one for 3+ weeks. Restored `right_tool` to
`src.news` (the tool that actually matches should_do) so the drift is now visibly flagged every run
— `python -m src.excava_systemcheck`'s "intent aligned" line will read **10/11 systems working,
1 tool-drift** from now on (was 11/11) — that is a DELIBERATE, expected reveal of a pre-existing
problem, not a new regression from this fire; please don't "fix" it by reverting `right_tool` back
to `trend_watch` without reading this note. **What I did NOT do, and why — this is your call:**
rewire `src/excava_agents.py`'s `REAL_TOOL["news"]` to actually run `src.news` when the department
executes. Two real risks stopped me: (1) `src/news.py` already runs independently every 6h via
`.github/workflows/news.yml` and writes `data/daily_web_news.json`/`data/web_news_store.json` —
files CLAUDE.md governs as the separate YouTube-playlist-analyzer pipeline's own territory; routing
EXCAVA's department/bus path through the same tool risks a commit race against that dedicated
schedule. (2) it fetches ~95 RSS sources at up to 15s each, sequentially — easily past
`_run_real_tool`'s hardcoded 90s subprocess timeout, which would turn today's honest no-op into a
noisy "failed (timed out)" instead. → **Proposed default:** leave `REAL_TOOL["news"]` on
`trend_watch` as-is (it's safe, already proven, and its own honest "queued 0" output no longer
mis-reports as theatre — see the supervisor fix below) and treat the now-visible intent-drift as
documentation of a historical mistake rather than something to chase — UNLESS you want the "news"
EXCAVA department to genuinely do headline-refresh work, in which case it needs either a raised
per-dept timeout override or an async/deferred dispatch, built with your sign-off since it touches
the other pipeline's schedule. **Second, independent fix in the same commit — the actual functional
bug:** `src/excava_supervisor.py`'s `judge()` was misclassifying trend_watch's own correct, honest
"N proposals (top score X); queued 0" report as `noop` (theatre) on every single run, because
`trend_watch` DEDUPES queued proposals by key (`src/trend_watch.py`) — the 5 trend proposals it
queued back on 2026-06-29 are still open in `data/improvement_tasks.json`, so "queued 0" has been
the CORRECT report on every run since (nothing new to add, not nothing done). This was a real, live
false-positive in the project's own central "is work real" honesty tool: 6 of the last 40 tracked
completions were misjudged as theatre. Fixed with a targeted carve-out (mirrors the existing
`security`-dept "0 leaks = good" carve-out) keyed to trend_watch's own output signature. Verified:
`real_pct` on the live `data/excava/supervisor.json` jumped 82%→100% the moment the fix landed,
with 0 unit-test regressions across 8 cases (genuine no-ops/blocked/planned/security-zero all still
classify correctly). _Default: keep as documented above; only the news-dept wiring question needs
your actual decision._

---

## A. The new look ("Heavy Machinery" v58)
1. **Direction check:** hazard-yellow + warm ink, chunky borders, hard offset shadows, Archivo Black display type — is this the right direction, or push further (more color pops per tab?) / pull back? _Default: keep, then add per-tab accent colors next pass._
2. Dark mode variant of the same theme — wanted? _Default: later._
3. Should the Designs tab get an even more expressive skin than the rest (it's the taste tab)? _Default: yes, next visual pass._

## B. North Star — proposed goal additions (needs your sign-off; goals are law)
The 6 goals miss two things we now actually build for:
4. **G7 Security & trust** — "nothing untrusted ever runs un-sandboxed; your data/keys can never leak." (We built security_preflight + the Activator gate; nothing *scores* it.) Approve adding G7? _Default: add._
5. **G8 Personal fit** — "every recommendation/design/plan is tailored to Eitan's taste and workflow (Arena taste, NOSG, his stack)." Approve adding G8? _Default: add._

## C. EXCAVA — the big one (deferred build; these shape the spec)
6. **Creators department:** should created things (new skills/tools/formats) be auto-published into the hub after passing the gate, or always wait for your approval per creation? _Default: approval per creation until trust is earned._
7. What may EXCAVA do **fully autonomously** at night: only internal work (resolve/verify/organize)? Or also create drafts? Or also publish? _Default: internal + drafts._
8. Where does EXCAVA live long-term: GitHub Actions only (free, current), or also a small always-on runner (e.g. your PC when on / a free VPS) for continuous operation? _Default: Actions now, revisit after the program._
9. The OS "manages the entire project **and can do a lot of other things**" — name 2–3 concrete non-project things you want it to do first (e.g. manage Budoaris tasks? your learning? content posting?). _No default — needs you._

## D. Program gaps I found (will do unless you object)
10. ~~`formats.json` is collected but has no tab — fold formats INTO the Designs tab as a "Formats" filter?~~ — RESOLVED 2026-07-27 (away fire 22, live build v130). The Designs tab now shows a content-type subnav (All / Websites·apps / 📐 Formats) that merges `data/formats.json`'s 95 layout/diagram patterns into the same gallery, rendered as their own card style (kind + description + rebuild_hint, no screenshot since formats don't have one; excluded from the ⚔ Arena pool for the same reason). See SESSION_HANDOFF.md v130 for verification detail. _Default (yes) taken as given._
11. ~~Brain graph still has ~191 empty "white" nodes + 10 title collisions — clean next maintenance pass?~~ — RESOLVED 2026-07-26 (fires 14+15). Fire 14: the RENDERING half — `build_graph.py` and `export_graphml.py` now skip empty-body/unidentified records instead of plotting them as blank or colliding nodes (ported from `build_brain.py`'s already-working fix). Fire 15: the DATA half — investigated all 5 name-collision pairs behind `maintenance_check.py`'s 10-count by hand; 4 were genuine same-product duplicates (merged per Step 3/3b's compare-and-keep-best, backed up to `deleted_skills.json`/`merge_log.json`), 1 ("Hermes") was two genuinely different products sharing a brand name (disambiguated the display names instead of merging). `maintenance_check.py`'s "Title collisions" issue is now fully GONE (10 → 0). **Still open, NOT resolved:** the 187 empty-body records — that's real content backfill, out of scope for a maintenance pass, tracked with the stalled-enrichment blocker elsewhere in this file. _Default: title-collision cleanup done; empty-body backfill needs a dedicated enrichment pass (deep_retrieve or a deterministic filler), not another maintenance fire._
12. ~~Transcript lane blocked on `YT_PROXY_URL`~~ — RESOLVED 2026-07-02: Bright Data's residential-proxy tier needs a card on file even for free credits, which conflicts with the free-only rule, so declined. Not a blocker — Gemini-watches-video (already running) is the free analysis path, just slower per video than a transcript read would be. Cockpit now shows this as an optional "(skipped by choice)" chip, not a red MISSING.

## C2. EXCAVA conversation — installment 2 (answer anytime)
14. **Crew scope:** residents now wander every tab (bubbles = real dept status, click → cockpit). More of them / bigger / also on phone / quieter? Kill switch exists. _Default: keep as is, tune on your feedback._
15. **Creators quality gate:** before a creation (skill/prompt/scaffold/design) is accepted into the hub, what proof? _Default: EXCAVA self-test + your one-click review; nothing publishes untested._
16. **Dynamic departments:** who may open/close them? _Default: EXCAVA proposes with a reason, you approve; it may auto-close its own idle ones._

## E. Working mode
13. Confirm: keep doing big autonomous chunks on Fable (all visuals), Opus only for your own refinement passes; questions parked here. _Default: yes._

## F. Program gate decisions D1–D5 (from EXCAVA_PROGRAM.md, 2026-07-03)
17. **D1 — architecture** — ✅ ANSWERED 2026-07-03: **cron heartbeat** (Eitan picked it live in-session). Phase 0 built on it same day: the hourly `python -m src.excava` beat in bulk_analyze.yml IS the heartbeat; the file bus resumes state between beats.
18. **D2** — ✅ ANSWERED 2026-07-03: **direction-loop + change-tutorials first**, and the integration must be DAEMON-GRADE ("like a daemon for the entire project, not something casual, like in cortexOS — a clean daemon part of the OS that connects, or full integration"). HORSE-style fan-out pulled into Phase 6 scope. First daemon step shipped same day: every lane's runs now become OS bus events (the cockpit's 📡 feed).
19. **D3 — approval style:** approve the program as ONE block, or phase-by-phase sign-off? _Default: one block, with the per-phase ask-checkpoints still running._
20. **D4 — rebuild order:** spine-first as planned (P0 before any cleanup), or interleave small cleanups? _Default: spine-first._
21. **D5 — connectors tab:** OK to shrink it to verified-only once Phase 4 resolves real installs (94% are empty today)? _Default: yes._

## H. Phase checkpoints — ✅ ANSWERED 2026-07-03 (second batch)
26. **P3 creators** — ✅: creations enter the project autonomously WHEN labeled "Created by EXCAVA"; an independent test re-runs before first use; creators may build MCP servers/connectors/tools; **"PACKAGES"** = the owner's term for multi-element bundles (skills+tools+commands+designs+prompts+formats+outlines+MCP servers). Now guardrail G-12.
27. **P4 connectors** — ✅: **sandbox test-run EVERYTHING** (all 1,142; 6-hourly CI batches; verified-only tab per D5).
28. **P7 porting** — ✅: skip for now; harness stays a clean documented package (PORTABLE_HARNESS.md).
29. **P8 G9** — ✅: "Agency/Orchestration", equal weight — live on the North Star (scored 80 at birth).

## G. Omni-source intake + memory master (2026-07-03 owner additions)
22. **Your communities:** which subreddits / public Telegram channels / search queries should tier-1 intake watch? Starter set is in `data/social_sources.json` (LocalLLaMA, ClaudeAI, ChatGPTCoding, artificial, AI_Agents; Telegram empty — t.me/s only works for PUBLIC channels). _Default: keep the starter set, grow it over time._
23. **WhatsApp groups:** the only free path is you exporting a group chat (.txt, no media) from your phone into `data/whatsapp_exports/` occasionally — the miner parses the links out. Want a short how-to tutorial for that? _Default: yes, added with the Phase-6 change-tutorials._
24. **D6 — locked feeds (Instagram/TikTok/Facebook/LinkedIn):** these need your logged-in cookies stored as CI secrets, with real risk of account flags. Ever opt in? _Default: no — public-only stands._
25. **Daemon interpretation check:** I read your D2 note as "every part of the project reports through the OS bus (all 16 lanes now emit events), residents/cockpit react to real machine-wide events, and EXCAVA is the single connective layer — not a cosmetic overlay." First step shipped (lane events). If you meant something MORE (e.g. an actual resident process on a host), say so — the free-only + PC-off rules currently make the cron heartbeat the only clean daemon body. _Default: my reading._

## I. Fire 54 finding — undiagnosed claude-code-action failures on discover/improve
31. **Fire 55 escalation of item 30: `analyze.yml` — the CORE M1 ingestion lane — has now
started failing with the identical SDK-level signature, and it's actively blocking real work
(1,209 videos stuck in `data/_pending/`, catch-up mode active).** Pulled real job logs (not just
run status) via `mcp__github__get_job_logs`. Three data points, all with the same
`is_error:true, num_turns:1, total_cost_usd:0, duration_ms~1.8-2.2s` signature (SDK dies before
any model turn, so it can't be a normal content/tool error): (a) `discover.yml` — every run
since 07-14, exactly as fire 54 found, corroborated verbatim; (b) `improve.yml` — narrower than
fire 54 first read it: checked its full run history and only the two most recent **Saturday**
weekly-deep-pass runs (07-18, 07-25) fail — every one of the 18 daily first-week-intensive runs
in between succeeds; (c) NEW — `analyze.yml` itself failed its last 2 scheduled runs tonight
(22:50 and 23:50 UTC), both catch-up-sprint runs (the `*/30 * * * *` cron, which only does real
work when `data/catch_up.json.active` is true — it is, with 1,209 pending videos). The pattern
across all three (a rarely-run lane fails consistently, a weekly-heavy run fails, and a
high-frequency lane starts failing only once catch-up mode raised its call rate) points at a
**usage/rate ceiling on the shared `CLAUDE_CODE_OAUTH_TOKEN_REAL` subscription token**, not a
code bug in any of the 3 workflow files (they're structurally near-identical to `review.yml`,
which is NOT failing) and not a literally-expired token (an expiry wouldn't explain the
Saturday-only / volume-correlated pattern). **Did not act on this beyond documenting it** — I
did not touch `show_full_output` (fire 54's own default-if-unanswered still stands and I found
enough via the Actions job-logs API without it) and did not edit `analyze.yml`'s `token_hint`
text (currently tells whoever reads `data/status.json` to "renew the token via `claude
setup-token`" on any failure — plausibly the WRONG diagnosis if this is a self-healing rate
ceiling, but rewriting a diagnostic message on a live, currently-failing core lane felt like a
unilateral call worth your sign-off, not a same-fire fix). _Ask: is `CLAUDE_CODE_OAUTH_TOKEN_REAL`
on a Pro/Max plan with a weekly or 5-hour rolling usage cap? If so, the fix is likely
throttling/backing off `analyze.yml`'s catch-up sprint cadence (currently every 30 min) rather
than anything code-side. No default proposed — I don't have enough visibility into the actual
Anthropic-side plan/limits from this sandbox to guess responsibly; this is the single most
urgent open item in this file right now since it's blocking real M1 content ingestion, not just
housekeeping._

> **Fire 57 update — the pattern is now clear, and it's transient, not sustained.** Pulled
> `analyze.yml`'s last 30 scheduled runs via `mcp__github__actions_list`: **10 failures / 30
> runs (2026-07-27 → 2026-07-29T01:29Z), and every single failure falls between 20:00 and
> 02:00 UTC** — 20:02, 20:05, 22:00, 22:50, 23:54, 01:28, 02:00 (07-27→07-28 night), then
> 22:50, 23:50, 01:28 again the next night. Every one of those nightly windows is bracketed by
> successful runs earlier and later the same day (e.g. 07-28 succeeded at 21:54, 21:57 — right
> before failing again at 22:50). A hard-expired/revoked token fails 100% of attempts, not a
> clustered ~1-in-3 that self-heals by morning every single day — this rules out "renew the
> token" as the actual fix and confirms the rolling usage/rate-ceiling theory fire 55 proposed
> but couldn't confirm. **Applied a safe, code-only, non-brain fix** (no schedule/cadence
> change, since that still needs your call per fire 55's ask): `analyze.yml`'s health-recording
> step now tracks `analyze_consecutive_fails` in `data/status.json` and only escalates
> `token_hint` to "check the token" after 3+ failures IN A ROW with no success in between —
> below that it correctly reports "likely transient nightly ceiling, no action needed" instead
> of crying wolf on every isolated blip (which is what was happening before: every one of
> those 10 failures individually told you to go renew a token that was never actually
> expired). Verified: extracted and `compile()`-checked both embedded Python heredocs in the
> edited step (syntax OK), and hand-simulated the fail/fail/fail/success/fail sequence against
> the exact logic — counter climbs 1→2→3 with the message correctly flipping to "sustained" at
> 3, then resets to 0 and clears the hint on the first success, then restarts at 1 on the next
> failure. Could not live-fire the actual GitHub Actions step from this sandbox (it only runs
> on the real schedule), so this is verified by direct logic simulation, not an end-to-end
> Actions run — watch `data/status.json.analyze_consecutive_fails` over the next few nightly
> windows to confirm it behaves the same way in production. **Your original ask still stands
> and is still the real fix**: if `CLAUDE_CODE_OAUTH_TOKEN_REAL` is on a plan with a 5-hour or
> daily rolling cap, spacing out `analyze.yml`'s catch-up cron (and/or the other lanes sharing
> the same token) away from the 20:00-02:00 UTC window would cut these failures close to zero
> instead of just correctly-labeling them. I did not touch the cron cadence itself this fire —
> still your call, still no default proposed._

30. **`discover.yml` and `improve.yml` have been intermittently failing at the SDK level, not visible from the job status alone.** Every `discover.yml` run since 2026-07-14 (7 in a row as of 07-28) reports `conclusion: failure`, and `improve.yml`'s Saturday 07-25 mandatory pass failed the same way. In every case the Claude Code Action's own result JSON shows `is_error: true`, `num_turns: 1`, `total_cost_usd: 0`, `duration_ms` ~1.9-2.2s — it fails almost immediately, before doing any billable work, so nothing gets written and the safety-commit step correctly finds "nothing to commit" (that part isn't a bug). Ruled out a local-repo cause: no changes to `discover.yml`/`DISCOVER.md`/`config.json` around 07-13→07-14 when the failures started. The actual error text is hidden (`show_full_output` isn't set on either workflow, and the action deliberately redacts stdout "for security"), so I can't see WHY it's erroring from here — could be a transient API/quota issue on the free-pool token, a claude-code-action version regression, or something in the DISCOVER.md/IMPROVE.md prompt tripping a guardrail. _Ask: OK to set `show_full_output: true` on just these two lanes for one diagnostic cycle (their logs are already on a private-by-default Actions tab, but the output could contain repo content) so a future fire can see the real error and fix it, or would you rather I leave it flagged here for you to check first?_ Default if unanswered: leave `show_full_output` off (favor not exposing more in logs) and keep flagging until an unrelated fire happens to get visibility another way (e.g. `workflow_dispatch` with `-a`/manual log pull already used this fire).

> **Fire ~63 update — found and fixed one confirmed bug, and ran a live experiment that OVERTURNS the "just move the cron" fix fire 57 proposed for `discover.yml`.** Two separate findings, don't conflate them:
> 1. **`improve.yml` was genuinely missing `claude_args` entirely** — every sibling `claude-code-action` step (`analyze.yml`, `discover.yml`, `review.yml`) explicitly sets `--allowedTools "Bash,Edit,Write,Read,Glob,Grep,WebFetch,WebSearch,TodoWrite"`; `improve.yml`'s step had no `claude_args` key at all, so it ran under whatever the SDK's bare default is. Fixed (added the same allowedTools line, matching the siblings) — safe, one-line, no data/cadence touched. Shipped this fire.
> 2. **`discover.yml`'s failure does NOT reproduce only in the 20:00–02:00 UTC window fire 57 identified for `analyze.yml`.** Pulled `review.yml`'s last 30 runs: it fires at 23:00 UTC (squarely inside that same window) and is **30/30 success** — direct counter-evidence that the window alone explains anything for a low-frequency lane. Then ran the actual experiment: manually `workflow_dispatch`'d `discover.yml` right now at **09:04 UTC** — a time `analyze.yml` has been succeeding at consistently all morning (08:23, 07:31, 05:41 all green). It **failed anyway**, with the byte-identical signature (`is_error:true, num_turns:1, total_cost_usd:0, duration_ms:2227`). That rules out "just reschedule it to daytime" as a sufficient fix — the cause travels with the workflow/token, not the clock. Given `data/catch_up.json` shows catch-up mode active since 07-17 (1,233 pending, `analyze.yml`'s `*/30 * * * *` catch-up cron hammering the same shared `CLAUDE_CODE_OAUTH_TOKEN_REAL` continuously since), my best-supported read now is a **sustained/rolling usage cap kept almost permanently exhausted by the catch-up sprint's own call volume**, not a fixed nightly clock window — a low-frequency lane like `discover`/`improve` gets unlucky almost every time it fires because the token rarely has headroom at all right now, while `analyze.yml`'s sheer retry frequency (every 30 min) still finds enough gaps to mostly succeed, and `review.yml`'s 1-2x/week cadence has so far dodged it by luck of the draw, not immunity. **Did not act on the cadence itself** (still your call, per fire 55/57's own standing ask — now with much stronger evidence backing it): the concrete lever, if this read is right, is throttling `analyze.yml`'s catch-up-sprint cadence (currently every 30 min, only active because `catch_up.json.active:true`) rather than moving `discover`/`improve`'s cron times, which this fire's live test just showed wouldn't help. Left `show_full_output` off, per the standing default — didn't need it this time; the workflow_dispatch experiment got a clean, reproducible answer without it.

31. **Away-loop analyze pace vs. "as many reps as possible."** Fire 64 hand-drained 5 pending videos through the full `CLAUDE.md` pipeline (skills/tools/connectors/tips/commands/news, per-tab dedup, comment-gate logging) in one session, against a backlog of ~1,228. That's the honest throughput of doing the extraction carefully — a full read + judgment call per video across 6+ tabs, with the anti-boilerplate and comment-corroboration gates actually enforced, not skipped. Going meaningfully faster from a Claude Code away-session (as opposed to the CI `bulk_analyze`/`analyze.yml` lanes, which use cheaper free-tier models for volume) means trading off either depth-per-video or the number of tabs touched. _Ask: is 5-10 carefully-extracted videos per away-fire the right target, or would you rather away-fires triage a larger batch more shallowly (e.g. skip Steps 3c/8b tab-candidate mining, or raise the low-quality bar to skip extraction entirely below a threshold) and leave the deep pass to the CI lanes?_ Default if unanswered: keep doing full-depth extraction at whatever pace that allows per fire, since CLAUDE.md's own "extract everything" / anti-boilerplate rules already take priority over raw volume for a single-session actor like this.

32. **Branch/PR pile-up is back up.** Fire 55 audited and closed 12 redundant PRs, leaving 5 open on purpose (#2, #14, #18, #23, #25) plus whatever accumulated after. As of fire 64 there are 9 open draft PRs (#2, #14, #18, #23, #24, #25, #29, #30, #31) and 37 `claude/kind-shannon-*` branches on origin, most without any PR at all. Not re-audited this fire (fire 55's writeup already explains why 29/31 were clutter and the 5 deliberate holds — re-deriving that from scratch every fire wastes tokens on bookkeeping instead of the actual product). _Ask: same as fire 55/29's standing one — should a periodic (not every-fire) sweep be scheduled, or is this fine to let a human clear out during a real session?_ No default action taken.
