from reservation import ReservationBuilder


reservation = (
    ReservationBuilder()
    .set_passenger_name("Juan Sanchez")
    .set_flight_number("AV123")
    .set_seat("12A")
    .set_base_price(500.0)
    .add_extra("Equipaje extra")
    .add_extra("Comida especial")
    .set_preferences("Asiento de ventana")
    .build()
)

print(reservation)