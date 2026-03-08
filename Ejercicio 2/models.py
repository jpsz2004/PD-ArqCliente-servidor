from dataclasses import dataclass


@dataclass
class Metric:
    """
    Representa una métrica obtenida del sistema de monitoreo.

    Atributos:
        name (str): Nombre de la métrica. Ejemplo: 'CPU'
        value (float): Valor actual de la métrica. Ejemplo: 85.0
        unit (str): Unidad de medida. Ejemplo: '%'
    """
    name: str
    value: float
    unit: str

    def __str__(self) -> str:
        """
        Devuelve una representación legible de la métrica.
        """
        return f"{self.name}: {self.value}{self.unit}"


@dataclass
class Alert:
    """
    Representa una alerta generada por el sistema de monitoreo.

    Atributos:
        message (str): Mensaje descriptivo de la alerta.
        metric_name (str): Nombre de la métrica que provocó la alerta.
        current_value (float): Valor actual detectado.
        threshold (float): Umbral configurado para esa métrica.
    """
    message: str
    metric_name: str
    current_value: float
    threshold: float

    def __str__(self) -> str:
        """
        Devuelve una representación legible de la alerta.
        """
        return (
            f"ALERTA -> {self.message} | "
            f"Métrica: {self.metric_name} | "
            f"Valor actual: {self.current_value} | "
            f"Umbral: {self.threshold}"
        )


class MonitoringConfig:
    """
    Clase Singleton que centraliza la configuración del sistema de monitoreo.

    Esta clase garantiza que solo exista una única instancia
    de configuración durante toda la ejecución del programa.

    Atributos:
        cpu_threshold (float): Umbral máximo permitido para CPU.
    """

    _instance = None

    def __new__(cls):
        """
        Controla la creación de instancias para implementar el patrón Singleton.
        Si no existe una instancia, la crea.
        Si ya existe, devuelve la misma instancia.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cpu_threshold = 80.0
        return cls._instance

    def get_cpu_threshold(self) -> float:
        """
        Retorna el umbral actual de CPU.
        """
        return self.cpu_threshold

    def set_cpu_threshold(self, value: float) -> None:
        """
        Actualiza el umbral de CPU.

        Args:
            value (float): Nuevo valor del umbral.
        """
        self.cpu_threshold = value