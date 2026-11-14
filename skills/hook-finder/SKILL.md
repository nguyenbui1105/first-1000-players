---
name: hook-finder
description: Finds the most clippable moments in a game and turns them into short-form video plans (TikTok, YouTube Shorts, Reels) with a 2-second hook, on-screen text and call to action, plus a script to cut vertical clips from screen recordings. Use when the user wants to make a trailer, short video, TikTok, gameplay clip, GIF, or asks "what is my game's hook" or "quay clip gì cho game".
---

# Hook Finder

Short video is the cheapest way for an unknown game to reach strangers. The job: find 3–5 moments a stranger would stop scrolling for, then plan clips that test them.

## Language

Answer in the user's language. Write on-screen text in the language of the target platform audience (ask: Vietnamese TikTok vs international).

## Workflow

1. Read `.agents/game-context.md` (run `game-context` first if missing).
2. **Mine moments.** Ask the user to describe or record 2–5 minutes of play. Score candidate moments with the 6 hook types below. If the user has a recording, ask for timestamps of interesting parts.
3. **Pick 3–5 moments** with the highest score. For each, write a clip plan (template below).
4. **Cut the clips** with `scripts/cut_clips.py` if the user has a recording and ffmpeg.
5. **Set up the test**: post variants over 1–2 weeks, record results in the table below, keep the winner's pattern.
6. Save the chosen moments to the "Most clippable moments" line in `.agents/game-context.md`.

## The 6 hook types (score each moment 0–2 per type)

| Type | Stops the scroll because… | Example |
|---|---|---|
| Satisfying | Repetitive, tactile, completes something | Stripping a cluster of ripe red pepper berries |
| Strange / novel | Viewer has never seen it in a game | A game about a Central Highlands pepper farm |
| Funny / physics | Something goes wrong in a silly way | Ladder slips, pepper sack rolls downhill |
| Atmosphere | Mood is instantly felt | Dawn mist over the plantation, rain on a tin roof |
| Local / cultural | "That's so us!" recognition, meme-able | Phin coffee dripping, specific local food, slang |
| Challenge / question | Viewer wants to answer or try | "Can you harvest 100 kg before the rain?" |

Moments scoring high on 2+ types are the best candidates. Atmosphere and local detail work for cozy games even without action.

## Clip plan template

```markdown
### Clip <n>: <name>
- Hook type(s):
- 0–2s (hook): <first frame must already show gameplay — no logo, no menu fade-in>
- 2–15s: <what happens>
- On-screen text (≤ 8 words):
- Ending / CTA: <"Wishlist on Steam" | "Play free — link in bio" | question to drive comments>
- Length: 10–25s
- Sound: <game audio / trending sound / voiceover>
- Source timestamps: <start–end in recording>
```

## Rules for every clip

- Gameplay in frame 1. No studio logos, no slow intros.
- Vertical 9:16, 1080×1920; keep text away from the bottom ~20% (UI overlays).
- One idea per clip. Make 3–5 variants of the strongest moment (different first second, different text) rather than one "perfect" trailer.
- Post consistently; most clips get little reach and that is normal. Judge a pattern after several posts, not one.
- Don't promise virality. Viral case studies are survivors; many devs post regularly with little result.
- If the clip shows AI-generated art, follow the user's disclosure plan (`ai-disclosure`).

## Results table (keep in the project, e.g. `marketing/clips.md`)

| Date | Platform | Clip | Variant | Views 48h | Avg watch % | Likes | Comments | Link clicks / wishlists |
|---|---|---|---|---|---|---|---|---|

## Cutting clips

`scripts/cut_clips.py` cuts vertical clips from a landscape recording using ffmpeg:

```bash
python3 scripts/cut_clips.py recording.mp4 --clip 00:01:12 15 harvest --clip 00:03:40 12 dawn --out clips/
```

Each `--clip` takes `START DURATION NAME`. Add `--no-crop` to keep the original framing (letterboxed to 9:16). Requires ffmpeg on PATH.

See `references/hook-examples.md` for case studies and what to learn from them.
