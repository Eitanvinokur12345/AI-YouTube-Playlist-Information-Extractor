# Database Design — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01
**Engine:** SQLite, encrypted at rest (see C-01)

---

## 1. Design principles

1. **Sync-ready from row one.** Every table carries the columns a future sync engine needs
   (`device_id`, `revision`, `updated_at`, `deleted_at`). Adding them later would mean migrating
   every row of a live personal history — cheap now, painful then.
2. **Multi-user-ready from row one.** Every user-scoped table has `user_id`, even though exactly one
   user exists. No query is allowed to assume a singleton.
3. **Soft deletes only.** A hard delete cannot be synced and cannot be undone. `deleted_at IS NULL`
   is part of every read. The one exception: a user-initiated *purge* physically removes rows and
   shreds media, because "delete my data" must actually mean it.
4. **Append-only history.** The XP ledger, the timeline, and habit entries are never updated in
   place. Correction is a new compensating row. This makes the gamification auditable and makes
   merges during sync trivial.
5. **Derived state is cached, never authoritative.** Level, XP totals, and streaks live in cache
   columns for O(1) reads and are always recomputable from their logs. A `recompute` command exists
   for every one of them, and a test asserts cache equals recomputation.
6. **No blobs in the database.** Media lives in the encrypted file store; the DB holds metadata and
   a reference. Blobs bloat the file, slow every query, and make backups unmanageable.
7. **UUIDv7 identifiers.** Globally unique (no cross-device collisions) and time-ordered (index
   locality as good as an autoincrement integer).

---

## 2. Conventions

| Convention | Rule |
|---|---|
| Table names | `snake_case`, singular (`goal`, not `goals`) |
| Primary key | `id TEXT PRIMARY KEY` — UUIDv7 as a lowercase hyphenated string |
| Timestamps | `TEXT`, ISO-8601 UTC with milliseconds (`2026-08-01T12:34:56.789Z`) — sortable as text, readable in a dump |
| Dates without time | `TEXT` as `YYYY-MM-DD` **in the user's local timezone**. Habit check-ins are local-day events; storing them as UTC instants makes "did I do it today" wrong for anyone not on UTC |
| Booleans | `INTEGER` 0/1, `NOT NULL DEFAULT 0` |
| Enums | `TEXT` with a `CHECK` constraint — readable in a dump, validated by the engine |
| Money/decimals | Not used. Measurements are `REAL` with an explicit unit column |
| Foreign keys | `ON DELETE RESTRICT`; lifecycle is managed by application code so soft deletes stay coherent |
| Every table | `created_at`, `updated_at`, `deleted_at`, `device_id`, `revision` |
| Every user-scoped table | `user_id NOT NULL REFERENCES user(id)` |

**Pragmas set on every connection:**

```sql
PRAGMA journal_mode = WAL;      -- concurrent reads during writes
PRAGMA foreign_keys = ON;       -- off by default in SQLite; must be set per connection
PRAGMA synchronous = NORMAL;    -- safe with WAL, much faster than FULL
PRAGMA busy_timeout = 5000;
```

---

## 3. Entity overview

```
                            ┌──────────┐
                            │   user   │
                            └────┬─────┘
                                 │ 1
        ┌────────────┬───────────┼───────────┬────────────┬──────────────┐
        │ n          │ n         │ n         │ n          │ n            │ n
   ┌────▼────┐  ┌────▼────┐ ┌────▼────┐ ┌────▼──────┐ ┌───▼────────┐ ┌───▼──────────┐
   │ profile │  │  goal   │ │  habit  │ │   task    │ │ xp_ledger  │ │timeline_event│
   └─────────┘  └────┬────┘ └────┬────┘ └───────────┘ └────────────┘ └──────────────┘
                     │ 1         │ 1
                ┌────▼──────┐ ┌──▼──────────┐
                │goal_      │ │habit_entry  │
                │milestone  │ │(append-only)│
                └───────────┘ └─────────────┘

   ┌────────────────┐   ┌──────────────┐   ┌───────────┐   ┌──────────────┐
   │progression_    │   │  settings    │   │attachment │   │ event_outbox │
   │state (cache)   │   │              │   │(phase 2)  │   │              │
   └────────────────┘   └──────────────┘   └───────────┘   └──────────────┘
```

Phase 2+ adds: `sleep_entry`, `workout`, `exercise`, `workout_set`, `body_measurement`,
`progress_photo`, `nutrition_entry`, `skin_entry`, `voice_session`, `voice_metric`, `focus_session`,
`resource`, `achievement`, `achievement_unlock`, `reward`, `reward_redemption`, `ai_request_log`,
`sync_state`. They follow the same conventions and are specified when their phase begins.

