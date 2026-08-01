# src/ — application source

**Empty by design.** Implementation has not been authorised — see
[`../docs/PRE_IMPLEMENTATION_REVIEW.md`](../docs/PRE_IMPLEMENTATION_REVIEW.md) §7.

The structure below is created in Sprint 1 (see [`../docs/MVP_PLAN.md`](../docs/MVP_PLAN.md)), and is
specified in [`../docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md) §3.

```
src/
├── app/          Expo Router routes — layout and wiring only, no logic
├── core/         db · crypto · events · storage · config · logging · errors · time · id
├── domain/       entities · values · rules · repository interfaces (imports nothing)
├── features/     vertical slices: profile · goals · habits · tasks · progression · timeline …
│                 each with data/ · application/ · ui/ · index.ts
├── services/     ai · media · backup · notification · sync
└── ui/           design system: tokens · primitives · layout · theming · i18n
```

Dependencies point inward only. The boundaries are enforced by lint rules
([`../docs/CODING_RULES.md`](../docs/CODING_RULES.md) §2), not by discipline — a violation fails CI.
