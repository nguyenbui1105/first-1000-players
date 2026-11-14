---
name: steam-page-wishlist
description: Plans a Steam release and grows wishlists - Coming Soon page timing, store page audit (capsule art, tags, description, screenshots, trailer), demo and Next Fest strategy, Personal Calendar, festivals and mailing list. Includes a script that checks capsule image sizes. Use when the user mentions Steam, wishlists, a Steam store page, capsule art, Next Fest, a demo, or asks "how do I launch on Steam" or "làm trang Steam".
---

# Steam Page & Wishlists

On Steam, wishlists gathered **before** launch decide how much the store shows a game. This skill gets the page up early, makes it read clearly as its genre, and plans how wishlists will grow month by month.

## Language

Answer in the user's language. Store page copy is written in English first (Steam's largest audience), then in other languages the game supports.

## Workflow

1. Read `.agents/game-context.md` (run `game-context` first if missing). You need genre, comparable games, state, AI usage.
2. **Figure out where the user is** and jump to the matching section:
   - No Steamworks account yet → *Timeline*
   - Page exists → *Store page audit*
   - Page live, planning launch → *Wishlist plan* and *Next Fest & demo*
3. Use `references/steam.md` for every number. Show its `last_checked` date and remind the user that Valve changes rules; link the official Steamworks page for anything binding.
4. End with a dated action list (this week / this month / before launch).

## Timeline (work backwards from the launch date)

- Steam Direct fee and paperwork first; tax/identity checks and a waiting period after paying the fee take weeks.
- Submit the store page for review well before you want it public (plan at least 7 business days).
- **Coming Soon page: public at least 2 weeks before release is the minimum; aim for months.** Recommend going public as soon as there are 5+ good screenshots and a short trailer.
- Pick a release date about 2 months out and keep it, so the game can appear in players' Personal Calendar for the full window.
- **Never shadow drop** (release with no page and no lead time).

## Store page audit

Score each item ✅ / ⚠️ / ❌ and give one concrete fix per ⚠️/❌:

1. **Capsule art** reads at thumbnail size: title legible at the small capsule's tiny auto-generated size; art says the genre instantly; no text beyond the game's title. Run `scripts/check_capsules.py` on the asset folder to verify exact sizes.
2. **Genre clarity:** a stranger can name the genre in 3 seconds from the capsule plus first screenshot. Store recommendations are increasingly personalized, so looking like the genre matters more than looking unique.
3. **Tags:** the top tags are the most specific, accurate genre/feature tags (e.g. "Farming Sim", "Cozy", "First-Person", "Relaxing"), not broad ones like "Indie" or "Casual" first.
4. **Short description:** one sentence with the player's verb and the hook, no vague claims ("unique", "immersive").
5. **First screenshots / GIF:** gameplay, not menus or logos; the first one shows the core loop.
6. **Trailer:** gameplay in the first seconds (reuse `hook-finder` clips).
7. **Long description:** short paragraphs, animated GIFs of features, bullet list of what you do.
8. **AI disclosure** filled in truthfully (use `ai-disclosure`). Flag AI-generated capsule art as the highest backlash risk.

## Wishlist plan

Build a month-by-month table from now until launch + 1 month:

| Month | Push | Channel | Expected effect |
|---|---|---|---|

Typical pushes: Coming Soon announcement, short-video series (`hook-finder`), community posts (`community-launcher`), a festival entry, demo release, Next Fest, creator outreach, launch-date announcement ~2 months out. Use the benchmark ranges in `references/steam.md` and say clearly that results vary widely.

Also recommend a **mailing list or Discord** from day one: Steam's launch notification does not reach every wishlister.

## Next Fest & demo

- A game can enter Next Fest **once**, so time it for when the demo is polished and the page already has wishlists. The strongest predictor of Next Fest results is wishlists **before** the fest.
- Demo: short (15–30 min), ends on a high point, has a wishlist call-to-action on the last screen.
- Release the demo early (before Next Fest) to gather feedback and wishlists.

## Rules

- Never promise a wishlist number or revenue. Present benchmarks as ranges from named sources.
- Flag estimates (Personal Calendar thresholds, revenue figures) as estimates.
- Don't advise buying wishlists, review manipulation, or keys-for-reviews. These break Steam rules.
- If a requested fact is not in `references/steam.md`, say so and point to the Steamworks documentation.
