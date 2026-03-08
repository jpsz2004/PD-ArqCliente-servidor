from adapter import LegacyAPI, LegacyAdapter
from observer import EmailAlert
from monitoring_facade import MonitoringFacade
from models import MonitoringConfig

def main():
    config = MonitoringConfig()
    config.set_cpu_threshold(80.0)

    legacy_api = LegacyAPI()
    adapter = LegacyAdapter(legacy_api)

    facade = MonitoringFacade(adapter)

    email_alert = EmailAlert()
    facade.add_observer(email_alert)

    facade.check_system()


if __name__ == "__main__":
    main()