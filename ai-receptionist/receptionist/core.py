"""Safe, deterministic business-action orchestration.

Natural-language understanding and telephony are intentionally OUT OF SCOPE here.
A voice model should call these domain methods through authenticated tools.
"""
from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Protocol
import re
import uuid

class BookingError(Exception):
    pass

class Calendar(Protocol):
    def slots(self, service: str) -> list[str]: ...
    def book(self, service: str, slot: str, name: str, phone: str, key: str) -> str: ...

@dataclass
class InMemoryCalendar:
    """Local demo only; NOT a concurrency-safe production calendar."""
    available: dict[str, list[str]]
    booked: dict[str, dict] = field(default_factory=dict)

    def slots(self, service: str) -> list[str]:
        return list(self.available.get(service, []))

    def book(self, service: str, slot: str, name: str, phone: str, key: str) -> str:
        if key in self.booked:
            record = self.booked[key]
            if (record["service"], record["slot"], record["name"], record["phone"]) != (service, slot, name, phone):
                raise BookingError("Idempotency key reused with different booking data")
            return record["confirmation_id"]
        if slot not in self.available.get(service, []):
            raise BookingError("Slot unavailable")
        self.available[service].remove(slot)
        confirmation_id = "DEMO-" + uuid.uuid4().hex[:8].upper()
        self.booked[key] = dict(service=service, slot=slot, name=name, phone=phone,
                                confirmation_id=confirmation_id)
        return confirmation_id

def valid_phone(phone: str) -> bool:
    """North American format for demo. Use libphonenumber in production."""
    return bool(re.fullmatch(r"\+1[2-9]\d{9}", phone))

@dataclass
class Receptionist:
    business: dict
    calendar: Calendar
    disclosed: bool = False
    recording_consent: bool = False

    def greet(self) -> str:
        self.disclosed = True
        return f"Thank you for calling {self.business['name']}. I'm an AI assistant. How can I help?"

    def info(self, field_name: str) -> str:
        if field_name not in ("hours", "location", "services", "phone"):
            return "I don't have that information confirmed. I can arrange a callback."
        value = self.business.get(field_name)
        return str(value) if value else "I don't have that information confirmed. I can arrange a callback."

    def list_slots(self, service: str) -> list[str]:
        self._require_greeting()
        if service not in self.business.get("services", []):
            raise BookingError("Service not verified")
        return self.calendar.slots(service)

    def confirm_booking(self, *, service: str, slot: str, name: str, phone: str,
                        caller_confirmed: bool, idempotency_key: str) -> str:
        self._require_greeting()
        if not caller_confirmed:
            raise BookingError("Explicit caller confirmation required")
        if not name.strip() or len(name) > 120:
            raise BookingError("Invalid customer name")
        if not valid_phone(phone):
            raise BookingError("Invalid demo phone; expected +1XXXXXXXXXX")
        if service not in self.business.get("services", []):
            raise BookingError("Service not verified")
        if not idempotency_key or len(idempotency_key) > 128:
            raise BookingError("Valid idempotency key required")
        tz = ZoneInfo(self.business["timezone"])
        try:
            timestamp = datetime.fromisoformat(slot)
        except ValueError as exc:
            raise BookingError("Invalid slot format") from exc
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise BookingError("Timezone-aware slot required")
        # Do not fabricate, mutate or silently normalize the authoritative slot.
        if slot not in self.calendar.slots(service):
            # A retry must go to the calendar, which handles idempotency itself.
            pass
        try:
            return self.calendar.book(service, slot, name.strip(), phone, idempotency_key)
        except BookingError:
            raise

    def _require_greeting(self) -> None:
        if not self.disclosed:
            raise BookingError("AI disclosure must precede business actions")

    def transfer(self) -> dict:
        self._require_greeting()
        if not self.business.get("human_transfer_enabled", False):
            return {"status": "callback_needed", "message": "I can ask our team to call you back."}
        return {"status": "provider_action_required", "message": "I'll try to connect you with the team."}
