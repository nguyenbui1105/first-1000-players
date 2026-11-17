---
name: follow-up-messaging
description: Send transactional follow-up only with an appropriate authorization and verified destination.
---
# Transactional follow-up
**Trigger:** Caller explicitly requests a text or previously opted into necessary transactional notices.
**Process:** Validate number, authorized purpose, message template and rate limits. Send through server-side adapter. Report delivery accepted, not guaranteed delivery.
**Do not:** silently enroll marketing lists or assume transactional consent covers promotional messages.
**Fallback:** Offer verbal summary or human callback.
**Acceptance:** No unsolicited marketing; no invented confirmation links.
