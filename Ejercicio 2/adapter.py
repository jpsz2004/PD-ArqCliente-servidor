from models import Metric

class LegacyAPI:
    """
    Simula una API legada de monitoreo.

    Esta API devuelve la información en un formato antiguo,
    distinto al formato que espera nuestro sistema.
    """

    def get_server_data(self) -> dict:
        """
        Retorna datos del servidor en formato legado.

        Returns:
            dict: Diccionario con el uso de CPU en una clave antigua.
        """
        return {"cpu_usage_percent": 65.0}


class LegacyAdapter:
    """
    Adaptador que transforma la respuesta de LegacyAPI
    al formato interno que utiliza el sistema.

    Convierte datos heredados en objetos Metric.
    """

    def __init__(self, legacy_api: LegacyAPI):
        """
        Inicializa el adaptador con una instancia de la API legada.

        Args:
            legacy_api (LegacyAPI): API externa en formato antiguo.
        """
        self.legacy_api = legacy_api

    def get_metric(self) -> Metric:
        """
        Obtiene los datos desde la API legada y los convierte
        en un objeto Metric.

        Returns:
            Metric: Métrica adaptada al formato interno del sistema.
        """
        data = self.legacy_api.get_server_data()
        cpu_value = data["cpu_usage_percent"]

        return Metric(
            name="CPU",
            value=cpu_value,
            unit="%"
        )