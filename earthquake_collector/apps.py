from django.apps import AppConfig


class EarthquakeCollectorConfig(AppConfig):
    name = 'earthquake_collector'

    def ready(self):
        import earthquake_collector.signals
