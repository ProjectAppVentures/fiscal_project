from django.apps import AppConfig


class FiscalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fiscal_app'

    def ready(self):
        # Registers the artifact retention guard (pre_delete).
        from . import signals  # noqa: F401

        # Huey autodiscovers `tasks` modules of installed apps only; Fiscal.'s live in the project package, so the
        # worker (`run_huey`) would start without the transmission, retry, alert and notice tasks. Load them here.
        import fiscal_project.tasks  # noqa: F401
