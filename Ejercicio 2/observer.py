from abc import ABC, abstractmethod
from models import Alert


class AlertObserver(ABC):
    """
    Interfaz abstracta para los observadores de alertas.

    Cualquier clase que quiera reaccionar ante una alerta
    debe implementar el método update().
    """

    @abstractmethod
    def update(self, alert: Alert) -> None:
        """
        Recibe una alerta y ejecuta una acción en respuesta.

        Args:
            alert (Alert): La alerta generada por el sistema.
        """
        pass


class EmailAlert(AlertObserver):
    """
    Observador concreto que simula el envío de alertas por correo electrónico.
    """

    def update(self, alert: Alert) -> None:
        """
        Simula el envío de una alerta por email.

        Args:
            alert (Alert): La alerta recibida.
        """
        print("Enviando alerta por email...")
        print(alert)