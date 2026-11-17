# Skill catalog

Each folder is a human- and agent-readable **SKILL.md**. Skills are capabilities, **not** permission to execute transactions without backend validation.

| Skill | Trigger | Outcome |
|---|---|---|
| identity-disclosure | Every incoming call | Caller knows they are speaking with AI |
| intake-routing | After greeting | Route intent with minimal questions |
| business-knowledge | Hours, pricing, policy | Grounded response or graceful unknown |
| appointment-scheduling | Book/reschedule/cancel | Confirmed transaction or fallback |
| customer-and-asset | Capture customer, vehicle, VIN or order | Validated minimum necessary details |
| human-handoff | Request, urgency, repeated failure | Human transfer or callback |
| confirmations | Booking / important action | Read-back and explicit approval |
| follow-up-messaging | Caller opts into a text | Approved concise message |
| compliance-and-privacy | Every call, especially recording | Minimal data, notices, consent |
| conversation-quality | Throughout and wrap-up | Clear, concise, recoverable interaction |

Skills are **portable policy documents**, not a vendor-specific executable configuration.
