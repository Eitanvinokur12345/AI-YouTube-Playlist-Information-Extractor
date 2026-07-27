# PROOF — what EXCAVA actually did (auto-generated every beat)

> **Do not trust these words — click the links.** Every link below goes to the RAW committed file or
> the GitHub Actions log. Those are GitHub's records, not numbers I generated. Verify anything yourself.
> Generated 2026-07-27T15:01:03.088664+00:00 · commit `b130f00d`

## Independently-checkable reality
- **Supervisor real_pct:** 100%  ({'real': 32, 'noop': 0, 'failed': 0, 'planned': 0, 'blocked': 8}) — [raw supervisor.json](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/excava/supervisor.json)
- **Movement (done trend):** [5014, 5014, 5076, 5081, 5127, 5132] — [raw movement.json](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/excava/movement.json)
- **Change since last beat:** designs -22
- **Live totals (recompute yourself):** 10374 elements · 2103 verified · 4246 with a real link · 956 designs · 15 creations

## SEE the agents talk (the real conversations)
- [Room transcripts by day](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/tree/main/data/excava/chats) — open a `.jsonl`, read what the agents actually said.
- [Decision artifacts they produced](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/tree/main/data/excava/artifacts)
- [Every CI beat + its full log](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/actions/workflows/excava_beat.yml) — GitHub's log of every run.

## What each department produced (latest) — click the evidence file to verify
| department | verdict | actual output | raw evidence (click) |
|---|---|---|---|
| **accessibility** | ? | Ran the accessibility scan. accessibility_scan: 0 issue(s) — clean | — |
| **analysis** | real | 1315 re-queued records are in data/_pending; the bulk-analyze lane (hourly, free pool) consumes them — lane is live. Done per criteria: queue owned +  | [`data/elements_index.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/elements_index.json) |
| **creators** | ? | Creators: 15 creations on record, 15 published — every one labeled 'Created by EXCAVA' with an independent test before first use (G-12). The daily cre | [`data/created_by_excava.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/created_by_excava.json) |
| **improve** | ? | Ran the self check. self-check: 40/50 (mechanical) | 0 new tasks | failing Qs: [1, 10, 12, 13, 14, 16, 20, 24, 45, 47] | [`data/self_check.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/self_check.json) |
| **memory** | real | Semantic index: 1504 vectors (model gemini-embedding-001); hub 7360 items → 5856 not yet embedded — embed lane (hourly CI) owns the catch-up. Pass com | [`data/brain_graph.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/brain_graph.json) |
| **mining** | ? | Ran the discovery agent. discovery: +2 new (of 146 sighted) → 808 queued; arxiv=78, gh-active=95, gh-new=40, hn-front=35, hn-new=88, huggingface-model | [`data/connectors.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/connectors.json) |
| **news** | ? | Ran the trend watch. trend_watch: 10 proposals (top score 10); queued 0 into self-improvement. | [`data/weekly_web_news.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/weekly_web_news.json) |
| **power** | ? | Ran the power scan.   - Together AI | Cloud inference platform hosting 200+ open-source models including Lla | — |
| **security** | real | Ran the security scan. security_scan: 0 secret leak(s), 0 injection-suspect records flagged. | [`data/security.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/security.json) |
| **visual** | real | Ran the collect designs. collect_designs: 956 designs (kept 956 / dropped 22 repo-only + 4 dead/parked + 49 non-design; +0 AI-product, +27 seeds, +48  | [`data/designs.json`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/designs.json) |
| **visualization** | ? | Ran the liveliness scan. liveliness_scan: 0 issue(s) — clean | — |
| **watch** | blocked | BLOCKED — watch needs video-analysis engine capacity (Gemini free quota is exhausted / needs an owner key). No fake work done; waiting on the owner. | [`data/_pending`](https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/tree/main/data/_pending) |

_Verdicts: **real** = ran a real tool / real assessment · **noop** = ran but produced nothing · **planned** = wrote a plan, did not execute · **failed**. The supervisor grades these against your intent charter + your 5-session history._
