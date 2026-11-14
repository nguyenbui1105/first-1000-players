---
name: platform-picker
description: Recommends where to release a game first (browser game portals like CrazyGames or Poki, itch.io, Steam, mobile) and in what order, based on engine, build size, genre, session length and the creator's goal. Use when the user asks where to publish, which platform to launch on, web vs Steam vs itch, or "nên đăng game ở đâu". Produces a staged release plan, not a single answer.
---

# Platform Picker

Help a vibecoder choose **where to release first** and **what comes next**. Most AI-built games are small, web-friendly and unproven, so the default is: *validate the hook cheaply on the web, then invest in Steam only if the signal is good*. Override the default whenever the game's facts say otherwise.

## Language

Answer in the user's language. Keep platform names and technical terms in English.

## Workflow

1. Read `.agents/game-context.md`. If missing, run the `game-context` interview (core questions 1–6 only) first.
2. Collect the 6 decision inputs (ask only for missing ones):
   - Engine and whether it exports to WebGL/HTML5
   - Initial download size of a web build (MB)
   - Genre and session length
   - Goal: players & feedback / wishlists / revenue
   - Has the user got a Steam Direct fee budget and time for a store page?
   - Does the game have online features, and in which countries will it be sold commercially? (local licensing flag, see below)
3. Walk the decision tree below.
4. Read `references/platforms.md` for the facts you cite. Always show the `last_checked` date and tell the user to verify terms on the official page before signing anything.
5. Output the plan in the format below.

## Decision tree

```
Is a playable build < ~50 MB and does it run well in a browser?
├─ Yes → Stage 1: itch.io (free, HTML5) + one portal (CrazyGames first: open self-upload, non-exclusive)
│        Initial download < 8 MB and polished? → also consider Poki (curated, exclusive web deal — read terms)
└─ No  → Stage 1: itch.io downloadable demo + make a "web slice" (one level, compressed) if feasible

Session length < 10 min, instant fun? → portals fit well (ad-revenue model, huge casual traffic)
Session long, cozy/sim/story, PC-style controls? → portals are for testing only; Steam is the real target

Goal = wishlists or revenue AND the hook test (hook-finder) got real traction?
└─ Stage 2: Steam "Coming Soon" page ASAP (wishlists need months), demo, Next Fest later

Mobile: only if controls are touch-native and the user accepts ASO + store review overhead. Rarely stage 1 for vibecoders.
```

"Real traction" is a judgment call; suggest concrete gates such as: strangers (not friends) finish the first session, comments ask "where can I get this?", a clip clearly outperforms the user's other clips.

## Output format

```markdown
## Recommended path for <game>

**Stage 1 (now → N weeks): <platforms>**
- Why: <2 bullets tied to the game's facts>
- To do: <3–5 concrete steps>
- Success gate to move on: <measurable signal>

**Stage 2: <platform>** — when the gate is passed
**Not now: <platform>** — <one-line reason>

⚠️ Check before you commit: <terms that need verification, with links>
```

## Rules

- Never promise income. Portal ad revenue is usually small (see references); present portals as a **player and data** channel first.
- Flag Poki's exclusivity clearly; recommend the user read the contract.
- For Steam, mention that wishlists take months to build and shadow-dropping (launching without a page/announcement) is the most common mistake.
- **Local licensing flag:** some countries require a license or government approval to publish games commercially or to run online games (for example Vietnam's Decree 147/2024/NĐ-CP, or approval for publishing in mainland China). If the game targets such a country, mention that rules exist and suggest checking with a local expert. Do not give legal advice, and don't assume rules for a country you have no source for.
- If a fact is not in `references/platforms.md`, say you are not sure and point to the official docs instead of guessing.
