import pytest
from api.clients.booking_client import BookingClient


client = BookingClient()


def test_get_booking_returns_200():
    """GET a known booking and check status and shape."""
    response = client.get_booking(1)

    assert response.status_code == 200
    body = response.json()
    assert "firstname" in body
    assert "bookingdates" in body


def test_create_booking_returns_new_id():
    """POST a new booking and verify it returns a booking ID."""
    payload = {
        "firstname": "Aswini",
        "lastname": "S",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-05"
        }
    }

    response = client.create_booking(payload)

    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == "Aswini"


def test_get_all_bookings_returns_list():
    """GET all bookings and confirm non-empty list."""
    response = client.get_all_bookings()

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
