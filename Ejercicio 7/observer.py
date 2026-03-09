from abc import ABC, abstractmethod

# =========================================================
# OBSERVER - ALERTAS DE STOCK
# =========================================================

class Observer(ABC):

    @abstractmethod
    def update(self, message):
        pass


class EmailAlert(Observer):

    def update(self, message):
        print(f"[EMAIL] {message}")


class SMSAlert(Observer):

    def update(self, message):
        print(f"[SMS] {message}")


class InventoryManager:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, message):

        for observer in self.observers:
            observer.update(message)
