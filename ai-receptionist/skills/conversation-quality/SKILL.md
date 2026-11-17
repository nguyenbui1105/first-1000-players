---
name: conversation-quality
description: Keep phone dialogue brief, natural, robust to interruption and measurable.
---
# Conversation quality
**Trigger:** Every speech turn.
**Process:** Short spoken sentences, one question at a time, summarize complex details, pause for interruptions, adapt to language. Distinguish silence, hangup, tool wait and utterance uncertainty. Recover from interruptions without repeating private information unnecessarily.
**Metrics:** Task success, unsupported claims, turn count, transfer attempt/completion, p50/p95 latency, booking collision, caller correction, callback completion.
**Fallback:** After two failures, ask whether the caller wants a person.
**Acceptance:** Evaluations cover accents, background noise, noisy vehicle names, corrections, overtalk and hangups.
