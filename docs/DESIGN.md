# Excavatortron — Design System

The dashboard's look is deliberate, not a template. This document explains every choice so the
look stays coherent as features are added. Two registers meet here: the **archive** (a calm,
warm reading surface for a huge body of knowledge) and the **instrument** (a live control panel
for a self-running pipeline). The design serves the product; it never competes with the data.

## 1. Palette — "field archive" warm neutrals, teal/emerald base, gold thread
- All color is **OKLCH**, never `#000`/`#fff`. Every neutral is tinted ~0.006–0.018 chroma toward
  warm hue 58–86, so white surfaces read as aged paper, not screen-white.
- **Base accent is teal/emerald** (`--accent` oklch 0.55 0.105 172), chosen precisely because it is
  NOT the reflexive AI-tool blue/indigo. It carries ≤10% of any surface (a Restrained strategy).
- **Gold is a thread, not a base.** `--gold` (oklch 0.80 0.118 86) appears only as a metallic
  *highlight*: the active nav tab's underline + rim, the #1 podium slot, the NEW badge, trend
  scores ≥8, the data/ hub graph node, and a fine top-rule on the structural panels. It recurs in
  every area so the whole UI feels of-a-piece, but it never floods the item cards. This restraint
  is the point: gold everywhere at low dose reads as luxury; gold on everything reads as noise.
- Status colors are fixed roles: green `--good` (healthy/free), amber `--warn` (caution), red
  `--bad` (risk/stalled). Gold is never a status; it is identity.

## 2. Typography
- Body is system-ui at 15.5px / 1.62 for long-form reading; line length is capped near 70ch.
- Display headings use a serif (Georgia stack, offline-safe) for the archive feel.
- Hierarchy comes from scale + weight contrast (≥1.25 steps), never from color alone.

## 3. Layout — bento hero, then breathing room
- The header is a **bento grid** on dark charcoal (oklch 0.205): an identity tile beside live stat
  tiles. It is the one dense, high-contrast moment; everything below it relaxes.
- Cards are used only where a card is the right affordance. **Nested cards are banned.** Spacing
  varies for rhythm rather than a uniform pad everywhere.
- Structural **panels** (Self-improvement clock, Live Pipeline, Trend watch) are visually distinct
  from **item cards** (a skill, a tool) via the gold top-rule + a short gold kicker under the title.

## 4. Absolute bans (enforced)
- No side-stripe borders (colored `border-left/right` > 1px). No gradient text. No glassmorphism by
  default. No hero-metric template. No identical endless card grids. No em dashes in UI copy.

## 5. Per-tab intent (why each tab is not generic)
- **Tool Rating** leads with a gold-crowned podium, then a ranked, filterable table; the #1 slot is
  the only gold-saturated element on the page.
- **Self-improvement** opens with a live countdown + "what it last did" proof, then the Trend watch
  and Maintenance grade. It is an instrument, so it shows motion and freshness, not static lists.
- **Developer** shows two graphs (knowledge + protocol orchestration) plus the **Live Pipeline**
  heartbeat. The protocol graph tints each node by which of the 5 goals it serves.
- **News** shows a synthesized digest (the system's own summary), not a wall of raw headlines.
- **Quick-read** restructures each card to its essence (key line + use case), not just tighter
  leading. Reading is processed for the user, not merely compressed.

## 6. Motion
- Ease-out (quart/expo) only; no bounce. Never animate layout properties. Transitions are ≤200ms
  and limited to color, border, shadow, transform.

## The slop test
If a viewer could say "AI made that" from the category alone, it has failed. The teal base (not
blue), the warm archival neutrals (not SaaS cream), and the disciplined gold thread (not navy-and-
gold finance cliché) are chosen to pass both the first- and second-order reflex checks.
