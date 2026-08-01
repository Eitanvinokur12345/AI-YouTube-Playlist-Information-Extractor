# MVP Plan — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01

---

## The MVP test

Phase 1 is finished when this is true: **the owner has used the app every day for a month, and
losing it would be annoying.** Not "the code compiles", not "all the screens exist" — daily use.

That test drives the sequencing below. Every sprint ends with something usable, and the app is never
in a state where it cannot be opened and operated.

---

## Phase 1 — Application foundation

Six sprints. A sprint is a unit of scope, not a fixed number of days — this is a solo project with no
imposed deadline, so the roadmap is ordered by dependency rather than dated (see
[`DEVELOPMENT_ROADMAP.md`](./DEVELOPMENT_ROADMAP.md)).

### Sprint 1 — Foundation

*Nothing user-facing ships here. This sprint buys the right to build everything else quickly.*

| # | Deliverable |
|---|---|
| 1.1 | Expo + TypeScript project scaffold, strict compiler settings, pinned SDK version |
| 1.2 | Tooling: ESLint (including the boundary rules from `ARCHITECTURE.md` §3.1), Prettier, Jest, RNTL, CI running lint + typecheck + tests |
| 1.3 | Folder structure per `ARCHITECTURE.md` §3, with a placeholder in each layer so the shape is visible |
| 1.4 | Encrypted SQLite connection, key bootstrap from keychain, first-run key generation |
| 1.5 | Migration runner: numbered, forward-only, transactional, with a `schema_version` record and a test that applies every migration from empty |
| 1.6 | Migration `001` — `meta`, `user`, `settings` tables |
| 1.7 | Core primitives: `Clock`, `IdGenerator` (UUIDv7), `Result`, error taxonomy, redacting logger |
| 1.8 | Event bus with a transactional outbox, durable dispatch, at-least-once delivery, and idempotency tests |
| 1.9 | Encrypted file store: write/read/shred, per-file keys, orphan scan |
| 1.10 | App shell: Expo Router, tab layout, theme tokens, i18n scaffold (RTL-ready), safe areas |
| 1.11 | App lock: biometric/PIN gate, background snapshot blur, re-auth timeout |
| 1.12 | First-run flow: generate keys, set backup passphrase, create the single local user |

**Done when:** the app installs on a physical device, locks and unlocks, creates an encrypted
database, survives a restart with data intact, and the database file is unreadable with an external
SQLite tool. CI is green.

**Risk note:** 1.4 and 1.5 are the highest-risk items in the entire project. If the encrypted-driver
choice does not work on both platforms, that must surface in Sprint 1, not Sprint 5. Spike this first,
before anything else.

### Sprint 2 — Profile and timeline

| # | Deliverable |
|---|---|
| 2.1 | Migration `002` — `profile`, `timeline_event` |
| 2.2 | Profile domain entity, repository, use cases (view, edit) |
| 2.3 | Profile screen: name, avatar, focus areas, "who I'm becoming" statement, member-since |
| 2.4 | Timeline service subscribing to the event bus, writing `timeline_event` rows |
| 2.5 | Timeline screen: reverse-chronological, paged backwards, grouped by day, filter by type |
| 2.6 | Design system pass: typography, spacing, colour, dark/light, empty states, loading, errors |

**Done when:** the profile is editable and persists, and every event published anywhere in the app
appears in the timeline. The timeline is deliberately built early — it is the integration test for
the event bus, and every later feature gets its history for free.

### Sprint 3 — Goals

| # | Deliverable |
|---|---|
| 3.1 | Migration `003` — `goal`, `goal_milestone` |
| 3.2 | Goal entity and rules: status transitions, progress computation, target validation |
| 3.3 | Repository + use cases: create, edit, archive, complete, add/complete milestone |
| 3.4 | Goals list (active / completed / archived), goal detail with milestones and progress |
| 3.5 | Create/edit goal form with validation |
| 3.6 | Events: `GoalCreated`, `GoalMilestoneReached`, `GoalCompleted`, `GoalArchived` |

**Done when:** goals can be created, progressed, and completed; each transition lands in the timeline.

### Sprint 4 — Habits, streaks, and XP

*The core loop. This is the sprint that decides whether the app is worth opening daily.*

| # | Deliverable |
|---|---|
| 4.1 | Migration `004` — `habit`, `habit_entry`, `xp_ledger`, `progression_state` |
| 4.2 | Schedule value object: daily, N-per-week, specific weekdays; "is due on date" logic |
| 4.3 | Streak rules with grace days, computed against *scheduled* occurrences (PRD X-6, X-7) |
| 4.4 | Habit repository + use cases: create, edit, archive, check in, undo check-in |
| 4.5 | XP service: idempotent awards keyed by event id, append-only ledger, reversal entries |
| 4.6 | Level curve and derivation; `progression_state` cache with a recompute-from-ledger path |
| 4.7 | Today screen: what is due now, one-tap check-in, XP bar, current level |
| 4.8 | Habit detail: streak, calendar heatmap of history, edit, archive |
| 4.9 | Level-up event, celebration, timeline entry |
| 4.10 | Property tests: no event sequence, including replays and crashes, can produce wrong XP |

