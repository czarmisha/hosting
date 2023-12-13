import time

from src.worker import celery_app


@celery_app.task
def test_task(a):
    time.sleep(20)
    return a
