# 🎮 First 1000 Players

**English** · [Tiếng Việt](README.vi.md)

> AI made building games easy. Getting anyone to play them is still hard.
> **First 1000 Players** is a pack of agent skills that helps AI vibecoders take a game from "it works" to its first 1,000 real players — honestly, without spam.

Around 20,000 games launched on Steam in 2025. Only ~3% reached 1,000 reviews, and the median release earned a few hundred dollars ([data](references/market.md)). Building is no longer the bottleneck. **Being seen is.**

Marketing skill packs exist for SaaS. Game-making skill packs exist for code. This one is for the step in between: **distribution for small, AI-built games** — web portals, itch.io, Steam, short video, communities, and the AI-disclosure question every vibecoder now faces.

## Skills

| Skill | Use it when you want to… |
|---|---|
| [`game-context`](skills/game-context/SKILL.md) | describe your game once, so every other skill knows its genre, audience, platforms and AI usage |
| [`platform-picker`](skills/platform-picker/SKILL.md) | decide where to release first (CrazyGames, Poki, itch.io, Steam…) and what comes next |
| [`hook-finder`](skills/hook-finder/SKILL.md) | find the moments strangers stop scrolling for and turn them into TikTok/Shorts clips |
| [`community-launcher`](skills/community-launcher/SKILL.md) | share your game on Reddit, Discord and local groups without breaking rules (drafts only) |
| [`ai-disclosure`](skills/ai-disclosure/SKILL.md) | write honest AI disclosures for Steam, itch.io and Reddit, and reduce backlash |

Coming next: `steam-page-wishlist`, `web-portal-publisher`, `feedback-analytics`, `launch-checklist`, `devlog-buildinpublic`, `creator-outreach`, `sea-vietnam-playbook`.

## Install


**Claude Code (plugin)**
```
/plugin marketplace add nguyenbui1105/first-1000-players
/plugin install first-1000-players@first-1000-players
```

**Any agent supporting the open [Agent Skills](https://agentskills.io) standard**
```bash
npx skills add nguyenbui1105/first-1000-players
```

**Manual** — copy the folders in `skills/` into:
- Claude Code: `.claude/skills/` (project) or `~/.claude/skills/` (global)
- Codex: `.agents/skills/`
- Cursor: `.cursor/skills/`

## Quick start

Open your game project with your agent and say:

```
Help me find my first players.
```

The agent runs `game-context`, writes `.agents/game-context.md`, then suggests `platform-picker` and `hook-finder`.

## Principles

1. **Drafts, not bots.** Skills never post, comment or DM for you. You publish.
2. **Honest about AI.** No skill helps hide AI use. Concealment backfires harder than disclosure.
3. **Numbers with dates.** Every benchmark has a source and a `last_checked` date. Platforms change; skills tell you to verify.
4. **No viral promises.** Viral stories are survivors. Skills set realistic gates and measure.
5. **Your language.** Skills answer in the language you write in. Docs: English and Vietnamese, more welcome.

## Case study

Every skill is tested first on a real game: a first-person pepper-farming game set in Đắk Lắk, Vietnam. Follow the public diary in [`case-studies/pepper-farm-daklak`](case-studies/pepper-farm-daklak/README.md) — including the bad numbers.

## Repo layout

```
skills/          one folder per skill (SKILL.md + references/ + scripts/)
references/      shared market data with sources
evals/           3+ test prompts per skill
scripts/         validate_skills.py
case-studies/    real distribution diaries
```

## Contributing

Updated a community's rules? Have a case study? See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate_skills.py` before opening a PR.

## License

MIT
