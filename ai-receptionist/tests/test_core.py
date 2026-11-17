import json
import unittest
from pathlib import Path
from receptionist import Receptionist, InMemoryCalendar, BookingError

SLOT = "2030-06-17T10:00:00-07:00"
PHONE = "+15035550199"

class ReceptionistTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads((Path(__file__).resolve().parents[1] /
                                    "businesses" / "maple-auto-care.example.json").read_text())
        self.calendar = InMemoryCalendar({"oil change": [SLOT]})
        self.agent = Receptionist(self.profile, self.calendar)

    def book(self, **updates):
        data = dict(service="oil change", slot=SLOT, name="Demo Caller",
                    phone=PHONE, caller_confirmed=True, idempotency_key="call-1")
        data.update(updates)
        return self.agent.confirm_booking(**data)

    def test_disclosure_required(self):
        with self.assertRaisesRegex(BookingError, "disclosure"):
            self.book()

    def test_valid_booking_and_same_key_retry(self):
        self.agent.greet()
        a = self.book()
        self.assertTrue(a.startswith("DEMO-"))
        self.assertEqual(self.book(), a)
        self.assertEqual(len(self.calendar.booked), 1)

    def test_booking_requires_explicit_confirmation(self):
        self.agent.greet()
        with self.assertRaisesRegex(BookingError, "confirmation"):
            self.book(caller_confirmed=False)

    def test_unsupported_service(self):
        self.agent.greet()
        with self.assertRaisesRegex(BookingError, "Service"):
            self.book(service="engine replacement")

    def test_conflicting_slot_no_false_booking(self):
        self.agent.greet()
        self.book()
        with self.assertRaisesRegex(BookingError, "unavailable"):
            self.book(idempotency_key="another-call")

    def test_reused_idempotency_key_different_payload_rejected(self):
        self.agent.greet()
        self.book()
        with self.assertRaisesRegex(BookingError, "different"):
            self.book(name="Other Caller")

    def test_phone_validation(self):
        self.agent.greet()
        with self.assertRaisesRegex(BookingError, "phone"):
            self.book(phone="unknown")

    def test_timezone_aware_slot_required(self):
        self.agent.greet()
        with self.assertRaisesRegex(BookingError, "Timezone"):
            self.book(slot="2030-06-17T10:00:00")

    def test_human_request_fallback(self):
        self.agent.greet()
        self.assertEqual(self.agent.transfer()["status"], "callback_needed")

    def test_unknown_info_not_hallucinated(self):
        self.assertIn("don't have", self.agent.info("pricing"))

if __name__ == "__main__":
    unittest.main()
