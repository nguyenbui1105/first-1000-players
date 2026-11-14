# Contributing

Thanks for helping vibecoders find players. This repo only stays useful if its advice is **true, current and tested**.

## Ground rules

1. **Every number needs a source and a date.** Add benchmarks to `references/benchmarks.md` (or a skill's `references/` file) with a link and `last_checked: YYYY-MM-DD`. No source, no number.
2. **Skills draft, humans post.** No skill may tell an agent to post, comment, DM or email on the user's behalf. Skills write drafts; the user publishes.
3. **Honest about AI.** Skills must never help hide AI use from players or platforms.
4. **Community rules change.** When you add a community to `skills/community-launcher/references/communities.md`, include the rules you checked and the date.
5. **Keep skills small.** `SKILL.md` under 500 lines; push detail into `references/` (one level deep).

## Adding or changing a skill

1. Copy an existing skill folder as a template.
2. Write at least 3 evals in `evals/<skill-name>.json` **before** writing long docs.
3. Run `python3 scripts/validate_skills.py`.
4. Test the skill on a real game, then describe what happened in your PR.

## Case studies

Real results beat advice. Add your game under `case-studies/<your-game>/` using the template in `case-studies/pepper-farm-daklak/`. Bad numbers are welcome — they teach the most.

## Translations

Docs live in English (`README.md`) and Vietnamese (`README.vi.md`). To add a language, create `docs/i18n/README.<lang-code>.md` and link it from the language bar at the top of both READMEs. Skills themselves stay in English (agents trigger on them most reliably) and are written to **answer in the user's language**.
