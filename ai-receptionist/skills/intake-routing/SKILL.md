---
name: intake-routing
description: Determine intent and route callers without locking into rigid scripts.
---
# Intake and routing
**Trigger:** After disclosure, or when caller changes topic.
**Intent classes:** FAQ; book; reschedule; cancel; order/status; callback; human; unknown.
**Process:** Listen fully. Ask at most one question at a time. If two intents are present, acknowledge both and prioritize urgent/human. Capture only details needed for action. Confirm high-impact interpretations.
**Output:** structured intent + confidence + collected fields.
**Escalate:** Repeated recognition failures, unsupported requests, abuse, emergencies, or demand for human.
**Acceptance:** Never invent an intent-specific action from low-confidence utterances.
