---
name: ai-disclosure
description: Audits where generative AI was used in a game (code, art, store and marketing images, audio, text, live generation) and drafts honest disclosure text for Steam, itch.io, Reddit and store pages, with advice on reducing player backlash. Use when the user asks about AI disclosure, Steam AI content survey, itch.io AI tags, whether to mention AI, or worries players will hate an AI-made game. Never helps hide AI use.
---

# AI Disclosure

Players and platforms react far worse to AI use that is **discovered** than to AI use that is **declared**. This skill makes disclosure accurate, short and calm — and points the user to where AI hurts most (visible art) so they can decide what to improve.

## Language

Answer in the user's language. Write each disclosure in the language of the platform where it will appear (English for Steam/itch by default).

## Workflow

1. Read the "AI usage" section of `.agents/game-context.md`. If empty, ask for each category: code, in-game art, store/marketing art (capsule, screenshots, trailer), audio/music/voice, text/dialogue, live AI generation during play. Ask for specifics ("AI generated textures, then I painted over them").
2. **Map each use to each platform's rules** using `references/policies.md`. Mark: must disclose / likely must disclose / not required / unclear.
3. **Draft disclosures** for each platform the user publishes on (templates below).
4. **Risk review:** point out the highest-backlash items (usually AI art on the capsule, screenshots and trailer) and offer options: keep and disclose, restyle consistently, or replace with human-made/commissioned art for the store assets first.
5. Update the "AI usage" section in `.agents/game-context.md`.

## Templates

**Steam (Content Survey, AI section) — pre-generated content**
> We used AI tools to help create <specific assets, e.g. "some background textures and placeholder sound effects">. All content was reviewed and edited by us. <If applicable: "Store page art and screenshots are made by hand.">

**Steam — live-generated content** (only if the game generates content with AI during play)
> The game uses AI to generate <what> during play. We use <guardrails> to prevent illegal or infringing content.

**itch.io** — set the Generative AI disclosure field and tick the matching sub-tags (Graphics / Sound / Text & Dialog / Code). Add one line in the description:
> Made with help from AI tools for <code/art/…>. Design, <x> and <y> are hand-made.

**Reddit / social posts** (when rules require it, e.g. r/IndieGaming)
> Disclosure: I used AI for <specifics>; <what is hand-made>.

## Rules

- Never write text that hides, minimizes or misstates AI use. If the user asks to hide it, explain the risks (platform rules, post removal, "discovered" backlash) and offer an honest version.
- Be specific, not apologetic. "AI-assisted code; hand-painted art" beats "we used some AI".
- Steam rules about code are a gray area (see references). Tell the user to read the current Steamworks form and answer it truthfully themselves; don't assert a final legal answer.
- When citing the sales impact data, say it is correlation, not proof of cause.
