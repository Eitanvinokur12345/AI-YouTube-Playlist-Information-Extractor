"""
src/excava_core.py — M2 class overhaul, CLASS 1 of 5: **Element / Package**.

THE PROBLEM THIS FIXES. `data/elements_index.json` is the one normalized view of all ~11k hub
items, but nothing owns *access* to it: 14 separate modules (`relate`, `deep_retrieve`,
`verify_elements`, `power_scan`, `excava_creators`, `discover_promote`, `build_hub_api`,
`github_meta_enrich`, `excava_backlog`, `excava_proof`, `excava_selfimprove`,
`excava_experiments`, `element_model` itself, plus `docs/dashboard.js`) each re-open the file
and re-interpret its fields by hand. Every one of them re-decides what "usable" means, what a
stub is, and how to reach a link. That duplication IS the 97-module fragmentation the END PLAN's
§2/§6 class overhaul exists to collapse — so `Element` is the correct first class: it is the
narrowest, most-depended-on shape in the system, and the other four (Tool, Room, Agent, Router)
all end up holding Elements.

WHAT THIS IS NOT. This is not a rewrite. `element_model.py` remains the sole builder of the
index and the sole write path (`set_field`); this module is a typed, tested *accessor* over its
output. Every existing consumer keeps working untouched — they are migrated one at a time, on
purpose (P5: an overhaul is never silently half-built). `activate.py` is the first migration.

LAW COMPLIANCE. Free + stdlib only, no new dependency (P1). Offline/online parity (P7): the
loader falls back to the public hub exactly like `activate.py` does, so this works outside the
repo. Read-only by default; the single write path delegates to `element_model.set_field`.

Run:
    python -m src.excava_core stats
    python -m src.excava_core find "github mcp" --usable
    python -m src.excava_core show connector:github-mcp
    python -m src.excava_core package my-stack --add tool:n8n --add connector:github-mcp
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
INDEX = DATA / "elements_index.json"
EXC = DATA / "excava"
PACKAGES = EXC / "packages.json"
REMOTE = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data"

# Status law (P3, mirrored from element_model): a low rating is NEVER a reason to discard.
# "niche" is a first-class usable status — a 1/10 may be perfect for exactly one task.
USABLE_STATUS = ("verified", "niche")


def _norm(s) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


class Element:
    """One hub item, in the unified shape. Wraps a record from elements_index.json.

    Read-only apart from `set()`, which routes to element_model's single write path.
    """

    __slots__ = ("_d",)

    def __init__(self, d: dict):
        self._d = d or {}

    # --- identity -------------------------------------------------------
    @property
    def id(self) -> str:
        return self._d.get("id", "")

    @property
    def type(self) -> str:
        return self._d.get("type", "")

    @property
    def name(self) -> str:
        return self._d.get("name", "")

    @property
    def what(self) -> str:
        return self._d.get("what", "")

    @property
    def category(self) -> str:
        return self._d.get("category", "")

    @property
    def body(self) -> str:
        """The element's own content (prompts/commands ARE their body)."""
        return self._d.get("body", "")

    @property
    def install(self) -> str:
        return self._d.get("install", "")

    @property
    def quality(self):
        return self._d.get("quality_score")

    @property
    def source_videos(self) -> list:
        return self._d.get("source_videos", []) or []

    @property
    def related_ids(self) -> list:
        return self._d.get("related", []) or []

    # --- links ----------------------------------------------------------
    @property
    def links(self) -> dict:
        return self._d.get("links", {}) or {}

    @property
    def github(self) -> str:
        return self.links.get("github", "")

    @property
    def website(self) -> str:
        return self.links.get("website", "")

    @property
    def best_link(self) -> str:
        """The one link most worth opening for this element."""
        return self.github or self.website or self.links.get("source_url", "")

    # --- status ---------------------------------------------------------
    @property
    def status(self) -> str:
        """verified | niche | unverified | dead (element_model's P3 status law)."""
        return (self._d.get("verified") or {}).get("status", "unverified")

    @property
    def is_stub(self) -> bool:
        return bool(self._d.get("stub"))

    @property
    def is_enriched(self) -> bool:
        return bool(self._d.get("enriched"))

    @property
    def is_dead(self) -> bool:
        return self.status == "dead"

    def is_usable(self) -> bool:
        """Can Eitan actually DO something with this today?

        Usable = it passed its checks (verified or niche) AND there is a real way in: a live
        link, an install line, or its own body. This is the single definition the 14 hand-rolled
        consumers each re-invented; every future class asks this method instead.
        """
        if self.status not in USABLE_STATUS:
            return False
        return bool(self.best_link or self.install or self.body)

    # --- actions --------------------------------------------------------
    def activation(self) -> dict:
        """The paste-ready setup recipe for this element.

        Delegates to `activate.plan()` rather than re-deriving the recipe (Ponytail: reuse the
        proven path). Imported lazily so `activate` can depend on this module without a cycle.
        """
        from src import activate as _activate

        raw = {
            "name": self.name,
            "slug": self.id.partition(":")[2],
            "github": self.github,
            "homepage": self.website,
            "quality_score": self.quality,
            "setup": self._d.get("setup") or ({"command": self.install} if self.install else {}),
        }
        return _activate.plan(raw, self.type)

    def set(self, field: str, value) -> bool:
        """The ONLY write path — delegates to element_model so the owning file stays truth."""
        from src import element_model

        return element_model.set_field(self.id, field, value)

    def related(self) -> list:
        idx = load()
        return [idx[r] for r in self.related_ids if r in idx]

    def to_dict(self) -> dict:
        return dict(self._d)

    def __repr__(self) -> str:
        return f"<Element {self.id} [{self.status}]{' stub' if self.is_stub else ''}>"


