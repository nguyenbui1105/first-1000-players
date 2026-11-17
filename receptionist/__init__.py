"""ReceptionistOS: offline reference domain layer (not a live telephony client)."""
from .core import Receptionist, InMemoryCalendar, BookingError

__all__ = ["Receptionist", "InMemoryCalendar", "BookingError"]
