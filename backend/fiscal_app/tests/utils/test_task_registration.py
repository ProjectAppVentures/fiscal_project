"""Tests that the Huey worker knows Fiscal.'s tasks (they live in fiscal_project/tasks.py, outside any app)."""

from django.conf import settings

FISCAL_TASKS = (
    'fiscal_project.tasks.transmit_due',
    'fiscal_project.tasks.transmit_due_every_minute',
    'fiscal_project.tasks.deliver_pending_webhooks',
    'fiscal_project.tasks.worker_heartbeat',
    'fiscal_project.tasks.check_alerts',
    'fiscal_project.tasks.check_test_sets',
)


def test_worker_registers_the_fiscal_tasks():
    """Fails if `run_huey` starts without the transmission, retry, notice, alert and test-set tasks.

    Huey only autodiscovers `tasks` modules of installed apps; without the import in FiscalAppConfig.ready the worker
    of production would never retry a document, poll a contingency or raise an alert.
    """
    registered = set(settings.HUEY._registry._registry)

    assert set(FISCAL_TASKS) <= registered
