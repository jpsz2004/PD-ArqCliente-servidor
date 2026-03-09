from abc import ABC, abstractmethod


class ReservationState(ABC):
    """
    Interfaz para los estados de una reserva.
    """

    @abstractmethod
    def confirm(self, reservation) -> None:
        """
        Confirma la reserva.
        """
        pass

    @abstractmethod
    def cancel(self, reservation) -> None:
        """
        Cancela la reserva.
        """
        pass

    @abstractmethod
    def check_in(self, reservation) -> None:
        """
        Realiza el check-in de la reserva.
        """
        pass