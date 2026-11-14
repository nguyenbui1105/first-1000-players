---
name: game-context
description: Builds and maintains a shared game-context file (.agents/game-context.md) describing a game's genre, comparable titles, target players, platforms, build size, AI usage and distribution goals. Use when the user starts marketing, launching or finding players for a game, or when another first-1000-players skill needs context that does not exist yet. Also triggers on "help me market my game", "who is my game for", "giới thiệu game của tôi", "tìm người chơi cho game".
---

# Game Context

Every other skill in this pack reads `.agents/game-context.md` first. This skill creates or updates it, so the user never has to explain their game twice.

## Language

Detect the user's language from their messages and answer in it. Write the context file in English (agents read it), but keep any quoted player-facing text (taglines, hooks) in the language the user will publish it in.

## Workflow

1. **Check for an existing file.** If `.agents/game-context.md` exists, read it, show a 3-line summary, and ask only what is missing or outdated.
2. **Look before asking.** Scan the project for clues: engine (`package.json` with three/babylon/phaser, `project.godot`, `ProjectSettings`, Unity `Assets/`), build output size, README, existing store text. Fill what you can and confirm it instead of asking.
3. **Interview in small batches.** Ask at most 4 questions per message, easiest first. Use the question list below. Accept "don't know yet" — record it as `unknown`, never invent.
4. **Write the file** using the template below.
5. **Read it back** in 5 bullets and ask the user to correct anything wrong.
6. **Suggest the next skill**: usually `platform-picker` if no platform is chosen, otherwise `hook-finder`.

## Questions

Core (always ask if unknown):
1. In one sentence, what does the player do? (verb first: "farm pepper on a misty hillside")
2. Genre and 2 comparable games — "X meets Y" (e.g. "Stardew Valley meets Euro Truck Simulator, first-person").
3. Who is it for? Pick one primary group, not "everyone".
4. Engine / tech, and how big is a playable build (MB)?
5. Current state: idea / prototype / playable demo / near launch / launched.
6. Goal for the next 3 months: players and feedback, wishlists, or revenue?

AI usage (needed by `ai-disclosure`):
7. Where was generative AI used: code, art (in-game / store / marketing), audio, text, live in-game generation? Be specific.

Optional:
8. Session length and total playtime.
9. Languages the game supports.
10. What makes it different or local (place, culture, humor)?
11. Existing audience: followers, email list, Discord, friends who play.
12. Budget for marketing (money and hours per week).

## Template

```markdown
# Game Context
last_updated: YYYY-MM-DD

## Pitch
- One-liner:
- X meets Y:
- Player fantasy (what it feels like):

## Game
- Genre / tags (top 5, most specific first):
- Engine / tech:
- Build size (MB) / runs in browser? :
- Session length / total playtime:
- Languages:
- State: idea | prototype | demo | near-launch | launched

## Players
- Primary audience:
- Where they hang out (communities, platforms):
- Comparable games they already love:

## Distribution
- Platforms (current / planned):
- Goal (next 3 months): players | wishlists | revenue
- Existing audience:
- Weekly marketing time / budget:

## Differentiators
- Local / cultural details:
- Most clippable moments (filled by hook-finder):

## AI usage (filled by ai-disclosure)
- Code:
- Art in game:
- Store / marketing art:
- Audio:
- Text / dialogue:
- Live generation in game:

## Open questions
-
```

## Rules

- Never invent facts about the game. Unknown stays `unknown`.
- Push for **specific** answers: "cozy players" is weak; "players who finished Stardew and want something slower and first-person" is useful.
- If the user says "everyone", explain in one line why a narrow audience spreads faster, then ask them to pick one group to start.
- Keep the file under 120 lines. Overwrite outdated lines; don't append history.