class Tool:
    """M2 class overhaul, CLASS 2 of 5 — wraps ONE OSS repo or MCP server as something CALLABLE.

    This is the class behind the END PLAN's highest-leverage lever (§8: "repos-as-running-tools").
    An Element says a tool EXISTS; a Tool says HOW TO RUN IT. The hub holds 1,463 connectors and
    thousands of repo-backed tools whose install line is buried in prose — until something parses
    that into a command, they are links, not tools (feature-inventory item 16: "OSS usable, not
    links").

    DETERMINISTIC BY DEFAULT (law: deterministic-first). Detection parses the install text with no
    network and no LLM, so an agent can ask "can I run this?" thousands of times for free. The
    registry lookup in `verify_connectors.resolve()` — which DOES hit npm/PyPI — is reused only
    when `resolve_online=True` is passed explicitly, so a network call is never a hidden cost.
    """

    # Ordered: the first pattern that matches decides the kind. Mirrors verify_connectors'
    # embedded-command regex (same proven expression) rather than inventing a second dialect.
    _CMD = re.compile(
        r"\b(npx\s+-?y?\s*[@\w\-/.]+"
        r"|npm\s+i(?:nstall)?\s+(?:-g\s+)?[@\w\-/.]+"
        r"|pip3?\s+install\s+[\w\-\[\]=.]+"
        r"|uvx\s+[\w\-]+"
        r"|uv\s+tool\s+run\s+[\w\-]+"
        r"|docker\s+run\s+[^\n]+)", re.I)

    __slots__ = ("element", "_kind", "_cmd")

    def __init__(self, element: "Element"):
        self.element = element
        self._kind, self._cmd = self._detect()

    # --- detection ------------------------------------------------------
    def _text(self) -> str:
        e = self.element
        return " ".join(str(x) for x in (e.install, e.what, e.body, e.links.get("source_url", "")))

    def _detect(self) -> tuple[str, str]:
        m = self._CMD.search(self._text())
        if m:
            cmd = " ".join(m.group(1).split())
            low = cmd.lower()
            kind = ("docker" if low.startswith("docker") else
                    "npm" if low.startswith(("npx", "npm")) else
                    "pip" if low.startswith("pip") else "pip")
            # An npx/uvx command on a connector is how an MCP server is launched.
            if self.element.type == "connector" or "-mcp" in low or "mcp-server" in low:
                kind = "mcp"
            return kind, cmd
        if self.element.type == "connector":
            return "mcp", ""            # a connector with no parsed command is still an MCP target
        if self.element.github:
            return "repo", ""           # clonable, but the run method is unknown until read
        if self.element.website:
            return "hosted", ""         # a signed-in product; nothing to install
        return "unknown", ""

    @property
    def kind(self) -> str:
        """mcp | npm | pip | docker | repo | hosted | unknown."""
        return self._kind

    @property
    def command(self) -> str:
        """The exact install/run line, verbatim from the source when one was stated."""
        return self._cmd

    @property
    def name(self) -> str:
        return self.element.name

    @property
    def id(self) -> str:
        return self.element.id

    def is_runnable(self) -> bool:
        """True when we hold a concrete command. `repo`/`hosted`/`unknown` are NOT runnable —
        saying otherwise would be exactly the display-over-reality failure law P4 forbids."""
        return bool(self._cmd) and self._kind in ("mcp", "npm", "pip", "docker")

    def resolve_online(self) -> bool:
        """Last resort: ask npm/PyPI whether a package matching this name exists.

        Reuses `verify_connectors.resolve()` (Ponytail — it is already proven and keyless)
        instead of a second registry client. Network call, so it is never implicit.
        """
        if self.is_runnable():
            return True
        try:
            from src import verify_connectors
            got = verify_connectors.resolve({"name": self.name, "install_or_source": self.element.install})
        except Exception:
            return False
        if not got:
            return False
        k, val = got
        self._cmd = val if k == "cmd" else (f"npx -y {val}" if k == "npx" else f"pip install {val}")
        self._kind = "mcp" if self.element.type == "connector" else ("npm" if k == "npx" else "pip")
        return True

    # --- calling it -----------------------------------------------------
    def mcp_config(self) -> dict | None:
        """Paste-ready `mcpServers` entry, or None when this is not an MCP server."""
        if self.kind != "mcp":
            return None
        parts = self._cmd.split() if self._cmd else []
        if parts and parts[0].lower() in ("npx", "uvx", "uv", "docker", "python"):
            command, args = parts[0], parts[1:]
        else:
            command, args = "npx", ["-y", "<package — see the repo README>"]
        slug = self.id.partition(":")[2] or _norm(self.name).replace(" ", "-")
        return {"mcpServers": {slug: {"command": command, "args": args}}}

    def invocation(self) -> dict:
        """How an agent would actually call this tool — the adapter spec the Router will read."""
        return {"id": self.id, "name": self.name, "kind": self.kind,
                "runnable": self.is_runnable(), "command": self._cmd or None,
                "mcp_config": self.mcp_config(),
                "open": self.element.best_link or None,
                "verified": self.element.status,
                "needs": ("a README read to find its run method" if self.kind == "repo" else
                          "sign-in at its website" if self.kind == "hosted" else
                          "a docker daemon" if self.kind == "docker" else None)}

    def __repr__(self) -> str:
        return f"<Tool {self.id} kind={self.kind} runnable={self.is_runnable()}>"

    # --- collection helpers ---------------------------------------------
    @staticmethod
    def wrap(element: "Element") -> "Tool":
        return Tool(element)

    @staticmethod
    def all(kind: str | None = None, runnable_only: bool = False,
            types: tuple | None = None) -> list:
        """Every element that could carry a run command.

        Fire 97 widened the default from ("tool","connector","skill","model") to ALL types. The
        dashboard's ▶run badge scans every element, and the two disagreed on 5 records — a
        `design` and some `prompt`s that genuinely do carry `npx …`/`pip install …` in their
        text. Two answers to "is this runnable?" is precisely the hand-rolled drift this class
        exists to end, so the narrower filter loses: is_runnable() is a claim about whether a
        real command is on file, not about whether the element is tool-SHAPED.
        """
        out = []
        for el in load().values():
            if types and el.type not in types:
                continue
            t = Tool(el)
            if kind and t.kind != kind:
                continue
            if runnable_only and not t.is_runnable():
                continue
            out.append(t)
        return out


