from time import sleep

from src.config.config import celery_app


@celery_app.task
def execute_task(idt: str):
    print(f"{idt} starting")
    sleep(10)
    print(f"{idt} stopping")