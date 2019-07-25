from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'apps.api.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

default_app_config = 'apps.api.authentication.AuthenticationAppConfig'
