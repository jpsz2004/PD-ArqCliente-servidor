from reservation import ReservationBuilder


reservation = (
    ReservationBuilder()
    .set_passenger_name("Juan Sanchez")
    .set_flight_number("AV123")
    .set_seat("12A")
    .set_base_price(500.0)
    .add_extra("Equipaje extra")
    .set_preferences("Ventana")
    .build()
)

print(reservation)

reservation.check_in()
reservation.confirm()
print(reservation)

reservation.check_in()
reservation.cancel()
print(reservation)

reservation.confirm()