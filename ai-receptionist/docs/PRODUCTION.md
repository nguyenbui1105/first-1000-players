# Deployment / security checklist

This repository **does not place real calls**. Before production:

- [ ] Pick jurisdiction(s); obtain counsel review for recording disclosures, TCPA, privacy, sector rules.
- [ ] Purchase/port phone number and connect provider; enable inbound only first.
- [ ] Configure verified business hours/services/location/prices with owner and last-review date.
- [ ] Implement calendar integration with atomic reservation and idempotency in DB.
- [ ] Validate webhook signatures, enforce tool auth scopes and rate limits.
- [ ] Implement secure secrets store; never add keys to repo or prompt context.
- [ ] Implement call transfer with destination allowlist and observable success/failure.
- [ ] Set recording **off by default** until policy and consent mechanism verified.
- [ ] Define retention, deletion, access logging, data residency and incident response.
- [ ] Separate transactional notices from opt-in marketing; prove SMS authorization.
- [ ] Test daylight savings / timezone changes / overlapping slots / retries.
- [ ] Run scenario suite and failure injection; review unsafe claims.
- [ ] Pilot with staff/test callers; measure quality, cost, end-to-end latency.
- [ ] Configure human on-call fallback and business-hours policy.

## Suggested milestone sequence

**M0:** Offline policy + tests (this repo).  
**M1:** Provider sandbox + one tool using mock data.  
**M2:** Transactional calendar + authorization + monitoring.  
**M3:** Limited inbound pilot + human escalation.  
**M4:** Multi-tenant controls and tenant-specific evaluation.

Never let a prompt act as an authorization system.