class Room:
    """M2 class overhaul, CLASS 3 of 5 — ONE conversation between agents that ends in an artifact.

    WRAPS, DOES NOT REPLACE, `src/excava_chat.py`. That module already runs real multi-turn
    debate on real engines and has 52 rooms and 2,305 committed artifacts behind it — rewriting
    it would destroy working machinery to satisfy a diagram. What it lacks is a TYPE: rooms are
    passed around as bare dicts, so every caller re-reads rooms.json and re-derives "is this
    room finished?", "where is its transcript?", "did it actually produce anything?" by hand.
    That is the same fragmentation Element and Tool already fixed for the hub.

    The read side is deterministic and offline — status, transcript, artifact. Only `advance()`
    spends engine calls, and it delegates to excava_chat.advance() rather than reimplementing a
    turn loop.
    """

    __slots__ = ("_d",)

    def __init__(self, d: dict):
        self._d = d or {}

    # --- identity -------------------------------------------------------
    @property
    def id(self) -> str:
        return self._d.get("id", "")

    @property
    def kind(self) -> str:
        """dept | cross | group | war — war rooms are the showpiece (M2.5)."""
        return self._d.get("kind", "")

    @property
    def goal(self) -> str:
        return self._d.get("goal", "")

    @property
    def dept(self) -> str:
        return self._d.get("dept", "")

    @property
    def done_criteria(self) -> str:
        return self._d.get("done_criteria", "")

    # --- progress -------------------------------------------------------
    @property
    def status(self) -> str:
        return self._d.get("status", "")

    @property
    def turns(self) -> int:
        return int(self._d.get("turns", 0) or 0)

    @property
    def max_turns(self) -> int:
        return int(self._d.get("max_turns", 0) or 0)

    def is_open(self) -> bool:
        return self.status == "open"

    def is_exhausted(self) -> bool:
        """Hit its turn ceiling without converging — a room that stopped, not one that finished."""
        return not self.is_open() and self.turns >= self.max_turns > 0 and not self.has_artifact()

    # --- what it actually produced (law P4: real, not display) -----------
    def has_artifact(self) -> bool:
        return bool(self._d.get("artifact"))

    @property
    def artifact_path(self) -> str:
        """excava_chat stores the artifact as {kind, ref, at, title, by} — the path is `ref`.
        A bare string is accepted too, so an older/simpler record still resolves."""
        a = self._d.get("artifact")
        if isinstance(a, dict):
            return str(a.get("ref") or "")
        return str(a or "")

    @property
    def artifact_title(self) -> str:
        a = self._d.get("artifact")
        return str(a.get("title", "")) if isinstance(a, dict) else ""

    @property
    def artifact_by(self) -> str:
        """Which agent synthesized it — provenance (law P9)."""
        a = self._d.get("artifact")
        return str(a.get("by", "")) if isinstance(a, dict) else ""

    def artifact_text(self) -> str:
        """The committed decision document, or '' — the ONE thing that proves the room worked."""
        if not self.has_artifact():
            return ""
        p = ROOT / self.artifact_path
        try:
            return p.read_text(encoding="utf-8")
        except Exception:
            return ""

    def artifact_is_real(self) -> bool:
        """An artifact that is missing, empty, or still carrying conflict markers is NOT real.

        This exists because 47 committed artifacts were found corrupted with git conflict
        markers on 2026-08-01 while every count still reported them as produced.
        """
        t = self.artifact_text()
        return bool(t.strip()) and not any(
            l.startswith(("<<<<<<<", "=======", ">>>>>>>")) for l in t.splitlines())

    def transcript(self, limit: int = 0) -> list:
        """What the agents actually SAID, newest day first (feature-inventory item 40)."""
        out = []
        for day in sorted((EXC / "chats").glob("*"), reverse=True):
            f = day / f"{self.id}.jsonl"
            if not f.exists():
                continue
            for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
        return out[-limit:] if limit else out

    def speakers(self) -> list:
        seen = []
        for m in self.transcript():
            n = m.get("name")
            if n and n != "room" and n not in seen:
                seen.append(n)
        return seen

    # --- the one action that costs engine calls --------------------------
    def advance(self, turns: int = 2) -> list:
        """Run real turns. Delegates to excava_chat.advance (Ponytail — proven path)."""
        from src import excava_chat
        return excava_chat.advance(self.id, turns=turns)

    def to_dict(self) -> dict:
        return dict(self._d)

    def __repr__(self) -> str:
        return f"<Room {self.id} {self.status} {self.turns}/{self.max_turns} artifact={self.has_artifact()}>"

    # --- collection ------------------------------------------------------
    @staticmethod
    def all(kind: str | None = None, status: str | None = None) -> list:
        try:
            d = json.loads((EXC / "rooms.json").read_text(encoding="utf-8"))
        except Exception:
            return []
        out = []
        for r in d.get("rooms", []):
            if not isinstance(r, dict):
                continue
            if kind and r.get("kind") != kind:
                continue
            if status and r.get("status") != status:
                continue
            out.append(Room(r))
        return out

    @staticmethod
    def get(room_id: str):
        for r in Room.all():
            if r.id == room_id:
                return r
        return None

    @staticmethod
    def open(kind: str, goal: str, dept: str = "", done_criteria: str = "",
             max_turns: int = 10) -> "Room":
        from src import excava_chat
        return Room(excava_chat.open_room(kind, goal, dept, done_criteria, max_turns))


