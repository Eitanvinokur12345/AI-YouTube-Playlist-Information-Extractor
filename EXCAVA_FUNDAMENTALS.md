# EXCAVA — Fundamentals (the plain-language course)

Written for Eitan, 2026-07-15. No jargon without a plain explanation. Read it once slowly; you'll
suddenly "own" the whole project. Everything here works beyond Claude — it's *your* reference.

---

## 0. The one picture to hold in your head

> You have a huge **library of AI abilities** (that's the **HUB / EXCAVATORTRON**).
> You have a **team of workers** (that's the **agents / EXCAVA**).
> You give the team a task. Each worker walks into the library, grabs the right ability off the
> shelf, and uses it to get the task done — and shows you the result.

That's the whole thing. Every fancy word below is just a detail of that one picture.

---

## 1. The two names (you corrected me — here it is, correct)

- **EXCAVATORTRON = the HUB.** The big machine that *excavated* (dug up) and *collected* thousands of
  AI abilities into one library. It is the **content** — the shelves and everything on them.
- **EXCAVA = the agents.** The **team** that *acts*. They read from the HUB and do real work.

Simple test: if it's *information sitting on a shelf* → EXCAVATORTRON. If it's a *worker doing
something* → EXCAVA.

---

## 2. What is an "Operating System" (OS)?

An OS is the software that lets you actually *use* a computer — Windows, macOS, Android. You don't
think about it, but it does 5 jobs:
1. **Runs programs** (opens apps).
2. **Schedules work** (decides what runs when).
3. **Stores files** (a place for everything, browsable).
4. **Takes your commands** (you click/type, it obeys).
5. **Manages permissions** (what's allowed).

An **agentic OS** (what you're building) is the same 5 jobs, but the "programs" are **AI agents** and
the "files" are **AI elements**. So: a system that takes your command, picks the right AI ability,
runs an agent to do it, stores everything in a browsable library, and keeps itself safe. That's it.

---

## 3. What is an "element"? (This is the word you were missing)

An **element** is *one reusable AI ability* — a single item on the library shelf. The HUB has ~6,800
of them. There are **six kinds**, and knowing the six is 80% of understanding the project:

| Element type | Plain meaning | Everyday analogy | Example |
|---|---|---|---|
| **Skill** | a packaged set of instructions for one kind of task | a recipe | "make a flyer", "review code" |
| **Tool** | a single action the AI can take | one power-tool | "resize image", "fetch a webpage" |
| **MCP connector** | a bridge to an outside app | a plug/adapter | connect to Notion, Slack, Figma |
| **Model** | the "brain" that thinks | the engine | Claude, Llama, Qwen |
| **Prompt** | a saved instruction that works well | a magic phrase | "summarize this in 5 bullets" |
| **Command** | a shortcut that runs something | a hotkey | `/review`, `/deploy` |

**Why this matters:** you told me "it's not just tools, it's elements." Exactly. A worker (agent)
doesn't only use *tools* — it can grab a **skill**, plug in a **connector**, pick a **model**, or run
a **prompt**. The HUB's power is that it has *all six types* collected in one place. That's rare.

> **MCP** (you'll see it a lot) = "Model Context Protocol." Boring name, simple idea: a **standard
> plug** so an AI can connect to any outside app (like USB is a standard plug for any device). A
> "connector" is one such plug.

---

## 4. What is an "agent"?

An **agent** is an AI worker that can *decide and act on its own*, not just answer. A chatbot
*replies*. An agent *does*: it reads the task, makes a little plan, picks elements from the HUB, uses
them step by step, checks the result, and hands it back. A **team of agents** = several workers, each
maybe specialized (one researches, one writes, one checks).

**The key shift you asked for:** old EXCAVA had agents that *talk to each other* (debate). You want
agents that *do the task* (execute). Talking is cheap and looks busy; doing is the point.

---

## 5. How the HUB "does tasks" instead of sitting empty (your exact question)

You said: *"the HUB should utilize elements while performing tasks independently, otherwise the OS
feels empty."* Right. A library nobody uses is dead. Two ways the HUB comes alive:

1. **On your command (pull):** you type a task → an agent searches the HUB → finds the best element(s)
   → uses them → result. The library is *pulled from* on demand.
2. **On its own (push / services):** small always-running workers use elements *without being asked* —
   e.g. every hour, use the "fetch + summarize" elements to pull new AI news into the HUB; use the
   "watch video" element to extract tools from a new video. The library *feeds itself* and *acts*.

So the HUB is never just a list. It's a **living library**: you draw from it, and it also works in the
background. That's what makes it feel like a real OS instead of a spreadsheet.

---

## 6. The engine problem (why your rooms died July 12) — and the free fix

- A **model** (the brain) runs on someone else's computer, and free ones have **rate limits** — "you
  may ask 30 questions an hour, then wait." Your agents share a few free brains, so when the limit
  hits, **the workers have no brain and freeze.** That's why the rooms stalled. Not a bug — no fuel.
- **The free fix = Ollama on a VPS.**
  - **VPS** = a **computer in the cloud that's always on** (a "Virtual Private Server"). Oracle gives
    one free forever.
  - **Ollama** = a program that runs **small AI brains on YOUR own computer/VPS** — *no rate limit,
    ever*, because it's yours. Free and unlimited.
  - So: put Ollama on the free VPS → your agents get an **unlimited free brain** for everyday steps,
    and you only borrow the strong free brains (Groq, Mistral) for the *hard* steps. **The starvation
    ends.** This is why your two answers — "free" and "VPS" — are actually one answer.

---

## 7. The "beat" and why everything goes through GitHub

- EXCAVA has no paid server, so it uses a clever trick: **GitHub Actions** (a free service meant for
  testing code) is made to run EXCAVA's **beat** — a job that wakes up every few minutes, does a
  little work, saves the results, and sleeps. That "heartbeat" is your **kernel** (the scheduler).
- The catch: GitHub Actions is a *batch job*, not a real server. It runs a few minutes then dies. So
  anything "live" (you type → it instantly acts) can't fully work here. **That's the other reason you
  need the VPS** — a real always-on computer where the live stuff actually lives.
- The screen you look at (**the cockpit**, on GitHub Pages) is a *static page* — it can *show* data
  but can't *do* anything by itself. Today, when you "click", it really just writes a note that the
  next beat reads. The VPS is what turns clicks into real-time actions.

---

## 8. Autonomy & permissions (who's allowed to do what)

Not every action should be automatic. EXCAVA uses **tiers**:
- **Low risk** (change a prompt, a setting) → the agent just does it.
- **Medium** (change its own code) → allowed only if an automatic safety test passes.
- **High** (a brand-new tool, spending, anything outward) → **stops and asks you** (a "pitch").

This is the OS's "are you sure?" / admin-password system. It's what lets EXCAVA be autonomous
*without* going rogue.

---

## 9. Self-improvement (what it should really mean)

Right now it's weak (it just tidies up). What it *should* be, and what you want more of:
> **Measure how often the team succeeds → find the #1 thing that fails → fix that → prove the number
> went up.** A system that can't measure its own success can't improve. This becomes a first-class
> part of the OS, not an afterthought.

---

## 10. How it all connects (the flow, one line)

**You** (command) → **EXCAVA agent** (plans) → searches **EXCAVATORTRON HUB** → grabs the right
**elements** (skill/tool/connector/model/prompt/command) → **executes** (brain = Ollama for easy
steps, strong engine for hard ones) → **checks** it → shows you the **result** → **self-improvement**
watches whether it worked. Meanwhile, **background services** keep feeding and using the HUB on their
own so it's never empty.

---

## 11. The 5 things you were missing (honest)

1. **The word "element"** and its six types — without it, the HUB looked like "just tools."
2. **EXCAVATORTRON = HUB vs EXCAVA = agents** — the two names had blurred together.
3. **Why free kept failing** — rate limits starve agents; Ollama-on-VPS is the free cure.
4. **Why "live" doesn't work yet** — no backend; GitHub Actions is a heartbeat, not a server.
5. **That the plan grew faster than your understanding** — we shipped features before the vocabulary
   was yours, so it felt like sand slipping. This document is the fix: now the words are yours.

---

## 12. Glossary (quick reference)

- **EXCAVATORTRON** — the HUB (the library of elements).
- **EXCAVA** — the agents (the team that acts).
- **Element** — one reusable AI ability (skill / tool / MCP connector / model / prompt / command).
- **Agent** — an AI worker that plans and *does*, not just replies.
- **HUB** — the browsable library of ~6,800 elements.
- **Model / engine** — the AI "brain" that thinks (Claude, Llama, Qwen…).
- **Rate limit** — a cap on how much a free brain will work per hour.
- **Ollama** — runs AI brains on your own computer/VPS; unlimited, free.
- **VPS** — an always-on cloud computer (Oracle's is free forever).
- **Beat / kernel** — the heartbeat job that schedules EXCAVA's work.
- **Cockpit** — the screen you look at.
- **MCP / connector** — a standard plug to connect AI to outside apps.
- **Autonomy tier** — how much an agent may do before asking you.
- **Pitch** — when an agent stops and asks your permission for something big.
- **Self-improvement** — EXCAVA measuring its own success and fixing its top failure.

---

*Next: with these words yours, the redesign conversation starts with the HUB — how it uses elements
and acts on its own — then the full design interview in `REBUILD_EXCAVA.md` §7. Ask me to explain any
line here live, in this session or the next.*
