from abc import ABC, abstractmethod


class ReservationObserver(ABC):
    """
    Interfaz para los observadores de una reserva.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Recibe una notificación relacionada con la reserva.
        """
        pass