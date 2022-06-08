from django.apps import AppConfig

from main import settings


class AlgoTodayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'algo_today'

class RandomNumConfig(AppConfig):
    name = 'algo_today'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator
            operator.start()