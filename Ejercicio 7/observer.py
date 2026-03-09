"""
Módulo del patrón Observer para el sistema de alertas.

Implementa el patrón Observer que permite notificar
a múltiples observadores cuando ocurre un evento.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interfaz abstracta para los observadores de alertas.
    
    Cualquier clase que quiera reaccionar ante una alerta
    debe implementar el método update().
    """
    
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Recibe un mensaje de alerta y ejecuta una acción.
        
        Args:
            message (str): Mensaje de alerta.
        """
        pass


class EmailAlert(Observer):
    """
    Observador concreto que simula el envío de alertas por email.
    """
    
    def update(self, message: str) -> None:
        """
        Simula el envío de una alerta por correo electrónico.
        
        Args:
            message (str): Mensaje de alerta recibido.
        """
        print(f"[EMAIL] {message}")


class SMSAlert(Observer):
    """
    Observador concreto que simula el envío de alertas por SMS.
    """
    
    def update(self, message: str) -> None:
        """
        Simula el envío de una alerta por SMS.
        
        Args:
            message (str): Mensaje de alerta recibido.
        """
        print(f"[SMS] {message}")


class InventoryManager:
    """
    Gestor de observadores para el sistema de inventario.
    
    Mantiene una lista de observadores y los notifica
    cuando ocurre un evento relevante.
    """
    
    def __init__(self):
        """Inicializa el gestor con una lista vacía de observadores."""
        self.observers = []
    
    def subscribe(self, observer: Observer) -> None:
        """
        Suscribe un observador a las notificaciones.
        
        Args:
            observer (Observer): Observador a suscribir.
        """
        self.observers.append(observer)
    
    def unsubscribe(self, observer: Observer) -> None:
        """
        Cancela la suscripción de un observador.
        
        Args:
            observer (Observer): Observador a desuscribir.
        """
        self.observers.remove(observer)
    
    def notify(self, message: str) -> None:
        """
        Notifica a todos los observadores suscritos.
        
        Args:
            message (str): Mensaje a notificar.
        """
        for observer in self.observers:
            observer.update(message)
