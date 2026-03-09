from reservation import ReservationBuilder
from pricing import EconomyPricing
from notifiers import EmailNotifier, SMSNotifier


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

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

reservation.add_observer(email_notifier)
reservation.add_observer(sms_notifier)

print(reservation)
print("Precio final:", reservation.calculate_price())

reservation.confirm()
reservation.check_in()
reservation.cancel()