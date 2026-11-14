# Platform facts

last_checked: 2026-11-14 (compiled from the sources listed; terms change — always verify on the official page)

## Contents
1. Web portals
2. itch.io
3. Steam
4. Revenue reality check
5. Sources

## 1. Web portals

| Platform | Revenue share to developer | Notes |
|---|---|---|
| Poki | Indicative: 100% on traffic the developer brings, 50/50 on Poki-driven traffic | Curated, strict review. Revenue-share deal is **web-exclusive**, default term about 5 years; non-exclusive deals pay a one-off license fee. Initial download < 8 MB, Poki SDK required. |
| CrazyGames | Not published in main docs. 2026 GameMaker jam terms: 60% ad revenue, 70% IAP | 50M+ monthly players claimed. Self-upload then QA review. Non-exclusive. Payout above €100. |
| GameDistribution | 33% of net revenue | Non-exclusive. |
| GameMonetize | 45% (90% when you host on your own site) | — |
| Y8 | 50% of eligible ad revenue | Non-exclusive. |

Common technical requirements: HTML5/WebGL build, fast first load, works in an iframe, mobile-friendly if possible, the portal's SDK for ads and events.

## 2. itch.io

- Open to everyone. Sell, pay-what-you-want, or free with donations. The creator sets itch.io's share.
- **Generative AI disclosure** field (since 2024-11-20) with sub-tags: Graphics, Sound, Text & Dialog, Code.
- Since 2026-11-03 the "No AI" filter also applies to search results; with it on, browse shrinks from 1.77M+ to under 425K visible projects. Untagged AI content in some categories is not indexed. Mass-uploading automated AI content is treated as spam.
- Traditional algorithms (pathfinding, procedural generation) do not need disclosure.

## 3. Steam (summary — the planned `steam-page-wishlist` skill will go deeper)

- About 20,000 games released in 2025 (~55/day); 2026 pace ~69.5/day (SteamDB, Aug 2026).
- June 2026 homepage redesign: entry to "Popular Upcoming" now estimated at ~80,000–100,000 wishlists (was ~7,000). New **Personal Calendar** surfaces upcoming games per player; early analysis suggests ~8,000–30,000 wishlists to appear, and it can bring 300–3,000 wishlists/day around launch.
- Next Fest: one entry per game; the best predictor of results is wishlists **before** the fest. Games entering with < 1,000 wishlists gained a median of ~322–462.
- Store visibility is increasingly personalized → the page must look clearly like its genre.
- AI disclosure required for player-facing AI content (see `ai-disclosure` skill).

## 4. Revenue reality check

- Median 2025 Steam release earned roughly $249 gross by one estimate (Gamalytic, Oct 2025); other methods give up to ~$1,700. 65.9% under $1,000.
- One published CrazyGames example: 451,327 plays → €556.92 (~€1.2 per 1,000 plays).
- Portals are excellent for **players and data**, rarely for income on their own.

## 5. Sources

- https://howtomarketagame.com/2026/06/25/how-the-steam-personal-calendar-affects-your-launch/
- https://howtomarketagame.com/2025/03/26/benchmarks-how-many-wishlists-can-i-get-from-steam-next-fest/
- https://www.steampageanalyzer.com/blog/how-many-games-release-on-steam
- https://www.steampageanalyzer.com/blog/indie-game-sales-statistics
- https://app.cinevva.com/guides/publish-game-poki
- https://app.cinevva.com/guides/publish-game-crazygames
- https://portalready.world/portals/
- https://playfox.org/news/indie-dev-revenue/
- https://www.engadget.com/2305699/itchio-adds-a-filter-for-games-with-gen-ai-disclosures/
- https://itch.io/docs/creators/quality-guidelines
