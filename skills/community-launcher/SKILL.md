---
name: community-launcher
description: Plans and drafts posts that introduce a game to online communities (Reddit, Discord, X/Bluesky, and regional or language-specific groups worldwide) without breaking their rules or looking like spam. Use when the user wants to share, promote or get feedback on their game in a community, asks which subreddits or groups to post in, or says "đăng game lên đâu", "find my first players". Drafts only; the user posts.
---

# Community Launcher

Get the first strangers to play — by being a good community member, not a spammer. This skill picks communities, checks their rules, and drafts posts. **It never posts, comments or sends messages itself.** The user reviews and publishes every draft.

## Language

Answer in the user's language. Write each draft in the language of the community it targets.

## Workflow

1. Read `.agents/game-context.md` (run `game-context` first if missing). You need: genre, state, platform links, AI usage.
2. **Ask where the target players are** (countries, languages) if `game-context` does not say. **Pick 3–5 communities** from `references/communities.md` (global Reddit/Discord lists plus the matching regional section) that match the game's genre and state. Prefer communities where a playable link is welcome (e.g. r/playmygame needs a free, instantly playable game). If the target region has no entry yet, say so, suggest how to find local communities (genre + country/language searches on Discord, Reddit, Facebook, local forums), and invite the user to contribute what they find.
3. **Check the rules.** Show the rules recorded in the reference with their `last_checked` date and tell the user to open the community's current rules before posting. If a rule is unclear, say so.
4. **Check readiness** with the checklist below. Stop and tell the user what is missing.
5. **Draft one post per community** using the template. Different communities get different angles — never paste the same text everywhere.
6. **Plan the schedule:** at most one community per day, respect each community's posting limit, and block 1–2 hours after posting to reply to every comment.
7. After posting, help the user log results (template at the bottom) and summarize what players said.

## Readiness checklist

- [ ] Link works on a fresh browser / clean machine; loads fast
- [ ] First 60 seconds are understandable without instructions
- [ ] 1–4 GIFs or a short video showing gameplay
- [ ] AI disclosure line ready if the community requires it (use `ai-disclosure`)
- [ ] User's account meets the community's age/karma rules and has some genuine non-promotional activity
- [ ] A clear question for feedback

## Post template

```markdown
Title: I made <one-line pitch> — <what you want: feedback on X / looking for playtesters>

<1–2 sentences: what it is, who it's for>
<1–2 sentences: a real story — why you made it, what you learned (honest about using AI tools if relevant)>
<GIF or video>
<Specific question: "Does the first minute make sense?" / "Is harvesting satisfying or tedious?">
<Link — only if the community allows it, placed where the rules say>
<AI disclosure line if required>
```

First person, 100–300 words, no hype words ("revolutionary", "best"), no all-caps, no emoji walls.

## Anti-spam rules (non-negotiable)

- One community per post; no cross-posting the same text the same day.
- Follow the ~9:1 habit: for every promotional post, the account should have many genuine contributions (comments, help, feedback on others' games). Encourage the user to give feedback on other devs' games in the same community first.
- Never use multiple accounts, vote manipulation, or ask friends to upvote.
- Never automate posting, DMs or comments.
- If a moderator removes a post, don't repost; read the reason and adapt.

## Results log

| Date | Community | Post link | Upvotes/likes | Comments | Plays/clicks | Key feedback |
|---|---|---|---|---|---|---|

See `references/communities.md` for the community list and rules.
