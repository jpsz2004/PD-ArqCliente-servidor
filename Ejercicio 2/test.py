# from models import Metric, Alert, MonitoringConfig


# # Probar Metric
# metric = Metric("CPU", 85.0, "%")
# print(metric)

# # Probar Alert
# alert = Alert(
#     message="La CPU superó el umbral permitido",
#     metric_name="CPU",
#     current_value=85.0,
#     threshold=80.0
# )
# print(alert)

# # Probar Singleton
# config1 = MonitoringConfig()
# config2 = MonitoringConfig()

# print("¿Es la misma instancia?:", config1 is config2)

# config1.set_cpu_threshold(90.0)
# print("Umbral desde config2:", config2.get_cpu_threshold())}

# from models import Alert
# from observer import EmailAlert


# alert = Alert(
#     message="La CPU superó el umbral permitido",
#     metric_name="CPU",
#     current_value=85.0,
#     threshold=80.0
# )

# email_observer = EmailAlert()
# email_observer.update(alert)

from adapter import LegacyAPI, LegacyAdapter


legacy_api = LegacyAPI()
adapter = LegacyAdapter(legacy_api)

metric = adapter.get_metric()
print(metric)