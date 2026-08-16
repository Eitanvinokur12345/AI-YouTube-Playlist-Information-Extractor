"""
src/task_focus.py — ONE shared implementation of "which part of my domain is this task about?"

WHY THIS EXISTS (2026-08-16 owner audit)
----------------------------------------
Every REAL_TOOL script used to take a DEPARTMENT and nothing else, so it could not do the task in
front of it — it re-ran one dept-wide script and whatever was claimed got stamped done. Measured
consequence: 797 of 892 surviving completions (89%) were closed by output BYTE-IDENTICAL to an
earlier completion; 153 different `improve` tasks all closed on the same self-check line.

src/self_check.py was converted first and proved the pattern. This module is that pattern extracted
so the remaining tools reuse it instead of growing eight divergent copies of a tokenizer and a
stop-list (P-Ponytail: reuse before building).

THE CONTRACT EVERY CONVERTED TOOL FOLLOWS
-----------------------------------------
1. The FULL scan always runs and always writes its full report file. A task may steer what is
   REPORTED, never what is RECORDED — otherwise a focused run corrupts the data into a partial
   result, which would be a worse bug than the one being fixed.
2. When the task matches nothing in the tool's domain, say UNFOCUSED honestly. A whole-suite run
   is NOT an answer to a task the tool cannot address, and pretending otherwise is precisely the
   theatre this work exists to end.
3. The focused line leads with the FINDINGS and carries the resolved focus in [brackets].
   excava_agents._evidence_seen() strips bracketed text before hashing, so the annotation cannot
   act as a nonce that lets two differently-worded tasks about the same finding both count as
   distinct work.
"""
from __future__ import annotations

import argparse
import re

# Words that carry no domain signal. Kept deliberately small: over-stripping makes everything match
# everything, which would hand back the "any task closes any run" bug in a new costume.
STOP = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "is", "are", "be", "it",
        "this", "that", "with", "at", "by", "from", "up", "all", "any", "no", "not", "every",
        "improve", "improvement", "fix", "check", "task", "excava", "run", "make", "new", "need",
        "should", "must", "our", "we", "its", "into", "over", "more", "less", "than", "then"}


def tokens(text: str) -> set[str]:
    """Domain-bearing words of a phrase, lowercased, 3+ chars, stop-words removed."""
    return {w for w in re.findall(r"[a-z][a-z0-9\-]{2,}", (text or "").lower()) if w not in STOP}


def select(task_text: str, candidates: dict[str, str]) -> tuple[list[str], str]:
    """Pick the candidate key(s) this task is about.

    `candidates` maps a key (the thing the tool can report on — a rule name, a source, a finding
    kind) to the text that key should be matched against. Returns (keys, how_it_was_chosen).
    Empty keys means UNFOCUSED — the caller must report that honestly rather than fall back to a
    whole-suite line.
    """
    if not (task_text or "").strip():
        return list(candidates), "no task given — full report"
    want = tokens(task_text)
    if not want:
        return list(candidates), "task had no domain words — full report"
    scored = []
    for key, text in candidates.items():
        overlap = want & (tokens(key) | tokens(text))
        if overlap:
            scored.append((len(overlap), key, overlap))
    if not scored:
        return [], "UNFOCUSED"
    best = max(s[0] for s in scored)
    top = [s for s in scored if s[0] == best][:4]
    return [s[1] for s in top], "/".join(sorted(top[0][2]))


def line(tool: str, task_text: str, candidates: dict[str, str], full_summary: str,
         synonyms: dict[str, str] | None = None) -> str:
    """The one output line a converted tool prints.

    `candidates` maps key -> the EVIDENCE to report for that key (e.g. "3 issue(s)", "clean").
    `synonyms` optionally maps key -> extra words to MATCH on, for when the evidence text alone is
    too thin to match a task against (a clean rule reporting "0 issues" shares no words with
    "aria labels and keyboard focus"). Matching uses key + synonyms + evidence; only the evidence
    is reported. `full_summary` is the tool's normal whole-run line, always appended so the full
    picture is never lost.
    """
    syn = synonyms or {}
    keys, how = select(task_text, {k: f"{syn.get(k, '')} {v}".strip() for k, v in candidates.items()})
    if not task_text.strip():
        return full_summary
    if not keys:
        return (f"{tool}[UNFOCUSED]: nothing in this tool's domain matches the task "
                f"(can report on: {', '.join(sorted(candidates)[:8]) or 'nothing'}) — "
                f"this task needs a different tool, not another whole-run. || {full_summary}")
    found = " | ".join(f"{k}: {candidates[k]}" for k in keys)
    return f"{tool}[{how}]: {found} || {full_summary}"


def add_arg(ap: argparse.ArgumentParser) -> argparse.ArgumentParser:
    ap.add_argument("--task", default="", help="task title/detail to focus this run's REPORT on")
    return ap


def arg() -> str:
    """--task for tools that have no argparse of their own, without disturbing their other flags."""
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--task", default="")
    return ap.parse_known_args()[0].task
