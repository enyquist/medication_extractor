# third party libraries
from django.apps import AppConfig


class DemoConfig(AppConfig):
    """Demo Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "demo"
