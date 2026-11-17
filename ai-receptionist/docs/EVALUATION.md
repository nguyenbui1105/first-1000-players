# Quality gates and business metrics

## Release-blocking checks

- AI identity is disclosed at start.
- 0 unsupported/fictional bookings.
- 0 sensitive data in basic logs.
- 100% of booking actions pass explicit authorization gate.
- 100% of duplicate idempotency retries do not create extra bookings.
- Human handoff is offered after repeated failure or on request.

## Field metrics

| Metric | Calculation | Suggested pilot acceptance |
|---|---|---|
| Correct action rate | Verified correct actions / requested actions | Set target with owner |
| False-confirmation rate | False successful claims / action attempts | **0** |
| Handoff availability | Completed human routes / requested routes | Monitor |
| Booking collision rate | Conflicting attempts / booking attempts | Monitor |
| Caller task resolution | Resolved sessions / eligible calls | Compare to human baseline |
| p95 response latency | Audio turn latency distribution | Measure on real carrier |
| Cost per resolved call | Provider+telephony+infra cost / resolved | Estimate from pilot |

Run a consented test set: ≥50 calls across happy path, no availability, ambiguous service, corrections, multilingual speakers, noise, interrupted speech, transfer failure, system outage, and explicit refusal to record. Numbers above are testing recommendations, not measured performance.