class Agent:
    """M2 class overhaul, CLASS 4 of 5 — one named worker: {name, role, engine, tools} (§2).

    WRAPS `data/excava/agents.json` (46 agents, 15 departments) and the dispatch already in
    `excava_agents.py`. The roster is real and healthy — every agent has scoped tools and every
    scoped module exists on disk (checked 2026-08-01) — so this class is not here to find rot in
    it. It is here to answer the question nothing could answer before: **has this agent actually
    DONE anything, or is it a name in a file?**

    That is the same law-P4 test the earlier classes apply — `Element.is_usable()`,
    `Tool.is_runnable()`, `Room.artifact_is_real()`. For an agent it is `has_spoken()`: a persona
    that has never opened its mouth in any room is decoration, however good its description is.
    Answering it requires the Room class, which is exactly the cross-class integration the
    collapse is for ("nothing orphaned").
    """

    __slots__ = ("_d",)

    def __init__(self, d: dict):
        self._d = d or {}

    # --- identity (§2's {name, role, engine, tools}) ----------------------
    @property
    def id(self) -> str:
        return self._d.get("id", "")

    @property
    def name(self) -> str:
        return self._d.get("name", "")

    @property
    def role(self) -> str:
        """lead | doer | checker | improver — the diversity axis stacked on model family (§2)."""
        return self._d.get("role", "")

    @property
    def department(self) -> str:
        return self._d.get("department", "")

    @property
    def tier(self) -> int:
        return int(self._d.get("tier", 0) or 0)

    @property
    def persona(self) -> str:
        return self._d.get("persona", "")

    @property
    def engine_pref(self) -> str:
        return self._d.get("engine_pref", "")

    @property
    def scoped_tools(self) -> list:
        return self._d.get("scoped_tools", []) or []

    def is_lead(self) -> bool:
        return self.role == "lead"

    # --- can it work? (deterministic, offline) ---------------------------
    def missing_tools(self) -> list:
        """Scoped modules that do not exist on disk — an agent scoped to nothing cannot act."""
        return [t for t in self.scoped_tools
                if not (ROOT / (t.replace(".", "/") + ".py")).exists()]

    def can_act(self) -> bool:
        return bool(self.scoped_tools) and not self.missing_tools()

    def tools(self) -> list:
        """Its scoped modules as Tool-ish descriptors. Distinct from the hub's Tool class: these
        are THIS repo's own modules, not mined OSS — kept separate on purpose so 'the agent's
        tools' is never confused with 'a wrapped OSS repo'."""
        return [{"module": t, "exists": (ROOT / (t.replace(".", "/") + ".py")).exists()}
                for t in self.scoped_tools]

    # --- has it actually done anything? (law P4) -------------------------
    def rooms(self) -> list:
        """Rooms this agent has actually spoken in."""
        return [r for r in Room.all() if self.name in r.speakers()]

    def has_spoken(self) -> bool:
        return bool(self.rooms())

    def artifacts_authored(self) -> list:
        """Artifacts this agent synthesized — the strongest evidence it did real work."""
        return [r for r in Room.all() if r.artifact_by == self.name and r.artifact_is_real()]

    def to_dict(self) -> dict:
        return dict(self._d)

    def __repr__(self) -> str:
        return f"<Agent {self.name} {self.role}@{self.department} spoken={self.has_spoken()}>"

    # --- collection ------------------------------------------------------
    @staticmethod
    def all(department: str | None = None, role: str | None = None) -> list:
        try:
            raw = json.loads((EXC / "agents.json").read_text(encoding="utf-8"))
        except Exception:
            return []
        items = raw if isinstance(raw, list) else raw.get("agents", [])
        out = []
        for a in items:
            if not isinstance(a, dict):
                continue
            if department and a.get("department") != department:
                continue
            if role and a.get("role") != role:
                continue
            out.append(Agent(a))
        return out

    @staticmethod
    def get(name_or_id: str):
        for a in Agent.all():
            if a.id == name_or_id or a.name.lower() == str(name_or_id).lower():
                return a
        return None

    @staticmethod
    def roster() -> dict:
        """The honest census: who exists, who can act, who has actually worked."""
        ags = Agent.all()
        silent = [a for a in ags if not a.has_spoken()]
        return {"total": len(ags),
                "departments": len({a.department for a in ags}),
                "can_act": sum(1 for a in ags if a.can_act()),
                "have_spoken": len(ags) - len(silent),
                "silent": [a.name for a in silent],
                "by_role": {r: sum(1 for a in ags if a.role == r)
                            for r in sorted({a.role for a in ags if a.role})}}


