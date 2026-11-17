---
name: appointment-scheduling
description: Check live availability, obtain permission, and book only after transactional confirmation.
---
# Appointment scheduling
**Trigger:** Caller wants an appointment, reschedule, or cancellation.
**Collect:** Service, preferred time/date/timezone, name and callback number as necessary.
**Process:** (1) Validate service and date. (2) Query authoritative calendar. (3) Offer actual returned slots, never invented ones. (4) Read back details. (5) Obtain explicit “yes.” (6) Commit using idempotency key. (7) Read real confirmation ID.
**Failure paths:** Missing info -> one question; no slot -> alternatives; timeout/conflict -> do NOT claim success, recheck and/or callback; caller changes mind -> stop.
**Reschedule/cancel:** Require authorized lookup and explicit confirmation; never treat a request as an executed cancellation.
**Acceptance:** Zero “confirmed” responses without successful booking result. Duplicate retries cannot create duplicate bookings.
