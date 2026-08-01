# API Contracts — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01

There is no network API in Phase 1. "API" here means the **internal contracts** between layers and
modules: repository interfaces, service interfaces, domain events, and the AI abstraction. These are
the seams described in [`ARCHITECTURE.md`](./ARCHITECTURE.md); this document is their precise form.

The TypeScript below is the specification, not shipped code. Signatures are expected to be
implemented as written; bodies are the implementation's problem.

---

## 1. Shared primitives

```ts
// core/errors — no exceptions for expected failures.
export type Result<T, E = AppError> =
  | { ok: true;  value: T }
  | { ok: false; error: E };

export type AppErrorCode =
  | 'not_found' | 'validation' | 'conflict' | 'permission_denied'
  | 'storage_full' | 'crypto_failure' | 'consent_denied'
  | 'provider_unavailable' | 'unknown';

export interface AppError {
  code: AppErrorCode;
  message: string;          // developer-facing; never shown raw to the user
  userMessage?: string;      // translated, safe to display
  cause?: unknown;
  context?: Record<string, string | number | boolean>;  // never PII
}
```

Expected failures (a duplicate check-in, a denied consent, a missing record) are `Result` values.
Exceptions are reserved for programmer errors and unrecoverable states. This distinction is enforced
in review: a `try/catch` around a domain call usually means the contract is wrong.

```ts
// core/id, core/time — injected, never called directly from logic.
export interface IdGenerator { next(): string; }        // UUIDv7
export interface Clock {
  now(): Date;
  today(timezone: string): LocalDate;                   // 'YYYY-MM-DD'
}
export type LocalDate = string & { readonly __brand: 'LocalDate' };
export type Iso8601   = string & { readonly __brand: 'Iso8601' };
export type EntityId  = string & { readonly __brand: 'EntityId' };
```

Branded types cost nothing at runtime and make it a compile error to pass an ISO timestamp where a
local date belongs — a mistake that would otherwise silently break streaks for every user not on
UTC.

---

## 2. Repository contracts

Repositories are the **only** way to reach the database (ARCHITECTURE §3.1). They speak in domain
entities and know nothing about screens.

```ts
// domain/repositories/base.ts
export interface Repository<T, TCreate, TUpdate> {
  findById(id: EntityId): Promise<T | null>;
  create(input: TCreate): Promise<Result<T>>;
  update(id: EntityId, patch: TUpdate): Promise<Result<T>>;
  softDelete(id: EntityId): Promise<Result<void>>;
}

// Every repository method runs inside the ambient transaction if one is open.
export interface TransactionScope {
  run<T>(work: (tx: Transaction) => Promise<T>): Promise<T>;
}
```

Rules for all repositories:

1. Reads exclude soft-deleted rows unless the method name says otherwise (`findByIdIncludingDeleted`).
2. Every write sets `updated_at`, `device_id`, and increments `revision`. No caller ever passes these.
3. No repository publishes events. Use cases do — repositories persist, they do not orchestrate.
4. No repository returns a database row. Mappers convert at the boundary.

### Representative interfaces

```ts
export interface HabitRepository extends Repository<Habit, CreateHabitInput, UpdateHabitInput> {
  listActive(userId: EntityId): Promise<Habit[]>;
  listDueOn(userId: EntityId, date: LocalDate): Promise<Habit[]>;
  updateStreakState(id: EntityId, state: StreakState): Promise<Result<void>>;
}

export interface HabitEntryRepository {
  findByHabitAndDate(habitId: EntityId, date: LocalDate): Promise<HabitEntry | null>;
  listForHabit(habitId: EntityId, range: DateRange): Promise<HabitEntry[]>;
  append(entry: NewHabitEntry): Promise<Result<HabitEntry>>;
  markDeleted(id: EntityId): Promise<Result<void>>;   // append-only: no hard delete
}

export interface XpLedgerRepository {
  /** Returns { ok:true } with the existing entry if source event was already applied. */
  appendIdempotent(entry: NewXpEntry): Promise<Result<XpEntry>>;
  sumLifetime(userId: EntityId): Promise<number>;
  sumSpendable(userId: EntityId): Promise<number>;
  listSince(userId: EntityId, since: Iso8601): Promise<XpEntry[]>;
}

export interface TimelineRepository {
  /** No-ops if an entry for sourceEventId already exists. */
  appendIdempotent(event: NewTimelineEvent): Promise<Result<void>>;
  page(userId: EntityId, opts: { before?: Iso8601; limit: number; kinds?: TimelineKind[] })
    : Promise<TimelineEvent[]>;
}
```