---

## 4. Phase 1 schema

### 4.1 Migration 001 — foundation

```sql
-- Schema versioning and device identity.
CREATE TABLE meta (
  key         TEXT PRIMARY KEY,
  value       TEXT NOT NULL,
  updated_at  TEXT NOT NULL
);
-- seeded: schema_version, device_id, app_installed_at

CREATE TABLE user (
  id          TEXT PRIMARY KEY,
  created_at  TEXT NOT NULL,
  updated_at  TEXT NOT NULL,
  deleted_at  TEXT,
  device_id   TEXT NOT NULL,
  revision    INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE settings (
  id          TEXT PRIMARY KEY,
  user_id     TEXT NOT NULL REFERENCES user(id),
  key         TEXT NOT NULL,
  value       TEXT NOT NULL,          -- JSON-encoded
  created_at  TEXT NOT NULL,
  updated_at  TEXT NOT NULL,
  deleted_at  TEXT,
  device_id   TEXT NOT NULL,
  revision    INTEGER NOT NULL DEFAULT 1,
  UNIQUE (user_id, key)
);

-- Transactional outbox: events are written in the same transaction as the data
-- that caused them, then dispatched after commit. See ARCHITECTURE.md 4.2.
CREATE TABLE event_outbox (
  id             TEXT PRIMARY KEY,
  type           TEXT NOT NULL,
  payload        TEXT NOT NULL,       -- JSON
  aggregate_id   TEXT,
  occurred_at    TEXT NOT NULL,
  dispatched_at  TEXT,
  attempts       INTEGER NOT NULL DEFAULT 0,
  last_error     TEXT,
  device_id      TEXT NOT NULL
);
CREATE INDEX idx_outbox_undispatched ON event_outbox (dispatched_at, occurred_at)
  WHERE dispatched_at IS NULL;
```

### 4.2 Migration 002 — profile and timeline

```sql
CREATE TABLE profile (
  id                 TEXT PRIMARY KEY,
  user_id            TEXT NOT NULL REFERENCES user(id),
  display_name       TEXT,
  avatar_path        TEXT,            -- encrypted file store reference, not a blob
  becoming_statement TEXT,            -- "who I'm becoming"
  focus_areas        TEXT NOT NULL DEFAULT '[]',   -- JSON array of strings
  timezone           TEXT NOT NULL,   -- IANA, e.g. "Asia/Jerusalem"
  created_at         TEXT NOT NULL,
  updated_at         TEXT NOT NULL,
  deleted_at         TEXT,
  device_id          TEXT NOT NULL,
  revision           INTEGER NOT NULL DEFAULT 1,
  UNIQUE (user_id)
);

-- Append-only. Never UPDATE, never DELETE (except purge).
CREATE TABLE timeline_event (
  id            TEXT PRIMARY KEY,
  user_id       TEXT NOT NULL REFERENCES user(id),
  kind          TEXT NOT NULL CHECK (kind IN (
                  'goal_created','goal_completed','goal_milestone','goal_archived',
                  'habit_created','habit_completed','habit_streak','habit_archived',
                  'task_completed','xp_awarded','level_up','achievement_unlocked',
                  'milestone','note')),
  title         TEXT NOT NULL,
  detail        TEXT,
  subject_type  TEXT,                 -- 'goal' | 'habit' | 'task' | ...
  subject_id    TEXT,
  source_event  TEXT,                 -- event_outbox.id that produced this
  occurred_at   TEXT NOT NULL,
  local_date    TEXT NOT NULL,        -- YYYY-MM-DD for day grouping
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL,
  deleted_at    TEXT,
  device_id     TEXT NOT NULL,
  revision      INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_timeline_user_time ON timeline_event (user_id, occurred_at DESC);
CREATE INDEX idx_timeline_kind      ON timeline_event (user_id, kind, occurred_at DESC);
CREATE UNIQUE INDEX idx_timeline_source ON timeline_event (source_event)
  WHERE source_event IS NOT NULL;   -- idempotent: one timeline row per source event
```

That last partial unique index is doing real work: it makes timeline writes idempotent at the
database level, so a redelivered event cannot duplicate a timeline entry no matter what the
application code does.

### 4.3 Migration 003 — goals

