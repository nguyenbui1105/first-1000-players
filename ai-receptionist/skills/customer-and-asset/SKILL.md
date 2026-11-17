---
name: customer-and-asset
description: Collect minimum information needed for service, vehicles, orders and callbacks.
---
# Customer and asset intake
**Trigger:** Booking, vehicle troubleshooting, order lookup or callback.
**Fields:** Name, callback number, service type; auto-specific year/make/model and optionally VIN when needed.
**Rules:** Read VIN back character by character if captured; avoid public repetition of sensitive identifiers; use VIN check digit / official decoder integration if required. Prefer last few characters for verification when full VIN is not needed. Mask numbers in logs. Ask consent before saving an unrelated marketing contact.
**Fallback:** If a field cannot be verified, mark unverified and hand off; do not silently guess.
**Acceptance:** Required fields validated and optional fields genuinely optional.
