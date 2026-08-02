"""
src/or1_phase_test.py — regression test for OR-1 phases 1 and 2 (src/excava_chat.py).

Phase 1 (independent brainstorm) and phase 2 (integration discussion) both hard-gate on
model-family diversity and must never fabricate a multi-agent result from one model. This
proves that gate, the phase-1 -> phase-2 handoff, and phase 2's no-cross-talk isolation — all
without live provider keys, by faking src.excava_engines and src.excava_agents. Free, stdlib,
no network. Run:  python -m src.or1_phase_test
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from src import excava_chat as chat

FAILS: list = []


def check(name: str, cond: bool, detail: str = "") -> None:
    print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else ' — ' + detail}")
    if not cond:
        FAILS.append(name)


CAST = [
    {"id": "improve-lead", "name": "Ratchet", "department": "improve", "role": "lead", "persona": "lead persona"},
    {"id": "improve-w1", "name": "Sprocket", "department": "improve", "role": "doer", "persona": "doer persona"},
    {"id": "improve-checker", "name": "Gauge", "department": "improve", "role": "checker", "persona": "checker persona"},
    {"id": "improve-improver", "name": "Overhaul", "department": "improve", "role": "improver", "persona": "improver persona"},
]

TWO_FAMILIES = [
    {"family": "GLM", "status": "live", "engine": "glm", "core": True},
    {"family": "DeepSeek", "status": "live", "engine": "deepseek", "core": True},
    {"family": "GPT", "status": "needs-key", "engine": "gh-models", "core": False},
]
ONE_FAMILY = [
    {"family": "GPT", "status": "live", "engine": "gh-models", "core": False},
]
HEALTHY_ENGINES = [{"name": "glm", "model": "glm-5.2"}, {"name": "deepseek", "model": "deepseek-v4"},
                   {"name": "gh-models", "model": "gpt-4o-mini"}]


class FakeAgents:
    @staticmethod
    def load_registry():
        return {"agents": CAST}


class FakeEngines:
    def __init__(self, roster, tag="p"):
        self.roster = roster
        self.tag = tag
        self.calls = []

    def families(self):
        return self.roster

    def healthy(self):
        return HEALTHY_ENGINES

    def complete(self, prompt, engine=None, dept="", difficulty="normal", max_tokens=700):
        self.calls.append({"prompt": prompt, "engine": engine})
        n = len(self.calls)
        return {"ok": True, "text": f"draft-text-{n} unique-marker-{self.tag}{n}",
                "engine": (engine or {}).get("name", "fake"), "model": "fake-model", "ms": 1}


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print("OR-1 phase 1/2 (src/excava_chat.py) regression test")

    orig_data, orig_engines, orig_agents, orig_sleep = chat.DATA, chat.engines, chat.agents, chat.time.sleep
    chat.time.sleep = lambda *_a, **_k: None
    chat.agents = FakeAgents()

    try:
        with tempfile.TemporaryDirectory() as td:
            chat.DATA = Path(td)

            # (a) phase 1 refuses to run below min_families, and makes zero engine calls doing so.
            fe1 = FakeEngines(ONE_FAMILY)
            chat.engines = fe1
            r = chat.or1_phase1("skill")
            check("phase1 blocks below min_families", r["ok"] is False, str(r))
            check("phase1 gate makes no engine calls", len(fe1.calls) == 0, str(fe1.calls))
            check("phase1 blocked reason names the shortfall",
                  "1 live model family" in r.get("reason", ""), r.get("reason"))

            # (b) phase 2 refuses to run with no phase-1 artifact on disk yet.
            fe2 = FakeEngines(TWO_FAMILIES)
            chat.engines = fe2
            r2 = chat.or1_phase2("skill")
            check("phase2 blocks with no phase-1 artifact", r2["ok"] is False, str(r2))
            check("phase2 makes no engine calls when phase1 is missing", len(fe2.calls) == 0, str(fe2.calls))

            # (c) phase 1 succeeds with 2 live families, one isolated call per cast member, and
            # writes both a JSON sidecar and a markdown artifact phase 2 can read back.
            fe3 = FakeEngines(TWO_FAMILIES, tag="p1")
            chat.engines = fe3
            r1 = chat.or1_phase1("skill")
            ref1 = chat._write_or1_artifact(r1)
            check("phase1 succeeds with 2 live families", r1["ok"] is True, str(r1))
            check("phase1 makes exactly one call per cast member", len(fe3.calls) == len(CAST),
                  f"{len(fe3.calls)} calls vs {len(CAST)} cast")
            check("phase1 families_used has >= 2 distinct families", len(r1["families_used"]) >= 2,
                  str(r1["families_used"]))
            check("phase1 markdown artifact written", (chat.DATA / ref1[len("data/"):]).exists(), ref1)
            check("phase1 JSON sidecar written",
                  (chat.DATA / "excava" / "artifacts" / "or1-phase1-skill.json").exists())

            # (d) phase 1 calls are genuinely isolated: no cast member's prompt contains another
            # member's response marker (no shared history leaking phase-1 draft into phase-1 draft).
            leaked = [c for i, c in enumerate(fe3.calls)
                      for j, other in enumerate(fe3.calls) if i != j
                      and f"unique-marker-p1{j + 1}" in c["prompt"]]
            check("phase1 prompts carry no cross-agent leakage", not leaked, str(leaked))

            # (e) phase 2 succeeds once phase 1's artifact exists, and every phase-2 prompt is
            # seeded with ALL phase-1 drafts (the actual integration input), independent of order.
            fe4 = FakeEngines(TWO_FAMILIES, tag="p2")
            chat.engines = fe4
            r2b = chat.or1_phase2("skill")
            check("phase2 succeeds once phase1 artifact exists", r2b["ok"] is True, str(r2b))
            check("phase2 makes exactly one call per cast member", len(fe4.calls) == len(CAST),
                  f"{len(fe4.calls)} calls vs {len(CAST)} cast")
            seeded_all = all(all(d["text"] in c["prompt"] for d in r1["drafts"] if d["ok"])
                             for c in fe4.calls)
            check("every phase2 prompt is seeded with every phase1 draft", seeded_all)

            # (f) phase 2 calls are ALSO isolated from each other (no phase-2 response leaking
            # into a later phase-2 prompt — phase 2 is a second solo pass, not a debate). Phase-1
            # markers are SUPPOSED to appear (that's the integration corpus); only p2-markers
            # from a different call would indicate real cross-agent leakage.
            leaked2 = [c for i, c in enumerate(fe4.calls)
                       for j, other in enumerate(fe4.calls) if i != j
                       and f"unique-marker-p2{j + 1}" in c["prompt"]]
            check("phase2 prompts carry no cross-agent leakage", not leaked2, str(leaked2))

            ref2 = chat._write_or1_artifact(r2b)
            check("phase2 markdown artifact written", (chat.DATA / ref2[len("data/"):]).exists(), ref2)
    finally:
        chat.DATA, chat.engines, chat.agents, chat.time.sleep = orig_data, orig_engines, orig_agents, orig_sleep

    print(f"\n{len(FAILS)} failure(s)" if FAILS else "\nall checks passed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
