from dataclasses import dataclass, field
from typing import List, Optional

from states import PendingState, ConfirmedState, CancelledState


@dataclass
class Reservation:
    """
    Representa una reserva de vuelo.

    Atributos:
        passenger_name (str): Nombre del pasajero.
        flight_number (str): Número del vuelo.
        seat (str): Asiento asignado.
        base_price (float): Precio base de la reserva.
        extras (List[str]): Servicios adicionales contratados.
        preferences (str): Preferencias del pasajero.
        state (Optional[object]): Estado actual de la reserva.
        pricing_strategy (Optional[object]): Estrategia de cálculo de precio.
        observers (List[object]): Observadores registrados para notificaciones.
    """
    passenger_name: str
    flight_number: str
    seat: str
    base_price: float
    extras: List[str] = field(default_factory=list)
    preferences: str = ""
    state: Optional[object] = None
    pricing_strategy: Optional[object] = None
    observers: List[object] = field(default_factory=list)

    def __post_init__(self):
        """
        Inicializa la reserva con estado pendiente por defecto.
        """
        if self.state is None:
            self.state = PendingState()

    def set_pricing_strategy(self, pricing_strategy: object) -> None:
        """
        Asigna la estrategia de cálculo de precio.
        """
        self.pricing_strategy = pricing_strategy

    def calculate_price(self) -> float:
        """
        Calcula el precio final de la reserva usando la estrategia asignada.
        """
        if self.pricing_strategy is None:
            raise ValueError("No se ha definido una estrategia de precio para la reserva.")

        return self.pricing_strategy.calculate_price(self.base_price)

    def set_state(self, state_name: str) -> None:
        """
        Cambia el estado actual de la reserva según el nombre recibido.

        Args:
            state_name (str): Nombre del nuevo estado.
        """
        if state_name == "ConfirmedState":
            self.state = ConfirmedState()
        elif state_name == "CancelledState":
            self.state = CancelledState()

    def confirm(self) -> None:
        """
        Delega la confirmación al estado actual.
        """
        self.state.confirm(self)

    def cancel(self) -> None:
        """
        Delega la cancelación al estado actual.
        """
        self.state.cancel(self)

    def check_in(self) -> None:
        """
        Delega el check-in al estado actual.
        """
        self.state.check_in(self)

    def __str__(self) -> str:
        """
        Devuelve una representación legible de la reserva.
        """
        return (
            f"Reserva de {self.passenger_name} | "
            f"Vuelo: {self.flight_number} | "
            f"Asiento: {self.seat} | "
            f"Precio base: {self.base_price} | "
            f"Extras: {self.extras} | "
            f"Preferencias: {self.preferences} | "
            f"Estado: {self.state.__class__.__name__}"
        )


# ---------- BUILDER ----------

class ReservationBuilder:
    """
    Builder para construir objetos Reservation paso a paso.
    """

    def __init__(self):
        """
        Inicializa el builder con valores por defecto.
        """
        self.passenger_name = ""
        self.flight_number = ""
        self.seat = ""
        self.base_price = 0.0
        self.extras = []
        self.preferences = ""

    def set_passenger_name(self, name: str):
        """
        Asigna el nombre del pasajero.
        """
        self.passenger_name = name
        return self

    def set_flight_number(self, flight_number: str):
        """
        Asigna el número de vuelo.
        """
        self.flight_number = flight_number
        return self

    def set_seat(self, seat: str):
        """
        Asigna el asiento.
        """
        self.seat = seat
        return self

    def set_base_price(self, price: float):
        """
        Asigna el precio base de la reserva.
        """
        self.base_price = price
        return self

    def add_extra(self, extra: str):
        """
        Agrega un servicio adicional.
        """
        self.extras.append(extra)
        return self

    def set_preferences(self, preferences: str):
        """
        Asigna las preferencias del pasajero.
        """
        self.preferences = preferences
        return self

    def build(self) -> Reservation:
        """
        Construye y retorna una instancia de Reservation.
        """
        return Reservation(
            passenger_name=self.passenger_name,
            flight_number=self.flight_number,
            seat=self.seat,
            base_price=self.base_price,
            extras=self.extras,
            preferences=self.preferences
        )