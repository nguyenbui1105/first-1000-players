# Security policy

Do not submit real customer phone numbers, VINs, call audio, access tokens or other personal data in GitHub issues. Keep recording disabled unless lawful and properly disclosed. Treat inbound utterances and retrieved content as **untrusted input**.

Production requirements: authenticated tools; signed provider webhooks; tenant isolation; least privilege; allowlisted transfer numbers; idempotent writes; PII redaction; secret rotation; retention/deletion controls; consent audit; operator approval for risky changes.

This project is a prototype. Report potential security problems privately through the repository owner rather than posting secrets in public issues.