class Router:
    """M2 class overhaul, CLASS 5 of 5 — routes ANY task to a department, an agent, a tool, and
    a brain/engine, in one call, and says WHY (the trace law every other class already follows).

    THE PROBLEM THIS FIXES. The routing decision is currently split across three modules a
    caller has to know about and stitch together by hand: `excava_agents.pick_department`
    (text -> department), `excava_agents.worker_for` + `REAL_TOOL`/`_task_tool_fit` (department
    -> agent + tool, gated by G-7 and the syscall domain check), and `excava_engines.pick_engine`
    (department -> brain). `Tool.invocation()` above already called its own output "the adapter
    spec the Router will read" — this is that Router.

    WHAT THIS IS NOT. Not a rewrite: the actual policy (keyword scoring, gating, engine tiering)
    stays exactly where it lives in `excava_agents`/`excava_engines`. Router only composes their
    real return values into one typed decision, so nothing here can silently diverge from what
    the bus/beat actually does when it ticks a department (`excava_agents.tick`) — same law as
    Tool wrapping `verify_connectors`, Room wrapping `excava_chat`, Agent wrapping the registry.
    """

    __slots__ = ("text", "department", "why", "runners_up", "agent_id", "tool", "tool_fits",
                 "blocked_reason", "engine")

    def __init__(self, text: str, department: str | None, why: str, runners_up: list,
                 agent_id: str | None, tool: str, tool_fits: bool | None,
                 blocked_reason: str | None, engine: dict | None):
        self.text = text
        self.department = department
        self.why = why
        self.runners_up = runners_up
        self.agent_id = agent_id
        self.tool = tool
        self.tool_fits = tool_fits
        self.blocked_reason = blocked_reason
        self.engine = engine

    @property
    def engine_name(self) -> str:
        return (self.engine or {}).get("name", "")

    @property
    def engine_lineage(self) -> str:
        from src import excava_engines as engines
        return engines.LINEAGE.get(self.engine_name, self.engine_name)

    def is_routable(self) -> bool:
        """False means: no department matched, or the one that did has no scoped worker (G-7)
        and no owner-flagged blocker either — a dead end the caller must not paper over."""
        return bool(self.department and (self.agent_id or self.blocked_reason))

    def to_dict(self) -> dict:
        return {"text": self.text, "department": self.department, "why": self.why,
                "runners_up": self.runners_up, "agent": self.agent_id,
                "tool": self.tool or None, "tool_fits": self.tool_fits,
                "blocked_reason": self.blocked_reason,
                "engine": self.engine_name or None, "engine_lineage": self.engine_lineage or None,
                "engine_status": (self.engine or {}).get("status", "") or None,
                "routable": self.is_routable()}

    def __repr__(self) -> str:
        return (f"<Router '{self.text[:30]}' -> {self.department or '(none)'} "
                f"via {self.engine_name or '(no engine)'} routable={self.is_routable()}>")

    # --- the routing decision --------------------------------------------
    @staticmethod
    def route(text: str, difficulty: str = "normal", reg: dict | None = None,
              can_do: dict | None = None) -> "Router":
        """text -> the full decision an agent needs to actually act. `reg`/`can_do` may be
        passed in by a caller that already loaded them (e.g. the beat, mid-tick) to avoid a
        second disk read; both default to a fresh load, same as `excava_agents.tick` does."""
        from src import excava_agents as agents
        from src import excava_engines as engines
        reg = agents.load_registry() if reg is None else reg
        dept, why, runners_up = agents.pick_department(text, reg, can_do or {})
        worker = agents.worker_for(reg, dept) if dept else None
        tool = agents.REAL_TOOL.get(dept, "") if dept else ""
        tool_fits = (agents._task_tool_fit({"title": text, "detail": ""}, tool)
                     if tool else None)
        blocked_reason = agents.BLOCKED.get(dept) if dept else None
        engine = engines.pick_engine(dept or "", difficulty)
        return Router(text, dept, why, runners_up, worker.get("id") if worker else None,
                      tool, tool_fits, blocked_reason, engine)