```sql
CREATE TABLE goal (
  id             TEXT PRIMARY KEY,
  user_id        TEXT NOT NULL REFERENCES user(id),
  title          TEXT NOT NULL,
  description    TEXT,
  category       TEXT NOT NULL,
  status         TEXT NOT NULL DEFAULT 'active'
                   CHECK (status IN ('active','completed','archived','abandoned')),
  difficulty     INTEGER NOT NULL DEFAULT 1 CHECK (difficulty BETWEEN 1 AND 3),
  target_date    TEXT,                -- YYYY-MM-DD
  metric_name    TEXT,                -- e.g. "body weight", "books read"
  metric_unit    TEXT,
  start_value    REAL,
  target_value   REAL,
  current_value  REAL,
  completed_at   TEXT,
  created_at     TEXT NOT NULL,
  updated_at     TEXT NOT NULL,
  deleted_at     TEXT,
  device_id      TEXT NOT NULL,
  revision       INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_goal_user_status ON goal (user_id, status, deleted_at);

CREATE TABLE goal_milestone (
  id            TEXT PRIMARY KEY,
  goal_id       TEXT NOT NULL REFERENCES goal(id),
  user_id       TEXT NOT NULL REFERENCES user(id),
  title         TEXT NOT NULL,
  target_value  REAL,
  target_date   TEXT,
  reached_at    TEXT,
  sort_order    INTEGER NOT NULL DEFAULT 0,
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL,
  deleted_at    TEXT,
  device_id     TEXT NOT NULL,
  revision      INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_milestone_goal ON goal_milestone (goal_id, sort_order);
```

Progress is computed, not stored: `(current_value − start_value) / (target_value − start_value)`,
clamped to 0–1, with a null-safe fallback to milestone completion ratio when no metric is defined.

### 4.4 Migration 004 — habits, entries, XP

```sql
CREATE TABLE habit (
  id                 TEXT PRIMARY KEY,
  user_id            TEXT NOT NULL REFERENCES user(id),
  goal_id            TEXT REFERENCES goal(id),      -- optional link
  title              TEXT NOT NULL,
  description        TEXT,
  category           TEXT NOT NULL,
  difficulty         INTEGER NOT NULL DEFAULT 1 CHECK (difficulty BETWEEN 1 AND 3),
  schedule_type      TEXT NOT NULL
                       CHECK (schedule_type IN ('daily','times_per_week','specific_days')),
  schedule_config    TEXT NOT NULL DEFAULT '{}',    -- JSON: {times:3} | {days:[1,3,5]}
  status             TEXT NOT NULL DEFAULT 'active'
                       CHECK (status IN ('active','paused','archived')),
  -- cached, recomputable from habit_entry
  current_streak     INTEGER NOT NULL DEFAULT 0,
  longest_streak     INTEGER NOT NULL DEFAULT 0,
  grace_days_used    INTEGER NOT NULL DEFAULT 0,
  last_completed_on  TEXT,
  created_at         TEXT NOT NULL,
  updated_at         TEXT NOT NULL,
  deleted_at         TEXT,
  device_id          TEXT NOT NULL,
  revision           INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_habit_user_status ON habit (user_id, status, deleted_at);

-- Append-only log of check-ins. One row per habit per local day, at most.
CREATE TABLE habit_entry (
  id           TEXT PRIMARY KEY,
  habit_id     TEXT NOT NULL REFERENCES habit(id),
  user_id      TEXT NOT NULL REFERENCES user(id),
  local_date   TEXT NOT NULL,          -- YYYY-MM-DD, user's timezone
  completed_at TEXT NOT NULL,
  state        TEXT NOT NULL DEFAULT 'completed'
                 CHECK (state IN ('completed','skipped','grace')),
  note         TEXT,
  created_at   TEXT NOT NULL,
  updated_at   TEXT NOT NULL,
  deleted_at   TEXT,
  device_id    TEXT NOT NULL,
  revision     INTEGER NOT NULL DEFAULT 1
);
CREATE UNIQUE INDEX idx_habit_entry_day ON habit_entry (habit_id, local_date)
  WHERE deleted_at IS NULL;
CREATE INDEX idx_habit_entry_user_date ON habit_entry (user_id, local_date DESC);

-- Append-only XP ledger. The single source of truth for XP and level.
CREATE TABLE xp_ledger (
  id               TEXT PRIMARY KEY,
  user_id          TEXT NOT NULL REFERENCES user(id),
  amount           INTEGER NOT NULL,     -- may be negative (reversal)
  reason           TEXT NOT NULL CHECK (reason IN (
                     'habit_completed','habit_streak','task_completed',
                     'goal_milestone','goal_completed','daily_bonus',
                     'reward_redeemed','reversal','manual_adjustment')),
  subject_type     TEXT,
  subject_id       TEXT,
  source_event_id  TEXT NOT NULL,        -- event_outbox.id — the idempotency key
  reverses_id      TEXT REFERENCES xp_ledger(id),
  occurred_at      TEXT NOT NULL,
  created_at       TEXT NOT NULL,
  updated_at       TEXT NOT NULL,
  deleted_at       TEXT,
  device_id        TEXT NOT NULL,
  revision         INTEGER NOT NULL DEFAULT 1
);
CREATE UNIQUE INDEX idx_xp_source_event ON xp_ledger (source_event_id, reason);
CREATE INDEX idx_xp_user_time ON xp_ledger (user_id, occurred_at DESC);

-- Cached aggregate. Recomputable from xp_ledger at any time.
CREATE TABLE progression_state (
  id                TEXT PRIMARY KEY,
  user_id           TEXT NOT NULL REFERENCES user(id),
  lifetime_xp       INTEGER NOT NULL DEFAULT 0,   -- drives level; never decreases
  spendable_xp      INTEGER NOT NULL DEFAULT 0,   -- currency for rewards
  level             INTEGER NOT NULL DEFAULT 1,
  xp_into_level     INTEGER NOT NULL DEFAULT 0,
  recomputed_at     TEXT NOT NULL,
  created_at        TEXT NOT NULL,
  updated_at        TEXT NOT NULL,
  deleted_at        TEXT,
  device_id         TEXT NOT NULL,
  revision          INTEGER NOT NULL DEFAULT 1,
  UNIQUE (user_id)
);
```

