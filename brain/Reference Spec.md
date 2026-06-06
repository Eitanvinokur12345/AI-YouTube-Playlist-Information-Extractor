---
tags: [reference, spec]
aliases: [Reference Spec, REFERENCE_SPEC, Original Spec]
---

# Reference Spec

The owner's original blueprint, preserved **verbatim** in `docs/REFERENCE_SPEC.md`. It is the
authoritative quality checklist the system returns to every run (see [[Reference Self-Check]]).

## Three parts
- **Part A — the original "YouTube Skills Tracker — System Prompt"**, verbatim: 7 tabs
  (1 Skills Library, 2 Models Ranking with 🥇🥈🥉 podium, 3 Skills Improvement, 4 Tips &
  Commands, 5 News daily/weekly/monthly, 6 Connectors + connect instructions, 7 Trend
  Recognition), the RUN REPORT box, the SELF-IMPROVEMENT SYSTEM, and the MCP tool requests.
- **Part B — cloud-architecture mapping.** The original describes a *local* 48-hour routine;
  Part B maps it to the cloud build with a translation table + 6 deltas:
  1. **[[Skills vs Tools]]** split (techniques vs products).
  2. Trend Recognition → **[[Dynamic Tabs]]**.
  3. **Extract everything the video AND its surroundings offer** (beyond 8000 chars → 80k +
     description + links + stats + comments). See [[Pipeline - Analyze]].
  4. **Batch speed** — ~50–100 videos / 48h ([[Cadence]] throughput target).
  5. **[[Three-Agent Review]]** every deep pass.
  6. **[[Stars and Freezing]]**.
- **Part C — the 50 self-check questions**, verbatim, each annotated with its cloud
  verification + the data file that proves it. Drives [[Reference Self-Check]].

## Why it's sacred
This is the contract. The self-check exists so the build can evolve without ever drifting away
from what the owner actually asked for. Re-read it on every deep pass (IMPROVE.md Step 0 + 7c).
