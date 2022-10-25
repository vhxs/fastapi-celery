from celery import Celery
from time import sleep

celery_app = Celery("test", backend="redis://redis:6379/0", broker="redis://redis:6379/0")

@celery_app.task
def execute_task(idt: str):
    print(f"{idt} starting")
    sleep(10)
    print(f"{idt} stopping")