**Done when:** a habit can be checked in daily, the streak survives a grace day, XP accrues, a
level-up fires exactly once, and replaying the entire event log reproduces the identical XP total.

### Sprint 5 — Tasks and integration

| # | Deliverable |
|---|---|
| 5.1 | Migration `005` — `task` |
| 5.2 | Task entity, repository, use cases: create, complete, uncomplete, link to a goal |
| 5.3 | Task list and inline creation; tasks surfaced on the Today screen |
| 5.4 | XP for task completion; timeline entries |
| 5.5 | Settings: XP curve tunables, grace-day count, lock timeout, theme, language |
| 5.6 | Storage usage screen — database size, media size, per-category breakdown (PRD P-11) |

**Done when:** the Today screen is a single coherent answer to "what am I doing today", combining
habits, tasks, and goal deadlines.

### Sprint 6 — Backup, hardening, and daily-use polish

| # | Deliverable |
|---|---|
| 6.1 | Encrypted export: full database + media, single file, passphrase-derived key (Argon2id) |
| 6.2 | Import/restore with schema-version compatibility checks and a dry-run validation pass |
| 6.3 | Delete-a-record and wipe-everything flows, with media shredding verified (PRD P-9, P-10) |
| 6.4 | Verification of P-16 … P-19: OS backup exclusion, no gallery writes, snapshot blur |
| 6.5 | Performance pass against Q-1 and Q-2 (cold start, 10,000-row lists) |
| 6.6 | Accessibility pass: screen reader, contrast, font scaling, reduce motion, RTL smoke test |
| 6.7 | Maestro E2E flows covering the seven MVP acceptance criteria |
| 6.8 | Empty states, error recovery, offline confirmation (Phase 1 makes no network calls at all) |

**Done when:** all seven acceptance criteria in `PRODUCT_REQUIREMENTS.md` §4 pass on a physical
device, including the wipe-and-restore test.

### Phase 1 exit criteria

1. Every MVP acceptance criterion passes on a real device.
2. Domain-layer coverage ≥ 90%; overall ≥ 70%.
3. Zero lint or type errors; boundary rules enforced in CI.
4. A backup taken on day one restores correctly on the final build.
5. The owner has used it daily for two weeks without hitting a blocking defect.

---

## Future phases

Each phase assumes the previous one is stable. Detail grows thinner further out on purpose — writing
a sprint plan for Phase 6 today would be fiction.

### Phase 2 — Health

Sleep entries and quality scoring; workout logging with an exercise catalogue and history; body
measurements with trends; **progress photos** (the first sensitive-media feature, which is why the
media protections P-16 … P-19 must be complete before it ships); recovery and nutrition tracking;
local notifications and reminders; the achievements and rewards catalogue on top of the Phase 1 XP
engine.

*Depends on:* Sprint 1 file store, Sprint 4 XP engine.
*Key decision needed first:* I-02 (health store integration), I-13 (photo protections), I-08
(notifications).

### Phase 3 — AI foundation and appearance

The `AiService`, consent gate, redactor, audit log, and processing-location UI — built before any AI
feature, so no feature can bypass them. First providers: on-device, then self-hosted, then external.
First analyses: progress-photo comparison, pattern detection over habit/sleep data, weekly narrative
summaries. Appearance tracking (skin, hair, style) builds on the photo infrastructure.

*Depends on:* Phase 2 media pipeline.
*Key decisions needed first:* I-03 (which providers), I-04 (which data classes may ever leave).

### Phase 4 — Voice and communication

Recording with the encrypted media pipeline; on-device acoustic analysis (volume, pace, pause
distribution) with no model required; session history and trends; optional transcription and coaching
feedback through the Phase 3 AI abstraction; the recording-consent warning (P-20).

*Depends on:* Phase 2 media pipeline, Phase 3 AI service for the model-dependent parts.

### Phase 5 — Synchronization

Encrypted event-log sync between the owner's own devices; the zero-knowledge relay or LAN-direct
peer transport; conflict resolution via HLC; new-device bootstrap from backup plus log catch-up.

*Depends on:* the sync-ready columns from Sprint 1, and a stable schema.
*Key decision needed first:* I-05 (topology, device count).

### Phase 6 — Productivity, knowledge, and platform expansion

Focus sessions and productivity analytics; the knowledge library with linked resources and reading
state; phone-usage restriction where the OS allows (O-04); web/desktop shells reusing the domain and
application layers.

### Phase 7 — Multi-user

Only if it is ever wanted. The schema is ready; this phase adds profile switching, per-user keys,
and — if it goes beyond one device's household — an actual identity model.

---

## What is deliberately not in Phase 1

Recorded so the omissions read as decisions rather than oversights: notifications, achievements,
rewards redemption, focus sessions, any AI, any network call, any sync, health, appearance, voice,
knowledge, web/desktop, and multi-user.

Every one of them is easier to add after the event bus, XP engine, and encrypted storage are proven —
and every one of them would have delayed the first day of real daily use.