class Package:
    """A named bundle of Elements — the plan's 'Element/Package' pair (§2, law P8).

    A Package is what EXCAVA hands over when one element is not enough: 'the stack for
    building an MCP-backed research agent' = a connector + a skill + a prompt. Persisted to
    data/excava/packages.json so a package built in one session survives into the next.
    """

    def __init__(self, name: str, element_ids: list | None = None, note: str = ""):
        self.name = name
        self.element_ids = list(element_ids or [])
        self.note = note

    def add(self, eid: str) -> bool:
        if eid in self.element_ids:
            return False
        self.element_ids.append(eid)
        return True

    def elements(self) -> list:
        idx = load()
        return [idx[e] for e in self.element_ids if e in idx]

    def missing(self) -> list:
        """Ids in the package that no longer resolve — a package can rot; say so honestly."""
        idx = load()
        return [e for e in self.element_ids if e not in idx]

    def to_dict(self) -> dict:
        return {"name": self.name, "elements": self.element_ids, "note": self.note}

    # --- persistence ----------------------------------------------------
    # Fire 95 found a REAL orphan: two package stores existed and the public hub API
    # (build_hub_api.py) only read the legacy one, so any package assembled through this class
    # was invisible outside the repo. Rather than move files (quarantine-never-delete), Package
    # now READS BOTH and is the single accessor; writes go to the class store. LEGACY is the
    # curated/pinned set built by earlier phases; PACKAGES is what this class creates.
    LEGACY = DATA / "packages.json"

    @staticmethod
    def _read(p: Path) -> list:
        try:
            return json.loads(p.read_text(encoding="utf-8")).get("packages", []) or []
        except Exception:
            return []

    @staticmethod
    def _store() -> dict:
        try:
            return json.loads(PACKAGES.read_text(encoding="utf-8"))
        except Exception:
            return {"packages": []}

    @classmethod
    def _from_raw(cls, p: dict) -> "Package":
        pkg = cls(p.get("name", p.get("id", "?")), p.get("elements", []),
                  p.get("note") or p.get("what", ""))
        return pkg

    @classmethod
    def load(cls, name: str):
        for p in cls._read(PACKAGES) + cls._read(cls.LEGACY):
            if p.get("name") == name or p.get("id") == name:
                return cls._from_raw(p)
        return None

    @classmethod
    def all(cls) -> list:
        """Every package from BOTH stores, class-created first, deduped by name."""
        out, seen = [], set()
        for p in cls._read(PACKAGES) + cls._read(cls.LEGACY):
            key = p.get("name") or p.get("id")
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(cls._from_raw(p))
        return out

    def save(self) -> None:
        store = self._store()
        pkgs = [p for p in store.get("packages", []) if p.get("name") != self.name]
        pkgs.append(self.to_dict())
        store["packages"] = pkgs
        PACKAGES.parent.mkdir(parents=True, exist_ok=True)
        PACKAGES.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Index access (cached; offline/online parity per P7)
# ---------------------------------------------------------------------------
_INDEX_CACHE: dict | None = None
_DUPES: list = []


def _raw_index() -> dict:
    """Local index first; fall back to the public hub so this works outside the repo (P7)."""
    try:
        if INDEX.exists():
            return json.loads(INDEX.read_text(encoding="utf-8"))
    except Exception:
        pass
    try:
        with urllib.request.urlopen(f"{REMOTE}/elements_index.json", timeout=20) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return {}


def load(refresh: bool = False) -> dict:
    """id -> Element for the whole hub. Cached; pass refresh=True after a rebuild.

    An id must be unique — it is how every consumer, override and relation addresses an element.
    The index does not currently guarantee that (see `duplicates()`), so collisions are recorded
    instead of being silently dropped: a swallowed record is invisible work, and the whole point
    of this class is that nothing goes quiet.
    """
    global _INDEX_CACHE, _DUPES
    if _INDEX_CACHE is None or refresh:
        raw = _raw_index()
        _INDEX_CACHE, _DUPES = {}, []
        for e in raw.get("elements", []):
            if not isinstance(e, dict) or not e.get("id"):
                continue
            eid = e["id"]
            if eid in _INDEX_CACHE:
                _DUPES.append(e)
                continue
            _INDEX_CACHE[eid] = Element(e)
    return _INDEX_CACHE


def duplicates() -> list:
    """Records the index emitted under an id that was already taken — they are UNREACHABLE.

    Cause (found 2026-07-30 by this class's first run): `element_model._slug()` truncates to 60
    chars, so distinct long `command` names collapse onto one id. Fixing the slug re-keys
    elements hub-wide and would invalidate `element_overrides.json` / `elements_related.json`
    keys, so it is deliberately a separate, verified increment — not a silent side-effect here.
    """
    load()
    return list(_DUPES)


def get(eid: str):
    return load().get(eid)


def find(query: str, type: str | None = None, usable_only: bool = False,
         limit: int = 10) -> list:
    """Score-ranked search over the hub.

    Scoring mirrors activate.find (exact > substring > all-words > some-words) so the two agree,
    but adds the status awareness activate.py never had: dead elements are excluded outright and
    usable ones outrank unusable ones at equal text score.
    """
    q = _norm(query)
    qs = set(q.split())
    hits = []
    for el in load().values():
        if type and el.type != type:
            continue
        if el.is_dead:
            continue
        if usable_only and not el.is_usable():
            continue
        n = _norm(el.name)
        if not n:
            continue
        words = set(n.split())
        if n == q:
            score = 100
        elif q and q in n:
            score = 70
        elif qs and qs <= words:
            score = 60
        elif qs & words:
            score = 30 + 8 * len(qs & words)
        elif q and q in _norm(el.what):
            score = 20
        else:
            continue
        # directly-installable kinds win ties, then usability, then rating
        score += {"connector": 4, "skill": 3, "prompt": 2, "command": 2}.get(el.type, 0)
        score += 5 if el.is_usable() else 0
        score += (el.quality or 0) / 100.0
        hits.append((score, el))
    hits.sort(key=lambda x: (-x[0], x[1].name))
    return [el for _, el in hits[:limit]]


def stats() -> dict:
    els = list(load().values())
    by_status, by_type = {}, {}
    for e in els:
        by_status[e.status] = by_status.get(e.status, 0) + 1
        by_type[e.type] = by_type.get(e.type, 0) + 1
    return {"total": len(els), "usable": sum(1 for e in els if e.is_usable()),
            "stubs": sum(1 for e in els if e.is_stub), "by_status": by_status,
            "by_type": dict(sorted(by_type.items(), key=lambda kv: -kv[1])),
            "unreachable": len(duplicates())}