`appendIdempotent` appears twice on purpose. At-least-once event delivery means every durable
subscriber needs an idempotent write, and naming it in the interface makes that contract impossible
to forget at the call site.

---

## 3. Domain events

Events are **past-tense facts**. They never instruct. Every event is a discriminated union member so
`switch` statements are exhaustively checked by the compiler.

```ts
export interface DomainEventBase {
  id: EntityId;             // = event_outbox.id; the idempotency key for all subscribers
  occurredAt: Iso8601;
  userId: EntityId;
  deviceId: string;
}

export type DomainEvent =
  | HabitCompleted | HabitUncompleted | HabitStreakReached
  | HabitCreated | HabitArchived
  | GoalCreated | GoalMilestoneReached | GoalCompleted | GoalArchived
  | TaskCompleted | TaskUncompleted
  | XpAwarded | LevelReached
  | ProfileUpdated
  // phase 2+
  | AchievementUnlocked | RewardRedeemed
  | SleepLogged | WorkoutLogged | MeasurementLogged | PhotoCaptured
  | VoiceSessionAnalyzed;

export interface HabitCompleted extends DomainEventBase {
  type: 'habit.completed';
  habitId: EntityId;
  entryId: EntityId;
  localDate: LocalDate;
  difficulty: 1 | 2 | 3;
  streakAfter: number;
}

export interface XpAwarded extends DomainEventBase {
  type: 'xp.awarded';
  amount: number;
  reason: XpReason;
  sourceEventId: EntityId;   // the event that caused it
  lifetimeAfter: number;
}

export interface LevelReached extends DomainEventBase {
  type: 'progression.level_reached';
  level: number;
  lifetimeXp: number;
}
```

### Event bus contract

```ts
export interface EventBus {
  /** Enqueues into the outbox. MUST be called inside the same transaction as the write. */
  publish(event: DomainEvent, tx: Transaction): Promise<void>;

  /** Durable: redelivered until acknowledged. Handler MUST be idempotent on event.id. */
  subscribe<T extends DomainEvent['type']>(
    type: T | T[],
    handler: EventHandler<Extract<DomainEvent, { type: T }>>,
    opts: { name: string; durable: true },
  ): Unsubscribe;

  /** Ephemeral: UI refresh only. Dropped on restart. Never used for state changes. */
  subscribeEphemeral<T extends DomainEvent['type']>(
    type: T | T[],
    handler: EventHandler<Extract<DomainEvent, { type: T }>>,
  ): Unsubscribe;
}

export type EventHandler<E> = (event: E) => Promise<Result<void>>;
```

Two subscription kinds, because they have different failure semantics. A durable handler that fails
retries with backoff and blocks nothing; an ephemeral handler that fails just misses a UI refresh.
Using an ephemeral subscription to mutate state is a defect — it silently loses writes across
restarts.

### Who publishes what, and who listens

| Event | Published by | Durable subscribers |
|---|---|---|
| `habit.completed` | habits | progression (XP), progression (achievements), timeline |
| `habit.uncompleted` | habits | progression (XP reversal), timeline |
| `habit.streak_reached` | habits | progression (bonus XP), timeline |
| `goal.completed` | goals | progression (XP), timeline |
| `task.completed` | tasks | progression (XP), timeline |
| `xp.awarded` | progression | timeline |
| `progression.level_reached` | progression | timeline, UI celebration (ephemeral) |
| `photo.captured` *(phase 2)* | health | appearance (comparison index), timeline |

The habits feature appears only in the left column, and progression only in the right. Neither
imports the other — which is the whole point.