`idx_xp_source_event` is the mechanism behind PRD rule X-2: a redelivered event cannot double-award,
because the second insert violates a unique constraint. The application catches that specific
violation and treats it as success. Correctness enforced by the database, not by careful code.

The two XP counters implement PRD §7.5: redeeming a reward decrements `spendable_xp` only, so buying
yourself a reward can never take away a level you earned.

### 4.5 Migration 005 — tasks

```sql
CREATE TABLE task (
  id            TEXT PRIMARY KEY,
  user_id       TEXT NOT NULL REFERENCES user(id),
  goal_id       TEXT REFERENCES goal(id),
  title         TEXT NOT NULL,
  notes         TEXT,
  priority      INTEGER NOT NULL DEFAULT 1 CHECK (priority BETWEEN 1 AND 3),
  due_date      TEXT,                  -- YYYY-MM-DD
  status        TEXT NOT NULL DEFAULT 'open'
                  CHECK (status IN ('open','completed','cancelled')),
  completed_at  TEXT,
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL,
  deleted_at    TEXT,
  device_id     TEXT NOT NULL,
  revision      INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_task_user_status ON task (user_id, status, due_date);
```

### 4.6 Attachment (schema defined now, used from Phase 2)

Defined here because C-05 ("where does unlimited content live") is a schema question, and the answer
has to be in the table from the start.

```sql
CREATE TABLE attachment (
  id             TEXT PRIMARY KEY,
  user_id        TEXT NOT NULL REFERENCES user(id),
  kind           TEXT NOT NULL CHECK (kind IN ('image','audio','video','document')),
  owner_type     TEXT NOT NULL,        -- 'progress_photo' | 'voice_session' | 'profile' ...
  owner_id       TEXT,
  location       TEXT NOT NULL DEFAULT 'local'
                   CHECK (location IN ('local','external','remote')),
  relative_path  TEXT NOT NULL,        -- within the encrypted media store
  remote_ref     TEXT,                 -- populated only if location != 'local'
  mime_type      TEXT NOT NULL,
  byte_size      INTEGER NOT NULL,
  width          INTEGER,
  height         INTEGER,
  duration_ms    INTEGER,
  thumb_path     TEXT,
  sensitive      INTEGER NOT NULL DEFAULT 1,   -- default sensitive; opt OUT, never opt in
  captured_at    TEXT,
  checksum       TEXT NOT NULL,        -- of the plaintext, for integrity verification
  created_at     TEXT NOT NULL,
  updated_at     TEXT NOT NULL,
  deleted_at     TEXT,
  device_id      TEXT NOT NULL,
  revision       INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX idx_attachment_owner ON attachment (owner_type, owner_id);
CREATE INDEX idx_attachment_user  ON attachment (user_id, kind, created_at DESC);
```

