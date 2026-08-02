"""
src/or1_phase_test.py — regression test for OR-1 phases 1-4 (src/excava_chat.py).

Phase 1 (independent brainstorm), phase 2 (integration discussion), phase 3 (adversarial
re-review from scratch) and phase 4 (resolution discussion — the FINAL guideline) all hard-gate
on model-family diversity and must never fabricate a multi-agent result from one model. This
proves that gate, the phase-1 -> phase-2 -> phase-3 -> phase-4 handoffs, and phases 2/3/4's
no-cross-talk isolation — all without live provider keys, by faking src.excava_engines and
src.excava_agents. Free, stdlib, no network. Run:
python -m src.or1_phase_test
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
    print("OR-1 phase 1/2/3 (src/excava_chat.py) regression test")

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

            # (g) phase 3 refuses to run with no phase-2 artifact -- delete it first and confirm
            # the gate fires (separate temp dir would also work, but this proves the ok-flag path).
            (chat.DATA / "excava" / "artifacts" / "or1-phase2-skill.json").unlink()
            fe5 = FakeEngines(TWO_FAMILIES, tag="gate3")
            chat.engines = fe5
            r3_missing = chat.or1_phase3("skill")
            check("phase3 blocks with no phase-2 artifact", r3_missing["ok"] is False, str(r3_missing))
            check("phase3 makes no engine calls when phase2 is missing", len(fe5.calls) == 0, str(fe5.calls))
            chat._write_or1_artifact(r2b)   # restore for the success-path checks below

            # (h) phase 3 also hard-gates on family diversity, independent of the phase-2 prereq.
            fe6 = FakeEngines(ONE_FAMILY)
            chat.engines = fe6
            r3_fam = chat.or1_phase3("skill")
            check("phase3 blocks below min_families", r3_fam["ok"] is False, str(r3_fam))
            check("phase3 gate makes no engine calls below min_families", len(fe6.calls) == 0, str(fe6.calls))

            # (i) phase 3 succeeds once phase 2's artifact exists, one isolated call per cast
            # member, every prompt seeded with ALL phase-2 integration drafts.
            fe7 = FakeEngines(TWO_FAMILIES, tag="p3")
            chat.engines = fe7
            r3 = chat.or1_phase3("skill")
            check("phase3 succeeds once phase2 artifact exists", r3["ok"] is True, str(r3))
            check("phase3 makes exactly one call per cast member", len(fe7.calls) == len(CAST),
                  f"{len(fe7.calls)} calls vs {len(CAST)} cast")
            check("phase3 families_used has >= 2 distinct families", len(r3["families_used"]) >= 2,
                  str(r3["families_used"]))
            seeded_all3 = all(all(d["text"] in c["prompt"] for d in r2b["integration_drafts"] if d["ok"])
                              for c in fe7.calls)
            check("every phase3 prompt is seeded with every phase2 integration draft", seeded_all3)

            # (j) phase 3 calls are ALSO isolated from each other (a second solo pass, same as
            # phase 2). Phase-2 markers are SUPPOSED to appear (that's the review corpus); only
            # p3-markers from a different call would indicate real cross-agent leakage.
            leaked3 = [c for i, c in enumerate(fe7.calls)
                       for j, other in enumerate(fe7.calls) if i != j
                       and f"unique-marker-p3{j + 1}" in c["prompt"]]
            check("phase3 prompts carry no cross-agent leakage", not leaked3, str(leaked3))

            ref3 = chat._write_or1_artifact(r3)
            check("phase3 markdown artifact written", (chat.DATA / ref3[len("data/"):]).exists(), ref3)
            check("phase3 JSON sidecar written",
                  (chat.DATA / "excava" / "artifacts" / "or1-phase3-skill.json").exists())

            # (k) phase 4 refuses to run with no phase-3 artifact -- delete it first and confirm
            # the gate fires.
            (chat.DATA / "excava" / "artifacts" / "or1-phase3-skill.json").unlink()
            fe8 = FakeEngines(TWO_FAMILIES, tag="gate4a")
            chat.engines = fe8
            r4_missing3 = chat.or1_phase4("skill")
            check("phase4 blocks with no phase-3 artifact", r4_missing3["ok"] is False, str(r4_missing3))
            check("phase4 makes no engine calls when phase3 is missing", len(fe8.calls) == 0, str(fe8.calls))
            chat._write_or1_artifact(r3)   # restore phase 3 for the remaining checks

            # (l) phase 4 also refuses to run with no phase-2 artifact, even once phase 3 exists
            # (phase 4 needs the integrated set phase 3 reviewed, not just phase 3's own output).
            (chat.DATA / "excava" / "artifacts" / "or1-phase2-skill.json").unlink()
            fe9 = FakeEngines(TWO_FAMILIES, tag="gate4b")
            chat.engines = fe9
            r4_missing2 = chat.or1_phase4("skill")
            check("phase4 blocks with no phase-2 artifact", r4_missing2["ok"] is False, str(r4_missing2))
            check("phase4 makes no engine calls when phase2 is missing", len(fe9.calls) == 0, str(fe9.calls))
            chat._write_or1_artifact(r2b)   # restore phase 2 for the success-path checks below

            # (m) phase 4 also hard-gates on family diversity, independent of the phase-2/3 prereqs.
            fe10 = FakeEngines(ONE_FAMILY)
            chat.engines = fe10
            r4_fam = chat.or1_phase4("skill")
            check("phase4 blocks below min_families", r4_fam["ok"] is False, str(r4_fam))
            check("phase4 gate makes no engine calls below min_families", len(fe10.calls) == 0, str(fe10.calls))

            # (n) phase 4 succeeds once phase 2 and phase 3 artifacts both exist, one isolated
            # call per cast member, every prompt seeded with BOTH phase-2 integration drafts and
            # phase-3 weakness lists.
            fe11 = FakeEngines(TWO_FAMILIES, tag="p4")
            chat.engines = fe11
            r4 = chat.or1_phase4("skill")
            check("phase4 succeeds once phase2+phase3 artifacts exist", r4["ok"] is True, str(r4))
            check("phase4 makes exactly one call per cast member", len(fe11.calls) == len(CAST),
                  f"{len(fe11.calls)} calls vs {len(CAST)} cast")
            check("phase4 families_used has >= 2 distinct families", len(r4["families_used"]) >= 2,
                  str(r4["families_used"]))
            seeded_integ = all(all(d["text"] in c["prompt"] for d in r2b["integration_drafts"] if d["ok"])
                               for c in fe11.calls)
            seeded_weak = all(all(d["text"] in c["prompt"] for d in r3["adversarial_drafts"] if d["ok"])
                              for c in fe11.calls)
            check("every phase4 prompt is seeded with every phase2 integration draft", seeded_integ)
            check("every phase4 prompt is seeded with every phase3 weakness list", seeded_weak)

            # (o) phase 4 calls are ALSO isolated from each other (a final solo pass, same shape
            # as phases 2/3). Phase-2/3 markers are SUPPOSED to appear (that's the resolution
            # input); only p4-markers from a different call would indicate real cross-agent leakage.
            leaked4 = [c for i, c in enumerate(fe11.calls)
                       for j, other in enumerate(fe11.calls) if i != j
                       and f"unique-marker-p4{j + 1}" in c["prompt"]]
            check("phase4 prompts carry no cross-agent leakage", not leaked4, str(leaked4))

            ref4 = chat._write_or1_artifact(r4)
            check("phase4 markdown artifact written", (chat.DATA / ref4[len("data/"):]).exists(), ref4)
            check("phase4 JSON sidecar written",
                  (chat.DATA / "excava" / "artifacts" / "or1-phase4-skill.json").exists())
    finally:
        chat.DATA, chat.engines, chat.agents, chat.time.sleep = orig_data, orig_engines, orig_agents, orig_sleep

    print(f"\n{len(FAILS)} failure(s)" if FAILS else "\nall checks passed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
