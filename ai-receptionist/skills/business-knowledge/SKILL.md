---
name: business-knowledge
description: Answer service and policy questions from a verified business profile.
---
# Grounded business knowledge
**Trigger:** Hours, address, pricing, services, warranty, or policies.
**Inputs:** Approved business profile with updated_at and provenance.
**Process:** Read exact configured facts; clarify which location/service. Quote only approved prices; distinguish estimate from final quote.
**Fallback:** Say “I don't have that confirmed; I can ask the team to follow up.”
**Do not:** fill gaps from common industry knowledge or promise undocumented policies.
**Acceptance:** Zero unsupported prices, opening hours, or guarantees.