# ---------------------------------------------------------------------------
def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="EXCAVA Element/Package class (M2 class 1 of 5)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("stats")
    f = sub.add_parser("find")
    f.add_argument("query")
    f.add_argument("--type")
    f.add_argument("--usable", action="store_true")
    f.add_argument("--limit", type=int, default=10)
    f.add_argument("--json", action="store_true")
    s = sub.add_parser("show")
    s.add_argument("eid")
    s.add_argument("--json", action="store_true")
    p = sub.add_parser("package")
    p.add_argument("name")
    p.add_argument("--add", action="append", default=[])
    p.add_argument("--note", default="")
    ts = sub.add_parser("tools", help="what in the hub can actually be RUN")
    ts.add_argument("--kind", choices=["mcp", "npm", "pip", "docker", "repo", "hosted", "unknown"])
    ts.add_argument("--runnable", action="store_true")
    ts.add_argument("--limit", type=int, default=20)
    ag = sub.add_parser("agents", help="the roster: who exists, who can act, who has WORKED")
    ag.add_argument("--department")
    ag.add_argument("--role", choices=["lead", "doer", "checker", "improver"])
    ag.add_argument("--silent", action="store_true", help="only those who never spoke")
    a1 = sub.add_parser("agent", help="ONE agent: tools, rooms, artifacts")
    a1.add_argument("who")
    rs = sub.add_parser("rooms", help="the conversations and what they PRODUCED")
    rs.add_argument("--kind")
    rs.add_argument("--status")
    rs.add_argument("--limit", type=int, default=15)
    r1 = sub.add_parser("room", help="ONE conversation: who spoke, what was decided")
    r1.add_argument("room_id")
    r1.add_argument("--transcript", action="store_true", help="print what the agents said")
    t1 = sub.add_parser("tool", help="how to run ONE element")
    t1.add_argument("eid")
    t1.add_argument("--online", action="store_true", help="ask npm/PyPI when no command is embedded")
    t1.add_argument("--json", action="store_true")
    rt = sub.add_parser("route", help="where would this task go: department, agent, tool, engine")
    rt.add_argument("text")
    rt.add_argument("--difficulty", choices=["normal", "hard", "grounded"], default="normal")
    rt.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.cmd == "stats":
        st = stats()
        print(f"hub: {st['total']} elements · {st['usable']} usable · {st['stubs']} stubs")
        print("  by status:", ", ".join(f"{k}={v}" for k, v in st["by_status"].items()))
        print("  by type:  ", ", ".join(f"{k}={v}" for k, v in st["by_type"].items()))
        if st["unreachable"]:
            print(f"  ⚠ {st['unreachable']} record(s) UNREACHABLE — id collisions "
                  f"(element_model._slug truncates at 60 chars):")
            for d in duplicates():
                print(f"      {d['id']}  <- {d.get('name', '')[:60]!r}")
        return 0

    if a.cmd == "find":
        hits = find(a.query, type=a.type, usable_only=a.usable, limit=a.limit)
        if a.json:
            print(json.dumps([h.to_dict() for h in hits], ensure_ascii=False, indent=2))
            return 0
        if not hits:
            print(f'no match for "{a.query}"')
            return 1
        for el in hits:
            mark = "USABLE" if el.is_usable() else el.status.upper()
            print(f"  [{mark:>10}] {el.id:<44} {el.what[:70]}")
        return 0

    if a.cmd == "show":
        el = get(a.eid)
        if not el:
            print(f"no element {a.eid}")
            return 1
        if a.json:
            print(json.dumps(el.to_dict(), ensure_ascii=False, indent=2))
            return 0
        print(f"{el.name}  ({el.type} | {el.status}{' | stub' if el.is_stub else ''})")
        print(f"  {el.what}")
        if el.best_link:
            print(f"  link: {el.best_link}")
        act = el.activation()
        print(f"  ACTIVATE ({act['kind']}{' | needs key' if act['needs_key'] else ''}):")
        for i, step in enumerate(act["steps"], 1):
            print(f"    {i}. {step}")
        if el.related_ids:
            print("  related:", ", ".join(el.related_ids[:6]))
        return 0

    if a.cmd == "package":
        pkg = Package.load(a.name) or Package(a.name, note=a.note)
        if a.note:
            pkg.note = a.note
        added = [e for e in a.add if get(e) and pkg.add(e)]
        unknown = [e for e in a.add if not get(e)]
        pkg.save()
        print(f"package '{pkg.name}': {len(pkg.element_ids)} element(s)"
              + (f" (+{len(added)} added)" if added else ""))
        for el in pkg.elements():
            print(f"  - {el.id:<44} {'usable' if el.is_usable() else el.status}")
        if unknown:
            print("  unknown ids (not added):", ", ".join(unknown))
        if pkg.missing():
            print("  MISSING (no longer in hub):", ", ".join(pkg.missing()))
        return 0

    if a.cmd == "agents":
        r = Agent.roster()
        print(f"roster: {r['total']} agents · {r['departments']} departments · "
              f"{r['can_act']} can act · {r['have_spoken']} have actually spoken")
        print("  by role:", ", ".join(f"{k}={v}" for k, v in r["by_role"].items()))
        if r["silent"]:
            print(f"  SILENT ({len(r['silent'])}) — named but never spoke: {', '.join(r['silent'])}")
        rows = Agent.all(department=a.department, role=a.role)
        if a.silent:
            rows = [x for x in rows if not x.has_spoken()]
        print(f"\nshowing {len(rows)}:")
        for x in rows:
            mark = "WORKED" if x.artifacts_authored() else ("spoke" if x.has_spoken() else "SILENT")
            print(f"  [{mark:>6}] {x.name:<12} {x.role:<9} {x.department:<14} {len(x.rooms())} room(s)")
        return 0

    if a.cmd == "agent":
        x = Agent.get(a.who)
        if not x:
            print(f"no agent {a.who}")
            return 1
        print(f"{x.name}  ({x.role} · {x.department} · tier {x.tier})")
        print(f"  persona: {x.persona[:140]}")
        print(f"  engine pref: {x.engine_pref or '(default)'}")
        print(f"  tools: {', '.join(t['module'] for t in x.tools()) or '(none)'}"
              + (f"  MISSING: {x.missing_tools()}" if x.missing_tools() else ""))
        rooms_in = x.rooms()
        arts = x.artifacts_authored()
        print(f"  spoke in {len(rooms_in)} room(s); authored {len(arts)} real artifact(s)")
        for r in arts[:5]:
            print(f"    - {r.artifact_path}")
        if not rooms_in:
            print("  NEVER SPOKEN — named in the roster but has not appeared in any room.")
        return 0

    if a.cmd == "rooms":
        rooms = Room.all(kind=a.kind, status=a.status)
        allr = Room.all()
        claimed = [r for r in allr if r.has_artifact()]
        real = [r for r in claimed if r.artifact_is_real()]
        print(f"rooms: {len(allr)} · {sum(1 for r in allr if r.is_open())} open · "
              f"{len(claimed)} produced an artifact · {len(real)} of those verify as REAL")
        print(f"\nshowing {min(len(rooms), a.limit)} of {len(rooms)}:")
        for r in rooms[:a.limit]:
            mark = "ART" if r.artifact_is_real() else ("???" if r.has_artifact() else "   ")
            print(f"  [{mark}] {r.id:<44} {r.status:<5} {r.turns}/{r.max_turns} turns  {r.goal[:38]}")
        return 0

    if a.cmd == "room":
        r = Room.get(a.room_id)
        if not r:
            print(f"no room {a.room_id}")
            return 1
        print(f"{r.id}  ({r.kind} · {r.status} · {r.turns}/{r.max_turns} turns)")
        print(f"  goal: {r.goal}")
        print(f"  done when: {r.done_criteria}")
        print(f"  spoke: {', '.join(r.speakers()) or '(nobody yet)'}")
        if r.has_artifact():
            ok = "REAL" if r.artifact_is_real() else "MISSING/CORRUPT"
            print(f"  artifact [{ok}] by {r.artifact_by}: {r.artifact_path}")
        else:
            print("  artifact: none yet")
        if a.transcript:
            print("\n  --- transcript ---")
            for m in r.transcript():
                print(f"  {m.get('name', '?'):>10}: {str(m.get('text', ''))[:100]}")
        return 0

    if a.cmd == "tools":
        ts = Tool.all(kind=a.kind, runnable_only=a.runnable)
        counts: dict = {}
        for t in Tool.all():
            counts[t.kind] = counts.get(t.kind, 0) + 1
        total_run = sum(1 for t in Tool.all() if t.is_runnable())
        print(f"tool-capable elements: {sum(counts.values())} · RUNNABLE (a real command on file): {total_run}")
        print("  by kind:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1])))
        print(f"\nshowing {min(len(ts), a.limit)} of {len(ts)}:")
        for t in ts[:a.limit]:
            print(f"  [{'RUN' if t.is_runnable() else '   '}] {t.id:<44} {t.kind:<7} {(t.command or t.element.best_link)[:52]}")
        return 0

    if a.cmd == "tool":
        el = get(a.eid)
        if not el:
            print(f"no element {a.eid}")
            return 1
        t = Tool(el)
        if a.online and not t.is_runnable():
            print("(asking npm/PyPI…)")
            t.resolve_online()
        inv = t.invocation()
        if a.json:
            print(json.dumps(inv, ensure_ascii=False, indent=2))
            return 0
        print(f"{t.name}  ({t.kind}{' · RUNNABLE' if t.is_runnable() else ' · not runnable yet'})")
        if inv["command"]:
            print(f"  run:  {inv['command']}")
        if inv["mcp_config"]:
            print("  MCP config (paste into claude_desktop_config.json):")
            print("    " + json.dumps(inv["mcp_config"], ensure_ascii=False))
        if inv["open"]:
            print(f"  open: {inv['open']}")
        if inv["needs"]:
            print(f"  needs: {inv['needs']}")
        if not t.is_runnable() and not a.online:
            print("  tip: re-run with --online to ask npm/PyPI for a matching package.")
        return 0

    if a.cmd == "route":
        r = Router.route(a.text, difficulty=a.difficulty)
        if a.json:
            print(json.dumps(r.to_dict(), ensure_ascii=False, indent=2))
            return 0
        print(f"'{a.text}'")
        if not r.department:
            print(f"  no department matched: {r.why}")
            return 1
        print(f"  department: {r.department}  ({r.why})")
        if r.runners_up:
            print(f"  runners-up: {', '.join(r.runners_up)}")
        print(f"  agent: {r.agent_id or '(none — G-7: no scoped worker)'}")
        if r.blocked_reason:
            print(f"  BLOCKED: {r.blocked_reason}")
        if r.tool:
            print(f"  tool: {r.tool}  (fits: {r.tool_fits})")
        print(f"  engine: {r.engine_name or '(none available)'}"
              + (f"  [{r.engine_lineage}]" if r.engine_name else ""))
        print(f"  routable: {r.is_routable()}")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
