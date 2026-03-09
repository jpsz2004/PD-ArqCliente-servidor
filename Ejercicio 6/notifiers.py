from reservation_observer import ReservationObserver


class EmailNotifier(ReservationObserver):
    """
    Observador concreto que simula el envío de notificaciones por correo.
    """

    def update(self, message: str) -> None:
        print(f"[EMAIL] {message}")




class SMSNotifier(ReservationObserver):
    """
    Observador concreto que simula el envío de notificaciones por SMS.
    """

    def update(self, message: str) -> None:
        print(f"[SMS] {message}")