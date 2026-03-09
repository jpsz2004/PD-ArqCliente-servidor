from reservation_state import ReservationState


class PendingState(ReservationState):
    """
    Estado pendiente de una reserva.
    """

    def confirm(self, reservation) -> None:
        """
        Confirma la reserva y la cambia al estado confirmado.
        """
        print("La reserva ha sido confirmada.")
        reservation.set_state("ConfirmedState")

    def cancel(self, reservation) -> None:
        """
        Cancela la reserva y la cambia al estado cancelado.
        """
        print("La reserva ha sido cancelada.")
        reservation.set_state("CancelledState")

    def check_in(self, reservation) -> None:
        """
        No permite check-in si la reserva aún está pendiente.
        """
        print("No se puede hacer check-in en una reserva pendiente.")


class ConfirmedState(ReservationState):
    """
    Estado confirmado de una reserva.
    """

    def confirm(self, reservation) -> None:
        """
        Informa que la reserva ya está confirmada.
        """
        print("La reserva ya está confirmada.")

    def cancel(self, reservation) -> None:
        """
        Cancela una reserva confirmada.
        """
        print("La reserva confirmada ha sido cancelada.")
        reservation.set_state("CancelledState")

    def check_in(self, reservation) -> None:
        """
        Realiza el check-in de la reserva confirmada.
        """
        print("Check-in realizado correctamente.")



class CancelledState(ReservationState):
    """
    Estado cancelado de una reserva.
    """

    def confirm(self, reservation) -> None:
        """
        No permite confirmar una reserva cancelada.
        """
        print("No se puede confirmar una reserva cancelada.")

    def cancel(self, reservation) -> None:
        """
        Informa que la reserva ya está cancelada.
        """
        print("La reserva ya está cancelada.")

    def check_in(self, reservation) -> None:
        """
        No permite check-in en una reserva cancelada.
        """
        print("No se puede hacer check-in en una reserva cancelada.")