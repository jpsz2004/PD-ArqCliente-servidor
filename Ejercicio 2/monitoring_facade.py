from models import Alert, MonitoringConfig
from adapter import LegacyAdapter
from observer import AlertObserver


class MonitoringFacade:
    """
    Fachada principal del sistema de monitoreo.
    """

    def __init__(self, adapter: LegacyAdapter):
        self.adapter = adapter
        self.config = MonitoringConfig()
        self.observers = []

    def add_observer(self, observer: AlertObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self, alert: Alert) -> None:
        for observer in self.observers:
            observer.update(alert)

    def check_system(self) -> None:
        metric = self.adapter.get_metric()
        threshold = self.config.get_cpu_threshold()

        print(f"Métrica obtenida: {metric}")
        print(f"Umbral configurado: {threshold}%")

        if metric.value > threshold:
            alert = Alert(
                message="La CPU superó el umbral permitido",
                metric_name=metric.name,
                current_value=metric.value,
                threshold=threshold
            )
            self.notify_observers(alert)
        else:
            print("El sistema funciona dentro de los parámetros normales.")