---

## 4. Feature module contracts

Each feature exposes exactly one public surface via `index.ts`. Nothing else is importable from
outside (enforced by lint).

```ts
export interface HabitsModule {
  readonly useCases: {
    createHabit(input: CreateHabitInput): Promise<Result<Habit>>;
    updateHabit(id: EntityId, patch: UpdateHabitInput): Promise<Result<Habit>>;
    archiveHabit(id: EntityId): Promise<Result<void>>;
    completeHabit(id: EntityId, date?: LocalDate): Promise<Result<HabitCompletionResult>>;
    undoCompletion(id: EntityId, date: LocalDate): Promise<Result<void>>;
    getHabitsDueToday(): Promise<Habit[]>;
    getHabitHistory(id: EntityId, range: DateRange): Promise<HabitEntry[]>;
  };
  readonly queries: { … };   // read models for the UI, no side effects
}

export interface ProgressionModule {
  readonly useCases: {
    getProgression(): Promise<ProgressionSnapshot>;
    recomputeFromLedger(): Promise<Result<ProgressionSnapshot>>;  // cache repair
    redeemReward(rewardId: EntityId): Promise<Result<RewardRedemption>>;
  };
  /** Registers this module's durable event subscriptions. Called once at startup. */
  readonly register: (bus: EventBus) => void;
}
```

`recomputeFromLedger` is public deliberately. Any cached aggregate needs a user-reachable repair
path, and a repair path that only exists in tests is a repair path that does not exist.

---

## 5. Core service contracts

```ts
export interface CryptoService {
  ensureMasterKey(): Promise<Result<void>>;              // first run or unlock
  encryptBytes(plain: Uint8Array): Promise<Result<EncryptedBlob>>;
  decryptBytes(blob: EncryptedBlob): Promise<Result<Uint8Array>>;
  deriveBackupKey(passphrase: string, params: KdfParams): Promise<Result<Uint8Array>>;
  rotateMasterKey(next: Uint8Array): Promise<Result<void>>;
}

export interface FileStore {
  write(kind: AttachmentKind, bytes: Uint8Array, meta: FileMeta): Promise<Result<StoredFile>>;
  read(relativePath: string): Promise<Result<Uint8Array>>;
  shred(relativePath: string): Promise<Result<void>>;    // overwrite, then unlink
  usage(): Promise<StorageUsage>;
  scanOrphans(): Promise<OrphanReport>;                   // runs at startup
}

export interface BackupService {
  export(opts: { passphrase: string; destination: string }): Promise<Result<BackupManifest>>;
  inspect(source: string): Promise<Result<BackupManifest>>;      // before restoring
  restore(opts: { source: string; passphrase: string }): Promise<Result<RestoreReport>>;
}

export interface AppLockService {
  isEnrolled(): Promise<boolean>;
  authenticate(reason: string): Promise<Result<void>>;
  lock(): void;
  onLockStateChange(cb: (locked: boolean) => void): Unsubscribe;
}
```

`inspect` before `restore` is a deliberate two-step: the user sees what a backup contains (date,
counts, schema version) before it is allowed to touch live data.

---

## 6. AI contracts

The single chokepoint through which every model call passes (ARCHITECTURE §5). Its shape is what
makes the privacy requirements P-12 … P-15 enforceable rather than aspirational.

