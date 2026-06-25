import requests


class BookingClient:
    """API client for the Restful-Booker booking endpoints."""

    BASE_URL = "https://restful-booker.herokuapp.com"

    def get_booking(self, booking_id: int):
        """GET a single booking by ID."""
        return requests.get(f"{self.BASE_URL}/booking/{booking_id}")

    def get_all_bookings(self):
        """GET all bookings."""
        return requests.get(f"{self.BASE_URL}/booking")

    def create_booking(self, payload: dict):
        """POST a new booking."""
        return requests.post(f"{self.BASE_URL}/booking", json=payload)