`location` is what makes C-05 Option B (offload to the user's own NAS/server) a later feature rather
than a later migration. `sensitive` defaults to 1 — media is treated as private unless explicitly
marked otherwise, because the opposite default fails dangerously.

---

## 5. Migrations

### Policy

- **Forward-only, numbered, immutable.** `001_foundation.sql`, `002_profile_timeline.sql`, …
  A migration that has ever run on a real device is never edited; corrections come as a new
  migration. Editing a shipped migration means two devices with the same `schema_version` have
  different schemas — an unresolvable state.
- **One transaction per migration.** A failure rolls back completely. There is no half-migrated
  state.
- **Schema version in `meta`.** Read at startup; migrations above the current version run in order.
- **No down-migrations.** Rolling back a personal data store loses data. Recovery is
  restore-from-backup, which is why backup lands in Sprint 6 and not later.
- **Backup before migrating.** From Sprint 6 onward, the runner snapshots the database before
  applying anything, and restores it automatically on failure.

### Testing (non-negotiable)

Every migration is covered by three tests, permanently:

1. **Fresh install** — apply `001..N` to an empty database; assert the final schema.
2. **Upgrade path** — load a fixture database at version `N−1` containing realistic data; apply `N`;
   assert no data was lost or corrupted.
3. **Idempotent runner** — run the migrator twice; the second run is a no-op.

The version-`N−1` fixtures are committed to the repository and never regenerated. They are the only
honest test that a real upgrade works.

### Version compatibility

The database records the app version that last opened it. An older app opening a newer database
refuses to run rather than corrupting it — with a clear message, not a crash.

---

## 6. Encryption considerations

### At rest

The entire database file is encrypted (C-01, ADR-2). Consequences to design around:

- **The key must exist before the connection opens.** Migration therefore runs *after* key
  bootstrap, which shapes the startup sequence: keychain → key → open DB → migrate → compose modules
  → render.
- **A wrong key looks like a corrupt file, not an auth error.** The open path must distinguish "not
  yet initialised" from "key mismatch" from "genuinely corrupt", and report each differently. Getting
  this wrong turns a recoverable state into a support nightmare for the one person who uses it.
- **WAL and journal files are encrypted too.** Any tooling or backup that copies the database must
  copy `-wal` and `-shm`, or checkpoint first. Backup checkpoints first.
- **Key rotation** (changing the passphrase) rewrites the file. It must be transactional, verified,
  and never leave both an old and a new file where a crash could pick the wrong one.

### Media

Handled outside the database entirely: per-file AES-256-GCM with a random file key, wrapped by the
master key and stored in the file header. Rotating the master key rewraps headers rather than
re-encrypting gigabytes of photos — a small design choice that turns an hour-long operation into a
second-long one.

The `checksum` column stores a hash of the **plaintext**, so integrity can be verified after
decryption. AES-GCM already authenticates the ciphertext; the plaintext checksum additionally proves
the right file was decrypted for the right row after a restore.

### Backups

An export is: checkpoint WAL → copy the encrypted database → copy the encrypted media → package with
a manifest (schema version, app version, device id, counts, checksums) → encrypt the package with a
key derived from the user's passphrase via Argon2id (parameters recorded in the manifest header so
future versions can verify what was used) → write to the user's chosen location.

Restore reverses it, validating the manifest and checksums *before* touching existing data. A failed
restore must never leave the app worse off than a refusal.

### Not encrypted

`meta.schema_version` and `meta.device_id` sit inside the encrypted file like everything else — there
is no plaintext sidecar. Nothing about the user's data is stored outside the encrypted boundary, not
even counts or timestamps.

---

## 7. Query patterns to design for

The indexes above exist because of these specific reads:

| Screen | Query | Index |
|---|---|---|
| Today | Habits due on date D | `idx_habit_user_status` + schedule evaluation in code |
| Today | Tasks due ≤ D, open | `idx_task_user_status` |
| Timeline | Page N of events, newest first | `idx_timeline_user_time` |
| Habit detail | Entries for habit over a year | `idx_habit_entry_day` |
| Progression | Sum of XP by day/week/month | `idx_xp_user_time` |
| Goals | Active goals with progress | `idx_goal_user_status` |
| Storage screen | Sum of `byte_size` grouped by kind | `idx_attachment_user` |

Schedule evaluation ("is this habit due today") happens in the domain layer, not in SQL. It depends on
streak state, grace days, and the user's timezone — logic that belongs in tested pure functions, not
in a query.

---

## 8. Data volume expectations

One user, ten years, aggressive use:

| Table | Rows |
|---|---|
| `habit_entry` | ~55,000 (15 habits × 3,650 days) |
| `timeline_event` | ~150,000 |
| `xp_ledger` | ~120,000 |
| `task` | ~20,000 |
| `attachment` | ~15,000 (metadata only — bytes on disk) |

Well under a hundred megabytes of structured data. SQLite handles this without effort; the performance
work is entirely about not doing full-table scans on render, which the indexes and virtualized lists
above address. **Media is the only real storage concern** — 15,000 photos at 3 MB is ~45 GB, which is
exactly why C-05 needs an answer and why the storage-usage screen is in Sprint 5.
