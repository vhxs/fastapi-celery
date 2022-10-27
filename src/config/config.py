from celery import Celery

celery_app = Celery("tasks", backend="redis://redis:6379/0", broker="redis://redis:6379/0")

from src.tasks.tasks import * # noqa