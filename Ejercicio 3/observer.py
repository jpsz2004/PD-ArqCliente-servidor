"""
Módulo del patrón Observer para notificaciones del sistema.

Implementa el patrón Observer que permite notificar
a estudiantes cuando ocurren eventos relevantes en un curso.
"""

from abc import ABC, abstractmethod
from models import Student


class Observer(ABC):
    """
    Interfaz abstracta para los observadores.
    
    Cualquier clase que quiera reaccionar ante eventos
    debe implementar el método update().
    """
    
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Recibe una notificación y ejecuta una acción.
        
        Args:
            message (str): Mensaje de notificación.
        """
        pass


class StudentObserver(Observer):
    """
    Observador concreto que representa a un estudiante.
    
    Recibe notificaciones sobre eventos del curso.
    """
    
    def __init__(self, student: Student):
        """
        Inicializa el observador para un estudiante.
        
        Args:
            student (Student): Estudiante a notificar.
        """
        self.student = student
    
    def update(self, message: str) -> None:
        """
        Notifica al estudiante con un mensaje.
        
        Args:
            message (str): Mensaje de notificación.
        """
        print(f"Notificación para {self.student.name}: {message}")


class Course:
    """
    Representa un curso que notifica a sus observadores.
    
    Implementa el patrón Subject del Observer pattern,
    manteniendo una lista de observadores suscritos.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un curso.
        
        Args:
            name (str): Nombre del curso.
        """
        self.name = name
        self.observers = []
    
    def subscribe(self, observer: Observer) -> None:
        """
        Suscribe un observador al curso.
        
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
