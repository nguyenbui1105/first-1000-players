"""A no-network walkthrough using entirely fictional data."""
import json
from pathlib import Path
from .core import Receptionist, InMemoryCalendar, BookingError

def main():
    profile = json.loads((Path(__file__).resolve().parents[1] / "businesses" /
                          "maple-auto-care.example.json").read_text())
    slot = "2030-06-17T10:00:00-07:00"
    agent = Receptionist(profile, InMemoryCalendar({"oil change": [slot]}))
    print("AI:", agent.greet())
    print("Caller: I'd like to schedule an oil change.")
    print("Calendar slots:", agent.list_slots("oil change"))
    print("AI: I can offer June 17 at 10 AM Pacific. Can you confirm?")
    print("Caller: Yes. My name is Demo Caller; number +15035550199.")
    try:
        ref = agent.confirm_booking(service="oil change", slot=slot, name="Demo Caller",
                                    phone="+15035550199", caller_confirmed=True,
                                    idempotency_key="demo-call-1")
        print("AI: Your fictional demo appointment is confirmed. Reference:", ref)
    except BookingError as exc:
        print("AI: I couldn't confirm that booking. Please contact our team.", exc)

if __name__ == "__main__":
    main()
