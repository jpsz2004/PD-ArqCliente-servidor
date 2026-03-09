from reservation import ReservationBuilder
from pricing import EconomyPricing
from notifiers import EmailNotifier, SMSNotifier


def main():
    print("=== Sistema de Reservas de Aerolínea ===\n")

    # Builder: construir reserva
    reservation = (
        ReservationBuilder()
        .set_passenger_name("Juan Sanchez")
        .set_flight_number("AV123")
        .set_seat("12A")
        .set_base_price(500)
        .add_extra("Equipaje extra")
        .set_preferences("Ventana")
        .build()
    )

    print("Reserva creada:")
    print(reservation)
    print()

    # Strategy: asignar estrategia de precio
    reservation.set_pricing_strategy(EconomyPricing())
    print("Precio final:", reservation.calculate_price())
    print()

    # Observer: agregar notificadores
    email = EmailNotifier()
    sms = SMSNotifier()

    reservation.add_observer(email)
    reservation.add_observer(sms)

    print("Notificadores agregados\n")

    # State: cambiar estados
    print("Confirmando reserva...")
    reservation.confirm()
    print()

    print("Realizando check-in...")
    reservation.check_in()
    print()

    print("Cancelando reserva...")
    reservation.cancel()
    print()

    print("Estado final:")
    print(reservation)


if __name__ == "__main__":
    main()