```ts
export type PrivacyClass =
  | 'derived_metrics'   // aggregates, counts, streaks
  | 'text_personal'     // goal text, notes, journals
  | 'image_body'        // progress photos, skin, physique
  | 'audio_voice';      // voice recordings

export type AiTask =
  | 'summarize_progress' | 'detect_patterns' | 'coach_reply'
  | 'analyze_photo_change' | 'analyze_skin' | 'analyze_style'
  | 'transcribe_audio'  | 'analyze_speech_delivery';

export type ProcessingLocation =
  | { kind: 'on_device' }
  | { kind: 'self_hosted'; host: string }
  | { kind: 'external';    provider: string; model: string };

export interface AiRequest<TIn> {
  task: AiTask;
  privacyClass: PrivacyClass;
  input: TIn;
  /** Hard ceiling. The router MUST NOT exceed it even if a provider is available. */
  maxLocation: 'on_device' | 'self_hosted' | 'external';
}

export interface AiResult<TOut> {
  output: TOut;
  processedAt: ProcessingLocation;   // NOT optional — P-13 depends on it
  model: string;
  latencyMs: number;
  usage?: { inputTokens?: number; outputTokens?: number; cost?: number };
  confidence?: number;
}

export interface AiService {
  /** Denies with 'consent_denied' when the class is not permitted to leave the device. */
  run<TIn, TOut>(req: AiRequest<TIn>): Promise<Result<AiResult<TOut>>>;
  /** What is possible right now, given consent + provider availability. */
  capabilities(): Promise<AiCapabilityMap>;
  auditLog(range: DateRange): Promise<AiAuditEntry[]>;
}

export interface AiProvider {
  readonly id: string;
  readonly location: ProcessingLocation;
  supports(task: AiTask): boolean;
  isAvailable(): Promise<boolean>;
  run<TIn, TOut>(task: AiTask, input: TIn, signal: AbortSignal): Promise<Result<TOut>>;
}

export interface ConsentGate {
  isAllowed(cls: PrivacyClass, dest: ProcessingLocation['kind']): Promise<boolean>;
  grant(cls: PrivacyClass, dest: ProcessingLocation['kind']): Promise<void>;
  revoke(cls: PrivacyClass, dest: ProcessingLocation['kind']): Promise<void>;
  matrix(): Promise<ConsentMatrix>;   // rendered directly in settings
}

export interface AiAuditEntry {
  id: EntityId;
  occurredAt: Iso8601;
  task: AiTask;
  privacyClass: PrivacyClass;
  destination: ProcessingLocation;
  inputSummary: string;    // "1 image, 2.1 MB" — a description, never the content
  outcome: 'success' | 'denied' | 'failed';
}
```

Four contract details worth stating explicitly, because each one closes a specific hole:

- **`processedAt` is required on every result.** A UI cannot forget to show where processing happened
  if the type will not compile without it.
- **`maxLocation` is a ceiling the router may not exceed**, so a feature can request "on-device only"
  regardless of what the user has consented to globally.
- **`inputSummary` describes, never contains.** The audit log must be safe to display and safe to
  export; putting content in it would recreate the problem it exists to solve.
- **Consent defaults to denied for every `(class, destination)` pair.** A new privacy class added
  later is automatically private until someone deliberately allows it — the safe direction for a
  default to fail.

---

## 7. Sync contracts (Phase 5 — shape reserved now)

Sketched so Phase 1 code does not accidentally preclude it.

```ts
export interface SyncService {
  status(): Promise<SyncStatus>;
  pushPending(): Promise<Result<PushReport>>;
  pull(): Promise<Result<PullReport>>;
  pairDevice(invite: DeviceInvite): Promise<Result<PairedDevice>>;
  unpair(deviceId: string): Promise<Result<void>>;
}

/** Relay stores opaque ciphertext. Plaintext never crosses this boundary. */
export interface SyncTransport {
  upload(batch: EncryptedBatch): Promise<Result<void>>;
  download(since: HlcTimestamp): Promise<Result<EncryptedBatch[]>>;
}
```

`SyncTransport` accepting only `EncryptedBatch` is the type-level statement of P-21: there is no
signature through which plaintext could reach a server, so a zero-knowledge relay is a property of
the interface rather than a promise in a document.

---

## 8. Contract stability rules

1. A feature's `index.ts` is its contract. Changing it is a deliberate act and requires updating this
   document in the same commit.
2. Events are append-only: add new event types, never repurpose an existing one. Old events are
   persisted in the outbox and will be replayed by whatever code exists when they are.
3. Event payloads may gain optional fields; required fields may never be removed or retyped.
4. Every interface is designed to be implementable by a test double without a device.
5. `Result` at every boundary that can fail for an expected reason. Any exception crossing a module
   boundary is a bug.
