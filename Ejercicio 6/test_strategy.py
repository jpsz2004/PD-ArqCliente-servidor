from reservation import ReservationBuilder
from pricing import EconomyPricing, PremiumPricing


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

reservation.set_pricing_strategy(EconomyPricing())
print("Precio económico:", reservation.calculate_price())

reservation.set_pricing_strategy(PremiumPricing())
print("Precio premium:", reservation.calculate_price())