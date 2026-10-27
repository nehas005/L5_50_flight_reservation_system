
import hashlib
import secrets
from pathlib import Path

FLIGHTS = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}

total_revenue = 0.0


def book_flight_seat(
    flight_no,
    passenger,
    luggage_weight=15,
    baggage_tags=None,
):
    """Book an available seat and record its baggage tag."""
    global total_revenue

    if baggage_tags is None:
        baggage_tags = []

    flight = FLIGHTS.get(flight_no)
    if flight is None or flight["is_full"] or flight["seats"] <= 0:
        return False

    flight["seats"] -= 1
    flight["is_full"] = flight["seats"] <= 0
    total_revenue += flight["fare"]

    baggage_tags.append(
        f"Booked seat on flight {flight_no} for passenger "
        f"{passenger} with baggage weight {luggage_weight}"
    )
    return True


def cancel_booking(flight_no):
    """Cancel a booking by restoring one available seat."""
    flight = FLIGHTS.get(flight_no)
    if flight is None:
        return False

    flight["seats"] += 1
    flight["is_full"] = False
    return True


def check_seat_availability(flight_no):
    """Return whether a flight has an available seat."""
    flight = FLIGHTS.get(flight_no)
    return flight is not None and not flight["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate=0.15):
    """Calculate the baggage surcharge from the flight fare."""
    flight = FLIGHTS.get(flight_no)
    if flight is None:
        raise ValueError(f"Unknown flight number: {flight_no}")
    if not 0 <= surcharge_rate <= 1:
        raise ValueError("Surcharge rate must be between 0 and 1.")

    base_fare = flight["fare"]
    return base_fare * surcharge_rate


def generate_passenger_hash(passenger_id):
    """Generate a SHA-256 digest of a passenger identifier."""
    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_flight_manifest(filename="flight_manifest.txt"):
    """Write the current flight data to a manifest file."""
    with Path(filename).open("w", encoding="utf-8") as manifest:
        manifest.write(str(FLIGHTS))

    print(f"Boarding manifest printed: {filename}")


def get_flight_summary():
    """Count flights that have available seats."""
    return sum(
        not flight["is_full"] and flight["seats"] > 0
        for flight in FLIGHTS.values()
    )


def main():
    """Run a demonstration of the reservation system."""
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")

    print("Is AI101 open:", check_seat_availability("AI101"))
    print("Baggage Fee:", calculate_baggage_fee("AI101"))
    print("Passenger Hash:", generate_passenger_hash("PASSPORT_IND_119"))
    print("Boarding PIN:", generate_boarding_pin())

    export_flight_manifest()
    print("Available flights:", get_flight_summary())


if __name__ == "__main__":
    main()
