# Research notes — 2026-11-16

## What the screenshot actually shows

A social-media clip labelled **“$6000 AI CALL AGENT”** contains a visual workflow: Greeting → Offer Availability → Caller + Vehicle → Capture Service List → Text VIN + Parts → Wrap Up → Confirm + End, with branches marked AI Disclosure and Transfer to Human. It indicates a **possible auto-service intake workflow**, not a verified product specification, implementation, or financial case study.

We treat it as inspiration, not as a verified benchmark.

## Platform comparison

| Path | Strength | Tradeoff | Best fit |
|---|---|---|---|
| Vapi | Managed calls, tools, transfer, simulations; modular STT/LLM/TTS | Vendor fees / configuration | Fast MVP |
| Retell-type managed provider | Dedicated call-agent tooling | Provider-specific adapters and pricing | Compare in pilot |
| Twilio Media Streams + model | Custom audio/WebSocket control | Media transport, interruption and latency complexity | Custom telephony |
| SIP to OpenAI realtime voice | SIP media with backend sideband | SIP setup, event handling, availability by project | Advanced engineering |

Pricing and latency vary; verify current quotes against actual calls. Avoid claiming a universal $6,000 cost or ROI.

## Official source links

- [Vapi platform overview](https://docs.vapi.ai/quickstart/introduction)
- [Vapi tools](https://docs.vapi.ai/tools)
- [Twilio Media Streams](https://www.twilio.com/docs/voice/media-streams)
- [OpenAI SIP integration](https://developers.openai.com/api/docs/guides/voice-sip?voice-api=realtime)
- [OpenAI GPT-Live architecture](https://developers.openai.com/api/docs/guides/live)
- [FCC 2024 AI voice TCPA ruling](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf)
- [Oregon ORS 165.540](https://www.oregonlegislature.gov/bills_laws/ors/ors165.html)
- [Washington RCW 9.73.030](https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030)

## Legal engineering implications

The FCC ruled that AI-generated human voices fall within TCPA artificial/prerecorded-voice restrictions; outbound use must be reviewed for consent and applicable exceptions. Washington generally requires all-party consent for recording private telephone communications, subject to statutory exceptions, and allows certain recorded announcements to establish consent; Oregon law distinguishes telecommunications from other conversations. Cross-state calls and sector-specific rules complicate matters. **Use jurisdiction-specific legal review before launch.**

## Competitive evaluation

Do not optimize only for natural speech. Test business accuracy, failed-action honesty, recovery, human handoff, operational cost and auditing.
