from abc import ABC, abstractmethod

# =========================================================
# OBSERVER PATTERN
# Notificación de calificaciones
# =========================================================

class Observer(ABC):

    @abstractmethod
    def update(self, message):
        pass


class StudentObserver(Observer):

    def __init__(self, student):
        self.student = student

    def update(self, message):
        print(f"Notificación para {self.student.name}: {message}")


class Course:

    def __init__(self, name):
        self.name = name
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
