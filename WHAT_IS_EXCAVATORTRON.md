# What is this project? (plain English — no code, promise)

_A guide for understanding Excavatortron without reading a single line of code._

## The one-sentence version
**Excavatortron is an automated assistant that hunts down every useful AI tool, skill, and trick in
the world, checks that each one is real and working, and organizes them into a library you can browse —
and it does this by itself, around the clock, for free.**

## The problem it solves
There are thousands of AI tools, tips, and tricks — scattered across YouTube videos, GitHub, forums,
and new ones appear every day. No human can keep up. Excavatortron keeps up *for* you: it watches an
AI YouTube playlist (and other places on the internet), pulls out everything useful that's mentioned,
verifies it actually exists and works, and files it away so you can find and use it.

## How it's organized — like a company
Instead of one big program, it's built like a **company with about 12 departments**, each with a job:

| Department | Its job (in plain words) |
|---|---|
| **Mining** | Hunts the whole internet for brand-new AI tools (GitHub, Hacker News, Reddit, Product Hunt…) |
| **Analysis** | Studies each tool deeply — what it is, what it does |
| **Links** | Finds the real website / download page for each tool, and checks the link works |
| **Security** | Makes sure nothing collected is dangerous or fake |
| **Visual** | Collects good design examples (nice-looking AI websites/apps) |
| **Memory** | Keeps everything organized and instantly findable |
| **News** | Tracks what's newest in AI |
| **Creators** | Builds ready-to-use "kits" out of the tools |
| **Improve** | Makes the whole system a little better each day |
| **Watch / Transcripts** | Pull the words and content out of the videos |

## The "monster" characters are little AI workers
Each department has small AI helpers (the creatures you see on the floor). They're not decoration —
they **actually talk to each other to make decisions**: one proposes an action ("let's do X"), another
pushes back ("prove that's a good idea first"), and then they act. They run on **free** AI models, so
the whole thing costs nothing to run.

## It runs by itself, in the cloud
You do **not** need your computer on. It lives on the internet (GitHub) and wakes up roughly **every
10 minutes** to do a round of work — we call each round a "beat." Every beat, the departments do their
jobs and **write down exactly what they did** so you can check.

## How YOU can see it's real — no code needed
This is the important part, because a lot of this project used to only *look* busy while doing nothing.
Three things you can read with your own eyes:
1. **The agents' real conversations** — plain English. You can read exactly what the workers argued about
   and decided. (In the app's "Rooms" tab, or the `chats` folder.)
2. **`PROOF.md`** — a plain summary, refreshed every beat: what each department actually produced, with a
   click-through link to the real proof. If a department did nothing, it *says so* ("noop" or "planned").
3. **The dashboard** — the visual version of all of the above.

## What it's ultimately trying to become — the "North Star"
Nine big goals, such as: know about *every* AI tool (not just the playlist), have a real working link
for each one, be genuinely useful to you, stay safe, and learn your personal taste. Some are close,
some are far — and the honest score for each is tracked openly.

## The honest state, plainly
It is **partly real and partly still catching up.** The library and the tool-hunting are real. Making
the AI workers do genuinely useful work (instead of just looking busy) is the thing being fixed right
now — and every improvement is something you can verify yourself in `PROOF.md`, not just take on trust.
